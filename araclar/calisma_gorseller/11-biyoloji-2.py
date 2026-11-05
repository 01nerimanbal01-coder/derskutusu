"""11. sınıf Biyoloji 2. hafta (Bitkisel Hormonlar ve Tepkiler) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def hormon_kartlari():
    kartlar = [
        ('1. Oksin', 'Büyüme &amp; Yönelim', YES, YES_A),
        ('2. Sitokinin', 'Bölünme &amp; Gençlik', MAVI, MAVI_A),
        ('3. ABA (Stres)', 'Dormansi &amp; Stoma', TUR, TUR_A),
        ('4. Etilen Gazı', 'Meyve Olgunlaşması', KIR, KIR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Bitkisel hormonlar ve işlevleri kartı.', 34)


def fototropizma_koleoptil_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'FOTOTROPİZMA VE ASİMETRİK OKSİN BİRİKİMİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Işık Alan Taraf', 9.4, TUR)
    ic += yazi(92, 76, 'Oksin gölgeye kaçar', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Hücre uzaması yavaş', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, '#ffffff', YESIL_K)
    ic += yazi(267, 56, 'Gölge Taraf (Karanlık)', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Yoğun oksin birikimi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Hızlı uzama → Işığa bükülme', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Fototropizmada asimetrik oksin dağılımı şeması.', 34)


def nasti_turgor_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'NASTİ HAREKETİ VE TURGOR BASINCI DEĞİŞİMİ', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Açık Durum (Normal)', 9.6, CAM)
    ic += yazi(92, 76, 'Yüksek turgor basıncı', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Yaprakçıklar dik ve açık', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Dokunma Sonrası (Uyarılmış)', 9.6, TUR)
    ic += yazi(267, 76, 'Ani su kaybı &amp; kofullar boşalır', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Hızlı kapanma (Sismonasti)', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Nasti turgor basıncı mekanizması modeli.', 34)


def tropizma_nasti_karsilastirma():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'TROPİZMA VE NASTİ HAREKETLERİNİN FARK KARTLARI', 10.3, MOR)
    ic += kutu(20, 38, 145, 68, '#ffffff', MOR)
    ic += yazi(92, 58, 'TROPİZMA (Yönelim)', 9.6, MOR)
    ic += yazi(92, 78, 'Uyaranın yönüne bağlıdır', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Hormonal asimetrik büyüme', 8.8, MOR, ince=True)

    ic += kutu(195, 38, 145, 68, YES_A, YES)
    ic += yazi(267, 58, 'NASTİ (Irganım)', 9.6, YESIL_K)
    ic += yazi(267, 78, 'Uyaranın yönüne bağlı değildir', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Turgor basıncıyla ani tepki', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Tropizma ve nasti temel farkları şeması.', 34)


def cimlenme_hormon_basamaklari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 20, 'ÇİMLENMEDE HORMONAL KONTROL SIRASI', 10.2, TUR)
    adımlar = [
        ('1. Adım', 'ABA Azalır', 16),
        ('2. Adım', 'Giberellin Artar', 102),
        ('3. Adım', 'Oksin &amp; Bölünme', 188),
        ('4. Adım', 'Etilen &amp; Olgunluk', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 56, b, 9.3, TUR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Tohum çimlenmesi hormonal adımları.', 34)


def etilen_olgunlasma_deneyi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'ETİLEN GAZI VE MEYVE OLGUNLAŞMA ETKİSİ', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Olgun Elma (Kaynak)', 9.4, KIR)
    ic += yazi(92, 76, 'Yoğun etilen gazı salgılar', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Hücre çeperini yumuşatır', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Ham Muzlar (Hedef)', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Etilen gazını absorbe eder', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Hızla sararır &amp; tatlanır', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Etilen gazı olgunlaştırma etkisi şeması.', 34)


def hareket_turleri_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'BİTKİSEL TEPKİ MEKANİZMALARI TANIMLARI', 10.1, YESIL_K)
    kartlar = [
        ('Fototropizma', 'Işığa Yönelim', 16),
        ('Geotropizma', 'Yer Çekimi Bağı', 102),
        ('Termonasti', 'Sıcaklıkla Açılma', 188),
        ('Kemotropizma', 'Kimyasala Yönelim', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Bitkisel hareket türleri kartı.', 34)


def hormon_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['H', 'O', 'R', 'M', 'O', 'N']
    for i, h in enumerate(harfler):
        x = 42 + i * 46
        ic += kutu(x, 42, 40, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 20, 74, h, 16.0, MAVI)
        ic += yazi(x + 20, 36, f'{i + 1}. Harf', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Hormon kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = hormon_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = fototropizma_koleoptil_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = nasti_turgor_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = tropizma_nasti_karsilastirma()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = cimlenme_hormon_basamaklari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = etilen_olgunlasma_deneyi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = hareket_turleri_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = hormon_sifre_kutulari()
    s[10]['en_fazla'] = 34
