"""8. sınıf Fen Bilimleri 3. hafta (İklim ve Hava Hareketleri: hava olayları, yağış/çiy/kırağı/sis, alçak-yüksek basınç ve rüzgâr, iklim ve hava olayları farkı) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10.5, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def basinc_ruzgar_sema():
    ic = f'<rect x="6" y="6" width="276" height="122" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += rozet(26, 24, 'K', TUR)
    ic += yazi(150, 26, 'K Bölgesi (Isınan Hava)', 11.5, TUR)
    # Bulut ve yağmur
    ic += f'<rect x="92" y="36" width="104" height="20" rx="10" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(144, 50, 'Bulutlu ve Yağışlı', 10.2, MAVI)
    # Yükselici ok
    ic += f'<line x1="144" y1="98" x2="144" y2="62" stroke="{TUR}" stroke-width="2.6"/>'
    ic += f'<polygon points="144,56 138,65 150,65" fill="{TUR}"/>'
    ic += yazi(196, 82, 'Yükselici hava', 10.8, TUR, 'start')
    ic += yazi(144, 116, 'Çevreden merkeze hava akışı', 10.8, LAC, ince=True)

    # Sağ kutu: L bölgesi
    ic += f'<rect x="318" y="6" width="276" height="122" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += rozet(338, 24, 'L', MAVI)
    ic += yazi(462, 26, 'L Bölgesi (Soğuyan Hava)', 11.5, MAVI)
    ic += f'<circle cx="456" cy="46" r="10" fill="#f5c421" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(512, 50, 'Hava açık', 10.8, TUR, 'start')
    # Alçalıcı ok
    ic += f'<line x1="456" y1="62" x2="456" y2="96" stroke="{MAVI}" stroke-width="2.6"/>'
    ic += f'<polygon points="456,102 450,93 462,93" fill="{MAVI}"/>'
    ic += yazi(508, 82, 'Alçalıcı hava', 10.8, MAVI, 'start')
    ic += yazi(456, 116, 'Merkezden çevreye hava akışı', 10.8, LAC, ince=True)

    # L -> K rüzgâr oku
    ic += f'<line x1="316" y1="68" x2="286" y2="68" stroke="{YESIL_K}" stroke-width="3"/>'
    ic += f'<polygon points="282,68 291,62 291,74" fill="{YESIL_K}"/>'
    return svg(600, 134, ic, 'K bölgesi (yükselici hava, bulutlu) ve L bölgesi (alçalıcı hava, açık gökyüzü) arasında L den K ye yatay rüzgâr akışı.', 18)


def yogusma_siniflama_tablosu():
    gruplar = [
        ('1. Grup · Yeryüzüne İner (Yağış)', 'Yağmur: Sıvı su damlaları', 'Dolu: 5–50 mm buz küreleri', 'Kar: Küçük buz kristalleri', MAVI, MAVI_A),
        ('2. Grup · Soğuk Yüzeyde Birikir', 'Çiy: Yoğuşan sıvı damlacıklar', 'Kırağı: 0 °C altında doğrudan', '  buza dönüşen kristaller', YES, YES_A),
        ('3. Grup · Havada Asılı Kalır', 'Sis: Yere yakın tabakada', '  asılı kalan su damlacıkları', '  veya buz kristalleri', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, s3, renk, arka) in enumerate(gruplar):
        x = 6 + i * 198
        ic += f'<rect x="{x}" y="6" width="192" height="106" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 96, 24, bas, 10.8, renk)
        ic += f'<line x1="{x + 12}" y1="32" x2="{x + 180}" y2="32" stroke="{renk}" stroke-width="1.1"/>'
        ic += yazi(x + 14, 52, s1, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 14, 72, s2, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 14, 92, s3, 10.6, LAC, 'start', ince=True)
    return svg(600, 118, ic, 'Yağış (yağmur, dolu, kar), yüzeyde birikenler (çiy, kırağı) ve yere yakın havada asılı kalan (sis) sınıflandırma şeması.', 18)


def hava_iklim_olcut_kartlari():
    ic = f'<rect x="6" y="6" width="286" height="104" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Hava Olayları Kartı', 11.5, TUR)
    ic += yazi(20, 45, 'Alan: Sınırlı (dar) bir yer', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 63, 'Süre ve Veri: Kısa süre, gün içi gözlemler', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 81, 'Değişkenlik: Fazla (tahmine dayanır)', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 99, 'Sözcükler: Yağmurlu, güneşli, rüzgârlı', 10.8, TUR, 'start')

    ic += f'<rect x="308" y="6" width="286" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'İklim Özelliği Kartı', 11.5, MAVI)
    ic += yazi(322, 45, 'Alan: Geniş bir bölge', 10.8, LAC, 'start', ince=True)
    ic += yazi(322, 63, 'Süre ve Veri: En az 35–40 yıllık ortalama', 10.8, LAC, 'start', ince=True)
    ic += yazi(322, 81, 'Değişkenlik: Az (daha kesin bilgi verir)', 10.8, LAC, 'start', ince=True)
    ic += yazi(322, 99, 'Sözcükler: Sıcak, soğuk, kurak, yağışlı', 10.8, MAVI, 'start')
    return svg(600, 116, ic, 'Hava olayları ve iklim karşılaştırma kartları: alan, süre, veri, değişkenlik ve kullanılan sözcükler.', 18)


def iki_sehir_sicaklik_karti():
    ic = f'<rect x="6" y="6" width="272" height="96" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += rozet(26, 24, 'P', MAVI)
    ic += yazi(148, 25, 'P Kenti Gözlem Verisi', 11.5, MAVI)
    ic += yazi(22, 48, 'Hava sıcaklığı: 14 °C (Soğuk)', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 68, 'Hava molekülleri alçalıyor', 10.8, LAC, 'start', ince=True)
    ic += yazi(22, 88, 'Yüzeydeki hava yoğunluğu fazla', 10.8, MAVI, 'start')

    ic += f'<line x1="284" y1="54" x2="316" y2="54" stroke="{GRI}" stroke-width="2" stroke-dasharray="4 3"/>'
    ic += yazi(300, 44, 'Rüzgâr?', 10.5, LAC)

    ic += f'<rect x="322" y="6" width="272" height="96" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += rozet(342, 24, 'R', TUR)
    ic += yazi(464, 25, 'R Kenti Gözlem Verisi', 11.5, TUR)
    ic += yazi(338, 48, 'Hava sıcaklığı: 29 °C (Sıcak)', 10.8, LAC, 'start', ince=True)
    ic += yazi(338, 68, 'Hava molekülleri yükseliyor', 10.8, LAC, 'start', ince=True)
    ic += yazi(338, 88, 'Yüzeydeki hava yoğunluğu az', 10.8, TUR, 'start')
    return svg(600, 108, ic, 'P kenti (14 derece, alçalıcı hava, yoğunluk fazla) ve R kenti (29 derece, yükselici hava, yoğunluk az) karşılaştırması.', 18)


def yagmur_olusum_akisi():
    adlar = [
        ('1. Aşama', 'Isınma ve Hız', TUR, TUR_A),
        ('2. Aşama', 'Alçak Basınç', MOR, MOR_A),
        ('3. Aşama', 'Rüzgâr Akışı', YES, YES_A),
        ('4. Aşama', 'Yoğuşma-Bulut', MAVI, MAVI_A),
        ('5. Aşama', 'Yağmur İnmesi', LAC, GRI_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 6 + i * 119
        ic += f'<rect x="{x}" y="10" width="102" height="68" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.7"/>'
        ic += yazi(x + 51, 35, ust, 11.5, renk)
        ic += yazi(x + 51, 58, alt, 10.8, LAC)
        if i < 4:
            ic += f'<line x1="{x + 104}" y1="44" x2="{x + 117}" y2="44" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 113} 39 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 88, ic, 'Alçak basınç alanı ve yağmur oluşumunun 5 aşamalı akış şeması.', 17)


def ifade_ayirt_panosu():
    kartlar = [
        ('I. Cümle', '“Bu sabah okul yolunda yoğun sis', 'nedeniyle görüş mesafesi kısaldı.”', TUR, TUR_A),
        ('II. Cümle', '“İç Anadolu’da uzun yıllar ortalamasına', 'göre yaz ayları sıcak ve kuraktır.”', MAVI, MAVI_A),
        ('III. Cümle', '“Yarın öğleden sonra kent genelinde', 'kuvvetli rüzgâr ve yağmur bekleniyor.”', YES, YES_A),
        ('IV. Cümle', '“Karadeniz kıyılarında 40 yıllık kayıtlara', 'göre her mevsim yağışlı geçmektedir.”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="52" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 14, y + 34, s1, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 14, y + 47, s2, 10.6, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört gözlem ve kayıt cümlesi kartı: I ve III kısa süreli hava olayı, II ve IV uzun yıllık iklim ifadesi.', 18)


def dalgalanma_grafigi():
    ic = f'<rect x="6" y="6" width="286" height="108" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 24, '1. Grafik: Haftalık Günlük Sıcaklık', 11.5, TUR)
    ic += f'<polyline points="28,84 66,46 104,78 142,42 180,82 218,50 256,74" fill="none" stroke="{TUR}" stroke-width="2.6"/>'
    for px, py in [(28, 84), (66, 46), (104, 78), (142, 42), (180, 82), (218, 50), (256, 74)]:
        ic += f'<circle cx="{px}" cy="{py}" r="3.5" fill="{TUR}"/>'
    ic += yazi(149, 104, 'Günden güne dalgalanma çok fazla', 10.8, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="108" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 24, '2. Grafik: 40 Yıllık Temmuz Ortalaması', 11.5, MAVI)
    ic += f'<polyline points="330,64 368,62 406,65 444,63 482,64 520,62 558,63" fill="none" stroke="{MAVI}" stroke-width="2.6"/>'
    for px, py in [(330, 64), (368, 62), (406, 65), (444, 63), (482, 64), (520, 62), (558, 63)]:
        ic += f'<circle cx="{px}" cy="{py}" r="3.5" fill="{MAVI}"/>'
    ic += yazi(451, 104, 'Uzun yıllık ortalama çizgisi dengeli', 10.8, LAC, ince=True)
    return svg(600, 120, ic, 'Haftalık günlük sıcaklık dalgalanması (değişkenlik fazla) ile 40 yıllık temmuz ortalaması (değişkenlik az) grafikleri.', 18)


def dolu_kar_karsilastirma():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Dolu Yağışı', 11.5, TUR)
    ic += f'<circle cx="44" cy="60" r="14" fill="#fff" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(44, 64, 'Buz', 10.5, TUR)
    ic += yazi(72, 48, 'Fırtınadaki dikey hareketlerle', 10.6, LAC, 'start', ince=True)
    ic += yazi(72, 64, '  yağmur damlaları aniden donar.', 10.6, LAC, 'start', ince=True)
    ic += yazi(72, 82, 'Çapı: 5–50 mm buz küreleri', 10.8, TUR, 'start')

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Kar Yağışı', 11.5, MAVI)
    ic += f'<circle cx="346" cy="60" r="14" fill="#fff" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(346, 64, 'Kar', 10.5, MAVI)
    ic += yazi(374, 48, '0 °C’nin altında su buharı', 10.6, LAC, 'start', ince=True)
    ic += yazi(374, 64, '  soğuyarak katılaşır ve birleşir.', 10.6, LAC, 'start', ince=True)
    ic += yazi(374, 82, 'Yapısı: Küçük buz kristalleri', 10.8, MAVI, 'start')
    return svg(600, 110, ic, 'Dolu (fırtınada aniden donan 5-50 mm buz küreleri) ve kar (0 derece altında birleşen buz kristalleri) karşılaştırma kartları.', 18)


def gezi_plan_karti():
    ic = f'<rect x="6" y="6" width="286" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 24, '1. Kaynak: Hava Tahmini Raporu', 11.5, YESIL_K)
    ic += yazi(20, 46, 'Meteorolojik uydulardan saatlik', 10.8, LAC, 'start', ince=True)
    ic += yazi(28, 62, 'alınan sıcaklık, yağış ve rüzgâr verisi', 10.8, LAC, 'start', ince=True)
    ic += yazi(20, 82, 'Cumartesi sabahının anlık durumu', 10.8, YESIL_K, 'start')

    ic += f'<rect x="308" y="6" width="286" height="96" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, '2. Kaynak: Bölgesel İklim Haritası', 11.5, MOR)
    ic += yazi(322, 46, 'Bölgenin son 40 yılına ait', 10.8, LAC, 'start', ince=True)
    ic += yazi(330, 62, 'mevsimlik sıcaklık ve yağış ortalaması', 10.8, LAC, 'start', ince=True)
    ic += yazi(322, 82, 'Uzun yılların genel iklim özelliği', 10.8, MOR, 'start')
    return svg(600, 108, ic, 'Arazi çalışması planı için 1. kaynak (saatlik uydu hava tahmini) ve 2. kaynak (40 yıllık bölgesel iklim haritası).', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = basinc_ruzgar_sema()
    s[4]['gorsel'] = yogusma_siniflama_tablosu()
    s[5]['gorsel'] = hava_iklim_olcut_kartlari()
    s[6]['gorsel'] = iki_sehir_sicaklik_karti()
    s[7]['gorsel'] = yagmur_olusum_akisi()
    s[8]['gorsel'] = ifade_ayirt_panosu()
    s[9]['gorsel'] = dalgalanma_grafigi()
    s[10]['gorsel'] = dolu_kar_karsilastirma()
    s[12]['gorsel'] = gezi_plan_karti()
