# -*- coding: utf-8 -*-
"""10-fizik-7 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket, en_fazla=32):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 360 115"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.5, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 76, a, c, 6, 0.75)
        ic += yazi(x + 40, 48, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="58" x2="{x + 72}" y2="58" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 78, d, 7.5, LAC, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket):
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, MAVI)
    ic += kutu(14, 28, 160, 76, '#f8fafc', MAVI, 6, 0.75)
    ic += yazi(94, 48, sol_b, 9, MAVI)
    ic += yazi(94, 68, sol_d1, 8, LAC, ince=True)
    ic += yazi(94, 88, sol_d2, 7.5, SOLUK, ince=True)
    ic += kutu(186, 28, 160, 76, '#f8fafc', TUR, 6, 0.75)
    ic += yazi(266, 48, sag_b, 9, TUR)
    ic += yazi(266, 68, sag_d1, 8, LAC, ince=True)
    ic += yazi(266, 88, sag_d2, 7.5, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [MAVI, TUR, MOR]
    for i, (b, d1, d2) in enumerate(uclu):
        c = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 54, 48, b, 8.8, c)
        ic += yazi(x + 54, 68, d1, 7.8, LAC, ince=True)
        ic += yazi(x + 54, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)

def g0():
    return kart4('SERBEST DÜŞME TEMEL BAĞINTILARI', [('İlk Hız', 'v₀ = 0 (Serbest)'), ('İvme Sabit', 'a = g = 10 m/s²'), ('Anlık Hız', 'v = g · t = 10t'), ('Düşey Yol', 'h = ½g·t² = 5t²')], '10-fizik-7 temel bagintilar')

def g1():
    return karsilastir2('HAVASIZ ORTAMDA KÜTLE BAĞIMSIZLIĞI', 'Demir Gülle (m₁ = 10 kg)', 'Etki eden kuvvet: G₁ = m₁·g', 'İvme: a₁ = G₁ / m₁ = g', 'Kuş Tüyü (m₂ = 2 g)', 'Etki eden kuvvet: G₂ = m₂·g', 'İvme: a₂ = G₂ / m₂ = g (Aynı anda!)', '10-fizik-7 galileo deneyi')

def g2():
    return karsilastir2('TOPLAM SÜRE İLE O SANİYE İÇİNDEKİ YOL', 't Saniye SONUNDA Toplam Yol', 'h = 5·t² (1 s->5 m, 2 s->20 m,', '3 s->45 m, 4 s->80 m, 5 s->125 m)', 'n. Saniye İÇİNDE Alınan Yol', 'Δh = 5 m, 15 m, 25 m, 35 m, 45 m', 'Örn: Yalnız 4. sn içinde 35 m!', '10-fizik-7 saniye farki')

def g3():
    return uclu_sema('SERBEST DÜŞME HAREKET GRAFİKLERİ (- YÖN)', [('İvme-Zaman (a-t)', 'a = -g sabit doğru', 'Alan -> Hız değişimi (Δv)'), ('Hız-Zaman (v-t)', 'Orijinden eğimi -g doğru', 'Alan -> Düşey yol (-h)'), ('Konum-Zaman (y-t)', 'Eğimi artan parabol', 'Eğim -> Anlık hız (v)')], '10-fizik-7 grafikler')

def g5():
    return kart4('SANİYE SANİYE HIZ VE TOPLAM YÜKSEKLİK', [('t = 1 s Sonu', 'v = 10 m/s | h = 5 m'), ('t = 2 s Sonu', 'v = 20 m/s | h = 20 m'), ('t = 3 s Sonu', 'v = 30 m/s | h = 45 m'), ('t = 4 s Sonu', 'v = 40 m/s | h = 80 m')], '10-fizik-7 saniye tablosu')

def g6():
    return uclu_sema('GALİLEO TEK SAYILAR KURALI (h - 3h - 5h)', [('0 - t Aralığı', 'Alınan yol: h (5 m)', 'Son hız: v (10 m/s)'), ('t - 2t Aralığı', 'Alınan yol: 3h (15 m)', 'Toplam yol: 4h (20 m)'), ('2t - 3t Aralığı', 'Alınan yol: 5h (25 m)', 'Toplam yol: 9h (45 m)')], '10-fizik-7 tek sayilar')

def g8():
    return kart4('ZAMANSIZ HIZ VE ORTALAMA HIZ (g=10)', [('h = 20 m -> t = 2 s', 'v = 20 m/s, v_ort = 10'), ('h = 45 m -> t = 3 s', 'v = 30 m/s, v_ort = 15'), ('h = 80 m -> t = 4 s', 'v = 40 m/s, v_ort = 20'), ('h = 180 m -> t = 6 s', 'v = 60 m/s, v_ort = 30')], '10-fizik-7 sayisal degerler')

def g11():
    return karsilastir2('KUYUYA BIRAKILAN TAŞ PROBLEMİ (t = 3 s)', 'Kuyunun Derinliği (h)', 'h = ½ · g · t² = 5 · 3² = 45 m', 'Ardışık yollar: 5 + 15 + 25 = 45 m', 'Çarpma Hızı ve Ortalama Hız', 'Son hız: v = g · t = 10 · 3 = 30 m/s', 'Ortalama hız: v_ort = (0 + 30)/2 = 15 m/s', '10-fizik-7 kuyu problemi')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
