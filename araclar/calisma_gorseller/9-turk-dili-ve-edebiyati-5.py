"""9. sınıf turk-dili-ve-edebiyati 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ogeler = [('İzlenimsel', 'Sanatsal ve öznel', MAVI, MAVI_A), ('Açıklayıcı', 'Bilgi verici, nesnel', YES, YES_A), ('Portre', 'Fiziksel ve ruhsal', TUR, TUR_A), ('Öz Değerlendirme', 'Yazarın iç denetimi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Betimleme türleri ve değerlendirme kavramları', 34)

def g1():
    b, s1, s2 = ('ŞİİRİ BETİMLEME PARAGRAFINA DÖNÜŞTÜRME İLKESİ', 'Dizeler olduğu gibi kopyalanmaz; özgün düzyazı cümleleriyle yeniden kurulur.', 'Mekân, zaman, varlık unsurları ve imgeler genel-özel sırasıyla betimlenir.')
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, b, 10, MAVI)
    ic += kutu(16, 36, 328, 64, '#f4f8fe', MAVI) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Şiirden betimleme paragrafına dönüşüm altın kuralı', 34)

def g2():
    b, s1, s2 = ('BETİMLEME (TASVİR) İLE ÖYKÜLEME (HİKÂYE ETME) AYRIMI', 'Betimleme: Durağanlık, sıfatlar ve mekân ayrıntısı (Fotoğraf Karesi)', 'Öyküleme: Zaman akışı, olay zinciri ve hareket fiilleri (Sinema Filmi)')
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, b, 10, TUR) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Betimleme ve öyküleme farkı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Beş Duyu', 'Görme, işitme, koklama', MAVI, MAVI_A), ('Sıfat Tamlaması', 'Sıfat-isim arası virgül yok', TUR, TUR_A), ('Üç Nokta (...)', 'Eksiltili izlenim cümlesi', YES, YES_A), ('Paydaş Görüşü', 'Akran/öğretmen katkısı', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Dil bilgisi, noktalama ve çoklu duyular', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Çözümleme', 'Tema ve imgeyi bul', YES, YES_A), ('2. Planlama', 'Bakış açısı ve sıra', MAVI, MAVI_A), ('3. Yazma', 'Duyusal tasvir kur', TUR, TUR_A), ('4. Değerlendirme', 'Öz/akran redaksiyon', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Şiirden paragrafa yazma ve değerlendirme akışı', 34)

def g6():
    b, s1, s2 = ('BETİMLEME PARAGRAFINDA ÇOKLU DUYU KULLANIMI', 'Görme (taş kaldırım) + Koklama (ıslak toprak kokusu) + İşitme (nal sesleri)', 'Birden fazla duyunun kaynaştırılması sahneyi okurun zihninde canlandırır.')
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, b, 10, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, s1, 9.8, LAC) + yazi(180, 84, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Çoklu duyuların betimlemede kaynaştırılması', 34)

def g7():
    b, s1, s2 = ('METİNSELLİK ÖLÇÜTLERİ VE YAZMA SÜRECİ TERİMLERİ', 'Bağdaşıklık (Anlam Uyumu)  ·  Redaksiyon (Düzeltme)  ·  Portre (Kişi Tasviri)', 'Değerlendirme süreci öğrencinin özgün yazar kimliğini geliştirmesini sağlar.')
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, b, 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, s1, 9.6, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, 'Bağdaşıklık, redaksiyon ve portre kavramları', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ogeler = [('İmge Aktarımı', 'Atmosferi koruma', MAVI, MAVI_A), ('Bağlaşıklık', 'Dil bilgisel bağlar', TUR, TUR_A), ('Söz Varlığı', 'Sıfat ve söz sanatı', YES, YES_A), ('Paydaş Katkısı', 'Yeni yazma hedefi', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ogeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.2, LAC, ince=True)
    return svg(360, 115, ic, 'Rubrik değerlendirme ölçütleri', 34)

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
