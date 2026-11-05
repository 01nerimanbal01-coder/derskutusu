"""8. sınıf Din Kültürü ve Ahlak Bilgisi 10. hafta (Zekât Verilecekler ve Sadaka) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#dcfce7', '#f3e8ff', '#fee2e2', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def akrabalik_zekat_semasi():
    """Soru 2 (s[1]): Usûl, fürû, eş (verilmez) ve yan soy akrabalar (verilir) şeması."""
    ic = kutu(4, 4, 172, 86, KIR_A, KIR, 8)
    ic += yazi(90, 21, 'Bakmakla Yükümlü Oldukları', KIR, boy=10.2)
    ic += yazi(90, 42, '• Usûl: Anne · Baba · Dede', LAC, ince=True, boy=9.8)
    ic += yazi(90, 60, '• Fürû: Oğul · Kız · Torun', LAC, ince=True, boy=9.8)
    ic += yazi(90, 78, '• Eş (Karı-Koca) -> VERİLMEZ', KIR, boy=9.8)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(270, 21, 'Yan Soy Yakın Akrabalar', YESIL_K, boy=10.2)
    ic += yazi(270, 42, '• Kardeşler (Abla · Ağabey)', LAC, ince=True, boy=9.8)
    ic += yazi(270, 60, '• Amca · Hala · Dayı · Teyze', LAC, ince=True, boy=9.8)
    ic += yazi(270, 78, 'Yoksul iseler -> VERİLİR', YESIL_K, boy=9.8)
    return svg(360, 94, ic, 'Zekât verilemeyen usûl-fürû-eş ile zekât verilebilen yan soy akrabalar şeması.', 15)


def dort_ibadet_hukum_karti():
    """Soru 3 (s[2]): Zekât, Fitre, Genel Sadaka ve Sadaka-i Cariye kartları."""
    kartlar = [
        (4, 4, '1. Zekât İbadeti', 'Yıllık malî ibadet · Farz', MAVI, MAVI_A),
        (184, 4, '2. Fıtır Sadakası', 'Ramazan şükrü · Hükmü: ?', TUR, TUR_A),
        (4, 52, '3. Genel Sadaka', 'Maddi-manevi iyilik · Hükmü: ?', MOR, MOR_A),
        (184, 52, '4. Sadaka-i Cariye', 'Kalıcı hayır eseri · Hükmü: ?', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.3)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.6)
    return svg(360, 100, ic, 'Zekât, fitre, genel sadaka ve sadaka-i cariye karşılaştırma kartları.', 15)


def bakara_264_kaya_benzetmesi():
    """Soru 6 (s[5]): Bakara 264 sağanak yağmur ve sert kaya benzetmesi."""
    ic = kutu(4, 4, 352, 84, KUM, ALTIN, 8)
    ic += yazi(180, 20, 'Bakara Suresi 264. Ayet · Kaya ve Sağanak Yağmur Temsili', KAHVE)
    ic += kutu(12, 28, 162, 52, KIR_A, KIR, 6)
    ic += yazi(93, 46, 'Olumsuz Davranış:', KIR, boy=10.0)
    ic += yazi(93, 66, 'Başa kakma · Gönül kırma · Riya', LAC, ince=True, boy=9.4)

    ic += kutu(186, 28, 162, 52, MAVI_A, MAVI, 6)
    ic += yazi(267, 46, 'Ayetteki Benzetme Sonucu:', MAVI, boy=10.0)
    ic += yazi(267, 66, 'Toprağı akıp giden çıplak kaya', LAC, ince=True, boy=9.4)
    return svg(360, 92, ic, 'Bakara suresi 264. ayetteki başa kakma ve sert kaya benzetmesi panosu.', 15)


def sadakai_cariye_uckarti():
    """Soru 7 (s[6]): Sadaka-i cariyenin 3 kolu."""
    kartlar = [
        (6, '1. Kalıcı Hayır Eseri', 'Okul · Cami · Çeşme', 'Hastane · Ağaç dikimi', YES, YES_A),
        (124, '2. Faydalı İlim', 'İnsanlığa yararlı kitap', 've bilimsel buluşlar', MAVI, MAVI_A),
        (242, '3. Salih Evlat', 'Anne-babasının ardından', 'hayır dua eden evlat', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 4, 112, 84, z, r, 8)
        ic += yazi(x + 56, 22, bas, r, boy=10.0)
        ic += yazi(x + 56, 46, s1, LAC, ince=True, boy=9.3)
        ic += yazi(x + 56, 66, s2, LAC, boy=9.3)
    return svg(360, 92, ic, 'Vefattan sonra amel defterini açık tutan üç sadaka-i cariye unsuru.', 15)


def ibnus_sebil_durum_karti():
    """Soru 8 (s[7]): Yolculukta parası biten zengin yolcu (İbnü's-Sebîl) kartı."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(90, 22, 'Memleketindeki Durumu', MAVI)
    ic += yazi(90, 44, 'Bursa’da evi ve fabrikası var', LAC, ince=True, boy=9.8)
    ic += yazi(90, 64, '(Nisap miktarı mal sahibi)', MAVI, boy=9.6)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8)
    ic += yazi(270, 22, 'Yolculuktaki Durumu', TUR)
    ic += yazi(270, 44, 'Çantası çalındı, parası bitti', LAC, ince=True, boy=9.8)
    ic += yazi(270, 64, 'Tevbe 60 Sınıfı: ?', TUR, boy=9.8)
    return svg(360, 90, ic, 'Memleketinde zengin olup yolculukta parasız kalan İbnüs-Sebil durum kartı.', 14)


def infak_adabi_akis():
    """Soru 9 (s[8]): 4 adımlı infak adabı akış şeması."""
    adimlar = [
        (4, '1. Niyet', 'Yalnız Allah', 'rızası (İhlas)', MAVI, MAVI_A),
        (93, '2. Mal Seçimi', 'Helal, temiz ve', 'kaliteli mal', YES, YES_A),
        (182, '3. Öncelik', 'Yoksul akraba', 've komşular', TUR, TUR_A),
        (271, '4. Teslim', 'Gizlilik ve', 'onur koruma', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.2)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.4)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.4)
    return svg(360, 88, ic, 'İnfak adabının niyetten teslim aşamasına dört basamaklı akış şeması.', 14)


def zekat_sadaka_karsilastirma():
    """Soru 10 (s[9]): Zekât ve Sadaka karşılaştırma panosu."""
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi(90, 21, 'Zekât İbadeti', MAVI, boy=10.3)
    ic += yazi(90, 42, '• Hükmü farzdır (Nisap şartı)', LAC, ince=True, boy=9.5)
    ic += yazi(90, 60, '• Yılda 1 kez mal ile verilir', LAC, ince=True, boy=9.5)
    ic += yazi(90, 78, '• Tevbe 60’taki 8 sınıfa verilir', MAVI, boy=9.5)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(270, 21, 'Sadaka İbadeti', YESIL_K, boy=10.3)
    ic += yazi(270, 42, '• Sünnettir (Fitre vaciptir)', LAC, ince=True, boy=9.5)
    ic += yazi(270, 60, '• Zaman ve miktar sınırı yoktur', LAC, ince=True, boy=9.5)
    ic += yazi(270, 78, '• Maddi ve manevi olabilir', YESIL_K, boy=9.5)
    return svg(360, 94, ic, 'Zekât ve sadaka ibadetlerinin hükümleri ve kapsamları karşılaştırma panosu.', 15)


def bakara_267_ayet_karti():
    """Soru 12 (s[11]): Bakara suresi 267. ayet malın iyisinden infak etme kartı."""
    ic = kutu(4, 4, 352, 82, YES_A, YES, 8)
    ic += yazi(180, 21, 'Bakara Suresi 267. Ayet · İnfakta Kalite ve Nezaket İlkesi', YESIL_K)
    ic += yazi(180, 46, '«Ey iman edenler! Kazandıklarınızın iyilerinden infak edin...', LAC, ince=True, boy=10.0)
    ic += yazi(180, 68, 'Size verilse gözünüzü yummadan alamayacağınız kötü malı vermeyin.»', LAC, boy=10.0)
    return svg(360, 90, ic, 'Bakara suresi 267. ayet mealini içeren infak adabı kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = akrabalik_zekat_semasi()
    s[2]['gorsel'] = dort_ibadet_hukum_karti()
    s[5]['gorsel'] = bakara_264_kaya_benzetmesi()
    s[6]['gorsel'] = sadakai_cariye_uckarti()
    s[7]['gorsel'] = ibnus_sebil_durum_karti()
    s[8]['gorsel'] = infak_adabi_akis()
    s[9]['gorsel'] = zekat_sadaka_karsilastirma()
    s[11]['gorsel'] = bakara_267_ayet_karti()
