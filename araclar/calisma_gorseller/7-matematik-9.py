"""7. sınıf Matematik 9. hafta (Dikdörtgenler Prizmasının Yüzey Açınımı, Yüzey Alanı ve Hacmi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK); eğik kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def hediye_kutusu_prizma():
    ic = kutu(6, 6, 172, 78, MAVI_A, MAVI)
    ic += f'<rect x="30" y="30" width="84" height="42" fill="#93c5fd" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<polygon points="30,30 52,16 136,16 114,30" fill="#bfdbfe" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += f'<polygon points="114,30 136,16 136,58 114,72" fill="#60a5fa" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(72, 81, 'a = 5 cm', 9.5, LAC)
    ic += yazi(148, 68, 'b = 4 cm', 9.5, MAVI)
    ic += yazi(150, 38, 'c = 3 cm', 9.5, KIR)

    ic += kutu(184, 6, 170, 78, YES_A, YES)
    ic += yazi(269, 24, 'Hediye Kutusu Ölçüleri', 10.2, YES)
    ic += yazi(269, 46, 'Yüzey Alanı = 2·(ab + ac + bc)', 9.4, LAC, ince=True)
    ic += yazi(269, 68, 'Hacim (V) = a · b · c = ?', 9.8, YES)
    return svg(360, 90, ic, 'Ayrıtları 5 cm, 4 cm ve 3 cm olan dikdörtgenler prizması kutu.', 15)


def dort_prizma_boyut_karti():
    kartlar = [
        ('1. K Prizması', '4 × 3 × 2 br', MAVI, MAVI_A),
        ('2. L Prizması', '5 × 4 × 3 br', YES, YES_A),
        ('3. M Kare Prizma', '6 × 6 × 5 cm', TUR, TUR_A),
        ('4. N Küpü', '4 × 4 × 4 cm', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.5, LAC, ince=True)
    return svg(360, 82, ic, 'K, L, M ve N prizmalarının ayrıt uzunlukları kartları.', 14)


def prizma_acinim_es_yuzler():
    ic = kutu(6, 6, 210, 78, MAVI_A, MAVI)
    ic += kutu(76, 10, 44, 22, TUR_A, TUR, 2)
    ic += yazi(98, 25, '3', 10.0, TUR)
    ic += kutu(44, 32, 32, 26, YES_A, YES, 2)
    ic += yazi(60, 49, '1', 10.0, YES)
    ic += kutu(76, 32, 44, 26, MAVI_A, MAVI, 2)
    ic += yazi(98, 49, '2', 10.0, MAVI)
    ic += kutu(120, 32, 32, 26, YES_A, YES, 2)
    ic += yazi(136, 49, 'L', 10.0, YES)
    ic += kutu(152, 32, 44, 26, MAVI_A, MAVI, 2)
    ic += yazi(174, 49, 'M', 10.0, MAVI)
    ic += kutu(76, 58, 44, 22, TUR_A, TUR, 2)
    ic += yazi(98, 73, 'K', 10.0, TUR)

    ic += kutu(222, 6, 132, 78, MOR_A, MOR)
    ic += yazi(288, 24, 'Katlama Kuralı', 10.2, MOR)
    ic += yazi(288, 46, 'Birer yüz atlanarak', 9.4, LAC, ince=True)
    ic += yazi(288, 66, 'karşılıklı yüz bulunur', 9.4, MOR)
    return svg(360, 90, ic, 'Dikdörtgenler prizması açınımında 1, 2, 3 ve K, L, M yüzleri.', 15)


def eksik_birim_kup_kutusu():
    ic = kutu(6, 6, 172, 76, TUR_A, TUR)
    ic += yazi(92, 22, 'Prizma Boyutları', 10.2, TUR)
    ic += yazi(92, 44, 'Boy = 5 br · En = 3 br', 9.6, LAC, ince=True)
    ic += yazi(92, 64, 'Yükseklik = 4 br (4 katman)', 9.6, TUR)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, 'İçindeki Birim Küpler', 10.2, MAVI)
    ic += yazi(269, 44, 'Mevcut küp sayısı = 11 adet', 9.6, LAC, ince=True)
    ic += yazi(269, 64, 'Dolması için gereken = ?', 9.6, KIR)
    return svg(360, 88, ic, '5x3x4 birimlik kutuda mevcut 11 birim küp ve eksik küp hesabı.', 15)


def ustu_acik_akvaryum_karti():
    ic = kutu(6, 6, 348, 74, CAM_A, CAM)
    ic += yazi(180, 22, 'Üstü Açık Cam Akvaryum (5 Yüzeyli)', 10.4, CAM)
    ic += yazi(180, 44, 'Taban Ayrıtları: a = 8 dm,  b = 5 dm  ·  Yükseklik: c = 4 dm', 9.6, LAC, ince=True)
    ic += yazi(180, 65, '1 Alt Taban (a·b) + 4 Yan Cam Yüzey = ? dm²', 9.8, MAVI)
    return svg(360, 86, ic, 'Boyutları 8 dm, 5 dm ve 4 dm olan üstü açık cam akvaryum.', 14)


def kup_alan_hacim_seridi():
    adimlar = [
        ('1. Tüm Alan', '6 · a² = 216 cm²', MAVI, MAVI_A),
        ('2. Bir Yüz', 'a² = 36 cm²', YES, YES_A),
        ('3. Bir Ayrıt', 'a = 6 cm', TUR, TUR_A),
        ('4. Hacim', 'V = a³ = ? cm³', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += yazi(x + 41, 52, alt, 9.3, LAC, ince=True)
    return svg(360, 82, ic, 'Yüzey alanından küpün hacmine ulaşma işlem basamakları.', 14)


def koli_kup_yerlestirme_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Büyük Depolama Kolisi', 10.2, MAVI)
    ic += yazi(91, 43, 'Boyutlar: 16 cm × 12 cm × 8 cm', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'Küçük Küp Kutu: 2×2×2 cm', 9.4, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Doluluk Oranı', 10.2, YES)
    ic += yazi(269, 43, 'Kolinin dörtte üçü dolduruluyor', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'Yerleştirilen kutu adedi = ?', 9.5, KIR)
    return svg(360, 88, ic, '16x12x8 cm kolinin dörtte üçüne 2 cm ayrıtlı küp kutu yerleştirme.', 15)


def iki_prizma_hacim_alan_karti():
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI)
    ic += yazi(91, 22, 'A Prizması (6 × 4 × 2 br)', 10.2, MAVI)
    ic += yazi(91, 43, 'Hacmi: V = 6·4·2 = 48 br³', 9.5, LAC, ince=True)
    ic += yazi(91, 64, 'Yüzey Alanı = ? br²', 9.6, MAVI)

    ic += kutu(184, 6, 170, 74, TUR_A, TUR)
    ic += yazi(269, 22, 'B Prizması (4 × 4 × 3 br)', 10.2, TUR)
    ic += yazi(269, 43, 'Hacmi: V = 4·4·3 = 48 br³', 9.5, LAC, ince=True)
    ic += yazi(269, 64, 'Yüzey Alanı = ? br²', 9.6, TUR)
    return svg(360, 86, ic, 'Hacimleri 48 birimküp olan A ve B prizmalarının yüzey alanı karşılaştırması.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = hediye_kutusu_prizma()
    s[2]['gorsel'] = dort_prizma_boyut_karti()
    s[5]['gorsel'] = prizma_acinim_es_yuzler()
    s[6]['gorsel'] = eksik_birim_kup_kutusu()
    s[7]['gorsel'] = ustu_acik_akvaryum_karti()
    s[8]['gorsel'] = kup_alan_hacim_seridi()
    s[9]['gorsel'] = koli_kup_yerlestirme_karti()
    s[11]['gorsel'] = iki_prizma_hacim_alan_karti()
