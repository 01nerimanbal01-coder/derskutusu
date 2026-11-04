"""7. sınıf Matematik 5. hafta (Rasyonel Sayılarda Karşılaştırma, Sıralama ve Yoğunluk) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); eğik kesir yok (K155); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dikey_kesir(cx, cy, isaret, pay, payda, renk=LAC):
    """Dikey kesir çizer (K155 uyumlu, eğik çizgi yok)."""
    ic = ''
    dx = 0
    if isaret:
        ic += yazi(cx - 14, cy + 4, isaret, renk)
        dx = 6
    ic += yazi(cx + dx, cy - 5, str(pay), renk)
    ic += f'<line x1="{cx + dx - 11}" y1="{cy - 1}" x2="{cx + dx + 11}" y2="{cy - 1}" stroke="{renk}" stroke-width="1.5"/>'
    ic += yazi(cx + dx, cy + 13, str(payda), renk)
    return ic


def soguk_hava_depolari():
    """Soru 1: K (-7/4), L (-3/8), M (-5/2), N (-9/8) soğuk hava depoları."""
    depolar = [
        ('K Deposu', 7, 4, MAVI, MAVI_A, 6),
        ('L Deposu', 3, 8, YES, YES_A, 94),
        ('M Deposu', 5, 2, TUR, TUR_A, 182),
        ('N Deposu', 9, 8, MOR, MOR_A, 270),
    ]
    ic = ''
    for ad, pay, payda, r, z, x in depolar:
        ic += kutu(x, 6, 84, 78, z, r, 7, 1.4)
        ic += yazi(x + 42, 24, ad, r)
        ic += dikey_kesir(x + 36, 56, '−', pay, payda, LAC)
        ic += yazi(x + 68, 60, '°C', r)
    return svg(360, 90, ic, 'Dört soğuk hava deposunun rasyonel sıcaklık değerleri.', 16)


def siralama_strateji_karti():
    """Soru 2: Karşılaştırma stratejileri özet kartı."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Rasyonel Sayılarda Karşılaştırma İlkeleri', KAHVE)
    ilkeler = [
        ('Eşit Pay', 'Paydası küçük olan >', MAVI, MAVI_A, 10),
        ('Negatif Sayı', '0’a yakın olan >', KIR, KIR_A, 126),
        ('Zıt İşaret', 'Pozitif (+) > Negatif (−)', YES, YES_A, 242),
    ]
    for bas, alt, r, z, x in ilkeler:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Rasyonel sayıları karşılaştırmada üç temel ilke kartı.', 16)


def tarti_kavanoz_kartlari():
    """Soru 4: x = 3/8, y = 6/13, z = 2/5 kütle kartları."""
    kartlar = [
        ('x Kavanozu', 3, 8, MAVI, MAVI_A, 6),
        ('y Kavanozu', 6, 13, TUR, TUR_A, 126),
        ('z Kavanozu', 2, 5, YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, '#f8fafc', GRI, 8, 1.3)
    for ad, pay, payda, r, z, x in kartlar:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.4)
        ic += yazi(x + 54, 28, ad, r)
        ic += dikey_kesir(x + 42, 56, '', pay, payda, LAC)
        ic += yazi(x + 74, 60, 'kg', r)
    return svg(360, 94, ic, 'Üç kavanozun rasyonel sayı cinsinden kütle kartları.', 16)


def bilinmeyenli_esitsizlik_seridi():
    """Soru 5: -2/3 < m/15 < -1/5 eşitsizlik şeridi."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Payda Eşitleme İle Tam Sayı Değerlerini Bulma', MOR)
    ic += kutu(24, 28, 312, 52, '#fff', MOR, 6, 1.3)
    ic += dikey_kesir(86, 54, '−', 2, 3, KIR)
    ic += yazi(132, 58, '&lt;', LAC)
    ic += dikey_kesir(178, 54, '', 'm', 15, MAVI)
    ic += yazi(224, 58, '&lt;', LAC)
    ic += dikey_kesir(270, 54, '−', 1, 5, KIR)
    return svg(360, 94, ic, 'Eksi iki bölü üç ile eksi bir bölü beş arasındaki m bölü on beş eşitsizliği.', 16)


def yogunluk_sayi_dogrusu():
    """Soru 7: 3/7 ile 4/7 tam ortasındaki K noktası sayı doğrusu."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Rasyonel Sayılarda Yoğunluk · Tam Orta Nokta (K)', MAVI)
    ic += f'<line x1="40" y1="52" x2="320" y2="52" stroke="{LAC}" stroke-width="2.2"/>'
    for x, renk in [(70, MAVI), (180, KIR), (290, MAVI)]:
        ic += f'<circle cx="{x}" cy="52" r="5" fill="{renk}"/>'
    ic += dikey_kesir(70, 74, '', 3, 7, MAVI)
    ic += yazi(180, 38, 'K (Orta Nokta)', KIR)
    ic += yazi(180, 76, '2 ile genişlet: ? ÷ 14', LAC, 'middle', True)
    ic += dikey_kesir(290, 74, '', 4, 7, MAVI)
    return svg(360, 96, ic, 'Üç bölü yedi ile dört bölü yedi tam ortasındaki K noktasını gösteren sayı doğrusu.', 16)


def negatif_siralama_adimlari():
    """Soru 8: Negatif rasyonel sayıları sıralama 4 adımı."""
    adimlar = [
        ('1. Adım', 'Pozitif kabul et', MAVI, MAVI_A, 6),
        ('2. Adım', 'Paydaları 10 yap', TUR, TUR_A, 94),
        ('3. Adım', 'Pozitif sırala', MOR, MOR_A, 182),
        ('4. Adım', 'Yönü ters çevir', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Negatif rasyonel sayıları sıralamanın dört işlem basamağı.', 15)


def devirli_ondalik_fisleri():
    """Soru 9: A = 3,6161..., B = 3,6111..., C = 3,6100... basamak açılımı."""
    fisler = [
        ('A Çözeltisi', '3,6161...', MAVI, MAVI_A, 6),
        ('B Çözeltisi', '3,6111...', TUR, TUR_A, 126),
        ('C Çözeltisi', '3,6100...', YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, '#f8fafc', GRI, 8, 1.3)
    for bas, deger, r, z, x in fisler:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.4)
        ic += yazi(x + 54, 32, bas, r)
        ic += yazi(x + 54, 60, deger, LAC)
    return svg(360, 94, ic, 'Üç çözeltinin devirli ve sonlu ondalık basamak açılımları.', 16)


def yarima_butune_yakinlik_karti():
    """Soru 12: 1/8 (0'a yakın), 5/9 (1/2'ye yakın), 11/12 (1'e yakın) kartları."""
    kartlar = [
        ('Sıfıra (0) Yakın', 1, 8, MAVI, MAVI_A, 6),
        ('Yarıma Yakın', 5, 9, TUR, TUR_A, 126),
        ('Bütüne (1) Yakın', 11, 12, YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    for bas, pay, payda, r, z, x in kartlar:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.3)
        ic += yazi(x + 54, 28, bas, r)
        ic += dikey_kesir(x + 54, 58, '', pay, payda, LAC)
    return svg(360, 94, ic, 'Sıfıra, yarıma ve bir bütüne yakın rasyonel sayı kartları.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = soguk_hava_depolari()
    s[1]['gorsel'] = siralama_strateji_karti()
    s[3]['gorsel'] = tarti_kavanoz_kartlari()
    s[4]['gorsel'] = bilinmeyenli_esitsizlik_seridi()
    s[6]['gorsel'] = yogunluk_sayi_dogrusu()
    s[7]['gorsel'] = negatif_siralama_adimlari()
    s[8]['gorsel'] = devirli_ondalik_fisleri()
    s[11]['gorsel'] = yarima_butune_yakinlik_karti()
