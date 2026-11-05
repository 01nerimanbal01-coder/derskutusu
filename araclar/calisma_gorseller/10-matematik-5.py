# -*- coding: utf-8 -*-
"""10-matematik-5 çalışma kâğıdı görselleri.
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
    svg = kart4('ÜÇGENDE ALAN TEMEL BAĞINTILARI', [('Taban × Yükseklik', 'A = (a · h_a) / 2'), ('Sinüs Alan', 'A = ½ · b · c · sin A'), ('Eşkenar Üçgen', '__ESKENAR__'), ('Benzerlik-Alan', 'A₁ / A₂ = k²')], '10-matematik-5 alan bağıntıları')
    return svg.replace(
        '<text x="222.0" y="78.0" text-anchor="middle" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">__ESKENAR__</text>',
        '<text x="207.5" y="78.0" text-anchor="end" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">A = (a² · </text>'
        '<path d="M 208.5 75.0 L 210.0 75.0 L 211.5 78.5 L 214.0 70.5 L 220.5 70.5" fill="none" stroke="#0b2257" stroke-width="0.9" stroke-linecap="round" stroke-linejoin="round"/>'
        '<text x="217.2" y="78.0" text-anchor="middle" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">3</text>'
        '<text x="221.5" y="78.0" text-anchor="start" font-size="7.5" font-family="Noto Sans, sans-serif" font-weight="400" fill="#0b2257">) / 4</text>'
    )

def g1():
    return karsilastir2('SİNÜS ALAN TEOREMİ UYGULAMASI', 'Verilen Ölçüler', '|AB| = 8 cm, |AC| = 10 cm', 'Aradaki açı: m(A) = 30° (sin 30° = ½)', 'Alan Hesabı', 'Alan = ½ · 8 · 10 · sin 30°', 'Alan = 40 · ½ = 20 cm²', '10-matematik-5 sinüs alan hesabı')

def g2():
    return karsilastir2('PARALEL DOĞRULARDA ALAN TAŞIMA', 'Sabit Unsurlar (d₁ // d₂)', 'Taban [BC] sabit uzunlukta', 'Paraleller arası h yüksekliği sabit', 'Sonuç', 'Tepe noktası d₁ üzerinde kaysa da', 'Alan(ABC) = Alan(A\'BC) değişmez', '10-matematik-5 alan taşıma')

def g3():
    return uclu_sema('TABAN-ALAN ORANTISI VE KENARORTAY', [('Eşit Yükseklik', 'Alanlar tabanla orantılı', 'S₁ / S₂ = a / b'), ('Kenarortay', 'Tabanı ikiye böler', 'Alan: S ve S'), ('Ağırlık Merkezi', '3 kenarortay kesişir', '6 eş alan (6S)')], '10-matematik-5 taban alan paylaşımı')

def g5():
    return kart4('BENZER ÜÇGENDE ALAN ADIMLARI (k = 2/5)', [('1. Oran Bul', 'k = |AD|/|AB| = 2/5'), ('2. Karesini Al', 'k² = 4 / 25'), ('3. Tüm Alan', '4S=12 -> 25S=75'), ('4. Dörtgen', '75 - 12 = 63 br²')], '10-matematik-5 benzerlik alan adımları')

def g6():
    return karsilastir2('TABAN ORANINA GÖRE ALAN PAYLAŞIMI', 'Oran: 3·|BD| = 2·|DC|', '|BD| = 2k -> Alan(ABD) = 2S', '|DC| = 3k -> Alan(ADC) = 3S', 'Toplam Alan Çözümü', 'Toplam 5S = 45 cm² -> S = 9 cm²', 'Alan(ABD) = 2S = 18 cm²', '10-matematik-5 taban paylaşımı')

def g8():
    return kart4('MERDİVEN ALAN KURALI (EŞİT ARALIKLAR)', [('1. Dilim', 'Üst üçgen: S'), ('2. Dilim', 'Orta şerit: 3S'), ('3. Dilim', 'Alt şerit: 5S'), ('4. Dilim', 'Taban şeridi: 7S')], '10-matematik-5 merdiven kuralı')

def g11():
    return karsilastir2('NEDEN ALANLAR ORANI k² OLUR?', 'Uzunluk Boyutu (1B)', 'Taban: a\' = k · a', 'Yükseklik: h\' = k · h', 'Alan Boyutu (2B)', 'A\' = ½ · (k·a) · (k·h)', 'A\' = k² · (½·a·h) = k² · A', '10-matematik-5 k kare ispatı')

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
