"""6. sınıf İngilizce 8. hafta (Theme 2: Classroom Life — Study Routines, Present Progressive vs. Simple Present & Numbers) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def defne_calisma_karti():
    ic = kutu(8, 6, 584, 92, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 6, 584, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 24, 'STUDENT ACTIVITY BOARD · DEFNE’S SCHEDULE', 12, '#fff')
    ic += kutu(20, 40, 270, 50, '#fff', MAVI, 7, 1.4)
    ic += yazi(155, 58, 'Every Afternoon (Routine):', 12, MAVI)
    ic += yazi(155, 78, 'Reviews notes & keeps a diary', 12, LAC, ince=True)
    ic += kutu(310, 40, 270, 50, YES_A, YES, 7, 1.4)
    ic += yazi(445, 58, 'Right Now (At the Moment):', 12, YES)
    ic += yazi(445, 78, 'Searching for science project in library', 12, LAC)
    return svg(600, 104, ic, 'Defne’nin günlük rutini ve şu an kütüphanede fen projesi araştırması yaptığını gösteren kart.', 22)


def iki_zaman_karti():
    ic = kutu(8, 8, 284, 84, TUR_A, TUR, 9, 1.5)
    ic += kutu(8, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(150, 25, '1. General Routine (Normally)', 12, '#fff')
    ic += yazi(150, 52, '“Kaan normally ___ (1) ___ alone', 12, LAC)
    ic += yazi(150, 74, 'in his room after dinner.”', 12, TUR, ince=True)

    ic += kutu(308, 8, 284, 84, MAVI_A, MAVI, 9, 1.5)
    ic += kutu(308, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(450, 25, '2. Action in Progress (Today · Now)', 12, '#fff')
    ic += yazi(450, 52, '“...but today he ___ (2) ___', 12, LAC)
    ic += yazi(450, 74, 'in pairs with his peer right now.”', 12, MAVI, ince=True)
    return svg(600, 100, ic, 'Simple Present (normally) ve Present Progressive (today / right now) boşluk doldurma kartları.', 22)


def sayi_panosu():
    kartlar = [
        ('1. 268', 'two hundred and sixty-eight', MAVI, MAVI_A),
        ('2. 380', 'three hundred and ? ', YES, YES_A),
        ('3. 12th', '? (Ordinal form of 12)', TUR, TUR_A),
        ('4. 23rd', '? (Ordinal form of 23)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += kutu(x + 6, y + 6, 78, 30, renk, renk, 6, 1)
        ic += yazi(x + 45, y + 25, bas, 12, '#fff')
        ic += yazi(x + 188, y + 25, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Cardinal (245, 380) ve Ordinal (12th, 23rd) sayı panosu.', 22)


def question_tag_kartlari():
    ic = kutu(8, 8, 284, 82, CAM_A, CAM, 9, 1.5)
    ic += yazi(150, 26, 'Sentence 1 (Present Progressive)', 12, CAM)
    ic += yazi(150, 50, '“Emre is reading a poem aloud,', 12, LAC, ince=True)
    ic += yazi(150, 72, '__________ ?” (he + is → ?)', 12, LAC)

    ic += kutu(308, 8, 284, 82, MOR_A, MOR, 9, 1.5)
    ic += yazi(450, 26, 'Sentence 2 (Simple Present)', 12, MOR)
    ic += yazi(450, 50, '“They review their notes every evening,', 12, LAC, ince=True)
    ic += yazi(450, 72, '__________ ?” (they + V1 → ?)', 12, LAC)
    return svg(600, 98, ic, 'Question Tag tamamlanacak iki cümle kartı.', 22)


def uc_ogrenci_aliskanlik():
    kartlar = [
        ('Arda', 'Reviews notes twice a week', '& keeps a study diary', MAVI, MAVI_A),
        ('Selin', 'Works in groups · Shares', 'creative ideas with peers', YES, YES_A),
        ('Bora', 'Does research in library', '& practises vocabulary daily', TUR, TUR_A),
    ]
    ic = ''
    for i, (ad, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 198
        ic += kutu(x, 8, 188, 82, arka, renk, 9, 1.5)
        ic += kutu(x, 8, 188, 25, renk, renk, 9, 1)
        ic += yazi(x + 94, 25, ad, 12, '#fff')
        ic += yazi(x + 94, 52, s1, 12, LAC, ince=True)
        ic += yazi(x + 94, 72, s2, 12, renk)
    return svg(600, 98, ic, 'Arda, Selin ve Bora’nın çalışma alışkanlıklarını gösteren üç bilgi kartı.', 22)


def dort_sayi_karti():
    kartlar = [
        ('1. Card: 415', 'four hundred and fifteen', YES, YES_A),
        ('2. Card: 20th', 'twentieth', MAVI, MAVI_A),
        ('3. Card: 50th', 'fiftieth', MOR, MOR_A),
        ('4. Card: 32nd (!)', 'thirty-two (?)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, okunus, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, okunus, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Dört sayı kartı; 4. kartta 32nd sıra sayısı yanlışlıkla thirty-two yazılmış.', 22)


def rutin_ve_bugun_karti():
    ic = kutu(8, 8, 584, 84, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 25, 'MY STUDY ROUTINE (EVERY DAY) vs. RIGHT NOW (TODAY)', 12, '#fff')
    ic += yazi(300, 52, 'Routine prompts: review notes · keep a diary · read silently (every evening · usually)', 12, LAC, ince=True)
    ic += yazi(300, 74, 'Now prompts: practise vocabulary · work in pairs · do research (right now · at the moment)', 12, MOR)
    return svg(600, 100, ic, 'Genel çalışma rutini ve şu an yapılan sınıf etkinliği yazma ipucu kartı.', 22)


def sinif_diyalog_balonu():
    ic = kutu(8, 8, 584, 84, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 584, 26, YES, YES, 9, 1)
    ic += yazi(300, 25, 'CLASSROOM DIALOGUE · EXAM RESULTS (SCORE: 100)', 12, '#fff')
    ic += yazi(300, 52, 'Ege: “Look at my exam paper! I answered all the questions correctly.', 12, LAC, ince=True)
    ic += yazi(300, 74, '______________________________ !”   |   Peer: “Congratulations, Ege!”', 12, YES)
    return svg(600, 100, ic, 'Sınavdan 100 tam puan alan Ege’nin sınıf arkadaşıyla konuşma kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = defne_calisma_karti()
    s[4]['gorsel'] = iki_zaman_karti()
    s[5]['gorsel'] = sayi_panosu()
    s[6]['gorsel'] = question_tag_kartlari()
    s[8]['gorsel'] = uc_ogrenci_aliskanlik()
    s[9]['gorsel'] = dort_sayi_karti()
    s[11]['gorsel'] = rutin_ve_bugun_karti()
    s[12]['gorsel'] = sinif_diyalog_balonu()
