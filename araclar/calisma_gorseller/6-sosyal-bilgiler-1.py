"""6. sınıf Sosyal Bilgiler 1. hafta (zaman içinde değişen gruplar ve roller) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def akraba():
    """Akrabalık şeması: yalnız adlar (rol yazılmaz; öğrenci ilişkiyi şemadan çıkarır)."""
    ic = ''
    ad = lambda x, y, metin, d, c: kutu(x - 40, y - 15, 80, 30, d, c) + yazi(x, y + 5, metin, 13, LAC)  # noqa: E731
    ic += ad(125, 20, 'Ahmet', MAVI_A, MAVI) + ad(235, 20, 'Leyla', KIR_A, KIR)
    ic += f'<line x1="165" y1="20" x2="195" y2="20" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<path d="M180 20 V52 M110 52 H250 M110 52 V66 M250 52 V66" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    ic += ad(110, 81, 'Selma', KIR_A, KIR) + ad(250, 81, 'Gül', KIR_A, KIR)
    ic += f'<path d="M110 96 V118 M250 96 V118" fill="none" stroke="{LAC}" stroke-width="1.6"/>'
    ic += ad(110, 133, 'Ada', KIR_A, KIR) + ad(250, 133, 'Can', MAVI_A, MAVI)
    ic += (f'<rect x="286" y="4" width="10" height="10" rx="2" fill="{KIR_A}" stroke="{KIR}"/>' + yazi(300, 13, 'kadın', 11, SOLUK, 'start', True)
           + f'<rect x="286" y="20" width="10" height="10" rx="2" fill="{MAVI_A}" stroke="{MAVI}"/>' + yazi(300, 29, 'erkek', 11, SOLUK, 'start', True))
    ic += yazi(180, 164, 'Çizgiler anne-babayı çocuklarına, eşleri birbirine bağlar.', 10.5, SOLUK, 'middle', True)
    return svg(340, 170, ic, 'Akrabalık şeması: Ahmet ile Leyla evli; çocukları Selma ve Gül. Selma’nın çocuğu Ada, Gül’ün çocuğu Can. Kutu renkleri: kadın kırmızı, erkek mavi.', 31)


def telefon():
    """Deniz'in telefonundaki dört grup bildirimi (ekran görüntüsü biçiminde; 2 × 2 kart, yarım sütunda okunur punto)."""
    bildirim = [('7-B Sınıf grubu', ['Yarın sınıfın nöbetçisi', 'Deniz.'], MAVI, MAVI_A),
                ('Aile', ['Deniz, kardeşini okuldan', 'alır mısın?'], KIR, KIR_A),
                ('Voleybol takımı', ['Cumartesi maçı var,', 'Deniz de kadroda.'], TUR, TUR_A),
                ('Kuzenler', ['Pazar günü dedemizin', 'evinde buluşalım.'], YES, YES_A)]
    ic = f'<rect x="2" y="2" width="356" height="146" rx="14" fill="#f5f7fc" stroke="{LAC}" stroke-width="3"/>'
    ic += f'<path d="M2 16 a14 14 0 0 1 14 -14 H344 a14 14 0 0 1 14 14 V24 H2 Z" fill="{LAC}"/>' + yazi(180, 18, 'Deniz’in telefonu · Bildirimler', 11, '#fff')
    for i, (grup, satirlar, c, d) in enumerate(bildirim):
        x, y = 10 + (i % 2) * 172, 31 + (i // 2) * 57
        ic += kutu(x, y, 166, 51, '#ffffff', d, 8, 1.4) + f'<circle cx="{x + 13}" cy="{y + 13}" r="5.5" fill="{c}"/>'
        ic += yazi(x + 24, y + 17, grup, 12, c, 'start') + ''.join(yazi(x + 10, y + 32 + j * 13, s, 11, LAC, 'start', True) for j, s in enumerate(satirlar))
    return svg(360, 150, ic, 'Deniz’in telefonundaki bildirimler: 7-B Sınıf grubu: Yarın sınıfın nöbetçisi Deniz. Aile: Deniz, kardeşini okuldan alır mısın? Voleybol takımı: Cumartesi maçı var, Deniz de kadroda. Kuzenler: Pazar günü dedemizin evinde buluşalım.', 36)


def degerler():
    """Üç değer rozeti."""
    ic = ''
    for i, (ad, c, d, sekil) in enumerate([('Paylaşma', TUR, TUR_A, 'pay'), ('Birlikte yaşama', YES, YES_A, 'ev'), ('Dayanışma', MAVI, MAVI_A, 'zincir')]):
        x = 60 + i * 120
        ic += f'<circle cx="{x}" cy="44" r="34" fill="{d}" stroke="{c}" stroke-width="2"/>'
        if sekil == 'pay':    # ikiye bölünmüş daire (paylaşılan bütün)
            ic += f'<circle cx="{x}" cy="40" r="16" fill="{c}"/><line x1="{x}" y1="22" x2="{x}" y2="58" stroke="#fff" stroke-width="3"/>'
        elif sekil == 'ev':   # tek çatı altında üç pencere
            ic += f'<path d="M{x - 20} 42 L{x} 24 L{x + 20} 42 Z" fill="{c}"/><rect x="{x - 15}" y="42" width="30" height="18" fill="{c}"/>'
            ic += ''.join(f'<rect x="{x - 11 + k * 8}" y="47" width="5" height="6" fill="#fff"/>' for k in range(3))
        else:                 # iç içe geçmiş halkalar
            ic += f'<circle cx="{x - 8}" cy="42" r="11" fill="none" stroke="{c}" stroke-width="4"/><circle cx="{x + 8}" cy="42" r="11" fill="none" stroke="{c}" stroke-width="4"/>'
        ic += yazi(x, 96, ad, 12.5, LAC)
    return svg(360, 104, ic, 'Üç değer rozeti: Paylaşma, Birlikte yaşama, Dayanışma', 24)


def yaslar():
    """Rol kartları (A-E); öğrenci yaşlarla eşleştirir."""
    kart = [('A', 'Üniversite öğrencisi', MOR, MOR_A), ('B', 'Sınıf nöbetçisi', MAVI, MAVI_A), ('C', 'Meslek grubunda idareci', KIR, KIR_A),
            ('D', ['Aile büyüğü:', 'dede ya da babaanne'], YES, YES_A), ('E', ['Meslek grubunda', 'çalışan (mühendis)'], TUR, TUR_A)]
    ic = ''
    for i, (h, ad, c, d) in enumerate(kart):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, d, c) + f'<circle cx="{x + 17}" cy="{y + 19}" r="10" fill="{c}"/>' + yazi(x + 17, y + 23.5, h, 12, '#fff')
        satirlar = ad if isinstance(ad, list) else [ad]
        for j, s in enumerate(satirlar):
            ic += yazi(x + 33, y + 23 + (j - (len(satirlar) - 1) / 2) * 13, s, 10.5, LAC, 'start')
    return svg(360, 136, ic, 'Rol kartları: A üniversite öğrencisi, B sınıf nöbetçisi, C meslek grubunda idareci, D aile büyüğü: dede ya da babaanne, E meslek grubunda çalışan (mühendis)', 27)


def odak():
    """Yuvarlak masa toplantısı: konu panosu ve rol kartları (insan figürü yok)."""
    ic = kutu(70, 4, 220, 38, '#ffffff', MOR, 6, 1.6) + yazi(180, 19, 'Konu:', 11, MOR) + yazi(180, 34, 'Okul kütüphanesini geliştirelim', 11.5, LAC, 'middle', True)
    ic += f'<ellipse cx="180" cy="98" rx="120" ry="38" fill="{TUR_A}" stroke="{TUR}" stroke-width="2"/>'
    for x, y in [(46, 76), (314, 76), (46, 122), (314, 122), (180, 146)]:
        ic += f'<circle cx="{x}" cy="{y}" r="10" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>'
    for x, y, ad in [(126, 88, 'Araştırmacı'), (236, 88, 'Lider'), (180, 114, 'Proje koordinatörü')]:
        w = 14 + len(ad) * 7.2
        ic += kutu(x - w / 2, y - 12, w, 21, '#ffffff', TUR, 4, 1.1) + yazi(x, y + 4, ad, 11, LAC)
    return svg(360, 160, ic, 'Yuvarlak masa toplantısı. Pano: Konu: Okul kütüphanesini geliştirelim. Masada rol kartları: Araştırmacı, Lider, Proje koordinatörü.', 34)


def elif_():
    """Elif'in 2012 ve 2026'daki grupları ve rolleri (yarım sütuna göre)."""
    sol = [('Aile', 'çocuk'), ('Okul', 'öğrenci'), ('Basketbol takımı', 'oyuncu')]
    sag = [('Aile', 'anne'), ('Meslek grubu', 'veteriner'), ('Sivil toplum kuruluşu', 'gönüllü')]
    ic = ''
    for k, (yil, liste, c, d) in enumerate([('Elif · 2012', sol, MAVI, MAVI_A), ('Elif · 2026', sag, TUR, TUR_A)]):
        x = 4 + k * 190
        ic += kutu(x, 4, 162, 130, d, c) + f'<rect x="{x}" y="4" width="162" height="25" rx="8" fill="{c}"/><rect x="{x}" y="18" width="162" height="11" fill="{c}"/>'
        ic += yazi(x + 81, 22, yil, 12.5, '#fff')
        for i, (g, r) in enumerate(liste):
            ic += yazi(x + 10, 47 + i * 29, f'{g}:', 11, SOLUK, 'start', True) + yazi(x + 10, 61 + i * 29, r, 12.5, c, 'start')
    ic += f'<line x1="169" y1="66" x2="187" y2="66" stroke="{LAC}" stroke-width="2"/><path d="M184 60 L194 66 L184 72 Z" fill="{LAC}"/>'
    return svg(360, 138, ic, 'Elif 2012: Aile çocuk, Okul öğrenci, Basketbol takımı oyuncu. Elif 2026: Aile anne, Meslek grubu veteriner, Sivil toplum kuruluşu gönüllü.', 33)


def gelecek():
    """Gelecekte üstlenilebilecek roller için seçenek kartları."""
    kart = [('Bilim projesi takımında', 'araştırmacı', CAM, CAM_A), ('Millî takımda', 'sporcu', KIR, KIR_A),
            ('Müzik grubunda', 'saz ustası', MOR, MOR_A), ('Meslek grubunda', 'veteriner', YES, YES_A)]
    ic = ''
    for i, (ust, rol, c, d) in enumerate(kart):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, d, c) + yazi(x + 86, y + 16, ust, 10, SOLUK, 'middle', True) + yazi(x + 86, y + 31, rol, 12, c)
    return svg(360, 92, ic, 'Kartlar: bilim projesi takımında araştırmacı, millî takımda sporcu, müzik grubunda saz ustası, meslek grubunda veteriner', 22)


def uygula(o):
    s = o['sorular']
    s[2]['gorsel'] = akraba()
    s[4]['gorsel'] = telefon()
    s[5]['gorsel'] = degerler()
    s[8]['gorsel'] = yaslar()
    s[9]['gorsel'] = odak()
    s[10]['gorsel'] = elif_()
    s[11]['gorsel'] = gelecek()
