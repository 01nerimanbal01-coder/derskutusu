"""9. sınıf Tarih 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('5T tarih araştırma yöntemi', [
        ('1. Tarama', 'Kaynakları toplama', MAVI, MAVI_A),
        ('2. Tasnif', 'Sınıflandırma yapma', YES, YES_A),
        ('3. Tahlil', 'Yeterlilik kontrolü', TUR, TUR_A),
        ('4-5. Tenkit/Terkip', 'Eleştiri ve sentez', MOR, MOR_A)
    ])
def g1():
    return uclu_pano('Tenkit (Eleştiri) aşamasının iki boyutu', '4. BASAMAK TENKİT: DIŞ TENKİT VE İÇ TENKİT AYRIMI', [
        ('Dış Tenkit', 'Kâğıt, mürekkep, orijinallik', MAVI, '#f4f8fe'),
        ('İç Tenkit', 'Yazar tarafsız ve doğru mu?', YES, YES_A),
        ('Çapraz Kontrol', 'Farklı kaynaklarla kıyas', TUR, TUR_A)
    ], MAVI, MAVI_A)
def g2():
    return bilgi_panosu('Dış tenkit ve iç tenkit soru anahtarı', 'SORU ÇÖZÜM ANAHTARI: DIŞ TENKİT Mİ, İÇ TENKİT Mİ?',
        'Dış Tenkit: “Bu belge sahte mi, hangi yüzyıla ait, mührü ve mürekkebi orijinal mi?”',
        'İç Tenkit: “Yazar olayı abartmış mı, ideolojisi ne, Hitit ve Mısır kaynakları uyuşuyor mu?”', CAM, CAM_A)
def g3():
    return dörtlu_kart('Tarihçilikte temel ilkeler', [
        ('Nesnellik', 'Kanıta dayalı tarafsızlık', MAVI, MAVI_A),
        ('Anakronizm Yasağı', 'Dönemin şartlarıyla bak', KIR, KIR_A),
        ('Dinamik Bilgi', 'Yeni kanıtla güncellenir', YES, YES_A),
        ('Dijital Tenkit', 'Sahte veriyi ayıklama', TUR, TUR_A)
    ])
def g5():
    return akis_karti('5T yöntemi uygulama sırası', [
        ('1. Tarama', 'Arşiv ve buluntu ara', MAVI, MAVI_A),
        ('2-3. Tasnif/Tahlil', 'Sınıfla ve çözümle', YES, YES_A),
        ('4. Tenkit', 'Dış ve iç eleştiri yap', TUR, TUR_A),
        ('5. Terkip', 'Sentezle ve eseri yaz', MOR, MOR_A)
    ])
def g6():
    return uclu_pano('Tarihsel bilginin dinamik yapısı', 'YENİ BULUNTULAR VE TARİHSEL BİLGİNİN DEĞİŞEBİLİRLİĞİ', [
        ('Göbeklitepe Kazısı', '12.000 yıllık tapınak', TUR, TUR_A),
        ('Eski Kabul Değişti', 'Yerleşik hayat önceliği', MAVI, '#f4f8fe'),
        ('Dinamik Bilim', 'Tarih dogmatik değildir', YES, YES_A)
    ], YES, YES_A)
def g7():
    return bilgi_panosu('Dijital tarihçilik ve büyük veri', '21. YÜZYILDA DİJİTAL TARİHÇİLİK VE KAYNAK DOĞRULAMA',
        'Sayısallaştırma, OCR, CBS haritalama ve sanal müzeler araştırmaları hızlandırmıştır',
        'Dijital ortamdaki dezenformasyona karşı resmi arşiv (.gov, .edu) doğrulaması zorunludur.', TUR, TUR_A, '#fff6ea')
def g8():
    return dörtlu_kart('Metodoloji ve dijital araçlar', [
        ('Dış Tenkit', 'Fiziksel orijinallik', MAVI, MAVI_A),
        ('İç Tenkit', 'İçerik ve tarafsızlık', YES, YES_A),
        ('Dijital Arşiv', 'Küresel hızlı erişim', CAM, CAM_A),
        ('CBS ve Büyük Veri', 'Harita ve veri analizi', MOR, MOR_A)
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
