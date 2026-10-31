"""8. sınıf İngilizce 7. hafta (Unit 3: In the Kitchen — Cooking Methods, Kitchen Tools, Sequence Linkers & Preferences) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK; eğik kesir yok K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#8a5a2b', '#c9a227'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def mutfak_arac_kartlari():
    kartlar = [
        ('1. Kart', 'grater', 'cheddar cheese', TUR, TUR_A),
        ('2. Kart', 'strainer', 'boiled pasta', MAVI, MAVI_A),
        ('3. Kart', 'rolling pin', 'pizza dough', YES, YES_A),
        ('4. Kart', 'frying pan', 'potatoes in oil', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, arac, nesne, renk, arka) in enumerate(kartlar):
        x = 10 + i * 146
        ic += kutu(x, 6, 138, 86, arka, renk, 8, 1.5)
        ic += yazi(x + 69, 24, bas, 11, renk)
        ic += f'<line x1="{x + 14}" y1="32" x2="{x + 124}" y2="32" stroke="{renk}" stroke-width="1.2" stroke-dasharray="3 2"/>'
        ic += yazi(x + 69, 52, f'Tool: {arac}', 11.2, LAC)
        ic += yazi(x + 69, 74, f'({nesne})', 10.5, LAC, 'middle', True)
    return svg(600, 98, ic, 'Dört mutfak aracı kartı: 1. grater, 2. strainer, 3. rolling pin, 4. frying pan.', 14)


def sef_pisirme_kartlari():
    ic = kutu(8, 6, 284, 96, YES_A, YES, 9, 1.5)
    ic += yazi(150, 24, 'Leo’s Kitchen Habits', 11.5, YES)
    ic += yazi(22, 46, 'Prefers steaming broccoli & carrots', 10.5, LAC, 'start', True)
    ic += yazi(22, 64, 'Often grills fish or chicken breast', 10.5, LAC, 'start', True)
    ic += yazi(22, 82, 'Never fries food (dislikes greasy meals)', 10.5, YES, 'start')

    ic += kutu(308, 6, 284, 96, MOR_A, MOR, 9, 1.5)
    ic += yazi(450, 24, 'Maya’s Kitchen Habits', 11.5, MOR)
    ic += yazi(322, 46, 'Loves baking apple pies & cookies', 10.5, LAC, 'start', True)
    ic += yazi(322, 64, 'Uses the oven at the weekend', 10.5, LAC, 'start', True)
    ic += yazi(322, 82, 'Enjoys preparing homemade desserts', 10.5, MOR, 'start')
    return svg(600, 108, ic, 'Leo ve Maya mutfak alışkanlıkları kartları: Leo buharda ve ızgarada pişirmeyi sever, yağlı yemeklerden kaçınır; Maya hafta sonu fırında tatlı pişirir.', 14)


def tat_tercih_kartlari():
    ic = kutu(8, 6, 284, 88, KIR_A, KIR, 9, 1.5)
    ic += yazi(150, 24, 'Kerem’s Taste Note', 11.5, KIR)
    ic += yazi(150, 46, '“I can’t eat Mexican tacos with', 10.5, LAC, 'middle', True)
    ic += yazi(150, 62, 'red chili pepper. They are too spicy!”', 10.5, LAC, 'middle', True)
    ic += yazi(150, 80, '(Dislikes: spicy / chili food)', 10.5, KIR)

    ic += kutu(308, 6, 284, 88, TUR_A, TUR, 9, 1.5)
    ic += yazi(450, 24, 'Selin’s Taste Note', 11.5, TUR)
    ic += yazi(450, 46, '“I have a sweet tooth! I always', 10.5, LAC, 'middle', True)
    ic += yazi(450, 62, 'prefer chocolate cake to salty snacks.”', 10.5, LAC, 'middle', True)
    ic += yazi(450, 80, '(Prefers: sweet desserts)', 10.5, TUR)
    return svg(600, 100, ic, 'Kerem ve Selin tat tercihi kartları: Kerem acı/baharatlı yemekleri sevmez, Selin tatlıları tercih eder.', 14)


def fiil_tanim_fisleri():
    fisler = [
        ('1. Fiş · Ece', 'mash:', 'to crush boiled potatoes with a fork', MAVI, MAVI_A),
        ('2. Fiş · Can', 'whisk:', 'to beat eggs and sugar fast in a bowl', YES, YES_A),
        ('3. Fiş · Emre', 'roast:', 'to cook pasta in boiling hot water', KIR, KIR_A),
        ('4. Fiş · Duru', 'slice:', 'to cut bread or tomatoes into thin pieces', MOR, MOR_A),
    ]
    ic = ''
    for i, (kim, fiil, aciklama, renk, arka) in enumerate(fisler):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 56
        ic += kutu(x, y, 288, 48, arka, renk, 8, 1.4)
        ic += yazi(x + 14, y + 19, f'{kim} — {fiil}', 11, renk, 'start')
        ic += yazi(x + 14, y + 37, aciklama, 10.5, LAC, 'start', True)
    return svg(600, 118, ic, 'Dört öğrencinin mutfak fiili açıklama fişleri: 1. mash, 2. whisk, 3. roast (hatalı: boiling water), 4. slice.', 14)


def tarif_basamak_sema():
    adlar = [
        ('Step 1', 'First (Crack eggs)', MAVI, MAVI_A),
        ('Step 2', 'Second (Whisk)', YES, YES_A),
        ('Step 3', 'Next (Melt butter)', TUR, TUR_A),
        ('Step 4', 'After that (Cook)', MOR, MOR_A),
        ('Step 5', 'Finally (Serve)', ALTIN, '#fffbe6'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += kutu(x, 8, 105, 64, arka, renk, 9, 1.5)
        ic += yazi(x + 52.5, 30, ust, 11.2, renk)
        ic += yazi(x + 52.5, 52, alt, 10.3, LAC, 'middle', True)
        if i < 4:
            ic += f'<line x1="{x + 106}" y1="40" x2="{x + 118}" y2="40" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 80, ic, 'Omlet tarifinin 5 sıralama bağlacı basamağı: First, Second, Next, After that, Finally.', 14)


def corba_malzeme_karti():
    ic = kutu(8, 6, 584, 98, '#fffbe6', ALTIN, 10, 1.6)
    ic += yazi(300, 24, 'Lentil Soup Recipe Card (Mercimek Çorbası Tarifi)', 11.8, KAHVE)
    ic += kutu(20, 34, 270, 58, '#fff', TUR, 7, 1.3)
    ic += yazi(32, 52, 'Step 1 (Preparation):', 10.8, TUR, 'start')
    ic += yazi(32, 70, 'Peel and chop 1 onion, 1 potato', 10.5, LAC, 'start', True)
    ic += yazi(32, 84, 'and 1 carrot on a chopping board.', 10.5, LAC, 'start', True)

    ic += kutu(310, 34, 270, 58, '#fff', YES, 7, 1.3)
    ic += yazi(322, 52, 'Step 2 (Cooking Tool & Method):', 10.8, YES, 'start')
    ic += yazi(322, 70, 'Put red lentils and vegetables into a', 10.5, LAC, 'start', True)
    ic += yazi(322, 84, 'large saucepan (pot) and boil them.', 10.5, LAC, 'start', True)
    return svg(600, 110, ic, 'Mercimek çorbası tarif kartı: 1 soğan, 1 patates ve 1 havuç soyulup doğranır; büyük tencerede (saucepan/pot) haşlanır.', 14)


def uc_arkadas_tat_tablo():
    kartlar = [
        ('1. Bora (Fish)', 'Method: grilling fish', 'Avoids: greasy food', MAVI, MAVI_A),
        ('2. Zeynep (Vegetables)', 'Method: steaming vegetables', 'Avoids: salty food', YES, YES_A),
        ('3. Arda (Chicken)', 'Method: roasting in the oven', 'Avoids: spicy / chili food', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 196
        ic += kutu(x, 6, 190, 82, arka, renk, 8, 1.5)
        ic += yazi(x + 95, 25, bas, 11, renk)
        ic += yazi(x + 95, 48, s1, 10.5, LAC, 'middle', True)
        ic += yazi(x + 95, 68, s2, 10.5, renk)
    return svg(600, 94, ic, 'Üç gencin (Bora, Zeynep, Arda) pişirme yöntemi tercihi ve kaçındığı tat kartları.', 14)


def pisirme_yontem_tablosu():
    ic = kutu(8, 6, 584, 108, '#fff', GRI, 9, 1.5)
    ic += yazi(300, 24, 'Cooking Method Preferences of Four Friends (+ : Likes / - : Dislikes)', 11.5, LAC)
    satirlar = [
        ('Mert', 'Bake (+)', 'Grill (+)', 'Fry (-)', 'Boil (+)', MAVI),
        ('Sude', 'Steam (+)', 'Grill (+)', 'Fry (-)', 'Bake (+)', YES),
        ('Kaan', 'Roast (+)', 'Grill (+)', 'Boil (-)', 'Bake (+)', TUR),
        ('Ela', 'Steam (+)', 'Bake (+)', 'Fry (-)', 'Grill (+)', MOR),
    ]
    for i, (isim, c1, c2, c3, c4, renk) in enumerate(satirlar):
        y = 34 + i * 19
        ic += yazi(60, y + 13, isim, 10.8, renk)
        for j, met in enumerate((c1, c2, c3, c4)):
            x = 120 + j * 112
            r_kutu = KIR_A if '(-)' in met else YES_A
            c_kutu = KIR if '(-)' in met else YES
            ic += kutu(x, y, 102, 16, r_kutu, c_kutu, 4, 1.1)
            ic += yazi(x + 51, y + 12, met, 10.3, LAC)
    return svg(600, 120, ic, 'Dört arkadaşın (Mert, Sude, Kaan, Ela) yemek pişirme yöntemi tercih tablosu.', 14)


def salata_ipucu_karti():
    ic = kutu(8, 6, 584, 92, YES_A, YES, 9, 1.5)
    ic += yazi(300, 24, 'Fresh Salad Recipe Cue Card (Salata Tarifi İpucu Kartı)', 11.5, YES)
    ic += yazi(24, 46, 'Ingredients: tomatoes, cucumbers, green peppers, olive oil, lemon juice, salt', 10.5, LAC, 'start', True)
    ic += yazi(24, 66, 'Verbs to use: wash → peel → chop / dice → pour (olive oil) → mix & serve', 10.5, LAC, 'start', True)
    ic += yazi(24, 84, 'Sequence Linkers: First, ... · Second, ... · Then, ... · Finally, ...', 10.5, YES, 'start')
    return svg(600, 104, ic, 'Taze salata tarifi yazmak için malzemeler, fiiller ve sıralama bağlaçları ipucu kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = mutfak_arac_kartlari()
    s[1]['gorsel'] = sef_pisirme_kartlari()
    s[3]['gorsel'] = tat_tercih_kartlari()
    s[5]['gorsel'] = fiil_tanim_fisleri()
    s[6]['gorsel'] = tarif_basamak_sema()
    s[7]['gorsel'] = corba_malzeme_karti()
    s[8]['gorsel'] = uc_arkadas_tat_tablo()
    s[9]['gorsel'] = pisirme_yontem_tablosu()
    s[13]['gorsel'] = salata_ipucu_karti()
