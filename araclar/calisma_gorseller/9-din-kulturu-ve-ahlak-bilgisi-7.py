"""9. sınıf Din Kültürü ve Ahlak Bilgisi 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def dörtlu_kart(etiket, kartlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis_karti(etiket, adimlar):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def uclu_pano(etiket, ust_baslik, kutular, ana_renk=MAVI, ana_acik=MAVI_A):
    ic = kutu(4, 4, 352, 107, ana_acik, ana_renk) + yazi(180, 23, ust_baslik, 10, ana_renk)
    for i, (b, alt, c, d) in enumerate(kutular):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 66, d, c) + yazi(x + 52, 55, b, 9.5, c) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def bilgi_panosu(etiket, baslik, satir1, satir2, c=CAM, d=CAM_A, ic_d='#eaf7fa'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 25, baslik, 10, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, satir1, 9.6, LAC) + yazi(180, 82, satir2, 8.6, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return dörtlu_kart('Rûm suresi kâinat delilleri', [
        ('Rûm 20: Toprak', 'Beşerin yaratılışı', MAVI, MAVI_A),
        ('Rûm 21: Aile', 'Sekînet ve rahmet', YES, YES_A),
        ('Rûm 22: Çeşitlilik', 'Dil ve renk farkı', TUR, TUR_A),
        ('Rûm 24: Yağmur', 'Toprağın dirilişi', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Aile yuvasının üç manevi direği', 'RÛM SURESİ 21. AYET: AİLEDE HUZUR İLKELERİ', [
        ('Sekînet', 'Gönül huzuru ve güven', MAVI, '#f4f8fe'),
        ('Meveddet', 'Karşılıklı içten sevgi', YES, YES_A),
        ('Rahmet', 'Şefkat ve merhamet', TUR, TUR_A)
    ], YES, YES_A)
def g2():
    return bilgi_panosu('Dillerin ve renklerin farklılığı', 'RÛM SURESİ 22. AYET: EVRENSEL ÇEŞİTLİLİK VE BİLENLER',
        '“Göklerin ve yerin yaratılması ile dillerinizin ve renklerinizin farklı olması O’nun ayetlerindendir.”',
        'Farklılıklar ayrımcılık sebebi değil, Yüce Allah’ın yaratma sanatındaki eşsiz zenginliktir.', CAM, CAM_A)
def g3():
    return dörtlu_kart('Ayet sonlarındaki tefekkür çağrısı', [
        ('Yetefekkerûn', 'Düşünen toplum (21)', MAVI, MAVI_A),
        ('Li’l-âlimîn', 'Bilenler/âlimler (22)', YES, YES_A),
        ('Yesmeûn', 'İşiten toplum (23)', TUR, TUR_A),
        ('Ya’kılûn', 'Aklını kullanan (24)', MOR, MOR_A)
    ])
def g5():
    return akis_karti('Rûm 20-27. ayetlerin konu akışı', [
        ('1. Rûm 20-21', 'Yaratılış ve aile', MAVI, MAVI_A),
        ('2. Rûm 22-23', 'Dil/renk ve rızık', YES, YES_A),
        ('3. Rûm 24', 'Yağmur ve diriliş', TUR, TUR_A),
        ('4. Rûm 25-27', 'Düzen ve el-Hakîm', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('İlk yaratma ve yeniden diriltme', 'RÛM SURESİ 27. AYET: AHİRET DELİLİ VE ESMÂ-İ HÜSNÂ', [
        ('İlk Yaratma', 'Yoktan başlatan O’dur', MAVI, '#f4f8fe'),
        ('Yeniden Diriltme', 'O’nun için daha kolay', YES, YES_A),
        ('El-Azîz ve El-Hakîm', 'Mutlak güç ve hikmet', TUR, TUR_A)
    ], MAVI, MAVI_A)
def g7():
    return bilgi_panosu('Temel Kur’an kavramları', 'ÂYET (DELİL) · SEKÎNET (HUZUR) · TEFEKKÜR (DERİN DÜŞÜNCE)',
        'Kâinattaki her düzen ve nimet Allah’ın varlığına işaret eden kevnî bir ayettir',
        'İnsan aklını kullanarak (tefekkür) yaratılıştan ahiret bilincine ulaşır.', TUR, TUR_A, '#fff6ea')
def g8():
    return dörtlu_kart('Rûm suresi anahtar terimleri', [
        ('Meveddet', 'İçten sevgi bağı', YES, YES_A),
        ('Ba’s / Haşir', 'Yeniden diriliş', MAVI, MAVI_A),
        ('El-Azîz', 'Mutlak güç sahibi', TUR, TUR_A),
        ('El-Hakîm', 'Hikmet sahibi', MOR, MOR_A)
    ])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
