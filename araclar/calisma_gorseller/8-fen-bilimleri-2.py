"""8. sınıf Fen Bilimleri 2. hafta (Mevsimlerin Oluşumu: Gün Dönümleri, Ekinokslar ve Gölge Boyu) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ozel_tarihler_sema():
    kartlar = [
        ('21 Haziran', 'Yengeç’e dik (90°)', 'KYK: Yaz başlar', TUR, TUR_A),
        ('23 Eylül', 'Ekvator’a dik (90°)', 'KYK: Sonbahar (12 sa)', MOR, MOR_A),
        ('21 Aralık', 'Oğlak’a dik (90°)', 'KYK: Kış başlar', MAVI, MAVI_A),
        ('21 Mart', 'Ekvator’a dik (90°)', 'KYK: İlkbahar (12 sa)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 72, z, r, 8, 1.4)
        ic += yazi(x + 71, 24, bas, 10.8, r)
        ic += yazi(x + 71, 45, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 71, 63, s2, 10.0, r)
    return svg(600, 84, ic, 'Dört özel mevsim tarihi ve ışınların dik düştüğü enlemler.', 12)


def isik_acisi_deney_sema():
    ic = kutu(6, 6, 286, 78, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(149, 24, '1. Düzenek · K Yüzeyi (Eğik Açı: 30°)', 10.6, MAVI)
    ic += yazi(149, 46, '• Geniş alan aydınlanır → Birim enerji az', 10.0, LAC, ince=True)
    ic += yazi(149, 66, '• Termometredeki sıcaklık artışı düşük', 10.1, MAVI)

    ic += kutu(308, 6, 286, 78, TUR_A, TUR, 9, 1.5)
    ic += yazi(451, 24, '2. Düzenek · L Yüzeyi (Dik Açı: 90°)', 10.6, TUR)
    ic += yazi(451, 46, '• Dar alan aydınlanır → Birim enerji fazla', 10.0, LAC, ince=True)
    ic += yazi(451, 66, '• Termometredeki sıcaklık artışı yüksek', 10.1, TUR)
    return svg(600, 90, ic, 'Eğik ve dik açılı ışık deney düzeneklerinin karşılaştırılması.', 12)


def gece_gunduz_panosu():
    ic = kutu(6, 6, 286, 74, TUR_A, TUR, 8, 1.5)
    ic += yazi(149, 24, '21 Haziran → 21 Aralık Aralığı (KYK)', 10.6, TUR)
    ic += yazi(149, 46, 'En uzun gündüz geride kalır; gündüzler', 10.0, LAC, ince=True)
    ic += yazi(149, 64, 'kısalmaya, geceler uzamaya başlar.', 10.1, TUR)

    ic += kutu(308, 6, 286, 74, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(451, 24, '21 Aralık → 21 Haziran Aralığı (KYK)', 10.6, MAVI)
    ic += yazi(451, 46, 'En uzun gece geride kalır; gündüzler', 10.0, LAC, ince=True)
    ic += yazi(451, 64, 'uzamaya, geceler kısalmaya başlar.', 10.1, MAVI)
    return svg(600, 86, ic, 'Kuzey Yarım Küre de gün dönümlerinden sonraki gece-gündüz değişimi.', 12)


def golge_boyu_sutun_grafik():
    kartlar = [
        ('P Şehri (Yengeç Dön.)', '21 Haz. gölge: 0 cm', '21 Ara. gölge: 80 cm', TUR, TUR_A),
        ('R Şehri (Türkiye - KYK)', '21 Haz. gölge: 35 cm', '21 Ara. gölge: 110 cm', MAVI, MAVI_A),
        ('S Şehri (Güney YK)', '21 Haz. gölge: 95 cm', '21 Ara. gölge: 20 cm', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.5, r)
        ic += yazi(x + 96, 46, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.1, r)
    return svg(600, 86, ic, 'P, R ve S şehirlerinde 21 Haziran ve 21 Aralık öğle vakti gölge boyları.', 12)


def turkiye_bayrak_golgesi():
    adimlar = [
        ('21 Haziran', 'En kısa gölge (> 0)', TUR, TUR_A),
        ('23 Eylül’e Doğru', 'Açı küçülür, gölge uzar', MOR, MOR_A),
        ('21 Aralık', 'En uzun gölge boyu', MAVI, MAVI_A),
        ('21 Mart’a Doğru', 'Açı büyür, gölge kısalır', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 50, alt, 9.9, LAC, ince=True)
    return svg(600, 78, ic, 'Türkiye de yıl boyunca öğle vakti gölge boyu değişim halkaları.', 12)


def sicaklik_tablo_karti():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'X Şehri Sıcaklık Ortalaması', 10.8, MAVI)
    ic += yazi(149, 46, 'Ocak: −5 °C  ·  Temmuz: 29 °C', 10.2, LAC)
    ic += yazi(149, 64, 'Temmuz sıcak → Kuzey Yarım Küre', 10.0, MAVI, ince=True)

    ic += kutu(308, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Y Şehri Sıcaklık Ortalaması', 10.8, TUR)
    ic += yazi(451, 46, 'Ocak: 31 °C  ·  Temmuz: 2 °C', 10.2, LAC)
    ic += yazi(451, 64, 'Ocak sıcak → Güney Yarım Küre', 10.0, TUR, ince=True)
    return svg(600, 84, ic, 'X ve Y şehirlerinin Ocak ve Temmuz sıcaklık ortalamaları kartı.', 12)


def yorunge_k_m_sema():
    ic = kutu(6, 6, 588, 78, '#fbfcff', GRI, 9, 1.5)
    ic += kutu(16, 14, 196, 62, TUR_A, TUR, 8, 1.4)
    ic += yazi(114, 34, 'K Konumu (21 Haziran)', 10.5, TUR)
    ic += yazi(114, 54, 'GYK: Kış başlangıcı', 10.0, LAC, ince=True)
    ic += f'<circle cx="300" cy="45" r="22" fill="{ALTIN}" stroke="{TUR}" stroke-width="1.5"/>' + yazi(300, 49, 'Güneş', 10.0, LAC)
    ic += kutu(388, 14, 196, 62, YES_A, YES, 8, 1.4)
    ic += yazi(486, 34, 'M Konumu (21 Aralık)', 10.5, YES)
    ic += yazi(486, 54, 'GYK: Yaz başlangıcı', 10.0, LAC, ince=True)
    return svg(600, 90, ic, 'Dünya nın yörüngedeki K (21 Haziran) ve M (21 Aralık) konumları.', 12)


def aralik_mart_cizelgesi():
    ic = kutu(6, 6, 588, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(300, 24, 'Kuzey Yarım Küre · 21 Aralık → 21 Mart Süre Değişimi', 10.8, MAVI)
    ic += yazi(300, 46, '21 Aralık (9 sa gündüz, 15 sa gece)  →  Her gün gündüz uzar  →  21 Mart (12 sa gündüz, 12 sa gece)', 10.0, LAC, ince=True)
    ic += yazi(300, 64, 'Dikkat: 21 Mart ekinoksuna ulaşana dek gece süresi hâlâ gündüzden uzundur!', 10.1, KIR)
    return svg(600, 84, ic, '21 Aralık ile 21 Mart arasında gece ve gündüz süresi karşılaştırması.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ozel_tarihler_sema()
    s[1]['gorsel'] = isik_acisi_deney_sema()
    s[3]['gorsel'] = gece_gunduz_panosu()
    s[5]['gorsel'] = golge_boyu_sutun_grafik()
    s[6]['gorsel'] = turkiye_bayrak_golgesi()
    s[7]['gorsel'] = sicaklik_tablo_karti()
    s[8]['gorsel'] = yorunge_k_m_sema()
    s[11]['gorsel'] = aralik_mart_cizelgesi()
