from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 1: SCHOOL LIFE — NATIONAL DAYS, CELEBRATIONS & REVISION', R['koyu']))

    # Sol panel: National & Religious Days in Türkiye
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. NATIONAL & RELIGIOUS DAYS (BAYRAMLAR)', R['koyu'], 13, 'bold', 'middle'))

    gunler = [
        (98, '29 October — Republic Day', '29 Ekim Cumhuriyet Bayramı (We celebrate Republic Day!)'),
        (146, '23 April — National Sovereignty & Children’s Day', '23 Nisan Ulusal Egemenlik ve Çocuk Bayramı'),
        (194, '19 May — Commemoration of Atatürk, Youth & Sports Day', '19 Mayıs Atatürk’ü Anma, Gençlik ve Spor Bayramı'),
        (242, '15 July & 30 August', '15 Temmuz Demokrasi Günü & 30 Ağustos Zafer Bayramı'),
        (290, 'Religious Days (Dini Bayramlarımız)', 'Ramadan Feast (Eid al-Fitr) & Sacrifice Feast (Eid al-Adha)'),
    ]
    for y, b, a in gunler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Theme 1 Grammar & Speaking Revision
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. THEME 1 COMPLETE REVISION', '#1e40af', 13, 'bold', 'middle'))

    tekrar = [
        (98, 'People & Places at School', 'headmaster, coach, librarian • lab, gym, canteen, library'),
        (146, 'Countries & Asking Origin', 'Where are you from? — I am from Türkiye / Azerbaijan / Japan.'),
        (194, 'School Clubs & Preferences (V-ing)', 'Which club are you in? — Do you like doing experiments?'),
        (242, 'School Rules (must / mustn’t / can’t)', 'We must wear a uniform. / We mustn’t run in the corridors.'),
        (290, 'Celebration Verbs (Kutlama Fiilleri)', 'celebrate • decorate the classroom • read poems • hang flags'),
    ]
    for y, b, a in tekrar:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'PREPOSITIONS OF TIME: ON + Gün/Tarih ("on 29 October", "on Monday")  |  IN + Ay/Mevsim ("in October", "in May")', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'HAPPY REPUBLIC DAY! — "We decorate our school with Turkish flags and sing the National Anthem on 29 October!"', '#334155', 11, 'normal', 'middle'))

    kaydet('5-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()
