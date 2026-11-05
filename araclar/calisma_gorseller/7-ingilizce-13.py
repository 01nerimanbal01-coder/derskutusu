"""7. sınıf İngilizce 13. hafta (Unit 4: Wild Animals - Endangered Species & Fact Files) görselleri.
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


def panda_fact_file():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 24, 'FACT FILE: GIANT PANDA', YES, kalin=True)
    ic += yazi(92, 52, 'Class: Mammal · Status: Endangered', LAC, kalin=True)
    ic += yazi(92, 80, 'Habitat: Bamboo Forests (China)', YES)
    ic += kutu(184, 6, 170, 103, CAM_A, CAM)
    ic += yazi(269, 24, 'Diet, Weight & Lifespan', CAM, kalin=True)
    ic += yazi(269, 52, 'Diet: Herbivore (99% Bamboo)', LAC)
    ic += yazi(269, 80, 'Weight: ~110 kg · Lifespan: 20 yrs', CAM, kalin=True)
    return svg(ic, 'Giant Panda kimlik kartı: yaşam alanı, beslenme, ağırlık ve ömür.')


def endangered_extinct_kartlari():
    kartlar = [
        (6, 6, '1. Dodo Bird († 1681)', 'Extinct · Past Simple', KIR, KIR_A),
        (184, 6, '2. Polar Bear (Arctic)', 'Endangered · Present Simple', MAVI, MAVI_A),
        (6, 60, '3. Woolly Mammoth (†)', 'Extinct · Died out 4,000 yrs ago', MOR, MOR_A),
        (184, 60, '4. Monk Seal (Türkiye)', 'Endangered · ~700 left alive', YES, YES_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Soyu tükenmiş ve nesli tehlikedeki dört hayvan kartı.')


def tehdit_neden_kartlari():
    kartlar = [
        (6, 6, '1. Polar Bears', 'Reason: Melting Arctic Ice', MAVI, MAVI_A),
        (184, 6, '2. African Elephants', 'Reason: Hunted for Ivory Tusks', TUR, TUR_A),
        (6, 60, '3. Caretta Carettas', 'Reason: Bamboo Trees on Beach (?)', KIR, KIR_A),
        (184, 60, '4. Bengal Tigers', 'Reason: Hunted for Striped Fur', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Dört vahşi hayvanın neslinin tehlikeye girme nedenleri.')


def dodo_past_karti():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 24, 'EXTINCT SPECIES: THE DODO BIRD (Until 1681)', MOR, kalin=True)
    ic += yazi(180, 56, 'Dodos (1) ___ on Mauritius Island. They had small wings, so they (2) ___ .', LAC, kalin=True)
    ic += yazi(180, 86, 'Sailors hunted them easily, and they (3) ___ extinct in 1681.', KIR, kalin=True)
    return svg(ic, 'Soyu tükenen Dodo kuşu hakkında geçmiş zaman boşluk doldurma kartı.')


def save_wildlife_posteri():
    ic = kutu(6, 6, 172, 103, YES_A, YES)
    ic += yazi(92, 24, 'WE SHOULD (DOs)', YES, kalin=True)
    ic += yazi(92, 54, '• Protect natural habitats', LAC, kalin=True)
    ic += yazi(92, 82, '• Plant trees & keep seas clean', YES)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 24, 'WE SHOULDN’T (DON’Ts)', KIR, kalin=True)
    ic += yazi(269, 54, '• Hunt animals for fur or tusks', LAC, kalin=True)
    ic += yazi(269, 82, '• Cut down forests or pollute water', KIR)
    return svg(ic, 'Vahşi yaşamı korumak için yapılması ve yapılmaması gerekenler posteri.')


def roportaj_siralama_adimlari():
    adimlar = [
        (6, '1. Question', 'Which animal…?', MAVI, MAVI_A),
        (94, '2. Species', 'Monk seal is…', YES, YES_A),
        (182, '3. Reason?', 'Why in danger?', TUR, TUR_A),
        (270, '4. Explanation', 'Because people…', MOR, MOR_A),
    ]
    ic = ''
    for x, b1, b2, r, z in adimlar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, b1, r, kalin=True)
        ic += yazi(x + 42, 70, b2, LAC, kalin=True)
    return svg(ic, 'Akdeniz foku hakkında soru-cevap röportaj sıralaması.')


def threat_report_grafigi():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, 'Main Causes of Wildlife Extinction (%)', LAC, kalin=True)
    ic += f'<rect x="24" y="36" width="64" height="50" rx="4" fill="{KIR}" />'
    ic += yazi(56, 102, 'Habitat 45%', KIR, kalin=True)
    ic += f'<rect x="110" y="54" width="64" height="32" rx="4" fill="{TUR}" />'
    ic += yazi(142, 102, 'Hunting 25%', TUR, kalin=True)
    ic += f'<rect x="196" y="66" width="64" height="20" rx="4" fill="{MOR}" />'
    ic += yazi(228, 102, 'Climate 15%', MOR, kalin=True)
    ic += f'<rect x="280" y="66" width="64" height="20" rx="4" fill="{MAVI}" />'
    ic += yazi(312, 102, 'Pollution 15%', MAVI, kalin=True)
    return svg(ic, 'Yaban hayatını tehdit eden faktörlerin yüzdelik sütun grafiği.')


def amur_leopard_karti():
    ic = kutu(6, 6, 172, 103, TUR_A, TUR)
    ic += yazi(92, 24, 'AMUR LEOPARD (Endangered)', TUR, kalin=True)
    ic += yazi(92, 54, 'Class: Mammal · Diet: Carnivore', LAC, kalin=True)
    ic += yazi(92, 82, 'Habitat: Snowy Forests in Asia', TUR)
    ic += kutu(184, 6, 170, 103, KIR_A, KIR)
    ic += yazi(269, 24, 'Size & Main Threat', KIR, kalin=True)
    ic += yazi(269, 54, 'Weight: ~45 kg · Lifespan: 15 yrs', LAC)
    ic += yazi(269, 82, 'Threat: Poaching for spotted fur', KIR, kalin=True)
    return svg(ic, 'Amur leoparı bilgi kartı: sınıfı, yaşam alanı, ağırlığı ve tehdit.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = panda_fact_file()
    s[2]['gorsel'] = endangered_extinct_kartlari()
    s[5]['gorsel'] = tehdit_neden_kartlari()
    s[6]['gorsel'] = dodo_past_karti()
    s[7]['gorsel'] = save_wildlife_posteri()
    s[8]['gorsel'] = roportaj_siralama_adimlari()
    s[9]['gorsel'] = threat_report_grafigi()
    s[11]['gorsel'] = amur_leopard_karti()
