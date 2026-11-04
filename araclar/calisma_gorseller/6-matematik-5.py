"""6. sınıf Matematik 5. hafta (Deneysel Olasılıkta Tekrar Sayısı ve Ondalık Gösterimlerin Basamak Değerleri) çalışma kâğıdı görselleri.
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


def raptiye_tekrar_tablosu():
    kartlar = [
        ('10 Atış', 'Sivri Uç: 8 · Göreli: %80', MAVI, MAVI_A),
        ('50 Atış', 'Sivri Uç: 29 · Göreli: %58', TUR, TUR_A),
        ('200 Atış', 'Sivri Uç: 130 · Göreli: %65', MOR, MOR_A),
        ('500 Atış (En Güvenilir)', 'Sivri Uç: 320 · Göreli: %64 (0,64)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, '10, 50, 200 ve 500 raptiye atışında sivri ucun yukarı gelme göreli sıklıkları.', 21)


def basamak_tablosu_36_409():
    ic = kutu(6, 6, 588, 88, KUM, GRI, 9, 1.4)
    sutunlar = [
        ('Onlar', '3', '30', MAVI, MAVI_A),
        ('Birler', '6', '6', MAVI, MAVI_A),
        ('Virgül', ',', 'Tam|Ondalık', TUR, TUR_A),
        ('Onda 1', '4', '0,4', YES, YES_A),
        ('Yüzde 1', '0', '0', GRI, GRI_A),
        ('Binde 1', '9', '0,009', MOR, MOR_A),
    ]
    for i, (ad, rak, deg, renk, arka) in enumerate(sutunlar):
        x = 14 + i * 96
        ic += kutu(x, 12, 88, 76, arka, renk, 7, 1.4)
        ic += kutu(x, 12, 88, 24, renk, renk, 7, 1)
        ic += yazi(x + 44, 28, ad, '#fff', kalin=True)
        ic += yazi(x + 44, 54, rak, LAC, kalin=True)
        ic += yazi(x + 44, 78, deg, renk, kalin=True)
    return svg(600, 100, ic, '36,409 sayısının basamak adları, rakamları ve basamak değerleri şeması.', 21)


def sekiz_rakami_kartlari():
    kartlar = [
        ('1. Kart: 8,42', 'Virgülün solunda ilk basamak', MAVI, MAVI_A),
        ('2. Kart: 1,85', 'Virgülün sağında 1. basamak', YES, YES_A),
        ('3. Kart: 5,083', 'Virgülün sağında 2. basamak', TUR, TUR_A),
        ('4. Kart: 0,248', 'Virgülün sağında 3. basamak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört farklı ondalık gösterimde 8 rakamının konumunu gösteren kartlar.', 21)


def kapali_torba_bilye_karti():
    ic = kutu(6, 6, 286, 86, CAM_A, CAM, 9, 1.4)
    ic += kutu(6, 6, 286, 26, CAM, CAM, 9, 1)
    ic += yazi(149, 24, 'Kapalı Torba Bilgisi', '#fff', kalin=True)
    ic += yazi(149, 50, 'Toplam Bilye Sayısı: 40 adet', LAC, kalin=True)
    ic += yazi(149, 74, 'Renkler: Yalnız Kırmızı ve Mavi', CAM, kalin=True)

    ic += kutu(308, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(451, 24, '200 Çekiliş Deney Sonucu', '#fff', kalin=True)
    ic += yazi(451, 50, 'Kırmızı Sıklığı: 70 · Mavi: 130', LAC, kalin=True)
    ic += yazi(451, 74, 'Kırmızı Göreli Sıklık: 70 ÷ 200 = %35', KIR, kalin=True)
    return svg(600, 98, ic, '40 bilyeli kapalı torbadan yapılan 200 çekilişin sonuç kartı.', 21)


def bes_rakami_siralama_kartlari():
    kartlar = [
        ('K: 9,125', 'Binde birler (0,005)', MAVI, MAVI_A),
        ('L: 4,052', 'Yüzde birler (0,05)', YES, YES_A),
        ('M: 0,581', 'Onda birler (0,5)', TUR, TUR_A),
        ('N: 5,314', 'Birler basamağı (5)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Dört kartta 5 rakamının basamak değerlerini karşılaştıran şema.', 21)


def iki_kup_600_atis_karti():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += kutu(6, 6, 286, 26, YES, YES, 9, 1)
    ic += yazi(149, 24, 'K Küpü (600 Atış Sıklıkları)', '#fff', kalin=True)
    ic += yazi(149, 50, '1:98 · 2:102 · 3:99 · 4:101 · 5:97 · 6:103', LAC, kalin=True)
    ic += yazi(149, 74, 'Her yüz yaklaşık %16,7 (Dengeli)', YESIL_K, kalin=True)

    ic += kutu(308, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(308, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(451, 24, 'L Küpü (600 Atış Sıklıkları)', '#fff', kalin=True)
    ic += yazi(451, 50, '1:70 · 2:74 · 3:72 · 4:240 · 5:71 · 6:73', LAC, kalin=True)
    ic += yazi(451, 74, '4 yüzü: 240 ÷ 600 = %40 (Aşırı Yüksek!)', KIR, kalin=True)
    return svg(600, 98, ic, '600 kez atılan K ve L sayı küplerinin yüz sıklıklarını karşılaştıran kart.', 21)


def mert_sifir_hatasi_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += kutu(6, 6, 286, 26, KIR, KIR, 9, 1)
    ic += yazi(149, 24, 'Mert’in İddiası (!)', '#fff', kalin=True)
    ic += yazi(149, 50, '“0,705 sayısındaki 0’ı silersek', LAC, kalin=True)
    ic += yazi(149, 74, '0,75 olur, değer değişmez.”', KIR, kalin=True)

    ic += kutu(308, 6, 286, 86, MAVI_A, MAVI, 9, 1.4)
    ic += kutu(308, 6, 286, 26, MAVI, MAVI, 9, 1)
    ic += yazi(451, 24, 'Basamak Kontrolü', '#fff', kalin=True)
    ic += yazi(451, 50, '0,705 → 5 binde birler (0,005)', LAC, kalin=True)
    ic += yazi(451, 74, '0,75 → 5 yüzde birler (0,05)', MAVI, kalin=True)
    return svg(600, 98, ic, '0,705 ile 0,75 sayılarında yer tutucu sıfırın etkisini gösteren kart.', 21)


def alisveris_fisi_panosu():
    kartlar = [
        ('Kalem Kutusu: 45,80 TL', '45 TL + 80 kuruş (8 onda birlik)', MAVI, MAVI_A),
        ('Çanta Şeridi: 1,35 m', '1 m + 35 cm (35 yüzde birlik)', YES, YES_A),
        ('Elma Paketi: 2,065 kg', '2 kg + 65 g (65 binde birlik)', TUR, TUR_A),
        ('Silgi Etiketi: 9,05 TL', '9 TL + 5 kuruş (5 yüzde birlik)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Fiyat, uzunluk ve kütle etiketlerinin ondalık basamak yorumu panosu.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = raptiye_tekrar_tablosu()
    s[4]['gorsel'] = basamak_tablosu_36_409()
    s[5]['gorsel'] = sekiz_rakami_kartlari()
    s[6]['gorsel'] = kapali_torba_bilye_karti()
    s[7]['gorsel'] = bes_rakami_siralama_kartlari()
    s[8]['gorsel'] = iki_kup_600_atis_karti()
    s[10]['gorsel'] = mert_sifir_hatasi_karti()
    s[11]['gorsel'] = alisveris_fisi_panosu()
