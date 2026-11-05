"""11. sınıf Felsefe 2. hafta görselleri.
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


def felsefe_donem_kartlari():
    kartlar = [
        ('1. İlk Çağ (Physis)', 'Canlı Organizma', YES, YES_A),
        ('2. Modern Dönem', 'Mekanik Makine', TUR, TUR_A),
        ('3. 20. Yüzyıl Kriz', 'İçsel Değer Arayışı', MAVI, MAVI_A),
        ('4. Çevre Etiği', 'Bütüncül Sorumluluk', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Felsefe tarihinde doğa anlayışları kartı.', 34)

def bacon_bilgi_guc_karti():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'FRANCIS BACON: MODERN DOĞA ANLAYIŞI', 10.3, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Bilgi Güçtür Tezi', 9.4, TUR)
    ic += yazi(92, 76, 'Doğayı fethetme gayesi', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Mekanik nesne algısı', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Çağdaş Eleştiri', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Sömürü yerine uyum arayışı', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Ekolojik denge bilinci', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Bacon bilgi güçtür tezi ve eleştirisi.', 34)

def uc_etik_cember_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'AHLAKİ ÇEMBERİN GENİŞLEME KESİTİ', 10.3, MAVI)
    ic += kutu(20, 36, 95, 70, TUR_A, TUR)
    ic += yazi(67, 56, 'Antroposentrik', 9.2, TUR)
    ic += yazi(67, 76, 'Yalnızca İnsan', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Araçsal Değer', 8.8, TUR, ince=True)

    ic += kutu(132, 36, 95, 70, YES_A, YES)
    ic += yazi(179, 56, 'Biyosentrik', 9.2, YESIL_K)
    ic += yazi(179, 76, 'Tüm Canlılar', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Yaşama Saygı', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 36, 95, 70, '#ffffff', MAVI)
    ic += yazi(292, 56, 'Ekosentrik', 9.2, MAVI)
    ic += yazi(292, 76, 'Toprak, Su, Hava', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Bütüncül Değer', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Ahlaki çember genişleme aşamaları.', 34)

def derin_ekoloji_ilkeleri():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'DERİN EKOLOJİ (ARNE NAESS) İLKELERİ', 10.3, YESIL_K)
    ic += kutu(20, 38, 145, 68, '#ffffff', YES)
    ic += yazi(92, 58, 'Biyotik Eşitlik İlkesi', 9.6, YESIL_K)
    ic += yazi(92, 78, 'İnsan türü doğanın üstünde', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'değil, eşit bir parçasıdır', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 38, 145, 68, CAM_A, CAM)
    ic += yazi(267, 58, 'Zengin Çeşitlilik', 9.6, CAM)
    ic += yazi(267, 78, 'Tüm yaşam biçimlerinin', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'kendinde değeri esastır', 8.8, CAM, ince=True)
    return svg(360, 125, ic, 'Derin ekoloji temel ilkeleri şeması.', 34)

def felsefe_tarih_seridi_2():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'İNSAN-DOĞA ANLAYIŞININ TARİHSEL ADIMLARI', 10.2, CAM)
    adımlar = [
        ('1. Mitolojik', 'Kutsal Doğa', 16),
        ('2. Antik Felsefe', 'Arkhe Arayışı', 102),
        ('3. Aydınlanma', 'Mekanik Nesne', 188),
        ('4. Çağdaş', 'Biyoetik &amp; Denge', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.3, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Doğa anlayışının tarihsel zaman şeridi.', 34)

def toprak_etigi_piramidi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'ALDO LEOPOLD: TOPRAK ETİĞİ MODELİ', 10.3, MOR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MOR)
    ic += yazi(92, 56, 'Biyotik Topluluk Üyeliği', 9.4, MOR)
    ic += yazi(92, 76, 'Toprak, su, bitki ve hayvan', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'ortak yaşam ağını kurar', 8.8, MOR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Ahlaki İlke Kuralı', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Topluluğun bütünlüğünü ve', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'güzelliğini koruyan eylem iyidir', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Aldo Leopold toprak etiği şeması.', 34)

def akim_tez_eslestirme_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'ÇEVRE ETİĞİ AKIMLARI VE TEMEL TEZLERİ', 10.1, YESIL_K)
    kartlar = [
        ('Toprak Etiği', 'Sade Üye Olma', 16),
        ('Derin Ekoloji', 'Biyotik Eşitlik', 102),
        ('Sorumluluk', 'Gelecek Kuşaklar', 188),
        ('Sığ Ekoloji', 'İnsan Refahı', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Çevre etiği akım ve tez kartı.', 34)

def doga_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, TUR)
    harfler = ['D', 'O', 'Ğ', 'A']
    for i, h in enumerate(harfler):
        x = 75 + i * 56
        ic += kutu(x, 42, 48, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 24, 74, h, 16.0, TUR)
        ic += yazi(x + 24, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Doğa kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = felsefe_donem_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = bacon_bilgi_guc_karti()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = uc_etik_cember_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = derin_ekoloji_ilkeleri()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = felsefe_tarih_seridi_2()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = toprak_etigi_piramidi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = akim_tez_eslestirme_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = doga_sifre_kutulari()
    s[10]['en_fazla'] = 34
