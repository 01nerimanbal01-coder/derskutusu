"""9. sınıf Kimya 8. hafta görselleri (SVG; insan figürü yok K024; K178 beyaz bant yok; max-height:24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'
STIL = 'width:100%;max-height:24mm;display:block;margin:1mm auto;'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="{STIL}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 77, a, c, 5, 0.75)
        ic += yazi(x + 40, 46, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="54" x2="{x + 72}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 90, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, c1)
    ic += kutu(12, 28, 162, 77, a1, c1, 6, 0.75)
    ic += yazi(93, 46, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="54" x2="164" y2="54" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 72, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 91, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 28, 162, 77, a2, c2, 6, 0.75)
    ic += yazi(267, 46, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="54" x2="338" y2="54" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 72, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 91, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 77, a, c, 6, 0.75)
        ic += yazi(x + 54, 46, b, 8.6, c)
        ic += f'<line x1="{x + 10}" y1="54" x2="{x + 98}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 91, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 8 + i * 87
        ic += kutu(x, 28, 79, 77, a, c, 5, 0.75)
        ic += yazi(x + 39.5, 46, b, 8.2, c)
        ic += yazi(x + 39.5, 70, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39.5, 89, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ox = x + 80.5
            ic += f'<polygon points="{ox:.1f},62 {ox+5:.1f},66.5 {ox:.1f},71" fill="{ana_renk}"/>'
    return svg(ic, etiket)

def g0():
    return kart4('PERİYODİK TABLODA ÖZEL GRUP ADLARI VE BLOKLAR', [
        ('1A & 2A (s Bloğu)', '1A: Alkali Metaller', '2A: Toprak Alkali'),
        ('3A & 6A (p Bloğu)', '3A: Toprak Metalleri', '6A: Kalkojenler'),
        ('7A & 8A (p Bloğu)', '7A: Halojenler (17)', '8A: Soy Gazlar (18)'),
        ('B Grupları (d/f)', 'd: Geçiş Metalleri', 'f: Lantanit / Aktinit')
    ], '9-kimya-8 özel gruplar')

def g1():
    return karsilastir2('ELEKTRON DİZİLİMİNDEN YER BULMA (15P ÖRNEĞİ)',
        '1. Adım: Temel Hâl Dizilimi', '15P: 1s^2 2s^2 2p^6 3s^2 3p^3', 'En büyük baş kuantum sayısı n = 3 -> 3. Periyot',
        '2. Adım: Grup ve Blok Tespiti', 'Değerlik e^- = 2 + 3 = 5 -> 5A (IUPAC 15)', 'Son orbital p olduğu için -> p bloğu',
        '9-kimya-8 yer bulma')

def g2():
    return kart4('ELEMENTLERİN SINIFLANDIRILMASI VE ÖZELLİKLERİ', [
        ('Metaller', 'Parlak, işlenir, iletir', 'Bileşikte yalnız (+)'),
        ('Ametaller', 'Mat, kırılgan, yalıtkan', 'Bileşikte (+) veya (-)'),
        ('Yarı Metaller', 'B, Si, Ge, As, Sb, Te', 'Fiziksel metal, kimyasal ametal'),
        ('Soy Gazlar (8A)', 'He, Ne, Ar, Kr, Xe', 'Monoatomik, kararlı gaz')
    ], '9-kimya-8 element sınıfları')

def g3():
    return uclu_sema('MODERN PERİYODİK SİSTEMİN TEMEL YAPISI', [
        ('Sıralama Ölçütü', 'Artan atom numarası', '(Proton sayısı / Moseley)'),
        ('7 Yatay Periyot', '1. periyot: 2 element', '2. ve 3. periyot: 8 element'),
        ('18 Düşey Sütun', '8 tane A, 8 tane B', '8B grubu 3 sütundur')
    ], '9-kimya-8 periyodik yapı')

def g5():
    return akis4('PERİYODİK TABLODA YER BULMA ADIMLARI', [
        ('1. Elektron Sayısı', 'Nötr atomda', 'p^+ = e^- eşitliği'),
        ('2. Dizilimi Yaz', '1s^2 2s^2 2p^6...', 'Aufbau sırasıyla'),
        ('3. Periyot (n)', 'En büyük baş', 'kuantum sayısı'),
        ('4. Grup & Blok', 'Son orbital -> Blok', 'Değerlik e^- -> Grup')
    ], '9-kimya-8 yer bulma akışı')

def g6():
    return karsilastir2('ÖZEL İSTİSNA ELEMENTLER: 1H VE 2He',
        'Hidrojen (1H : 1s^1)', '1. Periyot, 1A grubu, s bloğu', '1A grubunda olmasına rağmen AMETALDİR!',
        'Helyum (2He : 1s^2)', '1. Periyot, 8A (18. grup), s bloğu', 'Değerlik e^-=2 olsa da SOY GAZDIR (2A değil!)',
        '9-kimya-8 H ve He istisnası', KIR, KIR_A, MAVI, MAVI_A)

def g7():
    return karsilastir2('B GRUBU (d BLOĞU) YER BULMA KURALI (26Fe)',
        'Dizilim ve Periyot', '26Fe : [Ar] 4s^2 3d^6', 'En büyük n = 4 -> 4. Periyot, d bloğu',
        'Grup Numarası (ns + (n-1)d)', 'Değerlik e^- = 2 + 6 = 8', 'Toplam 8, 9, 10 ise -> 8B (IUPAC 8. grup)',
        '9-kimya-8 B grubu bulma', MOR, MOR_A, YES, YES_A)

def g10():
    return karsilastir2('1A GRUBUNDA HİDROJEN VE ALKALİ METALLER',
        '1H (Hidrojen - Ametal)', 'Oda koşullarında H2 moleküler gazdır', 'Elektron ortaklaşmasıyla kovalent bağ yapar',
        '3Li, 11Na, 19K (Alkali Metaller)', 'Oda koşullarında yumuşak ve parlak katıdır', '1 elektron vererek daima +1 iyonu oluşturur',
        '9-kimya-8 1A karşılaştırma', CAM, CAM_A, TUR, TUR_A)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[10]['gorsel'] = g10()
