"""8. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta (Zekât İbadeti, Nisap ve Zekât Oranları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans 10.5-11.5 pt (K150 EK); eğik kesir çizgisi yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#d97706', '#15803d', '#dc2626', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, KUM = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#fffdf5'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False, boy=10.8):
    ag = '500' if ince else '700'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-family="Noto Sans, sans-serif" font-size="{boy}" font-weight="{ag}" fill="{renk}">{metin}</text>'


def selim_bey_varlik_karti():
    """Soru 2 (s[1]): Selim Bey'in mal varlığı dökümü (Asli ihtiyaç vs Nisaba tabi)."""
    kartlar = [
        (4, 4, '1. İkamet Konutu', 'Ailesiyle oturduğu ev', MAVI, MAVI_A),
        (184, 4, '2. Yatırım Altını', '120 gram altın (1 yıllık)', TUR, TUR_A),
        (4, 52, '3. Binek Otomobil', 'İşe gittiği özel araç', YES, YES_A),
        (184, 52, '4. Ticari Ürünler', 'Mağaza satış malları', MOR, MOR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.6)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=10.2)
    return svg(360, 100, ic, 'Selim Bey mal varlığı kartları: konut, altın, otomobil ve ticari ürünler.', 15)


def hayvan_zekat_kartlari():
    """Soru 3 (s[2]): Hayvan türleri ve nisap-zekât oran kartları."""
    kartlar = [
        (4, 'Küçükbaş', '40–120: 1 koyun', '121–200: 2 koyun', MAVI, MAVI_A),
        (124, 'Büyükbaş', '30–39: 1 buzağı', '(2 yaşında)', YES, YES_A),
        (244, 'Deve', 'Her 5 deve için', '1 koyun veya keçi', TUR, TUR_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in kartlar:
        ic += kutu(x, 4, 112, 82, z, r, 8)
        ic += yazi(x + 56, 22, bas, r, boy=10.8)
        ic += yazi(x + 56, 46, s1, LAC, boy=10.0)
        ic += yazi(x + 56, 68, s2, LAC, ince=True, boy=9.8)
    return svg(360, 90, ic, 'Küçükbaş, büyükbaş ve develerde zekât ölçüleri şeması.', 15)


def toprak_urunleri_osur_panosu():
    """Soru 6 (s[5]): K ve L buğday tarlalarında sulama türü ve ürün miktarı."""
    ic = kutu(4, 4, 172, 86, YES_A, YES, 8)
    ic += yazi(90, 22, 'K Tarlası · 5.000 kg Buğday', YESIL_K)
    ic += yazi(90, 44, 'Yağmur Suyu (Masrafsız)', LAC, ince=True)
    ic += yazi(90, 64, 'Öşür Oranı: Onda bir (%10)', YESIL_K)
    ic += yazi(90, 82, 'Zekât Miktarı = ? kg', LAC)

    ic += kutu(184, 4, 172, 86, TUR_A, TUR, 8)
    ic += yazi(270, 22, 'L Tarlası · 5.000 kg Buğday', TUR)
    ic += yazi(270, 44, 'Motorlu Sulama (Masraflı)', LAC, ince=True)
    ic += yazi(270, 64, 'Öşür Oranı: Yirmide bir (%5)', TUR)
    ic += yazi(270, 82, 'Zekât Miktarı = ? kg', LAC)
    return svg(360, 94, ic, 'K ve L buğday tarlalarında sulama yöntemine göre öşür hesabı.', 15)


def dort_komsu_nisap_karti():
    """Soru 7 (s[6]): 4 komşunun birikimleri ve nisap karşılaştırması."""
    kartlar = [
        (4, 4, 'Ahmet Bey', '110 g altın (Nisap: 85 g)', YES, YES_A),
        (184, 4, 'Zeynep Hanım', '25 koyun (Nisap: 40 koyun)', KIR, KIR_A),
        (4, 52, 'Murat Bey', '96 g altın değerinde mal', MAVI, MAVI_A),
        (184, 52, 'Elif Hanım', '32 sığır (Nisap: 30 sığır)', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 172, 44, z, r, 7)
        ic += yazi(x + 86, y + 18, bas, r, boy=10.6)
        ic += yazi(x + 86, y + 36, alt, LAC, ince=True, boy=9.8)
    return svg(360, 100, ic, 'Dört komşunun mal varlığı ve nisap sınırları kartı.', 15)


def nakit_ticaret_hesap_karti():
    """Soru 8 (s[7]): 160.000 TL nakit + 40.000 TL ticaret malı zekât hesabı."""
    ic = kutu(4, 4, 352, 84, KUM, ALTIN, 8)
    ic += yazi(180, 21, 'Yıllık Zekât Hesaplama Kartı · Oran: Kırkta Bir (%2,5)', KAHVE)
    ic += kutu(12, 28, 162, 52, MAVI_A, MAVI, 6)
    ic += yazi(93, 46, 'Nakit Birikim (1 Yıllık)', MAVI)
    ic += yazi(93, 68, '160.000 TL', LAC)

    ic += kutu(186, 28, 162, 52, YES_A, YES, 6)
    ic += yazi(267, 46, 'Ticaret Malı (1 Yıllık)', YESIL_K)
    ic += yazi(267, 68, '40.000 TL', LAC)
    return svg(360, 92, ic, '160.000 TL nakit ve 40.000 TL ticaret malı zekât hesaplama kartı.', 15)


def zekat_surec_akis_sema():
    """Soru 9 (s[8]): 4 adımlı zekât yükümlülüğü ve ödeme akışı."""
    adimlar = [
        (4, '1. Adım', 'Borç ve asli', 'ihtiyacı düş', MAVI, MAVI_A),
        (93, '2. Adım', '85 g altın', 'nisabını ölç', TUR, TUR_A),
        (182, '3. Adım', '1 kamerî yıl', 'şartını ara', MOR, MOR_A),
        (271, '4. Adım', '%2,5 payı', 'fakire ver', YES, YES_A),
    ]
    ic = ''
    for x, bas, s1, s2, r, z in adimlar:
        ic += kutu(x, 4, 85, 80, z, r, 7)
        ic += yazi(x + 42, 22, bas, r, boy=10.4)
        ic += yazi(x + 42, 44, s1, LAC, ince=True, boy=9.8)
        ic += yazi(x + 42, 64, s2, LAC, boy=9.8)
    return svg(360, 88, ic, 'Zekât hesaplama ve ödeme sürecinin dört aşamalı şeması.', 14)


def ayet_karsilastirma_panosu():
    """Soru 10 (s[9]): Tevbe 103 ve En'âm 141 ayet mealleri panosu."""
    ic = kutu(4, 4, 352, 42, MAVI_A, MAVI, 7)
    ic += yazi(180, 20, 'Tevbe Suresi, 103. Ayet:', MAVI, boy=10.4)
    ic += yazi(180, 37, '«Onların mallarından, kendilerini temizleyip arındıracağın bir sadaka (zekât) al...»', LAC, ince=True, boy=9.4)

    ic += kutu(4, 50, 352, 42, YES_A, YES, 7)
    ic += yazi(180, 66, 'En’âm Suresi, 141. Ayet:', YESIL_K, boy=10.4)
    ic += yazi(180, 83, '«...Ürün verdiğinde ürününden yiyin, hasat günü de hakkını (öşürünü) verin...»', LAC, ince=True, boy=9.4)
    return svg(360, 96, ic, 'Tevbe 103 ve Enam 141 ayet mealleri panosu.', 15)


def sulama_hikmet_karti():
    """Soru 12 (s[11]): Yağmur suyu (%10) vs Masraflı sulama (%5) karşılaştırma kartı."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8)
    ic += yazi(90, 22, 'Doğal Sulama (Yağmur)', YESIL_K)
    ic += yazi(90, 45, 'Sulama gideri ve emek az', LAC, ince=True, boy=10.0)
    ic += yazi(90, 68, 'Oran: Onda bir (%10)', YESIL_K)

    ic += kutu(184, 4, 172, 82, MOR_A, MOR, 8)
    ic += yazi(270, 22, 'Masraflı Sulama (Motor)', MOR)
    ic += yazi(270, 45, 'Elektrik, yakıt ve emek var', LAC, ince=True, boy=10.0)
    ic += yazi(270, 68, 'Oran: Yirmide bir (%5)', MOR)
    return svg(360, 90, ic, 'Doğal sulama ve masraflı sulamada öşür oranlarının karşılaştırılması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = selim_bey_varlik_karti()
    s[2]['gorsel'] = hayvan_zekat_kartlari()
    s[5]['gorsel'] = toprak_urunleri_osur_panosu()
    s[6]['gorsel'] = dort_komsu_nisap_karti()
    s[7]['gorsel'] = nakit_ticaret_hesap_karti()
    s[8]['gorsel'] = zekat_surec_akis_sema()
    s[9]['gorsel'] = ayet_karsilastirma_panosu()
    s[11]['gorsel'] = sulama_hikmet_karti()
