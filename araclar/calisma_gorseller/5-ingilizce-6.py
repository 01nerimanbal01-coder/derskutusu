"""5. sınıf İngilizce 6. hafta (School Clubs, Countries and National Days: Do You Like + -ing, Mustn’t / Can’t & Imperatives) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kulup_tanitim_karti():
    ic = kutu(6, 6, 588, 86, MAVI_A, MAVI, 9, 1.5)
    ic += kutu(6, 6, 588, 26, MAVI, MAVI, 9, 1)
    ic += yazi(300, 24, 'SCHOOL CLUB APPLICATION CARD · LAB & NATURE', '#fff', kalin=True)
    ic += yazi(300, 52, '“I love ___ (1) in the laboratory, so I want to join ___ (2).”', LAC, kalin=True)
    ic += yazi(300, 76, 'Clues: microscope · test tubes · science lab', MAVI)
    return svg(600, 98, ic, 'Fen laboratuvarında deney yapma ve bilim kulübü başvuru kartı.', 21)


def okul_kurallari_tabelasi():
    kartlar = [
        ('1. Library Rule', 'No shouting! · Don’t make a noise!', KIR, KIR_A),
        ('2. Corridor Rule', 'No running! · Walk carefully!', TUR, TUR_A),
        ('3. Classroom Rule', 'Listen to your teacher carefully!', YES, YES_A),
        ('4. Garden Rule', 'Follow the rules and play safe!', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Kütüphane, koridor, sınıf ve bahçe kuralları tabelası.', 21)


def dort_kulup_ogrenci_karti():
    kartlar = [
        ('1. Mert', 'maths club · solving problems', MAVI, MAVI_A),
        ('2. Zeynep', 'art club · drawing pictures', MOR, MOR_A),
        ('3. Demir', 'drama club · acting on stage', TUR, TUR_A),
        ('4. Ece', 'folk dance club · dancing together', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört öğrencinin okul kulüpleri ve sevdikleri etkinlik kartları.', 21)


def diyalog_tercih_karti():
    ic = kutu(6, 6, 286, 86, MOR_A, MOR, 9, 1.4)
    ic += yazi(149, 25, '1. Question (You)', MOR, kalin=True)
    ic += yazi(149, 52, '“___ you like ___ (play)', LAC, kalin=True)
    ic += yazi(149, 75, 'chess in the chess club?”', LAC)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, '2. Answer (My Sister - She)', YESIL_K, kalin=True)
    ic += yazi(451, 52, '“Yes! And my sister ___ (love)', LAC, kalin=True)
    ic += yazi(451, 75, '___ (solve) puzzles.”', LAC)
    return svg(600, 98, ic, 'Do you like playing ve She loves solving diyalog tamamlama kartı.', 21)


def milli_bayram_takvimi():
    kartlar = [
        ('23 April', 'Children’s Day', MAVI, MAVI_A),
        ('19 May', 'Youth & Sports Day', YES, YES_A),
        ('30 August', 'Victory Day', TUR, TUR_A),
        ('29 October', 'Republic Day', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 82, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 62, alt, LAC, kalin=True)
    return svg(600, 94, ic, '23 Nisan, 19 Mayıs, 30 Ağustos ve 29 Ekim millî bayram takvim kartları.', 21)


def ulke_tanimlik_kartlari():
    satirlar = [
        ('Card 1', 'Kaan is from Türkiye and he is in a technology club.', YES, YES_A),
        ('Card 2', 'Leyla is from Azerbaijan and she is in an art club.', MAVI, MAVI_A),
        ('Card 3', 'Oliver is from the UK and he is in a sports club.', CAM, CAM_A),
        ('Card 4 (!)', 'Yumi is from the Japan and she is in a environment club.', KIR, KIR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(102, y + 15, metin, LAC, 'start', kalin=(i == 3))
    return svg(600, 112, ic, 'Ülkeler ve a-an-the kullanımıyla ilgili dört öğrenci kartı.', 21)


def kutuphane_koridor_posteri():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, '1. Warning Sign: Corridors', KIR, kalin=True)
    ic += yazi(149, 52, 'NO RUNNING IN CORRIDORS!', LAC, kalin=True)
    ic += yazi(149, 75, '(Use: You mustn’t ...)', KIR)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(451, 25, '2. Warning Sign: Library', TUR, kalin=True)
    ic += yazi(451, 52, 'NO NOISE IN THE LIBRARY!', LAC, kalin=True)
    ic += yazi(451, 75, '(Use: Don’t ...)', TUR)
    return svg(600, 98, ic, 'Koridorda koşmama ve kütüphanede gürültü yapmama uyarı posteri.', 21)


def kulup_tercih_tablosu():
    kartlar = [
        ('Arda (Science Club)', 'Loves doing experiments (+)', YES, YES_A),
        ('Sinem (Art Club)', 'Enjoys drawing & painting (+)', MAVI, MAVI_A),
        ('Burak (Drama Club)', 'Likes acting on stage (+)', TUR, TUR_A),
        ('Ceren (Music Club)', 'Hates playing chess (-)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Arda, Sinem, Burak ve Ceren’in kulüp tercihlerini gösteren pano.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kulup_tanitim_karti()
    s[4]['gorsel'] = okul_kurallari_tabelasi()
    s[5]['gorsel'] = dort_kulup_ogrenci_karti()
    s[6]['gorsel'] = diyalog_tercih_karti()
    s[7]['gorsel'] = milli_bayram_takvimi()
    s[8]['gorsel'] = ulke_tanimlik_kartlari()
    s[10]['gorsel'] = kutuphane_koridor_posteri()
    s[11]['gorsel'] = kulup_tercih_tablosu()
