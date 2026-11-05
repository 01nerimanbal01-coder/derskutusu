"""9. sınıf Fizik 4. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kurumlar = [('TÜBİTAK', 'Bilim destek çatı kurumu', MAVI, MAVI_A), ('TENMAK', 'Nükleer ve enerji kurumu', YES, YES_A), ('CERN', 'Parçacık fiziği merkezi', TUR, TUR_A), ('NASA', 'Uzay ve havacılık dairesi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurumlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Bilim ve araştırma kurumları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'CERN · BÜYÜK HADRON ÇARPIŞTIRICISI (LHC)', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 48, 'Yerin 100 Metre Altında 27 Kilometrelik Dairesel Tünel', 11, LAC) + yazi(180, 70, 'Atom altı parçacıklar ışık hızına yakın çarpıştırılarak evren incelenir.', 9, SOLUK, ince=True)
    return svg(360, 100, ic, 'CERN parçacık hızlandırıcı tünel şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'TÜRKİYE UZAY AJANSI (TUA) VE MİLLÎ PROGRAM', 11, TUR)
    ic += yazi(180, 48, 'Yerli uydu teknolojileri, fırlatma sistemleri ve uzay araştırmaları', 10, LAC)
    ic += yazi(180, 68, 'Türkiye\'nin uzay ekosistemini ve insan kaynağını geliştirir.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Türkiye Uzay Ajansı kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    alanlar = [('Nanoteknoloji', 'Akıllı mikroçipler', MAVI, MAVI_A), ('Medikal Fizik', 'Radyoterapi &amp; MR', TUR, TUR_A), ('Savunma', 'Radar ve optik', YES, YES_A), ('Nükleer', 'Enerji ve santraller', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(alanlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Fizik bilimi kariyer ve inovasyon alanları', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Kuram', 'Fiziksel model', YES, YES_A), ('2. Prototip', 'Laboratuvarda üretim', MAVI, MAVI_A), ('3. Test', 'Sensörle ölçüm', TUR, TUR_A), ('4. Ürün', 'Sanayiye aktarım', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10.5, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Teknolojik ürün geliştirme basamakları', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'MEDİKAL FİZİK · RADYASYON ONKOLOJİSİ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Doğrusal Hızlandırıcı (LINAC) ve Radyoterapi Sistemleri', 11, LAC) + yazi(180, 70, 'Fizikçiler kanserli dokuya hedeflenen ışın dozunu hassasiyetle hesaplar.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Medikal fizik radyoterapi panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    meslek = [('Optik Müh.', 'Lazer ve fiber sistemler', MAVI, MAVI_A), ('Nükleer Fizikçi', 'Santral işletimi ve güvenlik', TUR, TUR_A), ('Biyofizikçi', 'Hücre zarı elektrik potansiyeli', YES, YES_A), ('Jeofizik Müh.', 'Deprem dalgaları analizi', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(meslek):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 9.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Fizik meslek dalları uzmanlık kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: C - E - R - N', 11.5, YES)
    harfler = [('1', 'C'), ('2', 'E'), ('3', 'R'), ('4', 'N')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES) + yazi(x + 25, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'CERN şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
