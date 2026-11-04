"""6. sınıf İngilizce 9. hafta (Theme 2: Classroom Life — Activities, Preferences, Time, Dates &amp; Revision) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def tercih_tablosu_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Mert’s Preferences', 10.3, MAVI)
    ic += yazi(91, 44, '(+) work in pairs (loves)', 9.7, YESIL_K)
    ic += yazi(91, 64, '(-) read aloud (dislikes)', 9.7, KIR, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Ece’s Preferences', 10.3, YESIL_K)
    ic += yazi(269, 44, '(+) do research (enjoys)', 9.7, YESIL_K)
    ic += yazi(269, 64, '(-) read aloud (hates)', 9.7, KIR, ince=True)
    return svg(360, 88, ic, 'Mert ve Ece’nin sınıf içi etkinlik tercihlerini gösteren kart.', 15)


def saat_ve_tarih_panosu():
    kartlar = [
        ('1. 08.15', 'a quarter past eight', MAVI, MAVI_A),
        ('2. 10.30', 'half past ? ', YES, YES_A),
        ('3. 11.45', 'a quarter to ? ', TUR, TUR_A),
        ('4. 19th May', 'the ? of May', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Saatler ve 19 Mayıs tarihi bilgi kartları.', 15)


def zaman_karsilastirma_panosu():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Habit (Every Day)', 10.3, TUR)
    ic += yazi(91, 44, '“Cem normally ___ (1) ___', 9.7, LAC)
    ic += yazi(91, 64, 'new words every evening...”', 9.5, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, '2. Action Now (At the Moment)', 10.1, MAVI)
    ic += yazi(269, 44, '“...but now he ___ (2) ___', 9.7, LAC)
    ic += yazi(269, 64, 'a science task in groups.”', 9.5, LAC, ince=True)
    return svg(360, 88, ic, 'Simple Present ve Present Progressive karşılaştırma kartı.', 15)


def dort_question_tag_karti():
    kartlar = [
        ('Card A', 'You are focusing, aren’t you?', YES, YES_A),
        ('Card B', 'Pelin enjoys it, doesn’t she?', MAVI, MAVI_A),
        ('Card C', 'They don’t read, do they?', MOR, MOR_A),
        ('Card D (!)', 'Kerem is marking, doesn’t he?', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, met, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Dört Question Tag kontrol kartı.', 16)


def kutuphane_sayi_fisi():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 22, 'Cardinal Number (100–500)', 10.1, CAM)
    ic += yazi(91, 46, 'Book Code: 345', 10.4, LAC)
    ic += yazi(91, 66, 'Spelling = ?', 9.6, CAM, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'Ordinal Number (1st–50th)', 10.1, MOR)
    ic += yazi(269, 46, 'Student Rank: 31st', 10.4, LAC)
    ic += yazi(269, 66, 'Spelling = ?', 9.6, MOR, ince=True)
    return svg(360, 88, ic, '345 sayma sayısı ve 31st sıra sayısı yazım kartı.', 15)


def diyalog_siralama_panosu():
    adimlar = [
        ('Step 1', 'Ask about working alone', MAVI, MAVI_A),
        ('Step 2', 'Teacher suggests pairs', YES, YES_A),
        ('Step 3', 'Express enjoyment (+V-ing)', TUR, TUR_A),
        ('Step 4', 'Start &amp; take turns now', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 54, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Sınıf içi ikili çalışma diyaloğu akış basamakları.', 15)


def milli_gunler_takvimi():
    gunler = [
        ('23rd April', 'Children’s Day · 09.30', MAVI, MAVI_A),
        ('19th May', 'Youth Day · 10.00', YES, YES_A),
        ('29th October', 'Republic Day · 10.15', TUR, TUR_A),
        ('10th November', 'Atatürk Memorial · 09.05', MOR, MOR_A),
    ]
    ic = ''
    for i, (tarih, bilgi, r, z) in enumerate(gunler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, tarih, 10.1, r)
        ic += yazi(x + 86, y + 31, bilgi, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Millî günlerin tarih ve saatlerini gösteren takvim panosu.', 16)


def tercih_yazma_ipucu_karti():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 22, 'LEARNING PREFERENCES · WRITING PROMPTS', 10.3, YESIL_K)
    ic += yazi(180, 44, 'Positive (+): enjoy / love / like + working in pairs · doing research', 9.5, LAC, ince=True)
    ic += yazi(180, 64, 'Negative (-): dislike / hate + reading aloud · doing long exercises', 9.5, KIR, ince=True)
    return svg(360, 88, ic, 'Sınıf içi öğrenme tercihleri yazma ipucu kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tercih_tablosu_karti()
    s[2]['gorsel'] = saat_ve_tarih_panosu()
    s[5]['gorsel'] = zaman_karsilastirma_panosu()
    s[6]['gorsel'] = dort_question_tag_karti()
    s[7]['gorsel'] = kutuphane_sayi_fisi()
    s[8]['gorsel'] = diyalog_siralama_panosu()
    s[9]['gorsel'] = milli_gunler_takvimi()
    s[11]['gorsel'] = tercih_yazma_ipucu_karti()
