#!/usr/bin/env python3
"""Haftalık konu özetlerini Claude API ile üretir (Max planının aylık API kredisiyle çalışır).

Her sınıf-ders için bir istek atar; model araclar/ozetler/<sinif>-<ders>-<hafta>.json dosyasını
sitenin kanonik şemasında yazar. Araç çıktıyı yayın denetimiyle aynı kurallarla sınar, hatalıysa
hataları modele geri verip bir kez daha dener, sonra:
  - araclar/gorseller/<ad>-<hafta>.py   görsel modülü (GORSELLER + uygula)
  - araclar/sosyal/bilgi-<sinif>-<kısa ders>-<hafta>.json   sosyal medya bilgi kartı
dosyalarını üretir. Var olan özetler atlanır; yarıda kalan bir çalıştırma aynı komutla sürdürülür.

Kaynaklar: public/veri/gunluk-plan/<plan>.json (haftanın ünite/konu/çıktıları) ve önceki haftaların
özetleri (üslup ve süreklilik). Lise İngilizce gibi plan dosyası olmayan derslerde yalnız önceki
haftalar kullanılır.

Kullanım:
  export ANTHROPIC_API_KEY=...            # console.anthropic.com → API Keys (KURULUM.md)
  python3 araclar/ozet_api_uret.py --hafta 15                      # 103 dersin tamamı
  python3 araclar/ozet_api_uret.py --hafta 15 --dersler 7-matematik,5-fen-bilimleri
  python3 araclar/ozet_api_uret.py --hafta 15 --model claude-sonnet-5-5 --butce 30
  python3 araclar/ozet_api_uret.py --hafta 15 --kuru               # API'siz prova (14. haftayı kopyalar)
  python3 araclar/ozet_api_uret.py --kuyruk-baslangici             # sosyal kuyruk için sıradaki saat
Sonrasında: python3 araclar/yayin_denetle.py --onar && python3 araclar/sosyal_gorsel.py --kuyruk <saat>
"""
import argparse
import importlib.util
import json
import re
import sys
import threading
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
PUBLIC = KOK / 'public'
OZETLER = ARACLAR / 'ozetler'
GORSELLER = ARACLAR / 'gorseller'
SOSYAL = ARACLAR / 'sosyal'
PLANLAR = PUBLIC / 'veri' / 'gunluk-plan'

VARSAYILAN_MODEL = 'claude-opus-5-5'
# USD / 1M jeton: (girdi, çıktı, önbellek yazma, önbellek okuma)
FIYAT = {
    'claude-opus-5-5': (4.0, 20.0, 5.0, 0.20),
    'claude-sonnet-5-5': (2.0, 10.0, 2.5, 0.20),
    'claude-haiku-5-5': (0.10, 0.50, 0.125, 0.01),
}
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

# Birden çok plan dosyası olan ya da adı plan adıyla birebir örtüşmeyen dersler
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
OZEL_HAFTA = re.compile(r'ara tatil|yarıyıl|yariyil|dönem sonu|sene sonu|bayram', re.I)

ATIF_RE = re.compile(r"\b(ders kitab|MEB kitab|kitapta\b|kitaptaki|kitaba göre|kitabın|ünitede|özgün (anlam )?özet|bu satırda|kaynak notu)", re.I)
GOSTERIM = ('koyu', 'us', 'alt', 'kesir', 'kok', 'ar', 'uzunluk', 'aci', 'olcu', 'dogru', 'vektor', 'devir', 'isin', 'parca', 'formul', 'vurgu', 'renk', 'egik', 'i')
KUTU_TURLERI = ('bilgi', 'dikkat', 'kural', 'tanim', 'ipucu', 'hatirla')
ZORUNLU = ('sinif', 'ders', 'hafta', 'tarih', 'yayin_tarihi', 'unite', 'konu', 'ciktilar', 'giris', 'bolumler', 'ornekler', 'etkinlikler', 'ozet')

SISTEM = """Sen derskutusu.com için haftalık konu özeti yazan deneyimli bir Türk öğretmen ve içerik editörüsün. Site, Türkiye Yüzyılı Maarif Modeli (MEB 2026-2027) programına göre 5-12. sınıf öğrencilerine ücretsiz, özgün ve etkileşimli konu özetleri sunar. Görevin: verilen sınıf, ders ve hafta için sitenin kanonik JSON şemasında TEK bir özet dosyası yazmak.

ÇIKTI BİÇİMİ
- Yanıtın yalnız geçerli bir JSON nesnesi olsun: açıklama, selamlama, kod çiti (```), Markdown yok. İlk karakter { ve son karakter } olmalı.
- Türkçe karakterleri doğrudan yaz (\\u kaçışı kullanma). Dizelerde satır sonu için \\n kullanılabilir.
- Hedef uzunluk 38-55 KB (önceki haftaların dosyalarıyla aynı derinlik). Kısa geçiştirme yok; her bölüm ders kitabı düzeyinde dolu olsun.

ŞEMA (alan adları birebir böyle)
{
 "ad": "<sinif>-<ders>-<hafta>", "sinif": <tam sayı>, "ders": "<ders kodu>", "ders_adi": "<ders adı>", "hafta": <tam sayı>,
 "tarih": "<verilen>", "yayin_tarihi": "<verilen YYYY-AA-GG>",
 "unite": "...", "konu": "...",
 "ciktilar": ["MEB kodlu öğrenme çıktısı/süreç bileşeni cümleleri", 2-4 madde],
 "giris": "Haftanın kapsamını 2-3 cümlede sıcak bir dille anlatan paragraf ({koyu:...} vurguları olabilir)",
 "ozet": ["Haftanın en önemli 5-6 kazanımı; her madde tek cümle, {koyu:Başlık:} ile başlayabilir"],
 "bolumler": [ 6 bölüm; her biri:
   {"baslik": "...",
    "metin": ["2-3 dolu paragraf; kavramlar {koyu:...} ile vurgulanır"],
    "tablo": {"basliklar": ["...", "..."], "satirlar": [["...", "..."], ...]}   (isteğe bağlı, bölümlerin çoğunda olsun)
    "kutular": [{"tur": "bilgi|dikkat|kural|tanim|ipucu|hatirla", "baslik": "...", "metin": "..."}]  (1-2 kutu)
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

GÖRSELLER
- 6 bölümün 6'sında da "gorsel" olsun: geçerli, kendi içinde tam XML olan SVG (xmlns ve viewBox şart; & için &amp;, < için &lt; yaz; CSS/script yok; dış dosya yok).
- Genişlik 700-900, yükseklik 240-420 birim; açık arka plan (#f8fafc) ve yuvarlatılmış kutular; yazılar 10-16 punto; şema, akış, zaman çizelgesi, karşılaştırma kutuları, sayı doğrusu, grafik gibi konuya özgü görseller. Yazılar Türkçe (İngilizce dersinde İngilizce olabilir; Arapça dersinde Arapça harf kullanma, çeviri yazı kullan).
- SVG içinde √ ∛ ∜ karakterleri olmasın; kök için "karekök" yaz ya da metin alanlarındaki {kok:...} gösterimini kullan.

METİN GÖSTERİMİ (site bu işaretleri HTML'e çevirir; başka süslü parantezli gösterim kullanma)
- {koyu:metin} kalın; {us:x|2} üs (x²); {alt:H|2} alt indis (H₂); {kesir:pay|payda} kesir (pay ve paydada | olmasın); {kok:ifade} karekök, {kok:ifade|3} küp kök; {uzunluk:AB} |AB| (mutlak değer/uzunluk; buraya {kesir} içinde ihtiyaç duyulan | için de bu kullanılır); {ar:عربي} Arapça (yalnız Arapça/Kur'an/Mesleki Arapça derslerinde).
- √ ∛ ∜ karakterlerini ve LaTeX'i ($...$, \\frac) asla kullanma. Çarpma için × veya ·, bölme için ÷, eksi için − kullanılabilir.
- Şu kelime ve kalıplar hiçbir alanda geçmesin (yayın denetimi reddeder): "ders kitabı/kitabı/kitabın/kitabının" ile başlayan atıflar, "MEB kitabı", "kitapta", "kitaptaki", "kitaba göre", "kitabın", "ünitede" (bunun yerine "bu ünite kapsamında" de), "özgün özet", "bu satırda", "kaynak notu". Metin kitaptan alıntı değil, özgün anlatım olmalı.

İÇERİK İLKELERİ
- Konu, verilen MEB günlük/yıllık planındaki ünite-konu-öğrenme çıktısına ve o haftanın süreç bileşenlerine tam uyar. Plan satırı bir önceki haftayla aynı konuyu gösteriyorsa konunun önceki haftalarda işlenmemiş kalan alt başlıklarını, uygulamalarını ve pekiştirmelerini işle; önceki haftanın bölüm başlıklarını tekrarlama. Plan satırında konu boşsa ünitenin ders kitabı sırasındaki bir sonraki konusunu seç. Plan verilmemişse önceki haftalardan devam eden temanın sırasındaki konuyu seç.
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


def plan_dosyasi(kimlik):
    if kimlik in PLAN_ESLEME:
        return PLANLAR / f'{PLAN_ESLEME[kimlik]}-gunluk-plan-2026-2027.json'
    sinif, ders = kimlik.split('-', 1)
    adaylar = sorted(PLANLAR.glob(f'{sinif}-sinif-{ders}-gunluk-plan-*.json'))
    return adaylar[0] if len(adaylar) == 1 else None


def plan_satiri(kimlik, hafta):
    """Planın o haftasındaki alanlar: {hafta, tarih, unite, konu, ciktilar, surec, sure} ya da None."""
    p = plan_dosyasi(kimlik)
    if not p or not p.exists():
        return None
    plan = json.loads(p.read_text(encoding='utf-8'))
    h = next((x for x in plan.get('haftalar', []) if x.get('no') == hafta), None)
    if not h:
        return None
    alanlar = {k: v for _, al in h.get('bolumler', []) for k, v in al}
    return {'hafta': h.get('hafta', ''), 'tarih': h.get('tarih', ''), 'unite': alanlar.get('Ünite / Tema', ''),
            'konu': alanlar.get('Konu (içerik çerçevesi)', ''), 'ciktilar': alanlar.get('Öğrenme çıktıları', ''),
            'surec': alanlar.get('Süreç bileşenleri / açıklamalar', ''), 'sure': alanlar.get('Süre', '')}


def hafta_tarihi(hafta, kimlikler):
    """Haftanın pazartesi tarihi (planların çoğunluğuna göre) → ('28 Aralık 2026 - 1 Ocak 2027', '2026-12-28')."""
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


def dogrula(d, kimlik, hafta, e_fonk):
    """Yayın denetimi (yayin_denetle.py) ve sayfa üreticisiyle aynı kurallar; sorun listesi döndürür."""
    h = []
    for a in ZORUNLU:
        if a not in d:
            h.append(f'zorunlu alan eksik: {a}')
    if h:
        return h
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
        if not isinstance(b.get('metin'), list) or len(b['metin']) < 2:
            h.append(f'bolumler[{i}]: metin en az 2 paragraflık liste olmalı')
        g = b.get('gorsel')
        if g:
            gorselli += 1
            if not isinstance(g, str) or not g.lstrip().startswith('<svg'):
                h.append(f'bolumler[{i}].gorsel: <svg ile başlayan dize olmalı')
            else:
                try:
                    ET.fromstring(g)
                except ET.ParseError as exc:
                    h.append(f'bolumler[{i}].gorsel geçersiz XML: {exc}')
                if 'viewBox' not in g:
                    h.append(f'bolumler[{i}].gorsel: viewBox yok')
                if re.search('[√∛∜]', g):
                    h.append(f'bolumler[{i}].gorsel: düz kök işareti')
        for k in b.get('kutular', []) + ([b['kutu']] if b.get('kutu') else []):
            if not k.get('metin'):
                h.append(f'bolumler[{i}]: kutu metni eksik')
        t = b.get('tablo')
        if t and (not t.get('satirlar') or not t.get('basliklar')):
            h.append(f'bolumler[{i}].tablo: basliklar ve satirlar gerekli')
    if gorselli < 4:
        h.append(f'görselli bölüm sayısı {gorselli} (6 olmalı, en az 4)')
    if not 4 <= len(d['ozet']) <= 7 or not all(isinstance(x, str) for x in d['ozet']):
        h.append('ozet 5-6 dizelik liste olmalı')
    if not 1 <= len(d['ciktilar']) <= 6:
        h.append('ciktilar 2-4 maddelik liste olmalı')
    for yol, s in _dizeler(d):
        if '<svg' in s:
            continue
        m = ATIF_RE.search(s)
        if m:
            h.append(f"{yol}: yasak ifade '{m.group(0)}'")
        if re.search('[√∛∜]', s):
            h.append(f'{yol}: düz kök işareti; {{kok:...}} kullan')
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
        h.append(f'içerik {boyut} bayt: çok kısa (hedef 38-55 KB); bölümleri, örnekleri ve açıklamaları genişlet')
    return h


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
    (GORSELLER / f'{ad}.py').write_text(icerik, encoding='utf-8')


_US = str.maketrans('0123456789+-=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ')
_ALT = str.maketrans('0123456789+-=()', '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎')


def duz_metin(s):
    """Site gösterimlerini sosyal kart için düz metne çevirir; Arapça harfleri kaldırır."""
    s = re.sub(r'\{ar:[^{}]*\}', '', s)
    s = re.sub(r'\{us:([^{}|]+)\|([^{}]+)\}', lambda m: m.group(1) + m.group(2).translate(_US), s)
    s = re.sub(r'\{alt:([^{}|]+)\|([^{}]+)\}', lambda m: m.group(1) + m.group(2).translate(_ALT), s)
    s = re.sub(r'\{kesir:([^{}|]+)\|([^{}]+)\}', r'\1/\2', s)
    s = re.sub(r'\{kok:([^{}|]+)(?:\|(\d+))?\}', lambda m: ('küp kök' if m.group(2) == '3' else 'karekök') + f'({m.group(1)})', s)
    s = re.sub(r'\{uzunluk:([^{}]+)\}', r'|\1|', s)
    s = re.sub(r'\{[a-z]+:([^{}]*)\}', r'\1', s)
    s = re.sub(r'[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]+', '', s)
    s = re.sub(r'\(\s*\)', '', s)
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
    paragraflar = [kirp(duz_metin(x), 240) for x in d['ozet'][:2]]
    kart = {'ozet': f'{kimlik}-{hafta}', 'baslik': kirp(duz_metin(d['bolumler'][0]['baslik']), 80),
            'paragraflar': paragraflar, 'bilgi': ' '.join(paragraflar)}
    (SOSYAL / f'bilgi-{sinif}-{dosya}-{hafta}.json').write_text(json.dumps(kart, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def kuyruk_baslangici():
    """sosyal/kuyruk.json içindeki son gönderiden bir saat sonrası (ISO, yerel saat)."""
    k = json.loads((KOK / 'sosyal' / 'kuyruk.json').read_text(encoding='utf-8'))
    son = max(g['zaman'] for g in k['gonderiler'])
    t = datetime.fromisoformat(son) + timedelta(hours=1)
    return t.replace(tzinfo=None).isoformat(timespec='minutes')


# ------------------------------------------------------------------ üretim

class Sayac:
    def __init__(self, model):
        self.model = model
        self.kilit = threading.Lock()
        self.girdi = self.cikti = self.onbellek_yaz = self.onbellek_oku = 0
        self.istek = 0

    def ekle(self, kullanim):
        with self.kilit:
            self.istek += 1
            self.girdi += kullanim.input_tokens or 0
            self.cikti += kullanim.output_tokens or 0
            self.onbellek_yaz += getattr(kullanim, 'cache_creation_input_tokens', 0) or 0
            self.onbellek_oku += getattr(kullanim, 'cache_read_input_tokens', 0) or 0

    def maliyet(self):
        g, c, oy, oo = FIYAT.get(self.model, FIYAT[VARSAYILAN_MODEL])
        return (self.girdi * g + self.cikti * c + self.onbellek_yaz * oy + self.onbellek_oku * oo) / 1e6

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


def model_cagir(client, model, caba, mesajlar, sayac):
    import anthropic
    try:
        with client.beta.messages.stream(
            model=model,
            max_tokens=64000,
            system=[{'type': 'text', 'text': SISTEM, 'cache_control': {'type': 'ephemeral'}}],
            messages=mesajlar,
            output_config={'effort': caba},
            betas=['server-side-fallback-2026-07-01'],
            fallbacks='default',
        ) as akis:
            yanit = akis.get_final_message()
    except anthropic.AuthenticationError:
        raise SystemExit('ANTHROPIC_API_KEY geçersiz ya da eksik (KURULUM.md → API kredisi)')
    except anthropic.BadRequestError as exc:
        if 'credit' in str(exc).lower() or 'billing' in str(exc).lower():
            raise SystemExit('API kredisi bitti; platform.claude.com → Settings → Billing sayfasından bakiyeyi kontrol edin. '
                             'Ay başında kredi yenilenince aynı komut kaldığı yerden sürer.')
        raise
    sayac.ekle(yanit.usage)
    if yanit.stop_reason == 'refusal':
        raise RuntimeError(f'model isteği reddetti ({getattr(yanit.stop_details, "category", None)})')
    if yanit.stop_reason == 'max_tokens':
        raise RuntimeError('yanıt max_tokens sınırında kesildi')
    metin = ''.join(b.text for b in yanit.content if b.type == 'text')
    return metin, yanit


def tek_ozet(client, args, kimlik, tarih, yayin, dersler, e_fonk, sayac, kuru=False):
    hafta = args.hafta
    hedef = OZETLER / f'{kimlik}-{hafta}.json'
    satir = plan_satiri(kimlik, hafta)
    if satir and OZEL_HAFTA.search((satir.get('unite') or '') + ' ' + (satir.get('konu') or '')):
        return 'atlandı', f'planda özel hafta: {satir.get("unite")}'
    mesajlar = [{'role': 'user', 'content': istek_metni(kimlik, hafta, tarih, yayin, dersler)}]
    son_hata = ''
    for deneme in range(1, 3):
        if kuru:
            d = onceki_ozetler(kimlik, hafta, 1)[0]
            d['hafta'] = hafta
            metin = json.dumps(d, ensure_ascii=False)
        else:
            metin, _ = model_cagir(client, args.model, args.caba, mesajlar, sayac)
        try:
            d = json_ayikla(metin)
        except (ValueError, json.JSONDecodeError) as exc:
            son_hata = f'JSON çözülemedi: {exc}'
            sorunlar = [son_hata]
        else:
            sorunlar = dogrula(d, kimlik, hafta, e_fonk)
        if not sorunlar:
            d = normalize(d, kimlik, hafta, tarih, yayin, dersler)
            hedef.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            gorsel_modulu_yaz(d, f'{kimlik}-{hafta}')
            sosyal_karti_yaz(d, kimlik, hafta)
            return 'tamam', f'{len(json.dumps(d, ensure_ascii=False).encode()) // 1024} KB' + (f', {deneme}. denemede' if deneme > 1 else '')
        son_hata = '; '.join(sorunlar[:12])
        if kuru:
            break
        mesajlar += [{'role': 'assistant', 'content': metin},
                     {'role': 'user', 'content': 'Yanıt yayın denetiminden geçmedi. Şu sorunları gidererek dosyanın TAMAMINI yeniden, yalnız JSON olarak yaz:\n- ' + '\n- '.join(sorunlar[:25])}]
    return 'hata', son_hata


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--hafta', type=int, help='üretilecek hafta numarası (planlardaki "no")')
    ap.add_argument('--dersler', help='virgülle ayrılmış sınıf-ders kimlikleri (boşsa hepsi)')
    ap.add_argument('--model', default=VARSAYILAN_MODEL, help=f'varsayılan {VARSAYILAN_MODEL}; daha ucuz: claude-sonnet-5-5')
    ap.add_argument('--caba', default='high', choices=['low', 'medium', 'high', 'xhigh'], help='düşünme derinliği (output_config.effort)')
    ap.add_argument('--paralel', type=int, default=3, help='aynı anda açık istek sayısı (429 alırsanız düşürün)')
    ap.add_argument('--butce', type=float, default=60.0, help='USD; tahmini harcama bunu aşınca yeni istek açılmaz')
    ap.add_argument('--kuru', action='store_true', help='API çağırmadan prova: önceki haftayı kopyalar, son işlemleri sınar')
    ap.add_argument('--kuyruk-baslangici', action='store_true', help='sosyal kuyruğa eklenecek ilk saati yazdır ve çık')
    args = ap.parse_args()

    if args.kuyruk_baslangici:
        print(kuyruk_baslangici())
        return
    if not args.hafta:
        ap.error('--hafta gerekli')

    dersler = dersler_sozlugu()
    kimlikler = args.dersler.split(',') if args.dersler else ozet_kimlikleri()
    bilinmeyen = [k for k in kimlikler if k.split('-', 1)[1] not in dersler]
    if bilinmeyen:
        ap.error(f'tanımsız ders: {bilinmeyen}')
    tarih, yayin = hafta_tarihi(args.hafta, ozet_kimlikleri())
    bekleyen = [k for k in kimlikler if not (OZETLER / f'{k}-{args.hafta}.json').exists()]
    print(f'{args.hafta}. hafta ({tarih}) · {len(kimlikler)} ders, {len(bekleyen)} üretilecek · model {args.model} · çaba {args.caba}')
    if not bekleyen:
        return

    client = None
    if not args.kuru:
        import anthropic
        client = anthropic.Anthropic(max_retries=6)
    e_fonk = _yukle('ozet_uret_api', ARACLAR / 'ozet_uret.py').e
    sayac = Sayac(args.model)
    sonuc = {'tamam': [], 'hata': [], 'atlandı': []}
    basla = time.time()

    with ThreadPoolExecutor(max_workers=max(1, args.paralel)) as havuz:
        isler = {}
        sira = list(bekleyen)
        while sira or isler:
            while sira and len(isler) < max(1, args.paralel) and sayac.maliyet() < args.butce:
                k = sira.pop(0)
                isler[havuz.submit(tek_ozet, client, args, k, tarih, yayin, dersler, e_fonk, sayac, args.kuru)] = k
            if not isler:
                break
            biten = next(as_completed(list(isler)))
            k = isler.pop(biten)
            try:
                durum, not_ = biten.result()
            except Exception as exc:  # ağ/API hatası: diğer dersler sürsün
                durum, not_ = 'hata', f'{type(exc).__name__}: {exc}'
            sonuc[durum].append(k)
            print(f'  [{durum}] {k}-{args.hafta}: {not_}', flush=True)
    if sira:
        print(f'Bütçe ({args.butce:.0f} $) doldu; {len(sira)} ders bekliyor: aynı komut kaldığı yerden sürer.')
    print(f'\n{len(sonuc["tamam"])} özet üretildi, {len(sonuc["hata"])} hata, {len(sonuc["atlandı"])} atlandı · {(time.time() - basla) / 60:.0f} dk')
    if not args.kuru:
        print(f'Kullanım: {sayac}')
    if sonuc['hata']:
        print('Hatalı dersler (yeniden deneyin): ' + ', '.join(sonuc['hata']))
    print('Sonraki adım: python3 araclar/yayin_denetle.py --onar && python3 araclar/sosyal_gorsel.py --kuyruk "$(python3 araclar/ozet_api_uret.py --kuyruk-baslangici)"')
    sys.exit(1 if sonuc['hata'] or sira else 0)


if __name__ == '__main__':
    main()
