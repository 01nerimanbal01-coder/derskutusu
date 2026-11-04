"""11. sınıf Fizik 1. hafta (Serbest Düşmede Hız Değişimi ve İvme) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def serbest_dusme_formulleri():
    kartlar = [
        ('1. Başlangıç', 'v0 = 0 (İlk hızsız)', MAVI, MAVI_A),
        ('2. Anlık Hız', 'v = g · t', YES, YES_A),
        ('3. Düşülen Yol', 'h = (1/2)·g·t²', TUR, TUR_A),
        ('4. İvme Sabiti', 'a = g ≈ 10 m/s²', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.2, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.6, LAC, ince=True)
    return svg(360, 125, ic, 'Serbest düşme formülleri kartı.', 34)


def havasiz_tup_deneyi():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'HAVASIZ ORTAMDA SERBEST DÜŞME DENEYİ', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, YES_A, YES)
    ic += yazi(92, 56, 'm Kütleli Bilye', 9.8, YESIL_K)
    ic += yazi(92, 76, 'İvme: a = g = 10 m/s²', 8.9, LAC, ince=True)
    ic += yazi(92, 92, 'Düşüş Süresi: t', 8.9, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, TUR_A, TUR)
    ic += yazi(267, 56, '10m Kütleli Gülle', 9.8, TUR)
    ic += yazi(267, 76, 'İvme: a = g = 10 m/s²', 8.9, LAC, ince=True)
    ic += yazi(267, 92, 'Düşüş Süresi: t (Aynı!)', 8.9, TUR, ince=True)
    return svg(360, 125, ic, 'Havasız tüpte iki farklı kütlenin düşüşü.', 34)


def saniye_adim_kesiti():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, '3 SANİYELİK SERBEST DÜŞMEDE HIZ VE YOL ADIMLARI', 10.2, YESIL_K)
    adimlar = [
        ('t = 1 s', 'v = 10 m/s · h = 5 m', 16),
        ('t = 2 s', 'v = 20 m/s · h = 20 m', 130),
        ('t = 3 s', 'v = 30 m/s · h = 45 m', 244),
    ]
    for zmn, dty, x in adimlar:
        ic += kutu(x, 36, 100, 70, '#ffffff', YESIL_K)
        ic += yazi(x + 50, 56, zmn, 9.6, YESIL_K)
        ic += f'<line x1="{x + 8}" y1="66" x2="{x + 92}" y2="66" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 50, 86, dty, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Saniyelerdeki hız ve konum adımları.', 34)


def ivme_vektor_semasi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'YER ÇEKİMİ İVMESİ VE SABİT DEĞERİ', 10.3, TUR)
    ic += kutu(20, 38, 145, 68, '#ffffff', TUR)
    ic += yazi(92, 58, 'Yer Çekimi İvmesi (g)', 9.6, TUR)
    ic += yazi(92, 78, 'g ≈ 10 m/s² (Sabit)', 8.9, LAC, ince=True)
    ic += yazi(92, 92, 'Yönü: Daima aşağı', 8.9, TUR, ince=True)

    ic += kutu(195, 38, 145, 68, MAVI_A, MAVI)
    ic += yazi(267, 58, 'Hız Değişimi (Δv)', 9.6, MAVI)
    ic += yazi(267, 78, 'Δv = g · Δt = 10 m/s', 8.9, LAC, ince=True)
    ic += yazi(267, 92, 'Her saniye 10 artar', 8.9, MAVI, ince=True)
    return svg(360, 125, ic, 'Yer çekimi ivmesi ve hız değişimi şeması.', 34)


def h_3h_5h_yol_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'EŞİT ZAMAN ARALIKLARINDA ALINAN DÜŞEY YOLLAR', 10.2, CAM)
    yollar = [
        ('1. sn (0-1s)', 'Alınan: 5 m (h)', 16),
        ('2. sn (1-2s)', 'Alınan: 15 m (3h)', 102),
        ('3. sn (2-3s)', 'Alınan: 25 m (5h)', 188),
        ('4. sn (3-4s)', 'Alınan: 35 m (7h)', 274),
    ]
    for b, d, x in yollar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.2, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.3, LAC, ince=True)
    return svg(360, 125, ic, 'h, 3h, 5h, 7h yolu oranları şeması.', 34)


def hiz_zaman_grafigi_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'SERBEST DÜŞME HIZ-ZAMAN (v-t) GRAFİK ÖZETİ', 10.2, MOR)
    ic += kutu(20, 36, 145, 70, '#ffffff', MOR)
    ic += yazi(92, 56, 'Eğim: İvme (a = g)', 9.6, MOR)
    ic += yazi(92, 76, 'Eğim = Δv / Δt = 10 m/s²', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Doğrusal artan hız', 8.8, MOR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Alan: Alınan Yol (h)', 9.6, YESIL_K)
    ic += yazi(267, 76, '0-4 s Alan = (4·40)/2 = 80 m', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Toplam düşüş yolu', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Hız zaman grafiği eğim ve alan analizi.', 34)


def fizik_eslestirme_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'SÜRE - HIZ - YOL EŞLEŞTİRME VERİLERİ', 10.1, YESIL_K)
    kartlar = [
        ('t = 2 s Hız', '20 m/s', 16),
        ('t = 2 s Yol', '20 metre', 102),
        ('h = 45 m Süre', '3 saniye', 188),
        ('1 s Hız Artışı', '10 m/s (g)', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 9.0, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.8, LAC, ince=True)
    return svg(360, 125, ic, 'Serbest düşme büyüklükleri kartı.', 34)


def konum_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['K', 'O', 'N', 'U', 'M']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 22, 74, h, 16.0, MAVI)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Konum kavramı şifre kutuları.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = serbest_dusme_formulleri()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = havasiz_tup_deneyi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = saniye_adim_kesiti()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = ivme_vektor_semasi()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = h_3h_5h_yol_kesiti()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = hiz_zaman_grafigi_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = fizik_eslestirme_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = konum_sifre_kutulari()
    s[10]['en_fazla'] = 34
