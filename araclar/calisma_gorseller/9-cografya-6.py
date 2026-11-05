"""9. sınıf Coğrafya 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return dörtlu_kart('Harita anahtarı ve projeksiyon türleri', [
        ('Lejant', 'Sembol ve renk dili', TUR, TUR_A),
        ('Silindirik', 'Ekvator (0°-30°)', MAVI, MAVI_A),
        ('Konik', 'Orta Kuşak (Türkiye)', YES, YES_A),
        ('Düzlem (Ufki)', 'Kutuplar ve dar alan', MOR, MOR_A)
    ])

def g1():
    return uclu_pano('Projeksiyon bölgeleri ve bozulma', 'PROJEKSİYON YÖNTEMLERİ VE EN AZ BOZULMA KUŞAKLARI', [
        ('Silindirik (0°-30°)', 'Brezilya, Endonezya, Kenya', MAVI, '#f4f8fe'),
        ('Konik (30°-60°)', 'Türkiye, Fransa, Japonya', YES, YES_A),
        ('Düzlem (60°-90°)', 'Norveç, İzlanda, Kutuplar', MOR, MOR_A)
    ], MAVI, MAVI_A)

def g2():
    return bilgi_panosu('Kesir ölçek uzunluk hesaplama kartı', 'UZUNLUK FORMÜLÜ · 5 SIFIR KURALI',
        'Gerçek Uzunluk (GU) = Harita Uzunluğu (HU) × Ölçek Paydası',
        '1 : 600.000 ölçekte 5 sıfır silinir → 1 cm = 6 km  |  8 cm × 6 km = 48 km', CAM, CAM_A)

def g3():
    return dörtlu_kart('Haritanın temel elemanları ve kroki farkı', [
        ('Başlık & Ölçek', 'Amaç ve küçültme oranı', MAVI, MAVI_A),
        ('Lejant & Yön', 'Harita dili ve kuzey oku', YES, YES_A),
        ('Kroki Farkı', 'Krokide ölçek bulunmaz', TUR, TUR_A),
        ('Fiziki Harita', 'Yükselti ve eğim okunur', MOR, MOR_A)
    ])

def g5():
    return akis_karti('Ölçekten gerçek uzunluk bulma adımları', [
        ('1. Harita Ölçümü', 'Cetvelle cm ölç (HU)', MAVI, MAVI_A),
        ('2. 5 Sıfır Sil', 'Paydayı km’ye çevir', YES, YES_A),
        ('3. Çarpma İşlemi', 'HU × Ölçek (km)', TUR, TUR_A),
        ('4. Sonuç (GU)', 'Gerçek kuş uçuşu km', MOR, MOR_A)
    ])

def g6():
    return uclu_pano('Kullanım amaçlarına göre harita türleri', 'GENEL HARİTALAR VE TEMATİK (ÖZEL) HARİTALAR', [
        ('Fiziki Harita', 'Yükselti ve yer şekilleri', YES, YES_A),
        ('Siyasi Harita', 'Ülke ve il sınırları', MAVI, '#f4f8fe'),
        ('Tematik Harita', 'Deprem, toprak, iklim', TUR, TUR_A)
    ], TUR, TUR_A)

def g7():
    return bilgi_panosu('Kartografya ve alan türleri', 'KARTOGRAFYA · FİZİKİ HARİTA · GERÇEK VE İZDÜŞÜM ALAN',
        'Kartografya (Harita bilimi)  ·  Fiziki Harita (Renk = Yükselti)',
        'Gerçek alan ile izdüşüm alan farkı fazlaysa yer şekilleri dağlık ve engebelidir.', YES, YES_A, '#eaf8f0')

def g8():
    return dörtlu_kart('Türk-İslam haritacıları ve eserleri', [
        ('Pîrî Reis', 'Kitâb-ı Bahriye (1513)', MAVI, MAVI_A),
        ('Kaşgarlı Mahmud', 'Türk Dünyası Haritası', TUR, TUR_A),
        ('El-İdrîsî', 'Kitâbü Rucâr haritası', YES, YES_A),
        ('Kâtip Çelebi', 'Cihannüma adlı eser', MOR, MOR_A)
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
