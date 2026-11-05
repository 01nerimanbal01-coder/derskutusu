"""9. sınıf Coğrafya 4. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    proj = [('Silindirik', 'Ekvator ve çevresi', MAVI, MAVI_A), ('Konik', 'Orta kuşak ülkeleri', YES, YES_A), ('Düzlem', 'Kutuplar ve dar alanlar', TUR, TUR_A), ('Kesikli', 'Kıta alanlarını koruma', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(proj):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Projeksiyon türleri ve uygun alanlar kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'TÜRKİYE İÇİN EN UYGUN PROJEKSİYON: KONİK', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 48, 'Türkiye 36° - 42° Kuzey Paralellerindedir (Orta Kuşak)', 11, LAC) + yazi(180, 70, 'Konik projeksiyon orta enlemlerde şekil ve alan bozulmasını en aza indirir.', 9, SOLUK, ince=True)
    return svg(360, 100, ic, 'Konik projeksiyon ve Türkiye modeli', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'HARİTA ANAHTARI: LEJANT', 11, TUR)
    ic += yazi(180, 48, 'Haritadaki işaret, renk ve çizgilerin ne anlama geldiğini açıklar.', 10.5, LAC)
    ic += yazi(180, 68, 'Kullanıcının haritayı doğru okumasını ve yorumlamasını sağlar.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Harita lejantı kavram kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Ölçek', 'Küçültme oranı', MAVI, MAVI_A), ('Lejant', 'Sembol anahtarı', TUR, TUR_A), ('Yön Oku', 'Kuzey doğrultusu', YES, YES_A), ('Koordinat', 'Enlem ve boylam', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Haritanın temel unsurları panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Amaç', 'Başlık ve konu', YES, YES_A), ('2. Projeksiyon', 'Enleme uygun seçim', MAVI, MAVI_A), ('3. Ölçek', 'Küçültme paydası', TUR, TUR_A), ('4. Lejant', 'Sembol ve işaret', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10.5, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Harita hazırlama basamakları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 22, 'ÖLÇEK VE AYRINTI İLİŞKİSİ', 11, CAM)
    ic += kutu(20, 32, 150, 48, '#eaf7fa', CAM) + yazi(95, 48, 'Büyük Ölçek (1/25.000)', 10, LAC) + yazi(95, 68, 'Dar alan · Ayrıntı fazla', 8.5, SOLUK, ince=True)
    ic += kutu(190, 32, 150, 48, TUR_A, TUR) + yazi(265, 48, 'Küçük Ölçek (1/2.000.000)', 10, TUR) + yazi(265, 68, 'Geniş alan · Ayrıntı az', 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Büyük ve küçük ölçek karşılaştırma panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    unsurlar = [('Başlık', 'Konu ve kapsam', MAVI, MAVI_A), ('Ölçek', 'Mesafe oranı', TUR, TUR_A), ('Yön Oku', 'Kuzey yönü', YES, YES_A), ('Koordinat', 'Mutlak konum', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(unsurlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Harita unsurları işlev kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: L - E - J - A - N - T', 11.5, YES)
    harfler = [('1', 'L'), ('2', 'E'), ('3', 'J'), ('4', 'A'), ('5', 'N'), ('6', 'T')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES) + yazi(x + 21, 46, no, 9, SOLUK, ince=True) + yazi(x + 21, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Lejant şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
