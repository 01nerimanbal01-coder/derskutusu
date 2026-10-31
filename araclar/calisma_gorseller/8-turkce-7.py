"""8. sınıf Türkçe 7. hafta (Cümlenin Yardımcı Ögeleri, Ara Söz ve Cümlede Vurgu) çalışma kâğıdı görselleri.
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


def yardimci_ogeler_semasi():
    """Soru 1: Cümlenin yardımcı ögeleri ve soruları 4 kutulu şema."""
    kartlar = [
        ('Belirtili Nesne', 'Ek: -ı / -i / -u / -ü', 'Soru: Neyi, kimi, nereyi?', MAVI, MAVI_A),
        ('Belirtisiz Nesne', 'Ek: Hâl eki almaz', 'Soru: Ne? (Özneden sonra)', TUR, TUR_A),
        ('Yer Tamlayıcısı', 'Ek: -e / -de / -den', 'Soru: Kime, nerede, nereden?', YES, YES_A),
        ('Zarf Tamlayıcısı', 'Zaman, durum, miktar, yön', 'Soru: Nasıl, ne zaman, niçin?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 14, bas, 10.5, r)
        ic += yazi(x + 86, y + 27, s1, 10.5, LAC, 'middle', True)
        ic += yazi(x + 86, y + 39, s2, 10.5, LAC)
    return svg(360, 96, ic, 'Yardımcı ögeler şeması: Belirtili nesne, Belirtisiz nesne, Yer tamlayıcısı ve Zarf tamlayıcısı soruları.', 14)


def cumle_cozumleme_panosu():
    """Soru 3: Fedakâr Anadolu kadınları cümlesinin 5 parçalı öge çözümleme panosu."""
    ic = kutu(4, 4, 352, 78, KUM, GRI, 8, 1.2)
    ic += yazi(180, 19, 'Cümle Çözümleme Panosu (YÖN Kuralı: Yüklem → Özne → Nesne → Tamlayıcılar)', 10.5, MAVI)
    parcalar = [
        ('Fedakâr Anadolu', 'kadınları', 'Kim?', MAVI, MAVI_A, 8, 80),
        ('cephedeki', 'askerlere', 'Kime?', TUR, TUR_A, 92, 68),
        ('kış', 'boyunca', 'Ne zaman?', MOR, MOR_A, 164, 62),
        ('cephane', '(ek yok)', 'Ne?', YES, YES_A, 230, 60),
        ('taşıdı.', '(Yargı)', 'Yüklem', KIR, KIR_A, 294, 58),
    ]
    for s1, s2, soru, r, z, x, w in parcalar:
        ic += kutu(x, 26, w, 50, z, r, 6, 1.2)
        ic += yazi(x + w / 2, 41, s1, 10.5, LAC)
        ic += yazi(x + w / 2, 55, s2, 10.5, LAC, 'middle', True)
        ic += yazi(x + w / 2, 70, soru, 10.5, r)
    return svg(360, 86, ic, 'Beş bölümlü cümle çözümleme panosu: Fedakâr Anadolu kadınları, cephedeki askerlere, kış boyunca, cephane, taşıdı.', 14)


def yon_sozcukleri_fisleri():
    """Soru 5: Yer-yön sözcüklerinin yalın ve ek almış kullanımlarını gösteren 4 fiş."""
    fisler = [
        ('1. Fiş', 'bir adım ileri çıktı', '(Yalın hâlde)', MAVI, MAVI_A),
        ('2. Fiş', 'depodan dışarıya taşıdı', '(-ya yönelme ekli)', KIR, KIR_A),
        ('3. Fiş', 'öğrenciler içeri girdi', '(Yalın hâlde)', YES, YES_A),
        ('4. Fiş', 'merdivenlerden yukarı tırmandı', '(Yalın hâlde)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 14, bas, 10.5, r)
        ic += yazi(x + 86, y + 27, s1, 10.5, LAC)
        ic += yazi(x + 86, y + 39, s2, 10.5, SOLUK, 'middle', True)
    return svg(360, 96, ic, 'Dört yön sözcüğü fişi: 1 ileri çıktı, 2 dışarıya taşıdı, 3 içeri girdi, 4 yukarı tırmandı.', 14)


def metin_karti_memleket():
    """Soru 6: Memleketin Hayatı Söz Konusu metin kartı."""
    ic = kutu(4, 4, 352, 78, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Metin Kartı: “Memleketin Hayatı Söz Konusu”', 11, MAVI)
    ic += kutu(14, 26, 332, 48, '#fff', MAVI, 6, 1.2)
    ic += yazi(180, 44, '“Ulusun bağımsızlığı tehlikeye düştüğünde,', 10.5, LAC, 'middle', True)
    ic += yazi(180, 62, 'hiçbir güçlük vatan savunmasını engelleyemez.”', 10.5, LAC)
    return svg(360, 86, ic, 'Memleketin Hayatı Söz Konusu metin kartı: vatan savunması kararlılığı ve fedakârlık.', 14)


def vurgu_kurali_semasi():
    """Soru 7: Fiil cümlesinde vurgunun yüklemden hemen önceki ögede olduğunu gösteren şema."""
    ic = kutu(4, 4, 352, 74, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 20, 'Fiil Cümlelerinde Vurgu Kuralı', 11, TUR)
    ic += kutu(20, 28, 120, 40, '#fff', GRI, 6, 1.2)
    ic += yazi(80, 52, 'Diğer Ögeler …', 11, SOLUK, 'middle', True)
    ic += kutu(150, 28, 108, 40, KIR_A, KIR, 6, 1.5)
    ic += yazi(204, 45, 'VURGULU ÖGE', 10.5, KIR)
    ic += yazi(204, 60, '(Yüklemden önce)', 10.5, LAC, 'middle', True)
    ic += kutu(268, 28, 72, 40, MAVI_A, MAVI, 6, 1.4)
    ic += yazi(304, 52, 'YÜKLEM', 11, MAVI)
    return svg(360, 82, ic, 'Fiil cümlelerinde vurgu şeması: yüklemden hemen önceki öge vurguludur.', 14)


def ara_soz_kartlari():
    """Soru 9: Dört ara söz kartı (I, II, III belirtili nesne; IV özne)."""
    kartlar = [
        ('I. Kart', '… karargâh kentini, Ankara’yı,', 'hafta sonu gezdik.', MAVI, MAVI_A),
        ('II. Kart', '… sahil ilçesini, Mudanya’yı,', 'çok özledim.', TUR, TUR_A),
        ('III. Kart', '… hatırayı, gümüş pusulayı,', 'özenle saklıyoruz.', YES, YES_A),
        ('IV. Kart', '… biri, Hasan Tahsin,', 'İzmir’de ilk kurşunu attı.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 14, bas, 10.5, r)
        ic += yazi(x + 86, y + 27, s1, 10.5, LAC)
        ic += yazi(x + 86, y + 39, s2, 10.5, SOLUK, 'middle', True)
    return svg(360, 96, ic, 'Dört ara söz kartı: I Ankarayı, II Mudanyayı, III gümüş pusulayı, IV Hasan Tahsin.', 14)


def hal_eki_tuzak_karti():
    """Soru 10: 'ayakta bekledi' (durum/zarf) ve 'kulübede bekledi' (yer tamlayıcısı) karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 74, TUR_A, TUR, 8, 1.3)
    ic += yazi(90, 20, '1. Cümle (-ta eki)', 11, TUR)
    ic += yazi(90, 40, '“Nöbetçiler bütün gece', 10.5, LAC, 'middle', True)
    ic += yazi(90, 56, 'ayakta bekledi.” (Nasıl?)', 10.5, TUR)

    ic += kutu(184, 4, 172, 74, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, '2. Cümle (-de eki)', 11, YES)
    ic += yazi(270, 40, '“Nöbetçiler nöbet', 10.5, LAC, 'middle', True)
    ic += yazi(270, 56, 'kulübede bekledi.” (Nerede?)', 10.5, YES)
    return svg(360, 82, ic, 'Karşılaştırma kartı: ayakta bekledi nasıl sorusu, kulübede bekledi nerede sorusu.', 14)


def hitabe_karti():
    """Soru 13: Atatürk'ün Gençliğe Hitabesi başlangıç cümlesi ve 'Ey Türk gençliği!' hitabı."""
    ic = kutu(4, 4, 352, 76, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, 'Atatürk’ün Gençliğe Hitabesi’nden', 11, KIR)
    ic += kutu(14, 26, 332, 46, '#fff', KIR, 6, 1.2)
    ic += yazi(180, 44, '“Ey Türk gençliği! Birinci vazifen, Türk istiklalini,', 10.5, KIR)
    ic += yazi(180, 62, 'Türk Cumhuriyetini ilelebet muhafaza etmektir.”', 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Gençliğe Hitabe kartı: Ey Türk gençliği hitabı ve birinci vazifen cümlesi.', 14)


def isim_fiil_vurgu_karti():
    """Soru 14: İsim cümlesi ve fiil cümlesinde vurgu karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, '1. Cümle (İsim Cümlesi)', 11, MAVI)
    ic += yazi(90, 40, '“En büyük güç', 10.5, LAC, 'middle', True)
    ic += yazi(90, 56, 'milletin iradesidir.”', 10.5, MAVI)

    ic += kutu(184, 4, 172, 74, MOR_A, MOR, 8, 1.3)
    ic += yazi(270, 20, '2. Cümle (Fiil Cümlesi)', 11, MOR)
    ic += yazi(270, 40, '“Milletimiz cephede', 10.5, LAC, 'middle', True)
    ic += yazi(270, 56, 'kahramanca savaştı.”', 10.5, MOR)
    return svg(360, 82, ic, 'Vurgu karşılaştırma kartı: 1. cümle isim cümlesi, 2. cümle fiil cümlesi.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = yardimci_ogeler_semasi()
    s[2]['gorsel'] = cumle_cozumleme_panosu()
    s[4]['gorsel'] = yon_sozcukleri_fisleri()
    s[5]['gorsel'] = metin_karti_memleket()
    s[6]['gorsel'] = vurgu_kurali_semasi()
    s[8]['gorsel'] = ara_soz_kartlari()
    s[9]['gorsel'] = hal_eki_tuzak_karti()
    s[12]['gorsel'] = hitabe_karti()
    s[13]['gorsel'] = isim_fiil_vurgu_karti()
