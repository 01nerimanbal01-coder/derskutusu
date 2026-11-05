"""12. sınıf Din Kültürü ve Ahlak Bilgisi 8. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.5, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Fatır suresi ve bilim kurumları kavramları', [('Fâtır', 'Yoktan eşsiz yaratan', YES, YES_A), ('Haşyet', 'Bilgiye dayalı saygı', MAVI, MAVI_A), ('Beytülhikme', 'Bağdat bilim merkezi', MOR, MOR_A), ('Darüşşifa', 'Tıp ve şifa kurumu', TUR, TUR_A)])

def g1():
    return uclu('Fatır 27-28. ayetlerde işaret edilen tabiat alanları', 'FATIR SURESİ 27-28. AYETLERDE KEVNİ DELİLLER', ('Yağmur & Meyveler', 'Meteoroloji ve Botanik', YES, YES_A), ('Renkli Dağ Katmanları', 'Jeoloji ve Coğrafya', TUR, TUR_A), ('İnsan & Canlı Türleri', 'Biyoloji ve Zooloji', MAVI, MAVI_A), YES, YES_A)

def g2():
    return pano('Âlim kavramı ve haşyet bilinci', 'FATIR SURESİ 28. AYET · İLİM VE HAŞYET İLİŞKİSİ', '"Kulları içinden ancak âlimler, Allah\'tan (gereğince) haşyet duyar."', 'Sanattaki inceliği bilen âlim, Yaratıcının sonsuz kudretine derin saygı duyar.', MAVI, MAVI_A, '#f4f8fe')

def g3():
    return kart4('Fatır suresi ve İslam medeniyeti bilgileri', [('el-Melâike', 'Fatır suresinin diğer adı', MAVI, MAVI_A), ('Garâbîbü Sûd', 'Simsiyah dağ katmanı', TUR, TUR_A), ('Rasathane', 'Gözlemevi kurumu', MOR, MOR_A), ('el-Gafûr', 'Çokça bağışlayan', YES, YES_A)])

def g5():
    return akis4('Kevni ayetlerden haşyet bilincine ulaşma', [('1. Bitkiler', 'Yağmur ve meyveler', YES, YES_A), ('2. Dağlar', 'Renkli kayaç yolları', TUR, TUR_A), ('3. Canlılar', 'Biyolojik çeşitlilik', MAVI, MAVI_A), ('4. Haşyet', 'Derin saygı ve iman', MOR, MOR_A)])

def g6():
    return kart4('İslam medeniyetinde eğitim ve bilim kurumları', [('Suffe', 'İlk eğitim kurumu', YES, YES_A), ('Beytülhikme', 'Tercüme akademisi', MOR, MOR_A), ('Darülkurra', 'Kur\'an kıraat okulu', MAVI, MAVI_A), ('Darüşşifa', 'Uygulamalı tıp/hastane', TUR, TUR_A)])

def g7():
    return uclu('Haşyet, Nizamiye ve ilahi isimler', 'FATIR 28. AYET VE İSLAM EĞİTİM GELENEĞİ', ('Haşyet Bilinci', 'Âlimlerin derin saygısı', YES, YES_A), ('Nizamiye Medresesi', 'Selçuklu yükseköğretimi', MOR, MOR_A), ('el-Azîz & el-Gafûr', 'Mutlak güç ve mağfiret', MAVI, MAVI_A), MOR, MOR_A)

def g8():
    return kart4('Müslüman âlimler ve öncü çalışmaları', [('Cezerî', 'Sibernetik & Robotik', TUR, TUR_A), ('Pîrî Reis', 'Kitâb-ı Bahriye', CAM, CAM_A), ('Akşemseddin', 'Maddetü\'l-Hayât', YES, YES_A), ('İbn Haldun', 'Mukaddime (Sosyoloji)', MOR, MOR_A)])

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
