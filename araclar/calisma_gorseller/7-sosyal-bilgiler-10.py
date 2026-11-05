"""7. sınıf Sosyal Bilgiler 10. hafta (Osmanlı Devleti’ni Cihan Devleti Yapan Politikalar: İskân, İstimalet, Gaza ve Cihat, Millet ve Tımar Sistemi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kurulus_buyume_panosu():
    kartlar = [
        (4, 4, '1. Coğrafi Konum', 'Söğüt-Domaniç (Uç Beyliği)', MAVI, MAVI_A),
        (184, 4, '2. Gaza ve Cihat', 'Batı (Bizans) yönünde fetih', YES, YES_A),
        (4, 50, '3. Komşu Durumu', 'Bizans ve Balkanlarda dağınıklık', TUR, TUR_A),
        (184, 50, '4. Beylik İlişkisi', 'Türk beylikleriyle barış ve destek', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.8, r)
        ic += yazi(x + 86, y + 34, alt, 9.1, LAC, ince=True)
    return svg(360, 96, ic, 'Osmanlı Beyliği’nin kısa sürede büyümesini sağlayan etkenler panosu.', 15)


def devlet_uygulama_kartlari():
    kartlar = [
        ('1. Rumeli Göçü', 'İskân Politikası', MAVI, MAVI_A),
        ('2. Hoşgörü', '? Politikası', YES, YES_A),
        ('3. Atlı Asker', 'Tımar Sistemi', TUR, TUR_A),
        ('4. Sosyal Eser', '? Sistemi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.8"/>'
        ic += yazi(x + 41, 54, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'İskân, İstimalet, Tımar ve Vakıf uygulama kartları.', 14)


def bosna_ahidnamesi_fermani():
    ic = kutu(6, 6, 348, 76, TUR_A, TUR)
    ic += yazi(180, 22, 'Fatih Sultan Mehmet’in Bosna Ahidnâmesi (1463)', 10.0, TUR)
    ic += yazi(180, 44, '«Bosna rahiplerine ve kiliselerine kimse engel olmayacak,', 9.3, LAC, ince=True)
    ic += yazi(180, 64, 'canları, malları ve ibadetleri devlet güvencesinde olacaktır.»', 9.3, YES)
    return svg(360, 88, ic, 'Fatih Sultan Mehmet’in Bosna Ahidnâmesi hoşgörü belgesi.', 14)


def iskan_uygulama_semasi():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'İskân Seçim İlkeleri', 10.0, MAVI)
    ic += yazi(91, 43, '• Konargöçer Yörükler seçildi', 9.2, LAC, ince=True)
    ic += yazi(91, 63, '• Husumetli ailelerden biri alındı', 9.1, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'İskân Destek İlkeleri', 10.0, YES)
    ic += yazi(269, 43, '• Toprak ve geçici vergi muafiyeti', 9.2, LAC, ince=True)
    ic += yazi(269, 63, '• Boş arazilerin tarıma açılması', 9.2, YES)
    return svg(360, 88, ic, 'İskân politikasının seçim ve destek ilkeleri şeması.', 15)


def timar_sistemi_semasi():
    kutular = [
        (6, '1. Ekonomik Boyut', 'Toprak sürekli ekilir,', 'üretim hiç aksamaz', YES, YES_A),
        (124, '2. Askerî Boyut', 'Gelirle Tımarlı Sipahi', '(atlı asker) beslenir', MAVI, MAVI_A),
        (242, '3. İdari Boyut', 'Taşrada güvenlik ve', 'devlet otoritesi sürer', TUR, TUR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kutular:
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 22, bas, 9.6, r)
        ic += yazi(x + 56, 44, s1, 8.9, LAC, ince=True)
        ic += yazi(x + 56, 62, s2, 8.9, r)
    return svg(360, 86, ic, 'Tımar sisteminin ekonomik, askerî ve idari faydaları.', 14)


def fetih_kalicilik_zinciri():
    adimlar = [
        ('1. Askerî Güç', 'Gaza ve Fetih', MAVI, MAVI_A),
        ('2. İstimalet', 'Adalet / Hoşgörü', YES, YES_A),
        ('3. İskân', 'Türkmen Göçü', TUR, TUR_A),
        ('4. Vakıf İmarı', 'Cami / Medrese', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += yazi(x + 41, 52, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'Fetihlerin kalıcı olmasını sağlayan dört aşamalı zincir.', 14)


def anadolu_zümreleri_panosu():
    kartlar = [
        (4, 4, 'Ahiyan-ı Rûm (Ahiler)', 'Esnaf dayanışması ve üretim', MAVI, MAVI_A),
        (184, 4, 'Gaziyan-ı Rûm (Alpler)', 'Vatan savunması ve gaza', KIR, KIR_A),
        (4, 50, 'Bacıyan-ı Rûm (Kadınlar)', 'Sosyal dayanışma ve üretim', YES, YES_A),
        (184, 50, 'Abdalan-ı Rûm (Dervişler)', 'Gönülleri fetheden erenler', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 9.6, r)
        ic += yazi(x + 86, y + 34, alt, 9.0, LAC, ince=True)
    return svg(360, 96, ic, 'Anadolu’da Osmanlı’yı destekleyen dört toplumsal zümre.', 15)


def seyh_edebali_karti():
    ic = kutu(6, 6, 348, 74, CAM_A, CAM)
    ic += yazi(180, 22, 'Şeyh Edebali’nin Osman Gazi’ye Vasiyeti', 10.2, CAM)
    ic += yazi(180, 44, '«Ey oğul! Beysin! Bundan sonra öfke bize, uysallık sana...', 9.3, LAC, ince=True)
    ic += yazi(180, 64, 'İnsanı yaşat ki devlet yaşasın!» (Adalet ve Sosyal Devlet)', 9.5, MAVI)
    return svg(360, 86, ic, 'Şeyh Edebali’nin İnsanı yaşat ki devlet yaşasın öğüdü.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kurulus_buyume_panosu()
    s[2]['gorsel'] = devlet_uygulama_kartlari()
    s[5]['gorsel'] = bosna_ahidnamesi_fermani()
    s[6]['gorsel'] = iskan_uygulama_semasi()
    s[7]['gorsel'] = timar_sistemi_semasi()
    s[8]['gorsel'] = fetih_kalicilik_zinciri()
    s[9]['gorsel'] = anadolu_zümreleri_panosu()
    s[11]['gorsel'] = seyh_edebali_karti()
