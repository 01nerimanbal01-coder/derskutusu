"""9. sınıf İngilizce 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kaliplar = [('Must', 'Obligation / Rule', MAVI, MAVI_A), ('Used to', 'Past habit', YES, YES_A), ('Will', 'Future prediction', TUR, TUR_A), ('Need to', 'Necessity', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kaliplar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 11, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Modal verbs and tenses usage cards', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'FIRST CONDITIONAL · ENVIRONMENTAL ACTION', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, 'If we recycle waste paper, we will protect natural forests.', 11, LAC) + yazi(180, 70, 'Condition (Present Simple) + Result (Future Simple with Will)', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'First conditional environmental notice', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'DIALOGUE: PAST HABITS (USED TO)', 11, TUR)
    ic += yazi(180, 48, '“Did you use to play outside when you were a child?”', 11, LAC)
    ic += yazi(180, 68, '“Yes, I used to ride my bike in the garden every afternoon.”', 10, SOLUK, ince=True)
    return svg(360, 96, ic, 'Used to past habit dialogue card', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    yapilar = [('Used to + V1', 'No longer true', MAVI, MAVI_A), ('If + Present', 'Possible future', TUR, TUR_A), ('Tag: Isn\'t it?', 'Seeking confirm', YES, YES_A), ('Should + V1', 'Giving advice', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(yapilar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'English grammar patterns reference cards', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    steps = [('1. Set Limit', 'Define hours', YES, YES_A), ('2. Mute Alerts', 'Silence phone', MAVI, MAVI_A), ('3. Outdoor', 'Walk in park', TUR, TUR_A), ('4. Reading', 'Read a book', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Digital detox planning steps flowchart', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'QUESTION TAGS · CONFIRMATION PATTERN', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, '“You have finished your group project, haven\'t you?”', 11, LAC) + yazi(180, 70, 'Positive sentence takes a negative question tag.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Question tag rule board', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    colloc = [('Take care', 'İlgilenmek', MAVI, MAVI_A), ('Make decision', 'Karar vermek', TUR, TUR_A), ('Keep in touch', 'İletişimde kalmak', YES, YES_A), ('Do research', 'Araştırma yapmak', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(colloc):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 9.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'English collocations vocabulary cards', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'KEYWORD: E - A - R - T - H', 11.5, YES)
    harfler = [('1', 'E'), ('2', 'A'), ('3', 'R'), ('4', 'T'), ('5', 'H')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Earth keyword letter boxes', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
