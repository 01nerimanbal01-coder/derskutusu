"""6. sınıf Sosyal Bilgiler 5. hafta (Toplumsal Sorunlar ve Çözüm Önerileri: Nedenleri Karşılaştırma ve Çözüm Geliştirme) çalışma kâğıdı görselleri.
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


def sorun_cumlesi_kontrol_karti():
    satirlar = [
        ('1. Not (Tam)', 'Atatürk Parkı’nda akşamları lambalar yanmıyor; sakinler yürüyemiyor.', YES, YES_A),
        ('2. Not (Genel)', 'Şehirlerde insanlar parkların temizliğine hiç dikkat etmiyor.', MAVI, MAVI_A),
        ('3. Not (Belirsiz)', 'Günümüzde enerji konusunda her yerde sıkıntılar yaşanıyor.', TUR, TUR_A),
        ('4. Not (Bireysel)', 'Kardeşim dün akşam masa lambasını kapatmayı unuttu.', MOR, MOR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 26
        ic += kutu(6, y, 588, 22, arka, renk, 6, 1.3)
        ic += kutu(6, y, 108, 22, renk, renk, 6, 1)
        ic += yazi(60, y + 15, no, '#fff', kalin=True)
        ic += yazi(122, y + 15, metin, LAC, 'start', kalin=(i == 0))
    return svg(600, 112, ic, 'Nerede, kimler, ne zaman ve ne sorularına göre dört sorun notu kartı.', 21)


def trafik_farkli_bakis_panosu():
    kartlar = [
        ('Sürücü (Veli) Bakışı', 'Okul önünde kısa süreli cep yok', MAVI, MAVI_A),
        ('Yaya (Öğrenci) Bakışı', 'Araçlar yaya geçidini kapatıyor', YES, YES_A),
        ('Belediye Uzmanı Bakışı', 'Sabah saatinde otobüs seferi az', TUR, TUR_A),
        ('Okul Müdürü Bakışı', 'Tüm sınıflar aynı dakikada giriyor', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Okul önü trafik sorununa dört farklı bakış açısını gösteren pano.', 21)


def teknoloji_sorun_agaci_kartlari():
    kartlar = [
        ('1. Kontrolsüz Ekran', 'Sorun ağacının ana gövdesi', TUR, TUR_A),
        ('2. Evde Kural Olmaması', 'Sorunu besleyen kök neden', KIR, KIR_A),
        ('3. Uyku ve Dikkat Kaybı', 'Dallarda görülen olumsuz sonuç', MOR, MOR_A),
        ('4. Ekransız Aile Akşamı', 'Kök nedene yönelik çözüm', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Teknoloji bağımlılığı sorun ağacının gövde, kök, dal ve çözüm kartları.', 21)


def su_israfi_paylasim_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(6, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(149, 24, 'Bireyin Sorumluluğu', '#fff', kalin=True)
    ic += yazi(149, 50, 'Diş fırçalarken musluğu kapatmak,', LAC, kalin=True)
    ic += yazi(149, 74, 'damlatan musluğu hemen bildirmek', MAVI, kalin=True)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(308, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(451, 24, 'Belediye & Okul Sorumluluğu', '#fff', kalin=True)
    ic += yazi(451, 50, 'Şebeke boru kaçaklarını onarmak,', LAC, kalin=True)
    ic += yazi(451, 74, 'tasarruflu musluk başlığı takmak', YESIL_K, kalin=True)
    return svg(600, 98, ic, 'Su israfını önlemede birey ve kurum görev paylaşımı kartı.', 21)


def oneri_duzenleme_dongusu():
    adimlar = [
        ('1. Paylaş & Dinle', 'Savunmaya geçmeden dinle', MAVI, MAVI_A),
        ('2. Güçlü / Zayıf', 'Görüşleri iki gruba ayır', TUR, TUR_A),
        ('3. Somut Ekle', 'Kim, ne zaman, nasıl yaz', YES, YES_A),
        ('4. 4 Ölçüt Kontrol', 'Özgün, uygulanır, kalıcı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Geri bildirimlerle çözüm önerisini düzenleme döngüsünün 4 adımı.', 21)


def neden_zinciri_gurultu_sema():
    ic = kutu(6, 6, 588, 86, CAM_A, CAM, 9, 1.5)
    ic += kutu(6, 6, 588, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 24, 'OKUL KORİDORUNDA GÜRÜLTÜ · “NEDEN?” ZİNCİRİ ANALİZİ', '#fff', kalin=True)
    ic += yazi(300, 50, 'Belirti: Koridor çok gürültülü → Neden 1: Öğrenciler koridorda koşup bağırıyor', LAC, kalin=True)
    ic += yazi(300, 74, '→ Kök Neden: Yağmurlu günlerde katlarda ve bahçede masa oyunu / etkinlik köşesi yok!', CAM, kalin=True)
    return svg(600, 98, ic, 'Okul koridorundaki gürültünün kök nedenine inen Neden zinciri şeması.', 21)


def kutuphane_oneri_elestiri_karti():
    ic = kutu(6, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += kutu(6, 6, 286, 26, TUR, TUR, 9, 1)
    ic += yazi(149, 24, 'İlk Öneri (Eksik Hâli)', '#fff', kalin=True)
    ic += yazi(149, 50, '“Okul kütüphanesine herkes', LAC, kalin=True)
    ic += yazi(149, 74, 'evden kitap getirip bıraksın.”', TUR, kalin=True)

    ic += kutu(308, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(451, 24, 'Sınıftan Gelen 2 Zayıf Yön', '#fff', kalin=True)
    ic += yazi(451, 50, '1) Kitapları kim, ne zaman ayıracak?', LAC, kalin=True)
    ic += yazi(451, 74, '2) Raflara nasıl kaydedilecek?', KIR, kalin=True)
    return svg(600, 98, ic, 'Kütüphane kitap bağışı önerisi ve sınıftan gelen iki geri bildirim kartı.', 21)


def sorumluluk_eslestirme_panosu():
    kartlar = [
        ('Enerji Tasarrufu', 'Birey: Lambayı kapat | Kurum: Kamu spotu', YES, YES_A),
        ('Atık Yönetimi', 'Birey: Atığı ayrıştır | Belediye: Tesis kur', MAVI, MAVI_A),
        ('Gürültü Kirliliği', 'Birey: Sesi kıs | Belediye: Ses bariyeri', CAM, CAM_A),
        ('Hatalı Kart (!)', 'Birey: Üst geçit inşa et (?) | Kurum: Geçidi kullan', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Bireysel ve kurumsal sorumluluk örneklerini karşılaştıran dörtlü pano.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sorun_cumlesi_kontrol_karti()
    s[4]['gorsel'] = trafik_farkli_bakis_panosu()
    s[5]['gorsel'] = teknoloji_sorun_agaci_kartlari()
    s[6]['gorsel'] = su_israfi_paylasim_karti()
    s[7]['gorsel'] = oneri_duzenleme_dongusu()
    s[8]['gorsel'] = neden_zinciri_gurultu_sema()
    s[10]['gorsel'] = kutuphane_oneri_elestiri_karti()
    s[11]['gorsel'] = sorumluluk_eslestirme_panosu()
