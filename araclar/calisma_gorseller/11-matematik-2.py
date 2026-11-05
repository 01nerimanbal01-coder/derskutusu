"""11. sınıf Matematik 2. hafta görselleri.
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


def korelasyon_deger_kartlari():
    kartlar = [
        ('1. r = +0.85', 'Güçlü Pozitif', YES, YES_A),
        ('2. r = -0.90', 'Çok Güçlü Negatif', KIR, KIR_A),
        ('3. r = 0.05', 'İlişkisiz Dağılım', MAVI, MAVI_A),
        ('4. r = -0.40', 'Orta Zayıf Negatif', TUR, TUR_A),
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
    return svg(360, 125, ic, 'Korelasyon katsayısı r değerleri kartı.', 34)

def serpme_diyagrami_pozitif():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'POZİTİF DOĞRUSAL İLİŞKİ SERPME DİYAGRAMI', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, 'Eğilim Yönü', 9.6, YESIL_K)
    ic += yazi(92, 76, 'Sağa yukarı yönelen noktalar', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'x artarken y de artar', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, MAVI_A, MAVI)
    ic += yazi(267, 56, 'Korelasyon Gücü', 9.6, MAVI)
    ic += yazi(267, 76, 'r &gt; 0 (Pozitif Değer)', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Ör: Çalışma süresi &amp; net', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Pozitif serpme diyagramı modeli.', 34)

def r_katsayisi_aralik_cetveli():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'KORELASYON KATSAYISI (r) SAYI DOĞRUSU ARALIĞI', 10.2, CAM)
    araliklar = [
        ('-1.0 (Tam Negatif)', 'Mükemmel Ters', 16),
        ('-0.5 (Orta Negatif)', 'Ters Yönlü', 102),
        ('0.0 (İlişkisiz)', 'Doğrusal Bağ Yok', 188),
        ('+1.0 (Tam Pozitif)', 'Mükemmel Doğru', 274),
    ]
    for b, d, x in araliklar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 8.4, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Korelasyon katsayısı sayı doğrusu cetveli.', 34)

def bso_dort_bolge_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'BÖLGELERE GÖRE SAYIM ORANI (BSO) DÖRT BÖLGE MODELİ', 10.3, TUR)
    ic += kutu(20, 38, 145, 68, '#ffffff', TUR)
    ic += yazi(92, 58, '1. ve 3. Bölgeler', 9.4, TUR)
    ic += yazi(92, 78, 'Nokta yoğunluğu fazlaysa', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Pozitif Korelasyon Kararı', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 38, 145, 68, '#ffffff', KIR)
    ic += yazi(267, 58, '2. ve 4. Bölgeler', 9.4, KIR)
    ic += yazi(267, 78, 'Nokta yoğunluğu fazlaysa', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Negatif Korelasyon Kararı', 8.8, KIR, ince=True)
    return svg(360, 125, ic, 'BSO yöntemi 4 bölge karar şeması.', 34)

def veri_analiz_adimlari():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'İKİ NİCEL DEĞİŞKENLİ ANALİZ ADIMLARI', 10.2, MOR)
    adımlar = [
        ('1. Veri', 'Eşleşmiş (x,y)', 16),
        ('2. Diyagram', 'Serpme Çizimi', 102),
        ('3. Eğilim', 'Doğru Belirleme', 188),
        ('4. r Katsayısı', 'Güç Kararı', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'İki nicel analiz basamakları.', 34)

def dort_serpme_tipi_semasi():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'GÜÇLÜ NEGATİF KORELASYON DİYAGRAMI MODELİ', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Eğilim Doğrusu', 9.4, KIR)
    ic += yazi(92, 76, 'Sağa aşağı inen dar hat', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'x artarken y azalır', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, 'r Değeri Yaklaşımı', 9.4, TUR)
    ic += yazi(267, 76, 'r ≈ -0.90 ile -1.00', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Çok güçlü negatif ilişki', 8.8, TUR, ince=True)
    return svg(360, 125, ic, 'Güçlü negatif korelasyon diyagramı.', 34)

def korelasyon_aralik_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'KORELASYON GÜCÜ SINIFLANDIRMA ARALIKLARI', 10.1, YESIL_K)
    kartlar = [
        ('0.80 - 1.00', 'Çok Güçlü Bağ', 16),
        ('0.60 - 0.80', 'Güçlü Bağ', 102),
        ('0.40 - 0.60', 'Orta Düzey Bağ', 188),
        ('0.00 - 0.20', 'Zayıf / Önemsiz', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Korelasyon gücü aralık kartları.', 34)

def serpme_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['S', 'E', 'R', 'P', 'M', 'E']
    for i, h in enumerate(harfler):
        x = 42 + i * 46
        ic += kutu(x, 42, 40, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 20, 74, h, 16.0, MAVI)
        ic += yazi(x + 20, 36, f'{i + 1}. Harf', 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Serpme kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = korelasyon_deger_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = serpme_diyagrami_pozitif()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = r_katsayisi_aralik_cetveli()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = bso_dort_bolge_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = veri_analiz_adimlari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = dort_serpme_tipi_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = korelasyon_aralik_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = serpme_sifre_kutulari()
    s[10]['en_fazla'] = 34
