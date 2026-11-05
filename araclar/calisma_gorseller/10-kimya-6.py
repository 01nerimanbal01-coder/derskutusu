# -*- coding: utf-8 -*-
"""10-kimya-6 çalışma kâğıdı görselleri.
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
    return kart4('MOL - KÜTLE - HACİM BAĞINTILARI', [('Tanecik -> Mol', 'n = N / N_A'), ('Kütle -> Mol', 'n = m / M_A'), ('NK Gaz Hacmi', '0°C, 1 atm: 22,4 L/mol'), ('Oda Koşulu Hacim', '25°C, 1 atm: 24,5 L/mol')], '10-kimya-6 mol bağıntıları')

def g1():
    return karsilastir2('NK GAZ HACMİNDEN KÜTLEYE GEÇİŞ (CH₄)', '1. Adım: Hacimden Mol Bulma', 'NK\'da V = 11,2 L CH₄ gazı', 'n = 11,2 / 22,4 = 0,5 mol CH₄', '2. Adım: Molden Kütle ve Atom', 'm = 0,5 · 16 = 8 gram CH₄', 'Toplam atom = 0,5 · 5 = 2,5 mol atom', '10-kimya-6 CH4 mol hesabı')

def g2():
    return karsilastir2('MOLAR HACİMDE FİZİKSEL HÂL KURALI', 'Gaz Fazındaki Maddeler', '0°C, 1 atm\'de 1 mol He(g), O₂(g)', '22,4 Litre hacim kaplar', 'Sıvı ve Katı Faz (Örn: H₂O)', '0°C, 1 atm\'de H₂O sıvı/katı hâldedir!', '1 mol H₂O(s) ≈ 18 mL (22,4 L DEĞİL!)', '10-kimya-6 fiziksel hal uyarısı')

def g3():
    return uclu_sema('AVOGADRO YASASI VE ATOM-MOL ANALİZİ', [('Avogadro Yasası', 'Aynı T ve P altında', 'Eşit mol gaz = Eşit hacim'), ('C₃H₈O Bileşiği (1 mol)', '3 mol C + 8 mol H + 1 mol O', 'Toplam 12 mol atom içerir'), ('Ortalama Atom Kütlesi', 'Σ(İzotop Kütlesi × %Bolluk)', '100\'e bölünerek bulunur')], '10-kimya-6 Avogadro ve bileşik')

def g5():
    return kart4('BİLEŞİKTE ATOM SAYISINDAN HACMİ BULMA', [('1. Atom Molü', 'Toplam atom molünü bul'), ('2. Bileşik Molü', 'Formül sayısına böl (n)'), ('3. Kütle Hesabı', 'm = n · M_A ile kontrol'), ('4. NK Hacmi', 'V = n · 22,4 L çarpımı')], '10-kimya-6 hesaplama adımları')

def g6():
    return karsilastir2('BİLEŞİKTE ATOM MOLÜNDEN KÜTLE HESABI (SO₃)', 'Atom Sayısı Analizi (1 mol SO₃ = 4 mol atom)', 'Toplam 1,2 mol atom içeren SO₃ gazı', 'n(SO₃) = 1,2 / 4 = 0,3 mol SO₃', 'Kütle ve NK Hacim Hesabı (M_A = 80)', 'm = 0,3 · 80 = 24 gram SO₃', 'V_NK = 0,3 · 22,4 = 6,72 Litre', '10-kimya-6 SO3 analizi')

def g8():
    return kart4('0,2 MOL C₂H₆ GAZININ NİCEL ANALİZİ', [('Bileşik Kütlesi', '0,2 · 30 = 6 gram'), ('NK\'daki Hacmi', '0,2 · 22,4 = 4,48 L'), ('Karbon Atomu', '0,2 · 2 = 0,4 mol C'), ('Toplam Atom', '0,2 · 8 = 1,6 mol atom')], '10-kimya-6 C2H6 analizi')

def g11():
    return karsilastir2('GAZ KARIŞIMI PROBLEMİ (He ve CH₄)', 'Verilen Karışım Bilgileri', 'n_toplam = 0,5 mol (NK hacmi 11,2 L)', 'm_toplam = 4,4 gram (He=4, CH₄=16)', 'Denklem Çözümü (x mol CH₄)', '16x + 4(0,5 - x) = 4,4 -> 12x = 2,4', 'x = 0,2 mol CH₄ ve 0,3 mol He', '10-kimya-6 gaz karışımı')

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
