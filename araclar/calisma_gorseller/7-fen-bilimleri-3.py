"""7. sınıf Fen Bilimleri 3. hafta (Uzayda Neler Var? Yıldızların oluşumu ve yaşam döngüsü) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-12.5 pt (K150 EK); kesir yok (K155)."""

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


def yasam_yolu_sema():
    ic = f'<rect x="6" y="6" width="286" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Küçük Kütleli Yıldız (< 8 Güneş Kütlesi)', 11.0, YESIL_K)
    ic += yazi(20, 48, '1. Kırmızı dev evresi', 10.3, LAC, 'start', ince=True)
    ic += yazi(20, 68, '2. K = ?  →  3. Son basamak: L = ?', 10.6, YESIL_K, 'start')
    ic += yazi(20, 86, '(Demir ve karbondan oluşan yığın)', 10.1, LAC, 'start', ince=True)

    ic += f'<rect x="308" y="6" width="286" height="96" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Büyük Kütleli Yıldız (> 8 Güneş Kütlesi)', 11.0, TUR)
    ic += yazi(322, 48, '1. Kırmızı süperdev evresi', 10.3, LAC, 'start', ince=True)
    ic += yazi(322, 68, '2. Büyük patlama: M = ?', 10.6, TUR, 'start')
    ic += yazi(322, 86, '3. Nötron yıldızı ya da kara delik', 10.2, LAC, 'start', ince=True)
    return svg(600, 108, ic, 'İki yıldız grubunun yaşam yolu: Küçük kütlelide K ve L basamakları, büyük kütlelide M patlaması.', 17)


def bulutsu_panosu():
    kartlar = [
        ('1. Kart: Atbaşı Bulutsusu', 'Avcı Takımyıldızı’ndadır; şekli', 'denizatının başına benzer.', MAVI, MAVI_A),
        ('2. Kart: Orion Bulutsusu', 'Avcı Takımyıldızı’ndadır; gözlem', 'aracı olmadan rahatça görülür.', YES, YES_A),
        ('3. Kart: Tarantula Bulutsusu', 'Yalnızca en soğuk ve en küçük', 'kütleli yıldızları barındırır.', KIR, '#fdeaea'),
        ('4. Kart: Ortak Özellikleri', 'Hidrojen gazı ve tozdan oluşur;', 'yıldızların doğum bölgeleridir.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 10.6, renk, 'start')
        ic += yazi(x + 18, y + 33, s1, 9.8, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 45, s2, 9.8, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Bulutsu bilgi panosu: 1. Atbaşı, 2. Orion, 3. Tarantula (hatalı açıklama), 4. Ortak özellikler.', 18)


def kutle_grup_kartlari():
    kartlar = [
        ('1. Kart: Güneş', 'Başlangıç kütlesi:', '1 Güneş kütlesi', YES, YES_A),
        ('2. Kart: R Yıldızı', 'Başlangıç kütlesi:', '4 Güneş kütlesi', MAVI, MAVI_A),
        ('3. Kart: S Yıldızı', 'Başlangıç kütlesi:', '15 Güneş kütlesi', TUR, TUR_A),
        ('4. Kart: T Yıldızı', 'Başlangıç kütlesi:', '25 Güneş kütlesi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 25, bas, 10.6, renk)
        ic += f'<line x1="{x + 14}" y1="33" x2="{x + 122}" y2="33" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 53, s1, 10.0, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.5, LAC)
    return svg(600, 102, ic, 'Başlangıç kütleleri verilen dört yıldız kartı: Güneş (1), R (4), S (15) ve T (25 Güneş kütlesi).', 17)


def on_yildiz_gecis_sema():
    ic = f'<rect x="8" y="8" width="272" height="90" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(144, 26, 'Ön Yıldız Aşaması', 11.3, KIR)
    ic += f'<circle cx="44" cy="60" r="16" fill="{KIR}" opacity=".55" stroke="{KIR}" stroke-width="1.8"/>'
    ic += yazi(72, 52, 'Çöken bulut ısınır; donuk', 10.2, LAC, 'start', ince=True)
    ic += yazi(72, 68, 'kırmızı görünüm ortaya çıkar.', 10.2, LAC, 'start', ince=True)
    ic += yazi(72, 84, 'Henüz yıldız sayılmaz.', 10.3, KIR, 'start')

    ic += f'<line x1="286" y1="53" x2="314" y2="53" stroke="{LAC}" stroke-width="2.2"/><path d="M309 48 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'

    ic += f'<rect x="320" y="8" width="272" height="90" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(456, 26, 'Gerçek Yıldız Aşaması', 11.3, TUR)
    ic += f'<circle cx="356" cy="60" r="18" fill="{ALTIN}" stroke="{TUR}" stroke-width="2"/>'
    ic += yazi(386, 52, 'Sıcaklık yeterince yükselir.', 10.2, LAC, 'start', ince=True)
    ic += yazi(386, 68, 'Merkezde çekirdek tepkimeleri', 10.3, TUR, 'start')
    ic += yazi(386, 84, 'başlar ve yıldız doğar.', 10.2, LAC, 'start', ince=True)
    return svg(600, 106, ic, 'Ön yıldız ile gerçek yıldız aşamalarının karşılaştırma şeması.', 17)


def kucuk_kutle_zinciri():
    evr = [
        ('1. Evre', 'Bulutsuda çökme', MAVI, MAVI_A),
        ('2. Evre', 'Yıldızın doğuşu', TUR, TUR_A),
        ('3. Evre', 'Kırmızı dev', KIR, '#fdeaea'),
        ('4. Evre', 'Gezegenimsi bulut', MOR, MOR_A),
        ('5. Evre', 'Beyaz cüce', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(evr):
        x = 8 + i * 118
        ic += f'<rect x="{x}" y="10" width="102" height="76" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 51, 35, ust, 10.8, renk)
        ic += yazi(x + 51, 60, alt, 9.6, LAC, ince=True)
        if i < 4:
            ic += f'<line x1="{x + 111}" y1="48" x2="{x + 117}" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 96, ic, 'Küçük kütleli yıldızın yaşam yolundaki beş evre.', 17)


def kutle_omur_grafik():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 22, 'X, Y ve Z Yıldızlarının Başlangıç Kütleleri (Güneş Kütlesi Cinsinden)', 11.3, LAC)
    # Sol: sütun grafiği
    ic += f'<line x1="56" y1="30" x2="56" y2="92" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="56" y1="92" x2="340" y2="92" stroke="{LAC}" stroke-width="1.6"/>'
    # 8 Güneş kütlesi sınır çizgisi (y = 92 - 8*2.6 = 71.2)
    ic += f'<line x1="56" y1="71" x2="340" y2="71" stroke="{KIR}" stroke-width="1.4" stroke-dasharray="5 3"/>'
    ic += yazi(50, 74, '8', 10.2, KIR, 'end')
    barlar = [('X Yıldızı', 3, 96, YES), ('Y Yıldızı', 20, 184, TUR), ('Z Yıldızı', 10, 272, MAVI)]
    for ad, deger, bx, renk in barlar:
        bh = deger * 2.6
        by = 92 - bh
        ic += f'<rect x="{bx}" y="{by:.1f}" width="40" height="{bh:.1f}" rx="4" fill="{renk}"/>'
        ic += yazi(bx + 20, by - 4, f'{deger}', 10.4, LAC)
        ic += yazi(bx + 20, 104, ad, 10.4, LAC)
    # Sağda kural bilgi kutusu
    ic += f'<rect x="358" y="34" width="222" height="66" rx="8" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += yazi(469, 50, 'Kütle – Yaşam Süresi Kuralı', 10.8, KAHVE)
    ic += yazi(469, 68, 'Sınır: 8 Güneş kütlesi', 10.2, KIR)
    ic += yazi(469, 85, 'Kütle arttıkça ömür kısalır.', 10.2, LAC, ince=True)
    return svg(600, 116, ic, 'X (3), Y (20) ve Z (10 Güneş kütlesi) yıldızlarının başlangıç kütleleri sütun grafiği ve 8 Güneş kütlesi sınırı.', 18)


def yas_tahmin_gorseli():
    ic = f'<rect x="8" y="6" width="282" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 24, '1. Parlaklık ve Sıcaklık Grafiği', 11.0, MAVI)
    ic += f'<line x1="36" y1="86" x2="36" y2="34" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="36" y1="86" x2="264" y2="86" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<circle cx="110" cy="48" r="8" fill="{YES}"/>' + yazi(130, 52, 'M Yıldızı (Üst bölge)', 10.3, YESIL_K, 'start')
    ic += f'<circle cx="110" cy="74" r="8" fill="{TUR}"/>' + yazi(130, 78, 'N Yıldızı (Alt bölge)', 10.3, TUR, 'start')
    ic += yazi(150, 99, 'Sıcaklık / Parlaklık Bölgeleri', 10.0, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 24, '2. Dönme Hızı Gözlem Tablosu', 11.0, YESIL_K)
    ic += f'<rect x="326" y="36" width="250" height="26" rx="6" fill="#fff" stroke="{YES}" stroke-width="1.3"/>'
    ic += yazi(451, 53, 'M Yıldızı: Ekseninde hızlı döner', 10.4, YESIL_K)
    ic += f'<rect x="326" y="68" width="250" height="26" rx="6" fill="#fff" stroke="{TUR}" stroke-width="1.3"/>'
    ic += yazi(451, 85, 'N Yıldızı: Ekseninde yavaş döner', 10.4, TUR)
    return svg(600, 110, ic, 'M ve N yıldızlarının parlaklık-sıcaklık grafiğindeki bölgeleri ve dönme hızları.', 17)


def parlaklik_degisimi_grafik():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, '3. Yöntem: Yıldızda Parlaklık Değişimi – Zaman Grafiği', 11.3, LAC)
    ic += f'<line x1="68" y1="86" x2="68" y2="34" stroke="{LAC}" stroke-width="1.6"/>'
    ic += f'<line x1="68" y1="86" x2="360" y2="86" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(62, 44, 'Parlaklık', 9.6, LAC, 'end')
    ic += yazi(358, 98, 'Zaman', 9.8, LAC, 'end')
    ic += f'<path d="M74 62 Q98 34 122 62 T170 62 T218 62 T266 62 T314 62 T354 62" fill="none" stroke="{MAVI}" stroke-width="2.4"/>'
    ic += f'<rect x="378" y="34" width="198" height="56" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(477, 52, 'İç Titreşim Etkisi', 10.8, MAVI)
    ic += yazi(477, 70, 'Parlaklık dalgalanmasından', 10.1, LAC, ince=True)
    ic += yazi(477, 84, 'iç yapı ve yaş tahmin edilir.', 10.1, LAC, ince=True)
    return svg(600, 108, ic, 'Yıldızda iç titreşimler yüzünden oluşan parlaklık değişimi-zaman grafiği.', 17)


def iki_bulutsu_fark_karti():
    ic = f'<rect x="8" y="8" width="282" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, '1. Gözlem Notu · Bulutsu (Nebula)', 11.2, MAVI)
    ic += yazi(149, 49, 'Hidrojen gazı ve tozdan oluşan dev buluttur.', 10.2, LAC, ince=True)
    ic += yazi(149, 67, 'Hem küçük hem büyük kütleli yıldızların', 10.2, LAC, ince=True)
    ic += yazi(149, 83, 'yaşama başladığı doğum bölgesidir.', 10.3, MAVI)

    ic += f'<rect x="310" y="8" width="282" height="88" rx="10" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, '2. Gözlem Notu · Gezegenimsi Bulutsu', 11.2, MOR)
    ic += yazi(451, 49, 'Küçük kütleli yıldızın kırmızı dev', 10.2, LAC, ince=True)
    ic += yazi(451, 67, 'evresinden sonra geçtiği yaşlılık aşamasıdır.', 10.2, LAC, ince=True)
    ic += yazi(451, 83, 'Ardından geriye beyaz cüce kalır.', 10.3, MOR)
    return svg(600, 104, ic, 'Bulutsu (nebula) ile gezegenimsi bulutsu arasındaki görev farkını gösteren iki gözlem notu.', 17)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = yasam_yolu_sema()
    s[4]['gorsel'] = bulutsu_panosu()
    s[5]['gorsel'] = kutle_grup_kartlari()
    s[6]['gorsel'] = on_yildiz_gecis_sema()
    s[7]['gorsel'] = kucuk_kutle_zinciri()
    s[8]['gorsel'] = kutle_omur_grafik()
    s[9]['gorsel'] = yas_tahmin_gorseli()
    s[10]['gorsel'] = parlaklik_degisimi_grafik()
    s[12]['gorsel'] = iki_bulutsu_fark_karti()
