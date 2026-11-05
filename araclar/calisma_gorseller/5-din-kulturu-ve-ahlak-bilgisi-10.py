"""5. sınıf Din Kültürü ve Ahlak Bilgisi 10. hafta (Namazın Kılınışı: Beş Vakit Namazın Rekât Sayıları, Rükün Uygulamaları ve Cemaatle Namaz) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def bes_vakit_rekat_cizelgesi():
    kartlar = [
        ('Sabah (4)', '2 Sünnet + 2 Farz', MAVI, MAVI_A),
        ('Öğle (10)', '4 Sünnet + 4 Farz + 2', YES, YES_A),
        ('İkindi (8)', '[ K = ? ] + 4 Farz', TUR, TUR_A),
        ('Akşam (5)', '[ L = ? ] + 2 Sünnet', MOR, MOR_A),
    ]
    ic = ''
    for i, (vakit, det, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, vakit, 10.2, r)
        ic += yazi(x + 86, y + 31, det, 9.5, LAC, ince=True)
    return svg(360, 94, ic, 'Beş vakit namazın rekât sayıları çizelgesi.', 16)


def dort_namaz_hareketi_kartlari():
    kartlar = [
        ('1. Eğilme', 'Eller dizde düz bel', MAVI, MAVI_A),
        ('2. Doğrulma', 'Rükûdan kalkış', YES, YES_A),
        ('3. Kapanma', 'Alın ve eller yerde', TUR, TUR_A),
        ('4. Bitiriş', 'Sağa ve sola dönüş', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Namazdaki rükû, doğrulma, secde ve selam hareket kartları.', 15)


def son_oturus_dua_akisi():
    adimlar = [
        ('1. Dua (?)', '[ 1 ]', MAVI, MAVI_A),
        ('2. Salavatlar', 'Salli ve Barik', YES, YES_A),
        ('3. Dua (?)', '[ 2 ]', TUR, TUR_A),
        ('4. Kapanış', 'Sağa-Sola Selam', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += yazi(x + 41, 54, alt, 9.6, LAC)
    return svg(360, 84, ic, 'Ka’de-i âhire (son oturuş) dua sırası şeması.', 15)


def ezan_ve_kamet_ifadeleri():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, 'I. Özel Çağrı Cümlesi', 10.2, TUR)
    ic += yazi(91, 44, '«Essalâtü hayrun mine’n-nevm»', 9.4, LAC)
    ic += yazi(91, 65, '(Namaz uykudan hayırlıdır)', 9.3, TUR, ince=True)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'II. Özel Çağrı Cümlesi', 10.2, MAVI)
    ic += yazi(269, 44, '«Kad kâmeti’s-salâh»', 9.8, LAC)
    ic += yazi(269, 65, '(Namaz başladı / ayağa kalkın)', 9.3, MAVI, ince=True)
    return svg(360, 88, ic, 'Sabah ezanı ve kamet içinde yer alan özel ifadeler.', 15)


def cemaatle_namaz_panosu():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 22, 'Camide Cemaatle Namaz ve Saf Düzeni', 10.5, YESIL_K)
    ic += yazi(180, 44, '• İmam önde namazı kıldırır, cemaat arkada omuz omuza saf tutar.', 9.6, LAC, ince=True)
    ic += yazi(180, 65, '• Paylaşma, kardeşlik, birlik ve toplumsal dayanışma bilincini geliştirir.', 9.6, YESIL_K)
    return svg(360, 88, ic, 'Cemaatle namazın uygulanışı ve toplumsal faydaları kartı.', 15)


def iki_rekat_kilis_adimlari():
    adimlar = [
        ('A Adımı', 'Niyet + 1. Rekât Kıraat', MAVI, MAVI_A),
        ('B Adımı', '1. Rekât Rükû ve Secde', YES, YES_A),
        ('C Adımı', '2. Rekât + Son Oturuş', TUR, TUR_A),
        ('D Adımı', 'Dualar ve Selam', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 54, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'İki rekâtlık namazın baştan sona kılınış basamakları.', 15)


def cemaat_namazlari_bilgi_karti():
    kartlar = [
        ('Cuma Namazı', 'Farz · 2 rekât · Hutbeli', MAVI, MAVI_A),
        ('Bayram Namazı', 'Vacip · Yılda 2 kez · 2 rekât', YES, YES_A),
        ('Teravih Namazı', 'Sünnet · Ramazan’da 20 rekât', TUR, TUR_A),
        ('Cenaze Namazı', 'Rükûsuz ve secdesiz dua namazı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Cuma, bayram, teravih ve cenaze namazlarının özellikleri.', 16)


def birinci_ikinci_rekat_kiyam_farki():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Rekât Kıyamda Okunanlar', 10.1, MAVI)
    ic += yazi(91, 44, 'Sübhaneke + Eûzü-Besmele', 9.7, LAC)
    ic += yazi(91, 65, '+ Fâtiha + Zamm-ı Sûre', 9.7, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Rekât Kıyamda Okunanlar', 10.1, YESIL_K)
    ic += yazi(269, 44, 'Yalnızca Besmele çekilir', 9.7, LAC)
    ic += yazi(269, 65, '+ Fâtiha + Zamm-ı Sûre', 9.7, YESIL_K, ince=True)
    return svg(360, 88, ic, '1. rekât ve 2. rekât kıyam okumalarının karşılaştırılması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bes_vakit_rekat_cizelgesi()
    s[2]['gorsel'] = dort_namaz_hareketi_kartlari()
    s[5]['gorsel'] = son_oturus_dua_akisi()
    s[6]['gorsel'] = ezan_ve_kamet_ifadeleri()
    s[7]['gorsel'] = cemaatle_namaz_panosu()
    s[8]['gorsel'] = iki_rekat_kilis_adimlari()
    s[9]['gorsel'] = cemaat_namazlari_bilgi_karti()
    s[11]['gorsel'] = birinci_ikinci_rekat_kiyam_farki()
