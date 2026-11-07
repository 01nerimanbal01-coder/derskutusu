"""12. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 9. hafta görselleri (şematik; insan figürü yok)."""
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


def us(m):
    return f'<tspan baseline-shift="super" font-size="70%">{m}</tspan>'


def alt(m):
    return f'<tspan baseline-shift="sub" font-size="70%">{m}</tspan>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ok(x1, y1, x2, y2, renk=SOLUK, k=1):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2 - 6 * math.cos(a - 0.45):.1f},{y2 - 6 * math.sin(a - 0.45):.1f} {x2:.1f},{y2:.1f} {x2 - 6 * math.cos(a + 0.45):.1f},{y2 - 6 * math.sin(a + 0.45):.1f}'
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="{k}"/>'
            f'<polyline points="{u}" fill="none" stroke="{renk}" stroke-width="{k}"/>')


def cubuk(veri, baslik, etiket, mm=40, renk=MAVI, birim=''):
    """veri: [(alt yazı, değer, gösterilecek yazı)]"""
    n = len(veri); en, boy = 360, 168
    ust = max(v for _, v, _ in veri)
    ic = kutu(2, 2, 356, 164, GRI_A, GRI, 8) + yazi(180, 22, baslik, 12.5, renk)
    ox, oy, yuk = 24, 140, 96
    ic += f'<line x1="{ox}" y1="{oy}" x2="346" y2="{oy}" stroke="{LAC}" stroke-width="1"/>'
    adim = (346 - ox) / n
    for i, (a, v, g) in enumerate(veri):
        h = yuk * v / ust; x = ox + i * adim + adim * 0.2; w = adim * 0.6
        ic += f'<rect x="{x:.1f}" y="{oy - h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" fill="{renk}"/>'
        ic += yazi(x + w / 2, oy - h - 5, g, 12, renk)
        ic += yazi(x + w / 2, oy + 17, a, 12, LAC)
    return svg(ic, en, boy, etiket, mm)


def raporlar():
    ic = kutu(2, 2, 356, 150, GRI_A, GRI, 8)
    for i, (bas, sat, r, ra) in enumerate([
            ('Batı Anadolu raporu', ['Bölgede Türkler', 'çoğunluktadır.', 'İşgal haksızdır;', 'olaylardan işgal', 'kuvvetleri sorumludur.'], MAVI, MAVI_A),
            ('Doğu Anadolu raporu', ['Bölgede Türkler', 'çoğunluktadır.', 'Türklerin Ermenileri', 'katledeceği iddiası', 'gerçeği yansıtmaz.'], MOR, MOR_A)]):
        x = 12 + i * 174
        ic += kutu(x, 12, 162, 130, ra, r, 8, 1)
        ic += yazi(x + 81, 32, bas, 12, r)
        ic += f'<line x1="{x + 12}" y1="40" x2="{x + 150}" y2="40" stroke="{r}" stroke-width="0.7"/>'
        for j, t in enumerate(sat):
            ic += yazi(x + 81, 60 + j * 18, t, 11.5, LAC, ince=True)
    return svg(ic, 360, 152, 'İki yabancı heyet raporunun tespitleri', 38)


def ankara():
    ic = kutu(2, 2, 356, 146, '#f4ecd9', GRI, 8)
    ic += f'<circle cx="230" cy="78" r="9" fill="{KIR}"/>' + yazi(230, 104, 'Ankara', 13, KIR)
    ic += f'<circle cx="62" cy="40" r="6" fill="{LAC}"/>' + yazi(62, 26, 'İstanbul', 12, LAC)
    ic += f'<path d="M62 40 Q140 52 230 78" fill="none" stroke="{LAC}" stroke-width="2.4" stroke-dasharray="10 4"/>'
    ic += f'<path d="M62 46 Q140 62 226 84" fill="none" stroke="{TUR}" stroke-width="1.2"/>'
    ic += yazi(160, 46, 'demir yolu ve telgraf', 11, SOLUK, ince=True)
    ic += ok(200, 96, 120, 124, MAVI, 1.6) + yazi(96, 136, 'Batı Cephesi', 11.5, MAVI)
    ic += kutu(256, 24, 92, 40, '#fff', GRI, 8) + yazi(302, 41, '20. Kolordu', 11.5, LAC) + yazi(302, 56, 'Ankara’da', 11, SOLUK, ince=True)
    ic += kutu(256, 112, 92, 26, '#fff', GRI, 8) + yazi(302, 129, '27 Aralık 1919', 11.5, LAC)
    return svg(ic, 360, 150, 'Ankara’nın konumu, İstanbul bağlantısı ve Batı Cephesi (şematik)', 38)


def not_karti():
    ic = kutu(2, 2, 356, 112, GRI_A, GRI, 8)
    ic += kutu(30, 12, 300, 92, '#fffdf5', TUR, 6, 1.2)
    ic += yazi(180, 32, 'Misak-ı Millî’den', 12.5, TUR)
    for j, t in enumerate(['Arap çoğunluğun yaşadığı işgal altındaki', 'yerlerin geleceği, halkın serbestçe', 'vereceği oyla belirlenmelidir.']):
        ic += yazi(180, 54 + j * 18, t, 12, LAC, ince=True)
    return svg(ic, 360, 116, 'Misak-ı Millî maddesinden not kartı', 30)


def isgal_akisi():
    ic = kutu(2, 2, 356, 120, GRI_A, GRI, 8)
    ic += kutu(12, 14, 152, 96, KIR_A, KIR, 8, 1) + yazi(88, 34, '16 Mart 1920', 12.5, KIR)
    for j, t in enumerate(['İstanbul resmen işgal', 'Mebusan Meclisi basıldı', 'Milletvekilleri tutuklandı']):
        ic += yazi(88, 56 + j * 18, t, 11, LAC, ince=True)
    ic += ok(170, 62, 194, 62, SOLUK, 1.5)
    ic += kutu(198, 14, 150, 96, MAVI_A, MAVI, 8, 1) + yazi(273, 34, '23 Nisan 1920', 12.5, MAVI)
    ic += yazi(273, 66, '?', 22, MAVI)
    return svg(ic, 360, 124, '16 Mart 1920 işgalinden 23 Nisan 1920’ye', 32)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = raporlar()
    s[3]['gorsel'] = ankara()
    s[9]['gorsel'] = not_karti()
    s[11]['gorsel'] = isgal_akisi()
