"""10. sınıf Türk Dili ve Edebiyatı 2. hafta (Koşuk, Koşma, Türkü ve Ninni) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_nazim_bicimleri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    bicimler = [
        ('Koşuk', 'İslamiyet Öncesi', MAVI, MAVI_A),
        ('Koşma', 'Âşık Edebiyatı (11li)', YES, YES_A),
        ('Türkü', 'Bent & Kavuştak', TUR, TUR_A),
        ('Ninni', 'Anne şefkati / Ezgili', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(bicimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Dört Türk halk şiiri nazım biçimi', 34)


def g1_tapshirma():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += kutu(14, 12, 140, 76, '#d8f3e2', YES, 6, 1.2)
    ic += yazi(84, 28, 'TAPŞIRMA (MAHLAS)', 10, YES)
    ic += yazi(84, 48, 'Karac’oğlan der ki...', 9.5, LAC)
    ic += yazi(84, 70, 'Son Dörtlük İmzası', 9, TUR)

    ic += kutu(168, 12, 178, 76, '#eaf8f0', YES, 6, 1.2)
    ic += yazi(257, 28, 'Âşık Edebiyatı Geleneği', 10, YES)
    ic += yazi(257, 46, '• Şair adını son dörtlükte anar', 9, LAC, ince=True)
    ic += yazi(257, 60, '• Şiirin aidiyetini tesciller', 9, LAC, ince=True)
    ic += yazi(257, 74, '• Kopuzdan bağlamaya aktarım', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Halk şiirinde tapşırma ve mahlas geleneği', 34)


def g2_ses_degisimi():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ciftler = [
        ('tag', 'dağ'),
        ('yaşıl', 'yeşil'),
        ('buka', 'boğa'),
        ('edgü', 'iyi')
    ]
    for i, (eski, yeni) in enumerate(ciftler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#fef6ec', TUR, 6, 1.2)
        ic += yazi(x + 40, 30, eski, 11, KIR)
        ic += yazi(x + 40, 48, '↓', 12, TUR)
        ic += yazi(x + 40, 68, yeni, 11, YES)
    return svg(360, 100, ic, 'Türkçede tarihsel ses değişimi örnekleri', 34)


def g3_turku():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    ic += kutu(14, 12, 150, 76, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(89, 28, 'BENT BÖLÜMÜ', 10.5, CAM)
    ic += yazi(89, 48, 'Asıl konunun ve olayın', 9, LAC, ince=True)
    ic += yazi(89, 62, 'işlendiği 3-4 dizelik', 9, LAC, ince=True)
    ic += yazi(89, 76, 'değişen ana dörtlük', 9, LAC, ince=True)

    ic += kutu(176, 12, 170, 76, '#f2fbfd', CAM, 6, 1.2)
    ic += yazi(261, 28, 'KAVUŞTAK (BAĞLAMA)', 10.5, MOR)
    ic += yazi(261, 48, 'Her bendin sonunda', 9, LAC, ince=True)
    ic += yazi(261, 62, 'aynen yinelenen', 9, LAC, ince=True)
    ic += yazi(261, 76, 'nakarat bölümü', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Türkü nazım biçiminde bent ve kavuştak yapısı', 34)


def g5_cozumleme_akisi():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    adımlar = [
        ('1. Nazım Birimi', 'Dörtlük / Bent'),
        ('2. Ölçü', 'Hece sayısı & Durak'),
        ('3. Ahenk', 'Kafiye & Redif'),
        ('4. Anlam', 'Tema & İmgeler')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Şiir çözümleme aşamaları akış şeması', 34)


def g6_ahenk():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += kutu(14, 12, 150, 76, '#ece4fd', MOR, 6, 1.2)
    ic += yazi(89, 28, 'ALİTERASYON', 11, MOR)
    ic += yazi(89, 48, 'Aynı ünsüz seslerin', 9, LAC, ince=True)
    ic += yazi(89, 62, 'dizede müzikal', 9, LAC, ince=True)
    ic += yazi(89, 76, 'olarak tekrarlanması', 9, LAC, ince=True)

    ic += kutu(176, 12, 170, 76, '#f4effe', MOR, 6, 1.2)
    ic += yazi(261, 28, 'ASONANS', 11, TUR)
    ic += yazi(261, 48, 'Aynı ünlü seslerin', 9, LAC, ince=True)
    ic += yazi(261, 62, 'ahenk yaratacak', 9, LAC, ince=True)
    ic += yazi(261, 76, 'biçimde yinelenmesi', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Aliterasyon ve asonans ahenk karşılaştırması', 34)


def g8_kosma_turleri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    turler = [
        ('Güzelleme', 'Aşk & Doğa', MAVI, MAVI_A),
        ('Koçaklama', 'Yiğitlik & Savaş', KIR, KIR_A),
        ('Taşlama', 'Eleştiri & Yergi', TUR, TUR_A),
        ('Ağıt', 'Ölüm & Hüzün', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(turler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Koşmanın tematik dört ana türü', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: K - O - Ş - U - K', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'O'), ('3', 'Ş'), ('4', 'U'), ('5', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Koşuk şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_nazim_bicimleri()
    s[1]['gorsel'] = g1_tapshirma()
    s[2]['gorsel'] = g2_ses_degisimi()
    s[3]['gorsel'] = g3_turku()
    s[5]['gorsel'] = g5_cozumleme_akisi()
    s[6]['gorsel'] = g6_ahenk()
    s[8]['gorsel'] = g8_kosma_turleri()
    s[10]['gorsel'] = g10_sifre_seridi()
