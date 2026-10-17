from _taban import Primitifler, renkler, kaydet


def ciz():
    P = Primitifler()
    R = renkler('ingilizce')
    ic = []
    ic.append(P.baslik(400, 32, 'UNIT 3: IN THE KITCHEN — COOKING PROCESSES, TOOLS & PREFERENCES', R['koyu']))

    # Sol panel: Cooking Methods & Preparation Verbs
    ic.append(P.kutu(20, 56, 365, 290, R['acik'], R['orta']))
    ic.append(P.metin(202, 80, '1. COOKING METHODS & PREPARATION VERBS', R['koyu'], 12, 'bold', 'middle'))

    sol = [
        (100, 'Cooking Methods (How do you cook it?)', 'boil (water), fry (hot oil), bake/roast (oven), grill, steam.'),
        (150, 'Cutting & Preparing Verbs', 'peel (kabuk soymak), chop / dice / slice (doğramak/dilimlemek).'),
        (200, 'Mixing & Dough Verbs', 'grate (rendelemek), mash (ezmek), knead (yoğurmak),whisk (çırpmak).'),
        (250, 'Adding & Serving Verbs', 'pour (dökmek), sprinkle (serpmek), spread (sürmek), serve (servis).'),
        (300, 'Kitchen Tools (Utensils)', 'grater, peeler, knife, chopping board, saucepan, frying pan, bowl.'),
    ]
    for y, b, a in sol:
        ic.append(P.kutu(35, y, 335, 42, '#ffffff', R['orta']))
        ic.append(P.metin(202, y + 16, b, R['koyu'], 10.5, 'bold', 'middle'))
        ic.append(P.metin(202, y + 32, a, '#334155', 9.5, 'normal', 'middle'))

    # Sağ panel: Sequence Linkers & Tastes / Preferences
    ic.append(P.kutu(400, 56, 380, 290, '#fef3c7', '#d97706'))
    ic.append(P.metin(590, 80, '2. SEQUENCE LINKERS & FOOD PREFERENCES', '#92400e', 12, 'bold', 'middle'))

    sag = [
        (100, 'Sequence Linkers (Describing a Recipe Step by Step)', 'FIRST (İlk) -> SECOND -> NEXT / THEN -> AFTER THAT -> FINALLY (Son)!'),
        (150, 'Before / After / Until / When', 'Bake it UNTIL it turns golden brown. / Wash hands BEFORE cooking.'),
        (200, 'Tastes & Textures (How does it taste?)', 'sweet (tatlı), sour (ekşi), spicy/chili (baharatlı/acı), salty, greasy.'),
        (250, 'Asking About Ingredients vs. Recipe', 'What are the ingredients? (İçindekiler) vs. How do you make it?'),
        (300, 'Expressing Preferences (Prefer ... to ...)', 'I prefer steamed vegetables TO fried food because it is healthier.'),
    ]
    for y, b, a in sag:
        ic.append(P.kutu(415, y, 350, 42, '#ffffff', '#d97706'))
        ic.append(P.metin(590, y + 16, b, '#92400e', 10.2, 'bold', 'middle'))
        ic.append(P.metin(590, y + 32, a, '#334155', 9.2, 'normal', 'middle'))

    # Alt bant
    ic.append(P.kutu(20, 360, 760, 48, '#f0fdf4', R['orta']))
    ic.append(P.metin(400, 380, 'LGS RECIPE TIP: Always check FIRST (step 1) and FINALLY (last step) when ordering mixed recipe sentences!', R['koyu'], 10.5, 'bold', 'middle'))
    ic.append(P.metin(400, 398, 'boil -> in hot water (saucepan/pot) | fry -> in hot oil (frying pan) | bake/roast -> in the oven (baking tray)!', '#334155', 10.5, 'normal', 'middle'))

    kaydet('8-ingilizce-7.svg', P.sar(ic))


if __name__ == '__main__':
    ciz()


def uygula(v):
    from _taban import SON_SVG
    SON_SVG.clear()
    ciz()
    svg_ic = SON_SVG.get('_son')
    if svg_ic and v.get('bolumler'):
        v['bolumler'][0]['gorsel'] = svg_ic
