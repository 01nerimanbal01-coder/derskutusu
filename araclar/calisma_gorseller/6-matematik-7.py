"""6. sınıf Matematik 7. hafta (Kesir - Bölme İlişkisi, Sonlu ve Devirli Ondalık Gösterimler ile Yuvarlama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K, KUM = '#c9a227', '#8a5a2b', '#0f6b45', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def kesir(x, y, pay, payda, boy=11.2, renk=LAC):
    """Dikey kesir: pay üstte, çizgi, payda altta (K155)."""
    w = max(len(pay), len(payda)) * boy * 0.65 + 6
    return (yazi(x, y - 3, pay, boy, renk)
            + f'<line x1="{x - w / 2:.1f}" y1="{y + 1:.1f}" x2="{x + w / 2:.1f}" y2="{y + 1:.1f}" stroke="{renk}" stroke-width="1.4"/>'
            + yazi(x, y + boy + 2, payda, boy, renk))


def kesir_kartlari():
    kartlar = [
        ('1. Kart', '7', '20', MAVI, MAVI_A),
        ('2. Kart', '11', '8', YES, YES_A),
        ('3. Kart', '8', '9', TUR, TUR_A),
        ('4. Kart', '13', '25', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, pay, payda, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 11.2, renk)
        ic += f'<line x1="{x + 16}" y1="32" x2="{x + 120}" y2="32" stroke="{renk}" stroke-width="1"/>'
        ic += kesir(x + 68, 56, pay, payda, 11.8, LAC)
    return svg(600, 100, ic, 'Dört kesir kartı: 1. Kart 7 bölü 20, 2. Kart 11 bölü 8, 3. Kart 8 bölü 9, 4. Kart 13 bölü 25.', 22)


def zeytinyagi_paylasim():
    ic = f'<rect x="8" y="8" width="268" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(142, 26, 'Zeytinyağı Dolum Tankı', 11.4, YESIL_K)
    ic += yazi(142, 48, 'Toplam miktar: 18 litre', 11.0, LAC)
    ic += yazi(142, 68, 'Özdeş şişe sayısı: 8 adet', 10.6, LAC, ince=True)
    ic += yazi(142, 84, '(Her şişeye eşit miktarda yağ doluyor)', 10.1, YESIL_K, ince=True)

    ic += f'<line x1="282" y1="51" x2="306" y2="51" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="312" y="8" width="280" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(452, 26, 'Kesir ve Bölme İlişkisi', 11.4, TUR)
    ic += yazi(378, 58, '1 Şişe =', 11.2, LAC)
    ic += kesir(430, 54, '18', '8', 11.5, TUR)
    ic += yazi(505, 58, '= 18 ÷ 8 = ? L', 11.2, LAC)
    return svg(600, 102, ic, '18 litre zeytinyağının 8 özdeş şişeye eşit paylaştırılması ve 18 bölü 8 bölme işlemi.', 22)


def olcum_panosu():
    veriler = [
        ('1. Ölçüm', '14,638 g', MAVI, MAVI_A),
        ('2. Ölçüm', '27,384 g', YES, YES_A),
        ('3. Ölçüm', '9,847 g', TUR, TUR_A),
        ('4. Ölçüm', '35,492 g', MOR, MOR_A),
    ]
    ic = f'<rect x="6" y="6" width="588" height="92" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Hassas Terazi Ölçüm Kayıt Panosu', 11.4, LAC)
    for i, (bas, deger, renk, arka) in enumerate(veriler):
        x = 16 + i * 144
        ic += f'<rect x="{x}" y="34" width="132" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 66, 52, bas, 10.6, renk)
        ic += yazi(x + 66, 74, deger, 11.6, LAC)
    return svg(600, 104, ic, 'Dört hassas terazi ölçüm kaydı: 14,638 g, 27,384 g, 9,847 g ve 35,492 g.', 22)


def dijital_tarti_karti():
    ic = f'<rect x="8" y="8" width="284" height="86" rx="10" fill="{KUM}" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += yazi(150, 26, 'Dijital Tartı Ekranı (Gerçek Kütle)', 11.2, KAHVE)
    ic += f'<rect x="50" y="36" width="200" height="44" rx="6" fill="#1e293b" stroke="{LAC}" stroke-width="1.4"/>'
    ic += yazi(150, 64, '6,4a8 kg', 12.4, '#fde047')

    ic += f'<rect x="308" y="8" width="284" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(450, 26, 'Etiket Bilgisi (Yuvarlanmış)', 11.2, YESIL_K)
    ic += yazi(450, 50, 'Onda birler basamağına', 10.5, LAC, ince=True)
    ic += yazi(450, 68, 'yuvarlanmış kütle: 6,5 kg', 11.4, YESIL_K)
    ic += yazi(450, 84, '(4 rakamı 1 artarak 5 olmuştur)', 10.1, LAC, ince=True)
    return svg(600, 102, ic, 'Dijital tartıda 6,4a8 kg kavun ve onda birler basamağına yuvarlanmış 6,5 kg etiket bilgisi.', 22)


def bolme_adimlari_sema():
    adimlar = [
        ('13 ÷ 6 İşlemi', '13 = 2 × 6 + 1', '(Tam kısım 2, kalan 1)', MAVI, MAVI_A),
        ('Onda Birler', '10 ÷ 6 = 1 (kalan 4)', '(Virgül konur: 2,1...)', TUR, TUR_A),
        ('Yüzde Birler', '40 ÷ 6 = 6 (kalan 4)', '(6 sürekli tekrar eder)', MOR, MOR_A),
        ('Devir Gösterimi', '2,1666...', '(Yalnız 6 devreder)', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 10.9, renk)
        ic += yazi(x + 68, 50, s1, 10.5, LAC)
        ic += yazi(x + 68, 72, s2, 10.0, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 137}" y1="50" x2="{x + 147}" y2="50" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 100, ic, '13 bölü 6 kesrinin bölme yoluyla devirli ondalık gösterime dönüştürülme aşamaları.', 22)


def devirli_karsilastirma_kartlari():
    kartlar = [
        ('K Sayısı (Yalnız 5 Devirli)', 'Açık yazılışı: 3,4555...', 'Binde birler basamağı: 5', MAVI, MAVI_A),
        ('L Sayısı (45 Birlikte Devirli)', 'Açık yazılışı: 3,4545...', 'Binde birler basamağı: 4', TUR, TUR_A),
        ('M Sayısı (Sonlu Ondalık)', 'Açık yazılışı: 3,4500...', 'Binde birler basamağı: 0', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 196
        ic += f'<rect x="{x}" y="8" width="188" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 94, 26, bas, 10.6, renk)
        ic += f'<line x1="{x + 12}" y1="34" x2="{x + 176}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 94, 54, s1, 10.6, LAC)
        ic += yazi(x + 94, 74, s2, 10.2, LAC, ince=True)
    return svg(600, 100, ic, 'K = 3,4555..., L = 3,4545... ve M = 3,4500... sayılarının basamak açılımları.', 22)


def yuvarlama_sayi_dogrusu():
    ic = f'<rect x="6" y="6" width="588" height="90" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Yüzde Birler Basamağına Yuvarlandığında 4,76 Olan Sayı Aralığı', 11.2, LAC)
    ic += f'<line x1="50" y1="60" x2="550" y2="60" stroke="{LAC}" stroke-width="2.2"/>'
    ic += f'<rect x="140" y="52" width="320" height="16" rx="4" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.5"/>'
    noktalar = [
        (60, '4,750', GRI),
        (140, 'En küçük = ?', TUR),
        (300, '4,76 (Hedef)', MAVI),
        (460, 'En büyük = ?', TUR),
        (540, '4,770', GRI),
    ]
    for x, et, renk in noktalar:
        ic += f'<circle cx="{x}" cy="60" r="4.5" fill="{renk}"/>'
        ic += yazi(x, 82 if x in (140, 460) else 44, et, 10.4, renk)
    return svg(600, 102, ic, 'Sayı doğrusunda yüzde birlere yuvarlandığında 4,76 olan en küçük ve en büyük üç basamaklı ondalık gösterimler.', 22)


def devirli_yuvarlama_karti():
    ic = f'<rect x="8" y="8" width="584" height="84" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(300, 27, 'Devirli Ondalık Gösterimi Yuvarlama Kartı', 11.4, MOR)
    ic += yazi(300, 50, 'Verilen sayı: 5,3888... (Virgülden sonra 3 tekrar etmez, yalnız 8 devreder)', 10.6, LAC)
    ic += yazi(300, 72, 'İpucu: Önce devreden 8 rakamını birkaç kez yan yana aç, sonra sağdaki ilk rakama bak!', 10.2, MOR, ince=True)
    return svg(600, 100, ic, 'Yalnızca 8 rakamı devreden 5,3888... sayısının basamaklarını açarak yuvarlama bilgi kartı.', 22)


def alisveris_fisi_karti():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="{KUM}" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += yazi(300, 24, 'KIRTASİYE ALIŞVERİŞ FİŞİ · Yuvarlama ile Tahmin', 11.3, KAHVE)
    urunler = [
        ('1. Defter', '18,75 TL', MAVI, MAVI_A),
        ('2. Boya Seti', '32,40 TL', TUR, TUR_A),
        ('3. Kalem Kutusu', '24,85 TL', YES, YES_A),
    ]
    for i, (ad, fiyat, renk, arka) in enumerate(urunler):
        x = 18 + i * 190
        ic += f'<rect x="{x}" y="34" width="180" height="54" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 90, 52, ad, 10.8, renk)
        ic += yazi(x + 90, 74, f'Fiyat: {fiyat}', 11.0, LAC)
    return svg(600, 104, ic, 'Alışveriş fişi: Defter 18,75 TL, Boya seti 32,40 TL, Kalem kutusu 24,85 TL.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kesir_kartlari()
    s[4]['gorsel'] = zeytinyagi_paylasim()
    s[5]['gorsel'] = olcum_panosu()
    s[6]['gorsel'] = dijital_tarti_karti()
    s[7]['gorsel'] = bolme_adimlari_sema()
    s[8]['gorsel'] = devirli_karsilastirma_kartlari()
    s[9]['gorsel'] = yuvarlama_sayi_dogrusu()
    s[10]['gorsel'] = devirli_yuvarlama_karti()
    s[12]['gorsel'] = alisveris_fisi_karti()
