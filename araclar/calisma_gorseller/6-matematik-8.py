"""6. sınıf Matematik 8. hafta (Kesir, Ondalık ve Yüzde Gösterimleriyle Dört İşlem Problemleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, ALTIN, KAHVE, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#c9a227', '#8a5a2b', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.5, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kesir(x, y, pay, payda, boy=12, renk=LAC):
    """Dikey kesir: pay üstte, yatay çizgi, payda altta (K155)."""
    w = max(len(pay), len(payda)) * boy * 0.65 + 6
    return (yazi(x, y - 4, pay, boy, renk)
            + f'<line x1="{x - w / 2:.1f}" y1="{y:.1f}" x2="{x + w / 2:.1f}" y2="{y:.1f}" stroke="{renk}" stroke-width="1.5"/>'
            + yazi(x, y + boy + 2, payda, boy, renk))


def serit_yol_diyagrami():
    ic = kutu(8, 6, 584, 96, KUM, GRI, 9, 1.5)
    ic += yazi(300, 23, '320 km Yolun Şerit Diyagram Modeli (8 Eş Parça)', 12, LAC)
    for i in range(8):
        x = 24 + i * 69
        if i < 2:
            renk, arka, et = MAVI, MAVI_A, '%25'
        elif i < 5:
            renk, arka, et = TUR, TUR_A, 'Gidilen'
        else:
            renk, arka, et = YES, YES_A, 'Kalan ?'
        ic += kutu(x, 34, 65, 36, arka, renk, 5, 1.4)
        ic += yazi(x + 32.5, 56, et, 12, renk)
    ic += yazi(300, 90, '1. Etap: %25 (2 parça)  ·  2. Etap: 8’de 3 (3 parça)  ·  Kalan: 3 parça = ? km', 12, LAC, ince=True)
    return svg(600, 108, ic, '320 km yolun 8 eş parçalı şerit diyagramı: 2 parça yüzde 25, 3 parça 8’de 3 ve kalan 3 parça.', 22)


def zeytinyagi_siseleme_karti():
    ic = kutu(8, 8, 284, 86, YES_A, YES, 9, 1.6)
    ic += kutu(8, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(150, 25, '1. Adım: Satılan ve Kalan Yağ', 12, '#fff')
    ic += yazi(115, 56, 'Toplam 36 L · Satılan:', 12, LAC, ince=True)
    ic += kesir(208, 52, '1', '4', 12, YES)
    ic += yazi(150, 82, 'Kalan yağ miktarı = ? L', 12, YES)

    ic += kutu(308, 8, 284, 86, TUR_A, TUR, 9, 1.6)
    ic += kutu(308, 8, 284, 26, TUR, TUR, 9, 1)
    ic += yazi(450, 25, '2. Adım: 0,75 L Şişelere Dolum', 12, '#fff')
    ic += yazi(450, 54, 'Her şişe: 0,75 L (yani %75 L)', 12, LAC, ince=True)
    ic += yazi(450, 78, 'Gereken şişe = Kalan ÷ 0,75 = ?', 12, TUR)
    return svg(600, 102, ic, '36 litre zeytinyağının dörtte biri satıldıktan sonra kalanının 0,75 litrelik şişelere doldurulması.', 22)


def magaza_indirim_panosu():
    kartlar = [
        ('1. Ceket: 600 TL', 'İndirim: %25 → 450 TL', MAVI, MAVI_A),
        ('2. Çanta: 400 TL', 'İndirim: %15 (0,15) → ? TL', YES, YES_A),
        ('3. Ayakkabı: 500 TL', 'İndirim: %20 → ? TL', TUR, TUR_A),
        ('4. Saat: 800 TL', 'İndirim: 0,3 (%30) → 560 TL', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 8 + (i % 2) * 296
        y = 6 + (i // 2) * 48
        ic += kutu(x, y, 288, 42, arka, renk, 8, 1.5)
        ic += yazi(x + 144, y + 18, bas, 12, renk)
        ic += yazi(x + 144, y + 35, alt, 12, LAC, ince=True)
    return svg(600, 104, ic, 'Dört ürünün etiket fiyatı ve indirim oranlarını gösteren mağaza panosu.', 22)


def su_deposu_karti():
    ic = kutu(8, 8, 584, 86, CAM_A, CAM, 9, 1.6)
    ic += kutu(8, 8, 584, 26, CAM, CAM, 9, 1)
    ic += yazi(300, 25, 'SU DEPOSU DOLULUK ORANI MODELİ', 12, '#fff')
    ic += yazi(118, 60, 'Başlangıç doluluk:', 12, LAC)
    ic += kesir(196, 56, '2', '5', 12, CAM)
    ic += yazi(250, 60, '(= %40)', 12, CAM)
    ic += yazi(438, 54, 'Eklenen: 90 L su → Yeni doluluk: %85', 12, LAC, ince=True)
    ic += yazi(438, 78, 'Fark: %85 − %40 = %45 → Tamamı = ? L', 12, LAC)
    return svg(600, 102, ic, 'Beşte ikisi dolu su deposuna 90 litre su eklenince yüzde 85 doluluk oranına ulaşması.', 22)


def polya_adimlari_sema():
    adimlar = [
        ('1. Problemi Anla', 'Verilen ve isteneni yaz', MAVI, MAVI_A),
        ('2. Strateji Seç', 'Ortak gösterim ve diyagram', YES, YES_A),
        ('3. Planı Uygula', 'Dört işlemleri gerçekleştir', TUR, TUR_A),
        ('4. Kontrol Et', 'Tahminle kıyasla ve genelle', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += kutu(x, 8, 138, 80, arka, renk, 8, 1.5)
        ic += kutu(x, 8, 138, 26, renk, renk, 8, 1)
        ic += yazi(x + 69, 25, bas, 12, '#fff')
        ic += yazi(x + 69, 60, alt, 12, LAC, ince=True)
    return svg(600, 96, ic, 'Polya’nın dört problem çözme adımını gösteren şema.', 22)


def manav_fisi_karti():
    ic = kutu(8, 6, 584, 92, KUM, KAHVE, 9, 1.6)
    ic += kutu(8, 6, 584, 26, KAHVE, KAHVE, 9, 1)
    ic += yazi(300, 24, 'MANAV ALIŞVERİŞ FİŞİ · Kasaya Verilen: 200 TL', 12, '#fff')
    ic += kutu(20, 38, 270, 52, YES_A, YES, 7, 1.4)
    ic += yazi(155, 56, 'Elma: 2,5 kg × 36,4 TL', 12, YES)
    ic += yazi(155, 78, 'Tutar = 91 TL', 12, LAC)
    ic += kutu(310, 38, 270, 52, TUR_A, TUR, 7, 1.4)
    ic += yazi(412, 56, 'Mandalina:', 12, TUR)
    ic += kesir(462, 52, '3', '2', 12, TUR)
    ic += yazi(522, 56, 'kg × 28 TL', 12, TUR)
    ic += yazi(445, 80, '(1,5 kg × 28 TL = 42 TL)', 12, LAC, ince=True)
    return svg(600, 104, ic, '2,5 kg elma ve 3 bölü 2 kg mandalina içeren manav alışveriş fişi.', 22)


def kalanin_kesri_karti():
    ic = kutu(8, 8, 584, 86, MOR_A, MOR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, MOR, MOR, 9, 1)
    ic += yazi(300, 25, 'ZEYNEP’İN HARÇLIK PLANI · Başlangıç: 480 TL', 12, '#fff')
    ic += yazi(135, 58, '1. Harcama: Tüm paranın', 12, LAC, ince=True)
    ic += kesir(228, 54, '1', '3', 12, MOR)
    ic += yazi(255, 58, '’ü', 12, LAC)
    ic += yazi(440, 54, '2. Harcama: Kalan paranın %25’i', 12, MOR)
    ic += yazi(440, 78, 'Son durumda geriye kalan = ? TL', 12, LAC)
    return svg(600, 102, ic, '480 TL harçlığın önce üçte birinin, sonra kalanın yüzde 25’inin harcanması şeması.', 22)


def zihinden_islem_karti():
    ic = kutu(8, 8, 284, 84, MAVI_A, MAVI, 9, 1.6)
    ic += kutu(8, 8, 284, 26, MAVI, MAVI, 9, 1)
    ic += yazi(150, 25, '1. Zihinden Strateji: 32 × 0,25', 12, '#fff')
    ic += yazi(125, 58, 'İpucu: 0,25 =', 12, LAC, ince=True)
    ic += kesir(184, 54, '1', '4', 12, MAVI)
    ic += yazi(222, 58, '(Çeyrek)', 12, MAVI)
    ic += yazi(150, 82, '32 ÷ 4 = ?', 12, LAC)

    ic += kutu(308, 8, 284, 84, YES_A, YES, 9, 1.6)
    ic += kutu(308, 8, 284, 26, YES, YES, 9, 1)
    ic += yazi(450, 25, '2. Zihinden Strateji: 15 ÷ 0,5', 12, '#fff')
    ic += yazi(425, 58, 'İpucu: 0,5 =', 12, LAC, ince=True)
    ic += kesir(480, 54, '1', '2', 12, YES)
    ic += yazi(518, 58, '(Yarım)', 12, YES)
    ic += yazi(450, 82, '15 × 2 = ?', 12, LAC)
    return svg(600, 100, ic, '0,25 ile çarpma ve 0,5’e bölme zihinden işlem strateji kartları.', 22)


def yuruyus_parkuru_panosu():
    ic = kutu(8, 8, 584, 86, TUR_A, TUR, 9, 1.6)
    ic += kutu(8, 8, 584, 26, TUR, TUR, 9, 1)
    ic += yazi(300, 25, 'YÜRÜYÜŞ PARKURU ETAP TABLOSU', 12, '#fff')
    ic += yazi(115, 58, 'Sabah: 0,35 (%35)', 12, LAC)
    ic += yazi(260, 58, '· Öğleden sonra:', 12, LAC, ince=True)
    ic += kesir(332, 54, '2', '5', 12, TUR)
    ic += yazi(378, 58, '(= %40)', 12, TUR)
    ic += yazi(495, 58, '· Kalan: 600 m', 12, YES)
    ic += yazi(300, 82, 'Toplam yürünen: %35 ve %40 → Kalan %25 = 600 m ise tamamı = ? m', 12, LAC, ince=True)
    return svg(600, 102, ic, 'Sabah 0,35’i, öğleden sonra 5’te 2’si yürünen ve 600 metresi kalan yürüyüş parkuru.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = serit_yol_diyagrami()
    s[4]['gorsel'] = zeytinyagi_siseleme_karti()
    s[5]['gorsel'] = magaza_indirim_panosu()
    s[6]['gorsel'] = su_deposu_karti()
    s[7]['gorsel'] = polya_adimlari_sema()
    s[8]['gorsel'] = manav_fisi_karti()
    s[9]['gorsel'] = kalanin_kesri_karti()
    s[11]['gorsel'] = zihinden_islem_karti()
    s[12]['gorsel'] = yuruyus_parkuru_panosu()
