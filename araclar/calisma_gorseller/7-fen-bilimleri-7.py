"""7. sınıf Fen Bilimleri 7. hafta (Kuvvet, İş ve Enerji İlişkisi: Kinetik ve Potansiyel Enerji) çalışma kâğıdı görselleri (SVG; insan figürü yok K024; yazı 10.5-13 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=23):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk=LAC, r=11, boy=11.5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.35, metin, boy, renk)


def arac_kinetik_deney():
    araclar = [
        ('K Otomobili', 'Kütle: 1000 kg', 'Sürat: saatte 60 km', MAVI, MAVI_A, 6),
        ('L Otomobili', 'Kütle: 1000 kg', 'Sürat: saatte 100 km', TUR, TUR_A, 204),
        ('M Kamyonu', 'Kütle: 2500 kg', 'Sürat: saatte 100 km', YES, YES_A, 402),
    ]
    ic = ''
    for bas, kutle, surat, renk, arka, x in araclar:
        cx = x + 96
        ic += f'<rect x="{x}" y="6" width="192" height="122" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(cx, 25, bas, 12, renk)
        # Araç gövdesi (insan figürü yok)
        ic += f'<rect x="{cx - 42}" y="42" width="84" height="22" rx="6" fill="{renk}"/>'
        ic += f'<circle cx="{cx - 24}" cy="66" r="7" fill="{LAC}"/><circle cx="{cx + 24}" cy="66" r="7" fill="{LAC}"/>'
        ic += yazi(cx, 92, kutle, 11.5, LAC)
        ic += yazi(cx, 112, surat, 11, LAC, ince=True)
    return svg(600, 134, ic, 'Üç araç kartı: K (1000 kg, saatte 60 km), L (1000 kg, saatte 100 km), M (2500 kg, saatte 100 km).', 21)


def kum_havuzu_deneyi():
    ic = f'<rect x="6" y="6" width="588" height="126" rx="10" fill="#f8fafc" stroke="{GRI}" stroke-width="1.6"/>'
    # Kum havuzu
    ic += f'<rect x="40" y="96" width="520" height="26" rx="6" fill="#fde68a" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 114, 'Özdeş Kum Havuzu', 11.5, KAHVE)
    # K bilyesi (h yüksekliği)
    ic += f'<circle cx="150" cy="54" r="14" fill="{MAVI}" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(150, 58, 'K', 12, '#fff')
    ic += yazi(150, 30, 'Kütle: m (Özdeş)', 11, MAVI)
    ic += f'<line x1="150" y1="70" x2="150" y2="94" stroke="{MAVI}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += yazi(192, 84, 'h = 1 m', 11.5, MAVI)
    # L bilyesi (2h yüksekliği)
    ic += f'<circle cx="430" cy="28" r="14" fill="{TUR}" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(430, 32, 'L', 12, '#fff')
    ic += yazi(345, 32, 'Kütle: m (Özdeş)', 11, TUR)
    ic += f'<line x1="430" y1="44" x2="430" y2="94" stroke="{TUR}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += yazi(476, 72, '2h = 2 m', 11.5, TUR)
    return svg(600, 138, ic, 'Kum havuzu deneyi: özdeş m kütleli K bilyesi h=1 m, L bilyesi 2h=2 m yükseklikten bırakılıyor.', 21)


def enerji_durum_kartlari():
    kart = [
        ('1. Kart · Rayda Giden Tren', 'Yatay rayda sabit süratle ilerler.', 'Enerji: Kinetik enerji', MAVI, MAVI_A),
        ('2. Kart · Dalda Duran Elma', 'Yerden 3 m yüksekte hareketsizdir.', 'Enerji: ?', YES, YES_A),
        ('3. Kart · Gerilmiş Ok Yayı', 'Esnek yay çekilerek bekletiliyor.', 'Enerji ve Nedeni: ?', TUR, TUR_A),
        ('4. Kart · Uçan Helikopter', 'Gökyüzünde yüksekte ilerler.', 'Enerji: ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 64
        ic += f'<rect x="{x}" y="{y}" width="286" height="58" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="58" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 35, s1, 11, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 51, s2, 11.5, LAC, 'start')
    return svg(600, 134, ic, 'Dört enerji durum kartı: 1. Rayda giden tren, 2. Dalda duran elma, 3. Gerilmiş ok yayı, 4. Uçan helikopter.', 21)


def egik_duzlem_takoz():
    ic = ''
    duzenekler = [
        ('1. Düzenek', 'm', 'h', 'Sürüklenme: x', MAVI, MAVI_A, 6),
        ('2. Düzenek', '2m', 'h', 'Sürüklenme: 2x', TUR, TUR_A, 304),
    ]
    for bas, kutle, yuk, sonuc, renk, arka, x in duzenekler:
        ic += f'<rect x="{x}" y="6" width="290" height="114" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.7"/>'
        ic += yazi(x + 145, 24, bas, 12, renk)
        # Eğik düzlem üçgeni ve yatay yol
        ic += f'<polygon points="{x + 24},96 {x + 24},46 {x + 124},96" fill="#fff" stroke="{LAC}" stroke-width="1.6"/>'
        ic += f'<line x1="{x + 24}" y1="96" x2="{x + 266}" y2="96" stroke="{LAC}" stroke-width="2"/>'
        ic += f'<circle cx="{x + 54}" cy="54" r="11" fill="{renk}"/>'
        ic += yazi(x + 54, 58, kutle, 10.5, '#fff')
        ic += yazi(x + 18, 74, yuk, 11, LAC)
        ic += f'<rect x="{x + 148}" y="76" width="34" height="20" rx="3" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.4"/>'
        ic += yazi(x + 165, 90, 'Takoz', 10.5, LAC)
        ic += yazi(x + 205, 58, sonuc, 11.5, renk)
    return svg(600, 126, ic, 'Eğik düzlem deneyi: aynı h yüksekliğinden bırakılan m ve 2m kütleli bilyelerin takozu sürükleme miktarları.', 21)


def raf_top_sirala():
    ic = f'<rect x="6" y="6" width="588" height="122" rx="10" fill="#fbf7ee" stroke="{KAHVE}" stroke-width="1.8"/>'
    raflar = [
        (34, '3. Raf (3h)', [('N Kutusu · 25 N', 410, MOR, MOR_A)]),
        (68, '2. Raf (2h)', [('L Kutusu · 10 N', 220, MAVI, MAVI_A), ('M Kutusu · 25 N', 410, TUR, TUR_A)]),
        (102, '1. Raf (1h)', [('K Kutusu · 10 N', 220, YES, YES_A)]),
    ]
    for y, ad, kutular in raflar:
        ic += f'<line x1="24" y1="{y}" x2="576" y2="{y}" stroke="{KAHVE}" stroke-width="2.4"/>'
        ic += yazi(32, y - 8, ad, 11, KAHVE, 'start')
        for metin, kx, renk, arka in kutular:
            ic += f'<rect x="{kx - 68}" y="{y - 26}" width="136" height="24" rx="5" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
            ic += yazi(kx, y - 10, metin, 11, LAC)
    return svg(600, 134, ic, 'Üç katlı kitaplık rafında K (1. raf 10 N), L (2. raf 10 N), M (2. raf 25 N) ve N (3. raf 25 N) kutuları.', 21)


def yay_sikisma_sema():
    yaylar = [
        ('K Yayı', 'Tel: İnce çelik', 'Sıkışma: 5 cm', MAVI, MAVI_A, 6, 1.8),
        ('L Yayı', 'Tel: İnce çelik', 'Sıkışma: 10 cm', TUR, TUR_A, 204, 1.8),
        ('M Yayı', 'Tel: Kalın çelik', 'Sıkışma: 10 cm', YES, YES_A, 402, 3.2),
    ]
    ic = ''
    for bas, tel, sikisma, renk, arka, x, kalin in yaylar:
        cx = x + 96
        ic += f'<rect x="{x}" y="6" width="192" height="118" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.7"/>'
        ic += yazi(cx, 25, bas, 12, renk)
        # Yay zikzak çizimi
        ic += f'<path d="M{x + 28} 54 l14 -10 l14 20 l14 -20 l14 20 l14 -20 l14 20 l14 -10" fill="none" stroke="{LAC}" stroke-width="{kalin}" stroke-linecap="round"/>'
        ic += yazi(cx, 86, tel, 11, LAC)
        ic += yazi(cx, 106, sikisma, 11.5, renk)
    return svg(600, 130, ic, 'Üç çelik yay: K (ince, 5 cm sıkışma), L (ince, 10 cm sıkışma), M (kalın, 10 cm sıkışma).', 21)


def esnek_esnek_olmayan():
    kartlar = [
        ('1. Sıkışmış Yay', 'Kuvvet kalkınca', 'eski hâline döner', YES, YES_A),
        ('2. Oyun Hamuru', 'Kuvvet kalkınca', 'eski hâline dönmez', TUR, TUR_A),
        ('3. Gerilmiş Lastik', 'Kuvvet kalkınca', 'eski hâline döner', MAVI, MAVI_A),
        ('4. Buruşuk Kâğıt', 'Kuvvet kalkınca', 'eski hâline dönmez', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        cx = x + 71
        ic += f'<rect x="{x}" y="6" width="142" height="104" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(cx, 28, bas, 10.6, renk)
        ic += f'<line x1="{x + 14}" y1="36" x2="{x + 128}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(cx, 62, s1, 10.2, LAC, ince=True)
        ic += yazi(cx, 82, s2, 10.2, LAC)
    return svg(600, 116, ic, 'Dört nesne kartı: 1. Sıkışmış yay, 2. Oyun hamuru, 3. Gerilmiş lastik, 4. Buruşuk kâğıt.', 20)


def ucan_kus_sema():
    ic = f'<rect x="6" y="6" width="286" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.7"/>'
    ic += yazi(149, 26, 'K Kuşu (Havada Uçuyor)', 12, MAVI)
    ic += yazi(149, 52, 'Kütle: 2 kg  |  Yükseklik: 15 m', 11, LAC)
    ic += yazi(149, 74, 'Sürat: saniyede 8 m (Hareketli)', 11, LAC, ince=True)
    ic += yazi(149, 96, 'Enerji: Kinetik + Çekim Potansiyeli', 11, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="106" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.7"/>'
    ic += yazi(451, 26, 'L Kuşu (Dalda Hareketsiz)', 12, YESIL_K)
    ic += yazi(451, 52, 'Kütle: 2 kg  |  Yükseklik: 15 m', 11, LAC)
    ic += yazi(451, 74, 'Sürat: 0 (Hareketsiz duruyor)', 11, LAC, ince=True)
    ic += yazi(451, 96, 'Enerji: Yalnız Çekim Potansiyeli', 11, YESIL_K)
    return svg(600, 118, ic, 'Aynı yükseklikte (15 m) ve eşit kütleli (2 kg) uçan K kuşu ile dalda duran L kuşunun karşılaştırması.', 20)


def baraj_turbin_karti():
    ic = f'<rect x="6" y="6" width="272" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.7"/>'
    ic += yazi(142, 26, '1. Aşama · Baraj Gölü (Yüksekte)', 11.5, MAVI)
    ic += yazi(142, 52, 'Yüksekte biriktirilen su kütlesi', 11, LAC, ince=True)
    ic += yazi(142, 74, 'Depolanan: Çekim Potansiyel Enerjisi', 11, MAVI)

    ic += f'<line x1="284" y1="55" x2="316" y2="55" stroke="{LAC}" stroke-width="2.2"/><path d="M311 50 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="322" y="6" width="272" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.7"/>'
    ic += yazi(458, 26, '2. Aşama · Akan Su ve Türbin', 11.5, YESIL_K)
    ic += yazi(458, 52, 'Kapaklardan hızla akan suyun hareketi', 11, LAC, ince=True)
    ic += yazi(458, 74, 'Kazanılan: Kinetik (Hareket) Enerjisi', 11, YESIL_K)
    return svg(600, 110, ic, 'Baraj gölündeki yüksek suyun çekim potansiyel enerjisinin akan suda kinetik enerjiye dönüşümü.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = arac_kinetik_deney()
    s[4]['gorsel'] = kum_havuzu_deneyi()
    s[5]['gorsel'] = enerji_durum_kartlari()
    s[6]['gorsel'] = egik_duzlem_takoz()
    s[7]['gorsel'] = raf_top_sirala()
    s[8]['gorsel'] = yay_sikisma_sema()
    s[9]['gorsel'] = esnek_esnek_olmayan()
    s[10]['gorsel'] = ucan_kus_sema()
    s[12]['gorsel'] = baraj_turbin_karti()
