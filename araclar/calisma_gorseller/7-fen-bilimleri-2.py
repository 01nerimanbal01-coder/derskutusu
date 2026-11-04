"""7. sınıf Fen Bilimleri 2. hafta (Uzay Gözlem Araçlarının Modeli ve Uzay Kirliliği) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yorunge_ve_isik_sema():
    ic = kutu(6, 6, 368, 86, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(190, 23, 'Dünya Yörüngesindeki İşlevsiz Parçalar (Uzay Kirliliği)', 10.6, MAVI)
    ic += f'<circle cx="64" cy="58" r="22" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>' + yazi(64, 62, 'Dünya', 10.0, '#fff')
    ic += f'<ellipse cx="64" cy="58" rx="46" ry="26" fill="none" stroke="{KIR}" stroke-width="1.2" stroke-dasharray="4 3"/>'
    ic += yazi(235, 45, '• Görevi bitmiş eski haberleşme uydusu', 10.0, LAC, 'middle', True)
    ic += yazi(235, 62, '• Boş yakıt tankı ve roket kademesi', 10.0, LAC, 'middle', True)
    ic += yazi(235, 79, '• Kopmuş uzay sondası parçaları', 10.0, KIR)

    ic += kutu(386, 6, 208, 86, TUR_A, TUR, 9, 1.5)
    ic += yazi(490, 24, 'Yeryüzü · Gözlemevi Çevresi', 10.6, TUR)
    ic += yazi(490, 48, 'Cadde ve şehir aydınlatmaları', 10.1, LAC, ince=True)
    ic += yazi(490, 68, '→ Işık Kirliliği (Uzay çöpü değil)', 10.2, TUR)
    return svg(600, 98, ic, 'Yörüngedeki uzay çöpleri ile yeryüzündeki ışık kirliliği ayrımı.', 12)


def alti_ayakkabi_cozum_kartlari():
    kartlar = [
        ('Gri Spor Ayakkabısı', 'Radar ve teleskopla izleme', '#64748b', GRI_A),
        ('Turuncu Lastik Çizme', 'Acil çarpışma riskini önleme', TUR, TUR_A),
        ('Lacivert Resmî Ayakkabı', 'Yörüngeden çıkarma kuralları', LAC, MAVI_A),
        ('Kahverengi Yürüyüş', 'Pratik ve faydalı mekanizma', KAHVE, '#f7efe6'),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.3, r)
        ic += yazi(x + 71, 52, alt, 9.8, LAC, ince=True)
    return svg(600, 80, ic, 'Altı ayakkabı tekniğiyle uzay kirliliği çözüm kartları.', 12)


def gozlem_ve_ssn_panosu():
    ic = kutu(6, 6, 286, 76, YES_A, YES, 8, 1.5)
    ic += yazi(149, 24, 'Model Tasarım ve Değerlendirme', 10.8, YES)
    ic += yazi(149, 46, '• Basit ve atık malzemelerle özgün model', 10.0, LAC, ince=True)
    ic += yazi(149, 66, '• Dereceli puanlama ve öz değerlendirme', 10.0, YES)

    ic += kutu(308, 6, 286, 76, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(451, 24, 'Uzay Gözetim Ağı (SSN) Raporu', 10.8, MAVI)
    ic += yazi(451, 46, '• Radar ve teleskoplarla kalıntıları izler', 10.0, LAC, ince=True)
    ic += yazi(451, 66, '• 130 milyondan fazla çok hızlı uzay çöpü', 10.0, MAVI)
    return svg(600, 88, ic, 'Model değerlendirme araçları ve Uzay Gözetim Ağı bilgileri.', 12)


def etki_zinciri_sema():
    kutular = [
        ('Uzay Çöpleri Artar', 'Yüksek hızla çarpışma', KIR, KIR_A),
        ('Haberleşme Aksar', 'İletişim uyduları zarar görür', TUR, TUR_A),
        ('Ulaşım Etkilenir', 'Konum sinyalleri kesilir', MAVI, MAVI_A),
        ('Ulusal Güvenlik', 'Gözlem uyduları tehlikeye girer', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kutular):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 68, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 52, alt, 9.9, LAC, ince=True)
    return svg(600, 80, ic, 'Uzay kirliliğinin yeryüzündeki yaşamda aksatabileceği alanlar.', 12)


def model_basamak_rehberi():
    adimlar = [
        ('1. Planla ve Çiz', 'Özgün tasarım kâğıda', MAVI, MAVI_A),
        ('2. Modeli Oluştur', 'Basit ve atık gereçler', TUR, TUR_A),
        ('3. Sınıfa Sun', 'Anlat ve dikkatle dinle', YES, YES_A),
        ('4. Geliştir', 'Karşılaştır ve araştır', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.5, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Uzay gözlem aracı modeli hazırlama adımları.', 12)


def hiz_hasar_karti():
    ic = kutu(6, 6, 588, 74, KIR_A, KIR, 9, 1.5)
    ic += yazi(300, 25, 'Neden Küçük Bir Parça Bile Büyük Tehlike Oluşturur?', 11.0, KIR)
    ic += yazi(300, 48, 'Kalıntı Boyutu: Yalnızca bilye veya vida büyüklüğünde (1–2 cm)', 10.2, LAC, ince=True)
    ic += yazi(300, 66, 'Yörünge Hareket Özelliği: Çok yüksek hız → Çarpışma anında yıkıcı darbe!', 10.4, KIR)
    return svg(600, 86, ic, 'Küçük uzay çöplerinin yüksek hız nedeniyle oluşturduğu çarpışma tehlikesi.', 12)


def iki_proje_karti():
    ic = kutu(6, 6, 286, 76, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 25, 'K Grubu Projesi · Temizleme Ağı', 10.8, MAVI)
    ic += yazi(149, 47, 'Yörüngede başıboş dolanan eski uydu ve', 10.1, LAC, ince=True)
    ic += yazi(149, 65, 'roket parçalarını yakalayıp Dünya’ya indirmek', 10.2, MAVI)

    ic += kutu(308, 6, 286, 76, YES_A, YES, 8, 1.5)
    ic += yazi(451, 25, 'L Grubu Projesi · Çevreci Roket', 10.8, YES)
    ic += yazi(451, 47, 'Uzaya parça bırakmayan, yeniden kullanılan', 10.1, LAC, ince=True)
    ic += yazi(451, 65, 'sürdürülebilir uzay araçları geliştirmek', 10.2, YES)
    return svg(600, 88, ic, 'Mevcut uzay çöpünü azaltan K projesi ile yeni çöp oluşumunu önleyen L projesi.', 12)


def kirlilik_fark_karti():
    ic = kutu(6, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(149, 24, 'Işık Kirliliği', 10.8, TUR)
    ic += yazi(149, 46, 'Ortam: Yeryüzü atmosferi (şehir ışıkları)', 10.1, LAC, ince=True)
    ic += yazi(149, 63, 'Etkisi: Gözlemevi görüntüsünü bozar', 10.1, TUR)

    ic += kutu(308, 6, 286, 72, MOR_A, MOR, 8, 1.5)
    ic += yazi(451, 24, 'Uzay Kirliliği', 10.8, MOR)
    ic += yazi(451, 46, 'Ortam: Dünya çevresindeki uzay yörüngesi', 10.1, LAC, ince=True)
    ic += yazi(451, 63, 'Etkisi: Uzay araçlarına çarpma tehlikesi', 10.1, MOR)
    return svg(600, 84, ic, 'Işık kirliliği ile uzay kirliliğinin ortam ve etki karşılaştırması.', 12)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yorunge_ve_isik_sema()
    s[2]['gorsel'] = alti_ayakkabi_cozum_kartlari()
    s[3]['gorsel'] = gozlem_ve_ssn_panosu()
    s[5]['gorsel'] = etki_zinciri_sema()
    s[6]['gorsel'] = model_basamak_rehberi()
    s[7]['gorsel'] = hiz_hasar_karti()
    s[8]['gorsel'] = iki_proje_karti()
    s[11]['gorsel'] = kirlilik_fark_karti()
