"""10. sınıf Coğrafya 1. hafta (coğrafi bakış) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def ok(x1, y1, x2, y2, renk=GRI, kalin=1.8):
    a = math.atan2(y2 - y1, x2 - x1)
    u = f'{x2:.1f},{y2:.1f} {x2 - 7 * math.cos(a - 0.45):.1f},{y2 - 7 * math.sin(a - 0.45):.1f} {x2 - 7 * math.cos(a + 0.45):.1f},{y2 - 7 * math.sin(a + 0.45):.1f}'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2 - 5 * math.cos(a):.1f}" y2="{y2 - 5 * math.sin(a):.1f}" stroke="{renk}" stroke-width="{kalin}"/><polygon points="{u}" fill="{renk}"/>'


def yildiz(x, y, r, renk=ALTIN):
    p = ' '.join(f'{x + (r if k % 2 == 0 else r * 0.45) * math.cos(-math.pi / 2 + k * math.pi / 5):.1f},{y + (r if k % 2 == 0 else r * 0.45) * math.sin(-math.pi / 2 + k * math.pi / 5):.1f}' for k in range(10))
    return f'<polygon points="{p}" fill="{renk}"/>'


SU = '#5aa9e6'


def satir_kartlari(kart, etiket, en_fazla):
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 29
        ic += kutu(4, y, 352, 25, d, c, 8, 1.3) + rozet(21, y + 12.5, h, c) + yazi(38, y + 17, s, 11.5, LAC, 'start', True)
    return svg(360, 4 + len(kart) * 29, ic, etiket, en_fazla)


KUM, YAPRAK = '#f0dfb8', '#2f9e55'


def yerler():
    ad = [['Keban Barajı', '(Elâzığ)'], ['Tarım alanları', '(Muğla)'], ['Varda Köprüsü', '(Adana)'], ['Konyaaltı Plajı', '(Antalya)']]
    ic = ''
    for i, a in enumerate(ad):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 88, '#fff', GRI, 8, 1.2) + rozet(x0 + 13, 17, str(i + 1), LAC) + yazi(x0 + 42, 72, a[0], 9.6, LAC) + yazi(x0 + 42, 84, a[1], 9.6, SOLUK, 'middle', True)
    c = [4 + i * 89 + 42 for i in range(4)]
    ic += f'<rect x="{c[0] - 28}" y="30" width="26" height="26" fill="{SU}"/><path d="M{c[0] - 2} 24 h8 l10 32 h-18 Z" fill="{SOLUK}"/><path d="M{c[0] + 16} 56 q6 -6 12 0 Z" fill="{SU}"/>'
    ic += f'<rect x="{c[1] - 26}" y="28" width="52" height="30" fill="#e9d8a6"/>' + ''.join(f'<line x1="{c[1] - 22 + k * 9}" y1="30" x2="{c[1] - 26 + k * 9}" y2="56" stroke="{YAPRAK}" stroke-width="3"/>' for k in range(6))
    ic += f'<rect x="{c[2] - 28}" y="28" width="56" height="5" fill="{SOLUK}"/>' + ''.join(f'<path d="M{c[2] - 26 + k * 13} 58 V33 h13 V58 h-3 V42 a3.5 3.5 0 0 0 -7 0 V58 Z" fill="#b9b1a0"/>' for k in range(4))
    ic += f'<rect x="{c[3] - 28}" y="44" width="56" height="14" fill="{KUM}"/><rect x="{c[3] - 28}" y="30" width="56" height="14" fill="{SU}"/><line x1="{c[3] + 4}" y1="54" x2="{c[3] + 4}" y2="34" stroke="{KAHVE}" stroke-width="1.6"/><path d="M{c[3] - 10} 38 a14 12 0 0 1 28 0 Z" fill="{KIR}"/>'
    return svg(360, 96, ic, 'Yerler: 1 Keban Barajı (Elâzığ), 2 tarım alanları (Muğla), 3 Varda Köprüsü (Adana), 4 Konyaaltı Plajı (Antalya)', 24)


def alan_grafik():
    x0, y0, h = 40, 100, 74
    veri = [('1975', 5949), ('1986', 5168), ('1995', 4731), ('2002', 5300), ('2011', 5580), ('2018', 3464)]
    ic = f'<line x1="{x0}" y1="{y0 - h - 4}" x2="{x0}" y2="{y0}" stroke="{LAC}" stroke-width="1.3"/><line x1="{x0}" y1="{y0}" x2="348" y2="{y0}" stroke="{LAC}" stroke-width="1.3"/>'
    for v in (2000, 4000, 6000):
        y = y0 - v / 6400 * h
        ic += f'<line x1="{x0}" y1="{y:.1f}" x2="348" y2="{y:.1f}" stroke="{GRI}" stroke-width="0.6" stroke-dasharray="3 3"/>' + yazi(x0 - 4, y + 3.5, f'{v:,}'.replace(',', '.'), 9, SOLUK, 'end', True)
    for k, (yil, v) in enumerate(veri):
        x, bh = 54 + k * 50, v / 6400 * h
        ic += f'<rect x="{x}" y="{y0 - bh:.1f}" width="30" height="{bh:.1f}" fill="{CAM}"/>' + yazi(x + 15, y0 - bh - 3.5, f'{v:,}'.replace(',', '.'), 10, LAC) + yazi(x + 15, y0 + 12, yil, 10, LAC)
    ic += yazi(194, 11, 'Marmara Gölü’nün alanı (hektar)', 10.5, LAC)
    return svg(360, 116, ic, 'Sütun grafiği, Marmara Gölü’nün alanı (hektar): 1975 5.949; 1986 5.168; 1995 4.731; 2002 5.300; 2011 5.580; 2018 3.464', 29)


def cizelge(bas, sat, en, etiket, en_fazla, boy=11):
    """Basit tablo: bas = başlıklar, sat = satırlar, en = sütun sınırlarının x değerleri."""
    H = 24 + 20 * len(sat)
    ic = kutu(4, 4, 352, H, '#fff', MAVI, 6, 1.3) + f'<rect x="4" y="4" width="352" height="24" rx="6" fill="{MAVI_A}"/>'
    sinir = [4] + en + [356]
    ic += ''.join(f'<line x1="{x}" y1="4" x2="{x}" y2="{4 + H}" stroke="{MAVI}" stroke-width="0.8"/>' for x in en)
    ic += ''.join(yazi((sinir[k] + sinir[k + 1]) / 2, 20, b, boy, LAC) for k, b in enumerate(bas))
    for r, s in enumerate(sat):
        y = 28 + r * 20
        ic += f'<line x1="4" y1="{y}" x2="356" y2="{y}" stroke="{MAVI}" stroke-width="0.8"/>' + ''.join(yazi((sinir[k] + sinir[k + 1]) / 2, y + 14, h, boy, LAC, 'middle', True) for k, h in enumerate(s))
    return svg(360, H + 8, ic, etiket, en_fazla)


def degisim_tablosu():
    return cizelge(['Dönem', 'Göl alanındaki değişim'], [['1975-1986', '781 hektar daraldı'], ['1986-1995', '437 hektar daraldı'], ['2002-2011', '280 hektar genişledi'], ['2011-2018', '2.116 hektar daraldı']], [130],
                   'Tablo: 1975-1986 arasında 781 hektar daraldı; 1986-1995 arasında 437 hektar daraldı; 2002-2011 arasında 280 hektar genişledi; 2011-2018 arasında 2.116 hektar daraldı', 28)


def butce_tablosu():
    return cizelge(['Su miktarı (milyon m³)', '2012', '2017'], [['Girdiler toplamı', '195,2', '31,65'], ['Çıktılar toplamı', '187,48', '111,63']], [180, 268],
                   'Tablo (milyon m³): girdiler toplamı 2012’de 195,2, 2017’de 31,65; çıktılar toplamı 2012’de 187,48, 2017’de 111,63', 18)


def mahalle():
    ic = kutu(4, 4, 352, 112, '#f4f1ea', GRI, 8, 1.2)
    for x in (92, 180, 268):
        ic += f'<rect x="{x - 5}" y="4" width="10" height="112" fill="#fff"/>'
    ic += f'<rect x="4" y="55" width="352" height="10" fill="#fff"/>'
    kuyu = {'K1': (48, 30), 'K2': (136, 90), 'K3': (224, 30), 'K4': (312, 90)}
    nokta = [(200, 14), (212, 44), (236, 46), (246, 22), (204, 30), (240, 34), (226, 14), (252, 40), (196, 46), (218, 84), (150, 40), (256, 82), (300, 30), (60, 84)]
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{KIR}"/>' for x, y in nokta)
    for ad, (x, y) in kuyu.items():
        ic += f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" rx="2" fill="{MAVI}"/>' + yazi(x, y + 19 if y < 60 else y - 10, ad, 10.5, LAC)
    return svg(360, 120, ic, 'Mahalle krokisi: dört kuyu (K1, K2, K3, K4) ve can kaybı yaşanan evleri gösteren kırmızı noktalar; noktaların çoğu K3 kuyusunun çevresinde toplanmış', 29)


def kanal():
    ic = kutu(4, 4, 352, 100, KUM, GRI, 8, 1.2)
    ic += f'<path d="M12 4 H348 a8 8 0 0 1 8 8 V26 Q250 38 180 30 Q100 22 4 30 V12 a8 8 0 0 1 8 -8 Z" fill="{SU}"/>' + yazi(90, 20, 'Akdeniz', 11, '#fff')
    ic += f'<path d="M206 104 Q210 84 196 70 L214 70 Q232 86 236 104 Z" fill="{SU}"/>' + yazi(262, 98, 'Kızıldeniz', 10.5, LAC)
    ic += f'<path d="M180 30 L204 72" stroke="{SU}" stroke-width="7"/>'
    ic += f'<rect x="178" y="47" width="28" height="7" rx="2" fill="{KIR}" transform="rotate(12 192 50)"/>'
    ic += yazi(80, 70, 'Mısır', 12, KAHVE) + f'<line x1="222" y1="46" x2="208" y2="50" stroke="{LAC}" stroke-width="1"/>' + yazi(264, 49, 'Sıkışan gemi', 10.5, LAC)
    return svg(360, 108, ic, 'Kroki: Mısır’da Akdeniz’i Kızıldeniz’e bağlayan dar kanal ve kanalda sıkışan gemi', 25)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = yerler()
    s[2]['gorsel'] = alan_grafik()
    s[3]['gorsel'] = degisim_tablosu()
    s[5]['gorsel'] = butce_tablosu()
    s[7]['gorsel'] = mahalle()
    s[9]['gorsel'] = kanal()
