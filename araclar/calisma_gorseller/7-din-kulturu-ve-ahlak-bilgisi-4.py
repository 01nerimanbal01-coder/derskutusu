"""7. sınıf DKAB 4. hafta (Ahiret aşamaları: baas, haşir, mahşer, amel defteri, mizan, cennet ve cehennem) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=11, boy=12):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.36, metin, boy, renk)


def sur_ufleme():
    ic = ''
    kartlar = [
        ('İsrafil’in Sûra 1. Üflemesi', 'Dünya hayatı ve evrenin düzeni sona erer.', 'K', TUR, TUR_A),
        ('İsrafil’in Sûra 2. Üflemesi', 'Ölen bütün insanlar yeniden hayata kavuşturulur.', 'L', MAVI, MAVI_A),
    ]
    for i, (bas, aciklama, harf, renk, arka) in enumerate(kartlar):
        x = 6 + i * 298
        ic += f'<rect x="{x}" y="6" width="286" height="122" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += f'<rect x="{x}" y="6" width="286" height="28" rx="10" fill="{renk}"/><rect x="{x}" y="22" width="286" height="12" fill="{renk}"/>'
        ic += yazi(x + 143, 25, bas, 12.5, '#fff')
        # Sûr (boru) sembolü
        sx, sy = x + 44, 66
        ic += f'<path d="M{sx - 24} {sy + 8} Q{sx - 4} {sy + 6} {sx + 16} {sy - 12} L{sx + 16} {sy + 18} Q{sx - 4} {sy + 10} {sx - 24} {sy + 12} Z" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.4"/>'
        ic += f'<ellipse cx="{sx + 16}" cy="{sy + 3}" rx="4" ry="15" fill="#f4d27a" stroke="{KAHVE}" stroke-width="1.4"/>'
        ic += f'<path d="M{sx + 24} {sy - 6} q6 9 0 18 M{sx + 30} {sy - 10} q8 13 0 26" fill="none" stroke="{renk}" stroke-width="1.6" stroke-linecap="round"/>'
        ic += yazi(x + 178, 58, aciklama[:26], 11.5, LAC, ince=True)
        ic += yazi(x + 178, 76, aciklama[26:], 11.5, LAC, ince=True)
        ic += f'<rect x="{x + 78}" y="90" width="130" height="28" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.6" stroke-dasharray="5 3"/>'
        ic += yazi(x + 143, 109, f'Aşama: {harf} ?', 12.5, renk)
    ic += f'<path d="M294 67 H302" stroke="{LAC}" stroke-width="2.2"/><path d="M298 62 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 134, ic, 'İsrafil’in sûra iki kez üflemesi: 1. üfleme ile dünya düzeni sona erer (K aşaması), 2. üfleme ile insanlar yeniden diriltilir (L aşaması).', 25)


def cennet_panosu():
    kartlar = [
        ('1', 'Adn', YES, YES_A),
        ('2', 'Hüsna', YES, YES_A),
        ('3', 'Haşir', MOR, MOR_A),
        ('4', 'Meva', YES, YES_A),
        ('5', 'Mizan', TUR, TUR_A),
        ('6', 'Darülmukame', YES, YES_A),
    ]
    ic = f'<rect x="4" y="4" width="592" height="136" rx="12" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="1.8"/>'
    ic += yazi(300, 24, 'Kur’an-ı Kerim’de Cennet İsimleri Panosu', 13, YESIL_K)
    for i, (no, ad, renk, arka) in enumerate(kartlar):
        col = i % 3
        row = i // 3
        x = 18 + col * 190
        y = 36 + row * 48
        ic += f'<rect x="{x}" y="{y}" width="176" height="40" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += rozet(x + 20, y + 20, no, renk, 10, 11.5)
        ic += yazi(x + 100, y + 25, ad, 12.5, LAC)
    return svg(600, 144, ic, 'Altı kartlı pano: 1. Adn, 2. Hüsna, 3. Haşir, 4. Meva, 5. Mizan, 6. Darülmukame.', 26)


def ayet_kartlari():
    kart = [
        ('1. Kart · Nahl 38', '“Allah’ın ölen birini diriltmesi', 'bizzat üstlendiği gerçek vaadidir.”', MAVI, MAVI_A),
        ('2. Kart · İsra 13', '“Kıyamet gününde insana açılmış', 'bir kitap çıkaracağız.”', MOR, MOR_A),
        ('3. Kart · Enbiya 47', '“Kıyamet günü için adalet', 'terazileri kurarız...”', TUR, TUR_A),
        ('4. Kart · Tevbe 72', '“Altından ırmaklar akan cennetler ve', 'Adn cennetlerinde güzel meskenler...”', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kart):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 68
        ic += f'<rect x="{x}" y="{y}" width="286" height="60" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="60" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.5, renk, 'start')
        ic += yazi(x + 18, y + 36, s1, 11.5, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 52, s2, 11.5, LAC, 'start', ince=True)
    return svg(600, 140, ic, 'Dört ayet kartı: 1. Nahl 38 (yeniden diriltme vaadi), 2. İsra 13 (açılmış kitap), 3. Enbiya 47 (adalet terazileri), 4. Tevbe 72 (Adn cennetleri).', 23)


def hasir_mahser_sema():
    ic = ''
    # Sol kutu: K (Olay)
    ic += f'<rect x="8" y="8" width="182" height="108" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += rozet(26, 26, 'K', MAVI, 11, 12)
    ic += yazi(108, 28, 'Olayın Adı: ?', 12.5, MAVI)
    ic += yazi(99, 58, 'Diriltilen insanların', 11.5, LAC, ince=True)
    ic += yazi(99, 76, 'hesap vermek üzere', 11.5, LAC, ince=True)
    ic += yazi(99, 94, 'bir araya toplanması', 11.5, LAC, ince=True)
    # Ok 1
    ic += f'<line x1="194" y1="62" x2="212" y2="62" stroke="{LAC}" stroke-width="2"/><path d="M208 57 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    # Orta kutu: L (Yer)
    ic += f'<rect x="218" y="8" width="182" height="108" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += rozet(236, 26, 'L', TUR, 11, 12)
    ic += yazi(318, 28, 'Yerin Adı: ?', 12.5, TUR)
    ic += yazi(309, 58, 'Diriltilen insanların', 11.5, LAC, ince=True)
    ic += yazi(309, 76, 'toplanıp hesap verdiği', 11.5, LAC, ince=True)
    ic += yazi(309, 94, 'büyük toplanma alanı', 11.5, LAC, ince=True)
    # Ok 2
    ic += f'<line x1="404" y1="62" x2="422" y2="62" stroke="{LAC}" stroke-width="2"/><path d="M418 57 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    # Sağ kutu: Amel defteri
    ic += f'<rect x="428" y="8" width="164" height="108" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(510, 26, 'Amel Defteri', 12.5, YESIL_K)
    cx, cy = 510, 64
    ic += f'<path d="M{cx} {cy - 18} Q{cx - 22} {cy - 24} {cx - 44} {cy - 18} V{cy + 16} Q{cx - 22} {cy + 10} {cx} {cy + 18} Z" fill="#fff" stroke="{YESIL_K}" stroke-width="1.6"/>'
    ic += f'<path d="M{cx} {cy - 18} Q{cx + 22} {cy - 24} {cx + 44} {cy - 18} V{cy + 16} Q{cx + 22} {cy + 10} {cx} {cy + 18} Z" fill="#fff" stroke="{YESIL_K}" stroke-width="1.6"/>'
    for k in range(3):
        ic += f'<line x1="{cx - 36}" y1="{cy - 10 + k * 8}" x2="{cx - 8}" y2="{cy - 8 + k * 8}" stroke="{GRI}" stroke-width="1.4"/>'
        ic += f'<line x1="{cx + 8}" y1="{cy - 8 + k * 8}" x2="{cx + 36}" y2="{cy - 10 + k * 8}" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(510, 102, 'Kur’an’daki adı: ?', 11.5, YESIL_K)
    return svg(600, 124, ic, 'K kutusu: toplanma olayı, L kutusu: toplanılan yer, sağda açılmış amel defteri (Kur’an’daki adı soruluyor).', 24)


def baglanti_zinciri():
    adlar = [
        ('1. Halka', 'İlk Sûr', MAVI, MAVI_A),
        ('2. Halka', 'İkinci Sûr', MOR, MOR_A),
        ('3. Halka', 'Toplanma', TUR, TUR_A),
        ('4. Halka', 'Adalet Tartısı', ALTIN, '#fffbe6'),
        ('5. Halka', 'Son Yurt', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 8 + i * 118
        ic += f'<rect x="{x}" y="14" width="98" height="72" rx="14" fill="{arka}" stroke="{renk}" stroke-width="2"/>'
        ic += yazi(x + 49, 40, ust, 12, renk)
        ic += yazi(x + 49, 64, alt, 11.5, LAC)
        if i < 4:
            ic += f'<line x1="{x + 100}" y1="50" x2="{x + 116}" y2="50" stroke="{LAC}" stroke-width="2.2"/>'
            ic += f'<path d="M{x + 111} 45 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 100, ic, 'Ahiret aşamalarının 5 halkalı bağlantı zinciri: 1. İlk Sûr, 2. İkinci Sûr, 3. Toplanma, 4. Adalet Tartısı, 5. Son Yurt.', 20)


def mizan_terazisi():
    ic = ''
    # Sol: 1. Terazi (Sevap ağır)
    ic += f'<rect x="6" y="6" width="190" height="132" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(101, 24, '1. Terazi (Sevap ağır)', 12, YESIL_K)
    ic += f'<line x1="101" y1="44" x2="101" y2="112" stroke="{LAC}" stroke-width="2.6"/><rect x="77" y="112" width="48" height="6" rx="3" fill="{LAC}"/>'
    ic += f'<line x1="45" y1="62" x2="157" y2="42" stroke="{LAC}" stroke-width="2.6"/><circle cx="101" cy="52" r="4" fill="{ALTIN}"/>'
    ic += f'<line x1="45" y1="62" x2="45" y2="80" stroke="{LAC}" stroke-width="1.5"/><rect x="17" y="80" width="56" height="20" rx="5" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(45, 94, 'Sevap', 11, YESIL_K)
    ic += f'<line x1="157" y1="42" x2="157" y2="60" stroke="{LAC}" stroke-width="1.5"/><rect x="129" y="60" width="56" height="20" rx="5" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(157, 74, 'Günah', 11, TUR)
    ic += yazi(101, 131, 'Sonuç: Mükâfat', 11.5, YESIL_K)

    # Orta: Enbiya 47
    ic += f'<rect x="204" y="6" width="192" height="132" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Enbiya suresi 47. ayet', 12, KAHVE)
    ic += yazi(300, 50, '“Kıyamet günü için adalet', 11, LAC, ince=True)
    ic += yazi(300, 68, 'terazileri kurarız; kimseye', 11, LAC, ince=True)
    ic += yazi(300, 86, 'haksızlık edilmez. Yapılan,', 11, LAC, ince=True)
    ic += yazi(300, 104, 'bir hardal tanesi kadar olsa', 11, LAC, ince=True)
    ic += yazi(300, 122, 'bile onu ortaya koyarız.”', 11, LAC, ince=True)

    # Sağ: 2. Terazi (Günah ağır)
    ic += f'<rect x="404" y="6" width="190" height="132" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(499, 24, '2. Terazi (Günah ağır)', 12, TUR)
    ic += f'<line x1="499" y1="44" x2="499" y2="112" stroke="{LAC}" stroke-width="2.6"/><rect x="475" y="112" width="48" height="6" rx="3" fill="{LAC}"/>'
    ic += f'<line x1="443" y1="42" x2="555" y2="62" stroke="{LAC}" stroke-width="2.6"/><circle cx="499" cy="52" r="4" fill="{ALTIN}"/>'
    ic += f'<line x1="443" y1="42" x2="443" y2="60" stroke="{LAC}" stroke-width="1.5"/><rect x="415" y="60" width="56" height="20" rx="5" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(443, 74, 'Sevap', 11, YESIL_K)
    ic += f'<line x1="555" y1="62" x2="555" y2="80" stroke="{LAC}" stroke-width="1.5"/><rect x="527" y="80" width="56" height="20" rx="5" fill="#fff" stroke="{KIR}" stroke-width="1.5"/>'
    ic += yazi(555, 94, 'Günah', 11, KIR)
    ic += yazi(499, 131, 'Sonuç: Ceza', 11.5, KIR)
    return svg(600, 144, ic, 'Mizan terazisinin iki durumu (1. terazide sevap ağır, 2. terazide günah ağır) ve Enbiya suresi 47. ayet.', 24)


def enam_olcu():
    ic = f'<rect x="6" y="6" width="286" height="104" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(149, 26, 'İyilikle Gelen Kul (Enam 160)', 12, YESIL_K)
    ic += f'<rect x="24" y="42" width="84" height="36" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(66, 65, '1 İyilik', 12, YESIL_K)
    ic += f'<line x1="116" y1="60" x2="152" y2="60" stroke="{YESIL_K}" stroke-width="2.2"/><path d="M147 55 l6 5 l-6 5" fill="none" stroke="{YESIL_K}" stroke-width="2"/>'
    ic += f'<rect x="160" y="42" width="114" height="36" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(217, 65, '10 Kat Mükâfat', 12, YESIL_K)
    ic += yazi(149, 98, 'Merhamet ve lütuf ölçüsü', 11, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(451, 26, 'Kötülükle Gelen Kul (Enam 160)', 12, MAVI)
    ic += f'<rect x="326" y="42" width="84" height="36" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(368, 65, '1 Kötülük', 12, MAVI)
    ic += f'<line x1="418" y1="60" x2="454" y2="60" stroke="{MAVI}" stroke-width="2.2"/><path d="M449 55 l6 5 l-6 5" fill="none" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<rect x="462" y="42" width="114" height="36" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(519, 65, 'Yalnız 1 Dengi', 12, MAVI)
    ic += yazi(451, 98, 'Haksızlık yapmayan adalet ölçüsü', 11, LAC, ince=True)
    return svg(600, 116, ic, 'Enam suresi 160. ayet şeması: 1 iyiliğe 10 kat mükâfat, 1 kötülüğe yalnız 1 dengi karşılık.', 21)


def hadis_levha():
    ic = f'<rect x="6" y="6" width="588" height="96" rx="10" fill="#fbf7ee" stroke="{ALTIN}" stroke-width="2"/>'
    ic += f'<rect x="6" y="6" width="10" height="96" rx="4" fill="{ALTIN}"/>'
    ic += yazi(28, 28, 'Hadis-i Şerif (Tirmizi, “Sıfatü’l-Kıyâme”, 25):', 12, KAHVE, 'start')
    ic += yazi(28, 52, '“Akıllı kişi, kendini hesaba çeken ve ölümden sonrası için çalışandır…”', 12.5, LAC, 'start')
    ic += f'<rect x="28" y="66" width="220" height="26" rx="6" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(138, 83, 'Dünya: Kendini hesaba çekme', 11.5, MAVI)
    ic += f'<line x1="256" y1="79" x2="292" y2="79" stroke="{LAC}" stroke-width="2"/><path d="M287 74 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="300" y="66" width="260" height="26" rx="6" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(430, 83, 'Ahiret: Ebedî hayat için hazırlık', 11.5, YESIL_K)
    return svg(600, 108, ic, 'Tirmizi hadisi levhası: Akıllı kişi, kendini hesaba çeken ve ölümden sonrası için çalışandır.', 22)


def adalet_rahmet_kart():
    ic = f'<rect x="6" y="6" width="286" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(149, 26, '1. Kart · İlahi Adalet (Mümin 17)', 12, MAVI)
    ic += yazi(149, 50, 'Dünyada her haksızlık karşılık', 11.5, LAC, ince=True)
    ic += yazi(149, 68, 'bulmasa da ahirette eksiksiz adalet', 11.5, LAC, ince=True)
    ic += yazi(149, 86, 'gerçekleşir; kimseye zulmedilmez.', 11.5, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="106" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(451, 26, '2. Kart · İlahi Rahmet ve Tövbe', 12, YESIL_K)
    ic += yazi(451, 50, 'Allah günaha düşen kula cezayı', 11.5, LAC, ince=True)
    ic += yazi(451, 68, 'hemen vermez; düşünme, pişman olma', 11.5, LAC, ince=True)
    ic += yazi(451, 86, 've tövbe etme imkânı tanır.', 11.5, LAC, ince=True)
    return svg(600, 118, ic, 'İki kart: 1. Kart İlahi Adalet (Mümin 17), 2. Kart İlahi Rahmet ve Tövbe.', 23)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sur_ufleme()
    s[4]['gorsel'] = cennet_panosu()
    s[5]['gorsel'] = ayet_kartlari()
    s[6]['gorsel'] = hasir_mahser_sema()
    s[7]['gorsel'] = baglanti_zinciri()
    s[8]['gorsel'] = mizan_terazisi()
    s[9]['gorsel'] = enam_olcu()
    s[10]['gorsel'] = hadis_levha()
    s[12]['gorsel'] = adalet_rahmet_kart()
