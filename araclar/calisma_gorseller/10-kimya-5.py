# -*- coding: utf-8 -*-
"""10-kimya-5 çalışma kâğıdı görselleri.
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
    return kart4('MOL KAVRAMI DÖNÜŞÜM KÖPRÜSÜ', [('Tanecik', 'n = N / N_A'), ('Kütle (g)', 'n = m / M_A'), ('NK Hacim', 'n = V / 22,4 L'), ('Oda Koşulu', 'n = V / 24,5 L')], '10-kimya-5 mol dönüşüm köprüsü')

def g1():
    return karsilastir2('22 GRAM CO₂ GAZININ NK ANALİZİ', '1. Adım: Mol Sayısı (n)', 'M_A(CO₂) = 12 + 2·16 = 44 g/mol', 'n = 22 / 44 = 0,5 mol CO₂', '2. Adım: NK Gaz Hacmi (V)', '1 mol gaz NK\'da 22,4 L', 'V = 0,5 · 22,4 = 11,2 L', '10-kimya-5 CO2 mol hacim hesabı')

def g2():
    return karsilastir2('1 TANE VE 1 MOL SU (H₂O) FARKI', 'Mikroskobik: 1 Tane H₂O', 'Kütle = 18 akb', 'Gram karşılığı = 18 / N_A g', 'Makroskobik: 1 Mol H₂O', 'N_A tane molekül içerir', 'Kütle = 18 gram (18·N_A akb)', '10-kimya-5 akb ve gram farkı')

def g3():
    return uclu_sema('1 MOL H₂SO₄ BİLEŞİĞİNİN ATOM ANALİZİ', [('Hidrojen (H)', '2 mol H atomu', '2 gram H'), ('Kükürt (S)', '1 mol S atomu', '32 gram S'), ('Oksijen (O)', '4 mol O atomu', '64 gram O (Toplam 7 mol)')], '10-kimya-5 bileşik atom analizi')

def g5():
    return kart4('KÜTLEDEN ATOM SAYISINA 4 ADIM', [('1. M_A Bul', 'Formül ağırlığı'), ('2. n = m/M_A', 'Bileşik molü'), ('3. Atom Molü', 'n × atom sayısı'), ('4. Tane Sayısı', 'Atom molü × N_A')], '10-kimya-5 işlem basamakları')

def g6():
    return karsilastir2('KLOR İZOTOPLARI ORTALAMA ATOM KÜTLESİ', 'İzotop Bolluk Verileri', '³⁵Cl: %75 bolluk', '³⁷Cl: %25 bolluk', 'Ağırlıklı Ortalama Hesabı', '(35·75 + 37·25) / 100', 'Ortalama A = 35,5 akb', '10-kimya-5 ortalama atom kütlesi')

def g8():
    return kart4('0,2 MOL C₃H₈ (PROPAN) ÖZET KARTI', [('Kütle (m)', '0,2 × 44 = 8,8 g'), ('Karbon Molü', '0,2 × 3 = 0,6 mol C'), ('Hidrojen Molü', '0,2 × 8 = 1,6 mol H'), ('Toplam Atom', '2,2 × N_A tane')], '10-kimya-5 C3H8 analizi')

def g11():
    return karsilastir2('BAĞIL ATOM KÜTLESİ VE İZOTOP ORTALAMASI', 'Referans Standart', 'Karbon-12 (¹²C = 12,000 akb)', '1 akb = 1 / N_A gram', 'Küsuratlı Değer Nedeni', 'Doğadaki izotop karışımı', 'Bolluk yüzdesine göre ortalama', '10-kimya-5 izotop ortalaması')

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
