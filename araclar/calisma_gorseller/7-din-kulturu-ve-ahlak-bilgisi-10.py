"""7. sınıf Din Kültürü ve Ahlak Bilgisi 10. hafta (Kurban İbadeti, Hz. İbrahim ve Hz. İsmail, Kurbanlık Şartları ve Adak/Akika Kurbanları) çalışma kâğıdı görselleri.
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


def yukumluluk_sartlari_panosu():
    kartlar = [
        (4, 4, '1. Şart · Ehliyet', 'Akıllı ve ergen olmak', MAVI, MAVI_A),
        (184, 4, '2. Şart · Zenginlik', '80,18 g altın (Nisap)', YES, YES_A),
        (4, 50, '3. Şart · Yolculuk (?)', 'Seferi (yolcu) olmak', KIR, KIR_A),
        (184, 50, '4. Şart · İhtiyaç Dışı', 'Borçtan arta kalan mal', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 42, z, r, 7)
        ic += yazi(x + 86, y + 16, bas, 10.0, r)
        ic += yazi(x + 86, y + 34, alt, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Kurban ibadetiyle yükümlü olma şartları panosu.', 15)


def kurbanlik_hayvan_kartlari():
    kartlar = [
        ('1. Küçükbaş', 'Koyun ve Keçi', '1 Yaş · 1 Kişi', MAVI, MAVI_A),
        ('2. Büyükbaş', 'Sığır ve Manda', '? Yaş · ? Kişi', YES, YES_A),
        ('3. Büyükbaş', 'Deve', '? Yaş · 1-7 Kişi', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, tur, sart, r, z) in enumerate(kartlar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 74, z, r)
        ic += yazi(x + 56, 22, bas, 10.0, r)
        ic += yazi(x + 56, 44, tur, 9.8, LAC)
        ic += yazi(x + 56, 65, sart, 9.4, r, ince=True)
    return svg(360, 86, ic, 'Kurbanlık hayvan türlerinin yaş ve hisse şartları.', 14)


def kurban_eti_paylasim_semasi():
    paylar = [
        (6, '1. Pay (1/3)', 'Kurban kesenin ailesi', MAVI, MAVI_A),
        (124, '2. Pay (1/3)', 'Komşu, akraba ve dostlar', YES, YES_A),
        (242, '3. Pay (1/3)', '? (Üçüncü grup)', KIR, KIR_A),
    ]
    ic = ''
    for x, bas, alt, r, z in paylar:
        ic += kutu(x, 6, 112, 72, z, r)
        ic += yazi(x + 56, 26, bas, 10.2, r)
        ic += yazi(x + 56, 54, alt, 9.4, LAC, ince=True)
    return svg(360, 84, ic, 'Kurban etinin üç eşit parçaya bölünmesi şeması.', 14)


def adak_akika_vaka_karti():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'Selim Bey’in Kurbanı', 10.0, TUR)
    ic += yazi(91, 43, '«Hastam iyileşirse keseceğim»', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 'Şart gerçekleşti (Vacip)', 9.5, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Merve Hanım’ın Kurbanı', 10.0, YES)
    ic += yazi(269, 43, '«Yeni doğan bebeğimize şükür»', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'Çocuk nimeti için (Sünnet)', 9.5, YES)
    return svg(360, 88, ic, 'Adak ve akika kurbanı vaka karşılaştırma kartları.', 15)


def saffat_ayet_levhasi():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 24, 'Hz. İbrahim ve Hz. İsmail Kıssası (Sâffât Suresi, 102)', 10.2, MAVI)
    ic += yazi(180, 48, '«Babacığım! Sana emrolunan şeyi yap; inşallah beni', 9.6, LAC, ince=True)
    ic += yazi(180, 66, 'sabredenlerden bulacaksın.» (Sadakat ve Teslimiyet)', 9.6, YES)
    return svg(360, 88, ic, 'Sâffât suresi 102. ayet teslimiyet ve sabır levhası.', 14)


def kurban_uygulama_seridi():
    adimlar = [
        ('1. Seçim', 'Sağlıklı Hayvan', MAVI, MAVI_A),
        ('2. Vakit', 'Bayram Namazı', YES, YES_A),
        ('3. Kesim', 'Kıble ve Tekbir', TUR, TUR_A),
        ('4. Paylaşım', 'Üçe Bölüşüm', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += yazi(x + 41, 52, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Kurban ibadetinin dört aşamalı uygulama şeridi.', 14)


def kurbanlik_secim_rehberi():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Kurban Olabilenler (Geçerli)', 10.0, YES)
    ic += yazi(91, 44, '• Sağlıklı, besili, azaları tam', 9.4, LAC, ince=True)
    ic += yazi(91, 64, '• Koyun/Keçi ≥1 yaş · Sığır ≥2 yaş', 9.3, YES)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, 'Kurban Olamayanlar (Geçersiz)', 10.0, KIR)
    ic += yazi(269, 44, '• Kör, topal, aşırı zayıf/hasta', 9.4, LAC, ince=True)
    ic += yazi(269, 64, '• Yaşını doldurmamış keçi/sığır', 9.3, KIR)
    return svg(360, 88, ic, 'Kurbanlık hayvanlarda aranan sağlık ve yaş şartları rehberi.', 15)


def toplumsal_dayanisma_karti():
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Bireysel Kazançlar', 10.2, MAVI)
    ic += yazi(91, 44, '• Allah’a yakınlaşma ve takva', 9.4, LAC, ince=True)
    ic += yazi(91, 64, '• Fedakârlık ve cömertlik', 9.4, MAVI)

    ic += kutu(184, 6, 170, 74, CAM_A, CAM)
    ic += yazi(269, 22, 'Toplumsal Kazançlar', 10.2, CAM)
    ic += yazi(269, 44, '• Sosyal yardımlaşma ve paylaşma', 9.4, LAC, ince=True)
    ic += yazi(269, 64, '• Kardeşlik ve sevgi bağları', 9.4, YES)
    return svg(360, 86, ic, 'Kurban ibadetinin bireysel ve toplumsal faydaları kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yukumluluk_sartlari_panosu()
    s[2]['gorsel'] = kurbanlik_hayvan_kartlari()
    s[5]['gorsel'] = kurban_eti_paylasim_semasi()
    s[6]['gorsel'] = adak_akika_vaka_karti()
    s[7]['gorsel'] = saffat_ayet_levhasi()
    s[8]['gorsel'] = kurban_uygulama_seridi()
    s[9]['gorsel'] = kurbanlik_secim_rehberi()
    s[11]['gorsel'] = toplumsal_dayanisma_karti()
