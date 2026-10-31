"""8. sınıf Türkçe 1. hafta (Okuma Kültürü: Metni anlama ve fiilimsilere giriş) çalışma kâğıdı görselleri.
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


def fiilimsi_gorev_semasi():
    """İsim-fiil, sıfat-fiil ve zarf-fiilin cümledeki görevleri."""
    kartlar = [
        ('İsim-fiil', 'Bir işin adı olur', 'Örn: not tutmak', MAVI, MAVI_A, 4),
        ('Sıfat-fiil', 'Bir adı niteler', 'Örn: aldığım dergi', TUR, TUR_A, 122),
        ('Zarf-fiil', 'Nasıl / ne zaman', 'Örn: çizerek, bakınca', YES, YES_A, 240),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 58
        ic += kutu(x, 4, 116, 74, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 10, r)
        ic += f'<line x1="{x + 12}" y1="27" x2="{x + 104}" y2="27" stroke="{r}" stroke-width="1"/>'
        ic += yazi(cx, 44, s1, 9.4, LAC)
        ic += yazi(cx, 61, s2, 9.2, LAC, 'middle', True)
    return svg(360, 82, ic, 'Fiilimsi türleri görev şeması: İsim-fiil işin adı, Sıfat-fiil adı niteler, Zarf-fiil nasıl ve ne zaman belirtir.', 22)


def okuma_paragraf_karti():
    """Bilinçli not alma konulu okuma kartı."""
    ic = kutu(4, 4, 352, 84, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{MAVI}"/><rect x="4" y="14" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 18, 'OKUMA KARTI · Konu ve Ana Düşünce', 10, '#fff')
    ic += yazi(180, 38, 'Okurken her cümleyi deftere aynen yazmak dikkati dağıtır.', 9.5, LAC, 'middle', True)
    ic += yazi(180, 54, 'Bunun yerine okuma amacına uygun anahtar bilgileri seçerek', 9.5, LAC, 'middle', True)
    ic += yazi(180, 70, 'kısa notlar almak, metni hızlı ve kalıcı anlamayı sağlar.', 9.5, MAVI, 'middle')
    return svg(360, 92, ic, 'Bilinçli not alma ve anahtar bilgileri seçme konulu okuma kartı.', 22)


def arastirma_yazma_rehberi():
    """Sözlük doğrulama, güvenilir kaynak ve bağlantı ifadeleri rehberi."""
    ic = kutu(4, 4, 172, 82, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, 'Sözcük ve Kaynak', 9.8, YES)
    ic += yazi(90, 38, 'Tahmin et → Sözlükle doğrula', 9.2, LAC, 'middle', True)
    ic += yazi(90, 54, 'Güvenilir ağ: .edu ve .gov', 9.2, LAC, 'middle', True)
    ic += yazi(90, 70, 'Yalnız önemli yeri çiz', 9.2, YES, 'middle')

    ic += kutu(184, 4, 172, 82, MOR_A, MOR, 8, 1.3)
    ic += yazi(270, 20, 'Bağlantı ve Fiilimsi', 9.8, MOR)
    ic += yazi(270, 38, '“oysaki” → karşıtlık kurar', 9.2, LAC, 'middle', True)
    ic += yazi(270, 54, '“özellikle” → vurgu yapar', 9.2, LAC, 'middle', True)
    ic += yazi(270, 70, 'Fiilimsi kip-kişi eki almaz', 9.2, MOR, 'middle')
    return svg(360, 90, ic, 'Sözlük ve kaynak kullanımı ile bağlantı ve fiilimsi ipuçları rehberi.', 22)


def oku_cumle_fisleri():
    """Dört cümle fişinde okumak/okuduğum/okudu/okuyarak karşılaştırması."""
    fisler = [
        ('1. fiş · okumak', 'Sesli okumak etkiledi.', MAVI, MAVI_A),
        ('2. fiş · okuduğum', 'Okuduğum öyküyü önerdim.', TUR, TUR_A),
        ('3. fiş · okudu', 'Dergiyi merakla okudu.', KIR, KIR_A),
        ('4. fiş · okuyarak', 'Metni okuyarak ulaştı.', YES, YES_A),
    ]
    ic = ''
    for i, (bas, cum, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 15, bas, 9.6, r, 'middle')
        ic += yazi(x + 86, y + 30, cum, 9.2, LAC, 'middle', True)
    return svg(360, 92, ic, 'Dört cümle fişi: 1. okumak, 2. okuduğum, 3. okudu çekimli fiil, 4. okuyarak.', 22)


def baglam_ipucu_karti():
    """Ağdalı sözcüğünün bağlamdan tahmin edilmesi kartı."""
    ic = kutu(4, 4, 352, 76, CAM_A, CAM, 8, 1.4)
    ic += yazi(180, 20, 'Bağlamdan Anlam Tahmini Kartı', 10.2, CAM)
    ic += yazi(180, 40, '“Yazarın dili ağdalıydı; uzun cümleler ve yabancı', 9.5, LAC, 'middle', True)
    ic += yazi(180, 55, 'kelimeler yüzünden ne dediği güç anlaşılıyordu.”', 9.5, LAC, 'middle', True)
    ic += yazi(180, 71, 'Adım: İpucu sözleri bul → Tahmin et → Sözlükten doğrula', 9.2, CAM, 'middle')
    return svg(360, 84, ic, 'Ağdalı sözcüğünün bağlamdan tahmin edilmesi için örnek cümle kartı.', 22)


def icin_iliski_semasi():
    """Dört cümlede için edatının amaç-sonuç ve neden-sonuç kullanımı."""
    cumleler = [
        ('I) Yeni kavramları öğrenmek için sözlük kullandı.', MAVI, MAVI_A),
        ('II) Notlarını evde unuttuğu için sunumu erteledi.', KIR, KIR_A),
        ('III) Konuyu pekiştirmek için iki kaynak daha taradı.', YES, YES_A),
        ('IV) Hava erken karardığı için okuma saatini öne aldı.', TUR, TUR_A),
    ]
    ic = ''
    for i, (met, r, z) in enumerate(cumleler):
        y = 4 + i * 23
        ic += kutu(4, y, 352, 20, z, r, 5, 1.2)
        ic += yazi(14, y + 14, met, 9.5, LAC, 'start')
    return svg(360, 96, ic, 'Dört cümlede için sözcüğünün kullanımı: I ve III amaç-sonuç, II ve IV neden-sonuç.', 23)


def gecis_ifadeleri_taslagi():
    """Sıralama bildiren geçiş ifadeleriyle oluşturulmuş metin taslağı."""
    ic = kutu(4, 4, 352, 80, KUM, GRI, 8, 1.3)
    ic += yazi(180, 20, 'Bilgilendirici Metin Hazırlık Basamakları', 10.2, LAC)
    ic += yazi(16, 39, '(1) ………… araştırma konumu ve yazma amacımı belirledim.', 9.5, MAVI, 'start')
    ic += yazi(16, 56, '(2) ………… kütüphanedeki kaynaklardan kısa notlar çıkardım.', 9.5, TUR, 'start')
    ic += yazi(16, 73, '(3) ………… notları kendi cümlelerimle metne dönüştürdüm.', 9.5, YES, 'start')
    return svg(360, 88, ic, 'Üç basamaklı metin hazırlık taslağı: 1 İlk olarak, 2 Ardından, 3 Son olarak.', 22)


def konusma_gorsel_secimi():
    """Hazırlıklı konuşma konusu için seçilen üç görsel kartı."""
    kartlar = [
        ('1. Görsel', 'Kütüphane rafı ve', 'okuma köşesi', YES, YES_A, 4),
        ('2. Görsel', 'Yıllara göre kitap', 'okuma grafiği', MAVI, MAVI_A, 122),
        ('3. Görsel', 'Standart futbol', 'sahası ölçüleri', KIR, KIR_A, 240),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        cx = x + 58
        ic += kutu(x, 4, 116, 72, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 10, r)
        ic += yazi(cx, 42, s1, 9.4, LAC, 'middle', True)
        ic += yazi(cx, 58, s2, 9.4, LAC, 'middle', True)
    return svg(360, 80, ic, 'Okuma alışkanlığı sunumu için üç görsel adayı: 1 kütüphane, 2 kitap okuma grafiği, 3 futbol sahası ölçüleri.', 22)


def yaz_koku_karti():
    """Açık uçlu soru için yaz- fiil kökünden üç fiilimsi üretme kartı."""
    ic = kutu(4, 4, 352, 72, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 19, 'Kök: “yaz-” → Görevine Göre Fiilimsi Kurma', 10.2, MOR)
    ic += yazi(180, 38, '1) İsim-fiil: İşin adını belirtecek biçimde (yazmak / yazma)', 9.4, LAC, 'middle', True)
    ic += yazi(180, 53, '2) Sıfat-fiil: Bir ismi niteleyecek biçimde (yazdığım / yazılan)', 9.4, LAC, 'middle', True)
    ic += yazi(180, 68, '3) Zarf-fiil: Nasıl/ne zaman yapıldığını belirterek (yazarak)', 9.4, LAC, 'middle', True)
    return svg(360, 80, ic, 'Yaz fiil kökünden isim-fiil, sıfat-fiil ve zarf-fiil kurma ipucu kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = fiilimsi_gorev_semasi()
    s[1]['gorsel'] = okuma_paragraf_karti()
    s[3]['gorsel'] = arastirma_yazma_rehberi()
    s[5]['gorsel'] = oku_cumle_fisleri()
    s[7]['gorsel'] = baglam_ipucu_karti()
    s[8]['gorsel'] = icin_iliski_semasi()
    s[9]['gorsel'] = gecis_ifadeleri_taslagi()
    s[10]['gorsel'] = konusma_gorsel_secimi()
    s[13]['gorsel'] = yaz_koku_karti()
