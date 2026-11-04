"""8. sınıf DKAB 8. hafta (İslam'ın Paylaşma ve Yardımlaşmaya Verdiği Önem, İnfak ve Ensar-Muhacir Kardeşliği) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); yalnız '·' veya '-' ayırıcı (K155/K172)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=14):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ayet_kartlari_sema():
    """Soru 1: Bakara 261, Âl-i İmrân 92 ve Haşr 9 ayet kartları."""
    ic = kutu(4, 4, 352, 98, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 21, 'Kur’an-ı Kerim’de Paylaşma ve Dayanışma Ayetleri', KAHVE)
    kartlar = [
        ('1. Kart', 'Bakara, 261', '1 tohum -> 700 tane', YES, YES_A, 10),
        ('2. Kart', 'Âl-i İmrân, 92', 'Sevilen maldan infak', MAVI, MAVI_A, 126),
        ('3. Kart', 'Haşr, 9', 'Kardeşini tercih etme', TUR, TUR_A, 242),
    ]
    for bas, sure, ozet, r, z, x in kartlar:
        ic += kutu(x, 28, 108, 68, z, r, 7, 1.3)
        ic += yazi(x + 54, 45, bas, r)
        ic += yazi(x + 54, 63, sure, LAC)
        ic += yazi(x + 54, 82, ozet, LAC, 'middle', True)
    return svg(360, 106, ic, 'Paylaşma ayetleri kartları: Bakara 261, Âl-i İmrân 92 ve Haşr 9.')


def infak_basak_sema():
    """Soru 3: Bakara Suresi 261. ayet yedi başaklı tohum bereket şeması."""
    ic = kutu(4, 4, 352, 96, YES_A, YES, 9, 1.4)
    ic += yazi(180, 21, 'Bakara Suresi 261. Ayet · İnfakın Bereketi', YESIL_K)
    ic += kutu(14, 30, 96, 60, '#fff', YES, 7, 1.3)
    ic += yazi(62, 52, '1 Tohum', YESIL_K)
    ic += yazi(62, 74, '(İnfak)', LAC, 'middle', True)
    ic += yazi(122, 62, '->', YESIL_K)
    ic += kutu(134, 30, 96, 60, '#fff', TUR, 7, 1.3)
    ic += yazi(182, 52, '7 Başak', TUR)
    ic += yazi(182, 74, '(Her dalda 100)', LAC, 'middle', True)
    ic += yazi(242, 62, '->', TUR)
    ic += kutu(254, 30, 92, 60, '#fff', MAVI, 7, 1.3)
    ic += yazi(300, 52, '700 Tane', MAVI)
    ic += yazi(300, 74, '(Katlanan ecir)', LAC, 'middle', True)
    return svg(360, 104, ic, 'Bakara Suresi 261. ayetteki 1 tohumdan 7 başak ve 700 tane bereket şeması.')


def fayda_eslestirme_sema():
    """Soru 5: Paylaşmanın bireysel ve toplumsal faydaları 4 satırlı tablo (3. satır hatalı)."""
    ic = kutu(4, 4, 352, 102, '#fff', MAVI, 9, 1.4)
    ic += yazi(180, 20, 'Paylaşmanın Bireysel ve Toplumsal Etkileri Kartı', MAVI)
    satirlar = [
        ('1. Cimrilik ve hırsı temizler · Bireysel', YES_A, YES),
        ('2. Sevgi bağlarını güçlendirir · Toplumsal', MAVI_A, MAVI),
        ('3. Sınıf ayrımını derinleştirir · Toplumsal', KIR_A, KIR),
        ('4. Şükür ve huzur kazandırır · Bireysel', MOR_A, MOR),
    ]
    for i, (met, z, r) in enumerate(satirlar):
        y = 26 + i * 19
        ic += kutu(14, y, 332, 16, z, r, 4, 1.1)
        ic += yazi(180, y + 12, met, LAC, 'middle', True)
    return svg(360, 110, ic, 'Paylaşmanın bireysel ve toplumsal faydaları 4 satırlı tablo.')


def hadis_dayanisma_kartlari():
    """Soru 6: İki hadis-i şerif dayanışma kartı."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, '1. Hadis-i Şerif', MAVI)
    ic += yazi(90, 44, '“Müminler merhamette', LAC, 'middle', True)
    ic += yazi(90, 62, 'bir bedenin organları', LAC, 'middle', True)
    ic += yazi(90, 80, 'gibidir.”', MAVI)

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, '2. Hadis-i Şerif', TUR)
    ic += yazi(270, 44, '“Komşusu açken', LAC, 'middle', True)
    ic += yazi(270, 62, 'tok yatan bizden', LAC, 'middle', True)
    ic += yazi(270, 80, 'değildir.”', TUR)
    return svg(360, 100, ic, 'Hz. Peygamberin yardımlaşma konulu iki hadis kartı.')


def ensar_muhacir_koprusu():
    """Soru 7: Medine'de Muhacir, Muâhât ve Ensar kardeşlik köprüsü."""
    ic = kutu(4, 4, 352, 96, KUM, ALTIN, 9, 1.4)
    ic += yazi(180, 21, 'Medine’de Kardeşlik Köprüsü (622 Hicret Sonrası)', KAHVE)
    ic += kutu(12, 28, 106, 64, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(65, 45, 'MUHACİR', MAVI)
    ic += yazi(65, 63, 'Mekke’den göç etti', LAC, 'middle', True)
    ic += yazi(65, 80, 'İffetle çalıştı', MAVI, 'middle', True)

    ic += kutu(127, 36, 106, 48, '#fff', ALTIN, 7, 1.4)
    ic += yazi(180, 55, 'MUÂHÂT', KAHVE)
    ic += yazi(180, 73, 'Kardeşlik Akdi', LAC, 'middle', True)

    ic += kutu(242, 28, 106, 64, YES_A, YES, 7, 1.3)
    ic += yazi(295, 45, 'ENSAR', YESIL_K)
    ic += yazi(295, 63, 'Evini ve malını açtı', LAC, 'middle', True)
    ic += yazi(295, 80, 'Îsâr ahlakı gösterdi', YESIL_K, 'middle', True)
    return svg(360, 104, ic, 'Medinede Muhacir, Muâhât ve Ensar kardeşlik köprüsü şeması.')


def muahat_zaman_seridi():
    """Soru 8: Ensar-Muhacir kardeşliğinin 4 aşamalı zaman şeridi."""
    adlar = [
        ('1. Adım', 'Hicret', MAVI, MAVI_A),
        ('2. Adım', 'Misafirlik', YES, YES_A),
        ('3. Adım', 'Muâhât', TUR, TUR_A),
        ('4. Adım', 'Ortak Üretim', MOR, MOR_A),
    ]
    ic = kutu(4, 4, 352, 84, '#fff', GRI, 8, 1.2)
    ic += yazi(180, 20, 'Medine’de Dayanışma Toplumunun Oluşum Akışı', LAC)
    for i, (ust, alt, r, z) in enumerate(adlar):
        x = 12 + i * 86
        ic += kutu(x, 28, 78, 52, z, r, 7, 1.3)
        ic += yazi(x + 39, 48, ust, r)
        ic += yazi(x + 39, 68, alt, LAC, 'middle', True)
    return svg(360, 92, ic, 'Hicret, Misafirlik, Muâhât ve Ortak Üretim 4 adımlı zaman şeridi.')


def maun_birr_panosu():
    """Soru 9: Maûn Suresi uyarısı ve Birr (gerçek iyilik) karşılaştırma panosu."""
    ic = kutu(4, 4, 172, 92, KIR_A, KIR, 8, 1.4)
    ic += yazi(90, 22, 'Maûn Suresi Uyarısı', KIR)
    ic += yazi(90, 44, 'Yetimi itip kakmak', LAC, 'middle', True)
    ic += yazi(90, 62, 'Riya (gösteriş) yapmak', LAC, 'middle', True)
    ic += yazi(90, 80, 'Yardımı (maûn) esirgemek', KIR, 'middle', True)

    ic += kutu(184, 4, 172, 92, YES_A, YES, 8, 1.4)
    ic += yazi(270, 22, 'Birr (Gerçek İyilik)', YESIL_K)
    ic += yazi(270, 44, 'İhlasla Allah rızası', LAC, 'middle', True)
    ic += yazi(270, 62, 'Sevilen maldan infak', LAC, 'middle', True)
    ic += yazi(270, 80, 'Yetim ve yoksulu gözetmek', YESIL_K, 'middle', True)
    return svg(360, 100, ic, 'Maûn Suresi uyarısı ile Birr gerçek iyilik ahlakı karşılaştırma panosu.')


def uc_davranis_karti():
    """Soru 12: I Muâhât, II Manevi sadaka, III Maûn örnek davranış kartları."""
    kartlar = [
        ('I. Davranış', 'Göçmen aileyi', 'kardeş edinmek', MAVI, MAVI_A, 6),
        ('II. Davranış', 'Üzgün arkadaşına', 'tebessüm etmek', YES, YES_A, 124),
        ('III. Davranış', 'Komşuya tuz ve', 'mutfak kabı vermek', TUR, TUR_A, 242),
    ]
    ic = ''
    for bas, s1, s2, r, z, x in kartlar:
        ic += kutu(x, 4, 112, 86, z, r, 8, 1.4)
        ic += yazi(x + 56, 22, bas, r)
        ic += yazi(x + 56, 48, s1, LAC, 'middle', True)
        ic += yazi(x + 56, 68, s2, LAC)
    return svg(360, 94, ic, 'Üç örnek davranış kartı: I Kardeş edinme, II Tebessüm etme, III Komşuya kap verme.')


def carsi_iffet_karti():
    """Soru 13: Sa'd bin Rebî ve Abdurrahman bin Avf iffet ve çalışkanlık kartı."""
    ic = kutu(4, 4, 352, 90, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 21, 'Sahabe Örneği · Cömertlik ve Alın Teri Dengesi', KAHVE)
    ic += kutu(14, 28, 160, 58, YES_A, YES, 6, 1.2)
    ic += yazi(94, 46, 'Sa’d bin Rebî (Ensar):', YESIL_K)
    ic += yazi(94, 68, '“Malımın yarısı senindir.”', LAC, 'middle', True)
    ic += kutu(186, 28, 160, 58, MAVI_A, MAVI, 6, 1.2)
    ic += yazi(266, 46, 'Abdurrahman b. Avf:', MAVI)
    ic += yazi(266, 68, '“Bana çarşıyı gösterin.”', LAC, 'middle', True)
    return svg(360, 98, ic, 'Sad bin Rebî ve Abdurrahman bin Avf diyalog kartı.')


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ayet_kartlari_sema()
    s[2]['gorsel'] = infak_basak_sema()
    s[4]['gorsel'] = fayda_eslestirme_sema()
    s[5]['gorsel'] = hadis_dayanisma_kartlari()
    s[6]['gorsel'] = ensar_muhacir_koprusu()
    s[7]['gorsel'] = muahat_zaman_seridi()
    s[8]['gorsel'] = maun_birr_panosu()
    s[11]['gorsel'] = carsi_iffet_karti()
