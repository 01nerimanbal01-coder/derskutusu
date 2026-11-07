"""10. sınıf Türk Dili ve Edebiyatı 9. hafta görselleri (SVG; insan figürü yok; şiir kartı, ölçek, film şeridi karesi; görsel içi yazı ≈ gövde puntosu, K150 EK).

Dörtlük ve kare metni bu çalışma için yazılmış özgün metinlerdir.
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

DORTLUK = ['Bir türkü tutturdu dağın rüzgârı', 'Uykudan uyandı köyün pınarı', 'Güneşle ısındı evin duvarı', 'Yeniden yeşerdi gönlün baharı']


def siir_karti():
    ic = kutu(2, 2, 356, 128, '#fff', MOR, 8, 1.3)
    ic += f'<rect x="2" y="2" width="6" height="128" rx="3" fill="{MOR}"/>'
    for i, d in enumerate(DORTLUK):
        ic += yazi(30, 34 + 26 * i, d, 13, LAC, 'start', True)
    ic += yazi(340, 124, '(özgün dörtlük)', 10.5, SOLUK, 'end', True)
    return svg(ic, 360, 132, 'Dört dizelik özgün bir şiir', 34)


def rubrik():
    sat = [('Boğumlama ve telaffuz', 4), ('Vurgu, tonlama ve durak', 2), ('Beden dili, göz teması', 3), ('Akıcılık ve doğallık', 4)]
    ic = kutu(2, 2, 356, 36 + 28 * len(sat), GRI_A, GRI, 8)
    ic += yazi(180, 22, 'Masal anlatımı puanlama anahtarı (en çok 4)', 11.5, SOLUK, ince=True)
    for i, (ad, p) in enumerate(sat):
        y = 32 + 28 * i
        ic += kutu(12, y, 336, 24, '#fff', GRI, 4)
        ic += yazi(22, y + 16, ad, 11.5, LAC, 'start', True)
        for k in range(4):
            ic += f'<circle cx="{262 + k * 20}" cy="{y + 12}" r="6.5" fill="{MAVI if k < p else "#fff"}" stroke="{MAVI}"/>'
    return svg(ic, 360, 40 + 28 * len(sat), 'Masal anlatımı için dört ölçütlü puanlama anahtarı', 40)


def kare():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += kutu(12, 12, 150, 126, '#fff', LAC, 4, 1.4)
    ic += f'<rect x="40" y="46" width="94" height="84" fill="{TUR_A}" stroke="{TUR}"/><path d="M58 130 L58 72 Q87 48 116 72 L116 130" fill="#fff" stroke="{TUR}"/>'
    ic += f'<circle cx="106" cy="102" r="3" fill="{TUR}"/>'
    ic += yazi(87, 30, 'KARE 3', 12, LAC)
    satir = [('Çekim:', 'yakın plan (kapı)'), ('Yönerge:', '(Çoban kapıya yaklaşır.)'), ('Diyalog:', '— Bu kapı dün yoktu!'), ('Ses:', 'uzun bir gıcırtı')]
    for i, (a, b) in enumerate(satir):
        ic += yazi(174, 36 + 28 * i, a, 11, MAVI, 'start') + yazi(174, 50 + 28 * i, b, 11, LAC, 'start', True)
    return svg(ic, 360, 154, 'Bir film şeridinin üçüncü karesi', 40)


def nbo():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    sut = [('Ne biliyorum?', 'Ninnileri', 'dinlemiştim.', MAVI, MAVI_A), ('Ne bilmek', 'istiyorum?', 'Koşuk nasıl söylenir?', TUR, TUR_A), ('Ne öğrendim?', '', '', YES, YES_A)]
    for i, (b, s1, s2, r, a) in enumerate(sut):
        x = 10 + i * 116
        ic += kutu(x, 10, 108, 96, '#fff', r, 6, 1.2)
        ic += f'<rect x="{x}" y="10" width="108" height="26" rx="6" fill="{a}"/>' + yazi(x + 54, 28, b if i != 1 else 'Ne bilmek istiyorum?', 10.5, r)
        if i == 0:
            ic += yazi(x + 54, 60, s1, 11, LAC, ince=True) + yazi(x + 54, 76, s2, 11, LAC, ince=True)
        elif i == 1:
            ic += yazi(x + 54, 60, 'Koşuk nasıl', 11, LAC, ince=True) + yazi(x + 54, 76, 'söylenirdi?', 11, LAC, ince=True)
        else:
            ic += yazi(x + 54, 70, '?', 18, YES)
    return svg(ic, 360, 116, 'Üç sütunlu giriş-çıkış kartı', 30)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = siir_karti()
    s[3]['gorsel'] = rubrik()
    s[5]['gorsel'] = kare()
    s[9]['gorsel'] = nbo()
    s[11]['gorsel'] = siir_karti()
