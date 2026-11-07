"""10. sınıf Felsefe 9. hafta görselleri (SVG; insan figürü yok; kavram kartları ve şemalar; görsel içi yazı ≈ gövde puntosu, K150 EK).
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


def varliklar():
    ad = ['çınar ağacı', 'üçgen', 'nehir', 'adalet', '7 sayısı', 'masa']
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    for i, a in enumerate(ad):
        x, y = 12 + (i % 3) * 114, 12 + (i // 3) * 42
        ic += kutu(x, y, 108, 34, '#fff', MAVI, 17, 1.2) + yazi(x + 54, y + 22, a, 12, LAC, ince=True)
    return svg(ic, 360, 100, 'Altı varlık örneği', 26)


def nicelik():
    ic = kutu(2, 2, 356, 126, GRI_A, GRI, 8)
    for i, (no, daire) in enumerate((('I', [('', 0, 0)]), ('II', [('ruh', -21, 0), ('madde', 21, 0)]),
                                     ('III', [('su', -19, -17), ('hava', 19, -17), ('toprak', -19, 19), ('ateş', 19, 19)]))):
        cx = 64 + i * 116
        ic += kutu(cx - 54, 10, 108, 110, '#fff', MOR, 6, 1.2) + yazi(cx, 28, no, 13, MOR)
        r = 22 if len(daire) == 1 else (20 if len(daire) == 2 else 18)
        for t, dx, dy in daire:
            ic += f'<circle cx="{cx + dx}" cy="{72 + dy}" r="{r}" fill="{MOR_A}" stroke="{MOR}"/>'
            if t:
                ic += yazi(cx + dx, 76 + dy, t, 9.5 if len(daire) > 2 else 10.5, LAC, ince=True)
        if len(daire) == 1:
            ic += yazi(cx, 76, 'tek ilke', 10.5, LAC, ince=True)
    return svg(ic, 360, 130, 'Varlığın sayısına ilişkin üç görüşün şeması', 30)


def soz_karti(soz, alt_yazi, etiket):
    ic = kutu(2, 2, 356, 84, '#fff', TUR, 8, 1.3)
    ic += yazi(22, 40, '“', 30, TUR, 'start')
    for i, s in enumerate(soz):
        ic += yazi(180, 32 + 18 * i, s, 12, LAC, ince=True)
    ic += yazi(340, 78, alt_yazi, 10.5, SOLUK, 'end', True)
    return svg(ic, 360, 88, etiket, 24)


def dort_neden():
    kutular = [('Maddi neden', 'kil'), ('Formel neden', '?'), ('Fail neden', 'çömlekçi'), ('Ereksel neden', 'su saklamak')]
    ic = kutu(2, 2, 356, 132, GRI_A, GRI, 8)
    ic += kutu(140, 52, 80, 30, MAVI_A, MAVI, 15, 1.3) + yazi(180, 72, 'VAZO', 13, MAVI)
    pos = [(14, 12), (222, 12), (14, 92), (222, 92)]
    for (b, t), (x, y) in zip(kutular, pos):
        ic += kutu(x, y, 124, 32, '#fff', TUR if t == '?' else GRI, 6, 1.2)
        ic += yazi(x + 62, y + 13, b, 10.5, SOLUK, ince=True) + yazi(x + 62, y + 27, t, 12, KIR if t == '?' else LAC)
        ic += f'<line x1="{x + 62}" y1="{y + (32 if y < 50 else 0)}" x2="180" y2="{52 if y < 50 else 82}" stroke="{GRI}" stroke-dasharray="3 3"/>'
    return svg(ic, 360, 136, 'Bir vazonun var olmasındaki dört neden şeması', 36)


def hal_degisimi():
    ic = kutu(2, 2, 356, 96, GRI_A, GRI, 8)
    for i, (ad, r, a) in enumerate((('buz', MAVI, MAVI_A), ('su', MAVI, '#d9ecfb'), ('buhar', SOLUK, '#fff'))):
        x = 24 + i * 116
        ic += kutu(x, 18, 84, 40, a, r, 8, 1.3) + yazi(x + 42, 43, ad, 13, r)
        if i < 2:
            ic += f'<line x1="{x + 88}" y1="38" x2="{x + 108}" y2="38" stroke="{LAC}" stroke-width="1.4"/><polygon points="{x + 113},38 {x + 105},34 {x + 105},42" fill="{LAC}"/>'
    ic += yazi(180, 80, 'Isıtılan madde biçim, sıcaklık ve hâl değiştirir.', 11.5, LAC, ince=True)
    return svg(ic, 360, 100, 'Buzun suya, suyun buhara dönüşmesi', 26)


def karsitlik():
    ic = kutu(2, 2, 356, 104, GRI_A, GRI, 8)
    for x, ad, s1, s2, r, a in ((10, 'Herakleitos', 'Her şey akar; aynı', 'ırmağa iki kez girilmez.', TUR, TUR_A),
                                (184, 'Parmenides', 'Değişim duyuların', 'yanılgısıdır; varlık birdir.', MAVI, MAVI_A)):
        ic += kutu(x, 10, 166, 88, '#fff', r, 6, 1.2) + f'<rect x="{x}" y="10" width="166" height="26" rx="6" fill="{a}"/>'
        ic += yazi(x + 83, 28, ad, 12, r) + yazi(x + 83, 60, s1, 11, LAC, ince=True) + yazi(x + 83, 78, s2, 11, LAC, ince=True)
    return svg(ic, 360, 108, 'Herakleitos ve Parmenides karşılaştırması', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = varliklar()
    s[3]['gorsel'] = nicelik()
    s[5]['gorsel'] = soz_karti(['Hiçbir şey yoktur; olsaydı bile bilemezdik;', 'bilseydik bile başkasına aktaramazdık.'], 'İlk Çağ\'dan bir düşünür', 'Bir düşünürün sözü')
    s[7]['gorsel'] = dort_neden()
    s[9]['gorsel'] = hal_degisimi()
    s[10]['gorsel'] = karsitlik()
