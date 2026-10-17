"""6. sınıf Fen Bilimleri 4. hafta (bileşke kuvvet) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048); görsel içi yazı sayfa puntosunda (K150 EK: 13 birim ≈ gövde, 12 ≈ tablo puntosu); kesir yok (K155).
Ölçek: 1 N = 20 birim (kareli zeminde 1 kare = 24 birim = 1 N)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'
N = 20  # 1 N uzunluğu


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=13, renk=LAC, hiza='start', ara=16):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def numara(x, y, n, renk=LAC, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4.3, str(n), 11.5, '#fff')


def ok(x1, y1, x2, y2, renk=MAVI, kalin=3, bas=9):
    """Kuvvet oku (yatay ya da dikey); uç üçgeni renkli."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    bx, by = x2 - bas * ux, y2 - bas * uy
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{kalin}" stroke-linecap="round"/>'
            f'<path d="M{bx + 5.5 * px:.1f} {by + 5.5 * py:.1f} L{x2:.1f} {y2:.1f} L{bx - 5.5 * px:.1f} {by - 5.5 * py:.1f} Z" fill="{renk}"/>')


def cisim(x, y, b, ad, renk=LAC, zemin=GRI_A):
    return kutu(x, y, b, b, zemin, renk, 4, 1.6) + yazi(x + b / 2, y + b / 2 + 5, ad, 13, renk)


def olcek(x, y, metin='1 N'):
    return (f'<line x1="{x}" y1="{y}" x2="{x + N}" y2="{y}" stroke="{SOLUK}" stroke-width="2"/>'
            f'<line x1="{x}" y1="{y - 4}" x2="{x}" y2="{y + 4}" stroke="{SOLUK}" stroke-width="1.5"/><line x1="{x + N}" y1="{y - 4}" x2="{x + N}" y2="{y + 4}" stroke="{SOLUK}" stroke-width="1.5"/>'
            + yazi(x + N + 6, y + 4.5, metin, 11.5, SOLUK, 'start'))


def pusula(x, y):
    return (f'<line x1="{x - 22}" y1="{y}" x2="{x + 22}" y2="{y}" stroke="{SOLUK}" stroke-width="1.2"/>'
            + yazi(x - 26, y + 4, 'B', 11, SOLUK, 'end') + yazi(x + 26, y + 4, 'D', 11, SOLUK, 'start'))


def kuvvet_ozellik():
    """K cismine tek kuvvet; 1 uygulama noktası, 2 yön (uç), 3 doğrultu (kesik çizgi), 4 büyüklük (uzunluk ayracı)."""
    ic = f'<line x1="20" y1="60" x2="340" y2="60" stroke="{MOR}" stroke-width="1.2" stroke-dasharray="6 4"/>'
    ic += cisim(70, 40, 40, 'K') + ok(110, 60, 230, 60, MAVI, 3.5, 10) + yazi(170, 50, 'F', 13, MAVI)
    ic += f'<circle cx="110" cy="60" r="4" fill="{KIR}"/>'
    ic += numara(110, 86, 1, KIR, 8) + f'<line x1="110" y1="66" x2="110" y2="78" stroke="{KIR}" stroke-width="1.2"/>'
    ic += numara(236, 34, 2, MAVI, 8) + f'<line x1="228" y1="52" x2="234" y2="42" stroke="{MAVI}" stroke-width="1.2"/>'
    ic += numara(312, 44, 3, MOR, 8) + f'<line x1="312" y1="52" x2="312" y2="59" stroke="{MOR}" stroke-width="1.2"/>'
    ic += (f'<line x1="110" y1="74" x2="230" y2="74" stroke="{YES}" stroke-width="1.5"/><line x1="110" y1="70" x2="110" y2="78" stroke="{YES}" stroke-width="1.5"/>'
           f'<line x1="230" y1="70" x2="230" y2="78" stroke="{YES}" stroke-width="1.5"/>') + numara(170, 90, 4, YES, 8)
    ic += olcek(262, 92) + pusula(44, 100)
    return svg(360, 110, ic, 'K cismine doğuya doğru çizilmiş tek bir kuvvet oku F. 1: okun çıktığı nokta (kırmızı). 2: okun ucu. 3: okun bulunduğu kesik çizgi. 4: okun uzunluğunu gösteren ayraç. Ölçek çubuğu 1 N; B batı, D doğu.', 28)


def dort_cisim():
    """Dört cisim, ikişer kuvvet: A aynı yön (doğu-doğu), B zıt yön (doğu-batı), C farklı doğrultu (kuzey-doğu), D zıt yön (kuzey-güney)."""
    ic = ''
    for i, h in enumerate('ABCD'):
        x = 4 + i * 89
        ic += kutu(x, 4, 85, 96, '#fff', GRI, 6, 1.1) + yazi(x + 12, 20, h, 13, LAC)
        cx, cy = x + 42, 54
        ic += cisim(cx - 11, cy - 11, 22, '', LAC, MAVI_A)
        if h == 'A':
            ic += ok(cx + 11, cy - 7, cx + 40, cy - 7, MAVI, 2.6, 8) + ok(cx + 11, cy + 7, cx + 40, cy + 7, YES, 2.6, 8)
        elif h == 'B':
            ic += ok(cx + 11, cy, cx + 40, cy, MAVI, 2.6, 8) + ok(cx - 11, cy, cx - 40, cy, YES, 2.6, 8)
        elif h == 'C':
            ic += ok(cx, cy - 11, cx, cy - 38, MAVI, 2.6, 8) + ok(cx + 11, cy, cx + 40, cy, YES, 2.6, 8)
        else:
            ic += ok(cx, cy - 11, cx, cy - 38, MAVI, 2.6, 8) + ok(cx, cy + 11, cx, cy + 38, YES, 2.6, 8)
    return svg(360, 104, ic, 'Dört kart. A: cisme doğuya doğru iki ok. B: cisme biri doğuya, biri batıya iki ok. C: cisme biri kuzeye, biri doğuya iki ok. D: cisme biri kuzeye, biri güneye iki ok.', 27)


def ayni_yon():
    """K cismine doğu yönünde F1 = 4 N ve F2 = 3 N."""
    ic = cisim(40, 30, 40, 'K') + ok(80, 42, 80 + 4 * N, 42, MAVI, 3.5, 10) + ok(80, 58, 80 + 3 * N, 58, YES, 3.5, 10)
    ic += yazi(80 + 4 * N + 8, 46, 'F1 = 4 N', 12.5, MAVI, 'start') + yazi(80 + 3 * N + 8, 62, 'F2 = 3 N', 12.5, YES, 'start')
    ic += olcek(262, 44) + pusula(306, 78)
    return svg(360, 90, ic, 'K cismine aynı noktadan doğuya doğru iki ok: F1 = 4 N (uzun), F2 = 3 N (daha kısa). Ölçek çubuğu 1 N; B batı, D doğu.', 22)


def zit_yon():
    """L cismine batı yönünde F1 = 6 N, doğu yönünde F2 = 2 N."""
    ic = cisim(150, 24, 40, 'L') + ok(150, 44, 150 - 6 * N, 44, MAVI, 3.5, 10) + ok(190, 44, 190 + 2 * N, 44, YES, 3.5, 10)
    ic += yazi(90, 32, 'F1 = 6 N', 12.5, MAVI) + yazi(236, 36, 'F2 = 2 N', 12.5, YES, 'start')
    ic += olcek(262, 76) + pusula(44, 78)
    return svg(360, 88, ic, 'L cismine batıya doğru uzun bir ok F1 = 6 N, doğuya doğru kısa bir ok F2 = 2 N. Ölçek çubuğu 1 N; B batı, D doğu.', 22)


def kareli():
    """Kareli zemin (1 kare = 1 N): K cismine doğu 5 kare, batı 2 kare."""
    k = 24
    ic = f'<rect x="12" y="8" width="{14 * k}" height="{4 * k}" fill="#fff" stroke="{GRI}" stroke-width="1"/>'
    ic += ''.join(f'<line x1="{12 + i * k}" y1="8" x2="{12 + i * k}" y2="{8 + 4 * k}" stroke="{GRI_A}" stroke-width="1"/>' for i in range(1, 14))
    ic += ''.join(f'<line x1="12" y1="{8 + j * k}" x2="{12 + 14 * k}" y2="{8 + j * k}" stroke="{GRI_A}" stroke-width="1"/>' for j in range(1, 4))
    cx = 12 + 5 * k
    ic += cisim(cx, 8 + k + 1, k - 2, 'K') + ok(cx + k - 1, 8 + 1.5 * k, cx + k - 1 + 5 * k, 8 + 1.5 * k, MAVI, 3.5, 10)
    ic += ok(cx, 8 + 2.5 * k, cx - 2 * k, 8 + 2.5 * k, YES, 3.5, 10)
    ic += yazi(cx + k + 2.5 * k, 8 + 1.5 * k - 8, 'F1 = 5 N', 12.5, MAVI) + yazi(cx - k, 8 + 2.5 * k + 18, 'F2 = 2 N', 12.5, YES)
    ic += f'<rect x="12" y="{8 + 4 * k + 8}" width="{k}" height="{k}" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1"/>' + yazi(12 + k + 8, 8 + 4 * k + 8 + 16, '1 kare = 1 N', 12.5, LAC, 'start')
    ic += pusula(306, 8 + 4 * k + 22)
    return svg(360, 8 + 5 * k + 14, ic, 'Her karesi 1 N olan kareli zeminde K cismi. Doğuya doğru beş kare uzunluğunda F1 = 5 N oku, batıya doğru iki kare uzunluğunda F2 = 2 N oku. Altta 1 kare = 1 N; B batı, D doğu.', 36)


def itme_cekme():
    """Öğretmen masasına batı yönünde biri itme, biri çekme olan iki kuvvet (üstten görünüm)."""
    ic = f'<rect x="120" y="30" width="120" height="52" rx="6" fill="#d9a066" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += ''.join(f'<rect x="{x}" y="{y}" width="10" height="10" rx="2" fill="{KAHVE}"/>' for x, y in [(124, 34), (226, 34), (124, 68), (226, 68)])
    ic += yazi(180, 60, 'masa', 12.5, '#fff')
    ic += ok(300, 56, 242, 56, MAVI, 3.5, 10) + yazi(300, 44, 'itme', 12.5, MAVI, 'end')
    ic += ok(118, 56, 60, 56, YES, 3.5, 10) + yazi(100, 44, 'çekme', 12.5, YES, 'end')
    ic += pusula(44, 96) + yazi(300, 98, 'iki kuvvet de batıya', 11.5, SOLUK)
    return svg(360, 104, ic, 'Üstten görünen masa. Sağ kenarına batıya doğru bastıran itme oku, sol kenarından batıya doğru uzanan çekme oku. B batı, D doğu; not: iki kuvvet de batıya.', 26)


def araba():
    """Yolda kalan araba: 1. durumda tek kuvvet, 2. durumda aynı yönde üç kuvvet (insan yok)."""
    def arac(x, y, renk):
        return (f'<path d="M{x} {y + 22} h8 l10 -14 h30 l12 14 h18 v14 h-78 z" fill="{renk}" stroke="{LAC}" stroke-width="1.2"/>'
                f'<rect x="{x + 22}" y="{y + 10}" width="24" height="11" rx="2" fill="#dbe9ff"/>'
                f'<circle cx="{x + 18}" cy="{y + 38}" r="6" fill="{LAC}"/><circle cx="{x + 60}" cy="{y + 38}" r="6" fill="{LAC}"/>')
    ic = ''
    for i, (bas, n, sonuc) in enumerate([('1. durum', 1, 'hareket etmiyor'), ('2. durum', 3, 'hareket ediyor')]):
        x = 6 + i * 178
        ic += kutu(x, 4, 170, 104, KUM, GRI, 8, 1.1) + yazi(x + 85, 22, bas, 13, LAC)
        ic += f'<line x1="{x + 8}" y1="76" x2="{x + 162}" y2="76" stroke="{SOLUK}" stroke-width="1.5"/>'
        ic += arac(x + 84, 32, MAVI_A if i == 0 else YES_A)
        for k in range(n):
            y = 58 - (n - 1) * 7 + k * 14
            ic += ok(x + 24, y, x + 76, y, [MAVI, YES, TUR][k], 3, 9) + yazi(x + 14, y + 4, f'F{k + 1}', 11.5, [MAVI, YES, TUR][k], 'end')
        ic += yazi(x + 85, 98, sonuc, 12, KIR if i == 0 else YES)
    return svg(360, 112, ic, '1. durum: arabaya doğuya doğru tek ok F1; araba hareket etmiyor. 2. durum: arabaya doğuya doğru üç ok F1, F2, F3; araba hareket ediyor.', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = kuvvet_ozellik()
    s[1]['gorsel'] = dort_cisim()
    s[2]['gorsel'] = ayni_yon()
    s[3]['gorsel'] = zit_yon()
    s[6]['gorsel'] = kareli()
    s[7]['gorsel'] = itme_cekme()
    s[9]['gorsel'] = araba()
