"""7. sınıf Türkçe 2. hafta (Martı Jonathan Livingston: Problem Çözme, İzlediğini Değerlendirme, E-postaya Cevap ve Sunum) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=12):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.8, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def icerik_degerlendirme_sema():
    olcutler = [
        ('1. Başlık Ölçütü', 'İçeriğe uygun mu?', 'Gerekçe ya da yeni başlık', MAVI, MAVI_A),
        ('2. Örnekler Ölçütü', 'Anlatımı destekliyor mu?', 'Gerekçe ya da ek örnekler', TUR, TUR_A),
        ('3. Akış Ölçütü', 'Sıralama ilgi çekici mi?', 'Gerekçe ya da yeni sıra', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(olcutler):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 74, z, r, 8, 1.5)
        ic += yazi(x + 96, 24, bas, 10.8, r)
        ic += yazi(x + 96, 46, s1, 10.1, LAC, ince=True)
        ic += yazi(x + 96, 65, s2, 10.0, r)
    return svg(600, 86, ic, 'İzlenen içeriği başlık, örnekler ve akış yönünden değerlendirme şeması.', 12)


def jonathan_problem_karti():
    ic = kutu(6, 6, 286, 76, MAVI_A, MAVI, 9, 1.5)
    ic += yazi(149, 24, 'Jonathan’ın Hedefi ve Çabası', 10.8, MAVI)
    ic += yazi(149, 46, '• Yalnızca yiyecek için değil, kusursuz', 10.1, LAC, ince=True)
    ic += yazi(149, 65, 'uçmayı öğrenmek için bütün gün çalışır.', 10.1, MAVI)

    ic += kutu(308, 6, 286, 76, TUR_A, TUR, 9, 1.5)
    ic += yazi(451, 24, 'Ailesinin Kaygısı ve Uyarıları', 10.8, TUR)
    ic += yazi(451, 46, '• Avlanmadığı için çok zayıflamıştır;', 10.1, LAC, ince=True)
    ic += yazi(451, 65, 'kış yaklaşırken beslenmesi gerekmektedir.', 10.1, TUR)
    return svg(600, 88, ic, 'Martı Jonathan ın öğrenme hedefi ile ailesinin beslenme kaygısı.', 12)


def eposta_yanit_rehberi():
    adimlar = [
        ('Konu ve Amaç', 'Sorunu doğru anla', MAVI, MAVI_A),
        ('Selam ve Hitap', 'Sevgili Deniz,', YES, YES_A),
        ('Gerekçeli Çözüm', 'Kanıt ve örnek ver', TUR, TUR_A),
        ('Kapanış ve Öz Denetim', 'Saygılarımla · Form', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.4, r)
        ic += yazi(x + 71, 50, alt, 10.0, LAC, ince=True)
    return svg(600, 78, ic, 'Bir e-postaya cevap yazarken izlenen dört temel kural.', 12)


def hayat_okul_ornekleri():
    ic = kutu(6, 6, 588, 78, KUM := '#fffdf5', GRI, 9, 1.4)
    ic += yazi(300, 23, '“Hayat Büyük Bir Okuldur” İçeriğindeki Öğrenme Örnekleri', 10.8, LAC)
    etiketler = [
        ('Okuma yazma', MAVI, MAVI_A, 12),
        ('Satranç', TUR, TUR_A, 110),
        ('Metal işleme', MOR, MOR_A, 192),
        ('Araba kullanma', YES, YES_A, 290),
        ('Resim yapma', KIR, KIR_A, 404),
        ('Halk oyunları', CAM, CAM_A, 498),
    ]
    for met, r, z, x in etiketler:
        w = 88 if len(met) < 12 else 106
        ic += kutu(x, 34, w, 30, z, r, 14, 1.3)
        ic += yazi(x + w / 2, 53, met, 9.8, r)
    ic += yazi(300, 77, 'Anahtar Kelime: Öğrenmek (Beşikten mezara her yaşta ve her ortamda sürer)', 10.0, SOLUK, ince=True)
    return svg(600, 90, ic, 'Hayat Büyük Bir Okuldur içeriğindeki altı farklı öğrenme örneği.', 12)


def sunum_hazirlik_adimlari():
    adimlar = [
        ('1. Görüşme Yap', '3 akran ve 3 yetişkin', MAVI, MAVI_A),
        ('2. Karşılaştır', 'Benzer ve farklı hedefler', YES, YES_A),
        ('3. Materyal Hazırla', 'Tablo, grafik, sunu', TUR, TUR_A),
        ('4. Planla ve Prova Et', 'Materyalle önceden dene', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 142, 66, z, r, 8, 1.4)
        ic += yazi(x + 71, 26, bas, 10.4, r)
        ic += yazi(x + 71, 50, alt, 9.9, LAC, ince=True)
    return svg(600, 78, ic, 'Sözlü sunuma hazırlık ve çoklu ortam materyali kullanma basamakları.', 12)


def eksik_degerlendirme_karti():
    ic = kutu(6, 6, 286, 70, KIR_A, KIR, 8, 1.5)
    ic += yazi(149, 24, 'Öğrencinin Yazdığı Not (Eksik)', 10.6, KIR)
    ic += yazi(149, 46, '“İçerikteki örnekler yeterli değil.”', 10.2, LAC)
    ic += yazi(149, 63, 'Gerekçe ve yeni örnek önerisi yok!', 9.9, KIR, ince=True)

    ic += kutu(308, 6, 286, 70, YES_A, YES, 8, 1.5)
    ic += yazi(451, 24, 'Doğru Değerlendirme Kuralı', 10.6, YES)
    ic += yazi(451, 46, 'Uygun değilse: Nedenini açıkla ve', 10.0, LAC, ince=True)
    ic += yazi(451, 63, 'eklenebilecek yeni örnekleri yaz.', 10.1, YES)
    return svg(600, 82, ic, 'İzlenen içeriği değerlendirirken öneri yazma kuralı kartı.', 12)


def eposta_bolumleri_sema():
    bolumler = [
        ('1. Bölüm · Hitap', 'Sevgili Deniz,', MAVI, MAVI_A),
        ('2. Bölüm · Yanıt', 'İletini okudum, teşekkürler.', YES, YES_A),
        ('3. Bölüm · Gerekçe', 'Yuvalar korunacak; çünkü...', TUR, TUR_A),
        ('4. Bölüm · Kapanış', 'Saygılarımla · Başkan', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(bolumler):
        x, y = 6 + (i % 2) * 298, 6 + (i // 2) * 44
        ic += kutu(x, y, 286, 38, z, r, 7, 1.4)
        ic += yazi(x + 12, y + 16, bas, 10.4, r, 'start')
        ic += yazi(x + 12, y + 31, alt, 10.0, LAC, 'start', ince=True)
    return svg(600, 96, ic, 'Cevap e-postasının dört yapısal bölümü.', 12)


def hedef_karsilastirma_notu():
    ic = kutu(6, 6, 286, 72, MAVI_A, MAVI, 8, 1.5)
    ic += yazi(149, 24, 'Gençlerin 5 Yıllık Hedefleri', 10.8, MAVI)
    ic += yazi(149, 45, '• Yabancı dil öğrenmek (Ortak)', 10.1, MAVI)
    ic += yazi(149, 63, '• Fen lisesini kazanmak · Yüzme öğrenmek', 10.0, LAC, ince=True)

    ic += kutu(308, 6, 286, 72, TUR_A, TUR, 8, 1.5)
    ic += yazi(451, 24, 'Yetişkinlerin 5 Yıllık Hedefleri', 10.8, TUR)
    ic += yazi(451, 45, '• Yabancı dil öğrenmek (Ortak)', 10.1, TUR)
    ic += yazi(451, 63, '• Meslek kursunu bitirmek · Bahçe kurmak', 10.0, LAC, ince=True)
    return svg(600, 84, ic, 'Üç akran ve üç yetişkinin beş yıllık hedef görüşme notları.', 12)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = icerik_degerlendirme_sema()
    s[1]['gorsel'] = jonathan_problem_karti()
    s[3]['gorsel'] = eposta_yanit_rehberi()
    s[5]['gorsel'] = hayat_okul_ornekleri()
    s[6]['gorsel'] = sunum_hazirlik_adimlari()
    s[7]['gorsel'] = eksik_degerlendirme_karti()
    s[8]['gorsel'] = eposta_bolumleri_sema()
    s[11]['gorsel'] = hedef_karsilastirma_notu()
