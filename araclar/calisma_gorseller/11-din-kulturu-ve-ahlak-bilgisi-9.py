"""11. sınıf Din Kültürü 9. hafta görselleri: din-felsefe ilişkisi (SVG şemalar; insan figürü yok, ayet metni yok)."""
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


def venn():
    ic = cerceve(360, 150)
    ic += f'<ellipse cx="128" cy="76" rx="100" ry="62" fill="{YES}" fill-opacity="0.15" stroke="{YES}" stroke-width="1.4"/>'
    ic += f'<ellipse cx="232" cy="76" rx="100" ry="62" fill="{MAVI}" fill-opacity="0.15" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(80, 52, 'DİN', 13, YES) + yazi(86, 74, 'Kaynak: vahiy', 10.5, LAC, ince=True) + yazi(86, 90, 'Yöntem: iman,', 10.5, LAC, ince=True) + yazi(88, 104, 'ibadet, salih amel', 10, LAC, ince=True)
    ic += yazi(280, 52, 'FELSEFE', 13, MAVI) + yazi(274, 74, 'Kaynak: akıl,', 10.5, LAC, ince=True) + yazi(274, 90, 'merak, şüphe', 10.5, LAC, ince=True) + yazi(272, 104, 'Yöntem: sorgulama', 10, LAC, ince=True)
    ic += f'<circle cx="180" cy="76" r="17" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>' + yazi(180, 83, '?', 18, KIR)
    return svg(ic, 360, 150, 'Din ve felsefenin karşılaştırma şeması', 34)


def zaman():
    ic = cerceve(360, 128)
    ic += f'<line x1="16" y1="62" x2="344" y2="62" stroke="{LAC}" stroke-width="2.2"/>'
    olay = [(40, '9. yy', 'Kindî', 'Bağdat'), (110, '10. yy', 'Fârâbî', 'Bağdat-Şam'), (180, '11. yy', 'İbn Sînâ', 'Buhara-Hemedan'),
            (250, '11-12. yy', 'Gazzâlî', 'Tus-Bağdat'), (320, '12. yy', 'X', 'Endülüs')]
    for x, t, ad, yer in olay:
        c = KIR if ad == 'X' else MAVI
        ic += f'<circle cx="{x}" cy="62" r="6" fill="{c}"/>' + yazi(x, 46, t, 11.5, c)
        if ad == 'X':
            ic += f'<circle cx="{x}" cy="90" r="11" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>' + yazi(x, 95, 'X', 13, KIR)
        else:
            ic += yazi(x, 92, ad, 11.5, LAC)
        ic += yazi(x, 116, yer, 9.5, SOLUK, ince=True)
    return svg(ic, 360, 128, 'İslam düşünürleri zaman şeridi', 30)


def agac():
    ic = cerceve(360, 140)
    ic += kutu(130, 12, 100, 32, GRI_A, LAC) + yazi(180, 33, 'Varlık', 13)
    ic += f'<path d="M 180 44 L 180 58 M 90 58 L 270 58 M 90 58 L 90 72 M 270 58 L 270 72" fill="none" stroke="{LAC}" stroke-width="1.4"/>'
    ic += kutu(20, 72, 140, 56, KIR_A, KIR) + yazi(90, 94, 'Zorunlu Varlık', 12, KIR) + yazi(90, 116, '?', 16, KIR)
    ic += kutu(200, 72, 140, 56, MAVI_A, MAVI) + yazi(270, 94, 'Mümkün Varlık', 12, MAVI) + yazi(270, 114, 'yaratılmışlar', 11, LAC, ince=True)
    return svg(ic, 360, 140, 'İbn Sînâ’nın varlık ayrımı', 30)


def kavram_kartlari():
    k = [('I', 'Taakkul', MAVI, MAVI_A), ('II', 'Tefekkür', YES, YES_A), ('III', 'Tedebbür', MOR, MOR_A), ('IV', 'Tezekkür', TUR, TUR_A)]
    ic = cerceve(360, 92)
    for i, (n, t, c, a) in enumerate(k):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 68, a, c) + yazi(x + 40, 36, n, 13, c) + f'<line x1="{x + 12}" y1="46" x2="{x + 68}" y2="46" stroke="{c}" stroke-width="0.6"/>' + yazi(x + 40, 66, t, 12, LAC)
    return svg(ic, 360, 92, 'Dört kavram kartı', 22)


def aktarim():
    ic = cerceve(360, 120)
    k = [(10, 'Bağdat', 'Beytülhikme', MAVI, MAVI_A), (128, 'Toledo · Sicilya', 'Latince çeviri', MOR, MOR_A), (246, 'Avrupa', '12. yy ve sonrası', YES, YES_A)]
    for x, a, b, c, d in k:
        ic += kutu(x, 24, 104, 60, d, c) + yazi(x + 52, 50, a, 11.5, c) + yazi(x + 52, 68, b, 10.5, LAC, ince=True)
    for x in (115, 233):
        ic += f'<line x1="{x}" y1="54" x2="{x + 8}" y2="54" stroke="{LAC}" stroke-width="1.6"/><polygon points="{x + 12},54 {x + 5},50 {x + 5},58" fill="{LAC}"/>'
    ic += yazi(180, 106, 'Fârâbî, İbn Sînâ ve İbn Rüşd’ün eserleri', 10.5, SOLUK, ince=True)
    return svg(ic, 360, 120, 'Eserlerin Avrupa’ya aktarım yolu', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = venn()
    s[3]['gorsel'] = zaman()
    s[5]['gorsel'] = agac()
    s[7]['gorsel'] = kavram_kartlari()
    s[12]['gorsel'] = aktarim()
