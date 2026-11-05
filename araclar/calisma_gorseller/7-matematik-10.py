"""7. sınıf Matematik 10. hafta (Dikdörtgenler Prizmasının Hacim Bağıntısı ve Standart Hacim Ölçme Birimleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def prizma_hacim_karti():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += f'<rect x="34" y="28" width="76" height="40" fill="#bfdbfe" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="34,28 54,14 130,14 110,28" fill="#dbeafe" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += f'<polygon points="110,28 130,14 130,54 110,68" fill="#93c5fd" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(72, 78, 'a = 7 cm', 9.2, MAVI)
    ic += yazi(146, 48, 'b = 4 cm', 9.0, YES)
    ic += yazi(20, 50, '5 cm', 9.0, KIR)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 24, 'Dikdörtgenler Prizması', 10.0, YES)
    ic += yazi(269, 45, 'Taban Ayrıtları: 7 cm ve 4 cm', 9.3, LAC, ince=True)
    ic += yazi(269, 65, 'Yükseklik: c = 5 cm · V = ?', 9.5, MAVI)
    return svg(360, 88, ic, 'Ayrıtları 7 cm, 4 cm ve 5 cm olan dikdörtgenler prizması.', 15)


def birim_donusum_kartlari():
    kartlar = [
        ('1. Kart', '5,2 m³ -> dm³', MAVI, MAVI_A),
        ('2. Kart', '90 000 cm³ -> dm³', YES, YES_A),
        ('3. Kart', '0,08 dm³ -> cm³', TUR, TUR_A),
        ('4. Kart', '14 000 mm³ -> cm³', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.6, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.8"/>'
        ic += yazi(x + 41, 54, alt, 8.9, LAC, ince=True)
    return svg(360, 82, ic, 'Standart hacim ölçme birimleri dönüşüm kartları.', 14)


def kare_prizma_yukseklik():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 24, 'Kare Prizma Bilgileri', 10.0, TUR)
    ic += yazi(91, 45, 'Taban Ayrıtları: a = 5 cm, b = 5 cm', 9.2, LAC, ince=True)
    ic += yazi(91, 65, 'Taban Alanı = 5 × 5 = 25 cm²', 9.4, TUR)

    ic += kutu(184, 6, 170, 76, MOR_A, MOR)
    ic += yazi(269, 24, 'Hacim ve Yükseklik', 10.0, MOR)
    ic += yazi(269, 45, 'Toplam Hacim (V) = 450 cm³', 9.3, LAC, ince=True)
    ic += yazi(269, 65, 'Yükseklik (h) = V ÷ Taban Alanı = ?', 9.3, KIR)
    return svg(360, 88, ic, 'Hacmi 450 cm³ ve taban ayrıtı 5 cm olan kare prizma.', 15)


def meyve_suyu_kutusu_svg():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, 'Meyve Suyu Kutusu', 10.0, YES)
    ic += yazi(91, 43, 'Boyutlar: 10 cm × 8 cm × 25 cm', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 'Hacim (cm³) = 10 · 8 · 25', 9.4, YES)

    ic += kutu(184, 6, 170, 76, CAM_A, CAM)
    ic += yazi(269, 22, 'Sıvı Ölçüsü Dönüşümü', 10.0, CAM)
    ic += yazi(269, 43, '1 000 cm³ = 1 dm³ = 1 Litre', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'Kapasite = ? Litre (L)', 9.5, KIR)
    return svg(360, 88, ic, '10 cm, 8 cm ve 25 cm boyutlarında meyve suyu kutusu.', 15)


def su_tanki_problemi():
    ic = kutu(6, 6, 170, 74, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Başlangıçtaki Su', 10.0, MAVI)
    ic += yazi(91, 44, 'Miktar = 3,2 m³', 9.5, LAC, ince=True)
    ic += yazi(91, 64, '(1 m³ = 1 000 dm³ = 1 000 L)', 9.1, MAVI)

    ic += kutu(184, 6, 170, 74, KIR_A, KIR)
    ic += yazi(269, 22, 'Kullanılan ve Kalan Su', 10.0, KIR)
    ic += yazi(269, 44, 'Harcanan = 700 dm³ (700 L)', 9.4, LAC, ince=True)
    ic += yazi(269, 64, 'Kalan Su = ? Litre', 9.5, KIR)
    return svg(360, 86, ic, 'Su tankında m³, dm³ ve litre dönüşüm problemi.', 14)


def akvaryum_cozum_adimlari():
    adimlar = [
        ('1. Taban Alanı', '40 × 30 cm²', MAVI, MAVI_A),
        ('2. Hacim (cm³)', 'Alan × 50 cm', TUR, TUR_A),
        ('3. Desimetreküp', '÷ 1 000 (dm³)', YES, YES_A),
        ('4. Kapasite (L)', '1 dm³ = 1 L', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.5, r)
        ic += yazi(x + 41, 52, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Akvaryumun litre kapasitesini bulma adımları.', 14)


def koli_kup_yerlestirme():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Büyük Dikdörtgen Koli', 10.0, MAVI)
    ic += yazi(91, 44, 'Ayrıtlar: 12 cm, 16 cm, 20 cm', 9.3, LAC, ince=True)
    ic += yazi(91, 64, 'VKoli = 12 · 16 · 20 cm³', 9.3, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, 'Küçük Küp Hediye Kutusu', 10.0, TUR)
    ic += yazi(269, 44, 'Bir ayrıtı: a = 4 cm', 9.3, LAC, ince=True)
    ic += yazi(269, 64, 'Küp Sayısı = (12÷4)·(16÷4)·(20÷4)', 9.0, KIR)
    return svg(360, 88, ic, '12x16x20 cm kolinin içine 4 cm ayrıtlı küp yerleştirme.', 15)


def esit_hacimli_prizma_kup():
    ic = kutu(6, 6, 170, 74, YES_A, YES)
    ic += yazi(91, 22, 'K Dikdörtgenler Prizması', 10.0, YES)
    ic += yazi(91, 43, 'Ayrıtlar: 9 cm, 4 cm ve 6 cm', 9.3, LAC, ince=True)
    ic += yazi(91, 63, 'VK = 9 · 4 · 6 = 216 cm³', 9.4, YES)

    ic += kutu(184, 6, 170, 74, MOR_A, MOR)
    ic += yazi(269, 22, 'L Küpü (VK = VL)', 10.0, MOR)
    ic += yazi(269, 43, 'Tüm ayrıtları eşit: a cm', 9.3, LAC, ince=True)
    ic += yazi(269, 63, 'VL = a³ = 216 cm³  →  a = ?', 9.4, KIR)
    return svg(360, 86, ic, 'Eşit hacimli K dikdörtgenler prizması ve L küpü.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = prizma_hacim_karti()
    s[2]['gorsel'] = birim_donusum_kartlari()
    s[5]['gorsel'] = kare_prizma_yukseklik()
    s[6]['gorsel'] = meyve_suyu_kutusu_svg()
    s[7]['gorsel'] = su_tanki_problemi()
    s[8]['gorsel'] = akvaryum_cozum_adimlari()
    s[9]['gorsel'] = koli_kup_yerlestirme()
    s[11]['gorsel'] = esit_hacimli_prizma_kup()
