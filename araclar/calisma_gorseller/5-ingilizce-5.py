"""5. sınıf İngilizce 5. hafta (School Life: People and Places at School, a/an/the and To Be) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def personel_kimlik_karti():
    ic = kutu(6, 6, 588, 86, MOR_A, MOR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 24, 'SCHOOL STAFF ID CARD · PERSONEL TANITIM KARTI', '#fff', kalin=True)
    ic += yazi(300, 50, 'Name: Mrs. Yıldız · Role: (1) ___ assistant to the headmaster', LAC, kalin=True)
    ic += yazi(300, 74, 'Place: (2) ___ is in the administration department next to the gate.', MOR, kalin=True)
    return svg(600, 98, ic, 'Mrs. Yıldız müdür yardımcısı personel tanıtım kartı.', 20)


def okul_yerlesim_plani():
    kartlar = [
        ('Upstairs (1st Floor)', 'Library & Science Lab', MAVI, MAVI_A),
        ('Downstairs (Ground Floor)', 'Canteen & Conference Hall', YES, YES_A),
        ('Next to the School Gate', 'Administration Department', TUR, TUR_A),
        ('Outside (School Garden)', 'Sports Field', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okulun alt ve üst katlarındaki yerleri gösteren yerleşim planı.', 20)


def dort_personel_gorev_kartlari():
    kartlar = [
        ('1. Mr. Demir', 'Headmaster · Administration Dept.', MAVI, MAVI_A),
        ('2. Mrs. Kaya', 'Cook · Canteen (Downstairs)', TUR, TUR_A),
        ('3. Mr. Arslan', 'Coach · Sports Field (Outside)', YES, YES_A),
        ('4. Ms. Çelik', 'Science Teacher · Science Lab', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört okul çalışanının görev ve çalışma yerlerini gösteren kartlar.', 20)


def who_what_soru_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 25, 'Question 1 · Asking About a Person', MAVI, kalin=True)
    ic += yazi(149, 50, '“(1) ___ is in the office?”', LAC, kalin=True)
    ic += yazi(149, 74, 'Answer: “Mrs. Demir, the secretary.”', LAC)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'Question 2 · Asking About a Thing', YESIL_K, kalin=True)
    ic += yazi(451, 50, '“(2) ___ is that on the wall?”', LAC, kalin=True)
    ic += yazi(451, 74, 'Answer: “It is the notice board.”', LAC)
    return svg(600, 98, ic, 'Who ve What soru sözcüklerinin kullanıldığı iki diyalog kartı.', 20)


def tanisma_diyalogu_kartlari():
    kartlar = [
        ('Step 1 · Greeting', 'Hello! I am Deniz (5-A).', MAVI, MAVI_A),
        ('Step 2 · New Student', 'Nice to meet you! I am Mert.', YES, YES_A),
        ('Step 3 · Classmate', 'This is Ela, my classmate.', TUR, TUR_A),
        ('Step 4 · Question', 'Who is our English teacher?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Okulda yeni bir öğrenciyle tanışma adımlarını gösteren dört kart.', 20)


def dil_bilgisi_denetim_kartlari():
    satirlar = [
        ('Card 1', 'I am a student and Mr. Kaya is our basketball coach.', YES, YES_A),
        ('Card 2', 'There is an administration department next to the gate.', MAVI, MAVI_A),
        ('Card 3 (!)', 'The students is wearing an uniform in the school corridor.', KIR, KIR_A),
        ('Card 4', 'The conference hall is big and the library is very quiet.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 88, 22, renk, renk, 6, 1)
        ic += yazi(50, y + 15, no, '#fff', kalin=True)
        ic += yazi(104, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'a/an/the ve am/is/are kurallarını içeren dört cümle kartı.', 20)


def zamir_donusturme_karti():
    ic = kutu(6, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(149, 25, 'Sentence 1 · Singular Female', TUR, kalin=True)
    ic += yazi(149, 50, '[Mrs. Demir] is the secretary.', LAC, kalin=True)
    ic += yazi(149, 74, '→ ___ is in the administration dept.', TUR, kalin=True)

    ic += kutu(308, 6, 286, 86, MOR_A, MOR, 9, 1.4)
    ic += yazi(451, 25, 'Sentence 2 · Plural Places', MOR, kalin=True)
    ic += yazi(451, 50, '[The library and the lab] are big.', LAC, kalin=True)
    ic += yazi(451, 74, '→ ___ are upstairs on the 1st floor.', MOR, kalin=True)
    return svg(600, 98, ic, 'Özneleri kişi zamirlerine dönüştürme etkinliği kartı.', 20)


def okuma_metni_okulumuz_karti():
    ic = kutu(6, 6, 588, 88, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'READING TEXT · WELCOME TO ATATÜRK SECONDARY SCHOOL', '#fff', kalin=True)
    ic += yazi(300, 50, 'Our headmaster is Mr. Yılmaz. He is kind. The canteen is downstairs and clean.', LAC, kalin=True)
    ic += yazi(300, 74, 'Our coach, Mr. Kaya, trains the team in the sports field every afternoon. ↘', LAC)
    return svg(600, 100, ic, 'Atatürk Ortaokulunu tanıtan İngilizce okuma metni kartı.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = personel_kimlik_karti()
    s[4]['gorsel'] = okul_yerlesim_plani()
    s[5]['gorsel'] = dort_personel_gorev_kartlari()
    s[6]['gorsel'] = who_what_soru_karti()
    s[7]['gorsel'] = tanisma_diyalogu_kartlari()
    s[8]['gorsel'] = dil_bilgisi_denetim_kartlari()
    s[10]['gorsel'] = zamir_donusturme_karti()
    s[11]['gorsel'] = okuma_metni_okulumuz_karti()
