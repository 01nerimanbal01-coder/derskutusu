"""6. sınıf İngilizce 11. hafta (Personal Life: Physical Appearance, Personality Traits, Comparative Adjectives &amp; Clothing) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dis_gorunus_diyalog_karti():
    ic = kutu(6, 6, 348, 36, MAVI_A, MAVI)
    ic += yazi(180, 28, 'Kaan: “......................................................................?”', 10.1, MAVI)

    ic += kutu(6, 48, 348, 40, YES_A, YES)
    ic += yazi(180, 65, 'Burcu: “He is tall and slim. He has got short curly', 9.5, LAC)
    ic += yazi(180, 81, 'black hair and hazel eyes.” (Physical Appearance)', 9.5, YESIL_K)
    return svg(360, 94, ic, 'Dış görünüş cevabına uygun İngilizce soru kalıbı kartı.', 16)


def comparative_donusum_panosu():
    kartlar = [
        ('1. tall', 'taller than', MAVI, MAVI_A),
        ('2. slim', '2x m + -er = ?', YES, YES_A),
        ('3. outgoing', 'Uzun sıfat = ?', TUR, TUR_A),
        ('4. good', 'Düzensiz = ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Kısa, uzun ve düzensiz sıfatların karşılaştırma dönüşüm panosu.', 15)


def sac_sifat_sirasi_kartlari():
    kartlar = [
        ('A Kartı (!)', 'is long hair / has got slim', KIR, KIR_A),
        ('B Kartı (!)', 'brown long straight hair', TUR, TUR_A),
        ('C Kartı (✓)', 'Size + Shape + Colour + Hair', YES, YES_A),
        ('D Kartı (!)', 'straight long brown hair', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Saç sıfatlarının doğru dizilişi ve is/has got kuralı kartları.', 16)


def efe_tuna_karsilastirma_tablosu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 21, 'EFE (13 years old)', 10.2, MAVI)
    ic += yazi(91, 42, '• Height: 164 cm | Weight: 52 kg', 9.2, LAC, ince=True)
    ic += yazi(91, 62, '• Always on time (Punctual: ★★★★★)', 9.1, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 21, 'TUNA (12 years old)', 10.2, TUR)
    ic += yazi(269, 42, '• Height: 155 cm | Weight: 58 kg', 9.2, LAC, ince=True)
    ic += yazi(269, 62, '• Sometimes late (Punctual: ★★☆☆☆)', 9.1, TUR)
    return svg(360, 88, ic, 'Efe ve Tuna boy, kilo, yaş ve dakiklik karşılaştırma kartı.', 15)


def mevsim_giysi_kombin_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 21, 'Alper · Snowy Winter Day', 10.0, CAM)
    ic += yazi(91, 43, 'Clothes: coat, scarf,', 9.5, LAC)
    ic += yazi(91, 63, 'and winter boots', 9.5, CAM, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 21, 'Sude · Sunny Summer Day', 10.0, YESIL_K)
    ic += yazi(269, 43, 'Clothes: dress, cap,', 9.5, LAC)
    ic += yazi(269, 63, 'and sandals', 9.5, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Kış ve yaz mevsiminde giyilen kıyafet kombinleri kartı.', 15)


def yeni_arkadas_diyalog_adimlari():
    adimlar = [
        ('1. Adım', 'Who is the girl in blue?', MAVI, MAVI_A),
        ('2. Adım', 'She is Pelin.', YES, YES_A),
        ('3. Adım', 'What is she like?', TUR, TUR_A),
        ('4. Adım', 'Cheerful and helpful.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Yeni sınıf arkadaşını tanıtma diyalog adımları.', 16)


def merve_bora_karne_panosu():
    ic = kutu(6, 6, 170, 76, MOR_A, MOR)
    ic += yazi(91, 21, 'MERVE’S PROFILE', 10.2, MOR)
    ic += yazi(91, 42, '• English: 95  |  Science: 90', 9.4, LAC)
    ic += yazi(91, 62, '• Trait: Outgoing &amp; cheerful', 9.2, MOR, ince=True)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 21, 'BORA’S PROFILE', 10.2, MAVI)
    ic += yazi(269, 42, '• English: 80  |  Science: 75', 9.4, LAC)
    ic += yazi(269, 62, '• Trait: Shy &amp; calm', 9.2, MAVI, ince=True)
    return svg(360, 88, ic, 'Merve ve Bora ders notları ile kişilik özellikleri karşılaştırma panosu.', 15)


def comparative_hata_avcisi():
    ic = kutu(6, 6, 348, 76, KIR_A, KIR)
    ic += yazi(180, 22, 'GRAMMAR ERROR HUNTER · HATA AVCISI KARTI', 10.2, KIR)
    ic += yazi(180, 44, '✗ 1) “Mert is more taller than Can.”   (Short adjective rule!)', 9.5, LAC)
    ic += yazi(180, 65, '✗ 2) “Aslı is gooder at tennis than Eda.”   (Irregular adjective rule!)', 9.5, LAC)
    return svg(360, 88, ic, 'Karşılaştırma sıfatlarında yapılan iki yaygın hatayı gösteren kart.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dis_gorunus_diyalog_karti()
    s[2]['gorsel'] = comparative_donusum_panosu()
    s[5]['gorsel'] = sac_sifat_sirasi_kartlari()
    s[6]['gorsel'] = efe_tuna_karsilastirma_tablosu()
    s[7]['gorsel'] = mevsim_giysi_kombin_karti()
    s[8]['gorsel'] = yeni_arkadas_diyalog_adimlari()
    s[9]['gorsel'] = merve_bora_karne_panosu()
    s[11]['gorsel'] = comparative_hata_avcisi()
