from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 1: SCHOOL LIFE — NATIONAL DAYS, ROUTINES & TENSE REVISION', R['koyu']))

    # Sol panel: Simple Present (Routines) vs. Present Continuous (Now / Celebrations)
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SIMPLE PRESENT vs. PRESENT CONTINUOUS', R['koyu'], 13, 'bold', 'middle'))

    sol = [
        (100, 'Simple Present Tense (Geniş Zaman — Rutinler)', 'I/You/We/They + V1  |  He/She/It + V-s/es/ies'),
        (148, 'Rutin Zaman İfadeleri (Time Expressions)', 'every day • always • usually • often • on Mondays'),
        (196, 'Örnek (School Routine)', '"We celebrate Republic Day on 29 October every year."'),
        (244, 'Present Continuous Tense (Şimdiki Zaman — Şu An)', 'am / is / are + V-ing (now, right now, at the moment, today)'),
        (292, 'Örnek (Ongoing Celebration)', '"Look! The students are decorating the school with flags now!"'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 40, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 15, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: National Days, School Roles & Responsibilities
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. NATIONAL DAYS & RESPONSIBILITIES', '#1e40af', 13, 'bold', 'middle'))

    sag = [
        (100, 'National Days in Türkiye', '29 October Republic Day • 23 April • 19 May • 15 July • 30 August'),
        (148, 'Celebration Vocabulary', 'enthusiastically (coşkuyla) • parade (geçit töreni) • folk dance'),
        (196, 'Roles at School (Okuldaki Görevliler)', 'headmaster (manage) • teacher (teach) • counselor (guide)'),
        (244, 'Student Responsibilities (must / have to)', 'keep the school clean • obey the rules • attend classes on time'),
        (292, 'Question Words Revision', 'What time • How often • Who • Where • What is she doing now?'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 40, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 15, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 31, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'KEY DIFFERENCE: "every year / usually" → V1 / V-s (celebrate/celebrates)  |  "now / Look! / today" → am/is/are + V-ing (is celebrating)!', '#92400e', 10, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Happy 29 October Republic Day! — "Today is 29 October, and we are celebrating Republic Day enthusiastically!"', '#334155', 11, 'normal', 'middle'))

    kaydet('6-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
