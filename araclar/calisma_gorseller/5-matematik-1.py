"""5. sınıf Matematik 1. hafta çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES = '#0b2257', '#2451d6', '#ee7d12', '#12a150'
MAVI_A, TUR_A, GRI = '#e8eefe', '#fff1df', '#9aa6bd'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket):
    return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{etiket}">{ic}</svg>'


def ok(kimlik, renk):
    return (f'<defs><marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{renk}"/></marker></defs>')


def nokta(x, y, harf, dx=0, dy=-12, renk=LAC):
    return (f'<circle cx="{x}" cy="{y}" r="4.2" fill="{renk}"/>'
            f'<text x="{x + dx}" y="{y + dy}" text-anchor="middle" font-size="15" {YAZI} fill="{renk}">{harf}</text>')


def isin():
    ic = ok('ck5ok1', MAVI)
    ic += f'<line x1="40" y1="46" x2="292" y2="46" stroke="{MAVI}" stroke-width="3" stroke-linecap="round" marker-end="url(#ck5ok1)"/>'
    ic += nokta(40, 46, 'A', 0, 26) + nokta(170, 46, 'B', 0, 26)
    return svg(320, 84, ic, 'A noktasından başlayıp B noktasından geçerek uzanan ışın')


def araclar():
    ic = ''
    # 1 cetvel
    ic += f'<rect x="8" y="30" width="112" height="26" rx="3" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += ''.join(f'<line x1="{14 + i * 10}" y1="30" x2="{14 + i * 10}" y2="{40 if i % 5 == 0 else 36}" stroke="{TUR}" stroke-width="1.2"/>' for i in range(11))
    # 2 çizgeç (ölçüsüz)
    ic += f'<rect x="140" y="30" width="112" height="26" rx="3" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    # 3 gönye
    ic += f'<path d="M280 70 L280 14 L346 70 Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8" stroke-linejoin="round"/>'
    ic += f'<path d="M280 60 H290 V70" fill="none" stroke="{MAVI}" stroke-width="1.4"/>'
    # 4 pergel
    ic += f'<circle cx="398" cy="14" r="5" fill="{LAC}"/><line x1="398" y1="18" x2="380" y2="70" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<line x1="398" y1="18" x2="418" y2="66" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/><path d="M416 62 l6 12 l-8 -3z" fill="{TUR}"/>'
    # 5 açıölçer
    ic += f'<path d="M448 70 A46 46 0 0 1 540 70 Z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += ''.join(f'<line x1="{494 + 38 * c:.1f}" y1="{70 - 38 * s:.1f}" x2="{494 + 44 * c:.1f}" y2="{70 - 44 * s:.1f}" stroke="{TUR}" stroke-width="1.2"/>'
                  for c, s in [(1, 0), (.866, .5), (.5, .866), (0, 1), (-.5, .866), (-.866, .5), (-1, 0)])
    ic += f'<circle cx="494" cy="70" r="2.5" fill="{TUR}"/>'
    for x, ad in [(64, 'cetvel'), (196, 'çizgeç'), (306, 'gönye'), (400, 'pergel'), (494, 'açıölçer')]:
        ic += f'<text x="{x}" y="96" text-anchor="middle" font-size="14" {YAZI} fill="{LAC}">{ad}</text>'
    return svg(550, 104, ic, 'Cetvel, çizgeç, gönye, pergel ve açıölçer').replace('<svg ', '<svg style="max-height:21mm" ', 1)


def aci():
    ic = ok('ck5ok2', MAVI)
    ic += f'<path d="M60 130 L250 130" stroke="{MAVI}" stroke-width="3" stroke-linecap="round" marker-end="url(#ck5ok2)"/>'
    ic += f'<path d="M60 130 L205 30" stroke="{MAVI}" stroke-width="3" stroke-linecap="round" marker-end="url(#ck5ok2)"/>'
    ic += f'<path d="M96 130 A36 36 0 0 0 89.6 109.6" fill="none" stroke="{TUR}" stroke-width="2.4"/>'
    ic += nokta(60, 130, 'B', -14, 5) + nokta(150, 68, 'A', -10, -8) + nokta(190, 130, 'C', 0, 22)
    return svg(270, 160, ic, 'Köşesi B, kolları BA ve BC ışınları olan açı')


def cember():
    ic = f'<circle cx="130" cy="88" r="68" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2.6"/>'
    ic += f'<line x1="130" y1="88" x2="182" y2="44.3" stroke="{TUR}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<line x1="62" y1="88" x2="198" y2="88" stroke="{YES}" stroke-width="3" stroke-linecap="round"/>'
    ic += nokta(130, 88, 'M', 0, 22) + nokta(182, 44.3, 'A', 12, -6) + nokta(62, 88, 'B', -14, 5) + nokta(198, 88, 'C', 14, 5)
    return svg(260, 170, ic, 'Merkezi M olan çember; A çember üzerinde, B ve C çember üzerinde ve BC doğru parçası M noktasından geçiyor')


def borular():
    ic = f'<line x1="20" y1="140" x2="340" y2="140" stroke="{LAC}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<text x="330" y="160" font-size="15" {YAZI} font-style="italic" fill="{LAC}">d</text>'
    ic += f'<rect x="20" y="140" width="320" height="10" fill="{MAVI_A}"/>'
    px, py = 180, 30
    for x2, no in [(70, '1'), (180, '2'), (300, '3')]:
        ic += f'<line x1="{px}" y1="{py}" x2="{x2}" y2="140" stroke="{TUR}" stroke-width="4" stroke-linecap="round" opacity=".9"/>'
        mx, my = (px + x2) / 2, (py + 140) / 2
        ic += f'<circle cx="{mx + (10 if x2 >= 180 else -10)}" cy="{my}" r="10" fill="#fff" stroke="{TUR}" stroke-width="1.6"/>'
        ic += f'<text x="{mx + (10 if x2 >= 180 else -10)}" y="{my + 5}" text-anchor="middle" font-size="12" {YAZI} fill="{TUR}">{no}</text>'
    ic += nokta(px, py, 'P', 0, -10)
    return svg(360, 168, ic, 'P noktasındaki kuyudan d doğrusu olan su kanalına üç boru; 1 ve 3 eğik, 2 dik')


def ucgen():
    A, B, C, D = (150, 24), (40, 150), (290, 150), (190, 150)
    ic = f'<path d="M{A[0]} {A[1]} L{B[0]} {B[1]} L{C[0]} {C[1]} Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2.6" stroke-linejoin="round"/>'
    ic += f'<line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{MAVI}" stroke-width="2.6"/>'
    ic += nokta(*A, 'A', 0, -10) + nokta(*B, 'B', -14, 5) + nokta(*C, 'C', 14, 5) + nokta(*D, 'D', 0, 22)
    return svg(330, 176, ic, 'A, B, C noktaları ve BC üzerindeki D noktası; A ile D birleştirilmiş')


def nesneler():
    ic = ''
    # 1 hulahop
    ic += f'<ellipse cx="60" cy="58" rx="44" ry="44" fill="none" stroke="{TUR}" stroke-width="7"/>'
    # 2 bozuk para
    ic += f'<circle cx="180" cy="58" r="34" fill="#f2c14e" stroke="#c9961f" stroke-width="3"/><circle cx="180" cy="58" r="25" fill="none" stroke="#c9961f" stroke-width="1.5"/>'
    # 3 yüzük
    ic += f'<circle cx="290" cy="64" r="26" fill="none" stroke="#b9bfca" stroke-width="7"/><path d="M280 36 l10 -12 l10 12 l-10 8z" fill="#7cc7ff" stroke="#3a8fd6" stroke-width="1.5"/>'
    # 4 yuvarlak masa
    ic += f'<line x1="395" y1="70" x2="385" y2="104" stroke="#8a5a2b" stroke-width="5" stroke-linecap="round"/><line x1="445" y1="70" x2="455" y2="104" stroke="#8a5a2b" stroke-width="5" stroke-linecap="round"/>'
    ic += f'<ellipse cx="420" cy="60" rx="58" ry="18" fill="#d9a066" stroke="#8a5a2b" stroke-width="2.5"/>'
    for x, no in [(60, '1'), (180, '2'), (290, '3'), (420, '4')]:
        ic += f'<circle cx="{x}" cy="124" r="11" fill="{LAC}"/><text x="{x}" y="129" text-anchor="middle" font-size="13" {YAZI} fill="#fff">{no}</text>'
    return svg(490, 140, ic, '1 hulahop, 2 bozuk para, 3 yüzük, 4 yuvarlak masa').replace('<svg ', '<svg style="max-height:22mm" ', 1)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = isin()
    s[3]['gorsel'] = araclar()
    s[5]['gorsel'] = aci()
    s[9]['gorsel'] = cember()
    s[10]['gorsel'] = borular()
    s[11]['gorsel'] = ucgen()
    s[12]['gorsel'] = nesneler()
