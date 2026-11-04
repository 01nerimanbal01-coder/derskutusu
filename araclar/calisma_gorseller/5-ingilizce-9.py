"""5. sınıf İngilizce 9. hafta (Asking For and Telling the Time, Daily School Routines, Present Simple &amp; Object Pronouns) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dijital_saat_kartlari():
    saatler = [
        ('1. Clock', '08:00', 'eight o’clock', MAVI, MAVI_A),
        ('2. Clock', '09:30', 'half past nine', YES, YES_A),
        ('3. Clock', '10:45', 'quarter past ten', KIR, KIR_A),
        ('4. Clock', '11:20', 'twenty past eleven', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, dij, okunus, r, z) in enumerate(saatler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 22, bas, 10.2, r)
        ic += yazi(x + 41, 45, dij, 12.0, LAC)
        ic += yazi(x + 41, 66, okunus, 8.9, LAC, ince=True)
    return svg(360, 86, ic, 'Dört dijital saat ve İngilizce okunuş kartı.', 15)


def ders_saat_cizelgesi():
    kartlar = [
        ('1. Maths', '08:30 · Mon', MAVI, MAVI_A),
        ('2. Science', '09:15 · Tue', YES, YES_A),
        ('3. English', '10:45 · Thu', TUR, TUR_A),
        ('4. Art', '01:00 · Fri', MOR, MOR_A),
    ]
    ic = ''
    for i, (ders, zaman, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, ders, 10.4, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, zaman, 9.8, LAC, ince=True)
    return svg(360, 84, ic, 'Dört dersin gün ve başlangıç saati kartları.', 15)


def zamir_eslestirme_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Subject → Object (Tekil)', 10.2, MAVI)
    ic += yazi(91, 44, 'I → me  |  She → her', 9.9, LAC, ince=True)
    ic += yazi(91, 65, 'He → [ K = ? ]', 10.2, MAVI)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'Subject → Object (Çoğul)', 10.2, MOR)
    ic += yazi(269, 44, 'We → us  |  You → you', 9.9, LAC, ince=True)
    ic += yazi(269, 65, 'They → [ L = ? ]', 10.2, MOR)
    return svg(360, 88, ic, 'Özne zamirleri ve nesne zamirleri eşleştirme şeması.', 15)


def mert_ece_diyalog_karti():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += yazi(16, 29, 'Mert:', 10.4, MAVI, 'start')
    ic += yazi(200, 29, '? (Double Science Lesson)', 10.2, LAC)

    ic += kutu(6, 50, 348, 38, YES_A, YES)
    ic += yazi(16, 73, 'Ece:', 10.4, YESIL_K, 'start')
    ic += yazi(200, 73, 'It starts at twenty past ten (10:20).', 10.2, LAC, ince=True)
    return svg(360, 94, ic, 'Mert ve Ece arasında ders başlama saati diyaloğu.', 16)


def iki_saat_soru_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Asking the Time', 10.3, TUR)
    ic += yazi(91, 44, 'Q: What time is it?', 9.9, LAC)
    ic += yazi(91, 65, 'Clock: [ 04:30 ] → It is ...', 9.7, TUR, ince=True)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 22, '2. Asking Routine Time', 10.3, CAM)
    ic += yazi(269, 44, 'Q: What time does Ali go home?', 9.5, LAC)
    ic += yazi(269, 65, 'Time: [ 03:15 ] → He goes ...', 9.7, CAM, ince=True)
    return svg(360, 88, ic, 'What time is it ve What time does sorularının karşılaştırılması.', 15)


def burak_sabah_rutini():
    kartlar = [
        ('A · 08:15', 'Arrive at school', TUR, TUR_A),
        ('B · 07:00', 'Wake up early', MAVI, MAVI_A),
        ('C · 12:00', 'Lunch at noon', MOR, MOR_A),
        ('D · 07:30', 'Have breakfast', YES, YES_A),
    ]
    ic = ''
    for i, (saat, eylem, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, saat, 10.3, r)
        ic += yazi(x + 41, 55, eylem, 9.3, LAC, ince=True)
    return svg(360, 84, ic, 'Okul günü sabah rutinlerini saatleriyle gösteren dört kart.', 15)


def sinif_panosu_duyurulari():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 21, 'Class 5-B Noticeboard (Sınıf Panosu)', 10.5, MAVI)
    ic += yazi(180, 41, '• Double Maths lessons: on Monday at quarter past nine (09:15).', 9.5, LAC, ince=True)
    ic += yazi(180, 58, '• Classroom Bookshelf: There are 56 (fifty-six) storybooks.', 9.5, LAC, ince=True)
    ic += yazi(180, 75, '• Rule: Put your rubbish in the rubbish bin! I.T. is on Friday at 10:00.', 9.5, YESIL_K)
    return svg(360, 92, ic, '5-B sınıf panosundaki ders, kitaplık ve kural duyuruları.', 16)


def borrow_lend_karsilastirma():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'BORROW (Ödünç Almak)', 10.2, YESIL_K)
    ic += yazi(91, 45, '“Can I borrow your pen?”', 9.9, LAC)
    ic += yazi(91, 65, '(Kalemini ödünç alabilir miyim?)', 9.1, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, 'LEND (Ödünç Vermek)', 10.2, MOR)
    ic += yazi(269, 45, '“Can you lend me your pen?”', 9.9, LAC)
    ic += yazi(269, 65, '(Bana kalemini ödünç verir misin?)', 9.1, LAC, ince=True)
    return svg(360, 88, ic, 'Borrow ve lend fiillerinin anlam ve kullanım karşılaştırması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dijital_saat_kartlari()
    s[2]['gorsel'] = ders_saat_cizelgesi()
    s[5]['gorsel'] = zamir_eslestirme_karti()
    s[6]['gorsel'] = mert_ece_diyalog_karti()
    s[7]['gorsel'] = iki_saat_soru_karti()
    s[8]['gorsel'] = burak_sabah_rutini()
    s[9]['gorsel'] = sinif_panosu_duyurulari()
    s[11]['gorsel'] = borrow_lend_karsilastirma()
