"""11. sınıf TDE 9. hafta görselleri: e-posta ve dilekçe şablonları, anlatım kartları, puanlama anahtarı (SVG; insan figürü yok)."""
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


def no(x, y, n, renk=TUR):
    return f'<circle cx="{x}" cy="{y}" r="8.5" fill="{renk}"/>' + yazi(x, y + 4, n, 11, '#fff')


def cubuk(x, y, w):
    return f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2.5" fill="#d5dae4"/>'


def eposta():
    ic = cerceve(360, 200)
    ic += f'<rect x="12" y="10" width="336" height="182" rx="6" fill="#fff" stroke="{GRI}" stroke-width="1"/>'
    ic += f'<rect x="12" y="10" width="336" height="20" rx="6" fill="{MAVI}"/><rect x="12" y="22" width="336" height="8" fill="{MAVI}"/>'
    ic += yazi(24, 24, 'Yeni ileti', 11, '#fff', 'start')
    alan = [('1', 'Kime:', 'mudurluk@ornekokul.k12.tr'), ('2', 'Bilgi (CC):', 'rehberlik@ornekokul.k12.tr'), ('3', 'Konu:', 'Hocam')]
    for i, (n, a, d) in enumerate(alan):
        y = 46 + i * 22
        ic += no(30, y - 4, n) + yazi(46, y, a, 11.5, SOLUK, 'start') + yazi(124, y, d, 11.5, LAC, 'start', True)
        ic += f'<line x1="44" y1="{y + 7}" x2="340" y2="{y + 7}" stroke="#e3e7ee" stroke-width="1"/>'
    ic += no(30, 116, '4') + yazi(46, 120, 'Sayın Müdürüm,', 11.5, LAC, 'start', True)
    for i, w in enumerate((280, 260, 230)):
        ic += cubuk(46, 132 + i * 11, w)
    ic += no(30, 176, '5') + yazi(46, 180, 'Saygılarımla · Deniz Kaya · 11-B sınıfı', 11.5, LAC, 'start', True)
    return svg(ic, 360, 200, 'Numaralı bölümleriyle bir e-posta', 42)


def dilekce():
    ic = cerceve(360, 210)
    ic += f'<rect x="70" y="10" width="220" height="190" fill="#fff" stroke="{GRI}" stroke-width="1"/>'
    ic += f'<rect x="110" y="20" width="140" height="22" rx="3" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="0.8"/>' + yazi(180, 35, 'Makam adı', 10.5, MAVI)
    ic += f'<rect x="82" y="54" width="196" height="64" rx="3" fill="{YES_A}" stroke="{YES}" stroke-width="0.8"/>'
    for i, w in enumerate((176, 186, 160, 120)):
        ic += cubuk(90, 64 + i * 13, w)
    ic += f'<rect x="196" y="128" width="84" height="40" rx="3" fill="{MOR_A}" stroke="{MOR}" stroke-width="0.8"/>'
    ic += yazi(238, 144, 'Tarih · İmza', 10, MOR) + yazi(238, 158, 'Ad Soyad', 10, MOR)
    ic += f'<rect x="80" y="160" width="96" height="32" rx="3" fill="{TUR_A}" stroke="{TUR}" stroke-width="0.8"/>' + yazi(128, 180, 'Adres · Ekler', 10, TUR)
    for x, y, h in ((60, 31, 'K'), (60, 86, 'L'), (300, 148, 'M'), (60, 176, 'N')):
        ic += yazi(x, y + 5, h, 14, LAC, 'end' if x < 100 else 'start')
    return svg(ic, 360, 210, 'Dilekçe şablonu', 42)


def kartlar():
    k = [('I', 'Başvurumun sonucunu öğrenmek istiyorum.'), ('II', 'Etkinliğe tüm öğrencilerin hepsi katıldı.'),
         ('III', 'Ödevini bitirince kardeşini aradı.'), ('IV', 'Mevzubahis talebimin tetkikini istirham ederim.')]
    ic = cerceve(360, 150)
    renk = [(MAVI, MAVI_A), (YES, YES_A), (MOR, MOR_A), (TUR, TUR_A)]
    for i, (n, t) in enumerate(k):
        y = 10 + i * 34
        c, a = renk[i]
        ic += f'<rect x="10" y="{y}" width="340" height="28" rx="6" fill="{a}" stroke="{c}" stroke-width="1"/>'
        ic += yazi(30, y + 19, n, 12.5, c) + yazi(52, y + 19, t, 11.5, LAC, 'start', True)
    return svg(ic, 360, 150, 'Dört cümle kartı', 34)


def metin():
    ic = cerceve(360, 132)
    ic += f'<rect x="12" y="10" width="336" height="112" rx="5" fill="#fff" stroke="{GRI}" stroke-width="1"/>'
    A = f'<tspan font-weight="700" text-decoration="underline" fill="{LAC}">'
    N = lambda n: f'</tspan><tspan font-weight="700" font-size="9.5" fill="{KIR}" baseline-shift="super"> {n}</tspan><tspan>'
    satir = [f'Okul {A}Müdürlüğüne{N("I")}',
             f'Kulübümüzün etkinlik raporunu Millî Eğitim {A}Bakanlığı&#39;na{N("II")}',
             f'ileteceğiz. {A}2026-2027{N("III")} eğitim öğretim yılı için gereğini',
             f'{A}arz ederim{N("IV")}.']
    for k, t in enumerate(satir):
        ic += f'<text x="24" y="{38 + k * 24}" font-size="12" {INCE} fill="{LAC}"><tspan>{t}</tspan></text>'
    return svg(ic, 360, 132, 'Altı çizili sözcükleri olan dilekçe metni', 30)


def rubrik():
    ic = cerceve(360, 150)
    satir = [('Ölçüt', 'Puan (1–4)'), ('İçerik ve amaç', '4'), ('Yapı ve bölümler', '3'), ('Dil ve anlatım', '4'), ('Yazım ve noktalama', '2')]
    for i, (a, b) in enumerate(satir):
        y = 12 + i * 26
        d = MAVI if i == 0 else ('#fff' if i % 2 else GRI_A)
        ic += f'<rect x="40" y="{y}" width="280" height="26" fill="{d}" stroke="#dde2ea" stroke-width="1"/>'
        r = '#fff' if i == 0 else LAC
        ic += yazi(54, y + 17.5, a, 12, r, 'start', i != 0) + yazi(270, y + 17.5, b, 12.5, r)
    ic += f'<line x1="220" y1="12" x2="220" y2="142" stroke="#dde2ea" stroke-width="1"/>'
    return svg(ic, 360, 150, 'Dereceli puanlama anahtarı', 32)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = eposta()
    s[2]['gorsel'] = dilekce()
    s[4]['gorsel'] = kartlar()
    s[6]['gorsel'] = metin()
    s[9]['gorsel'] = rubrik()
