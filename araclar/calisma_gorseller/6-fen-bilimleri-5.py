"""6. sınıf Fen Bilimleri 5. hafta (Bileşke Kuvvet: Dengelenmiş ve Dengelenmemiş Kuvvetler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def k_kutusu_uc_kuvvet():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += yazi(80, 24, '← Batı', LAC, kalin=True)
    ic += yazi(520, 24, 'Doğu →', LAC, kalin=True)
    ic += f'<line x1="40" y1="78" x2="560" y2="78" stroke="{GRI}" stroke-width="2"/>'
    ic += kutu(240, 30, 120, 48, MAVI_A, MAVI, 8, 1.6)
    ic += yazi(300, 58, 'K Kutusu', MAVI, kalin=True)
    ic += f'<line x1="240" y1="54" x2="110" y2="54" stroke="{KIR}" stroke-width="2.5"/>'
    ic += f'<polygon points="110,54 122,48 122,60" fill="{KIR}"/>'
    ic += yazi(165, 44, 'F3 = 12 N', KIR, kalin=True)
    ic += f'<line x1="360" y1="42" x2="490" y2="42" stroke="{YES}" stroke-width="2.5"/>'
    ic += f'<polygon points="490,42 478,36 478,48" fill="{YES}"/>'
    ic += yazi(430, 32, 'F1 = 10 N', YESIL_K, kalin=True)
    ic += f'<line x1="360" y1="64" x2="470" y2="64" stroke="{TUR}" stroke-width="2.5"/>'
    ic += f'<polygon points="470,64 458,58 458,70" fill="{TUR}"/>'
    ic += yazi(425, 58, 'F2 = 8 N', TUR, kalin=True)
    return svg(600, 100, ic, 'K kutusuna doğuya 10 N ve 8 N, batıya 12 N etki eden kuvvet diyagramı.', 21)


def dort_cisim_kuvvet_panosu():
    kartlar = [
        ('1. Cisim', '← 8 N ve ← 8 N (R = 16 N Batı)', MAVI, MAVI_A),
        ('2. Cisim (Dengede)', '← 12 N ve 12 N → (R = 0 N)', YES, YES_A),
        ('3. Cisim', '↑ 15 N ve ↓ 9 N (R = 6 N Kuzey)', TUR, TUR_A),
        ('4. Cisim', '10 N →, 4 N → ve ← 6 N (R = 8 N)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört cisme etki eden kuvvet çiftlerini karşılaştıran pano.', 21)


def dinamometre_deney_tablo_karti():
    kartlar = [
        ('1. Deneme', 'Batı: 4 N ↔ Doğu: 4 N', YES, YES_A),
        ('2. Deneme', 'Batı: 3 N ↔ Doğu: 8 N', MAVI, MAVI_A),
        ('3. Deneme', 'Batı: 9 N ↔ Doğu: 9 N', TUR, TUR_A),
        ('4. Deneme', 'Batı: 10 N ↔ Doğu: 4 N', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört denemede dinamometrelerin gösterdiği zıt yönlü kuvvet değerleri.', 21)


def l_kutusu_dengeleme_sema():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'L KUTUSU DENGELEME PROBLEMI · R = 0 N OLSUN', '#fff', kalin=True)
    ic += yazi(300, 50, 'Batı Yönü: 11 N + [ ? ] ← [ L Kutusu ] → Doğu Yönü: 14 N + 6 N = 20 N', LAC, kalin=True)
    ic += yazi(300, 74, 'Hedef: Doğu ve batı yönündeki toplam kuvvet büyüklüklerini eşitlemek', CAM, kalin=True)
    return svg(600, 98, ic, 'Doğuya 14 N ve 6 N, batıya 11 N çekilen L kutusunu dengeleme şeması.', 21)


def dort_araba_bileske_kartlari():
    arabalar = [
        ('P Arabası', '← 6 N | 6 N →', YES, YES_A),
        ('R Arabası', '← 5 N | 8 N →', MAVI, MAVI_A),
        ('S Arabası', '4 N → | 3 N →', TUR, TUR_A),
        ('T Arabası', '← 15 N | 3 N →', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(arabalar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'P, R, S ve T deney arabalarına etki eden kuvvet kartları.', 21)


def makarali_agirlik_duzenegi():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    ic += kutu(18, 18, 165, 64, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(100, 40, 'Sol Kefe (Batı)', MAVI, kalin=True)
    ic += yazi(100, 64, '2 Özdeş Kütle = 10 N', LAC, kalin=True)

    ic += kutu(200, 24, 200, 52, YES_A, YES, 8, 1.5)
    ic += yazi(300, 46, 'Deney Arabası', YESIL_K, kalin=True)
    ic += yazi(300, 66, '← 10 N | 15 N →', LAC, kalin=True)

    ic += kutu(417, 18, 165, 64, TUR_A, TUR, 8, 1.4)
    ic += yazi(500, 40, 'Sağ Kefe (Doğu)', TUR, kalin=True)
    ic += yazi(500, 64, '3 Özdeş Kütle = 15 N', LAC, kalin=True)
    return svg(600, 100, ic, 'Sol kefede 2 kütle (10 N), sağ kefede 3 kütle (15 N) asılı makaralı araba düzeneği.', 21)


def fark_onemli_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(6, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(149, 24, '1. Deneme · Küçük Kuvvetler', '#fff', kalin=True)
    ic += yazi(149, 50, 'Batıya 2 N ↔ Doğuya 2 N', LAC, kalin=True)
    ic += yazi(149, 74, 'R = 2 N − 2 N = 0 N (Durur)', MAVI, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(308, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(451, 24, '2. Deneme · 4 Kat Büyük Kuvvet', '#fff', kalin=True)
    ic += yazi(451, 50, 'Batıya 8 N ↔ Doğuya 8 N', LAC, kalin=True)
    ic += yazi(451, 74, 'R = 8 N − 8 N = 0 N (Yine Durur)', YESIL_K, kalin=True)
    return svg(600, 98, ic, '2 N - 2 N ve 8 N - 8 N uygulanan iki denemede de bileşkenin 0 N olduğunu gösteren kart.', 21)


def deney_degiskenleri_panosu():
    kartlar = [
        ('Bağımsız Değişken', 'Kuvvetler arasındaki fark (R)', MAVI, MAVI_A),
        ('Bağımlı Değişken', '2 saniyede alınan yol (cm)', YES, YES_A),
        ('Kontrol Edilen 1', 'Oyuncak araba ve yatay zemin', TUR, TUR_A),
        ('Kontrol Edilen 2', 'İplerin zemine paralel doğrultusu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Kuvvet deneyindeki bağımsız, bağımlı ve kontrol edilen değişkenler panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = k_kutusu_uc_kuvvet()
    s[4]['gorsel'] = dort_cisim_kuvvet_panosu()
    s[5]['gorsel'] = dinamometre_deney_tablo_karti()
    s[6]['gorsel'] = l_kutusu_dengeleme_sema()
    s[7]['gorsel'] = dort_araba_bileske_kartlari()
    s[8]['gorsel'] = makarali_agirlik_duzenegi()
    s[10]['gorsel'] = fark_onemli_karti()
    s[11]['gorsel'] = deney_degiskenleri_panosu()
