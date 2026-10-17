#!/usr/bin/env python3
"""Sosyal medya "Bunu biliyor muydunuz?" kartları (1080×1350) ve paylaşım kuyruğu kayıtları.

İçerik dosyası: araclar/sosyal/<kimlik>.json
  {
    "ozet": "8-fen-bilimleri-3",            # araclar/ozetler/<ozet>.json (sınıf-ders-hafta)
    "baslik": "Mevsimleri eksen eğikliği oluşturur",   # karttaki büyük başlık (2-3 satır)
    "paragraflar": ["...", "..."],          # karttaki iki kısa paragraf
    "bilgi": "...",                         # gönderi metninin ilk cümleleri ("Bunu biliyor muydunuz?" betik ekler)
    "renk": "c05621"                        # isteğe bağlı vurgu rengi; yoksa dersin paletinden seçilir
  }
Çıktı: public/sosyal/<kimlik>.png (+ Instagram API için .jpg). Yazı tipi: araclar/fontlar/Poppins-*.ttf (SIL OFL).

Kullanım:
  python3 araclar/sosyal_gorsel.py                      # görseli olmayan içerikleri üretir
  python3 araclar/sosyal_gorsel.py --hepsi              # bütün içerikleri yeniden üretir
  python3 araclar/sosyal_gorsel.py bilgi-8-fen-bilimleri-3   # yalnız verilenleri üretir
  python3 araclar/sosyal_gorsel.py --kuyruk 2026-10-13T09:00 # kuyrukta olmayan içerikleri sırayla ekler
                                                              # (günde 6 gönderi: 09, 11, 13, 15, 17, 19)
  python3 araclar/sosyal_gorsel.py --liste                   # paylaşılmamışları sosyal/bekleyen.md'ye yazar
Paylaşım: sosyal/kuyruk.json'daki kayıtlar IG_TOKEN (Instagram) ya da FB_PAGE_TOKEN (Facebook) varsa
araclar/sosyal_paylas.py ile kendiliğinden, yoksa Meta Business Suite'ten elle paylaşılır; paylaşılınca "durum" dolar.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

KOK = Path(__file__).resolve().parent.parent
ICERIK = KOK / 'araclar' / 'sosyal'
OZETLER = KOK / 'araclar' / 'ozetler'
FONTLAR = KOK / 'araclar' / 'fontlar'
CIKTI = KOK / 'public' / 'sosyal'
KUYRUK = KOK / 'sosyal' / 'kuyruk.json'
LOGO = KOK / 'public' / 'profil-512.png'
TSI = timezone(timedelta(hours=3))

W, H = 1080, 1350
UST_H, ALT_Y = 210, 1200
KENAR = 72
NAVY, BG, GOLD, ACIK_MAVI, BEYAZ, METIN = '#0b2257', '#f6f8fd', '#f2b33d', '#7d9cff', '#ffffff', '#26314d'

# ders dizini -> (dosya adı parçası, üst rozet, altlık adı, gönderi metnindeki ad, etiket, renk paleti)
DERSLER = {
    'din-kulturu-ve-ahlak-bilgisi': ('din-kulturu', 'DİN KÜLTÜRÜ', 'Din Kültürü', 'Din Kültürü ve Ahlak Bilgisi', 'dinkültürü',
                                     ['8a5214', '975a16', 'a0611a', 'b7791f', '92400e']),
    'fen-bilimleri': ('fen-bilimleri', 'FEN BİLİMLERİ', 'Fen Bilimleri', 'Fen Bilimleri', 'fenbilimleri',
                      ['c05621', '0e8fa8', 'd97706', 'e0662b', '0f766e']),
    'matematik': ('matematik', 'MATEMATİK', 'Matematik', 'Matematik', 'matematik',
                  ['2b6cb0', '3730a3', '1a5fb4', '4c51bf', '2c4a95', '5a67d8', '3b4cca']),
    'sosyal-bilgiler': ('sosyal-bilgiler', 'SOSYAL BİLGİLER', 'Sosyal Bilgiler', 'Sosyal Bilgiler', 'sosyalbilgiler',
                        ['c05621', 'dd6b20', '9c4221']),
    'turkce': ('turkce', 'TÜRKÇE', 'Türkçe', 'Türkçe', 'türkçe',
               ['97266d', 'b83280', '5a67d8']),
    'arapca': ('arapca', 'ARAPÇA', 'Arapça', 'Arapça', 'arapça',
               ['0369a1', '1e40af', '075985', '1d4ed8', '0c4a6e', '1e3a8a']),
    'ingilizce': ('ingilizce', 'İNGİLİZCE', 'İngilizce', 'İngilizce', 'ingilizce',
                  ['b91c1c', 'c2366b', '9f1239', 'd64545', 'c53030', '9c4221']),
    'tc-inkilap-tarihi-ve-ataturkculuk': ('inkilap-tarihi', 'İNKILAP TARİHİ', 'T.C. İnkılap Tarihi', 'T.C. İnkılap Tarihi', 'inkılaptarihi',
                                          ['9b2c2c', '7f1d1d']),
    'cografya': ('cografya', 'COĞRAFYA', 'Coğrafya', 'Coğrafya', 'coğrafya',
                 ['2c7a7b', '319795', '285e61']),
    'biyoloji': ('biyoloji', 'BİYOLOJİ', 'Biyoloji', 'Biyoloji', 'biyoloji', ['2f855a', '276749', '1f9d55', '22543d']),
    'fizik': ('fizik', 'FİZİK', 'Fizik', 'Fizik', 'fizik', ['2451d6', '1e4e8c', '3182ce', '1a365d']),
    'kimya': ('kimya', 'KİMYA', 'Kimya', 'Kimya', 'kimya', ['9d174d', '1f6f8b', 'ad1457', 'c2366b']),
    'tarih': ('tarih', 'TARİH', 'Tarih', 'Tarih', 'tarih', ['822727', '9b2c2c', '7b341e']),
    'felsefe': ('felsefe', 'FELSEFE', 'Felsefe', 'Felsefe', 'felsefe', ['553c9a', '6b46c1']),
    'turk-dili-ve-edebiyati': ('edebiyat', 'EDEBİYAT', 'Türk Dili ve Edebiyatı', 'Türk Dili ve Edebiyatı', 'edebiyat',
                               ['744210', '633806', '5f370e']),
    'kuran-i-kerim': ('kuran-i-kerim', 'KUR’AN-I KERİM', 'Kur’an-ı Kerim', 'Kur’an-ı Kerim', 'kuranıkerim',
                      ['0f766e', '0e7490', '115e59', '155e75']),
    'peygamberimizin-hayati': ('peygamberimizin-hayati', 'PEYGAMBERİMİZİN HAYATI', 'Peygamberimizin Hayatı', 'Peygamberimizin Hayatı',
                               'peygamberimizinhayatı', ['15803d', '166534', '2d6a4f', '1f7a4d']),
    'temel-dini-bilgiler': ('temel-dini-bilgiler', 'TEMEL DİNÎ BİLGİLER', 'Temel Dinî Bilgiler', 'Temel Dinî Bilgiler', 'temeldinibilgiler',
                            ['4f46e5', '6d28d9', '4338ca', '7c3aed']),
    'mesleki-arapca': ('mesleki-arapca', 'MESLEKİ ARAPÇA', 'Mesleki Arapça', 'Mesleki Arapça', 'meslekiarapça', ['312e81', '1e1b4b']),
    'fikih': ('fikih', 'FIKIH', 'Fıkıh', 'Fıkıh', 'fıkıh', ['7c2d12', '9a3412', 'b45309']),
    'hadis': ('hadis', 'HADİS', 'Hadis', 'Hadis', 'hadis', ['065f46', '047857', '0f766e']),
    'siyer': ('siyer', 'SİYER', 'Siyer', 'Siyer', 'siyer', ['166534', '15803d', '14532d']),
    'akaid': ('akaid', 'AKAİD', 'Akaid', 'Akaid', 'akaid', ['4c1d95', '5b21b6', '6d28d9']),
    'dinler-tarihi': ('dinler-tarihi', 'DİNLER TARİHİ', 'Dinler Tarihi', 'Dinler Tarihi', 'dinlertarihi', ['78350f', '92400e', 'b45309']),
    'hitabet-ve-mesleki-uygulama': ('hitabet-ve-mesleki-uygulama', 'HİTABET', 'Hitabet ve Mesleki Uygulama', 'Hitabet ve Mesleki Uygulama',
                                    'hitabet', ['1e3a8a', '1d4ed8', '0369a1']),
    'tefsir': ('tefsir', 'TEFSİR', 'Tefsir', 'Tefsir', 'tefsir', ['115e59', '0f766e', '134e4a']),
    'islam-kultur-ve-medeniyeti': ('islam-kultur-ve-medeniyeti', 'İSLAM KÜLTÜRÜ', 'İslam Kültür ve Medeniyeti', 'İslam Kültür ve Medeniyeti',
                                   'islamkültürü', ['1e40af', '0369a1', '1d4ed8']),
    'kelam': ('kelam', 'KELAM', 'Kelam', 'Kelam', 'kelam', ['3730a3', '4338ca', '312e81']),
}

_fontlar = {}


def font(agirlik, boyut):
    anahtar = (agirlik, boyut)
    if anahtar not in _fontlar:
        _fontlar[anahtar] = ImageFont.truetype(str(FONTLAR / f'Poppins-{agirlik}.ttf'), boyut)
    return _fontlar[anahtar]


def rgb(hexrenk):
    hexrenk = hexrenk.lstrip('#')
    return tuple(int(hexrenk[i:i + 2], 16) for i in (0, 2, 4))


SUP_MAP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿˣʸ', '0123456789+-=()nxy')
SUB_MAP = str.maketrans('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓ', '0123456789+-=()aeox')
_SUP_RE = re.compile(r'[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿˣʸ]+')
_SUB_RE = re.compile(r'[₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓ]+')


def metin_hazirla(metin):
    """Karekök içi ve çarpım/eşitlik içeren matematik ifadelerinin satır ortasında bölünmesini önler."""
    metin = metin.replace('\u0394', '\u2206')
    # √(...) içindeki boşlukları bölünmez boşluk (\u00a0) yap
    def _kok_ic(m):
        return '√(' + m.group(1).replace(' ', '\u00a0') + ')'
    s = re.sub(r'√\(([^)]+)\)', _kok_ic, metin)
    # · 10^ veya = √ veya a^(-n) = 1 / a^n gibi ifadeleri birbirine bağla
    s = re.sub(r'([^\t\n\r ]+)\s+·\s+(10\^[^\t\n\r ,.;:)]+)', lambda m: f'{m.group(1)}\u00a0·\u00a0{m.group(2)}', s)
    s = re.sub(r'(√[^\t\n\r ]+)\s*=\s*(√[^\t\n\r ]+)\s*=\s*([^\t\n\r ,.;:]+)', lambda m: f'{m.group(1)}\u00a0=\u00a0{m.group(2)}\u00a0=\u00a0{m.group(3)}', s)
    s = re.sub(r'(a\^\(-n\))\s*=\s*(1)\s*/\s*(a\^n)', lambda m: f'{m.group(1)}\u00a0=\u00a01\u00a0/\u00a0{m.group(3)}', s)
    return s


def _normalize_sup_sub(s):
    s = _SUP_RE.sub(lambda m: '^(' + m.group(0).translate(SUP_MAP) + ')', s)
    s = _SUB_RE.sub(lambda m: '_(' + m.group(0).translate(SUB_MAP) + ')', s)
    return s


def _parcala_ic(s):
    """Üs (^), alt indis (_) ve normal metin parçalarını ayrıştırır."""
    dugumler = []
    i, n = 0, len(s)
    buf = []
    while i < n:
        ch = s[i]
        if ch in ('^', '_') and i + 1 < n:
            if buf:
                dugumler.append(('text', ''.join(buf)))
                buf = []
            tip = 'sup' if ch == '^' else 'sub'
            if s[i + 1] == '(':
                kapanis = s.find(')', i + 2)
                if kapanis != -1:
                    ic = s[i + 2:kapanis].replace('-', '−')
                    dugumler.append((tip, ic))
                    i = kapanis + 1
                    continue
            m = re.match(r'[0-9A-Za-zçğıöşüÇĞİÖŞÜ+-]+', s[i + 1:])
            if m:
                ic = m.group(0).replace('-', '−')
                dugumler.append((tip, ic))
                i += 1 + len(m.group(0))
                continue
        buf.append(ch)
        i += 1
    if buf:
        dugumler.append(('text', ''.join(buf)))
    return dugumler


def parcala(soz):
    """Bir sözcüğü/ifadeyi ('text', ...), ('sup', ...), ('sub', ...), ('sqrt', [...]) düğümlerine ayırır."""
    s = _normalize_sup_sub(soz.replace('\u00a0', ' '))
    dugumler = []
    i, n = 0, len(s)
    buf = []
    while i < n:
        if s[i] == '√':
            if buf:
                dugumler.extend(_parcala_ic(''.join(buf)))
                buf = []
            if i + 1 < n and s[i + 1] == '(':
                # Eşleşen parantezi bul
                derinlik = 0
                kapanis = -1
                for j in range(i + 1, n):
                    if s[j] == '(':
                        derinlik += 1
                    elif s[j] == ')':
                        derinlik -= 1
                        if derinlik == 0:
                            kapanis = j
                            break
                if kapanis != -1:
                    ic = s[i + 2:kapanis]
                    dugumler.append(('sqrt', _parcala_ic(ic)))
                    i = kapanis + 1
                    continue
            m = re.match(r'[0-9A-Za-zçğıöşüÇĞİÖŞÜπ]+(?:\^\([^)]+\)|\^[0-9A-Za-zçğıöşüÇĞİÖŞÜ+-]+)?', s[i + 1:])
            if m:
                ic = m.group(0)
                dugumler.append(('sqrt', _parcala_ic(ic)))
                i += 1 + len(ic)
                continue
            dugumler.append(('sqrt', []))
            i += 1
        else:
            buf.append(s[i])
            i += 1
    if buf:
        dugumler.extend(_parcala_ic(''.join(buf)))
    return dugumler


def dugum_genislik(dugum, agirlik, boyut):
    tip, deger = dugum
    f = font(agirlik, boyut)
    if tip == 'text':
        return f.getlength(deger)
    if tip in ('sup', 'sub'):
        alt_ag = 600 if agirlik == 500 else agirlik
        alt_b = round(boyut * 0.60)
        return font(alt_ag, alt_b).getlength(deger) + round(boyut * 0.03)
    if tip == 'sqrt':
        rw = f.getlength('√')
        if not deger:
            return round(rw * 0.90) + round(boyut * 0.34)
        ic_gen = sum(dugum_genislik(d, agirlik, boyut) for d in deger)
        return round(rw * 0.95) + ic_gen + round(boyut * 0.10)
    return 0.0


def metin_genislik(metin, agirlik, boyut):
    return sum(dugum_genislik(d, agirlik, boyut) for d in parcala(metin))


def metin_ciz(draw, xy, metin, agirlik, boyut, dolgu):
    x, y = xy
    f = font(agirlik, boyut)
    for tip, deger in parcala(metin):
        if tip == 'text':
            draw.text((x, y), deger, font=f, fill=dolgu, anchor='ls')
            x += f.getlength(deger)
        elif tip == 'sup':
            alt_ag = 600 if agirlik == 500 else agirlik
            alt_b = round(boyut * 0.60)
            af = font(alt_ag, alt_b)
            draw.text((x + round(boyut * 0.015), y - round(boyut * 0.36)), deger, font=af, fill=dolgu, anchor='ls')
            x += af.getlength(deger) + round(boyut * 0.03)
        elif tip == 'sub':
            alt_ag = 600 if agirlik == 500 else agirlik
            alt_b = round(boyut * 0.60)
            af = font(alt_ag, alt_b)
            draw.text((x + round(boyut * 0.015), y + round(boyut * 0.18)), deger, font=af, fill=dolgu, anchor='ls')
            x += af.getlength(deger) + round(boyut * 0.03)
        elif tip == 'sqrt':
            rw = f.getlength('√')
            _, y0, _, _ = f.getbbox('√', anchor='ls')
            kalinlik = max(3, round(boyut * (0.105 if agirlik >= 700 else 0.078)))
            draw.text((x, y), '√', font=f, fill=dolgu, anchor='ls')
            bar_x0 = x + round(rw * (0.85 if agirlik >= 700 else 0.81))
            bar_y0 = y + y0
            if not deger:
                bar_x1 = bar_x0 + round(boyut * 0.32)
                draw.rectangle((bar_x0, bar_y0, bar_x1, bar_y0 + kalinlik), fill=dolgu)
                x += round(rw * 0.90) + round(boyut * 0.34)
            else:
                ic_x = x + round(rw * 0.95)
                for alt_d in deger:
                    alt_tip, alt_deg = alt_d
                    if alt_tip == 'text':
                        draw.text((ic_x, y), alt_deg, font=f, fill=dolgu, anchor='ls')
                    elif alt_tip == 'sup':
                        alt_ag = 600 if agirlik == 500 else agirlik
                        alt_b = round(boyut * 0.54)
                        draw.text((ic_x + round(boyut * 0.015), y - round(boyut * 0.26)), alt_deg, font=font(alt_ag, alt_b), fill=dolgu, anchor='ls')
                    elif alt_tip == 'sub':
                        alt_ag = 600 if agirlik == 500 else agirlik
                        alt_b = round(boyut * 0.60)
                        draw.text((ic_x + round(boyut * 0.015), y + round(boyut * 0.18)), alt_deg, font=font(alt_ag, alt_b), fill=dolgu, anchor='ls')
                    ic_x += dugum_genislik(alt_d, agirlik, boyut)
                bar_x1 = ic_x + round(boyut * 0.07)
                draw.rectangle((bar_x0, bar_y0, bar_x1, bar_y0 + kalinlik), fill=dolgu)
                x = bar_x1 + round(boyut * 0.03)
    return x - xy[0]


def sar(metin, agirlik, boyut, genislik):
    """Sözcükleri satırlara böler; tek sözcük bile sığmıyorsa olduğu gibi bırakır."""
    hazir = metin_hazirla(metin)
    satirlar, satir = [], ''
    for soz in re.split(r'[ \t\n\r]+', hazir.strip()):
        if not soz:
            continue
        deneme = f'{satir} {soz}'.strip()
        if metin_genislik(deneme, agirlik, boyut) <= genislik or not satir:
            satir = deneme
        else:
            satirlar.append(satir)
            satir = soz
    if satir:
        satirlar.append(satir)
    return satirlar


def aralikli(draw, xy, metin, f, dolgu, aralik, hiza='l'):
    """Harf aralıklı yazı (rozet ve etiketler). hiza: l = soldan, r = sağdan."""
    x, y = xy
    genislik = sum(f.getlength(h) for h in metin) + aralik * (len(metin) - 1)
    if hiza == 'r':
        x -= genislik
    for h in metin:
        draw.text((x, y), h, font=f, fill=dolgu, anchor='ls')
        x += f.getlength(h) + aralik
    return genislik


def coz(kimlik):
    """İçerik dosyasını okur, özet bilgisiyle birleştirir."""
    icerik = json.loads((ICERIK / f'{kimlik}.json').read_text(encoding='utf-8'))
    m = re.fullmatch(r'(\d+)-(.+)-(\d+)', icerik['ozet'])
    if not m:
        raise ValueError(f'{kimlik}: ozet alanı sınıf-ders-hafta biçiminde olmalı')
    sinif, ders, hafta = int(m.group(1)), m.group(2), int(m.group(3))
    if ders not in DERSLER:
        raise ValueError(f'{kimlik}: {ders} için DERSLER tablosunda kayıt yok')
    dosya, rozet, altlik, ad, etiket, palet = DERSLER[ders]
    beklenen = f'bilgi-{sinif}-{dosya}-{hafta}'
    if kimlik != beklenen:
        raise ValueError(f'{kimlik}: dosya adı {beklenen} olmalı')
    renk = icerik.get('renk') or palet[(sinif + hafta) % len(palet)]
    return dict(icerik, kimlik=kimlik, sinif=sinif, ders=ders, hafta=hafta, rozet=rozet, altlik=altlik, ad=ad,
                etiket=etiket, renk=renk.lstrip('#'), sayfa=f'{sinif}-{ders}-hafta-{hafta}')


def ciz(v):
    """Kartı çizer; (görsel, bilgi) döndürür. bilgi: başlık/paragraf boyutları ve taşma durumu."""
    vurgu = rgb(v['renk'])
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)

    # gövdedeki nokta ızgarası
    for y in range(UST_H + 24, ALT_Y, 48):
        for x in range(24, W, 48):
            d.ellipse((x - 1, y - 1, x + 2, y + 2), fill='#e2e6ef')

    # saydam daire + soru işareti (gövdeyle sınırlı)
    katman = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    kd = ImageDraw.Draw(katman)
    kd.ellipse((1115 - 322, 1115 - 322, 1115 + 322, 1115 + 322), fill=vurgu + (30,))
    kd.text((935, 1045), '?', font=font(800, 400), fill=vurgu + (62,), anchor='mm')
    maske = Image.new('L', (W, H), 0)
    ImageDraw.Draw(maske).rectangle((0, UST_H, W, ALT_Y), fill=255)
    katman.putalpha(ImageChops.multiply(katman.getchannel('A'), maske))
    im = Image.alpha_composite(im.convert('RGBA'), katman).convert('RGB')
    d = ImageDraw.Draw(im)

    # üst şerit: logo, yazı markası, rozet
    d.rectangle((0, 0, W, UST_H), fill=NAVY)
    logo = Image.open(LOGO).convert('RGBA').resize((131, 131), Image.LANCZOS)
    im.paste(logo, (72, 42), logo)
    d.text((213, 102), 'DERS ', font=font(800, 44), fill=BEYAZ, anchor='ls')
    d.text((213 + font(800, 44).getlength('DERS '), 102), 'KUTUSU', font=font(800, 44), fill=ACIK_MAVI, anchor='ls')
    aralikli(d, (215, 135), 'DERSKUTUSU.COM', font(700, 22), GOLD, 0.3)
    rozet = f'{v["sinif"]}. SINIF · {v["rozet"]}'
    rf = font(700, 25)
    rg = sum(rf.getlength(h) for h in rozet) + 1.3 * (len(rozet) - 1)
    d.rounded_rectangle((1016 - rg - 36, 82, 1016, 128), radius=23, fill=vurgu)
    aralikli(d, (1016 - 18, 114), rozet, rf, BEYAZ, 1.3, 'r')

    # gövde: etiket, başlık, çizgi, paragraflar (sığmazsa küçült)
    aralikli(d, (KENAR, 292), 'BUNU BİLİYOR MUYDUNUZ?', font(800, 31), '#' + v['renk'], 1.4)
    bb, pb = 68, 37
    while True:
        baslik = sar(v['baslik'], 800, bb, W - 2 * KENAR)
        bsatir = round(bb * 1.15)
        psatir = round(pb * 1.36)
        y = 342 + round(bb * 0.70)                    # ilk satırın taban çizgisi
        y_son = y + bsatir * (len(baslik) - 1)
        cizgi_y = y_son + round(bb * 0.53)
        py = cizgi_y + 10 + round(pb * 1.97)
        paragraflar = [sar(p, 500, pb, W - 2 * KENAR - 20) for p in v['paragraflar']]
        satir_sayisi = sum(len(p) for p in paragraflar)
        alt = py + psatir * (satir_sayisi - 1) + round(pb * 0.68) * (len(paragraflar) - 1) + round(pb * 0.3)
        if alt <= ALT_Y - 40 or (bb <= 54 and pb <= 30):
            break
        bb, pb = max(54, bb - 2), max(30, pb - 1)
    for i, satir in enumerate(baslik):
        metin_ciz(d, (KENAR, y + bsatir * i), satir, 800, bb, NAVY)
    d.rounded_rectangle((KENAR, cizgi_y, KENAR + 160, cizgi_y + 10), radius=5, fill=vurgu)
    for p in paragraflar:
        for satir in p:
            metin_ciz(d, (KENAR, py), satir, 500, pb, METIN)
            py += psatir
        py += round(pb * 0.68)

    # altlık
    d.rectangle((0, ALT_Y, W, H), fill=vurgu)
    d.text((KENAR, 1260), f'{v["sinif"]}. sınıf {v["altlik"]} · {v["hafta"]}. hafta konu özeti', font=font(700, 30), fill=BEYAZ, anchor='ls')
    d.text((KENAR, 1302), 'Özet, çözümlü örnekler ve etkinlikler sitemizde', font=font(500, 25), fill=BEYAZ, anchor='ls')
    d.text((1008, 1284), 'derskutusu.com', font=font(800, 35), fill=BEYAZ, anchor='rs')
    return im, dict(baslik_boyut=bb, paragraf_boyut=pb, baslik_satir=len(baslik), paragraf_satir=satir_sayisi, alt=alt)


_TO_SUP = str.maketrans('0123456789+-=()nxy', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿˣʸ')


def _metin_us_temizle(s):
    s = re.sub(r'\^\(([^)]+)\)', lambda m: m.group(1).translate(_TO_SUP), s)
    s = re.sub(r'\^([0-9nxy+-]+)', lambda m: m.group(1).translate(_TO_SUP), s)
    return s


def gonderi_metni(v):
    bilgi = _metin_us_temizle(v["bilgi"].strip())
    return (f'Bunu biliyor muydunuz? {bilgi}\n'
            'Faydalı bulduysanız arkadaşınızı etiketleyin.\n'
            f'📘 {v["sinif"]}. sınıf {v["ad"]} {v["hafta"]}. hafta konu özeti, çözümlü örnekler ve etkinlikler ücretsiz burada 👉 '
            f'derskutusu.com/ozet/{v["sayfa"]}\n'
            f'#derskutusu #{v["etiket"]} #{v["sinif"]}sınıf #bunubiliyormuydunuz #maarifmodeli')


def kuyruk_ekle(kimlikler, baslangic, saatler=(9, 11, 13, 15, 17, 19)):
    k = json.loads(KUYRUK.read_text(encoding='utf-8'))
    varolan = {g['kimlik'] for g in k['gonderiler']}
    zaman = datetime.fromisoformat(baslangic).replace(tzinfo=TSI)
    eklenen = 0
    for kimlik in kimlikler:
        if kimlik in varolan:
            continue
        v = coz(kimlik)
        while zaman.hour not in saatler:
            zaman = (zaman + timedelta(hours=1)).replace(minute=0)
        k['gonderiler'].append({'kimlik': kimlik, 'zaman': zaman.isoformat(timespec='minutes'),
                                'gorsel': f'https://derskutusu.com/sosyal/{kimlik}.png',
                                'metin': gonderi_metni(v), 'hedef': ['instagram', 'facebook'], 'durum': {}})
        zaman += timedelta(hours=1)
        eklenen += 1
    KUYRUK.write_text(json.dumps(k, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return eklenen


def bekleyen_listesi():
    """Paylaşılmamış gönderileri elle paylaşım için sosyal/bekleyen.md dosyasına yazar."""
    k = json.loads(KUYRUK.read_text(encoding='utf-8'))
    bekleyen = [g for g in k['gonderiler'] if any(not g['durum'].get(h) for h in g['hedef'])]
    satirlar = ['# Paylaşım bekleyen gönderiler', '',
                'Her gönderi için: görseli indirin, Meta Business Suite\'te Facebook sayfası + Instagram seçip görseli ekleyin, metni yapıştırın, paylaşın; '
                'aynı görseli hikâye olarak da paylaşın. Paylaşınca bu oturuma "paylaştım" yazın, kuyruk güncellenir.', '',
                f'Toplam {len(bekleyen)} gönderi.', '']
    for g in bekleyen:
        kanallar = ', '.join(h for h in g['hedef'] if not g['durum'].get(h))
        satirlar += [f'## {g["kimlik"]}', f'Sıra: {g["zaman"][:16].replace("T", " ")} · Bekleyen: {kanallar} · Görsel: {g["gorsel"]}', '',
                     '```', g['metin'], '```', '']
    (KOK / 'sosyal' / 'bekleyen.md').write_text('\n'.join(satirlar), encoding='utf-8')
    return len(bekleyen)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('kimlikler', nargs='*', help='üretilecek kart kimlikleri (boşsa görseli olmayanlar)')
    ap.add_argument('--hepsi', action='store_true', help='var olan görselleri de yeniden üret')
    ap.add_argument('--kuyruk', metavar='BASLANGIC', help='kuyrukta olmayan içerikleri bu andan başlayarak ekle (ör. 2026-10-13T09:00)')
    ap.add_argument('--cikti', help='görselleri bu dizine yaz (deneme için)')
    ap.add_argument('--liste', action='store_true', help='paylaşılmamış gönderileri sosyal/bekleyen.md dosyasına yaz')
    a = ap.parse_args()
    hepsi = sorted(p.stem for p in ICERIK.glob('bilgi-*.json'))
    cikti = Path(a.cikti) if a.cikti else CIKTI
    cikti.mkdir(parents=True, exist_ok=True)
    secili = a.kimlikler or [k for k in hepsi if a.hepsi or not (cikti / f'{k}.png').exists()]
    for kimlik in secili:
        v = coz(kimlik)
        for alan in ('baslik', 'paragraflar', 'bilgi'):
            if not v.get(alan):
                raise ValueError(f'{kimlik}: {alan} alanı boş')
        if any('\u0600' <= h <= '\u06ff' for h in v['baslik'] + ''.join(v['paragraflar'])):
            raise ValueError(f'{kimlik}: kart metninde Arap harfi var; Poppins bunu çizemez, çeviri yazı kullanın (bilgi alanında kalabilir)')
        im, bilgi = ciz(v)
        im.save(cikti / f'{kimlik}.png', optimize=True)
        im.save(cikti / f'{kimlik}.jpg', quality=90, optimize=True)   # Instagram API yalnız JPEG kabul eder
        uyari = ' KÜÇÜLTÜLDÜ' if bilgi['baslik_boyut'] < 68 else ''
        print(f'{kimlik}: başlık {bilgi["baslik_satir"]} satır/{bilgi["baslik_boyut"]}px, '
              f'paragraf {bilgi["paragraf_satir"]} satır/{bilgi["paragraf_boyut"]}px, alt {bilgi["alt"]}{uyari}')
    if a.kuyruk:
        print(f'kuyruğa {kuyruk_ekle(hepsi, a.kuyruk)} gönderi eklendi')
    if a.liste or a.kuyruk:
        print(f'sosyal/bekleyen.md: {bekleyen_listesi()} gönderi bekliyor')


if __name__ == '__main__':
    sys.exit(main())
