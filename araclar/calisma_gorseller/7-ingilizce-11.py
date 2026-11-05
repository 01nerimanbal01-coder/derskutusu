"""7. sınıf İngilizce 11. hafta (Unit 3: Biographies — Time Expressions, Conjunctions &amp; Biography Reports) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px, max-height 21-22mm."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def feza_gursey_timeline():
    adimlar = [
        (6, '1921 · Birth', 'İstanbul', 'Apr 7, 1921', MAVI, MAVI_A),
        (110, '1944 · Univ.', 'Graduated', 'İstanbul Univ.', YES, YES_A),
        (214, '1950 · PhD', 'Moved to', 'London (UK)', TUR, TUR_A),
        (318, '1986 · Award', 'Wigner', 'Medal', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, b3, r, z in adimlar:
        ic += kutu(x, 6, 96, 84, z, r)
        ic += yazi(x + 48, 25, b1, r, kalin=True)
        ic += yazi(x + 48, 52, b2, LAC)
        ic += yazi(x + 48, 75, b3, r, kalin=True)
    return svg(420, 96, ic, 'Feza Gürsey kronolojik yaşam çizelgesi kartları.', 21)


def time_conjunction_board():
    kartlar = [
        (6, 6, '1. in + year', 'in 1938', MAVI, MAVI_A),
        (214, 6, '2. on + date', 'Oct 29, 1923', YES, YES_A),
        (6, 54, '3. ... + ago', '10 years + ?', TUR, TUR_A),
        (214, 54, '4. to + V1', 'to study medicine', MOR, MOR_A),
    ]
    ic = ''
    for x, y, kural, ornek, r, z in kartlar:
        ic += kutu(x, y, 200, 42, z, r)
        ic += yazi(x + 100, y + 18, kural, r, kalin=True)
        ic += yazi(x + 100, y + 36, ornek, LAC)
    return svg(420, 102, ic, 'Zaman edatları ve amaç mastarı özet kartları.', 22)


def interview_card_remziye():
    ic = kutu(6, 6, 408, 38, MAVI_A, MAVI)
    ic += yazi(18, 30, 'Seda:  « ......................... ? »', MAVI, 'start', True)
    ic += kutu(6, 50, 408, 42, YES_A, YES)
    ic += yazi(18, 69, 'Mert: «She moved to Paris in 1920', LAC, 'start')
    ic += yazi(18, 86, 'to study chemistry at Sorbonne University.»', YES, 'start', True)
    return svg(420, 98, ic, 'Remziye Hisar’ın Paris’e taşınma amacını anlatan diyalog kartı.', 21)


def cause_result_puzzle():
    ic = kutu(6, 6, 200, 84, TUR_A, TUR)
    ic += yazi(106, 25, 'CAUSE (Sebep)', TUR, kalin=True)
    ic += yazi(106, 51, 'Hulusi Behçet researched', LAC)
    ic += yazi(106, 73, 'for many years.', LAC)

    ic += kutu(214, 6, 200, 84, YES_A, YES)
    ic += yazi(314, 25, 'RESULT (Sonuç)', YES, kalin=True)
    ic += yazi(314, 51, 'He discovered Behçet’s', LAC)
    ic += yazi(314, 73, 'Disease in 1937.', YES, kalin=True)
    return svg(420, 96, ic, 'Hulusi Behçet sebep ve sonuç cümle birleştirme kartı.', 21)


def biography_notes_vecihi():
    ic = kutu(6, 6, 200, 84, CAM_A, CAM)
    ic += yazi(106, 25, 'Vecihi Hürkuş · Birth', CAM, kalin=True)
    ic += yazi(106, 52, 'Date: January 6, 1896', LAC)
    ic += yazi(106, 75, 'City: İstanbul', CAM, kalin=True)

    ic += kutu(214, 6, 200, 84, MOR_A, MOR)
    ic += yazi(314, 25, 'Milestone · 1924', MOR, kalin=True)
    ic += yazi(314, 52, 'Action: build (V2: built)', LAC)
    ic += yazi(314, 75, 'the first Turkish plane', MOR, kalin=True)
    return svg(420, 96, ic, 'Vecihi Hürkuş doğum ve ilk Türk uçağı başarı kartı.', 21)


def bio_report_plan():
    adimlar = [
        (6, '1. Birth', 'Samarkand', MAVI, MAVI_A),
        (110, '2. Youth', 'Astronomy', YES, YES_A),
        (214, '3. Move', 'To İstanbul', TUR, TUR_A),
        (318, '4. 1474', 'Sahn-ı Seman', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 96, 84, z, r)
        ic += yazi(x + 48, 30, b1, r, kalin=True)
        ic += yazi(x + 48, 66, b2, LAC)
    return svg(420, 96, ic, 'Ali Kuşçu kronolojik biyografi raporu aşamaları.', 21)


def two_inventors_table():
    ic = kutu(6, 6, 200, 86, MAVI_A, MAVI)
    ic += yazi(106, 24, 'Guglielmo Marconi', MAVI, kalin=True)
    ic += yazi(106, 46, 'Born: 1874, Italy', LAC)
    ic += yazi(106, 66, 'Invented: Radio', LAC)
    ic += yazi(106, 84, 'Nobel Physics: 1909', MAVI, kalin=True)

    ic += kutu(214, 6, 200, 86, YES_A, YES)
    ic += yazi(314, 24, 'John Logie Baird', YES, kalin=True)
    ic += yazi(314, 46, 'Born: 1888, Scotland', LAC)
    ic += yazi(314, 66, 'Invented: Television', LAC)
    ic += yazi(314, 84, 'Died: 1946 (No Nobel)', YES, kalin=True)
    return svg(420, 98, ic, 'Marconi ve Baird biyografi karşılaştırma kartları.', 21)


def error_hunter_bio():
    ic = kutu(6, 6, 408, 40, KIR_A, KIR)
    ic += yazi(18, 31, '1)  Sinan was born in May 12, 1995.   (✗)', KIR, 'start', True)
    ic += kutu(6, 52, 408, 40, TUR_A, TUR)
    ic += yazi(18, 77, '2)  Elif graduated university ago two years.   (✗)', TUR, 'start', True)
    return svg(420, 98, ic, 'Zaman edatı ve zarf hatası içeren iki İngilizce cümle kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = feza_gursey_timeline()
    s[2]['gorsel'] = time_conjunction_board()
    s[5]['gorsel'] = interview_card_remziye()
    s[6]['gorsel'] = cause_result_puzzle()
    s[7]['gorsel'] = biography_notes_vecihi()
    s[8]['gorsel'] = bio_report_plan()
    s[9]['gorsel'] = two_inventors_table()
    s[11]['gorsel'] = error_hunter_bio()
