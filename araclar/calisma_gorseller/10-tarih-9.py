"""10. sınıf Tarih 9. hafta görselleri (SVG; insan figürü yok; kart, şema ve zaman şeridi; görsel içi yazı ≈ gövde puntosu, K150 EK).

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


def ok(x1, y1, x2, y2, renk=LAC, kalin=1.4):
    a = math.atan2(y2 - y1, x2 - x1)
    u1 = (x2 - 7 * math.cos(a - 0.45), y2 - 7 * math.sin(a - 0.45))
    u2 = (x2 - 7 * math.cos(a + 0.45), y2 - 7 * math.sin(a + 0.45))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<polygon points="{x2},{y2} {u1[0]:.1f},{u1[1]:.1f} {u2[0]:.1f},{u2[1]:.1f}" fill="{renk}"/>')


def iki_sutun(sol_bas, sol, sag_bas, sag, etiket):
    n = max(len(sol), len(sag))
    boy = 52 + 34 * n
    ic = kutu(2, 2, 356, boy - 4, GRI_A, GRI, 8)
    for x, bas, maddeler, r, a in ((10, sol_bas, sol, KIR, KIR_A), (184, sag_bas, sag, MAVI, MAVI_A)):
        ic += kutu(x, 10, 166, boy - 20, '#fff', r, 6, 1.2)
        ic += f'<rect x="{x}" y="10" width="166" height="24" rx="6" fill="{a}"/>' + yazi(x + 83, 27, bas, 12, r)
        for i, m in enumerate(maddeler):
            for k, parca in enumerate(m):
                ic += yazi(x + 10, 52 + 34 * i + 14 * k, parca, 11, LAC, 'start', True)
    return svg(ic, 360, boy, etiket, 8 + boy * 0.24)


def zaman_seridi():
    ic = kutu(2, 2, 356, 92, GRI_A, GRI, 8)
    yillar = [(1040, 30), (1048, 90), (1071, 160), (1176, 290)]
    ic += ok(14, 50, 348, 50, LAC, 2)
    for y, x in yillar:
        ic += f'<circle cx="{x}" cy="50" r="5" fill="{MAVI}"/>' + yazi(x, 36, str(y), 12, MAVI)
    for (a, xa), (b, xb), r in zip(yillar, yillar[1:] + [(0, 344)], ('I', 'II', 'III', 'IV')):
        ic += yazi((xa + xb) / 2, 74, r, 13, KIR)
    ic += yazi(180, 90, 'Dandanakan · Pasinler · Malazgirt · Miryokefalon', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 96, 'Dört savaşın yıllarını gösteren zaman şeridi; aralıklar I-IV', 26)


def kart(baslik, satirlar, etiket, renk=YES, acik=YES_A):
    boy = 40 + 22 * len(satirlar)
    ic = kutu(2, 2, 356, boy - 4, '#fff', renk, 8, 1.3)
    ic += f'<rect x="2" y="2" width="356" height="28" rx="8" fill="{acik}"/>' + yazi(180, 21, baslik, 12.5, renk)
    for i, s in enumerate(satirlar):
        ic += f'<circle cx="20" cy="{46 + 22 * i}" r="3" fill="{renk}"/>' + yazi(30, 50 + 22 * i, s, 11.5, LAC, 'start', True)
    return svg(ic, 360, boy, etiket, 8 + boy * 0.24)


def sanatlar():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    ic += kutu(10, 10, 166, 132, '#fff', TUR, 6, 1.2) + yazi(93, 28, 'I', 13, TUR)
    for i in range(3):
        for j in range(3):
            cx, cy = 50 + j * 34, 56 + i * 26
            pts = ' '.join(f'{cx + 13 * math.cos(math.pi / 4 * k + math.pi / 8):.1f},{cy + 11 * math.sin(math.pi / 4 * k + math.pi / 8):.1f}' for k in range(8))
            ic += f'<polygon points="{pts}" fill="{TUR_A}" stroke="{TUR}" stroke-width="1"/>'
    ic += yazi(93, 134, 'çivisiz geçme ahşap', 10.5, SOLUK, ince=True)
    ic += kutu(184, 10, 166, 132, '#fff', MAVI, 6, 1.2) + yazi(267, 28, 'II', 13, MAVI)
    ic += f'<rect x="222" y="40" width="90" height="82" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += f'<path d="M244 122 L244 78 Q267 52 290 78 L290 122" fill="#fff" stroke="{MAVI}" stroke-width="1.2"/>'
    for k in range(5):
        ic += f'<rect x="{226 + k * 17}" y="44" width="12" height="10" fill="none" stroke="{MAVI}" stroke-width="0.8"/>'
    ic += yazi(267, 134, 'anıtsal yapı girişi', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 154, 'Selçuklu sanatından iki örnek: I ve II', 40)


def ticaret():
    ic = kutu(2, 2, 356, 170, GRI_A, GRI, 8)
    lim = [('Sinop', 60, 26, 'Karadeniz'), ('Antalya', 40, 112, 'Akdeniz'), ('Alanya', 120, 122, 'Akdeniz')]
    ic += kutu(196, 56, 84, 30, YES_A, YES, 6, 1.2) + yazi(238, 75, 'Konya', 12, YES)
    ic += kutu(296, 20, 56, 26, YES_A, YES, 6, 1.2) + yazi(324, 37, 'Kayseri', 11, YES)
    for ad, x, y, deniz in lim:
        ic += kutu(x - 34, y - 14, 68, 24, MAVI_A, MAVI, 6, 1.2) + yazi(x, y + 3, ad, 11.5, MAVI)
        ic += f'<line x1="{x + 34}" y1="{y}" x2="196" y2="71" stroke="{TUR}" stroke-width="1.3" stroke-dasharray="5 3"/>'
    ic += f'<line x1="280" y1="64" x2="296" y2="40" stroke="{TUR}" stroke-width="1.3" stroke-dasharray="5 3"/>'
    ic += yazi(180, 152, '- - -  kervansaraylarla donatılmış yollar', 11, TUR, ince=True)
    ic += yazi(180, 166, 'Yolda mal kaybına devlet tazminatı', 11, SOLUK, ince=True)
    return svg(ic, 360, 174, 'Limanlardan iç bölgelere uzanan ticaret yolları şeması', 45)


def ikta():
    adim = ['Devlet, toprağın vergi gelirini tahsis eder', 'İkta sahibi vergiyi toplar', 'Gelirle atlı asker besler', 'Savaşta askerleriyle orduya katılır']
    ic = kutu(2, 2, 356, 30 + 30 * len(adim), GRI_A, GRI, 8)
    for i, a in enumerate(adim):
        y = 12 + 30 * i
        ic += kutu(30, y, 300, 22, '#fff', MOR, 5, 1.1) + yazi(180, y + 15, a, 11.5, LAC, ince=True)
        if i < len(adim) - 1:
            ic += ok(180, y + 22, 180, y + 30, MOR, 1.2)
    ic += yazi(180, 22 + 30 * len(adim), 'Toprağın mülkiyeti devlette kalır', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 34 + 30 * len(adim), 'İkta sisteminin işleyiş şeması', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = iki_sutun('Orta Çağ Avrupası', [['Eğitim kilise ve', 'manastır tekelinde'], ['Engizisyon farklı', 'düşüneni cezalandırır'], ['Akıl hastaları', 'dışlanır']],
                               'Türk-İslam dünyası', [['Medresede aklî ve naklî', 'ilimler birlikte'], ['Vakıflarla parasız,', 'burslu eğitim'], ['Darüşşifalarda', 'ücretsiz tedavi']],
                               'Orta Çağ Avrupası ile Türk-İslam dünyasının karşılaştırması')
    s[3]['gorsel'] = zaman_seridi()
    s[5]['gorsel'] = kart('Gevher Nesibe Darüşşifası (Kayseri, 1206)', ['Hastalar din, dil ayrımı gözetilmeden ücretsiz bakılır.',
                          'Ruh hastaları su sesi ve musiki makamlarıyla tedavi edilir.', 'Tıp medresesinde öğrenciler hasta başında yetişir.'], 'Gevher Nesibe Darüşşifası bilgi kartı')
    s[7]['gorsel'] = sanatlar()
    s[9]['gorsel'] = ticaret()
    s[12]['gorsel'] = ikta()
