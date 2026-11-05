"""5. sınıf İngilizce 10. hafta (Theme 2: Classroom Life — School Subjects, Weekly Timetables, Classroom Objects & Present Simple) çalışma kâğıdı görselleri.
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


def dort_okul_dersi_kartlari():
    kartlar = [
        ('1. P.E.', 'Sports in gym', MAVI, MAVI_A),
        ('2. I.T.', 'Coding & PC', YES, YES_A),
        ('3. Art', 'Number problems', KIR, KIR_A),
        ('4. Science', 'Lab experiments', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 23, bas, 10.3, r)
        ic += f'<line x1="{x + 8}" y1="31" x2="{x + 74}" y2="31" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.1, LAC, ince=True)
    return svg(360, 86, ic, 'Dört okul dersi ve etkinlik eşleştirme kartı.', 15)


def sinif_envanteri_sayilar():
    kartlar = [
        ('1. Smartboard', 'Count: 1', MAVI, MAVI_A),
        ('2. Seats', 'Count: 28', YES, YES_A),
        ('3. Dictionaries', 'Count: 64', TUR, TUR_A),
        ('4. Storybooks', 'Count: 95', MOR, MOR_A),
    ]
    ic = ''
    for i, (esya, adet, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, esya, 9.8, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, adet, 10.2, LAC)
    return svg(360, 84, ic, 'Sınıftaki eşya sayılarını gösteren dört envanter kartı.', 15)


def persembe_ders_programi_karti():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += yazi(16, 29, 'Selin’s Question:', 10.2, MAVI, 'start')
    ic += yazi(220, 29, 'What time is the double I.T. class on Thursday?', 9.6, LAC)

    ic += kutu(6, 50, 348, 40, YES_A, YES)
    ic += yazi(16, 74, 'Thursday Timetable:', 10.2, YESIL_K, 'start')
    ic += yazi(235, 74, 'Double I.T. Lesson: [ 09:45 — 11:15 ]', 9.9, LAC)
    return svg(360, 96, ic, 'Perşembe günü blok Bilişim dersi başlangıç ve bitiş saati.', 16)


def sosyal_dil_diyalog_balonu():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'Emre (Needs Help)', 10.2, TUR)
    ic += yazi(91, 44, '“This Maths project is hard.', 9.4, LAC, ince=True)
    ic += yazi(91, 65, '[ I = ? ]”', 10.2, TUR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Derya (Accepts Happily)', 10.2, YESIL_K)
    ic += yazi(269, 44, '“Sure! [ II = ? ]', 9.6, LAC, ince=True)
    ic += yazi(269, 65, 'Let’s study together.”', 9.5, YESIL_K)
    return svg(360, 88, ic, 'Yardım isteme ve memnuniyetle kabul etme sosyal dil kartı.', 15)


def nesne_zamiri_cumle_kartlari():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Plural Object (They)', 10.1, MAVI)
    ic += yazi(91, 44, 'Where are my notebooks?', 9.5, LAC, ince=True)
    ic += yazi(91, 65, 'I can’t find [ ___ ].', 10.0, MAVI)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Female Object (She)', 10.1, MOR)
    ic += yazi(269, 44, 'Mrs. Aydın is speaking.', 9.5, LAC, ince=True)
    ic += yazi(269, 65, 'Please listen to [ ___ ].', 10.0, MOR)
    return svg(360, 88, ic, 'Çoğul ve tekil özneler için nesne zamiri tamamlama kartları.', 15)


def carsamba_program_akisi():
    kartlar = [
        ('A · 10:15', 'Morning break', TUR, TUR_A),
        ('B · 08:40', 'First lesson starts', MAVI, MAVI_A),
        ('C · 14:20', 'Last lesson finishes', MOR, MOR_A),
        ('D · 12:30', 'Lunch in hall', YES, YES_A),
    ]
    ic = ''
    for i, (saat, eylem, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, saat, 10.2, r)
        ic += yazi(x + 41, 55, eylem, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Çarşamba günü ders ve mola saatleri akış kartları.', 15)


def sinif_5c_kurallar_panosu():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 21, 'Class 5-C Timetable & Rules Board', 10.4, MAVI)
    ic += yazi(180, 40, '• Tuesday 09:00: Double Science lessons in the laboratory.', 9.5, LAC, ince=True)
    ic += yazi(180, 58, '• Rule: Walk slowly and don’t shout loudly! (84 dictionaries on shelf)', 9.4, LAC, ince=True)
    ic += yazi(180, 75, '• Friday Afternoon: Art lesson starts at quarter past एक (01:15).', 9.5, YESIL_K).replace('एक', 'one')
    return svg(360, 92, ic, '5-C sınıfı haftalık ders programı ve sınıf kuralları panosu.', 16)


def do_ve_does_saat_sorulari():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Question with DO (You/We)', 9.9, YESIL_K)
    ic += yazi(91, 44, 'What time do you have', 9.5, LAC, ince=True)
    ic += yazi(91, 64, 'English? → [ 10:15 · Tue ]', 9.6, YESIL_K)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 22, '2. Question with DOES (It)', 9.9, CAM)
    ic += yazi(269, 44, 'What time does the English', 9.5, LAC, ince=True)
    ic += yazi(269, 64, 'lesson start? → [ 10:15 · Tue ]', 9.6, CAM)
    return svg(360, 88, ic, 'What time do ve What time does soru kalıplarının karşılaştırılması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_okul_dersi_kartlari()
    s[2]['gorsel'] = sinif_envanteri_sayilar()
    s[5]['gorsel'] = persembe_ders_programi_karti()
    s[6]['gorsel'] = sosyal_dil_diyalog_balonu()
    s[7]['gorsel'] = nesne_zamiri_cumle_kartlari()
    s[8]['gorsel'] = carsamba_program_akisi()
    s[9]['gorsel'] = sinif_5c_kurallar_panosu()
    s[11]['gorsel'] = do_ve_does_saat_sorulari()
