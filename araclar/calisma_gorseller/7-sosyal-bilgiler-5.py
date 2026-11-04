"""7. sınıf Sosyal Bilgiler 5. hafta (Millî Meseleler Karşısında Türk Toplumunun Tutum ve Davranışları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def milli_mesele_kavram_haritasi():
    """Soru 1: Millî mesele kavram haritası."""
    unsurlar = [
        ('1. Vatan ve Sınır Güvenliği', 'Bağımsızlık ve Bayrak', KIR, KIR_A),
        ('2. Millî Egemenlik', 'Demokrasi ve Hukuk', MAVI, MAVI_A),
        ('3. Doğal Afet Dayanışması', 'Deprem · Sel · Yangın', TUR, TUR_A),
        ('4. Ortak Değer ve Gelecek', '? (Hangisi yazılamaz?)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(unsurlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Millî meseleleri oluşturan ortak değerler kavram haritası.', 16)


def tarihten_gunumuze_dayanisma_kartlari():
    """Soru 2: Tarihten günümüze 4 millî kenetlenme örneği."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Tarihten Günümüze Millî Kenetlenme Tabloları', KAHVE)
    kartlar = [
        ('1921 · Tekâlif-i Milliye', 'Ordumuzla tam dayanışma', KIR, KIR_A, 10, 28),
        ('2023 · Asrın Dayanışması', 'Deprem bölgesine tek yürek', MAVI, MAVI_A, 184, 28),
        ('1974 · Savunma Vakıfları', 'ASELSAN · TUSAŞ · ROKETSAN', YES, YES_A, 10, 58),
        ('2016 · 15 Temmuz Ruhu', 'Demokrasi ve millî irade', TUR, TUR_A, 184, 58),
    ]
    for bas, alt, r, z, x, y in kartlar:
        ic += kutu(x, y, 166, 26, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 17, f'{bas}: {alt}', LAC, 'middle', True)
    return svg(360, 96, ic, 'Tarihten günümüze dört millî kenetlenme örneği kartı.', 16)


def cumhuriyet_milli_durus_seridi():
    """Soru 4: 1921, 1939, 1974 tarih şeridi."""
    tarihler = [
        ('1921', 'Millî Mücadele Ruhu', KIR, KIR_A, 6),
        ('1939', 'Kırk Asırlık Türk Yurdu', MAVI, MAVI_A, 126),
        ('1974', 'Kıbrıs & Millî Sanayi', YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, '#f8fafc', GRI, 8, 1.3)
    for yil, acik, r, z, x in tarihler:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.4)
        ic += yazi(x + 54, 32, f'{yil} Yılı', r)
        ic += yazi(x + 54, 58, acik, LAC, 'middle', True)
    return svg(360, 94, ic, 'Cumhuriyet döneminde millî duruş sergilenen yıllar şeridi.', 16)


def imece_vakif_kultur_koprusu():
    """Soru 5: İmece ve Vakıf kültüründen Kızılay ve AFAD'a köprü."""
    ic = kutu(4, 4, 352, 86, TUR_A, TUR, 8, 1.4)
    ic += yazi(180, 20, 'Yardımlaşma Mirasımız: Geçmişten Günümüze Köprü', TUR)
    ic += kutu(12, 28, 162, 52, '#fff', KAHVE, 6, 1.2)
    ic += yazi(93, 46, 'Köklü Kültür Mirasımız', KAHVE)
    ic += yazi(93, 66, 'İmece · Ahilik · Vakıf', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(267, 46, 'Günümüz Kurumlarımız', KIR)
    ic += yazi(267, 66, 'Türk Kızılay · AFAD · STK’lar', LAC, 'middle', True)
    return svg(360, 94, ic, 'İmece ve vakıf kültürünün günümüz yardım kurumlarına yansıması.', 16)


def ortak_gurur_panosu():
    """Soru 7: Bilim, uzay, teknoloji ve sporda ortak gurur panosu."""
    alanlar = [
        ('Bilim & Nobel', 'Prof. Dr. Aziz Sancar', MAVI, MAVI_A),
        ('Millî Teknoloji', 'Togg · İHA · Uzay Misyonu', TUR, TUR_A),
        ('Uluslararası Spor', 'Olimpiyat ve Dünya Şampiyonlukları', KIR, KIR_A),
        ('Kültür & Miras', 'UNESCO Dünya Miraslarımız', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(alanlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Bilim, teknoloji, spor ve kültürde millî gurur panosu.', 16)


def afet_dayanisma_rehberi():
    """Soru 8: Afet anında 4 adımlı bilinçli dayanışma rehberi."""
    adimlar = [
        ('1. Doğru Bilgi', 'Resmî duyuruyu izle', MAVI, MAVI_A, 6),
        ('2. Hat & Ulaşım', 'Yolları açık tut', TUR, TUR_A, 94),
        ('3. İhtiyaç Listesi', 'Uygun yardım hazırla', MOR, MOR_A, 182),
        ('4. Teslimat', 'Yetkili merkeze ulaştır', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Doğal afetlerde dört aşamalı bilinçli vatandaşlık rehberi.', 15)


def gorevini_en_iyi_yapma_panosu():
    """Soru 9: 4 öğrencinin vatanseverlik ve sorumluluk çalışmaları."""
    ogrenciler = [
        ('1. Öğrenci', 'Derslerine planlı çalışıp bilim projesi üretiyor', MAVI, MAVI_A),
        ('2. Öğrenci', 'Türkçeyi özenli kullanıp tarihini araştırıyor', KIR, KIR_A),
        ('3. Öğrenci', 'Su ve elektriği tasarruflu kullanıp fidan dikiyor', YES, YES_A),
        ('4. Öğrenci', 'Okul Kızılay kolunda yardım kampanyasına katılıyor', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(ogrenciler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Görevini en iyi yapan dört öğrencinin sorumluluk panosu.', 16)


def dezenformasyon_uyari_karti():
    """Soru 12: Dijital medyada dezenformasyona karşı bilinç kartı."""
    ic = kutu(4, 4, 352, 86, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, 'Dijital Vatandaşlık Uyarısı · Bilgi Kirliliği (Dezenformasyon)', KIR)
    ic += kutu(12, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(93, 46, 'Yanlış Tutum (✗)', KIR)
    ic += yazi(93, 66, 'Kaynağı belirsiz haberi yaymak', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Doğru Tutum (✓)', YESIL_K)
    ic += yazi(267, 66, 'Resmî açıklamaları doğrulamak', LAC, 'middle', True)
    return svg(360, 94, ic, 'Sosyal medyada yalan haberlere karşı doğru ve yanlış tutum kartı.', 16)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = milli_mesele_kavram_haritasi()
    s[1]['gorsel'] = tarihten_gunumuze_dayanisma_kartlari()
    s[3]['gorsel'] = cumhuriyet_milli_durus_seridi()
    s[4]['gorsel'] = imece_vakif_kultur_koprusu()
    s[6]['gorsel'] = ortak_gurur_panosu()
    s[7]['gorsel'] = afet_dayanisma_rehberi()
    s[8]['gorsel'] = gorevini_en_iyi_yapma_panosu()
    s[11]['gorsel'] = dezenformasyon_uyari_karti()
