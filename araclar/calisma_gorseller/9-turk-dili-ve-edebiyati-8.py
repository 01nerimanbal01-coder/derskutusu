"""9. sınıf Türk Dili ve Edebiyatı 8. hafta görselleri (SVG; insan figürü yok K024; K178 beyaz bant yok; max-height:24mm)."""
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
    return kart4('İKNA EDİCİ KONUŞMANIN TEMEL DAYANAKLARI (TDE3.2 - 3.3)', [
        ('Retorik Üçlüsü', 'Ethos (Güven)', 'Pathos & Logos'),
        ('Geliştirme Yolları', 'Tanık gösterme', 'Sayısal veri & Örnek'),
        ('Anlatım İlkeleri', 'Açıklık, Duruluk', 'Yalınlık, Akıcılık'),
        ('Sunum & Beden Dili', 'Diksiyon, Vurgu', 'Jest, Mimik, Göz teması')
    ], '9-tde-8 ikna dayanakları')

def g1():
    return uclu_sema('RETORİK ÜÇLÜSÜ VE DİLİN İŞLEVLERİ', [
        ('Ethos (Güvenilirlik)', 'Uzmanlık ve dürüstlük', 'İletişim etiğine uyum'),
        ('Logos (Mantık & Kanıt)', 'Göndergesel işlev', 'Sayısal veri ve belgeler'),
        ('Pathos (Duygu & Çağrı)', 'Heyecana bağlı işlev', 'Alıcıyı harekete geçirme')
    ], '9-tde-8 retorik ve işlevler')

def g2():
    return kart4('DÜŞÜNCEYİ GELİŞTİRME YOLLARI (TDE3.3)', [
        ('Tanımlama', 'Kavramın sınırlarını', 'Bu nedir? ile çizme'),
        ('Karşılaştırma', 'İki durum arasındaki', 'benzerlik ve farklar'),
        ('Tanık Gösterme', 'Uzman kişinin sözünü', 'kanıt olarak alıntılama'),
        ('Sayısal Veriler', 'İstatistik, grafik', 've araştırma oranları')
    ], '9-tde-8 düşünceyi geliştirme')

def g3():
    return karsilastir2('İYİ BİR ANLATIMIN NİTELİKLERİ (ANLATIM İLKELERİ)',
        'Açıklık · Duruluk · Yalınlık', 'Açıklık: Tek ve net anlam', 'Duruluk: Gereksiz sözcük yok · Yalınlık: Sade dil',
        'Akıcılık · Özlük · Özgünlük', 'Akıcılık: Kolay seslendirme', 'Özlük: Az sözle çok anlam · Özgünlük: Kişisel üslup',
        '9-tde-8 anlatım ilkeleri')

def g5():
    return akis4('İKNA EDİCİ KONUŞMA TASARIMI VE SUNUM SÜRECİ', [
        ('1. Planlama', 'Amaç ve hedef kitle', 'Kaynak & görsel seçimi'),
        ('2. Giriş Bölümü', 'Çarpıcı soru/anekdot', 'Dikkat çekici açılış'),
        ('3. Gelişme Bölümü', 'Kanıtlar (Logos)', 'Bağdaşıklık ögeleri'),
        ('4. Sonuç & Öz Değ.', 'Etkili çağrı kapanışı', 'Geri bildirim analizi')
    ], '9-tde-8 konuşma süreci')

def g6():
    return karsilastir2('METİN VE KONUŞMADA BÜTÜNLÜK: BAĞDAŞIKLIK VE BAĞLAŞIKLIK',
        'Bağdaşıklık (Dil Bilgisel Bağlantı)', 'ancak, çünkü, buna karşılık, üstelik', 'dolayısıyla, özetle gibi geçiş ifadeleri',
        'Bağlaşıklık (Mantıksal Tutarlılık)', 'Düşüncelerin birbiriyle çelişmemesi', 'Konu bütünlüğünün sonuna dek korunması',
        '9-tde-8 bağdaşıklık bağlaşıklık', MOR, MOR_A, YES, YES_A)

def g7():
    return uclu_sema('SESLE ANLAM OLUŞTURMA VE BEDEN DİLİ YÖNETİMİ (TDE3.4)', [
        ('Diksiyon & Boğumlama', 'Standart Türkçe', 'Net hece telaffuzu'),
        ('Vurgu & Tonlama', 'Monotonluktan uzak', 'Anlama uygun ezgi/durak'),
        ('Beden Dili & Mekân', 'Göz teması, jest, mimik', 'Kürsü ve zaman yönetimi')
    ], '9-tde-8 diksiyon beden dili', CAM, CAM_A)

def g10():
    return karsilastir2('SÖYLEMDE İLETİ TÜRLERİ: AÇIK İLETİ VE ÖRTÜK İLETİ',
        'Açık İleti (Doğrudan Anlatım)', 'Anlam sözcüklerin temel anlamıyla nettir', 'Herkes tarafından aynı şekilde anlaşılır',
        'Örtük İleti (Dolaylı / Sezdirmeli Anlatım)', 'İmge, deyim ve söz sanatlarıyla sunulur', 'Dinleyicinin çıkarım yapmasını sağlar',
        '9-tde-8 açık örtük ileti', MAVI, MAVI_A, TUR, TUR_A)

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
