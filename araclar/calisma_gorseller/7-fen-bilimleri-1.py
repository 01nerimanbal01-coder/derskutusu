"""7. sınıf Fen Bilimleri 1. hafta (uzay araştırmaları) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, GRI, GRI_A, SOLUK = '#e8eefe', '#fff1df', '#e3f6ea', '#9aa6bd', '#eef1f6', '#5b6479'
PANEL = '#2b4c9b'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def harf(x, y, h, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{renk}"/>' + yazi(x, y + 4.5, h, 12, '#fff')


def panel(x, y, w, h):
    ic = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{PANEL}" stroke="{LAC}" stroke-width=".8"/>'
    return ic + ''.join(f'<line x1="{x + w * k / 4:.1f}" y1="{y}" x2="{x + w * k / 4:.1f}" y2="{y + h}" stroke="#7fa0e6" stroke-width=".6"/>' for k in range(1, 4))


def roket(cx, cy):
    ic = f'<path d="M{cx} {cy - 30} q9 10 9 24 v26 h-18 v-26 q0 -14 9 -24z" fill="#f4f6fb" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<path d="M{cx - 9} {cy + 8} l-7 12 h7z M{cx + 9} {cy + 8} l7 12 h-7z" fill="{KIR}"/><circle cx="{cx}" cy="{cy - 8}" r="3.5" fill="{MAVI}"/>'
    return ic + f'<path d="M{cx - 6} {cy + 20} q6 14 12 0z" fill="{TUR}"/>'


def mekik(cx, cy):
    ic = f'<path d="M{cx} {cy - 26} q8 8 8 22 l18 18 v6 h-52 v-6 l18 -18 q0 -14 8 -22z" fill="#f4f6fb" stroke="{LAC}" stroke-width="1.4"/>'
    return ic + f'<path d="M{cx - 4} {cy - 14} h8 v5 h-8z" fill="{LAC}"/><path d="M{cx - 5} {cy + 20} v4 h10 v-4z" fill="{GRI}"/>'


def istasyon(cx, cy):
    ic = f'<line x1="{cx - 30}" y1="{cy}" x2="{cx + 30}" y2="{cy}" stroke="{GRI}" stroke-width="2.4"/>'
    ic += panel(cx - 32, cy - 22, 12, 18) + panel(cx - 32, cy + 4, 12, 18) + panel(cx + 20, cy - 22, 12, 18) + panel(cx + 20, cy + 4, 12, 18)
    return ic + f'<rect x="{cx - 12}" y="{cy - 6}" width="24" height="12" rx="3" fill="#e9edf5" stroke="{LAC}" stroke-width="1.2"/><rect x="{cx - 4}" y="{cy - 14}" width="8" height="28" rx="2" fill="#e9edf5" stroke="{LAC}" stroke-width="1.2"/>'


def uydu(cx, cy):
    ic = panel(cx - 30, cy - 6, 18, 12) + panel(cx + 12, cy - 6, 18, 12)
    ic += f'<line x1="{cx - 12}" y1="{cy}" x2="{cx + 12}" y2="{cy}" stroke="{GRI}" stroke-width="1.6"/>'
    ic += f'<rect x="{cx - 8}" y="{cy - 9}" width="16" height="18" rx="2" fill="#f3c64f" stroke="{LAC}" stroke-width="1.2"/>'
    return ic + f'<path d="M{cx - 7} {cy + 12} a8 5 0 0 0 14 0z" fill="#e9edf5" stroke="{LAC}" stroke-width="1"/><line x1="{cx}" y1="{cy + 9}" x2="{cx}" y2="{cy + 12}" stroke="{LAC}"/>'


def teleskop(cx, cy):
    ic = f'<g transform="rotate(-30 {cx} {cy - 6})"><rect x="{cx - 24}" y="{cy - 14}" width="44" height="12" rx="3" fill="#e9edf5" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<rect x="{cx + 18}" y="{cy - 16}" width="6" height="16" rx="1.5" fill="{MAVI}"/></g>'
    return ic + f'<path d="M{cx} {cy - 4} l-12 26 M{cx} {cy - 4} l12 26 M{cx} {cy - 4} v26" stroke="{LAC}" stroke-width="1.6" fill="none"/>'


def araclar():
    ic = ''
    for i, (h, f) in enumerate([('A', roket), ('B', mekik), ('C', istasyon), ('D', uydu), ('E', teleskop)]):
        x = 4 + i * 72
        ic += f'<rect x="{x}" y="4" width="66" height="84" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>'
        ic += f(x + 33, 48) + harf(x + 14, 17, h)
    return svg(364, 92, ic, 'Beş uzay teknolojisi: A roket, B uzay mekiği, C uzay istasyonu, D yapay uydu, E teleskop', 22)


def harita():
    ic = f'<rect x="0" y="0" width="360" height="136" rx="8" fill="#dff1ff"/>'
    ic += f'<path d="M0 104 H360 V136 H0 Z" fill="#cfe9c0"/>'
    ic += f'<path d="M188 104 L248 26 L300 104 Z" fill="#a8b8c9" stroke="#7a8aa0"/><path d="M234 44 L248 26 L262 44 L254 40 L248 46 L242 40 Z" fill="#fff"/>'
    ic += f'<path d="M270 104 L318 56 L360 104 Z" fill="#b9c6d4" stroke="#7a8aa0"/>'
    ic += f'<path d="M330 64 L336 40 L342 64 M332 56 h8 M333 48 h6" stroke="{LAC}" stroke-width="1.4" fill="none"/>'
    ic += ''.join(f'<path d="M{336 + d} {38 - abs(d) / 2} q{d} -4 0 -8" stroke="{KIR}" stroke-width="1.1" fill="none"/>' for d in (-6, 6))
    for i, (x, h) in enumerate([(12, 40), (30, 56), (50, 34), (68, 48), (86, 30)]):
        ic += f'<rect x="{x}" y="{104 - h}" width="16" height="{h}" fill="#7d88a3"/>'
        ic += ''.join(f'<rect x="{x + 3 + (k % 2) * 6}" y="{104 - h + 5 + (k // 2) * 9}" width="3.5" height="4" fill="#ffd166"/>' for k in range(2 * (h // 12)))
    ic += f'<path d="M110 128 C140 110 150 124 176 106" stroke="{KIR}" stroke-width="2" stroke-dasharray="5 3" fill="none"/>'
    ic += yazi(118, 132, 'deprem kuşağı', 10.5, KIR, 'start')
    for h_, x, y in [('A', 38, 40), ('B', 248, 14), ('C', 318, 46), ('D', 150, 102)]:
        ic += f'<circle cx="{x}" cy="{y + 4}" r="3" fill="{LAC}"/>' + harf(x, y - 10, h_, TUR)
    ic += yazi(336 - 30, 26, 'verici', 10.5, SOLUK, 'end')
    return svg(360, 136, ic, 'Bölge haritası: A şehir merkezinde, B yüksek bir dağın zirvesinde, C televizyon-radyo vericisinin yanında, D deprem kuşağında alçak bir yerde', 32)


def teleskoplar():
    ic = f'<rect x="0" y="0" width="360" height="132" rx="8" fill="#0f1b3d"/>'
    ic += f'<path d="M0 132 Q180 70 360 132 Z" fill="#8fc7ff" opacity=".45"/><path d="M0 132 Q180 100 360 132 Z" fill="#6b8f5a"/>'
    ic += yazi(300, 110, 'atmosfer', 11, '#cfe6ff')
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r="1" fill="#fff"/>' for x, y in [(30, 14), (80, 30), (150, 10), (220, 22), (330, 12), (300, 40), (120, 48)])
    for x in (60, 70, 80):
        ic += f'<line x1="{x + 30}" y1="6" x2="{x}" y2="90" stroke="#ffe08a" stroke-width="1.2" opacity=".5" stroke-dasharray="3 3"/>'
    ic += teleskop(78, 104).replace(LAC, '#ffffff')
    for x in (236, 246, 256):
        ic += f'<line x1="{x}" y1="4" x2="{x}" y2="34" stroke="#ffe08a" stroke-width="1.4"/>'
    ic += f'<rect x="232" y="38" width="30" height="14" rx="3" fill="#e9edf5"/>' + panel(214, 40, 16, 10) + panel(264, 40, 16, 10)
    ic += harf(104, 112, 1, TUR) + harf(292, 44, 2, TUR)
    return svg(360, 132, ic, 'Yerdeki 1 numaralı teleskop atmosferin altında, ışınlar atmosferden zayıflayarak geliyor; 2 numaralı teleskop atmosferin üstünde, uzayda', 30)


def gorevler():
    ic = ''
    for i, h in enumerate('KLMN'):
        x = 4 + i * 90
        ic += f'<rect x="{x}" y="4" width="84" height="76" rx="8" fill="#fff" stroke="{GRI}" stroke-width="1.3"/>' + harf(x + 14, 18, h)
        cx = x + 42
        if h == 'K':    # haberleşme: çanak anten ve ekran
            ic += f'<rect x="{cx - 4}" y="36" width="30" height="22" rx="2" fill="{LAC}"/><rect x="{cx - 1}" y="39" width="24" height="16" fill="#8fc7ff"/>'
            ic += f'<path d="M{cx - 30} 44 a14 14 0 0 0 22 12z" fill="#e9edf5" stroke="{LAC}" stroke-width="1.2"/><line x1="{cx - 17}" y1="52" x2="{cx - 17}" y2="68" stroke="{LAC}" stroke-width="1.6"/>'
            ic += ''.join(f'<path d="M{cx - 12 + k * 5} {34 - k * 4} q6 -6 12 0" stroke="{MAVI}" stroke-width="1.2" fill="none"/>' for k in range(2))
        elif h == 'L':  # hava tahmini
            ic += f'<circle cx="{cx - 8}" cy="40" r="10" fill="#ffc93c"/><path d="M{cx - 12} 56 a10 10 0 0 1 8 -14 a12 12 0 0 1 22 2 a8 8 0 0 1 0 12z" fill="#e9edf5" stroke="{GRI}"/>'
            ic += ''.join(f'<line x1="{cx - 4 + k * 8}" y1="62" x2="{cx - 7 + k * 8}" y2="70" stroke="{MAVI}" stroke-width="1.6"/>' for k in range(3))
        elif h == 'M':  # yer-yön bulma
            ic += f'<rect x="{cx - 16}" y="30" width="32" height="44" rx="4" fill="{LAC}"/><rect x="{cx - 13}" y="34" width="26" height="34" fill="{YES_A}"/>'
            ic += f'<path d="M{cx - 13} 58 L{cx + 13} 44" stroke="{GRI}" stroke-width="3"/><path d="M{cx + 2} 38 a6 6 0 0 1 12 0 c0 6 -6 12 -6 12 c0 0 -6 -6 -6 -12z" fill="{KIR}"/>'
        else:           # yukarıdan görüntü: tarlalar ve su basmış alan
            for r in range(3):
                for c in range(3):
                    renk = ['#a7d37a', '#d9c27a', '#7fbf5f'][(r + c) % 3]
                    ic += f'<rect x="{cx - 30 + c * 20}" y="{30 + r * 15}" width="19" height="14" fill="{renk}"/>'
            ic += f'<path d="M{cx - 30} 60 q14 -12 30 -4 t30 -6 v24 h-60z" fill="#6aa9e0" opacity=".85"/>'
    return svg(364, 84, ic, 'Dört kullanım alanı: K televizyon yayını ve çanak anten, L hava tahmini, M telefonda yol bulma, N yukarıdan çekilmiş tarla ve su basmış alan görüntüsü', 20)


def urunler():
    ic = ''
    adlar = [('Yol bulma', 'sistemi'), ('Dijital', 'termometre'), ('Duman', 'dedektörü'), ('Güneş', 'paneli')]
    for i, ad in enumerate(adlar):
        x = 4 + i * 90
        cx = x + 42
        ic += f'<rect x="{x}" y="4" width="84" height="64" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>'
        if i == 0:
            ic += f'<rect x="{cx - 12}" y="12" width="24" height="46" rx="4" fill="{LAC}"/><rect x="{cx - 9}" y="16" width="18" height="36" fill="{YES_A}"/><path d="M{cx - 4} 26 a4 4 0 0 1 8 0 c0 4 -4 8 -4 8 c0 0 -4 -4 -4 -8z" fill="{KIR}"/>'
        elif i == 1:
            ic += f'<rect x="{cx - 7}" y="12" width="14" height="36" rx="7" fill="#fff" stroke="{LAC}" stroke-width="1.3"/><rect x="{cx - 5}" y="18" width="10" height="10" fill="{LAC}"/><line x1="{cx}" y1="48" x2="{cx}" y2="60" stroke="{GRI}" stroke-width="3"/>'
        elif i == 2:
            ic += f'<circle cx="{cx}" cy="34" r="20" fill="#fff" stroke="{LAC}" stroke-width="1.3"/><circle cx="{cx}" cy="34" r="12" fill="none" stroke="{GRI}"/><circle cx="{cx + 8}" cy="26" r="2.5" fill="{KIR}"/>'
        else:
            ic += f'<g transform="skewX(-20)">{panel(cx + 4, 16, 34, 30)}</g><line x1="{cx}" y1="46" x2="{cx}" y2="60" stroke="{GRI}" stroke-width="2.4"/>'
        ic += yazi(cx, 82, ad[0], 10.5, LAC) + yazi(cx, 95, ad[1], 10.5, LAC)
    return svg(364, 100, ic, 'Dört ürün: telefonda yol bulma, dijital termometre, duman dedektörü, güneş paneli', 22)


def kart():
    ic = f'<rect x="4" y="4" width="352" height="116" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<rect x="4" y="4" width="352" height="22" rx="10" fill="{MAVI}"/><rect x="4" y="16" width="352" height="10" fill="{MAVI}"/>'
    ic += yazi(180, 20, 'UZAY TEKNOLOJİSİ KARTI', 12, '#fff')
    for i, m in enumerate(["Dünya'dan kontrol edilen robotik bir araçtır.", 'Enerjisini güneş panellerinden sağlar.',
                           'Bir gök cismini ya da uzaydaki olayları', 'incelemek için gönderilir.']):
        if i < 3:
            ic += f'<circle cx="20" cy="{44 + i * 20}" r="3.5" fill="{MAVI}"/>'
        ic += yazi(30, 48.5 + i * 20, m, 12, LAC, 'start')
    return svg(360, 124, ic, "Uzay teknolojisi kartı: Dünya'dan kontrol edilen robotik bir araçtır. Enerjisini güneş panellerinden sağlar. Bir gök cismini ya da uzaydaki olayları incelemek için gönderilir.", 23)


def gorev_karti():
    ic = f'<rect x="4" y="4" width="352" height="112" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(180, 24, 'GÖREV KARTI · Alper Gezeravcı', 12.5, '#b35c00')
    satir = [('Tarih:', '19 Ocak 2024'), ('Roket:', 'Falcon 9'), ('Kaldığı yer:', 'Uluslararası Uzay İstasyonu'), ('Süre:', '18 gün, 13 bilimsel deney')]
    for i, (a, b) in enumerate(satir):
        ic += yazi(86, 46 + i * 19, a, 11.5, SOLUK, 'start') + yazi(170, 46 + i * 19, b, 11.5, LAC, 'start')
    ic += roket(50, 62).replace('cy - 30', 'cy - 30')
    return svg(360, 120, ic, 'Görev kartı: Alper Gezeravcı, 19 Ocak 2024, roket Falcon 9, kaldığı yer Uluslararası Uzay İstasyonu, 18 gün, 13 bilimsel deney', 24)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = araclar()
    s[3]['gorsel'] = harita()
    s[4]['gorsel'] = teleskoplar()
    s[6]['gorsel'] = gorevler()
    s[7]['gorsel'] = urunler()
    s[9]['gorsel'] = kart()
    s[13]['gorsel'] = gorev_karti()
