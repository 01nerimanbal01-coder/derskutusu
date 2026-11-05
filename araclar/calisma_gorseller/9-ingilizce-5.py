"""9. sınıf ingilizce 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def g0():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [( 'Skimming', 'Ana fikri bulma', MAVI, MAVI_A), ('Scanning', 'Özel detay tarama', YES, YES_A), ('Cybersecurity', 'Siber güvenlik', TUR, TUR_A), ('Self-Reflection', 'Öz değerlendirme', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Okuma ve değerlendirme kavramları', 34)

def g1():
    b, s1, s2 = ('ROOTS & ROUTES · CYBERSECURITY EDUCATION AT SCHOOL', 'CAN: Use strong passwords & protect personal data', 'CAN\'T: Share private passwords or click unsafe links')
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, b, 10, MAVI)
    ic += kutu(16, 36, 328, 64, '#f4f8fe', MAVI) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Siber güvenlik eğitimi kuralları', 34)

def g2():
    b, s1, s2 = ('READING STRATEGIES: SKIMMING VS. SCANNING', 'Skimming: Reading quickly for the main idea / best title', 'Scanning: Looking for specific details (names, dates, capitals)')
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, b, 10, TUR) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Skimming ve scanning okuma stratejileri', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('29 October', 'Republic Day', MAVI, MAVI_A), ('23 April', 'Children\'s Day', TUR, TUR_A), ('19 May', 'Youth & Sports', YES, YES_A), ('State Verbs', 'know, like, need', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Millî günler ve durum fiilleri', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Greeting', 'Country & Ankara', YES, YES_A), ('2. Attractions', 'Historical sites', MAVI, MAVI_A), ('3. Celebrations', 'National days', TUR, TUR_A), ('4. Reflection', 'Check portfolio', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Introducing Türkiye sunum adımları', 34)

def g6():
    b, s1, s2 = ('GRAMMAR FOCUS · PRESENT CONTINUOUS TENSE', 'Look! The students are performing folk dances right now.', 'Time expressions: now, right now, at the moment, today, Look!')
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, b, 10, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, s1, 9.8, LAC) + yazi(180, 84, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Simple Present ve Present Continuous farkı', 34)

def g7():
    b, s1, s2 = ('THEME 1 VOCABULARY · SCHOOL LIFE & CULTURE', 'National Anthem (Millî Marş) · Cybersecurity · E-Portfolio', 'Students introduce Türkiye\'s cultural heritage safely online.')
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, b, 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Millî marş, siber güvenlik ve portfolyo', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('Heritage', 'Kültürel miras', MAVI, MAVI_A), ('Folk Dance', 'Halk oyunları', TUR, TUR_A), ('Personal Data', 'Kişisel veriler', YES, YES_A), ('Attractions', 'Turistik yerler', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Kültürel miras ve turistik yerler', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
