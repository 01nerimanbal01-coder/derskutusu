from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'THEME 2: HOBBIES & SKILLS — PAST ABILITIES AND HABITS', R['koyu']))

    # Sol panel: Past Abilities: Could vs. Was/Were Able To
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. PAST ABILITIES: COULD vs. WAS/WERE ABLE TO', R['koyu'], 11.4, 'bold', 'middle'))

    sol = [
        (100, 'General Past Ability: COULD + V1', 'Geçmişteki genel yetenekler: “Mozart could play the piano when he was four.”'),
        (150, 'Specific Achievement: WAS/WERE ABLE TO + V1', 'Zor bir durumda tek seferlik başarı (= managed to): “She was able to win the tough match.”'),
        (200, 'Negative Form: COULDN’T = WASN’T ABLE TO', 'Olumsuz cümlede fark yoktur! Hem genel hem özel durumda “couldn’t” kullanılabilir.'),
        (250, 'Sense & Perception Verbs with COULD', 'See, hear, smell, taste, feel, remember, understand fiilleriyle özel durumda da “could” kullanılır.'),
        (300, 'Succeeded in + V-ing / Managed to + V1', '“He managed to fix the engine” = “He succeeded in fixing the engine” = “He was able to fix it.”'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.0, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Sağ panel: Past Habits & States: USED TO and DIY Vocabulary
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. PAST HABITS (USED TO) & DIY VOCABULARY', '#92400e', 11.4, 'bold', 'middle'))

    sag = [
        (100, 'Affirmative: USED TO + V1', 'Geçmişte yapılıp artık bırakılan alışkanlık/durum: “I used to collect stamps as a child.”'),
        (150, 'Negative: DIDN’T USE TO + V1', 'Dikkat: “didn’t” geldiğinde “d” düşer! “People didn’t use to have smartphones.”'),
        (200, 'Question: DID + Subject + USE TO + V1?', '“Where did you use to live before moving to Ankara?”'),
        (250, 'Compare: BE USED TO / GET USED TO + V-ing', 'Alışkın olmak / alışmak: “I am used to waking up early” (İsim veya V-ing alır!).'),
        (300, 'DIY (Do It Yourself) & Craft Vocabulary', 'Knitting, pottery, carpentry, origami, upcycling, screwdriver, drill, glue gun.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.0, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.0, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'GOLDEN RULE: Geçmişte tek seferlik zor bir durumu başarmada OLUMLU cümlede “could” DEĞİL, “was/were able to (managed to)” kullanılır!', R['koyu'], 9.6, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'Example: “The fire spread quickly, but everyone WAS ABLE TO escape safely.” (NOT: could escape)', '#334155', 10, 'normal', 'middle'))

    kaydet('11-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic