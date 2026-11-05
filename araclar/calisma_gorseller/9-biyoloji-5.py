"""9. sınıf Biyoloji 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kavramlar = [('Bağımsız', 'Değiştirilen neden', MAVI, MAVI_A), ('Bağımlı', 'Ölçülen sonuç', YES, YES_A), ('Kontrol', 'Sabit tutulanlar', TUR, TUR_A), ('Tahmin', 'Eğer... ise... dır', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kavramlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Kontrollü deney değişkenleri ve tahmin kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'KONTROLLÜ DENEY · SICAKLIĞIN ENZİM HIZINA ETKİSİ', 10.5, MAVI)
    ic += kutu(16, 36, 104, 64, '#f4f8fe', MAVI) + yazi(68, 56, '1. Tüp: 0 °C', 10, MAVI) + yazi(68, 78, 'Eşit enzim + substrat', 8.5, SOLUK, ince=True)
    ic += kutu(128, 36, 104, 64, YES_A, YES) + yazi(180, 56, '2. Tüp: 35 °C', 10, YES) + yazi(180, 78, 'Optimum tepkime hızı', 8.5, SOLUK, ince=True)
    ic += kutu(240, 36, 104, 64, KIR_A, KIR) + yazi(292, 56, '3. Tüp: 70 °C', 10, KIR) + yazi(292, 78, 'Enzim yapısı bozulur', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Enzim hızı sıcaklık kontrollü deney düzeneği', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'HİPOTEZ DOĞRULANMAZSA İZLENECEK BİLİMSEL YOL', 10.5, TUR)
    ic += yazi(180, 58, 'Deney verileri hipotezi desteklemezse veriler ASLA değiştirilmez!', 10.5, LAC)
    ic += yazi(180, 82, 'Mevcut hipotez gözden geçirilerek revize edilir veya yeni hipotez kurulur.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Hipotez yenileme ve veri dürüstlüğü kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Dürüstlük', 'Veriyi doğru kaydet', MAVI, MAVI_A), ('Tarafsızlık', 'Ön yargıdan uzak ol', TUR, TUR_A), ('Emeğe Saygı', 'Kaynak ve atıf göster', YES, YES_A), ('Canlı Hakkı', 'Etik kurul onayı al', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Bilim etiğinin dört temel ilkesi panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Gözlem', 'Problemi belirle', YES, YES_A), ('2. Hipotez', 'Tahmin cümlesi kur', MAVI, MAVI_A), ('3. Deney', 'Kontrollü sınama', TUR, TUR_A), ('4. Çıkarım', 'Etik analiz ve yayım', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 10.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Bilimsel araştırma süreci akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'BİLİM ETİĞİNİ DENETLEME VE DOĞRULAMA ARAÇLARI', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'Etik Kurul Onayı · Aydınlatılmış Onam Formu · İntihal Yazılımı', 10.5, LAC) + yazi(180, 84, 'Gönüllü bireylerin bilgilendirilmiş rızası Aydınlatılmış Onam ile belgelenir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Bilim etiği denetim araçları panosu', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'BİYOGÜVENLİK, BİYOETİK VE YAYIN DÜRÜSTLÜĞÜ', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Biyoetik (Ahlaki Boyut)  ·  Dilimleme (Yapay Bölme)  ·  Kontrol Grubu', 10, LAC) + yazi(180, 82, 'Genetik araştırmalarda kişisel veri gizliliği ve biyogüvenlik esastır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Biyoetik ve yayın etiği özet kartı', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Replacement', 'Hücre/simülasyon seç', MAVI, MAVI_A), ('Reduction', 'Hayvan sayısını azalt', TUR, TUR_A), ('Refinement', 'Acı ve stresi önle', YES, YES_A), ('İntihal Tarama', 'Kopya oranını sına', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Hayvan deneylerinde 3R etik ilkesi kartı', 34)

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
