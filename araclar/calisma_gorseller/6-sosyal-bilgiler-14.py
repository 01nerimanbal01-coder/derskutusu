"""6. sınıf Sosyal Bilgiler 14. hafta (VII-XIII. Yüzyıl İslam Medeniyeti Ortak Miras) görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, ACIK = '#9aa6bd', '#eef1f6', '#475569', '#f8fafc'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def uygula(o):
    s = o['sorular']

    # s[0]: Hârizmî, İbn Sînâ, İbnü’l-Heysem sembollü kartlar
    ic0 = kutu(4, 4, 352, 107, GRI_A, GRI)
    bilginler = [
        ('HÂRİZMÎ', '0 · x + b = c', 'Cebir ve Algoritma', MAVI, MAVI_A),
        ('İBN SÎNÂ', 'El-Kânûn fi’t-Tıb', 'Tıp ve Eczacılık', YES, YES_A),
        ('İBNÜ’L-HEYSEM', 'Kitâbü’l-Menâzır', 'Optik ve Mercek', TUR, TUR_A),
    ]
    for i, (b, o1, o2, c, d) in enumerate(bilginler):
        x = 10 + i * 115
        ic0 += kutu(x, 11, 110, 93, d, c)
        ic0 += yazi(x + 55, 29, b, 9.0, c)
        ic0 += f'<line x1="{x+10}" y1="38" x2="{x+100}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic0 += yazi(x + 55, 62, o1, 8.5, LAC)
        ic0 += yazi(x + 55, 84, o2, 8.0, SOLUK, ince=True)
    s[0]['gorsel'] = svg(ic0, 'Hârizmî, İbn Sînâ ve İbnü’l-Heysem bilim kartları')

    # s[1]: Bağdat Beytü’l-Hikme kubbeli mimari ve 3 birim şeması
    ic1 = kutu(6, 5, 348, 105, MAVI_A, MAVI)
    ic1 += f'<path d="M140,28 Q180,4 220,28 Z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.2"/>'
    ic1 += yazi(180, 24, 'BEYTÜ’L-HİKME (Bağdat)', 8.4, LAC)
    bol = [
        ('Tercüme Bürosu', 'Antik eser çevirisi', MAVI, ACIK),
        ('Büyük Kütüphane', 'Yüz binlerce yazma', YES, YES_A),
        ('Rasathane', 'Gök gözlemi ve deney', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(bol):
        x = 14 + i * 112
        ic1 += kutu(x, 36, 106, 64, d, c)
        ic1 += yazi(x + 53, 58, b, 8.6, c)
        ic1 += yazi(x + 53, 82, alt, 7.9, LAC, ince=True)
    s[1]['gorsel'] = svg(ic1, 'Beytü’l-Hikme tercüme, kütüphane ve rasathane birimleri')

    # s[2]: Kurum kartları (Nizamiye, Darüşşifa, Divan-ı Mezalim)
    ic2 = kutu(4, 4, 352, 107, GRI_A, GRI)
    kurumlar = [
        ('Nizamiye Medresesi', 'Burslu üniversite', 'Dini + Fen ilimleri', MAVI, MAVI_A),
        ('Darüşşifa', 'Ücretsiz şifahane', 'Uygulamalı tıp', YES, YES_A),
        ('Divan-ı Mezalim', 'Yüksek mahkeme', 'Adalet ve hak arama', TUR, TUR_A),
    ]
    for i, (b, k1, k2, c, d) in enumerate(kurumlar):
        x = 10 + i * 115
        ic2 += kutu(x, 11, 110, 93, d, c)
        ic2 += yazi(x + 55, 29, b, 8.4, c)
        ic2 += f'<line x1="{x+8}" y1="38" x2="{x+102}" y2="38" stroke="{c}" stroke-width="0.7"/>'
        ic2 += yazi(x + 55, 61, k1, 8.3, LAC)
        ic2 += yazi(x + 55, 82, k2, 8.0, SOLUK, ince=True)
    s[2]['gorsel'] = svg(ic2, 'Nizamiye Medresesi, Darüşşifa ve Divan-ı Mezalim kurumları')

    # s[5]: 4 Geleneksel Sanat Kartı (Tezhip, Ebru, Hat, Çini)
    ic5 = kutu(4, 4, 352, 107, GRI_A, GRI)
    sanat = [
        ('TEZHİP', 'Altın yaldız bezeme', TUR, TUR_A),
        ('EBRU', 'Kitreli suda desen', CAM, CAM_A),
        ('HAT (Hüsnühat)', 'Estetik güzel yazı', MAVI, MAVI_A),
        ('ÇİNİ', 'Sırlı toprak karo', YES, YES_A),
    ]
    for i, (b, alt, c, d) in enumerate(sanat):
        x = 10 + i * 86
        ic5 += kutu(x, 13, 80, 89, d, c)
        ic5 += yazi(x + 40, 35, b, 8.3, c)
        ic5 += f'<line x1="{x+7}" y1="45" x2="{x+73}" y2="45" stroke="{c}" stroke-width="0.7"/>'
        ic5 += yazi(x + 40, 72, alt, 7.6, LAC, ince=True)
    s[5]['gorsel'] = svg(ic5, 'Tezhip, ebru, hat ve çini sanatları özeti')

    # s[6]: Bilim Köprüsü Rotası (Bağdat/Kahire -> Endülüs Toledo ve Sicilya -> Avrupa Rönesans)
    ic6 = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic6 += yazi(180, 22, 'Bilimsel Mirasın Avrupa’ya Aktarım Köprüleri', 9.0, CAM)
    duraklar = [
        ('İslam Dünyası', 'Bağdat · Kahire', YES, YES_A),
        ('Çeviri Köprüleri', 'Endülüs ve Sicilya', TUR, TUR_A),
        ('Avrupa Etkisi', 'Latince → Rönesans', MAVI, MAVI_A),
    ]
    for i, (b, alt, c, d) in enumerate(duraklar):
        x = 14 + i * 112
        ic6 += kutu(x, 33, 104, 65, d, c)
        ic6 += yazi(x + 52, 55, b, 8.6, c)
        ic6 += yazi(x + 52, 79, alt, 8.0, LAC, ince=True)
        if i < 2:
            ic6 += f'<polygon points="{x+105},65 {x+111},60 {x+111},70" fill="{c}"/>'
    s[6]['gorsel'] = svg(ic6, 'Endülüs ve Sicilya üzerinden Avrupa’ya bilim aktarımı şeması')

    # s[7]: Bîrûnî (Yerküre ölçümü) ve Fârâbî (İlimlerin tasnifi ve müzik)
    ic7 = kutu(6, 6, 170, 103, MAVI_A, MAVI)
    ic7 += yazi(91, 23, 'BÎRÛNÎ', 9.4, MAVI)
    ic7 += f'<circle cx="44" cy="60" r="18" fill="{ACIK}" stroke="{MAVI}" stroke-width="1.3"/><ellipse cx="44" cy="60" rx="18" ry="6" fill="none" stroke="{MAVI}" stroke-width="0.9"/>'
    ic7 += yazi(115, 55, 'Dünya’nın dönüşü', 8.0, LAC)
    ic7 += yazi(115, 73, 've yarıçap hesabı', 8.0, SOLUK, ince=True)

    ic7 += kutu(184, 6, 170, 103, MOR_A, MOR)
    ic7 += yazi(269, 23, 'FÂRÂBÎ (Muallim-i Sânî)', 8.8, MOR)
    ic7 += kutu(200, 44, 34, 32, ACIK, MOR, r=3) + yazi(217, 64, 'İlim', 8.0, MOR)
    ic7 += yazi(292, 55, 'İhsâü’l-Ulûm', 8.2, LAC)
    ic7 += yazi(292, 73, 'Felsefe ve Müzik', 8.0, SOLUK, ince=True)
    s[7]['gorsel'] = svg(ic7, 'Bîrûnî ve Fârâbî çalışma alanları kartı')

    # s[8]: 4 aşamalı kronolojik/kültürel akış
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    adim = [
        ('1. İlk İlke', '«Oku!» ve Suffe', YES, YES_A),
        ('2. Altın Çağ', 'Beytü’l-Hikme', MAVI, MAVI_A),
        ('3. Tercüme', 'Toledo ve Sicilya', TUR, TUR_A),
        ('4. Sonuç', 'Rönesans’a etki', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(adim):
        x = 10 + i * 86
        ic8 += kutu(x, 14, 80, 87, d, c)
        ic8 += yazi(x + 40, 38, b, 8.5, c)
        ic8 += f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 74, alt, 7.8, LAC, ince=True)
        if i < 3:
            ic8 += f'<polygon points="{x+81},57 {x+85},52 {x+85},62" fill="{c}"/>'
    s[8]['gorsel'] = svg(ic8, 'İslam bilim mirasının doğuşu ve Avrupa’ya etkisi akışı')

    # s[9]: Divriği Ulu Camii ve Darüşşifası (UNESCO) mimari taçkapı kemeri
    ic9 = kutu(6, 6, 348, 103, TUR_A, TUR)
    # Taçkapı geometrik kemer çizimi
    ic9 += kutu(18, 16, 74, 83, ACIK, TUR, r=3, kalin=1.2)
    ic9 += f'<path d="M30,99 L30,52 Q55,24 80,52 L80,99 Z" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.2"/>'
    ic9 += f'<polygon points="55,34 61,44 49,44" fill="{TUR}"/>'
    ic9 += kutu(106, 16, 234, 83, ACIK, LAC, r=5, kalin=0.9)
    ic9 += yazi(223, 35, 'Divriği Ulu Camii ve Darüşşifası (Sivas)', 8.8, TUR)
    ic9 += yazi(223, 55, '• Üç boyutlu geometrik taş bezemeli taçkapılar', 8.0, LAC, ince=True)
    ic9 += yazi(223, 72, '• Cami (ibadet) + Darüşşifa (ücretsiz şifahane)', 8.0, LAC)
    ic9 += yazi(223, 89, '• UNESCO Dünya Kültür Mirası Listesi’ndedir', 8.0, YES)
    s[9]['gorsel'] = svg(ic9, 'Divriği Ulu Camii ve Darüşşifası mimari bilgi kartı')
