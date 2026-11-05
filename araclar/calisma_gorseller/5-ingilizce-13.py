"""5. sınıf İngilizce 13. hafta (Clothes, Possessive Adjectives, Routines & Question Tags) görselleri.
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
        'Winter Weather (Snowy & Cold)', 'Thick coat · Warm scarf · Gloves', 'Kış için kalın ve sıcak giysiler', MAVI, MAVI_A,
        'Summer Weather (Sunny & Hot)', 'Thin T-shirt · Sunglasses · Hat', 'Yaz için ince ve rahat giysiler', TUR, TUR_A,
        'Kış ve yaz mevsimine uygun giysi ve aksesuar kartları.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('I → my / You → your', 'my raincoat · your jacket', MAVI, MAVI_A),
        ('He → his (Erkek)', 'his blue jumper · his watch', YES, YES_A),
        ('She → her (Kız)', 'her red handbag · her skirt', MOR, MOR_A),
        ('We → our / They → their', 'our classroom · their uniforms', TUR, TUR_A),
    ], 'İngilizce kişi zamirleri ve iyelik sıfatları eşleşme tablosu.')
    s[5]['gorsel'] = dortlu_kart([
        ('Always (100%)', 'Her zaman (Every day)', YES, YES_A),
        ('Usually (80%)', 'Genellikle (Most days)', MAVI, MAVI_A),
        ('Sometimes (50%)', 'Bazen (On some days)', TUR, TUR_A),
        ('Never (0% — Mert’s Tie)', 'Asla / Hiçbir zaman', KIR, KIR_A),
    ], 'Sıklık zarfları (Frequency Adverbs) ve yüzdelik oranları.')
    s[6]['gorsel'] = dortlu_kart([
        ('07:15 (Quarter past seven)', 'Wake up and wash face', MAVI, MAVI_A),
        ('07:30 (Half past seven)', 'Have breakfast with family', YES, YES_A),
        ('07:45 (Quarter to eight)', 'Zeynep gets dressed for school', TUR, TUR_A),
        ('08:15 (Quarter past eight)', 'Arrive at school', MOR, MOR_A),
    ], 'Zeynep’in sabah rutini ve saat ifadeleri.')
    s[7]['gorsel'] = ikili_kart(
        '1. Positive → Negative Tag', 'You wear gloves, don’t you?', 'She wears a coat, doesn’t she?', YES, YES_A,
        '2. Negative → Positive Tag', 'You don’t wear a tie, do you?', 'She doesn’t like hats, does she?', KIR, KIR_A,
        'Geniş zamanda onay soruları (Question Tags) kuralları.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. En Sık: Always (100%)', '★★★★ (Her zaman)', YES, YES_A),
        ('2. Sık: Usually (80%)', '★★★☆ (Genellikle)', MAVI, MAVI_A),
        ('3. Orta: Sometimes (50%)', '★★☆☆ (Bazen)', TUR, TUR_A),
        ('4. Hiç: Never (0%)', '☆☆☆☆ (Asla)', KIR, KIR_A),
    ], 'Sıklık zarflarının %100’den %0’a sıralama kartları.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Card (Correct)', 'Ali → his thick jumper', YES, YES_A),
        ('2. Card (Correct)', 'Ayşe → her new handbag', MAVI, MAVI_A),
        ('3. Card (Error: They → their!)', 'Can and Efe → his trainers (✗)', KIR, KIR_A),
        ('4. Card (Correct)', 'Pelin wears..., doesn’t she?', MOR, MOR_A),
    ], 'İyelik sıfatı ve onay sorusu doğruluk kontrol kartları.')
    s[11]['gorsel'] = ikili_kart(
        '1. Winter Clothes Prompt', 'I usually wear my thick coat,', 'scarf and boots in winter.', MAVI, MAVI_A,
        '2. Daily Routine & Time Prompt', 'I go to school at', 'eight o’clock (08:00) every day.', YES, YES_A,
        'Kış giyim alışkanlığı ve okula gidiş saati yazma ipuçları.'
    )
