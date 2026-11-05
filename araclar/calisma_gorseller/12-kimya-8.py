"""12. sınıf Kimya 8. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.5, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Lityum iyon ve galvanik pil bileşenleri', [('Grafit Anot', 'Li tutan karbon', MAVI, MAVI_A), ('CoO₂ Katot', 'Metal oksit katot', MOR, MOR_A), ('Katı Polimer', 'Susuz elektrolit', YES, YES_A), ('Elektrot Kütlesi', 'Yalnız ömrü etkiler', TUR, TUR_A)])

def g1():
    return pano('Mg-Ag pilinde Le Chatelier denge etkisi', 'DENGE: Mg(k) + 2Ag⁺(Katot) ⇌ Mg²⁺(Anot) + 2Ag(k) + ISI', 'Katot kabına AgNO₃ eklemek → [Ag⁺] artar → Denge ürünlere kayar → E_pil ARTAR', 'Anot kabına su eklemek veya sistemi soğutmak da E_pil gerilimini artırır.', YES, YES_A, '#eaf8f0')

def g2():
    return uclu('Lityum iyon pilinin üstünlükleri', 'LİTYUM İYON PİLLERİNİN TEMEL ÜSTÜNLÜKLERİ', ('E°_yüks = +3,04 V', 'En yüksek potansiyel', KIR, KIR_A), ('Düşük Mol Kütlesi', 'Çok hafif ve kompakt', MAVI, MAVI_A), ('Tekrar Şarj (3,4 V)', 'Geniş sıcaklık aralığı', YES, YES_A), MOR, MOR_A)

def g3():
    return kart4('Pil potansiyelini etkileyen faktörler', [('Aktiflik Farkı', 'Artarsa E_pil artar', YES, YES_A), ('Isıtma Etkisi', 'Ekzotermik: E azalır', KIR, KIR_A), ('Susuz Polimer', 'Li suyla tepkime verir', MOR, MOR_A), ('Çözelti Hacmi', 'Sabit derişimde aynı', MAVI, MAVI_A)])

def g5():
    return akis4('Lityum iyon pili deşarj basamakları', [('1. Anot (Grafit)', 'Li → Li⁺ + e⁻', MAVI, MAVI_A), ('2. Dış Devre', 'Elektron akışı', TUR, TUR_A), ('3. Elektrolit', 'Li⁺ katoda göçer', CAM, CAM_A), ('4. Katot (CoO₂)', 'LiCoO₂ oluşumu', MOR, MOR_A)])

def g6():
    return uclu('X, Y ve Z metalleriyle kurulan pillerin gerilimleri', 'İNDİRGENME POTANSİYELLERİ: X(-1,66 V) · Y(-0,44 V) · Z(+0,34 V)', ('X - Z Pili', '1,66 + 0,34 = 2,00 V', KIR, KIR_A), ('X - Y Pili', '1,66 - 0,44 = 1,22 V', TUR, TUR_A), ('Y - Z Pili', '0,44 + 0,34 = 0,78 V', MAVI, MAVI_A), MAVI, MAVI_A)

def g7():
    return uclu('Lityum, ekzotermik denge ve pil ömrü', 'ELEKTROKİMYASAL PİL ÖZELLİKLERİ', ('Lityum (-3,04 V)', 'En aktif metal', MOR, MOR_A), ('Ekzotermik Pil', 'Soğutulursa E artar', YES, YES_A), ('Yüzey Alanı', 'Pil ömrünü etkiler', TUR, TUR_A), YES, YES_A)

def g8():
    return kart4('Lityum iyon pili tepkimeleri', [('Anot Tepkimesi', 'Li(k) → Li⁺ + e⁻', MAVI, MAVI_A), ('Katot Tepkimesi', 'Li⁺+CoO₂+e⁻→LiCoO₂', MOR, MOR_A), ('Net Tepkime', 'Li + CoO₂ → LiCoO₂', YES, YES_A), ('Çalışma Aralığı', '10 °C - 55 °C verim', TUR, TUR_A)])

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
