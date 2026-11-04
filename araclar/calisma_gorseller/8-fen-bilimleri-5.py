"""8. sınıf Fen Bilimleri 5. hafta (DNA’nın Yapısı, Kendini Eşlemesi ve Kalıtımın Temel Kavramları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
ALTIN, KAHVE, YESIL_K, GRI, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#9aa6bd', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kedigeni_siralama_sema():
    """Soru 1: K > L > M > N (Kromozom > DNA > Gen > Nükleotid) şeması."""
    yapilar = [
        ('K (En Büyük)', 'Kromozom', MOR, MOR_A, 6),
        ('L (Yönetici)', 'DNA Sarmalı', MAVI, MAVI_A, 94),
        ('M (Görev Birimi)', 'Gen Bölgesi', TUR, TUR_A, 182),
        ('N (Yapı Birimi)', 'Nükleotid', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in yapilar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'Kalıtsal yapıların büyükten küçüğe K, L, M ve N olarak sıralanışı.', 13)


def bezelye_genotip_fenotip_karti():
    """Soru 2: Bezelyede çiçek ve tohum rengi baskın/çekinik kartları."""
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    ic += yazi(180, 20, 'Bezelyelerde Baskın ve Çekinik Allel Rehberi', KAHVE)
    ic += kutu(12, 28, 162, 52, MOR_A, MOR, 6, 1.2)
    ic += yazi(93, 46, 'Çiçek Rengi Karakteri', MOR)
    ic += yazi(93, 66, 'Mor (M) > Beyaz (m)', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 52, YES_A, YES, 6, 1.2)
    ic += yazi(267, 46, 'Tohum Rengi Karakteri', YESIL_K)
    ic += yazi(267, 66, 'Sarı (S) > Yeşil (s)', LAC, 'middle', True)
    return svg(360, 94, ic, 'Bezelyelerde mor-beyaz çiçek ve sarı-yeşil tohum baskınlık kartı.', 13)


def dna_onarim_hatalari_sema():
    """Soru 4: 4 farklı DNA hata bölümü."""
    bolumler = [
        ('1. Bölüm · Yanlış Eş', '[ T ] — [ G ] (Onarılır)', MAVI, MAVI_A),
        ('2. Bölüm · Tek Boşluk', '[ C ] — [ ? ] (Onarılır)', YES, YES_A),
        ('3. Bölüm · Çift Kopma', '[ ? ] — [ ? ] (Onarılamaz!)', KIR, KIR_A),
        ('4. Bölüm · Tek Boşluk', '[ A ] — [ ? ] (Onarılır)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(bolumler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'DNA zincirinde onarılabilen ve onarılamayan hataları gösteren şema.', 13)


def nukleotid_malzeme_kutusu():
    """Soru 5: DNA modeli malzeme sayıları kartı."""
    ic = kutu(4, 4, 352, 86, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(180, 20, 'DNA Modeli Tasarım Kutusu · Malzeme Sayıları', MAVI)
    kutular = [
        ('Fosfat & Şeker', '180 P · 150 Şeker', TUR, '#fff', 10),
        ('A ve T Bazları', '40 Adenin · 30 Timin', YES, '#fff', 126),
        ('G ve C Bazları', '50 Guanin · 60 Sitozin', MOR, '#fff', 242),
    ]
    for bas, alt, r, z, x in kutular:
        ic += kutu(x, 28, 108, 52, z, r, 6, 1.3)
        ic += yazi(x + 54, 47, bas, r)
        ic += yazi(x + 54, 67, alt, LAC, 'middle', True)
    return svg(360, 94, ic, 'DNA modeli için fosfat, şeker ve organik baz sayılarını gösteren kart.', 13)


def dna_esleme_kl_zincirleri():
    """Soru 7: 1. ve 2. zincirden oluşan K ve L yeni zincirleri."""
    ic = kutu(4, 4, 352, 88, '#f8fafc', GRI, 8, 1.3)
    ic += yazi(180, 20, 'DNA Eşlemesi: Eski (1, 2) ve Yeni (K, L) Zincirler', MAVI)
    ic += kutu(12, 28, 162, 54, MAVI_A, MAVI, 6, 1.3)
    ic += yazi(93, 46, '1. Yeni DNA Molekülü', MAVI)
    ic += yazi(93, 68, '1. Zincir + K (Yeni → 2 ile aynı)', LAC, 'middle', True)
    ic += kutu(186, 28, 162, 54, YES_A, YES, 6, 1.3)
    ic += yazi(267, 46, '2. Yeni DNA Molekülü', YESIL_K)
    ic += yazi(267, 68, 'L (Yeni → 1 ile aynı) + 2. Zincir', LAC, 'middle', True)
    return svg(360, 96, ic, 'DNA eşlenmesinde birinci ve ikinci zincirlerin karşısına yapılan K ve L zincirleri.', 13)


def replikasyon_dort_adim():
    """Soru 8: DNA replikasyonu 4 basamaklı akış."""
    adimlar = [
        ('1. Açılma', 'Bağlar kopar', MAVI, MAVI_A, 6),
        ('2. Giriş', 'Nükleotid çekirdekte', TUR, TUR_A, 94),
        ('3. Eşleşme', 'A-T ve G-C bağlanır', MOR, MOR_A, 182),
        ('4. Sonuç', '2 özdeş DNA oluşur', YES, YES_A, 270),
    ]
    ic = ''
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 6, 84, 74, z, r, 7, 1.4)
        ic += yazi(x + 42, 30, bas, r)
        ic += yazi(x + 42, 58, alt, LAC, 'middle', True)
    return svg(360, 86, ic, 'DNA’nın kendini eşlemesi sürecinin dört aşaması.', 13)


def mendel_bezelye_panosu():
    """Soru 9: Mendel'in bezelye seçimi 4 maddelik pano."""
    maddeler = [
        ('1. Madde', 'Hızlı ve kolay yetişir', YES, YES_A),
        ('2. Madde (!)', 'Hiç çeşitlilik göstermez', KIR, KIR_A),
        ('3. Madde', 'Yabancı tozlaşmaya kapalıdır', MAVI, MAVI_A),
        ('4. Madde', 'Çok sayıda zıt karakter taşır', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(maddeler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 42, z, r, 7, 1.3)
        ic += yazi(x + 86, y + 17, bas, r)
        ic += yazi(x + 86, y + 35, alt, LAC, 'middle', True)
    return svg(360, 98, ic, 'Gregor Mendel’in bezelye bitkisini tercih etme nedenleri panosu.', 13)


def kromozom_sayisi_tablo_karti():
    """Soru 12: İnsan (46), Moli balığı (46), Eğrelti otu (500) kromozom tablosu."""
    canlilar = [
        ('İnsan (2n)', '46 Kromozom', MAVI, MAVI_A, 6),
        ('Moli Balığı (2n)', '46 Kromozom', TUR, TUR_A, 126),
        ('Eğrelti Otu (2n)', '500 Kromozom', YES, YES_A, 246),
    ]
    ic = kutu(4, 4, 352, 86, KUM, ALTIN, 8, 1.4)
    for ad, sayi, r, z, x in canlilar:
        ic += kutu(x, 10, 108, 72, z, r, 7, 1.3)
        ic += yazi(x + 54, 32, ad, r)
        ic += yazi(x + 54, 60, sayi, LAC)
    return svg(360, 94, ic, 'İnsan, moli balığı ve eğrelti otunun kromozom sayılarını karşılaştıran kart.', 13)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kedigeni_siralama_sema()
    s[1]['gorsel'] = bezelye_genotip_fenotip_karti()
    s[3]['gorsel'] = dna_onarim_hatalari_sema()
    s[4]['gorsel'] = nukleotid_malzeme_kutusu()
    s[6]['gorsel'] = dna_esleme_kl_zincirleri()
    s[7]['gorsel'] = replikasyon_dort_adim()
    s[8]['gorsel'] = mendel_bezelye_panosu()
    s[11]['gorsel'] = kromozom_sayisi_tablo_karti()
