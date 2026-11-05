"""6. sınıf İngilizce 12. hafta (Personality, Seasonal Clothes, Present Continuous vs Simple Present, Comparatives) görselleri.
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
        'Routine / Habit (Simple Present)', 'Time: usually / every day', 'Berk usually [ wears ] trainers.', MAVI, MAVI_A,
        'Action Now (Present Continuous)', 'Time: today / right now', 'Today he [ is wearing ] boots.', TUR, TUR_A,
        'Simple Present ve Present Continuous giyim karşılaştırma kartı.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. tall (1 syllable)', 'taller than · the tallest', MAVI, MAVI_A),
        ('2. slim (CVC doubling)', '... than · the slimmest', YES, YES_A),
        ('3. patient (long adj.)', 'more patient than · ...', TUR, TUR_A),
        ('4. good (irregular)', '... than · the ...', MOR, MOR_A),
    ], 'Comparative ve Superlative sıfat dönüşümleri tablosu.')
    s[5]['gorsel'] = ikili_kart(
        'Lost & Found Box: Item 1', 'Object: Blue Sports Trainers (Plural)', 'Owner Tag: Burak', MAVI, MAVI_A,
        'Question & Answer Rule', 'Whose trainers are these?', 'Plural → They are Burak’s trainers.', YES, YES_A,
        'Kayıp eşya kutusu ve Whose çoğul cevap kuralı.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('Ege (152 cm)', 'Organised: ★★☆ · Patient: ★★☆', MAVI, MAVI_A),
        ('Doruk (158 cm)', 'Organised: ★★★ · Patient: ★★☆', TUR, TUR_A),
        ('Çınar (165 cm - Tallest)', 'Organised: ★☆☆ · Patient: ★★★', YES, YES_A),
        ('Comparison Key', '165 > 158 > 152 cm', MOR, MOR_A),
    ], 'Ege, Doruk ve Çınar boy ve kişilik karşılaştırma tablosu.')
    s[7]['gorsel'] = ikili_kart(
        '1. Clue Card: Ceyda', 'Plans homework · Keeps desk tidy', 'Personality trait: o _ _ _ _ _ _ _ d', MAVI, MAVI_A,
        '2. Clue Card: Mert', 'Helps injured animals and friends', 'Personality trait: c _ _ _ _ g / helpful', YES, YES_A,
        'Ceyda ve Mert karakter ipucu kartları.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Question: Who?', 'Look at that boy! Who is he?', MAVI, MAVI_A),
        ('2. Question: Wearing?', 'What is he wearing right now?', TUR, TUR_A),
        ('3. Description', 'A green jacket and white trainers.', YES, YES_A),
        ('4. Character Info', 'That’s Emir! He is clever and polite.', MOR, MOR_A),
    ], 'Okul bahçesinde yeni arkadaşı tanıma diyaloğu.')
    s[9]['gorsel'] = ikili_kart(
        'Summer Holiday: Antalya (34 °C)', 'Hot and sunny beach weather', 'Pack: Swimsuit, sunglasses, T-shirt', TUR, TUR_A,
        'Winter Holiday: Uludağ (-4 °C)', 'Cold and snowy mountain weather', 'Pack: Thick coat, gloves, boots', CAM, CAM_A,
        'Yaz ve kış tatili bavul hazırlama kartları.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Friend A: Ali (162 cm)', 'Slim · Short hair · Friendly', 'Comparison: taller / slimmer than', MAVI, MAVI_A,
        'Friend B: Burak (156 cm)', 'Medium build · Patient & Organised', 'Comparison: more patient than', YES, YES_A,
        'İki arkadaşı dış görünüş ve kişilik yönünden karşılaştırma kartı.'
    )
