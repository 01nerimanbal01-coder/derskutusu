from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 2: PLANS — FUTURE TENSES (BE GOING TO, WILL & PRESENT CONTINUOUS)', R['koyu']))

    # Sol panel: Be Going To vs. Will (Plans, Intentions & Predictions)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. BE GOING TO vs. WILL (FUTURE FORMS)', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'BE GOING TO + V₁ (am / is / are going to + V₁)', '1) Prior Plans & Intentions: “I am going to study medicine.”'),
        (150, 'Predictions with Present Evidence (Somut Kanıt!)', '“Look at those black clouds! It is going to rain.” (Gözle görülür kanıt).'),
        (200, 'WILL + V₁ (won’t + V₁) — Spontaneous Decisions', '1) Konuşma anında verilen kararlar: “The phone is ringing. I’ll answer it!”'),
        (250, 'Predictions Based on Opinion (Kişisel Tahmin)', 'think, believe, hope, expect, probably, maybe: “I think they will win.”'),
        (300, 'Promises, Offers, Threats & Refusals (Will)', '“I promise I won’t tell anyone.” | “I will help you with your bag.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Present Continuous for Future & Time Clauses
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. FIXED ARRANGEMENTS & FUTURE EXPRESSIONS', '#92400e', 11.8, 'bold', 'middle'))

    sag = [
        (100, 'Present Continuous (am/is/are + V-ing) for Future', 'Fixed personal arrangements (bilet alınmış, randevu/saat kesinleşmiş!).'),
        (150, 'Example of Fixed Arrangement', '“We are flying to London at 09:00 tomorrow morning. Here are our tickets!”'),
        (200, 'Present Simple for Timetables & Schedules', 'Uçak, tren, sinema, ders saatleri: “The train leaves at 18:45.”'),
        (250, 'Making Suggestions & Invitations for Plans', 'Shall we...? / Let’s + V₁ / Why don’t we...? / How about + V-ing?'),
        (300, 'Future Time Expressions (Zaman Zarfları)', 'tomorrow, next week/month/year, tonight, in two days, soon, in 2030.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'EXAM KEY: “I think / I hope / probably / maybe” -> WILL + V₁  |  “Look! / Watch out! / Have already decided” -> BE GOING TO + V₁!', R['koyu'], 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Time Clauses (when, after, before, as soon as, until): Yan cümlecikte ASLA will kullanılmaz, Present Simple kullanılır!', '#334155', 9.8, 'normal', 'middle'))

    kaydet('10-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
