# -*- coding: utf-8 -*-
"""10-fizik-5 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket, en_fazla=32):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 360 115"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.5, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 76, a, c, 6, 0.75)
        ic += yazi(x + 40, 48, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="58" x2="{x + 72}" y2="58" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 78, d, 7.5, LAC, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket):
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, MAVI)
    ic += kutu(14, 28, 160, 76, '#f8fafc', MAVI, 6, 0.75)
    ic += yazi(94, 48, sol_b, 9, MAVI)
    ic += yazi(94, 68, sol_d1, 8, LAC, ince=True)
    ic += yazi(94, 88, sol_d2, 7.5, SOLUK, ince=True)
    ic += kutu(186, 28, 160, 76, '#f8fafc', TUR, 6, 0.75)
    ic += yazi(266, 48, sag_b, 9, TUR)
    ic += yazi(266, 68, sag_d1, 8, LAC, ince=True)
    ic += yazi(266, 88, sag_d2, 7.5, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [MAVI, TUR, MOR]
    for i, (b, d1, d2) in enumerate(uclu):
        c = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 54, 48, b, 8.8, c)
        ic += yazi(x + 54, 68, d1, 7.8, LAC, ince=True)
        ic += yazi(x + 54, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)

def g0():
    return karsilastir2('HAREKET GRAFİKLERİ DÖNÜŞÜM KÖPRÜSÜ', 'x -> v -> a Yönü (EĞİM)', 'x-t eğimi = Hız (v)', 'v-t eğimi = İvme (a)', 'a -> v -> x Yönü (ALAN)', 'a-t alanı = Hız değişimi (Δv)', 'v-t alanı = Yer değiştirme (Δx)', '10-fizik-5 grafik dönüşüm köprüsü')

def g1():
    return karsilastir2('İLK HIZSIZ HIZLANAN HAREKET (a = 4 m/s²)', 'Hız Hesabı (v = a · t)', 't = 5 s -> v = 4 · 5 = 20 m/s', 'Doğrusal artan v-t grafiği', 'Yol Hesabı (Δx = ½·a·t²)', 'Δx = ½ · 4 · 25 = 50 m', 'Üçgen alanı: (20 · 5) / 2 = 50 m', '10-fizik-5 hız ve yol hesabı')

def g2():
    return uclu_sema('a-t GRAFİĞİNDEN HIZA GEÇİŞ', [('a-t Grafiği Alanı', 'Δv = a · t verir', 'Yalnız değişimi ölçer'), ('İlk Hız (v₀)', 'Başlangıç koşuludur', 'Soruda verilmelidir'), ('Son Hız (v)', 'v = v₀ + Δv', 'Toplam hız bulunur')], '10-fizik-5 ivmeden hıza geçiş')

def g3():
    return uclu_sema('ARDIŞIK ZAMANLARDA x - 3x - 5x KURALI', [('0 - t Aralığı', 'Hız: 0 -> v', 'Alınan yol: x'), ('t - 2t Aralığı', 'Hız: v -> 2v', 'Alınan yol: 3x'), ('2t - 3t Aralığı', 'Hız: 2v -> 3v', 'Alınan yol: 5x')], '10-fizik-5 x 3x 5x kuralı')

def g5():
    return kart4('v-t GRAFİĞİNDEN DÖNÜŞÜM ADIMLARI', [('1. Eğim Bul', 'a = Δv / Δt'), ('2. a-t Çiz', 'Yatay sabit doğru'), ('3. Alan Bul', 'Δx yamuk/üçgen alanı'), ('4. x-t Çiz', 'Parabolik eğri')], '10-fizik-5 dönüşüm adımları')

def g6():
    return karsilastir2('DÜZGÜN YAVAŞLAYAN TREN ANALİZİ', 'Durma Süresi (t)', 'v₀ = 30 m/s, a = -3 m/s²', 't = 30 / 3 = 10 saniye', 'Durma Mesafesi (Δx)', 'Üçgen alanı = (30 · 10) / 2', 'Δx = 150 metre', '10-fizik-5 yavaşlayan tren')

def g8():
    return kart4('SABİT İVMELİ HAREKET DENKLEMLERİ', [('Hız Denklemi', 'v = v₀ + a·t'), ('Konum Denklemi', 'Δx = v₀·t + ½·a·t²'), ('Zamansız Hız', 'v² = v₀² + 2·a·Δx'), ('Ortalama Hız', 'Δx = ½·(v₀+v)·t')], '10-fizik-5 denklemler')

def g11():
    return karsilastir2('v-t YAMUK ALANINDAN KONUM DENKLEMİ', 'Alt Dikdörtgen Alanı', 'Taban: t, Yükseklik: v₀', 'Alan₁ = v₀ · t', 'Üst Üçgen Alanı', 'Taban: t, Yükseklik: a·t', 'Alan₂ = ½ · a · t²', '10-fizik-5 yamuk alanı türetimi')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
