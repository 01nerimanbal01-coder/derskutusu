"""7. sınıf İngilizce 1. hafta (Appearance and Personality: dış görünüş, kişilik ve karşılaştırma) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#c9a227', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:calc(16mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def rozet(x, y, metin, renk, r=10, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.35, metin, boy, renk)


def soru_cevap_kartlari():
    sorular = [
        ('1', 'What does she look like?', MAVI, MAVI_A),
        ('2', 'What is she like?', YES, YES_A),
        ('3', 'What does she like?', TUR, TUR_A),
    ]
    cevaplar = [
        ('A', 'She is honest, punctual and generous.', YES, YES_A),
        ('B', 'She likes reading books and cycling.', TUR, TUR_A),
        ('C', 'She is tall and slim with wavy hair.', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (no, met, r, z) in enumerate(sorular):
        y = 6 + i * 38
        ic += kutu(6, y, 274, 32, z, r, 7, 1.5)
        ic += rozet(22, y + 16, no, r, 9.5, 11)
        ic += yazi(38, y + 20, met, 11.2, LAC, 'start')
    for i, (harf, met, r, z) in enumerate(cevaplar):
        y = 6 + i * 38
        ic += kutu(296, y, 298, 32, '#fff', GRI, 7, 1.4)
        ic += rozet(312, y + 16, harf, LAC, 9.5, 11)
        ic += yazi(328, y + 20, met, 10.8, LAC, 'start', True)
    return svg(600, 122, ic, 'Üç soru kartı (1 look like, 2 be like, 3 like) ve üç cevap fişi (A kişilik, B sevilen etkinlik, C dış görünüş).', 23)


def profil_panosu():
    ic = kutu(6, 6, 286, 112, MAVI_A, MAVI, 10, 1.6)
    ic += f'<rect x="6" y="6" width="286" height="24" rx="10" fill="{MAVI}"/><rect x="6" y="18" width="286" height="12" fill="{MAVI}"/>'
    ic += yazi(149, 22, 'STUDENT CARD · EFE', 11.5, '#fff')
    ic += yazi(20, 46, 'Height & Build: 172 cm, slim', 10.8, LAC, 'start', True)
    ic += yazi(20, 64, 'Hair & Eyes: Wavy brown hair, green eyes', 10.8, LAC, 'start', True)
    ic += yazi(20, 82, 'Glasses: Yes (wears glasses)', 10.8, LAC, 'start', True)
    ic += yazi(20, 100, 'Habit: Always arrives on time', 10.8, MAVI, 'start')

    ic += kutu(308, 6, 286, 112, TUR_A, TUR, 10, 1.6)
    ic += f'<rect x="308" y="6" width="286" height="24" rx="10" fill="{TUR}"/><rect x="308" y="18" width="286" height="12" fill="{TUR}"/>'
    ic += yazi(451, 22, 'STUDENT CARD · MERT', 11.5, '#fff')
    ic += yazi(322, 46, 'Height & Build: 162 cm, of medium weight', 10.8, LAC, 'start', True)
    ic += yazi(322, 64, 'Hair & Eyes: Curly black hair, hazel eyes', 10.8, LAC, 'start', True)
    ic += yazi(322, 82, 'Glasses: No', 10.8, LAC, 'start', True)
    ic += yazi(322, 100, 'Habit: Makes friends easily (outgoing)', 10.8, TUR, 'start')
    return svg(600, 124, ic, 'Efe ve Mert öğrenci bilgi kartları: boy, kilo, saç, göz, gözlük ve davranış özellikleri.', 23)


def comparative_kartlari():
    kartlar = [
        ('1', 'slim  →  slimmer', 'Kısa sıfat: son harf çift yazılır + er', YES, YES_A),
        ('2', 'good  →  gooder', 'Düzensiz sıfat dönüşümü', KIR, KIR_A),
        ('3', 'outgoing  →  outgoinger', 'Uzun sıfat dönüşümü', TUR, TUR_A),
        ('4', 'tidy  →  tidier', 'Sonu -y ile biten sıfat: -ier alır', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (no, bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 58
        ic += kutu(x, y, 286, 50, z, r, 8, 1.5)
        ic += rozet(x + 20, y + 25, no, r, 10, 11)
        ic += yazi(x + 38, y + 21, bas, 11.8, LAC, 'start')
        ic += yazi(x + 38, y + 39, alt, 10.5, SOLUK, 'start', True)
    return svg(600, 120, ic, 'Dört comparative kartı: 1. slim -> slimmer, 2. good -> gooder, 3. outgoing -> outgoinger, 4. tidy -> tidier.', 22)


def davranis_notlari():
    notlar = [
        ('1. Fiş', 'Never late for classes;', 'arrives at school on time.', MAVI, MAVI_A),
        ('2. Fiş', 'Likes sharing her lunch', 'and buying small presents.', YES, YES_A),
        ('3. Fiş', '175 cm tall with a thin', 'body build (52 kg).', TUR, TUR_A),
        ('4. Fiş', 'Never tells lies; always', 'speaks the truth.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(notlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 92, z, r, 8, 1.5)
        ic += yazi(x + 71, 24, bas, 11.5, r)
        ic += f'<line x1="{x + 12}" y1="32" x2="{x + 130}" y2="32" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 71, 52, s1, 10.5, LAC, 'middle', True)
        ic += yazi(x + 71, 70, s2, 10.5, LAC, 'middle', True)
    return svg(600, 104, ic, 'Dört gözlem fişi: 1. zamanında gelme, 2. paylaşma ve hediye verme, 3. uzun ve zayıf yapı, 4. doğruyu söyleme.', 21)


def hata_duzeltme_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.6)
    ic += rozet(24, 24, 'A', KIR, 10, 11)
    ic += yazi(42, 28, 'Hatalı Cümle Kartı A', 11.5, KIR, 'start')
    ic += yazi(149, 54, '“My sister is more tall than me.”', 11.5, LAC)
    ic += yazi(149, 76, '(İpucu: tall kısa bir sıfattır.)', 10.5, SOLUK, 'middle', True)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.6)
    ic += rozet(326, 24, 'B', TUR, 10, 11)
    ic += yazi(344, 28, 'Hatalı Cümle Kartı B', 11.5, TUR, 'start')
    ic += yazi(451, 54, '“Kerem is generouser than Can.”', 11.5, LAC)
    ic += yazi(451, 76, '(İpucu: generous çok heceli bir sıfattır.)', 10.5, SOLUK, 'middle', True)
    return svg(600, 98, ic, 'İki hatalı karşılaştırma cümlesi: A My sister is more tall than me, B Kerem is generouser than Can.', 20)


def karsilastirma_tablosu():
    ic = kutu(6, 6, 588, 106, '#fff', GRI, 9, 1.5)
    ic += f'<rect x="6" y="6" width="588" height="24" rx="9" fill="{LAC}"/><rect x="6" y="18" width="588" height="12" fill="{LAC}"/>'
    basliklar = [('Özellik / Davranış', 95), ('ASLI', 275), ('DERYA', 465)]
    for met, x in basliklar:
        ic += yazi(x, 22, met, 11.2, '#fff')
    satirlar = [
        ('Age & Height', '12 years old · 154 cm', '13 years old · 164 cm'),
        ('Arrival at school', 'Always on time (08:15)', 'Sometimes late (08:40)'),
        ('Sharing & Homework', 'Finishes homework early', 'Shares her books with friends'),
    ]
    for i, (oz, a, d) in enumerate(satirlar):
        y = 34 + i * 24
        ic += f'<rect x="12" y="{y}" width="576" height="21" rx="4" fill="{GRI_A if i % 2 == 0 else "#fff"}"/>'
        ic += yazi(20, y + 14.5, oz, 10.8, LAC, 'start')
        ic += yazi(275, y + 14.5, a, 10.8, MAVI, 'middle', True)
        ic += yazi(465, y + 14.5, d, 10.8, TUR, 'middle', True)
    return svg(600, 118, ic, 'Aslı ve Derya karşılaştırma tablosu: yaş-boy, okula varış zamanı ve ödev-paylaşım alışkanlıkları.', 23)


def diyalog_karti():
    ic = kutu(6, 6, 266, 86, MAVI_A, MAVI, 10, 1.6)
    ic += yazi(22, 26, 'ARDA’S QUESTION:', 11.2, MAVI, 'start')
    ic += kutu(20, 36, 238, 42, '#fff', MAVI, 7, 1.4, ' stroke-dasharray="4 3"')
    ic += yazi(139, 61, '“ ? ”', 13, MAVI)

    ic += f'<line x1="276" y1="49" x2="300" y2="49" stroke="{LAC}" stroke-width="2"/><path d="M295 44 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'

    ic += kutu(306, 6, 288, 86, YES_A, YES, 10, 1.6)
    ic += yazi(322, 26, 'SELİN’S ANSWER:', 11.2, YES, 'start')
    ic += yazi(322, 50, '“She is very easy-going, honest', 11.2, LAC, 'start', True)
    ic += yazi(322, 70, 'and generous. She never tells lies.”', 11.2, LAC, 'start', True)
    return svg(600, 98, ic, 'Arda ve Selin konuşma kartı: Selin yeni sıra arkadaşının uyumlu, dürüst ve cömert olduğunu söylüyor.', 20)


def defne_karti():
    ic = kutu(6, 6, 588, 92, CAM_A, CAM, 10, 1.6)
    ic += f'<rect x="6" y="6" width="588" height="24" rx="10" fill="{CAM}"/><rect x="6" y="18" width="588" height="12" fill="{CAM}"/>'
    ic += yazi(300, 22, 'CLASSMATE PROFILE CARD · DEFNE YILMAZ', 11.5, '#fff')
    ic += yazi(24, 50, 'Height & Build:', 11, CAM, 'start')
    ic += yazi(130, 50, 'Of medium height, slim', 11, LAC, 'start', True)
    ic += yazi(310, 50, 'Personality:', 11, CAM, 'start')
    ic += yazi(400, 50, 'Honest and easy-going', 11, LAC, 'start', True)
    ic += yazi(24, 74, 'Hair & Eyes:', 11, CAM, 'start')
    ic += yazi(130, 74, 'Curly brown hair, hazel eyes', 11, LAC, 'start', True)
    ic += yazi(310, 74, 'Evidence:', 11, CAM, 'start')
    ic += yazi(400, 74, 'She always tells the truth.', 11, LAC, 'start', True)
    return svg(600, 104, ic, 'Defne Yılmaz tanıtım kartı: orta boylu, zayıf, kıvırcık kahverengi saçlı, dürüst çünkü her zaman doğruyu söyler.', 21)


def kanit_karti():
    ic = kutu(6, 6, 286, 92, MAVI_A, MAVI, 9, 1.6)
    ic += yazi(149, 24, 'Given Text (Verilen Metin)', 11.5, MAVI)
    ic += yazi(149, 48, '“Kaan is tall and of medium weight.', 11, LAC, 'middle', True)
    ic += yazi(149, 66, 'He has got short straight black hair', 11, LAC, 'middle', True)
    ic += yazi(149, 84, 'and green eyes. He wears glasses.”', 11, LAC, 'middle', True)

    ic += kutu(308, 6, 286, 92, KIR_A, KIR, 9, 1.6)
    ic += yazi(451, 24, 'Student’s Claim (Öğrencinin Yorumu)', 11.5, KIR)
    ic += yazi(451, 52, '“According to the text, Kaan is', 11, LAC, 'middle', True)
    ic += yazi(451, 70, 'very selfish and stubborn.”', 11.2, KIR)
    return svg(600, 104, ic, 'Verilen metinde yalnız Kaan’ın dış görünüşü anlatılıyor; öğrenci ise metne göre bencil ve inatçı olduğunu iddia ediyor.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = soru_cevap_kartlari()
    s[2]['gorsel'] = profil_panosu()
    s[4]['gorsel'] = comparative_kartlari()
    s[5]['gorsel'] = davranis_notlari()
    s[6]['gorsel'] = hata_duzeltme_karti()
    s[8]['gorsel'] = karsilastirma_tablosu()
    s[9]['gorsel'] = diyalog_karti()
    s[10]['gorsel'] = defne_karti()
    s[12]['gorsel'] = kanit_karti()
