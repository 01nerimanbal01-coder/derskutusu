"""11. sınıf Kimya 3. hafta (Maddelerin Enerji Kaynağı Potansiyeli) görselleri.
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


def yakit_turleri_kartlari():
    kartlar = [
        ('1. Hidrojen (H2)', '142 kJ/g &amp; Sıfır Karbon', YES, YES_A),
        ('2. Metan (CH4)', '55 kJ/g &amp; Temiz Fosil', MAVI, MAVI_A),
        ('3. Benzin (Sıvı)', '44 kJ/g &amp; CO2 Salımı', TUR, TUR_A),
        ('4. Kömür (Katı)', '18-25 kJ/g &amp; Kül &amp; Kükürt', KIR, KIR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Yakıt türleri ve ısıl değerleri kartı.', 34)


def isil_verim_sutunlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, '1 GRAM YAKITIN VERDİĞİ ENERJİ KARŞILAŞTIRMASI (kJ/g)', 9.8, YESIL_K)
    veriler = [
        ('H2 Gazı', '142 kJ/g', 16, YES),
        ('Doğal Gaz', '55 kJ/g', 102, MAVI),
        ('Petrol / Benzin', '44 kJ/g', 188, TUR),
        ('Linyit Kömür', '18 kJ/g', 274, KIR),
    ]
    for b, d, x, r in veriler:
        ic += kutu(x, 34, 70, 72, '#ffffff', r)
        ic += yazi(x + 35, 54, b, 8.4, r)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 78, d, 9.0, LAC)
        ic += yazi(x + 35, 94, 'Isıl Verim', 7.8, r, ince=True)
    return svg(360, 125, ic, 'Yakıtların gram başına enerji verimi sütunları.', 34)


def cevresel_etki_kesiti():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'FOSİL YAKIT ATIKLARI VE ÇEVRESEL SONUÇLARI', 10.0, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'CO2 Salınımı', 9.2, KIR)
    ic += yazi(92, 76, 'Sera gazı birikimi', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Küresel İklim Krizi', 8.6, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'SO2 ve NOx Salınımı', 9.2, TUR)
    ic += yazi(267, 76, 'Su buharıyla birleşme', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Asit Yağmurları Riski', 8.6, TUR, ince=True)
    return svg(360, 125, ic, 'Fosil yakıtların çevresel zararları şeması.', 34)


def hidrojen_temiz_dongusu():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'HİDROJEN ENERJİSİ VE SIFIR KARBON DÖNGÜSÜ', 10.0, MAVI)
    adımlar = [
        ('1. Su Elektrolizi', '2H2O -> 2H2 + O2', 16),
        ('2. H2 Depolama', 'Basınçlı tank veya sıvı', 102),
        ('3. Yakıt Pili / Yanma', '2H2 + O2 -> 2H2O', 188),
        ('4. Saf Su Çıktısı', 'Sıfır sera gazı atığı', 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MAVI)
        ic += yazi(x + 35, 54, b, 8.2, MAVI)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{MAVI}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Hidrojen temiz enerji döngüsü adımları.', 34)


def yakit_karsilastirma_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'YAKITLARIN ENERJİ VE ÇEVRESEL KARŞILAŞTIRMASI', 9.8, MOR)
    satirlar = [
        ('Yakıt Türü', 'Enerji (kJ/g)', 'Yanma Ürünü', 'Yenilenebilirlik', MOR),
        ('Hidrojen (H2)', '142 kJ/g', 'Yalnızca H2O (Saf)', 'Yenilenebilir', YESIL_K),
        ('Metan (CH4)', '55 kJ/g', 'CO2 + H2O', 'Fosil (Tükenir)', MAVI),
        ('Kömür (Katı)', '18-25 kJ/g', 'CO2 + SO2 + Kül', 'Fosil (Kirletici)', KIR),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.2, r)
        ic += yazi(130, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(215, y + 13, k3, 7.8, LAC, ince=(i > 0))
        ic += yazi(300, y + 13, k4, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Yakıtlar karşılaştırma tablosu.', 34)


def biyoetanol_karbon_dongusu():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'BİYOETANOL: KARBON NÖTR ENERJİ MODELİ', 10.0, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Bitki Büyüme Evresi', 9.2, YESIL_K)
    ic += yazi(92, 76, 'CO2 havadan emilir', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Fotosentezle şeker üretimi', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, 'Yakıt Yanma Evresi', 9.2, TUR)
    ic += yazi(267, 76, 'Aynı CO2 geri salınır', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Net Karbon Dengesi: Sıfır', 8.6, TUR, ince=True)
    return svg(360, 125, ic, 'Biyoetanol karbon nötr döngüsü.', 34)


def yanma_entalpisi_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'YANMA TEPKİMESİ ENERJİ KRİTERLERİ', 10.0, TUR)
    kartlar = [
        ('1. Tutuşma Sıcaklığı', 'Düşük aktivasyon enerjisi', 16),
        ('2. Egzotermik Isı', 'Yüksek negatif ΔH değeri', 102),
        ('3. Kararlı Ürünler', 'Düşük potansiyel enerjili bağ', 188),
        ('4. Depolama Güvenliği', 'Kolay nakliye &amp; muhafaza', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Yanma tepkimesi kriter kartları.', 34)


def temiz_enerji_gecis_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, 'SÜRDÜRÜLEBİLİR TEMİZ ENERJİ DÖNÜŞÜM ADIMLARI', 9.8, CAM)
    kutular = ['Fosil Tasarrufu', 'Biyokütle &amp; Güneş', 'Hidrojen Ağı', 'Net Sıfır Karbon']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', CAM, r=4)
        ic += yazi(x + 37, 66, f'Faz {i + 1}', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.2, CAM)
    return svg(360, 125, ic, 'Temiz enerji dönüşüm akış kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = yakit_turleri_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = isil_verim_sutunlari()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = cevresel_etki_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = hidrojen_temiz_dongusu()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = yakit_karsilastirma_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = biyoetanol_karbon_dongusu()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = yanma_entalpisi_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = temiz_enerji_gecis_kutulari()
    s[10]['en_fazla'] = 34
