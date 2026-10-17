from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'UNIT 2: SPORTS — ROUTINES, EQUIPMENT & ATHLETE BIOGRAPHIES', R['koyu']))

    # Sol panel: Talking About Sports Routines & Frequency
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. SPORTS ROUTINES & FREQUENCY QUESTIONS', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'How often do you go on a diet / train?', 'I never go on a diet, but I always eat healthy food.'),
        (150, 'Adverbs of Frequency (100% -> 0%)', 'always > usually > often > sometimes > rarely/seldom > never.'),
        (200, 'Time Expressions (At the end of sentences)', 'once a day, twice a week, three times a month, every morning.'),
        (250, 'PLAY / GO / DO Rules in Sports', 'PLAY: ball/team sports | GO: -ing sports | DO: individual/martial.'),
        (300, 'Why do you prefer individual sports?', 'Because they are more relaxing and I can train on my own.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Sports Equipment, Places & Athlete Profiles
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. EQUIPMENT, SCORE & ATHLETE PROFILES', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Sports Equipment (What do you need?)', 'Archery: bow & arrow | Tennis: racket & ball |Swimming: goggles.'),
        (150, 'More Equipment Vocabulary', 'Skating: helmet & knee pads | Climbing: rope | Boxing: gloves.'),
        (200, 'Match Results & Scores', 'win (kazanmak) / beat (yenmek) / lose (kaybetmek) / draw (berabere).'),
        (250, 'Asking About the Score', '"What is the score?" -> "It is 2-2 (two all). It is a draw (tie)!"'),
        (300, 'Reading Athlete Profiles (Mete Gazoz / Busenaz)', 'Trains 6 hours a day -> wakes up early -> wins gold medals!'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.5, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'KEY DIFFERENCE: "WIN a match / a medal / a cup" vs. "BEAT an opponent / the other team"!', R['koyu'], 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Spectators = Seyirciler | Opponent = Rakip | Medal = Madalya | Train / Work out = Antrenman yapmak | Go on a diet = Diyet yapmak.', '#334155', 10, 'normal', 'middle'))

    kaydet('7-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
