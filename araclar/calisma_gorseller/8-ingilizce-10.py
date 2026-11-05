"""8. sınıf İngilizce 10. hafta (Unit 3: In the Kitchen — Food Preferences &amp; Cooking Methods) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def dort_arkadas_tat_kartlari():
    """Soru 2 (s[1]): Leo, Maya, Sam ve Nina yemek tercihi kartları."""
    kartlar = [
        (4, 4, '1. Leo’s Preference', 'Salty crackers · Sour pickles', MAVI, MAVI_A),
        (184, 4, '2. Maya’s Preference', 'Cake · Baklava · Pudding', MOR, MOR_A),
        (4, 52, '3. Sam’s Preference', 'Spicy chili soup · Steak', KIR, KIR_A),
        (184, 52, '4. Nina’s Preference', 'Steamed broccoli · Carrots', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.3)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.6)
    return svg(360, 100, ic, 'Leo, Maya, Sam ve Nina adlı dört arkadaşın yiyecek tercih kartları.', 15)


def pisirme_yontemleri_panosu():
    """Soru 3 (s[2]): Boil, Bake, Steam, Grill 4 yöntem kartı."""
    kartlar = [
        (4, 4, '1. In Hot Water (Pot)', 'Pasta &amp; Eggs -> BOIL', MAVI, MAVI_A),
        (184, 4, '2. In a Hot Oven', 'Bread &amp; Cake -> ?', TUR, TUR_A),
        (4, 52, '3. Over Hot Vapour', 'Broccoli &amp; Fish -> ?', YES, YES_A),
        (184, 52, '4. Over Barbecue Fire', 'Meatballs &amp; Steak -> ?', KIR, KIR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.3)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.6)
    return svg(360, 100, ic, 'Dört temel pişirme yöntemini gösteren mutfak bilgi kartları.', 15)


def mercimek_corbasi_adimlari():
    """Soru 6 (s[5]): Lentil soup 4 sıralı adım kartı."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8)
    ic += yazi(180, 19, 'Chef’s Lentil Soup Recipe Steps (Mercimek Çorbası)', KAHVE, boy=10.2)
    adimlar = [
        (10, 26, 'First:', 'Chop onion &amp; carrot', MAVI, MAVI_A),
        (96, 26, 'Second:', 'Fry them in a pot', TUR, TUR_A),
        (182, 26, 'Next:', 'Rinse &amp; add lentils', YES, YES_A),
        (268, 26, 'Finally:', 'Blend &amp; serve hot', MOR, MOR_A),
    ]
    for x, y, bas, alt, r, z in adimlar:
        ic += kutu(x, y, 82, 58, z, r, 6)
        ic += yazi(x + 41, y + 20, bas, r, boy=10.0)
        ic += yazi(x + 41, y + 42, alt, LAC, ince=True, boy=8.9)
    return svg(360, 94, ic, 'Mercimek çorbası tarifinin First, Second, Next ve Finally adımları.', 15)


def pizza_hazirlik_kartlari():
    """Soru 7 (s[6]): Pizza yapımının 4 aşaması ve kullanılan araçlar."""
    kartlar = [
        (4, 4, 'Step I · Kneading Dough', 'Flour + water in a bowl', MAVI, MAVI_A),
        (184, 4, 'Step II · Rolling Dough', 'Flat circle with a rolling pin', TUR, TUR_A),
        (4, 52, 'Step III · Slicing Toppings', 'Knife &amp; cutting board', YES, YES_A),
        (184, 52, 'Step IV · Baking Pizza', 'Baking tray in hot oven', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.5)
    return svg(360, 100, ic, 'Pizza hazırlığının dört adımı ve kullanılan mutfak araçları.', 15)


def restoran_siparis_diyalogu():
    """Soru 8 (s[7]): Garson ve müşteri balık pişirme tercihi diyaloğu."""
    ic = kutu(4, 4, 352, 40, MAVI_A, MAVI, 8)
    ic += yazi(180, 19, 'Waiter: «How would you like your salmon fish, madam?»', MAVI, boy=10.2)
    ic += yazi(180, 35, '(Fried in oil, grilled or baked in the oven?)', LAC, ince=True, boy=9.4)

    ic += kutu(4, 48, 352, 42, YES_A, YES, 8)
    ic += yazi(180, 64, 'Customer: «I never eat greasy food. Please grill or bake it.»', YESIL_K, boy=10.0)
    ic += yazi(180, 81, '(Reason: Grilling and baking are healthier than frying.)', LAC, ince=True, boy=9.4)
    return svg(360, 94, ic, 'Restoranda garson ile müşteri arasındaki sağlıklı balık pişirme diyaloğu.', 15)


def elmali_kek_akis_semasi():
    """Soru 9 (s[8]): Apple Cake 4 aşamalı akış şeması."""
    adimlar = [
        (4, '1. First', 'Whisk eggs', 'and sugar', MAVI, MAVI_A),
        (93, '2. Second', 'Add milk, oil', 'and flour', TUR, TUR_A),
        (182, '3. Then', 'Pour into tray', '&amp; add apples', MOR, MOR_A),
        (271, '4. Finally', 'Bake at 180 °C', 'for 35 min', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.2)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.4)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.4)
    return svg(360, 88, ic, 'Elmalı kek tarifinin First, Second, Then ve Finally basamakları.', 14)


def aile_tercih_tablosu():
    """Soru 10 (s[9]): Father, Mother, Daughter, Son yemek tercih tablosu."""
    kartlar = [
        (4, 4, 'Father (Baba)', 'Likes: Grilled meat · Dislikes: Sweets', MAVI, MAVI_A),
        (184, 4, 'Mother (Anne)', 'Likes: Steamed vegetables (Healthy)', YES, YES_A),
        (4, 52, 'Daughter (Kız Çocuk)', 'Likes: Milky desserts · Dislikes: Sour', MOR, MOR_A),
        (184, 52, 'Son (Erkek Çocuk)', 'Likes: Spicy &amp; fried food · Dislikes: Boiled', KIR, KIR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.3)
    return svg(360, 100, ic, 'Dört aile üyesinin sevdiği ve sevmediği yemek türleri panosu.', 15)


def saglikli_sagliksiz_mutfak_karti():
    """Soru 12 (s[11]): Healthy Kitchen vs Unhealthy Kitchen karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8)
    ic += yazi(90, 22, 'Healthy Kitchen Habits', YESIL_K, boy=10.3)
    ic += yazi(90, 44, '• Steaming · Boiling · Grilling', LAC, ince=True, boy=9.6)
    ic += yazi(90, 64, '• Fresh, nutritious &amp; light', YESIL_K, boy=9.6)

    ic += kutu(184, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(270, 22, 'Unhealthy Kitchen Habits', KIR, boy=10.3)
    ic += yazi(270, 44, '• Deep frying in hot oil', LAC, ince=True, boy=9.6)
    ic += yazi(270, 64, '• Too greasy, fatty &amp; heavy', KIR, boy=9.6)
    return svg(360, 90, ic, 'Sağlıklı ve sağlıksız pişirme alışkanlıklarını karşılaştıran kart.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_arkadas_tat_kartlari()
    s[2]['gorsel'] = pisirme_yontemleri_panosu()
    s[5]['gorsel'] = mercimek_corbasi_adimlari()
    s[6]['gorsel'] = pizza_hazirlik_kartlari()
    s[7]['gorsel'] = restoran_siparis_diyalogu()
    s[8]['gorsel'] = elmali_kek_akis_semasi()
    s[9]['gorsel'] = aile_tercih_tablosu()
    s[11]['gorsel'] = saglikli_sagliksiz_mutfak_karti()
