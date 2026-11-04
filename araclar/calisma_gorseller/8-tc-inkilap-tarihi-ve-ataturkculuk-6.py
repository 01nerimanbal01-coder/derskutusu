"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 6. hafta (Birinci Dünya Savaşı ve Cepheler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def savas_basi_tedbirler():
    """Soru 1: Savaş başında Osmanlı Devleti'nin aldığı 4 tedbir kartı."""
    kartlar = [
        ('1. Tedbir · Siyasi', 'Tarafsızlık ilan edildi', MAVI, MAVI_A),
        ('2. Tedbir · Güvenlik', 'Boğazlar ulaşıma kapatıldı', TUR, TUR_A),
        ('3. Tedbir · Ekonomik', 'Kapitülasyonlar kaldırıldı', YES, YES_A),
        ('4. Tedbir · Askerî', 'Genel seferberlik başladı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Savaş başında Osmanlı Devleti’nin aldığı dört tedbir kartı.', 11)


def cepheler_uclu_sema():
    """Soru 2: Taarruz, Savunma ve Yardım cepheleri 3'lü şeması."""
    gruplar = [
        ('Taarruz (2K)', 'Kafkas · Kanal', 'Bizim açtıklarımız', KIR, KIR_A, 6),
        ('Savunma', 'Çanakkale · Irak', 'Hicaz · Suriye', MAVI, MAVI_A, 124),
        ('Yardım (-ya)', 'Galiçya · Romanya', 'Makedonya (Sınır dışı)', YES, YES_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in gruplar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC)
        ic += yazi(x + 56, 70, s2, LAC, 'middle', True)
    return svg(360, 94, ic, 'Osmanlı Devleti’nin savaştığı cephelerin üçlü sınıflandırması.', 11)


def almanya_amaclari_karti():
    """Soru 4: Almanya'nın Osmanlı'yı kendi yanında isteme nedenleri."""
    ic = kutu(4, 4, 352, 90, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Almanya’nın Osmanlı Devleti’ni Savaşa Çekme Amaçları', KAHVE)
    maddeler = [
        ('1. Askerî', 'Yeni cephelerle yükü azaltmak', MAVI, MAVI_A, 10, 28),
        ('2. Dini Güç', 'Halifelik (Cihat) çağrısı', MOR, MOR_A, 184, 28),
        ('3. Boğazlar', 'Rusya’ya yardımı kesmek', TUR, TUR_A, 10, 60),
        ('4. Süveyş', 'İngiliz sömürge yolunu kesmek', YES, YES_A, 184, 60),
    ]
    for bas, alt, r, z, x, y in maddeler:
        ic += kutu(x, y, 166, 28, z, r, 6, 1.2)
        ic += yazi(x + 83, y + 18, f'{bas}: {alt}', LAC, 'middle', True)
    return svg(360, 98, ic, 'Almanya’nın Osmanlı Devleti’ni savaşa çekme amaçları panosu.', 11)


def hicaz_kanal_fikir_karti():
    """Soru 5: Hicaz-Yemen cephesi ve İslamcılık fikri kartı."""
    ic = kutu(4, 4, 352, 86, TUR_A, TUR, 8, 1.4)
    ic += yazi(180, 20, 'Hicaz-Yemen Cephesi ve Fikir Akımlarına Etkisi', TUR)
    ic += kutu(14, 28, 158, 52, '#fff', YES, 6, 1.2)
    ic += yazi(93, 46, 'Medine Müdafaası', YESIL_K)
    ic += yazi(93, 66, 'Fahrettin Paşa savunması', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(267, 46, 'Şerif Hüseyin İsyanı', KIR)
    ic += yazi(267, 66, 'Halife çağrısı karşılık bulmadı', LAC, 'middle', True)
    return svg(360, 94, ic, 'Hicaz-Yemen Cephesi gelişmeleri ve fikir akımı etkisi kartı.', 11)


def canakkale_sonuclari_panosu():
    """Soru 7: Çanakkale Zaferi (1915) sonuçları panosu."""
    ic = kutu(4, 4, 352, 90, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, '1915 Çanakkale Deniz ve Kara Zaferlerinin Sonuçları', KIR)
    kutular = [
        ('Savaş Süresi', 'En az 2 yıl uzadı', MAVI, '#fff', 10),
        ('Çarlık Rusyası', 'Yardım alamadı, yıkıldı', TUR, '#fff', 126),
        ('Mustafa Kemal', 'Ulusal lider tanındı', YESIL_K, '#fff', 242),
    ]
    for bas, alt, r, z, x in kutular:
        ic += kutu(x, 28, 108, 54, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 68, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Çanakkale Zaferi’nin ulusal ve uluslararası sonuçları panosu.', 11)


def mustafa_kemal_cikis_seridi():
    """Soru 8: Mustafa Kemal'in görev yaptığı cepheler (ÇıKıS) zaman şeridi."""
    adimlar = [
        ('1. Çanakkale', '1915 · Conkbayırı', KIR, KIR_A, 6),
        ('2. Kafkas', '1916 · Muş-Bitlis', MAVI, MAVI_A, 94),
        ('3. Suriye', '1918 · Halep hattı', TUR, TUR_A, 182),
        ('4. Ateşkes', '30 Ekim Mondros', MOR, MOR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Mustafa Kemal’in Çanakkale, Kafkas ve Suriye cepheleri kronolojisi.', 11)


def kafkas_cephesi_karti():
    """Soru 9: Kafkas Cephesi ve Brest-Litovsk Antlaşması kartı."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Kafkas Cephesi Süreci ve 3 Mart 1918 Brest-Litovsk', MAVI)
    ic += kutu(12, 28, 162, 54, '#fff', MOR, 6, 1.2)
    ic += yazi(93, 46, 'Cephe Gelişmeleri', MOR)
    ic += yazi(93, 68, 'Sarıkamış · Muş ve Bitlis’in alınışı', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 54, YES_A, YES, 6, 1.3)
    ic += yazi(267, 46, 'Brest-Litovsk Sonucu', YESIL_K)
    ic += yazi(267, 68, 'Kars, Ardahan ve Batum geri alındı', LAC, 'middle', True)
    return svg(360, 96, ic, 'Kafkas Cephesi ve Brest-Litovsk Antlaşması ile kazanılan iller kartı.', 11)


def wilson_manda_karti():
    """Soru 12: Wilson İlkeleri ve Manda-Himaye dönüşümü kartı."""
    ic = kutu(4, 4, 352, 86, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'Wilson İlkeleri Karşısında İtilaf Devletleri’nin Tutumu', LAC)
    ic += kutu(14, 28, 158, 52, MAVI_A, MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Wilson İlkesi', MAVI)
    ic += yazi(93, 66, '«Toprak ve tazminat alınmayacak»', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, KIR_A, KIR, 6, 1.2)
    ic += yazi(267, 46, 'Yeni Sömürgecilik Adı', KIR)
    ic += yazi(267, 66, '«Manda ve Himaye» + Mondros 7', LAC, 'middle', True)
    return svg(360, 94, ic, 'Wilson İlkeleri ve manda-himaye sistemi karşılaştırma kartı.', 11)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = savas_basi_tedbirler()
    s[1]['gorsel'] = cepheler_uclu_sema()
    s[3]['gorsel'] = almanya_amaclari_karti()
    s[4]['gorsel'] = hicaz_kanal_fikir_karti()
    s[6]['gorsel'] = canakkale_sonuclari_panosu()
    s[7]['gorsel'] = mustafa_kemal_cikis_seridi()
    s[8]['gorsel'] = kafkas_cephesi_karti()
    s[11]['gorsel'] = wilson_manda_karti()
