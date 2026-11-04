"""6. sınıf İngilizce 5. hafta (People at School and Their Roles and Responsibilities) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

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


def okul_panosu_articles():
    ic = kutu(6, 6, 588, 86, MOR_A, MOR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 24, 'SCHOOL NOTICE BOARD · ARTICLES & THERE IS - THERE ARE', '#fff', kalin=True)
    ic += yazi(300, 50, '• We have (1) ___ assembly in the yard. (2) ___ assembly starts at 08.30.', LAC, kalin=True)
    ic += yazi(300, 74, '• (3) ___ three science laboratories and two music rooms on the first floor.', MOR, kalin=True)
    return svg(600, 98, ic, 'a, an, the ve there is, there are yapılarını içeren okul duyuru panosu.', 21)


def sifat_zarf_kontrol_kartlari():
    satirlar = [
        ('1. Card', 'Defne is a careful leader and she listens to everyone carefully.', YES, YES_A),
        ('2. Card', 'The student volunteers water the garden flowers willingly.', MAVI, MAVI_A),
        ('3. Card (!)', 'Arda is a good speaker and he leads our project team good.', KIR, KIR_A),
        ('4. Card', 'Speak in a polite manner and enter the library quietly.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(102, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'Carefully, willingly, good-well ve quietly yapılarını denetleyen dört kart.', 21)


def roportaj_soru_kartlari():
    kartlar = [
        ('1. ___ is the class leader?', 'Answer: Selin is. (Person)', MAVI, MAVI_A),
        ('2. ___ does he work?', 'Answer: In the canteen. (Place)', YES, YES_A),
        ('3. ___ does the nurse do?', 'Answer: Cares for students. (Duty)', TUR, TUR_A),
        ('4. ___ is the assembly?', 'Answer: On Monday morning. (Time)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Who, Where, What ve When soru sözcüklerini eşleştiren dört röportaj kartı.', 21)


def sude_gorev_donusum_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(6, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(149, 24, 'Sude’s Speech (“I” Subject)', '#fff', kalin=True)
    ic += yazi(149, 50, '“I lead the art club and', LAC, kalin=True)
    ic += yazi(149, 74, 'I care for the brushes.”', MAVI, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(308, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(451, 24, 'Third Person (“Sude / She”)', '#fff', kalin=True)
    ic += yazi(451, 50, 'Rule: He / She + Verb (-s)', LAC, kalin=True)
    ic += yazi(451, 74, 'lead → leads · care → cares', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'Birinci tekil şahıstan üçüncü tekil şahısa Present Simple dönüşüm kartı.', 21)


def konusma_plani_zinciri():
    adimlar = [
        ('1. Name & Role', 'Class 6-A · Class guide', MAVI, MAVI_A),
        ('2. Daily Duties', 'Show library & labs', YES, YES_A),
        ('3. Keen & Club', 'Keen on books · Volunteer', TUR, TUR_A),
        ('4. Support & Praise', 'Teacher · Team player!', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Sınıftaki rolünü anlatan konuşma ve yazma planının 4 adımı.', 21)


def proje_takimi_rolleri():
    kartlar = [
        ('Lale · Group Leader', 'Collects notes & leads the team well', YES, YES_A),
        ('Emre · Volunteer', 'Waters plants & carries posters willingly', MAVI, MAVI_A),
        ('Kaan · School Guide', 'Shows new students around cheerfully', TUR, TUR_A),
        ('Nehir · Team Player', 'Shares materials & helps friends politely', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Lale, Emre, Kaan ve Nehir’in proje grubundaki rollerini gösteren tablo.', 21)


def hata_duzeltme_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(6, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(149, 24, 'Student’s Draft (3 Mistakes!)', '#fff', kalin=True)
    ic += yazi(149, 50, '“There are a librarian in our school.', LAC, kalin=True)
    ic += yazi(149, 74, 'Him helps we kindly.”', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, CAM_A, CAM, 9, 1.4)
    ic += kutu(308, 6, 286, 26, CAM, CAM, 9, 1)
    ic += yazi(451, 24, 'Grammar Clues', '#fff', kalin=True)
    ic += yazi(451, 50, '1) Singular: There is a ...', LAC, kalin=True)
    ic += yazi(451, 74, '2) Subject: He/She · 3) Object: us', CAM, kalin=True)
    return svg(600, 98, ic, 'There is ve zamir kullanımı hatalarını içeren öğrenci taslağı kartı.', 21)


def okul_dergisi_roportaj_panosu():
    kartlar = [
        ('Ms Yıldız · Librarian', 'Works in library · Lends books politely', MAVI, MAVI_A),
        ('Mr Akın · Caretaker', 'Keeps classrooms and garden clean', YES, YES_A),
        ('School Numbers', '24 classrooms & 2 P.E. teachers', TUR, TUR_A),
        ('Student Responsibilities', 'Keep desks tidy & return books on time', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okul dergisi için yapılan görev ve sorumluluk röportajı özet panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = okul_panosu_articles()
    s[4]['gorsel'] = sifat_zarf_kontrol_kartlari()
    s[5]['gorsel'] = roportaj_soru_kartlari()
    s[6]['gorsel'] = sude_gorev_donusum_karti()
    s[7]['gorsel'] = konusma_plani_zinciri()
    s[8]['gorsel'] = proje_takimi_rolleri()
    s[10]['gorsel'] = hata_duzeltme_karti()
    s[11]['gorsel'] = okul_dergisi_roportaj_panosu()
