"""6. sınıf Matematik 3. hafta (Asal Sayılar ve Asal Çarpanlar, Ortak Kat ve Ortak Bölen) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK; eğik kesir yok K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def carpan_agaci_algoritma_svg():
    ic = f'<rect x="8" y="6" width="282" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 22, 'Çarpan Ağacı (K Sayısı)', 11, MAVI)
    # Dallar
    ic += f'<line x1="120" y1="38" x2="80" y2="56" stroke="{LAC}" stroke-width="1.8"/><line x1="120" y1="38" x2="160" y2="56" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="160" y1="56" x2="130" y2="76" stroke="{LAC}" stroke-width="1.8"/><line x1="160" y1="56" x2="195" y2="76" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="195" y1="76" x2="170" y2="96" stroke="{LAC}" stroke-width="1.8"/><line x1="195" y1="76" x2="225" y2="96" stroke="{LAC}" stroke-width="1.8"/>'
    for cx, cy, m, r in [(120, 36, 'K', TUR), (80, 58, '2', YES), (160, 58, 'L', TUR), (130, 78, '3', YES), (195, 78, '15', MAVI), (170, 96, '3', YES), (225, 96, '5', YES)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        ic += yazi(cx, cy + 4, m, 10.5, r)

    ic += f'<rect x="310" y="6" width="282" height="106" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 22, 'Asal Çarpan Algoritması (84 Sayısı)', 11, TUR)
    ic += f'<line x1="446" y1="30" x2="446" y2="104" stroke="{LAC}" stroke-width="2"/>'
    sat = [('84', '2', LAC), ('42', '2', LAC), ('21', 'M', KIR), ('7', '7', LAC), ('1', '', LAC)]
    for i, (sol, sag, r) in enumerate(sat):
        y = 42 + i * 15
        ic += yazi(434, y, sol, 10.6, LAC, 'end')
        if sag:
            ic += yazi(460, y, sag, 10.8, r, 'start')
    return svg(600, 118, ic, 'Solda K sayısının çarpan ağacı (K=2xL, L=3x15, 15=3x5), sağda 84 sayısının asal çarpan algoritması.', 23)


def dikdortgen_zemin_modelleri():
    kartlar = [
        ('1. Kart: 5 Birimkare', 'Model: Yalnız 1 × 5', 'Yorum: 5 asal sayıdır.', YES, YES_A),
        ('2. Kart: 12 Birimkare', 'Model: 1 × 12, 2 × 6, 3 × 4', 'Yorum: 12 asal değildir.', MAVI, MAVI_A),
        ('3. Kart: 15 Birimkare', 'Model: Yalnız 1 × 15 çizilmiş', 'Yorum: 15 asal sayıdır.', KIR, '#fdeaea'),
        ('4. Kart: 13 Birimkare', 'Model: Yalnız 1 × 13', 'Yorum: 13 asal sayıdır.', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 6 + (i // 2) * 58
        ic += f'<rect x="{x}" y="{y}" width="286" height="50" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="50" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 19, f'{bas} ({s1})', 10.5, LAC, 'start')
        ic += yazi(x + 18, y + 38, s2, 10.4, renk, 'start', ince=True)
    return svg(600, 124, ic, 'Dört dikdörtgen zemin kartı: 5, 12, 15 (hatalı yorum) ve 13 birimkare modelleri.', 23)


def sayi_ciftleri_analiz_panosu():
    kartlar = [
        ('1. Kart', '12 ve 18', 'Ortak bölenler : ?', MAVI, MAVI_A),
        ('2. Kart', '8 ve 25', 'Ortak bölenler : ?', YES, YES_A),
        ('3. Kart', '16 ve 24', 'Ortak bölenler : ?', TUR, TUR_A),
        ('4. Kart', '9 ve 14', 'Ortak bölenler : ?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, cift, alt, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, cift, 11.5, LAC)
        ic += yazi(x + 68, 76, alt, 10.3, renk, ince=True)
    return svg(600, 100, ic, 'Dört sayı çifti kartı: 12 ve 18, 8 ve 25, 16 ve 24, 9 ve 14.', 22)


def sayi_dogrusu_ortak_kat():
    ic = f'<rect x="6" y="6" width="588" height="98" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    x0, w = 36, 528
    y = 56
    ic += f'<line x1="{x0}" y1="{y}" x2="{x0 + w}" y2="{y}" stroke="{LAC}" stroke-width="2"/>'
    # 3'er üst yaylar
    for k in range(10):
        a = x0 + k * 3 * (w / 30)
        b = x0 + (k + 1) * 3 * (w / 30)
        mx = (a + b) / 2
        ic += f'<path d="M{a:.1f} {y} Q{mx:.1f} {y - 22} {b:.1f} {y}" fill="none" stroke="{MAVI}" stroke-width="1.5"/>'
    # 5'er alt yaylar
    for k in range(6):
        a = x0 + k * 5 * (w / 30)
        b = x0 + (k + 1) * 5 * (w / 30)
        mx = (a + b) / 2
        ic += f'<path d="M{a:.1f} {y} Q{mx:.1f} {y + 24} {b:.1f} {y}" fill="none" stroke="{TUR}" stroke-width="1.6"/>'
    for n in range(0, 31, 3):
        px = x0 + n * (w / 30)
        ortak = n in (0, 15, 30)
        ic += f'<circle cx="{px:.1f}" cy="{y}" r="{4 if ortak else 2.2}" fill="{KIR if ortak else LAC}"/>'
        ic += yazi(px, y - 24 if n % 5 == 0 else y - 16, str(n), 10, KIR if ortak else LAC)
    for n in (5, 10, 20, 25):
        px = x0 + n * (w / 30)
        ic += f'<circle cx="{px:.1f}" cy="{y}" r="2.2" fill="{TUR}"/>'
        ic += yazi(px, y + 26, str(n), 10, TUR)
    ic += yazi(150, 94, 'Üst yaylar: 3’er sıçrama', 10.3, MAVI)
    ic += yazi(450, 94, 'Alt yaylar: 5’er sıçrama', 10.3, TUR)
    return svg(600, 110, ic, '0’dan 30’a kadar sayı doğrusunda üstten 3’er, alttan 5’er sıçramalar; 15 ve 30 ortak noktalardır.', 22)


def eratosten_kalburu_adimlari():
    adimlar = [
        ('2’nin Katları', '2’yi seç, katlarını çiz', MAVI, MAVI_A),
        ('3’ün Katları', '3’ü seç, katlarını çiz', MOR, MOR_A),
        ('5 ve 7’nin Katları', '5 ve 7’nin katlarını çiz', TUR, TUR_A),
        ('Kalan Asallar', '1’i ayır, 25 asalı bul', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11.2, renk)
        ic += yazi(x + 68, 62, alt, 10.3, LAC, ince=True)
    return svg(600, 96, ic, 'Eratosten kalburu adımları: 2’nin katları, 3’ün katları, 5 ve 7’nin katları, 1’i ayırıp 25 asalı belirleme.', 22)


def fidan_aralik_ortak_kat():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 24, '80 Metrelik Yürüyüş Yolu Planı (Başlangıç: 0. Metre)', 11.2, YESIL_K)
    ic += f'<rect x="30" y="34" width="540" height="26" rx="5" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(300, 51, 'Sol Kenar: Her 6 metrede bir aydınlatma direği (0, 6, 12, 18, 24, …)', 10.5, MAVI)
    ic += f'<rect x="30" y="66" width="540" height="26" rx="5" fill="#fff" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(300, 83, 'Sağ Kenar: Her 8 metrede bir dinlenme bankı (0, 8, 16, 24, 32, …)', 10.5, TUR)
    return svg(600, 108, ic, '80 metrelik yürüyüş yolu: sol kenarda 6 metrede bir direk, sağ kenarda 8 metrede bir bank.', 22)


def zeytinyagi_siseleri_ortak_bolen():
    ic = f'<rect x="8" y="6" width="584" height="96" rx="10" fill="#fffbe6" stroke="{ALTIN}" stroke-width="1.6"/>'
    ic += f'<rect x="28" y="20" width="110" height="68" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.8"/>'
    ic += yazi(83, 46, '1. Fıçı', 11.2, YESIL_K)
    ic += yazi(83, 68, '24 Litre', 12, LAC)
    ic += f'<rect x="160" y="14" width="120" height="74" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(220, 44, '2. Fıçı', 11.2, MAVI)
    ic += yazi(220, 68, '36 Litre', 12, LAC)
    ic += f'<rect x="310" y="20" width="264" height="68" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(442, 42, 'Eşit Hacimli Şişeler (? Litre)', 11, TUR)
    ic += yazi(442, 62, 'Yağlar birbirine karıştırılmayacak.', 10.3, LAC, ince=True)
    ic += yazi(442, 78, 'Fıçılarda hiç yağ artmayacak.', 10.3, LAC, ince=True)
    return svg(600, 108, ic, '24 litre ve 36 litre zeytinyağı fıçıları ile karıştırılmadan doldurulacak eşit hacimli şişeler.', 22)


def hatali_carpan_agaci_karti():
    ic = f'<rect x="8" y="6" width="584" height="98" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(145, 24, 'Kerem’in Çarpan Ağacı (72)', 11, KIR)
    ic += f'<line x1="120" y1="40" x2="80" y2="62" stroke="{LAC}" stroke-width="1.8"/><line x1="120" y1="40" x2="165" y2="62" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="165" y1="62" x2="135" y2="86" stroke="{LAC}" stroke-width="1.8"/><line x1="165" y1="62" x2="200" y2="86" stroke="{LAC}" stroke-width="1.8"/>'
    for cx, cy, m, r in [(120, 38, '72', LAC), (80, 62, '2', YES), (165, 62, '36', MAVI), (135, 86, '4', KIR), (200, 86, '9', KIR)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        ic += yazi(cx, cy + 4, m, 10.5, r)
    ic += f'<rect x="276" y="20" width="298" height="70" rx="8" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(425, 40, 'Kerem’in Sonuç Notu:', 10.8, KIR)
    ic += yazi(425, 60, '“Ağacın uçlarında 2, 4 ve 9 kaldığı için', 10.4, LAC, ince=True)
    ic += yazi(425, 78, '72’nin asal çarpanları 2, 4 ve 9’dur.”', 10.4, LAC, ince=True)
    return svg(600, 110, ic, 'Kerem’in 72 sayısını 2, 4 ve 9 uçlarında bıraktığı hatalı çarpan ağacı ve notu.', 22)


def asal_carpan_karsilastirma_karti():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 30, '1. Sayı Kartı: 30', 11.5, MAVI)
    ic += yazi(149, 54, 'Asal çarpan çarpımı : ?', 10.6, LAC, ince=True)
    ic += yazi(149, 74, 'Asal çarpan listesi : ?', 10.6, MAVI)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 30, '2. Sayı Kartı: 45', 11.5, TUR)
    ic += yazi(451, 54, 'Asal çarpan çarpımı : ?', 10.6, LAC, ince=True)
    ic += yazi(451, 74, 'Asal çarpan listesi : ?', 10.6, TUR)
    return svg(600, 102, ic, '30 ve 45 sayılarının asal çarpanlarının çarpımı ve ortak asal çarpanlarını karşılaştırma kartları.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = carpan_agaci_algoritma_svg()
    s[4]['gorsel'] = dikdortgen_zemin_modelleri()
    s[5]['gorsel'] = sayi_ciftleri_analiz_panosu()
    s[6]['gorsel'] = sayi_dogrusu_ortak_kat()
    s[7]['gorsel'] = eratosten_kalburu_adimlari()
    s[8]['gorsel'] = fidan_aralik_ortak_kat()
    s[9]['gorsel'] = zeytinyagi_siseleri_ortak_bolen()
    s[10]['gorsel'] = hatali_carpan_agaci_karti()
    s[12]['gorsel'] = asal_carpan_karsilastirma_karti()
