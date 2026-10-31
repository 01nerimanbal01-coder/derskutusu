"""6. sınıf Sosyal Bilgiler 4. hafta (toplumsal sorunlar ve çözüm önerileri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048; karınca ve nesneler var); görsel içi yazı sayfa puntosunda (K150 EK); kesir yok (K155)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


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


def harf(x, y, h, renk=LAC):
    return f'<rect x="{x - 9}" y="{y - 9}" width="18" height="18" rx="4" fill="{renk}"/>' + yazi(x, y + 4.5, h, 11.5, '#fff')


def durum_kartlari():
    """Dört durum kartı: A ve C toplumsal, B ve D bireysel."""
    kartlar = [('A', ['Bir ilçede hava kirliliği', 'her yıl artıyor.'], MAVI, MAVI_A), ('B', ['Ece’nin bisikletinin', 'lastiği patladı.'], TUR, TUR_A),
               ('C', ['Bir ilde içme suyu', 'günlerdir kesik.'], YES, YES_A), ('D', ['Bir öğrenci ödevini', 'evde unuttu.'], MOR, MOR_A)]
    ic = ''
    for i, (h, m, renk, zemin) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 46
        ic += kutu(x, y, 172, 40, zemin, renk, 7, 1.3) + harf(x + 16, y + 20, h, renk) + duz(x + 32, y + 17, m, 11.5, LAC, 'start', 14)
    return svg(360, 96, ic, 'Dört kart. A: Bir ilçede hava kirliliği her yıl artıyor. B: Ece’nin bisikletinin lastiği patladı. C: Bir ilde içme suyu günlerdir kesik. D: Bir öğrenci ödevini evde unuttu.', 24)


def vakif_kartlari():
    """Üç vakfiye kartı: yer ve yıl."""
    veri = [(['Bulaşıcı Hastalıkları', 'Tedavi Vakfı'], 'Sivas · 1321', MAVI), (['İsrafı Önleyen', 'Vakıf'], 'İstanbul · 1613', YES), (['Afet Sonrası Bakım', 've Onarım Vakfı'], 'İstanbul · 1549', TUR)]
    ic = ''
    for i, (ad, yer, renk) in enumerate(veri):
        x = 4 + i * 119
        ic += f'<path d="M{x + 4} 10 h106 a4 4 0 0 1 4 4 v62 a4 4 0 0 1 -4 4 h-106 a4 4 0 0 1 -4 -4 v-62 a4 4 0 0 1 4 -4 z" fill="{KUM}" stroke="{KAHVE}" stroke-width="1.3"/>'
        ic += f'<rect x="{x}" y="6" width="114" height="8" rx="4" fill="{KAHVE}"/><rect x="{x}" y="78" width="114" height="8" rx="4" fill="{KAHVE}"/>'
        ic += ''.join(yazi(x + 57, 34 + k * 14, m, 9.8, LAC) for k, m in enumerate(ad)) + yazi(x + 57, 70, yer, 11, renk)
    return svg(360, 92, ic, 'Üç vakfiye kartı: Bulaşıcı Hastalıkları Tedavi Vakfı, Sivas 1321. İsrafı Önleyen Vakıf, İstanbul 1613. Afet Sonrası Bakım ve Onarım Yapan Vakfı, İstanbul 1549.', 23)


def karinca():
    """Su üstünde ateş karıncalarının salı: dalgalar, birbirine tutunan karıncalar (yarısı suyun altında)."""
    ic = f'<rect x="4" y="4" width="352" height="100" rx="8" fill="#dff0fb"/>'
    ic += f'<path d="M4 58 q20 -8 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 V104 H4 Z" fill="#8fc7ef"/>'
    ic += f'<path d="M4 58 q20 -8 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" fill="none" stroke="{MAVI}" stroke-width="1.5"/>'

    def ant(cx, cy, a=0):
        return (f'<g transform="rotate({a} {cx} {cy})"><ellipse cx="{cx - 6}" cy="{cy}" rx="4" ry="3" fill="#b3321b"/><ellipse cx="{cx}" cy="{cy}" rx="3.2" ry="2.6" fill="#b3321b"/>'
                f'<ellipse cx="{cx + 6}" cy="{cy}" rx="4.2" ry="3.2" fill="#8c2612"/>'
                f'<path d="M{cx - 2} {cy - 2} l-3 -5 M{cx} {cy - 2} l0 -6 M{cx + 2} {cy - 2} l3 -5 M{cx - 2} {cy + 2} l-3 5 M{cx} {cy + 2} l0 6 M{cx + 2} {cy + 2} l3 5" stroke="#5a1a0c" stroke-width="1"/></g>')
    sal = []
    for r in range(3):
        for k in range(7 - r):
            sal.append((110 + k * 20 + r * 10, 66 - r * 9, (k * 37) % 40 - 20))
    for cx, cy, a in sal:
        ic += ant(cx, cy, a)
    ic += f'<path d="M100 72 q70 14 150 0" fill="none" stroke="#b3321b" stroke-width="2" stroke-dasharray="3 3" opacity=".6"/>'
    ic += yazi(180, 96, 'ateş karıncalarının salı · yarısı suyun üstünde, yarısı altında', 11, '#1d4e89')
    ic += f'<rect x="12" y="12" width="80" height="18" rx="4" fill="#fff" opacity=".85"/>' + yazi(52, 25, 'su baskını', 11, MAVI)
    return svg(360, 108, ic, 'Mavi suyun üstünde birbirine tutunan ateş karıncalarından oluşan üçgen biçimli sal; salın yarısı suyun üstünde, yarısı altında. Köşede su baskını etiketi.', 28)


def toytos():
    """TOYTOS: yangın tehlike haritası ve erken uyarı."""
    ic = kutu(4, 4, 232, 104, '#fff', GRI, 8, 1.2) + yazi(120, 20, 'TOYTOS · yangın tehlike haritası', 11.5, LAC)
    ic += f'<path d="M20 42 q40 -16 80 -6 t70 -4 t50 8 v34 q-40 8 -80 2 t-70 4 t-50 -6 z" fill="#e9f3dc" stroke="#7aa05a" stroke-width="1.2"/>'
    for cx, cy, r, c in [(60, 56, 14, KIR), (120, 62, 11, TUR), (174, 52, 11, KIR), (202, 66, 8, TUR)]:
        ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".75"/>'
    ic += f'<rect x="20" y="90" width="10" height="8" rx="2" fill="#e9f3dc" stroke="#7aa05a" stroke-width="1"/>' + yazi(34, 97, 'ormanlık alan', 9.5, SOLUK, 'start')
    ic += ''.join(f'<rect x="{x}" y="90" width="10" height="8" rx="2" fill="{c}"/>' + yazi(x + 14, 97, m, 9.5, SOLUK, 'start') for x, c, m in [(118, KIR, 'yüksek'), (174, TUR, 'orta')])
    ic += kutu(246, 4, 110, 104, TUR_A, TUR, 8, 1.4) + yazi(301, 21, 'Erken uyarı', 11.5, TUR)
    ic += f'<path d="M301 32 q-15 0 -15 16 v10 l-5 7 h40 l-5 -7 v-10 q0 -16 -15 -16 z" fill="{ALTIN}" stroke="{KAHVE}" stroke-width="1.2"/><circle cx="301" cy="69" r="3.8" fill="{KAHVE}"/>'
    ic += duz(301, 86, ['riskli bölge önceden'], 9.8, LAC, 'middle') + duz(301, 98, ['bildirilir'], 9.8, LAC, 'middle')
    return svg(360, 112, ic, 'TOYTOS yangın tehlike haritası: ormanlık alan üzerinde kırmızı yüksek ve turuncu orta risk bölgeleri. Yanda zil simgesiyle erken uyarı kartı: riskli bölge önceden bildirilir.', 28)


def goc_grafik():
    """Dünyada başka ülkede yaşayanların sayısı (milyon): 1970-2020."""
    veri = [(1970, 84), (1980, 102), (1990, 153), (2000, 173), (2010, 221), (2015, 248), (2019, 272), (2020, 281)]
    x0, x1, y0, h = 44, 336, 112, 76
    ic = yazi(180, 15, 'Doğduğu ülkeden başka ülkede yaşayanlar (milyon kişi)', 11)
    ic += f'<line x1="{x0}" y1="{y0 - h - 6}" x2="{x0}" y2="{y0}" stroke="{SOLUK}" stroke-width="1.2"/><line x1="{x0}" y1="{y0}" x2="{x1 + 8}" y2="{y0}" stroke="{SOLUK}" stroke-width="1.2"/>'
    for v in (0, 100, 200, 300):
        y = y0 - v * h / 300
        ic += f'<line x1="{x0 - 3}" y1="{y:.1f}" x2="{x1 + 8}" y2="{y:.1f}" stroke="{GRI_A}" stroke-width="1"/>' + yazi(x0 - 6, y + 4, str(v), 10.5, SOLUK, 'end')
    nok = []
    for yil, v in veri:
        x = x0 + (yil - 1970) * (x1 - x0) / 50
        y = y0 - v * h / 300
        nok.append(f'{x:.1f},{y:.1f}')
    ic += f'<polyline points="{" ".join(nok)}" fill="none" stroke="{MAVI}" stroke-width="2.2"/>'
    for (yil, v), p in zip(veri, nok):
        x, y = map(float, p.split(','))
        ic += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{MAVI}"/>'
        if yil not in (2015, 2019):
            ic += yazi(x, y - 7, str(v), 10, LAC) + yazi(x, y0 + 14, str(yil), 10.5, SOLUK)
    return svg(360, 132, ic, 'Çizgi grafiği, doğduğu ülkeden başka ülkede yaşayanlar, milyon kişi: 1970’te 84, 1980’de 102, 1990’da 153, 2000’de 173, 2010’da 221, 2015’te 248, 2019’da 272, 2020’de 281.', 33)


def israf_grafik():
    """Evlerde bir yılda israf edilen gıda (milyon ton, 2024): Çin, Hindistan, ABD, Brezilya."""
    veri = [('Çin', 108.7, KIR), ('Hindistan', 78.2, TUR), ('ABD', 24.7, MAVI), ('Brezilya', 20.3, YES)]
    tx, ty, h = 50, 104, 74
    ic = yazi(190, 14, 'Evlerde bir yılda israf edilen gıda (milyon ton, 2024)', 11.5)
    ic += f'<line x1="{tx}" y1="{ty - h - 4}" x2="{tx}" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/><line x1="{tx}" y1="{ty}" x2="344" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/>'
    for v in (0, 40, 80, 120):
        y = ty - v * h / 120
        ic += f'<line x1="{tx - 3}" y1="{y:.1f}" x2="344" y2="{y:.1f}" stroke="{GRI_A}" stroke-width="1"/>' + yazi(tx - 6, y + 4, str(v), 10.5, SOLUK, 'end')
    for i, (ad, v, c) in enumerate(veri):
        x = tx + 20 + i * 72
        yuk = v * h / 120
        ic += f'<rect x="{x}" y="{ty - yuk:.1f}" width="40" height="{yuk:.1f}" rx="3" fill="{c}"/>' + yazi(x + 20, ty - yuk - 4, str(v).replace('.', ','), 11, LAC) + yazi(x + 20, ty + 15, ad, 11.5)
    return svg(360, 124, ic, 'Sütun grafiği, evlerde bir yılda israf edilen gıda, milyon ton, 2024: Çin 108,7; Hindistan 78,2; ABD 24,7; Brezilya 20,3.', 31)


def oneri_karti():
    """Bir grubun çözüm önerisi kartı ve dört ölçüt kutusu."""
    ic = kutu(4, 4, 352, 104, KUM, GRI, 8, 1.2) + f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19.5, 'GRUP ÖNERİSİ · okulda atık sorunu', 11.5, '#fff')
    ic += duz(16, 44, ['Yılda bir gün “Atık Günü” düzenleyelim: o gün herkes', 'evdeki plastik ve kâğıt atıkları okula getirsin,', 'toplananlar geri dönüşüme gönderilsin.'], 12, LAC, 'start', 15)
    konumlar = [(12, 'özgün'), (74, 'uygulanabilir'), (164, 'sürdürülebilir'), (256, 'toplumsal fayda')]
    for x, m in konumlar:
        ic += f'<rect x="{x}" y="86" width="12" height="12" rx="3" fill="#fff" stroke="{SOLUK}" stroke-width="1.2"/>' + yazi(x + 16, 95.5, m, 9.5, SOLUK, 'start')
    return svg(360, 112, ic, 'Grup önerisi kartı, okulda atık sorunu: Yılda bir gün Atık Günü düzenleyelim; o gün herkes evdeki plastik ve kâğıt atıkları okula getirsin, toplananlar geri dönüşüme gönderilsin. Altta dört boş ölçüt kutusu: özgün, uygulanabilir, sürdürülebilir, toplumsal fayda.', 28)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = durum_kartlari()
    s[1]['gorsel'] = vakif_kartlari()
    s[2]['gorsel'] = karinca()
    s[3]['gorsel'] = toytos()
    s[5]['gorsel'] = goc_grafik()
    s[6]['gorsel'] = israf_grafik()
    s[8]['gorsel'] = oneri_karti()
