"""7. sınıf İngilizce 10. hafta (Unit 3: Biographies — Telling Years and Dates, Prepositions of Time, Life Milestones & Achievements) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def tarih_okunus_kartlari():
    kartlar = [
        (4, 4, '1. Kart · 19th May, 1919', 'nineteenth of May, nineteen nineteen', YES, YES_A),
        (184, 4, '2. Kart · 29th Oct, 1923', 'twenty-nine of Oct, eighteen twenty-three', MAVI, MAVI_A),
        (4, 50, '3. Kart · 8th Sept, 1946', 'eight of Sept, nineteen sixty-four', TUR, TUR_A),
        (184, 50, '4. Kart · 10th Nov, 1938', 'tenth of Nov, nineteen eighty-three', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.8, r)
        ic += yazi(x + 86, y + 34, alt, 8.8, LAC, ince=True)
    return svg(360, 96, ic, 'Dört tam tarihin İngilizce yazılış ve okunuş kartları.', 15)


def edat_ve_bilgi_kartlari():
    kartlar = [
        ('1. Doğum', 'born ON 8th Sept', MAVI, MAVI_A),
        ('2. Eğitim', 'graduated ___ Univ.', YES, YES_A),
        ('3. Amaç', 'moved ___ study', TUR, TUR_A),
        ('4. Ödül Yılı', 'won Nobel ___ 2015', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.8"/>'
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'Biyografi cümlelerinde kullanılan edat ve kategori kartları.', 14)


def roportaj_amac_karti():
    ic = kutu(6, 6, 348, 38, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Reporter: ___ did Prof. Dr. Aziz Sancar move to the USA?', 9.8, MAVI)
    ic += yazi(180, 38, '(Soru kelimesi: Neden / Niçin?)', 9.0, LAC, ince=True)

    ic += kutu(6, 48, 348, 38, YES_A, YES)
    ic += yazi(180, 64, 'Scientist: He moved there ___ do research on DNA repair.', 9.8, YES)
    ic += yazi(180, 80, '(Amaç bildiren yapı: to + V1)', 9.0, LAC, ince=True)
    return svg(360, 92, ic, 'Why sorusu ve to + V1 amaç yapısı röportaj kartı.', 15)


def marie_curie_bilgi_karti():
    ic = kutu(6, 6, 348, 78, MOR_A, MOR)
    ic += yazi(180, 22, 'MARIE CURIE (1867 – 1934) · BIOGRAPHY CARD', 10.0, MOR)
    ic += yazi(180, 42, '• Born in Warsaw, Poland in 1867; moved to Paris in 1891.', 9.3, LAC, ince=True)
    ic += yazi(180, 58, '• Married Pierre Curie in 1895; discovered radium & polonium.', 9.3, LAC, ince=True)
    ic += yazi(180, 74, '• Won TWO Nobel Prizes (Physics in 1903 & Chemistry in 1911).', 9.4, YES)
    return svg(360, 90, ic, 'Marie Curie biyografi ve başarı bilgi kartı.', 15)


def nikola_tesla_karti():
    ic = kutu(6, 6, 348, 74, CAM_A, CAM)
    ic += yazi(180, 22, 'NIKOLA TESLA (1856 – 1943) · PERSONAL LIFE', 10.0, CAM)
    ic += yazi(180, 44, '• Brilliant inventor of alternating current (AC) electricity.', 9.3, LAC, ince=True)
    ic += yazi(180, 64, '• He NEVER got married and he LIVED ALONE in New York.', 9.4, KIR)
    return svg(360, 86, ic, 'Nikola Tesla kişisel yaşam ve buluş bilgi kartı.', 14)


def aziz_sancar_kronoloji_seridi():
    adimlar = [
        ('1. 1946', 'Born in Mardin', MAVI, MAVI_A),
        ('2. 1969', 'Graduated (MD)', YES, YES_A),
        ('3. 1970s', 'Moved to USA', TUR, TUR_A),
        ('4. 2015', 'Won Nobel Prize', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += yazi(x + 41, 52, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Prof. Dr. Aziz Sancar kronolojik yaşam şeridi.', 14)


def graham_bell_zaman_cizelgesi():
    adimlar = [
        (4, 4, '1847 · Birth', 'Born in Edinburgh, Scotland', MAVI, MAVI_A),
        (184, 4, '1870 · Moving (Age 23)', 'Moved to Canada with family', YES, YES_A),
        (4, 50, '1876 · Invention', 'Invented the first telephone', TUR, TUR_A),
        (184, 50, '1877 · Marriage', 'Got married to Mabel Hubbard', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in adimlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.6, r)
        ic += yazi(x + 86, y + 34, alt, 9.1, LAC, ince=True)
    return svg(360, 96, ic, 'Alexander Graham Bell dört aşamalı zaman çizelgesi.', 15)


def idil_biret_karti():
    ic = kutu(6, 6, 348, 74, TUR_A, TUR)
    ic += yazi(180, 22, 'İDİL BİRET · TURKISH PIANO PRODIGY', 10.0, TUR)
    ic += yazi(180, 43, '• Birth: 1941, Ankara  |  Education: Paris Conservatory (at age 7)', 9.3, LAC, ince=True)
    ic += yazi(180, 63, '• Achievement: Became a National Artist (Devlet Sanatçısı) in 1971', 9.3, MAVI)
    return svg(360, 86, ic, 'İdil Biret doğum, eğitim ve ödül bilgi kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = tarih_okunus_kartlari()
    s[2]['gorsel'] = edat_ve_bilgi_kartlari()
    s[5]['gorsel'] = roportaj_amac_karti()
    s[6]['gorsel'] = marie_curie_bilgi_karti()
    s[7]['gorsel'] = nikola_tesla_karti()
    s[8]['gorsel'] = aziz_sancar_kronoloji_seridi()
    s[9]['gorsel'] = graham_bell_zaman_cizelgesi()
    s[11]['gorsel'] = idil_biret_karti()
