"""8. sınıf Matematik 5. hafta (Bilimsel Gösterim) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""
import math

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


def bilgi_kartlari():
    kartlar = [('Işığın 1 saniyede', 'aldığı yol', '≈ 300 000 km', MAVI, MAVI_A),
               ('Bir kâğıt yaprağının', 'kalınlığı', '≈ 0,0001 m', TUR, TUR_A),
               ("Türkiye'nin", 'yüzölçümü', '≈ 783 600 km²', YES, YES_A)]
    ic = ''
    for i, (b1, b2, deger, renk, acik) in enumerate(kartlar):
        x = 4 + i * 200
        ic += f'<rect x="{x}" y="4" width="190" height="96" rx="10" fill="{acik}" stroke="{renk}" stroke-width="2"/>'
        ic += f'<path d="M{x} 14 a10 10 0 0 1 10 -10 h170 a10 10 0 0 1 10 10 v36 h-190 z" fill="{renk}"/>'
        ic += yazi(x + 95, 24, b1, 13, '#fff') + yazi(x + 95, 42, b2, 13, '#fff')
        ic += yazi(x + 95, 82, deger, 19, LAC)
    return svg(604, 104, ic, 'Üç bilgi kartı: ışığın 1 saniyede aldığı yol yaklaşık 300 000 km, bir kâğıt yaprağının kalınlığı yaklaşık 0,0001 m, Türkiye\'nin yüzölçümü yaklaşık 783 600 km²', 30)


def hesap_makinesi():
    ic = f'<rect x="4" y="4" width="172" height="196" rx="16" fill="#3a4357" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<rect x="16" y="16" width="148" height="56" rx="6" fill="#c9d8b6" stroke="#1f2633" stroke-width="2"/>'
    ic += yazi(156, 34, '4000000 × 900000', 11, '#2b3320', 'end')
    ic += yazi(156, 62, '3,6e12', 24, '#1b2214', 'end')
    tuslar = ['7', '8', '9', '×', '4', '5', '6', '−', '1', '2', '3', '+', '0', ',', 'e', '=']
    for i, t in enumerate(tuslar):
        x, y = 16 + (i % 4) * 38, 84 + (i // 4) * 28
        renk = TUR if t == '=' else ('#5b6478' if t in '×−+e' else '#eef1f6')
        yr = '#fff' if t in '=×−+e' else LAC
        ic += f'<rect x="{x}" y="{y}" width="32" height="22" rx="5" fill="{renk}"/>' + yazi(x + 16, y + 16, t, 13, yr)
    return svg(180, 204, ic, 'Hesap makinesi; ekranın üst satırında 4000000 × 900000 işlemi, alt satırında 3,6e12 sonucu yazıyor', 48)


def deniz_defter():
    satirlar = [['1)  270 000 = 2,7 · ', ('10', '5')],
                ['2)  0,000 46 = 4,6 · ', ('10', '−5')],
                ['3)  81 300 000 = 81,3 · ', ('10', '6')],
                ['4)  0,009 = 9 · ', ('10', '−3')]]
    ic = f'<rect x="4" y="4" width="352" height="156" rx="6" fill="#fffdf6" stroke="{GRI}" stroke-width="1.6"/>'
    ic += f'<line x1="44" y1="6" x2="44" y2="158" stroke="{KIR}" stroke-width="1.2"/>'
    for k in range(4):
        ic += f'<circle cx="22" cy="{30 + k * 36}" r="6" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    for k, s in enumerate(satirlar):
        y = 38 + k * 34
        ic += f'<line x1="44" y1="{y + 8}" x2="352" y2="{y + 8}" stroke="#c7d4ee" stroke-width="1"/>'
        ic += uslu(56, y, s, 17, MAVI, 'start')
    return svg(360, 164, ic, 'Deniz\'in defteri: 1) 270 000 = 2,7 · 10 üssü 5; 2) 0,000 46 = 4,6 · 10 üssü −5; 3) 81 300 000 = 81,3 · 10 üssü 6; 4) 0,009 = 9 · 10 üssü −3', 34)


def depolar():
    etiket = [('A', ['9,8 · ', ('10', '6')]), ('B', ['1,2 · ', ('10', '7')]),
              ('C', ['98 · ', ('10', '5')]), ('D', ['0,15 · ', ('10', '8')])]
    ic = ''
    for i, (h, p) in enumerate(etiket):
        x = 6 + i * 150
        ic += f'<path d="M{x} 50 L{x + 68} 8 L{x + 136} 50 V138 H{x} Z" fill="{MAVI_A}" stroke="{LAC}" stroke-width="2" stroke-linejoin="round"/>'
        ic += f'<circle cx="{x + 68}" cy="36" r="13" fill="{LAC}"/>' + yazi(x + 68, 41.5, h, 15, '#fff')
        ic += f'<rect x="{x + 14}" y="60" width="108" height="32" rx="6" fill="#fff" stroke="{TUR}" stroke-width="1.8"/>'
        ic += uslu(x + 68, 83, p, 16, LAC)
        ic += f'<rect x="{x + 40}" y="100" width="56" height="38" fill="#c9d3e6" stroke="{LAC}" stroke-width="1.6"/>'
        for k in range(1, 4):
            ic += f'<line x1="{x + 40}" y1="{100 + k * 9.5}" x2="{x + 96}" y2="{100 + k * 9.5}" stroke="{GRI}" stroke-width="1"/>'
    return svg(604, 142, ic, 'Dört depo; etiketlerdeki vida sayıları: A deposu 9,8 · 10 üssü 6, B deposu 1,2 · 10 üssü 7, C deposu 98 · 10 üssü 5, D deposu 0,15 · 10 üssü 8', 32)


def sac_teli():
    ic = f'<line x1="150" y1="118" x2="196" y2="160" stroke="#5b4636" stroke-width="14" stroke-linecap="round"/>'
    ic += f'<circle cx="100" cy="76" r="70" fill="#f4f8ff" stroke="{LAC}" stroke-width="6"/>'
    ic += '<clipPath id="m5mercek"><circle cx="100" cy="76" r="67"/></clipPath>'
    ic += f'<path d="M20 58 C70 46 130 50 190 40 L190 76 C130 86 70 82 20 94 Z" fill="#6b4a2f" clip-path="url(#m5mercek)"/>'
    ic += f'<line x1="100" y1="50" x2="100" y2="83" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<path d="M100 50 l-4 -8 h8 z M100 83 l-4 8 h8 z" fill="{KIR}"/>'
    ic += f'<line x1="100" y1="34" x2="100" y2="42" stroke="{KIR}" stroke-width="2"/><line x1="100" y1="91" x2="100" y2="99" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<rect x="196" y="56" width="100" height="34" rx="8" fill="#fff" stroke="{KIR}" stroke-width="1.8"/>'
    ic += f'<line x1="104" y1="66" x2="196" y2="72" stroke="{KIR}" stroke-width="1.2" stroke-dasharray="4 3"/>'
    ic += yazi(246, 79, '0,08 mm', 17, KIR)
    return svg(300, 166, ic, 'Büyüteçle bakılan saç teli; kalınlığı 0,08 mm olarak ölçülmüş', 34)


def kagit_desteleri():
    ic = ''
    for i in range(3):
        x = 10 + i * 92
        for k in range(7):
            y = 110 - k * 9
            ic += f'<rect x="{x + (k % 2) * 2}" y="{y}" width="78" height="9" rx="1.5" fill="{"#fff" if k % 2 else "#f2f4f9"}" stroke="{GRI}" stroke-width="1.1"/>'
        ic += f'<rect x="{x - 2}" y="70" width="84" height="10" fill="{TUR}" opacity="0.85"/>'
    ic += yazi(300, 96, '…', 26, LAC)
    ic += f'<rect x="330" y="10" width="226" height="48" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.8"/>'
    ic += uslu(443, 40, ['1 deste = 2,5 · ', ('10', '2'), ' yaprak'], 16, LAC)
    ic += f'<rect x="330" y="68" width="226" height="48" rx="8" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += uslu(443, 98, ['Deste sayısı: 4 · ', ('10', '3')], 16, LAC)
    return svg(560, 124, ic, 'Kâğıt desteleri; bir destede 2,5 · 10 üssü 2 yaprak, deste sayısı 4 · 10 üssü 3', 28)


def kasalar():
    sayi = [['5,03 · ', ('10', '6')], ['1,2 · ', ('10', '11')], ['9 · ', ('10', '8')]]
    ic = ''
    for i, p in enumerate(sayi):
        x = 6 + i * 200
        ic += f'<rect x="{x}" y="6" width="186" height="138" rx="10" fill="#d9dee8" stroke="{LAC}" stroke-width="2.2"/>'
        ic += f'<rect x="{x + 10}" y="16" width="166" height="118" rx="6" fill="#eef1f6" stroke="{GRI}" stroke-width="1.4"/>'
        ic += f'<rect x="{x + 20}" y="24" width="146" height="34" rx="6" fill="#fff" stroke="{MOR}" stroke-width="1.8"/>'
        ic += uslu(x + 93, 48, p, 17, LAC)
        ic += f'<circle cx="{x + 60}" cy="96" r="24" fill="#fff" stroke="{LAC}" stroke-width="2"/>'
        for k in range(12):
            a = k * math.pi / 6
            ic += f'<line x1="{x + 60 + 19 * math.cos(a):.1f}" y1="{96 + 19 * math.sin(a):.1f}" x2="{x + 60 + 23 * math.cos(a):.1f}" y2="{96 + 23 * math.sin(a):.1f}" stroke="{LAC}" stroke-width="1.2"/>'
        ic += f'<circle cx="{x + 60}" cy="96" r="7" fill="{LAC}"/>'
        ic += f'<rect x="{x + 104}" y="80" width="56" height="32" rx="5" fill="#1f2633"/>' + yazi(x + 132, 103, '? ?', 17, '#7dd3a8')
    return svg(604, 150, ic, 'Üç kasa; üzerlerindeki sayılar 5,03 · 10 üssü 6, 1,2 · 10 üssü 11 ve 9 · 10 üssü 8; şifre ekranlarında soru işareti', 32)


def kartlar_kare():
    kart = [(['3,4 · ', ('10', '−5')], MAVI, MAVI_A), (['3,■ · ', ('10', '−5')], TUR, TUR_A), (['0,000 038'], MAVI, MAVI_A)]
    ic = ''
    for i, (p, renk, acik) in enumerate(kart):
        x = 6 + i * 180
        ic += f'<rect x="{x}" y="6" width="140" height="56" rx="10" fill="{acik}" stroke="{renk}" stroke-width="2"/>'
        ic += uslu(x + 70, 42, p, 19, LAC)
        if i < 2:
            ic += yazi(x + 160, 44, '&lt;', 24, KIR)
    return svg(512, 68, ic, 'Üç kart küçükten büyüğe sıralı: 3,4 · 10 üssü −5 küçüktür 3,■ · 10 üssü −5 küçüktür 0,000 038', 20)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = bilgi_kartlari()
    s[5]['gorsel'] = hesap_makinesi()
    s[6]['gorsel'] = deniz_defter()
    s[8]['gorsel'] = depolar()
    s[10]['gorsel'] = sac_teli()
    s[11]['gorsel'] = kagit_desteleri()
    s[12]['gorsel'] = kasalar()
    s[13]['gorsel'] = kartlar_kare()
