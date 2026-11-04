"""8. sınıf İngilizce 5. hafta (Unit 2: Teen Life — Prefer / Would Rather, Personal Opinions & Camping) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def music_opinions_board():
    """Soru 1: 4 gencin müzik görüşleri kartı."""
    kartlar = [
        ('Arda · Classical', '«relaxing & harmonic» (+)', MAVI, MAVI_A),
        ('Selin · Folk Music', '«impressive & traditional» (+)', YES, YES_A),
        ('Mert · Heavy Metal', '«unbearable & too loud» (✗)', KIR, KIR_A),
        ('Zeynep · Pop Music', '«terrific & energetic» (+)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Dört gencin müzik türleri hakkındaki olumlu ve olumsuz sıfat kartları.', 12)


def camping_equipment_cards():
    """Soru 2: 4 temel kamp ekipmanı kartı."""
    ekipman = [
        ('Tent', 'Pitch a tent', YES, YES_A, 6),
        ('Sleeping Bag', 'Sleep warm', MAVI, MAVI_A, 94),
        ('Torch', 'See at night', TUR, TUR_A, 182),
        ('Compass', 'Find direction', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in ekipman:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Çadır, uyku tulumu, el feneri ve pusuladan oluşan kamp malzemesi kartları.', 12)


def emre_weekend_preferences():
    """Soru 4: Emre'nin hafta sonu tercih tablosu."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Emre’s Weekend Preference Card (Prefer + V-ing + to)', MOR)
    ic += kutu(12, 28, 162, 52, YES_A, YES, 6, 1.2)
    ic += yazi(93, 46, 'Preferred Activity (✓)', YESIL_K)
    ic += yazi(93, 66, 'Going trekking in forest', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, KIR_A, KIR, 6, 1.2)
    ic += yazi(267, 46, 'Disliked Activity (✗)', KIR)
    ic += yazi(267, 66, 'Hanging out at the mall', LAC, 'middle', True)
    return svg(360, 94, ic, 'Emre’nin doğa yürüyüşünü alışveriş merkezine tercih ettiğini gösteren kart.', 12)


def prefer_would_rather_bridge():
    """Soru 5: Prefer + V-ing + to ile Would rather + V1 + than dönüşüm kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Grammar Bridge · Prefer vs. Would Rather', MAVI)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Prefer + V-ing + to + V-ing', MAVI)
    ic += yazi(93, 66, 'prefer pitching ... to staying', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(267, 46, 'Would rather + V1 + than + V1', TUR)
    ic += yazi(267, 66, 'would rather pitch ... than stay', LAC, 'middle', True)
    return svg(360, 94, ic, 'Prefer ve Would rather kalıplarının dil bilgisi dönüşüm kartı.', 12)


def free_time_survey_chart():
    """Soru 7: 100 gencin boş zaman tercihleri sütun/kart grafiği."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Teenagers’ Free Time Survey Results (100 Students)', KAHVE)
    veriler = [
        ('Camping & Sports', '%45', YES, YES_A, 8),
        ('Music', '%30', MAVI, MAVI_A, 96),
        ('Detective Books', '%15', MOR, MOR_A, 184),
        ('Soap Operas', '%10', KIR, KIR_A, 272),
    ]
    for ad, oran, r, z, x in veriler:
        ic += kutu(x, 28, 80, 54, z, r, 6, 1.3)
        ic += yazi(x + 40, 47, oran, r)
        ic += yazi(x + 40, 69, ad, LAC, 'middle', True)
    return svg(360, 94, ic, 'Yüz öğrencinin boş zaman tercih oranlarını gösteren grafik kartı.', 12)


def camping_routine_steps():
    """Soru 8: 4 adımlı doğa kampı günlüğü."""
    adimlar = [
        ('1. Morning', 'Pitch the tents', YES, YES_A, 6),
        ('2. Afternoon', 'Trek & collect wood', MAVI, MAVI_A, 94),
        ('3. Evening', 'Make a campfire', TUR, TUR_A, 182),
        ('4. Night', 'Sleeping bags', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Kamp alanına varıştan gece uykusuna kadar dört aşamalı kamp rutini.', 12)


def fashion_casual_dialogue_card():
    """Soru 9: Clara ve Bora'nın giyim tercihi konuşma kartı."""
    ic = kutu(4, 4, 352, 86, TUR_A, TUR, 8, 1.4)
    ic += yazi(180, 20, 'Teen Style Chat · Trendy Outfits vs. Casual Clothes', TUR)
    ic += kutu(12, 28, 144, 52, '#fff', MOR, 6, 1.2)
    ic += yazi(84, 46, 'Clara’s Question', MOR)
    ic += yazi(84, 66, '«...follow fashion?»', LAC, 'middle', True)
    ic += kutu(164, 28, 184, 52, '#fff', YES, 6, 1.2)
    ic += yazi(256, 46, 'Bora’s Preference', YESIL_K)
    ic += yazi(256, 66, '«Casual clothes (jeans & T-shirt)»', LAC, 'middle', True)
    return svg(360, 94, ic, 'Clara ve Bora arasında moda ve rahat kıyafet tercihi diyaloğu.', 12)


def personal_preference_prompt_card():
    """Soru 12: Kişisel tercih ve sıfat yazma rehber kartı."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Weekend Preference & Opinion Writing Guide', YESIL_K)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Structures to Use', MAVI)
    ic += yazi(93, 66, 'prefer ... to / would rather ... than', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', MOR, 6, 1.2)
    ic += yazi(267, 46, 'Opinion Adjectives', MOR)
    ic += yazi(267, 66, 'terrific · relaxing · unbearable', LAC, 'middle', True)
    return svg(360, 94, ic, 'Prefer, would rather ve görüş sıfatlarıyla cümle kurma rehber kartı.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = music_opinions_board()
    s[1]['gorsel'] = camping_equipment_cards()
    s[3]['gorsel'] = emre_weekend_preferences()
    s[4]['gorsel'] = prefer_would_rather_bridge()
    s[6]['gorsel'] = free_time_survey_chart()
    s[7]['gorsel'] = camping_routine_steps()
    s[8]['gorsel'] = fashion_casual_dialogue_card()
    s[11]['gorsel'] = personal_preference_prompt_card()
