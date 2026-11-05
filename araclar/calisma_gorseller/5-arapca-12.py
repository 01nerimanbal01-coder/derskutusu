"""5. sınıf Arapça 12. hafta (2. Ünite Genel Uygulamaları ve Değerlendirmesi) görselleri.
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
        '1. Eşya · Okul Çantası', 'حَقِيبَةٌ', 'Sonu (ة) dişil → هٰذِهِ', MOR, MOR_A,
        '2. Eşya · Telli Defter', 'دَفْتَرٌ', 'Eril isim → هٰذَا', MAVI, MAVI_A,
        'Çanta ve defter işaret ismi kartları.', ar1=True, ar2=True
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Yönerge (Aç)', 'اِفْتَحْ / اِفْتَحِي كِتَابَكِ', MAVI, MAVI_A),
        ('2. Yönerge (Kapat)', 'أَغْلِقْ / أَغْلِقِي دَفْتَرَكِ', TUR, TUR_A),
        ('3. Yönerge (Al)', 'خُذْ / خُذِي الْقَلَمَ', YES, YES_A),
        ('4. Yönerge (Bana ver)', 'أَعْطِنِي / أَعْطِينِي', MOR, MOR_A),
    ], 'Sınıf içi eril ve dişil yönerge kartları.', ar=True)
    s[5]['gorsel'] = ikili_kart(
        'Soru Kartı (هَلْ ...؟)', 'هَلْ هٰذَا قَلَمٌ؟', 'Bu bir kalem midir?', MAVI, MAVI_A,
        'Görseldeki Nesne: Silgi', 'مِمْحَاةٌ (Dişil)', 'Cevap: لَا، هٰذِهِ ...', KIR, KIR_A,
        'Silgi doğrulama sorusu kartı.', ar1=True, ar2=True
    )
    s[6]['gorsel'] = ikili_kart(
        '1. Durum: Bulunma (فِي)', 'فِي الْمُخْتَبَرِ', 'Laboratuvarda (-de/-da)', YES, YES_A,
        '2. Durum: Yönelme (إِلَى)', 'إِلَى الْمَكْتَبَةِ', 'Kütüphaneye doğru (-e/-a)', TUR, TUR_A,
        'Okul krokisinde bulunma ve yönelme kartları.', ar1=True, ar2=True
    )
    s[7]['gorsel'] = ikili_kart(
        '2. Ünite Vecizesi', 'اَلْعِلْمُ نَافِعٌ', 'Anlamı: İlim faydalıdır.', CAM, CAM_A,
        'Sesletim Kuralları', 'اَلْـ (Cezim) · نَا (Med)', 'ـعٌ (Ötre Tenvin)', MOR, MOR_A,
        'El-ilmü nâfiun vecizesi ve sesletim kartı.', ar1=True, ar2=True
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Adım: Selamlaşma', 'اَلسَّلَامُ عَلَيْكُمْ', MAVI, MAVI_A),
        ('2. Adım: Soru', 'مَا هٰذِهِ؟', TUR, TUR_A),
        ('3. Adım: Tanıtım', 'هٰذِهِ حَقِيبَتِي', YES, YES_A),
        ('4. Adım: Yönerge', 'اِفْتَحْ حَقِيبَتَكَ', MOR, MOR_A),
    ], 'Sınıf içi dört adımlı diyalog kartları.', ar=True)
    s[9]['gorsel'] = dortlu_kart([
        ('1. Kart (Med + Tenvin)', 'نَافِعٌ', MAVI, MAVI_A),
        ('2. Kart (Şedde + Tenvin)', 'صَفٌّ', YES, YES_A),
        ('3. Kart (Cezim — Şedde Yok!)', 'مَكْتَبَةٌ', KIR, KIR_A),
        ('4. Kart (Kamerî Cezim)', 'اَلْعِلْمُ', CAM, CAM_A),
    ], 'Dört Arapça kelimenin sesletim inceleme tablosu.', ar=True)
    s[11]['gorsel'] = ikili_kart(
        '1. Eşya Tanıtımı', 'هٰذَا كِتَابٌ / هٰذِهِ سَبُّورَةٌ', 'İşaret ismi + Eşya', MAVI, MAVI_A,
        '2. Mekân Bildirme', 'أَنَا فِي الْمَكْتَبَةِ', 'Zamir + فِي + Okul Bölümü', YES, YES_A,
        'Sınıf eşyası tanıtımı ve mekân bildirme cümle kartları.', ar1=True, ar2=True
    )
