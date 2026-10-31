"""8. sınıf Türkçe 4. hafta (Atatürk Bizimle Dinleme Metni: Not Alma, Özet, Başlık ve Fiilimsiler) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def dinleme_surec_semasi():
    """Dinleme öncesi, sırası ve sonrası üç aşamalı şema."""
    asamalar = [
        ('1. Dinleme Öncesi', ['Kitap araştırmasını', 'arkadaşlarıyla', 'paylaşma'], MAVI, MAVI_A, 4),
        ('2. Dinlerken', ['Dikkat dağıtıcı', 'hareket etmeden', 'sözcük not alma'], TUR, TUR_A, 122),
        ('3. Dinleme Sonrası', ['Sözlük, özet, başlık', 've gerekçeli görüş', 'paylaşma'], YES, YES_A, 240),
    ]
    ic = ''
    for bas, sat, r, z, x in asamalar:
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        ic += yazi(x + 58, 19, bas, 10.5, r)
        for k, s_met in enumerate(sat):
            ic += yazi(x + 58, 37 + k * 16, s_met, 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Dinleme sürecinin üç aşaması: Dinlemeden önce, Dinlerken, Dinledikten sonra.', 14)


def sozluk_calisma_karti():
    """Tuna'nın iki sözcük için hazırladığı sözlük ve cümle kartı."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 19, 'Tuna’nın Not Aldığı Sözcükler ve Cümle Tablosu', 11, '#fff')
    # 1. satır
    ic += kutu(10, 30, 340, 28, YES_A, YES, 6, 1.2)
    ic += yazi(18, 42, '1) मुस्तakil → müstakil (TDK: Bağımsız, kendi başına olan)', 10.5, YES, 'start').replace('मुस्तakil → ', '')
    ic += yazi(18, 54, 'Cümle: “Dedem bahçeli, müstakil bir evde yaşıyor.”', 10.5, LAC, 'start', True)
    # 2. satır
    ic += kutu(10, 62, 340, 28, KIR_A, KIR, 6, 1.2)
    ic += yazi(18, 74, '2) imrenmek (Tahminim: Kıskanıp üzülmek demektir)', 10.5, KIR, 'start')
    ic += yazi(18, 86, 'Cümle: “Arkadaşımın başarısına çok imrendim ve ona kızdım.”', 10.5, LAC, 'start', True)
    return svg(360, 100, ic, 'Tuna nın sözlük tablosu: 1. sözcük müstakil TDK anlamı ve doğru cümle; 2. sözcük imrenmek tahminle yanlış anlam ve cümle.', 14)


def kok_gorev_semasi():
    """oku- fiil kökünden üç fiilimsi türü şeması."""
    ic = kutu(130, 4, 100, 24, LAC, LAC, 12, 1.2) + yazi(180, 20, 'Fiil kökü: oku-', 11, '#fff')
    kartlar = [
        ('İsim-fiil', 'İşin adını bildirir', 'okumak', TUR, TUR_A, 4),
        ('Sıfat-fiil', 'İsmi niteler', 'okunan', MAVI, MAVI_A, 122),
        ('Zarf-fiil', 'Zaman ve durum', 'okuyarak', YES, YES_A, 240),
    ]
    for bas, g, ornek, r, z, x in kartlar:
        ic += kutu(x, 34, 116, 54, z, r, 7, 1.3)
        ic += yazi(x + 58, 50, bas, 11, r)
        ic += yazi(x + 58, 65, g, 10.5, LAC, 'middle', True)
        ic += yazi(x + 58, 81, f'Örnek: {ornek}', 10.5, r)
    return svg(360, 92, ic, 'oku- kökünden isim-fiil okumak, sıfat-fiil okunan ve zarf-fiil okuyarak şeması.', 14)


def ozet_kontrol_kartlari():
    """Dört öğrencinin özet hazırlama yöntem kartları."""
    kartlar = [
        ('I. Kart · Ece', 'Olay sırasını korudu.', YES, YES_A),
        ('II. Kart · Kaan', 'Cümleleri aynen kopyaladı.', KIR, KIR_A),
        ('III. Kart · Nil', 'Kendi cümlelerini kurdu.', MAVI, MAVI_A),
        ('IV. Kart · Mert', 'Ayrıntıları özetten çıkardı.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, m, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 10.5, r, 'start')
        ic += yazi(x + 10, y + 31, m, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört özet kontrol kartı: I Ece sırayı korudu, II Kaan aynen kopyaladı, III Nil kendi cümlelerini kurdu, IV Mert ayrıntıları çıkardı.', 14)


def cumle_birlestirme_semasi():
    """İki cümleyi fiilimsiyle birleştirmede 4 anlam ilişkisi şeması."""
    satirlar = [
        ('Zaman (zarf-fiil)', 'Zil çaldı. Sınıfa girdi. → Zil çalınca sınıfa girdi.', YES, YES_A),
        ('Nasıl (zarf-fiil)', 'Sözlüğe baktı. Anlamı buldu. → Sözlüğe bakarak anlamı buldu.', MAVI, MAVI_A),
        ('Amaç (isim-fiil)', 'Kitap alacaktı. Sergiye gitti. → Kitap almak için sergiye gitti.', TUR, TUR_A),
        ('Niteleme (sıfat-fiil)', 'Yazar anı anlatıyor. Dinledik. → Anı anlatan yazarı dinledik.', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ornek, r, z) in enumerate(satirlar):
        y = 4 + i * 24
        ic += kutu(4, y, 118, 20, r, r, 5, 1)
        ic += yazi(63, y + 14, bas, 10.5, '#fff')
        ic += kutu(126, y, 330, 20, z, r, 5, 1.1)
        ic += yazi(134, y + 14, ornek, 10.5, LAC, 'start', True)
    return svg(460, 100, ic, 'Cümle birleştirmede zaman, nasıl, amaç ve niteleme ilişkileri şeması.', 14)


def gorus_bildirme_panosu():
    """Duru ve Emre'nin yazarlık sorusuna verdikleri yanıt kartları."""
    ic = kutu(4, 4, 172, 78, TUR_A, TUR, 8, 1.3)
    ic += yazi(90, 20, 'Duru’nun Yanıtı', 11, TUR)
    ic += yazi(90, 42, '“Bir yazar olsaydım çocuk', 10.5, LAC, 'middle', True)
    ic += yazi(90, 57, 'romanları yazmak isterdim.”', 10.5, LAC, 'middle', True)
    ic += yazi(90, 73, '(Yalnız görüş var, gerekçe yok)', 10.5, TUR)

    ic += kutu(184, 4, 172, 78, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, 'Emre’nin Yanıtı', 11, YES)
    ic += yazi(270, 38, '“Tarihî öyküler yazmak isterdim;', 10.5, LAC, 'middle', True)
    ic += yazi(270, 53, 'çünkü geçmişteki kahramanları', 10.5, LAC, 'middle', True)
    ic += yazi(270, 68, 'tanıtmak çok değerlidir.”', 10.5, YES)
    return svg(360, 86, ic, 'Duru ve Emre nin görüş bildirme kartları: Duru gerekçesiz, Emre çünkü diyerek gerekçeli görüş bildirmiştir.', 14)


def yaz_koku_fisleri():
    """yaz- kökünden türetilen dört sözcük fişi (3. fiş çekimli fiil)."""
    fisler = [
        ('1. fiş · yazılan', 'Sıfat-fiil (eserleri niteler)', MAVI, MAVI_A),
        ('2. fiş · yazarak', 'Zarf-fiil (durum bildirir)', YES, YES_A),
        ('3. fiş · yazdı', 'Kip ve kişi ekli yüklem', KIR, KIR_A),
        ('4. fiş · yazmak', 'İsim-fiil (işin adını bildirir)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 11, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'yaz- kökünden dört fiş: 1 yazılan, 2 yazarak, 3 yazdı, 4 yazmak.', 14)


def baslik_oneri_karti():
    """Köy okullarına kitap ulaştıran öğretmen metni özet ve başlık kartı."""
    ic = kutu(4, 4, 352, 78, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 20, 'Dinlenen Metnin Özeti ve Başlık Ölçütleri', 11, MAVI)
    ic += yazi(180, 40, 'Metin: Cumhuriyet’in ilk yıllarında bir öğretmenin tahta sandıklarla', 10.5, LAC, 'middle', True)
    ic += yazi(180, 55, 'köy okullarına kitap taşıyıp çocuklara okuma sevgisi kazandırması.', 10.5, LAC, 'middle', True)
    ic += yazi(180, 72, '1. Başlık: Konuyu yansıtmalı   ·   2. Başlık: Ana düşünceyi yansıtmalı', 10.5, MAVI)
    return svg(360, 86, ic, 'Köy okullarına kitap taşıyan öğretmen metni için konu ve ana düşünce başlığı kartı.', 14)


def arastir_fiilimsi_karti():
    """araştır- fiil kökünden üç fiilimsi kurma kartı."""
    ic = kutu(4, 4, 352, 74, CAM_A, CAM, 8, 1.3)
    ic += yazi(180, 20, 'Fiil Kökü: araştır-  →  Üç Farklı Görevde Cümle Kurma', 11, CAM)
    ic += yazi(16, 40, '1. Cümle (İsim-fiil): -mak veya -ma ekiyle işin adını bildirsin.', 10.5, LAC, 'start', True)
    ic += yazi(16, 56, '2. Cümle (Sıfat-fiil): -an veya -dığı ekiyle bir ismi nitelesin.', 10.5, LAC, 'start', True)
    ic += yazi(16, 72, '3. Cümle (Zarf-fiil): -arak veya -ınca ekiyle durum bildirsin.', 10.5, LAC, 'start', True)
    return svg(360, 82, ic, 'araştır- fiil kökünden isim-fiil, sıfat-fiil ve zarf-fiil cümleleri kurma ipucu kartı.', 14)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dinleme_surec_semasi()
    s[1]['gorsel'] = sozluk_calisma_karti()
    s[2]['gorsel'] = kok_gorev_semasi()
    s[6]['gorsel'] = ozet_kontrol_kartlari()
    s[7]['gorsel'] = cumle_birlestirme_semasi()
    s[8]['gorsel'] = gorus_bildirme_panosu()
    s[9]['gorsel'] = yaz_koku_fisleri()
    s[10]['gorsel'] = baslik_oneri_karti()
    s[13]['gorsel'] = arastir_fiilimsi_karti()
