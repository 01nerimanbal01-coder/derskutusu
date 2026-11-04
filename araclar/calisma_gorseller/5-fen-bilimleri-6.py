"""5. sınıf Fen Bilimleri 6. hafta (Güneş, Dünya ve Ay’ın Hareketleri ve Büyüklük Modeli) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, ALTIN, YESIL_K, KUM = '#9aa6bd', '#eef1f6', '#c9a227', '#0f6b45', '#fffdf5'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def nesne_model_kartlari():
    kartlar = [
        ('1. Kart', 'Güneş: Futbol topu', 'Dünya: Portakal · Ay: Karpuz', MAVI, MAVI_A),
        ('2. Kart', 'Güneş: Basketbol topu', 'Dünya: Ceviz · Ay: Mercimek', YES, YES_A),
        ('3. Kart', 'Güneş: Tenis topu', 'Dünya: Basketbol · Ay: Nohut', TUR, TUR_A),
        ('4. Kart', 'Güneş: Misket', 'Dünya: Pinpon topu · Ay: Erik', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 52
        ic += kutu(x, y, 288, 46, arka, renk, 8, 1.4)
        ic += yazi(x + 42, y + 20, bas, renk, kalin=True)
        ic += yazi(x + 185, y + 20, s1, LAC, kalin=True)
        ic += yazi(x + 144, y + 38, s2, LAC)
    return svg(600, 112, ic, 'Güneş, Dünya ve Ay büyüklük modeli için seçilen dört nesne kartı.', 21)


def yorunge_hareket_sema():
    ic = kutu(6, 6, 588, 96, KUM, GRI, 9, 1.4)
    ic += f'<ellipse cx="195" cy="54" rx="145" ry="38" fill="none" stroke="{MAVI}" stroke-width="1.5" stroke-dasharray="5,3"/>'
    ic += f'<circle cx="115" cy="54" r="24" fill="{TUR_A}" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(115, 58, 'K (Güneş)', TUR, kalin=True)
    ic += f'<circle cx="295" cy="54" r="32" fill="none" stroke="{MOR}" stroke-width="1.4" stroke-dasharray="3,2"/>'
    ic += f'<circle cx="295" cy="54" r="11" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(295, 36, 'L (Dünya)', MAVI, kalin=True)
    ic += f'<circle cx="327" cy="54" r="5" fill="{GRI_A}" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(352, 58, 'M (Ay)', LAC, kalin=True)
    ic += yazi(195, 28, '1. Yörünge (↺)', MAVI, kalin=True)
    ic += yazi(295, 97, '2. Yörünge (↺)', MOR, kalin=True)
    ic += kutu(392, 16, 190, 76, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(487, 36, 'Yön: Batıdan Doğuya (↺)', MAVI, kalin=True)
    ic += yazi(487, 58, '1: L’nin K etrafında yörüngesi', LAC)
    ic += yazi(487, 78, '2: M’nin L etrafında yörüngesi', LAC)
    return svg(600, 108, ic, 'Güneş (K), Dünya (L) ve Ay (M) dönme ve dolanma yörüngeleri şeması.', 21)


def dort_hareket_karti():
    kartlar = [
        ('1. Hareket Kartı', 'Güneş kendi ekseninde (↺)', TUR, TUR_A),
        ('2. Hareket Kartı', 'Dünya kendi ekseninde (↺)', MAVI, MAVI_A),
        ('3. Hareket Kartı', 'Dünya, Güneş etrafında (↺)', YES, YES_A),
        ('4. Hareket Kartı', 'Ay, Dünya etrafında (↺)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Güneş, Dünya ve Ay’ın dönme ve dolanma hareket kartları.', 21)


def ay_es_zamanli_kart():
    ic = kutu(6, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(149, 26, 'Ay’ın Kendi Ekseninde Dönmesi', MAVI, kalin=True)
    ic += yazi(149, 52, 'Süre: Yaklaşık 27,3 gün', LAC, kalin=True)
    ic += yazi(149, 76, 'Yön: Saat yönünün tersi (↺)', LAC)

    ic += kutu(308, 6, 286, 86, MOR_A, MOR, 9, 1.4)
    ic += yazi(451, 26, 'Ay’ın Dünya Etrafında Dolanması', MOR, kalin=True)
    ic += yazi(451, 52, 'Süre: Yaklaşık 27,3 gün', LAC, kalin=True)
    ic += yazi(451, 76, 'Sonuç: Hep aynı yüzü görülür', LAC)
    return svg(600, 98, ic, 'Ay’ın dönme ve dolanma sürelerinin eşitliğini gösteren bilgi kartı.', 21)


def sure_siralama_kartlari():
    kartlar = [
        ('Dünya Dönme', '1 tam tur: 24 saat', MAVI, MAVI_A),
        ('Güneş Dönme', '1 tam tur: ~25 gün', TUR, TUR_A),
        ('Ay Dolanma', '1 tam tur: ~27,3 gün', MOR, MOR_A),
        ('Dünya Dolanma', '1 tur: 365 gün 6 s', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 82, arka, renk, 8, 1.4)
        ic += yazi(x + 70, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 12}" y1="38" x2="{x + 128}" y2="38" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 70, 64, alt, LAC)
    return svg(600, 94, ic, 'Dört astronomik hareketin tamamlanma sürelerini gösteren kartlar.', 21)


def zaman_hesap_karti():
    ic = kutu(6, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(149, 26, '1. Hareket: Güneş Etrafında', TUR, kalin=True)
    ic += yazi(149, 52, 'Dünya 3 tam tur dolanıyor', LAC, kalin=True)
    ic += yazi(149, 76, '(1 tam dolanma = 1 yıl)', LAC)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 26, '2. Hareket: Kendi Ekseninde', YESIL_K, kalin=True)
    ic += yazi(451, 52, 'Dünya 15 tam tur dönüyor', LAC, kalin=True)
    ic += yazi(451, 76, '(1 tam dönme = 24 saat = 1 gün)', LAC)
    return svg(600, 98, ic, 'Dünya’nın 3 dolanma ve 15 dönme hareketinin zaman hesaplama kartı.', 21)


def model_degerlendirme_panosu():
    kartlar = [
        ('1. Ölçüt: Geometrik Şekil', 'Üçü de küresel strafor top', YES, YES_A),
        ('2. Ölçüt: Hacimsel Boyut', 'Sıralama: Güneş > Dünya > Ay', MAVI, MAVI_A),
        ('3. Ölçüt: Konum ve Mesafe', 'Ay Dünya’ya yakın, Güneş uzak', CAM, CAM_A),
        ('4. Ölçüt: Hareket Yönü (!)', 'Oklar saat yönünde (doğudan batıya)', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Kerem’in hazırladığı Güneş, Dünya ve Ay maketi değerlendirme panosu.', 21)


def tel_masali_model_duzenegi():
    ic = kutu(6, 6, 588, 90, KUM, GRI, 9, 1.4)
    ic += f'<rect x="70" y="44" width="250" height="14" rx="5" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    ic += f'<rect x="320" y="46" width="120" height="10" rx="4" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<circle cx="70" cy="51" r="24" fill="{TUR}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(70, 55, 'Güneş', '#fff', kalin=True)
    ic += f'<circle cx="320" cy="51" r="14" fill="{MAVI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(320, 26, 'Dünya', MAVI, kalin=True)
    ic += f'<circle cx="440" cy="51" r="8" fill="{GRI}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(440, 28, 'Ay', LAC, kalin=True)
    ic += yazi(195, 36, '1. Şerit (Uzun Kol)', TUR, kalin=True)
    ic += yazi(380, 36, '2. Şerit (Kısa Kol)', MAVI, kalin=True)
    ic += yazi(300, 82, 'Tel maşalar dönme ve dolanma hareketini birlikte gösterir', LAC)
    return svg(600, 102, ic, 'Uzun 1. şerit ve kısa 2. şeritten oluşan tel maşalı Güneş-Dünya-Ay modeli.', 21)


def cap_hacim_karsilastirma_grafigi():
    ic = kutu(6, 6, 286, 88, TUR_A, TUR, 9, 1.4)
    ic += yazi(149, 25, 'Çap Karşılaştırması', TUR, kalin=True)
    ic += yazi(149, 50, 'Güneş’in çapı ≈ 109 × Dünya çapı', LAC, kalin=True)
    ic += yazi(149, 74, 'Dünya’nın çapı ≈ 4 × Ay çapı', LAC)

    ic += kutu(308, 6, 286, 88, MAVI_A, MAVI, 9, 1.4)
    ic += yazi(451, 25, 'Hacim Sıralaması', MAVI, kalin=True)
    ic += yazi(451, 50, 'Büyüklük: Güneş > Dünya > Ay', LAC, kalin=True)
    ic += yazi(451, 74, 'Dünya’nın içine ~64 Ay sığar', LAC)
    return svg(600, 100, ic, 'Güneş, Dünya ve Ay’ın çap ve hacim oranlarını karşılaştıran pano.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = nesne_model_kartlari()
    s[4]['gorsel'] = yorunge_hareket_sema()
    s[5]['gorsel'] = dort_hareket_karti()
    s[6]['gorsel'] = ay_es_zamanli_kart()
    s[7]['gorsel'] = sure_siralama_kartlari()
    s[8]['gorsel'] = zaman_hesap_karti()
    s[9]['gorsel'] = model_degerlendirme_panosu()
    s[11]['gorsel'] = tel_masali_model_duzenegi()
    s[12]['gorsel'] = cap_hacim_karsilastirma_grafigi()
