"""11. sınıf Kimya 2. hafta görselleri.
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
        ('1. Hidrojen (H2)', '142 kJ/g · Sıfır CO2', YES, YES_A),
        ('2. Metan (CH4)', '55 kJ/g · Temiz Gaz', MAVI, MAVI_A),
        ('3. Kömür', '20 kJ/g · Yüksek Kül', TUR, TUR_A),
        ('4. Biyoetanol', 'Yenilenebilir Sıvı', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Yakıt türleri ve ısıl değer kartları.', 34)

def hidrojen_temiz_enerji_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'HİDROJEN YAKITI VE FOSİL YAKIT KARŞILAŞTIRMASI', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Hidrojen Yanması (H2)', 9.4, YESIL_K)
    ic += yazi(92, 76, '2H2 + O2 → 2H2O + Isı', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Sıfır Karbon · Temiz Su', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, KIR_A, KIR)
    ic += yazi(267, 56, 'Kömür Yanması (Fosil)', 9.4, KIR)
    ic += yazi(267, 76, 'C + O2 → CO2 + Kül', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Sera Gazı · Asit Yağmuru', 8.8, KIR, ince=True)
    return svg(360, 125, ic, 'Hidrojen ve kömür yanma ürünleri modeli.', 34)

def termodinamik_1yasa_modeli():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'TERMODİNAMİĞİN 1. YASASI: ENERJİNİN KORUNUMU', 10.3, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Kimyasal Potansiyel Enerji', 9.4, CAM)
    ic += yazi(92, 76, 'Yakıt bağlarında depolanan', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'E(toplam) = Sabit', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Dönüşen Enerji Türleri', 9.4, TUR)
    ic += yazi(267, 76, 'Q (Isı) + W (Mekanik İş)', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Yoktan var / vardan yok olmaz', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Termodinamik 1. yasa enerji korunum modeli.', 34)

def besin_enerji_degerleri():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'FİZYOLOJİK BESİN ENERJİ DEĞERLERİ (1 GRAM)', 10.3, TUR)
    ic += kutu(20, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(67, 58, 'Karbonhidrat', 9.4, TUR)
    ic += yazi(67, 78, '4 kcal / gram', 8.8, LAC, ince=True)
    ic += yazi(67, 92, '(17 kJ / g)', 8.8, TUR, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', YES)
    ic += yazi(179, 58, 'Protein', 9.4, YESIL_K)
    ic += yazi(179, 78, '4 kcal / gram', 8.8, LAC, ince=True)
    ic += yazi(179, 92, '(17 kJ / g)', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', KIR)
    ic += yazi(292, 58, 'Yağ (Lipit)', 9.4, KIR)
    ic += yazi(292, 78, '9 kcal / gram', 8.8, LAC, ince=True)
    ic += yazi(292, 92, '(38 kJ / g - En Yüksek)', 8.8, KIR, ince=True)
    return svg(360, 125, ic, 'Besinlerin fizyolojik enerji değerleri kartı.', 34)

def bomba_kalorimetresi_adimlari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'BOMBA KALORİMETRESİ İLE ISIL DEĞER TAYİNİ', 10.2, MOR)
    adımlar = [
        ('1. Tartım', 'Numune Alımı', 16),
        ('2. Tutuşturma', 'O2 Atmosferi', 102),
        ('3. Sıcaklık', 'ΔT Kaydı', 188),
        ('4. Hesap', 'Q = C · ΔT', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Kalorimetre ısıl değer tayin basamakları.', 34)

def yag_enerji_hesap_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, '10 GRAM YAĞIN ENERJİ POTANSİYELİ HESABI', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Birim Enerji Verisi', 9.6, YESIL_K)
    ic += yazi(92, 76, '1 gram yağ ≈ 9 kcal', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Hücresel oksidasyon', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Toplam Enerji Çıktısı', 9.6, TUR)
    ic += yazi(267, 76, '10 g · 9 kcal/g = 90 kcal', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Karbonhidrattan 2 kat fazla', 8.8, TUR, ince=True)
    return svg(360, 125, ic, '10 gram yağ enerji hesabı modeli.', 34)

def isil_deger_karsilastirma_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'YAKITLARIN BİRİM KÜTLE BAŞINA ISIL DEĞERLERİ', 10.1, YESIL_K)
    kartlar = [
        ('Hidrojen (H2)', '142 kJ / g', 16),
        ('Metan (CH4)', '55 kJ / g', 102),
        ('Linyit Kömürü', '18 kJ / g', 188),
        ('Kuru Odun', '16 kJ / g', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Yakıt ısıl değerleri karşılaştırma tablosu.', 34)

def yakit_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, CAM)
    harfler = ['Y', 'A', 'K', 'I', 'T']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', CAM, r=4)
        ic += yazi(x + 22, 74, h, 16.0, CAM)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Yakıt kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = yakit_turleri_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = hidrojen_temiz_enerji_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = termodinamik_1yasa_modeli()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = besin_enerji_degerleri()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = bomba_kalorimetresi_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = yag_enerji_hesap_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = isil_deger_karsilastirma_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = yakit_sifre_kutulari()
    s[10]['en_fazla'] = 34
