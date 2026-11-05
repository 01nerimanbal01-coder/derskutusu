"""12. sınıf Din Kültürü ve Ahlak Bilgisi 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return kart4('Öncü Müslüman âlimler ve başyapıtları', [('Hârizmî', 'Kitâbü’l-Cebr (0)', MAVI, MAVI_A), ('İbn Sînâ', 'el-Kânûn fi’t-Tıb', YES, YES_A), ('İbnü’l-Heysem', 'Kitâbü’l-Menâzır', TUR, TUR_A), ('İbn Haldun', 'Mukaddime (Ümran)', MOR, MOR_A)])

def g1():
    return uclu('İslam tıp ve astronomi bilginleri', 'İSLAM MEDENİYETİNDE TIP VE ASTRONOMİ ÖNCÜLERİ', ('Akşemseddin', 'Mâddetü’l-Hayât (Mikrop)', YES, YES_A), ('Uluğ Bey', 'Semerkant Rasathanesi', MAVI, MAVI_A), ('Ali Kuşçu', 'Risâletü’l-Fethiyye', TUR, TUR_A), YES, YES_A)

def g2():
    return pano('İbnül Heysem karanlık oda ve optik deneyi', 'İBNÜ’L-HEYSEM (ALHAZEN) · MODERN OPTİK VE KARANLIK ODA', 'Beytü’l-Muzlim (Camera Obscura) deneyiyle görme olayını kanıtladı:', 'Görme, gözden çıkan ışınlarla değil cisimden yansıyan ışığın göze gelmesiyle olur.', MAVI, MAVI_A, '#f4f8fe')

def g3():
    return kart4('Kimya, tefsir, hadis ve sibernetik öncüleri', [('Câbir b. Hayyân', 'İmbik ve asit keşfi', TUR, TUR_A), ('Elmalılı Yazır', 'Hak Dini Kur’an Dili', YES, YES_A), ('Kütüb-i Sitte', '6 sahih hadis eseri', MAVI, MAVI_A), ('Cezerî', 'Sibernetik ve robotik', MOR, MOR_A)])

def g5():
    return akis4('İslam bilim mirasının gelişimi ve Avrupa’ya etkisi', [('1. Tedvin Dönemi', 'Dinî ilimlerin kaydı', YES, YES_A), ('2. Beytülhikme', 'Tercüme ve gözlem', MAVI, MAVI_A), ('3. Altın Çağ', 'Özgün bilimsel eser', TUR, TUR_A), ('4. Batı’ya Etki', 'Endülüs -> Rönesans', MOR, MOR_A)])

def g6():
    return pano('Müslüman âlimlerin Batı dünyasındaki Latince isimleri', 'BATI DÜNYASINDA TANINAN MÜSLÜMAN BİLİM İNSANLARI', 'İbn Sînâ -> Avicenna · İbn Rüşd -> Averroes · Hârizmî -> Algoritmi', 'İbnü’l-Heysem -> Alhazen · Câbir b. Hayyân -> Geber', MOR, MOR_A, '#f5f0ff')

def g7():
    return pano('Fârâbî, Pîrî Reis ve Fuat Sezgin bilim mirası', 'FELSEFE, DENİZCİLİK VE BİLİM TARİHİ MİRASIMIZ', 'Fârâbî (Muallim-i Sânî) · Pîrî Reis (Kitâb-ı Bahriye) · Prof. Dr. Fuat Sezgin', 'Gülhane Parkı İslam Bilim ve Teknoloji Tarihi Müzesi bu mirası yaşatmaktadır.', CAM, CAM_A, '#eaf7fa')

def g8():
    return kart4('Tıp, cerrahi, astronomi ve fıkıh öncüleri', [('Ebû Bekir Râzî', 'Çiçek-kızamık farkı', YES, YES_A), ('Zehrâvî', '200+ cerrahi alet', KIR, KIR_A), ('Uluğ Bey', 'Zîc yıldız kataloğu', MAVI, MAVI_A), ('İmam Şâfiî', 'er-Risâle (Usul)', TUR, TUR_A)])

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
