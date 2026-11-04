"""5. sınıf Matematik 9. hafta (Çok Basamaklı Doğal Sayıları Okuma ve Yazma - Milyonlar Bölüğü) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def gunes_dunya_mesafe_karti():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 23, 'Astronomi Veri Kartı · Dünya – Güneş Uzaklığı', 10.5, TUR)
    ic += yazi(180, 46, 'Okunuşu: «Yüz kırk dokuz milyon altı yüz bin» km', 10.2, LAC)
    ic += yazi(180, 67, 'Milyonlar: 149  |  Binler: 600  |  Birler: ?', 9.8, TUR, ince=True)
    return svg(360, 88, ic, 'Dünya ile Güneş arasındaki uzaklığın okunuşu kartı.', 15)


def dort_sayi_veri_kartlari():
    kartlar = [
        ('1. Kart', '15 907 000', MAVI, MAVI_A),
        ('2. Kart', '85 000 412', YES, YES_A),
        ('3. Kart', '308 040 006', TUR, TUR_A),
        ('4. Kart', '7 001 050', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sayi, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.3, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, sayi, 9.5, LAC)
    return svg(360, 84, ic, 'Çok basamaklı dört doğal sayı kartı.', 15)


def boluk_yapbozu_sema():
    bolukler = [
        ('K · Milyonlar Bölüğü', '6 0 4', MAVI, MAVI_A),
        ('L · Binler Bölüğü', '0 1 8', YES, YES_A),
        ('M · Birler Bölüğü', '5 9 0', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, rak, r, z) in enumerate(bolukler):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 23, bas, 9.7, r)
        ic += yazi(x + 56, 56, rak, 14.5, LAC)
    return svg(360, 86, ic, '604 018 590 sayısının üç bölüğünü gösteren yapboz.', 15)


def uc_boluk_kart_dizilimi():
    kartlar = [
        ('1. Kart', '920', '(3 basamak)', MAVI, MAVI_A),
        ('2. Kart', '5', '(005 olur)', YES, YES_A),
        ('3. Kart', '38', '(038 olur)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 22, bas, 10.2, r)
        ic += yazi(x + 56, 46, s1, 13.0, LAC)
        ic += yazi(x + 56, 66, s2, 9.4, LAC, ince=True)
    return svg(360, 86, ic, 'Üç bölük kartı: 920, 5 ve 38.', 15)


def basamak_tablosu_toplam():
    bolukler = [
        ('Milyonlar Bölüğü', '5 7 2', MAVI, MAVI_A),
        ('Binler Bölüğü', '0 8 4', YES, YES_A),
        ('Birler Bölüğü', '6 1 9', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, rak, r, z) in enumerate(bolukler):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 23, bas, 9.8, r)
        ic += yazi(x + 56, 55, rak, 14.0, LAC)
    return svg(360, 86, ic, '572 084 619 sayısının bölük tablosu.', 15)


def basamak_sayisi_siralama_kartlari():
    kartlar = [
        ('Kart P', '73 006 090', '8 basamaklı', TUR, TUR_A),
        ('Kart R', '985 420', '6 basamaklı', MAVI, MAVI_A),
        ('Kart S', '210 500 040', '9 basamaklı', MOR, MOR_A),
        ('Kart T', '8 340 010', '7 basamaklı', YES, YES_A),
    ]
    ic = ''
    for i, (bas, sayi, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 22, bas, 10.2, r)
        ic += yazi(x + 41, 45, sayi, 9.2, LAC)
        ic += yazi(x + 41, 65, alt, 9.0, LAC, ince=True)
    return svg(360, 86, ic, '6, 7, 8 ve 9 basamaklı dört doğal sayı kartı.', 15)


def basamak_analiz_panosu():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 23, 'İncelenen Doğal Sayı: 830 416 295', 10.8, MAVI)
    ic += yazi(180, 46, 'Milyonlar Bölüğü: 830  |  Binler Bölüğü: 416  |  Birler Bölüğü: 295', 9.7, LAC)
    ic += yazi(180, 67, 'YüzB: 4 · OnB: 1 · Binler: 6   |   YüzM: 8 · OnM: 3 · Milyonlar: 0', 9.3, MAVI, ince=True)
    return svg(360, 88, ic, '830 416 295 sayısının bölük ve basamak analizi.', 15)


def kerem_hata_analizi_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, 'Kerem’in Hatalı Yazımı', 10.2, KIR)
    ic += yazi(91, 45, '«502 9 7» (5 basamak!)', 10.5, KIR)
    ic += yazi(91, 65, 'Eksik basamaklar atlandı', 9.3, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Doğru Bölük Kuralı', 10.2, YESIL_K)
    ic += yazi(269, 45, '[ 502 ] [ _ _ 9 ] [ _ _ 7 ]', 10.2, LAC)
    ic += yazi(269, 65, 'Her bölük 3 hane olmalı!', 9.3, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Eksik basamaklara sıfır yazılmaması hatası ve doğru bölük şeması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gunes_dunya_mesafe_karti()
    s[2]['gorsel'] = dort_sayi_veri_kartlari()
    s[5]['gorsel'] = boluk_yapbozu_sema()
    s[6]['gorsel'] = uc_boluk_kart_dizilimi()
    s[7]['gorsel'] = basamak_tablosu_toplam()
    s[8]['gorsel'] = basamak_sayisi_siralama_kartlari()
    s[9]['gorsel'] = basamak_analiz_panosu()
    s[11]['gorsel'] = kerem_hata_analizi_karti()
