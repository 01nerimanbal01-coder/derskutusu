"""5. sınıf İngilizce 12. hafta (Body Parts, Physical Features, Clothes & Daily Routines) görselleri.
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
        'Profile Card: Kerem', 'Height & Build: Tall and slim', 'Use: is (am/is/are)', MAVI, MAVI_A,
        'Hair & Eyes Features', 'Hair: Short curly brown hair', 'Use: has got (have/has got)', YES, YES_A,
        'Kerem fiziksel görünüm bilgi kartı.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. I → my', 'my two hands (2 el)', MAVI, MAVI_A),
        ('2. He → ? (his)', '... blue jacket', TUR, TUR_A),
        ('3. She → her', 'her white ... (tooth çoğulu)', YES, YES_A),
        ('4. They → ? (their)', '... warm boots', MOR, MOR_A),
    ], 'Zamirler, iyelik sıfatları ve çoğul isimler tablosu.')
    s[5]['gorsel'] = ikili_kart(
        'Weather Report: Snowy & -3 °C', 'Cold winter day outside', 'Keep neck, hands and feet warm!', CAM, CAM_A,
        'Winter Wardrobe Box', 'Coat · Scarf · Gloves · Boots', 'Avoid: T-shirt & sandals', TUR, TUR_A,
        'Karlı kış günü hava durumu ve uygun giysi seçimi kartı.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('Brush teeth: %100', 'always (every day)', YES, YES_A),
        ('Wear watch: %80', 'usually (most days)', MAVI, MAVI_A),
        ('Wear raincoat: %50', 'sometimes (on rainy days)', TUR, TUR_A),
        ('Skip breakfast: %0', 'never (0 days)', KIR, KIR_A),
    ], 'Arda haftalık sıklık zarfları (Frequency Chart) tablosu.')
    s[7]['gorsel'] = ikili_kart(
        '1. Positive Sentence (+ → −)', 'You wear glasses, ___ ___?', 'Ipucu: Simple Present (don’t you)', MAVI, MAVI_A,
        '2. Negative Sentence (− → +)', 'Mert doesn’t like cold, ___ ___?', 'Ipucu: He → does he', MOR, MOR_A,
        'Question Tags (eklenti soruları) uygulama kartları.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Greeting & Offer Help', 'How can I help you today?', MAVI, MAVI_A),
        ('2. Customer Request', 'I am looking for a winter jacket.', TUR, TUR_A),
        ('3. Fitting Room Suggestion', 'Would you like to try it on?', YES, YES_A),
        ('4. Decision & Thanks', 'It fits me well. Thank you!', MOR, MOR_A),
    ], 'Giyim mağazası alışveriş diyaloğu adımları.')
    s[9]['gorsel'] = dortlu_kart([
        ('Card 1: Mina', 'Short · Curly hair · No glasses', TUR, TUR_A),
        ('Card 2: Can', 'Tall · Wavy hair · Glasses', MAVI, MAVI_A),
        ('Card 3: Elif', 'Medium · Slim · Long straight · Glasses', YES, YES_A),
        ('Card 4: Bora', 'Medium · Straight hair · Cap', MOR, MOR_A),
    ], 'Dört farklı karakter profil etiketi karşılaştırması.')
    s[11]['gorsel'] = ikili_kart(
        'Step 1: Appearance', 'is tall / medium / slim', 'has got wavy / straight hair', MAVI, MAVI_A,
        'Step 2: Clothes Routine', 'usually wears jumper / jeans', 'tries on / puts on coat', YES, YES_A,
        'Arkadaş betimleme ve günlük giyim yazma rehberi kartı.'
    )
