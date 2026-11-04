"""7. sınıf Sosyal Bilgiler 6. hafta (Millî Meseleler ve Küreselleşme) çalışma kâğıdı görselleri.
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


def milli_dayanisma_panosu():
    """Soru 1: Tarihten günümüze 3 millî dayanışma örneği panosu."""
    kartlar = [
        ('1921 · Millî Mücadele', 'Tekalif-i Milliye', 'Ordu-millet kenetlenmesi', KIR, KIR_A, 6),
        ('1974 · Kıbrıs Sonrası', 'ASELSAN ve Vakıflar', 'Halk bağışıyla savunma', MAVI, MAVI_A, 124),
        ('Günümüz · Afetler', 'Deprem Seferberliği', 'AFAD ve Kızılay birliği', YES, YES_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 23, bas, r)
        ic += yazi(x + 56, 48, s1, LAC)
        ic += yazi(x + 56, 70, s2, LAC, 'middle', True)
    return svg(360, 94, ic, 'Tarihten günümüze Türk toplumunun üç millî dayanışma örneği.', 14)


def kuresellesme_boyutlari_sema():
    """Soru 2: Küreselleşmenin bilim, ekonomi ve kültür boyutları şeması."""
    ic = kutu(4, 4, 352, 88, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Küreselleşmenin İnsan ve Toplum Hayatındaki Boyutları', KAHVE)
    kartlar = [
        ('Bilim & Sağlık', 'Hızlı bilgi paylaşımı', YES, YES_A, 10),
        ('Ekonomi & Ticaret', 'Uluslararası e-ticaret', MAVI, MAVI_A, 126),
        ('Kültür & Dil', 'Etkileşim / Yozlaşma riski', TUR, TUR_A, 242),
    ]
    for bas, alt, r, z, x in kartlar:
        ic += kutu(x, 28, 108, 54, z, r, 7, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 68, alt, LAC, 'middle', True)
    return svg(360, 96, ic, 'Küreselleşmenin bilim, ekonomi ve kültür boyutları şeması.', 14)


def milli_populer_kultur_karti():
    """Soru 4: Millî kültür ve popüler kültür karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 90, YES_A, YES, 8, 1.4)
    ic += yazi(90, 22, 'Millî Kültür', YESIL_K)
    ic += yazi(90, 44, 'Tarihsel süreçte oluşur', LAC, 'middle', True)
    ic += yazi(90, 63, 'Dil, gelenek, el sanatları', LAC, 'middle', True)
    ic += yazi(90, 81, 'Kalıcıdır · Kimliği korur', YESIL_K)

    ic += kutu(184, 4, 172, 90, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, 'Popüler Kültür', TUR)
    ic += yazi(270, 44, 'Kitle iletişimle yayılır', LAC, 'middle', True)
    ic += yazi(270, 63, 'Fast-food, moda, akımlar', LAC, 'middle', True)
    ic += yazi(270, 81, 'Geçicidir · Tüketime dayalı', TUR)
    return svg(360, 98, ic, 'Millî kültür ve popüler kültür özellikleri karşılaştırması.', 14)


def kibris_aselsan_karti():
    """Soru 5: 1974 Kıbrıs Barış Harekâtı ve savunma sanayii dayanışması."""
    ic = kutu(4, 4, 352, 88, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 21, '1974 Kıbrıs Barış Harekâtı ve Savunma Sanayii Hamlesi', MAVI)
    ic += kutu(12, 28, 160, 54, KIR_A, KIR, 6, 1.2)
    ic += yazi(92, 46, 'Karşılaşılan Sorun:', KIR)
    ic += yazi(92, 68, 'Silah ve telsiz ambargosu', LAC, 'middle', True)
    ic += kutu(188, 28, 160, 54, YES_A, YES, 6, 1.2)
    ic += yazi(268, 46, 'Milletin Çözümü:', YESIL_K)
    ic += yazi(268, 68, 'Bağışlarla ASELSAN kuruluşu', LAC, 'middle', True)
    return svg(360, 96, ic, '1974 ambargosuna karşı halk bağışlarıyla ASELSAN kuruluşu kartı.', 14)


def cinar_agaci_metaforu():
    """Soru 7: Kökleri yerde (millî kültür), dalları gökte (evrensel bilim) çınar modeli."""
    ic = kutu(4, 4, 352, 90, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, '«Kökleri Yerde, Dalları Gökte Çınar» Modeli', LAC)
    ic += kutu(12, 28, 162, 56, TUR_A, TUR, 7, 1.3)
    ic += yazi(93, 47, 'Güçlü Kökler (Öz Kimlik)', TUR)
    ic += yazi(93, 69, 'Türkçe · Tarih · Millî Değerler', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 56, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(267, 47, 'Göğe Uzanan Dallar (Evrensel)', MAVI)
    ic += yazi(267, 69, 'Bilim · Teknoloji · Üretim', LAC, 'middle', True)
    return svg(360, 98, ic, 'Kökleri millî kültürde, dalları evrensel bilimde çınar modeli.', 14)


def kuresel_koy_akis_sema():
    """Soru 8: Dünyanın küresel köye dönüşüm süreci 4 adımlı şeması."""
    adimlar = [
        ('1. Teknoloji', 'Ulaşım ve genel ağ', MAVI, MAVI_A, 6),
        ('2. Hızlanma', 'Mesafelerin kısalması', MOR, MOR_A, 94),
        ('3. Etkileşim', 'Ticaret ve bilgi akışı', TUR, TUR_A, 182),
        ('4. Sonuç', '«Küresel Köy» Dünya', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Dünyanın küresel köye dönüşüm aşamaları şeması.', 18)


def dort_etki_ornek_karti():
    """Soru 9: Küreselleşmenin 4 farklı etkisi kartı."""
    kartlar = [
        ('1. Kart · Zanaat', 'El sanatlarının azalması', KIR, KIR_A),
        ('2. Kart · Bilim', 'Deprem uyarı sistemi paylaşımı', YES, YES_A),
        ('3. Kart · Beslenme', 'Tek tip fast-food yayılımı', TUR, TUR_A),
        ('4. Kart · Çevre', 'Aşırı tüketim ve e-atık', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Küreselleşmenin olumlu ve olumsuz dört örnek kartı.', 14)


def tabela_dil_karsilastirma():
    """Soru 12: Yabancı tabela ve Türkçe tabela karşılaştırma kartı."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Çarşı ve Sokak Tabelalarında Dil Bilinci', KAHVE)
    ic += kutu(14, 28, 158, 52, KIR_A, KIR, 6, 1.2)
    ic += yazi(93, 46, '1. Tabela (Yabancı Özenti)', KIR)
    ic += yazi(93, 66, '«Star Coffee & Food Center»', LAC, 'middle', True)
    ic += kutu(188, 28, 158, 52, YES_A, YES, 6, 1.2)
    ic += yazi(267, 46, '2. Tabela (Öz Türkçe)', YESIL_K)
    ic += yazi(267, 66, '«Çınar Kıraathanesi ve Aşevi»', LAC, 'middle', True)
    return svg(360, 94, ic, 'Yabancı tabela ile Türkçe tabelanın kültürel karşılaştırması.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = milli_dayanisma_panosu()
    s[1]['gorsel'] = kuresellesme_boyutlari_sema()
    s[3]['gorsel'] = milli_populer_kultur_karti()
    s[4]['gorsel'] = kibris_aselsan_karti()
    s[6]['gorsel'] = cinar_agaci_metaforu()
    s[7]['gorsel'] = kuresel_koy_akis_sema()
    s[8]['gorsel'] = dort_etki_ornek_karti()
    s[11]['gorsel'] = tabela_dil_karsilastirma()
