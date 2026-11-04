"""5. sınıf Fen Bilimleri 9. hafta (Basit Araç Gereçle Dinamometre Modeli Tasarlama, Esneklik Sınırı ve Ölçüm Hassasiyeti) çalışma kâğıdı görselleri.
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


def yay_son_boy_deneyi():
    kutular = [
        ('1. Yüksüz Yay', 'İlk Boy = 12 cm', 'Kuvvet = 0 N', MAVI, MAVI_A),
        ('2. 15 N Yük', 'Son Boy = 15 cm', 'Uzama = 3 cm', YES, YES_A),
        ('3. 45 N Yük', 'Son Boy = ? cm', 'Uzama = ? cm', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(kutular):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 23, bas, 10.3, r)
        ic += yazi(x + 56, 46, s1, 10.0, LAC)
        ic += yazi(x + 56, 67, s2, 9.8, LAC, ince=True)
    return svg(360, 88, ic, 'Serbest boyu 12 cm olan yayın 15 N ve 45 N yük altındaki boy değişimi.', 15)


def dort_dinamometre_hassasiyet():
    kartlar = [
        ('1. P Aracı', '10 N · 10 bölme', YES, YES_A),
        ('2. R Aracı', '20 N · 10 bölme', MAVI, MAVI_A),
        ('3. S Aracı', '50 N · 10 bölme', TUR, TUR_A),
        ('4. T Aracı', '100 N · 10 bölme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.4, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, '10 eşit bölmeli P, R, S ve T dinamometrelerinin kapasite kartları.', 15)


def malzeme_secim_kutulari():
    kutular = [
        ('1. Kutu', 'Tahta çubuk · Pamuk ip', KIR, KIR_A),
        ('2. Kutu', 'Sarmal yay · Şırınga · Cetvel', YES, YES_A),
        ('3. Kutu', 'Bakır tel · Oyun hamuru', TUR, TUR_A),
        ('4. Kutu', 'Keten bağ · Plastik boru', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, icerik, 9.6, LAC, ince=True)
    return svg(360, 94, ic, 'Dinamometre modeli için dört malzeme kutusu.', 16)


def iki_dinamometre_kamyon():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'K Dinamometresi', 10.4, MAVI)
    ic += yazi(91, 44, 'Kapasite: 30 N (10 bölme)', 9.9, LAC)
    ic += yazi(91, 65, '18 N Yük → ? bölme uzar', 9.8, MAVI, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'L Dinamometresi', 10.4, TUR)
    ic += yazi(269, 44, 'Kapasite: 60 N (10 bölme)', 9.9, LAC)
    ic += yazi(269, 65, '18 N Yük → ? bölme uzar', 9.8, TUR, ince=True)
    return svg(360, 88, ic, '30 N ve 60 N kapasiteli 10 bölmeli K ve L dinamometreleri.', 15)


def model_yenileme_kanit_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, '1. İlk Model (Kalın Yay)', 10.3, KIR)
    ic += yazi(91, 44, '100 N kapasiteli çelik yay', 9.8, LAC, ince=True)
    ic += yazi(91, 65, 'Kanıt: 2 N silgide uzamadı!', 9.8, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, '2. Yenilenen Model (?)', 10.3, YESIL_K)
    ic += yazi(269, 44, 'Hedef: 2 N silgiyi hassas ölçmek', 9.8, LAC, ince=True)
    ic += yazi(269, 65, 'Yay ve bölme nasıl değişmeli?', 9.8, YESIL_K)
    return svg(360, 88, ic, 'Kalın yaylı dinamometre modelini kanıta göre yenileme kartı.', 15)


def kalibrasyon_adim_kartlari():
    adimlar = [
        ('A', '0 N çizgisini işaretle', MAVI, MAVI_A),
        ('B', 'Özdeş yüklerle bölme çiz', TUR, TUR_A),
        ('C', 'Yayı ve kancayı tak', YES, YES_A),
        ('D', 'Farklı yüklerle test et', MOR, MOR_A),
    ]
    ic = ''
    for i, (kod, met, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, f'{kod} Adımı', 10.4, r)
        ic += yazi(x + 41, 55, met, 9.2, LAC, ince=True)
    return svg(360, 84, ic, 'Dinamometre modeli tasarım ve kalibrasyon basamakları.', 15)


def uc_yay_uzama_karsilastirma():
    yaylar = [
        ('X Yayı (İnce)', '10 N → 4 cm', '20 N → 8 cm', YES, YES_A),
        ('Y Yayı (Orta)', '10 N → 2 cm', '20 N → 4 cm', MAVI, MAVI_A),
        ('Z Yayı (Kalın)', '10 N → 1 cm', '20 N → 2 cm', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, r, z) in enumerate(yaylar):
        x = 6 + i * 118
        ic += kutu(x, 6, 112, 76, z, r)
        ic += yazi(x + 56, 22, bas, 10.2, r)
        ic += yazi(x + 56, 45, s1, 10.0, LAC)
        ic += yazi(x + 56, 66, s2, 10.0, LAC, ince=True)
    return svg(360, 88, ic, 'X, Y ve Z yaylarının 10 N ve 20 N kuvvet altındaki uzama miktarları.', 15)


def esneklik_siniri_asim_karti():
    ic = kutu(6, 6, 170, 76, KIR_A, KIR)
    ic += yazi(91, 22, '1. Aşama · Sınır Aşımı!', 10.3, KIR)
    ic += yazi(91, 44, 'Kapasite: En fazla 45 N', 9.9, LAC)
    ic += yazi(91, 65, 'Asılan Yük: 60 N demir gülle', 9.8, KIR)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '2. Aşama · Yeni Ölçüm', 10.3, TUR)
    ic += yazi(269, 44, 'Gülle çıkarılıp 15 N asıldı', 9.9, LAC)
    ic += yazi(269, 65, 'Sonuç: Hatalı değer gösterdi!', 9.8, TUR)
    return svg(360, 88, ic, '45 N kapasiteli dinamometreye 60 N yük asılması deneyi.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yay_son_boy_deneyi()
    s[2]['gorsel'] = dort_dinamometre_hassasiyet()
    s[5]['gorsel'] = malzeme_secim_kutulari()
    s[6]['gorsel'] = iki_dinamometre_kamyon()
    s[7]['gorsel'] = model_yenileme_kanit_karti()
    s[8]['gorsel'] = kalibrasyon_adim_kartlari()
    s[9]['gorsel'] = uc_yay_uzama_karsilastirma()
    s[11]['gorsel'] = esneklik_siniri_asim_karti()
