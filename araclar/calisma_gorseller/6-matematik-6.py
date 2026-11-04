"""6. sınıf Matematik 6. hafta (Ondalık Gösterimleri Çözümleme ve Kesir-Bölme İlişkisine Giriş) çalışma kâğıdı görselleri.
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


def karisik_basamak_kartlari():
    kutular = [
        ('1. Kart (Yüzde Birler)', '7 ÷ 100 (7 yüzde birlik)', MAVI, MAVI_A),
        ('2. Kart (Birler)', '8 tam (8 birlik)', TUR, TUR_A),
        ('3. Kart (Binde Birler)', '3 ÷ 1000 (3 binde birlik)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kutular):
        x = 6 + i * 198
        ic += kutu(x, 6, 192, 84, arka, renk, 8, 1.5)
        ic += yazi(x + 96, 26, bas, renk, kalin=True)
        ic += yazi(x + 96, 54, alt, LAC, kalin=True)
        ic += yazi(x + 96, 75, 'Onda birler basamağı: Boş (0)', LAC)
    return svg(600, 96, ic, 'Karışık sırada verilen birler, yüzde birler ve binde birler basamak kartları.', 21)


def esdegerlik_panosu():
    kartlar = [
        ('1. Kart', '4 onda birlik + 5 yüzde birlik', YES, YES_A),
        ('2. Kart', '45 yüzde birlik (45 ÷ 100)', MAVI, MAVI_A),
        ('3. Kart (!)', '4 onda birlik + 5 binde birlik', KIR, KIR_A),
        ('4. Kart', '450 binde birlik (450 ÷ 1000)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, '0,45 ondalık gösteriminin farklı çözümleme kartları.', 21)


def paylasim_genisletme_kartlari():
    kartlar = [
        ('1. 1 elma ÷ 4 kişi', 'Çarpan: ×25 → Payda 100', MAVI, MAVI_A),
        ('2. 9 L su ÷ 20 şişe', 'Çarpan: ×5 → Payda 100', YES, YES_A),
        ('3. 7 m ip ÷ 25 parça', 'Çarpan: ×4 → Payda 100', TUR, TUR_A),
        ('4. 3 kg un ÷ 8 paket', 'Çarpan: ×125 → Payda 1000', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört eşit paylaşım durumunun genişletme çarpanları kartları.', 21)


def zeytinyagi_market_etiketi():
    ic = kutu(6, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(149, 25, 'Net Hacim: 0,850 Litre', YESIL_K, kalin=True)
    ic += yazi(149, 50, '8 onda birlik + 5 yüzde birlik L', LAC, kalin=True)
    ic += yazi(149, 74, '(1 Litre = 1000 mililitre)', LAC)

    ic += kutu(308, 6, 286, 86, TUR_A, TUR, 9, 1.4)
    ic += yazi(451, 25, 'Satış Fiyatı: 145,60 TL', TUR, kalin=True)
    ic += yazi(451, 50, '145 tam lira + 60 yüzde birlik TL', LAC, kalin=True)
    ic += yazi(451, 74, '(1 TL = 100 kuruş)', LAC)
    return svg(600, 98, ic, '0,850 litre ve 145,60 TL yazılı zeytinyağı market etiketi.', 21)


def ondalik_siralama_kartlari():
    kartlar = [
        ('62 ÷ 1000', 'Binde 62 (0,062)', MAVI, MAVI_A),
        ('1 ÷ 4 (Çeyrek)', 'Yüzde 25 (0,250)', YES, YES_A),
        ('3 ÷ 5 (×2)', 'Onda 6 (0,600)', TUR, TUR_A),
        ('0,62 Sayısı', 'Yüzde 62 (0,620)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += kutu(x, 6, 140, 80, arka, renk, 8, 1.4)
        ic += kutu(x, 6, 140, 26, renk, renk, 8, 1)
        ic += yazi(x + 70, 24, bas, '#fff', kalin=True)
        ic += yazi(x + 70, 60, alt, LAC, kalin=True)
    return svg(600, 92, ic, 'Üç basamağa tamamlanarak karşılaştırılan dört sayı kartı.', 21)


def kurdele_paylasim_sema():
    ic = kutu(6, 6, 588, 86, KUM, GRI, 9, 1.4)
    ic += kutu(24, 20, 552, 26, TUR_A, TUR, 6, 1.5)
    ic += yazi(300, 38, 'Toplam Kurdele Uzunluğu: 11 metre → 4 Eş Parçaya Kesiliyor (11 ÷ 4)', TUR, kalin=True)
    ic += yazi(300, 68, 'Her parçaya: 2 tam metre + çeyrek metre (0,75 m) = 2,75 metre düşer', LAC, kalin=True)
    ic += yazi(300, 86, 'Kural: Bölünen (11) paya, bölen (4) paydaya yazılır.', MAVI)
    return svg(600, 98, ic, '11 metrelik kurdelenin 4 eş parçaya bölünmesi şeması.', 21)


def kaan_hata_analiz_karti():
    ic = kutu(6, 6, 286, 86, KIR_A, KIR, 9, 1.4)
    ic += yazi(149, 25, 'Kaan’ın Hatalı Çözümü (!)', KIR, kalin=True)
    ic += yazi(149, 52, '54 ÷ 1000 = 0,54', LAC, kalin=True)
    ic += yazi(149, 75, '(Virgülden sonra 2 basamak yazdı)', KIR)

    ic += kutu(308, 6, 286, 86, YES_A, YES, 9, 1.4)
    ic += yazi(451, 25, 'Basamak Tablosu İpucu', YESIL_K, kalin=True)
    ic += yazi(451, 52, 'Bölen 1000 → Sağda 3 basamak!', LAC, kalin=True)
    ic += yazi(451, 75, 'Onda birler: 0 · Yüzde birler: 5 · Binde birler: 4', LAC)
    return svg(600, 98, ic, '54 bölü 1000 işleminde Kaan’ın basamak kaydırma hatası kartı.', 21)


def yuzme_skorbord_panosu():
    kartlar = [
        ('1. Kulvar · Tuna', 'Süre: 28,4 s (28,40 s)', MAVI, MAVI_A),
        ('2. Kulvar · Emir', 'Süre: 28,35 s', TUR, TUR_A),
        ('3. Kulvar · Bora', 'Süre: 28,09 s (En kısa!)', YES, YES_A),
        ('4. Kulvar · Arda', 'Süre: 28,50 s', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.4)
        ic += yazi(x + 144, y + 18, bas, renk, kalin=True)
        ic += yazi(x + 144, y + 35, alt, LAC)
    return svg(600, 104, ic, 'Dört yüzücünün saniye cinsinden bitiriş derecelerini gösteren skorbord.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = karisik_basamak_kartlari()
    s[4]['gorsel'] = esdegerlik_panosu()
    s[5]['gorsel'] = paylasim_genisletme_kartlari()
    s[6]['gorsel'] = zeytinyagi_market_etiketi()
    s[7]['gorsel'] = ondalik_siralama_kartlari()
    s[8]['gorsel'] = kurdele_paylasim_sema()
    s[10]['gorsel'] = kaan_hata_analiz_karti()
    s[11]['gorsel'] = yuzme_skorbord_panosu()
