"""6. sınıf Türkçe 5. hafta (Türküz, Türkçe Konuşuruz: Materyal Seçimi, Anahtar Kelime, Söz Varlığı, Konuşma ve Yazma Görevi) çalışma kâğıdı görselleri.
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


def materyal_strateji_gorev_karti():
    kartlar = [
        ('1. Öğrenci: Duygu ve Ahenk', 'Materyal: Şiir · Strateji: Sesli okuma', YES, YES_A),
        ('2. Öğrenci: Bilgi Edinme', 'Materyal: Ansiklopedi · Strateji: Not alma', MAVI, MAVI_A),
        ('3. Öğrenci: Etkileşimsiz Video', 'Strateji: Kaydı durdurup anahtar not alma', TUR, TUR_A),
        ('Üst Bilişsel İzleme', 'İşe yaramayan stratejiyi fark edip değiştirme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okuma ve dinleme amaçlarına göre materyal ve strateji eşleştirme kartı.', 21)


def dil_adlari_yazim_kartlari():
    satirlar = [
        ('1. Kart', 'Karamanoğlu Mehmet Bey, “... Türkçeden başka dil kullanılmayacaktır.” dedi.', YES, YES_A),
        ('2. Kart', 'Derste “Türküz, Türkçe Konuşuruz” şiirini okuduk; Türkçe de çok zengindir.', MAVI, MAVI_A),
        ('3. Kart (!)', 'Türkçe’nin söz varlığını araştırırken Türk’çe sözlükten kelimeler seçtim.', KIR, KIR_A),
        ('4. Kart', 'Türk’ün tarih boyunca ürettiği eserlerde Türkçenin izlerini görürüz.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(102, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'Dil adlarına gelen eklerin ve tırnak işaretinin yazımını denetleyen dört kart.', 21)


def soz_varligi_unsurlari_panosu():
    kartlar = [
        ('1. Tatlı dil yılanı deliğinden çıkarır.', 'Özlü öğüt cümlesi', MAVI, MAVI_A),
        ('2. Ozanın türküsü dillere destan oldu.', 'Mecazlı kalıp söz', YES, YES_A),
        ('3. Gözleri sevinçten ışıl ışıl parladı.', 'Ahenkli kelime tekrarı', TUR, TUR_A),
        ('4. Şair ve ozan dilimizi ustaca işler.', 'Aynı anlamlı iki sözcük', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Atasözü, deyim, ikileme ve eş anlamlı sözcük örneklerini gösteren pano.', 21)


def kokten_turetme_agaci():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(6, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(149, 24, 'Örnek 1: “bil-” ve “sev-” Kökleri', '#fff', kalin=True)
    ic += yazi(149, 50, 'bil- → bilgi, bilim, bilgin, bilgisayar', LAC, kalin=True)
    ic += yazi(149, 74, 'sev- → sevgi, sevinç, sevimli, sevecen', YESIL_K, kalin=True)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, TUR, TUR, 9, 1)
    ic += yazi(451, 24, 'Sıra Sende: “göz” Kökü', '#fff', kalin=True)
    ic += yazi(451, 50, 'göz + (-lük, -cü, -lem, -etmek, -de)', LAC, kalin=True)
    ic += yazi(451, 74, 'En az 4 türemiş kelime yazınız!', TUR, kalin=True)
    return svg(600, 98, ic, 'Türkçede yapım ekleriyle tek kökten yeni kelimeler türetme şeması.', 21)


def konusma_planlama_zinciri():
    adimlar = [
        ('1. Amaç Seç', 'Bilgi / İkna / Duygu', MAVI, MAVI_A),
        ('2. Konu ve Tür', 'Dar konu · Uygun tür', YES, YES_A),
        ('3. Yöntem & Sunum', 'Not kartı · Ses ve vurgu', TUR, TUR_A),
        ('4. Öz Değerlendirme', 'Güçlü yön · Önlem al', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Hazırlıklı konuşmada amaç, konu, tür, sunum ve değerlendirme zinciri.', 21)


def kerem_ikna_konusma_karti():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'KEREM’İN KONUŞMA PLANI · SÜRE: 3 DAKİKA', '#fff', kalin=True)
    ic += yazi(300, 50, 'Amaç: İkna Etmek · Konu: Yabancı sözcükler yerine Türkçelerini kullanmak', LAC, kalin=True)
    ic += yazi(300, 74, 'Uygun Tür: Görüş bildiren konuşma · Yöntem: 2 gerekçe + örnek + 1 atasözü', CAM, kalin=True)
    return svg(600, 98, ic, 'İkna amaçlı 3 dakikalık konuşma için konu, tür ve yöntem kartı.', 21)


def tekrarli_paragraf_zenginlestirme():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(6, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(149, 24, 'Tekrarlı Taslak (Zayıf Anlatım)', '#fff', kalin=True)
    ic += yazi(149, 50, '“Türkçe önemli bir dildir. Kelimeleri', LAC, kalin=True)
    ic += yazi(149, 74, 'önemlidir. Şiirleri önemlidir.”', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(308, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(451, 24, 'Zenginleştirme Araçları', '#fff', kalin=True)
    ic += yazi(451, 50, '• Eş/Yakın anlam: dil-lisan, köklü', LAC, kalin=True)
    ic += yazi(451, 74, '• Deyim: dillere destan · İkileme: pırıl pırıl', MAVI, kalin=True)
    return svg(600, 98, ic, 'Aynı kelimenin tekrarlandığı taslağı söz varlığıyla zenginleştirme kartı.', 21)


def elif_yazma_plani_panosu():
    kartlar = [
        ('Hedef Kitle & Araç', 'Okul Dergisi · Düzenli ve özenli dil', MAVI, MAVI_A),
        ('Giriş Paragrafı', 'Konuyu tanıtan ve ilgi uyandıran giriş', YES, YES_A),
        ('Gelişme Paragrafı', 'Türetme gücünü örnekleyen açıklama', TUR, TUR_A),
        ('Metin Yapısı & Yazım', 'Açıklayıcı yapı · Doğru ek ve tırnak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okul dergisi için açıklayıcı metin yazma planı panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = materyal_strateji_gorev_karti()
    s[4]['gorsel'] = dil_adlari_yazim_kartlari()
    s[5]['gorsel'] = soz_varligi_unsurlari_panosu()
    s[6]['gorsel'] = kokten_turetme_agaci()
    s[7]['gorsel'] = konusma_planlama_zinciri()
    s[8]['gorsel'] = kerem_ikna_konusma_karti()
    s[10]['gorsel'] = tekrarli_paragraf_zenginlestirme()
    s[11]['gorsel'] = elif_yazma_plani_panosu()
