"""8. sınıf İngilizce 8. hafta (Unit 3: In the Kitchen — Cooking Methods, Kitchen Tools & Sequence Linkers) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); yalnız '·' veya '-' ayırıcı (K155/K172)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def pisirme_yontem_kartlari():
    """Soru 1: Üç yemek ve pişirme yöntemi kartı (bake, boil, grill)."""
    kartlar = [
        ('1. Kart · Apple Cake', 'Method: bake', 'Tool: oven · tray', MOR, MOR_A, 6),
        ('2. Kart · Spaghetti', 'Method: boil', 'Tool: large pot', MAVI, MAVI_A, 124),
        ('3. Kart · Salmon Fish', 'Method: grill', 'Tool: barbecue', YES, YES_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC)
        ic += yazi(x + 56, 70, s2, LAC, 'middle', True)
    return svg(360, 94, ic, 'Üç yemek pişirme kartı: Apple cake bake, Spaghetti boil, Salmon fish grill.')


def sebze_corbasi_akis():
    """Soru 3: Chef Clara's Vegetable Soup 4 aşamalı tarif kartı."""
    adlar = [
        ('1. First', 'Wash & peel', MAVI, MAVI_A),
        ('2. Second', 'Dice veggies', TUR, TUR_A),
        ('3. Then', 'Boil in a pot', YES, YES_A),
        ('4. Finally', 'Serve hot', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 21, 'Chef Clara’s Vegetable Soup — Step-by-Step Process', KAHVE)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 56, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 70, alt, LAC, 'middle', True)
    return svg(360, 96, ic, 'Sebze çorbası 4 aşamalı tarif şeması: First, Second, Then, Finally.')


def dort_arac_eslestirme_karti():
    """Soru 5: Dört öğrencinin mutfak aracı eşleştirme kartları (3. kart Berk hatalı)."""
    kartlar = [
        ('1. Arda · peeler', 'peel apples', YES, YES_A),
        ('2. Mina · whisk', 'beat eggs & milk', MAVI, MAVI_A),
        ('3. Berk · strainer', 'slice fresh bread', KIR, KIR_A),
        ('4. Elif · knife', 'dice the onions', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 48
        ic += kutu(x, y, 172, 44, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 18, bas, r)
        ic += yazi(x + 86, y + 36, alt, LAC, 'middle', True)
    return svg(360, 100, ic, 'Dört mutfak aracı kartı: 1 peeler, 2 whisk, 3 strainer hatalı, 4 knife.')


def muffin_tarif_karti():
    """Soru 6: Homemade Berry Muffins malzeme ve pişirme süresi kartı."""
    ic = kutu(4, 4, 352, 92, MOR_A, MOR, 9, 1.4)
    ic += yazi(180, 21, 'Homemade Berry Muffins — Recipe Card', MOR)
    ic += kutu(12, 28, 162, 60, '#fff', MOR, 7, 1.2)
    ic += yazi(93, 46, 'Ingredients:', MOR)
    ic += yazi(93, 64, 'Flour, eggs, milk,', LAC, 'middle', True)
    ic += yazi(93, 80, 'sugar & blueberries', LAC, 'middle', True)

    ic += kutu(186, 28, 162, 60, '#fff', TUR, 7, 1.2)
    ic += yazi(267, 46, 'Baking Info:', TUR)
    ic += yazi(267, 64, 'Preheat oven: 180 °C', LAC, 'middle', True)
    ic += yazi(267, 80, 'Bake for 25 minutes', TUR)
    return svg(360, 100, ic, 'Berry Muffins malzeme ve fırında pişirme süresi kartı.')


def tat_tercih_tablosu():
    """Soru 7: Dört arkadaşın tat ve yemek tercihleri tablosu."""
    ic = kutu(4, 4, 352, 102, '#fff', GRI, 9, 1.4)
    ic += yazi(180, 20, 'Taste and Food Preferences of Four Friends', LAC)
    satirlar = [
        ('Tuna · Likes: Salty soup · Avoids: Sweet cake', MAVI_A, MAVI),
        ('Pelin · Likes: Milky dessert · Avoids: Spicy food', TUR_A, TUR),
        ('Cem · Likes: Steamed broccoli · Avoids: Greasy fries', YES_A, YES),
        ('Derya · Likes: Sour lemon salad · Avoids: Bitter coffee', MOR_A, MOR),
    ]
    for i, (met, z, r) in enumerate(satirlar):
        y = 26 + i * 19
        ic += kutu(12, y, 336, 16, z, r, 4, 1.1)
        ic += yazi(180, y + 12, met, LAC, 'middle', True)
    return svg(360, 110, ic, 'Tuna, Pelin, Cem ve Deryanın tat tercihleri tablosu.')


def makarna_akis_semasi():
    """Soru 8: Makarna hazırlama ve süzme 4 adımlı şeması."""
    adlar = [
        ('Step 1', 'Boil water', MAVI, MAVI_A),
        ('Step 2', 'Cook pasta', TUR, TUR_A),
        ('Step 3', 'Drain pasta', YES, YES_A),
        ('Step 4', 'Add sauce', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 86, '#fff', MAVI, 8, 1.3)
    ic += yazi(180, 20, 'How to Cook Delicious Pasta (4 Steps)', MAVI)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 54, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Makarna pişirme 4 aşamalı akış şeması: Boil water, Cook pasta, Drain pasta, Add sauce.')


def mutfak_diyalog_karti():
    """Soru 9: David ve annesi arasında mutfak diyaloğu cevap özetleri."""
    ic = kutu(4, 4, 352, 96, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 20, 'Mum’s Answers in the Kitchen Dialogue', KAHVE)
    cevaplar = [
        ('Answer 1: “We are having chicken and salad tonight.”', MAVI_A, MAVI),
        ('Answer 2: “Olive oil, garlic, yoghurt and black pepper.”', YES_A, YES),
        ('Answer 3: “I usually roast or grill it for 20 minutes.”', TUR_A, TUR),
    ]
    for i, (met, z, r) in enumerate(cevaplar):
        y = 28 + i * 22
        ic += kutu(12, y, 336, 19, z, r, 5, 1.1)
        ic += yazi(180, y + 14, met, LAC, 'middle', True)
    return svg(360, 104, ic, 'Mutfak diyaloğunda annenin verdiği 3 yanıt kartı.')


def pisirme_anket_grafigi():
    """Soru 12: 100 gencin pişirme yöntemi tercihleri yüzdelik sütun/şerit grafiği."""
    ic = kutu(4, 4, 352, 100, '#fff', GRI, 9, 1.4)
    ic += yazi(180, 20, 'Cooking Method Survey Results (100 Teenagers)', LAC)
    barlar = [
        ('Grilling · 35%', 126, YES, YES_A),
        ('Steaming · 30%', 108, MAVI, MAVI_A),
        ('Baking · 20%', 72, MOR, MOR_A),
        ('Boiling · 15%', 54, TUR, TUR_A),
    ]
    for i, (etiket, boy, r, z) in enumerate(barlar):
        y = 28 + i * 18
        ic += kutu(14, y, 130, 15, z, r, 4, 1.1)
        ic += yazi(79, y + 12, etiket, LAC)
        ic += kutu(152, y, boy, 15, r, r, 4, 1.0)
    return svg(360, 108, ic, '100 gencin pişirme tercihleri anketi: Grilling yüzde 35, Steaming yüzde 30, Baking yüzde 20, Boiling yüzde 15.')


def omlet_ipucu_karti():
    """Soru 13: Healthy Omelette Cue Card ipucu kartı."""
    ic = kutu(4, 4, 352, 88, YES_A, YES, 9, 1.4)
    ic += yazi(180, 21, 'Healthy Omelette Cue Card (İpucu Kartı)', YESIL_K)
    ic += kutu(12, 28, 336, 56, '#fff', YES, 6, 1.2)
    ic += yazi(180, 46, '1. First: heat olive oil · 2. Second: whisk two eggs', LAC, 'middle', True)
    ic += yazi(180, 68, '3. Then: add grated cheese · 4. Finally: cook in the pan', YESIL_K)
    return svg(360, 96, ic, 'Omlet tarifi yazma ipucu kartı: First, Second, Then, Finally.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = pisirme_yontem_kartlari()
    s[2]['gorsel'] = sebze_corbasi_akis()
    s[4]['gorsel'] = dort_arac_eslestirme_karti()
    s[5]['gorsel'] = muffin_tarif_karti()
    s[6]['gorsel'] = tat_tercih_tablosu()
    s[7]['gorsel'] = makarna_akis_semasi()
    s[8]['gorsel'] = mutfak_diyalog_karti()
    s[11]['gorsel'] = omlet_ipucu_karti()
