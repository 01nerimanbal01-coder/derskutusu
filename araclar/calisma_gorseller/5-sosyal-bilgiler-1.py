"""5. sınıf Sosyal Bilgiler 1. hafta (gruplar ve roller) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A, SOLUK = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def harf(x, y, h, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{renk}"/>' + yazi(x, y + 4.5, h, 12, '#fff')


def ev(cx, cy):
    return (f'<path d="M{cx - 20} {cy} L{cx} {cy - 18} L{cx + 20} {cy} Z" fill="{KIR}"/>'
            f'<rect x="{cx - 15}" y="{cy}" width="30" height="22" fill="#fff3e0" stroke="{LAC}" stroke-width="1.2"/>'
            f'<rect x="{cx - 4}" y="{cy + 9}" width="8" height="13" fill="{TUR}"/><path d="M{cx - 3} {cy - 9} q3 -4 6 0 q-3 5 -3 5 q0 0 -3 -5z" fill="#fff"/>')


def okul(cx, cy):
    ic = f'<rect x="{cx - 24}" y="{cy - 6}" width="48" height="28" fill="#fdf6e3" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<path d="M{cx - 28} {cy - 6} L{cx} {cy - 18} L{cx + 28} {cy - 6} Z" fill="{MAVI}"/>'
    ic += ''.join(f'<rect x="{cx - 19 + k * 14}" y="{cy + 1}" width="8" height="7" fill="{MAVI_A}" stroke="{MAVI}" stroke-width=".8"/>' for k in range(3))
    ic += f'<rect x="{cx - 4}" y="{cy + 11}" width="8" height="11" fill="{MAVI}"/>'
    return ic + f'<line x1="{cx}" y1="{cy - 18}" x2="{cx}" y2="{cy - 30}" stroke="{LAC}" stroke-width="1.2"/><path d="M{cx} {cy - 30} h10 v6 h-10z" fill="{KIR}"/>'


def top_kale(cx, cy):
    ic = f'<path d="M{cx - 24} {cy + 20} V{cy - 10} H{cx + 24} V{cy + 20}" fill="none" stroke="{LAC}" stroke-width="2"/>'
    ic += ''.join(f'<line x1="{cx - 24 + k * 8}" y1="{cy - 10}" x2="{cx - 24 + k * 8}" y2="{cy + 20}" stroke="{GRI}" stroke-width=".7"/>' for k in range(1, 6))
    ic += f'<circle cx="{cx + 8}" cy="{cy + 12}" r="8" fill="#fff" stroke="{LAC}" stroke-width="1.2"/><path d="M{cx + 5} {cy + 9} l3 -2 l3 2 l-1 4 h-4z" fill="{LAC}"/>'
    return ic


def fidan(cx, cy, kalp=True):
    ic = f'<path d="M{cx - 20} {cy + 20} q20 -8 40 0 z" fill="#8a5a2b"/><line x1="{cx}" y1="{cy + 16}" x2="{cx}" y2="{cy - 6}" stroke="#6b4a2b" stroke-width="2.4"/>'
    ic += f'<ellipse cx="{cx - 8}" cy="{cy - 6}" rx="9" ry="5" fill="{YES}" transform="rotate(-25 {cx - 8} {cy - 6})"/><ellipse cx="{cx + 8}" cy="{cy - 10}" rx="9" ry="5" fill="{YES}" transform="rotate(25 {cx + 8} {cy - 10})"/>'
    return ic + (f'<path d="M{cx + 16} {cy - 22} c-4 -5 -10 0 -6 5 l6 6 l6 -6 c4 -5 -2 -10 -6 -5z" fill="{KIR}"/>' if kalp else '')


def gruplar():
    ic = ''
    for i, (h, ad, f) in enumerate([('K', 'Aile', ev), ('L', 'Okul', okul), ('M', 'Takım', top_kale), ('N', ('Sosyal', 'sorumluluk'), fidan)]):
        x = 4 + i * 90
        ic += f'<rect x="{x}" y="4" width="84" height="92" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>' + harf(x + 14, 18, h)
        ic += f(x + 44, 44) + (yazi(x + 42, 80, ad[0], 11, LAC) + yazi(x + 42, 92, ad[1], 11, LAC) if isinstance(ad, tuple) else yazi(x + 42, 88, ad, 12, LAC))
    return svg(364, 100, ic, 'Dört grup: K aile, L okul, M takım, N sosyal sorumluluk grubu', 23)


def program():
    gunler = [('Pazartesi', 'Okulda dersler', MAVI), ('Salı', 'Müzik kulübü çalışması', MOR), ('Perşembe', 'Hentbol takımı antrenmanı', TUR),
              ('Cumartesi', 'Park temizliği ekibinde gönüllü', YES), ('Pazar', 'Dede ve babaanne ziyareti', KIR)]
    ic = f'<rect x="4" y="4" width="352" height="142" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<rect x="4" y="4" width="352" height="22" rx="10" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 20, "Mira'nın haftalık programı", 12, '#fff')
    for i, (g, m, r) in enumerate(gunler):
        y = 32 + i * 23
        ic += f'<rect x="12" y="{y}" width="84" height="19" rx="5" fill="{r}"/>' + yazi(54, y + 14, g, 11.5, '#fff')
        ic += yazi(106, y + 14, m, 12, LAC, 'start')
    return svg(360, 150, ic, "Mira'nın haftalık programı: Pazartesi okulda dersler, Salı müzik kulübü, Perşembe hentbol takımı antrenmanı, Cumartesi park temizliği ekibinde gönüllü, Pazar dede ve babaanne ziyareti", 34)


def degisim():
    sol = ['4-A sınıfı: öğrenci', 'Futbol takımı: oyuncu']
    sag = ['5-B sınıfı: öğrenci', 'Satranç kulübü: üye', 'Sınıf: nöbetçi']
    ic = ''
    for k, (baslik, liste, d, c) in enumerate([('4. sınıfta', sol, MAVI_A, MAVI), ('5. sınıfta', sag, TUR_A, TUR)]):
        x = 4 + k * 196
        ic += f'<rect x="{x}" y="4" width="160" height="96" rx="8" fill="{d}" stroke="{c}" stroke-width="1.4"/>' + yazi(x + 80, 22, baslik, 12.5, c)
        ic += ''.join(yazi(x + 10, 44 + i * 19, m, 11.5, LAC, 'start') for i, m in enumerate(liste))
    ic += f'<line x1="168" y1="52" x2="192" y2="52" stroke="{LAC}" stroke-width="2"/><path d="M188 46 L198 52 L188 58 Z" fill="{LAC}"/>'
    return svg(364, 104, ic, "Kerem 4. sınıfta: 4-A sınıfı öğrencisi, mahalle futbol takımı oyuncusu. 5. sınıfta: 5-B sınıfı öğrencisi, satranç kulübü üyesi, sınıf nöbetçisi", 24)


def topluluklar():
    kart = [('K', ['Aynı otobüsteki, birbirini', 'tanımayan yolcular']), ('L', ['Okulun satranç kulübü', '']),
            ('M', ['Mahalledeki fidan dikme', 'gönüllüleri']), ('N', ['Bir voleybol takımı', ''])]
    ic = ''
    for i, (h, satir) in enumerate(kart):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.3"/>' + harf(x + 16, y + 22, h)
        dolu = [s for s in satir if s]
        for j, s in enumerate(dolu):
            ic += yazi(x + 32, y + 26 + (j - (len(dolu) - 1) / 2) * 14, s, 11, LAC, 'start')
    return svg(360, 104, ic, 'Dört topluluk: K aynı otobüste yolculuk eden birbirini tanımayan yolcular, L okulun satranç kulübü, M mahalledeki fidan dikme gönüllüleri, N bir voleybol takımı', 24)


def afis():
    ic = f'<rect x="60" y="4" width="240" height="120" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="2"/>'
    ic += yazi(180, 30, 'FİDAN DİKME GÜNÜ', 17, '#0c7a3c') + yazi(180, 52, 'Gönüllüler aranıyor!', 13, LAC)
    ic += yazi(180, 116, 'Cumartesi 10.00 · Mahalle parkı', 12, SOLUK)
    ic += fidan(116, 72, False) + fidan(244, 72, False)
    return svg(360, 128, ic, 'Afiş: Fidan dikme günü. Gönüllüler aranıyor. Cumartesi 10.00, Mahalle parkı', 28)


def gazete():
    ic = f'<rect x="4" y="4" width="352" height="22" rx="6" fill="{MOR}"/>' + yazi(180, 20, 'Sınıf gazetesi ekibi', 12.5, '#fff')
    gorev = [('Ada', 'Resimleri çiziyor.', TUR), ('Can', 'Haberleri yazıyor.', MAVI), ('Efe', 'Sayfaları bilgisayarda', YES)]  # Efe iki satır
    for i, (ad, m, r) in enumerate(gorev):
        x = 4 + i * 118
        ic += f'<rect x="{x}" y="32" width="112" height="70" rx="8" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        if i == 2:
            ic += yazi(x + 56, 52, ad, 13, r) + yazi(x + 56, 70, 'Sayfaları', 10.5, LAC) + yazi(x + 56, 83, 'bilgisayarda', 10.5, LAC) + yazi(x + 56, 96, 'düzenliyor.', 10.5, LAC)
        else:
            ic += yazi(x + 56, 52, ad, 13, r) + yazi(x + 56, 72, m, 10.5, LAC)
    return svg(360, 106, ic, 'Sınıf gazetesi ekibi: Ada resimleri çiziyor, Can haberleri yazıyor, Efe sayfaları bilgisayarda düzenliyor', 24)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = gruplar()
    s[4]['gorsel'] = program()
    s[6]['gorsel'] = degisim()
    s[7]['gorsel'] = topluluklar()
    s[9]['gorsel'] = afis()
    s[10]['gorsel'] = gazete()
