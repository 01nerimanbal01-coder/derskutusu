"""9. sınıf Arapça 4. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    medler = [('ا (Elif)', 'Fetha (Üstün) uzatır', MAVI, MAVI_A), ('و (Vav)', 'Damme (Ötre) uzatır', YES, YES_A), ('ي (Ye)', 'Kesra (Esre) uzatır', TUR, TUR_A), ('ـْ (Cezim)', 'Harfi durdurur', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(medler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 34, ar, 14, c) + f'<line x1="{x+10}" y1="44" x2="{x+70}" y2="44" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 66, tr, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Med harfleri ve harekeler kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'SINIF İÇİ EMİR: KIZ ÖĞRENCİYE HİTAP', 11, MAVI)
    ic += kutu(20, 32, 150, 56, '#f4f8fe', MAVI) + yazi(95, 48, 'Müzekker (Erkek):', 9.5, SOLUK, ince=True) + yazi(95, 70, 'اِقْرَأْ', 15, LAC)
    ic += kutu(190, 32, 150, 56, YES_A, YES) + yazi(265, 48, 'Müennes (Kız):', 9.5, YES) + yazi(265, 70, 'اِقْرَئِي', 15, YES)
    return svg(360, 100, ic, 'Müennes emir fiili levhası', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'VEDALAŞMA VE ESENLİK KALIPLARI', 11, TUR)
    ic += yazi(180, 50, 'إِلَى اللِّقَاءِ  ·  مَعَ السَّلَامَةِ', 15, LAC)
    ic += yazi(180, 70, 'Ayrılırken selamet ve esenlik dilekleriyle vedalaşılır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Arapça vedalaşma ifadeleri kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    kurallar = [('Elif Uzatması', 'Üstün ses uzatır', MAVI, MAVI_A), ('Vav Uzatması', 'Ötre ses uzatır', TUR, TUR_A), ('Ye Uzatması', 'Esre ses uzatır', YES, YES_A), ('Teşekkür', 'Şükran - Afven', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Med harfleri ve iletişim kuralları', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Dinle', 'اِسْتَمِعْ', YES, YES_A), ('2. Oku', 'اِقْرَأْ', MAVI, MAVI_A), ('3. Tekrar', 'أَعِدْ', TUR, TUR_A), ('4. Yaz', 'اُكْتُبْ', MOR, MOR_A)]
    for i, (bas, ar, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 28, bas, 10, c) + yazi(x + 40, 54, ar, 13, LAC)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Sınıf içi yönerge uygulama basamakları', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'TANIŞMA VE MEMNUNİYET DİYALOĞU', 11, CAM)
    ic += kutu(20, 36, 150, 44, '#eaf7fa', CAM) + yazi(95, 50, 'تَشَرَّفْتُ بِمَعْرِفَتِكَ', 11.5, LAC) + yazi(95, 68, '(Memnun oldum)', 9, SOLUK, ince=True)
    ic += kutu(190, 36, 150, 44, YES_A, YES) + yazi(265, 50, 'فُرْصَةٌ سَعِيدَةٌ', 11.5, YES) + yazi(265, 68, '(Çok memnun oldum)', 9, YES, ince=True)
    return svg(360, 96, ic, 'Memnuniyet diyalog kalıpları panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    nezaket = [('تَشَرَّفْتُ', 'Memnun oldum', MAVI, MAVI_A), ('شُكْرًا', 'Teşekkür ederim', TUR, TUR_A), ('عَفْوًا', 'Rica ederim', YES, YES_A), ('فِي أَمَانِ اللَّهِ', 'Allah\'a emanet', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(nezaket):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, ar, 12, c) + f'<line x1="{x+8}" y1="44" x2="{x+72}" y2="44" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 64, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Nezaket ve vedalaşma eşleştirme kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: U - Z - A - T - M - A', 11.5, YES)
    harfler = [('1', 'U'), ('2', 'Z'), ('3', 'A'), ('4', 'T'), ('5', 'M'), ('6', 'A')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES) + yazi(x + 21, 46, no, 9, SOLUK, ince=True) + yazi(x + 21, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Uzatma şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
