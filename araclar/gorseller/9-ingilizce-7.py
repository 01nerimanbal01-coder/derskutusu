from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 2: CLASSROOM LIFE — SCHOOL SUBJECTS, TIMETABLES & PRESENT SIMPLE', R['koyu']))

    # Sol panel: School Subjects, Days & Time Prepositions
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SCHOOL SUBJECTS & TIME EXPRESSIONS', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Core School Subjects (Temel Dersler)', 'Maths, Physics, Chemistry, Biology, History, Geography, Literature, PE.'),
        (150, 'Telling the Time (Saatleri Söyleme)', '08:30 -> half past eight | 09:15 -> quarter past nine | 09:45 -> quarter to ten.'),
        (200, 'Prepositions of Time: IN / ON / AT', 'AT + clock time (at 8:30, at noon) | ON + days (on Monday) | IN + parts of day.'),
        (250, 'Asking About Timetables (Ders Programı)', '“When do you have Chemistry?” -> “We have Chemistry on Tuesday at 10:00.”'),
        (300, 'Expressing Likes & Preferences', '“My favourite subject is Biology.” | “I am good at Maths / interested in Art.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.2, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Sağ panel: Present Simple Tense & Adverbs of Frequency
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. PRESENT SIMPLE & ADVERBS OF FREQUENCY', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Affirmative (+): I/You/We/They V₁ | He/She/It V-s', '“I study every day.”  |  “She studies Physics on Mondays.” (-s / -es / -ies)'),
        (150, 'Negative (-): don’t + V₁  /  doesn’t + V₁', '“We don’t have school on Sunday.” | “He doesn’t like waking up early.”'),
        (200, 'Questions (?): Do I/you/we/they...? / Does he/she/it...?', '“Does Ece go to the lab on Friday?” -> “Yes, she does. / No, she doesn’t.”'),
        (250, 'Adverbs of Frequency (Sıklık Zarfları)', 'always (100%) > usually > often > sometimes > rarely/seldom > never (0%).'),
        (300, 'Word Order with Frequency Adverbs', 'Before main verb (“I always do homework”), AFTER am/is/are (“He is never late”)!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'GOLDEN RULE: After DOESN’T and DOES, always use the base form V₁ (drops -s!): “She doesn’t study” (NOT doesn’t studies)!', R['koyu'], 10.2, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'How often do you have PE? -> Twice a week (haftada iki kez) / On Mondays and Thursdays.', '#334155', 10, 'normal', 'middle'))

    kaydet('9-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
