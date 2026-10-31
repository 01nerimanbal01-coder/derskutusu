"""8. sınıf Matematik 2. hafta (EBOB, EKOK ve Aralarında Asal Sayılar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:calc({en_fazla}mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def ebob_ekok_kural_semasi():
    """Soru 1: Asal çarpanların üslü çarpımıyla EBOB ve EKOK hesaplama kural kartları."""
    ic = kutu(4, 4, 172, 78, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'EBOB Kuralı', 11.5, MAVI)
    ic += yazi(90, 42, 'Yalnız ortak asal çarpanların', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, 'küçük üslüleri çarpılır.', 11, MAVI)
    ic += yazi(90, 74, 'Ör: EBOB(18, 30) = 2 · 3 = 6', 10.5, LAC)

    ic += kutu(184, 4, 172, 78, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'EKOK Kuralı', 11.5, TUR)
    ic += yazi(270, 42, 'Tüm asal çarpanların', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, 'büyük üslüleri çarpılır.', 11, TUR)
    ic += yazi(270, 74, 'Ör: EKOK(18, 30) = 90', 10.5, LAC)
    return svg(360, 86, ic, 'EBOB ve EKOK hesaplama şeması: EBOB için ortak asal çarpanların küçük üslüleri, EKOK için tüm asal çarpanların büyük üslüleri çarpılır.', 22)


def dort_sayi_cifti_karti():
    """Soru 3: I (12 ve 18), II (15 ve 25), III (16 ve 21), IV (20 ve 35) sayı çifti kartları."""
    kartlar = [
        ('I. kart', '12 ve 18', MAVI, MAVI_A),
        ('II. kart', '15 ve 25', TUR, TUR_A),
        ('III. kart', '16 ve 21', YES, YES_A),
        ('IV. kart', '20 ve 35', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cift, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 66, z, r, 8, 1.3)
        ic += yazi(x + 41, 22, bas, 11, r)
        ic += kutu(x + 8, 28, 66, 36, '#fff', r, 6, 1.1)
        ic += yazi(x + 41, 51, cift, 12, LAC)
    return svg(360, 78, ic, 'Dört sayı çifti kartı: I. kart 12 ve 18, II. kart 15 ve 25, III. kart 16 ve 21, IV. kart 20 ve 35.', 22)


def uslu_carpan_kartlari():
    """Soru 5: A = 2^3 * 3^2 * 5 ve B = 2^2 * 3^4 * 7 kartları."""
    ic = kutu(4, 4, 172, 74, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, 'A Sayısının Açılımı', 11, MAVI)
    ic += kutu(14, 28, 152, 40, '#fff', MAVI, 6, 1.1)
    ic += (f'<text x="90" y="53" text-anchor="middle" font-size="12" {YAZI} fill="{LAC}">'
           f'A = 2<tspan baseline-shift="super" font-size="75%">3</tspan> · '
           f'3<tspan baseline-shift="super" font-size="75%">2</tspan> · 5</text>')

    ic += kutu(184, 4, 172, 74, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, 'B Sayısının Açılımı', 11, TUR)
    ic += kutu(194, 28, 152, 40, '#fff', TUR, 6, 1.1)
    ic += (f'<text x="270" y="53" text-anchor="middle" font-size="12" {YAZI} fill="{LAC}">'
           f'B = 2<tspan baseline-shift="super" font-size="75%">2</tspan> · '
           f'3<tspan baseline-shift="super" font-size="75%">4</tspan> · 7</text>')
    return svg(360, 82, ic, 'İki asal çarpan kartı: A eşittir 2 üssü 3 çarpı 3 üssü 2 çarpı 5; B eşittir 2 üssü 2 çarpı 3 üssü 4 çarpı 7.', 22)


def zeytinyagi_bidonlari():
    """Soru 6: 48 L ve 60 L zeytinyağı depoları ve eş şişelere paylaştırma şeması."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    ic += kutu(14, 12, 102, 66, YES_A, YES, 8, 1.4)
    ic += yazi(65, 32, '1. Depo', 11, YES)
    ic += yazi(65, 54, '48 Litre', 12.5, LAC)
    ic += yazi(65, 70, '(Sızma yağ)', 10.5, SOLUK, 'middle', True)

    ic += kutu(126, 12, 102, 66, TUR_A, TUR, 8, 1.4)
    ic += yazi(177, 32, '2. Depo', 11, TUR)
    ic += yazi(177, 54, '60 Litre', 12.5, LAC)
    ic += yazi(177, 70, '(Riviera yağ)', 10.5, SOLUK, 'middle', True)

    ic += yazi(240, 48, '→', 13, MAVI)
    ic += kutu(252, 12, 94, 66, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(299, 32, 'Eşit Şişeler', 11, MAVI)
    ic += yazi(299, 52, 'En fazla ? L', 11.5, LAC)
    ic += yazi(299, 70, 'Toplam ? şişe', 10.5, MAVI)
    return svg(360, 90, ic, 'Zeytinyağı depoları şeması: 1. depo 48 litre, 2. depo 60 litre; eşit şişelere en fazla kaç litre ve toplam kaç şişe.', 22)


def deniz_fenerleri_semasi():
    """Soru 7: 15 saniye ve 20 saniye aralıklarla yanıp sönen iki deniz feneri zaman şeması."""
    ic = kutu(4, 4, 352, 80, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 20, 'Deniz Fenerlerinin Işık Çakma Aralıkları (Toplam Süre: 180 sn)', 11, MAVI)
    ic += kutu(14, 28, 158, 48, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, '1. Deniz Feneri', 11, MAVI)
    ic += yazi(93, 66, '15 saniyede bir yanar', 11, LAC, 'middle', True)
    ic += kutu(188, 28, 158, 48, '#fff', TUR, 6, 1.2)
    ic += yazi(267, 46, '2. Deniz Feneri', 11, TUR)
    ic += yazi(267, 66, '20 saniyede bir yanar', 11, LAC, 'middle', True)
    return svg(360, 88, ic, 'İki deniz feneri: 1. deniz feneri 15 saniyede bir, 2. deniz feneri 20 saniyede bir yanar; toplam süre 180 saniye.', 22)


def carpim_bagintisi_karti():
    """Soru 9: 36 ve K sayıları için EBOB(36, K) = 6 ve EKOK(36, K) = 180 kartı."""
    ic = kutu(4, 4, 352, 78, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Sayıların Çarpımı ile EBOB · EKOK İlişkisi', 11.5, MOR)
    kutular = [
        (14, 'Sayılar', '36 ve K', MAVI),
        (130, 'EBOB(36, K)', '6', YES),
        (246, 'EKOK(36, K)', '180', TUR),
    ]
    for x, bas, deg, r in kutular:
        ic += kutu(x, 28, 100, 46, '#fff', r, 6, 1.2)
        ic += yazi(x + 50, 45, bas, 10.5, r)
        ic += yazi(x + 50, 65, deg, 12, LAC)
    return svg(360, 86, ic, 'Çarpım bağıntısı kartı: Sayılar 36 ve K, EBOB 36 ve K eşittir 6, EKOK 36 ve K eşittir 180.', 22)


def dikdortgen_levha_karti():
    """Soru 10: Kenarları a cm ve b cm (aralarında asal), EKOK(a, b) = 72 olan dikdörtgen levha."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    ic += kutu(22, 16, 134, 54, YES_A, YES, 6, 1.5)
    ic += yazi(89, 46, 'Alan = a · b = ?', 11.5, YES)
    ic += yazi(89, 82, 'a cm', 11.5, LAC)
    ic += yazi(170, 46, 'b cm', 11.5, LAC)
    ic += kutu(196, 14, 150, 62, '#fff', MAVI, 7, 1.3)
    ic += yazi(271, 32, 'Verilen Bilgiler', 11, MAVI)
    ic += yazi(271, 50, 'a ve b aralarında asal', 10.5, LAC, 'middle', True)
    ic += yazi(271, 66, 'EKOK(a, b) = 72', 11, MOR)
    return svg(360, 90, ic, 'Kenar uzunlukları a cm ve b cm olan dikdörtgen levha; a ve b aralarında asal ve EKOK(a, b) eşittir 72.', 22)


def dort_problem_karti():
    """Soru 13: Dört problem durumu kartı (I, III, IV EBOB; II EKOK)."""
    kartlar = [
        ('I. Problem Kartı', 'Çuvallardaki bakliyatı', 'eş poşetlere paylaştırma', MAVI, MAVI_A),
        ('II. Problem Kartı', '12 ve 18 dk. arayla kalkan', 'iki vapurun birlikte kalkışı', TUR, TUR_A),
        ('III. Problem Kartı', 'İki tahta çubuğu eşit', 'uzunlukta parçalara kesme', YES, YES_A),
        ('IV. Problem Kartı', 'İki meyve grubunu eşit', 'sayıda kasalara dizme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 14, bas, 10.5, r)
        ic += yazi(x + 86, y + 27, s1, 10.5, LAC, 'middle', True)
        ic += yazi(x + 86, y + 39, s2, 10.5, LAC, 'middle', True)
    return svg(360, 96, ic, 'Dört problem kartı: I bakliyatı eş poşetlere paylaştırma, II iki vapurun birlikte kalkışı, III çubukları eşit parçalara kesme, IV meyveleri eşit kasalara dizme.', 24)


def tartisma_en_az_karti():
    """Soru 14: 'En az deniyorsa her zaman EKOK alınır' iddiası ve eşit gruplama karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 76, KIR_A, KIR, 8, 1.3)
    ic += yazi(90, 20, 'Yanlış Genelleme İddiası', 11, KIR)
    ic += yazi(90, 42, '“Soruda en az deniyorsa', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, 'her zaman EKOK alınır.”', 11, KIR)

    ic += kutu(184, 4, 172, 76, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, 'Eşit Gruplama Örneği', 11, YES)
    ic += yazi(270, 42, 'Paket sayısının en az olması', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, 'için paket boyu en büyük (EBOB)!', 10.5, YES)
    return svg(360, 84, ic, 'Tartışma kartı: En az deniyorsa her zaman EKOK alınır iddiası ile paket sayısının en az olması için EBOB kullanılması.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ebob_ekok_kural_semasi()
    s[2]['gorsel'] = dort_sayi_cifti_karti()
    s[4]['gorsel'] = uslu_carpan_kartlari()
    s[5]['gorsel'] = zeytinyagi_bidonlari()
    s[6]['gorsel'] = deniz_fenerleri_semasi()
    s[8]['gorsel'] = carpim_bagintisi_karti()
    s[9]['gorsel'] = dikdortgen_levha_karti()
    s[12]['gorsel'] = dort_problem_karti()
    s[13]['gorsel'] = tartisma_en_az_karti()
