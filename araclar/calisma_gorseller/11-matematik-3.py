"""11. sınıf Matematik 3. hafta (Serpilme Diyagramı ve Korelasyon) görselleri.
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


def korelasyon_tur_kartlari():
    kartlar = [
        ('1. Güçlü Pozitif', 'r = +0,80 .. +1,00', YES, YES_A),
        ('2. Güçlü Negatif', 'r = -0,80 .. -1,00', KIR, KIR_A),
        ('3. Zayıf İlişki', 'r = ±0,20 .. ±0,40', TUR, TUR_A),
        ('4. Sıfır İlişki', 'r ≈ 0,00 (Bağımsız)', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.0, LAC, ince=True)
    return svg(360, 125, ic, 'Korelasyon türleri ve katsayı aralıkları kartı.', 34)


def serpilme_nokta_bulutu():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'POZİTİF KORELASYON SERPİLME DİYAGRAMI (r ≈ +0,92)', 9.8, YESIL_K)
    ic += '<line x1="30" y1="105" x2="330" y2="105" stroke="#0b2257" stroke-width="0.75"/>'
    ic += '<line x1="30" y1="105" x2="30" y2="35" stroke="#0b2257" stroke-width="0.75"/>'
    ic += yazi(180, 118, 'X Değişkeni (Çalışma Saati)', 8.0, LAC, ince=True)
    ic += yazi(18, 40, 'Y', 8.0, LAC, ince=True)
    # Noktalar ve eğilim çizgisi
    ic += '<line x1="45" y1="95" x2="315" y2="45" stroke="#12a150" stroke-width="0.75" stroke-dasharray="3,3"/>'
    noktalar = [(55, 92), (80, 88), (110, 80), (140, 75), (170, 68), (200, 64), (230, 58), (260, 52), (290, 48)]
    for px, py in noktalar:
        ic += f'<circle cx="{px}" cy="{py}" r="3" fill="#2451d6"/>'
    return svg(360, 125, ic, 'Pozitif doğrusal serpilme diyagramı.', 34)


def negatif_iliski_modeli():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'TERS YÖNLÜ (NEGATİF) KORELASYON İLİŞKİSİ', 10.0, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Sürat Artışı (V)', 9.2, TUR)
    ic += yazi(92, 76, 'Ortalama hız yükselir', 8.6, LAC, ince=True)
    ic += yazi(92, 92, 'X ekseni artış yönünde', 8.6, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(267, 56, 'Varış Süresi (t)', 9.2, KIR)
    ic += yazi(267, 76, 'Hedefe varış kısalır', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'Y ekseni azalır (r &lt; 0)', 8.6, KIR, ince=True)
    return svg(360, 125, ic, 'Negatif korelasyon model şeması.', 34)


def korelasyon_aralik_cetveli():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'KORELASYON KATSAYISI (r) DEĞER CETVELİ [-1, +1]', 9.8, MAVI)
    adımlar = [
        ('-1.00', 'Tam Negatif Doğrusal', 16, KIR),
        ('-0.50', 'Orta Negatif', 102, TUR),
        ('0.00', 'Doğrusal İlişki Yok', 188, MAVI),
        ('+1.00', 'Tam Pozitif Doğrusal', 274, YES),
    ]
    for deg, ad, x, r in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', r)
        ic += yazi(x + 35, 54, deg, 9.6, r)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, ad, 7.6, LAC, ince=True)
    return svg(360, 125, ic, 'Korelasyon katsayısı sayı doğrusu cetveli.', 34)


def korelasyon_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'İKİ NİCEL DEĞİŞKEN ARASINDAKİ KORELASYON TABLOSU', 9.8, MOR)
    satirlar = [
        ('Değişken 1', 'Değişken 2', 'Korelasyon Katsayısı (r)', 'İlişki Türü', MOR),
        ('Ders Çalışma Saati', 'Sınav Puanı', '+0,88', 'Güçlü Pozitif', YESIL_K),
        ('Araç Yaşı', 'Piyasa Fiyatı', '-0,76', 'Güçlü Negatif', KIR),
        ('Ayakkabı Ölçüsü', 'Sınav Başarısı', '0,02', 'Sıfır (İlişkisiz)', MAVI),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = '#ffffff' if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(60, y + 13, k1, 8.0, r)
        ic += yazi(138, y + 13, k2, 8.0, LAC, ince=(i > 0))
        ic += yazi(218, y + 13, k3, 8.2, LAC, ince=(i > 0))
        ic += yazi(296, y + 13, k4, 8.0, LAC, ince=(i > 0))
    return svg(360, 125, ic, 'Korelasyon örnekleri karşılaştırma tablosu.', 34)


def dogrusal_model_tahmin():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, 'DOĞRUSAL MODEL: y = ax + b İLE TAHMİN', 10.0, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Model Formülü', 9.2, CAM)
    ic += yazi(92, 76, 'y = 2x + 10', 9.4, LAC)
    ic += yazi(92, 92, 'a: Eğim, b: Sabit', 8.2, CAM, ince=True)
    ic += kutu(195, 36, 145, 70, '#ffffff', YES)
    ic += yazi(267, 56, 'Tahmin Değeri', 9.2, YESIL_K)
    ic += yazi(267, 76, 'x = 20 için', 8.6, LAC, ince=True)
    ic += yazi(267, 92, 'y = 2(20) + 10 = 50', 8.8, YES, ince=True)
    return svg(360, 125, ic, 'Doğrusal model denklem ve tahmin şeması.', 34)


def aykiri_deger_etkisi_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'SERPİLME GRAFİĞİNDE AYKIRI (UÇ) DEĞER ETKİSİ', 10.0, TUR)
    kartlar = [
        ('1. Tipik Küme', 'Genel doğrusal eğilim', 16),
        ('2. Uç Veri Noktası', 'Kümeden çok uzakta nokta', 102),
        ('3. Katsayı Sapması', 'r değerini yanıltıcı yapar', 188),
        ('4. İnceleme Şartı', 'Özel sebep araştırılır', 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 54, b, 8.0, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.8, LAC, ince=True)
    return svg(360, 125, ic, 'Aykırı değer etkisi bilgi kartları.', 34)


def istatistik_adimlari_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, 'İKİ DEĞİŞKENLİ VERİ ANALİZİ AŞAMALARI', 10.0, YESIL_K)
    kutular = ['Veri Toplama', 'Serpilme Grafiği', 'Korelasyon (r)', 'Model Kurma']
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, '#ffffff', YESIL_K, r=4)
        ic += yazi(x + 37, 66, f'Adım {i + 1}', 8.2, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, 'İki değişkenli analiz aşamaları kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = korelasyon_tur_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = serpilme_nokta_bulutu()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = negatif_iliski_modeli()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = korelasyon_aralik_cetveli()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = korelasyon_tablosu()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = dogrusal_model_tahmin()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = aykiri_deger_etkisi_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = istatistik_adimlari_kutulari()
    s[10]['en_fazla'] = 34
