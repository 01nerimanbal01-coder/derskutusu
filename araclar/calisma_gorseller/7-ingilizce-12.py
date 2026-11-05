"""7. sınıf İngilizce 12. hafta (Wild Animals: Frequency, Habitats, should/shouldn't & Protecting Wildlife) görselleri.
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


def animal_profile_card():
    ic = kutu(6, 6, 348, 103, TUR_A, TUR)
    ic += yazi(180, 24, 'ANIMAL PROFILE CARD — Mystery Wild Animal', TUR, kalin=True)
    ic += yazi(180, 48, 'Class: Bird of Prey · Habitat: High Mountains & Cliffs', LAC, kalin=True)
    ic += yazi(180, 72, 'Body Parts: Large wings, hooked beak, sharp claws (talons)', LAC)
    ic += yazi(180, 95, 'Diet: Carnivore — It always hunts small animals from the sky.', MAVI, kalin=True)
    return svg(ic, 'Yüksek dağlarda yaşayan yırtıcı kartal tanıtım kartı.')


def four_habitats_table():
    kartlar = [
        (6, 6, '1. Bengal Tiger', 'Jungle · Carnivore', TUR, TUR_A),
        (184, 6, '2. Camel', 'Hot Desert · Herbivore', YES, YES_A),
        (6, 60, '3. Green Sea Turtle', 'Ocean · Reptile', CAM, CAM_A),
        (184, 60, '4. Polar Bear', 'Arctic Ice · Carnivore', MAVI, MAVI_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört vahşi hayvanın yaşam alanı ve beslenme türü kartları.')


def frequency_chart_card():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 24, 'Frequency Adverbs', MAVI, kalin=True)
    ic += yazi(92, 48, 'Always: 100% · Usually: 80%', LAC)
    ic += yazi(92, 70, 'Sometimes: 40% · Rarely: 15%', LAC)
    ic += yazi(92, 92, 'Never: 0%', KIR, kalin=True)
    ic += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic += yazi(269, 24, 'Owl (Baykuş) Habits', MOR, kalin=True)
    ic += yazi(269, 52, 'Hunt at night: 85% (Usually)', YES, kalin=True)
    ic += yazi(269, 80, 'Eat grass/fruit: 0% (Never)', KIR, kalin=True)
    return svg(ic, 'Sıklık zarfları yüzdeleri ve baykuşun beslenme alışkanlığı kartı.')


def protect_wildlife_poster():
    ic = kutu(6, 6, 172, 103, KIR_A, KIR)
    ic += yazi(92, 26, 'WE SHOULDN’T (-)', KIR, kalin=True)
    ic += yazi(92, 54, '• Hunt animals for fur/tusks', LAC)
    ic += yazi(92, 78, '• Pollute seas and rivers', LAC)
    ic += yazi(92, 98, '• Cut down bamboo trees', LAC)
    ic += kutu(184, 6, 170, 103, YES_A, YES)
    ic += yazi(269, 26, 'WE SHOULD (+)', YES, kalin=True)
    ic += yazi(269, 54, '• Keep wildlife habitats safe', LAC)
    ic += yazi(269, 78, '• Stop illegal poaching', LAC)
    ic += yazi(269, 98, '• [ ? Rule Box ? ]', YES, kalin=True)
    return svg(ic, 'Vahşi yaşamı koruma should ve shouldnt posteri.')


def dodo_extinct_card():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 26, 'EXTINCT SPECIES FILE: The Dodo Bird (Mauritius Island)', MOR, kalin=True)
    ic += yazi(180, 52, 'Height: ~1 meter · Feature: Flightless bird (could not fly)', LAC)
    ic += yazi(180, 76, 'Extinction Date: 1681 · Cause: Sailors overhunted them', KIR, kalin=True)
    ic += yazi(180, 96, 'and destroyed their forest habitats on the island.', LAC, kalin=True)
    return svg(ic, 'Nesli tükenen Dodo kuşu bilgi kartı.')


def interview_steps_card():
    adimlar = [
        (6, '1. Reporter', 'Which animal?', MAVI, MAVI_A),
        (94, '2. Biologist', 'Giant Pandas!', YES, YES_A),
        (182, '3. Reporter', 'Why endangered?', TUR, TUR_A),
        (270, '4. Biologist', 'Habitat loss!', KIR, KIR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Dev pandalar hakkında dört adımlı belgesel röportajı akışı.')


def threat_chart_card():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Endangered Species Threat Chart (%)', LAC, kalin=True)
    ic += kutu(14, 34, 80, 66, KIR_A, KIR)
    ic += yazi(54, 58, '50%', KIR, kalin=True)
    ic += yazi(54, 82, 'Habitat Loss', LAC, kalin=True)
    ic += kutu(100, 34, 80, 66, TUR_A, TUR)
    ic += yazi(140, 58, '30%', TUR, kalin=True)
    ic += yazi(140, 82, 'Overhunting', LAC)
    ic += kutu(186, 34, 80, 66, MAVI_A, MAVI)
    ic += yazi(226, 58, '12%', MAVI, kalin=True)
    ic += yazi(226, 82, 'Pollution', LAC)
    ic += kutu(272, 34, 74, 66, MOR_A, MOR)
    ic += yazi(309, 58, '8%', MOR, kalin=True)
    ic += yazi(309, 82, 'Climate', LAC)
    return svg(ic, 'Nesli tehlike altındaki türleri tehdit eden etkenlerin yüzde grafiği.')


def save_turtles_card():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 26, 'CAMPAIGN: Save the Mediterranean Sea Turtles (Caretta Caretta)!', CAM, kalin=True)
    ic += yazi(180, 54, '(+) Positive Action: Keep sandy beaches clean & protect nests.', YES, kalin=True)
    ic += yazi(180, 82, '(-) Negative Action: Throw plastic bags into the sea.', KIR, kalin=True)
    return svg(ic, 'Deniz kaplumbağalarını koruma kampanyası bilgi kartı.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = animal_profile_card()
    s[2]['gorsel'] = four_habitats_table()
    s[5]['gorsel'] = frequency_chart_card()
    s[6]['gorsel'] = protect_wildlife_poster()
    s[7]['gorsel'] = dodo_extinct_card()
    s[8]['gorsel'] = interview_steps_card()
    s[9]['gorsel'] = threat_chart_card()
    s[11]['gorsel'] = save_turtles_card()
