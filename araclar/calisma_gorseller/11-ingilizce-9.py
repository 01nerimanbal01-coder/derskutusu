"""11. sınıf İngilizce 9. hafta görselleri: gerund/infinitive kutuları, başarı öyküsü şeridi, cümle kartları, takvim (SVG; insan figürü yok)."""
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


def cerceve(en, boy):
    return f'<rect x="2" y="2" width="{en - 4}" height="{boy - 4}" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="0.8"/>'


def kutu(x, y, w, h, d, c, r=7):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{d}" stroke="{c}" stroke-width="1"/>'


def fiil_kutulari():
    ic = cerceve(360, 132)
    for x, bas, liste, c, a in ((10, 'verb + V-ing', ['mind', 'suggest', 'keep', 'finish'], MAVI, MAVI_A), (184, 'verb + to V1', ['want', 'hope', 'plan', '?'], TUR, TUR_A)):
        ic += kutu(x, 10, 166, 112, a, c) + yazi(x + 83, 30, bas, 13, c)
        for i, f in enumerate(liste):
            xx, yy = x + 14 + (i % 2) * 72, 44 + (i // 2) * 36
            ic += kutu(xx, yy, 66, 28, '#fff', c, 14) + yazi(xx + 33, yy + 19, f, 12.5 if f != '?' else 16, KIR if f == '?' else LAC)
    return svg(ic, 360, 132, 'Gerund ve infinitive alan fiiller', 30)


def serit():
    ic = cerceve(360, 150)
    ic += f'<line x1="24" y1="58" x2="336" y2="58" stroke="{LAC}" stroke-width="2"/>'
    for x, t, a, b, c, d in ((84, 'Age 8', 'He could swim', '1 km easily.', MAVI, MAVI_A), (276, '2024 Final', 'Injured shoulder,', 'but won gold.', KIR, KIR_A)):
        ic += f'<circle cx="{x}" cy="58" r="7" fill="{c}"/>' + yazi(x, 42, t, 12.5, c)
        ic += kutu(x - 74, 76, 148, 54, d, c) + yazi(x, 98, a, 11.5, LAC, ince=True) + yazi(x, 116, b, 11.5, LAC, ince=True)
    ic += yazi(180, 24, 'Mert’s swimming story', 12, SOLUK, ince=True)
    ic += yazi(84, 144, 'I', 11, MAVI) + yazi(276, 144, 'II', 11, KIR)
    return svg(ic, 360, 150, 'Bir yüzücünün başarı öyküsü şeridi', 34)


def cumle_kartlari():
    k = ['Despite being blind, she became a famous pianist.', 'Although he lost a leg, he kept running.',
         'In spite of she was ill, she sang on stage.', 'Even though the test was hard, Ece passed it.']
    renk = [(MAVI, MAVI_A), (YES, YES_A), (MOR, MOR_A), (TUR, TUR_A)]
    ic = cerceve(360, 150)
    for i, t in enumerate(k):
        y = 10 + i * 34
        c, a = renk[i]
        ic += kutu(10, y, 340, 28, a, c, 6) + yazi(30, y + 19, ['I', 'II', 'III', 'IV'][i], 12.5, c) + yazi(52, y + 19, t, 11.5, LAC, 'start', True)
    return svg(ic, 360, 150, 'Dört İngilizce cümle kartı', 34)


def takvim():
    ic = cerceve(360, 112)
    ic += f'<rect x="120" y="14" width="120" height="86" rx="8" fill="#fff" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<rect x="120" y="14" width="120" height="26" rx="8" fill="{KIR}"/><rect x="120" y="30" width="120" height="10" fill="{KIR}"/>'
    ic += yazi(180, 32, 'JULY', 13, '#fff') + yazi(180, 66, 'Visit', 12, LAC) + yazi(180, 84, 'cousins', 12, LAC)
    for x in (140, 220):
        ic += f'<rect x="{x - 3}" y="8" width="6" height="14" rx="3" fill="{LAC}"/>'
    ic += yazi(60, 60, 'Now:', 12, SOLUK, ince=True) + yazi(60, 76, 'November', 12, SOLUK, ince=True)
    ic += f'<line x1="94" y1="64" x2="112" y2="64" stroke="{LAC}" stroke-width="1.6"/><polygon points="116,64 109,60 109,68" fill="{LAC}"/>'
    return svg(ic, 360, 112, 'Gelecek yaz için takvim notu', 26)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = fiil_kutulari()
    s[4]['gorsel'] = serit()
    s[7]['gorsel'] = cumle_kartlari()
    s[13]['gorsel'] = takvim()
