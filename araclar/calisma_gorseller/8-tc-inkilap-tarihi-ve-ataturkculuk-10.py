"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 10. hafta (Sivas Kongresi, Amasya Görüşmeleri ve Ankara) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.5):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def erzurum_sivas_karsilastirma():
    """Soru 2 (s[1]): Erzurum Kongresi ve Sivas Kongresi karşılaştırma panosu."""
    ic = kutu(4, 4, 172, 86, MAVI_A, MAVI, 8)
    ic += yazi(90, 21, 'Erzurum Kongresi (Temmuz 1919)', MAVI, boy=10.1)
    ic += yazi(90, 42, '• Toplanış Biçimi: BÖLGESEL', LAC, ince=True, boy=9.6)
    ic += yazi(90, 60, '• Aldığı Kararlar: ULUSAL', LAC, ince=True, boy=9.6)
    ic += yazi(90, 78, '• Temsil Heyeti: 9 üye (Doğu)', MAVI, boy=9.6)

    ic += kutu(184, 4, 172, 86, KIR_A, KIR, 8)
    ic += yazi(270, 21, 'Sivas Kongresi (Eylül 1919)', KIR, boy=10.1)
    ic += yazi(270, 42, '• Toplanış Biçimi: ULUSAL (Millî)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 60, '• Aldığı Kararlar: ULUSAL (Millî)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 78, '• Temsil Heyeti: 16 üye (Tüm vatan)', KIR, boy=9.6)
    return svg(360, 94, ic, 'Erzurum ve Sivas kongrelerinin toplanış ve karar niteliği karşılaştırması.', 15)


def sivas_karar_kartlari():
    """Soru 3 (s[2]): Sivas Kongresi 4 temel karar ve uygulama kartı."""
    kartlar = [
        (4, 4, '1. Manda ve Himaye Reddi', '«Ya istiklal ya ölüm!» -> Tam Bağımsızlık', KIR, KIR_A),
        (184, 4, '2. ARMHC Kurulması', 'Cemiyetler birleşti -> İlke: ?', MAVI, MAVI_A),
        (4, 52, '3. Ali Fuat Paşa Ataması', 'Batı Cephesi komutanı -> Yetki: ?', TUR, TUR_A),
        (184, 52, '4. İrade-i Milliye Gazetesi', 'Halkı doğru bilgilendirme -> Alan: ?', YES, YES_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.3)
    return svg(360, 100, ic, 'Sivas Kongresi kararlarını ve uygulamalarını içeren dört bilgi kartı.', 15)


def amasya_gorusmeleri_protokolu():
    """Soru 6 (s[5]): Amasya Görüşmeleri (20-22 Ekim 1919) protokol panosu."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8)
    ic += yazi(180, 19, 'Amasya Görüşmeleri Protokolü (Mustafa Kemal Paşa ve Salih Paşa)', KAHVE, boy=10.1)
    ic += kutu(12, 26, 162, 58, MAVI_A, MAVI, 6)
    ic += yazi(93, 43, 'Bağımsızlık Maddeleri:', MAVI, boy=9.9)
    ic += yazi(93, 60, '• Vatanın bütünlüğü korunacak', LAC, ince=True, boy=9.3)
    ic += yazi(93, 76, '• Azınlıklara ayrıcalık yok', LAC, ince=True, boy=9.3)

    ic += kutu(186, 26, 162, 58, YES_A, YES, 6)
    ic += yazi(267, 43, 'Millî İrade Maddesi:', YESIL_K, boy=9.9)
    ic += yazi(267, 60, '• Seçimler hızla yapılacak ve', LAC, ince=True, boy=9.3)
    ic += yazi(267, 76, 'Mebusan Meclisi açılacak!', YESIL_K, boy=9.4)
    return svg(360, 94, ic, 'Amasya Görüşmeleri protokol maddelerini özetleyen pano.', 15)


def ankara_merkez_kartlari():
    """Soru 7 (s[6]): Ankara'nın merkez seçilme nedenlerini gösteren 4 kart."""
    kartlar = [
        (4, 4, 'I. Kart · Ulaşım & İletişim', 'Demir yolu ve telgraf ağı', MAVI, MAVI_A),
        (184, 4, 'II. Kart · Askerî Güç', '20. Kolordu’nun varlığı', TUR, TUR_A),
        (4, 52, 'III. Kart · Halk Desteği', 'Seymenlerin tam bağlılığı', YES, YES_A),
        (184, 52, 'IV. Kart · Cepheye Konum', 'Batı Cephesi’ne yakınlık', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.2)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.5)
    return svg(360, 100, ic, 'Temsil Heyetinin Ankarayı merkez seçme nedenlerini gösteren dört kart.', 15)


def milli_basin_panosu():
    """Soru 8 (s[7]): İrade-i Milliye ve Hâkimiyet-i Milliye gazeteleri panosu."""
    ic = kutu(4, 4, 172, 82, KIR_A, KIR, 8)
    ic += yazi(90, 22, 'İrade-i Milliye Gazetesi', KIR, boy=10.2)
    ic += yazi(90, 44, 'Çıkarıldığı Yer: Sivas (1919)', LAC, ince=True, boy=9.6)
    ic += yazi(90, 66, 'Anlamı: «Millî İrade»', KIR, boy=9.8)

    ic += kutu(184, 4, 172, 82, MAVI_A, MAVI, 8)
    ic += yazi(270, 22, 'Hâkimiyet-i Milliye Gazetesi', MAVI, boy=10.2)
    ic += yazi(270, 44, 'Çıkarıldığı Yer: Ankara (1920)', LAC, ince=True, boy=9.6)
    ic += yazi(270, 66, 'Anlamı: «Millî Egemenlik»', MAVI, boy=9.8)
    return svg(360, 90, ic, 'İrade-i Milliye ve Hâkimiyet-i Milliye gazetelerinin isim anlamları panosu.', 14)


def kronoloji_sivas_ankara():
    """Soru 9 (s[8]): Eylül - Aralık 1919 kronoloji şeridi."""
    adimlar = [
        (4, '1. Eylül 1919', 'Sivas Kongresi', 'toplandı', KIR, KIR_A),
        (93, '2. 30 Eylül', 'Damat Ferit', 'istifa etti', TUR, TUR_A),
        (182, '3. Ekim 1919', 'Amasya Görüşmesi', 'yapıldı', MOR, MOR_A),
        (271, '4. 27 Aralık', 'Temsil Heyeti', 'Ankara’ya geldi', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.0)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.3)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.3)
    return svg(360, 88, ic, 'Sivas Kongresinden Ankaraya gelişe dört aşamalı kronoloji şeridi.', 14)


def sivas_engelleme_ve_sonuc():
    """Soru 10 (s[9]): Sivas Kongresi engelleme girişimleri ve sonucu."""
    ic = kutu(4, 4, 172, 86, KIR_A, KIR, 8)
    ic += yazi(90, 21, 'Engelleme Girişimleri', KIR, boy=10.2)
    ic += yazi(90, 42, '• Elazığ Valisi Ali Galip olayı', LAC, ince=True, boy=9.5)
    ic += yazi(90, 60, '• Fransız Binbaşı Bruno’nun', LAC, ince=True, boy=9.5)
    ic += yazi(90, 78, 'Sivas’ı işgal tehdidi', KIR, boy=9.5)

    ic += kutu(184, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(270, 21, 'Kongrenin Sonucu', YESIL_K, boy=10.2)
    ic += yazi(270, 42, '• Tehditler boşa çıkarıldı', LAC, ince=True, boy=9.5)
    ic += yazi(270, 60, '• Sivas’ta başarıyla toplandı', LAC, ince=True, boy=9.5)
    ic += yazi(270, 78, '• Manda kesin reddedildi!', YESIL_K, boy=9.5)
    return svg(360, 94, ic, 'Sivas Kongresine yönelik engellemeler ve kongrenin başarıyla toplanması panosu.', 15)


def meclis_yeri_tartismasi_karti():
    """Soru 12 (s[11]): Mebusan Meclisi'nin toplanma yeri tartışması."""
    ic = kutu(4, 4, 352, 82, MAVI_A, MAVI, 8)
    ic += yazi(180, 20, 'Mebusan Meclisi’nin Toplanma Yeri Tartışması (Ekim 1919)', MAVI)
    ic += kutu(12, 28, 162, 48, '#fff', YES, 6)
    ic += yazi(93, 46, 'Mustafa Kemal Paşa’nın Görüşü:', YESIL_K, boy=9.8)
    ic += yazi(93, 66, '«Meclis Anadolu’da toplanmalı»', LAC, ince=True, boy=9.4)

    ic += kutu(186, 28, 162, 48, '#fff', KIR, 6)
    ic += yazi(267, 46, 'İstanbul Hükûmeti’nin Kararı:', KIR, boy=9.8)
    ic += yazi(267, 66, '«Başkent İstanbul’da toplanacak»', LAC, ince=True, boy=9.4)
    return svg(360, 90, ic, 'Mebusan Meclisinin Anadoluda mı yoksa İstanbulda mı toplanacağı tartışması kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = erzurum_sivas_karsilastirma()
    s[2]['gorsel'] = sivas_karar_kartlari()
    s[5]['gorsel'] = amasya_gorusmeleri_protokolu()
    s[6]['gorsel'] = ankara_merkez_kartlari()
    s[7]['gorsel'] = milli_basin_panosu()
    s[8]['gorsel'] = kronoloji_sivas_ankara()
    s[9]['gorsel'] = sivas_engelleme_ve_sonuc()
    s[11]['gorsel'] = meclis_yeri_tartismasi_karti()
