from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 3: HUMAN RIGHTS — EQUALITY, PURPOSE & MOTTOS', R['koyu']))

    # Sol panel: Human Rights Vocabulary & Core Concepts
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. HUMAN RIGHTS VOCABULARY & MOTTOS', R['koyu'], 13, 'bold', 'middle'))
    kelimeler = [
        (98, 'Universal Declaration of Human Rights (1948)', 'Evrensel İnsan Hakları Bildirgesi (dignity, equality, justice)'),
        (146, 'Positive Concepts (Olumlu Kavramlar)', 'freedom of speech • gender equality • tolerance • conscience'),
        (194, 'Violations & Problems (Hak İhlalleri)', 'racism • discrimination • prejudice • inequality • exploitation'),
        (242, 'Disadvantaged Groups (Dezavantajlı Gruplar)', 'refugees • disabled / physically challenged • minority groups'),
        (290, 'Writing a Human Rights Motto (Slogan)', '"All human beings are born free and equal in dignity!"'),
    ]
    for y, b, a in kelimeler:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 11, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Sağ panel: Expressing Purpose & Cause-Effect Connectors
    ic.append(P.kutu(400, 56, 380, 290, '#eff6ff', '#2563eb'))
    ic.append(P.metin(590, 80, '2. EXPRESSING PURPOSE & ARGUMENTATIVE ESSAY', '#1e40af', 13, 'bold', 'middle'))
    yapilar = [
        (98, 'to / in order (not) to / so as (not) to + V1', 'We must pass strict laws in order to prevent discrimination.'),
        (146, 'so that / in order that + S + can/will/could + V1', 'Accessible ramps are built so that disabled people can move.'),
        (194, 'for + Noun / V-ing (İsim veya İsim-Fiil ile Amaç)', 'NGOs work tirelessly for the protection of human rights.'),
        (242, 'Supporting Ideas & Giving Examples', 'First of all • Furthermore • For instance • Consequently'),
        (290, 'Expressing Obligation & Necessity', 'Every citizen should / must / ought to respect others’ rights.'),
    ]
    for y, b, a in yapilar:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#2563eb'))
        ic.append(P.metin(590, y + 16, b, '#1e40af', 11, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 10, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#fef3c7', '#d97706'))
    ic.append(P.metin(400, 380, 'GRAMMAR TIP: "in order to / so as to + V1 (Fiil Yalın)"  vs.  "so that / in order that + Subject + Modal + V1 (Tam Cümle)"', '#92400e', 11, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'MOTTO EXAMPLE: "Treat others the way you want to be treated — No one is free until everyone is free!"', '#334155', 11, 'normal', 'middle'))

    kaydet('12-ingilizce-6.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
