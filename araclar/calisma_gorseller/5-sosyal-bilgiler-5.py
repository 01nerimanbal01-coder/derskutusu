"""5. sınıf Sosyal Bilgiler 5. hafta (Yardımlaşma ve Dayanışma Faaliyetleri: Yardım Projesini Planlama ve Uygulama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def proje_gorev_kartlari():
    kartlar = [
        ('1. Kart · İhtiyaç Saptama', 'Hedef okulun eksiklerini öğrenir', YES, YES_A),
        ('2. Kart · Kampanya Sor. (!)', 'Ürünleri boyuna göre koliler', KIR, KIR_A),
        ('3. Kart · Faaliyet Yür. (!)', 'Toplantıyı ve iletişimi yönetir', TUR, TUR_A),
        ('4. Kart · Grup Yöneticisi (!)', 'Koridor panosuna afiş boyar', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Yardım projesi grubundaki görev unvanları ve iş eşleştirme kartları.', 20)


def kurum_stk_ayrim_kartlari():
    kartlar = [
        ('1. Kart · Türk Kızılay', 'Afet yardımı ve kan bağışı (STK)', KIR, KIR_A),
        ('2. Kart · AFAD', 'Devlete bağlı acil durum kurumu', MAVI, MAVI_A),
        ('3. Kart · TEMA Vakfı', 'Ağaçlandırma ve doğa koruma (STK)', YES, YES_A),
        ('4. Kart · LÖSEV', 'Lösemili çocuklara destek (STK)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Kamu kurumu olan AFAD ile sivil toplum kuruluşlarını karşılaştıran kartlar.', 20)


def dort_stk_calisma_kartlari():
    kartlar = [
        ('1. Türk Kızılay', 'Afet yardımı, çadır ve kan bağışı', KIR, KIR_A),
        ('2. Yeşilay', 'Bağımlılıkla mücadele ve eğitim', YES, YES_A),
        ('3. TEMA Vakfı', 'Erozyonla mücadele, fidan dikimi', TUR, TUR_A),
        ('4. LÖSEV', 'Lösemili çocuklara sağlık desteği', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Türk Kızılay, Yeşilay, TEMA Vakfı ve LÖSEV çalışma alanları kartları.', 20)


def eksik_duyuru_panosu():
    ic = kutu(6, 6, 588, 86, TUR_A, TUR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, TUR, TUR, 9, 1)
    ic += yazi(300, 24, 'OKUL DUYURU PANOSU · EKSİK KAMPANYA AFİŞİ (!)', '#fff', kalin=True)
    ic += yazi(300, 50, '“YARDIM KAMPANYAMIZA KATILIN! DESTEKLERİNİZİ BEKLİYORUZ!”', LAC, kalin=True)
    ic += yazi(300, 74, 'Eksik: Ne toplanıyor? · Kimin için? · Nereye bırakılacak? · Son tarih ne zaman?', KIR, kalin=True)
    return svg(600, 98, ic, 'Bilgileri eksik bırakılmış yardım kampanyası duyuru panosu kartı.', 20)


def proje_bes_adim_kartlari():
    kartlar = [
        ('1. Planlama', 'Amaç, süre ve ölçüt', MAVI, MAVI_A),
        ('2. Görev & Kaynak', 'İş bölümü ve liste', TUR, TUR_A),
        ('3. Uygulama', 'Toplama ve gönderim', YES, YES_A),
        ('4. Değerlendirme', 'Kontrol ve sonuç', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Yardım projesinin planlama, görev paylaşımı, uygulama ve değerlendirme adımları.', 20)


def anadolu_dayanisma_panosu():
    kartlar = [
        ('İmece Geleneği', 'Ortak işin sırayla ve el birliğiyle yapılması', YES, YES_A),
        ('Komşuluk Kültürü', 'Sevinçte ve zorlukta en yakın destek', MAVI, MAVI_A),
        ('Ahilik Teşkilatı', 'Esnaf arasında dürüstlük ve orta sandığı', TUR, TUR_A),
        ('Toplumsal Sonuç', 'Karşılıklı güven ve güçlü birlik duygusu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'İmece, komşuluk ve Ahilik geleneklerini özetleyen dayanışma panosu.', 20)


def degerlendirme_karsilastirma_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, 'A Grubu · Eksik Süreç', KIR, kalin=True)
    ic += yazi(149, 50, 'Kolileri kargoya verdikten sonra', LAC)
    ic += yazi(149, 72, 'toplantı yapmadan projeyi bitirdi.', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'B Grubu · Tam Süreç', YESIL_K, kalin=True)
    ic += yazi(451, 50, 'Kontrol listesiyle hedefin gerçekleşme', LAC)
    ic += yazi(451, 72, 'durumunu ve eksikleri değerlendirdi.', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'Proje sonunda değerlendirme yapan ve yapmayan iki grubun karşılaştırma kartı.', 20)


def el_ele_proje_plani_panosu():
    kartlar = [
        ('Proje Amacı & Süre', 'Giysi ve kırtasiye desteği · 4 hafta', MAVI, MAVI_A),
        ('Hedef Kitle', 'Deprem bölgesindeki kardeş okul', YES, YES_A),
        ('Sağlanan Kaynaklar', 'Sınıfımız, diğer sınıflar ve veliler', TUR, TUR_A),
        ('Başarı Ölçütü', 'Kolilerin zamanında ve tam ulaşması', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'El Ele Gönül Gönüle yardım projesinin plan tablosu.', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = proje_gorev_kartlari()
    s[4]['gorsel'] = kurum_stk_ayrim_kartlari()
    s[5]['gorsel'] = dort_stk_calisma_kartlari()
    s[6]['gorsel'] = eksik_duyuru_panosu()
    s[7]['gorsel'] = proje_bes_adim_kartlari()
    s[8]['gorsel'] = anadolu_dayanisma_panosu()
    s[10]['gorsel'] = degerlendirme_karsilastirma_karti()
    s[11]['gorsel'] = el_ele_proje_plani_panosu()
