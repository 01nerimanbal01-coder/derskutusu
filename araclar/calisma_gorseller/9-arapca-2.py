"""9. sınıf Arapça 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kartlar = [('مَرْحَبًا', 'Merhaba', MAVI, MAVI_A), ('صَبَاحُ النُّورِ', 'Aydınlık sabahlar', YES, YES_A), ('فِي أَمَانِ اللَّهِ', 'Allah\'a emanet', TUR, TUR_A), ('أَنَا بِخَيْرٍ', 'İyiyim', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 36, ar, 13, c) + f'<line x1="{x+10}" y1="46" x2="{x+70}" y2="46" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 66, tr, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Arapça karşılama ve veda kalıpları', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'TENVİN YAZIM KURALI: FETHATEYN (İKİ ÜSTÜN)', 11, MAVI)
    ic += kutu(20, 32, 150, 56, '#f4f8fe', MAVI) + yazi(95, 48, 'Elif desteğiyle:', 10, SOLUK, ince=True) + yazi(95, 70, 'بَيْتًا', 16, LAC)
    ic += kutu(190, 32, 150, 56, YES_A, YES) + yazi(265, 48, 'Kural:', 10, YES) + yazi(265, 70, 'İki üstün elif alır', 11, LAC)
    return svg(360, 100, ic, 'Tenvin iki üstün elif kuralı', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 30, 'HİTAP VE HÂL HATIR SORMA (MÜENNES / KIZ)', 11, TUR)
    ic += yazi(180, 54, 'كَيْفَ حَالُكِ؟', 16, LAC)
    ic += yazi(180, 72, '(Kef esreli okunarak kız öğrenciye sorulur)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Müennes hâl hatır sorma diyalog kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    turler = [('Şedde', 'ـّ', 'İkiler', KIR, KIR_A), ('Sükûn', 'ـْ', 'Durdurur', MAVI, MAVI_A), ('Tenvin', 'ـٌ ـٍ ـً', 'Çift ses', YES, YES_A), ('Elif-Dal', 'ا د ذ', 'Bitişmez', TUR, TUR_A)]
    for i, (b, sem, alt, c, d) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 28, b, 10.5, c) + yazi(x + 40, 50, sem, 15, LAC) + yazi(x + 40, 70, alt, 9, SOLUK, ince=True)
    return svg(360, 98, ic, 'Arapça ses işaretleri kartları', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Selam', 'السَّلَامُ عَلَيْكُمْ', YES, YES_A), ('2. Yanıt', 'وَعَلَيْكُمُ السَّلَامُ', MAVI, MAVI_A), ('3. Hatır', 'كَيْفَ حَالُكَ؟', TUR, TUR_A), ('4. Şükür', 'الْحَمْدُ لِلَّهِ', MOR, MOR_A)]
    for i, (bas, ar, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 28, bas, 10, c) + yazi(x + 40, 54, ar, 12, LAC)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Tanışma diyaloğu akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'SINIF İÇİ EMİR: KIZ ÖĞRENCİYE HİTAP', 11, CAM)
    ic += kutu(20, 36, 150, 44, '#eaf7fa', CAM) + yazi(95, 52, 'Müzekker (Erkek):', 9.5, SOLUK, ince=True) + yazi(95, 70, 'اُكْتُبْ', 14, LAC)
    ic += kutu(190, 36, 150, 44, TUR_A, TUR) + yazi(265, 52, 'Müennes (Kız):', 9.5, TUR) + yazi(265, 70, 'اُكْتُبِي', 14, TUR)
    return svg(360, 96, ic, 'Müzekker müennes emir panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    eylemler = [('اِقْرَأْ', 'Oku (Erkek)', MAVI, MAVI_A), ('اِقْرَئِي', 'Oku (Kız)', TUR, TUR_A), ('اِسْتَمِعْ', 'Dinle (Erkek)', YES, YES_A), ('اِسْتَمِعِي', 'Dinle (Kız)', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(eylemler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, ar, 13, c) + f'<line x1="{x+10}" y1="44" x2="{x+70}" y2="44" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 64, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Arapça emir fiilleri uyum kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KELİME: H - A - R - F', 11.5, YES)
    harfler = [('1', 'H'), ('2', 'A'), ('3', 'R'), ('4', 'F')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES) + yazi(x + 25, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Harf şifresi kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
