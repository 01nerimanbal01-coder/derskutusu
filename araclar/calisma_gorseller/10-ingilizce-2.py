"""10. sınıf İngilizce 2. hafta (Revision 1 & 2: Daily Life, Festivals, Smart Homes) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_vocabulary():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    words = [
        ('Habitats', 'Wildlife environments', MAVI, MAVI_A),
        ('Smart Home', 'Automated residence', YES, YES_A),
        ('Festival', 'Cultural celebration', TUR, TUR_A),
        ('Endangered', 'Species at risk', KIR, KIR_A)
    ]
    for i, (w, d, c, a) in enumerate(words):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, w, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'English vocabulary definition cards', 34)


def g1_linking():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(84, 32, 'Smart appliances', 10, MAVI)
    ic += yazi(84, 48, 'save domestic energy', 9.5, LAC, ince=True)
    ic += yazi(84, 72, '[ Advantage ]', 9, YES)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 28, 'LINKER: HOWEVER', 11, KIR)
    ic += yazi(257, 50, 'They can be quite', 9.5, LAC, ince=True)
    ic += yazi(257, 66, 'expensive initially.', 9.5, LAC, ince=True)
    ic += yazi(257, 80, '[ Contrast / Drawback ]', 8.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'However contrast linking word structure', 34)


def g2_idiom():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += kutu(14, 12, 120, 76, '#fef6ec', TUR, 6, 1.2)
    ic += f'<rect x="62" y="30" width="28" height="26" rx="4" fill="none" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<path d="M 90,36 C 96,36 96,48 90,48" fill="none" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(74, 74, 'Cup of Tea', 9.5, TUR)

    ic += kutu(146, 12, 200, 76, '#fffaf4', TUR, 6, 1.2)
    ic += yazi(246, 32, 'NOT MY CUP OF TEA', 11, TUR)
    ic += yazi(246, 52, 'Figurative Meaning:', 9.5, LAC)
    ic += yazi(246, 72, 'Not of interest or preference', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Idiom meaning explanation card', 34)


def g3_smart_home():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    devices = [
        ('Thermostat', 'Climate control', '#eaf8f0'),
        ('Solar Sensor', 'Clean electricity', '#d8f3e2'),
        ('Smart Plug', 'Schedule power', '#c7ebd2'),
        ('IoT Hub', 'Central wireless', '#b8e6c4')
    ]
    for i, (b, d, bg) in enumerate(devices):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Smart home connected devices grid', 34)


def g5_energy_saving():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    steps = [
        ('1. Monitor', 'Track energy use'),
        ('2. Install', 'LED & smart plug'),
        ('3. Automate', 'Timed shutdown'),
        ('4. Evaluate', 'Lower bills')
    ]
    for i, (b, acik) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#f2fbfd', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Home energy conservation flowchart', 34)


def g6_conservation():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 140, 76, '#ece4fd', MOR, 6, 1.2)
    ic += f'<circle cx="84" cy="46" r="22" fill="none" stroke="{MOR}" stroke-width="2"/>'
    ic += yazi(84, 50, 'NATURE', 9.5, MOR)
    ic += yazi(84, 76, 'Wildlife Reserve', 8.5, LAC)

    ic += kutu(168, 12, 178, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(257, 30, 'HABITAT PROTECTION', 10.5, MOR)
    ic += yazi(257, 48, '• Prevent deforestation', 9, LAC, ince=True)
    ic += yazi(257, 62, '• Guard wetland flyways', 9, LAC, ince=True)
    ic += yazi(257, 76, '• Stop illegal wildlife trade', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Wildlife reserve and habitat protection badge', 34)


def g8_culture_cards():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    countries = [
        ('Japan', 'Tokyo • Hanami', MAVI, MAVI_A),
        ('Spain', 'Madrid • Gracia', TUR, TUR_A),
        ('UK', 'London • High Tea', YES, YES_A),
        ('Australia', 'Canberra • Fauna', MOR, MOR_A)
    ]
    for i, (c, t, col, bg) in enumerate(countries):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, bg, col, 6, 1.2)
        ic += yazi(x + 40, 32, c, 11, col)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{col}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, t, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Country traditions and capitals comparison', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'KEY VOCABULARY STRIP: S - M - A - R - T', 11.5, YES)
    harfler = [('1', 'S'), ('2', 'M'), ('3', 'A'), ('4', 'R'), ('5', 'T')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Smart password letters key boxes', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_vocabulary()
    s[1]['gorsel'] = g1_linking()
    s[2]['gorsel'] = g2_idiom()
    s[3]['gorsel'] = g3_smart_home()
    s[5]['gorsel'] = g5_energy_saving()
    s[6]['gorsel'] = g6_conservation()
    s[8]['gorsel'] = g8_culture_cards()
    s[10]['gorsel'] = g10_sifre_seridi()
