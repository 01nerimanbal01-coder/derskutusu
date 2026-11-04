"""6. sınıf İngilizce 6. hafta (School Life: School Routines, Simple Present, Adverbs of Frequency, Object Pronouns & Articles) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def elif_rutin_karti():
    ic = kutu(8, 8, 584, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 25, 'ELİF’S SCHOOL ROUTINE · WORD ORDER RULE', 12, '#fff')
    ic += yazi(300, 52, 'Rule 1: Subject - Adverb - Verb (-s) → Elif / always / arrive / on time', 12, LAC)
    ic += yazi(300, 76, 'Rule 2: Subject - am, is, are - Adverb → She / be / never / late for assembly', 12, MOR, ince=True)
    return svg(600, 100, ic, 'Elif okul rutini ve sıklık zarfları dizilim kuralı kartı.', 22)


def nesne_zamiri_karti():
    ic = kutu(8, 8, 584, 86, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 584, 26, MAVI, MAVI, 9, 1)
    ic += yazi(300, 25, 'OBJECT PRONOUNS IN SCHOOL LIFE', 12, '#fff')
    ic += yazi(300, 52, '“Our English teacher gives ___ (1: we) a new project,', 12, LAC)
    ic += yazi(300, 76, 'and we show ___ (2: it) to ___ (3: she) in the classroom.”', 12, MAVI, ince=True)
    return svg(600, 102, ic, 'We, it ve she zamirlerinin nesne zamiri karşılıklarını soran cümle kartı.', 22)


def articles_imperatives_panosu():
    kartlar = [
        ('1. ___ science exam', 'Consonant sound (Tekil)', MAVI, MAVI_A),
        ('2. ___ art room', 'Vowel sound (Ünlü ses)', YES, YES_A),
        ('3. ___ school garden', 'Specific place (Belirli)', TUR, TUR_A),
        ('4. ___ litter the corridor!', 'Negative instruction', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Articles (a, an, the) ve olumsuz emir cümlesi örnek kartları.', 22)


def fatih_sali_rutini():
    ic = kutu(8, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, '1. Affirmative (+) · Tuesday', 12, '#fff')
    ic += yazi(150, 52, 'Fatih ___ (help) the librarian', 12, LAC)
    ic += yazi(150, 74, 'in the school library.', 12, YES, ince=True)

    ic += kutu(308, 8, 284, 84, KIR_A, KIR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, KIR, KIR, 9, 1)
    ic += yazi(450, 25, '2. Negative (-) · Tuesday', 12, '#fff')
    ic += yazi(450, 52, 'He ___ (not - join) the chess', 12, LAC)
    ic += yazi(450, 74, 'club after school.', 12, KIR, ince=True)
    return svg(600, 100, ic, 'Fatih Salı günü olumlu ve olumsuz geniş zaman cümle kartları.', 22)


def gunluk_akis_zinciri():
    adimlar = [
        ('1. Morning (08.30)', 'Arrive · Line up', MAVI, MAVI_A),
        ('2. Lesson (09.00)', 'Greet · Listen', YES, YES_A),
        ('3. Noon (12.30)', 'Lunch in canteen', TUR, TUR_A),
        ('4. Afternoon (15.30)', 'Attend clubs', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC)
    return svg(600, 96, ic, 'Sabah törenden öğleden sonra kulüp saatine okul rutini akış şeması.', 22)


def okul_kurallari_panosu():
    satirlar = [
        ('Rule A', 'Keep your classroom desk clean and tidy.', YES, YES_A),
        ('Rule B', 'Return the borrowed books to the library on time.', MAVI, MAVI_A),
        ('Rule C (!)', 'Don’t run in the corridors and don’t make noise.', KIR, KIR_A),
        ('Rule D', 'Follow instructions and raise your hand to speak.', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(51, y + 15, no, 12, '#fff')
        ic += yazi(102, y + 15, metin, 12, LAC, 'start', ince=(i != 2))
    return svg(600, 112, ic, 'Dört sınıf yönergesi; Rule C olumsuz emir cümlesi.', 22)


def articles_hata_kartlari():
    satirlar = [
        ('1. Card', 'An art teacher works in an art room on the second floor.', YES, YES_A),
        ('2. Card', 'We wear a school uniform and carry a student ID card.', MAVI, MAVI_A),
        ('3. Card', 'The headmaster’s office is next to the school library.', CAM, CAM_A),
        ('4. Card (!)', 'Kyle plays a guitar in an music club on the Fridays.', KIR, KIR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(8, y, 584, 22, arka, renk, 6, 1.3)
        ic += kutu(8, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(51, y + 15, no, 12, '#fff')
        ic += yazi(102, y + 15, metin, 12, LAC, 'start', ince=(i != 3))
    return svg(600, 112, ic, 'a, an, the kullanımıyla ilgili dört kart; 4. kart hatalı.', 22)


def kutuphane_soru_karti():
    ic = kutu(8, 8, 584, 84, CAM_A, CAM, 9, 1.6)
    ic += kutu(8, 8, 584, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 25, 'SPEAKING & WRITING CARD · SCHOOL LIBRARY', 12, '#fff')
    ic += yazi(300, 52, 'Question: “How often do you use the school library and who helps you there?”', 12, LAC)
    ic += yazi(300, 76, 'Clues: usually - twice a week · the librarian helps me - us find books', 12, CAM, ince=True)
    return svg(600, 100, ic, 'Okul kütüphanesi kullanım sıklığı ve nesne zamiri soru kartı.', 22)


def uclu_rutin_tablosu():
    kartlar = [
        ('Kyle (Music Club)', 'Usually plays the guitar on Fridays', MAVI, MAVI_A),
        ('Elif (Punctual)', 'Always on time · Never late for assembly', YES, YES_A),
        ('Fatih (Class President)', 'Helps the librarian on Tuesdays · Supports us', TUR, TUR_A),
        ('Common Rule', 'All three follow rules and respect teachers', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Kyle, Elif ve Fatih okul rutinleri karşılaştırma panosu.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = elif_rutin_karti()
    s[4]['gorsel'] = nesne_zamiri_karti()
    s[5]['gorsel'] = articles_imperatives_panosu()
    s[6]['gorsel'] = fatih_sali_rutini()
    s[7]['gorsel'] = gunluk_akis_zinciri()
    s[8]['gorsel'] = okul_kurallari_panosu()
    s[9]['gorsel'] = articles_hata_kartlari()
    s[11]['gorsel'] = kutuphane_soru_karti()
    s[12]['gorsel'] = uclu_rutin_tablosu()
