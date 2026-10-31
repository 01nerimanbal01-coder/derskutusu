"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 7. hafta (Mondros Ateşkes Antlaşması, İşgaller ve Tepkiler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 punto (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def mondros_cozumleme_semasi():
    """Soru 1: Mondros Ateşkes Antlaşması hükümlerinin alanlara göre amaç şeması."""
    kartlar = [
        ('Boğazlar Hükmü', 'İstanbul ve Trakya', 'bağlantısını kesmek', KIR, KIR_A),
        ('Askerî Hüküm', 'Ordunun terhisi:', 'Savunmasız bırakmak', TUR, TUR_A),
        ('Haberleşme - Ulaşım', 'Telgraf ve demiryolu:', 'Örgütlenmeyi önlemek', MAVI, MAVI_A),
        ('Ekonomik Hüküm', 'Kömür ve tersaneler:', 'Kaynaklara el koymak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 14, bas, 10.5, r)
        ic += yazi(x + 86, y + 27, s1, 10.5, LAC, 'middle', True)
        ic += yazi(x + 86, y + 39, s2, 10.5, LAC)
    return svg(360, 96, ic, 'Mondros çözümleme şeması: Boğazlar, Askerî, Haberleşme-Ulaşım ve Ekonomik hükümlerin amaçları.', 14)


def belge_karti_7_ve_24():
    """Soru 3: Mondros 7. ve 24. maddelerinin karşılaştırmalı belge kartı."""
    ic = kutu(4, 4, 172, 78, KIR_A, KIR, 8, 1.4)
    ic += yazi(90, 20, 'Mondros — 7. Madde', 11, KIR)
    ic += yazi(90, 38, '“Güvenliği tehdit eden', 10.5, LAC, 'middle', True)
    ic += yazi(90, 54, 'herhangi bir stratejik', 10.5, LAC, 'middle', True)
    ic += yazi(90, 70, 'nokta işgal edilebilir.”', 10.5, KIR)

    ic += kutu(184, 4, 172, 78, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 20, 'Mondros — 24. Madde', 11, TUR)
    ic += yazi(270, 38, '“Vilâyât-ı Sitte’de (6 il)', 10.5, LAC, 'middle', True)
    ic += yazi(270, 54, 'karışıklık çıkarsa bölge', 10.5, LAC, 'middle', True)
    ic += yazi(270, 70, 'işgal edilebilir.”', 10.5, TUR)
    return svg(360, 86, ic, 'Mondros Ateşkes Antlaşması 7. ve 24. madde belge kartları.', 14)


def paris_baris_semasi():
    """Soru 5: 18 Ocak 1919 Paris Barış Konferansı karar ve sonuç şeması."""
    ic = kutu(4, 4, 352, 78, KUM, GRI, 8, 1.2)
    ic += yazi(180, 19, 'Paris Barış Konferansı (18 Ocak 1919) — Batı Anadolu Kararı', 11, MAVI)
    ic += kutu(12, 26, 102, 48, MAVI_A, MAVI, 6, 1.3)
    ic += yazi(63, 44, 'Gizli Antlaşmalar', 10.5, MAVI)
    ic += yazi(63, 62, 'İzmir → İtalya', 11, LAC)

    ic += yazi(122, 52, '→', 12, KIR)
    ic += kutu(130, 26, 102, 48, TUR_A, TUR, 6, 1.3)
    ic += yazi(181, 44, 'Konferans Kararı', 10.5, TUR)
    ic += yazi(181, 62, 'İzmir → Yunanistan', 10.5, LAC)

    ic += yazi(240, 52, '→', 12, KIR)
    ic += kutu(248, 26, 100, 48, KIR_A, KIR, 6, 1.3)
    ic += yazi(298, 44, 'Siyasi Sonuç', 10.5, KIR)
    ic += yazi(298, 62, 'Görüş Ayrılığı!', 10.5, KIR)
    return svg(360, 86, ic, 'Paris Barış Konferansı şeması: İzmirin İtalya yerine Yunanistana verilmesi ve görüş ayrılığı.', 14)


def ani_karti_bogaz():
    """Soru 6: 13 Kasım 1918 İstanbul Boğazı anı kartı — Geldikleri gibi giderler!"""
    ic = kutu(4, 4, 352, 76, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, 'Tarihî Anı Kartı · 13 Kasım 1918 · İstanbul Boğazı', 11, MAVI)
    ic += kutu(16, 28, 328, 44, '#fff', MAVI, 6, 1.2)
    ic += yazi(180, 46, 'İtilaf donanmasını gören Mustafa Kemal Paşa:', 10.5, LAC, 'middle', True)
    ic += yazi(180, 64, '“Geldikleri gibi giderler!”', 12, KIR)
    return svg(360, 84, ic, '13 Kasım 1918 İstanbul Boğazı anı kartı: Mustafa Kemal Paşanın Geldikleri gibi giderler sözü.', 14)


def uc_farkli_tutum_tablosu():
    """Soru 7: İşgallere karşı İstanbul Hükûmeti, Mustafa Kemal Paşa ve Türk milletinin tutumu."""
    sutunlar = [
        ('İstanbul Hükûmeti', 'Teslimiyetçi', 'Nasihat Heyetleri', KIR, KIR_A, 6),
        ('Mustafa Kemal Paşa', 'Bağımsızlıkçı', 'Millî Mücadele', MAVI, MAVI_A, 124),
        ('Türk Milleti', 'Vatansever', 'Kuvâ-yı Milliye', YES, YES_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in sutunlar:
        ic += kutu(x, 4, 112, 74, z, r, 7, 1.3)
        ic += yazi(x + 56, 20, bas, 10.5, r)
        ic += kutu(x + 6, 26, 100, 44, '#fff', r, 5, 1.1)
        ic += yazi(x + 56, 44, s1, 10.5, LAC)
        ic += yazi(x + 56, 61, s2, 10.5, SOLUK, 'middle', True)
    return svg(360, 82, ic, 'İşgallere karşı üç tutum: İstanbul Hükûmeti teslimiyetçi, Mustafa Kemal Paşa bağımsızlıkçı, Türk milleti direnişçi.', 14)


def isgal_bolgeleri_panosu():
    """Soru 9: Mondros sonrasında işgal edilen başlıca bölgeler bilgi panosu."""
    bolgeler = [
        ('İngiltere', 'Musul (İlk işgal: 3 Kasım 1918)', KIR, KIR_A),
        ('Fransa', 'Adana, Antep, Urfa ve Maraş', MAVI, MAVI_A),
        ('İtalya', 'Antalya ve Konya çevresi', YES, YES_A),
        ('Yunanistan', 'İzmir (15 Mayıs 1919)', MOR, MOR_A),
    ]
    ic = ''
    for i, (dev, yer, r, z) in enumerate(bolgeler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 16, dev, 11, r)
        ic += yazi(x + 86, y + 32, yer, 10.5, LAC, 'middle', True)
    return svg(360, 92, ic, 'Mondros sonrası işgal bölgeleri panosu: İngiltere Musul, Fransa Adana Antep Urfa Maraş, İtalya Antalya Konya, Yunanistan İzmir.', 14)


def ilk_kursun_karsilastirma_karti():
    """Soru 10: Güney Cephesi (Hatay-Dörtyol) ve Batı Cephesi (İzmir - Hasan Tahsin) ilk direniş kartları."""
    ic = kutu(4, 4, 172, 76, TUR_A, TUR, 8, 1.3)
    ic += yazi(90, 20, 'Güneyde İlk Direniş', 11, TUR)
    ic += yazi(90, 40, 'Yer: Hatay - Dörtyol', 10.5, LAC)
    ic += yazi(90, 56, 'Fransız işgaline karşı', 10.5, LAC, 'middle', True)
    ic += yazi(90, 71, 'ilk silahlı direniş', 10.5, TUR)

    ic += kutu(184, 4, 172, 76, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, 'Batıda İlk Kurşun', 11, KIR)
    ic += yazi(270, 40, '15 Mayıs 1919 · İzmir', 10.5, LAC)
    ic += yazi(270, 56, 'Gazeteci Hasan Tahsin', 10.5, LAC)
    ic += yazi(270, 71, 'Ulusal bilinci uyandırdı', 10.5, KIR)
    return svg(360, 84, ic, 'İlk direnişler kartı: Güneyde Hatay Dörtyol, Batıda 15 Mayıs 1919 İzmirde Hasan Tahsin.', 14)


def milli_direnis_asamalari():
    """Soru 13: Türk milletinin işgallere karşı tepki aşamaları şeması."""
    ic = kutu(4, 4, 352, 78, KUM, GRI, 8, 1.2)
    ic += yazi(180, 19, 'Türk Milletinin İşgallere Karşı Tepki Aşamaları', 11, LAC)
    asamalar = [
        ('1. Aşama', 'Telgraflar', 've mitingler', MAVI, MAVI_A, 10),
        ('2. Aşama', 'Müdafaa-i Hukuk', 'Cemiyetleri', TUR, TUR_A, 129),
        ('3. Aşama', 'Kuvâ-yı Milliye', '(Silahlı direniş)', YES, YES_A, 248),
    ]
    for bas, s1, s2, r, z, x in asamalar:
        ic += kutu(x, 26, 102, 48, z, r, 6, 1.3)
        ic += yazi(x + 51, 41, bas, 10.5, r)
        ic += yazi(x + 51, 55, s1, 10.5, LAC)
        ic += yazi(x + 51, 68, s2, 10.5, LAC, 'middle', True)
    ic += yazi(120.5, 52, '→', 12, LAC)
    ic += yazi(239.5, 52, '→', 12, LAC)
    return svg(360, 86, ic, 'Türk milletinin tepki aşamaları: 1 Protesto ve mitingler, 2 Müdafaa-i Hukuk Cemiyetleri, 3 Kuvâ-yı Milliye.', 14)


def wilson_mondros_degerlendirme_karti():
    """Soru 14: Wilson İlkeleri vaadi ile Mondros sonrası işgal uygulaması karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Wilson İlkeleri Vaadi', 11, MAVI)
    ic += yazi(90, 42, '“Yenen devletler yenilenlerden', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, 'toprak almayacaktır.”', 10.5, MAVI)

    ic += kutu(184, 4, 172, 74, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, 'Mondros Sonrası Uygulama', 11, KIR)
    ic += yazi(270, 42, '7. madde bahanesiyle', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, 'Anadolu’nun işgal edilmesi', 10.5, KIR)
    return svg(360, 82, ic, 'Wilson İlkeleri toprak alınmayacak vaadi ile Mondros 7. madde bahanesiyle Anadolunun işgali karşılaştırma kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = mondros_cozumleme_semasi()
    s[2]['gorsel'] = belge_karti_7_ve_24()
    s[4]['gorsel'] = paris_baris_semasi()
    s[5]['gorsel'] = ani_karti_bogaz()
    s[6]['gorsel'] = uc_farkli_tutum_tablosu()
    s[8]['gorsel'] = isgal_bolgeleri_panosu()
    s[9]['gorsel'] = ilk_kursun_karsilastirma_karti()
    s[12]['gorsel'] = milli_direnis_asamalari()
    s[13]['gorsel'] = wilson_mondros_degerlendirme_karti()
