"""5. sınıf Matematik 6. hafta (Çokgenlerin Kenar ve Açı Özellikleri: Üçgen ve Dörtgen Çeşitleri ile Çokgen Deneyimleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def klm_ucgeni_sema():
    ic = kutu(6, 6, 588, 92, KUM, GRI, 9, 1.4)
    ic += f'<polygon points="150,18 75,84 225,84" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(150, 14, 'K (70°)', MAVI, kalin=True)
    ic += yazi(52, 88, 'L (55°)', LAC, kalin=True)
    ic += yazi(250, 88, 'M (55°)', LAC, kalin=True)
    ic += yazi(96, 50, '10 cm', MAVI, kalin=True)
    ic += yazi(204, 50, '10 cm', MAVI, kalin=True)
    ic += yazi(150, 94, '11 cm', LAC)

    ic += kutu(305, 16, 275, 72, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(442, 36, 'KLM Üçgeni Ölçüm Verileri', MAVI, kalin=True)
    ic += yazi(442, 57, 'Kenarlar: |KL| = 10 cm, |KM| = 10 cm, |LM| = 11 cm', LAC)
    ic += yazi(442, 77, 'İç Açılar: 55°, 55° ve 70° (Tümü < 90°)', LAC)
    return svg(600, 104, ic, 'Kenarları 10 cm, 10 cm, 11 cm ve açıları 55, 55, 70 derece olan KLM üçgeni.', 21)


def duzgun_cokgen_secim_kartlari():
    kartlar = [
        ('1. Kart: Dikdörtgen', 'Açıları 90° · Kenarları farklı', MAVI, MAVI_A),
        ('2. Kart: Eşkenar Dörtgen', '4 kenarı eşit · Açıları farklı', TUR, TUR_A),
        ('3. Kart: Düzgün Altıgen', '6 eş kenar · 6 eş açı (120°)', YES, YES_A),
        ('4. Kart: Dik İkizkenar Üçgen', 'Açıları: 45° - 45° - 90°', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dikdörtgen, eşkenar dörtgen, düzgün altıgen ve dik ikizkenar üçgen kartları.', 21)


def cokgen_eleman_kartlari():
    kartlar = [
        ('1. Üçgen', 'n = 3 kenar · n - 3 = 0', MAVI, MAVI_A),
        ('2. Dörtgen', 'n = 4 kenar · n - 3 = 1', YES, YES_A),
        ('3. Beşgen', 'n = 5 kenar · n - 3 = 2', TUR, TUR_A),
        ('4. Altıgen', 'n = 6 kenar · n - 3 = 3', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 82, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 62, alt, LAC, kalin=True)
    return svg(600, 94, ic, 'Üçgen, dörtgen, beşgen ve altıgenin kenar ve bir köşeden köşegen kartları.', 21)


def marangoz_cerceve_sema():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += f'<rect x="55" y="18" width="160" height="64" fill="{TUR_A}" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<line x1="55" y1="18" x2="215" y2="82" stroke="{KIR}" stroke-width="2.4" stroke-dasharray="5,3"/>'
    ic += yazi(42, 22, 'A', LAC, kalin=True)
    ic += yazi(228, 22, 'B', LAC, kalin=True)
    ic += yazi(228, 86, 'C', LAC, kalin=True)
    ic += yazi(42, 86, 'D', LAC, kalin=True)
    ic += yazi(135, 46, 'Çapraz Çıta [AC]', KIR, kalin=True)

    ic += kutu(265, 16, 315, 68, YES_A, YES, 8, 1.4)
    ic += yazi(422, 36, 'Marangozun Kitaplık Çerçevesi', YESIL_K, kalin=True)
    ic += yazi(422, 56, '[AC] çıtası komşu olmayan iki köşeyi birleştirir', LAC)
    ic += yazi(422, 75, 'Çerçeve 2 adet dik açılı üçgene bölünür', LAC)
    return svg(600, 100, ic, 'ABCD dikdörtgen çerçevesine çakılan AC köşegen çıtası şeması.', 21)


def kosegen_siralama_kartlari():
    kartlar = [
        ('Üçgen', 'Toplam: 0 köşegen', MAVI, MAVI_A),
        ('Dörtgen', 'Toplam: 2 köşegen', YES, YES_A),
        ('Beşgen', 'Toplam: 5 köşegen', TUR, TUR_A),
        ('Altıgen', 'Toplam: 9 köşegen', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += yazi(x + 70, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 12}" y1="38" x2="{x + 128}" y2="38" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 70, 62, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Üçgen, dörtgen, beşgen ve altıgenin toplam köşegen sayısı kartları.', 21)


def prs_dik_ucgen_karti():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += f'<polygon points="65,20 65,82 225,82" fill="{MOR_A}" stroke="{MOR}" stroke-width="2"/>'
    ic += f'<rect x="65" y="70" width="12" height="12" fill="none" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(50, 84, 'P (90°)', KIR, kalin=True)
    ic += yazi(50, 24, 'R (38°)', MOR, kalin=True)
    ic += yazi(252, 84, 'S (?°)', LAC, kalin=True)

    ic += kutu(295, 16, 285, 68, MOR_A, MOR, 8, 1.4)
    ic += yazi(437, 36, 'PRS Dik Açılı Üçgeni', MOR, kalin=True)
    ic += yazi(437, 56, 'm(P) = 90° · m(R) = 38° · m(S) = ?', LAC, kalin=True)
    ic += yazi(437, 75, 'İç açılar toplamı = 180° (Üç açı da farklı)', LAC)
    return svg(600, 100, ic, 'Açıları 90 derece, 38 derece ve soru işareti olan PRS dik üçgeni.', 21)


def kare_eskenar_dortgen_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 25, 'Kare (Düzgün Dörtgen)', MAVI, kalin=True)
    ic += yazi(149, 50, '4 kenar uzunluğu birbirine eşit', LAC, kalin=True)
    ic += yazi(149, 74, '4 iç açısının ölçüsü de 90° (Eşit)', LAC)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(451, 25, 'Eşkenar Dörtgen', TUR, kalin=True)
    ic += yazi(451, 50, '4 kenar uzunluğu birbirine eşit', LAC, kalin=True)
    ic += yazi(451, 74, '2 dar açısı ve 2 geniş açısı var', LAC)
    return svg(600, 98, ic, 'Kare ve eşkenar dörtgenin kenar ve açı karşılaştırma kartı.', 21)


def ozel_dortgenler_panosu():
    kartlar = [
        ('Kare & Dikdörtgen', 'Açıları 90° · Köşegenleri eşit', MAVI, MAVI_A),
        ('Paralelkenar', 'Karşılıklı kenar ve açıları eşit', YES, YES_A),
        ('İkizkenar Üçgen', 'Eşit kenarları gören açılar eşit', TUR, TUR_A),
        ('Dörtgende Köşegen', '1 köşeden 1, toplam 2 köşegen', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Özel dörtgenler ve üçgen özelliklerini özetleyen dörtlü pano.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = klm_ucgeni_sema()
    s[4]['gorsel'] = duzgun_cokgen_secim_kartlari()
    s[5]['gorsel'] = cokgen_eleman_kartlari()
    s[6]['gorsel'] = marangoz_cerceve_sema()
    s[7]['gorsel'] = kosegen_siralama_kartlari()
    s[8]['gorsel'] = prs_dik_ucgen_karti()
    s[10]['gorsel'] = kare_eskenar_dortgen_karti()
    s[11]['gorsel'] = ozel_dortgenler_panosu()
