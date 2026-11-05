"""5. sınıf Matematik 11. hafta (Doğal Sayılarla Dört İşlem, Zihinden İşlem ve Tahmin Stratejileri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kalanli_bolme_en_buyuk_karti():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 23, 'Kalanlı Bölme İşlemi Bağıntı Kartı', 10.5, MAVI)
    ic += yazi(180, 46, 'Bölünen (A) = ?   |   Bölen = 18   |   Bölüm = 30   |   Kalan = K', 9.9, LAC)
    ic += yazi(180, 67, 'Kural: A = (18 × 30) + K   ve   0 &lt; K &lt; 18  →  En büyük A = ?', 9.5, MAVI, ince=True)
    return svg(360, 88, ic, 'Bölenin 18, bölümün 30 olduğu kalanlı bölme kartı.', 15)


def dort_strateji_islem_kartlari():
    kartlar = [
        ('1. Bölme', '3 618 ÷ 18', MAVI, MAVI_A),
        ('2. Zihinden ×5', '72 × 5', YES, YES_A),
        ('3. Zihinden ×8', '35 × 8', TUR, TUR_A),
        ('4. Tahmin', '418 ÷ 7', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, islem, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, islem, 10.2, LAC)
    return svg(360, 84, ic, 'Bölme, zihinden çarpma ve tahmin işlem kartları.', 15)


def bolumde_sifir_dort_kart():
    kartlar = [
        ('1. Kart', '2 520 ÷ 12', MAVI, MAVI_A),
        ('2. Kart', '6 432 ÷ 32', YES, YES_A),
        ('3. Kart', '4 590 ÷ 15', TUR, TUR_A),
        ('4. Kart', '3 800 ÷ 19', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, islem, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, islem, 9.8, LAC)
    return svg(360, 84, ic, 'Dört farklı bölme işlemi kartı.', 15)


def elma_kasasi_paylastirma_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Hasat Edilen Elma', 10.3, YESIL_K)
    ic += yazi(91, 45, 'Toplam: 230 kg elma', 10.2, LAC)
    ic += yazi(91, 66, 'Tamamı kasalara konacak', 9.3, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'Kasa Kapasitesi', 10.3, TUR)
    ic += yazi(269, 45, '1 Kasa = En çok 12 kg', 10.2, LAC)
    ic += yazi(269, 66, 'Artan elma için +1 kasa!', 9.3, TUR, ince=True)
    return svg(360, 88, ic, '230 kg elmanın 12 kg kapasiteli kasalara paylaştırılması.', 15)


def magaza_yuvarlama_etiketleri():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1. Ürün · Dizüstü Bilgisayar', 10.1, MAVI)
    ic += yazi(91, 45, 'Fiyat: 28 640 TL', 10.5, LAC)
    ic += yazi(91, 66, 'En yakın binlik: ? TL', 9.4, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 22, '2. Ürün · Renkli Yazıcı', 10.1, MOR)
    ic += yazi(269, 45, 'Fiyat: 7 290 TL', 10.5, LAC)
    ic += yazi(269, 66, 'En yakın binlik: ? TL', 9.4, MOR, ince=True)
    return svg(360, 88, ic, 'Bilgisayar ve yazıcı fiyat etiketleri.', 15)


def zihinden_islem_siralama_kartlari():
    kartlar = [
        ('Kart K', '45 × 4', '(×2, ×2)', MAVI, MAVI_A),
        ('Kart L', '24 × 5', '(×10 ÷ 2)', YES, YES_A),
        ('Kart M', '1 500 ÷ 5', '(×2 ÷ 10)', TUR, TUR_A),
        ('Kart N', '30 × 8', '(×2, ×2, ×2)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 22, bas, 10.1, r)
        ic += yazi(x + 41, 44, s1, 10.2, LAC)
        ic += yazi(x + 41, 64, s2, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Dört zihinden işlem strateji kartı.', 15)


def fabrika_uretim_sevkiyat_panosu():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'Fabrika Aylık Üretim ve Kolileme Veri Panosu', 10.4, CAM)
    ic += yazi(180, 44, '• Ocak Üretimi: 425 600 adet   |   Şubat Üretimi: 384 400 adet', 9.7, LAC)
    ic += yazi(180, 65, '• A Tipi Koli: 24’lü (350 koli)   |   B Tipi Sevkiyat: 4 816 ürün ÷ 16’şarlı koli', 9.4, CAM, ince=True)
    return svg(360, 88, ic, 'Fabrika üretim ve kolileme veri panosu.', 15)


def tuna_bolme_hata_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, 'Tuna’nın Hatalı Çözümü', 10.2, KIR)
    ic += yazi(91, 45, '3 514 ÷ 7 = 52 (Yanlış!)', 10.3, KIR)
    ic += yazi(91, 66, '52 × 7 = 364 ≠ 3 514', 9.4, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Doğru Basamak Kontrolü', 10.2, YESIL_K)
    ic += yazi(269, 45, '35 ÷ 7 = 5  |  1’de 7 → ?', 10.1, LAC)
    ic += yazi(269, 66, 'Sonra 14 ÷ 7 = 2  →  Bölüm: ?', 9.4, YESIL_K, ince=True)
    return svg(360, 88, ic, '3 514 ÷ 7 işleminde bölümdeki sıfırın unutulması hatası.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kalanli_bolme_en_buyuk_karti()
    s[2]['gorsel'] = dort_strateji_islem_kartlari()
    s[5]['gorsel'] = bolumde_sifir_dort_kart()
    s[6]['gorsel'] = elma_kasasi_paylastirma_karti()
    s[7]['gorsel'] = magaza_yuvarlama_etiketleri()
    s[8]['gorsel'] = zihinden_islem_siralama_kartlari()
    s[9]['gorsel'] = fabrika_uretim_sevkiyat_panosu()
    s[11]['gorsel'] = tuna_bolme_hata_karti()
