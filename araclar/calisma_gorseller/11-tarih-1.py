"""11. sınıf Tarih 1. hafta (II. Viyana'dan Karlofça'ya) görselleri.
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


def kutsal_ittifak_toprak_kartlari():
    kartlar = [
        ('1. Avusturya', 'Macaristan &amp; Erdel', MAVI, MAVI_A),
        ('2. Lehistan', 'Podolya &amp; Kamaniçe', TUR, TUR_A),
        ('3. Venedik', 'Mora &amp; Dalmaçya', YES, YES_A),
        ('4. Rusya', 'Azak Kalesi (1700)', KIR, KIR_A),
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
    return svg(360, 125, ic, 'Kutsal İttifak devletleri ve toprak kayıpları kartı.', 34)


def viyana_sonrasi_ittifak_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, '1683 II. VİYANA SONRASI KUTSAL İTTİFAK OLUŞUMU', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Papa Öncülüğünde Birlik', 9.4, KIR)
    ic += yazi(92, 76, 'Avusturya, Rusya, Lehistan,', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Venedik ve Malta İttifakı', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Çok Cepheli 16 Yıl', 9.4, TUR)
    ic += yazi(267, 76, '1683-1699 Osmanlı Mücadelesi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Ağır Hazine ve Asker Kaybı', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Kutsal İttifak ve çok cepheli savaş şeması.', 34)


def tarihsel_zaman_cizgisi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, '1683-1699 SAVAŞ VE DİPLOMASİ ZAMAN ÇİZELGESİ', 10.2, CAM)
    adımlar = [
        ('1683', 'II. Viyana Bozgunu', 16),
        ('1684', 'Kutsal İttifak', 102),
        ('1697', 'Zenta Yenilgisi', 188),
        ('1699', 'Karlofça Barışı', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.4, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Tarihsel zaman çizelgesi şeması.', 34)


def cepheler_harita_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'OSMANLI DEVLETİ 16 YILLIK ÇOK CEPHELİ SAVAŞLARI', 10.3, TUR)
    ic += kutu(20, 38, 145, 68, '#ffffff', TUR)
    ic += yazi(92, 58, 'Batı &amp; Deniz Cepheleri', 9.6, TUR)
    ic += yazi(92, 78, 'Macaristan (Avusturya)', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Mora &amp; Dalmaçya (Venedik)', 8.8, TUR, ince=True)

    ic += kutu(195, 38, 145, 68, MAVI_A, MAVI)
    ic += yazi(267, 58, 'Kuzey &amp; Doğu Cepheleri', 9.6, MAVI)
    ic += yazi(267, 78, 'Podolya (Lehistan)', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Azak &amp; Kırım (Rusya)', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Çok cepheli savaş coğrafyası modeli.', 34)


def karlofca_surec_adimlari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "VİYANA KUŞATMASINDAN KARLOFÇA'YA ADIMLAR", 10.2, MOR)
    adımlar = [
        ('1. Adım', '1683 Kuşatma', 16),
        ('2. Adım', '1684 İttifak', 102),
        ('3. Adım', '1697 Zenta', 188),
        ('4. Adım', '1699 Karlofça', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Karlofça süreci kronolojik basamakları.', 34)


def karlofca_sonuclari_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'KARLOFÇA ANTLAŞMASI STRATEJİK DEĞİŞİMİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YESIL_K)
    ic += yazi(92, 56, '1683 Öncesi Dönem', 9.6, TUR)
    ic += yazi(92, 76, 'Askerî taarruz üstünlüğü', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Genişleme &amp; fetih siyaseti', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, KIR_A, KIR)
    ic += yazi(267, 56, '1699 Sonrası Dönem', 9.6, KIR)
    ic += yazi(267, 76, 'Savunma &amp; geri çekilme', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Mevcut toprakları koruma', 8.8, KIR, ince=True)
    return svg(360, 125, ic, 'Karlofça antlaşması stratejik sonuçları.', 34)


def antlasma_madde_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'ANTLAŞMA MADDELERİ VE TARİHSEL ETKİLERİ', 10.1, YESIL_K)
    kartlar = [
        ('25 Yıl Garanti', 'Avusturya Garantisi', 16),
        ("Azak Kalesi", "Rusya Karadeniz'de", 102),
        ('Podolya Terki', 'Lehistan Hattı', 188),
        ('Mora Terki', 'Venedik Nüfuzu', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Antlaşma maddeleri eşleştirme kartı.', 34)


def zenta_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, TUR)
    harfler = ['Z', 'E', 'N', 'T', 'A']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 22, 74, h, 16.0, TUR)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Zenta kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kutsal_ittifak_toprak_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = viyana_sonrasi_ittifak_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = tarihsel_zaman_cizgisi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = cepheler_harita_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = karlofca_surec_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = karlofca_sonuclari_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = antlasma_madde_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = zenta_sifre_kutulari()
    s[10]['en_fazla'] = 34
