"""10. sınıf Fizik 2. hafta (Sabit Hızlı Hareket ve Grafikler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_grafik_kurallari():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('x-t Eğimi', 'Hızı (v) verir', MAVI, MAVI_A),
        ('v-t Alanı', 'Yer değiştirme Δx', YES, YES_A),
        ('x-t Yatay', 'Cisim duruyor', TUR, TUR_A),
        ('v-t Yatay', 'Hız sabit (a=0)', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Hareket grafikleri yorum kuralları kartı', 34)


def g1_karsilasma():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # Yol çizgisi ve iki hareketli
    ic += f'<line x1="20" y1="50" x2="340" y2="50" stroke="{MAVI}" stroke-width="2"/>'
    # Sol hareketli A
    ic += f'<circle cx="40" cy="50" r="10" fill="{TUR}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(40, 32, 'v₁ = 20 m/s ->', 9, TUR)
    # Sağ hareketli B
    ic += f'<circle cx="320" cy="50" r="10" fill="{YES}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(320, 32, '<- v₂ = 30 m/s', 9, YES)
    # Mesafe ve hesap
    ic += yazi(180, 42, 'd = 500 m', 11, LAC)
    ic += yazi(180, 72, 't = d / (v₁ + v₂) = 500 / 50 = 10 saniye', 10.5, MAVI)
    return svg(360, 100, ic, 'Birbirine doğru koşan iki cismin karşılaşma şeması', 34)


def g2_yer_degistirme():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    # Koordinat çizgisi
    ic += f'<line x1="24" y1="52" x2="336" y2="52" stroke="{YES}" stroke-width="2"/>'
    for kx in (30, 105, 180, 255, 330):
        ic += f'<line x1="{kx}" y1="46" x2="{kx}" y2="58" stroke="{YES}" stroke-width="1.2"/>'
    ic += yazi(30, 70, 'x = 0', 8.5, LAC)
    ic += yazi(330, 70, 'x = 60 m', 8.5, LAC)
    # Formül kutusu
    ic += kutu(90, 12, 180, 30, '#eaf8f0', YES, 5, 1)
    ic += yazi(180, 30, 'Δx = v · t = 15 · 4 = 60 m', 10.5, YES)
    return svg(360, 100, ic, 'Sabit hızlı harekette yer değiştirme hesabı', 34)


def g3_parcali_hareket():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    # x-t grafik ekseni
    ic += f'<line x1="40" y1="80" x2="160" y2="80" stroke="{GRI}" stroke-width="1.2"/>'
    ic += f'<line x1="40" y1="80" x2="40" y2="16" stroke="{GRI}" stroke-width="1.2"/>'
    # Parçalı çizgi (0-4s artış, 4-6s yatay, 6-10s iniş)
    ic += f'<path d="M 40,80 L 80,30 L 100,30 L 140,60" fill="none" stroke="{TUR}" stroke-width="2.2"/>'
    ic += yazi(32, 24, 'x', 8.5, LAC)
    ic += yazi(160, 88, 't', 8.5, LAC)
    # Sağ bilgi kutusu
    ic += kutu(176, 12, 170, 76, '#fef6ec', TUR, 6, 1.1)
    ic += yazi(261, 30, 'PARÇALI HAREKET', 10.5, TUR)
    ic += yazi(261, 48, '• 0-4 s: İleri sabit hızlı', 9, LAC, ince=True)
    ic += yazi(261, 62, '• 4-6 s: Duruyor (v = 0)', 9, LAC, ince=True)
    ic += yazi(261, 76, '• 6-10 s: Geri sabit hızlı', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Parçalı konum zaman grafiği ve analizi', 34)


def g5_grafik_donusumu():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    adımlar = [
        ('1. Aralıklar', 'Zaman dilimleri'),
        ('2. Eğim', 'v = Δx / Δt'),
        ('3. İşaret', '+ / 0 / - hız'),
        ('4. v-t Çizimi', 'Yatay doğrular')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f2fbfd', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'x-t grafiğinden v-t grafiğine dönüşüm adımları', 34)


def g6_yetisme():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    # Aynı yönde giden iki araç
    ic += f'<line x1="20" y1="50" x2="340" y2="50" stroke="{MOR}" stroke-width="2"/>'
    # Arkadaki araç A
    ic += f'<circle cx="50" cy="50" r="10" fill="{TUR}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(50, 32, 'v₁ = 25 m/s ->', 9, TUR)
    # Öndeki araç B
    ic += f'<circle cx="170" cy="50" r="10" fill="{YES}" stroke="{LAC}" stroke-width="1.2"/>'
    ic += yazi(170, 32, 'v₂ = 15 m/s ->', 9, YES)
    # Hesaplama
    ic += yazi(110, 42, 'd = 100 m', 10, LAC)
    ic += yazi(260, 42, 't = d / (v₁ - v₂)', 10, MOR)
    ic += yazi(260, 62, '100 / (25 - 15) = 10 saniye', 10.5, LAC)
    return svg(360, 100, ic, 'Aynı yönde yetişme problemi ve formülü', 34)


def g8_birimler():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    birimler = [
        ('Konum (x)', 'Metre (m)', MAVI, MAVI_A),
        ('Zaman (t)', 'Saniye (s)', TUR, TUR_A),
        ('Hız (v)', 'Metre/saniye (m/s)', YES, YES_A),
        ('İvme (a)', 'm/s² (Sabit hızda 0)', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(birimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Mekanik temel büyüklükler ve SI birimleri', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: K - O - N - U - M', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'O'), ('3', 'N'), ('4', 'U'), ('5', 'M')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Konum şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_grafik_kurallari()
    s[1]['gorsel'] = g1_karsilasma()
    s[2]['gorsel'] = g2_yer_degistirme()
    s[3]['gorsel'] = g3_parcali_hareket()
    s[5]['gorsel'] = g5_grafik_donusumu()
    s[6]['gorsel'] = g6_yetisme()
    s[8]['gorsel'] = g8_birimler()
    s[10]['gorsel'] = g10_sifre_seridi()
