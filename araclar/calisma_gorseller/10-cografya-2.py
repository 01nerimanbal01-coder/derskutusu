"""10. sınıf Coğrafya 2. hafta (Bölgesel ve Küresel Örnek Olay Analizleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'

def g0_ornek_olaylar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    olaylar = [
        ('Marmara Gölü', 'Kuraklık / Aşırı sulama', TUR, TUR_A),
        ('Süveyş Kanalı', 'Deniz ticareti tıkanması', MAVI, MAVI_A),
        ('Aral Gölü', 'Nehirlerin kesilmesi', KIR, KIR_A),
        ('Meksika Körfezi', 'Derin petrol sızıntısı', CAM, CAM_A)
    ]
    for i, (b, detay, c, d) in enumerate(olaylar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9.5, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, detay, 8, LAC, ince=True)
    return svg(360, 100, ic, 'Dört coğrafi örnek olay kartı', 34)


def g1_suveys_semasi():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    # Süveyş ve Kızıldeniz rotası
    ic += kutu(14, 12, 140, 76, '#e0ebfd', MAVI, 6, 1.2)
    ic += yazi(84, 28, 'Akdeniz', 10, MAVI)
    ic += f'<line x1="84" y1="34" x2="84" y2="60" stroke="{KIR}" stroke-width="3"/>'
    ic += yazi(84, 48, 'Süveyş', 8.5, KIR)
    ic += yazi(84, 76, 'Kızıldeniz', 10, MAVI)

    ic += kutu(168, 12, 178, 76, '#f4f8fe', MAVI, 6, 1.2)
    ic += yazi(257, 30, 'KÜRESEL HAREKET VE AĞ', 10, MAVI)
    ic += yazi(257, 48, '• Asya - Avrupa en kısa hat', 9, LAC, ince=True)
    ic += yazi(257, 64, '• Kanal tıkanınca Ümit Burnu', 9, LAC, ince=True)
    ic += yazi(257, 78, '  rotasına 12 gün gecikme', 8.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Süveyş kanalı deniz ticaret rotası şeması', 34)


def g2_marmara_golu():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    # Göl su seviyesi karşılaştırması
    ic += kutu(14, 12, 150, 76, '#fef6ec', TUR, 6, 1.2)
    ic += yazi(89, 28, 'Marmara Gölü (Manisa)', 10, TUR)
    ic += f'<ellipse cx="89" cy="54" rx="60" ry="18" fill="{CAM}" opacity="0.3"/>'
    ic += f'<ellipse cx="89" cy="54" rx="20" ry="6" fill="{KIR}" opacity="0.7"/>'
    ic += yazi(89, 56, 'Kuruyan Alan', 8, LAC)

    ic += kutu(176, 12, 170, 76, '#fff8f0', TUR, 6, 1.2)
    ic += yazi(261, 30, 'Ekolojik Sorun', 10.5, TUR)
    ic += yazi(261, 48, '• Kaçak kuyu sondajları', 9, LAC, ince=True)
    ic += yazi(261, 62, '• Tarımsal aşırı sulama', 9, LAC, ince=True)
    ic += yazi(261, 76, '• Göçmen kuşların kaybı', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Marmara gölü su alanı daralma şeması', 34)


def g3_aral_golu():
    ic = kutu(4, 4, 352, 92, KIR_A, KIR)
    # Aral gölü kronolojik küçülme
    ic += kutu(14, 12, 150, 76, '#fde8e7', KIR, 6, 1.2)
    ic += yazi(89, 28, 'Aral Gölü (Orta Asya)', 10, KIR)
    ic += f'<rect x="35" y="38" width="108" height="14" fill="{CAM}" rx="3"/>'
    ic += yazi(89, 48, '1960: 68.000 km²', 8.5, LAC)
    ic += f'<rect x="65" y="58" width="48" height="14" fill="{KIR}" rx="3"/>'
    ic += yazi(89, 68, '2018: < %10 Su', 8.5, LAC)

    ic += kutu(176, 12, 170, 76, '#fff4f4', KIR, 6, 1.2)
    ic += yazi(261, 30, 'Tuz Fırtınaları', 10.5, KIR)
    ic += yazi(261, 48, '• Seyhun & Ceyhun saptırıldı', 9, LAC, ince=True)
    ic += yazi(261, 62, '• Pamuk tarımı havzayı kuruttu', 9, LAC, ince=True)
    ic += yazi(261, 76, '• İklim karasallaştı', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Aral gölü kuruma süreci ve ekolojik yıkım', 34)


def g5_arastirma_akisi():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    adımlar = [
        ('1. Konum', 'Mekânsal sınır'),
        ('2. Veri', 'Harita ve uydu'),
        ('3. Analiz', 'İnsan-çevre bağı'),
        ('4. Rapor', 'Sürdürülebilirlik')
    ]
    for i, (b, acik) in enumerate(adımlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 40, 32, b, 10.5, YES)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{YES}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, acik, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Coğrafi araştırma basamakları akış şeması', 34)


def g6_surdurulebilirlik():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    # Üçlü denge halkaları
    ic += f'<circle cx="70" cy="50" r="28" fill="{YES}" opacity="0.25" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(70, 52, 'Çevre', 10, YES)
    ic += f'<circle cx="115" cy="50" r="28" fill="{MAVI}" opacity="0.25" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(115, 52, 'Toplum', 10, MAVI)
    # Sağ açıklama kutusu
    ic += kutu(166, 12, 180, 76, '#f2fbfd', CAM, 6, 1.2)
    ic += yazi(256, 30, 'SÜRDÜRÜLEBİLİRLİK', 11, CAM)
    ic += yazi(256, 48, 'Gelecek nesillerin ihtiyaçlarını', 9, LAC, ince=True)
    ic += yazi(256, 62, 'tehlikeye atmadan doğal', 9, LAC, ince=True)
    ic += yazi(256, 76, 'kaynakları koruyarak kullanma', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Sürdürülebilirlik ilkeleri kavram şeması', 34)


def g8_cografi_kavramlar():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kavramlar = [
        ('Konum', 'Mekândaki yer', MAVI, MAVI_A),
        ('Dağılış', 'Yayılma alanı', TUR, TUR_A),
        ('Hareket', 'Akış ve ticaret', YES, YES_A),
        ('Ölçek', 'Yerelden küresele', MOR, MOR_A)
    ]
    for i, (b, d, c, a) in enumerate(kavramlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 32, b, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Coğrafyanın temel dört kavramı kartı', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: K - A - N - A - L', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'A'), ('3', 'N'), ('4', 'A'), ('5', 'L')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 46, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 23, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 23, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Kanal şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_ornek_olaylar()
    s[1]['gorsel'] = g1_suveys_semasi()
    s[2]['gorsel'] = g2_marmara_golu()
    s[3]['gorsel'] = g3_aral_golu()
    s[5]['gorsel'] = g5_arastirma_akisi()
    s[6]['gorsel'] = g6_surdurulebilirlik()
    s[8]['gorsel'] = g8_cografi_kavramlar()
    s[10]['gorsel'] = g10_sifre_seridi()
