"""8. sınıf Matematik 1. hafta çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def uslu(x, y, parcalar, boy=14, renk=LAC, hiza='middle'):
    """parcalar: düz metin ya da (taban, üs); üs küçük ve yukarıda, sonraki parça taban çizgisine döner."""
    ic, geri = '', 0.0
    for p in parcalar:
        if isinstance(p, tuple):
            ic += f'<tspan dy="{geri:.1f}">{p[0]}</tspan><tspan dy="{-boy * 0.42:.1f}" font-size="{boy * 0.68:.1f}">{p[1]}</tspan>'
            geri = boy * 0.42
        else:
            ic += f'<tspan dy="{geri:.1f}">{p}</tspan>'
            geri = 0.0
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}">{ic}</text>'


def dominolar():
    tas = [(1, 60), (2, 30), (3, None), (None, 15), (5, None), (6, None)]
    ic = ''
    for i, (a, b) in enumerate(tas):
        x, y = 4 + (i % 3) * 96, 4 + (i // 3) * 46
        ic += f'<rect x="{x}" y="{y}" width="86" height="38" rx="7" fill="#fff" stroke="{LAC}" stroke-width="1.8"/>'
        ic += f'<line x1="{x + 43}" y1="{y + 5}" x2="{x + 43}" y2="{y + 33}" stroke="{LAC}" stroke-width="1.4"/>'
        for j, n in enumerate((a, b)):
            cx = x + 21.5 + j * 43
            if n is None:
                ic += f'<rect x="{cx - 14}" y="{y + 7}" width="28" height="24" rx="4" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3" stroke-dasharray="3 2"/>'
            else:
                ic += yazi(cx, y + 25, n, 16)
    return svg(292, 96, ic, 'Altı domino taşı: 1 ve 60, 2 ve 30, 3 ve boş, boş ve 15, 5 ve boş, 6 ve boş', 22)


def makine():
    ic = ''
    for i, (n, r) in enumerate([(2, MAVI), (3, YES), (3, YES), (7, TUR)]):
        cx = 38 + i * 34
        ic += f'<circle cx="{cx}" cy="20" r="14" fill="{r}"/>' + yazi(cx, 25.5, n, 15, '#fff')
    ic += f'<path d="M20 40 H176 L128 66 H68 Z" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.6"/>'
    ic += f'<rect x="60" y="66" width="76" height="42" rx="8" fill="{MAVI}" stroke="{LAC}" stroke-width="1.6"/>'
    ic += yazi(98, 95, '×', 26, '#fff')
    ic += f'<line x1="136" y1="87" x2="200" y2="87" stroke="{LAC}" stroke-width="2.2"/><path d="M198 80 L210 87 L198 94 Z" fill="{LAC}"/>'
    ic += f'<rect x="214" y="68" width="60" height="38" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.8" stroke-dasharray="4 3"/>'
    ic += yazi(244, 94, '?', 20, TUR)
    return svg(280, 112, ic, 'Makineye 2, 3, 3 ve 7 asal sayıları giriyor; makine çarpıyor; çıkan sayı soru işareti', 24)


def ece_liste():
    ic = f'<rect x="2" y="2" width="176" height="118" rx="6" fill="#fffdf5" stroke="#e3d9b8" stroke-width="1.2"/>'
    ic += ''.join(f'<line x1="2" y1="{y}" x2="178" y2="{y}" stroke="#dbe4f5" stroke-width="1"/>' for y in range(26, 120, 22))
    ic += f'<line x1="92" y1="10" x2="92" y2="104" stroke="{LAC}" stroke-width="2"/>'
    for i, (a, b) in enumerate([('132', '4'), ('33', '3'), ('11', '11'), ('1', '')]):
        y = 26 + i * 22
        ic += yazi(80, y - 5, a, 15, MAVI, 'end') + (yazi(104, y - 5, b, 15, MAVI, 'start') if b else '')
    return svg(180, 122, ic, "Ece'nin bölen listesi: 132 bölü 4, 33 bölü 3, 11 bölü 11, 1", 26)


def salon():
    ic = f'<rect x="60" y="4" width="220" height="22" rx="4" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>' + yazi(170, 20, 'SAHNE', 12, MOR)
    for r in range(3):
        y = 40 + r * 20 if r < 2 else 100
        for c in range(7):
            x = 80 + c * 22 if c < 5 else 80 + (c + 1) * 22 + 6
            ic += f'<rect x="{x}" y="{y}" width="14" height="12" rx="2.5" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.2"/>'
        ic += yazi(80 + 5 * 22 + 12, y + 10, '…', 14, LAC)
    ic += yazi(170, 90, '⋮', 14, LAC)
    ic += f'<line x1="62" y1="40" x2="62" y2="112" stroke="{MAVI}" stroke-width="1.6"/><path d="M57 106 L62 114 L67 106" fill="none" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(54, 66, 'Sıra sayısı', 12, MAVI, 'end') + yazi(54, 81, "5'ten fazla", 12, MAVI, 'end')
    ic += f'<line x1="80" y1="124" x2="262" y2="124" stroke="{YES}" stroke-width="1.6"/><path d="M256 119 L264 124 L256 129" fill="none" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(171, 142, "Bir sıradaki sandalye sayısı 10'dan fazla", 12, '#0c7a3c')
    return svg(300, 148, ic, "Gösteri salonu şeması: sahne, sandalye sıraları; sıra sayısı 5'ten fazla, bir sıradaki sandalye sayısı 10'dan fazla", 30)


def harfler():
    ic = ''
    for i, (h, n) in enumerate([('A', 2), ('B', 3), ('C', 5), ('D', 7), ('E', 11)]):
        x = 4 + i * 58
        ic += f'<rect x="{x}" y="4" width="50" height="60" rx="7" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
        ic += yazi(x + 25, 29, h, 18, LAC) + f'<line x1="{x + 8}" y1="37" x2="{x + 42}" y2="37" stroke="{GRI}" stroke-width="1"/>' + yazi(x + 25, 56, n, 15, TUR)
    return svg(292, 68, ic, 'Harf kartları: A 2, B 3, C 5, D 7, E 11', 19)


def bulmaca():
    x0, y0, k = 20, 8, 50
    ic = ''
    for r in range(2):
        for c in range(2):
            x, y = x0 + c * k, y0 + r * k
            bos = (r, c) in ((0, 1), (1, 0))
            ic += f'<rect x="{x}" y="{y}" width="{k}" height="{k}" fill="{TUR_A if bos else "#fff"}" stroke="{LAC}" stroke-width="1.8"/>'
            if not bos:
                ic += yazi(x + k / 2, y + k / 2 + 7, 4 if r == 0 else 7, 20)
    ic += uslu(x0 + 2 * k + 12, y0 + k / 2 + 5, [('2', '3'), ' · 3'], 15, MAVI, 'start')
    ic += uslu(x0 + 2 * k + 12, y0 + 1.5 * k + 5, ['5 · 7'], 15, MAVI, 'start')
    ic += uslu(x0 + k / 2, y0 + 2 * k + 24, [('2', '2'), ' · 5'], 15, YES)
    ic += uslu(x0 + 1.5 * k, y0 + 2 * k + 46, ['2 · 3 · 7'], 15, YES)
    ic += f'<line x1="{x0 + 1.5 * k}" y1="{y0 + 2 * k + 4}" x2="{x0 + 1.5 * k}" y2="{y0 + 2 * k + 32}" stroke="{YES}" stroke-width="1" stroke-dasharray="2 2"/>'
    return svg(200, y0 + 2 * k + 52, ic, 'İki satır iki sütunlu tablo: sol üst 4, sağ alt 7, öteki kutular boş. Satır çarpımları 2 üssü 3 çarpı 3 ve 5 çarpı 7; sütun çarpımları 2 üssü 2 çarpı 5 ve 2 çarpı 3 çarpı 7', 32)


def kutular():
    ic = ''
    for i, r in enumerate([(MAVI_A, MAVI), (YES_A, YES), (TUR_A, TUR)]):
        x = 6 + i * 70
        ic += f'<path d="M{x} 30 L{x + 12} 18 H{x + 70} L{x + 58} 30 Z" fill="{r[1]}" opacity=".35"/>'
        ic += f'<rect x="{x}" y="30" width="58" height="50" rx="4" fill="{r[0]}" stroke="{r[1]}" stroke-width="1.6"/>'
        ic += f'<path d="M{x + 58} 30 L{x + 70} 18 V68 L{x + 58} 80 Z" fill="{r[1]}" opacity=".25"/>'
        ic += ''.join(f'<circle cx="{x + 14 + j * 15}" cy="{64 - (j % 2) * 5}" r="5.5" fill="{r[1]}"/>' for j in range(3))
        ic += yazi(x + 29, 50, '?', 16, LAC)
    ic += f'<path d="M226 34 H330 V76 H226 L212 55 Z" fill="#fff" stroke="{LAC}" stroke-width="1.6"/><circle cx="222" cy="55" r="3" fill="{LAC}"/>'
    ic += yazi(278, 49, 'Çarpım', 12, '#5b6479')
    ic += uslu(278, 70, [('2', '3'), ' · ', ('3', '2'), ' · 7'], 15, LAC)
    return svg(336, 86, ic, 'Üç kutu, bilye sayıları soru işareti; etiket: çarpım 2 üssü 3 çarpı 3 üssü 2 çarpı 7', 22)


def ogrenci_kartlari():
    ic = ''
    liste = [('Ali', [('2', '4'), ' · 3']), ('Can', [('2', '3'), ' · 6']), ('Efe', [('4', '2'), ' · 3']), ('Naz', ['2 · 24'])]
    for i, (ad, ifade) in enumerate(liste):
        x = 4 + i * 88
        ic += f'<rect x="{x}" y="4" width="80" height="54" rx="8" fill="{MAVI_A if i % 2 == 0 else TUR_A}" stroke="{MAVI if i % 2 == 0 else TUR}" stroke-width="1.6"/>'
        ic += yazi(x + 40, 22, ad, 12.5, '#5b6479')
        ic += uslu(x + 40, 46, ['48 = '] + ifade, 14, LAC)
    return svg(356, 62, ic, 'Dört öğrencinin yazdığı: Ali 48 eşittir 2 üssü 4 çarpı 3; Can 48 eşittir 2 üssü 3 çarpı 6; Efe 48 eşittir 4 üssü 2 çarpı 3; Naz 48 eşittir 2 çarpı 24', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dominolar()
    s[3]['gorsel'] = makine()
    s[5]['gorsel'] = ece_liste()
    s[7]['gorsel'] = salon()
    s[9]['gorsel'] = harfler()
    s[10]['gorsel'] = ogrenci_kartlari()
    s[12]['gorsel'] = bulmaca()
    s[13]['gorsel'] = kutular()
