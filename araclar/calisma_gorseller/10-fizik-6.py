# -*- coding: utf-8 -*-
"""10-fizik-6 çalışma kâğıdı görselleri.
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
    return kart4('SABİT İVMELİ HAREKET MODELLERİ', [('Hız Denklemi', 'v = v₀ ± a·t'), ('Konum Denklemi', 'Δx = v₀·t ± ½·a·t²'), ('Zamansız Hız', 'v² = v₀² ± 2·a·Δx'), ('Ortalama Hız', 'v_ort = (v₀ + v) / 2')], '10-fizik-6 matematiksel modeller')

def g1():
    return karsilastir2('İLK HIZSIZ HAREKET HESABI (a = 6 m/s²)', 'Hız (t = 4 s sonunda)', 'v = a · t = 6 · 4 = 24 m/s', 'Ortalama hız: (0 + 24) / 2 = 12 m/s', 'Toplam Yer Değiştirme (Δx)', 'Δx = ½ · a · t² = ½ · 6 · 16 = 48 m', 'Veya Δx = v_ort · t = 12 · 4 = 48 m', '10-fizik-6 ilk hızsız hareket')

def g2():
    return karsilastir2('FREN MESAFESİ VE HIZIN KARESİ İLİŞKİSİ', 'Durma Mesafesi Modeli', 'v_son = 0 -> Δx = v₀² / (2·a)', 'İlk hızın karesiyle doğru orantılıdır', 'Hız 3 Katına Çıkarsa (v -> 3v)', 'Durma süresi 3 katına (3t) çıkar', 'Fren mesafesi 3² = 9 katına (9d) çıkar!', '10-fizik-6 fren mesafesi')

def g3():
    return uclu_sema('ARDIL ZAMANLAR VE İŞARET ANALİZİ', [('x - 3x - 5x Kuralı', 'Her saniyede tek sayılar', 'Toplam yol: x, 4x, 9x, 16x'), ('Aynı İşaretli (v ve a)', 'v > 0, a > 0 veya v < 0, a < 0', 'Araç düzgün hızlanır'), ('Zıt İşaretli (v ve a)', 'v > 0, a < 0 veya v < 0, a > 0', 'Araç düzgün yavaşlar')], '10-fizik-6 oran ve işaretler')

def g5():
    return kart4('TOPLAM DURMA MESAFESİ ADIMLARI', [('1. Tehlike Anı', 'Engel fark edilir'), ('2. Tepki Süresi', 'Sabit v₀ ile Δx₁ = v₀·t_t'), ('3. Frene Basma', 'Sabit a ile yavaşlama'), ('4. Tam Durma', 'Δx_top = Δx₁ + v₀²/(2a)')], '10-fizik-6 durma adımları')

def g6():
    return karsilastir2('ZAMANSIZ HIZ DENKLEMİ UYGULAMASI', 'Verilen Büyüklükler', 'İlk hız v₀ = 20 m/s, Son hız v = 0', 'Durma mesafesi Δx = 50 m', 'İvme Hesabı (v² = v₀² - 2·a·Δx)', '0 = 400 - 2 · a · 50', '100·a = 400 -> a = 4 m/s²', '10-fizik-6 zamansız hız hesabı')

def g8():
    return kart4('İLK HIZSIZ HAREKETTE YOL ORANLARI (x = 5 m)', [('1. Saniye (0-1 s)', 'Alınan yol: x = 5 m'), ('2. Saniye (1-2 s)', 'Alınan yol: 3x = 15 m'), ('3. Saniye (2-3 s)', 'Alınan yol: 5x = 25 m'), ('4. Saniye (3-4 s)', 'Alınan yol: 7x = 35 m')], '10-fizik-6 ardışık saniye yolları')

def g11():
    return karsilastir2('TEPKİ MESAFESİ + FREN MESAFESİ HESABI', '1. Tepki Mesafesi (t_tepki = 0,5 s)', 'Sabit v₀ = 30 m/s hızla gider', 'Δx₁ = 30 · 0,5 = 15 metre', '2. Fren Mesafesi (a = 5 m/s²)', 'Δx₂ = v₀² / (2·a) = 900 / 10 = 90 m', 'Toplam Durma = 15 + 90 = 105 m', '10-fizik-6 toplam durma mesafesi')

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
