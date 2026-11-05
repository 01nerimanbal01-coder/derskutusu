"""11. sınıf Tarih 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return cizelge4([('Marki de Pombal', 'Lizbon kriz ve anketi', MAVI, MAVI_A), ('Gaiola Pombalina', 'Esnek ahşap kafes yapı', YES, YES_A), ('III. Mustafa', '1766 İstanbul imarı', TUR, TUR_A), ('Mehmed Tahir Ağa', 'Yeni Fatih Camii inşası', MOR, MOR_A)], '1755 Lizbon ve 1766 İstanbul depremleri')
def g1():
    return ikili('1755 LİZBON DEPREMİ VE AYDINLANMA TARTIŞMALARI', 'Voltaire (Candide)', 'Leibniz’in kaderci iyimserliğini eleştirdi', 'Jean-Jacques Rousseau', 'Yıkımı 6-7 katlı çarpık kentleşmeye bağladı', MAVI, MAVI_A, TUR, TUR_A, 'Voltaire ve Rousseau deprem tartışması')
def g2():
    return kart('MARKİ DE POMBAL VE MODERN SİSMOLOJİNİN DOĞUŞU', 'Pombal tüm kilise bölgelerine 13 soruluk deprem gözlem anketi gönderdi.', 'Sarsıntı yönü, süresi ve su seviyesi kaydedilerek modern sismoloji başlatıldı.', YES, YES_A, 'Pombal deprem anketi ve sismoloji')
def g3():
    return cizelge4([('Portekiz Ekonomisi', 'Yıkımla güç kaybı yaşadı', KIR, KIR_A), ('Immanuel Kant', 'Fiziksel süreçlerle açıkladı', MAVI, MAVI_A), ('Fatih Camii', '1766’da ana kubbesi çöktü', TUR, TUR_A), ('Narh Sistemi', 'Malzeme fiyatı sabitlendi', YES, YES_A)], '1755 ve 1766 depremleri tarihsel olgular')
def g5():
    return akis4([('1. Çadır Kurulumu', 'Güvenli barınma alanı', YES, YES_A), ('2. Su ve Fırınlar', 'Kemer ve fırın onarımı', MAVI, MAVI_A), ('3. Usta ve Narh', 'Eyaletten malzeme + fiyat', TUR, TUR_A), ('4. Yeniden İmar', '1767-1771 Fatih Camii', MOR, MOR_A)], '1766 İstanbul Depremi Osmanlı kriz yönetimi')
def g6():
    return ikili('DEPREMLERİN FELSEFİ VE MİMARİ YANSIMALARI', 'Aydınlanma Felsefesi Etkisi', 'Voltaire, Rousseau ve Kant’ın eserleri', 'Depreme Dayanıklı Ahşap Mimari', 'Lizbon’da Pombal Kafesi · İstanbul’da Hımış', CAM, CAM_A, MOR, MOR_A, 'Felsefi ve mimari dönüşüm')
def g7():
    return kart('TSUNAMİ, HAZİNE-İ HÂSSA VE HIMIŞ YAPI TEKNİĞİ', '1755 Lizbon Depremi’ni Tejo Nehri tsunamisi ve 5 günlük yangın izlemiştir.', '1766 İstanbul imarında Hazine-i Hâssa fonları ve esnek hımış tekniği kullanılmıştır.', TUR, TUR_A, 'Tsunami, Hazine-i Hassa ve hımış')
def g8():
    return cizelge4([('Voltaire', 'Optimizm eleştirisi', MAVI, MAVI_A), ('Rousseau', 'Çarpık kentleşme uyarısı', YES, YES_A), ('Immanuel Kant', 'Bilimsel deprem risaleleri', TUR, TUR_A), ('Narh Kararı', 'Fiyat ve ücret denetimi', MOR, MOR_A)], '18. yüzyıl deprem düşünürleri ve önlemleri')

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
