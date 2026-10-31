"""8. sınıf Matematik 4. hafta (Sayıların Ondalık Gösterimini Çözümleme ve 10’un farklı kuvvetleriyle ifade etme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def us_yazi(x, y, katsayi, us, boy=11.5, renk=LAC):
    """katsayi · 10^us ifadesini SVG içinde temiz üst simgeyle yazar."""
    on = f'{katsayi} · 10' if katsayi else '10'
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="{boy}" {YAZI} fill="{renk}">'
            f'{on}<tspan baseline-shift="super" font-size="75%">{us}</tspan></text>')


def basamak_semasi():
    """64,295 sayısının basamak ve 10'un kuvveti kartları."""
    kolonlar = [
        ('6', 'Onlar', '1', MAVI, MAVI_A, 8),
        ('4', 'Birler', '0', YES, YES_A, 74),
        ('2', 'Onda bir', '−1', TUR, TUR_A, 152),
        ('9', 'Yüzde bir', '−2', TUR, TUR_A, 218),
        ('5', 'Binde bir', '−3', TUR, TUR_A, 284),
    ]
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    for rak, ad, u, r, z, x in kolonlar:
        ic += kutu(x, 10, 62, 74, z, r, 7, 1.3)
        ic += kutu(x + 15, 14, 32, 24, '#fff', r, 5, 1.2)
        ic += yazi(x + 31, 31, rak, 13, r)
        ic += yazi(x + 31, 52, ad, 10.5, LAC, 'middle', True)
        ic += us_yazi(x + 31, 74, '', u, 11.5, r)
    ic += yazi(143, 32, ',', 18, LAC)
    return svg(360, 94, ic, '64,295 sayısının basamak şeması: 6 onlar 10 üssü 1, 4 birler 10 üssü 0, 2 onda birler 10 üssü eksi 1, 9 yüzde birler 10 üssü eksi 2, 5 binde birler 10 üssü eksi 3.', 23)


def ogrenci_cozumleme_kartlari():
    """Dört numaralı çözümleme kartı (II. kartta 90,304 için hata var)."""
    kartlar = [
        ('I. kart · 408,065', '4·10<tspan baseline-shift="super" font-size="75%">2</tspan> + 8·10<tspan baseline-shift="super" font-size="75%">0</tspan> + 6·10<tspan baseline-shift="super" font-size="75%">−2</tspan> + 5·10<tspan baseline-shift="super" font-size="75%">−3</tspan>', MAVI, MAVI_A),
        ('II. kart · 90,304', '9·10<tspan baseline-shift="super" font-size="75%">1</tspan> + 3·10<tspan baseline-shift="super" font-size="75%">−1</tspan> + 4·10<tspan baseline-shift="super" font-size="75%">−2</tspan>', KIR, KIR_A),
        ('III. kart · 15,72', '1·10<tspan baseline-shift="super" font-size="75%">1</tspan> + 5·10<tspan baseline-shift="super" font-size="75%">0</tspan> + 7·10<tspan baseline-shift="super" font-size="75%">−1</tspan> + 2·10<tspan baseline-shift="super" font-size="75%">−2</tspan>', YES, YES_A),
        ('IV. kart · 600,08', '6·10<tspan baseline-shift="super" font-size="75%">2</tspan> + 8·10<tspan baseline-shift="super" font-size="75%">−2</tspan>', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ifd, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 10.5, r, 'start')
        ic += f'<text x="{x + 10}" y="{y + 33}" text-anchor="start" font-size="10.5" {YAZI} fill="{LAC}">{ifd}</text>'
    return svg(360, 96, ic, 'Dört çözümleme kartı: I. kart 408,065, II. kart 90,304, III. kart 15,72, IV. kart 600,08.', 23)


def tartim_etiketleri():
    """K, L ve M paketlerinin çözümlenmiş kütle etiketleri."""
    etiketler = [
        ('K Paketi (g)', '4·10<tspan baseline-shift="super" font-size="75%">1</tspan> + 7·10<tspan baseline-shift="super" font-size="75%">−1</tspan> + 5·10<tspan baseline-shift="super" font-size="75%">−2</tspan>', MAVI, MAVI_A, 4),
        ('L Paketi (g)', '4·10<tspan baseline-shift="super" font-size="75%">1</tspan> + 8·10<tspan baseline-shift="super" font-size="75%">0</tspan> + 2·10<tspan baseline-shift="super" font-size="75%">−3</tspan>', TUR, TUR_A, 178),
        ('M Paketi (g)', '4·10<tspan baseline-shift="super" font-size="75%">1</tspan> + 7·10<tspan baseline-shift="super" font-size="75%">0</tspan> + 9·10<tspan baseline-shift="super" font-size="75%">−2</tspan>', YES, YES_A, 352),
    ]
    ic = ''
    for bas, ifd, r, z, x in etiketler:
        ic += kutu(x, 4, 168, 76, z, r, 8, 1.3)
        ic += yazi(x + 84, 22, bas, 11.5, r)
        ic += kutu(x + 8, 30, 152, 40, '#fff', r, 6, 1.1)
        ic += f'<text x="{x + 84}" y="55" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">{ifd}</text>'
    return svg(524, 84, ic, 'K, L ve M paketlerinin çözümlenmiş gram cinsinden tartım etiketleri.', 22)


def virgul_kaydirma_semasi():
    """0,0185 · 10^3 = K ve 5400 · 10^-2 = L işlem şeması."""
    ic = kutu(4, 4, 352, 84, KUM, GRI, 8, 1.2)
    # Üst satır
    ic += kutu(14, 12, 86, 28, MAVI_A, MAVI, 6, 1.3) + yazi(57, 30, '0,0185', 11.5, LAC)
    ic += f'<line x1="104" y1="26" x2="236" y2="26" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += kutu(126, 14, 92, 24, '#fff', MAVI, 12, 1.2)
    ic += us_yazi(172, 30, '× 1', '3', 10.5, MAVI).replace('× 1 · 10', '× 10')
    ic += kutu(242, 12, 98, 28, MAVI_A, MAVI, 6, 1.4) + yazi(291, 30, 'K = ?', 12, MAVI)
    # Alt satır
    ic += kutu(14, 48, 86, 28, TUR_A, TUR, 6, 1.3) + yazi(57, 66, '5400', 11.5, LAC)
    ic += f'<line x1="104" y1="62" x2="236" y2="62" stroke="{TUR}" stroke-width="1.8"/>'
    ic += kutu(126, 50, 92, 24, '#fff', TUR, 12, 1.2)
    ic += us_yazi(172, 66, '× 1', '−2', 10.5, TUR).replace('× 1 · 10', '× 10')
    ic += kutu(242, 48, 98, 28, TUR_A, TUR, 6, 1.4) + yazi(291, 66, 'L = ?', 12, TUR)
    return svg(360, 92, ic, 'Virgül kaydırma şeması: 0,0185 çarpı 10 üssü 3 eşittir K; 5400 çarpı 10 üssü eksi 2 eşittir L.', 23)


def donusum_zinciri():
    """148,6 sayısının farklı 10 kuvvetleriyle yazılış zinciri."""
    ic = kutu(4, 4, 352, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 20, 'Aynı Sayının Farklı Kuvvetlerle Yazılışı (Değer = 148,6)', 11, MAVI)
    halkalar = [
        ('1,486', '2', 14),
        ('14,86', '1', 102),
        ('148,6', '0', 190),
        ('1486', '−1', 278),
    ]
    for i, (k, u, x) in enumerate(halkalar):
        ic += kutu(x, 30, 70, 36, '#fff', MAVI, 6, 1.2)
        ic += us_yazi(x + 35, 53, k, u, 10.5, LAC)
        if i < 3:
            ic += yazi(x + 79, 52, '=', 12, MAVI)
    return svg(360, 82, ic, '148,6 sayısının 10 üssü 2, 10 üssü 1, 10 üssü 0 ve 10 üssü eksi 1 ile eşdeğer yazılışları.', 22)


def olcum_kartlari():
    """Beş ölçüm kartı: 420·10^-3, 420·10^-2, 0,42·10^2, 0,042·10^4, 4,2·10^3."""
    kartlar = [
        ('Kart 1', '0,42', '2', MAVI, MAVI_A),
        ('Kart 2', '420', '−3', TUR, TUR_A),
        ('Kart 3', '4,2', '3', YES, YES_A),
        ('Kart 4', '420', '−2', MOR, MOR_A),
        ('Kart 5', '0,042', '4', CAM, CAM_A),
    ]
    ic = ''
    for i, (ad, k, u, r, z) in enumerate(kartlar):
        x = 4 + i * 71
        ic += kutu(x, 4, 67, 68, z, r, 7, 1.3)
        ic += yazi(x + 33.5, 21, ad, 10.5, r)
        ic += us_yazi(x + 33.5, 50, k, u, 10.5, LAC)
    return svg(358, 76, ic, 'Beş ölçüm kartı: 0,42 çarpı 10 üssü 2, 420 çarpı 10 üssü eksi 3, 4,2 çarpı 10 üssü 3, 420 çarpı 10 üssü eksi 2, 0,042 çarpı 10 üssü 4.', 22)


def denge_kartlari():
    """İki eşitlik denge kartı (x ve y bilinmeyenli)."""
    ic = kutu(4, 4, 172, 76, MAVI_A, MAVI, 8, 1.4)
    ic += yazi(90, 22, '1. Eşitlik Kartı', 11, MAVI)
    ic += f'<text x="90" y="52" text-anchor="middle" font-size="11.5" {YAZI} fill="{LAC}">1,25 · 10<tspan baseline-shift="super" font-size="75%">6</tspan> = 1250 · 10<tspan baseline-shift="super" font-size="75%" fill="{KIR}">x</tspan></text>'
    ic += yazi(90, 70, '(Virgül 3 basamak sağa)', 10.5, SOLUK, 'middle', True)

    ic += kutu(184, 4, 172, 76, TUR_A, TUR, 8, 1.4)
    ic += yazi(270, 22, '2. Eşitlik Kartı', 11, TUR)
    ic += f'<text x="270" y="52" text-anchor="middle" font-size="11.5" {YAZI} fill="{LAC}">8400 · 10<tspan baseline-shift="super" font-size="75%">−5</tspan> = <tspan fill="{KIR}">y</tspan> · 10<tspan baseline-shift="super" font-size="75%">−2</tspan></text>'
    ic += yazi(270, 70, '(Üs 3 arttı)', 10.5, SOLUK, 'middle', True)
    return svg(360, 84, ic, 'İki eşitlik kartı: 1,25 çarpı 10 üssü 6 eşittir 1250 çarpı 10 üssü x; 8400 çarpı 10 üssü eksi 5 eşittir y çarpı 10 üssü eksi 2.', 22)


def us_toplam_karti():
    """608,409 sayısının a, b, c, d üsleriyle çözümlenmesi kartı."""
    ic = kutu(4, 4, 352, 74, MOR_A, MOR, 8, 1.4)
    ic += yazi(180, 22, 'Çözümlemede Üsleri Bulma', 11.5, MOR)
    ic += kutu(14, 30, 332, 38, '#fff', MOR, 6, 1.2)
    ic += (f'<text x="180" y="54" text-anchor="middle" font-size="11.5" {YAZI} fill="{LAC}">'
           f'608,409 = 6·10<tspan baseline-shift="super" font-size="75%" fill="{KIR}">a</tspan> + '
           f'8·10<tspan baseline-shift="super" font-size="75%" fill="{MAVI}">b</tspan> + '
           f'4·10<tspan baseline-shift="super" font-size="75%" fill="{YES}">c</tspan> + '
           f'9·10<tspan baseline-shift="super" font-size="75%" fill="{TUR}">d</tspan></text>')
    return svg(360, 82, ic, '608,409 eşittir 6 çarpı 10 üssü a artı 8 çarpı 10 üssü b artı 4 çarpı 10 üssü c artı 9 çarpı 10 üssü d.', 22)


def sembollu_cozumleme_karti():
    """75,083 sayısının ▲ ve ■ sembollü çözümleme kartı."""
    ic = kutu(4, 4, 352, 74, YES_A, YES, 8, 1.4)
    ic += yazi(180, 22, 'Eksik Terimli Çözümleme Kartı', 11.5, YES)
    ic += kutu(14, 30, 332, 38, '#fff', YES, 6, 1.2)
    ic += (f'<text x="180" y="54" text-anchor="middle" font-size="11" {YAZI} fill="{LAC}">'
           f'75,083 = <tspan fill="{KIR}">▲</tspan>·10<tspan baseline-shift="super" font-size="75%">1</tspan> + '
           f'5·10<tspan baseline-shift="super" font-size="75%">0</tspan> + '
           f'<tspan fill="{MAVI}">■</tspan>·10<tspan baseline-shift="super" font-size="75%">−2</tspan> + '
           f'3·10<tspan baseline-shift="super" font-size="75%">−3</tspan></text>')
    return svg(360, 82, ic, '75,083 sayısının çözümlenmesinde üçgen çarpı 10 üssü 1 artı 5 çarpı 10 üssü 0 artı kare çarpı 10 üssü eksi 2 artı 3 çarpı 10 üssü eksi 3.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = basamak_semasi()
    s[2]['gorsel'] = ogrenci_cozumleme_kartlari()
    s[5]['gorsel'] = tartim_etiketleri()
    s[6]['gorsel'] = virgul_kaydirma_semasi()
    s[7]['gorsel'] = donusum_zinciri()
    s[8]['gorsel'] = olcum_kartlari()
    s[9]['gorsel'] = denge_kartlari()
    s[10]['gorsel'] = us_toplam_karti()
    s[13]['gorsel'] = sembollu_cozumleme_karti()
