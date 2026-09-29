"""10. sınıf Fizik, 1. hafta: Sabit Hızlı Hareket (FİZ.10.1.1).

Görseller yalnız MEB 10. sınıf Fizik ders kitabındaki bilgilerle çizilir (kitap s. 20 Şekil 1.1, Grafik 1.1-1.2; s. 28 Kontrol Noktası).
Renk anlamı bütün görsellerde aynıdır: mavi = pozitif (+) yönde hareket ve hız, turuncu = yer değiştirme (Δx)
ve negatif (−) yönde hareket; gri = eksen ve yol.
"""
from ozet_gorsel import svg, ok_isareti

MAVI = ('g-ma', 'g-ms', 'g-mf')      # dolgu, çizgi, yazı
TURUNCU = ('g-ta', 'g-ts', 'g-tf')


def _gri_ok(kimlik):
    # g-c sınıfı dolguyu kapattığı için ok ucunun dolgusu ayrıca verilir
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            '<path d="M0 0L10 5L0 10z" style="fill:var(--g-cizgi)"/></marker>')


def esit_yer_degistirme():
    """Sabit hızla giden araç: eşit zaman aralıklarında eşit yer değiştirme, aynı hız oku (kitap s. 20, Şekil 1.1)."""
    W, H = 472, 196
    ic = '<defs>' + ok_isareti('fz10okM', 'g-mf') + ok_isareti('fz10okT', 'g-tf') + '</defs>'
    xs = (56, 176, 296, 416)
    zaman = ('t₀ = 0', 't₁ = t', 't₂ = 2t', 't₃ = 3t')
    yol = 104
    ic += f'<line x1="14" y1="{yol}" x2="458" y2="{yol}" class="g-c" stroke-width="2.5" stroke-linecap="round"/>'
    for x, t in zip(xs, zaman):
        ic += f'<text x="{x}" y="20" text-anchor="middle" font-size="12.5" font-weight="700" class="g-y">{t}</text>'
        ic += f'<text x="{x}" y="41" text-anchor="middle" font-size="14" font-weight="700" font-style="italic" class="g-mf">ϑ</text>'
        ic += (f'<line x1="{x - 17}" y1="50" x2="{x + 14}" y2="50" class="g-ms" stroke-width="2.5" '
               f'stroke-linecap="round" marker-end="url(#fz10okM)"/>')
        # araç: gövde + iki tekerlek (tekerlekler yola oturur)
        # gövde tekerleklere oturur (alt kenar 92, tekerlek üstü 91)
        ic += (f'<rect x="{x - 24}" y="64" width="48" height="28" rx="7" class="g-ma"/>'
               f'<rect x="{x - 24}" y="64" width="48" height="28" rx="7" class="g-ms" stroke-width="2"/>')
        for dx in (-13, 13):
            ic += f'<circle cx="{x + dx}" cy="{yol - 7}" r="6" class="g-mf"/>'
        # konum çentiği
        ic += f'<line x1="{x}" y1="{yol + 3}" x2="{x}" y2="{yol + 11}" class="g-c" stroke-width="2"/>'
    for a, b in zip(xs, xs[1:]):
        ic += (f'<line x1="{a + 7}" y1="122" x2="{b - 7}" y2="122" class="g-ts" stroke-width="2.5" '
               'marker-start="url(#fz10okT)" marker-end="url(#fz10okT)"/>')
        ic += f'<text x="{(a + b) / 2:.0f}" y="143" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">Δx</text>'
    ic += f'<text x="{W / 2:.0f}" y="170" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Eşit zaman aralıklarında eşit yer değiştirme</text>'
    ic += f'<text x="{W / 2:.0f}" y="189" text-anchor="middle" font-size="11.5" class="g-s">Hız okları aynı: hızın büyüklüğü ve yönü değişmez, ivme sıfırdır.</text>'
    return svg(W, H, ic, 'Sabit hızla giden bir aracın t sıfır, t, 2t ve 3t anlarındaki konumları. Her anda hız oku aynı uzunlukta ve aynı yönde; '
               'ardışık konumlar arasındaki yer değiştirmeler (Δx) eşit. Hızın büyüklüğü ve yönü değişmez, ivme sıfırdır.')


def _eksen(ox, oy, ust, alt, sag, kimlik):
    """Düşey eksen iki yönlü (+ ve −), zaman ekseni sağa oklu."""
    return (f'<line x1="{ox}" y1="{alt}" x2="{ox}" y2="{ust}" class="g-c" stroke-width="2" '
            f'marker-start="url(#{kimlik})" marker-end="url(#{kimlik})"/>'
            f'<line x1="{ox}" y1="{oy}" x2="{sag}" y2="{oy}" class="g-c" stroke-width="2" marker-end="url(#{kimlik})"/>')


def iki_grafik():
    """Zıt yönlerde sabit hızla giden K ve L araçlarının (kitapta A ve B) x-t ve ϑ-t grafikleri (kitap s. 20 Grafik 1.1-1.2, s. 28 Kontrol Noktası)."""
    W, H = 472, 286
    ic = '<defs>' + _gri_ok('fz10okC') + '</defs>'
    ust, alt, oy = 42, 214, 128
    # --- sol: konum-zaman ---
    ox, tx = 46, 170
    ic += '<text x="120" y="18" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Konum-zaman (x-t) grafiği</text>'
    ic += _eksen(ox, oy, ust, alt, 204, 'fz10okC')
    ic += f'<text x="{ox + 8}" y="{ust + 6}" font-size="12" class="g-y">x (m)</text>'
    ic += f'<text x="{ox - 6}" y="{oy + 4}" text-anchor="end" font-size="11.5" class="g-s">0</text>'
    ic += f'<line x1="{tx}" y1="68" x2="{tx}" y2="188" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += f'<line x1="{ox}" y1="{oy}" x2="{tx}" y2="68" class="{MAVI[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<line x1="{ox}" y1="{oy}" x2="{tx}" y2="188" class="{TURUNCU[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<text x="{tx + 8}" y="66" font-size="13" font-weight="800" class="{MAVI[2]}">K</text>'
    ic += f'<text x="{tx + 8}" y="197" font-size="13" font-weight="800" class="{TURUNCU[2]}">L</text>'
    ic += f'<text x="{tx + 7}" y="146" font-size="12" font-style="italic" class="g-y">t</text>'
    ic += f'<text x="210" y="146" text-anchor="middle" font-size="12" class="g-y">t (s)</text>'
    ic += '<text x="120" y="238" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Eğim = hız</text>'
    ic += '<text x="120" y="256" text-anchor="middle" font-size="11.5" class="g-s">K: pozitif eğim, L: negatif eğim</text>'
    # --- sağ: hız-zaman ---
    ox, tx = 286, 402
    ic += '<text x="358" y="18" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Hız-zaman (ϑ-t) grafiği</text>'
    ic += f'<rect x="{ox}" y="78" width="{tx - ox}" height="{oy - 78}" class="{MAVI[0]}"/>'
    ic += f'<rect x="{ox}" y="{oy}" width="{tx - ox}" height="{178 - oy}" class="{TURUNCU[0]}"/>'
    ic += _eksen(ox, oy, ust, alt, 442, 'fz10okC')
    ic += f'<text x="{ox + 8}" y="{ust + 6}" font-size="12" class="g-y">ϑ (m/s)</text>'
    ic += f'<line x1="{tx}" y1="78" x2="{tx}" y2="178" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += f'<line x1="{ox}" y1="78" x2="{tx}" y2="78" class="{MAVI[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<line x1="{ox}" y1="178" x2="{tx}" y2="178" class="{TURUNCU[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<text x="{ox - 6}" y="82" text-anchor="end" font-size="12" class="{MAVI[2]}">+ϑ</text>'
    ic += f'<text x="{ox - 6}" y="{oy + 4}" text-anchor="end" font-size="11.5" class="g-s">0</text>'
    ic += f'<text x="{ox - 6}" y="182" text-anchor="end" font-size="12" class="{TURUNCU[2]}">−ϑ</text>'
    ic += f'<text x="{(ox + tx) / 2:.0f}" y="108" text-anchor="middle" font-size="12" font-weight="700" class="{MAVI[2]}">Δx = ϑ · t</text>'
    ic += f'<text x="{(ox + tx) / 2:.0f}" y="158" text-anchor="middle" font-size="12" font-weight="700" class="{TURUNCU[2]}">Δx = −ϑ · t</text>'
    ic += f'<text x="{tx + 8}" y="82" font-size="13" font-weight="800" class="{MAVI[2]}">K</text>'
    ic += f'<text x="{tx + 8}" y="187" font-size="13" font-weight="800" class="{TURUNCU[2]}">L</text>'
    ic += f'<text x="{tx + 7}" y="146" font-size="12" font-style="italic" class="g-y">t</text>'
    ic += '<text x="448" y="146" text-anchor="middle" font-size="12" class="g-y">t (s)</text>'
    ic += '<text x="358" y="238" text-anchor="middle" font-size="12.5" font-weight="800" class="g-y">Alan = yer değiştirme</text>'
    ic += '<text x="358" y="256" text-anchor="middle" font-size="11.5" class="g-s">Eksenin altı: negatif yön</text>'
    # renk açıklaması
    ic += f'<circle cx="96" cy="276" r="6" class="{MAVI[2]}"/><text x="108" y="280" font-size="11.5" class="g-y">K: pozitif yönde gidiyor</text>'
    ic += f'<circle cx="276" cy="276" r="6" class="{TURUNCU[2]}"/><text x="288" y="280" font-size="11.5" class="g-y">L: negatif yönde gidiyor</text>'
    return svg(W, H, ic, 'Zıt yönlerde sabit hızla giden K ve L araçlarının grafikleri. Konum-zaman grafiğinde K doğrusu yukarı (pozitif eğim), '
               'L doğrusu aşağı (negatif eğim) gider; eğim hızı verir. Hız-zaman grafiğinde K çizgisi eksenin üstünde +ϑ, L çizgisi eksenin '
               'altında −ϑ değerinde yataydır; çizgi ile zaman ekseni arasındaki alan yer değiştirmeyi verir: K için Δx = ϑ · t, L için Δx = −ϑ · t.')


def dron_grafigi():
    """Örnek 2: dronun ϑ-t grafiği, (0-6) s +5 m/s, (6-10) s −3 m/s. Alanlar yalnız I ve II ile adlandırılır (cevap görselde yok)."""
    W, H = 440, 184
    ic = '<defs>' + _gri_ok('fz10okD') + '</defs>'
    ox, oy, px_s, px_v = 62, 104, 30, 12
    t6, t10 = ox + 6 * px_s, ox + 10 * px_s          # 242, 362
    y5, ym3 = oy - 5 * px_v, oy + 3 * px_v             # 44, 140
    ic += f'<rect x="{ox}" y="{y5}" width="{t6 - ox}" height="{oy - y5}" class="{MAVI[0]}"/>'
    ic += f'<rect x="{t6}" y="{oy}" width="{t10 - t6}" height="{ym3 - oy}" class="{TURUNCU[0]}"/>'
    ic += _eksen(ox, oy, 20, 170, 394, 'fz10okD')
    ic += f'<text x="{ox + 8}" y="24" font-size="12" class="g-y">ϑ (m/s)</text>'
    ic += '<text x="404" y="108" font-size="12" class="g-y">t (s)</text>'
    ic += f'<line x1="{t6}" y1="{y5}" x2="{t6}" y2="154" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += f'<line x1="{t10}" y1="{oy}" x2="{t10}" y2="154" class="g-c" stroke-width="1.5" stroke-dasharray="4 4"/>'
    ic += f'<line x1="{ox}" y1="{y5}" x2="{t6}" y2="{y5}" class="{MAVI[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<line x1="{t6}" y1="{ym3}" x2="{t10}" y2="{ym3}" class="{TURUNCU[1]}" stroke-width="3" stroke-linecap="round"/>'
    ic += f'<text x="{ox - 7}" y="{y5 + 4}" text-anchor="end" font-size="12" class="g-y">5</text>'
    ic += f'<text x="{ox - 7}" y="{oy + 4}" text-anchor="end" font-size="12" class="g-y">0</text>'
    ic += f'<text x="{ox - 7}" y="{ym3 + 4}" text-anchor="end" font-size="12" class="g-y">−3</text>'
    ic += f'<text x="{t6}" y="170" text-anchor="middle" font-size="12" class="g-y">6</text>'
    ic += f'<text x="{t10}" y="170" text-anchor="middle" font-size="12" class="g-y">10</text>'
    ic += f'<text x="{(ox + t6) / 2:.0f}" y="80" text-anchor="middle" font-size="14" font-weight="800" class="{MAVI[2]}">I</text>'
    ic += f'<text x="{(t6 + t10) / 2:.0f}" y="127" text-anchor="middle" font-size="13" font-weight="800" class="{TURUNCU[2]}">II</text>'
    return svg(W, H, ic, 'Dronun hız-zaman grafiği: 0 ile 6. saniye arasında hız +5 m/s (I. bölge, eksenin üstünde), '
               '6. ile 10. saniye arasında hız −3 m/s (II. bölge, eksenin altında).')


def uygula(o):
    g = {'Sabit hızlı hareket nedir?': esit_yer_degistirme(),
         'Konum-zaman ve hız-zaman grafikleri': iki_grafik()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
    for x in o.get('ornekler', []):
        if 'dronun ϑ-t grafiği' in x['soru']:
            x['gorsel'] = dron_grafigi()
