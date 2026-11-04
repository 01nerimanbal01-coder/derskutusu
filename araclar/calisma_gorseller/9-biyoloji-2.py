"""9. sınıf Biyoloji 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    bilginler = [('Hooke', 'Hücre keşfi (1665)', MAVI, MAVI_A), ('Jenner', 'Çiçek aşısı', YES, YES_A), ('Fleming', 'Penisilin (1928)', TUR, TUR_A), ('Mullis', 'PCR tekniği', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(bilginler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 12, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Biyoloji dönüm noktaları bilginleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'BİLİMSEL HİPOTEZİN TEMEL NİTELİĞİ', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, 'Test Edilebilir ve Yanlışlanabilir Olmalıdır', 12.5, LAC) + yazi(180, 70, 'Kontrollü deney ve gözlemlerle sınanmaya açık olmalıdır.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Hipotez niteliği şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, YES_A, YES, 8)
    ic += yazi(180, 28, 'KONTROLLÜ DENEYDE DEĞİŞKENLER', 11, YES)
    ic += yazi(180, 48, 'Bağımsız Değişken: Araştırmacının bizzat değiştirdiği etken', 11, LAC)
    ic += yazi(180, 68, 'Bağımlı Değişken: Buna bağlı olarak değişen sonuç', 10.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Kontrollü deney değişkenler kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Dinamik Bilgi', 'Değişebilir', MAVI, MAVI_A), ('Yöntem Çeşitliliği', 'Tek yol yok', TUR, TUR_A), ('Teori &amp; Kanun', 'Dönüşmez', YES, YES_A), ('Kanıt Odaklı', 'Sorgulanır', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9.5, LAC, ince=True)
    return svg(360, 98, ic, 'Bilimin doğası temel ilkeleri', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Problem', 'Gözlem yap', YES, YES_A), ('2. Hipotez', 'Önerme kur', MAVI, MAVI_A), ('3. Deney', 'Değişkeni sına', TUR, TUR_A), ('4. Çıkarım', 'Sonucu açıkla', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 11, c) + yazi(x + 40, 55, alt, 9.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Bilimsel araştırma süreci akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'KAYNAK GÜVENİLİRLİĞİ ÖLÇÜTLERİ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Hakemli Dergi · Kurumsal Adres (.edu / .gov) · Güncellik', 11, LAC) + yazi(180, 70, 'Uzman değerlendirmesinden geçmiş bilimsel yayınlar esas alınır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Bilimsel kaynak güvenilirlik ölçütleri panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    buluslar = [('Mendel', 'Kalıtım ilkeleri', MAVI, MAVI_A), ('DNA Modeli', 'Çift sarmal yapı', TUR, TUR_A), ('Dolly', 'Memeli klonlama', YES, YES_A), ('CRISPR', 'Genom düzenleme', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(buluslar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 11, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Genetik dönüm noktaları kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: H - Ü - C - R - E', 11.5, YES)
    harfler = [('1', 'H'), ('2', 'Ü'), ('3', 'C'), ('4', 'R'), ('5', 'E')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Hücre şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
