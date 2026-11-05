"""9. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('Mülakat türü ve iletişim kavramları', [
        ('Mülakat', 'Uzmanla soru-cevap', MAVI, MAVI_A),
        ('Diyorlar ki', 'Ruşen Eşref Ünaydın', TUR, TUR_A),
        ('Çok Modlu Metin', 'Söz + Ses + Görüntü', YES, YES_A),
        ('Göndergesel Dil', 'Nesnel bilgi aktarımı', MOR, MOR_A)
    ])

def g1():
    return uclu_pano('Mülakat ile röportaj farkı', 'MÜLAKAT (GÖRÜŞME) İLE RÖPORTAJ ARASINDAKİ FARKLAR', [
        ('Mülakat', 'Soru-cevap · Yorum katılmaz', MAVI, '#f4f8fe'),
        ('Röportaj', 'Gezi, gözlem ve izlenim', TUR, TUR_A),
        ('Ortak Yön', 'Öğretici gazete/dergi türü', YES, YES_A)
    ], MAVI, MAVI_A)

def g2():
    return bilgi_panosu('Çok modlu metin bileşenleri', 'ÇOK MODLU METİN OLARAK GÖRÜNTÜLÜ MÜLAKAT',
        'Sözlü Mod (Kelimeler) + İşitsel Mod (Vurgu, Tonlama) + Görsel/Davranışsal Mod (Jest, Mimik)',
        'Konuşmacının ses tonu ve beden dili, söylenen sözün örtük anlamını tamamlamaya yardım eder.', CAM, CAM_A)

def g3():
    return dörtlu_kart('Mülakatın bölümleri ve yayın etiği', [
        ('1. Giriş', 'Konu ve konuk tanıtımı', MAVI, MAVI_A),
        ('2. Gelişme', 'Planlı sorular ve yanıtlar', YES, YES_A),
        ('3. Sonuç', 'Özet ve teşekkür kapanışı', TUR, TUR_A),
        ('Yayın Etiği', 'Sözü değiştirmeden aktarma', MOR, MOR_A)
    ])

def g5():
    return akis_karti('Mülakat hazırlık ve uygulama süreci', [
        ('1. Ön Hazırlık', 'Araştırma, randevu, soru', MAVI, MAVI_A),
        ('2. Giriş Sunumu', 'Konuğu ve amacı tanıt', YES, YES_A),
        ('3. Görüşme Anı', 'Nazik soru ve etkin dinleme', TUR, TUR_A),
        ('4. Yayım Aşaması', 'Çarpıtmadan metne aktar', MOR, MOR_A)
    ])

def g6():
    return uclu_pano('Türk edebiyatında mülakat ustaları', 'TÜRK EDEBİYATINDA ÖNCÜ MÜLAKAT ESERLERİ', [
        ('Ruşen Eşref (1918)', 'Diyorlar ki · M. Kemal', TUR, TUR_A),
        ('Hikmet Feridun Es', 'Bugün de Diyorlar ki', MAVI, '#f4f8fe'),
        ('Mustafa Baydar', 'Edebiyatçılarımız Ne Diyorlar', YES, YES_A)
    ], TUR, TUR_A)

def g7():
    return bilgi_panosu('Sözlü ve sözsüz iletişim unsurları', 'SÖZLÜ İLETİŞİM (VURGU, TONLAMA) VE BEDEN DİLİ (JEST, MİMİK)',
        'Vurgu: Hece/kelime baskısı  ·  Tonlama: Sesin alçalıp yükselmesi  ·  Jest ve Mimik: El-kol ve yüz',
        'Röportajda yazar kişisel yorum katar; mülakatta ise konuğun sözleri olduğu gibi korunur.', YES, YES_A, '#eaf8f0')

def g8():
    return dörtlu_kart('Edebiyatımızda mülakat yazarları ve yapıtları', [
        ('Ruşen Eşref', 'Diyorlar ki (1918)', MAVI, MAVI_A),
        ('Hikmet Feridun', 'Bugün de Diyorlar ki', YES, YES_A),
        ('Mustafa Baydar', 'Edebiyatçılarımız Ne Diyorlar', TUR, TUR_A),
        ('Gavsi Ozansoy', '40 Yıl Sonra Diyorlar ki', MOR, MOR_A)
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
