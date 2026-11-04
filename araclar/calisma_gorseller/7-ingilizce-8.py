"""7. sınıf İngilizce 8. hafta (Unit 3: Biographies — Simple Past Tense, Dates and Years) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
CAM, CAM_A = '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def aziz_sancar_karti():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += f'<rect x="8" y="6" width="584" height="28" rx="10" fill="{MOR}"/>'
    ic += yazi(300, 25, 'BIOGRAPHY CARD : PROF. DR. AZİZ SANCAR', 12, '#fff')
    kutular = [
        ('Born', 'September 8, 1946 (Mardin)', MAVI, MAVI_A, 18),
        ('Education', 'İstanbul Univ. (1969)', YES, YES_A, 212),
        ('Nobel Prize', 'Chemistry (2015, USA)', TUR, TUR_A, 406),
    ]
    for bas, deg, renk, arka, x in kutular:
        ic += f'<rect x="{x}" y="42" width="176" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 88, 60, bas, 12, renk)
        ic += yazi(x + 88, 80, deg, 12, LAC, ince=True)
    return svg(600, 108, ic, 'Aziz Sancar biyografi bilgi kartı.', 20)


def tarih_yil_kartlari():
    kartlar = [
        ('1. Card', '1905', MOR, MOR_A),
        ('2. Card', '1700', MAVI, MAVI_A),
        ('3. Card', '2003', YES, YES_A),
        ('4. Card', 'May 19, 1919', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, deg, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, deg, 12, LAC)
    return svg(600, 84, ic, 'Dört yıl ve tarih okunuş kartı.', 19)


def diyalog_balon_svg():
    ic = f'<rect x="8" y="6" width="276" height="84" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(146, 30, 'Question (A):', 12, MAVI)
    ic += yazi(146, 56, '«Where (1) ___ you born?»', 12, LAC)

    ic += f'<rect x="300" y="6" width="292" height="84" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(446, 28, 'Answer (B):', 12, YES)
    ic += yazi(446, 50, '«I (2) ___ born in London, and', 12, LAC, ince=True)
    ic += yazi(446, 72, 'I (3) ___ to Manchester in 2010.»', 12, LAC, ince=True)
    return svg(600, 96, ic, 'Geçmiş zaman soru ve cevap konuşma balonları.', 20)


def marie_curie_amac_karti():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'FACT FILE : MARIE CURIE (1867 - 1934)', 12, TUR)
    ic += yazi(160, 54, 'Event : Moved to Paris in 1891', 12, LAC)
    ic += f'<line x1="300" y1="36" x2="300" y2="80" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(445, 50, 'Goal : Study physics and', 12, MAVI)
    ic += yazi(445, 70, 'mathematics at the university', 12, MAVI, ince=True)
    return svg(600, 98, ic, 'Marie Curie Paris taşınma ve eğitim amacı bilgi kartı.', 20)


def wright_kardesler_serit():
    adimlar = [
        ('1871 · Birth', 'Orville was born', 'in Dayton, Ohio', MAVI, MAVI_A, 10),
        ('1892 · Work', 'Opened a bicycle', 'repair shop', YES, YES_A, 206),
        ('1903 · Invention', 'Invented the first', 'engined airplane', MOR, MOR_A, 402),
    ]
    ic = ''
    for bas, s1, s2, renk, arka, x in adimlar:
        ic += f'<rect x="{x}" y="8" width="188" height="82" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 94, 28, bas, 12, renk)
        ic += yazi(x + 94, 52, s1, 12, LAC, ince=True)
        ic += yazi(x + 94, 72, s2, 12, LAC, ince=True)
    return svg(600, 98, ic, 'Wright Kardeşler biyografi zaman şeridi.', 20)


def yasam_evreleri_seridi():
    evreler = [
        ('Stage 1', '1954 · Be Born', MAVI, MAVI_A),
        ('Stage 2', '1978 · Graduate', YES, YES_A),
        ('Stage 3', '1982 · Get Married', TUR, TUR_A),
        ('Stage 4', '1998 · Win Award', MOR, MOR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(evreler):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'Dört aşamalı yaşam evreleri zaman şeridi.', 19)


def fiil_eslestirme_kartlari():
    kartlar = [
        ('Card 1', 'grow  ->  grew', YES, YES_A),
        ('Card 2', 'win   ->  won', MAVI, MAVI_A),
        ('Card 3', 'have  ->  had', MOR, MOR_A),
        ('Card 4', 'leave ->  leaved', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, fiil, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, fiil, 12, LAC)
    return svg(600, 84, ic, 'Dört düzensiz fiil V1-V2 eşleştirme kartı.', 19)


def yasar_dogu_karti():
    ic = f'<rect x="8" y="6" width="584" height="86" rx="10" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'PROFILE CARD : YAŞAR DOĞU (NATIONAL WRESTLER)', 12, CAM)
    ic += yazi(115, 58, 'Born : 1913, Samsun', 12, LAC)
    ic += yazi(310, 58, 'Medal : 1948 London Olympics (Gold)', 12, YES)
    ic += yazi(508, 58, 'Died : Jan 8, 1961', 12, KIR)
    return svg(600, 98, ic, 'Yaşar Doğu biyografi profil kartı.', 20)


def dort_yil_okunus_karti():
    kartlar = [
        ('Ece · 1881', 'eighteen eighty-one', YES, YES_A),
        ('Can · 1907', 'nineteen seventy', KIR, KIR_A),
        ('Nil · 2005', 'two thousand and five', MAVI, MAVI_A),
        ('Mert · 1600', 'sixteen hundred', MOR, MOR_A),
    ]
    ic = ''
    for i, (kisi, okunus, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 4 + (i // 2) * 48
        ic += f'<rect x="{x}" y="{y}" width="286" height="42" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 62, y + 26, kisi, 12, renk)
        ic += f'<line x1="{x + 116}" y1="{y + 6}" x2="{x + 116}" y2="{y + 36}" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 200, y + 26, okunus, 12, LAC, ince=True)
    return svg(600, 102, ic, 'Dört öğrencinin yıl okunuşu kartları.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = aziz_sancar_karti()
    s[1]['gorsel'] = tarih_yil_kartlari()
    s[3]['gorsel'] = diyalog_balon_svg()
    s[4]['gorsel'] = marie_curie_amac_karti()
    s[6]['gorsel'] = wright_kardesler_serit()
    s[7]['gorsel'] = yasam_evreleri_seridi()
    s[8]['gorsel'] = fiil_eslestirme_kartlari()
    s[11]['gorsel'] = yasar_dogu_karti()
    s[12]['gorsel'] = dort_yil_okunus_karti()
