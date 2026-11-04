"""6. sınıf Sosyal Bilgiler 6. hafta (Çözüm Önerilerini Savunma ve Evimiz Dünya’ya Giriş: Kıtalar, Okyanuslar ve Türkiye’nin Yeri) çalışma kâğıdı görselleri.
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


def muzakere_savunma_karti():
    satirlar = [
        ('1. Cümle', '“Okul önüne kısa süreli indirme-bindirme alanı yapılmalıdır.”', MAVI, MAVI_A),
        ('2. Cümle', '“Çünkü veliler sabahları yaya geçidini kapatmak zorunda kalmaz.”', YES, YES_A),
        ('3. Cümle', '“Bir hafta sayım yaptık; geçit her sabah ortalama 18 araçla kapandı.”', TUR, TUR_A),
    ]
    ic = ''
    for i, (no, metin, renk, arka) in enumerate(satirlar):
        y = 6 + i * 31
        ic += kutu(6, y, 588, 26, arka, renk, 6, 1.4)
        ic += kutu(6, y, 92, 26, renk, renk, 6, 1)
        ic += yazi(52, y + 17, no, '#fff', kalin=True)
        ic += yazi(108, y + 17, metin, LAC, 'start', kalin=(i == 0))
    return svg(600, 100, ic, 'İddia, gerekçe ve kanıt cümlelerinden oluşan müzakere savunma kartı.', 21)


def turkiye_iki_kita_sema():
    ic = kutu(6, 6, 588, 88, CAM_A, CAM, 9, 1.4)
    ic += kutu(22, 18, 175, 64, MOR_A, MOR, 8, 1.5)
    ic += yazi(109, 40, 'TRAKYA (Avrupa)', MOR, kalin=True)
    ic += yazi(109, 64, 'Başlangıç: Edirne', LAC)

    ic += kutu(212, 26, 130, 48, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(277, 46, 'İstanbul Boğazı', MAVI, kalin=True)
    ic += yazi(277, 64, '& Marmara', LAC)

    ic += kutu(358, 18, 218, 64, YES_A, YES, 8, 1.5)
    ic += yazi(467, 40, 'ANADOLU (Asya)', YESIL_K, kalin=True)
    ic += yazi(467, 64, 'Varış: Başkent Ankara', LAC)
    return svg(600, 100, ic, 'Avrupa’daki Trakya (Edirne) ile Asya’daki Anadolu (Ankara) geçiş şeması.', 21)


def harita_terimleri_panosu():
    kartlar = [
        ('1. Anadolu', 'Üç tarafı denizlerle çevrili', YES, YES_A),
        ('2. Gökçeada & Kıbrıs', 'Dört tarafı sularla çevrili', MAVI, MAVI_A),
        ('3. Çanakkale Boğazı', 'İki denizi bağlayan dar geçit', TUR, TUR_A),
        ('4. Hint Okyanusu', 'Kıtaları ayıran dev su kütlesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Anadolu, Gökçeada, Çanakkale Boğazı ve Hint Okyanusu terim kartları.', 21)


def kantin_uzlasma_karti():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 25, 'A Grubu Önerisi', MAVI, kalin=True)
    ic += yazi(149, 50, '“Kantinde plastik şişe satışı', LAC, kalin=True)
    ic += yazi(149, 74, 'atıkları azaltmak için kaldırılsın.”', LAC)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'B Grubu Önerisi ve İtirazı', YESIL_K, kalin=True)
    ic += yazi(451, 50, '“Önce katlara su sebili konulsun', LAC, kalin=True)
    ic += yazi(451, 74, 've öğrenciler matara getirsin.”', LAC)
    return svg(600, 98, ic, 'Kantin plastik şişe sorunu için A ve B gruplarının uzlaşma kartları.', 21)


def sorun_cozme_zinciri():
    kartlar = [
        ('1. Tanımla', 'Sorunu gözlemle fark et', MAVI, MAVI_A),
        ('2. Karşılaştır', 'Nedenleri çok yönlü incele', YES, YES_A),
        ('3. Geliştir', '4 ölçüte uygun öneri yaz', TUR, TUR_A),
        ('4. Savun', 'İddia, gerekçe, kanıt sun', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Toplumsal sorun çözme ve müzakere sürecinin 4 aşaması.', 21)


def dunya_kitalar_okyanuslar_karti():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(149, 25, '7 Kıta (Büyük Kara Parçaları)', YESIL_K, kalin=True)
    ic += yazi(149, 50, 'Asya, Afrika, Avrupa (Ortada bitişik)', LAC, kalin=True)
    ic += yazi(149, 74, 'K. ve G. Amerika, Avustralya, Antarktika', LAC)

    ic += kutu(308, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(451, 25, '3 Okyanus ve İç Denizler', MAVI, kalin=True)
    ic += yazi(451, 50, 'Okyanuslar: Büyük, Atlas ve Hint', LAC, kalin=True)
    ic += yazi(451, 74, 'Denizler: Akdeniz, Karadeniz (Küçük su)', LAC)
    return svg(600, 98, ic, 'Dünyadaki 7 kıta, 3 büyük okyanus ve denizleri karşılaştıran kart.', 21)


def agac_dikimi_savunma_karti():
    ic = kutu(6, 6, 588, 86, TUR_A, TUR, 9, 1.5)
    ic += kutu(6, 6, 588, 26, TUR, TUR, 9, 1)
    ic += yazi(300, 24, 'EKSİK SAVUNMA KARTI · OKUL BAHÇESİ ÖNERİSİ', '#fff', kalin=True)
    ic += yazi(300, 50, 'İddia: “Okul bahçemizin güney kenarına 15 adet çınar fidanı dikilmelidir.”', LAC, kalin=True)
    ic += yazi(300, 74, 'Eksik Unsurlar: 1) Gerekçe (Neden?) · 2) Kanıt (Hangi gözlem veya sayı?)', KIR, kalin=True)
    return svg(600, 98, ic, 'Okul bahçesine ağaç dikilmesi iddiasını içeren eksik savunma kartı.', 21)


def bogazlar_ve_denizler_panosu():
    kartlar = [
        ('İstanbul Şehrimiz', 'Hem Asya hem Avrupa’da toprağı var', MOR, MOR_A),
        ('Boğazlar ve Marmara', 'Anadolu ile Trakya’yı birbirinden ayırır', MAVI, MAVI_A),
        ('Üç Tarafımız Deniz', 'Kuzey: Karadeniz · Batı: Ege · Güney: Akdeniz', CAM, CAM_A),
        ('Kıtalar Köprüsü', 'Asya ile Avrupa’nın en yakın noktası', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Türkiye’nin iki kıtadaki konumu, boğazları ve çevre denizleri panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = muzakere_savunma_karti()
    s[4]['gorsel'] = turkiye_iki_kita_sema()
    s[5]['gorsel'] = harita_terimleri_panosu()
    s[6]['gorsel'] = kantin_uzlasma_karti()
    s[7]['gorsel'] = sorun_cozme_zinciri()
    s[8]['gorsel'] = dunya_kitalar_okyanuslar_karti()
    s[10]['gorsel'] = agac_dikimi_savunma_karti()
    s[11]['gorsel'] = bogazlar_ve_denizler_panosu()
