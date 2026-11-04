"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 5. hafta (Birinci Dünya Savaşı Sebepleri, Bloklaşma ve Osmanlı Cepheleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def savas_sebepleri_semasi():
    """Soru 1: Birinci Dünya Savaşı genel ve özel sebepler şeması."""
    ic = kutu(4, 4, 172, 86, KIR_A, KIR, 8, 1.4)
    ic += yazi(90, 22, 'Genel Sebepler (Küresel)', KIR)
    ic += yazi(90, 44, '• Sömürgecilik (Sanayi İnk.)', LAC, 'middle', True)
    ic += yazi(90, 63, '• Milliyetçilik (Fransız İht.)', LAC, 'middle', True)
    ic += yazi(90, 81, '• Bloklaşma & Silahlanma', KIR)

    ic += kutu(184, 4, 172, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(270, 22, 'Özel Sebepler & Kıvılcım', MAVI)
    ic += yazi(270, 44, '• Alsas-Loren (Alm.-Fra.)', LAC, 'middle', True)
    ic += yazi(270, 63, '• Panslavizm (Rusya-Avust.)', LAC, 'middle', True)
    ic += yazi(270, 81, '• Saraybosna Suikastı (1914)', MAVI)
    return svg(360, 94, ic, 'Birinci Dünya Savaşı genel ve özel sebeplerini karşılaştıran şema.', 12)


def osmanli_cepheler_panosu():
    """Soru 2: Taarruz, Savunma ve Yardım cepheleri panosu."""
    gruplar = [
        ('Taarruz («K»)', 'Kafkas · Kanal', KIR, KIR_A, 6),
        ('Savunma', 'Çanakkale · Irak · Hicaz', MAVI, MAVI_A, 124),
        ('Yardım («-ya»)', 'Galiçya · Makedonya', YES, YES_A, 242),
    ]
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    for bas, alt, r, z, x in gruplar:
        ic += kutu(x, 10, 112, 72, z, r, 7, 1.3)
        ic += yazi(x + 56, 34, bas, r)
        ic += yazi(x + 56, 62, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Osmanlı Devleti’nin Taarruz, Savunma ve Yardım cepheleri panosu.', 12)


def almanya_osmanli_beklentileri():
    """Soru 4: Almanya'nın Osmanlı'yı savaşa çekme nedenleri."""
    alanlar = [
        ('Askerî Amaç', 'Yeni cephelerle yükü azaltmak', MAVI, MAVI_A),
        ('Jeopolitik Amaç', 'Boğazları Rusya’ya kapatmak', TUR, TUR_A),
        ('Dinî Amaç (Halife)', 'Sömürgelerde cihat ayaklanması', YES, YES_A),
        ('Ekonomik Amaç', 'Musul-Kerkük petrolü ve insan gücü', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(alanlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Almanya’nın Osmanlı Devleti’nden askerî, jeopolitik, dinî ve ekonomik beklentileri.', 12)


def canakkale_zaferi_sonuc_karti():
    """Soru 5: Çanakkale Zaferi'nin sonuçları kartı."""
    ic = kutu(4, 4, 352, 86, KIR_A, KIR, 8, 1.4)
    ic += yazi(180, 20, 'Çanakkale Zaferi (1915) · Tarihin Akışını Değiştiren Sonuçlar', KIR)
    ic += kutu(12, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(93, 46, 'Çarlık Rusya Etkisi', MAVI)
    ic += yazi(93, 66, 'Yardım gitmedi → 1917 İhtilali', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', YES, 6, 1.2)
    ic += yazi(267, 46, 'Savaşın Süresi & Bulgaristan', YESIL_K)
    ic += yazi(267, 66, 'Savaş 2 yıl uzadı · İttifak büyüdü', LAC, 'middle', True)
    return svg(360, 94, ic, 'Çanakkale Zaferi’nin Rusya ve savaş süresi üzerindeki etkileri kartı.', 12)


def mustafa_kemal_conkbayiri_ongorusu():
    """Soru 7: Mustafa Kemal'in Çanakkale'de çıkarma yerini önceden bilmesi."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'Çanakkale Cephesi · 19. Tümen Komutanı Yarbay Mustafa Kemal', MAVI)
    adimlar = [
        ('1. Öngörü (Tahmin)', 'Kabatepe-Arıburnu çıkarması', TUR, '#fff', 10),
        ('2. Kararlı Hamle', 'Conkbayırı ve Anafartalar', KIR, '#fff', 126),
        ('3. Kişilik Özelliği', 'İleri Görüşlülük & Deha', YES, '#fff', 242),
    ]
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'Mustafa Kemal’in Çanakkale’de düşmanın çıkarma yapacağı yeri önceden sezmesi.', 12)


def savasa_giris_kronoloji_semasi():
    """Soru 8: Osmanlı'nın 1914 savaşa giriş adımları."""
    adimlar = [
        ('1. Kıvılcım', 'Saraybosna (Haziran)', MAVI, MAVI_A, 6),
        ('2. Tedbir', 'Tarafsızlık & Boğazlar', TUR, TUR_A, 94),
        ('3. Gemiler', 'Goben → Yavuz/Midilli', MOR, MOR_A, 182),
        ('4. Baskın', 'Rus limanları (Ekim)', KIR, KIR_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Osmanlı Devleti’nin 1914 yılında savaşa giriş sürecinin dört basamağı.', 12)


def cephe_kodlama_anahtari():
    """Soru 9: Cephe kodlama anahtarı kartı."""
    ic = kutu(4, 4, 352, 86, YES_A, YES, 8, 1.4)
    ic += yazi(180, 20, 'Osmanlı Cepheleri Hafıza Kodlama Kartı', YESIL_K)
    ic += kutu(12, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(93, 46, '«K» Kuralı (Taarruz)', KIR)
    ic += yazi(93, 66, 'Kafkas ve Kanal (2 Cephe)', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', MAVI, 6, 1.2)
    ic += yazi(267, 46, '«-ya» Kuralı (Yardım)', MAVI)
    ic += yazi(267, 66, 'Galiçya, Makedonya, Romanya', LAC, 'middle', True)
    return svg(360, 94, ic, 'Taarruz cephelerini K harfi, yardım cephelerini -ya ekiyle kodlayan kart.', 12)


def islamcilik_fikir_akimi_analizi():
    """Soru 12: Hicaz-Yemen cephesinde İslamcılık (Ümmetçilik) analizi."""
    ic = kutu(4, 4, 352, 86, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 20, 'Hicaz-Yemen ve Kanal Cepheleri · Fikir Akımı Analizi', MOR)
    ic += kutu(12, 28, 162, 52, '#fff', TUR, 6, 1.2)
    ic += yazi(93, 46, 'Beklenti (Cihat Çağrısı)', TUR)
    ic += yazi(93, 66, 'Tüm Müslümanların birleşmesi', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, '#fff', KIR, 6, 1.2)
    ic += yazi(267, 46, 'Yaşanan Sonuç', KIR)
    ic += yazi(267, 66, 'İslamcılık (Ümmetçilik) zayıfladı', LAC, 'middle', True)
    return svg(360, 94, ic, 'Hicaz-Yemen cephesindeki gelişmelerin İslamcılık fikir akımına etkisini gösteren kart.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = savas_sebepleri_semasi()
    s[1]['gorsel'] = osmanli_cepheler_panosu()
    s[3]['gorsel'] = almanya_osmanli_beklentileri()
    s[4]['gorsel'] = canakkale_zaferi_sonuc_karti()
    s[6]['gorsel'] = mustafa_kemal_conkbayiri_ongorusu()
    s[7]['gorsel'] = savasa_giris_kronoloji_semasi()
    s[8]['gorsel'] = cephe_kodlama_anahtari()
    s[11]['gorsel'] = islamcilik_fikir_akimi_analizi()
