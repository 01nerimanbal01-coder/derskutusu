#!/usr/bin/env python3
"""Haftalık çalışma kâğıtlarını Claude API ile üretir (özet botunun kardeşi; ozet_api_uret.py'nin parçalarını kullanır).

Birim: bir çalışma kâğıdı = <sinif>-<ders>-<hafta>. Eksik: araclar/ozetler'de özeti olup araclar/calisma'da kâğıdı olmayan.
Model kâğıdı tek JSON olarak yazar (calisma_uret.py şeması + "gorseller": {soru sırası: SVG}); bot sinif, ders, hafta,
tarih, yayin_tarihi ve ciktilar alanlarını plandan doldurur, görselleri veri modülüne (GORSELLER + sabit uygula) yazar:
  - araclar/calisma/<ad>.json
  - araclar/calisma_gorseller/<ad>.py
Denetim sırası (her kâğıt):
  1. şema ve tür kuralları, SVG XML geçerliliği, atıf/dış gönderme ifadeleri, yatay kesir, önceki haftalarla 5-gram örtüşme;
  2. calisma_uret.py ile geçici klasöre basım: iki PDF (cevapsız, cevaplı) tam ikişer sayfa, 2. sayfada KISA boşluk yok,
     cevaplı sürümde kutusundan taşan cevap yok (TAŞMA 0);
  3. gözle denetim ("g" isteği): basılan dört sayfanın PNG'si Claude'a gösterilir, yerleşim/görsel sorunu sorulur.
  Mekanik denetime ya da gözle denetimde ciddi bir soruna takılan kâğıda bir düzeltme turu ("d") yapılır.
Gözle denetimi bekleyen kâğıt araclar/veri/calisma_taslak/<ad>.json'da durur (yayımlanmaz).

Kipler:
  --toplu  Message Batches API (yarı fiyat). Gönderilen istekler araclar/veri/calisma_toplu_durum.json'da; custom_id
           'ck-h<hafta>-<sinif>-<ders>-<i|d|g>'. Süren istekteki ya da taslağı olan kâğıt yeniden gönderilmez.
  --topla  Yalnız toplayıcı (iş akışı iki saatte bir): biten sonuçları işler, g ve d turlarını gönderir.
  --kuru   API'siz prova: önceki haftanın kâğıdını bu haftanınmış gibi denetler ve basar; geçici klasöre yazar.
  (yok)    Anlık: istekler hemen yanıtlanır.

Kullanım:
  python3 araclar/calisma_api_uret.py --haftalar 9-16 --liste                 # eksik kâğıtlar
  python3 araclar/calisma_api_uret.py --haftalar 9 --siniflar 7 --dersler matematik --en-cok 1 --kuru
  python3 araclar/calisma_api_uret.py --haftalar 9-12 --siniflar 5-8 --toplu --butce 20
  python3 araclar/calisma_api_uret.py --topla
"""
import argparse
import base64
import copy
import functools
import html
import importlib
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
if str(ARACLAR) not in sys.path:
    sys.path.insert(0, str(ARACLAR))
import ozet_api_uret as oz  # noqa: E402  (istemci, JSON onarımı, sayaç, bütçe, toplu gönder/bekle, durum dosyası)

KOK = ARACLAR.parent
PUBLIC = KOK / 'public'
OZETLER = oz.OZETLER
CALISMA = ARACLAR / 'calisma'
YAZ = {'kagit': CALISMA, 'gorsel': ARACLAR / 'calisma_gorseller', 'taslak': ARACLAR / 'veri' / 'calisma_taslak'}  # --kuru geçici klasöre çevirir
DURUM = ARACLAR / 'veri' / 'calisma_toplu_durum.json'
# Özet botunun durum işlevleri (durum, durum_kaydet, toplu_gonder) bu süreçte çalışma kâğıdı kayıt dosyasını kullanır.
oz.DURUM, oz._DURUM = DURUM, None

VARSAYILAN_MODEL = oz.VARSAYILAN_MODEL
# Bir kâğıdın ilk isteğinin anlık fiyatla tahmini (USD); gözle denetim ve olası düzeltme payı bütçede ayrıca sayılır.
ISTEK_TAHMINI = {'claude-opus-5-5': 0.80, 'claude-sonnet-5-5': 0.40}
GOZ_PAYI = 0.08          # bir g isteği (4 sayfa PNG) yaklaşık
TURLER = ('coktan', 'dy', 'bosluk', 'eslestir', 'kisa', 'acik', 'tablo', 'siralama', 'sifre', 'kavram')
DUZEYLER = ('hatirla', 'uygula', 'ust')
ESKI_DUZEY = {'kavrama': 'uygula', 'kavra': 'uygula', 'analiz': 'ust', 'degerlendir': 'ust'}   # yalnız --kuru provası
AD_RE = re.compile(r'(\d+)-([a-z0-9]+(?:-[a-z0-9]+)*)-(\d+)')
OZEL_RE = re.compile(r'ck-h(\d+)-(\d+-[a-z0-9-]+?)-([idg])')
DIS_GONDERME = re.compile(r'(konu özet|özette|özetteki|yukarıdaki metin|önceki soru|bir önceki soruda|aşağıdaki metne göre)', re.I)
YATAY_KESIR = re.compile(r'(?<![\w/.,:-])\d{1,3}/\d{1,3}(?![\d/]|[\s.]\d{3})|[½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞]')
GOSTERIM_AD = re.compile(r'\{([a-z]+):')
KISA_MM = 45             # calisma_uret.py "KISA: soru eklenmeli" eşiği
ORTUSME_SORU, ORTUSME_KAGIT = 0.5, 0.2

SISTEM = """Sen derskutusu.com için haftalık ÇALIŞMA KÂĞIDI yazan deneyimli bir Türk öğretmen ve ölçme-değerlendirme editörüsün. Site, Türkiye Yüzyılı Maarif Modeli (MEB 2026-2027) programına göre 5-12. sınıf öğrencilerine ücretsiz, özgün, yazdırılabilir çalışma kâğıtları sunar. Kâğıt A4'te tam İKİ sayfa olur; cevapsız ve cevaplı iki PDF'e basılır.

Görevin: verilen sınıf, ders ve hafta için TEK bir çalışma kâğıdı JSON'u yazmak. Kaynak: o haftanın plan satırı (öğrenme çıktıları) ve sitede yayımlı konu özeti. Önceki haftanın kâğıdı yalnız biçim ve düzey örneğidir.

ÇIKTI
Yalnız tek bir JSON nesnesi yaz; kod çiti (```), açıklama, yorum yok. Alanlar:
{"konu": "kısa kâğıt başlığı (düz metin, en çok 110 karakter)",
 "hatirla": ["3-4 kısa bilgi maddesi (her biri en çok 190 karakter)"],
 "sorular": [12-14 soru],
 "gorseller": {"<sorunun 1 tabanlı sırası>": "<svg …>…</svg>"}}
sinif, ders, hafta, tarih, yayin_tarihi, ciktilar alanlarını YAZMA; onları araç plandan doldurur. Python ya da başka kod yazma; görseller yalnız "gorseller" içindeki SVG dizeleridir.

SORU ORTAK ALANLARI: {"tur", "duzey": "hatirla"|"uygula"|"ust", "genislik": "yarim"|"tam" (yoksa yarım), "soru": "soru kökü"}
TÜRLER
- coktan   {"secenekler": [4 şık; 9-12. sınıfta 5 şık olabilir], "dogru": 0 tabanlı doğru şık sırası}. Doğru şıklar kâğıt içinde farklı konumlara dağılsın; çeldiriciler makul olsun; "hepsi/hiçbiri" kullanma.
- dy       {"ifadeler": [{"metin", "dogru": true|false}] 4-6 ifade; ikisi de bulunsun}
- bosluk   {"cumleler": [{"metin": "… ___ …" (tam bir "___"), "cevap"}] 3-5 cümle, "fazla": [1-2 çeldirici kelime]}
- eslestir {"ciftler": [["sol", "sağ"]] 4-6 çift; sağ öğeler birbirinden farklı}
- kisa     {"cevap", "satir": 1-3}      acik {"cevap": "örnek yanıt", "satir": 2-5}
- tablo    {"basliklar": [2-4], "satirlar": [[hücre | {"b": "cevap"}]] her satır başlık sayısı kadar hücre; en az iki boş hücre}
- siralama {"ogeler": [4-6 öğe, DOĞRU sırada]} (araç karıştırır)
- sifre    {"satirlar": [{"ipucu", "cevap": "TEK KELİME", "anahtar": 0 tabanlı harf sırası}], "sonuc": "anahtar harflerin yukarıdan aşağı okunuşu"}; anahtar harfler Türkçe büyük harfe çevrilmiş cevaplardan alınır ve birleşince tam olarak sonucu verir.
- kavram   {"merkez", "dallar": [4-6 öğe; metin ya da {"b": "cevap", "ipucu": "kısa açıklama"}]}
Bir kâğıtta en az 6 farklı tür; 4-5 coktan; düzeyler dengeli (yaklaşık 4 hatirla, 6 uygula, 3 ust). Uzun tablolar ve geniş görselli sorular "genislik": "tam".

KURALLAR
1. Özgünlük (K039): bütün cümleler, sorular, örnekler, sayılar ve görseller senin; ders kitabından, özetten ya da önceki kâğıtlardan cümle/soru aktarma. Bilgiler programın ve özetin kapsamında, doğru ve güncel olsun.
2. Her soru kendi içinde çözülebilir (K164): çözüm için gereken bütün veri soru kökünde ya da sorunun görselinde bulunur. "özette", "yukarıdaki metin", "önceki soru", "kitapta" gibi dış göndermeler yasak. Görsele dayanan soru görselsiz anlaşılmıyorsa görseli mutlaka ver; görsel cevabı doğrudan ele vermesin.
3. Kesirler dikey (K155): metinde {kesir:pay|payda}; SVG'de pay, yatay çizgi, payda alt alta. "3/4" gibi yatay kesir ve ½ gibi tek karakterlik kesir yazma.
4. Doğal sınav dili: "Aşağıdakilerden hangisi …?", "… boşluklara yazınız.", "… eşleştiriniz." Öğrenciye "sen" ya da "siz" diye tutarlı hitap; ifadeler kısa ve açık. Sınıf düzeyine uygun sözcükler.
5. Ders kitabına, MEB kitabına, üniteye, özete ya da kaynağa atıf yapma ("ders kitabında", "kitaptaki", "ünitede", "kaynak notu" yasak).
6. Kâğıt iki A4 sayfayı dolduracak kadar içerik taşısın ama taşmasın: 12-14 soru, 5-8'i görselli (tablo, şifre ve kavram haritası da görsel sayılır).
SİTE GÖSTERİMİ (metin alanlarında; SVG içinde kullanma): {koyu:metin}, {kesir:a|b}, {us:x|2} (x²), {alt:H|2} (H₂), {kok:x} (√x). Kimya formülü H{alt:2}O biçiminde. Başka süslü parantez kullanma. "konu" düz metindir: gösterim kullanma (sayfa başlığına olduğu gibi basılır); birim üssü gerekiyorsa m², m³ yaz.
GÖRSEL (SVG) KURALLARI
- Geçerli XML: <svg viewBox="0 0 G Y" role="img" aria-label="…"> ile başlar; genişlik G en çok 600, yükseklik Y en çok 260. width/height verme; baskıda yer sınırlı olduğu için style="max-height:24mm" ver (geniş şema en çok 34mm); görseller yatay ve alçak olsun (oran en az 2,5:1). & yerine &amp;; HTML varlığı (&nbsp;) yok.
- Yazılar font-family="Noto Sans, sans-serif", font-size 12-14, Türkçe karakterli; her yazı viewBox içinde kalır, yazılar ve şekiller üst üste binmez.
- Renkler: lacivert #0b2257, mavi #2451d6, turuncu #ee7d12, yeşil #12a150, kırmızı #d63a3a, mor #7c3aed; açık zeminler #e8eefe, #fff1df, #e3f6ea.
- İnsan figürü, yüz, el çizme (K024/K048); dinî konularda canlı tasviri yok. <script>, <image>, <foreignObject>, dış bağlantı yok.
- Görseldeki sayılar ve adlar soru metniyle birebir tutarlı olsun; cevaplanacak bilgi görselde ise soru kökü görsele açıkça gönderme yapsın ("Görseldeki …").
"""

GOZ_SISTEM = """Sen basılı çalışma kâğıtlarını yayından önce gözle denetleyen bir dizgi ve içerik editörüsün. Sana bir çalışma kâğıdının A4 baskı sayfaları PNG olarak gösterilir: önce cevapsız sürümün 2 sayfası, sonra cevaplı sürümün 2 sayfası (cevaplar turuncu yazılır). Yalnız gerçekten görünen sorunları bildir:
- taşan, kesilen, üst üste binen ya da okunmayan yazı veya görsel; görsel içindeki yazının çerçeveden taşması;
- görsel ile soru metni arasında tutarsızlık (sayılar, adlar, etiketler), görsel olmadan çözülemeyen soruda eksik görsel;
- yatay yazılmış kesir (3/4 gibi), insan figürü ya da yüz;
- cevaplı sürümde yanlış ya da eksik görünen cevap, cevap kutusundan taşan cevap;
- sayfa altında büyük boş alan ya da sayfa dışına çıkan içerik.
Zevk ve üslup önerisi, küçük hizalama farkı sorun değildir. Her sorun için soru numarası basılı kâğıttaki numaradır (sayfa geneli için 0). "agirlik": düzeltilmeden yayımlanamayacaksa "ciddi", yoksa "kucuk".
Yalnız JSON yaz, kod çiti yok: {"sorunlar": [{"soru": 3, "agirlik": "ciddi", "sorun": "…"}]}. Sorun yoksa {"sorunlar": []}."""


# ------------------------------------------------------------------ birim ve kaynaklar

def birim_ad(sinif, ders, hafta):
    return f'{sinif}-{ders}-{hafta}'


def ad_coz(ad):
    """'7-matematik-9' → (7, 'matematik', 9); geçersizse None."""
    m = AD_RE.fullmatch(ad or '')
    return (int(m.group(1)), m.group(2), int(m.group(3))) if m else None


def ozel_kimlik(hafta, kimlik, tur):
    cid = f'ck-h{hafta}-{kimlik}-{tur}'
    if tur not in 'idg' or len(cid) > 64 or not re.fullmatch(r'[A-Za-z0-9_-]+', cid):
        raise ValueError(f'geçersiz custom_id: {cid}')
    return cid


def ozel_coz(cid):
    """'ck-h9-7-matematik-i' → (9, '7-matematik', 'i'); başka botun kimliği → (None, None, None)."""
    m = OZEL_RE.fullmatch(cid or '')
    return (int(m.group(1)), m.group(2), m.group(3)) if m else (None, None, None)


def aralik(metin):
    """'9-12,14' → {9, 10, 11, 12, 14}; boşsa None."""
    if not metin or not str(metin).strip():
        return None
    kume = set()
    for parca in str(metin).replace(' ', '').split(','):
        if not parca:
            continue
        m = re.fullmatch(r'(\d+)(?:-(\d+))?', parca)
        if not m:
            raise ValueError(f'geçersiz aralık: {parca}')
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        kume |= set(range(min(a, b), max(a, b) + 1))
    return kume


@functools.lru_cache(maxsize=None)
def plan_satiri(kimlik, hafta):
    return oz.plan_satiri(kimlik, hafta)


def ozet_oku(kimlik, hafta, dizin=None):
    p = (dizin or OZETLER) / f'{kimlik}-{hafta}.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


def plan_tarihi(sinif, ders, hafta, ozet_dizin=None):
    """Sıralama anahtarı: planın o haftasının pazartesisi; plan yoksa özetin yayın tarihi."""
    s = plan_satiri(f'{sinif}-{ders}', hafta)
    if s and re.fullmatch(r'\d{4}-\d{2}-\d{2}', s.get('tarih') or ''):
        return s['tarih']
    o = ozet_oku(f'{sinif}-{ders}', hafta, ozet_dizin) or {}
    return o.get('yayin_tarihi') or '9999'


def eksikler(haftalar=None, siniflar=None, dersler=None, en_cok=0, ozet_dizin=None, kagit_dizin=None):
    """Özeti olup kâğıdı olmayan birimler [(sinif, ders, hafta)], plan tarihine göre sıralı.
    dersler: {'matematik', '7-turkce', …} (ders adı bütün sınıflarda, sınıf-ders yalnız o sınıfta)."""
    ozet_dizin, kagit_dizin = ozet_dizin or OZETLER, kagit_dizin or CALISMA
    liste = []
    for p in ozet_dizin.glob('*.json'):
        c = ad_coz(p.stem)
        if not c:
            continue
        sinif, ders, hafta = c
        if (haftalar and hafta not in haftalar) or (siniflar and sinif not in siniflar):
            continue
        if dersler and ders not in dersler and f'{sinif}-{ders}' not in dersler:
            continue
        if (kagit_dizin / f'{p.stem}.json').exists():
            continue
        liste.append(c)
    liste.sort(key=lambda b: (plan_tarihi(*b, ozet_dizin=ozet_dizin), b[2], b[0], b[1]))
    return liste[:en_cok] if en_cok else liste


KOD_RE = re.compile(r'(?<![\w.])([A-ZÇĞİÖŞÜ]{1,6}(?:\.[A-ZÇĞİÖŞÜ0-9]+)*\.\d+\.\d+)\.?\s*')
CIKTI_SINIR = 480        # kâğıt başlığındaki çıktı metni (yayımlanmış kâğıtlarda ortanca 327, en çok 761 karakter)


def _kisalt(s, sinir):
    return s if len(s) <= sinir else s[:sinir].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'


def ciktilar_al(kimlik, hafta, ozet):
    """Planın o haftasındaki öğrenme çıktıları: kod + başlık (alt maddeler a), b)… atılır). Özetin andığı kodlar varsa
    yalnız onlar; başlık alanı taşmasın diye toplam CIKTI_SINIR karakter. Planda kod yoksa özetin çıktıları."""
    metin = re.sub(r'\s+', ' ', (plan_satiri(kimlik, hafta) or {}).get('ciktilar') or '')
    eslesme = list(KOD_RE.finditer(metin))
    maddeler, gorulen = [], set()
    for i, m in enumerate(eslesme):
        son = eslesme[i + 1].start() if i + 1 < len(eslesme) else len(metin)
        baslik = re.split(r'\s[a-zçğı]\)\s', metin[m.end():son])[0]
        baslik = re.sub(r'\s+[A-ZÇĞİÖŞÜ][\wçğıöşü/ ]{0,30}:\s*$', '', baslik).strip(' .;:-')
        if m.group(1) not in gorulen and baslik:
            gorulen.add(m.group(1))
            maddeler.append((m.group(1), f'{m.group(1)}. {_kisalt(baslik, 150)}'))
    ozet_kod = {m.group(1) for c_ in (ozet or {}).get('ciktilar') or [] for m in KOD_RE.finditer(c_)}
    if ozet_kod & gorulen:
        maddeler = [x for x in maddeler if x[0] in ozet_kod]
    if not maddeler:
        maddeler = [(None, _kisalt(x, 200)) for x in (ozet or {}).get('ciktilar') or []]
    secilen, top = [], 0
    for _, x in maddeler:
        if secilen and top + len(x) > CIKTI_SINIR:
            break
        secilen.append(x)
        top += len(x)
    return secilen


def tarihler(kimlik, hafta, ozet):
    """(etiket, yayin_tarihi): etiket özetten; yayın tarihi plan haftasından önceki cumartesi (yoksa özetinki)."""
    etiket = (ozet or {}).get('tarih') or ''
    s = plan_satiri(kimlik, hafta)
    if s and re.fullmatch(r'\d{4}-\d{2}-\d{2}', s.get('tarih') or ''):
        bas = datetime.strptime(s['tarih'], '%Y-%m-%d')
        if not etiket:
            etiket = oz.hafta_tarihi(hafta, [kimlik])[0]
        return etiket, (bas - timedelta(days=2)).strftime('%Y-%m-%d')
    return etiket, (ozet or {}).get('yayin_tarihi') or datetime.now(timezone.utc).strftime('%Y-%m-%d')


def gorselli_yukle(ad, kagit_dizin=None, gorsel_dizin=None):
    """Yayımlanmış kâğıt + görsel modülü uygulanmış hâli (calisma_uret.py ile aynı yükleme)."""
    kagit_dizin, gorsel_dizin = kagit_dizin or CALISMA, gorsel_dizin or ARACLAR / 'calisma_gorseller'
    o = json.loads((kagit_dizin / f'{ad}.json').read_text(encoding='utf-8'))
    modul = gorsel_dizin / f'{ad}.py'
    if modul.exists():
        spec = importlib.util.spec_from_file_location(f'ck_api_{ad.replace("-", "_")}', modul)
        m = importlib.util.module_from_spec(spec)
        sys.modules.setdefault('ozet_gorsel', importlib.import_module('ozet_gorsel'))
        spec.loader.exec_module(m)
        m.uygula(o)
    return o


SORU_ALANLARI = {'coktan': ('secenekler', 'dogru'), 'dy': ('ifadeler',), 'bosluk': ('cumleler', 'kelimeler', 'fazla'),
                 'eslestir': ('ciftler',), 'kisa': ('cevap', 'satir'), 'acik': ('cevap', 'satir'),
                 'tablo': ('basliklar', 'satirlar'), 'siralama': ('ogeler',), 'sifre': ('satirlar', 'sonuc'),
                 'kavram': ('merkez', 'dallar')}


def api_bicimi(o, svg_sinir=None):
    """Yayımlanmış kâğıt → modelin yazacağı biçim (bot alanları ve iç alanlar atılır, görseller "gorseller"e taşınır).
    svg_sinir: yalnız ilk N görsel tam verilir (istem örneği kısa kalsın)."""
    sorular, gorseller = [], {}
    for i, s in enumerate(o.get('sorular', []), 1):
        t = s.get('tur')
        yeni = {k: s[k] for k in ('tur', 'duzey', 'genislik', 'soru') + SORU_ALANLARI.get(t, ()) if k in s}
        sorular.append(yeni)
        if s.get('gorsel') and (svg_sinir is None or len(gorseller) < svg_sinir):
            gorseller[str(i)] = s['gorsel']
    return {'konu': o.get('konu', ''), 'hatirla': o.get('hatirla', []), 'sorular': sorular, 'gorseller': gorseller}


def onceki_kagit(kimlik, hafta, kagit_dizin=None):
    """(hafta, gorselli kâğıt) — aynı sınıf-dersin en yakın önceki haftası; yoksa (None, None)."""
    kagit_dizin = kagit_dizin or CALISMA
    for h in range(hafta - 1, 0, -1):
        if (kagit_dizin / f'{kimlik}-{h}.json').exists():
            return h, gorselli_yukle(f'{kimlik}-{h}', kagit_dizin)
    return None, None


def _gorselsiz(x):
    if isinstance(x, dict):
        return {k: _gorselsiz(v) for k, v in x.items() if k not in ('gorsel', 'ad', 'ders_adi')}
    if isinstance(x, list):
        return [_gorselsiz(v) for v in x]
    return x


def ornek_kisalt(ad, en_cok=5):
    """İstem örneği: yayımlanmış bir kâğıttan farklı türlerde en çok 5 soru ve en kısa görseli."""
    try:
        o = gorselli_yukle(ad)
    except (OSError, ValueError):
        return None
    sorular = o['sorular']
    gorselli = sorted((i for i, s in enumerate(sorular) if s.get('gorsel')), key=lambda i: len(sorular[i]['gorsel']))
    secilen = gorselli[:1]
    turler = {sorular[i]['tur'] for i in secilen}
    for i, s in enumerate(sorular):
        if len(secilen) < en_cok and s['tur'] not in turler:
            secilen.append(i)
            turler.add(s['tur'])
    secilen = [sorular[i] if i in gorselli[:1] else {k: v for k, v in sorular[i].items() if k != 'gorsel'} for i in sorted(secilen)]
    k = api_bicimi({**o, 'sorular': secilen, 'hatirla': o.get('hatirla', [])[:2]})
    return json.dumps(k, ensure_ascii=False)


def _sistem():
    ornekler = [(ad, ornek_kisalt(ad)) for ad in ('7-matematik-8', '6-sosyal-bilgiler-8')]
    ek = '\n\nYAYIMLANMIŞ İKİ KÂĞITTAN KISALTILMIŞ ÖRNEK (yalnız biçim; gerçek kâğıt 12-14 soru ve 5-8 görsel içerir):\n'
    ek += '\n'.join(f'[{ad}]\n{metin}' for ad, metin in ornekler if metin)
    return SISTEM + ek


SISTEM_TAM = None


def sistem_metni():
    global SISTEM_TAM
    if SISTEM_TAM is None:
        SISTEM_TAM = _sistem()
    return SISTEM_TAM


def istek_metni(sinif, ders, hafta, ctx):
    kimlik = f'{sinif}-{ders}'
    ozet = ozet_oku(kimlik, hafta)
    if not ozet:
        raise ValueError(f'{kimlik}-{hafta}: konu özeti yok')
    s = plan_satiri(kimlik, hafta) or {}
    etiket, _ = tarihler(kimlik, hafta, ozet)
    plan = '\n'.join(f'{ad}: {s[k].strip()[:2500]}' for ad, k in (('Ünite / Tema', 'unite'), ('Konu', 'konu'),
                     ('Öğrenme çıktıları', 'ciktilar'), ('Süreç bileşenleri', 'surec')) if (s.get(k) or '').strip())
    h, onceki = onceki_kagit(kimlik, hafta)
    metin = (f'Sınıf: {sinif}. sınıf · Ders: {ctx["dersler"].get(ders, ders)} ({ders}) · Hafta: {hafta} ({etiket})\n\n'
             f'PLAN SATIRI (bu hafta):\n{plan or "(plan dosyası yok; konu özetindeki öğrenme çıktılarını kullan)"}\n\n'
             f'BU HAFTANIN KONU ÖZETİ (sitede yayımlı; içerik kaynağı, cümlelerini aynen aktarma):\n'
             f'{json.dumps(_gorselsiz(ozet), ensure_ascii=False)}\n\n')
    if onceki:
        metin += (f'ÖNCEKİ HAFTANIN KÂĞIDI ({h}. hafta; yalnız biçim ve düzey örneği, konusu farklı, sorularını kullanma; '
                  f'görsellerden yalnız ikisi verildi):\n{json.dumps(api_bicimi(onceki, svg_sinir=2), ensure_ascii=False)}\n\n')
    return metin + f'{sinif}. sınıf {ctx["dersler"].get(ders, ders)} {hafta}. hafta çalışma kâğıdını yaz. Yalnız JSON.'


def ilk_mesaj(sinif, ders, hafta, ctx):
    return {'role': 'user', 'content': istek_metni(sinif, ders, hafta, ctx)}


# ------------------------------------------------------------------ doğrulama

def _metinler(x, yol=''):
    """(yol, dize) çiftleri; 'gorsel' alanları ve SVG'ler hariç."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in ('gorsel', 'gorseller'):
                yield from _metinler(v, f'{yol}.{k}' if yol else k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from _metinler(v, f'{yol}[{i}]')
    elif isinstance(x, str):
        yield yol, x


def _svg_metni(svg):
    try:
        kok = ET.fromstring(svg)
    except ET.ParseError:
        return ''
    return ' '.join(t.strip() for t in kok.itertext() if t.strip())


def svg_denetle(no, svg):
    sorunlar = []
    if not isinstance(svg, str) or not svg.lstrip().startswith('<svg'):
        return [f'gorseller["{no}"]: <svg ile başlayan bir dize olmalı']
    if len(svg) > 16000:
        sorunlar.append(f'gorseller["{no}"]: SVG çok uzun ({len(svg)} karakter; en çok 16000)')
    try:
        kok = ET.fromstring(svg)
    except ET.ParseError as exc:
        return sorunlar + [f'gorseller["{no}"]: SVG geçerli XML değil ({exc})']
    if not kok.tag.endswith('svg'):
        sorunlar.append(f'gorseller["{no}"]: kök öğe svg değil')
    m = re.fullmatch(r'\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*', kok.get('viewBox') or '')
    if not m:
        sorunlar.append(f'gorseller["{no}"]: viewBox="0 0 G Y" gerekli')
    elif float(m.group(1)) > 640 or float(m.group(2)) > 320:
        sorunlar.append(f'gorseller["{no}"]: viewBox en çok 600×260 olmalı ({m.group(1)}×{m.group(2)})')
    for e in kok.iter():
        ad = e.tag.split('}')[-1]
        if ad in ('script', 'foreignObject', 'image', 'iframe'):
            sorunlar.append(f'gorseller["{no}"]: <{ad}> kullanılamaz')
        for a, v in e.attrib.items():
            if a.lower().startswith('on') or ('href' in a and re.match(r'\s*(https?:|javascript:|data:)', v or '')):
                sorunlar.append(f'gorseller["{no}"]: {ad} öğesinde izin verilmeyen öznitelik {a}')
    yazi = _svg_metni(svg)
    if YATAY_KESIR.search(yazi):
        sorunlar.append(f'gorseller["{no}"]: yatay kesir ({YATAY_KESIR.search(yazi).group(0)}); pay, çizgi, payda alt alta çizilmeli (K155)')
    if oz.ATIF_RE.search(yazi):
        sorunlar.append(f'gorseller["{no}"]: atıf ifadesi ({oz.ATIF_RE.search(yazi).group(0)})')
    return sorunlar


def _dize(x):
    return isinstance(x, str) and x.strip() != ''


def soru_denetle(i, s, sinif):
    """Tek sorunun şema ve tür kuralları."""
    y = f'sorular[{i}]'
    if not isinstance(s, dict):
        return [f'{y}: nesne olmalı']
    t, sorunlar = s.get('tur'), []
    if t not in TURLER:
        return [f'{y}.tur geçersiz ({t!r}); olabilecekler: {", ".join(TURLER)}']
    if s.get('duzey') not in DUZEYLER:
        sorunlar.append(f'{y}.duzey "hatirla", "uygula" ya da "ust" olmalı ({s.get("duzey")!r})')
    if s.get('genislik', 'yarim') not in ('yarim', 'tam'):
        sorunlar.append(f'{y}.genislik "yarim" ya da "tam" olmalı')
    if not _dize(s.get('soru')):
        sorunlar.append(f'{y}.soru boş')
    if t == 'coktan':
        sec, d = s.get('secenekler'), s.get('dogru')
        if not (isinstance(sec, list) and 4 <= len(sec) <= 5 and all(_dize(x) for x in sec)):
            sorunlar.append(f'{y}: coktan 4 ya da 5 dolu şık ister')
        elif len({x.strip() for x in sec}) != len(sec):
            sorunlar.append(f'{y}: aynı şık iki kez yazılmış')
        elif sinif <= 8 and len(sec) != 4:
            sorunlar.append(f'{y}: 5-8. sınıfta coktan 4 şıklı olmalı')
        if not (type(d) is int and isinstance(sec, list) and 0 <= d < len(sec)):
            sorunlar.append(f'{y}.dogru 0 tabanlı geçerli şık sırası olmalı ({d!r})')
    elif t == 'dy':
        f = s.get('ifadeler')
        if not (isinstance(f, list) and 3 <= len(f) <= 7 and all(isinstance(x, dict) and _dize(x.get('metin')) and type(x.get('dogru')) is bool for x in f)):
            sorunlar.append(f'{y}: dy 3-7 ifade ister: {{"metin", "dogru": true|false}}')
        elif len({x['dogru'] for x in f}) < 2:
            sorunlar.append(f'{y}: dy ifadelerinin hepsi aynı (doğru ve yanlış ifade bulunmalı)')
    elif t == 'bosluk':
        c = s.get('cumleler')
        if not (isinstance(c, list) and 1 <= len(c) <= 6 and all(isinstance(x, dict) and isinstance(x.get('metin'), str)
                                                                and x['metin'].count('___') == 1 and _dize(x.get('cevap')) for x in c)):
            sorunlar.append(f'{y}: bosluk 1-6 cümle ister; her cümlede tam bir "___" ve dolu "cevap"')
        elif len({x['cevap'].strip() for x in c}) != len(c):
            sorunlar.append(f'{y}: boşluk cevapları birbirinden farklı olmalı')
        if 'fazla' in s and not (isinstance(s['fazla'], list) and all(_dize(x) for x in s['fazla'])):
            sorunlar.append(f'{y}.fazla dize listesi olmalı')
    elif t == 'eslestir':
        c = s.get('ciftler')
        if not (isinstance(c, list) and 3 <= len(c) <= 8 and all(isinstance(x, list) and len(x) == 2 and all(_dize(v) for v in x) for x in c)):
            sorunlar.append(f'{y}: eslestir 3-8 [sol, sağ] çifti ister')
        elif len({x[1].strip() for x in c}) != len(c) or len({x[0].strip() for x in c}) != len(c):
            sorunlar.append(f'{y}: eşleştirme öğeleri birbirinden farklı olmalı')
    elif t in ('kisa', 'acik'):
        if not _dize(s.get('cevap')):
            sorunlar.append(f'{y}.cevap boş')
        if 'satir' in s and not (type(s['satir']) is int and 1 <= s['satir'] <= 8):
            sorunlar.append(f'{y}.satir 1-8 arası tam sayı olmalı')
    elif t == 'tablo':
        b, r = s.get('basliklar'), s.get('satirlar')
        if not (isinstance(b, list) and 2 <= len(b) <= 5 and all(_dize(x) for x in b)):
            sorunlar.append(f'{y}: tablo 2-5 başlık ister')
        elif not (isinstance(r, list) and 2 <= len(r) <= 8 and all(isinstance(x, list) and len(x) == len(b) for x in r)):
            sorunlar.append(f'{y}: tablo 2-8 satır ister; her satırda başlık sayısı kadar hücre')
        else:
            hucre = [h for x in r for h in x]
            if not all(_dize(h) or (isinstance(h, dict) and _dize(h.get('b'))) for h in hucre):
                sorunlar.append(f'{y}: tablo hücresi dize ya da {{"b": cevap}} olmalı')
            elif sum(isinstance(h, dict) for h in hucre) < 2:
                sorunlar.append(f'{y}: tabloda en az iki boş ({{"b": …}}) hücre olmalı')
    elif t == 'siralama':
        o = s.get('ogeler')
        if not (isinstance(o, list) and 3 <= len(o) <= 8 and all(_dize(x) for x in o)):
            sorunlar.append(f'{y}: siralama 3-8 öğe ister')
        elif len({x.strip() for x in o}) != len(o):
            sorunlar.append(f'{y}: sıralama öğeleri birbirinden farklı olmalı')
    elif t == 'sifre':
        r = s.get('satirlar')
        if not (isinstance(r, list) and 3 <= len(r) <= 9 and _dize(s.get('sonuc'))
                and all(isinstance(x, dict) and _dize(x.get('ipucu')) and _dize(x.get('cevap')) and type(x.get('anahtar')) is int for x in r)):
            sorunlar.append(f'{y}: sifre 3-9 satır {{"ipucu", "cevap", "anahtar"}} ve "sonuc" ister')
        else:
            buyuk = [tr_buyuk(x['cevap']) for x in r]
            hata = [j + 1 for j, (x, k) in enumerate(zip(r, buyuk)) if not 0 <= x['anahtar'] < len(k) or k[x['anahtar']] == ' ']
            if hata:
                sorunlar.append(f'{y}: sifre satır {hata} anahtar sırası cevabın dışında ya da boşlukta')
            else:
                anahtar = ''.join(k[x['anahtar']] for x, k in zip(r, buyuk))
                if anahtar != tr_buyuk(s['sonuc']).replace(' ', ''):
                    sorunlar.append(f'{y}: şifre anahtar harfleri "{anahtar}" sonuçla ("{s["sonuc"]}") aynı değil')
    elif t == 'kavram':
        d = s.get('dallar')
        if not (_dize(s.get('merkez')) and isinstance(d, list) and 3 <= len(d) <= 6
                and all(_dize(x) or (isinstance(x, dict) and _dize(x.get('b'))) for x in d)):
            sorunlar.append(f'{y}: kavram "merkez" ve 3-6 dal ister')
        elif not any(isinstance(x, dict) for x in d):
            sorunlar.append(f'{y}: kavram haritasında en az bir boş ({{"b": …}}) dal olmalı')
    return sorunlar


def tr_buyuk(s):
    return s.translate(str.maketrans('iıçğöşü', 'İIÇĞÖŞÜ')).upper()


def sema_denetle(d, sinif):
    if not isinstance(d, dict):
        return ['yanıt bir JSON nesnesi olmalı']
    sorunlar = []
    for k in ('konu', 'hatirla', 'sorular'):
        if k not in d:
            sorunlar.append(f'"{k}" alanı yok')
    if sorunlar:
        return sorunlar
    if not _dize(d['konu']) or len(d['konu']) > 160:
        sorunlar.append('"konu" dolu ve en çok 160 karakter olmalı')
    elif '{' in d['konu'] or '}' in d['konu']:
        sorunlar.append('"konu" düz metin olmalı: süslü parantezli gösterim ({us:…}, {kesir:…}, {kok:…}) kullanılmaz, '
                        'çünkü sayfa başlığına olduğu gibi basılır; birim üssü gerekiyorsa m², m³ yazılabilir')
    h = d['hatirla']
    if not (isinstance(h, list) and 2 <= len(h) <= 5 and all(_dize(x) for x in h)):
        sorunlar.append('"hatirla" 2-5 dolu madde olmalı')
    s = d['sorular']
    if not (isinstance(s, list) and 12 <= len(s) <= 14):
        return sorunlar + [f'"sorular" 12-14 soru olmalı ({len(s) if isinstance(s, list) else type(s).__name__})']
    for i, x in enumerate(s):
        sorunlar += soru_denetle(i, x, sinif)
    if sorunlar:
        return sorunlar
    turler = {x['tur'] for x in s}
    if len(turler) < 5:
        sorunlar.append(f'en az 5 farklı soru türü olmalı ({len(turler)}: {", ".join(sorted(turler))})')
    duzey = {x['duzey'] for x in s}
    if duzey != set(DUZEYLER):
        sorunlar.append(f'üç düzey de bulunmalı (eksik: {", ".join(sorted(set(DUZEYLER) - duzey))})')
    dogrular = [x['dogru'] for x in s if x['tur'] == 'coktan']
    if len(dogrular) >= 4 and len(set(dogrular)) == 1:
        sorunlar.append('çoktan seçmeli soruların hepsinde doğru şık aynı konumda; dağıtılmalı')
    g = d.get('gorseller', {})
    if not isinstance(g, dict):
        return sorunlar + ['"gorseller" {"soru sırası": "<svg…>"} nesnesi olmalı']
    for no, svg in g.items():
        if not (str(no).isdigit() and 1 <= int(no) <= len(s)):
            sorunlar.append(f'gorseller anahtarı "{no}" 1-{len(s)} arası soru sırası olmalı')
            continue
        sorunlar += svg_denetle(no, svg)
    return sorunlar


def icerik_denetle(d):
    sorunlar = []
    for yol, s in _metinler({k: d.get(k) for k in ('konu', 'hatirla', 'sorular')}):
        if oz.ATIF_RE.search(s):
            sorunlar.append(f'{yol}: atıf ifadesi "{oz.ATIF_RE.search(s).group(0)}" kullanılmamalı')
        if DIS_GONDERME.search(s):
            sorunlar.append(f'{yol}: dış gönderme "{DIS_GONDERME.search(s).group(0)}"; soru kendi içinde çözülebilmeli (K164)')
        kesir = YATAY_KESIR.search(re.sub(r'\{[a-z]+:[^{}]*\}', '', s))
        if kesir:
            sorunlar.append(f'{yol}: yatay kesir "{kesir.group(0)}"; {{kesir:a|b}} yazılmalı (K155)')
        for ad in GOSTERIM_AD.findall(s):
            if ad not in oz.GOSTERIM:
                sorunlar.append(f'{yol}: tanımsız gösterim {{{ad}:…}}')
        if s.count('{') != s.count('}'):
            sorunlar.append(f'{yol}: süslü parantezler dengesiz')
    for i, x in enumerate(d.get('sorular', [])):
        if isinstance(x, dict) and re.search(r'\b(görsel|şekil|grafik|tablo|harita)(de|da|deki|daki|e|a|i|ı)\b', x.get('soru', ''), re.I) \
                and str(i + 1) not in d.get('gorseller', {}) and x.get('tur') not in ('tablo', 'kavram', 'sifre'):
            sorunlar.append(f'sorular[{i}]: soru görsele gönderme yapıyor ama gorseller["{i + 1}"] yok (K164)')
    return sorunlar


def _kelimeler(s):
    return re.findall(r'\w+', re.sub(r'\{[a-z]+:([^{}]*)\}', lambda m: m.group(1).replace('|', ' '), s).lower())


def bes_gramlar(metin):
    k = _kelimeler(metin)
    return {tuple(k[i:i + 5]) for i in range(len(k) - 4)}


def soru_metni(s):
    return ' '.join(v for _, v in _metinler(s))


def ortusme(d, kimlik, hafta, haric=(), kagit_dizin=None):
    """Önceki haftaların kâğıtlarıyla 5-gram örtüşmesi: tek soruda ≥ %50 ya da bütün kâğıtta ≥ %20 sorun."""
    kagit_dizin = kagit_dizin or CALISMA
    havuz = set()
    for h in range(1, hafta):
        p = kagit_dizin / f'{kimlik}-{h}.json'
        if h not in haric and p.exists():
            o = json.loads(p.read_text(encoding='utf-8'))
            for s in o.get('sorular', []) + [{'h': x} for x in o.get('hatirla', [])]:
                havuz |= bes_gramlar(soru_metni(s))
    if not havuz:
        return []
    sorunlar, top, ortak = [], 0, 0
    for i, s in enumerate(d.get('sorular', [])):
        g = bes_gramlar(soru_metni(s))
        o = len(g & havuz)
        top, ortak = top + len(g), ortak + o
        if len(g) >= 8 and o / len(g) >= ORTUSME_SORU:
            sorunlar.append(f'sorular[{i}]: önceki haftaların kâğıtlarıyla %{100 * o // len(g)} örtüşüyor; soru özgün olmalı (K039)')
    if top and ortak / top >= ORTUSME_KAGIT:
        sorunlar.append(f'kâğıt önceki haftaların kâğıtlarıyla %{100 * ortak // top} örtüşüyor (K039)')
    return sorunlar


def tamamla(d, sinif, ders, hafta, model=''):
    """Model çıktısı → (kâğıt, görseller {sıra: svg}); bot alanları plandan."""
    kimlik = f'{sinif}-{ders}'
    ozet = ozet_oku(kimlik, hafta)
    etiket, yayin = tarihler(kimlik, hafta, ozet)
    sorular = []
    for s in d['sorular']:
        izinli = ('tur', 'duzey', 'genislik', 'soru', 'sutun') + SORU_ALANLARI[s['tur']]
        sorular.append({k: s[k] for k in izinli if k in s})
    gorseller = {int(k): v for k, v in sorted(d.get('gorseller', {}).items(), key=lambda kv: int(kv[0]))}
    for no in gorseller:
        sorular[no - 1]['gorsel_var'] = True
    kagit = {'sinif': sinif, 'ders': ders, 'hafta': hafta, 'tarih': etiket, 'yayin_tarihi': yayin,
             'konu': d['konu'].strip(), 'ciktilar': ciktilar_al(kimlik, hafta, ozet), 'hatirla': d['hatirla'], 'sorular': sorular,
             'yazan': f'Claude API · calisma_api_uret.py{" · " + model if model else ""}'}
    return kagit, gorseller


# ------------------------------------------------------------------ basım ve taşma

_CU = None
_CU_KILIT = threading.Lock()
BASIM_KILIDI = threading.Lock()
TASMA_BETIK = """<pre id="ck-tasma"></pre><script>
Promise.all([...document.fonts].map(f => f.load())).then(() => document.fonts.ready).then(() => {
  const b = [];
  document.querySelectorAll('.ck .cvp').forEach(c => {
    const r = c.getBoundingClientRect(), soru = c.closest('.ck-soru'); if (!soru || !r.height) return;
    const no = soru.querySelector('.ck-no').textContent, k = soru.getBoundingClientRect();
    const alan = c.closest('.ck-satirlar'), a = alan ? alan.getBoundingClientRect() : k;
    const alt = Math.round(r.bottom - a.bottom), sag = Math.round(r.right - k.right);
    if (alt > 10 || sag > 1) b.push({no, alt, sag, metin: c.textContent.slice(0, 60)});
  });
  document.getElementById('ck-tasma').textContent = JSON.stringify(b);
});</script>"""
TASMA_EK = '<style>body { margin: 0; } .ck { width: 191mm !important; padding: 0 !important; box-shadow: none !important; }</style>'


def cu():
    """calisma_uret.py (Chrome gerektirir; ilk basımda yüklenir)."""
    global _CU
    with _CU_KILIT:
        if _CU is None:
            m = importlib.import_module('calisma_uret')
            m._api_font = m.yazi_tipleri()
            _CU = m
    return _CU


def tasma(ad):
    """Cevaplı baskı belgesinde kutusundan/satırından taşan cevaplar (DKCALISMA cevap_tasma.py ile aynı ölçüt)."""
    m_ = cu()
    kaynak = m_.IS / f'{ad}-cevapli.html'
    belge = kaynak.read_text(encoding='utf-8').replace('</head>', TASMA_EK + '</head>', 1).replace('</body>', TASMA_BETIK + '</body>', 1)
    gecici, dom = m_.IS / f'_tasma-{ad}.html', m_.IS / f'_tasma-{ad}-dom.html'
    gecici.write_text(belge, encoding='utf-8')
    try:
        m_.chrome_calistir(m_.CHROME_ARGS + ['--allow-file-access-from-files', '--window-size=1200,1600',
                           '--virtual-time-budget=8000', '--dump-dom', gecici.as_uri()], dom, m_.IS / f'_tasma-{ad}-chrome.log',
                           lambda: m_.dom_tamam(dom, 'ck-tasma', bos=True))
    finally:
        gecici.unlink(missing_ok=True)
    m = re.search(r'<pre id="ck-tasma">(\[.*?\])</pre>', dom.read_text(encoding='utf-8'), re.S)
    if not m:
        return ['taşma ölçülemedi']
    return [f'basılı {x["no"]}. soruda cevap kutusundan taşıyor (alt +{x["alt"]} px, sağ +{x["sag"]} px): "{x["metin"]}"; cevabı kısaltın'
            for x in json.loads(html.unescape(m.group(1)))]


def _sigmiyor(o, olcum, m_):
    """İki sayfaya sığmayan kâğıt için modele ölçülü geri bildirim."""
    k = min(m_.OLCEKLER)
    boy, g = olcum[k]['boy'], 7 * k
    tam = [s.get('genislik') == 'tam' for s in o['sorular']]
    gerek = sum((2 if t else 1) * (b + g) for b, t in zip(boy, tam))
    kapasite = 2 * ((m_.SAYFA_BOY - m_.PAY - olcum[k]['ust']) + (m_.SAYFA_BOY - m_.PAY))
    uzun = sorted(range(len(boy)), key=lambda i: -boy[i] * (2 if tam[i] else 1))[:4]
    return (f'en küçük ölçekte ({k}) bile içerik iki sayfanın yaklaşık %{round(100 * gerek / kapasite)} kadarını tutuyor; en uzun sorular: '
            + ', '.join(f'sorular[{i}] {boy[i] / m_.MM:.0f} mm{" (tam genişlik)" if tam[i] else ""}' for i in uzun)
            + '. Görselleri alçaltın (style="max-height:24mm" ya da daha az), uzun soru köklerini ve şıkları kısaltın ya da bir soru çıkarın.')


def bas(kagit, gorseller, ad, hedef):
    """Geçici klasöre basar. Döner (sorunlar, bilgi): bilgi = {'pdf': [cevapsız, cevaplı], 'sira': [basılı no → JSON sırası (1 tabanlı)],
    'sayfa': (s1, s2), 'olcek', 'bosluk'}."""
    m_ = cu()
    o = copy.deepcopy(kagit)
    for no, svg in gorseller.items():
        o['sorular'][no - 1]['gorsel'] = svg
    asil = list(o['sorular'])
    pub = Path(hedef) / 'public'
    (pub / 'calisma' / 'pdf').mkdir(parents=True, exist_ok=True)
    for ad_ in ('calisma.css', 'logo.svg'):
        if not (pub / ad_).exists():
            (pub / ad_).symlink_to(PUBLIC / ad_)
    with BASIM_KILIDI:
        eski, m_.PUBLIC = m_.PUBLIC, pub
        try:
            olcum = m_.olc(o, ad, m_._api_font)
            adaylar = m_.yerlesim(o, olcum) if olcum else []
            if not adaylar:
                return [f'ölçümlü yerleşim yok: ' + (_sigmiyor(o, olcum, m_) if olcum else 'ölçüm alınamadı')], None
            for olcek, plan, bosluk in adaylar:
                o['sorular'] = list(asil)
                plan = m_.sirala(o, plan)
                s1, _ = m_.pdf_yap(o, ad, False, m_._api_font, plan, olcek)
                s2, _ = m_.pdf_yap(o, ad, True, m_._api_font, plan, olcek)
                if max(s1, s2) <= 2:
                    break
            sorunlar = tasma(ad)
        finally:
            m_.PUBLIC = eski
    sira = [next(j for j, x in enumerate(asil, 1) if x is s) for s in o['sorular']]
    if (s1, s2) != (2, 2):
        sorunlar.insert(0, f'PDF sayfa sayısı cevapsız {s1}, cevaplı {s2}; ikisi de tam 2 sayfa olmalı '
                           + ('(içerik kısaltılmalı)' if max(s1, s2) > 2 else '(soru eklenmeli ya da görseller büyütülmeli)'))
    elif max(bosluk[2:] or [0]) > KISA_MM:
        sorunlar.insert(0, f'2. sayfanın sütun altında {max(bosluk[2:])} mm boşluk (KISA): bir soru eklenmeli ya da görseller büyütülmeli')
    return sorunlar, {'pdf': [pub / 'calisma' / 'pdf' / f'{ad}.pdf', pub / 'calisma' / 'pdf' / f'{ad}-cevapli.pdf'],
                      'sira': sira, 'sayfa': (s1, s2), 'olcek': olcek, 'bosluk': bosluk}


def png_sayfalar(pdfler, dpi=110):
    import pymupdf as fitz
    cikti = []
    for p in pdfler:
        with fitz.open(p) as belge:
            cikti += [sayfa.get_pixmap(dpi=dpi).tobytes('png') for sayfa in belge]
    return cikti


def mekanik(metin, sinif, ders, hafta, ctx, haric=()):
    """Denetim + basım. Döner (sorunlar, kagit, gorseller, bilgi)."""
    try:
        d = oz.json_ayikla(metin)
    except (ValueError, json.JSONDecodeError) as exc:
        return [f'JSON çözülemedi: {exc}'], None, None, None
    sorunlar = sema_denetle(d, sinif)
    if sorunlar:
        return sorunlar, None, None, None
    sorunlar = icerik_denetle(d) + ortusme(d, f'{sinif}-{ders}', hafta, haric)
    if sorunlar:
        return sorunlar, None, None, None
    kagit, gorseller = tamamla(d, sinif, ders, hafta, ctx.get('model', ''))
    ad = birim_ad(sinif, ders, hafta)
    try:
        sorunlar, bilgi = bas(kagit, gorseller, ad, ctx['gecici'] / ad)
    except Exception as exc:          # gösterim çözücüsü, Chrome: kâğıt yayımlanmaz, sorun modele verilir
        if isinstance(exc, SystemExit):
            raise
        return [f'basım hatası: {type(exc).__name__}: {exc}'], None, None, None
    return sorunlar, kagit, gorseller, bilgi


def kaydet(kagit, gorseller, ad):
    """araclar/calisma/<ad>.json + araclar/calisma_gorseller/<ad>.py (veri modülü; uygula sabit)."""
    YAZ['kagit'].mkdir(parents=True, exist_ok=True)
    YAZ['gorsel'].mkdir(parents=True, exist_ok=True)
    (YAZ['kagit'] / f'{ad}.json').write_text(json.dumps(kagit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    ders = kagit['ders']
    satirlar = ''.join(f'    {no}: {svg!r},\n' for no, svg in sorted(gorseller.items()))
    (YAZ['gorsel'] / f'{ad}.py').write_text(
        f'"""{kagit["sinif"]}. sınıf {ders} {kagit["hafta"]}. hafta çalışma kâğıdı görselleri (calisma_api_uret.py; veri modülü).\n'
        'SVG; insan figürü yok (K024/K048); kesirler dikey (K155)."""\n\n'
        f'GORSELLER = {{\n{satirlar}}}\n\n\n'
        'def uygula(o):\n'
        '    for no, svg in GORSELLER.items():\n'
        "        if 1 <= no <= len(o['sorular']):\n"
        "            o['sorular'][no - 1]['gorsel'] = svg\n"
        '    return o\n', encoding='utf-8')
    taslak_sil(ad)


def taslak_yaz(ad, veri):
    YAZ['taslak'].mkdir(parents=True, exist_ok=True)
    (YAZ['taslak'] / f'{ad}.json').write_text(json.dumps(veri, ensure_ascii=False) + '\n', encoding='utf-8')


def taslak_oku(ad):
    p = YAZ['taslak'] / f'{ad}.json'
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else None


def taslak_sil(ad):
    (YAZ['taslak'] / f'{ad}.json').unlink(missing_ok=True)


def var_mi(ad):
    return (YAZ['kagit'] / f'{ad}.json').exists()


# ------------------------------------------------------------------ istekler

class Sayac(oz.Sayac):
    def istek_basi(self, toplu=False):
        v = ISTEK_TAHMINI.get(self.model, 0.8) * (0.5 if toplu else 1.0)
        return max(v, self.dolar / self.istek) if self.istek else v


def istek_parametreleri(model, caba, mesajlar, toplu):
    return dict(model=model, max_tokens=64000,
                system=[{'type': 'text', 'text': sistem_metni(), 'cache_control': {'type': 'ephemeral', **({'ttl': '1h'} if toplu else {})}}],
                messages=mesajlar, output_config={'effort': caba})


def goz_parametreleri(model, pngler, ad):
    icerik = []
    for i, png in enumerate(pngler):
        etiket = f'{"Cevapsız" if i < 2 else "Cevaplı"} sürüm, {i % 2 + 1}. sayfa'
        icerik += [{'type': 'text', 'text': etiket},
                   {'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/png', 'data': base64.b64encode(png).decode()}}]
    icerik.append({'type': 'text', 'text': f'{ad} çalışma kâğıdının basılı sayfaları. Sorunları JSON olarak yaz.'})
    return dict(model=model, max_tokens=8000, system=GOZ_SISTEM, messages=[{'role': 'user', 'content': icerik}],
                output_config={'effort': 'medium'})


def goz_coz(metin):
    """g yanıtı → [{'soru', 'agirlik', 'sorun'}]; çözülemezse None."""
    try:
        d = oz.json_ayikla(metin)
    except (ValueError, json.JSONDecodeError):
        return None
    liste = d.get('sorunlar') if isinstance(d, dict) else None
    if not isinstance(liste, list):
        return None
    return [x for x in liste if isinstance(x, dict) and _dize(x.get('sorun'))]


def goz_sorunlari(bulgular, sira):
    """Gözle denetim bulguları → düzeltme mesajı maddeleri (basılı numara JSON sırasına çevrilir)."""
    cikti = []
    for b in bulgular:
        no = b.get('soru')
        if type(no) is int and 1 <= no <= len(sira):
            yer = f'basılı {no}. soru = JSON sorular[{sira[no - 1] - 1}] (gorseller anahtarı "{sira[no - 1]}")'
        else:
            yer = 'sayfa geneli'
        cikti.append(f'Gözle denetim ({b.get("agirlik", "ciddi")}), {yer}: {b["sorun"]}')
    return cikti


def _akis(client, params):
    def cagri():
        with client.beta.messages.stream(**params, betas=['server-side-fallback-2026-07-01'], fallbacks='default') as akis:
            return akis.get_final_message()
    return oz._api(cagri)


def _toplu_istek(custom_id, params):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    return Request(custom_id=custom_id, params=MessageCreateParamsNonStreaming(**params))


def durum_gonder(args):
    """Toplu istek kaydı hemen dala gönderilir: başka botların toplayıcısı bu isteği 'bilinmeyen' saymasın."""
    if not getattr(args, 'durum_gonder', False):
        return
    komutlar = [['git', 'add', str(DURUM)], ['git', 'commit', '-q', '-m', 'Çalışma kâğıdı toplu istek kayıtları'],
                ['git', 'pull', '-q', '--rebase', '--autostash'], ['git', 'push', '-q']]
    for k in komutlar:
        r = subprocess.run(k, cwd=KOK, capture_output=True, text=True)
        if r.returncode:
            print(f'  (kayıt dosyası şimdi gönderilemedi: {" ".join(k[:2])}: {r.stderr.strip()[:200]}; iş sonunda gönderilir)', flush=True)
            if k[1] == 'pull':
                subprocess.run(['git', 'rebase', '--abort'], cwd=KOK, capture_output=True)
            return


def toplu_gonder(client, istekler, etiket, args):
    if not istekler:
        return None
    b = oz.toplu_gonder(client, istekler, etiket)
    durum_gonder(args)
    return b


# ------------------------------------------------------------------ anlık kip

def tek_kagit(client, args, birim, ctx, sayac, izin):
    """Anlık: i → denetim/basım → g → (gerekirse d → denetim/basım → g). Döner (durum, bilgi, maliyet)."""
    sinif, ders, hafta = birim
    ad = birim_ad(*birim)
    yerel = Sayac(args.model)
    mesaj = ilk_mesaj(sinif, ders, hafta, ctx)

    def cagir(params):
        y = _akis(client, params)
        yerel.ekle(y.usage, getattr(y, 'model', None))
        sayac.ekle(y.usage, getattr(y, 'model', None))
        return oz.yanit_metni(y)

    metin = cagir(istek_parametreleri(args.model, args.caba, [mesaj], False))
    for tur in ('i', 'd'):
        sorunlar, kagit, gorseller, bilgi = mekanik(metin, sinif, ders, hafta, ctx)
        if not sorunlar:
            bulgular = goz_coz(cagir(goz_parametreleri(args.model, png_sayfalar(bilgi['pdf']), ad)))
            if bulgular is None:
                print(f'  {ad}: gözle denetim yanıtı çözülemedi; mekanik denetim geçtiği için kaydediliyor', flush=True)
                bulgular = []
            ciddi = [b for b in bulgular if b.get('agirlik') != 'kucuk']
            if not ciddi:
                kaydet(kagit, gorseller, ad)
                ek = f'; küçük bulgular: {"; ".join(b["sorun"] for b in bulgular)[:300]}' if bulgular else ''
                return 'tamam', f'{len(kagit["sorular"])} soru, {len(gorseller)} görsel, ölçek {bilgi["olcek"]}' \
                    + (' (düzeltme turunda)' if tur == 'd' else '') + ek, yerel.maliyet()
            sorunlar = goz_sorunlari(bulgular, bilgi['sira'])
        if tur == 'd':
            return 'hata', '; '.join(sorunlar[:6]), yerel.maliyet()
        if not izin():
            return 'hata', f'bütçe ya da süre doldu; düzeltme yapılmadı ({"; ".join(sorunlar[:3])})', yerel.maliyet()
        print(f'  [düzeltilecek] {ad}: {"; ".join(sorunlar[:3])}', flush=True)
        metin = cagir(istek_parametreleri(args.model, args.caba, oz.duzeltme_mesajlari(mesaj, metin, sorunlar), False))


def anlik_uret(client, args, birimler, ctx, sayac, bitis):
    sonuc = {'tamam': [], 'hata': []}
    kalan = list(birimler)
    kilit, acik = threading.Lock(), {'n': 0}
    durdu = None

    def izin():
        with kilit:
            return time.time() < bitis and sayac.maliyet() + acik['n'] * sayac.istek_basi() <= args.butce

    def is_(b):
        try:
            return tek_kagit(client, args, b, ctx, sayac, izin)
        finally:
            with kilit:
                acik['n'] -= 1

    with ThreadPoolExecutor(max_workers=max(1, args.paralel)) as havuz:
        isler = {}
        while kalan or isler:
            while kalan and not durdu and len(isler) < max(1, args.paralel) and time.time() < bitis:
                with kilit:
                    if sayac.maliyet() + (acik['n'] + 1) * (sayac.istek_basi() * 1.4 + GOZ_PAYI) > args.butce:
                        break
                    acik['n'] += 1
                b = kalan.pop(0)
                isler[havuz.submit(is_, b)] = b
            if not isler:
                break
            biten = next(as_completed(list(isler)))
            b = isler.pop(biten)
            try:
                durum_, not_, dolar = biten.result()
            except SystemExit as exc:
                durdu = durdu or str(exc)
                durum_, not_, dolar = 'hata', 'çalıştırma durduruldu', 0
            except Exception as exc:
                durum_, not_, dolar = 'hata', f'{type(exc).__name__}: {exc}', 0
            sonuc[durum_].append(birim_ad(*b))
            print(f'  [{durum_}] {birim_ad(*b)}: {not_} · {dolar:.2f} $', flush=True)
    if durdu:
        print(f'  [dur] {durdu}', flush=True)
        raise oz.Durdu(durdu, sonuc, [birim_ad(*b) for b in kalan])
    return sonuc, [birim_ad(*b) for b in kalan]


# ------------------------------------------------------------------ toplu kip

def baska_istekler():
    """Başka botların kayıt dosyalarındaki toplu istekler (özet botu toplu_durum.json ve *_toplu_durum.json)."""
    kimlikler = set()
    for p in DURUM.parent.glob('*toplu_durum.json'):
        if p.resolve() == DURUM.resolve():
            continue
        try:
            v = json.loads(p.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        kimlikler |= set(v.get('gonderilen') or {}) | set(v.get('toplanan') or [])
    return kimlikler


def _birim(h, kimlik):
    sinif, ders = kimlik.split('-', 1)
    return int(sinif), ders, h


def sonuc_isle(r, ctx, sayac, png_onbellek):
    """Tek toplu sonuç → ('tamam'|'goz'|'duzelt'|'hata'|'atla', bilgi)."""
    h, kimlik, tur = ozel_coz(r.custom_id)
    sinif, ders, _ = _birim(h, kimlik)
    ad = birim_ad(sinif, ders, h)
    if var_mi(ad):
        return 'atla', 'kâğıt zaten var'
    if r.result.type != 'succeeded':
        hata = getattr(getattr(r.result, 'error', None), 'error', None)
        if tur == 'g' and taslak_oku(ad):
            return 'goz', 'gözle denetim isteği sonuçlanmadı; yeniden gönderilecek'
        return 'hata', f'toplu istek sonucu: {r.result.type} {getattr(hata, "message", "") or ""}'.strip()
    y = r.result.message
    sayac.ekle(y.usage, getattr(y, 'model', None), toplu=True)
    try:
        metin = oz.yanit_metni(y)
    except RuntimeError as exc:
        return 'hata', str(exc)
    if tur in ('i', 'd'):
        sorunlar, kagit, gorseller, bilgi = mekanik(metin, sinif, ders, h, ctx)
        if sorunlar:
            if tur == 'd':
                taslak_sil(ad)
                return 'hata', '; '.join(sorunlar[:6])
            return 'duzelt', (metin, sorunlar)
        taslak_yaz(ad, {'metin': metin, 'tur': tur, 'sira': bilgi['sira'],
                        'zaman': datetime.now(timezone.utc).isoformat(timespec='seconds')})
        png_onbellek[ad] = png_sayfalar(bilgi['pdf'])
        return 'goz', f'{len(kagit["sorular"])} soru, {len(gorseller)} görsel; gözle denetime gidiyor'
    ts = taslak_oku(ad)
    if not ts:
        return 'hata', 'gözle denetim sonucu geldi ama taslak yok'
    bulgular = goz_coz(metin)
    if bulgular is None:
        print(f'  {ad}: gözle denetim yanıtı çözülemedi; mekanik denetim geçtiği için kaydediliyor', flush=True)
        bulgular = []
    ciddi = [b for b in bulgular if b.get('agirlik') != 'kucuk']
    if not ciddi:
        kagit, gorseller = tamamla(oz.json_ayikla(ts['metin']), sinif, ders, h, ctx.get('model', ''))
        kaydet(kagit, gorseller, ad)
        return 'tamam', f'{len(kagit["sorular"])} soru, {len(gorseller)} görsel' + (' (düzeltme turunda)' if ts['tur'] == 'd' else '') \
            + (f'; küçük bulgular: {"; ".join(b["sorun"] for b in bulgular)[:300]}' if bulgular else '')
    sorunlar = goz_sorunlari(bulgular, ts['sira'])
    if ts['tur'] == 'd':
        taslak_sil(ad)
        return 'hata', 'düzeltmeden sonra da gözle denetimde ciddi sorun: ' + '; '.join(sorunlar[:4])
    return 'duzelt', (ts['metin'], sorunlar)


def topla(client, args, ctx, sayac, bitis, butce, bekle_bilinmeyen, gonder=True):
    """Son 28 gündeki toplu istekleri işler. Döner {'yazilan': [ad], 'hata': [(ad, bilgi)], 'bekleyen': {ad}, 'bilinmeyen': bool}.
    Mekanik denetimi geçen ilk tur/düzeltme sonuçları taslak olarak yazılır ve gözle denetime (g) gönderilir; sorunlu ilk tur
    ve gözle denetimde ciddi sorunlu taslak düzeltme turuna (d) gider. Gönderimi kalmış taslaklar için g yeniden gönderilir."""
    d = oz.durum()
    sinir = datetime.now(timezone.utc) - timedelta(days=oz.KURTARMA_GUN)
    t = {'yazilan': [], 'hata': [], 'bekleyen': set(), 'bilinmeyen': False}
    baska = baska_istekler()
    duzelt, png = {}, {}
    toplular = [b for b in _liste(client, sinir) if b.id not in d['toplanan'] and b.id not in baska]
    toplular.sort(key=lambda b: b.processing_status != 'ended')
    for b in toplular:
        if b.processing_status in ('in_progress', 'canceling'):
            bilinen = d['gonderilen'].get(b.id)
            if bilinen:
                t['bekleyen'] |= {birim_ad(*_birim(h, k)) for h, k, _ in map(ozel_coz, bilinen['istekler']) if k}
                continue
            if not bekle_bilinmeyen:
                t['bilinmeyen'] = True
                continue
            print(f'İçeriği kayıtlı olmayan toplu istek {b.id} sürüyor; bitmesi bekleniyor (iki kez ödememek için).', flush=True)
            b = oz.toplu_bekle(client, b.id, bitis, 'önceki toplu istek')
            if b is None:
                t['bilinmeyen'] = True
                continue
        if b.processing_status != 'ended':
            continue
        bilinen = d['gonderilen'].get(b.id) or {}
        try:
            for r in oz._api(lambda: client.messages.batches.results(b.id)):
                h, k, tur = ozel_coz(r.custom_id)
                if not k:
                    continue
                ad = birim_ad(*_birim(h, k))
                sonuc, bilgi = sonuc_isle(r, ctx, sayac, png)
                if sonuc == 'atla':
                    continue
                if sonuc == 'tamam':
                    t['yazilan'].append(ad)
                elif sonuc == 'duzelt':
                    duzelt[ad] = bilgi
                elif sonuc == 'hata':
                    t['hata'].append((ad, bilgi))
                print(f'  [{"düzeltilecek" if sonuc == "duzelt" else sonuc}] {ad}/{tur}: '
                      f'{"; ".join(bilgi[1][:3]) if sonuc == "duzelt" else bilgi} ({b.id})', flush=True)
        except Exception as exc:
            if isinstance(exc, SystemExit):
                raise
            print(f'  {b.id} sonuçları okunamadı: {type(exc).__name__}: {exc}', flush=True)
            if bilinen:
                t['bekleyen'] |= {birim_ad(*_birim(h, k)) for h, k, _ in map(ozel_coz, bilinen['istekler']) if k}
            else:
                t['bilinmeyen'] = True
            continue
        d['toplanan'].append(b.id)
        d['gonderilen'].pop(b.id, None)
        oz.durum_kaydet()
    # gözle denetimi bekleyen ve hiçbir süren istekte olmayan taslaklar (yeni yazılanlar ve gönderimi kalmış olanlar)
    goz = sorted(p.stem for p in YAZ['taslak'].glob('*.json') if p.stem not in t['bekleyen'] and p.stem not in duzelt and not var_mi(p.stem))
    engel = (not gonder and 'bu kipte g/d gönderilmez') or (t['bilinmeyen'] and 'içeriği bilinmeyen toplu istek sürüyor') \
        or (time.time() >= bitis and 'süre doldu')
    if engel:
        for ad, (_, sorunlar) in duzelt.items():
            if not taslak_oku(ad):
                t['hata'].append((ad, f'{engel}; düzeltme gönderilmedi ({"; ".join(sorunlar[:3])})'))
        t['bekleyen'] |= set(goz)
        return t
    istekler = []
    for ad in goz:
        sinif, ders, h = ad_coz(ad)
        if ad not in png:
            ts = taslak_oku(ad)
            s, _, _, bilgi = mekanik(ts['metin'], sinif, ders, h, ctx)
            if s:          # taslak artık geçmiyor (ör. kaynak değişti): taslak atılır, kâğıt yeniden üretilir
                taslak_sil(ad)
                t['hata'].append((ad, 'taslak yeniden basılamadı: ' + '; '.join(s[:3])))
                continue
            png[ad] = png_sayfalar(bilgi['pdf'])
        istekler.append(_toplu_istek(ozel_kimlik(h, f'{sinif}-{ders}', 'g'), goz_parametreleri(args.model, png[ad], ad)))
        butce.kalan -= GOZ_PAYI
    sigan = butce.al(len(duzelt))
    for i, (ad, (metin, sorunlar)) in enumerate(sorted(duzelt.items())):
        if i >= sigan:
            taslak_sil(ad)
            t['hata'].append((ad, f'bütçe doldu; düzeltme gönderilmedi ({"; ".join(sorunlar[:3])})'))
            continue
        sinif, ders, h = ad_coz(ad)
        try:
            mesajlar = oz.duzeltme_mesajlari(ilk_mesaj(sinif, ders, h, ctx), metin, sorunlar)
        except ValueError as exc:
            t['hata'].append((ad, str(exc)))
            continue
        istekler.append(_toplu_istek(ozel_kimlik(h, f'{sinif}-{ders}', 'd'), istek_parametreleri(args.model, args.caba, mesajlar, True)))
    if istekler:
        toplu_gonder(client, istekler, f'Gözle denetim ve düzeltme turu ({len(goz)} g, {len(istekler) - len(goz)} d)', args)
        t['bekleyen'] |= {birim_ad(*_birim(h, k)) for h, k, _ in (ozel_coz(r['custom_id']) for r in istekler)}
    return t


def _liste(client, sinir):
    for b in oz._api(lambda: client.messages.batches.list(limit=50)):     # en yeni önce
        if b.created_at < sinir:
            break
        yield b


def toplu_uret(client, args, birimler, ctx, sayac, bitis):
    adlar = [birim_ad(*b) for b in birimler]
    sonuc = {'tamam': [], 'hata': [], 'bekliyor': []}
    butce = oz.Butce(args.butce, sayac.istek_basi(toplu=True) * 1.3 + GOZ_PAYI / 2)

    def isle(t):
        for ad in t['yazilan']:
            if ad in adlar and ad not in sonuc['tamam']:
                sonuc['tamam'].append(ad)
        for ad, _ in t['hata']:
            if ad in adlar and ad not in sonuc['hata']:
                sonuc['hata'].append(ad)

    t = topla(client, args, ctx, sayac, bitis, butce, bekle_bilinmeyen=True)
    isle(t)
    if t['bilinmeyen']:
        raise SystemExit('İçeriği kayıtlı olmayan bir toplu istek süre içinde bitmedi; aynı kâğıda iki kez ödememek için yeni istek gönderilmedi.')
    yeni = [b for b in birimler if not var_mi(birim_ad(*b)) and not taslak_oku(birim_ad(*b))
            and birim_ad(*b) not in t['bekleyen'] and birim_ad(*b) not in sonuc['hata']]
    kalan = []
    if yeni and time.time() >= bitis:
        return sonuc, [birim_ad(*b) for b in yeni]
    if yeni:
        sigan = butce.al(len(yeni))
        gonder, kalan = yeni[:sigan], [birim_ad(*b) for b in yeni[sigan:]]
        if kalan:
            print(f'Bütçe ({args.butce:.0f} $) tahminen {len(gonder)} kâğıda yetiyor; {len(kalan)} kâğıt sonraki çalıştırmaya kaldı.', flush=True)
        istekler = []
        for sinif, ders, h in gonder:
            try:
                istekler.append(_toplu_istek(ozel_kimlik(h, f'{sinif}-{ders}', 'i'),
                                             istek_parametreleri(args.model, args.caba, [ilk_mesaj(sinif, ders, h, ctx)], True)))
            except ValueError as exc:
                sonuc['hata'].append(birim_ad(sinif, ders, h))
                print(f'  [hata] {birim_ad(sinif, ders, h)}: {exc}', flush=True)
        toplu_gonder(client, istekler, '1. tur', args)
    son_rapor = 0
    while True:
        bekliyor = [a for a in adlar if not var_mi(a) and a not in sonuc['hata'] and a not in kalan]
        if not bekliyor or time.time() >= bitis:
            break
        if time.time() - son_rapor > 300:
            print(f'  {len(bekliyor)} kâğıt toplu istekte bekliyor…', flush=True)
            son_rapor = time.time()
        time.sleep(60)
        isle(topla(client, args, ctx, sayac, bitis, butce, bekle_bilinmeyen=False))
    sonuc['bekliyor'] = [a for a in adlar if not var_mi(a) and a not in sonuc['hata'] and a not in kalan]
    return sonuc, kalan


# ------------------------------------------------------------------ prova

def kuru_kagit(birim, ctx):
    """API'siz prova: önceki haftanın kâğıdı bu haftanınmış gibi denetlenir, basılır ve geçici klasöre yazılır."""
    sinif, ders, hafta = birim
    ad = birim_ad(*birim)
    h, onceki = onceki_kagit(f'{sinif}-{ders}', hafta)
    if not onceki:
        return 'hata', 'önceki haftanın kâğıdı yok'
    d = api_bicimi(onceki)
    for x in d['sorular']:      # eski kâğıtlardaki Bloom adları (kavrama, analiz…) şemanın üç düzeyine
        x['duzey'] = ESKI_DUZEY.get(x.get('duzey'), x.get('duzey'))
    metin = json.dumps(d, ensure_ascii=False)
    sorunlar, kagit, gorseller, bilgi = mekanik(metin, sinif, ders, hafta, ctx, haric=(h,))
    if sorunlar:
        return 'hata', '; '.join(sorunlar[:6])
    pngler = png_sayfalar(bilgi['pdf'])
    for i, p in enumerate(pngler):
        (ctx['gecici'] / f'{ad}-{"cevapsiz" if i < 2 else "cevapli"}-s{i % 2 + 1}.png').write_bytes(p)
    kaydet(kagit, gorseller, ad)
    return 'tamam', (f'{h}. haftadan prova: {len(kagit["sorular"])} soru, {len(gorseller)} görsel, ölçek {bilgi["olcek"]}, '
                     f'sayfa {bilgi["sayfa"]}, 2. sayfa boşluk {bilgi["bosluk"][2:]} mm; PNG {ctx["gecici"]}/{ad}-*.png '
                     f'(g isteği {len(pngler)} sayfa gönderirdi)')


# ------------------------------------------------------------------ ana

def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--haftalar', help='hafta aralığı, ör. 9-16 ya da 9,11')
    ap.add_argument('--siniflar', help='sınıf aralığı, ör. 5-8')
    ap.add_argument('--dersler', help='virgülle: ders adı (matematik) ya da sınıf-ders (7-matematik)')
    ap.add_argument('--en-cok', type=int, default=0, help='en çok bu kadar kâğıt (plan tarihine göre önce gelenler)')
    ap.add_argument('--model', default=VARSAYILAN_MODEL, choices=sorted(ISTEK_TAHMINI))
    ap.add_argument('--caba', default='high', choices=['low', 'medium', 'high', 'xhigh'])
    ap.add_argument('--toplu', action='store_true', help='Message Batches API (yarı fiyat)')
    ap.add_argument('--topla', action='store_true', help='yalnız toplayıcı: biten sonuçları işle, g/d turlarını gönder')
    ap.add_argument('--kuru', action='store_true', help="API'siz prova: önceki haftanın kâğıdından; geçici klasöre yazar")
    ap.add_argument('--liste', action='store_true', help='eksik kâğıtları yazdır ve çık')
    ap.add_argument('--paralel', type=int, default=3, help='anlık kipte aynı anda açık kâğıt')
    ap.add_argument('--butce', type=float, default=20.0, help='USD; yeni istekler için tahmini harcama sınırı')
    ap.add_argument('--sure-dk', type=float, default=0, help='bu kadar dakika sonra yeni istek açma ve beklemeyi bırak (0 = sınırsız)')
    ap.add_argument('--durum-gonder', action='store_true', help='toplu istek kaydını gönderir göndermez dala commit/push et (iş akışı)')
    args = ap.parse_args()

    dersler = oz.dersler_sozlugu()
    secim = {x.strip() for x in (args.dersler or '').split(',') if x.strip()} or None
    if secim:
        tanimsiz = [x for x in secim if x not in dersler and not (re.fullmatch(r'\d+-.+', x) and x.split('-', 1)[1] in dersler)]
        if tanimsiz:
            ap.error(f'tanımsız ders: {tanimsiz}')
    try:
        birimler = eksikler(aralik(args.haftalar), aralik(args.siniflar), secim, args.en_cok)
    except ValueError as exc:
        ap.error(str(exc))
    if args.liste:
        for b in birimler:
            print(birim_ad(*b), plan_tarihi(*b))
        print(f'{len(birimler)} eksik kâğıt')
        return
    gecici = Path(tempfile.mkdtemp(prefix='calisma-api-'))
    ctx = {'dersler': dersler, 'model': args.model, 'gecici': gecici}
    sayac = Sayac(args.model)
    basla = time.time()
    bitis = basla + args.sure_dk * 60 if args.sure_dk else float('inf')

    if args.topla:
        import anthropic
        client = anthropic.Anthropic(max_retries=6)
        try:
            t = topla(client, args, ctx, sayac, bitis, oz.Butce(args.butce, sayac.istek_basi(toplu=True)), bekle_bilinmeyen=False)
        except SystemExit as exc:
            print(f'DURDU: {exc}')
            sys.exit(1)
        print(f'\nToplayıcı: {len(t["yazilan"])} kâğıt yazıldı, {len(t["hata"])} hata, {len(t["bekleyen"])} kâğıt toplu istekte bekliyor'
              + (' · içeriği kayıtlı olmayan süren toplu istek var' if t['bilinmeyen'] else ''))
        print(f'Toplanan sonuçların maliyeti: {sayac}')
        for ad, bilgi in t['hata']:
            print(f'Hatalı: {ad}: {bilgi}')
        return

    if not birimler:
        print('Eksik kâğıt yok.')
        return
    print(f'{len(birimler)} kâğıt: {", ".join(birim_ad(*b) for b in birimler[:12])}{" …" if len(birimler) > 12 else ""} · '
          f'model {args.model} · çaba {args.caba} · {"prova" if args.kuru else "toplu (yarı fiyat)" if args.toplu else "anlık"}', flush=True)
    if args.kuru:
        for k in YAZ:
            YAZ[k] = gecici / k
            YAZ[k].mkdir()
        print(f'Prova: dosyalar {gecici} klasörüne yazılıyor (depoya dokunulmaz).', flush=True)
        hata = 0
        for b in birimler:
            durum_, not_ = kuru_kagit(b, ctx)
            hata += durum_ == 'hata'
            print(f'  [{durum_}] {birim_ad(*b)}: {not_}', flush=True)
        sys.exit(1 if hata else 0)

    import anthropic
    client = anthropic.Anthropic(max_retries=6)
    durdu, kalan = None, []
    sonuc = {'tamam': [], 'hata': [], 'bekliyor': []}
    try:
        if args.toplu:
            sonuc, kalan = toplu_uret(client, args, birimler, ctx, sayac, bitis)
        else:
            onceki = Sayac(args.model)    # önceden ödenmiş toplu sonuçlar bu çalıştırmanın bütçesinden düşülmez
            t = topla(client, args, ctx, onceki, bitis, oz.Butce(0, 1), bekle_bilinmeyen=True, gonder=False)
            if t['yazilan']:
                print(f'Önceki toplu isteklerden {len(t["yazilan"])} kâğıt yazıldı (daha önce ödendi: {onceki})', flush=True)
            if t['bilinmeyen']:
                raise SystemExit('İçeriği kayıtlı olmayan bir toplu istek sürüyor; aynı kâğıda iki kez ödememek için anlık üretim başlatılmadı.')
            haric = {a for a in t['bekleyen']} | {p.stem for p in YAZ['taslak'].glob('*.json')}
            sonuc['bekliyor'] = sorted(a for a in haric if a in {birim_ad(*b) for b in birimler})
            hedef = [b for b in birimler if not var_mi(birim_ad(*b)) and birim_ad(*b) not in haric]
            s2, kalan = anlik_uret(client, args, hedef, ctx, sayac, bitis)
            sonuc['tamam'] += s2['tamam']
            sonuc['hata'] += s2['hata']
    except oz.Durdu as exc:
        durdu = str(exc)
        sonuc['tamam'] += exc.sonuc['tamam']
        sonuc['hata'] += exc.sonuc['hata']
        kalan = exc.kalan
    except SystemExit as exc:
        durdu = str(exc)
    yazilan = [birim_ad(*b) for b in birimler if var_mi(birim_ad(*b))]
    print(f'\n{len(yazilan)} kâğıt yazıldı, {len(sonuc["hata"])} hata, {len(sonuc.get("bekliyor", []))} toplu istekte bekliyor, '
          f'{len(kalan)} gönderilmedi · {(time.time() - basla) / 60:.0f} dk')
    if durdu:
        print(f'DURDU: {durdu}')
    print(f'Maliyet: {sayac}' + (f' · kâğıt başına {sayac.maliyet() / len(yazilan):.2f} $' if yazilan else ''))
    if sonuc['hata']:
        print('Hatalı kâğıtlar (yeniden çalıştırılınca tekrar denenir): ' + ', '.join(sonuc['hata']))
    if sonuc.get('bekliyor'):
        print('Toplu istekte bekleyenler (toplayıcı iki saatte bir yazar): ' + ', '.join(sonuc['bekliyor']))
    if kalan:
        print('Gönderilmeyenler (bütçe ya da süre doldu): ' + ', '.join(kalan))
    sys.exit(1 if durdu or sonuc['hata'] or kalan else 0)


if __name__ == '__main__':
    main()
