"""10. sınıf Arapça 1. hafta (Akrabalarım: Meslek, İş ve Çalışma Yeri) çalışma kâğıdı görselleri.
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


def g0_akrabalar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Amca', 'عَمّ', TUR, TUR_A),
        ('Teyze', 'خَالَة', YES, YES_A),
        ('Nine', 'جَدَّة', MAVI, MAVI_A),
        ('Hala', 'عَمَّة', MOR, MOR_A)
    ]
    for i, (b, ar, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 28, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="36" x2="{x + 72}" y2="36" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, ar, 15, LAC)
    return svg(360, 100, ic, 'Dört temel Arapça akrabalık adı kartı', 34)


def g1_tesniye_doktorlar():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İKİL (TESNİYE) KADIN DOKTORLAR VE GÖREV YERİ', 11, MAVI)
    ic += kutu(20, 32, 150, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(95, 48, 'İki Kadın Doktor:', 10, SOLUK, ince=True)
    ic += yazi(95, 70, 'طَبِيبَتَانِ', 15, LAC)

    ic += kutu(190, 32, 150, 56, YES_A, YES, 6, 1.1)
    ic += yazi(265, 48, 'Çalıştıkları Yer:', 10, YES)
    ic += yazi(265, 70, 'تَعْمَلَانِ فِي الْمُسْتَشْفَى', 13, LAC)
    return svg(360, 100, ic, 'İki kadın doktor ve hastane çalışma yeri kartı', 34)


def g2_ogretmen_okul():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 160, 74, TUR_A, TUR, 8, 1.2)
    ic += yazi(90, 28, 'Meslek (Erkek):', 10.5, TUR)
    ic += yazi(90, 54, 'مُدَرِّس', 16, LAC)
    ic += yazi(90, 72, '(Öğretmen)', 9.5, SOLUK, ince=True)

    ic += kutu(190, 10, 160, 74, YES_A, YES, 8, 1.2)
    ic += yazi(270, 28, 'Çalışma Yeri:', 10.5, YES)
    ic += yazi(270, 54, 'مَدْرَسَة', 16, LAC)
    ic += yazi(270, 72, '(Okul)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Öğretmen ve okul çalışma yeri kartı', 34)


def g3_dil_bilgisi():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    kurallar = [
        ('هَذَانِ', 'İki erkek', MAVI, MAVI_A),
        ('خَال', 'Dayı', TUR, TUR_A),
        ('مَا مِهْنَتُهَا؟', 'Kadın meslek', YES, YES_A),
        ('هُمَا', 'O ikisi', MOR, MOR_A)
    ]
    for i, (ar, tr, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, ar, 13, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 10, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel dil bilgisi kural kartı', 34)


def g5_tekil_ikil_cogul():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    basamaklar = [
        ('1. Müfred (Tekil)', 'طَالِب', YES, YES_A),
        ('2. Tesniye (İkil)', 'طَالِبَانِ', MAVI, MAVI_A),
        ('3. Cemi (Çoğul)', 'طُلَّاب', TUR, TUR_A),
        ('4. İşaret (Çoğul)', 'هَؤُلَاءِ', MOR, MOR_A)
    ]
    for i, (b, ar, c, d) in enumerate(basamaklar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 26, b, 9.5, c)
        ic += yazi(x + 40, 54, ar, 14, LAC)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Tekil, ikil ve çoğul isim akışı', 34)


def g6_akraba_ziyareti():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'AİLE SEVGİSİ VE AKRABA ZİYARETİ İFADESİ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 54, 'أَزُورُ أَقَارِبِي فِي الْعِيدِ', 15, LAC)
    ic += yazi(180, 70, '(Bayramda akrabalarımı ziyaret ederim)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Akraba ziyareti ahlaki değer kartı', 34)


def g8_meslek_sorulari():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    sorular = [
        ('مَا مِهْنَتُهُ؟', 'Erkek mesleği', MAVI, MAVI_A),
        ('مَا مِهْنَتُهَا؟', 'Kadın mesleği', TUR, TUR_A),
        ('أَيْنَ يَعْمَلُ؟', 'Çalışma yeri', YES, YES_A),
        ('مَاذَا تَفْعَلُ؟', 'Yaptığı iş', MOR, MOR_A)
    ]
    for i, (ar, tr, c, d) in enumerate(sorular):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, ar, 12.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Dört meslek ve iş sorma cümlesi', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KELİME ŞİFRE ŞERİDİ: A - İ - L - E', 11.5, YES)
    harfler = [('1', 'A'), ('2', 'İ'), ('3', 'L'), ('4', 'E')]
    for i, (no, h) in enumerate(harfler):
        x = 65 + i * 60
        ic += kutu(x, 32, 50, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 25, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 25, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Aile şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_akrabalar()
    s[1]['gorsel'] = g1_tesniye_doktorlar()
    s[2]['gorsel'] = g2_ogretmen_okul()
    s[3]['gorsel'] = g3_dil_bilgisi()
    s[5]['gorsel'] = g5_tekil_ikil_cogul()
    s[6]['gorsel'] = g6_akraba_ziyareti()
    s[8]['gorsel'] = g8_meslek_sorulari()
    s[10]['gorsel'] = g10_sifre_seridi()
