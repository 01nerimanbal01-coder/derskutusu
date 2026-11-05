"""9. sınıf Din Kültürü 8. hafta görselleri (SVG; insan figürü yok K024; K178 beyaz bant yok; max-height:24mm)."""
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
    return kart4('İMANIN MAHİYETİ VE TEMEL KAVRAMLAR', [
        ('Kalp ile Tasdik', 'Gönülden onaylama', 'İmanın asli rüknü'),
        ('Dil ile İkrar', 'Sözle ifade etme', 'Tevhid ve Şehadet'),
        ('İcmalî & Tafsilî', 'Kapsamına göre', 'Özet ve ayrıntılı iman'),
        ('Taklidî & Tahkikî', 'Delile dayanmasına göre', 'Çevre ve araştırma')
    ], '9-din-8 iman kavramları')

def g1():
    return uclu_sema('TASDİK VE İKRAR DURUMUNA GÖRE İNSANLAR', [
        ('Mümin', 'Kalp ile tasdik EDER', 'Dil ile ikrar EDER'),
        ('Münafık (İkiyüzlü)', 'Kalp ile tasdik ETMEZ', 'Çıkar için ikrar EDER'),
        ('Kâfir (İnkârcı)', 'Kalp ile tasdik ETMEZ', 'Diliyle de inkâr EDER')
    ], '9-din-8 tasdik ikrar tablosu')

def g2():
    return karsilastir2('KAPSAMI BAKIMINDAN İMAN: İCMALÎ VE TAFSİLÎ',
        'İcmalî (Toptan / Özet) İman', 'Kelime-i Tevhid ve Şehadet ile', 'İnanç esaslarına bütüncül inanma',
        'Tafsilî (Ayrıntılı) İman', 'Âmentü’deki 6 iman esasına', 'Tek tek ve ayrıntılarıyla inanma',
        '9-din-8 icmali tafsili')

def g3():
    return kart4('ÂMENTÜ’DE YER ALAN ALTI İMAN ESASI (TAFSİLÎ İMAN)', [
        ('1-2. Esaslar', 'Allah’a İman', 'Meleklere İman'),
        ('3-4. Esaslar', 'Kitaplara İman', 'Peygamberlere İman'),
        ('5-6. Esaslar', 'Ahiret Gününe İman', 'Kader ve Kazaya İman'),
        ('Tam Bütünlük', 'Bölünmez bütündür', 'Salih amelle korunur')
    ], '9-din-8 altı iman esası')

def g5():
    return akis4('İCMALÎ İMANDAN TAHKİKÎ İMANA OLGUNLAŞMA SÜRECİ', [
        ('1. Kalbî Tasdik', 'Şüphesiz onay', 'Asli rükün'),
        ('2. Dil ile İkrar', 'Kelime-i Şehadet', 'İcmalî iman'),
        ('3. Sahih Bilgi', '6 esası öğrenme', 'Tafsilî iman'),
        ('4. Tefekkür & Amel', 'Delille kavrama', 'Tahkikî iman')
    ], '9-din-8 iman süreci')

def g6():
    return karsilastir2('DELİLE DAYANMASI BAKIMINDAN: TAKLİDÎ VE TAHKİKÎ İMAN',
        'Taklidî İman', 'Delil ve araştırmaya dayanmaz', 'Aile ve çevreden görülerek benimsenir',
        'Tahkikî İman', 'Bilgi, delil ve tefekküre dayanır', 'Şüpheler karşısında sarsılmaz, güçlüdür',
        '9-din-8 taklidi tahkiki', MOR, MOR_A, YES, YES_A)

def g7():
    return karsilastir2('KELİME-İ TEVHİD VE KELİME-İ ŞEHADET',
        'Kelime-i Tevhid', 'Lâ ilâhe illallah Muhammedün Resûlullah', 'Allah’tan başka ilah yoktur, Muhammed elçisidir',
        'Kelime-i Şehadet', 'Eşhedü en lâ ilâhe illallah ve eşhedü...', 'Şahitlik ederim ki... O’nun kulu ve elçisidir',
        '9-din-8 tevhid şehadet', CAM, CAM_A, TUR, TUR_A)

def g10():
    return uclu_sema('İMAN - SAHİH BİLGİ - SALİH AMEL BÜTÜNLÜĞÜ', [
        ('Bölünmezlik İlkesi', '6 esasın tamamı', 'Birini inkâr hepsini bozar'),
        ('Sahih Bilgi', 'Kur’an ve Sünnet', 'Hurafelerden arınma'),
        ('Salih Amel', 'İmanın meyvesi', 'Ahlak ve ibadetle koruma')
    ], '9-din-8 iman amel bütünlüğü', MAVI, MAVI_A)

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
