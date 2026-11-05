"""7. sınıf Türkçe 13. hafta görselleri (SVG; K024 insan figürsüz; K178 beyaz bantsız)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
STIL = 'width:100%;max-height:22mm;display:block;margin:1mm auto;'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="{STIL}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    t = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{t}</text>'


def cizgi(x1, y1, x2, y2, renk=GRI, kalin=0.65, kesik=''):
    d = f' stroke-dasharray="{kesik}"' if kesik else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalin}"{d}/>'


def kart4(baslik, kartlar, etiket, ana=MAVI, arka=GRI_A):
    ic = kutu(4, 4, 352, 107, arka, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(kartlar):
        c, a = palet[i % 4]
        x = 9 + i * 86
        ic += kutu(x, 26, 82, 80, a, c, 5)
        ic += yazi(x + 41, 43, b, 8.2, c)
        ic += cizgi(x + 7, 50, x + 75, 50, c, 0.55)
        ic += yazi(x + 41, 69, s1, 7.6, LAC, ince=True)
        ic += yazi(x + 41, 89, s2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def ikili_pano(baslik, b1, d1a, d1b, b2, d2a, d2b, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1) + yazi(180, 19, baslik, 9.4, c1)
    ic += kutu(10, 26, 165, 80, a1, c1, 5)
    ic += yazi(92.5, 43, b1, 8.6, c1) + cizgi(20, 50, 165, 50, c1, 0.55)
    ic += yazi(92.5, 69, d1a, 7.8, LAC, ince=True) + yazi(92.5, 89, d1b, 7.4, SOLUK, ince=True)
    ic += kutu(185, 26, 165, 80, a2, c2, 5)
    ic += yazi(267.5, 43, b2, 8.6, c2) + cizgi(195, 50, 340, 50, c2, 0.55)
    ic += yazi(267.5, 69, d2a, 7.8, LAC, ince=True) + yazi(267.5, 89, d2b, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_pano(baslik, uclu, etiket, ana=YES, arka=YES_A):
    ic = kutu(4, 4, 352, 107, arka, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(uclu):
        c, a = palet[i % 3]
        x = 10 + i * 114
        ic += kutu(x, 26, 108, 80, a, c, 5)
        ic += yazi(x + 54, 43, b, 8.4, c) + cizgi(x + 8, 50, x + 100, 50, c, 0.55)
        ic += yazi(x + 54, 69, s1, 7.6, LAC, ince=True) + yazi(x + 54, 89, s2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana) + yazi(180, 19, baslik, 9.4, ana)
    palet = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, s1, s2) in enumerate(adimlar):
        c, a = palet[i % 4]
        x = 8 + i * 87
        ic += kutu(x, 26, 79, 80, a, c, 5)
        ic += yazi(x + 39.5, 43, b, 8.0, c)
        ic += yazi(x + 39.5, 68, s1, 7.4, LAC, ince=True)
        ic += yazi(x + 39.5, 88, s2, 7.0, SOLUK, ince=True)
        if i < 3:
            ox = x + 80.5
            ic += f'<polygon points="{ox:.1f},61 {ox+5:.1f},66 {ox:.1f},71" fill="{ana}"/>'
    return svg(ic, etiket)


def g1():
    return kart4('«ESKİCİ» HİKÂYE UNSURLARI HARİTASI (REFİK HALİT KARAY)', [
        ('Kişi Kadrosu', 'Küçük Hasan (5 yaş)', 'Türk eskici ve hala'),
        ('Mekân (Yer)', 'İstanbul’dan gemiyle', 'Filistin’deki kasaba'),
        ('Temel Çatışma', 'Arapça konuşulan ev', 'Dil yalnızlığı / suskunluk'),
        ('Ana Duygu', 'Ana dili sevgisi', 'Memleket özlemi')
    ], 'Eskici hikâyesinin unsurları')


def g2():
    return uclu_pano('FİİLİ BELİRTEN ZARFLAR VE BULUNUŞ SORULARI', [
        ('1. Cümle: heyecanla', 'Fiil: dinledi', 'Soru: Nasıl dinledi?'),
        ('2. Cümle: sabahleyin', 'Fiil: geldi', 'Soru: Ne zaman geldi?'),
        ('3. Cümle: pek', 'Fiil: duygulanmıştı', 'Soru: Ne kadar?')
    ], 'Üç zarf türünün cümle analizi')


def g4():
    return ikili_pano('YER-YÖN ZARFI KURALI: YALIN HÂL ŞARTI!',
        'Yer-Yön Zarfı (Ek Almamış)', 'içeri · dışarı · aşağı · yukarı · ileri · geri', 'Örnek: «Sessizce dışarı baktı.» (Zarf)',
        'Çekim Eki Alırsa İSİM Olur!', 'içeriye · dışarıda · aşağıya · ilerisinde', 'Örnek: «İçeriye girdik.» (Dolaylı tümleç / İsim)',
        'Yer-yön zarfı ile isim ayrımı', YES, YES_A, KIR, KIR_A)


def g5():
    return akis4('«ESKİCİ» HİKÂYESİNİN OLAY ÖRGÜSÜ BÖLÜMLERİ', [
        ('1. Serim', 'Yetim kalan Hasan', 'Filistin’e gönderilir'),
        ('2. Düğüm (Baş)', 'Yabancı dil ortamı', 'Derin suskunluk'),
        ('3. Düğüm (Doruk)', 'Türk eskici gelir', 'Türkçe tatlı sohbet'),
        ('4. Çözüm', 'Eskici evden ayrılır', 'Özlem gözyaşları')
    ], 'Eskici öyküsünün serim düğüm çözüm akışı')


def g6():
    return ikili_pano('SÖZ SANATI ÇÖZÜMLEME KARTI',
        'Benzetilen (Zayıf Unsur)', 'Küçük Hasan’ın derin suskunluğu', 'Benzetme Edatı / Yüklemi: «... benziyordu»',
        'Kendisine Benzetilen (Güçlü Unsur)', 'Kışın donup kalan sessiz bir akarsu', 'Ortak Yön: Hareketsizlik ve sessizlik',
        'Benzetme teşbih sanatı öğeleri', MAVI, MAVI_A, MOR, MOR_A)


def g8():
    return ikili_pano('AYNI SÖZCÜK: İSMİN ÖNÜNDE Mİ, FİİLİN ÖNÜNDE Mİ?',
        '1. Cümle: «Hızlı tren istasyona yanaştı.»', '«hızlı» + «tren» (İsim)', 'Nasıl tren? → İsmi niteler',
        '2. Cümle: «Tren raylarda hızlı ilerliyor.»', '«hızlı» + «ilerliyor» (Fiil)', 'Nasıl ilerliyor? → Eylemi belirtir',
        'Sıfat ve durum zarfı karşılaştırması', TUR, TUR_A, YES, YES_A)


def g9():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM)
    ic += yazi(180, 19, 'METİN PARÇASI ANALİZİ: DÜŞÜNCEYİ GELİŞTİRME YOLLARI', 9.2, CAM)
    ic += kutu(12, 27, 336, 76, GRI_A, CAM, 5)
    ic += yazi(180, 46, '«Ana dili, bireyin dünyayı anlamlandırdığı ilk ses yuvasıdır.» (Nedir? sorusu)', 8.0, LAC)
    ic += cizgi(24, 56, 336, 56, CAM, 0.55)
    ic += yazi(180, 74, 'Yahya Kemal de bu gerçeği «Türkçem, benim ses bayrağım!» sözüyle vurgular.', 8.0, MAVI)
    ic += yazi(180, 93, 'İpucu: Tanım cümlesi + Tanınmış bir şairin tırnak içi alıntı sözü', 7.4, SOLUK, ince=True)
    return svg(ic, 'Tanımlama ve tanık gösterme metin kartı')


def g11():
    return uclu_pano('ANA DİLİ VE KÜLTÜREL AİDİYET PANOSU', [
        ('Duygusal Bağ', 'Ana dili sesi', 'Güven ve sıcaklık verir'),
        ('İletişim Köprüsü', 'Ortak kelimeler', 'Yalnızlığı sona erdirir'),
        ('Manevi Vatan', 'Memleket hatırası', 'Dil ile yaşatılır')
    ], 'Ana dili ve manevi vatan iletisi', MOR, MOR_A)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[4]['gorsel'] = g4()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[9]['gorsel'] = g9()
    s[11]['gorsel'] = g11()
