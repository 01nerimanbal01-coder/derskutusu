"""8. sınıf İngilizce 9. hafta (Unit 3: In the Kitchen — Describing Simple Processes &amp; Recipes) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def omlet_baglac_karti():
    """Soru 2 (s[1]): Sebzeli omlet tarifinde (I) First ve (II) Finally boşlukları."""
    adimlar = [
        (4, 4, 'Step 1 · (I) ___', 'Put some oil into the pan', MAVI, MAVI_A),
        (184, 4, 'Step 2 · Second', 'Crack and whisk two eggs', YES, YES_A),
        (4, 52, 'Step 3 · Then', 'Add salt and diced peppers', TUR, TUR_A),
        (184, 52, 'Step 4 · (II) ___', 'Cook both sides and serve', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in adimlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.4)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.8)
    return svg(360, 100, ic, 'Dört adımlı omlet tarifinde sıralama bağlaçları şeması.', 15)


def mutfak_eylem_arac_karti():
    """Soru 3 (s[2]): Drain, Grate, Whisk, Peel ve araçları kartı."""
    kartlar = [
        (4, '1. DRAIN', 'Strainer', 'Süzmek', MAVI, MAVI_A),
        (93, '2. GRATE', 'Grater', 'Rendelemek', TUR, TUR_A),
        (182, '3. WHISK', 'Whisk / Fork', 'Çırpmak', YES, YES_A),
        (271, '4. PEEL', 'Peeler / Knife', 'Soymak', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.3)
        ic += yazi(x + 42, 44, s1, LAC, boy=9.6)
        ic += yazi(x + 42, 64, s2, LAC, ince=True, boy=9.4)
    return svg(360, 88, ic, 'Mutfak hazırlık fiilleri ve kullanılan mutfak araçları kartları.', 14)


def clara_firin_diyalog():
    """Soru 6 (s[5]): Pişirme süresi diyaloğu (How long should we bake...)."""
    ic = kutu(4, 4, 352, 40, MAVI_A, MAVI, 7)
    ic += yazi(180, 20, 'Mother’s Question:', MAVI, boy=10.4)
    ic += yazi(180, 36, '« ___ ? »', LAC, boy=10.8)

    ic += kutu(4, 48, 352, 42, TUR_A, TUR, 7)
    ic += yazi(180, 64, 'Clara’s Answer:', TUR, boy=10.4)
    ic += yazi(180, 81, '«We should bake it in a preheated oven at 190 °C for 45 minutes.»', LAC, ince=True, boy=9.8)
    return svg(360, 94, ic, 'Clara ve annesi arasında fırında pişirme süresi diyaloğu.', 15)


def makarna_before_after_sema():
    """Soru 7 (s[6]): Boil -> Drain -> Add Sauce -> Serve akışı."""
    adimlar = [
        (4, '1. BOIL', 'Cook in salted', 'water (10 min)', MAVI, MAVI_A),
        (124, '2. DRAIN', 'Use a metal', 'strainer', TUR, TUR_A),
        (244, '3. SERVE', 'Pour tomato', 'sauce on top', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 112, 80, z, r, 8)
        ic += yazi(x + 56, 22, bas, r, boy=10.6)
        ic += yazi(x + 56, 44, s1, LAC, ince=True, boy=9.8)
        ic += yazi(x + 56, 64, s2, LAC, boy=9.8)
    return svg(360, 88, ic, 'Makarna haşlama, süzme ve servis etme aşamaları şeması.', 14)


def pankek_adimlari_karti():
    """Soru 8 (s[7]): Pankek hazırlık adımları kartı."""
    ic = kutu(4, 4, 352, 84, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Pancake Recipe Steps · What is the Next Step?', KAHVE, boy=10.6)
    adlar = [
        (10, '1. First', 'Whisk eggs &amp; milk', MAVI, MAVI_A),
        (126, '2. Second', 'Add flour &amp; sugar', TUR, TUR_A),
        (242, '3. Next', 'Pour into hot pan', YES, YES_A),
    ]
    for x, bas, alt, r, z in adlar:
        ic += kutu(x, 28, 108, 52, z, r, 6)
        ic += yazi(x + 54, 46, bas, r, boy=10.2)
        ic += yazi(x + 54, 66, alt, LAC, ince=True, boy=9.4)
    return svg(360, 92, ic, 'Üç adımlı pankek hazırlama şeması.', 15)


def makarna_siralama_panosu():
    """Soru 9 (s[8]): First -> Second -> Next -> Finally makarna sıralama şeması."""
    adimlar = [
        (4, '1. FIRST', 'Boil water &amp;', 'add salt', MAVI, MAVI_A),
        (93, '2. SECOND', 'Add pasta &amp;', 'cook 10 min', TUR, TUR_A),
        (182, '3. NEXT', 'Drain with', 'a strainer', MOR, MOR_A),
        (271, '4. FINALLY', 'Add sauce &amp;', 'serve warm', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.0)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.4)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.4)
    return svg(360, 88, ic, 'Dört aşamalı makarna pişirme süreci şeması.', 14)


def mercimek_corbasi_tarif_karti():
    """Soru 10 (s[9]): Lentil Soup Recipe kartı."""
    ic = kutu(4, 4, 158, 86, TUR_A, TUR, 8)
    ic += yazi(83, 21, 'Ingredients (Lentil Soup)', TUR, boy=10.2)
    ic += yazi(83, 41, '• 1 cup of red lentils', LAC, ince=True, boy=9.5)
    ic += yazi(83, 59, '• 1 onion &amp; 1 carrot', LAC, ince=True, boy=9.5)
    ic += yazi(83, 77, '• 1 tbsp butter &amp; water', LAC, ince=True, boy=9.5)

    ic += kutu(168, 4, 188, 86, YES_A, YES, 8)
    ic += yazi(262, 21, 'Cooking Process (In a Pot)', YESIL_K, boy=10.2)
    ic += yazi(262, 41, '1. Peel and dice onion &amp; carrot.', LAC, ince=True, boy=9.3)
    ic += yazi(262, 59, '2. Boil with lentils in a pot (25 min).', LAC, ince=True, boy=9.3)
    ic += yazi(262, 77, '3. Blend until smooth &amp; serve hot.', YESIL_K, boy=9.3)
    return svg(360, 94, ic, 'Mercimek çorbası malzemeleri ve tencerede pişirme aşamaları kartı.', 15)


def patates_puresi_karti():
    """Soru 12 (s[11]): Mashed potatoes 4 aşamalı hazırlık kartı."""
    adimlar = [
        (4, '1. First', 'peel 4 potatoes', MAVI, MAVI_A),
        (93, '2. Second', 'boil in water', TUR, TUR_A),
        (182, '3. Then', 'mash with fork', MOR, MOR_A),
        (271, '4. Finally', 'add milk &amp; butter', YES, YES_A),
    ]
    ic = ''
    for x, bas, alt, r, z in adimlar:
        ic += kutu(x, 6, 85, 76, z, r, 7)
        ic += yazi(x + 42, 26, bas, r, boy=10.3)
        ic += yazi(x + 42, 54, alt, LAC, ince=True, boy=9.4)
    return svg(360, 88, ic, 'Patates püresi yapımının dört aşamalı kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = omlet_baglac_karti()
    s[2]['gorsel'] = mutfak_eylem_arac_karti()
    s[5]['gorsel'] = clara_firin_diyalog()
    s[6]['gorsel'] = makarna_before_after_sema()
    s[7]['gorsel'] = pankek_adimlari_karti()
    s[8]['gorsel'] = makarna_siralama_panosu()
    s[9]['gorsel'] = mercimek_corbasi_tarif_karti()
    s[11]['gorsel'] = patates_puresi_karti()
