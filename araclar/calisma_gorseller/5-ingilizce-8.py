"""5. sınıf İngilizce 8. hafta (Classroom Rules, School Subjects, Days of the Week and Timetables) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def ders_programi_karti():
    kutular = [
        ('1. Preposition', 'We have P.E.', 'K = ?  Monday.', MAVI, MAVI_A),
        ('2. Numbers', 'I like solving', 'problems in L = ?', TUR, TUR_A),
        ('3. Drawing', 'She loves painting', 'pictures in M = ?', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 25, bas, renk, kalin=True)
        ic += yazi(x + 56, 52, s1, LAC)
        ic += yazi(x + 56, 76, s2, LAC, kalin=True)
    return svg(360, 100, ic, 'Ders programı tamamlama kartları: K edatı, L sayı dersi ve M resim dersi.', 21)


def sinif_kurallari_panosu():
    kurallar = [
        ('1. Raise your hand', 'before speaking!', MAVI, MAVI_A),
        ('2. Keep classroom', 'clean and tidy!', YES, YES_A),
        ('3. Don’t eat food', 'or shout in class!', KIR, '#fdeaea'),
        ('4. Don’t run fast', 'in the corridors!', TUR, TUR_A),
    ]
    ic = ''
    for i, (s1, s2, renk, arka) in enumerate(kurallar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, s1, renk, kalin=True)
        ic += yazi(x + 86, y + 37, s2, LAC)
    return svg(360, 106, ic, 'Sınıf kuralları panosu: parmak kaldırma, temiz tutma, sınıfta yememe ve koridorda koşmama.', 21)


def dort_ogrenci_ders_karti():
    kartlar = [
        ('1. Arda', 'Numbers', 'Monday', MAVI, MAVI_A),
        ('2. Selin', 'Experiments', 'Tuesday', YES, YES_A),
        ('3. Bora', 'Guitar', 'Wednesday', TUR, TUR_A),
        ('4. Elif', 'Basketball', 'Friday', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, etk, gun, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 24, ad, renk, kalin=True)
        ic += yazi(x + 41, 50, etk, LAC)
        ic += yazi(x + 41, 74, gun, LAC, kalin=True)
    return svg(360, 98, ic, 'Arda, Selin, Bora ve Elif’in sevdiği etkinlikler ve ders günleri.', 21)


def izin_isteme_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 25, '1. Asking Permission', MAVI, kalin=True)
    ic += yazi(91, 52, 'knocking on the door:', LAC)
    ic += yazi(91, 76, '“May I ... , teacher?”', LAC, kalin=True)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(269, 25, '2. Teacher’s Answer', YESIL_K, kalin=True)
    ic += yazi(269, 52, 'Giving permission:', LAC)
    ic += yazi(269, 76, '“Yes, you ... / Sure.”', LAC, kalin=True)
    return svg(360, 100, ic, 'Öğrencinin içeri girme izni istemesi ve öğretmenin olumlu yanıtı kartı.', 21)


def hafta_ici_gunler_zinciri():
    gunler = [
        ('Monday', '1st Day', MAVI, MAVI_A),
        ('Tuesday', '2nd Day', YES, YES_A),
        ('Thursday', '4th Day', TUR, TUR_A),
        ('Friday', '5th Day', MOR, MOR_A),
    ]
    ic = ''
    for i, (gun, sira, renk, arka) in enumerate(gunler):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 30, gun, renk, kalin=True)
        ic += yazi(x + 41, 64, sira, LAC)
    return svg(360, 96, ic, 'Hafta içi günler sıralama kartları: Monday, Tuesday, Thursday, Friday.', 21)


def begeni_tablosu_svg():
    satirlar = [
        ('Tuna', 'Likes: Maths', 'Dislikes: Art', MAVI, MAVI_A),
        ('Merve', 'Likes: English', 'Dislikes: P.E.', YES, YES_A),
        ('Can', 'Likes: Science', 'Dislikes: Music', TUR, TUR_A),
        ('Duru', 'Likes: Music', 'Dislikes: Maths', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, sev, sevmez, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 10, y + 19, f'{ad} · {sev}', renk, 'start', kalin=True)
        ic += yazi(x + 10, y + 37, sevmez, LAC, 'start')
    return svg(360, 106, ic, 'Tuna, Merve, Can ve Duru’nun sevdiği ve sevmediği dersler tablosu.', 21)


def ders_gunu_diyalog_karti():
    ic = f'<rect x="6" y="6" width="348" height="42" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(16, 31, 'Student A:  _________________________ ?', MAVI, 'start', kalin=True)

    ic += f'<rect x="6" y="54" width="348" height="42" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(16, 79, 'Student B:  We have Science on Tuesday and Thursday.', LAC, 'start', kalin=True)
    return svg(360, 102, ic, 'Fen bilimleri dersinin hangi günler olduğunu soran diyalog kartı.', 21)


def zeynep_favori_ders_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.5"/>'
    ic += yazi(180, 26, 'STUDENT TIMETABLE CARD · ZEYNEP', MOR, kalin=True)
    ic += yazi(180, 52, 'Favourite Subject: English', LAC, kalin=True)
    ic += yazi(180, 76, 'Days: Wednesday and Friday', LAC)
    return svg(360, 100, ic, 'Zeynep’in en sevdiği ders (English) ve günleri (Wednesday, Friday) kartı.', 21)


def odunc_isteme_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(180, 26, 'IN THE MATHS LESSON · POLITE REQUEST', TUR, kalin=True)
    ic += yazi(180, 52, 'Emre: “I need to draw a straight line.', LAC)
    ic += yazi(180, 76, 'Can I borrow your ruler, please?”', LAC, kalin=True)
    return svg(360, 100, ic, 'Emre’nin matematik dersinde düz çizgi çizmek için cetvel isteme kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ders_programi_karti()
    s[4]['gorsel'] = sinif_kurallari_panosu()
    s[5]['gorsel'] = dort_ogrenci_ders_karti()
    s[6]['gorsel'] = izin_isteme_karti()
    s[7]['gorsel'] = hafta_ici_gunler_zinciri()
    s[8]['gorsel'] = begeni_tablosu_svg()
    s[9]['gorsel'] = ders_gunu_diyalog_karti()
    s[11]['gorsel'] = zeynep_favori_ders_karti()
    s[12]['gorsel'] = odunc_isteme_karti()
