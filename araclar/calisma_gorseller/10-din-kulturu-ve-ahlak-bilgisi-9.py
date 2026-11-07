"""10. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta görselleri (SVG; insan figürü yok; kavram kartları, ayet meali kartı, durum kartları; K150 EK).
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


def sifat_kartlari():
    ad = ['Vücûd', 'Kıdem', 'Bekâ', 'İlim', 'Kudret', 'Vahdâniyet']
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    for i, a in enumerate(ad):
        x, y = 12 + (i % 3) * 114, 12 + (i // 3) * 42
        ic += kutu(x, y, 108, 34, '#fff', YES, 6, 1.2) + yazi(x + 54, y + 22, a, 12.5, LAC)
    return svg(ic, 360, 100, 'Altı sıfat kartı', 26)


def ayet_karti():
    ic = kutu(2, 2, 356, 84, '#fff', YES, 8, 1.3) + f'<rect x="2" y="2" width="6" height="84" rx="3" fill="{YES}"/>'
    ic += yazi(180, 34, '"O\'nun benzeri hiçbir şey yoktur.', 12.5, LAC, ince=True)
    ic += yazi(180, 54, 'O, işitendir, görendir."', 12.5, LAC, ince=True)
    ic += yazi(340, 76, '(Şûrâ suresi, 11. ayet, meal)', 10.5, SOLUK, 'end', True)
    return svg(ic, 360, 88, 'Şûrâ suresi 11. ayetin meali', 24)


def tecelli():
    kart = [('1', 'Kuşun yavrusunu', 'şefkatle beslemesi'), ('2', 'Gezegenlerin düzenli', 'yörüngede dönmesi'), ('3', 'Kurumuş toprağın', 'yağmurla canlanması')]
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    for i, (n, s1, s2) in enumerate(kart):
        x = 10 + i * 116
        ic += kutu(x, 10, 108, 80, '#fff', TUR, 6, 1.2) + f'<circle cx="{x + 54}" cy="28" r="11" fill="{TUR_A}" stroke="{TUR}"/>'
        ic += yazi(x + 54, 33, n, 12.5, TUR) + yazi(x + 54, 60, s1, 10.5, LAC, ince=True) + yazi(x + 54, 76, s2, 10.5, LAC, ince=True)
    return svg(ic, 360, 100, 'Evrenden üç durum kartı', 26)


def dua_durumlari():
    ic = kutu(2, 2, 356, 70, GRI_A, GRI, 8)
    for x, b, t in ((10, 'Durum 1', 'Arkadaşı ağır hastalanmıştır.'), (184, 'Durum 2', 'Ailesi geçim sıkıntısı çekmektedir.')):
        ic += kutu(x, 10, 166, 54, '#fff', MAVI, 6, 1.2) + yazi(x + 83, 30, b, 11.5, MAVI) + yazi(x + 83, 50, t, 10.5, LAC, ince=True)
    return svg(ic, 360, 74, 'Dua edilen iki durum', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sifat_kartlari()
    s[3]['gorsel'] = ayet_karti()
    s[5]['gorsel'] = tecelli()
    s[9]['gorsel'] = dua_durumlari()
