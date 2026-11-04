"""8. sınıf Türkçe 9. hafta (Atatürk ve Eğitim, Cümlenin Ögeleri, Vurgu, Ara Söz ve Cümle Dışı Unsur) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def cumle_vurgu_panosu():
    """Soru 2 (s[1]): Fiil cümlesinde vurgunun yerini gösteren pano."""
    ic = kutu(4, 4, 352, 84, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Fiil Cümlesinde Vurgu · Yüklemden Hemen Önceki Öge', MAVI, boy=10.5)
    bolumler = [
        (10, 78, 'Başkomutan M. Kemal', 'Özne', MAVI, '#fff'),
        (92, 66, 'Temmuz 1921’de', 'Zarf T.', TUR, '#fff'),
        (162, 54, 'Ankara’da', 'Yer T.', MOR, '#fff'),
        (220, 76, 'Maarif Kongresi’ni', 'Vurgu (?)', KIR, KIR_A),
        (300, 50, 'topladı.', 'Yüklem', YESIL_K, YES_A),
    ]
    for x, w, s1, s2, r, z in bolumler:
        ic += kutu(x, 28, w, 50, z, r, 6)
        ic += yazi(x + w / 2, 47, s1, LAC, ince=True, boy=8.2)
        ic += yazi(x + w / 2, 68, s2, r, boy=9.0)
    return svg(360, 92, ic, 'Fiil cümlesinde öge dizilimi ve yüklemden önceki vurgulu öge şeması.', 15)


def ara_soz_gorev_kartlari():
    """Soru 3 (s[2]): Ara söz ve ara cümle görev kartları."""
    kartlar = [
        (4, 4, '1. Cümle · Ara Söz', '«Atatürk, Başöğretmenimiz, ...»', MAVI, MAVI_A),
        (184, 4, '2. Cümle · Ara Söz', '«Samsun’a, Karadeniz’in incisine, ...»', YES, YES_A),
        (4, 52, '3. Cümle · Ara Söz', '«Nutuk’u, o eşsiz eseri, ...»', TUR, TUR_A),
        (184, 52, '4. Cümle · Ara Cümle', '«O sabah - hiç unutmam - ...»', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.2)
    return svg(360, 100, ic, 'Dört cümlede ara söz ve ara cümle örnek kartları.', 15)


def soru_eki_oge_kartlari():
    """Soru 6 (s[5]): Soru cümlelerinde hangi ögenin buldurulduğu kartları."""
    kartlar = [
        (4, 4, '1. Kart · «Defne mi»', 'Kim okudu? -> Özne', MAVI, MAVI_A),
        (184, 4, '2. Kart · «kütüphanede mi»', 'Nerede? -> ?', YES, YES_A),
        (4, 52, '3. Kart · «ne zaman»', 'Ne zaman? -> Zarf T.', TUR, TUR_A),
        (184, 52, '4. Kart · «neyi»', 'Neyi? -> Belirtili Nesne', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.0)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.4)
    return svg(360, 100, ic, 'Dört soru cümlesinde buldurulan öge analizi kartları.', 15)


def yazim_noktalama_denetim_panosu():
    """Soru 7 (s[6]): Ara söz noktalama eşliği ve belirli gün yazımı panosu."""
    ic = kutu(4, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(90, 21, 'Ara Söz Noktalama Kuralı', KIR, boy=10.3)
    ic += yazi(90, 43, 'Doğru: , ara söz , veya - ara söz -', YESIL_K, boy=9.4)
    ic += yazi(90, 62, 'Yanlış: - ara söz , (Eşleşmez!)', KIR, boy=9.4)
    ic += yazi(90, 78, 'Başı ve sonu aynı işaret olmalı', LAC, ince=True, boy=8.8)

    ic += kutu(184, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(270, 21, 'Belirli Gün ve Hafta Adları', MAVI, boy=10.3)
    ic += yazi(270, 43, '• 10 Kasım Atatürk’ü Anma Günü', LAC, ince=True, boy=9.2)
    ic += yazi(270, 62, '• 24 Kasım Öğretmenler Günü', LAC, ince=True, boy=9.2)
    ic += yazi(270, 78, 'Her kelimesi büyük harfle başlar', MAVI, boy=9.0)
    return svg(360, 90, ic, 'Ara söz noktalaması ve belirli gün adlarının yazımı kural panosu.', 15)


def vurgu_tasima_karti():
    """Soru 8 (s[7]): Vurguyu özneye taşıma şeması."""
    ic = kutu(4, 4, 352, 82, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Cümlede Vurguyu Özneye Taşıma Yöntemi', KAHVE, boy=10.5)
    ic += kutu(12, 28, 336, 24, '#fff', TUR, 5)
    ic += yazi(180, 44, 'Mevcut: Cumhuriyet öğretmenleri / genç nesilleri / [bilimin ışığıyla] / yetiştiriyor.', LAC, ince=True, boy=9.0)
    ic += kutu(12, 56, 336, 24, YES_A, YES, 5)
    ic += yazi(180, 72, 'Hedef: Özneyi («Cumhuriyet öğretmenleri») yüklemin hemen önüne getir!', YESIL_K, boy=9.4)
    return svg(360, 90, ic, 'Fiil cümlesinde vurguyu özneye taşıma şeması.', 14)


def islem_basamaklari_sergi_akis():
    """Soru 9 (s[8]): İşlem basamaklarına göre yazma 4 aşamalı şema."""
    adimlar = [
        (4, '1. İlk olarak', 'Kitap listesini', 'belirleme', MAVI, MAVI_A),
        (93, '2. İkinci adımda', 'Eserleri toplayıp', 'tasnif etme', TUR, TUR_A),
        (182, '3. Ardından', 'Masaları ve kartları', 'düzenleme', MOR, MOR_A),
        (271, '4. Son olarak', 'Sergiyi ziyarete', 'açıp tanıtma', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=9.8)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.4)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.4)
    return svg(360, 88, ic, 'Kitap sergisi hazırlığının işlem basamaklarına göre dört aşaması.', 14)


def ataturk_egitim_metin_karti():
    """Soru 10 (s[9]): Atatürk ve Eğitim metin analizi 4 numaralı cümle kartı."""
    cumleler = [
        (4, 4, '(I) Amaç-Sonuç', 'Cehaleti yenmek amacıyla Ankara’da Maarif Kongresi toplandı.', MAVI, MAVI_A),
        (184, 4, '(II) Neden-Sonuç', 'Cephede savaş sürdüğü için kongrenin ertelenmesi önerildi.', TUR, TUR_A),
        (4, 52, '(III) Öge Dizilimi', 'Atatürk / kongrede / millî eğitim programını / açıkladı.', YES, YES_A),
        (184, 52, '(IV) Hitap (CDU)', 'Gençler! Cumhuriyet sizden fikri hür nesiller bekliyor.', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in cumleler:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 17, bas, r, boy=9.8)
        ic += yazi(x + 86, y + 35, alt, LAC, ince=True, boy=8.3)
    return svg(360, 100, ic, 'Atatürk ve Eğitim metni dört cümlelik anlam ve öge analizi kartı.', 15)


def oge_arasoz_cozumleme_karti():
    """Soru 12 (s[11]): Gazi Mustafa Kemal, Cumhuriyetimizin kurucusu, ... öge çözümleme kartı."""
    ic = kutu(4, 4, 352, 82, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Öge ve Ara Söz Çözümleme Kartı (Y – Ö – N Yöntemi)', MAVI, boy=10.5)
    ic += kutu(12, 28, 336, 26, '#fff', MAVI, 6)
    ic += yazi(180, 45, '«Gazi Mustafa Kemal, Cumhuriyetimizin kurucusu, 1928 yılında bütün millete yeni Türk harflerini öğretti.»', LAC, boy=8.2)
    ic += yazi(180, 72, 'Sorular: Kim? (Özne + Ara Söz)  |  Ne zaman?  |  Kime?  |  Neyi?  |  Yüklem', MAVI, ince=True, boy=9.4)
    return svg(360, 90, ic, 'Ara söz içeren cümlenin YÖN yöntemiyle ögelerine ayrılması kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cumle_vurgu_panosu()
    s[2]['gorsel'] = ara_soz_gorev_kartlari()
    s[5]['gorsel'] = soru_eki_oge_kartlari()
    s[6]['gorsel'] = yazim_noktalama_denetim_panosu()
    s[7]['gorsel'] = vurgu_tasima_karti()
    s[8]['gorsel'] = islem_basamaklari_sergi_akis()
    s[9]['gorsel'] = ataturk_egitim_metin_karti()
    s[11]['gorsel'] = oge_arasoz_cozumleme_karti()
