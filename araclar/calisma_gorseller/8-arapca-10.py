"""8. sınıf Arapça 10. hafta (2. Ünite: Kültür ve Sanat — Sinema ve Tiyatro) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Türkçe Noto Sans 11-12 pt, Arapça Arial 18-20 pt RTL (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, SARI_A = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fefce8'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi_tr(x, y, metin, renk=LAC, hiza='middle', kalin=True, boy=10.8):
    ag = '700' if kalin else '500'
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def yazi_ar(x, y, metin, renk=LAC, hiza='middle', boy=19):
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="{boy}" fill="{renk}">{metin}</text>'


def kultur_merkezi_afisleri():
    """Soru 2 (s[1]): 1 ve 2 numaralı salon etkinlik afişleri."""
    ic = kutu(4, 4, 352, 26, MOR_A, MOR, 7)
    ic += yazi_tr(95, 21, 'Kültür Merkezi Salon Afişleri', MOR)
    ic += yazi_ar(265, 22, 'السِّينَمَا وَالْمَسْرَحُ', LAC, boy=17)

    ic += kutu(4, 34, 172, 60, TUR_A, TUR, 8)
    ic += yazi_tr(90, 52, '1. Salon (الصَّالَة ١)', TUR)
    ic += yazi_ar(90, 82, 'مَسْرَحِيَّةٌ تَارِيخِيَّةٌ', LAC)

    ic += kutu(184, 34, 172, 60, MAVI_A, MAVI, 8)
    ic += yazi_tr(270, 52, '2. Salon (الصَّالَة ٢)', MAVI)
    ic += yazi_ar(270, 82, 'فِيلْمٌ وَثَائِقِيٌّ عِلْمِيٌّ', LAC)
    return svg(360, 98, ic, '1. salon tarihî tiyatro oyunu ve 2. salon bilimsel belgesel film afişi.', 15)


def gise_soru_kartlari():
    """Soru 3 (s[2]): Gişe ve fuar 4 soru kalıbı kartı."""
    kartlar = [
        (4, 4, '1. Yer Sorusu', 'إِلَى أَيْنَ تَذْهَبُ؟', MAVI, MAVI_A),
        (184, 4, '2. Kişi Sorusu', 'مَعَ مَنْ تُشَاهِدُ؟', TUR, TUR_A),
        (4, 52, '3. Saat Sorusu', 'مَتَى يَبْدَأُ الْعَرْضُ؟', YES, YES_A),
        (184, 52, '4. Ücret Sorusu', 'كَمْ سِعْرُ التَّذَاكِرِ؟', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi_tr(x + 86, y + 17, bas, r, boy=10.3)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=17)
    return svg(360, 100, ic, 'Gişe ve kültür etkinliklerinde kullanılan dört soru kartı.', 15)


def gise_bilet_diyalogu():
    """Soru 6 (s[5]): Bilet gişesi (شُبَّاكُ التَّذَاكِرِ) diyalog panosu."""
    ic = kutu(4, 4, 352, 42, MOR_A, MOR, 8)
    ic += yazi_tr(14, 22, 'Gişe Görevlisi:', MOR, 'start')
    ic += yazi_ar(232, 31, 'مَاذَا تُرِيدِينَ مِنْ شُبَّاكِ التَّذَاكِرِ؟', LAC, boy=17)

    ic += kutu(4, 50, 352, 44, YES_A, YES, 8)
    ic += yazi_tr(14, 68, 'Meryem:', YES, 'start')
    ic += yazi_ar(215, 81, 'أُرِيدُ تَذْكِرَتَيْنِ لِمَسْرَحِيَّةٍ كُومِيدِيَّةٍ', LAC, boy=17)
    return svg(360, 98, ic, 'Tiyatro bilet gişesinde Meryem ile görevli arasındaki konuşma panosu.', 15)


def dort_tercih_karti():
    """Soru 7 (s[6]): 4 kültür-sanat cümle kartı (I. kart el sanatları eğlencelidir)."""
    kartlar = [
        (4, 4, 'I. Kart', 'اَلْأَعْمَالُ الْيَدَوِيَّةُ مُمْتِعَةٌ', YES, YES_A),
        (184, 4, 'II. Kart', 'اَلرِّوَايَةُ التَّارِيخِيَّةُ طَوِيلَةٌ', MAVI, MAVI_A),
        (4, 52, 'III. Kart', 'أُحِبُّ الرُّسُومَ الْمُتَحَرِّكَةَ', MOR, MOR_A),
        (184, 52, 'IV. Kart', 'اَلصُّنْدُوقُ فِي زَاوِيَةِ الْغُرْفَةِ', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, ar, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi_tr(x + 86, y + 16, bas, r, boy=10.2)
        ic += yazi_ar(x + 86, y + 38, ar, LAC, boy=16)
    return svg(360, 100, ic, 'Dört öğrencinin kültür ve sanat ifadelerini içeren kartlar.', 15)


def calisma_ozdeyis_panosu():
    """Soru 8 (s[7]): Çalışma ve üretme temalı Arapça özdeyiş panosu."""
    ic = kutu(4, 4, 352, 82, SARI_A, TUR, 8)
    ic += yazi_tr(180, 22, 'El Sanatları Atölyesi Özdeyiş Panosu', TUR)
    ic += yazi_ar(180, 52, 'مَنْ لَا يَعْمَلُ لَا يُنْتِجُ', LAC, boy=20)
    ic += yazi_ar(180, 76, 'اَلْعَمَلُ خَيْرٌ مِنَ التَّسَوُّلِ', YES, boy=18)
    return svg(360, 90, ic, 'Çalışmayan üretmez ve çalışmak dilenmekten hayırlıdır yazılı pano.', 14)


def tiyatro_zaman_seridi():
    """Soru 9 (s[8]): أَوَّلًا -> قَبْلَ -> ثُمَّ -> بَعْدَ sıralama şeması."""
    adimlar = [
        (4, '1. İlk Adım', 'أَوَّلًا: الذَّهَابُ', MAVI, MAVI_A),
        (93, '2. Gösterim Öncesi', 'قَبْلَ الْعَرْضِ', TUR, TUR_A),
        (182, '3. Gösterim Anı', 'ثُمَّ الْمُشَاهَدَةُ', MOR, MOR_A),
        (271, '4. Gösterim Sonu', 'بَعْدَ الْعَرْضِ', YES, YES_A),
    ]
    ic = ''
    for x, bas, ar, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi_tr(x + 42, 22, bas, r, boy=9.8)
        ic += yazi_ar(x + 42, 60, ar, LAC, boy=16)
    return svg(360, 88, ic, 'Tiyatro ziyaretinde kullanılan dört sıralama bağlacı akış şeması.', 14)


def sinema_seans_panosu():
    """Soru 10 (s[9]): Sinema seans, tür ve bilet kuralı bilgi panosu."""
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi_tr(90, 21, 'Gösterim Türü ve Kuralı', MAVI, boy=10.2)
    ic += yazi_ar(90, 48, 'فِيلْمٌ وَثَائِقِيٌّ عَنِ الطَّبِيعَةِ', LAC, boy=16)
    ic += yazi_ar(90, 76, 'اَلتَّذَاكِرُ قَبْلَ الدُّخُولِ', KIR, boy=16)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi_tr(270, 21, 'Başlama ve Bitiş Saati', YES, boy=10.2)
    ic += yazi_ar(270, 48, 'يَبْدَأُ: السَّاعَةَ السَّادِسَةَ مَسَاءً', LAC, boy=15)
    ic += yazi_ar(270, 76, 'يَنْتَهِي: السَّاعَةَ الثَّامِنَةَ مَسَاءً', LAC, boy=15)
    return svg(360, 94, ic, 'Doğa belgeseli filmi seans saatleri ve giriş öncesi bilet kuralı panosu.', 15)


def gezi_ozet_karti():
    """Soru 12 (s[11]): Tiyatro gezisi özet cümle kartı."""
    ic = kutu(4, 4, 352, 84, MOR_A, MOR, 8)
    ic += yazi_tr(180, 21, 'Hafta Sonu Tiyatro Gezisi Özet Kartı', MOR)
    ic += yazi_ar(180, 50, 'ذَهَبْتُ إِلَى الْمَسْرَحِ مَعَ وَالِدِي، وَاشْتَرَيْنَا التَّذَاكِرَ', LAC, boy=17)
    ic += yazi_ar(180, 76, 'قَبْلَ الْعَرْضِ، ثُمَّ شَاهَدْنَا مَسْرَحِيَّةً تَارِيخِيَّةً', YES, boy=17)
    return svg(360, 92, ic, 'Babamla tiyatroya gidiş, gösterimden önce bilet alış ve oyun izleyiş kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kultur_merkezi_afisleri()
    s[2]['gorsel'] = gise_soru_kartlari()
    s[5]['gorsel'] = gise_bilet_diyalogu()
    s[6]['gorsel'] = dort_tercih_karti()
    s[7]['gorsel'] = calisma_ozdeyis_panosu()
    s[8]['gorsel'] = tiyatro_zaman_seridi()
    s[9]['gorsel'] = sinema_seans_panosu()
    s[11]['gorsel'] = gezi_ozet_karti()
