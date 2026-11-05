"""8. sınıf İngilizce 12. hafta (On the Phone: Formal/Informal Calls, Purposes, 'Will' & Call Center) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def office_call_card():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'Secretary (Reception)', MAVI, kalin=True)
    ic += yazi(92, 54, '«I’m sorry, Mr. Parker is', LAC)
    ic += yazi(92, 76, 'in a meeting right now.', LAC)
    ic += yazi(92, 96, 'He is not available.»', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'Caller’s Decision (Will)', YES, kalin=True)
    ic += yazi(269, 56, '«OK, no problem!', LAC)
    ic += yazi(269, 82, '[ ? Spontaneous Decision ? ]»', YES, kalin=True)
    return svg(ic, 'Sekreter ve arayan kişi arasındaki telefon görüşmesi kartı.')


def phone_memo_note():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 22, 'PHONE MEMO — WHILE YOU WERE OUT', TUR, kalin=True)
    ic += yazi(180, 44, 'To: Mrs. Clara Green   |   From: Dr. Emily Watson', LAC, kalin=True)
    ic += yazi(180, 68, 'Message: Called to confirm Friday’s dentist appointment at 14:00.', LAC)
    ic += yazi(180, 92, 'Action: Please call back · Tel: 0555 418 90 23', MAVI, kalin=True)
    return svg(ic, 'Dr. Emily Watson tarafından bırakılan telefon notu (memo).')


def formal_informal_cards():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'FORMAL CALL (Polite)', MAVI, kalin=True)
    ic += yazi(92, 52, '• May I speak to ...?', LAC)
    ic += yazi(92, 74, '• Could you put me through?', LAC)
    ic += yazi(92, 95, '• Hold on a moment, please.', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic += yazi(269, 26, 'INFORMAL CALL (Friendly)', MOR, kalin=True)
    ic += yazi(269, 52, '• Hey buddy, what’s up?', LAC)
    ic += yazi(269, 74, '• Hang on a sec!', LAC)
    ic += yazi(269, 95, '• Is Kevin home?', MOR, kalin=True)
    return svg(ic, 'Resmî ve samimi telefon konuşması kalıpları karşılaştırması.')


def call_center_menu():
    kartlar = [
        (6, 6, 'Press 1 — Flights', 'Book or cancel a flight', MAVI, MAVI_A),
        (184, 6, 'Press 2 — Returns', 'Return damaged product', KIR, KIR_A),
        (6, 60, 'Press 3 — Store Info', 'Address & working hours', YES, YES_A),
        (184, 60, 'Press 4 — Careers', 'Job applications', TUR, TUR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Çağrı merkezi sesli yanıt menüsü tuşları.')


def smartphone_apps_card():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Bora’s App 1: Dictionary', YES, kalin=True)
    ic += yazi(92, 56, 'Purpose (to + V1):', LAC)
    ic += yazi(92, 82, 'to practice English words', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 26, 'Bora’s App 2: Maps & GPS', CAM, kalin=True)
    ic += yazi(269, 56, 'Purpose (to + V1):', LAC)
    ic += yazi(269, 82, 'to find his way in the city', CAM, kalin=True)
    return svg(ic, 'Bora’nın akıllı telefon uygulama kullanım amaçları.')


def hospital_call_steps():
    adimlar = [
        (6, '1. Greeting', 'Green Valley Hospital', MAVI, MAVI_A),
        (94, '2. Request', 'Put me through...', YES, YES_A),
        (182, '3. Line Busy', 'Leave a message?', TUR, TUR_A),
        (270, '4. Message', 'Sinan called!', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Hastane sekreteriyle yapılan dört adımlı telefon diyaloğu.')


def teen_survey_chart():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Smartphone Usage Survey Among 100 Teens (%)', LAC, kalin=True)
    barlar = [
        (14, '40%', 'Homework', YES, YES_A),
        (98, '30%', 'Chat/Friends', MAVI, MAVI_A),
        (182, '20%', 'Mobile Games', TUR, TUR_A),
        (266, '10%', 'Shopping', MOR, MOR_A),
    ]
    for x, yuzde, et, r, z in barlar:
        ic += kutu(x, 34, 78, 66, z, r)
        ic += yazi(x + 39, 58, yuzde, r, kalin=True)
        ic += yazi(x + 39, 84, et, LAC, kalin=True)
    return svg(ic, 'Gençlerin akıllı telefon kullanım amaçlarını gösteren anket grafiği.')


def communication_choice_card():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 26, 'Face-to-Face Talk', YES, kalin=True)
    ic += yazi(92, 54, '• Warm and sincere', LAC)
    ic += yazi(92, 80, '• Clear body language', YES, kalin=True)
    ic += kutu(184, 6, 170, 103, MAVI_A, MAVI)
    ic += yazi(269, 26, 'Texting (SMS / Chat)', MAVI, kalin=True)
    ic += yazi(269, 54, '• Fast, cheap and easy', LAC)
    ic += yazi(269, 80, '• Send photos & emojis', MAVI, kalin=True)
    return svg(ic, 'Yüz yüze iletişim ve mesajlaşma tercih nedenleri kartı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = office_call_card()
    s[2]['gorsel'] = phone_memo_note()
    s[5]['gorsel'] = formal_informal_cards()
    s[6]['gorsel'] = call_center_menu()
    s[7]['gorsel'] = smartphone_apps_card()
    s[8]['gorsel'] = hospital_call_steps()
    s[9]['gorsel'] = teen_survey_chart()
    s[11]['gorsel'] = communication_choice_card()
