"""9. sınıf Din Kültürü 4. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    turler = [('Sadık Haber', 'Evrensel bağlayıcı vahiy', MAVI, MAVI_A), ('Selim Akıl', 'Mantıki doğru tahlil', YES, YES_A), ('Rüya &amp; İlham', 'Öznel bireysel sezgi', TUR, TUR_A), ('Taklit', 'Delilsiz benimseme', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'İslam bilgi kaynakları ve bağlayıcılık', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'TEBEYYÜN İLKESİ · BİLGİYİ TEYİT ETME (HUCURÂT, 6)', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, '"Bir fasık size bir haber getirirse onu iyice araştırın..."', 11, LAC) + yazi(180, 70, 'Zanna ve doğrulanmamış haberlere dayanarak hüküm vermek yasaklanmıştır.', 9, SOLUK, ince=True)
    return svg(360, 100, ic, 'Hucurât 6 ayet levhası ve tebeyyün bilinci', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'RÜYA VE İLHAMIN DİNDEKİ KONUMU', 11, TUR)
    ic += yazi(180, 48, 'Bireysel ve öznel tecrübelerdir; denetlenemez ve aktarılamaz.', 10.5, LAC)
    ic += yazi(180, 68, 'İslam fıkhında başkaları için bağlayıcı bir dinî delil teşkil etmez.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Rüya ve ilhamın kişiselliği kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Vahiy', 'Gayb rehberi', MAVI, MAVI_A), ('Akıl', 'Anlama aracı', TUR, TUR_A), ('Tebeyyün', 'Teyit ve tahkik', YES, YES_A), ('Duyular', 'Somut kanıt', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Doğru bilgi ve tahkik ilkeleri', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Şüphe', 'Haberi sorgula', YES, YES_A), ('2. Kaynak', 'İlk yazarı araştır', MAVI, MAVI_A), ('3. Teyit', 'Bağımsız denetim', TUR, TUR_A), ('4. Kanaat', 'Kesinleşince paylaş', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10.5, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Dijital ortamda tebeyyün adımları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'DOĞRU BİLGİYİ ENGELLEYEN UNSURLAR', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Zan · Hevâ (Nefsi Arzular) · Körü Körüne Taklit · Taassup', 10.5, LAC) + yazi(180, 70, 'Bencil arzular ve peşin hükümler hakikatin görülmesini engeller.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Bilgi engelleri ve hevâ uyarısı panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    engeller = [('Zan', 'Delilsiz kuşku', MAVI, MAVI_A), ('Hevâ', 'Bencil nefis arzusu', TUR, TUR_A), ('Ön Yargı', 'Peşin dayanaksız hüküm', YES, YES_A), ('Taklit', 'Sorgulamadan izleme', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(engeller):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Bilgi engelleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: T - A - H - K - İ - K', 11.5, YES)
    harfler = [('1', 'T'), ('2', 'A'), ('3', 'H'), ('4', 'K'), ('5', 'İ'), ('6', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES) + yazi(x + 21, 46, no, 9, SOLUK, ince=True) + yazi(x + 21, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Tahkik şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
