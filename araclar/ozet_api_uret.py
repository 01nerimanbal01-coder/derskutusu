#!/usr/bin/env python3
"""Haftalık konu özetlerini Claude API ile üretir (Max planının aylık API kredisiyle çalışır).

Her sınıf-ders için bir istek atar; model araclar/ozetler/<sinif>-<ders>-<hafta>.json dosyasını
sitenin kanonik şemasında yazar. Araç çıktıyı yayın denetimiyle aynı kurallarla sınar (sayfayı
geçici bir klasöre gerçekten derleyip HTML'i de denetler), hatalıysa sorunları modele geri verip
bir kez daha dener, sonra:
  - araclar/gorseller/<ad>-<hafta>.py   görsel modülü (GORSELLER + uygula)
  - araclar/sosyal/bilgi-<sinif>-<kısa ders>-<hafta>.json   sosyal medya bilgi kartı
dosyalarını üretir. Var olan özetler atlanır; yarıda kalan bir çalıştırma aynı komutla sürdürülür.

İki kip:
  --toplu  Message Batches API: aynı model, yarı fiyat; sonuçlar genelde bir saat içinde gelir.
           Önceki bir çalıştırma yarıda kaldıysa son 48 saatteki toplu isteklerin sonuçları
           yeniden ödenmeden toplanır.
  (yok)    Anlık akış: istekler hemen yanıtlanır, reddedilen istek sunucuda yedek modele düşer.

Kaynaklar: public/veri/gunluk-plan/<plan>.json (haftanın ünite/konu/çıktıları) ve önceki haftaların
özetleri (üslup ve süreklilik). Plan dosyası olmayan lise İngilizcede yalnız önceki haftalar kullanılır.

Kullanım:
  export ANTHROPIC_API_KEY=...            # platform.claude.com → API Keys (KURULUM.md)
  python3 araclar/ozet_api_uret.py --hafta 15 --toplu                 # 103 dersin tamamı
  python3 araclar/ozet_api_uret.py --hafta 15 --dersler 7-matematik,5-fen-bilimleri
  python3 araclar/ozet_api_uret.py --hafta 15 --model claude-sonnet-5-5 --butce 30
  python3 araclar/ozet_api_uret.py --hafta 15 --kuru               # API'siz prova; geçici klasöre yazar
  python3 araclar/ozet_api_uret.py --kuyruk-baslangici             # sosyal kuyruk için sıradaki saat
  python3 araclar/ozet_api_uret.py --yayin-hazirla yeni.txt        # derle; denetimden geçmeyen yeni özeti ayıkla
Sonrasında: python3 araclar/sosyal_gorsel.py --kuyruk "$(python3 araclar/ozet_api_uret.py --kuyruk-baslangici)"
"""
import argparse
import html
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import threading
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
PUBLIC = KOK / 'public'
OZETLER = ARACLAR / 'ozetler'          # okuma: önceki haftalar ve var olan özetler
PLANLAR = PUBLIC / 'veri' / 'gunluk-plan'
YAZ = {'ozet': OZETLER, 'gorsel': ARACLAR / 'gorseller', 'sosyal': ARACLAR / 'sosyal'}   # --kuru geçici klasöre çevirir

VARSAYILAN_MODEL = 'claude-opus-5-5'
# USD / 1M jeton, anlık fiyat: (girdi, çıktı, önbellek yazma, önbellek okuma). Toplu istek bunların yarısı.
FIYAT = {
    'claude-opus-5-5': (4.0, 20.0, 5.0, 0.20),
    'claude-sonnet-5-5': (2.0, 10.0, 2.5, 0.20),
    'claude-haiku-5-5': (0.10, 0.50, 0.125, 0.01),
    'claude-opus-5': (5.0, 25.0, 6.25, 0.50),       # yedek model olarak çalışabilir
    'claude-opus-4-8': (5.0, 25.0, 6.25, 0.50),
    'claude-sonnet-5': (2.0, 10.0, 2.5, 0.20),
}
# Bir isteğin anlık fiyatla tahmini (24.10.2026 denemesi: Opus 5.5, çaba high, 3 istek 3,96 $).
ISTEK_TAHMINI = {'claude-opus-5-5': 1.35, 'claude-sonnet-5-5': 0.70, 'claude-haiku-5-5': 0.04}
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

# Birden çok plan dosyası olan dersler: sitenin konu ağacı ve önceki özetlerle aynı plan
PLAN_ESLEME = {
    '5-temel-dini-bilgiler': '5-7-sinif-temel-dini-bilgiler-islam-1',
    '6-temel-dini-bilgiler': '5-7-sinif-temel-dini-bilgiler-islam-1',
    '7-temel-dini-bilgiler': '5-7-sinif-temel-dini-bilgiler-islam-1',
    '8-temel-dini-bilgiler': '8-sinif-temel-dini-bilgiler-islam-2',
    '9-temel-dini-bilgiler': '9-11-sinif-temel-dini-bilgiler-islam-1',
    '10-temel-dini-bilgiler': '9-11-sinif-temel-dini-bilgiler-islam-1',
    '11-temel-dini-bilgiler': '9-11-sinif-temel-dini-bilgiler-islam-1',
    '12-temel-dini-bilgiler': '12-sinif-temel-dini-bilgiler-islam-2',
    '9-kuran-i-kerim': '9-sinif-kuran-i-kerim',
    '10-kuran-i-kerim': '10-sinif-kuran-i-kerim',
    '11-cografya': '11-sinif-cografya-4-saat',
    '12-cografya': '12-sinif-cografya-4-saat',
}

ATIF_RE = re.compile(r"\b(ders kitab|MEB kitab|kitapta\b|kitaptaki|kitaba göre|kitabın|ünitede|özgün (anlam )?özet|bu satırda|kaynak notu)", re.I)
GOSTERIM = ('koyu', 'us', 'alt', 'kesir', 'kok', 'ar', 'uzunluk', 'aci', 'olcu', 'dogru', 'vektor', 'devir', 'isin', 'parca', 'formul', 'vurgu', 'renk', 'egik', 'i')
GOSTERIM_RE = re.compile(r'\{(?:' + '|'.join(GOSTERIM) + r'):')
KOK_ISARETI = re.compile('[√∛∜]')
KUTU_TURLERI = ('bilgi', 'dikkat', 'kural', 'tanim', 'ipucu', 'hatirla')
ZORUNLU = ('sinif', 'ders', 'hafta', 'tarih', 'yayin_tarihi', 'unite', 'konu', 'ciktilar', 'giris', 'bolumler', 'ornekler', 'etkinlikler', 'ozet')

SISTEM = """Sen derskutusu.com için haftalık konu özeti yazan deneyimli bir Türk öğretmen ve içerik editörüsün. Site, Türkiye Yüzyılı Maarif Modeli (MEB 2026-2027) programına göre 5-12. sınıf öğrencilerine ücretsiz, özgün ve etkileşimli konu özetleri sunar. Görevin: verilen sınıf, ders ve hafta için sitenin kanonik JSON şemasında TEK bir özet dosyası yazmak.

ÇIKTI BİÇİMİ
- Yanıtın yalnız geçerli bir JSON nesnesi olsun: açıklama, selamlama, kod çiti (```), Markdown yok. İlk karakter { ve son karakter } olmalı.
- Türkçe karakterleri doğrudan yaz (\\u kaçışı kullanma). Dizelerde satır sonu için \\n kullanılabilir.
- Hedef uzunluk 40-55 KB (önceki haftaların dosyalarıyla aynı derinlik); 60 KB'ı geçme. Kısa geçiştirme yok, gereksiz tekrar da yok.

ŞEMA (alan adları ve türleri birebir böyle)
{
 "ad": "<sinif>-<ders>-<hafta>", "sinif": <tam sayı>, "ders": "<ders kodu>", "ders_adi": "<ders adı>", "hafta": <tam sayı>,
 "tarih": "<verilen>", "yayin_tarihi": "<verilen YYYY-AA-GG>",
 "unite": "düz metin", "konu": "düz metin",
 "ciktilar": ["MEB kodlu öğrenme çıktısı/süreç bileşeni cümleleri", 2-4 madde],
 "giris": "Haftanın kapsamını 2-3 cümlede sıcak bir dille anlatan paragraf ({koyu:...} vurguları olabilir)",
 "ozet": ["Haftanın en önemli 5-6 kazanımı; her madde tek cümle, {koyu:Başlık:} ile başlayabilir"],
 "bolumler": [ 6 bölüm; her biri:
   {"baslik": "düz metin",
    "metin": ["2-3 dolu paragraf; kavramlar {koyu:...} ile vurgulanır"],
    "tablo": {"basliklar": ["...", "..."], "satirlar": [["...", "..."], ...]}   (isteğe bağlı, bölümlerin çoğunda olsun),
    "kutular": [{"tur": "bilgi|dikkat|kural|tanim|ipucu|hatirla", "baslik": "düz metin", "metin": "..."}]  (1-2 kutu),
    "gorsel": "<svg viewBox=\\"0 0 760 300\\" xmlns=\\"http://www.w3.org/2000/svg\\" font-family=\\"Arial, sans-serif\\">...</svg>"
   } ],
 "ornekler": [ TAM 6 adet {"soru": "...", "cevap": "adım adım çözüm", "ipucu": "..."} ],
 "etkinlikler": [ TAM 8 adet, bu sırayla:
   4 × {"tur": "coktan", "soru": "...", "secenekler": ["A", "B", "C", "D"], "dogru": <0-3>, "aciklama": "..."},
   1 × {"tur": "dy", "soru": "Aşağıdaki ifadelerin doğru mu yanlış mı olduğunu belirleyiniz.", "ifadeler": [4-5 × {"metin": "...", "dogru": true|false, "aciklama": "..."}]}  (en az biri yanlış),
   1 × {"tur": "eslestir", "soru": "...", "ciftler": [5 × ["sol kavram", "sağ açıklama"]]},
   1 × {"tur": "bosluk", "soru": "Aşağıdaki cümlelerde boş bırakılan yerleri uygun kavramlarla tamamlayınız.", "cumleler": [5 × {"metin": "... ___ ...", "cevap": "tek kelime/kısa"}], "kelimeler": [cevaplar], "fazla": [2 çeldirici]},
   1 × {"tur": "ogretici", "soru": "çok adımlı uygulama sorusu", "ipuclari": ["1. adım ...", "2. adım ...", "3. adım ..."], "cevap": "tam çözüm"} ]
}
"düz metin" yazan alanlarda (unite, konu, bölüm ve kutu başlıkları) süslü parantezli gösterim kullanma; bu alanlar sayfaya olduğu gibi basılır.

GÖRSELLER
- 6 bölümün 6'sında da "gorsel" olsun: geçerli, kendi içinde tam XML olan SVG (xmlns ve viewBox şart; & için &amp;, < için &lt; yaz; CSS/script yok; dış dosya yok).
- Genişlik 700-900, yükseklik 240-420 birim; açık arka plan (#f8fafc) ve yuvarlatılmış kutular; yazılar 10-16 punto; şema, akış, zaman çizelgesi, karşılaştırma kutuları, sayı doğrusu, grafik gibi konuya özgü görseller. Yazılar Türkçe (İngilizce dersinde İngilizce olabilir; Arapça dersinde Arapça harf kullanma, çeviri yazı kullan).
- SVG içinde süslü parantezli gösterim ({kok:...}, {us:...} vb.) ASLA kullanma; SVG sayfaya olduğu gibi basılır. Kök işaretini (√, &#8730;, &radic;) da yazma: kök için "karekök(16) = 4" gibi düz yazı, üs için x² gibi Unicode üst simge kullan.

METİN GÖSTERİMİ (yalnız SVG ve "düz metin" alanları dışındaki metinlerde; site bu işaretleri HTML'e çevirir; başka süslü parantezli gösterim kullanma)
- {koyu:metin} kalın; {us:x|2} üs (x²); {alt:H|2} alt indis (H₂); {kesir:pay|payda} kesir (pay ve paydada | olmasın); {kok:ifade} karekök, {kok:ifade|3} küp kök; {uzunluk:AB} |AB| (mutlak değer/uzunluk; {kesir} içinde | gerektiğinde de bu kullanılır); {ar:عربي} Arapça (yalnız Arapça/Kur'an/Mesleki Arapça derslerinde).
- √ ∛ ∜ karakterlerini (ve &#8730; gibi karşılıklarını) ve LaTeX'i ($...$, \\frac) asla kullanma. Çarpma için × veya ·, bölme için ÷, eksi için − kullanılabilir.
- Şu kelime ve kalıplar hiçbir alanda geçmesin (yayın denetimi reddeder): "ders kitabı/kitabı/kitabın/kitabının" ile başlayan atıflar, "MEB kitabı", "kitapta", "kitaptaki", "kitaba göre", "kitabın", "ünitede" (bunun yerine "bu ünite kapsamında" de), "özgün özet", "bu satırda", "kaynak notu". Metin kitaptan alıntı değil, özgün anlatım olmalı.

İÇERİK İLKELERİ
- Konu, verilen MEB günlük/yıllık planındaki ünite-konu-öğrenme çıktısına ve o haftanın süreç bileşenlerine tam uyar. Plan satırı bir önceki haftayla aynı konuyu gösteriyorsa konunun önceki haftalarda işlenmemiş kalan alt başlıklarını, uygulamalarını ve pekiştirmelerini işle; önceki haftanın bölüm başlıklarını tekrarlama. Plan satırında konu boşsa ünitenin bir sonraki konusunu seç. Plan verilmemişse önceki haftalardan devam eden temanın sırasındaki konuyu seç.
- Yaş düzeyine uygun, sıcak ama ciddi bir dil; "bu hafta", "haftamızda" gibi bağlantılar olabilir. Dinî derslerde ayet ve hadisler mealle, sure/ayet numarasıyla; tarihsel olgular ve sayısal bilgiler doğru olmalı (emin olmadığın tarih/sayıyı yazma).
- Örnekler ve etkinlikler konunun kendisiyle ilgili, çözülebilir, cevapları doğru ve tutarlı olsun; çoktan seçmeli soruların tek doğru cevabı olsun; dogru indeksi 0'dan başlar.
- Konu matematik/fen ise işlemleri adım adım yaz; sözel derslerde kavram-örnek-sonuç düzeninde yaz. Dil derslerinde hedef kelimeler Türkçe karşılıklarıyla birlikte verilir.
- Önceki haftanın dosyası sana örnek olarak verilir: aynı derinlik, aynı alan adları, aynı üslup; ama içerik yeni haftanın konusu olacak."""


def _yukle(ad, yol):
    spec = importlib.util.spec_from_file_location(ad, yol)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dersler_sozlugu():
    return json.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))['dersler']


def ozet_kimlikleri():
    """araclar/ozetler içindeki sınıf-ders çiftleri (sınıf sırasıyla)."""
    kimlikler = {re.sub(r'-\d+$', '', p.stem) for p in OZETLER.glob('*.json') if re.fullmatch(r'\d+-.+-\d+', p.stem)}
    return sorted(kimlikler, key=lambda k: (int(k.split('-')[0]), k))


# ------------------------------------------------------------------ plan

def plan_dosyasi(kimlik):
    """Dersin günlük plan dosyası; lise İngilizce gibi planı olmayan derslerde None."""
    if kimlik in PLAN_ESLEME:
        return PLANLAR / f'{PLAN_ESLEME[kimlik]}-gunluk-plan-2026-2027.json'
    sinif, ders = kimlik.split('-', 1)
    # Arapça planları -iho/-aihl ekiyle adlandırılır (5-sinif-arapca-iho-..., 11-sinif-mesleki-arapca-aihl-...)
    adaylar = sorted(p for p in PLANLAR.glob(f'{sinif}-sinif-{ders}-*gunluk-plan-*.json')
                     if re.fullmatch(rf'{sinif}-sinif-{re.escape(ders)}(?:-(?:iho|aihl))?-gunluk-plan-.+', p.stem))
    return adaylar[0] if len(adaylar) == 1 else None


def plan_satiri(kimlik, hafta):
    """Planın o haftasındaki alanlar: {hafta, tarih, unite, konu, ciktilar, surec, sure} ya da None.
    Eski programdaki planlar (8. ve 12. sınıflar) 'Konu', 'Kazanımlar', 'Açıklamalar' adlarını kullanır."""
    p = plan_dosyasi(kimlik)
    if not p or not p.exists():
        return None
    plan = json.loads(p.read_text(encoding='utf-8'))
    h = next((x for x in plan.get('haftalar', []) if x.get('no') == hafta), None)
    if not h:
        return None
    alanlar = {k: v for _, al in h.get('bolumler', []) for k, v in al}

    def al(*adlar):
        return next((alanlar[a] for a in adlar if (alanlar.get(a) or '').strip()), '')

    return {'hafta': h.get('hafta', ''), 'tarih': h.get('tarih', ''), 'unite': al('Ünite / Tema'),
            'konu': al('Konu (içerik çerçevesi)', 'Konu'), 'ciktilar': al('Öğrenme çıktıları', 'Kazanımlar'),
            'surec': al('Süreç bileşenleri / açıklamalar', 'Açıklamalar'), 'sure': al('Süre')}


def hafta_tarihi(hafta, kimlikler):
    """Haftanın pazartesi tarihi (planların çoğunluğuna göre) → ('28 Aralık 2026-1 Ocak 2027', '2026-12-28')."""
    sayac = {}
    for k in kimlikler:
        s = plan_satiri(k, hafta)
        if s and re.fullmatch(r'\d{4}-\d{2}-\d{2}', s['tarih'] or ''):
            sayac[s['tarih']] = sayac.get(s['tarih'], 0) + 1
    if not sayac:
        raise SystemExit(f'{hafta}. hafta için planlarda tarih bulunamadı')
    bas = datetime.strptime(max(sayac, key=sayac.get), '%Y-%m-%d')
    son = bas + timedelta(days=4)
    if bas.month == son.month:
        etiket = f'{bas.day}-{son.day} {AYLAR[bas.month - 1]} {bas.year}'
    elif bas.year == son.year:
        etiket = f'{bas.day} {AYLAR[bas.month - 1]}-{son.day} {AYLAR[son.month - 1]} {bas.year}'
    else:
        etiket = f'{bas.day} {AYLAR[bas.month - 1]} {bas.year}-{son.day} {AYLAR[son.month - 1]} {son.year}'
    return etiket, bas.strftime('%Y-%m-%d')


def onceki_ozetler(kimlik, hafta, adet=3):
    liste = []
    for h in range(hafta - 1, max(0, hafta - 1 - adet), -1):
        p = OZETLER / f'{kimlik}-{h}.json'
        if p.exists():
            liste.append(json.loads(p.read_text(encoding='utf-8')))
    return liste


def ornek_kirp(o):
    """Örnek dosyada 3. bölümden sonraki SVG'leri kısaltır (istek boyutu düşer, biçim yine görülür)."""
    k = json.loads(json.dumps(o, ensure_ascii=False))
    for i, b in enumerate(k.get('bolumler', [])):
        if i >= 2 and isinstance(b.get('gorsel'), str) and len(b['gorsel']) > 400:
            b['gorsel'] = b['gorsel'][:300] + '…(kısaltıldı; sen tam SVG yazacaksın)</svg>'
    for anahtar in ('claude_denetim', 'kalite'):
        k.pop(anahtar, None)
    return k


def istek_metni(kimlik, hafta, tarih, yayin, dersler):
    sinif, ders = kimlik.split('-', 1)
    satir = plan_satiri(kimlik, hafta)
    onceki = onceki_ozetler(kimlik, hafta)
    if not onceki:
        raise ValueError(f'{kimlik}: önceki hafta özeti yok; üslup örneği gerekli')
    parcalar = [f'SINIF: {sinif}\nDERS: {dersler[ders]} (kod: {ders})\nHAFTA: {hafta}\nTARİH: {tarih}\nYAYIN TARİHİ: {yayin}\nDOSYA ADI (ad alanı): {kimlik}-{hafta}']
    if satir:
        sonraki = plan_satiri(kimlik, hafta + 1)
        parcalar.append('MEB GÜNLÜK PLANINDA BU HAFTA:\n' + json.dumps(satir, ensure_ascii=False, indent=1))
        if sonraki:
            parcalar.append('PLANDA BİR SONRAKİ HAFTA (sınır; buraya girme):\n' + json.dumps({k: sonraki[k] for k in ('unite', 'konu', 'ciktilar')}, ensure_ascii=False, indent=1))
    else:
        parcalar.append('Bu ders için plan dosyası yok: önceki haftalardaki tema sırasını MEB 2026-2027 yıllık planına göre sürdür.')
    gecmis = [{'hafta': o['hafta'], 'unite': o.get('unite'), 'konu': o.get('konu'), 'bolum_basliklari': [b.get('baslik') for b in o.get('bolumler', [])]} for o in onceki]
    parcalar.append('ÖNCEKİ HAFTALARDA İŞLENENLER (tekrarlama, devam et):\n' + json.dumps(gecmis, ensure_ascii=False, indent=1))
    parcalar.append(f'ÜSLUP VE ŞEMA ÖRNEĞİ — {onceki[0]["hafta"]}. haftanın dosyası (içeriğini değil biçimini ve derinliğini örnek al):\n' + json.dumps(ornek_kirp(onceki[0]), ensure_ascii=False))
    parcalar.append(f'Şimdi {sinif}. sınıf {dersler[ders]} {hafta}. hafta özetini yukarıdaki şemayla, yalnız JSON olarak yaz.')
    return '\n\n'.join(parcalar)


# ----------------------------------------------------------------- doğrulama

def _dizeler(o, yol=''):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from _dizeler(v, f'{yol}.{k}' if yol else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _dizeler(v, f'{yol}[{i}]')
    elif isinstance(o, str):
        yield yol, o


def _kok_var(s):
    """yayin_denetle.py ile aynı: HTML karşılıkları (&#8730; &radic;) ve \\u221a kaçışları da kök sayılır."""
    return bool(KOK_ISARETI.search(html.unescape(re.sub(r'\\u221[abc]', '√', s, flags=re.I))))


def sema_denetle(d):
    """Alan türleri: sayfa üreticisinin .get/+ ile eriştiği her yer sözlük/liste olmalı."""
    h = []
    for a in ZORUNLU:
        if a not in d:
            h.append(f'zorunlu alan eksik: {a}')
    if h:
        return h
    for a in ('unite', 'konu', 'giris', 'tarih', 'yayin_tarihi'):
        if not isinstance(d[a], str):
            h.append(f'{a} düz metin (dize) olmalı')
    for a in ('ciktilar', 'ozet', 'bolumler', 'ornekler', 'etkinlikler'):
        if not isinstance(d[a], list):
            h.append(f'{a} liste olmalı')
    if h:
        return h
    if not all(isinstance(x, str) for x in d['ciktilar'] + d['ozet']):
        h.append('ciktilar ve ozet dize listesi olmalı')
    for i, b in enumerate(d['bolumler']):
        if not isinstance(b, dict):
            h.append(f'bolumler[{i}] nesne olmalı')
            continue
        if not isinstance(b.get('metin', []), list) or not all(isinstance(x, str) for x in b.get('metin', [])):
            h.append(f'bolumler[{i}].metin dize listesi olmalı')
        if 'tablo' in b and not isinstance(b['tablo'], dict):
            h.append(f'bolumler[{i}].tablo {{"basliklar": [...], "satirlar": [[...]]}} nesnesi olmalı')
        elif isinstance(b.get('tablo'), dict) and not all(isinstance(r, list) for r in b['tablo'].get('satirlar', [])):
            h.append(f'bolumler[{i}].tablo.satirlar liste listesi olmalı')
        if not isinstance(b.get('kutular', []), list) or not all(isinstance(k, dict) for k in b.get('kutular', [])):
            h.append(f'bolumler[{i}].kutular nesne listesi olmalı')
        if 'kutu' in b and not isinstance(b['kutu'], dict):
            h.append(f'bolumler[{i}].kutu nesne olmalı')
        if 'gorsel' in b and not isinstance(b['gorsel'], str):
            h.append(f'bolumler[{i}].gorsel SVG dizesi olmalı')
    for i, o in enumerate(d['ornekler']):
        if not isinstance(o, dict):
            h.append(f'ornekler[{i}] nesne olmalı')
    for i, x in enumerate(d['etkinlikler']):
        if not isinstance(x, dict):
            h.append(f'etkinlikler[{i}] nesne olmalı')
            continue
        for alan, tur in (('secenekler', list), ('ifadeler', list), ('ciftler', list), ('cumleler', list), ('kelimeler', list), ('fazla', list), ('ipuclari', list)):
            if alan in x and not isinstance(x[alan], tur):
                h.append(f'etkinlikler[{i}].{alan} liste olmalı')
        for alan in ('ifadeler', 'cumleler'):
            if isinstance(x.get(alan), list) and not all(isinstance(y, dict) for y in x[alan]):
                h.append(f'etkinlikler[{i}].{alan} nesne listesi olmalı')
    return h


def icerik_denetle(d, e_fonk):
    """Yayın denetimi (yayin_denetle.py) ve sayfa üreticisiyle aynı kurallar."""
    h = []
    if len(d['ornekler']) != 6:
        h.append(f"örnek sayısı {len(d['ornekler'])} (6 olmalı)")
    for i, o in enumerate(d['ornekler']):
        if not o.get('soru') or not o.get('cevap'):
            h.append(f'ornekler[{i}]: soru/cevap eksik')
    E = d['etkinlikler']
    turler = [x.get('tur') for x in E]
    if len(E) != 8:
        h.append(f'etkinlik sayısı {len(E)} (8 olmalı)')
    if turler.count('coktan') != 4:
        h.append(f"coktan sayısı {turler.count('coktan')} (4 olmalı)")
    for t in ('dy', 'eslestir', 'bosluk', 'ogretici'):
        if turler.count(t) != 1:
            h.append(f"etkinlik türü '{t}' tam 1 kez olmalı")
    for i, x in enumerate(E):
        t = x.get('tur')
        if not x.get('soru'):
            h.append(f'etkinlikler[{i}] ({t}): soru eksik')
        if t == 'coktan':
            n = len(x.get('secenekler', []))
            if not 4 <= n <= 5:
                h.append(f'etkinlikler[{i}]: 4 seçenek olmalı')
            if not isinstance(x.get('dogru'), int) or isinstance(x.get('dogru'), bool) or not 0 <= x.get('dogru', -1) < n:
                h.append(f'etkinlikler[{i}]: dogru, seçenek dizisinde geçerli bir indeks (0-{max(n - 1, 0)}) olmalı')
            if not x.get('aciklama'):
                h.append(f'etkinlikler[{i}]: aciklama eksik')
        elif t == 'dy':
            ifl = x.get('ifadeler', [])
            if not 4 <= len(ifl) <= 6:
                h.append(f'etkinlikler[{i}]: dy 4-6 ifade olmalı')
            for j, y in enumerate(ifl):
                if not isinstance(y.get('dogru'), bool) or not y.get('metin'):
                    h.append(f'etkinlikler[{i}].ifadeler[{j}]: metin ve dogru (true/false) gerekli')
            if ifl and not any(y.get('dogru') is False for y in ifl):
                h.append(f'etkinlikler[{i}]: en az bir yanlış ifade olmalı')
        elif t == 'eslestir':
            c = x.get('ciftler', [])
            if not 4 <= len(c) <= 6 or not all(isinstance(y, list) and len(y) == 2 and y[0] and y[1] for y in c):
                h.append(f'etkinlikler[{i}]: ciftler [[sol, sağ], ...] biçiminde 4-6 çift olmalı')
        elif t == 'bosluk':
            c = x.get('cumleler', [])
            if not 4 <= len(c) <= 6:
                h.append(f'etkinlikler[{i}]: 4-6 cümle olmalı')
            for j, y in enumerate(c):
                if '___' not in y.get('metin', '') or not y.get('cevap'):
                    h.append(f'etkinlikler[{i}].cumleler[{j}]: metin içinde ___ ve cevap gerekli')
            if not x.get('fazla'):
                h.append(f'etkinlikler[{i}]: fazla (çeldirici) en az 1 olmalı')
        elif t == 'ogretici':
            if len(x.get('ipuclari', [])) < 2 or not x.get('cevap'):
                h.append(f'etkinlikler[{i}]: ipuclari (2-3) ve cevap gerekli')
    B = d['bolumler']
    if not 5 <= len(B) <= 6:
        h.append(f'bölüm sayısı {len(B)} (6 olmalı)')
    gorselli = 0
    for i, b in enumerate(B):
        if not b.get('baslik'):
            h.append(f'bolumler[{i}]: baslik eksik')
        if len(b.get('metin', [])) < 2:
            h.append(f'bolumler[{i}]: metin en az 2 paragraf olmalı')
        g = b.get('gorsel')
        if g:
            gorselli += 1
            if not g.lstrip().startswith('<svg'):
                h.append(f'bolumler[{i}].gorsel: <svg ile başlayan dize olmalı')
            else:
                try:
                    ET.fromstring(g)
                except ET.ParseError as exc:
                    h.append(f'bolumler[{i}].gorsel geçersiz XML: {exc}')
                if 'viewBox' not in g:
                    h.append(f'bolumler[{i}].gorsel: viewBox yok')
                if GOSTERIM_RE.search(g):
                    h.append(f'bolumler[{i}].gorsel: SVG içinde süslü parantezli gösterim var ({GOSTERIM_RE.search(g).group(0)}...); düz yazı kullan')
                if _kok_var(g):
                    h.append(f'bolumler[{i}].gorsel: SVG içinde kök işareti var; "karekök(...)" yaz')
        for k in b.get('kutular', []) + ([b['kutu']] if b.get('kutu') else []):
            if not k.get('metin'):
                h.append(f'bolumler[{i}]: kutu metni eksik')
            if GOSTERIM_RE.search(k.get('baslik') or ''):
                h.append(f'bolumler[{i}]: kutu başlığı düz metin olmalı (süslü parantezli gösterim var)')
        if GOSTERIM_RE.search(b.get('baslik') or ''):
            h.append(f'bolumler[{i}]: bölüm başlığı düz metin olmalı')
        t = b.get('tablo')
        if t and (not t.get('satirlar') or not t.get('basliklar')):
            h.append(f'bolumler[{i}].tablo: basliklar ve satirlar gerekli')
    if gorselli < 4:
        h.append(f'görselli bölüm sayısı {gorselli} (6 olmalı, en az 4)')
    for a in ('unite', 'konu'):
        if GOSTERIM_RE.search(d[a]):
            h.append(f'{a} düz metin olmalı (süslü parantezli gösterim var)')
    if not 4 <= len(d['ozet']) <= 7:
        h.append('ozet 5-6 dizelik liste olmalı')
    if not 1 <= len(d['ciktilar']) <= 6:
        h.append('ciktilar 2-4 maddelik liste olmalı')
    for yol, s in _dizeler(d):
        if _kok_var(s) and '<svg' not in s:
            h.append(f'{yol}: kök işareti; {{kok:...}} kullan')
        if '<svg' in s:
            continue
        m = ATIF_RE.search(s)
        if m:
            h.append(f"{yol}: yasak ifade '{m.group(0)}'")
        for m in re.finditer(r'\{([a-z]+):', s):
            if m.group(1) not in GOSTERIM:
                h.append(f'{yol}: tanımsız gösterim {{{m.group(1)}:...}}')
        for m in re.finditer(r'\{kesir:([^{}]+)\}', s):
            pay, sep, payda = m.group(1).partition('|')
            if not sep or not pay.strip() or not payda.strip() or '|' in payda:
                h.append(f'{yol}: bozuk kesir {m.group(0)}')
        try:
            e_fonk(s)
        except Exception as exc:
            h.append(f'{yol}: {exc}')
    boyut = len(json.dumps(d, ensure_ascii=False).encode())
    if boyut < 26000:
        h.append(f'içerik {boyut} bayt: çok kısa (hedef 40-55 KB); bölümleri, örnekleri ve açıklamaları genişlet')
    return h


class SayfaDenetci:
    """Özeti geçici bir klasöre gerçekten derler; yayin_denetle.py'nin HTML kurallarını uygular."""

    def __init__(self, dersler):
        self.gecici = Path(tempfile.mkdtemp(prefix='ozet-sayfa-'))
        (self.gecici / 'ozet').mkdir()
        self.mod = _yukle('ozet_uret_sayfa', ARACLAR / 'ozet_uret.py')
        self.mod.PUBLIC = self.gecici
        self.dersler = json.loads((PUBLIC / 'veri' / 'dersler.json').read_text(encoding='utf-8'))   # sayfa_uret bütün dosyayı ister
        self.kilit = threading.Lock()

    def denetle(self, d):
        with self.kilit:
            try:
                self.mod.sayfa_uret(d, self.dersler, [], {})
            except Exception as exc:
                return [f'sayfa derlenemedi: {type(exc).__name__}: {exc}']
            dosya = self.gecici / 'ozet' / f'{d["sinif"]}-{d["ders"]}-hafta-{d["hafta"]}.html'
            s = dosya.read_text(encoding='utf-8')
            dosya.unlink()
        h = []
        if _kok_var(s):
            h.append('derlenen sayfada düz kök işareti var (SVG ya da başlıkta √ / &#8730;); "karekök(...)" ya da {kok:...} kullan')
        kalan = GOSTERIM_RE.search(s)
        if kalan:
            bas = max(0, kalan.start() - 60)
            h.append(f'derlenen sayfada çözülmemiş gösterim: …{html.unescape(re.sub(r"<[^>]+>", " ", s[bas:kalan.start() + 40]))}… (SVG, başlık, unite ve konu düz metin olmalı)')
        if re.search(r'<span class="s-kesir"[^>]*>(?:<span>\s*</span>|<span>[^<]*</span><span>\s*</span>)', s):
            h.append('derlenen sayfada boş kesir (pay ya da payda boş)')
        return h


def dogrula(d, e_fonk, sayfa):
    """Sorun listesi; boşsa dosya yazılabilir. Beklenmedik biçim istisna atmaz, sorun olarak döner."""
    if not isinstance(d, dict):
        return ['yanıt bir JSON nesnesi olmalı']
    try:
        h = sema_denetle(d)
        if h:
            return h
        h = icerik_denetle(d, e_fonk)
        if h:
            return h
        return sayfa.denetle(d)
    except Exception as exc:
        return [f'şema hatası: {type(exc).__name__}: {exc}']


# ------------------------------------------------------------- son işlemler

def normalize(d, kimlik, hafta, tarih, yayin, dersler):
    sinif, ders = kimlik.split('-', 1)
    d['ad'] = f'{kimlik}-{hafta}'
    d['sinif'] = int(sinif)
    d['ders'] = ders
    d['ders_adi'] = dersler[ders]
    d['hafta'] = hafta
    d['tarih'] = tarih
    d['yayin_tarihi'] = yayin
    for b in d.get('bolumler', []):
        for k in b.get('kutular', []) + ([b['kutu']] if b.get('kutu') else []):
            tur = k.pop('tip', None) or k.get('tur')
            k['tur'] = {'onemli': 'dikkat', 'kavram': 'tanim'}.get(tur, tur) if tur in KUTU_TURLERI + ('onemli', 'kavram') else 'bilgi'
    sira = ['ad', 'sinif', 'ders', 'ders_adi', 'hafta', 'tarih', 'yayin_tarihi', 'unite', 'konu', 'ciktilar', 'giris', 'ozet', 'bolumler', 'ornekler', 'etkinlikler']
    return {k: d[k] for k in sira if k in d} | {k: v for k, v in d.items() if k not in sira}


def gorsel_modulu_yaz(d, ad):
    gorseller = {f'b{i + 1}': b['gorsel'] for i, b in enumerate(d.get('bolumler', [])) if b.get('gorsel')}
    icerik = ('# -*- coding: utf-8 -*-\n'
              f'# {ad} görsel modülü\n\n'
              f'GORSELLER = {gorseller!r}\n\n'
              'def uygula(v):\n'
              "    for idx, b in enumerate(v.get('bolumler', []), 1):\n"
              "        svg = GORSELLER.get(f'b{idx}') or GORSELLER.get(str(idx))\n"
              '        if svg:\n'
              "            b['gorsel'] = svg\n"
              '    return v\n')
    (YAZ['gorsel'] / f'{ad}.py').write_text(icerik, encoding='utf-8')


_US = str.maketrans('0123456789+-−=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿ')
_ALT = str.maketrans('0123456789+-−=()', '₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎')
_ARAP = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+')


def _parantez(s):
    s = s.strip()
    return f'({s})' if re.search(r'[\s+\-−×·÷]', s) else s


def _us_yaz(taban, us):
    return taban + (us.translate(_US) if all(c in '0123456789+-−=()n' for c in us) else f'^({us})' if len(us) > 1 else f'^{us}')


def _alt_yaz(taban, alt):
    return taban + (alt.translate(_ALT) if all(c in '0123456789+-−=()' for c in alt) else f'_{alt}')


def duz_metin(s):
    """Site gösterimlerini sosyal kart için düz metne çevirir; Arapça harfleri kaldırır.
    İç içe gösterimler en içten başlayarak, değişiklik kalmayana dek çözülür."""
    s = re.sub(r'\{ar:[^{}]*\}', '', s)
    onceki = None
    while onceki != s:
        onceki = s
        s = re.sub(r'\{us:([^{}|]+)\|([^{}]+)\}', lambda m: _us_yaz(m.group(1), m.group(2)), s)
        s = re.sub(r'\{alt:([^{}|]+)\|([^{}]+)\}', lambda m: _alt_yaz(m.group(1), m.group(2)), s)
        s = re.sub(r'\{kesir:([^{}|]+)\|([^{}]+)\}', lambda m: f'{_parantez(m.group(1))}/{_parantez(m.group(2))}', s)
        s = re.sub(r'\{kok:([^{}|]+)(?:\|(\d+))?\}', lambda m: {'3': 'küp kök', None: 'karekök'}.get(m.group(2), f'{m.group(2)}. dereceden kök') + f'({m.group(1).strip()})', s)
        s = re.sub(r'\{uzunluk:([^{}]+)\}', r'|\1|', s)
        s = re.sub(r'\{olcu:([^{}]+)\}', r'm(\1)', s)
        s = re.sub(r'\{devir:([^{}]+)\}', r'(\1)', s)
        s = re.sub(r'\{isin:([^{}]+)\}', r'[\1', s)
        s = re.sub(r'\{parca:([^{}]+)\}', r'[\1]', s)
        s = re.sub(r'\{renk:[^{}:|]*[:|]([^{}]*)\}', r'\1', s)
        # | taşıyan gösterimler (us, alt, kesir, kok, renk) yukarıda çözülür; iç içeyse bir sonraki turda
        s = re.sub(r'\{(?!(?:us|alt|kesir|kok|renk):)[a-z]+:([^{}]*)\}', r'\1', s)
    s = re.sub(r'\{[a-z]+:([^{}]*)\}', r'\1', s)      # beklenmedik biçim kalırsa kart ham işaret göstermesin
    s = _ARAP.sub('', s)
    s = re.sub(r'\(\s*[,;]?\s*\)', '', s)
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    s = re.sub(r'([,;])(\s*[,;])+', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def kirp(s, sinir):
    if len(s) <= sinir:
        return s
    kes = s[:sinir].rsplit(' ', 1)[0].rstrip(',;:')
    return kes if kes.endswith('.') else kes + '.'


def sosyal_karti_yaz(d, kimlik, hafta):
    sg = _yukle('sosyal_gorsel_api', ARACLAR / 'sosyal_gorsel.py')
    sinif, ders = kimlik.split('-', 1)
    dosya = sg.DERSLER[ders][0]
    # Arapça kelime içermeyen özet maddeleri önce: kart Arapça harf çizemez, çıkarılınca cümle bozulur
    maddeler = sorted(d['ozet'], key=lambda x: '{ar:' in x)
    paragraflar = [kirp(duz_metin(x), 240) for x in maddeler[:2]]
    kart = {'ozet': f'{kimlik}-{hafta}', 'baslik': kirp(duz_metin(d['bolumler'][0]['baslik']), 80),
            'paragraflar': paragraflar, 'bilgi': ' '.join(paragraflar)}
    (YAZ['sosyal'] / f'bilgi-{sinif}-{dosya}-{hafta}.json').write_text(json.dumps(kart, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def kaydet(d, kimlik, hafta, tarih, yayin, dersler):
    d = normalize(d, kimlik, hafta, tarih, yayin, dersler)
    (YAZ['ozet'] / f'{kimlik}-{hafta}.json').write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    gorsel_modulu_yaz(d, f'{kimlik}-{hafta}')
    sosyal_karti_yaz(d, kimlik, hafta)
    return len(json.dumps(d, ensure_ascii=False).encode()) // 1024


def kuyruk_baslangici():
    """sosyal/kuyruk.json içindeki son gönderiden bir saat sonrası (ISO, yerel saat)."""
    k = json.loads((KOK / 'sosyal' / 'kuyruk.json').read_text(encoding='utf-8'))
    son = max(g['zaman'] for g in k['gonderiler'])
    t = datetime.fromisoformat(son) + timedelta(hours=1)
    return t.replace(tzinfo=None).isoformat(timespec='minutes')


def yayin_hazirla(liste_dosyasi):
    """yayin_denetle.py --onar'ı çalıştırır. Hata yalnız bu çalıştırmada eklenen özetlerdense o özetleri
    (ve görsel modülü, sosyal kartı) ayıklayıp yeniden dener; böylece tek dosya bütün haftanın
    yayımını durdurmaz. Ayıklananlar yazdırılır; çıkış kodu 0 = yayımlanabilir."""
    yeni = [s.strip() for s in Path(liste_dosyasi).read_text(encoding='utf-8').splitlines() if s.strip()]
    ayiklanan = []

    def ayikla(ad, neden):
        m = re.fullmatch(r'(\d+)-(.+)-(\d+)', ad)
        sinif, ders, hafta = m.group(1), m.group(2), m.group(3)
        sg = _yukle('sosyal_gorsel_hazirla', ARACLAR / 'sosyal_gorsel.py')
        for yol in (OZETLER / f'{ad}.json', ARACLAR / 'gorseller' / f'{ad}.py',
                    ARACLAR / 'sosyal' / f'bilgi-{sinif}-{sg.DERSLER[ders][0]}-{hafta}.json',
                    PUBLIC / 'ozet' / f'{sinif}-{ders}-hafta-{hafta}.html'):
            yol.unlink(missing_ok=True)
        ayiklanan.append(ad)
        print(f'::warning::{ad} yayın denetiminden geçmedi ({neden[:300]}); bu hafta yayımlanmadan ayıklandı (Artifacts yedeğinde duruyor).', flush=True)

    # Önce üretimdeki denetimin aynısı: sayfa üreticisini çökertecek bir özet (dosya adı vermeden
    # çöker) derlemeye hiç girmesin.
    dersler = dersler_sozlugu()
    e_fonk, sayfa = _yukle('ozet_uret_hazirla', ARACLAR / 'ozet_uret.py').e, SayfaDenetci(dersler)
    for yol in yeni:
        m = re.fullmatch(r'araclar/ozetler/(\d+-.+-\d+)\.json', yol)
        if not m or not (KOK / yol).exists():
            continue
        try:
            d = json.loads((KOK / yol).read_text(encoding='utf-8'))
        except Exception as exc:
            ayikla(m.group(1), f'JSON okunamadı: {exc}')
            continue
        sorunlar = dogrula(d, e_fonk, sayfa)
        if sorunlar:
            ayikla(m.group(1), '; '.join(sorunlar[:3]))

    for _ in range(5):
        r = subprocess.run([sys.executable, str(ARACLAR / 'yayin_denetle.py'), '--onar'], cwd=KOK, capture_output=True, text=True)
        print(r.stdout[-3000:], r.stderr[-2000:], sep='\n', flush=True)
        if r.returncode == 0:
            k = subprocess.run([sys.executable, str(ARACLAR / 'kok_yayin_denetle.py')], cwd=KOK, capture_output=True, text=True)
            print(k.stdout[-1500:], k.stderr[-1500:], sep='\n', flush=True)
            if k.returncode == 0:
                break
            cikti = k.stdout + k.stderr
        else:
            cikti = r.stdout + r.stderr
        bozuk = set()
        for satir in cikti.splitlines():
            for m in re.finditer(r'(?:araclar/ozetler/|araclar/gorseller/|public/ozet/)(\d+-[a-z-]+?)(?:-hafta)?-(\d+)\.(?:json|py|html)', satir):
                ad = f'{m.group(1)}-{m.group(2)}'
                if f'araclar/ozetler/{ad}.json' in yeni:
                    bozuk.add(ad)
        if not bozuk:
            print('Denetim hatası bu çalıştırmanın özetlerinden kaynaklanmıyor; yayımlanmadı.', flush=True)
            return 1
        for ad in sorted(bozuk - set(ayiklanan)):
            ayikla(ad, 'yayin_denetle.py')
    else:
        return 1
    if ayiklanan:
        print('AYIKLANAN: ' + ', '.join(ayiklanan))
    return 0


# ------------------------------------------------------------------ üretim

class Sayac:
    """Harcama: anlık fiyat × (toplu istekte 0,5). usage.iterations varsa (yedek modele düşülen istek)
    her deneme kendi modelinin fiyatıyla sayılır."""

    def __init__(self, model):
        self.model = model
        self.kilit = threading.Lock()
        self.girdi = self.cikti = self.onbellek_yaz = self.onbellek_oku = 0
        self.dolar = 0.0
        self.istek = 0

    def ekle(self, kullanim, model=None, toplu=False):
        parcalar = [p for p in (getattr(kullanim, 'iterations', None) or []) if getattr(p, 'type', '') in ('message', 'fallback_message')] or [kullanim]
        with self.kilit:
            self.istek += 1
            for p in parcalar:
                tur = getattr(p, 'type', None)
                # 'message' = istenen modelin (belki reddedilen) denemesi; 'fallback_message' = yedek model
                m = getattr(p, 'model', None) or (self.model if tur == 'message' else model or self.model)
                g, c, oy, oo = FIYAT.get(m, FIYAT[VARSAYILAN_MODEL])
                ti, to = getattr(p, 'input_tokens', 0) or 0, getattr(p, 'output_tokens', 0) or 0
                ty, tk = getattr(p, 'cache_creation_input_tokens', 0) or 0, getattr(p, 'cache_read_input_tokens', 0) or 0
                self.girdi += ti
                self.cikti += to
                self.onbellek_yaz += ty
                self.onbellek_oku += tk
                self.dolar += (ti * g + to * c + ty * oy + tk * oo) / 1e6 * (0.5 if toplu else 1.0)

    def maliyet(self):
        return self.dolar

    def istek_basi(self, toplu=False):
        varsayilan = ISTEK_TAHMINI.get(self.model, 1.35) * (0.5 if toplu else 1.0)
        return max(varsayilan, self.dolar / self.istek) if self.istek else varsayilan

    def __str__(self):
        return (f'{self.istek} istek · girdi {self.girdi:,} · çıktı {self.cikti:,} · önbellek yaz/oku {self.onbellek_yaz:,}/{self.onbellek_oku:,} '
                f'· tahmini {self.maliyet():.2f} $')


def json_ayikla(metin):
    metin = metin.strip()
    metin = re.sub(r'^```(?:json)?\s*', '', metin)
    metin = re.sub(r'\s*```$', '', metin)
    bas, son = metin.find('{'), metin.rfind('}')
    if bas < 0 or son < 0:
        raise ValueError('yanıtta JSON nesnesi yok')
    return json.loads(metin[bas:son + 1])


KREDI_BITTI = ('API kredisi ya da harcama sınırı doldu. Kalan bakiye: platform.claude.com/settings/billing '
               '(Promotional credits). Kredi yenilenince aynı komut kaldığı yerden sürer.')


def _kredi_hatasi(exc):
    import anthropic
    metin = str(exc).lower()
    if isinstance(exc, anthropic.BadRequestError) and any(k in metin for k in ('credit', 'billing', 'usage limit')):
        return True
    if isinstance(exc, anthropic.RateLimitError):
        govde = getattr(exc, 'body', None) or {}
        hata = govde.get('error', {}) if isinstance(govde, dict) else {}
        kod = (hata.get('details') or {}).get('error_code') if isinstance(hata, dict) else None
        return kod == 'enforced_spend_limit_reached' or 'spend limit' in metin
    return False


def _api(cagri):
    """API hatalarını sınıflar: kimlik ve kredi sorunlarında bütün çalıştırma temiz durur."""
    import anthropic
    try:
        return cagri()
    except anthropic.AuthenticationError:
        raise SystemExit('ANTHROPIC_API_KEY geçersiz ya da eksik (KURULUM.md → Claude API kredisiyle özet üretme)')
    except (anthropic.BadRequestError, anthropic.RateLimitError) as exc:
        if _kredi_hatasi(exc):
            raise SystemExit(KREDI_BITTI)
        raise


def istek_parametreleri(args, mesajlar, toplu):
    p = dict(model=args.model, max_tokens=128000,   # düşünme + 40-55 KB JSON; kullanılmayan sınır ücretlendirilmez
             system=[{'type': 'text', 'text': SISTEM, 'cache_control': {'type': 'ephemeral', **({'ttl': '1h'} if toplu else {})}}],
             messages=mesajlar, output_config={'effort': args.caba})
    return p


def yanit_metni(yanit):
    if yanit.stop_reason == 'refusal':
        raise RuntimeError(f'model isteği reddetti ({getattr(yanit.stop_details, "category", None)})')
    if yanit.stop_reason == 'max_tokens':
        raise RuntimeError('yanıt max_tokens sınırında kesildi')
    return ''.join(b.text for b in yanit.content if b.type == 'text')


def denetle_ve_kaydet(metin, kimlik, ctx):
    """(sorunlar, kb). sorunlar boşsa dosyalar yazıldı."""
    try:
        d = json_ayikla(metin)
    except (ValueError, json.JSONDecodeError) as exc:
        return [f'JSON çözülemedi: {exc}'], 0
    sorunlar = dogrula(d, ctx['e'], ctx['sayfa'])
    if sorunlar:
        return sorunlar, 0
    return [], kaydet(d, kimlik, ctx['hafta'], ctx['tarih'], ctx['yayin'], ctx['dersler'])


def duzeltme_mesajlari(ilk_mesaj, metin, sorunlar):
    return [ilk_mesaj, {'role': 'assistant', 'content': metin},
            {'role': 'user', 'content': 'Yanıt yayın denetiminden geçmedi. Şu sorunları gidererek dosyanın TAMAMINI yeniden, yalnız JSON olarak yaz:\n- ' + '\n- '.join(sorunlar[:25])}]


# --- anlık kip

def tek_ozet(client, args, kimlik, ctx, sayac, butce_izni):
    mesaj = {'role': 'user', 'content': istek_metni(kimlik, args.hafta, ctx['tarih'], ctx['yayin'], ctx['dersler'])}
    mesajlar = [mesaj]
    for deneme in (1, 2):
        if deneme == 2 and not butce_izni():
            return 'hata', f'bütçe doldu; düzeltme denemesi yapılmadı ({ilk_sorun})'
        if args.kuru:
            d = onceki_ozetler(kimlik, args.hafta, 1)[0]
            d['hafta'] = args.hafta
            metin = json.dumps(d, ensure_ascii=False)
        else:
            def cagri():
                with client.beta.messages.stream(**istek_parametreleri(args, mesajlar, False),
                                                 betas=['server-side-fallback-2026-07-01'], fallbacks='default') as akis:
                    return akis.get_final_message()
            yanit = _api(cagri)
            sayac.ekle(yanit.usage, getattr(yanit, 'model', None))
            metin = yanit_metni(yanit)
        sorunlar, kb = denetle_ve_kaydet(metin, kimlik, ctx)
        if not sorunlar:
            return 'tamam', f'{kb} KB' + (f', 2. denemede (ilk sorun: {ilk_sorun})' if deneme == 2 else '')
        ilk_sorun = '; '.join(sorunlar[:3])
        if args.kuru:
            return 'hata', ilk_sorun
        mesajlar = duzeltme_mesajlari(mesaj, metin, sorunlar)
    return 'hata', '; '.join(sorunlar[:8])


def anlik_uret(client, args, bekleyen, ctx, sayac, bitis):
    sonuc = {'tamam': [], 'hata': []}
    kalan = list(bekleyen)
    kilit = threading.Lock()
    acik = {'n': 0}
    durdu = None

    def butce_izni():
        # açık işlerin her birinin bir istek daha yapabileceği varsayılır
        with kilit:
            return sayac.maliyet() + acik['n'] * sayac.istek_basi() <= args.butce

    def is_(k):
        try:
            return tek_ozet(client, args, k, ctx, sayac, butce_izni)
        finally:
            with kilit:
                acik['n'] -= 1

    with ThreadPoolExecutor(max_workers=max(1, args.paralel)) as havuz:
        isler = {}
        while kalan or isler:
            while kalan and not durdu and len(isler) < max(1, args.paralel) and time.time() < bitis:
                with kilit:
                    if sayac.maliyet() + (acik['n'] + 1) * sayac.istek_basi() > args.butce:
                        break
                    acik['n'] += 1
                k = kalan.pop(0)
                isler[havuz.submit(is_, k)] = k
            if not isler:
                break
            biten = next(as_completed(list(isler)))
            k = isler.pop(biten)
            try:
                durum, not_ = biten.result()
            except SystemExit as exc:      # kredi/anahtar: yeni iş açma, açık işler bitsin
                if not durdu:
                    print(f'  [dur] {exc}', flush=True)
                durdu = str(exc)
                durum, not_ = 'hata', 'çalıştırma durduruldu'
            except Exception as exc:       # ağ/API hatası: diğer dersler sürsün
                durum, not_ = 'hata', f'{type(exc).__name__}: {exc}'
            sonuc[durum].append(k)
            print(f'  [{durum}] {k}-{args.hafta}: {not_}', flush=True)
    if durdu:
        raise Durdu(durdu, sonuc, kalan)
    return sonuc, kalan


class Durdu(Exception):
    """Kredi/anahtar sorunu: çalıştırma durdu; o ana kadarki sonuç ve bekleyenler taşınır."""

    def __init__(self, mesaj, sonuc, kalan):
        super().__init__(mesaj)
        self.sonuc, self.kalan = sonuc, kalan


# --- toplu kip (Message Batches API: yarı fiyat)

def _ozel_kimlik(hafta, kimlik, tur):
    return f'h{hafta}-{kimlik}-{tur}'      # en çok 64 karakter, [a-zA-Z0-9_-]


def _ozel_coz(ozel, hafta):
    m = re.fullmatch(rf'h{hafta}-(\d+-[a-z0-9-]+)-(i|d)', ozel)
    return (m.group(1), m.group(2)) if m else (None, None)


def toplu_bekle(client, kimlik, bitis, etiket):
    while True:
        b = _api(lambda: client.messages.batches.retrieve(kimlik))
        if b.processing_status == 'ended':
            return b
        if time.time() > bitis:
            print(f'  {etiket}: süre doldu, toplu istek {kimlik} sürüyor; sonraki çalıştırma sonuçları ödemeden toplar.', flush=True)
            return None
        c = b.request_counts
        print(f'  {etiket}: işleniyor {c.processing}, biten {c.succeeded + c.errored + c.canceled + c.expired}', flush=True)
        time.sleep(60)


def toplu_sonuclari(client, batch_id, hafta, ctx, sayac, ilk_mesajlar=None, say=True):
    """Sonuçları işler. Döndürür: {kimlik: ('tamam'|'duzelt'|'hata', bilgi)}; 'duzelt' bilgisi (metin, sorunlar)."""
    cikti = {}
    for r in _api(lambda: client.messages.batches.results(batch_id)):
        kimlik, tur = _ozel_coz(r.custom_id, hafta)
        if not kimlik:
            continue
        if (OZETLER / f'{kimlik}-{hafta}.json').exists() and YAZ['ozet'] == OZETLER:
            cikti[kimlik] = ('tamam', 'zaten var')
            continue
        if r.result.type != 'succeeded':
            hata = getattr(getattr(r.result, 'error', None), 'error', None)
            cikti[kimlik] = ('hata', f'toplu istek sonucu: {r.result.type} {getattr(hata, "message", "") or ""}'.strip())
            continue
        yanit = r.result.message
        if say:
            sayac.ekle(yanit.usage, getattr(yanit, 'model', None), toplu=True)
        try:
            metin = yanit_metni(yanit)
        except RuntimeError as exc:
            cikti[kimlik] = ('hata', str(exc))
            continue
        sorunlar, kb = denetle_ve_kaydet(metin, kimlik, ctx)
        if not sorunlar:
            cikti[kimlik] = ('tamam', f'{kb} KB' + (' (düzeltme turunda)' if tur == 'd' else ''))
        elif tur == 'i':
            cikti[kimlik] = ('duzelt', (metin, sorunlar))
        else:
            cikti[kimlik] = ('hata', '; '.join(sorunlar[:8]))
    return cikti


def onceki_toplulari_topla(client, args, ctx, sayac, bitis):
    """Son 48 saatteki toplu istekler: süren varsa biter, bitenlerin bu haftaya ait sonuçları ödenmeden toplanır
    (önceki çalıştırma yarıda kaldıysa aynı özet için yeniden para ödenmez)."""
    sinir = datetime.now(timezone.utc) - timedelta(hours=48)
    toplanan = {}
    for b in _api(lambda: client.messages.batches.list(limit=50)):
        if b.created_at < sinir:
            break
        if b.processing_status in ('in_progress', 'canceling'):
            print(f'Önceki toplu istek {b.id} sürüyor; bitmesi bekleniyor.', flush=True)
            b = toplu_bekle(client, b.id, bitis, 'önceki toplu istek')
            if b is None:
                continue
        if b.processing_status != 'ended' or not b.results_url:
            continue
        for k, (durum, bilgi) in toplu_sonuclari(client, b.id, args.hafta, ctx, sayac, say=False).items():
            if durum == 'tamam' and bilgi != 'zaten var':
                toplanan[k] = bilgi
                print(f'  [tamam] {k}-{args.hafta}: {bilgi} (önceki toplu istekten, yeniden ödenmedi)', flush=True)
    return toplanan


def toplu_uret(client, args, bekleyen, ctx, sayac, bitis):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    sonuc = {'tamam': [], 'hata': []}
    if not args.kuru:
        for k, bilgi in onceki_toplulari_topla(client, args, ctx, sayac, bitis).items():
            if k in bekleyen:
                bekleyen.remove(k)
                sonuc['tamam'].append(k)
    # bütçe: ilk tur + düzeltme turunun beklenen payı (deneme: 3 istekte 1 düzeltme)
    tahmin = sayac.istek_basi(toplu=True) * 1.35
    sigan = max(0, int((args.butce - sayac.maliyet()) // tahmin))
    gonder, kalan = bekleyen[:sigan], bekleyen[sigan:]
    if kalan:
        print(f'Bütçe ({args.butce:.0f} $) tahminen {len(gonder)} derse yetiyor; {len(kalan)} ders sonraki çalıştırmaya kaldı.', flush=True)
    if not gonder:
        return sonuc, kalan
    ilk = {k: {'role': 'user', 'content': istek_metni(k, args.hafta, ctx['tarih'], ctx['yayin'], ctx['dersler'])} for k in gonder}
    if args.kuru:
        for k in gonder:
            durum, not_ = tek_ozet(None, args, k, ctx, sayac, lambda: True)
            sonuc[durum].append(k)
            print(f'  [{durum}] {k}-{args.hafta}: {not_} (prova)', flush=True)
        return sonuc, kalan

    def gonder_bekle(istekler, etiket):
        """Toplu isteği gönderir ve bitmesini bekler; biterse kimliğini, süre dolarsa None döndürür."""
        b = _api(lambda: client.messages.batches.create(requests=istekler))
        print(f'{etiket}: {len(istekler)} istek gönderildi ({b.id})', flush=True)
        return b.id if toplu_bekle(client, b.id, bitis, etiket) is not None else None

    b = gonder_bekle([Request(custom_id=_ozel_kimlik(args.hafta, k, 'i'),
                              params=MessageCreateParamsNonStreaming(**istek_parametreleri(args, [ilk[k]], True))) for k in gonder], '1. tur')
    if b is None:
        return sonuc, kalan + [k for k in gonder]
    ilk_tur = toplu_sonuclari(client, b, args.hafta, ctx, sayac)
    duzelt = {}
    for k in gonder:
        durum, bilgi = ilk_tur.get(k, ('hata', 'sonuç yok'))
        if durum == 'duzelt':
            duzelt[k] = bilgi
            print(f'  [düzeltilecek] {k}-{args.hafta}: {"; ".join(bilgi[1][:3])}', flush=True)
        else:
            sonuc[durum].append(k)
            print(f'  [{durum}] {k}-{args.hafta}: {bilgi}', flush=True)
    if duzelt:
        if sayac.maliyet() + len(duzelt) * sayac.istek_basi(toplu=True) > args.butce * 1.1:
            for k in duzelt:
                sonuc['hata'].append(k)
                print(f'  [hata] {k}-{args.hafta}: bütçe doldu; düzeltme turu yapılmadı', flush=True)
        else:
            b = gonder_bekle([Request(custom_id=_ozel_kimlik(args.hafta, k, 'd'),
                                      params=MessageCreateParamsNonStreaming(**istek_parametreleri(args, duzeltme_mesajlari(ilk[k], *duzelt[k]), True)))
                              for k in duzelt], '2. tur (düzeltme)')
            ikinci = toplu_sonuclari(client, b, args.hafta, ctx, sayac) if b else {}
            for k in duzelt:
                durum, bilgi = ikinci.get(k, ('hata', 'düzeltme turu sonucu yok (süre doldu ya da istek hata verdi)'))
                durum = 'hata' if durum == 'duzelt' else durum
                bilgi = '; '.join(bilgi[1][:8]) if isinstance(bilgi, tuple) else bilgi
                sonuc[durum].append(k)
                print(f'  [{durum}] {k}-{args.hafta}: {bilgi}', flush=True)
    return sonuc, kalan


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--hafta', type=int, help='üretilecek hafta numarası (planlardaki "no")')
    ap.add_argument('--dersler', help='virgülle ayrılmış sınıf-ders kimlikleri (boşsa hepsi)')
    ap.add_argument('--model', default=VARSAYILAN_MODEL, choices=sorted(ISTEK_TAHMINI), help=f'varsayılan {VARSAYILAN_MODEL}; daha ucuz: claude-sonnet-5-5')
    ap.add_argument('--caba', default='high', choices=['low', 'medium', 'high', 'xhigh'], help='düşünme derinliği (output_config.effort)')
    ap.add_argument('--toplu', action='store_true', help='Message Batches API ile yarı fiyatına üret (sonuç genelde bir saat içinde)')
    ap.add_argument('--paralel', type=int, default=4, help='anlık kipte aynı anda açık istek sayısı (429 alırsanız düşürün)')
    ap.add_argument('--butce', type=float, default=60.0, help='USD; tahmini harcama + açık işlerin payı bunu aşacaksa yeni istek açılmaz')
    ap.add_argument('--sure-dk', type=float, default=0, help='bu kadar dakika sonra yeni istek açma (0 = sınırsız)')
    ap.add_argument('--kuru', action='store_true', help="API çağırmadan prova: önceki haftayı kopyalar, geçici klasöre yazar")
    ap.add_argument('--kuyruk-baslangici', action='store_true', help='sosyal kuyruğa eklenecek ilk saati yazdır ve çık')
    ap.add_argument('--yayin-hazirla', metavar='LISTE', help='sayfaları derle ve denetle; listedeki yeni özetlerden denetime takılanları ayıkla')
    args = ap.parse_args()

    if args.kuyruk_baslangici:
        print(kuyruk_baslangici())
        return
    if args.yayin_hazirla:
        sys.exit(yayin_hazirla(args.yayin_hazirla))
    if not args.hafta:
        ap.error('--hafta gerekli')

    dersler = dersler_sozlugu()
    kimlikler = [k.strip() for k in args.dersler.split(',') if k.strip()] if args.dersler else ozet_kimlikleri()
    bilinmeyen = [k for k in kimlikler if '-' not in k or k.split('-', 1)[1] not in dersler]
    if bilinmeyen:
        ap.error(f'tanımsız ders: {bilinmeyen}')
    tarih, yayin = hafta_tarihi(args.hafta, ozet_kimlikleri())
    bekleyen = [k for k in kimlikler if not (OZETLER / f'{k}-{args.hafta}.json').exists()]
    plansiz = [k for k in bekleyen if not plan_satiri(k, args.hafta)]
    print(f'{args.hafta}. hafta ({tarih}) · {len(kimlikler)} ders, {len(bekleyen)} üretilecek · model {args.model} · çaba {args.caba} · '
          f'{"toplu (yarı fiyat)" if args.toplu else "anlık"}' + (f' · plan dosyası olmayan: {", ".join(plansiz)}' if plansiz else ''), flush=True)
    if not bekleyen:
        return
    if args.kuru:
        gecici = Path(tempfile.mkdtemp(prefix='ozet-prova-'))
        for ad in YAZ:
            YAZ[ad] = gecici / ad
            YAZ[ad].mkdir()
        print(f'Prova: dosyalar {gecici} klasörüne yazılıyor (depoya dokunulmaz).')

    client = None
    if not args.kuru:
        import anthropic
        client = anthropic.Anthropic(max_retries=6)
    ctx = {'e': _yukle('ozet_uret_api', ARACLAR / 'ozet_uret.py').e, 'sayfa': SayfaDenetci(dersler),
           'hafta': args.hafta, 'tarih': tarih, 'yayin': yayin, 'dersler': dersler}
    sayac = Sayac(args.model)
    basla = time.time()
    bitis = basla + args.sure_dk * 60 if args.sure_dk else float('inf')
    durdu = None
    try:
        if args.toplu:
            sonuc, kalan = toplu_uret(client, args, list(bekleyen), ctx, sayac, bitis)
        else:
            sonuc, kalan = anlik_uret(client, args, list(bekleyen), ctx, sayac, bitis)
    except Durdu as exc:               # anlık kip: kredi/anahtar sorunu, açık işler bitti
        durdu, sonuc, kalan = str(exc), exc.sonuc, exc.kalan
    except SystemExit as exc:          # toplu kip: yazılmış dosyalar korunur, özet yine basılır
        durdu = str(exc)
        sonuc = {'tamam': [], 'hata': []}
        kalan = [k for k in bekleyen if not (YAZ['ozet'] / f'{k}-{args.hafta}.json').exists()]
    yazilan = len([k for k in bekleyen if (YAZ['ozet'] / f'{k}-{args.hafta}.json').exists()])
    print(f'\n{yazilan} özet yazıldı, {len(sonuc["hata"])} hata, {len(kalan)} ders bekliyor · {(time.time() - basla) / 60:.0f} dk')
    if durdu:
        print(f'DURDU: {durdu}')
    if not args.kuru:
        print(f'Kullanım: {sayac}')
    if sonuc['hata']:
        print('Hatalı dersler (aynı hafta yeniden çalıştırılınca tekrar denenir): ' + ', '.join(sonuc['hata']))
    if kalan:
        print('Bekleyen dersler (bütçe ya da süre doldu): ' + ', '.join(kalan))
    sys.exit(1 if durdu or sonuc['hata'] or kalan else 0)


if __name__ == '__main__':
    main()
