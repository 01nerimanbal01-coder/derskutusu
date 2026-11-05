"""12. sınıf Matematik 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.8, kc) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Üstel ve logaritmik gerçek hayat modelleri', [('Richter Ölçeği', 'M = log(I / I0)', KIR, KIR_A), ('pH Ölçeği', 'pH = -log[H+]', TUR, TUR_A), ('Desibel (dB)', 'L = 10.log(I / I0)', MOR, MOR_A), ('Yarı Ömür', 'M = M0.(1/2)^(t/T)', YES, YES_A)])

def g1():
    return uclu('Richter deprem büyüklüğü ve genlik oranı', 'RİCHTER DEPREM ÖLÇEĞİ · YOĞUNLUK ORANI HESABI', ('1. Deprem: M1=7,2', 'Yoğunluk: I1', KIR, KIR_A), ('2. Deprem: M2=5,2', 'Fark: 7,2 - 5,2 = 2', TUR, TUR_A), ('Yoğunluk Oranı', 'I1 / I2 = 10² = 100 kat', YES, YES_A), MAVI, MAVI_A)

def g2():
    return pano('Sürekli üstel büyüme modelinde t zamanını bulma', 'ÜSTEL BÜYÜME DENKLEMİNDE ZAMANI (t) LOGARİTMAYLA ÇÖZME', 'P(t) = P0 . e^(0,05.t) = 3.P0  -->  e^(0,05.t) = 3  -->  0,05.t = ln 3', 'Her iki tarafın doğal logaritması (ln) alınarak t = ln 3 / 0,05 = 20.ln 3 bulunur.', MOR, MOR_A, '#f5f0ff')

def g3():
    return kart4('Üstel büyüme, azalma, pH ve desibel özellikleri', [('k > 0 / k < 0', 'Büyüme / Azalma', MAVI, MAVI_A), ('Yarı Ömür', 'Asla sıfırlanmaz', TUR, TUR_A), ('[H+] Artarsa', 'pH küçülür (Asit)', YES, YES_A), ('Eşik I = I0', 'L = 10.log(1) = 0 dB', MOR, MOR_A)])

def g5():
    return akis4('Karbon-14 arkeolojik yaş tayini çözüm basamakları', [('1. Model Kur', 'M = M0.(1/2)^(t/T)', MAVI, MAVI_A), ('2. Oran Yaz', 'M / M0 = 1/4 = (1/2)²', TUR, TUR_A), ('3. Üs Eşitle', 't / 5730 = 2', MOR, MOR_A), ('4. Sonuç Bul', 't = 11.460 yıl', YES, YES_A)])

def g6():
    return pano('Ses şiddeti düzeyi desibel kat artışı', 'SES ŞİDDETİ DÜZEYİ (DESİBEL) · ÇOKLU KAYNAK HESABI', '1 Makine: L1 = 10.log(I / I0) = 60 dB  |  100 Makine: I_yeni = 100 . I', 'L_yeni = 60 + 10.log(100) = 60 + 10.2 = 80 dB (Şiddet 100 kat -> +20 dB).', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Yarı ömür, asidik pH ve doğal logaritma özeti', 'RADYOAKTİF BOZUNMA, pH VE DOĞAL LOGARİTMA (ln)', 'Yarı Ömür (T)  ·  pH < 7 Asidik Çözelti  ·  e Tabanında Doğal Logaritma (ln)', 'Üstel denklemlerde taban e ise ln, taban 10 ise bayağı logaritma (log) kullanılır.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Logaritmik ölçeklerde kat değişimleri', [('Richter +3', '10³ = 1000 kat genlik', KIR, KIR_A), ('pH -2 Azalma', '10² = 100 kat [H+]', TUR, TUR_A), ('Ses +30 dB', '10³ = 1000 kat şiddet', MOR, MOR_A), ('3 Yarı Ömür', '(1/2)³ = 1/8 kütle', MAVI, MAVI_A)])

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
