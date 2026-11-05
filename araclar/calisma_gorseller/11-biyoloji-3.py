"""11. sınıf Biyoloji 3. hafta (Tropizma ve Nasti Hareketleri) görselleri.
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


def bitki_tepki_kartlari():
    kartlar = [
        ('1. Fototropizma', 'Işığa Yönelim', YES, YES_A),
        ('2. Jeotropizma', 'Yerçekimi Tepkisi', TUR, TUR_A),
        ('3. Tigmotropizma', 'Temasa Sarılma', MAVI, MAVI_A),
        ('4. Sismonasti', 'Sarsıntı &amp; Turgor', KIR, KIR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.8, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Bitkilerde temel tropizma ve nasti kartları.', 34)


def jeotropizma_fide_kesiti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'YATAY KONUMDAKİ FİDEDE ASİMETRİK OKSİN VE JEOTROPİZMA', 9.8, TUR)
    ic += kutu(16, 36, 150, 72, '#ffffff', YES)
    ic += yazi(91, 56, 'Gövde (Negatif Jeotropizma)', 9.0, YESIL_K)
    ic += yazi(91, 74, 'Alt yüzeyde oksin birikir', 8.4, LAC, ince=True)
    ic += yazi(91, 92, 'Hücreler uzar, yukarı bükülür', 8.4, YES, ince=True)
    ic += kutu(194, 36, 150, 72, '#ffffff', TUR)
    ic += yazi(269, 56, 'Kök (Pozitif Jeotropizma)', 9.0, TUR)
    ic += yazi(269, 74, 'Alt yüzeyde oksin birikir', 8.4, LAC, ince=True)
    ic += yazi(269, 92, 'Uzama baskılanır, aşağı bükülür', 8.4, KIR, ince=True)
    return svg(360, 125, ic, 'Fidede yerçekimi etkisiyle oksin dağılımı.', 34)


def nasti_turgor_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'NASTİ HAREKETİ VE ANİ TURGOR DEĞİŞİMİ', 10.2, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Uyarılmadan Önce', 9.4, KIR)
    ic += yazi(92, 76, 'K+ iyonları hücre içinde', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Yüksek Turgor -> Dik Durur', 8.6, YES, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(267, 56, 'Dokunma / Uyarı Sonrası', 9.4, KIR)
    ic += yazi(267, 76, 'K+ iyonları dışarı çıkar', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Turgor Düşer -> Yaprak Kapanır', 8.6, KIR, ince=True)
    return svg(360, 125, ic, 'Turgor basıncı değişimine bağlı nasti şeması.', 34)


def tigmotropizma_sarilma_semasi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'TİGMOTROPİZMA: DESTEĞE TEMAS VE SARILMA', 10.0, MAVI)
    adımlar = [
        ('1. Destek Teması', 'Sülük desteğe dokunur', 16),
        ('2. Oksin Göçü', 'Dış tarafa oksin aktarılır', 102),
        ('3. Asimetrik Uzama', 'Dış çeper daha hızlı uzar', 188),
        ('4. Helezon Sarılma', 'Destek etrafına kilitlenir', 274),
    ]
    for baslik, acik, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MAVI)
        ic += yazi(x + 35, 54, baslik, 8.4, MAVI)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{MAVI}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, acik, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Tigmotropizma sarılma basamakları şeması.', 34)


def tropizma_nasti_karsilastirma():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'TROPİZMA VE NASTİ HAREKETLERİNİN KARŞILAŞTIRILMASI', 9.8, YESIL_K)
    satirlar = [
        ('Özellik', 'Tropizma (Yönelim)', 'Nasti (Irganım)', YES),
        ('Uyaran Yönü', 'Bağımlıdır (+ / -)', 'Bağımsızdır (Yönsüz)', MAVI),
        ('Temel Neden', 'Asimetrik Oksin ve Büyüme', 'Turgor Basıncı Değişimi', TUR),
        ('Hız Düzeyi', 'Yavaş (Günler / Haftalar)', 'Çok Hızlı (Saniyeler)', KIR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else YES_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(70, y + 13, k1, 8.4, r)
        ic += yazi(180, y + 13, k2, 8.2, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.2, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Tropizma ve nasti karşılaştırma tablosu.', 34)


def kok_hidro_kemo_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'KÖKTE HİDROTROPİZMA VE KEMOTROPİZMA', 10.2, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, '+ Hidrotropizma', 9.4, CAM)
    ic += yazi(92, 76, 'Kök suya doğru yönelir', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Nem gradyenti izlenir', 8.6, YESIL_K, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(267, 56, '- Kemotropizma', 9.4, TUR)
    ic += yazi(267, 76, 'Aşırı tuzdan uzaklaşır', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Zararlı kimyasaldan kaçış', 8.6, KIR, ince=True)
    return svg(360, 125, ic, 'Kökün su ve kimyasallara tepki şeması.', 34)


def termonasti_lale_dongusu():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'TERMONASTİ: LALE ÇİÇEĞİNDE SICAKLIK TEPKİSİ', 10.0, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Düşük Sıcaklık (15 °C)', 9.2, MAVI)
    ic += yazi(92, 76, 'Dış yüzey turgoru artar', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Çiçek Kapalı Konumda', 8.6, LAC, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(267, 56, 'Yüksek Sıcaklık (22 °C)', 9.2, KIR)
    ic += yazi(267, 76, 'İç yüzey turgoru artar', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Çiçek Açık Konuma Geçer', 8.6, YES, ince=True)
    return svg(360, 125, ic, 'Termonasti sıcaklık döngüsü kartı.', 34)


def turgor_iyon_akisi_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'MOTOR HÜCRELERDE İYON AKIŞI VE TURGOR MEKANİZMASI', 9.8, MOR)
    adımlar = [
        ('1. Potasyum Girişi', 'K+ iyonları içeri akar', 16),
        ('2. Ozmotik Çekim', 'Su hücreye difüze olur', 102),
        ('3. Basınç Artışı', 'Turgor basıncı yükselir', 188),
        ('4. Mekanik Hareket', 'Organ dik konuma gelir', 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 54, b, 8.2, MOR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Motor hücrelerde iyon ve turgor şeması.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bitki_tepki_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = jeotropizma_fide_kesiti()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = nasti_turgor_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = tigmotropizma_sarilma_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = tropizma_nasti_karsilastirma()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = kok_hidro_kemo_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = termonasti_lale_dongusu()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = turgor_iyon_akisi_semasi()
    s[10]['en_fazla'] = 34
