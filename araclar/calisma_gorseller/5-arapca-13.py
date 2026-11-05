"""5. sınıf Arapça 13. hafta (Sınıf Arkadaşlarım, İyelik Ekleri ve Diyalog Uygulamaları) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115, mm=20):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ikili_kart(b1, s1a, s1b, r1, z1, b2, s2a, s2b, r2, z2, etiket, ar1=False, ar2=False):
    ic = kutu(6, 6, 170, 103, z1, r1)
    ic += yazi(91, 28, b1, r1, kalin=True)
    ic += (ar_yazi(91, 60, s1a, LAC) if ar1 else yazi(91, 58, s1a, LAC, kalin=True))
    ic += yazi(91, 90, s1b, r1)
    ic += kutu(184, 6, 170, 103, z2, r2)
    ic += yazi(269, 28, b2, r2, kalin=True)
    ic += (ar_yazi(269, 60, s2a, LAC) if ar2 else yazi(269, 58, s2a, LAC, kalin=True))
    ic += yazi(269, 90, s2b, r2)
    return svg(ic, etiket)


def dortlu_kart(kartlar, etiket, ar=False):
    konum = [(6, 6), (184, 6), (6, 60), (184, 60)]
    ic = ''
    for (x, y), (b1, b2, r, z) in zip(konum, kartlar):
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += (ar_yazi(x + 85, y + 41, b2, LAC) if ar else yazi(x + 85, y + 39, b2, LAC))
    return svg(ic, etiket)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ikili_kart(
        '1. Kart · Eril Tanıtım (Ali)', 'هٰذَا صَدِيقِي عَلِيٌّ', 'هُوَ طَالِبٌ (Erkek öğrenci)', MAVI, MAVI_A,
        '2. Kart · Dişil Tanıtım (Zeynep)', 'هٰذِهِ صَدِيقَتِي زَيْنَبُ', 'هِيَ طَالِبَةٌ (Kız öğrenci)', MOR, MOR_A,
        'Eril ve dişil sınıf arkadaşı tanıtım kartları.', ar1=True, ar2=True
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Kitap (كِتَابٌ)', 'كِتَابِي · كِتَابُكَ · كِتَابُكِ', MAVI, MAVI_A),
        ('2. Kalem (قَلَمٌ)', 'قَلَمِي · قَلَمُكَ · قَلَمُكِ', TUR, TUR_A),
        ('3. Defter (دَفْتَرٌ)', 'دَفْتَرِي · دَفْتَرُكَ · دَفْتَرُكِ', YES, YES_A),
        ('4. Çanta (حَقِيبَةٌ → ت)', 'حَقِيبَتِي · حَقِيبَتُكَ · حَقِيبَتُكِ', MOR, MOR_A),
    ], 'Sınıf eşyalarında bitişik iyelik zamirleri tablosu.', ar=True)
    s[5]['gorsel'] = ikili_kart(
        'Soru (Kerem → Ömer)', 'هَلْ هٰذَا دَفْتَرُكَ؟', 'Bu senin defterin mi?', MAVI, MAVI_A,
        'Cevap (Ömer · Olumlu)', 'نَعَمْ، هٰذَا دَفْتَرِي', 'Evet, bu benim defterim.', YES, YES_A,
        'Aidiyet doğrulama sorusu ve cevabı kartı.', ar1=True, ar2=True
    )
    s[6]['gorsel'] = ikili_kart(
        'Erkek Muhataba Rica', 'مِنْ فَضْلِكَ أَعْطِنِي', 'Lütfen bana ver (Eril)', MAVI, MAVI_A,
        'Kız Muhataba Rica (Meryem)', 'مِنْ فَضْلِكِ أَعْطِينِي', 'Lütfen bana ver (Dişil)', KIR, KIR_A,
        'Eril ve dişil nezaket ile ödünç isteme kalıpları.', ar1=True, ar2=True
    )
    s[7]['gorsel'] = ikili_kart(
        'Yuvarlak Tâ (ة) Kuralı 1', 'حَقِيبَةٌ + ـِي → حَقِيبَتِي', 'Çanta → Benim çantam', TUR, TUR_A,
        'Yuvarlak Tâ (ة) Kuralı 2', 'صَدِيقَةٌ + ـِي → صَدِيقَتِي', 'Kız arkadaş → Kız arkadaşım', MOR, MOR_A,
        'Yuvarlak tâ harfinin iyelik ekiyle açık tâya dönüşümü.', ar1=True, ar2=True
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Rica (Lütfen bana ver)', 'مِنْ فَضْلِكَ أَعْطِنِي الْقَلَمَ', MAVI, MAVI_A),
        ('2. Uzatma (Buyur, al)', 'تَفَضَّلْ، خُذِ الْقَلَمَ', YES, YES_A),
        ('3. Teşekkür (Teşekkürler)', 'شُكْرًا جَزِيلًا يَا صَدِيقِي', TUR, TUR_A),
        ('4. Karşılık (Rica ederim)', 'عَفْوًا!', MOR, MOR_A),
    ], 'Sınıf içi dört adımlı yardımlaşma diyaloğu.', ar=True)
    s[9]['gorsel'] = dortlu_kart([
        ('1. Kart (Doğru)', 'هٰذَا صَدِيقِي، هُوَ طَالِبٌ', YES, YES_A),
        ('2. Kart (Doğru)', 'هٰذِهِ مُعَلِّمَتِي، هِيَ فِي الصَّفِّ', MAVI, MAVI_A),
        ('3. Kart (Hatalı Ek!)', 'يَا فَاطِمَةُ، اِفْتَحِي كِتَابَكَ', KIR, KIR_A),
        ('4. Kart (Doğru)', 'تَفَضَّلِي، خُذِي الدَّفْتَرَ', CAM, CAM_A),
    ], 'Zamir ve iyelik eki uyum inceleme kartları.', ar=True)
    s[11]['gorsel'] = ikili_kart(
        '1. Kişi Tanıtım Kartı', 'هٰذَا صَدِيقِي، هُوَ طَالِبٌ', 'Arkadaşım ve öğrenci tanıtımı', MAVI, MAVI_A,
        '2. Aidiyet Bildirme Kartı', 'هٰذِهِ حَقِيبَتِي / هٰذَا كِتَابِي', 'Benim eşyam cümle kalıbı', YES, YES_A,
        'Kişi tanıtımı ve eşya aidiyeti cümle kurma kartları.', ar1=True, ar2=True
    )
