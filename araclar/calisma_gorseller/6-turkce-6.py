"""6. sınıf Türkçe 6. hafta (Türk Dil Kurumu Sunar - Kaşık: İzleme Stratejileri, Anlam Zenginliği ve İkileme-Pekiştirme Yazımı) çalışma kâğıdı görselleri.
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


def yuzey_anlam_yorum_karti():
    satirlar = [
        ('I. Not', 'Sunucu, “kaşık düşmanı” deyiminin şaka yollu “eş” demek olduğunu söyledi.', YES, YES_A),
        ('II. Not', 'Bence sunucu kaşıkla ilgili deyimleri pek sevmiyor olmalı.', TUR, TUR_A),
        ('III. Not', 'Videoda ekranda tahta bir kaşık ve eski bir sözlük sayfası gösterildi.', MAVI, MAVI_A),
        ('IV. Not', 'Bana göre kaşık dünyadaki en eski ve en önemli mutfak sözcüğüdür.', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 80, 22, renk, renk, 6, 1)
        ic += yazi(46, y + 15, no, '#fff', kalin=True)
        ic += yazi(96, y + 15, metin, LAC, 'start', kalin=(i in (0, 2)))
    return svg(600, 112, ic, 'Yüzey anlam bilgisi ve kişisel yorum içeren dört izleme notu kartı.', 21)


def ikileme_pekistirme_kartlari():
    satirlar = [
        ('1. Kart', 'Dedem köydeki işleri ağır ağır bitirip dinlendi.', YES, YES_A),
        ('2. Kart', 'Annem sofrayı tertemiz örtüyle hazırlayıp kaşıkları dizdi.', MAVI, MAVI_A),
        ('3. Kart (!)', 'Çorbayı kaşık, kaşık içtikten sonra sapa sağlam ayağa kalktı.', KIR, KIR_A),
        ('4. Kart', 'Eğri büğrü patikalardan geçerek güzel mi güzel yaylaya ulaştık.', CAM, CAM_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 86, 22, renk, renk, 6, 1)
        ic += yazi(49, y + 15, no, '#fff', kalin=True)
        ic += yazi(102, y + 15, metin, LAC, 'start', kalin=(i == 2))
    return svg(600, 112, ic, 'İkileme ve pekiştirmelerin yazımını denetleyen dört cümle kartı.', 21)


def soz_varligi_tablo_kartlari():
    kartlar = [
        ('1. kaşık kaşık yedirmek', 'Aynı sözcüğün tekrarı', MAVI, MAVI_A),
        ('2. sapasağlam durmak', 'İlk heceyle güçlendirme', YES, YES_A),
        ('3. eğri büğrü yollar', 'Ses benzerlikli tekrar', TUR, TUR_A),
        ('4. güzel mi güzel sofra', 'mı/mi edatıyla güçlendirme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'İkileme ve pekiştirme örneklerini gösteren dört söz varlığı kartı.', 21)


def efe_not_alma_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, 'Efe’nin İzleme Hatası (!)', KIR, kalin=True)
    ic += yazi(149, 50, 'Sunucunun her cümlesini yazmaya', LAC, kalin=True)
    ic += yazi(149, 74, 'çalıştı → Videonun yarısını kaçırdı!', KIR)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'Doğru Üst Bilişsel Strateji', YESIL_K, kalin=True)
    ic += yazi(451, 50, 'Yalnız anahtar kelimeleri not al,', LAC, kalin=True)
    ic += yazi(451, 74, 'gerekirse videoyu durdur ve geri sar.', LAC)
    return svg(600, 98, ic, 'Etkileşimsiz videoda yanlış ve doğru not alma stratejisi kartı.', 21)


def video_izleme_adimlari():
    kartlar = [
        ('1. İzleme Öncesi', 'Amaç ve başlıktan tahmin', MAVI, MAVI_A),
        ('2. İzleme Sırası', 'Anahtar kelime ve durdurma', YES, YES_A),
        ('3. İzleme Sonrası', 'Kavram haritası ve sözlük', TUR, TUR_A),
        ('4. Sözlü Paylaşım', '3 cümleyle anlatım ve soru', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Video izleme öncesi, sırası, sonrası ve sözlü etkileşim adımları.', 21)


def gorsel_ipuclari_panosu():
    kartlar = [
        ('Tahta Çorba Kaşığı', 'Gerçek anlam (Yemek aracı)', MAVI, MAVI_A),
        ('Tarihî El Yazması Sözlük', 'Sözcüğün köklü geçmişi', TUR, TUR_A),
        ('Kaşık Oyunu Ekibi', 'Halk oyununda ritim çalgısı', YES, YES_A),
        ('Aile Sofrası Görüntüsü', 'Deyimlerin günlük yaşam bağlamı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Videodaki görsel unsurların ilettiği anlamları gösteren dörtlü pano.', 21)


def oz_yansitma_karti():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'TEMA SONU ÖZ YANSITMA · ÜÇ CÜMLE KURALI', '#fff', kalin=True)
    ic += yazi(300, 50, '1) Güçlü yönüm ve gerekçesi · 2) Gelişmeye açık yönüm ve gerekçesi', LAC, kalin=True)
    ic += yazi(300, 74, '3) Gelişmeye açık yönüm için bir sonraki temada alacağım somut önlem', CAM, kalin=True)
    return svg(600, 98, ic, 'Güçlü yön, gelişmeye açık yön ve önlemden oluşan öz yansıtma kartı.', 21)


def cepheye_kosan_at_karti():
    ic = kutu(6, 6, 588, 86, TUR_A, TUR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, KIR, KIR, 9, 1)
    ic += yazi(300, 24, 'YENİ TEMA: BAĞIMSIZLIK YOLU · İLK METİN: CEPHEYE KOŞAN AT', '#fff', kalin=True)
    ic += yazi(300, 50, '• Başlık ve görselden Millî Mücadele yıllarına yönelik 2 tahmin yazılır.', LAC, kalin=True)
    ic += yazi(300, 74, '• Olay sırası kâğıdı ve sözlük hazırlanır; 29 Ekim ve tarih ön bilgileri hatırlanır.', LAC)
    return svg(600, 98, ic, 'Bağımsızlık Yolu teması ve Cepheye Koşan At metni ön hazırlık kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yuzey_anlam_yorum_karti()
    s[4]['gorsel'] = ikileme_pekistirme_kartlari()
    s[5]['gorsel'] = soz_varligi_tablo_kartlari()
    s[6]['gorsel'] = efe_not_alma_karti()
    s[7]['gorsel'] = video_izleme_adimlari()
    s[8]['gorsel'] = gorsel_ipuclari_panosu()
    s[10]['gorsel'] = oz_yansitma_karti()
    s[11]['gorsel'] = cepheye_kosan_at_karti()
