"""9. sınıf Arapça 1. hafta (Selamlaşma ve Arapça Yazıya Başlangıç) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def g0_selamlasma():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('1. Sabah', 'صَبَاحُ الْخَيْرِ', TUR, TUR_A),
        ('2. Karşılama', 'أَهْلًا وَسَهْلًا', YES, YES_A),
        ('3. Veda', 'مَعَ السَّلَامَةِ', MAVI, MAVI_A),
        ('4. Hâl Hatır', 'كَيْفَ حَالُكَ؟', MOR, MOR_A)
    ]
    for i, (b, a, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 28, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="36" x2="{x + 72}" y2="36" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 60, a, 13.5, LAC)
    return svg(360, 100, ic, 'Dört temel Arapça selamlaşma ve hitap kartı', 34)


def g1_harf_gruplari():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'KENDİNDEN SONRAYA BİTİŞMEYEN HARFLER', 11.5, MAVI)
    harfler = [('Elif', 'ا'), ('Dal', 'د'), ('Zel', 'ذ'), ('Ra', 'ر'), ('Ze', 'ز'), ('Vav', 'و')]
    for i, (ad, h) in enumerate(harfler):
        x = 14 + i * 56
        ic += kutu(x, 32, 50, 56, '#f4f8fe', MAVI, 6, 1.1)
        ic += yazi(x + 25, 52, h, 18, LAC)
        ic += yazi(x + 25, 78, ad, 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Kendisinden sonraki harfe bitişmeyen altı Arapça harf', 34)


def g2_diyalog():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 160, 74, TUR_A, TUR, 8, 1.2)
    ic += yazi(90, 28, 'Kerim (Hitap):', 11, TUR)
    ic += yazi(90, 52, 'مَسَاءُ الْخَيْرِ', 15, LAC)
    ic += yazi(90, 72, '(Hayırlı akşamlar)', 9.5, SOLUK, ince=True)

    ic += kutu(190, 10, 160, 74, YES_A, YES, 8, 1.2)
    ic += yazi(270, 28, 'Arkadaşı (Cevap):', 11, YES)
    ic += yazi(270, 52, 'مَسَاءُ النُّورِ', 15, LAC)
    ic += yazi(270, 72, '(Aydınlık akşamlar)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Akşam selamlaşması diyalog kartları', 34)


def g3_harekeler():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    harekeler = [
        ('Şedde', 'ـّ', 'Harfi ikiler', KIR, KIR_A),
        ('Yazı Yönü', '←', 'Sağdan sola', TUR, TUR_A),
        ('Sükûn', 'ـْ', 'Sessiz durdurur', MAVI, MAVI_A),
        ('Tenvin', 'ـٌ ـٍ ـً', 'Son çift ses', YES, YES_A)
    ]
    for i, (b, sembol, alt, c, d) in enumerate(harekeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 26, b, 10.5, c)
        ic += yazi(x + 40, 50, sembol, 17, LAC)
        ic += yazi(x + 40, 72, alt, 9, SOLUK, ince=True)
    return svg(360, 98, ic, 'Temel Arapça hareke ve işaret kartları', 34)


def g5_tanisma_akisi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. Selam', 'السَّلَامُ عَلَيْكُمْ', YES, YES_A),
        ('2. Karşılık', 'وَعَلَيْكُمُ السَّلَامُ', MAVI, MAVI_A),
        ('3. Hâl Hatır', 'كَيْفَ حَالُكَ؟', TUR, TUR_A),
        ('4. Şükür', 'أَنَا بِخَيْرٍ', MOR, MOR_A)
    ]
    for i, (bas, ar, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 26, bas, 10, c)
        ic += yazi(x + 40, 52, ar, 12.5, LAC)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Arapça tanışma ve selamlaşma sıralama akışı', 34)


def g6_emir_panosu():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'SINIF İÇİ YÖNERGE PANOSU (MÜENNES / KIZ ÖĞRENCİ)', 11, CAM)
    ic += kutu(20, 34, 150, 48, '#eaf7fa', CAM, 6, 1.1)
    ic += yazi(95, 52, 'Müzekker (Erkek):', 10, SOLUK, ince=True)
    ic += yazi(95, 70, 'اِقْرَأْ (Oku)', 13, LAC)

    ic += kutu(190, 34, 150, 48, TUR_A, TUR, 6, 1.2)
    ic += yazi(265, 52, 'Müennes (Kız Öğrenci):', 10, TUR)
    ic += yazi(265, 70, 'اِقْرَئِي (Oku)', 14, TUR)
    return svg(360, 96, ic, 'Öğretmen sınıf içi emir yönergesi panosu', 34)


def g8_sinif_yonergeleri():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    eylemler = [
        ('اِسْتَمِعْ', 'Dinle', MAVI, MAVI_A),
        ('اُكْتُبْ', 'Yaz', TUR, TUR_A),
        ('أَعِدْ', 'Tekrar et', YES, YES_A),
        ('اُنْظُرْ', 'Bak', MOR, MOR_A)
    ]
    for i, (ar, tr, c, d) in enumerate(eylemler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 36, ar, 14.5, c)
        ic += f'<line x1="{x + 12}" y1="46" x2="{x + 68}" y2="46" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, tr, 11, LAC)
    return svg(360, 96, ic, 'Dört temel sınıf içi yönerge kartı', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KELİME ŞİFRE ŞERİDİ', 11.5, YES)
    harfler = [('1', 'S'), ('2', 'E'), ('3', 'L'), ('4', 'A'), ('5', 'M')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Selam şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_selamlasma()
    s[1]['gorsel'] = g1_harf_gruplari()
    s[2]['gorsel'] = g2_diyalog()
    s[3]['gorsel'] = g3_harekeler()
    s[5]['gorsel'] = g5_tanisma_akisi()
    s[6]['gorsel'] = g6_emir_panosu()
    s[8]['gorsel'] = g8_sinif_yonergeleri()
    s[10]['gorsel'] = g10_sifre_seridi()
