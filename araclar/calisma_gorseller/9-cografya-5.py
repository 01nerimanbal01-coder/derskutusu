"""9. sınıf Coğrafya 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def g0():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    sekiller = [('Vadi', 'Sivri uç yükseğe bakar', MAVI, MAVI_A), ('Sırt', 'Sivri uç alçağa bakar', YES, YES_A), ('Boyun', 'İki tepe arası geçit', TUR, TUR_A), ('Falez', 'Kıyıda çakışan eğriler', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(sekiller):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Topografya yer şekilleri özet kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'HARİTADA EĞİM HESAPLAMA BAĞINTISI', 10.5, MAVI)
    ic += kutu(20, 36, 320, 64, '#f4f8fe', MAVI) + yazi(180, 58, 'Eğim (%) = (Yükselti Farkı h / Yatay Uzaklık L) × 100', 10.5, LAC) + yazi(180, 82, 'K (200 m) ile L (1000 m) arası: h = 800 m, L = 16 km = 16.000 m', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Eğim hesaplama formül ve veri panosu', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'FİZİKİ HARİTALARDA RENKLENDİRME YÖNTEMİ', 10.5, TUR)
    ic += yazi(180, 58, '0-500 m: Yeşil  |  500-1000 m: Sarı  |  1000-1500 m: Turuncu  |  >1500 m: Kahve', 9.5, LAC)
    ic += yazi(180, 82, 'Renkler bitki örtüsünü değil, deniz seviyesinden yükselti basamaklarını gösterir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Fiziki haritalarda yükselti renk basamakları', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Kıyı Çizgisi', 'Her zaman 0 metredir', MAVI, MAVI_A), ('Eküidistans', 'Sabit yükselti farkı', TUR, TUR_A), ('Sık Eğriler', 'Eğim ve diklik fazla', YES, YES_A), ('Komşu Yamaç', 'Akarsu iki yanı eşit', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'İzohips haritalarının temel kuralları', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Başlık', 'Konuyu ve alanı anla', YES, YES_A), ('2. Lejant', 'Sembol ve rengi çöz', MAVI, MAVI_A), ('3. Ölçek/Yön', 'Konum ve mesafe bul', TUR, TUR_A), ('4. Çıkarım', 'Mekânsal ilişki kur', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 10, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Harita okuma ve mekânsal analiz basamakları', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'GERÇEK UZUNLUK (GU) HESAPLAMA UYGULAMASI', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'GU = Harita Uzunluğu (5 cm) × Ölçek Paydası (300.000)', 10.5, LAC) + yazi(180, 84, 'Santimetreyi kilometreye çevirmek için 5 sıfır silinir (1 km = 100.000 cm).', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Gerçek uzunluk ölçek hesaplama panosu', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'TOPOGRAFYA UYGULAMALARI VE YER ŞEKİLLERİ', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Eküidistans (Eş Aralık)  ·  Delta Ovası (Birikim)  ·  Profil (Yan Kesit)', 10, LAC) + yazi(180, 82, 'İki nokta arasına çekilen doğrultunun yandan görünüşüne profil denir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Eküidistans, delta ve profil kavram şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    turler = [('İzobat', 'Eş derinlik eğrisi', MAVI, MAVI_A), ('Kapalı Çukur', 'İçe ok (→) işareti', TUR, TUR_A), ('Noktalama', 'Birim nokta dağılışı', YES, YES_A), ('İzoplet', 'Eş değer eğrileri', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Harita terimleri ve tematik yöntemler kartı', 34)

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
