"""5. sınıf Türkçe 11. hafta (Gazi Mustafa Kemal ve Sığırtmaç Mustafa Bölüm 2, Metinler Arası Karşılaştırma, Kök ve Yapım Ekleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_turemis_kelime_karti():
    kartlar = [
        ('1. Kart', 'Bakıcı (bak-)', YES, YES_A),
        ('2. Kart', 'Tuzluk (tuz)', MAVI, MAVI_A),
        ('3. Kart', 'Vatandaş (vatan)', TUR, TUR_A),
        ('4. Kart', 'Çiftçi (çift)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, kel, 9.2, LAC)
    return svg(360, 84, ic, 'Kök türleri incelenen dört türemiş sözcük kartı.', 15)


def kok_ve_ek_tablo_kartlari():
    kartlar = [
        ('1. Sözcük', 'Kitaplık', MAVI, MAVI_A),
        ('2. Sözcük', 'Bilgi', YES, YES_A),
        ('3. Sözcük', 'Ağaçlar', TUR, TUR_A),
        ('4. Sözcük', 'Yazıcı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, kel, 10.2, LAC)
    return svg(360, 84, ic, 'Kök ve ek yapısı incelenen dört sözcük kartı.', 15)


def basit_turemis_cumle_kartlari():
    kartlar = [
        ('1. Kart', 'Altı çizili: doğruluk (doğru-luk)', MAVI, MAVI_A),
        ('2. Kart', 'Altı çizili: doktorlar (doktor-lar)', YES, YES_A),
        ('3. Kart', 'Altı çizili: ağaçlık (ağaç-lık)', TUR, TUR_A),
        ('4. Kart', 'Altı çizili: vatansever (vatan-sever)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, met, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Altı çizili sözcüklerin ek yapısını gösteren dört kart.', 15)


def iki_metin_karsilastirma_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'I. Metin · Sığırtmaç Mustafa', 10.0, MAVI)
    ic += yazi(91, 44, '• Olay, kişi, yer ve zaman var', 9.4, LAC, ince=True)
    ic += yazi(91, 64, '• Öyküleyici anlatım (Düz yazı)', 9.4, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'II. Metin · Mustafa Kemal Şiiri', 10.0, TUR)
    ic += yazi(269, 44, '• Dize, dörtlük ve kafiye var', 9.4, LAC, ince=True)
    ic += yazi(269, 64, '• Coşkulu ve duygusal anlatım', 9.4, TUR)
    return svg(360, 88, ic, 'Aynı temayı işleyen öyküleyici metin ve şiir karşılaştırması.', 15)


def cinar_agaci_soz_sanati_karti():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 22, 'Söz Sanatları İnceleme Kartı', 10.4, YESIL_K)
    ic += yazi(180, 45, '«Çiftliğin yaşlı çınar ağacı, küçük Mustafa’ya gülümseyerek:', 9.7, LAC)
    ic += yazi(180, 66, '— Yolun açık olsun cesur çocuk, dedi.»  (1. Sanat: ? · 2. Sanat: ?)', 9.6, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Çınar ağacının gülümsemesi ve konuşması söz sanatı kartı.', 15)


def sigirtmac_mustafa_bolum2_akisi():
    adimlar = [
        ('A · Hastane', 'Tedaviye alınması', MAVI, MAVI_A),
        ('B · Tokgözlülük', 'Harçlığı almaması', TUR, TUR_A),
        ('C · Eğitim', 'Okula başlaması', YES, YES_A),
        ('D · Subaylık', 'Harp Okulu mezunu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 55, met, 9.1, LAC, ince=True)
    return svg(360, 84, ic, 'Gazi Mustafa Kemal ve Sığırtmaç Mustafa 2. bölüm olay akışı.', 15)


def yazim_kurallari_denetim_panosu():
    cumleler = [
        ('I. Cümle', 'Gazi Mustafa Kemal Paşa (Unvan)', MAVI, MAVI_A),
        ('II. Cümle', '15 Eylül 1929 Pazar (Belirli tarih)', YES, YES_A),
        ('III. Cümle', 'Sığırtmaç Mustafa (Lakap/Unvan)', TUR, TUR_A),
        ('IV. Cümle', 'Zeynep Teyzem (Gerçek akrabalık!)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, met, r, z) in enumerate(cumleler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.1, r)
        ic += yazi(x + 86, y + 31, met, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Unvan, tarih ve akrabalık adlarının yazımı denetim panosu.', 15)


def kahramanlar_kisilik_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Gazi Mustafa Kemal Atatürk', 10.1, MAVI)
    ic += yazi(91, 44, '• Hastanede tedavi ettirmesi', 9.5, LAC, ince=True)
    ic += yazi(91, 64, '• Okula başlatıp desteklemesi', 9.5, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Küçük Sığırtmaç Mustafa', 10.1, YESIL_K)
    ic += yazi(269, 44, '• Emeği olmayan parayı almaması', 9.5, LAC, ince=True)
    ic += yazi(269, 64, '• Çok çalışıp subay olması', 9.5, LAC, ince=True)
    return svg(360, 88, ic, 'Atatürk ve Sığırtmaç Mustafa kişilik özellikleri kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_turemis_kelime_karti()
    s[2]['gorsel'] = kok_ve_ek_tablo_kartlari()
    s[5]['gorsel'] = basit_turemis_cumle_kartlari()
    s[6]['gorsel'] = iki_metin_karsilastirma_karti()
    s[7]['gorsel'] = cinar_agaci_soz_sanati_karti()
    s[8]['gorsel'] = sigirtmac_mustafa_bolum2_akisi()
    s[9]['gorsel'] = yazim_kurallari_denetim_panosu()
    s[11]['gorsel'] = kahramanlar_kisilik_karti()
