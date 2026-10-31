"""6. sınıf İngilizce 7. hafta (Theme 1: School Life — National Days, Celebrations & Different Schools) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def toren_program_karti():
    ic = kutu(8, 6, 584, 96, KIR_A, KIR, 9, 1.6)
    ic += kutu(8, 6, 584, 24, KIR, KIR, 9, 1)
    ic += yazi(300, 22, '29 OCTOBER REPUBLIC DAY CEREMONY PROGRAMME', 10.8, '#fff')
    gorevler = [
        ('09.30 — Choir', 'Singing the National Anthem', MAVI, MAVI_A),
        ('09.45 — Sinan (Stage)', 'Reciting a Republic Day Poem', TUR, TUR_A),
        ('10.00 — Dance Club', 'Performing Traditional Folk Dances', YES, YES_A),
    ]
    for i, (bas, alt, renk, arka) in enumerate(gorevler):
        x = 18 + i * 190
        ic += kutu(x, 38, 180, 56, arka, renk, 7, 1.4)
        ic += yazi(x + 90, 58, bas, 10.5, renk)
        ic += yazi(x + 90, 78, alt, 10.1, LAC, ince=True)
    return svg(600, 108, ic, '29 October Republic Day tören programı: koro, Sinan’ın şiir okuması ve halk oyunları.', 22)


def zaman_karsilastirma_karti():
    ic = kutu(8, 8, 284, 86, MOR_A, MOR, 9, 1.5)
    ic += kutu(8, 8, 284, 24, MOR, MOR, 9, 1)
    ic += yazi(150, 24, '1. Routine (Every Year)', 10.6, '#fff')
    ic += yazi(150, 52, '“We ___ (1) ___ Republic Day', 10.4, LAC)
    ic += yazi(150, 74, 'on 29 October every year.”', 10.2, MOR, ince=True)

    ic += kutu(308, 8, 284, 86, MAVI_A, MAVI, 9, 1.5)
    ic += kutu(308, 8, 284, 24, MAVI, MAVI, 9, 1)
    ic += yazi(450, 24, '2. Right Now (Look! / Now)', 10.6, '#fff')
    ic += yazi(450, 52, '“Look! The students ___ (2) ___', 10.4, LAC)
    ic += yazi(450, 74, 'the school with flags right now!”', 10.2, MAVI, ince=True)
    return svg(600, 102, ic, 'Simple Present (every year) ve Present Continuous (right now) karşılaştırma kartları.', 22)


def uc_okul_kartlari():
    okullar = [
        ('1. Ankara Fine Arts H.S.', 'Ankara, Türkiye', 'Music rooms & art studios', MOR, MOR_A),
        ('2. Samsun Alanlı V.L.C.', 'Samsun, Türkiye', 'Gardening & nature crafts', YES, YES_A),
        ('3. Baku Turkish Sec. Sch.', 'Baku, Azerbaijan', 'Cultural clubs & national days', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, yer, etk, renk, arka) in enumerate(okullar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 84, arka, renk, 9, 1.6)
        ic += kutu(x, 8, 188, 24, renk, renk, 9, 1)
        ic += yazi(x + 94, 24, ad, 10.4, '#fff')
        ic += yazi(x + 94, 52, yer, 10.5, LAC)
        ic += yazi(x + 94, 74, etk, 10.1, renk, ince=True)
    return svg(600, 100, ic, 'Ankara, Samsun ve Bakü’deki üç okul ortamını tanıtan bilgi kartları.', 22)


def nesne_zamiri_kartlari():
    ic = kutu(8, 8, 284, 80, CAM_A, CAM, 9, 1.5)
    ic += yazi(150, 28, 'Sentence 1 (Plural Noun → ?)', 10.6, CAM)
    ic += yazi(150, 50, 'The students are preparing the posters.', 10.2, LAC, ince=True)
    ic += yazi(150, 70, 'The teacher helps ___ (the students).', 10.3, LAC)

    ic += kutu(308, 8, 284, 80, TUR_A, TUR, 9, 1.5)
    ic += yazi(450, 28, 'Sentence 2 (Singular Female → ?)', 10.6, TUR)
    ic += yazi(450, 50, 'Mrs Aydın is our music teacher.', 10.2, LAC, ince=True)
    ic += yazi(450, 70, 'We listen to ___ (Mrs Aydın) carefully.', 10.3, LAC)
    return svg(600, 96, ic, 'Nesne zamiri dönüşümü için iki cümle kartı: the students ve Mrs Aydın.', 22)


def ogrenci_tercih_kartlari():
    kartlar = [
        ('Ece (Ankara)', 'Loves violin & painting', '→ Fine Arts High School', MOR, MOR_A),
        ('Mert (Samsun)', 'Enjoys gardening & nature', '→ Alanlı Village Life Centre', YES, YES_A),
        ('Leyla (Baku)', 'Celebrates common Turkish', '& Azerbaijani national days', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 82, arka, renk, 9, 1.5)
        ic += kutu(x, 8, 188, 24, renk, renk, 9, 1)
        ic += yazi(x + 94, 24, bas, 10.6, '#fff')
        ic += yazi(x + 94, 50, s1, 10.2, LAC, ince=True)
        ic += yazi(x + 94, 70, s2, 10.2, renk)
    return svg(600, 98, ic, 'Ece, Mert ve Leyla’nın okul tercihlerini gösteren üç kart.', 22)


def gorevliler_panosu():
    kartlar = [
        ('1. Headmaster', 'Manages the school', MAVI, MAVI_A),
        ('2. Librarian', 'Lends books in library', YES, YES_A),
        ('3. Chef', 'Prepares healthy meals', TUR, TUR_A),
        ('4. Security Guard (!)', 'Teaches English & Science (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, gorev, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 118, 30, renk, renk, 6, 1)
        ic += yazi(x + 65, y + 25, bas, 10.2, '#fff')
        ic += yazi(x + 206, y + 25, gorev, 10.2, LAC, ince=True)
    return svg(600, 104, ic, 'Okul görevlileri panosu: 4. kartta güvenlik görevlisine yanlış görev yazılmış.', 22)


def takvim_yapraklari():
    ic = kutu(8, 8, 284, 82, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 24, MAVI, MAVI, 9, 1)
    ic += yazi(150, 24, 'CALENDAR LEAF 1 · 19 MAY', 10.8, '#fff')
    ic += yazi(150, 50, 'Commemoration of Atatürk,', 10.5, LAC)
    ic += yazi(150, 70, 'Youth and Sports Day', 10.4, MAVI)

    ic += kutu(308, 8, 284, 82, KIR_A, KIR, 9, 1.6)
    ic += kutu(308, 8, 284, 24, KIR, KIR, 9, 1)
    ic += yazi(450, 24, 'CALENDAR LEAF 2 · 30 AUGUST', 10.8, '#fff')
    ic += yazi(450, 50, 'Victory Day', 10.8, LAC)
    ic += yazi(450, 70, '(Zafer Bayramı)', 10.2, KIR, ince=True)
    return svg(600, 98, ic, '19 May ve 30 August takvim yaprakları.', 22)


def bayram_davet_afisi():
    ic = kutu(8, 6, 584, 86, KIR_A, KIR, 9, 1.6)
    ic += kutu(8, 6, 584, 24, KIR, KIR, 9, 1)
    ic += yazi(300, 22, 'HAPPY 29 OCTOBER REPUBLIC DAY! · SCHOOL CEREMONY POSTER', 10.8, '#fff')
    ic += yazi(300, 48, 'Date: on 29 October  |  Place: School Garden  |  Time: 09.30 a.m.', 10.4, LAC)
    ic += yazi(300, 70, 'Activities: decorate with flags · sing the national anthem · read poems', 10.2, KIR, ince=True)
    return svg(600, 98, ic, '29 Ekim Cumhuriyet Bayramı okul töreni afişi.', 22)


def sorumluluk_listesi():
    kurallar = [
        ('1. Rule', 'Attend classes on time & listen', YES, YES_A),
        ('2. Rule (!)', 'Throw rubbish on corridor floor', KIR, KIR_A),
        ('3. Rule', 'Respect national values', MAVI, MAVI_A),
        ('4. Rule', 'Share group tasks fairly', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, metin, renk, arka) in enumerate(kurallar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 78, 30, renk, renk, 6, 1)
        ic += yazi(x + 45, y + 25, bas, 10.4, '#fff')
        ic += yazi(x + 188, y + 25, metin, 10.2, LAC, ince=True)
    return svg(600, 104, ic, 'Öğrenci sorumlulukları listesi: 2. kuralda koridora çöp atma ifadesi yanlış verilmiş.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = toren_program_karti()
    s[4]['gorsel'] = zaman_karsilastirma_karti()
    s[5]['gorsel'] = uc_okul_kartlari()
    s[6]['gorsel'] = nesne_zamiri_kartlari()
    s[8]['gorsel'] = ogrenci_tercih_kartlari()
    s[9]['gorsel'] = gorevliler_panosu()
    s[10]['gorsel'] = takvim_yapraklari()
    s[12]['gorsel'] = bayram_davet_afisi()
    s[13]['gorsel'] = sorumluluk_listesi()
