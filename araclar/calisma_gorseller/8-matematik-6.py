"""8. sınıf Matematik 6. hafta (Kareköklü İfadeler: Tam kare sayılar ve karekökleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 9.5–11 pt (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=22):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kok_kutu(x, y, ic_metin, w_ic=34, renk=MAVI, yazi_renk=LAC):
    """Vektörel kök sembolü ve içindeki ifadeyi çizer."""
    p = f'<path d="M{x:.1f} {y - 4:.1f} L{x + 2.2:.1f} {y - 5.5:.1f} L{x + 5.5:.1f} {y + 2:.1f} L{x + 9.8:.1f} {y - 13.5:.1f} H{x + 11 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
    t = yazi(x + 11 + w_ic / 2, y, ic_metin, 10.2, yazi_renk)
    return p + t


def kare_modelleri():
    """Alanları 64, 121, 196 ve 289 cm2 olan dört kare modeli."""
    kareler = [
        ('64 cm²', 'Kenar = 8 cm', MAVI, MAVI_A, 12, 46),
        ('121 cm²', 'Kenar = ?', TUR, TUR_A, 92, 52),
        ('196 cm²', 'Kenar = ?', YES, YES_A, 178, 58),
        ('289 cm²', 'Kenar = ?', MOR, MOR_A, 272, 64),
    ]
    ic = kutu(4, 4, 352, 88, KUM, GRI, 8, 1.2)
    for alan, ken, r, z, x, boy in kareler:
        y = 70 - boy
        cx = x + boy / 2
        ic += kutu(x, y, boy, boy, z, r, 4, 1.5)
        ic += yazi(cx, y + boy / 2 + 4, alan, 9.8, r)
        ic += yazi(cx, 84, ken, 9.4, LAC)
    return svg(360, 96, ic, 'Alanları 64, 121, 196 ve 289 santimetrekare olan dört kare modeli.', 22)


def asal_carpan_kartlari():
    """Dört asal çarpan kartı (M kartında tek üs var)."""
    kartlar = [
        ('K Kartı', '2<tspan baseline-shift="super" font-size="75%">4</tspan> · 3<tspan baseline-shift="super" font-size="75%">2</tspan>', MAVI, MAVI_A, 4),
        ('L Kartı', '2<tspan baseline-shift="super" font-size="75%">2</tspan> · 5<tspan baseline-shift="super" font-size="75%">2</tspan> · 7<tspan baseline-shift="super" font-size="75%">2</tspan>', YES, YES_A, 92),
        ('M Kartı', '2<tspan baseline-shift="super" font-size="75%">3</tspan> · 3<tspan baseline-shift="super" font-size="75%">2</tspan> · 5<tspan baseline-shift="super" font-size="75%">1</tspan>', KIR, KIR_A, 180),
        ('N Kartı', '3<tspan baseline-shift="super" font-size="75%">4</tspan> · 11<tspan baseline-shift="super" font-size="75%">2</tspan>', MOR, MOR_A, 268),
    ]
    ic = ''
    for bas, ifd, r, z, x in kartlar:
        cx = x + 43
        ic += kutu(x, 4, 86, 72, z, r, 8, 1.3)
        ic += yazi(cx, 21, bas, 10, r)
        ic += kutu(x + 7, 29, 72, 34, '#fff', r, 6, 1.1)
        ic += f'<text x="{cx}" y="51" text-anchor="middle" font-size="10.2" {YAZI} fill="{LAC}">{ifd}</text>'
    return svg(358, 80, ic, 'Dört asal çarpan kartı: K, L, M ve N kartları.', 22)


def karekok_bilgi_panosu():
    """Tam kare, kök işlemi ve kare motif düğüm sayısı bilgi panosu."""
    ic = kutu(4, 4, 172, 80, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Kare ve Karekök İlişkisi', 9.8, MAVI)
    ic += yazi(90, 38, '14² = 196 ve (−14)² = 196', 9.2, LAC, 'middle', True)
    ic += yazi(90, 54, 'Motif: 16 · 16 = 256 düğüm', 9.2, LAC, 'middle', True)
    ic += yazi(90, 70, 'Negatif kök tam sayı olmaz', 9.2, MAVI, 'middle')

    ic += kutu(184, 4, 172, 80, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Uzaklık ve Yakınlık', 9.8, TUR)
    ic += yazi(270, 38, 'Önce kök içi işlem yapılır', 9.2, LAC, 'middle', True)
    ic += yazi(270, 54, '49 < 52 < 64 (7 ile 8 arası)', 9.2, LAC, 'middle', True)
    ic += yazi(270, 70, '52 − 49 = 3 → 7’ye yakın', 9.2, TUR, 'middle')
    return svg(360, 88, ic, 'Kare-karekök ilişkisi ve tam karelere yakınlık bilgi panosu.', 22)


def islem_kartlari():
    """A = kok(25 + 144) ve B = kok(36 + 64) işlem kartları."""
    ic = kutu(4, 4, 172, 74, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 20, '1. İşlem Kartı (A)', 10.2, MAVI)
    ic += kutu(18, 28, 144, 36, '#fff', MAVI, 6, 1.2)
    ic += yazi(44, 51, 'A =', 10.8, MAVI)
    ic += kok_kutu(62, 51, '25 + 144', 64, MAVI, LAC)

    ic += kutu(184, 4, 172, 74, YES_A, YES, 8, 1.4)
    ic += yazi(270, 20, '2. İşlem Kartı (B)', 10.2, YES)
    ic += kutu(198, 28, 144, 36, '#fff', YES, 6, 1.2)
    ic += yazi(224, 51, 'B =', 10.8, YES)
    ic += kok_kutu(242, 51, '36 + 64', 60, YES, LAC)
    return svg(360, 82, ic, 'A eşittir karekök içinde 25 artı 144 ve B eşittir karekök içinde 36 artı 64 işlem kartları.', 22)


def uzaklik_sayi_dogrusu():
    """8 ile 9 arasında kok(70) ve kok(77) sayı doğrusu modeli."""
    ic = kutu(4, 4, 352, 82, KUM, GRI, 8, 1.2)
    ic += f'<line x1="36" y1="44" x2="324" y2="44" stroke="{LAC}" stroke-width="2.2" stroke-linecap="round"/>'
    ic += f'<line x1="56" y1="36" x2="56" y2="52" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += yazi(56, 28, '8', 10.8, MAVI)
    ic += kok_kutu(36, 71, '64', 22, MAVI, MAVI)

    ic += f'<line x1="304" y1="36" x2="304" y2="52" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += yazi(304, 28, '9', 10.8, MAVI)
    ic += kok_kutu(284, 71, '81', 22, MAVI, MAVI)

    ic += f'<circle cx="144" cy="44" r="5" fill="{TUR}"/>'
    ic += kok_kutu(124, 28, '70', 22, TUR, TUR)
    ic += yazi(144, 71, '70 − 64 = 6', 9.4, LAC, 'middle', True)

    ic += f'<circle cx="240" cy="44" r="5" fill="{YES}"/>'
    ic += kok_kutu(220, 28, '77', 22, YES, YES)
    ic += yazi(236, 71, '81 − 77 = 4', 9.4, LAC, 'middle', True)
    return svg(360, 90, ic, '8 (karekök 64) ile 9 (karekök 81) arasında karekök 70 ve karekök 77 noktaları.', 22)


def yanyana_uc_kare():
    """K (81 cm2), L (144 cm2) ve M (225 cm2) yan yana kareler ve |AB| doğru parçası."""
    ic = kutu(4, 4, 352, 90, '#fff', GRI, 8, 1.2)
    ic += kutu(46, 28, 42, 42, MAVI_A, MAVI, 2, 1.5)
    ic += yazi(67, 47, 'K', 10.2, MAVI)
    ic += yazi(67, 61, '81 cm²', 9.2, LAC)

    ic += kutu(88, 16, 54, 54, TUR_A, TUR, 2, 1.5)
    ic += yazi(115, 40, 'L', 10.2, TUR)
    ic += yazi(115, 56, '144 cm²', 9.4, LAC)

    ic += kutu(142, 6, 64, 64, YES_A, YES, 2, 1.5)
    ic += yazi(174, 34, 'M', 10.2, YES)
    ic += yazi(174, 52, '225 cm²', 9.6, LAC)

    ic += f'<line x1="46" y1="76" x2="206" y2="76" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<circle cx="46" cy="76" r="3" fill="{KIR}"/><circle cx="206" cy="76" r="3" fill="{KIR}"/>'
    ic += yazi(36, 80, 'A', 10.2, KIR)
    ic += yazi(216, 80, 'B', 10.2, KIR)
    ic += yazi(284, 42, '|AB| = ?', 11, KIR)
    ic += yazi(284, 60, '(Kenarlar toplamı)', 9.4, SOLUK, 'middle', True)
    return svg(360, 98, ic, 'Yan yana dizilmiş 81, 144 ve 225 santimetrekare alanlı K, L, M kareleri ve AB alt kenarı.', 22)


def k_noktasi_sayi_dogrusu():
    """9 ile 10 arasında 10'a yakın K noktası sayı doğrusu."""
    ic = kutu(4, 4, 352, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 19, 'Sayı Doğrusunda K Noktasının Konumu', 10.2, MAVI)
    ic += f'<line x1="44" y1="49" x2="316" y2="49" stroke="{LAC}" stroke-width="2.2" stroke-linecap="round"/>'
    ic += f'<line x1="74" y1="41" x2="74" y2="57" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += yazi(74, 35, '9', 10.8, MAVI)
    ic += yazi(74, 69, '(Tam kare: 81)', 9.2, LAC, 'middle', True)

    ic += f'<line x1="286" y1="41" x2="286" y2="57" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += yazi(286, 35, '10', 10.8, MAVI)
    ic += yazi(286, 69, '(Tam kare: 100)', 9.2, LAC, 'middle', True)

    ic += f'<line x1="180" y1="45" x2="180" y2="53" stroke="{GRI}" stroke-width="1.5" stroke-dasharray="2 2"/>'
    ic += f'<circle cx="248" cy="49" r="5.5" fill="{KIR}"/>'
    ic += yazi(248, 35, 'K = ?', 10.5, KIR)
    return svg(360, 82, ic, '9 ile 10 arasında ve 10 sayısına daha yakın olan K noktası sayı doğrusu.', 22)


def aralik_kare_karton():
    """Kenarı 8 cm ile 9 cm arasında olan karesel karton modeli."""
    ic = kutu(4, 4, 352, 80, TUR_A, TUR, 8, 1.3)
    ic += kutu(20, 11, 64, 64, '#fff', TUR, 4, 1.6)
    ic += yazi(52, 40, 'Alan = A', 10, TUR)
    ic += yazi(52, 56, '(Doğal sayı)', 9.2, LAC, 'middle', True)
    ic += yazi(218, 25, 'Karesel Karton Bilgisi:', 10.2, TUR)
    ic += yazi(218, 45, 'Kenar uzunluğu: 8 cm < Kenar < 9 cm', 9.5, LAC, 'middle', True)
    ic += yazi(218, 64, '8² = 64 cm²  <  Alan (A)  <  9² = 81 cm²', 9.8, LAC)
    return svg(360, 88, ic, 'Kenar uzunluğu 8 cm ile 9 cm arasında olan doğal sayı alanlı karesel karton.', 22)


def tam_kare_carpan_karti():
    """540 sayısının asal çarpanlarına ayrılmış biçimi ve tam kare tamamlama kartı."""
    ic = kutu(4, 4, 352, 72, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 19, 'Asal Çarpanlarla Tam Kareye Tamamlama Kartı', 10.2, MOR)
    ic += kutu(16, 27, 328, 36, '#fff', MOR, 6, 1.2)
    ic += (f'<text x="180" y="50" text-anchor="middle" font-size="10.5" {YAZI} fill="{LAC}">'
           f'540 = 2<tspan baseline-shift="super" font-size="75%" fill="{YES}">2</tspan> · '
           f'3<tspan baseline-shift="super" font-size="75%" fill="{KIR}">3</tspan> · '
           f'5<tspan baseline-shift="super" font-size="75%" fill="{KIR}">1</tspan>'
           f'   →   540 · <tspan fill="{MAVI}">k</tspan> = Tam Kare Sayı</text>')
    return svg(360, 80, ic, '540 eşittir 2 üssü 2 çarpı 3 üssü 3 çarpı 5 üssü 1 asal çarpan kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kare_modelleri()
    s[1]['gorsel'] = asal_carpan_kartlari()
    s[3]['gorsel'] = karekok_bilgi_panosu()
    s[5]['gorsel'] = islem_kartlari()
    s[7]['gorsel'] = uzaklik_sayi_dogrusu()
    s[8]['gorsel'] = yanyana_uc_kare()
    s[9]['gorsel'] = k_noktasi_sayi_dogrusu()
    s[10]['gorsel'] = aralik_kare_karton()
    s[13]['gorsel'] = tam_kare_carpan_karti()
