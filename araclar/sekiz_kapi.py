#!/usr/bin/env python3
"""Sekiz Kapı — Ders Kutusu'nun yayın öncesi denetim sistemi.

Site, sorular ve kitapçıklar sekiz kapıdan geçer; bir kapıda hata varsa kapı "KAPALI" sayılır ve çıkış kodu 1 olur.

  1. Yayın denetimi     yayin_denetle.py (özet şeması, kök/gösterim, kesir, derleme senkronu) + kok_yayin_denetle.py
  2. Soru bütünlüğü     özet etkinlik ve örnekleri, çalışma kâğıdı ve KPSS soruları, ASDS cevap anahtarları
  3. Tekrar ve çakışma  aynı soru iki kez; haftalar arası kopya; dosya adı/alan uyuşmazlığı; katalog, sitemap, kuyruk tekrarı
  4. Bağlantı ve dosya  HTML iç bağlantı/kaynakları, veri dosyalarının işaret ettiği dosyalar, sitemap, JS söz dizimi
  5. PDF kitapçıklar    her PDF açılıyor mu, sayfa sayısı; sitenin ürettiği kitapçıklarda üst üste binen kelimeler
  6. Yerleşim           gerçek tarayıcıda yatay taşma, üst üste binen metin, betik hatası (tests/sekiz-kapi-yerlesim.cjs)
  7. Veri tutarlılığı   JSON geçerliliği, katalog alanları, ASDS/yazılı/plan/kelime/sosyal kuyruk tutarlılığı
  8. Canlı site         derskutusu.com (yalnız --canli): sayfalar, DNS, sertifika, yayın güncelliği (nobetci.py)

Kullanım:
  python3 araclar/sekiz_kapi.py                 # 1-7 (tarayıcı varsa 6 dahil); canlı site atlanır
  python3 araclar/sekiz_kapi.py --hizli         # yayın denetimi hızlı kip, PDF binme taraması ve tarayıcı örnekleri kısa
  python3 araclar/sekiz_kapi.py --kapi 2,3,5    # yalnız seçilen kapılar
  python3 araclar/sekiz_kapi.py --canli         # 8. kapı: derskutusu.com'a bağlanır
  python3 araclar/sekiz_kapi.py --tarayicisiz   # 6. kapıyı atla (node/Playwright yoksa kendiliğinden atlanır)
  python3 araclar/sekiz_kapi.py --rapor KLASOR  # rapor klasörü (varsayılan sekiz-kapi-sonuc/: rapor.md, rapor.json, yerlesim.json)
  python3 araclar/sekiz_kapi.py --ayrinti 40    # her kapı için yazılacak bulgu sayısı (varsayılan 15; 0 = hepsi)

Yalnız standart kütüphane kullanır. pdfinfo/pdftotext (poppler-utils) ve node + Playwright varsa 5. ve 6. kapılar tam çalışır,
yoksa ilgili bölüm "atlandı" diye raporlanır. GITHUB_STEP_SUMMARY tanımlıysa özet tablo oraya da yazılır.
"""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import datetime as dt
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
PUBLIC = KOK / 'public'
TESTS = KOK / 'tests'
sys.path.insert(0, str(ARACLAR))

SITE = 'https://derskutusu.com/'
KAPI_ADLARI = {1: 'Yayın denetimi', 2: 'Soru bütünlüğü', 3: 'Tekrar ve çakışma', 4: 'Bağlantı ve dosya',
               5: 'PDF kitapçıklar', 6: 'Yerleşim (tarayıcı)', 7: 'Veri tutarlılığı', 8: 'Canlı site'}
# Sitemap'te olmayan ama bilerek dışarıda tutulan sayfalar (araç/yardımcı sayfalar)
SITEMAP_DISI = {'404.html', 'ara.html', 'ders-dagitim-uygulama.html', 'goruntule.html', 'index.html', 'okul-bildir.html',
                'sinif.html', 'tahta.html', 'yazili.html'}
# Sitenin kendi ürettiği kitapçıklar: üst üste binme taraması bunlarda yapılır (public/dosyalar resmî MEB belgeleridir)
PDF_URETIM_KLASORLERI = ('asds', 'yazili', 'calisma', 'kpss', 'kutuphane')
TARIH_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
KELIME_RE = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', re.S)
ALNUM_RE = re.compile(r'[0-9A-Za-zÇĞİÖŞÜçğıöşü]')


class Kapi:
    def __init__(self, no):
        self.no, self.ad = no, KAPI_ADLARI[no]
        self.hatalar, self.uyarilar, self.notlar = [], [], []
        self.atlandi = None
        self.sure = 0.0

    def hata(self, m):
        self.hatalar.append(m)

    def uyari(self, m):
        self.uyarilar.append(m)

    def bilgi(self, m):
        self.notlar.append(m)

    @property
    def durum(self):
        if self.atlandi:
            return 'ATLANDI'
        if self.hatalar:
            return 'KAPALI'
        return 'UYARI' if self.uyarilar else 'AÇIK'


# ----------------------------------------------------------------------------- yardımcılar
def json_oku(p):
    try:
        return json.loads(Path(p).read_text(encoding='utf-8')), None
    except Exception as exc:  # bozuk dosya raporlanır, denetim sürer
        return None, f'{exc.__class__.__name__}: {exc}'


def norm(s):
    """Karşılaştırma için hafif normalleştirme: küçük harf, tek boşluk, sondaki nokta/soru işareti."""
    return re.sub(r'\s+', ' ', str(s).casefold()).strip().rstrip('.?!:').strip()


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(KOK))
    except ValueError:
        return str(p)


def dizeler(o, yol=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from dizeler(v, f'{yol}.{k}' if yol else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from dizeler(v, f'{yol}[{i}]')
    elif isinstance(o, str):
        yield yol, o


def dosya_adi_coz(stem):
    """'5-fen-bilimleri-7' -> (5, 'fen-bilimleri', 7); uymuyorsa None."""
    parca = stem.split('-')
    if len(parca) >= 3 and parca[0].isdigit() and parca[-1].isdigit():
        return int(parca[0]), '-'.join(parca[1:-1]), int(parca[-1])
    return None


def dersler_sozlugu():
    d, _ = json_oku(PUBLIC / 'veri' / 'dersler.json')
    return (d or {}).get('dersler', {}), (d or {})


def ozet_dosyalari():
    return sorted((ARACLAR / 'ozetler').glob('*.json'))


def calisma_dosyalari():
    return sorted((ARACLAR / 'calisma').glob('*.json'))


def kpss_dosyalari():
    return sorted((ARACLAR / 'kpss').glob('*.json'))


def soru_metni(s):
    return str(s.get('soru') or s.get('metin') or '').strip()


# ----------------------------------------------------------------------------- 1. kapı
def kapi_1(k, ayar):
    spec = importlib.util.spec_from_file_location('yayin_denetle_sk', ARACLAR / 'yayin_denetle.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    dosya_sayisi, hatalar = mod.denetle(hizli=ayar.hizli)
    for h in hatalar:
        k.hata(h)
    k.bilgi(f'{dosya_sayisi} kaynak/web dosyası ve {len(ozet_dosyalari())} konu özeti yayın denetiminden geçti'
            + (' (hızlı kip)' if ayar.hizli else ''))
    if not ayar.hizli:
        r = subprocess.run([sys.executable, str(ARACLAR / 'kok_yayin_denetle.py')], cwd=str(KOK), capture_output=True, text=True)
        if r.returncode != 0:
            for satir in (r.stdout + r.stderr).strip().splitlines():
                if satir and not satir.startswith('Traceback') and 'kaynak/web/Word dosyası' not in satir:
                    k.hata(f'kök denetimi: {satir.strip()[:200]}')
        else:
            k.bilgi((r.stdout.strip().splitlines() or ['kök denetimi tamam'])[0])


# ----------------------------------------------------------------------------- 2. kapı
def soru_denetle(s, ad, hata, uyari, secenek_sayisi=None):
    tur = s.get('tur')
    soru = soru_metni(s)
    if tur == 'coktan':
        sec = s.get('secenekler')
        if not isinstance(sec, list) or len(sec) < 2:
            hata(f'{ad}: seçenek listesi eksik'); return
        if not soru:
            hata(f'{ad}: soru metni boş')
        if any(not str(x).strip() for x in sec):
            hata(f'{ad}: boş seçenek var')
        n = secenek_sayisi or (4, 5)
        if len(sec) not in (n if isinstance(n, tuple) else (n,)):
            uyari(f'{ad}: {len(sec)} seçenek (beklenen {n if not isinstance(n, tuple) else " ya da ".join(map(str, n))})')
        tam = [re.sub(r'\s+', ' ', str(x)).strip() for x in sec]
        if len(set(tam)) < len(tam):
            hata(f"{ad}: aynı seçenek iki kez '{next(x for x in tam if tam.count(x) > 1)[:40]}'")
        elif len({x.casefold() for x in tam}) < len(tam):
            # yazım (büyük/küçük harf) sorularında bilerek olur; başka sorularda kopya şık olabilir
            uyari(f"{ad}: yalnız büyük/küçük harfi farklı iki seçenek '{next(x for x in tam if sum(y.casefold() == x.casefold() for y in tam) > 1)[:40]}'")
        d = s.get('dogru')
        if isinstance(d, bool) or not isinstance(d, int) or not 0 <= d < len(sec):
            hata(f'{ad}: dogru={d!r} seçenek aralığının dışında (0-{len(sec) - 1})')
    elif tur == 'dy':
        ifadeler = s.get('ifadeler')
        if not isinstance(ifadeler, list) or len(ifadeler) < 2:
            hata(f'{ad}: doğru/yanlış ifadeleri eksik (en az 2)'); return
        cevaplar = []
        for i, f in enumerate(ifadeler):
            if not isinstance(f, dict) or not str(f.get('metin', '')).strip():
                hata(f'{ad}: ifade {i + 1} metni boş'); continue
            if not isinstance(f.get('dogru'), bool):
                hata(f'{ad}: ifade {i + 1} için dogru true/false değil ({f.get("dogru")!r})')
            cevaplar.append(f.get('dogru'))
        if len(ifadeler) >= 3 and len(set(cevaplar)) == 1:
            uyari(f'{ad}: bütün ifadeler aynı cevaplı ({"hepsi doğru" if cevaplar[0] else "hepsi yanlış"})')
        if len({norm(f.get('metin', '')) for f in ifadeler if isinstance(f, dict)}) < len(ifadeler):
            hata(f'{ad}: aynı ifade iki kez')
    elif tur == 'eslestir':
        c = s.get('ciftler')
        if not isinstance(c, list) or len(c) < 2:
            hata(f'{ad}: eşleştirme çiftleri eksik (en az 2)'); return
        if any(not (isinstance(x, list) and len(x) == 2 and str(x[0]).strip() and str(x[1]).strip()) for x in c):
            hata(f'{ad}: her çift [sol, sağ] iki dolu metinden oluşmalı'); return
        sol, sag = [norm(x[0]) for x in c], [norm(x[1]) for x in c]
        if len(set(sol)) < len(sol):
            hata(f'{ad}: sol sütunda aynı öğe iki kez (eşleştirme belirsiz)')
        if len(set(sag)) < len(sag):
            hata(f'{ad}: sağ sütunda aynı öğe iki kez (eşleştirme belirsiz)')
    elif tur == 'bosluk':
        cumleler = s.get('cumleler')
        if not isinstance(cumleler, list) or not cumleler:
            hata(f'{ad}: boşluk cümleleri eksik'); return
        cevaplar = set()
        for i, c in enumerate(cumleler):
            if not isinstance(c, dict):
                hata(f'{ad}: cümle {i + 1} nesne değil'); continue
            if '___' not in str(c.get('metin', '')) and '…' not in str(c.get('metin', '')) and '...' not in str(c.get('metin', '')):
                hata(f'{ad}: cümle {i + 1} içinde boşluk işareti (___) yok')
            if not str(c.get('cevap', '')).strip():
                hata(f'{ad}: cümle {i + 1} cevabı boş')
            cevaplar.add(norm(c.get('cevap', '')))
        fazla = s.get('fazla') or []
        for f in fazla:
            if norm(f) in cevaplar:
                hata(f"{ad}: çeldirici '{f}' aynı zamanda doğru cevap (fazla listesinden çıkarın)")
        kelimeler = s.get('kelimeler')
        if isinstance(kelimeler, list) and kelimeler:
            havuz = {norm(x) for x in kelimeler}
            eksik = [c.get('cevap') for c in cumleler if isinstance(c, dict) and norm(c.get('cevap', '')) not in havuz]
            if eksik:
                uyari(f'{ad}: kelime havuzunda olmayan cevap {eksik[:3]}')
    elif tur == 'ogretici':
        if not soru:
            hata(f'{ad}: öğretici soru metni boş')
        if not str(s.get('cevap', '')).strip():
            hata(f'{ad}: öğretici sorunun cevabı boş')
        ipuclari = s.get('ipuclari')
        if not ipuclari:
            uyari(f'{ad}: öğretici soruda ipucu yok')
        elif any(len(ALNUM_RE.findall(str(i))) < 3 for i in ipuclari):
            hata(f'{ad}: öğretici ipucu boş ya da anlamsız ({[str(i)[:12] for i in ipuclari][:3]})')
    elif tur in ('kisa', 'acik'):
        if not soru:
            hata(f'{ad}: soru metni boş')
        if not str(s.get('cevap', '')).strip():
            hata(f'{ad}: cevap boş')
        satir = s.get('satir')
        if satir is not None and (isinstance(satir, bool) or not isinstance(satir, int) or satir < 1):
            hata(f'{ad}: satir={satir!r} (1 ya da daha büyük tam sayı olmalı)')
    elif tur == 'tablo':
        b, satirlar = s.get('basliklar'), s.get('satirlar')
        if not isinstance(b, list) or not b or not isinstance(satirlar, list) or not satirlar:
            hata(f'{ad}: tablo başlıkları ya da satırları eksik'); return
        bos_hucre = False
        for i, r in enumerate(satirlar):
            if not isinstance(r, list) or len(r) != len(b):
                hata(f'{ad}: {i + 1}. satırda {len(r) if isinstance(r, list) else "?"} hücre var, başlık sayısı {len(b)}'); continue
            for h in r:
                if isinstance(h, dict) and not str(h.get('b', '')).strip():
                    bos_hucre = True
        if bos_hucre:
            hata(f'{ad}: cevap hücresi ({{"b": ...}}) boş')
        if not any(isinstance(h, dict) for r in satirlar if isinstance(r, list) for h in r):
            uyari(f'{ad}: tabloda doldurulacak hücre yok')
    elif tur == 'siralama':
        o = s.get('ogeler')
        if not isinstance(o, list) or len(o) < 3:
            hata(f'{ad}: sıralama öğeleri eksik (en az 3)'); return
        if len({norm(x) for x in o}) < len(o):
            hata(f'{ad}: aynı öğe iki kez (sıralama belirsiz)')
    elif tur == 'sifre':
        satirlar, sonuc = s.get('satirlar'), str(s.get('sonuc', '')).strip()
        if not isinstance(satirlar, list) or not satirlar or not sonuc:
            hata(f'{ad}: şifre satırları ya da sonuç eksik'); return
        harfler = []
        for i, r in enumerate(satirlar):
            cevap = str(r.get('cevap', '')).strip() if isinstance(r, dict) else ''
            a = r.get('anahtar') if isinstance(r, dict) else None
            if not cevap or not str(r.get('ipucu', '')).strip():
                hata(f'{ad}: {i + 1}. satırın ipucu ya da cevabı boş'); continue
            if isinstance(a, bool) or not isinstance(a, int) or not 0 <= a < len(cevap):
                hata(f'{ad}: {i + 1}. satır anahtar={a!r} cevabın ({cevap}) dışında'); continue
            harfler.append(cevap[a])
        if harfler and len(harfler) == len(satirlar) and norm(''.join(harfler)) != norm(sonuc):
            hata(f"{ad}: anahtar harfler '{''.join(harfler)}' sonuç '{sonuc}' ile uyuşmuyor")
    elif tur == 'kavram':
        if not str(s.get('merkez', '')).strip() or not isinstance(s.get('dallar'), list) or not s.get('dallar'):
            hata(f'{ad}: kavram haritasının merkezi ya da dalları eksik'); return
        if any(isinstance(d, dict) and not str(d.get('b', '')).strip() for d in s['dallar']):
            hata(f'{ad}: boş kutunun cevabı ("b") boş')
    else:
        uyari(f'{ad}: bilinmeyen soru türü {tur!r}')


def kapi_2(k, ayar):
    sayac = 0
    for p in ozet_dosyalari():
        d, err = json_oku(p)
        if err:
            continue  # 1. ve 7. kapı raporlar
        r = rel(p)
        dogrular = []
        for i, e in enumerate(d.get('etkinlikler', [])):
            sayac += 1
            soru_denetle(e, f'{r} etkinlik {i + 1}', k.hata, k.uyari, secenek_sayisi=(4, 5))
            if e.get('tur') == 'coktan' and isinstance(e.get('dogru'), int):
                dogrular.append(e['dogru'])
        if len(dogrular) >= 4 and len(set(dogrular)) == 1:
            k.uyari(f'{r}: bütün çoktan seçmelilerde doğru cevap aynı şıkta ({"ABCDE"[dogrular[0]]})')
        for i, o in enumerate(d.get('ornekler', [])):
            sayac += 1
            if not str(o.get('soru', '')).strip():
                k.hata(f'{r} örnek {i + 1}: soru metni boş')
            if not str(o.get('cevap', '')).strip():
                k.hata(f'{r} örnek {i + 1}: cevap boş')
    for p in calisma_dosyalari():
        d, err = json_oku(p)
        if err:
            continue
        r = rel(p)
        sorular = d.get('sorular')
        if not isinstance(sorular, list) or not sorular:
            k.hata(f'{r}: sorular listesi boş'); continue
        for i, s in enumerate(sorular):
            sayac += 1
            soru_denetle(s, f'{r} soru {i + 1}', k.hata, k.uyari, secenek_sayisi=(4, 5))
            if s.get('duzey') not in (None, 'hatirla', 'uygula', 'ust'):
                k.uyari(f'{r} soru {i + 1}: duzey={s.get("duzey")!r} (hatirla|uygula|ust)')
    for p in kpss_dosyalari():
        d, err = json_oku(p)
        if err:
            continue
        r = rel(p)
        kimlikler = set()
        for i, s in enumerate(d.get('sorular', [])):
            sayac += 1
            soru_denetle(s, f'{r} soru {i + 1}', k.hata, k.uyari, secenek_sayisi=5)
            if s.get('id') in kimlikler:
                k.hata(f'{r} soru {i + 1}: id {s.get("id")!r} tekrar ediyor')
            kimlikler.add(s.get('id'))
        for i, o in enumerate(d.get('ornekler', [])):
            if not str(o.get('soru', '')).strip() or not str(o.get('cevap', '')).strip():
                k.hata(f'{r} örnek {i + 1}: soru ya da cevap boş')
    # ASDS cevap anahtarları
    asds, err = json_oku(PUBLIC / 'veri' / 'asds.json')
    if asds:
        for blok in asds.get('siniflar', []):
            for sv in blok.get('sinavlar', []):
                ad = f"public/veri/asds.json {sv.get('kimlik')}"
                anahtar = sv.get('anahtar_a') or {}
                if not anahtar:
                    k.hata(f'{ad}: anahtar_a boş'); continue
                toplam = 0
                for ders, harfler in anahtar.items():
                    if not re.fullmatch(r'[A-E]+', str(harfler)):
                        k.hata(f"{ad}: {ders} anahtarı yalnız A-E harflerinden oluşmalı ('{str(harfler)[:20]}')")
                    toplam += len(str(harfler))
                beklenen = sv.get('soru_sayisi') or blok.get('soru_sayisi')
                if beklenen and toplam != beklenen:
                    k.hata(f'{ad}: cevap anahtarında {toplam} cevap var, sınav {beklenen} soruluk')
                dagilim = blok.get('ders_dagilimi', [])
                if dagilim and len(anahtar) != len(dagilim):
                    k.uyari(f'{ad}: anahtarda {len(anahtar)} ders, dağılımda {len(dagilim)} ders')
                for dd in dagilim:
                    ilk = norm(dd.get('ders', '')).split(' ')[0].rstrip('.')
                    uygun = [v for kk, v in anahtar.items() if norm(kk).startswith(ilk)]
                    if len(uygun) == 1 and len(uygun[0]) != dd.get('soru'):
                        k.hata(f"{ad}: {dd.get('ders')} için {len(uygun[0])} cevap var, {dd.get('soru')} soru olmalı")
    k.bilgi(f'{sayac} soru/etkinlik/örnek denetlendi')


# ----------------------------------------------------------------------------- 3. kapı
def kapi_3(k, ayar):
    dersler, _ = dersler_sozlugu()
    havuz = {}        # (sinif, ders, norm soru) -> [dosya adları]
    ozet_sorulari = {}  # (sinif, ders, hafta) -> {norm soru}
    for p in ozet_dosyalari():
        d, err = json_oku(p)
        if err:
            continue
        r = rel(p)
        ad = dosya_adi_coz(p.stem)
        if not ad:
            k.hata(f'{r}: dosya adı <sınıf>-<ders>-<hafta>.json biçiminde değil'); continue
        sinif, ders, hafta = ad
        if (d.get('sinif'), str(d.get('ders')), d.get('hafta')) != (sinif, ders, hafta):
            k.hata(f'{r}: dosya adı ile içerik uyuşmuyor (sinif={d.get("sinif")}, ders={d.get("ders")}, hafta={d.get("hafta")})')
        gorulen, metinler = {}, set()
        for i, e in enumerate(d.get('etkinlikler', [])):
            if e.get('tur') == 'coktan':
                metinler.add(('etkinlik', i + 1, soru_metni(e)))
            for f in e.get('ifadeler', []) if e.get('tur') == 'dy' else []:
                metinler.add(('ifade', i + 1, str(f.get('metin', ''))))
        for i, o in enumerate(d.get('ornekler', [])):
            metinler.add(('örnek', i + 1, str(o.get('soru', ''))))
        soru_kumesi = set()
        for tur, i, m in sorted(metinler):
            a = norm(m)
            if len(a) < 12:
                continue
            if a in gorulen:
                k.hata(f"{r}: {tur} {i} ile {gorulen[a][0]} {gorulen[a][1]} aynı soru ('{m[:50]}')")
            gorulen[a] = (tur, i)
            if tur != 'ifade':
                soru_kumesi.add(a)
                havuz.setdefault((sinif, ders, a), []).append(p.stem)
        ozet_sorulari[(sinif, ders, hafta)] = soru_kumesi
    # Haftalar arası kopya: iki dosyanın ortak soruları
    ciftler = {}
    for (sinif, ders, a), dosyalar in havuz.items():
        dosyalar = sorted(set(dosyalar))
        for i in range(len(dosyalar)):
            for j in range(i + 1, len(dosyalar)):
                ciftler.setdefault((dosyalar[i], dosyalar[j]), []).append(a)
    for (d1, d2), ortak in sorted(ciftler.items()):
        if len(ortak) >= 3:
            k.hata(f'araclar/ozetler/{d1}.json ile {d2}.json üst üste biniyor: {len(ortak)} aynı soru (haftalardan biri kopya)')
        else:
            k.uyari(f"araclar/ozetler/{d1}.json ile {d2}.json ortak soru: '{ortak[0][:60]}'")
    # Çalışma kâğıtları
    for p in calisma_dosyalari():
        d, err = json_oku(p)
        if err:
            continue
        r = rel(p)
        ad = dosya_adi_coz(p.stem)
        if not ad:
            k.hata(f'{r}: dosya adı <sınıf>-<ders>-<hafta>.json biçiminde değil'); continue
        sinif, ders, hafta = ad
        if (d.get('sinif'), str(d.get('ders')), d.get('hafta')) != (sinif, ders, hafta):
            k.hata(f'{r}: dosya adı ile içerik uyuşmuyor (sinif={d.get("sinif")}, ders={d.get("ders")}, hafta={d.get("hafta")})')
        gorulen = set()
        for i, s in enumerate(d.get('sorular', [])):
            a = norm(soru_metni(s))
            if len(a) < 12:
                continue
            if a in gorulen:
                k.hata(f'{r}: soru {i + 1} daha önceki bir soruyla aynı')
            gorulen.add(a)
            if s.get('tur') == 'coktan' and a in ozet_sorulari.get((sinif, ders, hafta), ()):
                k.uyari(f"{r}: soru {i + 1} aynı haftanın konu özetindeki etkinlikle aynı ('{soru_metni(s)[:50]}')")
    # Katalog, sitemap, sosyal kuyruk, ASDS
    ic, err = json_oku(PUBLIC / 'veri' / 'icerikler.json')
    if ic:
        hedefler, basliklar = {}, {}
        for i, x in enumerate(ic.get('icerikler', [])):
            anahtar = (x.get('sinif'), x.get('ders'), x.get('tur'), x.get('goruntule') or x.get('dosya'))
            if anahtar in hedefler:
                k.hata(f'public/veri/icerikler.json [{i}] ile [{hedefler[anahtar]}] aynı kayıt: {anahtar[3]}')
            hedefler[anahtar] = i
            b = (x.get('sinif'), x.get('ders'), norm(x.get('baslik', '')))
            if b in basliklar:
                k.uyari(f"public/veri/icerikler.json [{i}] başlığı [{basliklar[b]}] ile aynı: '{x.get('baslik', '')[:60]}'")
            basliklar[b] = i
    sm = PUBLIC / 'sitemap.xml'
    if sm.exists():
        adresler = re.findall(r'<loc>([^<]+)</loc>', sm.read_text(encoding='utf-8'))
        tekrar = sorted({a for a in adresler if adresler.count(a) > 1})
        for a in tekrar[:20]:
            k.hata(f'public/sitemap.xml: adres iki kez {a}')
    ky, err = json_oku(KOK / 'sosyal' / 'kuyruk.json')
    if ky:
        gorulen = {}
        for i, g in enumerate(ky.get('gonderiler', [])):
            kim = g.get('kimlik')
            if kim in gorulen:
                k.hata(f'sosyal/kuyruk.json: gönderi {i} kimliği {kim!r} gönderi {gorulen[kim]} ile aynı')
            gorulen[kim] = i
    asds, err = json_oku(PUBLIC / 'veri' / 'asds.json')
    if asds:
        for blok in asds.get('siniflar', []):
            gorulen = {}
            for sv in blok.get('sinavlar', []):
                imza = json.dumps(sv.get('anahtar_a'), sort_keys=True, ensure_ascii=False)
                if imza in gorulen:
                    k.hata(f"public/veri/asds.json: {sv.get('kimlik')} ile {gorulen[imza]} cevap anahtarı birebir aynı (kopya sınav?)")
                gorulen[imza] = sv.get('kimlik')
    k.bilgi(f'{len(havuz)} benzersiz soru, {len(ciftler)} dosya çifti karşılaştırıldı')


# ----------------------------------------------------------------------------- 4. kapı
TEKIL = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Toplayici(HTMLParser):
    def __init__(self):
        super().__init__()
        self.baglantilar, self.idler = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.idler.add(a['id'])
        for alan in ('href', 'src', 'data-src', 'action', 'poster'):
            v = a.get(alan)
            if v and v.strip():
                self.baglantilar.append((tag, alan, v.strip(), self.getpos()[0]))


def hedef_coz(sayfa, deger):
    """Göreli/mutlak iç bağlantıyı diskteki dosyaya çevirir; dış ya da denetlenmeyen bağlantıda None."""
    if deger.startswith(('http://', 'https://', '//', 'mailto:', 'tel:', 'javascript:', 'data:', 'blob:')):
        return None
    yol = unquote(urlparse(deger).path)
    if not yol:
        return None
    hedef = PUBLIC / yol.lstrip('/') if yol.startswith('/') else (sayfa.parent / yol)
    try:
        hedef = hedef.resolve()
    except OSError:
        return None
    if hedef.is_dir():
        hedef = hedef / 'index.html'
    if not hedef.exists() and hedef.suffix == '' and hedef.with_suffix('.html').exists():
        hedef = hedef.with_suffix('.html')
    return hedef


def kapi_4(k, ayar):
    sayfalar = sorted(PUBLIC.rglob('*.html'))
    kirik = {}
    capa = 0
    for p in sayfalar:
        t = Toplayici()
        try:
            t.feed(p.read_text(encoding='utf-8'))
        except Exception as exc:
            k.hata(f'{rel(p)}: HTML ayrıştırılamadı ({exc})'); continue
        for tag, alan, deger, satir in t.baglantilar:
            if deger.startswith('#'):
                if deger[1:] and deger[1:] not in t.idler and len(sayfalar) < 200:
                    capa += 1
                continue
            hedef = hedef_coz(p, deger)
            if hedef is None:
                continue
            if not hedef.exists():
                kirik.setdefault(rel(hedef) if KOK in hedef.parents else str(hedef), []).append(f'{rel(p)}:{satir} <{tag} {alan}>')
    for hedef, kaynaklar in sorted(kirik.items()):
        k.hata(f'eksik dosya {hedef} ← {len(kaynaklar)} bağlantı (ilk: {kaynaklar[0]})')
    k.bilgi(f'{len(sayfalar)} HTML sayfasının iç bağlantıları tarandı')

    def var(yol, kaynak):
        y = str(yol).split('#')[0].split('?')[0].lstrip('/')
        if not y or (PUBLIC / y).exists():
            return True
        k.hata(f'{kaynak}: {yol} diskte yok'); return False

    ic, _ = json_oku(PUBLIC / 'veri' / 'icerikler.json')
    for i, x in enumerate((ic or {}).get('icerikler', [])):
        for alan in ('dosya', 'goruntule'):
            if x.get(alan) and not x[alan].startswith('http'):
                var(x[alan], f'icerikler.json [{i}] {alan}')
    b, _ = json_oku(PUBLIC / 'veri' / 'belgeler.json')
    for g in (b or {}).get('gruplar', []):
        for x in g.get('belgeler', []):
            if x.get('dosya'):
                var(x['dosya'], f"belgeler.json '{x.get('kimlik') or x.get('baslik', '')[:40]}'")
    yk, _ = json_oku(PUBLIC / 'veri' / 'yazili-kagitlari.json')
    for tablo, yazililar in (yk or {}).get('tablolar', {}).items():
        for yno, senaryolar in yazililar.items():
            for s in senaryolar:
                for ek in ('', '-cevapli'):
                    var(f'yazili/pdf/{tablo}-{yno}-yazili-senaryo-{s}{ek}.pdf', 'yazili-kagitlari.json')
    yc, _ = json_oku(PUBLIC / 'veri' / 'yazili-cikti.json')
    for tablo, liste in (yc or {}).get('tablolar', {}).items():
        for x in liste:
            for ek in ('', '-cevapli'):
                var(f"yazili/cikti/{x.get('dosya')}{ek}.pdf", f'yazili-cikti.json {tablo}')
    asds, _ = json_oku(PUBLIC / 'veri' / 'asds.json')
    for blok in (asds or {}).get('siniflar', []):
        for sv in blok.get('sinavlar', []):
            for ad, yol in (sv.get('dosyalar') or {}).items():
                var(yol, f"asds.json {sv.get('kimlik')} {ad}")
    kp, _ = json_oku(PUBLIC / 'veri' / 'kpss.json')
    for m in (kp or {}).get('moduller', []):
        var(f"kpss/{m.get('id')}.html", 'kpss.json')
    gp, _ = json_oku(PUBLIC / 'veri' / 'gunluk-planlar.json')
    for pl in (gp or {}).get('planlar', []):
        var(f"veri/gunluk-plan/{pl.get('ad')}.json", 'gunluk-planlar.json')
        var(f"dosyalar/gunluk-plan/{pl.get('ad')}.docx", 'gunluk-planlar.json')
    ky, _ = json_oku(KOK / 'sosyal' / 'kuyruk.json')
    for i, g in enumerate((ky or {}).get('gonderiler', [])):
        gorsel = str(g.get('gorsel', ''))
        if gorsel.startswith(SITE) and not g.get('durum'):   # paylaşılmış gönderinin dosyası artık gerekmez
            var(gorsel[len(SITE):], f"sosyal/kuyruk.json bekleyen gönderi {g.get('kimlik')}")
    sm = PUBLIC / 'sitemap.xml'
    if sm.exists():
        adresler = re.findall(r'<loc>([^<]+)</loc>', sm.read_text(encoding='utf-8'))
        for a in adresler:
            if not a.startswith(SITE):
                k.hata(f'sitemap.xml: site dışı adres {a}'); continue
            y = a[len(SITE):]
            if y and not (PUBLIC / y).exists():
                k.hata(f'sitemap.xml: {y} diskte yok')
        kayitli = {a[len(SITE):] for a in adresler if a.startswith(SITE)}
        for p in sayfalar:
            r = str(p.relative_to(PUBLIC))
            if r not in kayitli and r not in SITEMAP_DISI:
                k.uyari(f'public/{r} sitemap.xml içinde değil')
    else:
        k.hata('public/sitemap.xml yok')
    node = shutil.which('node')
    if node:
        bozuk = 0
        for js in sorted(PUBLIC.glob('*.js')):
            r = subprocess.run([node, '--check', str(js)], capture_output=True, text=True)
            if r.returncode != 0:
                bozuk += 1
                k.hata(f'{rel(js)}: JavaScript söz dizimi hatası: {(r.stderr.strip().splitlines() or ["?"])[-1][:160]}')
        k.bilgi(f'{len(list(PUBLIC.glob("*.js")))} betik dosyası node --check ile sınandı')
    else:
        k.bilgi('node yok: JavaScript söz dizimi denetimi atlandı')


# ----------------------------------------------------------------------------- 5. kapı
def pdf_yapisal(p):
    try:
        with p.open('rb') as f:
            bas = f.read(8)
            f.seek(max(0, p.stat().st_size - 2048))
            son = f.read()
    except OSError as exc:
        return f'okunamadı ({exc})'
    if not bas.startswith(b'%PDF-'):
        return 'PDF başlığı yok (bozuk ya da HTML hata sayfası)'
    if b'%%EOF' not in son:
        return 'dosya sonu işareti (%%EOF) yok; eksik indirilmiş olabilir'
    return None


def pdf_sayfa_sayisi(p):
    if shutil.which('pdfinfo'):
        r = subprocess.run(['pdfinfo', str(p)], capture_output=True, text=True, timeout=60)
        m = re.search(r'^Pages:\s+(\d+)', r.stdout, re.M)
        if r.returncode != 0 or not m:
            return None, (r.stderr.strip().splitlines() or ['pdfinfo okuyamadı'])[-1][:120]
        return int(m.group(1)), None
    try:
        import pypdf  # isteğe bağlı
        return len(pypdf.PdfReader(str(p)).pages), None
    except ImportError:
        return None, 'atla'
    except Exception as exc:
        return None, f'pypdf okuyamadı ({exc})'[:160]


def pdf_binme(p, esik=0.6):
    """pdftotext -bbox kelime kutularıyla birbirine giren kelimeler: (sayfa, kelime1, kelime2, oran)."""
    r = subprocess.run(['pdftotext', '-bbox', str(p), '-'], capture_output=True, text=True, timeout=180)
    bulgular = []
    for pno, sayfa in enumerate(r.stdout.split('<page ')[1:], 1):
        kelimeler = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in KELIME_RE.findall(sayfa)]
        kelimeler = [w for w in kelimeler if w[2] - w[0] > 0.5 and w[3] - w[1] > 0.5 and len(ALNUM_RE.findall(w[4])) >= 2]
        kelimeler.sort(key=lambda w: (w[1], w[0]))
        for i, (x0, y0, x1, y1, t) in enumerate(kelimeler):
            for X0, Y0, X1, Y1, T in kelimeler[i + 1:]:
                if Y0 >= y1:
                    break
                ix, iy = min(x1, X1) - max(x0, X0), min(y1, Y1) - max(y0, Y0)
                if ix <= 0 or iy <= 0:
                    continue
                oran = ix * iy / min((x1 - x0) * (y1 - y0), (X1 - X0) * (Y1 - Y0))
                if oran >= esik:
                    bulgular.append((pno, t, T, round(oran * 100)))
                    if len(bulgular) >= 5:
                        return bulgular
    return bulgular


def kapi_5(k, ayar):
    pdfler = sorted(PUBLIC.rglob('*.pdf'))
    if not pdfler:
        k.hata('public/ altında hiç PDF yok'); return
    for p in pdfler:
        if p.stat().st_size < 1024:
            k.hata(f'{rel(p)}: {p.stat().st_size} bayt (boş ya da bozuk)'); continue
        sorun = pdf_yapisal(p)
        if sorun:
            k.hata(f'{rel(p)}: {sorun}')
    asds, _ = json_oku(PUBLIC / 'veri' / 'asds.json')
    beklenen = {}
    for blok in (asds or {}).get('siniflar', []):
        for sv in blok.get('sinavlar', []):
            n = sv.get('sayfa_sayisi') or blok.get('sayfa_sayisi')
            d = sv.get('dosyalar') or {}
            if n:
                for ad in ('a_cevapsiz', 'b_cevapsiz'):
                    if d.get(ad):
                        beklenen[d[ad].lstrip('/')] = n
                for ad in ('a_cevapli', 'b_cevapli'):
                    if d.get(ad):
                        beklenen[d[ad].lstrip('/')] = n + 1   # + cevap anahtarı sayfası
    with ThreadPoolExecutor(4) as h:
        sayfalar = list(h.map(pdf_sayfa_sayisi, pdfler))
    okunan = 0
    for p, (n, err) in zip(pdfler, sayfalar):
        if err == 'atla':
            continue
        if err:
            k.hata(f'{rel(p)}: {err}'); continue
        okunan += 1
        if n < 1:
            k.hata(f'{rel(p)}: sayfa yok')
        r = str(p.relative_to(PUBLIC))
        if r in beklenen and n != beklenen[r]:
            k.hata(f'{rel(p)}: {n} sayfa, kitapçık {beklenen[r]} sayfa olmalı')
    cevapsiz = [p for p in pdfler if not p.stem.endswith('-cevapli') and p.parent.name in ('pdf', 'cikti') and p.parts[-3] in ('yazili', 'calisma')]
    for p in cevapsiz:
        if not p.with_name(p.stem + '-cevapli.pdf').exists():
            k.hata(f'{rel(p)}: cevaplı sürümü ({p.stem}-cevapli.pdf) yok')
    if okunan:
        k.bilgi(f'{len(pdfler)} PDF yapısal olarak, {okunan} tanesi sayfa sayısıyla denetlendi')
    else:
        k.bilgi(f'{len(pdfler)} PDF yalnız yapısal olarak denetlendi (pdfinfo/pypdf yok)')
    if ayar.hizli:
        k.bilgi('üst üste binme taraması hızlı kipte atlandı'); return
    if not shutil.which('pdftotext'):
        k.uyari('pdftotext (poppler-utils) yok: PDF üst üste binme taraması yapılamadı'); return
    uretim = [p for p in pdfler if p.relative_to(PUBLIC).parts[0] in PDF_URETIM_KLASORLERI]

    def tara(p):
        try:
            return p, pdf_binme(p), None
        except Exception as exc:
            return p, [], str(exc)[:120]

    with ThreadPoolExecutor(4) as h:
        for p, bulgular, err in h.map(tara, uretim):
            if err:
                k.uyari(f'{rel(p)}: binme taraması yapılamadı ({err})'); continue
            for pno, t, T, oran in bulgular:
                k.hata(f"{rel(p)}: s.{pno} '{t}' ile '{T}' üst üste (%{oran})")
    k.bilgi(f'{len(uretim)} site üretimi PDF kelime kutularıyla binme için tarandı')


# ----------------------------------------------------------------------------- 6. kapı
def kapi_6(k, ayar, rapor_klasoru):
    if ayar.tarayicisiz:
        k.atlandi = '--tarayicisiz'; return
    node = shutil.which('node')
    if not node:
        k.atlandi = 'node yok (CI iş akışı kurar; yerelde Node 22 + Playwright gerekir)'; return
    sinama = subprocess.run([node, '-e', "try{require('playwright')}catch{require('@playwright/test')}"], capture_output=True, text=True)
    if sinama.returncode != 0:
        k.atlandi = 'Playwright yok: npm install @playwright/test && npx playwright install chromium'; return
    cikti = rapor_klasoru / 'yerlesim.json'
    komut = [node, str(TESTS / 'sekiz-kapi-yerlesim.cjs'), '--cikti', str(cikti), '--ekran-goruntusu']
    if ayar.hizli:
        komut += ['--genislikler', '1366,360', '--ornek', '1']
    r = subprocess.run(komut, cwd=str(KOK), capture_output=True, text=True, timeout=1800)
    if r.returncode == 3 or not cikti.exists():
        k.atlandi = (r.stderr.strip().splitlines() or r.stdout.strip().splitlines() or ['tarayıcı denetimi çalışmadı'])[-1][:200]; return
    y, err = json_oku(cikti)
    if err:
        k.hata(f'yerleşim raporu okunamadı: {err}'); return
    for s in y.get('sayfalar', []):
        ad = f"{s['rota']} @{s['genislik']}px"
        if s.get('tasma'):
            ogeler = '; '.join(f"{t['oge'].split('>')[-1]} ({t['genislik']}px) '{t['metin'][:30]}'" for t in s['tasma'][:3])
            k.hata(f"{ad}: yatay taşma, sayfa {s.get('sayfaGenisligi')}px > pencere {s.get('pencere')}px — {ogeler}")
        for b in s.get('binme', []):
            k.hata(f"{ad}: üst üste binen metin '{b['aMetin']}' ⟷ '{b['bMetin']}' ({b['a']} / {b['b']}, %{int(b['oran'] * 100)})")
        for h in s.get('betikHatalari', []):
            k.hata(f'{ad}: sayfa betiği hatası: {h}')
        for yk in s.get('yuklenemeyen', []):
            k.uyari(f'{ad}: yüklenemeyen kaynak {yk}')
    t = y.get('toplam', {})
    k.bilgi(f"{t.get('sayfa', 0)} sayfa görünümü Chromium'da ölçüldü (genişlikler: {', '.join(map(str, y.get('genislikler', [])))})")


# ----------------------------------------------------------------------------- 7. kapı
def kapi_7(k, ayar):
    jsonlar = sorted(list((PUBLIC / 'veri').rglob('*.json')) + [KOK / 'sosyal' / 'kuyruk.json']
                     + [p for kl in ('ozetler', 'calisma', 'kpss', 'sosyal', 'veri') for p in (ARACLAR / kl).glob('*.json')])
    for p in jsonlar:
        _, err = json_oku(p)
        if err:
            k.hata(f'{rel(p)}: geçersiz JSON ({err})')
    dersler, dv = dersler_sozlugu()
    if not dersler:
        k.hata('public/veri/dersler.json: ders listesi boş'); return
    turler = {t.get('ad') for t in dv.get('turler', [])}
    siniflar = {s for kd in dv.get('kademeler', []) for s in kd.get('siniflar', [])} or set(range(5, 13))
    ic, _ = json_oku(PUBLIC / 'veri' / 'icerikler.json')
    liste = (ic or {}).get('icerikler', [])
    konu = 0
    for i, x in enumerate(liste):
        ad = f"icerikler.json [{i}] '{str(x.get('baslik', ''))[:40]}'"
        if x.get('sinif') not in siniflar:
            k.hata(f'{ad}: sinif={x.get("sinif")!r} tanımlı değil')
        if x.get('ders') not in dersler:
            k.hata(f'{ad}: ders={x.get("ders")!r} dersler.json içinde yok')
        if turler and x.get('tur') not in turler:
            k.hata(f'{ad}: tur={x.get("tur")!r} dersler.json türlerinde yok')
        if x.get('kitle') not in ('ogrenci', 'ogretmen', None, ''):
            k.uyari(f'{ad}: kitle={x.get("kitle")!r} (ogrenci|ogretmen)')
        if not str(x.get('baslik', '')).strip():
            k.hata(f'icerikler.json [{i}]: başlık boş')
        if not (x.get('goruntule') or x.get('dosya')):
            k.hata(f'{ad}: ne goruntule ne dosya var')
        if x.get('tarih') and not TARIH_RE.match(str(x['tarih'])):
            k.hata(f'{ad}: tarih={x.get("tarih")!r} (YYYY-AA-GG)')
        if x.get('tur') == 'Konu anlatımı':
            konu += 1
    ozet_sayisi = len(ozet_dosyalari())
    if konu != ozet_sayisi:
        k.hata(f'icerikler.json içinde {konu} konu anlatımı kaydı var, araclar/ozetler içinde {ozet_sayisi} özet')
    for p in ozet_dosyalari():
        d, err = json_oku(p)
        if d and d.get('yayin_tarihi') and not TARIH_RE.match(str(d['yayin_tarihi'])):
            k.hata(f'{rel(p)}: yayin_tarihi={d.get("yayin_tarihi")!r}')
    asds, _ = json_oku(PUBLIC / 'veri' / 'asds.json')
    if asds:
        toplam = sum(len(b.get('sinavlar', [])) for b in asds.get('siniflar', []))
        if asds.get('toplam_sinav') != toplam:
            k.hata(f"asds.json: toplam_sinav={asds.get('toplam_sinav')} ama {toplam} sınav listelenmiş")
        pdf = sum(len(sv.get('dosyalar') or {}) for b in asds.get('siniflar', []) for sv in b.get('sinavlar', []))
        if asds.get('toplam_pdf') != pdf:
            k.hata(f"asds.json: toplam_pdf={asds.get('toplam_pdf')} ama {pdf} dosya bağlanmış")
        for b in asds.get('siniflar', []):
            dagilim = sum(d.get('soru', 0) for d in b.get('ders_dagilimi', []))
            if dagilim != b.get('soru_sayisi'):
                k.hata(f"asds.json {b.get('sinif')}. sınıf: ders dağılımı {dagilim} soru, soru_sayisi {b.get('soru_sayisi')}")
            kimlikler = [sv.get('kimlik') for sv in b.get('sinavlar', [])]
            for sv in b.get('sinavlar', []):
                if sv.get('sinif') != b.get('sinif'):
                    k.hata(f"asds.json {sv.get('kimlik')}: sinif={sv.get('sinif')} blok {b.get('sinif')}")
                if sv.get('yayin_tarihi') and not TARIH_RE.match(str(sv['yayin_tarihi'])):
                    k.hata(f"asds.json {sv.get('kimlik')}: yayin_tarihi={sv.get('yayin_tarihi')!r}")
            if len(set(kimlikler)) != len(kimlikler):
                k.hata(f"asds.json {b.get('sinif')}. sınıf: sınav kimliği tekrar ediyor")
    yk, _ = json_oku(PUBLIC / 'veri' / 'yazili-kagitlari.json')
    sen, _ = json_oku(PUBLIC / 'veri' / 'senaryolar.json')
    if yk:
        for tablo in (yk.get('ulke') or {}):
            if tablo not in (yk.get('tablolar') or {}):
                k.hata(f'yazili-kagitlari.json: ulke {tablo} için tablo yok')
        if sen:
            for tablo in (yk.get('tablolar') or {}):
                if tablo not in sen.get('tablolar', {}):
                    k.uyari(f'yazili-kagitlari.json: {tablo} için senaryolar.json tablosu yok')
    kel, _ = json_oku(PUBLIC / 'veri' / 'kelimeler.json')
    for s in (kel or {}).get('siniflar', []):
        for t in s.get('temalar', []):
            gorulen = set()
            for w in t.get('kelimeler', []):
                if not str(w.get('en', '')).strip() or not str(w.get('tr', '')).strip():
                    k.hata(f"kelimeler.json {s.get('sinif')}. sınıf tema {t.get('no')}: boş kelime {w}")
                a = norm(w.get('en', ''))
                if a in gorulen:
                    k.uyari(f"kelimeler.json {s.get('sinif')}. sınıf tema {t.get('no')}: '{w.get('en')}' iki kez")
                gorulen.add(a)
    ay, _ = json_oku(PUBLIC / 'veri' / 'ayarlar.json')
    for alan in ('site_adi', 'slogan', 'aciklama', 'eposta'):
        if not str((ay or {}).get(alan, '')).strip():
            k.hata(f'ayarlar.json: {alan} boş')
    for ad, alan in (('ziyaret.json', 'toplam'), ('indirmeler.json', 'toplam')):
        d, _ = json_oku(PUBLIC / 'veri' / ad)
        if d is not None and (isinstance(d.get(alan), bool) or not isinstance(d.get(alan), int) or d.get(alan) < 0):
            k.hata(f'{ad}: {alan}={d.get(alan)!r}')
    ky, _ = json_oku(KOK / 'sosyal' / 'kuyruk.json')
    for i, g in enumerate((ky or {}).get('gonderiler', [])):
        if not g.get('kimlik') or not str(g.get('metin', '')).strip():
            k.hata(f'sosyal/kuyruk.json gönderi {i}: kimlik ya da metin boş')
        try:
            dt.datetime.fromisoformat(str(g.get('zaman', '')))
        except ValueError:
            k.hata(f"sosyal/kuyruk.json gönderi {g.get('kimlik')}: zaman={g.get('zaman')!r} ISO değil")
    kart_sayisi = 0
    for p in sorted((ARACLAR / 'sosyal').glob('*.json')):
        d, err = json_oku(p)
        if err:
            continue
        kart_sayisi += 1
        for alan in ('ozet', 'baslik', 'paragraflar', 'bilgi'):
            if not d.get(alan):
                k.uyari(f'{rel(p)}: {alan} boş')
        if not (PUBLIC / 'sosyal' / f'{p.stem}.png').exists():
            k.uyari(f'{rel(p)}: görseli (public/sosyal/{p.stem}.png) üretilmemiş')
    k.bilgi(f'{len(jsonlar)} JSON dosyası, {len(liste)} katalog kaydı, {kart_sayisi} sosyal kart denetlendi')


# ----------------------------------------------------------------------------- 8. kapı
def kapi_8(k, ayar):
    if not ayar.canli:
        k.atlandi = 'çevrim dışı (canlı site için --canli)'; return
    spec = importlib.util.spec_from_file_location('nobetci_sk', ARACLAR / 'nobetci.py')
    nob = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nob)
    sorun, ana_var = nob.sayfalar()
    z_sorun, _ = nob.ziyaret_ve_yayin()
    for s in sorun + z_sorun + nob.dns() + nob.sertifika() + nob.alan_adi():
        k.hata(s)
    if ayar.derin:
        for s in nob.site_haritasi():
            k.hata(s)
        kirik, toplam = nob.dis_baglantilar()
        for s in kirik:
            k.uyari(s)
        k.bilgi(f'{toplam} dış bağlantı denendi')
    k.bilgi(f"{len(nob.ONEMLI)} canlı sayfa, DNS, sertifika ve alan adı denetlendi; ana sayfa {'açık' if ana_var else 'KAPALI'}")


# ----------------------------------------------------------------------------- rapor
SIMGE = {'AÇIK': '✅', 'UYARI': '⚠️', 'KAPALI': '❌', 'ATLANDI': '⏭️'}


def rapor_yaz(kapilar, ayar, klasor, baslangic):
    zaman = dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=3)
    kapali = [k for k in kapilar if k.durum == 'KAPALI']
    satirlar = [f"# Sekiz Kapı denetimi · {zaman:%d.%m.%Y %H:%M} (TSİ)", '',
                f"**Sonuç:** {'bütün kapılar açık' if not kapali else str(len(kapali)) + ' kapı KAPALI'}"
                + (' · hızlı kip' if ayar.hizli else '') + f" · {time.time() - baslangic:.0f} sn", '',
                '| Kapı | Denetim | Durum | Hata | Uyarı | Süre |', '|---|---|---|---|---|---|']
    for k in kapilar:
        satirlar.append(f"| {k.no} | {k.ad} | {SIMGE[k.durum]} {k.durum} | {len(k.hatalar)} | {len(k.uyarilar)} | {k.sure:.0f} sn |")
    n = ayar.ayrinti
    for k in kapilar:
        satirlar += ['', f"## {k.no}. kapı · {k.ad} — {SIMGE[k.durum]} {k.durum}"]
        if k.atlandi:
            satirlar.append(f'- atlandı: {k.atlandi}')
        for b in k.notlar:
            satirlar.append(f'- {b}')
        for h in (k.hatalar if not n else k.hatalar[:n]):
            satirlar.append(f'- ❌ {h}')
        if n and len(k.hatalar) > n:
            satirlar.append(f'- … ve {len(k.hatalar) - n} hata daha (rapor.json)')
        for u in (k.uyarilar if not n else k.uyarilar[:n]):
            satirlar.append(f'- ⚠️ {u}')
        if n and len(k.uyarilar) > n:
            satirlar.append(f'- … ve {len(k.uyarilar) - n} uyarı daha (rapor.json)')
    md = '\n'.join(satirlar) + '\n'
    klasor.mkdir(parents=True, exist_ok=True)
    (klasor / 'rapor.md').write_text(md, encoding='utf-8')
    (klasor / 'rapor.json').write_text(json.dumps({
        'zaman': zaman.isoformat(timespec='minutes'), 'hizli': ayar.hizli, 'canli': ayar.canli,
        'kapilar': [{'no': k.no, 'ad': k.ad, 'durum': k.durum, 'atlandi': k.atlandi, 'sure': round(k.sure, 1),
                     'bilgi': k.notlar, 'hatalar': k.hatalar, 'uyarilar': k.uyarilar} for k in kapilar]},
        ensure_ascii=False, indent=1), encoding='utf-8')
    ozet = os.environ.get('GITHUB_STEP_SUMMARY')
    if ozet:
        with open(ozet, 'a', encoding='utf-8') as f:
            f.write(md)
    cikti = os.environ.get('GITHUB_OUTPUT')
    if cikti:
        with open(cikti, 'a', encoding='utf-8') as f:
            f.write(f"durum={'kapali' if kapali else 'acik'}\nkapali={','.join(str(k.no) for k in kapali)}\n")
    return md


def main():
    ap = argparse.ArgumentParser(description='Sekiz Kapı: Ders Kutusu yayın denetimi', formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--kapi', help='yalnız bu kapılar, virgülle (ör. 2,3,5)')
    ap.add_argument('--hizli', action='store_true', help='hızlı kip (yayın denetimi hızlı, PDF binme taraması yok, tarayıcıda az sayfa)')
    ap.add_argument('--canli', action='store_true', help='8. kapı: derskutusu.com canlı denetimi')
    ap.add_argument('--derin', action='store_true', help='canlı denetimde site haritası ve dış bağlantılar da')
    ap.add_argument('--tarayicisiz', action='store_true', help='6. kapıyı (tarayıcı) atla')
    ap.add_argument('--rapor', default='sekiz-kapi-sonuc', help='rapor klasörü')
    ap.add_argument('--ayrinti', type=int, default=15, help='kapı başına yazılacak bulgu sayısı (0 = hepsi)')
    ayar = ap.parse_args()
    secili = {int(x) for x in ayar.kapi.split(',')} if ayar.kapi else set(KAPI_ADLARI)
    for x in secili:
        if x not in KAPI_ADLARI:
            ap.error(f'kapı {x} yok (1-8)')
    klasor = Path(ayar.rapor).resolve()
    klasor.mkdir(parents=True, exist_ok=True)
    baslangic = time.time()
    kapilar = []
    for no in sorted(secili):
        k = Kapi(no)
        t = time.time()
        print(f'[{no}/8] {k.ad} …', flush=True)
        try:
            if no == 6:
                kapi_6(k, ayar, klasor)
            else:
                globals()[f'kapi_{no}'](k, ayar)
        except Exception as exc:  # kapı çökerse diğerleri sürsün; çöken kapı kapalı sayılır
            k.hata(f'denetim çöktü: {exc.__class__.__name__}: {str(exc)[:300]}')
        k.sure = time.time() - t
        kapilar.append(k)
        print(f'      {SIMGE[k.durum]} {k.durum}: {len(k.hatalar)} hata, {len(k.uyarilar)} uyarı ({k.sure:.0f} sn)'
              + (f' — {k.atlandi}' if k.atlandi else ''), flush=True)
    md = rapor_yaz(kapilar, ayar, klasor, baslangic)
    print()
    print(md)
    print(f'Rapor: {klasor / "rapor.md"}')
    sys.exit(1 if any(k.durum == 'KAPALI' for k in kapilar) else 0)


if __name__ == '__main__':
    main()
