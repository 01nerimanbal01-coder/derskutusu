"""6. sınıf Türkçe 11. hafta (Rafadan Tayfa - İstiklâl Marşı ve Tema Değerlendirmesi: Sözcük Türleri, Tamlamalar ve Metin Türleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def sifat_zamir_ayrim_kartlari():
    kartlar = [
        ('1. Kart: Bazı şairler', 'İsmin önünde → Sıfat', MAVI, MAVI_A),
        ('2. Kart: O yıllarda', 'İsmin önünde → Sıfat', TUR, TUR_A),
        ('3. Kart: Hangi kıtayı', 'İsmin önünde → Sıfat', MOR, MOR_A),
        ('4. Kart: Bunu buldum', 'İsmin yerine → Zamir', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Sıfat ve zamir görevindeki sözcükleri ayırt etme kartları.', 16)


def dort_tamlama_panosu():
    kartlar = [
        ('1. bayrağın gölgesi', 'Belirtili isim tam.', MAVI, MAVI_A),
        ('2. İstiklâl Marşı', 'Ne marşı? = ?', YES, YES_A),
        ('3. sönmez şafaklar', 'Nasıl şafaklar? = ?', TUR, TUR_A),
        ('4. şairin vatan sevgisi', '3 isim = ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Belirtili, belirtisiz, zincirleme isim tamlaması ve sıfat tamlaması panosu.', 15)


def oykuleyici_bilgilendirici_pano():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 21, 'I. Metin (Olay Anlatımı)', 10.0, MAVI)
    ic += yazi(91, 42, '“O sabah Hayri ve arkadaşları', 9.2, LAC, ince=True)
    ic += yazi(91, 61, 'sahne dekorunu heyecanla kurdu.”', 9.2, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 21, 'II. Metin (Bilgi Aktarımı)', 10.0, YESIL_K)
    ic += yazi(269, 42, '“İstiklâl Marşı, 12 Mart 1921’de', 9.2, LAC, ince=True)
    ic += yazi(269, 61, '724 şiir arasından seçilmiştir.”', 9.2, LAC, ince=True)
    return svg(360, 88, ic, 'Öyküleyici ve bilgilendirici iki metnin karşılaştırma panosu.', 15)


def yazim_kurallari_kontrol_kartlari():
    kartlar = [
        ('A Kartı (✓)', 'Mehmet Âkif · İstiklâl Marşı’nı', MAVI, MAVI_A),
        ('B Kartı (!)', 'Türk Milletine (Millet büyük?)', KIR, KIR_A),
        ('C Kartı (✓)', 'TBMM’de · 12 Mart 1921', YES, YES_A),
        ('D Kartı (✓)', 'Millî Mücadele · hâlâ', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Büyük harfler, kesme işareti ve düzeltme işareti kontrol kartları.', 16)


def o_zamiri_ayrim_karti():
    ic = kutu(6, 6, 170, 76, CAM_A, CAM)
    ic += yazi(91, 21, '1. Cümle · İnsan Yerine', 10.0, CAM)
    ic += yazi(91, 43, '“O, İstiklâl Marşı’nı yazan', 9.4, LAC, ince=True)
    ic += yazi(91, 63, 'vatan şairidir.” (O = ?)', 9.5, CAM)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 21, '2. Cümle · Nesne Yerine', 10.0, TUR)
    ic += yazi(269, 43, '“O, dedemden kalan tarihi', 9.4, LAC, ince=True)
    ic += yazi(269, 63, 'madalyadır.” (O = ?)', 9.5, TUR)
    return svg(360, 88, ic, 'Kişi zamiri O ile işaret zamiri O ayrımını gösteren kart.', 15)


def serim_dugum_cozum_akisi():
    adimlar = [
        ('1. Serim', 'Tiyatro kararı', MAVI, MAVI_A),
        ('2. Düğüm', 'Merak ve araştırma', TUR, TUR_A),
        ('3. Gelişme', 'Fedakârlığı öğrenme', MOR, MOR_A),
        ('4. Çözüm', 'Sahnede coşkulu alkış', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 54, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Öyküleyici metinde serim, düğüm ve çözüm bölümleri akışı.', 15)


def sozcuk_turu_analiz_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'CÜMLEDE SÖZCÜK TÜRLERİ ANALİZ KARTI', 10.2, MOR)
    ic += yazi(180, 45, '“① Bu millet, ② sarsılmaz bir ③ cesaret ile ④ onu korumuştur.”', 9.6, LAC)
    ic += yazi(180, 66, '① Bu (+millet)   |   ② sarsılmaz (+cesaret)   |   ③ cesaret   |   ④ onu (bayrağı)', 9.0, MOR, ince=True)
    return svg(360, 88, ic, 'Cümle içindeki dört numaralı sözcüğün tür analizi kartı.', 15)


def isim_sifat_tamlamasi_farki():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 21, '1. Öbek: “tören alanı”', 10.1, YESIL_K)
    ic += yazi(91, 43, 'Soru: Ne alanı? → Tören alanı', 9.3, LAC, ince=True)
    ic += yazi(91, 63, 'Tamlanan eki: alan-ı (İyelik)', 9.3, YESIL_K)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 21, '2. Öbek: “geniş alan”', 10.1, MAVI)
    ic += yazi(269, 43, 'Soru: Nasıl alan? → Geniş alan', 9.3, LAC, ince=True)
    ic += yazi(269, 63, 'Tamlanan eki: Yok (Yalın isim)', 9.3, MAVI)
    return svg(360, 88, ic, 'Belirtisiz isim tamlaması ile sıfat tamlaması arasındaki fark kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sifat_zamir_ayrim_kartlari()
    s[2]['gorsel'] = dort_tamlama_panosu()
    s[5]['gorsel'] = oykuleyici_bilgilendirici_pano()
    s[6]['gorsel'] = yazim_kurallari_kontrol_kartlari()
    s[7]['gorsel'] = o_zamiri_ayrim_karti()
    s[8]['gorsel'] = serim_dugum_cozum_akisi()
    s[9]['gorsel'] = sozcuk_turu_analiz_karti()
    s[11]['gorsel'] = isim_sifat_tamlamasi_farki()
