# -*- coding: utf-8 -*-
"""10-kimya-7 çalışma kâğıdı görselleri.
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
    return kart4('AKB VE MOL TEMEL KAVRAMLARI', [('1 akb (1 u)', '1 / N_A gram'), ('1 gram', 'N_A tane akb'), ('Gerçek Kütle', '1 tanenin gram kütlesi'), ('Molar Kütle (M_A)', '1 molün gram kütlesi')], '10-kimya-7 temel kavramlar')

def g1():
    return karsilastir2('1 TANE MOLEKÜL VS. 1 MOL MOLEKÜL (CH₄=16)', '1 Tane CH₄ Molekülü', 'Kütlesi = 16 akb', 'Gerçek kütlesi = 16 / N_A gram', '1 Mol (N_A Tane) CH₄ Molekülü', 'Molar kütlesi = 16 gram', 'akb cinsinden = 16 · N_A akb', '10-kimya-7 tane mol farki')

def g2():
    return karsilastir2('İZOTOP VE ORTALAMA ATOM KÜTLESİ', 'İzotop Bolluk Yüzdesi', 'Doğada ³⁵Cl (%75) ve ³⁷Cl (%25)', 'Ağırlıklı ortalama alınır', 'Ortalama Atom Kütlesi Hesabı', '(35·75 + 37·25) / 100 = 35,5 akb', 'Bolluğu çok olana daha yakındır', '10-kimya-7 ortalama kutle')

def g3():
    return uclu_sema('SU (H₂O = 18) KÜTLE KARŞILAŞTIRMASI', [('1 Tane H₂O', '18 akb', '18 / N_A gram'), ('1 Mol H₂O', '18 gram', '18 · N_A akb'), ('0,5 Mol H₂O', '9 gram', '1,5 mol atom içerir')], '10-kimya-7 su kutleleri')

def g5():
    return kart4('BİLEŞİK FORMÜLÜ BULMA BASAMAKLARI', [('1. Kütle / Yüzde', 'Element kütlelerini al'), ('2. Mol Hesabı', 'n = m / M_A uygula'), ('3. Basit Formül', 'En küçük tam sayıya böl'), ('4. Gerçek Formül', 'Gerçek M_A ile genişlet')], '10-kimya-7 formul adimlari')

def g6():
    return uclu_sema('0,3 MOL N₂O₃ (M_A = 76) ANALİZİ', [('Bileşik Kütlesi', 'm = 0,3 × 76', '22,8 gram N₂O₃'), ('Azot ve Oksijen', '0,6 mol N atomu', '0,9 mol O atomu'), ('Toplam Atom', '0,3 × 5 = 1,5 mol', '1,5 · N_A tane atom')], '10-kimya-7 bilesik analizi')

def g8():
    return kart4('OKSİJEN VE SU NİCELİK EŞLEŞTİRMESİ', [('1 tane O atomu', '16 akb = 16/N_A g'), ('1 mol O₂ gazı', '32 gram = 32·N_A akb'), ('0,5 mol H₂O', '1,5 mol atom içerir'), ('3,6 gram H₂O', 'n = 3,6/18 = 0,2 mol')], '10-kimya-7 nicelikler')

def g11():
    return karsilastir2('KRİSTAL SULU BİLEŞİK (Na₂CO₃·nH₂O)', '1 Mol Bileşiğin Kütlesi', '0,1 molü 28,6 g -> 1 molü 286 g', 'Susuz Na₂CO₃ = 106 g/mol', 'Kristal Suyu (n) Hesabı', '18n = 286 - 106 = 180 g su', 'n = 180 / 18 = 10 (Na₂CO₃·10H₂O)', '10-kimya-7 hidrat tuz')

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
