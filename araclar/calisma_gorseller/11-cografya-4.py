"""11. sınıf Coğrafya 4. hafta (Web Tabanlı CBS ve Tematik Haritalar) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def geometri_tur_kartlari():
    kartlar = [
        ('1. Nokta Geometri', 'Kuyu, Durak, İstasyon', MAVI, MAVI_A),
        ('2. Çizgi Geometri', 'Yol, Akarsu, Fay Hattı', YES, YES_A),
        ('3. Poligon Geometri', 'Orman, Göl, Parsel Alanı', TUR, TUR_A),
        ('4. Lejant Rehberi', 'Sembol ve Renk Cetveli', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Vektör geometri türleri ve lejant kartı.', 34)


def sorgulama_filtre_semasi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'MEKÂNSAL VERİ FİLTRELEME VE SORGU İŞLEMİ', 10.0, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Sorgu Kriteri', 9.2, MAVI)
    ic += yazi(92, 76, 'Eğim &gt; %20 VE Orman', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'Mantıksal VE Operatörü', 8.6, MAVI, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'Filtrelenen Parseller', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Yalnızca şartı sağlayanlar', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Haritada Vurgulanır', 8.6, YES, ince=True)
    return svg(360, 125, ic, 'Mekânsal sorgu ve filtreleme şeması.', 34)


def toplanma_alani_haritasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'KENTSEL AFET TOPLANMA ALANI TEMATİK ANALİZİ', 9.8, YESIL_K)
    adımlar = [
        ('1. Yol Erişimi', 'Ana artere &lt;200 m', 16),
        ('2. Fay Güvenliği', 'Fay hattına &gt;500 m', 102),
        ('3. Düz Zemin', 'Eğim &lt; %5 güvenli', 188),
        ('4. Seçilen Alan', 'Park ve Meydanlar', 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Afet toplanma alanı analiz kriterleri.', 34)


def cbs_katman_yonetimi_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'WEB CBS KATMAN YÖNETİMİ VE SAYDAMLIK KONTROLÜ', 9.8, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Üst Katmanlar', 9.2, TUR)
    ic += yazi(92, 76, '• Tematik Noktalar (Hastane)', 8.2, LAC, ince=True)
    ic += yazi(92, 92, '• Tematik Çizgiler (Yollar)', 8.2, LAC, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(267, 56, 'Altlık Katman', 9.2, MAVI)
    ic += yazi(267, 76, '• Sayısal Yükseklik (DEM)', 8.2, LAC, ince=True)
    ic += yazi(267, 92, '• Yüksek Çözünürlüklü Uydu', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Katman yönetimi ve altlık harita şeması.', 34)


def cbs_islem_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'WEB CBS TEMEL KATMAN İŞLEMLERİ TABLOSU', 9.8, MOR)
    satirlar = [
        ('İşlem Adı', 'Kullanılan Araç', 'Kullanım Amacı', MOR),
        ('Katman Görünürlüğü', 'Göz İkonu (Aç/Kapa)', 'Karmaşıklığı Azaltma', MAVI),
        ('Saydamlık (Opacity)', 'Yüzde Kaydırıcı (%0-%100)', 'Altlık Haritayı Görme', YESIL_K),
        ('Mekânsal Tampon', 'Tampon Kuşak (Buffer)', 'Koruma Sınırı Çizme', TUR),
    ]
    for i, (k1, k2, k3, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(180, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(285, y + 13, k3, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'CBS katman işlemleri tablosu.', 34)


def yangin_risk_analiz_kesiti():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'ORMAN YANGINI RİSK KADEME HARİTALAMASI', 10.0, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Kritik Risk Kuşağı', 9.2, KIR)
    ic += yazi(92, 76, 'Kızılçam + Düşük Nem (&lt;%20)', 8.2, LAC, ince=True)
    ic += yazi(92, 92, 'Şiddetli Rüzgâr (&gt;40 km/h)', 8.2, KIR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'Düşük Risk Kuşağı', 9.2, YESIL_K)
    ic += yazi(267, 76, 'Geniş Yapraklı Nemli Orman', 8.2, LAC, ince=True)
    ic += yazi(267, 92, 'Yüksek Nem (&gt;%65)', 8.2, YES, ince=True)
    return svg(360, 125, ic, 'Orman yangını risk kademeleri kesiti.', 34)


def tematik_harita_kartlari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'TEMATİK HARİTA OLUŞTURMA BASAMAKLARI', 10.0, CAM)
    kartlar = [
        ('1. Veri Girişi', 'Nokta ve poligon çizimi', 16),
        ('2. Öznitelik', 'Tabloya sayısal değer girme', 102),
        ('3. Semboloji', 'Renk ve boyut derecelendirme', 188),
        ('4. Çıktı Paylaşımı', 'Web harita bağlantısı açma', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 54, b, 8.2, CAM)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Tematik harita basamakları kartı.', 34)


def cbs_cikti_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'WEB TABANLI HARİTA YAYIN DÖNGÜSÜ', 10.0, YESIL_K)
    kutular = ['Saha Verisi', 'Bulut Depo', 'Canlı Harita', 'Afet Müdahale']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'Aşama {i + 1}', 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, 'Web harita yayın döngüsü kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = geometri_tur_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = sorgulama_filtre_semasi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = toplanma_alani_haritasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = cbs_katman_yonetimi_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = cbs_islem_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = yangin_risk_analiz_kesiti()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = tematik_harita_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = cbs_cikti_kutulari()
    s[10]['en_fazla'] = 34
