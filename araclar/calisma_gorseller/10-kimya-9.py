"""10. sınıf Kimya 9. hafta görselleri (SVG; insan figürü yok; görsel içi yazı ≈ gövde puntosu, K150 EK).

viewBox genişliği 360 birim ≈ yarım sütun (≈88 mm); 12 birimlik yazı ≈ 8,5–9 pt.
"""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7'
GRI, GRI_A, SOLUK = '#9aa6bd', '#f3f5f9', '#5b6479'
KALIN = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, en, boy, etiket, mm):
    return (f'<svg viewBox="0 0 {en} {boy}" style="width:100%;max-height:{mm}mm;display:block;margin:1mm auto;" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>')


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else KALIN} fill="{renk}">{metin}</text>'


def us(metin):
    return f'<tspan baseline-shift="super" font-size="70%">{metin}</tspan>'


def alt(metin):
    return f'<tspan baseline-shift="sub" font-size="70%">{metin}</tspan>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'



def f(formul, boy=None):
    """C2H6 → C₂H₆ (rakam harf/parantez ardındaysa alt simge)."""
    import re
    return re.sub(r'(?<=[A-Za-z)])(\d+)', lambda m: alt(m.group(1)), formul)


def tepkime_karti(denklem, notlar, etiket, baslik='Denkleştirilmiş tepkime'):
    boy = 70 + 20 * len(notlar)
    ic = kutu(2, 2, 356, boy - 4, GRI_A, GRI, 8)
    ic += yazi(180, 22, baslik, 11.5, SOLUK, ince=True)
    ic += kutu(14, 30, 332, 30, '#fff', MAVI, 6, 1)
    ic += yazi(180, 50, denklem, 13.5, LAC)
    for i, n in enumerate(notlar):
        ic += yazi(180, 80 + 20 * i, n, 12, LAC, ince=True)
    return svg(ic, 360, boy, etiket, 12 + boy * 0.2)


def molekul_kabi():
    """Kapta 3 X₂ (mavi çift) ve 6 Y₂ (turuncu çift) molekülü; yanında tepkime."""
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += kutu(16, 16, 170, 122, '#fff', LAC, 10, 1.2)
    x2 = [(46, 44), (122, 58), (70, 112)]
    y2 = [(96, 34), (150, 92), (36, 80), (110, 96), (152, 38), (124, 124)]
    for x, y in x2:
        ic += f'<circle cx="{x - 7}" cy="{y}" r="8" fill="{MAVI}"/><circle cx="{x + 7}" cy="{y}" r="8" fill="{MAVI}"/>'
    for x, y in y2:
        ic += f'<circle cx="{x - 5}" cy="{y}" r="5.5" fill="{TUR}"/><circle cx="{x + 5}" cy="{y}" r="5.5" fill="{TUR}"/>'
    ic += f'<circle cx="208" cy="40" r="8" fill="{MAVI}"/>' + yazi(222, 44, ': X atomu', 12, LAC, 'start', True)
    ic += f'<circle cx="208" cy="66" r="5.5" fill="{TUR}"/>' + yazi(222, 70, ': Y atomu', 12, LAC, 'start', True)
    ic += kutu(198, 88, 150, 40, '#fff', MAVI, 6)
    ic += yazi(273, 113, f'X{alt(2)} + 3Y{alt(2)} → 2XY{alt(3)}', 13, LAC)
    return svg(ic, 360, 154, 'Kapta üç X2 ve altı Y2 molekülü ile X2 + 3Y2 → 2XY3 tepkimesi', 40)


def bds_kart():
    ic = kutu(2, 2, 356, 116, GRI_A, GRI, 8)
    ic += yazi(180, 24, f'N{alt(2)}(g) + 3H{alt(2)}(g) → 2NH{alt(3)}(g)', 13.5, LAC)
    sut = [96, 176, 256, 330]
    for x, b in zip(sut[1:], ['N₂', 'H₂', 'NH₃']):
        ic += yazi(x, 52, f(b.replace('₂', '2').replace('₃', '3')), 12.5, MAVI)
    satir = [('Başlangıç', ['2 mol', '9 mol', '0']), ('Sonuç', ['?', '?', '?'])]
    for i, (ad, d) in enumerate(satir):
        y = 76 + 28 * i
        ic += kutu(12, y - 17, 336, 24, '#fff', GRI, 4)
        ic += yazi(sut[0] - 34, y, ad, 12, LAC, 'start' if False else 'middle')
        for x, v in zip(sut[1:], d):
            ic += yazi(x, y, v, 12.5, KIR if v == '?' else LAC, ince=v != '?')
    return svg(ic, 360, 120, 'Amonyak tepkimesinin başlangıç mol sayıları', 32)


def iki_kap(sol, sag, alt_yazi):
    ic = kutu(2, 2, 356, 128, GRI_A, GRI, 8)
    for x, (ust, ad, renk, acik) in zip((34, 196), (sol, sag)):
        ic += f'<path d="M{x} 30 L{x} 92 Q{x} 102 {x + 10} 102 L{x + 120} 102 Q{x + 130} 102 {x + 130} 92 L{x + 130} 30" fill="{acik}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 65, 62, ust, 15, renk)
        ic += yazi(x + 65, 84, ad, 12, LAC, ince=True)
    ic += yazi(180, 66, '+', 18, LAC)
    ic += yazi(180, 122, alt_yazi, 11.5, SOLUK, ince=True)
    return svg(ic, 360, 132, 'Tepkimeye konulan iki maddenin kütleleri', 34)


def veri_karti(satirlar, etiket):
    boy = 30 + 26 * len(satirlar)
    ic = kutu(2, 2, 356, boy - 4, GRI_A, GRI, 8)
    for i, (sol, sag) in enumerate(satirlar):
        y = 30 + 26 * i
        ic += kutu(14, y - 17, 332, 23, '#fff', GRI, 4)
        ic += yazi(24, y, sol, 12, LAC, 'start', True)
        ic += yazi(336, y, sag, 12.5, MAVI, 'end')
    return svg(ic, 360, boy, etiket, 10 + boy * 0.22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = tepkime_karti(f'2H{alt(2)}(g) + O{alt(2)}(g) → 2H{alt(2)}O(g)', ['Mol kütleleri: H = 1 g/mol, O = 16 g/mol'],
                                   'Hidrojen ile oksijenden su buharı oluşumu')
    s[2]['gorsel'] = tepkime_karti(f'CH{alt(4)}(g) + 2O{alt(2)}(g) → CO{alt(2)}(g) + 2H{alt(2)}O(g)',
                                   ['Mol kütleleri: H = 1, C = 12, O = 16 g/mol'], 'Metanın yanma tepkimesi')
    s[3]['gorsel'] = tepkime_karti(f'Mg(k) + 2HCl(suda) → MgCl{alt(2)}(suda) + H{alt(2)}(g)',
                                   ['Tepkimeye giren magnezyum: 7,2 g', 'Mg = 24 g/mol · gaz hacmi NŞA koşullarında'],
                                   'Magnezyum ile hidroklorik asit tepkimesi')
    s[6]['gorsel'] = bds_kart()
    s[8]['gorsel'] = molekul_kabi()
    s[9]['gorsel'] = veri_karti([(f'Tepkime: CaCO{alt(3)}(k) → CaO(k) + CO{alt(2)}(g)', ''),
                                 (f'Isıtılan CaCO{alt(3)} kütlesi', '50 g'),
                                 (f'Toplanan CO{alt(2)} gazı (NŞA)', '8,96 L'),
                                 (f'CaCO{alt(3)} mol kütlesi', '100 g/mol')], 'Kireç taşının ısıtılması deney verileri')
    s[11]['gorsel'] = iki_kap(('11,2 g', 'demir (Fe)', MAVI, MAVI_A), ('8 g', 'kükürt (S)', TUR, TUR_A),
                              f'Fe(k) + S(k) → FeS(k) · Fe = 56, S = 32 g/mol')
    s[12]['gorsel'] = tepkime_karti(f'2C{alt(2)}H{alt(6)}(g) + 7O{alt(2)}(g) → 4CO{alt(2)}(g) + 6H{alt(2)}O(s)',
                                    ['Yakılan etan: 6 g · H = 1, C = 12, O = 16 g/mol'], 'Etanın yanma tepkimesi')
