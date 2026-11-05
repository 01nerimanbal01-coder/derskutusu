# -*- coding: utf-8 -*-
"""10-fizik-8 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="width:100%;max-height:24mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 80, 78, a, c, 6, 0.75)
        ic += yazi(x + 40, 44, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 72}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 69, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, c1)
    ic += kutu(12, 26, 162, 78, a1, c1, 6, 0.75)
    ic += yazi(93, 44, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="52" x2="164" y2="52" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 70, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 89, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 26, 162, 78, a2, c2, 6, 0.75)
    ic += yazi(267, 44, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="52" x2="338" y2="52" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 70, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 89, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 26, 108, 78, a, c, 6, 0.75)
        ic += yazi(x + 54, 44, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 100}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 70, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 89, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM, arka_renk=CAM_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 78, 78, a, c, 6, 0.75)
        ic += yazi(x + 39, 44, b, 8.3, c)
        ic += yazi(x + 39, 68, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39, 88, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+80},64 {x+85},60 {x+85},68" fill="{ana_renk}"/>'
    return svg(ic, etiket)


def g0():
    return kart4('FİZİKSEL İŞ, ENERJİ VE MEKANİK GÜÇ MODELLERİ', [
        ('Fiziksel İş (W)', 'W = F · Δx', 'Birim: Joule (N·m)'),
        ('Net İş (W_net)', 'W_net = F_net · Δx', 'Skaler büyüklüktür'),
        ('İş-Enerji Teoremi', 'W_net = ΔE_k', 'E_k,son - E_k,ilk'),
        ('Mekanik Güç (P)', 'P = W / t = F · v', 'Birim: Watt (J/s)')
    ], '10-fizik-8 iş enerji güç modelleri')

def g1():
    return karsilastir2('SÜRTÜNMELİ YATAY DÜZLEMDE NET İŞ HESABI',
        'Kuvvetler ve Yer Değiştirme (Δx = 5 m)', 'Uygulanan Kuvvet: F = 30 N (+x yönü)', 'Sürtünme Kuvveti: f_s = 10 N (-x yönü)',
        'İşlerin Hesaplanması', 'W_F = 30 · 5 = +150 J | W_s = -10 · 5 = -50 J', 'W_net = (30 - 10) · 5 = +100 Joule',
        '10-fizik-8 net iş hesabı')

def g2():
    return uclu_sema('FİZİKSEL ANLAMDA İŞİN GERÇEKLEŞME ŞARTLARI', [
        ('Pozitif İş (+W)', 'F ile Δx aynı yönlü', 'Enerjiyi artırır'),
        ('Negatif İş (-W)', 'F ile Δx zıt yönlü', 'Sürtünme ısıya çevirir'),
        ('İş Yapılmaz (W=0)', 'Δx = 0 veya F ⊥ Δx', 'Sabit duvar, yatay taşıma')
    ], '10-fizik-8 işin şartları')

def g4():
    return karsilastir2('KUVVET-YER DEĞİŞTİRME (F-x) GRAFİĞİ ALANI',
        '1. Bölge (0 - 4 m Aralığı)', 'Sabit F₁ = +20 N kuvvet etki ediyor', 'Alan₁ = W₁ = 20 · 4 = +80 Joule',
        '2. Bölge (4 - 6 m Aralığı)', 'Zıt yönlü F₂ = -10 N kuvvet etki ediyor', 'Alan₂ = -10 · 2 = -20 J -> W_net = 60 J',
        '10-fizik-8 F-x grafiği alanı')

def g6():
    return karsilastir2('AYNI İŞİ YAPAN A VE B VİNÇLERİNİN GÜÇ ANALİZİ',
        'A Vinci (W_A = 2000 J, t_A = 4 s)', 'P_A = W_A / t_A = 2000 / 4 = 500 Watt', 'Aynı işi daha kısa sürede yapar',
        'B Vinci (W_B = 2000 J, t_B = 10 s)', 'P_B = W_B / t_B = 2000 / 10 = 200 Watt', 'W_A = W_B iken P_A > P_B olur',
        '10-fizik-8 mekanik güç karşılaştırması')

def g7():
    return akis4('F-x GRAFİĞİNDEN SON KİNETİK ENERJİYİ BULMA', [
        ('1. Üst Alan', '+W₁ pozitif işi', 'dikdörtgen/üçgenden bul'),
        ('2. Alt Alan', '-W₂ negatif işi', 'eksen altından bul'),
        ('3. Net İş', 'W_net = W₁ - W₂', 'cebirsel toplam al'),
        ('4. Kinetik Enerji', 'E_son = E_ilk + W_net', 'İş-Enerji Teoremi')
    ], '10-fizik-8 F-x grafiği çözüm adımları')

def g8():
    return karsilastir2('İŞ-ENERJİ TEOREMİ UYGULAMASI (W_net = ΔE_k)',
        'Başlangıç Durumu ve Net İş', 'E_k,ilk = 30 Joule | F_net = 25 N, Δx = 4 m', 'Yapılan Net İş: W_net = 25 · 4 = 100 J',
        'Son Kinetik Enerji Hesabı', 'W_net = E_k,son - E_k,ilk -> 100 = E_son - 30', 'E_k,son = 30 + 100 = 130 Joule',
        '10-fizik-8 iş enerji teoremi hesabı')

def g11():
    return uclu_sema('GÜNLÜK HAYATTA FİZİKSEL İŞ ANALİZİ', [
        ('Market Arabası İtme', 'F ve Δx yatay paralel', 'Fiziksel iş yapılır (W>0)'),
        ('Duvarı İtme', 'Kuvvet var ama Δx = 0', 'Fiziksel iş yapılmaz (W=0)'),
        ('Yatayda Çanta Taşıma', 'F düşey, Δx yatay (F⊥Δx)', 'Düşey kuvvet iş yapmaz')
    ], '10-fizik-8 günlük hayat iş örnekleri')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[4]['gorsel'] = g4()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
