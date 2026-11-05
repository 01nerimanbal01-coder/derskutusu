"""6. sınıf İngilizce 13. hafta (Appearance, Personality, Comparative & Superlative) görselleri.
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
    s[1]['gorsel'] = dortlu_kart([
        ('Ali’s Height: 152 cm', 'The shortest in the group', TUR, TUR_A),
        ('Burak’s Height: 160 cm', 'Taller than Ali (160 > 152)', MAVI, MAVI_A),
        ('Can’s Height: 168 cm', 'The tallest of all (168 cm)', YES, YES_A),
        ('Comparison Rule', 'taller than · the tallest', MOR, MOR_A),
    ], 'Ali, Burak ve Can’ın boy uzunluğu karşılaştırma kartları.')
    s[2]['gorsel'] = dortlu_kart([
        ('1. Short Adjective: tall', 'taller than → the tallest', MAVI, MAVI_A),
        ('2. Long Adjective: patient', 'more patient → the most patient', YES, YES_A),
        ('3. Irregular: good', 'better than → the best', TUR, TUR_A),
        ('4. Irregular: bad', 'worse than → the worst', KIR, KIR_A),
    ], 'Kısa, uzun ve düzensiz sıfatların Comparative ve Superlative tablosu.')
    s[5]['gorsel'] = ikili_kart(
        'Emre’s Physical Appearance', 'is: Tall and slim', 'has got: Short wavy hair, brown eyes', MAVI, MAVI_A,
        'Emre’s Personality & Habits', 'is: Organised, tidy and helpful', 'wears: Comfortable trainers', YES, YES_A,
        'Emre’nin fiziksel görünüş ve kişilik profil kartı.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Selin’s Maths Score: 95 / 100', 'Very good score!', 'Irregular: good → better → best', YES, YES_A,
        'Mert’s Maths Score: 85 / 100', '95 > 85 Comparison:', 'Selin’s mark is ... than Mert’s.', MAVI, MAVI_A,
        'Selin ve Mert’in matematik notlarının good/better ile karşılaştırılması.'
    )
    s[7]['gorsel'] = ikili_kart(
        '1. Daily Habit (Simple Present)', 'Time clue: usually / every day', 'Ece usually wears trainers.', MAVI, MAVI_A,
        '2. Action Now (Present Cont.)', 'Time clue: now / today', 'She is wearing boots now.', TUR, TUR_A,
        'Geniş zaman (alışkanlık) ve şimdiki zaman (şu an) karşılaştırması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Heart (Göğüs / Kalp)', 'En üstteki iç organımız', KIR, KIR_A),
        ('2. Stomach (Karın / Mide)', 'Göğsün altındaki sindirim organı', TUR, TUR_A),
        ('3. Knee (Diz Eklemi)', 'Bacağın ortasındaki eklem', MAVI, MAVI_A),
        ('4. Ankle (Ayak Bileği)', 'Bacağın en altındaki bilek', YES, YES_A),
    ], 'Vücut bölümlerinin yukarıdan aşağıya doğru sıralama kartları.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Card (Correct)', 'more patient than (Uzun sıfat)', YES, YES_A),
        ('2. Card (Correct)', 'has got short straight hair', MAVI, MAVI_A),
        ('3. Card (Error: more taller!)', 'taller than (more kullanılmaz!)', KIR, KIR_A),
        ('4. Card (Correct)', 'Whose white trainers are these?', MOR, MOR_A),
    ], 'Comparative ve dış görünüş cümlelerinde hata analizi.')
    s[11]['gorsel'] = ikili_kart(
        'Profile 1: İpek (Height: 164 cm)', 'Appearance: Tall, wavy hair', 'Personality: Friendly, energetic', MAVI, MAVI_A,
        'Profile 2: Duru (Height: 156 cm)', 'Appearance: Medium height, slim', 'Personality: Very patient & organised', YES, YES_A,
        'İpek ve Duru’yu dış görünüş ve kişilik yönünden karşılaştırma kartları.'
    )
