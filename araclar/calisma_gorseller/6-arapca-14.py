"""6. sınıf Arapça 14. hafta çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#475569'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="14.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle', boy=14.0):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" font-weight="700" fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: Okul bölümleri 3 kart
    ic0 = kutu(4, 4, 352, 107, GRI_A, GRI)
    birimler = [
        ('Yönetim Birimleri', 'غُرْفَةُ الْمُدِيرِ', 'غُرْفَةُ الْمُعَلِّمِينَ', MAVI, MAVI_A),
        ('Bilim ve Okuma', 'اَلْمَكْتَبَةُ', 'اَلْمُخْتَبَرُ', YES, YES_A),
        ('Sosyal Alanlar', 'اَلصَّالَةُ الرِّيَاضِيَّةُ', 'اَلْمَقْصَفُ', TUR, TUR_A),
    ]
    for i, (bas, a1, a2, c, d) in enumerate(birimler):
        x = 10 + i * 115
        ic0 += kutu(x, 11, 110, 93, d, c)
        ic0 += yazi(x + 55, 27, bas, 8.6, c)
        ic0 += f'<line x1="{x+8}" y1="34" x2="{x+102}" y2="34" stroke="{c}" stroke-width="0.7"/>'
        ic0 += ar_yazi(x + 55, 60, a1, LAC, boy=13.0)
        ic0 += ar_yazi(x + 55, 88, a2, c, boy=12.5)
    s[0]['gorsel'] = svg(ic0, 'Okul bölümleri Arapça isim tamlaması kartları')

    # s[1]: 3 katlı okul kesiti (Kat 3: Laboratuvar, Kat 2: Kütüphane, Kat 1: Kantin ve Müdür Odası)
    ic1 = kutu(6, 5, 348, 105, GRI_A, GRI)
    ic1 += f'<polygon points="24,18 180,6 336,18" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1"/>'
    katlar = [
        (20, '3. Kat · اَلطَّابِقُ الثَّالِثُ', 'اَلْمُخْتَبَرُ (Laboratuvar)', MOR, MOR_A),
        (48, '2. Kat · اَلطَّابِقُ الثَّانِي', 'اَلْمَكْتَبَةُ (Kütüphane)', YES, YES_A),
        (76, '1. Kat · اَلطَّابِقُ الْأَوَّلُ', 'اَلْمَقْصَفُ (Kantin)', TUR, TUR_A),
    ]
    for yk, sol_m, sag_m, c, d in katlar:
        ic1 += kutu(24, yk, 312, 25, d, c, r=4)
        ic1 += yazi(102, yk + 16, sol_m, 8.6, c)
        ic1 += f'<line x1="180" y1="{yk+3}" x2="180" y2="{yk+22}" stroke="{c}" stroke-width="0.7"/>'
        ic1 += yazi(258, yk + 16, sag_m, 8.8, LAC)
    s[1]['gorsel'] = svg(ic1, 'Üç katlı okul binası kat planı')

    # s[2]: Tekil - Çoğul eşya kartları (Kitap, Raf, Sıra ikonlarıyla)
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    esyalar = [
        ('كِتَابٌ ← كُتُبٌ', MAVI, MAVI_A, '1 → 3 Kitap'),
        ('رَفٌّ ← رُفُوفٌ', YES, YES_A, '1 → 3 Raf'),
        ('مِقْعَدٌ ← مَقَاعِدُ', TUR, TUR_A, '1 → 3 Sıra'),
    ]
    for i, (ar_m, c, d, alt) in enumerate(esyalar):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        # Vektörel kitap/raf/sıra sembolü
        if i == 0:
            ic2 += kutu(x + 28, 19, 16, 20, '#f8fafc', c, r=2) + kutu(x + 48, 19, 16, 20, '#f8fafc', c, r=2) + kutu(x + 68, 19, 16, 20, '#f8fafc', c, r=2)
        elif i == 1:
            ic2 += f'<line x1="{x+24}" y1="23" x2="{x+86}" y2="23" stroke="{c}" stroke-width="2"/><line x1="{x+24}" y1="33" x2="{x+86}" y2="33" stroke="{c}" stroke-width="2"/>'
        else:
            ic2 += kutu(x + 35, 20, 40, 10, '#f8fafc', c, r=2) + f'<line x1="{x+40}" y1="30" x2="{x+40}" y2="39" stroke="{c}" stroke-width="1.5"/><line x1="{x+70}" y1="30" x2="{x+70}" y2="39" stroke="{c}" stroke-width="1.5"/>'
        ic2 += ar_yazi(x + 55, 66, ar_m, LAC, boy=13.5)
        ic2 += yazi(x + 55, 92, alt, 8.5, c)
    s[2]['gorsel'] = svg(ic2, 'Tekil ve çoğul okul eşyaları kartları')

    # s[5]: Koridor krokisi (Öğretmenler Odası - Kütüphane yan yana, karşıda Sınıf)
    ic5 = kutu(6, 6, 348, 103, GRI_A, GRI)
    ic5 += kutu(16, 14, 152, 36, MAVI_A, MAVI) + yazi(92, 28, 'اَلْمَكْتَبَةُ (Kütüphane)', 8.8, MAVI) + yazi(92, 43, 'بِجَانِبِ ← Yanında', 8.0, SOLUK, ince=True)
    ic5 += kutu(192, 14, 146, 36, YES_A, YES) + yazi(265, 28, 'غُرْفَةُ الْمُعَلِّمِينَ', 9.0, YES) + yazi(265, 43, 'Öğretmenler Odası', 8.0, SOLUK, ince=True)
    ic5 += f'<line x1="168" y1="32" x2="192" y2="32" stroke="{KIR}" stroke-width="1.4" stroke-dasharray="3,2"/>'
    ic5 += yazi(180, 63, 'اَلْمَمَرُّ (Koridor)', 8.5, SOLUK)
    ic5 += kutu(95, 71, 170, 30, TUR_A, TUR) + yazi(180, 90, 'اَلصَّفُّ السَّادِسُ (6. Sınıf)', 8.8, TUR)
    s[5]['gorsel'] = svg(ic5, 'Okul koridoru konum krokisi')

    # s[6]: Laboratuvar ve Kütüphane eşya kartları (Mikroskop + Bilgisayar vs Raf + Sözlük)
    ic6 = kutu(6, 6, 170, 103, CAM_A, CAM)
    ic6 += yazi(91, 23, 'اَلْمُخْتَبَرُ (Laboratuvar)', 9.2, CAM)
    # Mikroskop + ekran çizimi
    ic6 += kutu(30, 33, 42, 28, '#f8fafc', CAM, r=3) + f'<line x1="51" y1="61" x2="51" y2="68" stroke="{CAM}" stroke-width="2"/><line x1="38" y1="68" x2="64" y2="68" stroke="{CAM}" stroke-width="2"/>'
    ic6 += f'<path d="M122,34 L130,52 M126,44 C136,46 136,62 122,65 M112,66 L138,66" fill="none" stroke="{CAM}" stroke-width="2"/>'
    ic6 += ar_yazi(91, 92, 'مِجْهَرٌ وَحَاسُوبٌ', LAC, boy=13.5)

    ic6 += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic6 += yazi(269, 23, 'اَلْمَكْتَبَةُ (Kütüphane)', 9.2, MOR)
    ic6 += kutu(220, 34, 98, 30, '#f8fafc', MOR, r=3)
    for kx in range(228, 310, 14):
        ic6 += kutu(kx, 39, 9, 21, MOR_A, MOR, r=1, kalin=0.8)
    ic6 += ar_yazi(269, 92, 'رُفُوفٌ وَقَامُوسٌ', LAC, boy=13.5)
    s[6]['gorsel'] = svg(ic6, 'Laboratuvar ve kütüphane eşyaları')

    # s[7]: Sınıf kapısı ve izin diyaloğu balonları (insansız)
    ic7 = kutu(6, 6, 348, 103, GRI_A, GRI)
    # Kapı çizimi
    ic7 += kutu(16, 14, 52, 87, TUR_A, TUR, r=3) + kutu(23, 22, 38, 30, '#f8fafc', TUR, r=2) + f'<circle cx="59" cy="60" r="3" fill="{TUR}"/>'
    ic7 += kutu(80, 14, 262, 40, MAVI_A, MAVI) + ar_yazi(211, 34, 'هَلْ يُمْكِنُنِي الدُّخُولُ؟', MAVI, boy=13.5) + yazi(211, 49, 'İçeri girebilir miyim?', 8.2, SOLUK, ince=True)
    ic7 += kutu(80, 61, 126, 40, YES_A, YES) + ar_yazi(143, 81, 'تَفَضَّلْ (Eril)', YES, boy=13.0) + yazi(143, 96, 'Buyur (Erkek)', 8.0, SOLUK, ince=True)
    ic7 += kutu(216, 61, 126, 40, MOR_A, MOR) + ar_yazi(279, 81, 'تَفَضَّلِي (Dişil)', MOR, boy=13.0) + yazi(279, 96, 'Buyur (Kız)', 8.0, SOLUK, ince=True)
    s[7]['gorsel'] = svg(ic7, 'Sınıfa giriş izni ve eril-dişil buyur kalıbı')

    # s[8]: 4 adımlı diyalog akışı
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlar = [
        ('1. Sınıf Sorusu', 'فِي أَيِّ صَفٍّ؟', MAVI, MAVI_A),
        ('2. Sınıf Cevabı', 'اَلصَّفُّ السَّادِسُ', YES, YES_A),
        ('3. Kat Sorusu', 'فِي أَيِّ طَابِقٍ؟', TUR, TUR_A),
        ('4. Konum ve Teşekkür', 'شُكْرًا ← عَفْوًا', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic8 += kutu(x, 13, 80, 89, d, c) + yazi(x + 40, 34, b, 8.2, c)
        ic8 += f'<line x1="{x+7}" y1="44" x2="{x+73}" y2="44" stroke="{c}" stroke-width="0.7"/>'
        ic8 += ar_yazi(x + 40, 74, alt, LAC, boy=12.0)
        if i < 3:
            ic8 += f'<polygon points="{x+81},57 {x+85},52 {x+85},62" fill="{c}"/>'
    s[8]['gorsel'] = svg(ic8, 'Dört adımlı okul içi diyalog akışı')

    # s[9]: Ayet ve Veciz Söz levhası
    ic9 = kutu(6, 6, 170, 103, YES_A, YES)
    ic9 += yazi(91, 24, 'Tâhâ Suresi · 114. Ayet', 8.8, YES)
    ic9 += ar_yazi(91, 56, 'وَقُلْ رَبِّ زِدْنِي عِلْمًا', LAC, boy=13.5)
    ic9 += yazi(91, 86, 'Rabbim, ilmimi artır!', 8.3, SOLUK, ince=True)

    ic9 += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic9 += yazi(269, 24, 'Ünite Veciz Sözü', 8.8, TUR)
    ic9 += ar_yazi(269, 56, 'مَنْ جَدَّ وَجَدَ', LAC, boy=14.5)
    ic9 += yazi(269, 86, 'Ciddiyetle çalışan başarır.', 8.3, SOLUK, ince=True)
    s[9]['gorsel'] = svg(ic9, 'İlim konulu ayet ve veciz söz levhası')
