"""12. sınıf Kimya 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.8, kc) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Standart elektrot potansiyeli ve istemlilik kavramları', [('SHE Referansı', 'E° = 0,00 V', MAVI, MAVI_A), ('E°_hücre > 0', 'İstemli tepkime', YES, YES_A), ('E°_hücre < 0', 'İstemsiz tepkime', KIR, KIR_A), ('Anot Seçimi', 'E°_yüks büyük olan', TUR, TUR_A)])

def g1():
    return uclu('Mg ve Ag standart elektrot potansiyelleri', 'STANDART İNDİRGENME POTANSİYELLERİ VE PİL GERİLİMİ', ('Mg2+ + 2e- -> Mg', 'E°_ind = -2,37 V (Anot)', MAVI, MAVI_A), ('Ag+ + e- -> Ag', 'E°_ind = +0,80 V (Katot)', TUR, TUR_A), ('Net Pil Gerilimi', 'E° = 2,37 + 0,80 = +3,17 V', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('Elektrot potansiyeli E° işlem kuralları', 'STANDART ELEKTROT POTANSİYELİ (E°) İŞLEM KURALLARI', '1) Yarı tepkime ters çevrilirse E° işaret değiştirir: E°_yüks = -E°_ind', '2) Yarı tepkime bir katsayıyla çarpılır veya bölünürse E° DEĞİŞMEZ!', MOR, MOR_A, '#f5f0ff')

def g3():
    return kart4('Aktif ve soy metallerin E° özellikleri', [('Aktif Metaller', 'E°_ind < 0 (Negatif)', MAVI, MAVI_A), ('Kuvvetli İndirgen', 'E°_yüks en büyük', TUR, TUR_A), ('Soy Metaller', 'Cu, Ag, Au: E°_ind > 0', MOR, MOR_A), ('Çubuk Aşınması', 'Aktif metal çözünür', YES, YES_A)])

def g5():
    return akis4('Metallerin indirgenme potansiyelinden aktiflik sıralaması', [('1. Ag (+0,80 V)', 'En pasif (Soy)', MOR, MOR_A), ('2. Cu (+0,34 V)', 'Yarı soy metal', TUR, TUR_A), ('3. Zn (-0,76 V)', 'Aktif metal', MAVI, MAVI_A), ('4. Mg (-2,37 V)', 'En aktif metal', YES, YES_A)])

def g6():
    return pano('Metalik aktiflik ve kapta çözelti saklama kuralı', 'METALİK AKTİFLİK SIRALAMASI (X > Y > Z) VE KAP AŞINMASI', 'Kap metali çözeltideki katyondan AKTİF ise tepkime olur, kap aşınır ve delinir!', 'X > Z olduğu için X metalinden yapılmış kapta Z(NO3)2 çözeltisi SAKLANAMAZ.', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Anot, hidrojen gazı çıkışı ve pasif kap özeti', 'ELEKTROKİMYASAL HÜCRE VE AKTİFLİK ÖZETİ', 'Yükseltgenme: Anot  ·  Aktif Metal + Asit -> H2 Gazı  ·  Saklama: Pasif Kap', 'Hidrojenin standart potansiyeli (0,00 V) aktif ve soy metalleri ayıran sınırdır.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Galvanik pilde anot, katot ve yoğun özellik', [('Anot Elektrot', 'Yükseltgenir, aşınır', TUR, TUR_A), ('Katot Elektrot', 'İndirgenme olur', MAVI, MAVI_A), ('İndirgen Metal', 'Elektron veren aktif', YES, YES_A), ('Yoğun Özellik', 'Katsayı E°’yi etkilemez', MOR, MOR_A)])

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
