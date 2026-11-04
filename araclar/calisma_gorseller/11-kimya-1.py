"""11. sınıf Kimya 1. hafta (Fiziksel ve Kimyasal Olaylarda Enerji Değişimi) görselleri.
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


def enerji_degisim_kartlari():
    kartlar = [
        ('1. Endotermik', 'Isı Alan (ΔH &gt; 0)', MAVI, MAVI_A),
        ('2. Ekzotermik', 'Isı Veren (ΔH &lt; 0)', KIR, KIR_A),
        ('3. Bağ Kırılması', 'Endotermik Süreç', TUR, TUR_A),
        ('4. Bağ Oluşumu', 'Ekzotermik Süreç', YES, YES_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Enerji değişimi ve bağ dengesi kartı.', 34)


def kalorimetre_isi_deneyi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'KALORİMETRE KABI VE SICAKLIK DEĞİŞİMİ', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Başlangıç Sıcaklığı', 9.6, KIR)
    ic += yazi(92, 76, 'Saf Su: T1 = 20 °C', 8.9, LAC, ince=True)
    ic += yazi(92, 92, 'Dengeli ortam', 8.9, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Son Sıcaklık', 9.6, YESIL_K)
    ic += yazi(267, 76, 'Tepkime Sonu: T2 = 38 °C', 8.9, LAC, ince=True)
    ic += yazi(267, 92, 'ΔT = +18 °C → Ekzotermik', 8.9, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Kalorimetre kabı sıcaklık artışı şeması.', 34)


def entalpi_seviye_grafigi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'GİRENLER VE ÜRÜNLER ENTALPİ KIYASLAMASI', 10.2, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Endotermik Olay', 9.6, CAM)
    ic += yazi(92, 76, 'H(ürünler) &gt; H(girenler)', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'ΔH = (+) pozitif', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'Ekzotermik Olay', 9.6, TUR)
    ic += yazi(267, 76, 'H(girenler) &gt; H(ürünler)', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'ΔH = (-) negatif', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Entalpi farkı karşılaştırma şeması.', 34)


def sistem_cevre_dongusu():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'SİSTEM VE ÇEVRE ARASINDAKİ ISI AKIŞI', 10.3, YESIL_K)
    ic += kutu(20, 38, 145, 68, '#ffffff', YESIL_K)
    ic += yazi(92, 58, 'SİSTEM (Reaksiyon)', 9.6, YESIL_K)
    ic += yazi(92, 78, 'İncelenen kimyasal ortam', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Isı verir / Isı alır', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 38, 145, 68, MAVI_A, MAVI)
    ic += yazi(267, 58, 'ÇEVRE (Dış Ortam)', 9.6, MAVI)
    ic += yazi(267, 78, 'Sistem dışındaki evren', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Termometre ölçüm alanı', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Sistem ve çevre ısı akışı diyagramı.', 34)


def isi_deney_adimlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 20, 'KALORİMETRE ISI ÖLÇÜM DENEY BASAMAKLARI', 10.2, TUR)
    adımlar = [
        ('1. Adım', 'İlk Sıcaklık', 16),
        ('2. Adım', 'Madde İlavesi', 102),
        ('3. Adım', 'ΔT Kaydı', 188),
        ('4. Adım', 'Q Hesabı', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', TUR)
        ic += yazi(x + 35, 56, b, 9.3, TUR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Kalorimetre deney basamakları şeması.', 34)


def potansiyel_enerji_grafigi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'POTANSİYEL ENERJİ - TEPKİME KOORDİNATI (ENDOTERMİK)', 10.1, MOR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MOR)
    ic += yazi(92, 56, 'Girenler Seviyesi', 9.6, MOR)
    ic += yazi(92, 76, 'Düşük potansiyel enerji', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Örnek: H2O(s) elektroliz', 8.8, MOR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Ürünler Seviyesi', 9.6, YESIL_K)
    ic += yazi(267, 76, 'Yüksek potansiyel enerji', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'ΔH = Hürün - Hgiren &gt; 0', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Potansiyel enerji tepkime koordinatı şeması.', 34)


def bag_enerji_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'KİMYASAL BAĞ ENERJİSİ VE ISI YÖNÜ', 10.1, YESIL_K)
    kartlar = [
        ('Naftalin Gaz', 'Endotermik', 16),
        ('Kömür Yanması', 'Ekzotermik', 102),
        ('Azot Yanması', 'Endotermik (İstisna)', 188),
        ('Cl + Cl → Cl2', 'Ekzotermik', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.6, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Kimyasal bağ enerjisi tablosu.', 34)


def deney_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, CAM)
    harfler = ['D', 'E', 'N', 'E', 'Y']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', CAM, r=4)
        ic += yazi(x + 22, 74, h, 16.0, CAM)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Deney kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = enerji_degisim_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = kalorimetre_isi_deneyi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = entalpi_seviye_grafigi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = sistem_cevre_dongusu()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = isi_deney_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = potansiyel_enerji_grafigi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = bag_enerji_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = deney_sifre_kutulari()
    s[10]['en_fazla'] = 34
