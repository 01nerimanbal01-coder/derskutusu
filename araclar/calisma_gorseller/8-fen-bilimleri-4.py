"""8. sınıf Fen Bilimleri 4. hafta (İklim bilimi, sera gazları ve iklim değişikliği; DNA, gen, nükleotid ve kromozom) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=11.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def sera_etkisi_sema():
    ic = f'<rect x="6" y="6" width="588" height="128" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    # Atmosfer kuşağı ve yeryüzü
    ic += f'<rect x="14" y="42" width="380" height="44" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.2" stroke-dasharray="4 3"/>'
    ic += yazi(26, 58, 'Atmosfer (Sera gazları: CH₄, CO₂, O₃, H₂O)', 11, MAVI, 'start')
    ic += f'<rect x="14" y="102" width="380" height="24" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(204, 118, 'Yeryüzü', 11.5, YESIL_K)
    # Güneş
    ic += f'<circle cx="48" cy="24" r="13" fill="#f5c421" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(70, 28, 'Güneş ışınları', 11, TUR, 'start')
    # Gelen ve yansıyan ışınlar
    ic += f'<line x1="60" y1="32" x2="118" y2="100" stroke="{TUR}" stroke-width="2.2"/>'
    ic += f'<line x1="118" y1="100" x2="162" y2="20" stroke="{TUR}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += yazi(170, 24, 'Uzaya yansıyan', 10.5, TUR, 'start', ince=True)
    # Tutulan ısı
    ic += f'<line x1="280" y1="100" x2="280" y2="68" stroke="{KIR}" stroke-width="2.4"/>'
    ic += f'<path d="M280 68 Q305 68 305 98" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
    ic += yazi(314, 82, 'Tutulan ısı', 11, KIR, 'start')
    for cx, cy in [(248, 72), (272, 74), (308, 66), (344, 72), (370, 68)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{YES}"/>'
    # Sağ bilgi kutusu
    ic += f'<rect x="404" y="14" width="180" height="112" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(494, 34, 'Sera Etkisi Dengesi', 11.5, TUR)
    ic += yazi(494, 56, 'Doğal düzey:', 11, YESIL_K)
    ic += yazi(494, 72, 'Dünya sıcaklığını korur.', 10.8, LAC, ince=True)
    ic += yazi(494, 94, 'Aşırı artış:', 11, KIR)
    ic += yazi(494, 110, 'Küresel ısınmaya yol açar.', 10.8, LAC, ince=True)
    return svg(600, 140, ic, 'Sera etkisi modeli: Güneş ışınları, uzaya yansıyan ışınlar, sera gazları tarafından tutulan ısı ve küresel ısınma dengesi.', 16)


def kromozom_grafigi():
    veriler = [
        ('Eğrelti otu', 500, 260, MAVI),
        ('Denizyıldızı', 94, 82, MOR),
        ('Moli balığı', 46, 52, TUR),
        ('Buğday', 42, 48, YES),
        ('Kızıl tilki', 38, 44, KIR),
    ]
    ic = f'<rect x="6" y="6" width="588" height="128" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, 'Bazı Canlı Türlerinin Kromozom Sayıları (İnsan = 46)', 12, LAC)
    for i, (ad, sayi, boy_w, renk) in enumerate(veriler):
        y = 34 + i * 19
        ic += yazi(118, y + 12, ad, 11, LAC, 'end')
        ic += f'<rect x="126" y="{y}" width="{boy_w}" height="14" rx="4" fill="{renk}"/>'
        ic += yazi(134 + boy_w, y + 12, str(sayi), 11, renk, 'start')
    ic += f'<rect x="430" y="38" width="152" height="84" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(506, 58, 'Karşılaştırma Notu', 11.5, MAVI)
    ic += yazi(506, 78, 'Buğday (42), eğrelti', 10.8, LAC, ince=True)
    ic += yazi(506, 94, 'otundan (500) daha', 10.8, LAC, ince=True)
    ic += yazi(506, 110, 'gelişmiş bir bitkidir.', 10.8, LAC, ince=True)
    return svg(600, 140, ic, 'Bazı canlıların kromozom sayıları grafiği: Eğrelti otu 500, Denizyıldızı 94, Moli balığı 46, Buğday 42, Kızıl tilki 38.', 16)


def nukleotid_modelleri():
    ic = f'<rect x="6" y="6" width="278" height="120" rx="10" fill="#f7f9fd" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(145, 24, 'Bir Nükleotidin Üç Kısımlı Yapısı', 11.5, MAVI)
    ic += f'<circle cx="52" cy="68" r="20" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(52, 72, '1', 12, TUR)
    ic += f'<line x1="72" y1="68" x2="96" y2="68" stroke="{LAC}" stroke-width="2.2"/>'
    ic += f'<polygon points="122,44 146,60 137,88 107,88 98,60" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(122, 73, '2', 12, YESIL_K)
    ic += f'<line x1="146" y1="68" x2="170" y2="68" stroke="{LAC}" stroke-width="2.2"/>'
    ic += f'<rect x="170" y="48" width="96" height="40" rx="8" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.8"/>'
    ic += yazi(218, 72, '3 (A, T, G, C)', 11.5, MOR)
    ic += yazi(145, 112, '1 ve 2 her nükleotidde aynıdır.', 10.8, LAC, ince=True)

    ic += f'<rect x="294" y="6" width="300" height="120" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(444, 24, 'Dört Çeşit Nükleotid Kartı', 11.5, KAHVE)
    bazlar = [('A', 'Adenin', MAVI, MAVI_A), ('T', 'Timin', TUR, TUR_A), ('G', '? nükleotidi', YES, YES_A), ('C', 'Sitozin', MOR, MOR_A)]
    for i, (harf, ad, renk, arka) in enumerate(bazlar):
        x = 306 + (i % 2) * 142
        y = 34 + (i // 2) * 42
        ic += f'<rect x="{x}" y="{y}" width="134" height="36" rx="7" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += rozet(x + 20, y + 18, harf, renk, 10, 11)
        ic += yazi(x + 80, y + 22, ad, 11, LAC)
    return svg(600, 132, ic, 'Bir nükleotidin üç parçası (1, 2, 3) ve A, T, G, C bazlı dört nükleotid kartı.', 16)


def iklim_meteoroloji_kart():
    ic = f'<rect x="6" y="6" width="286" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += rozet(26, 26, 'K', MAVI, 11, 11.5)
    ic += yazi(158, 28, 'K Araştırmacısının Çalışması', 12, MAVI)
    ic += yazi(149, 54, 'Bir bölgenin 35 yıllık sıcaklık ve', 11.2, LAC, ince=True)
    ic += yazi(149, 72, 'yağış kayıtlarını inceleyerek', 11.2, LAC, ince=True)
    ic += yazi(149, 90, 'bölgenin iklim tipini belirler.', 11.2, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="106" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += rozet(328, 26, 'L', TUR, 11, 11.5)
    ic += yazi(460, 28, 'L Araştırmacısının Çalışması', 12, TUR)
    ic += yazi(451, 54, 'Yarın beklenen sağanak yağışın', 11.2, LAC, ince=True)
    ic += yazi(451, 72, 'oluşum nedenlerini ve günlük', 11.2, LAC, ince=True)
    ic += yazi(451, 90, 'yaşama etkilerini araştırır.', 11.2, TUR)
    return svg(600, 118, ic, 'K araştırmacısı 35 yıllık kayıtlarla iklim tipini belirler; L araştırmacısı günlük sağanak yağışın nedenlerini araştırır.', 16)


def kalitim_birimleri_kutu():
    kutular = [
        (6, 6, 588, 116, '#f7f9fd', GRI, 'Çekirdek (Yönetim merkezi)'),
        (28, 26, 544, 90, MAVI_A, MAVI, 'Kromozom (Kromatin ağının kısalıp kalınlaşmış hâli)'),
        (52, 46, 496, 64, YES_A, YES, 'DNA (Çift zincirli sarmal molekül)'),
        (78, 66, 444, 38, TUR_A, TUR, 'Gen (Görev birimi)   ⊃   Nükleotid (Yapı birimi)'),
    ]
    ic = ''
    for x, y, w, h, arka, renk, bas in kutular:
        ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 14, y + 17 if h > 40 else y + 23, bas, 11.5, LAC if renk == GRI else renk, 'start')
    return svg(600, 128, ic, 'İç içe kutularla kalıtım birimleri: Çekirdek, Kromozom, DNA, Gen ve Nükleotid.', 16)


def iki_bolge_iklim():
    ic = f'<rect x="6" y="6" width="286" height="112" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'K Bölgesi Gözlem Verileri', 12, YESIL_K)
    ic += yazi(22, 48, '- Ulaşan Güneş enerjisi: Orta düzey', 11, LAC, 'start', ince=True)
    ic += yazi(22, 68, '- Yeryüzü özelliği: Benzer arazi yapısı', 11, LAC, 'start', ince=True)
    ic += yazi(22, 88, '- Sera gazı miktarı: Normal düzeyde', 11, YESIL_K, 'start')
    ic += yazi(149, 108, 'Doğal ısı dengesi korunuyor', 10.8, YESIL_K, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="112" rx="10" fill="{TUR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'L Bölgesi Gözlem Verileri', 12, KIR)
    ic += yazi(324, 48, '- Ulaşan Güneş enerjisi: Orta düzey', 11, LAC, 'start', ince=True)
    ic += yazi(324, 68, '- Yeryüzü özelliği: Benzer arazi yapısı', 11, LAC, 'start', ince=True)
    ic += yazi(324, 88, '- Sera gazı miktarı: Normalin çok üzerinde', 11, KIR, 'start')
    ic += yazi(451, 108, 'Atmosferde aşırı ısı tutuluyor', 10.8, KIR, ince=True)
    return svg(600, 124, ic, 'K ve L bölgelerinin karşılaştırılması: Güneş enerjisi ve yeryüzü benzer, L bölgesinde sera gazı yoğunluğu çok yüksek.', 16)


def hucre_dna_konum():
    ic = f'<rect x="6" y="6" width="286" height="112" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Gelişmiş Hücre', 12, MAVI)
    ic += f'<ellipse cx="90" cy="70" rx="64" ry="34" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += f'<circle cx="90" cy="70" r="20" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += f'<path d="M80 68 q5 -8 10 0 t10 0" fill="none" stroke="{MOR}" stroke-width="2"/>'
    ic += yazi(172, 60, 'Çekirdek:', 11.5, MOR, 'start')
    ic += yazi(172, 78, 'DNA çekirdek', 11, LAC, 'start', ince=True)
    ic += yazi(172, 94, 'içinde bulunur.', 11, LAC, 'start', ince=True)

    ic += f'<rect x="308" y="6" width="286" height="112" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'İlkel Hücre (Örn. Bakteri)', 12, TUR)
    ic += f'<rect x="328" y="42" width="116" height="56" rx="28" fill="#fff" stroke="{TUR}" stroke-width="1.8"/>'
    ic += f'<path d="M358 70 q14 -14 28 0 t28 0" fill="none" stroke="{KIR}" stroke-width="2"/>'
    ic += yazi(458, 60, 'Sitoplazma:', 11.5, KIR, 'start')
    ic += yazi(458, 78, 'Çekirdek yoktur; DNA', 11, LAC, 'start', ince=True)
    ic += yazi(458, 94, 'sitoplazmadadır.', 11, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Gelişmiş hücrede DNA çekirdek içinde, ilkel hücrede DNA sitoplazma içinde bulunur.', 16)


def dna_dizilim_kart():
    ic = f'<rect x="6" y="6" width="286" height="102" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 25, '1. Canlının DNA Parçası', 12, MAVI)
    for i, b in enumerate(['A', 'T', 'G', 'C', 'A', 'G']):
        x = 24 + i * 42
        ic += f'<rect x="{x}" y="38" width="34" height="28" rx="6" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
        ic += yazi(x + 17, 57, b, 12, MAVI)
    ic += yazi(149, 88, 'Kullanılan baz çeşitleri: A, T, G, C', 11, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="102" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 25, '2. Canlının DNA Parçası', 12, YESIL_K)
    for i, b in enumerate(['G', 'C', 'A', 'T', 'C', 'A', 'T']):
        x = 320 + i * 37
        ic += f'<rect x="{x}" y="38" width="31" height="28" rx="6" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
        ic += yazi(x + 15.5, 57, b, 12, YESIL_K)
    ic += yazi(451, 88, 'Kullanılan baz çeşitleri: A, T, G, C', 11, LAC, ince=True)
    return svg(600, 114, ic, 'İki farklı canlının DNA parçaları: baz çeşitleri aynı (A, T, G, C), nükleotid sayısı ve diziliş sırası farklı.', 16)


def iklim_degisikligi_pano():
    adlar = [
        ('1. Sera Gazı Artışı', 'CH₄, CO₂, O₃, H₂O', 'normalin üstüne çıkar', TUR, TUR_A),
        ('2. Küresel Isınma', 'Atmosferde tutulan', 'ısı tehlikeli boyuta ulaşır', KIR, '#fdeaea'),
        ('3. İklim Değişikliği', 'Dünya genelinde uzun', 'yıllarda yağış/sıcaklık değişir', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(adlar):
        x = 6 + i * 200
        ic += f'<rect x="{x}" y="8" width="188" height="92" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 94, 28, bas, 11.5, renk)
        ic += yazi(x + 94, 54, s1, 11, LAC, ince=True)
        ic += yazi(x + 94, 72, s2, 11, LAC, ince=True)
        if i < 2:
            ic += f'<line x1="{x + 190}" y1="54" x2="{x + 204}" y2="54" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 200} 49 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 108, ic, 'Sera gazı artışı, küresel ısınma ve iklim değişikliği arasındaki zincir.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sera_etkisi_sema()
    s[4]['gorsel'] = kromozom_grafigi()
    s[5]['gorsel'] = nukleotid_modelleri()
    s[6]['gorsel'] = iklim_meteoroloji_kart()
    s[7]['gorsel'] = kalitim_birimleri_kutu()
    s[8]['gorsel'] = iki_bolge_iklim()
    s[9]['gorsel'] = hucre_dna_konum()
    s[10]['gorsel'] = dna_dizilim_kart()
    s[12]['gorsel'] = iklim_degisikligi_pano()
