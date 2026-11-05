"""6. sınıf Matematik 10. hafta (Kesir, Ondalık ve Yüzde Gösterimleriyle Çok Adımlı Problemler ve 2. Tema Değerlendirmesi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.1, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kesir(x, y, pay, payda, boy=9.5, renk=LAC):
    """Dikey kesir: pay üstte, yatay çizgi, payda altta (K155)."""
    w = max(len(pay), len(payda)) * boy * 0.65 + 5
    return (yazi(x, y - 3, pay, boy, renk)
            + f'<line x1="{x - w / 2:.1f}" y1="{y:.1f}" x2="{x + w / 2:.1f}" y2="{y:.1f}" stroke="{renk}" stroke-width="1.3"/>'
            + yazi(x, y + boy + 1, payda, boy, renk))


def kutuphane_serit_modeli():
    ic = kutu(6, 6, 348, 78, MAVI_A, MAVI)
    ic += yazi(180, 21, 'Kalanın Kesri Şerit Modeli (5 Eş Parça)', 10.1, MAVI)
    for i in range(5):
        x = 16 + i * 66
        if i == 0:
            r, z, et = MAVI, '#fff', '1. (%20)'
        elif i < 3:
            r, z, et = TUR, TUR_A, '2. Kalan'
        else:
            r, z, et = YES, YES_A, 'Kalan'
        ic += kutu(x, 28, 62, 28, z, r, 5, 1.3)
        ic += yazi(x + 31, 46, et, 9.2, r)
    ic += yazi(180, 72, 'Dizilmeyen son 2 parça = 140 kitap  →  Tamamı (5 parça) = ?', 9.3, LAC, ince=True)
    return svg(360, 90, ic, 'Beş eş parçalı kütüphane kitapları şerit diyagramı.', 15)


def bal_kampanya_panosu():
    kartlar = [
        ('1. K: 1,5 kg', '360 TL (240 TL/kg)', MAVI, MAVI_A),
        ('2. L: 2 kg', '500 TL (%10 ind.)', YES, YES_A),
        ('3. M: 2,5 kg', '550 TL (? TL/kg)', TUR, TUR_A),
        ('4. N: 4 kg', '1200 TL (%25 ind.)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 8.7, LAC, ince=True)
    return svg(360, 84, ic, 'Dört marketin bal satış fiyatları ve indirim oranları.', 15)


def su_tasarrufu_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'SÜRDÜRÜLEBİLİR SU TASARRUFU HESABI', 10.1, CAM)
    ic += yazi(180, 44, '1. Adım: Günde 13,5 L × 20 gün = Kurtarılan toplam su (L)', 9.4, LAC, ince=True)
    ic += yazi(135, 66, '2. Adım: Kurtarılan suyun', 9.4, CAM)
    ic += kesir(208, 62, '2', '3', 9.0, CAM)
    ic += yazi(255, 66, '’si = ? L', 9.4, CAM)
    return svg(360, 88, ic, '20 günde tasarruf edilen suyun üçte ikisini hesaplama kartı.', 15)


def bisiklet_parkuru_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Etap (Geçilen Yol)', 10.0, TUR)
    ic += yazi(68, 46, '18 km yolun', 9.4, LAC, ince=True)
    ic += kesir(115, 42, '1', '3', 9.0, TUR)
    ic += yazi(136, 46, '’i', 9.4, LAC)
    ic += yazi(91, 68, 'Kalan yol = 18 − 6 = 12 km', 9.2, TUR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Etap (Sabit Hızla)', 10.0, YESIL_K)
    ic += yazi(269, 45, 'Dakikada 0,4 km hız', 9.4, LAC, ince=True)
    ic += yazi(269, 68, 'Süre = 12 ÷ 0,4 = ? dk', 9.3, YESIL_K)
    return svg(360, 88, ic, '18 km bisiklet parkurunun iki etaplı çözüm kartı.', 15)


def problem_kurma_islem_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'MATEMATİKSEL İŞLEME UYGUN PROBLEM KURMA', 10.1, MOR)
    ic += yazi(180, 45, 'Verilen İşlem:   (45 − 7,5) ÷ 1,25 = ?', 10.4, LAC)
    ic += yazi(180, 66, '1. Adım: 45 − 7,5 = 37,5   |   2. Adım: 37,5 ÷ 1,25 = ?', 9.3, MOR, ince=True)
    return svg(360, 88, ic, 'Parantezli ondalık çıkarma ve bölme işlem kartı.', 15)


def dort_islem_siralama_panosu():
    kartlar = [
        ('K İşlemi', '60 × 0,25', MAVI, MAVI_A),
        ('L İşlemi', '60 × (%40)', YES, YES_A),
        ('M İşlemi', '60 ÷ 1,5', TUR, TUR_A),
        ('N İşlemi', '60 ÷ 0,5', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 54, alt, 9.5, LAC)
    return svg(360, 84, ic, '60 sayısıyla yapılan dört farklı çarpma ve bölme işlemi.', 15)


def ekolojik_bahce_plani():
    ic = kutu(6, 6, 110, 76, KIR_A, KIR)
    ic += yazi(61, 22, 'Domates Alanı', 9.8, KIR)
    ic += yazi(42, 48, 'Oran:', 9.2, LAC, ince=True)
    ic += kesir(74, 44, '3', '8', 9.0, KIR)
    ic += yazi(61, 68, '(800 m²’nin)', 9.0, LAC, ince=True)

    ic += kutu(125, 6, 110, 76, YES_A, YES)
    ic += yazi(180, 22, 'Biber Alanı', 9.8, YESIL_K)
    ic += yazi(180, 46, 'Oran: 0,25 (%25)', 9.2, LAC)
    ic += yazi(180, 66, 'Çeyrek bahçe', 9.0, YESIL_K, ince=True)

    ic += kutu(244, 6, 110, 76, MOR_A, MOR)
    ic += yazi(299, 22, 'Çilek Alanı', 9.8, MOR)
    ic += yazi(299, 46, 'Geriye Kalan Alan', 9.2, LAC)
    ic += yazi(299, 66, '800 − (Dom.+Bib.)', 8.9, MOR, ince=True)
    return svg(360, 88, ic, '800 metrekarelik bahçenin domates, biber ve çilek ekim dağılımı.', 15)


def strateji_degistirme_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, '1. Uygun Olmayan Yol', 9.9, KIR)
    ic += kesir(42, 44, '1', '3', 9.0, KIR)
    ic += yazi(102, 48, '= 0,333... (Devirli)', 9.2, LAC, ince=True)
    ic += yazi(91, 68, 'Ondalık dil tam çıkmaz!', 9.1, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Doğru Strateji (Kesir)', 9.9, YESIL_K)
    ic += yazi(245, 48, '0,25 =', 9.3, LAC, ince=True)
    ic += kesir(282, 44, '1', '4', 9.0, YESIL_K)
    ic += yazi(269, 68, 'Paydalar 12’de eşitlenir', 9.1, YESIL_K)
    return svg(360, 88, ic, 'Paydası 3 olan kesirde ondalık yerine kesir stratejisine geçiş.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kutuphane_serit_modeli()
    s[2]['gorsel'] = bal_kampanya_panosu()
    s[5]['gorsel'] = su_tasarrufu_karti()
    s[6]['gorsel'] = bisiklet_parkuru_karti()
    s[7]['gorsel'] = problem_kurma_islem_karti()
    s[8]['gorsel'] = dort_islem_siralama_panosu()
    s[9]['gorsel'] = ekolojik_bahce_plani()
    s[11]['gorsel'] = strateji_degistirme_karti()
