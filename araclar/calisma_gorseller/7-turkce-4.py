"""7. sınıf Türkçe 4. hafta (Gençliğin Kıymeti: Hedef Sunumu, Öz Değerlendirme Yazısı ve Sebep-Sonuç Metin Yapısı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–13 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def duz(x, y, satirlar, boy=10.5, renk=LAC, hiza='start', ara=14):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def gorusme_tablosu():
    """Üç akran ve üç yetişkinin 5 yıllık hedef görüşme çizelgesi."""
    ic = kutu(4, 4, 172, 92, MAVI_A, MAVI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="172" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="172" height="10" fill="{MAVI}"/>'
    ic += yazi(90, 19, '3 Akranın 5 Yıllık Hedefleri', 11, '#fff')
    ic += duz(12, 42, [
        '• Bilim olimpiyatlarına katılmak',
        '• Müzik aleti çalmayı öğrenmek',
        '• Yüzme kursunu tamamlamak',
    ], 10.5, LAC, 'start', 16)

    ic += kutu(184, 4, 172, 92, TUR_A, TUR, 8, 1.3)
    ic += f'<rect x="184" y="4" width="172" height="22" rx="8" fill="{TUR}"/><rect x="184" y="16" width="172" height="10" fill="{TUR}"/>'
    ic += yazi(270, 19, '3 Yetişkinin 5 Yıllık Hedefleri', 11, '#fff')
    ic += duz(192, 42, [
        '• Mesleki uzmanlığı bitirmek',
        '• Müzik aleti çalmayı öğrenmek',
        '• Kendi atölyesini açmak',
    ], 10.5, LAC, 'start', 16)
    return svg(360, 100, ic, 'Görüşme çizelgesi: 3 akranın hedefleri bilim olimpiyatlarına katılmak, müzik aleti çalmayı öğrenmek, yüzme kursunu tamamlamak; 3 yetişkinin hedefleri mesleki uzmanlığı bitirmek, müzik aleti çalmayı öğrenmek, kendi atölyesini açmak.', 21)


def sema_kartlari():
    """Üç sebep-sonuç grafik düzenleyici şema kartı."""
    kartlar = [
        ('Bir sebep, çok sonuç', MAVI, MAVI_A, 4),
        ('Sebep-sonuç zinciri', MOR, MOR_A, 122),
        ('Çok sebep, bir sonuç', TUR, TUR_A, 240),
    ]
    ic = ''
    for i, (bas, r, z, x) in enumerate(kartlar):
        cx = x + 58
        ic += kutu(x, 4, 116, 86, z, r, 8, 1.3)
        ic += yazi(cx, 20, bas, 10.5, r)
        if i == 0:
            ic += kutu(x + 10, 42, 34, 20, '#fff', r, 5, 1.2) + yazi(x + 27, 55.5, 'S', 11, r)
            for k, dy in enumerate([28, 46, 64]):
                ic += f'<line x1="{x + 44}" y1="52" x2="{x + 68}" y2="{dy + 6}" stroke="{r}" stroke-width="1.4"/>'
                ic += kutu(x + 68, dy, 38, 14, '#fff', r, 4, 1.1) + yazi(x + 87, dy + 10.5, f'Sn{k + 1}', 10.5, LAC)
        elif i == 1:
            for k, etiket in enumerate(['S', 'Sn/S', 'Sn']):
                kx = x + 8 + k * 36
                ic += kutu(kx, 42, 30, 22, '#fff', r, 5, 1.2) + yazi(kx + 15, 56.5, etiket, 10.5, r)
                if k < 2:
                    ic += f'<line x1="{kx + 30}" y1="53" x2="{kx + 36}" y2="53" stroke="{r}" stroke-width="1.6"/>'
        else:
            for k, dy in enumerate([28, 46, 64]):
                ic += kutu(x + 10, dy, 38, 14, '#fff', r, 4, 1.1) + yazi(x + 29, dy + 10.5, f'S{k + 1}', 10.5, LAC)
                ic += f'<line x1="{x + 48}" y1="{dy + 7}" x2="{x + 72}" y2="52" stroke="{r}" stroke-width="1.4"/>'
            ic += kutu(x + 72, 42, 34, 20, '#fff', r, 5, 1.2) + yazi(x + 89, 55.5, 'Sn', 11, r)
    return svg(360, 94, ic, 'Üç grafik düzenleyici şema kartı: Bir sebep çok sonuç, Sebep-sonuç zinciri ve Çok sebep bir sonuç.', 20)


def kavram_kartlari():
    """Beş kavram rozet kartı (Ön bilgi, Amaca ulaşma, İçeriğin yeterliliği, Dilin anlaşılırlığı, Geçiş ifadeleri)."""
    ogeler = [
        ('Ön bilgi', MAVI, MAVI_A),
        ('Amaca ulaşma', YES, YES_A),
        ('İçeriğin yeterliliği', TUR, TUR_A),
        ('Dilin anlaşılırlığı', MOR, MOR_A),
        ('Geçiş ifadeleri', CAM, CAM_A),
    ]
    ic = ''
    for i, (ad, r, z) in enumerate(ogeler):
        x = 2 + i * 71
        cx = x + 35
        ic += kutu(x, 4, 69, 64, z, r, 7, 1.3)
        ic += f'<circle cx="{cx}" cy="24" r="10" fill="{r}"/>' + yazi(cx, 28, str(i + 1), 11, '#fff')
        parcalar = ad.split(' ')
        if len(parcalar) == 2:
            ic += yazi(cx, 46, parcalar[0], 10.5, LAC) + yazi(cx, 59, parcalar[1], 10.5, LAC)
        else:
            ic += yazi(cx, 52, ad, 10.5, LAC)
    return svg(358, 72, ic, 'Beş kavram kartı: 1 Ön bilgi, 2 Amaca ulaşma, 3 İçeriğin yeterliliği, 4 Dilin anlaşılırlığı, 5 Geçiş ifadeleri.', 19)


def zincir_semasi():
    """Sebep-sonuç zinciri şeması (1. halka -> K: ? -> 3. halka)."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    ic += yazi(180, 20, 'SEBEP-SONUÇ ZİNCİRİ ŞEMASI', 11.5, LAC)
    ic += kutu(10, 30, 102, 46, MAVI_A, MAVI, 7, 1.3)
    ic += yazi(61, 47, 'Düzenli doğa', 10.5, MAVI) + yazi(61, 62, 'yürüyüşü yapmak', 10.5, MAVI)
    ic += f'<line x1="114" y1="53" x2="126" y2="53" stroke="{SOLUK}" stroke-width="2"/>'
    ic += kutu(128, 30, 104, 46, MOR_A, MOR, 7, 1.5)
    ic += yazi(180, 47, 'K: ? (Sonuç ve', 10.5, MOR) + yazi(180, 62, 'sonraki sebep)', 10.5, MOR)
    ic += f'<line x1="234" y1="53" x2="246" y2="53" stroke="{SOLUK}" stroke-width="2"/>'
    ic += kutu(248, 30, 102, 46, TUR_A, TUR, 7, 1.3)
    ic += yazi(299, 47, 'İşleri yorulmadan', 10.5, TUR) + yazi(299, 62, 'tamamlamak', 10.5, TUR)
    return svg(360, 90, ic, 'Sebep-sonuç zinciri: Düzenli doğa yürüyüşü yapmak ok K soru işareti sonuç ve sonraki sebep ok İşleri yorulmadan tamamlamak.', 19)


def sunum_oz_yansitma():
    """Mert'in konuşmacı öz değerlendirme kartı."""
    ic = kutu(4, 4, 352, 86, CAM_A, CAM, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{CAM}"/><rect x="4" y="16" width="352" height="10" fill="{CAM}"/>'
    ic += yazi(180, 19, 'KONUŞMACI ÖZ DEĞERLENDİRME KARTI · Mert', 11, '#fff')
    ic += kutu(12, 32, 336, 24, YES_A, YES, 5, 1.1)
    ic += yazi(20, 48, 'Güçlü yön: Hedefleri tabloyla eksiksiz karşılaştırdım.', 10.5, LAC, 'start')
    ic += kutu(12, 60, 336, 24, KIR_A, KIR, 5, 1.1)
    ic += yazi(20, 76, 'Gelişmeye açık yön: Not kâğıdına baktım, göz teması kuramadım.', 10.5, LAC, 'start')
    return svg(360, 94, ic, 'Mert konuşmacı öz değerlendirme kartı: Güçlü yön hedefleri tabloyla eksiksiz karşılaştırdım; Gelişmeye açık yön not kâğıdına baktım, göz teması kuramadım.', 19)


def ifadeler_panosu():
    """Dört numaralı cümle fişi (sebep ve sonuç ifadeleri)."""
    fisler = [
        ('I. fiş', ['Düzenli kitap okuduğu için', 'dağarcığı zenginleşti.'], MAVI, MAVI_A),
        ('II. fiş', ['Planlı çalıştı; böylece', 'ödevini erken bitirdi.'], TUR, TUR_A),
        ('III. fiş', ['Soruları yazdı, dolayısıyla', 'verileri kolay topladı.'], YES, YES_A),
        ('IV. fiş', ['Prova yaptı; sonuç olarak', 'sahnede hiç takılmadı.'], MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, satirlar, r, z) in enumerate(fisler):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += f'<rect x="{x + 6}" y="{y + 6}" width="38" height="16" rx="4" fill="{r}"/>'
        ic += yazi(x + 25, y + 17.5, bas, 10, '#fff')
        ic += duz(x + 48, y + 17, satirlar, 10, LAC, 'start', 14)
    return svg(360, 96, ic, 'Dört cümle fişi: I. fiş okuduğu için, II. fiş böylece, III. fiş dolayısıyla, IV. fiş sonuç olarak.', 19)


def metin_bolumleri():
    """Sebep-sonuç metninin üç bölümü: Giriş, Gelişme, Sonuç."""
    ic = kutu(4, 4, 352, 76, '#fff', GRI, 8, 1.2)
    bolumler = [
        ('1. Giriş Bölümü', 'Konuya başlangıç', MAVI, MAVI_A, 12),
        ('2. Gelişme Bölümü', 'Sebep ve sonuçlar', TUR, TUR_A, 128),
        ('3. Sonuç Bölümü', 'Genel toparlama', YES, YES_A, 244),
    ]
    for bas, alt, r, z, x in bolumler:
        ic += kutu(x, 14, 104, 56, z, r, 7, 1.3)
        ic += yazi(x + 52, 34, bas, 11, r)
        ic += yazi(x + 52, 54, alt, 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Bilgilendirici metnin üç bölümü: 1. Giriş Bölümü, 2. Gelişme Bölümü, 3. Sonuç Bölümü.', 18)


def yazma_taslagi():
    """Kendini değerlendirme yazısı taslak planı (4 kutu)."""
    satirlar = [
        ('1. Paragraf:', 'Okuma alışkanlığı ölçütü (kendi yaşamımdan örnek)', MAVI, MAVI_A),
        ('2. Paragraf:', 'Zaman kullanımı ölçütü (komşumuzun çalışma planı)', TUR, TUR_A),
        ('3. Paragraf:', 'Sosyal sorumluluk ve yabancı dil ölçütleri bir arada', MOR, MOR_A),
        ('4. Adım:', 'Geçiş ifadeleri ile yazım ve noktalama denetimi', YES, YES_A),
    ]
    ic = kutu(4, 4, 352, 102, '#fff', GRI, 8, 1.2)
    for i, (bas, metin, r, z) in enumerate(satirlar):
        y = 10 + i * 23
        ic += kutu(12, y, 336, 20, z, r, 5, 1.1)
        ic += yazi(20, y + 14, bas, 10.5, r, 'start')
        ic += yazi(92, y + 14, metin, 10.5, LAC, 'start', True)
    return svg(360, 110, ic, 'Kendini değerlendirme yazısı taslak planı: 1. paragraf kendi yaşamımdan örnek, 2. paragraf komşumuzun çalışma planı, 3. paragraf iki ölçüt bir arada, 4. adım yazım ve noktalama denetimi.', 21)


def olcut_karti():
    """Okuma alışkanlığı edinme ölçüt kartı."""
    ic = kutu(4, 4, 352, 76, MAVI_A, MAVI, 8, 1.4)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="16" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 19, 'ÖLÇÜT LİSTESİ · 1. Madde', 11.5, '#fff')
    ic += yazi(180, 44, '“Okuma alışkanlığı edinerek bilgisini ve hayal dünyasını olgunlaştırmak”', 10.5, LAC)
    ic += yazi(180, 66, 'Son iki yıldaki durum · Kendi yaşamından örnek · Sebep-sonuç ifadesi', 10.5, MAVI, 'middle', True)
    return svg(360, 84, ic, 'Ölçüt listesi 1. madde: Okuma alışkanlığı edinerek bilgisini ve hayal dünyasını olgunlaştırmak.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = gorusme_tablosu()
    s[1]['gorsel'] = sema_kartlari()
    s[2]['gorsel'] = kavram_kartlari()
    s[3]['gorsel'] = zincir_semasi()
    s[4]['gorsel'] = sunum_oz_yansitma()
    s[5]['gorsel'] = ifadeler_panosu()
    s[8]['gorsel'] = metin_bolumleri()
    s[9]['gorsel'] = yazma_taslagi()
    s[12]['gorsel'] = olcut_karti()
