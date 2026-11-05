"""9. sınıf Biyoloji 3. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    turler = [('Hipotez', 'Sınanabilir önerme', MAVI, MAVI_A), ('Teori', 'Geniş kapsamlı neden', YES, YES_A), ('Kanun', 'Nasıl işlediği ilkesi', TUR, TUR_A), ('Gözlem', 'Duyu/araçla veri tespiti', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 11, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Bilimsel bilgi türleri kartları', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'BİLİMSEL BİLGİNİN DEĞİŞEBİLİR VE DİNAMİK YAPISI', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, 'Yeni Kanıtlar ve Gözlemler Mevcut Bilgiyi Geliştirir', 11.5, LAC) + yazi(180, 70, 'Bilimsel teoriler mutlak dogmalar değil, sürekli sınanan açıklamalardır.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Bilimin dinamik doğası şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, YES_A, YES, 8)
    ic += yazi(180, 28, 'TEORİ VE KANUN İLİŞKİSİ · FARKLI BİLGİ TÜRLERİ', 11, YES)
    ic += yazi(180, 48, 'Teori "Neden?", Kanun "Nasıl?" sorusuna yanıt verir.', 11.5, LAC)
    ic += yazi(180, 68, 'Teoriler kanıtlandıkça asla kanuna dönüşmez, her ikisi de ayrı türdür.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Teori ve kanun farkı panosu', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Kanıt Odaklı', 'Gözlem ve deney', MAVI, MAVI_A), ('Sorgulayıcı', 'Kuşkucu yaklaşım', TUR, TUR_A), ('Yaratıcılık', 'Hayal gücü ve akıl', YES, YES_A), ('Evrensel Etik', 'Dürüstlük ve tarafsızlık', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Bilimin temel nitelikleri panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Problem', 'Merak ve gözlem', YES, YES_A), ('2. Veri', 'Ölçüm ve kayıt', MAVI, MAVI_A), ('3. Hipotez', 'Sınanabilir önerme', TUR, TUR_A), ('4. Deney', 'Kontrollü sınama', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10.5, c) + yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Bilimsel yöntem basamakları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'KONTROLLÜ DENEY DÜZENEĞİ · ENZİM HIZI', 11, CAM)
    ic += kutu(20, 36, 150, 44, '#eaf7fa', CAM) + yazi(95, 52, 'Bağımsız Değişken:', 9.5, CAM) + yazi(95, 70, 'Sıcaklık Değerleri', 11, LAC)
    ic += kutu(190, 36, 150, 44, TUR_A, TUR) + yazi(265, 52, 'Bağımlı Değişken:', 9.5, TUR) + yazi(265, 70, 'Tepkime Hızı', 11, TUR)
    return svg(360, 96, ic, 'Kontrollü deney değişkenleri panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    degiskenler = [('Bağımsız', 'Müdahale edilen etken', MAVI, MAVI_A), ('Bağımlı', 'Ölçülen netice', TUR, TUR_A), ('Sabit', 'Değişmeyen koşullar', YES, YES_A), ('Deney Grubu', 'Uygulama yapılan örnek', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(degiskenler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Deney değişken türleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: T - E - O - R - İ', 11.5, YES)
    harfler = [('1', 'T'), ('2', 'E'), ('3', 'O'), ('4', 'R'), ('5', 'İ')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Teori şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
