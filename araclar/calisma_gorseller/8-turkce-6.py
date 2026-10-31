"""8. sınıf Türkçe 6. hafta (215 Okkalık Mermi Nasıl Kaldırıldı?: Yazı karakterleri, 5N1K, medya karşılaştırması ve özne) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 9.5–11 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def bes_n_bir_k_semasi():
    """Metindeki olayın 5N1K unsurları şeması."""
    kartlar = [
        ('Kim?', 'Topçu Neferi', 'Seyit', MAVI, MAVI_A, 4),
        ('Nerede?', 'Mecidiye', 'Tabyası’nda', TUR, TUR_A, 92),
        ('Ne zaman?', '18 Mart Deniz', 'Savaşı’nda', YES, YES_A, 180),
        ('Niçin?', 'Topun vinci', 'kırıldığı için', MOR, MOR_A, 268),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 43
        ic += kutu(x, 4, 86, 74, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 10, r)
        ic += f'<line x1="{x + 10}" y1="27" x2="{x + 76}" y2="27" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 44, s1, 9.4, LAC, 'middle', True)
        ic += yazi(cx, 60, s2, 9.4, LAC, 'middle', True)
    return svg(358, 82, ic, 'Metinden dört 5N1K unsuru: Kim, Nerede, Ne zaman ve Niçin.', 22)


def yazi_karakteri_bolumleri():
    """Metnin üç bölümünde dik ve eğik yazı karakteri kullanımı."""
    ic = kutu(4, 4, 352, 84, KUM, GRI, 8, 1.2)
    bolumler = [
        ('1. Bölüm (Dik):', 'Giriş — Yazar savaşın bütünlüğünü açıklar.', MAVI, MAVI_A, 9),
        ('2. Bölüm (Eğik):', 'Olay — Kırık vinç ve 215 okkalık mermi anlatılır.', TUR, TUR_A, 33),
        ('3. Bölüm (Dik):', 'Kapanış — Yazar ordunun fedakârlığını değerlendirir.', MAVI, MAVI_A, 57),
    ]
    for bas, acik, r, z, y in bolumler:
        ic += kutu(10, y, 340, 21, z, r, 5, 1.2)
        ic += yazi(18, y + 14, bas, 9.5, r, 'start')
        ic += yazi(112, y + 14, acik, 9.2, LAC, 'start', True)
    return svg(360, 92, ic, 'Metnin üç bölümünde dik ve eğik yazı karakteri kullanımı şeması.', 22)


def medya_ve_ozne_panosu():
    """Medya karşılaştırma ölçütleri ve özne bulma kuralları panosu."""
    ic = kutu(4, 4, 172, 80, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, 'Metin ve Film Karşılaştırma', 9.6, YES)
    ic += yazi(90, 38, 'Ölçüt: Olay, kişi, yer, zaman', 9.2, LAC, 'middle', True)
    ic += yazi(90, 54, '“kısaltılmıştır” → Bir bölüm', 9.2, LAC, 'middle', True)
    ic += yazi(90, 70, 'İhsan: O ana verilmiş lütuf', 9.2, YES, 'middle')

    ic += kutu(184, 4, 172, 80, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(270, 20, 'Cümlede Özneyi Bulma', 9.6, MAVI)
    ic += yazi(270, 38, 'Önce yüklem, sonra özne', 9.2, LAC, 'middle', True)
    ic += yazi(270, 54, 'İlk sözcük hep özne olmaz', 9.2, LAC, 'middle', True)
    ic += yazi(270, 70, 'İsim cümlesinde de özne var', 9.2, MAVI, 'middle')
    return svg(360, 88, ic, 'Metin-animasyon film karşılaştırma ölçütleri ve cümlede özneyi bulma kuralları.', 22)


def ozne_cumle_fisleri():
    """Dört cümle fişinde tırnak içi bölümlerin özne denetimi."""
    fisler = [
        ('1. fiş · Kim savundu?', '“Mecidiye’deki topçular”', MAVI, MAVI_A),
        ('2. fiş · Ne zaman?', '“Sabahın erken saatlerinde”', KIR, KIR_A),
        ('3. fiş · Ne yaşayacaktır?', '“Çanakkale’deki bu destan”', YES, YES_A),
        ('4. fiş · Ne içeriyor?', '“Kütüphanedeki tarih atlası”', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 9.5, r, 'middle')
        ic += yazi(x + 86, y + 30, cum, 9.2, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört cümle fişi: 1, 3 ve 4 özne; 2. fişteki Sabahın erken saatlerinde zaman bildiren söz.', 22)


def metin_film_karsilastirma_karti():
    """Yazılı metin ile animasyon film karşılaştırma tablosu kartı."""
    ic = kutu(4, 4, 352, 84, '#fff', GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{LAC}"/><rect x="4" y="14" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 18, 'Yazılı Metin ve Animasyon Film Karşılaştırma Özeti', 10, '#fff')
    satirlar = [
        ('Olay:', '215 okkalık merminin namluya sürülmesi (Aynı)', YES),
        ('Kahramanlar:', 'Topçu Neferi Seyit ve Niğdeli Ali (Aynı)', YES),
        ('Mekân-Zaman:', 'Metinde yazılı betimleme, filmde görsel sahne (Farklı)', TUR),
    ]
    for i, (b, ac, r) in enumerate(satirlar):
        y = 32 + i * 18
        ic += yazi(14, y + 10, b, 9.5, r, 'start')
        ic += yazi(100, y + 10, ac, 9.2, LAC, 'start', True)
    return svg(360, 92, ic, 'Yazılı metin ve animasyon film karşılaştırma tablosu: olay ve kahramanlar aynı, mekân ve zaman sunumu farklı.', 22)


def soru_cevap_uyum_kartlari():
    """Dört 5N1K soru-cevap uyum kartı (III. kartta Ne zaman sorusuna yer cevabı)."""
    kartlar = [
        ('I. Kart · Kim?', 'Kim kutladı? → Cevat Paşa', MAVI, MAVI_A),
        ('II. Kart · Nasıl?', 'Nasıl taşıdı? → Omzuna alarak', YES, YES_A),
        ('III. Kart · Ne zaman?', 'Ne zaman? → Mecidiye Tabyası’na', KIR, KIR_A),
        ('IV. Kart · Niçin?', 'Niçin? → Vinci kırık olduğu için', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 9.5, r, 'middle')
        ic += yazi(x + 86, y + 30, cum, 9.0, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört 5N1K soru-cevap kartı: III. kartta Ne zaman sorusuna yer cevabı verilmiş.', 22)


def sonuc_paragrafi_karti():
    """Giriş bölümü aranacak sonuç paragrafı kartı."""
    ic = kutu(4, 4, 352, 78, CAM_A, CAM, 8, 1.4)
    ic += yazi(180, 19, 'Metnin Sonuç Paragrafı (Giriş Bununla Uyumlu Olmalı)', 9.8, CAM)
    ic += yazi(180, 39, '“Kısacası, Çanakkale Şehitliği ve tabyalar gibi tarihî', 9.4, LAC, 'middle', True)
    ic += yazi(180, 55, 'mekânları yerinde ziyaret etmek, öğrencilerde tarih', 9.4, LAC, 'middle', True)
    ic += yazi(180, 71, 'bilincini yalnız okumaktan çok daha güçlü pekiştirir.”', 9.4, CAM, 'middle')
    return svg(360, 86, ic, 'Tarihî mekânları yerinde ziyaret etmenin önemini vurgulayan sonuç paragrafı kartı.', 22)


def cumle_cozumleme_karti():
    """Fiil ve isim cümlesinde özne çözümleme kartı."""
    ic = kutu(4, 4, 352, 80, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 19, 'Özne Çözümleme Kartı (Önce Yüklemi, Sonra Özneyi Bul)', 9.8, TUR)
    ic += kutu(12, 27, 336, 21, '#fff', MAVI, 5, 1.2)
    ic += yazi(180, 41, '1. Cümle: Boğaz’ı savunan kahraman topçular / mevzileri onardı.', 9.3, LAC, 'middle')
    ic += kutu(12, 53, 336, 21, '#fff', YES, 5, 1.2)
    ic += yazi(180, 67, '2. Cümle: Bu tabya / Çanakkale savunmasının kilit noktasıdır.', 9.3, LAC, 'middle')
    return svg(360, 88, ic, 'İki cümlede özne ve yüklem çözümleme kartı.', 22)


def ozne_kurma_karti():
    """Açık uçlu soru için söz öbeği özneli fiil cümlesi ve isim cümlesi kurma kartı."""
    ic = kutu(4, 4, 352, 72, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 19, 'Cümle Kurma ve Özne Gösterme Rehberi', 10, MOR)
    ic += yazi(180, 38, '1) Öznesi söz öbeği olan bir fiil cümlesi yazınız.', 9.4, LAC, 'middle', True)
    ic += yazi(180, 53, '2) Yüklemi fiil olmayan bir isim cümlesi yazıp öznesini belirtiniz.', 9.4, LAC, 'middle', True)
    ic += yazi(180, 68, 'İpucu: Yükleme “Kim?” veya “Ne?” sorusunu sorarak doğrulayınız.', 9.2, MOR, 'middle')
    return svg(360, 80, ic, 'Söz öbeği özneli fiil cümlesi ve isim cümlesi kurma ipucu kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = bes_n_bir_k_semasi()
    s[1]['gorsel'] = yazi_karakteri_bolumleri()
    s[3]['gorsel'] = medya_ve_ozne_panosu()
    s[5]['gorsel'] = ozne_cumle_fisleri()
    s[7]['gorsel'] = metin_film_karsilastirma_karti()
    s[8]['gorsel'] = soru_cevap_uyum_kartlari()
    s[9]['gorsel'] = sonuc_paragrafi_karti()
    s[10]['gorsel'] = cumle_cozumleme_karti()
    s[13]['gorsel'] = ozne_kurma_karti()
