"""7. sınıf İngilizce 9. hafta (Unit 3: Biographies — Simple Past Negative/Interrogative, Irregular Verbs & Famous Figures) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def roportaj_soru_karti():
    ic = kutu(6, 6, 348, 38, MOR_A, MOR)
    ic += yazi(180, 22, 'Journalist: "(1) ___ Aziz Sancar (2) ___ from university?"', 10.0, MOR)
    ic += yazi(180, 38, '(Wh- question + Simple Past base verb)', 9.2, LAC, ince=True)

    ic += kutu(6, 48, 348, 36, YES_A, YES)
    ic += yazi(180, 66, 'Historian: "He graduated from Istanbul University in 1969."', 10.0, YES)
    return svg(360, 90, ic, 'Gazeteci ve tarihçi arasında mezuniyet yılı diyaloğu.', 15)


def duzensiz_fiil_tablo_kartlari():
    kartlar = [
        ('1. win', 'V2: won', MAVI, MAVI_A),
        ('2. write', 'V2: ? (yazdı)', TUR, TUR_A),
        ('3. become', '(-): ? (olmadı)', YES, YES_A),
        ('4. spend', 'V2: ? / (-): ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.3, LAC, ince=True)
    return svg(360, 82, ic, 'win, write, become ve spend düzensiz fiillerinin çekim kartları.', 14)


def idil_biret_biyografi_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'İDİL BİRET — Famous Turkish Pianist', 10.4, CAM)
    ic += yazi(180, 42, '• Born in Ankara in 1941; began playing the piano at age 3.', 9.6, LAC, ince=True)
    ic += yazi(180, 60, '• Went to Paris at age 7 to study at the Paris Conservatory.', 9.6, LAC, ince=True)
    ic += yazi(180, 76, '• Graduated with high honours and won many music awards.', 9.6, MAVI)
    return svg(360, 88, ic, 'Ünlü piyanist İdil Biret’in yaşam dönüm noktaları kartı.', 15)


def dort_dilbilgisi_karti():
    kutular = [
        ('1. Kart (+)', 'grew up in Savur', YES, YES_A),
        ('2. Kart (?)', 'Did Marconi invent...?', MAVI, MAVI_A),
        ('3. Kart (-)', 'didn’t discovered (!)', KIR, KIR_A),
        ('4. Kart (+)', 'wrote famous novels', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r)
        ic += yazi(x + 86, y + 14, bas, 10.0, r)
        ic += yazi(x + 86, y + 29, icerik, 9.5, LAC, ince=True)
    return svg(360, 90, ic, 'Simple Past Tense olumlu, olumsuz ve soru çekim kartları.', 15)


def fleming_donusturme_karti():
    ic = kutu(6, 6, 348, 74, TUR_A, TUR)
    ic += yazi(180, 22, '(+) Alexander Fleming discovered penicillin in 1928.', 10.1, TUR)
    ic += yazi(180, 46, '(-) Negative Form : Subject + didn’t + V1 ...', 9.6, LAC, ince=True)
    ic += yazi(180, 66, '(?) Question Form : Did + Subject + V1 ...?', 9.6, MAVI)
    return svg(360, 86, ic, 'Olumlu geçmiş zaman cümlesini olumsuz ve soruya dönüştürme kartı.', 14)


def ataturk_kronoloji_seridi():
    adimlar = [
        ('1. First', '1881 · Born in Salonika', MAVI, MAVI_A),
        ('2. Then', '1905 · Military Academy', YES, YES_A),
        ('3. After that', '1920 · Opened Assembly', TUR, TUR_A),
        ('4. Finally', '1923 · Founded Republic', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 52, alt, 8.9, LAC, ince=True)
    return svg(360, 82, ic, 'Atatürk’ün biyografisinde kronolojik sıralama bağlaçları şeridi.', 14)


def tesla_edison_karsilastirma():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += yazi(91, 22, 'NIKOLA TESLA', 10.3, MAVI)
    ic += yazi(91, 42, 'Born: 1856, Smiljan → 1884 USA', 9.3, LAC, ince=True)
    ic += yazi(91, 60, 'Work: Alternating current (AC)', 9.3, LAC, ince=True)
    ic += yazi(91, 76, 'Family: Didn’t get married (alone)', 9.3, KIR)

    ic += kutu(184, 6, 170, 78, YES_A, YES)
    ic += yazi(269, 22, 'THOMAS EDISON', 10.3, YES)
    ic += yazi(269, 42, 'Born: 1847, Ohio (USA)', 9.3, LAC, ince=True)
    ic += yazi(269, 60, 'Work: Invented electric lightbulb', 9.3, LAC, ince=True)
    ic += yazi(269, 76, 'Family: Got married & had kids', 9.3, YES)
    return svg(360, 90, ic, 'Nikola Tesla ve Thomas Edison biyografi karşılaştırma kartı.', 15)


def marie_curie_ipucu_karti():
    ic = kutu(6, 6, 170, 74, KIR_A, KIR)
    ic += yazi(91, 22, '1. Negative Sentence (-)', 10.1, KIR)
    ic += yazi(91, 43, 'not stay in Warsaw → move to Paris', 9.3, LAC, ince=True)
    ic += yazi(91, 64, '(Use: didn’t stay / moved)', 9.4, KIR)

    ic += kutu(184, 6, 170, 74, MOR_A, MOR)
    ic += yazi(269, 22, '2. Affirmative Sentence (+)', 10.1, MOR)
    ic += yazi(269, 43, 'discover radium / win two Prizes', 9.3, LAC, ince=True)
    ic += yazi(269, 64, '(Use: discovered / won)', 9.4, MOR)
    return svg(360, 86, ic, 'Marie Curie hakkında olumsuz ve olumlu cümle kurma ipucu kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = roportaj_soru_karti()
    s[2]['gorsel'] = duzensiz_fiil_tablo_kartlari()
    s[5]['gorsel'] = idil_biret_biyografi_karti()
    s[6]['gorsel'] = dort_dilbilgisi_karti()
    s[7]['gorsel'] = fleming_donusturme_karti()
    s[8]['gorsel'] = ataturk_kronoloji_seridi()
    s[9]['gorsel'] = tesla_edison_karsilastirma()
    s[11]['gorsel'] = marie_curie_ipucu_karti()
