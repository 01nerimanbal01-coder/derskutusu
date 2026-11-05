"""12. sınıf Din Kültürü ve Ahlak Bilgisi 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return kart4('Müslüman bilim insanları ve öncü alanları', [('Harizmi', 'Cebir · Sıfır (0)', MAVI, MAVI_A), ('İbni Sina', 'el-Kânûn fi’t-Tıb', YES, YES_A), ('Cezeri', 'Sibernetik · Robotik', TUR, TUR_A), ('Cabir b. Hayyan', 'Kimya · İmbik · Asit', MOR, MOR_A)])

def g1():
    return uclu('Fizik, felsefe ve sosyolojide öncü eserler', 'İSLAM MEDENİYETİNDE DENEYSEL BİLİM VE DÜŞÜNCE', ('İbni Heysem', 'Kitabü’l-Menâzır (Optik)', MAVI, MAVI_A), ('Farabi', 'İhsâü’l-Ulûm (Mantık)', YES, YES_A), ('İbni Haldun', 'Mukaddime (Sosyoloji)', TUR, TUR_A), MAVI, MAVI_A)

def g2():
    return pano('Fatır Suresi 27 ve 28. ayetlerde haşyet bilinci', 'KUR’AN’DAN MESAJLAR: FATIR SURESİ 27-28. AYETLER', 'Tabiattaki Renk, Meyve, Kayaç ve Canlı Çeşitliliği → Kudret Delili', 'Haşyet: Allah’ın ilmini ve azametini kavrayan âlimlerin derin saygısı', MOR, MOR_A, '#f5f0ff')

def g3():
    return kart4('Tıp, coğrafya ve tefekkür çalışmaları', [('Akşemseddin', 'Mikrop fikri (Tıp)', YES, YES_A), ('Ebû Bekir Razi', 'Çiçek ve kızamık', MAVI, MAVI_A), ('Fatır 27-28', 'Tefekkür ve bilim', MOR, MOR_A), ('Piri Reis', 'Kitab-ı Bahriye', TUR, TUR_A)])

def g5():
    return akis4('Fatır suresi 27-28. ayetlerin tefekkür akışı', [('1. Yağmur-Meyve', 'Farklı renk ve tatlar', YES, YES_A), ('2. Dağlar-Kayaç', 'Beyaz, kızıl, siyah', TUR, TUR_A), ('3. Canlılar', 'Farklı renk ve türler', MAVI, MAVI_A), ('4. Âlimler', 'Derin saygı (Haşyet)', MOR, MOR_A)])

def g6():
    return pano('İslam dünyasında coğrafya çalışmaları', 'COĞRAFYA BİLİMİNDE MÜSLÜMAN ÂLİMLERİN ÖNCÜLÜĞÜ', 'İbni Hurdazbih: Kitabü’l-Mesâlik ve’l-Memâlik (İslam Coğrafyasının Babası)', 'Harizmi: Kitabü Sureti’l-Arz · Piri Reis: Dünya Haritası ve Kitab-ı Bahriye', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Dil, astronomi ve Fatır kavramı', 'KUR’AN DİLİ, ASTRONOMİ VE YARATILIŞ KAVRAMLARI', 'Ebü’l-Esved ed-Düelî (Harekeleme) · Fezari (İlk Usturlab) · Fâtır (Yaratan)', 'Müslüman bilginler hem vahyi korumuş hem de evreni rasathanelerde incelemiştir.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Hadis, sözlük, jeodezi ve tıp öncüleri', [('Buhari - Müslim', 'Sahih hadis külliyatı', MAVI, MAVI_A), ('Halil b. Ahmed', 'Kitabü’l-Ayn sözlüğü', TUR, TUR_A), ('Biruni', 'Jeodezi · Özgül ağırlık', MOR, MOR_A), ('İbni Nefis', 'Küçük kan dolaşımı', YES, YES_A)])

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
