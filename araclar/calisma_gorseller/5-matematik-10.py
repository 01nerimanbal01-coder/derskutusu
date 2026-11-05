"""5. sınıf Matematik 10. hafta (Çok Basamaklı Doğal Sayılarda Basamak Değeri, Çözümleme ve Karşılaştırma) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def cozumleme_birlestirme_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'Basamak Birimleriyle Çözümlenmiş Doğal Sayı', 10.4, MOR)
    ic += yazi(180, 45, '(9 × 100 000 000) + (5 × 1 000 000) + (7 × 10 000)', 9.6, LAC)
    ic += yazi(180, 65, '+ (4 × 100) + (8 × 1)  →  Standart Yazılışı = ?', 9.7, MOR, ince=True)
    return svg(360, 88, ic, 'Çözümlenmiş dokuz basamaklı doğal sayının kartı.', 15)


def basamak_degeri_dort_kart():
    kartlar = [
        ('1. Rakam: 8', '864 259 137', MAVI, MAVI_A),
        ('2. Rakam: 6', '864 259 137', YES, YES_A),
        ('3. Rakam: 5', '864 259 137', TUR, TUR_A),
        ('4. Rakam: 9', '864 259 137', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sayi, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, sayi, 9.2, LAC, ince=True)
    return svg(360, 84, ic, '864 259 137 sayısında dört rakamın basamak incelemesi.', 15)


def iki_alti_farki_karti():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Aynı Rakamın Farklı Basamaklardaki Değer Farkı', 10.3, MAVI)
    ic += yazi(180, 46, 'Sayı:  4 [ 6 ] 2   1 9 [ 6 ]   3 8 0', 11.2, LAC)
    ic += yazi(180, 67, 'On milyonlardaki 6 ile binlerdeki 6’nın basamak değerleri farkı = ?', 9.3, MAVI, ince=True)
    return svg(360, 88, ic, '462 196 380 sayısındaki iki 6 rakamının basamak değerleri farkı.', 15)


def sembollu_karsilastirma_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Sol Taraf (Büyük Sayı)', 10.1, YESIL_K)
    ic += yazi(91, 45, '548  [ ▲ ] 32  910', 10.6, LAC)
    ic += yazi(91, 65, 'On binler basamağı: 3', 9.4, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Sağ Taraf (Küçük Sayı)', 10.1, TUR)
    ic += yazi(269, 45, '>   548  675  100', 10.6, LAC)
    ic += yazi(269, 65, 'Yüz binler: 6 · On binler: 7', 9.4, TUR, ince=True)
    return svg(360, 88, ic, '548 ▲32 910 > 548 675 100 eşitsizliğinde bilinmeyen rakam.', 15)


def yedi_rakam_dizilim_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'Verilen Yedi Rakam Kartı (Birer Kez Kullanılacak)', 10.3, CAM)
    ic += yazi(180, 46, '[ 0 ]   [ 2 ]   [ 3 ]   [ 5 ]   [ 6 ]   [ 8 ]   [ 9 ]', 11.0, LAC)
    ic += yazi(180, 67, '7 Basamaklı En Büyük Sayı = ?   |   7 Basamaklı En Küçük Sayı = ?', 9.3, CAM, ince=True)
    return svg(360, 88, ic, 'Yedi rakamla en büyük ve en küçük 7 basamaklı sayı oluşturma.', 15)


def dort_baraj_kapasite_kartlari():
    kartlar = [
        ('K Barajı', '68 450 900', '8 basamak', TUR, TUR_A),
        ('L Barajı', '680 120 500', '9 basamak', MAVI, MAVI_A),
        ('M Barajı', '680 190 000', '9 basamak', YES, YES_A),
        ('N Barajı', '684 005 300', '9 basamak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, sayi, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 22, bas, 10.2, r)
        ic += yazi(x + 41, 45, sayi, 9.1, LAC)
        ic += yazi(x + 41, 65, alt, 9.0, LAC, ince=True)
    return svg(360, 86, ic, 'K, L, M ve N barajlarının su kapasitesi sayıları.', 15)


def sayi_analiz_panosu_307m():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Sayı Analiz Panosu: 307 540 829', 10.5, MAVI)
    ic += yazi(180, 44, 'Milyonlar Bölüğü: 307  |  Binler Bölüğü: 540  |  Birler Bölüğü: 829', 9.6, LAC)
    ic += yazi(180, 65, 'Çözümleme: 300 000 000 + 7 000 000 + 500 000 + 40 000 + 800 + 20 + 9', 9.0, MAVI, ince=True)
    return svg(360, 88, ic, '307 540 829 sayısının bölük ve çözümleme panosu.', 15)


def iki_sayi_adim_karsilastirma():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Doğal Sayı', 10.2, MAVI)
    ic += yazi(91, 45, '715  4 [ 8 ] 2  300', 10.6, LAC)
    ic += yazi(91, 65, 'On binler basamağı = 8', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Doğal Sayı', 10.2, MOR)
    ic += yazi(269, 45, '715  4 [ 2 ] 8  900', 10.6, LAC)
    ic += yazi(269, 65, 'On binler basamağı = 2', 9.4, MOR, ince=True)
    return svg(360, 88, ic, '715 482 300 ve 715 428 900 sayılarının basamak karşılaştırması.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = cozumleme_birlestirme_karti()
    s[2]['gorsel'] = basamak_degeri_dort_kart()
    s[5]['gorsel'] = iki_alti_farki_karti()
    s[6]['gorsel'] = sembollu_karsilastirma_karti()
    s[7]['gorsel'] = yedi_rakam_dizilim_karti()
    s[8]['gorsel'] = dort_baraj_kapasite_kartlari()
    s[9]['gorsel'] = sayi_analiz_panosu_307m()
    s[11]['gorsel'] = iki_sayi_adim_karsilastirma()
