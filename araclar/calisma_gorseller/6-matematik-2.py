"""6. sınıf Matematik 2. hafta (2, 3, 4, 5, 6, 9 ve 10 ile Bölünebilme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def dort_sayi_karti():
    kartlar = [
        ('1. Kart', '2 514', 'Son iki: 14 · Top.: 12', MAVI, MAVI_A),
        ('2. Kart', '3 456', 'Son iki: 56 · Top.: 18', YES, YES_A),
        ('3. Kart', '4 726', 'Son iki: 26 · Top.: 19', TUR, TUR_A),
        ('4. Kart', '5 130', 'Son iki: 30 · Top.: 9', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sayi, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 84, arka, renk, 9, 1.6)
        ic += yazi(x + 68, 26, bas, 10.8, renk)
        ic += yazi(x + 68, 52, sayi, 12.2, LAC)
        ic += yazi(x + 68, 76, alt, 10, SOLUK, ince=True)
    return svg(600, 100, ic, 'Dört sayı kartı: 2 514, 3 456, 4 726 ve 5 130.', 22)


def basamak_karti_54a2():
    ic = kutu(8, 6, 584, 88, MAVI_A, MAVI, 10, 1.6)
    ic += yazi(300, 24, '3 ile Kalansız Bölünen Dört Basamaklı Doğal Sayı', 10.8, MAVI)
    haneler = [('5', LAC, '#fff'), ('4', LAC, '#fff'), ('a', TUR, TUR_A), ('2', LAC, '#fff')]
    for i, (h, r, z) in enumerate(haneler):
        x = 76 + i * 74
        ic += kutu(x, 34, 62, 46, z, r, 8, 1.6)
        ic += yazi(x + 31, 63, h, 12.5, r)
    ic += kutu(390, 34, 186, 46, '#fff', MAVI, 8, 1.4)
    ic += yazi(483, 54, '5 + 4 + a + 2 = 11 + a', 10.6, LAC)
    ic += yazi(483, 72, '(3’ün katı olmalı)', 10.2, MAVI, ince=True)
    return svg(600, 100, ic, '5 4a2 dört basamaklı sayısı ve rakamlar toplamı 11+a koşulu.', 22)


def kontrol_panosu_sayilar():
    sayilar = [
        ('1 260', 'Son: 0 · Son iki: 60', MAVI, MAVI_A),
        ('2 316', 'Son: 6 · Son iki: 16', YES, YES_A),
        ('4 275', 'Son: 5 · Son iki: 75', TUR, TUR_A),
        ('3 500', 'Son: 0 · Son iki: 00', MOR, MOR_A),
    ]
    ic = ''
    for i, (s, alt, renk, arka) in enumerate(sayilar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 78, arka, renk, 9, 1.6)
        ic += yazi(x + 68, 34, s, 12, LAC)
        ic += yazi(x + 68, 62, alt, 10, renk, ince=True)
    return svg(600, 94, ic, 'Kontrol panosundaki dört sayı: 1 260, 2 316, 4 275 ve 3 500.', 22)


def kargo_kolisi_73b0():
    ic = kutu(8, 6, 584, 88, TUR_A, TUR, 10, 1.6)
    ic += kutu(24, 18, 210, 64, '#e6b87d', '#8a5a2b', 6, 1.5)
    ic += kutu(94, 18, 70, 16, '#fffdf5', '#8a5a2b', 2, 1)
    ic += yazi(129, 30, 'KARGO', 10.2, '#8a5a2b')
    ic += yazi(129, 56, 'Kod : 7 3b0', 12, LAC)
    ic += yazi(129, 74, '(4 basamaklı)', 10, SOLUK, ince=True)
    ic += kutu(256, 18, 320, 64, '#fff', TUR, 8, 1.4)
    ic += yazi(416, 38, 'Koli Takip Kodu Koşulları:', 10.8, TUR)
    ic += yazi(416, 56, '4 ile kalansız bölünür (son iki basamak: b0)', 10.3, LAC, ince=True)
    ic += yazi(416, 74, '9 ile kalansız bölünür (7 + 3 + b + 0 = 9’un katı)', 10.3, LAC, ince=True)
    return svg(600, 100, ic, 'Kargo kolisi takip kodu 7 3b0: hem 4’e hem 9’a kalansız bölünür.', 22)


def iki_kosul_adimlari():
    adimlar = [
        ('1. Adım (5 Kuralı)', 'b = 0 veya b = 5', MAVI, MAVI_A),
        ('2. Adım (Çift Olma)', '6 için çift: b = 0', TUR, TUR_A),
        ('3. Adım (3 Kuralı)', '4 + 3 + a + 0 = 7 + a', MOR, MOR_A),
        ('4. Adım (Sonuç)', 'a ∈ {2, 5, 8}', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 136, 76, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 136, 24, renk, renk, 9, 1)
        ic += yazi(x + 68, 24, bas, 10.4, '#fff')
        ic += yazi(x + 68, 56, alt, 10.6, LAC)
    return svg(600, 92, ic, '4 3ab sayısının 5 ve 6 ile bölünebilme çözüm basamakları.', 22)


def bolen_filtre_semasi():
    ic = kutu(8, 8, 282, 84, YES_A, YES, 9, 1.6)
    ic += yazi(149, 26, '1. Giriş Sayısı: 540', 11.2, YES)
    ic += yazi(149, 48, 'Son rakam: 0 · Son iki basamak: 40', 10.3, LAC, ince=True)
    ic += yazi(149, 68, 'Rakamlar toplamı: 5 + 4 + 0 = 9', 10.4, YES)

    ic += kutu(310, 8, 282, 84, TUR_A, TUR, 9, 1.6)
    ic += yazi(451, 26, '2. Giriş Sayısı: 635', 11.2, TUR)
    ic += yazi(451, 48, 'Son rakam: 5 · Son iki basamak: 35', 10.3, LAC, ince=True)
    ic += yazi(451, 68, 'Rakamlar toplamı: 6 + 3 + 5 = 14', 10.4, TUR)
    return svg(600, 100, ic, '540 ve 635 sayılarının basamak ve rakamlar toplamı filtre kartları.', 22)


def dolap_kilidi_64k():
    ic = kutu(8, 8, 584, 82, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(24, 18, 170, 62, LAC, LAC, 8, 1.4)
    ic += yazi(109, 38, 'DOLAP ŞİFRESİ', 10.4, '#fff')
    ic += yazi(109, 64, '6 4 k', 12.5, ALTIN)
    ic += kutu(214, 18, 362, 62, '#fff', MAVI, 8, 1.4)
    ic += yazi(395, 40, 'Kural: 64k sayısı 6 ile tam bölünmektedir.', 10.6, MAVI)
    ic += yazi(395, 62, 'İpucu: Sayı hem 2’ye (çift) hem 3’e tam bölünmelidir.', 10.2, LAC, ince=True)
    return svg(600, 98, ic, 'Üç basamaklı 64k dolap şifresi ve 6 ile tam bölünebilme koşulu.', 22)


def karsi_ornek_karti():
    ic = kutu(8, 8, 282, 82, KIR_A, KIR, 9, 1.6)
    ic += yazi(149, 26, '1. Yanılgı İddiası', 10.8, KIR)
    ic += yazi(149, 48, '“3 ile bölünen her doğal sayı', 10.4, LAC, ince=True)
    ic += yazi(149, 66, 'mutlaka 9 ile de bölünür.”', 10.4, LAC, ince=True)

    ic += kutu(310, 8, 282, 82, TUR_A, TUR, 9, 1.6)
    ic += yazi(451, 26, '2. Yanılgı İddiası', 10.8, TUR)
    ic += yazi(451, 48, '“Birler basamağı çift olan her sayı', 10.4, LAC, ince=True)
    ic += yazi(451, 66, 'mutlaka 4 ile de bölünür.”', 10.4, LAC, ince=True)
    return svg(600, 98, ic, 'Karşı örnekle çürütülecek iki bölünebilme yanılgısı kartı.', 22)


def simit_paket_karti():
    ic = kutu(8, 8, 584, 82, KUM, ALTIN, 9, 1.6)
    ic += yazi(300, 26, 'FIRIN PAKETLEME PLANI · TOPLAM 468 ADET SİMİT', 10.8, LAC)
    ic += kutu(24, 36, 264, 42, YES_A, YES, 7, 1.4)
    ic += yazi(156, 54, '1. Seçenek: 6’şarlı Paketler', 10.5, YES)
    ic += yazi(156, 70, '(2 ve 3 kuralı birlikte)', 10, LAC, ince=True)
    ic += kutu(312, 36, 264, 42, MAVI_A, MAVI, 7, 1.4)
    ic += yazi(444, 54, '2. Seçenek: 9’arlı Paketler', 10.5, MAVI)
    ic += yazi(444, 70, '(9 ile bölünebilme kuralı)', 10, LAC, ince=True)
    return svg(600, 96, ic, '468 simidin 6’şarlı ve 9’arlı paketlere kalansız bölünebilme incelemesi.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_sayi_karti()
    s[4]['gorsel'] = basamak_karti_54a2()
    s[5]['gorsel'] = kontrol_panosu_sayilar()
    s[6]['gorsel'] = kargo_kolisi_73b0()
    s[7]['gorsel'] = iki_kosul_adimlari()
    s[8]['gorsel'] = bolen_filtre_semasi()
    s[9]['gorsel'] = dolap_kilidi_64k()
    s[10]['gorsel'] = karsi_ornek_karti()
    s[12]['gorsel'] = simit_paket_karti()
