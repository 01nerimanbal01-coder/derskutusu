"""11. sınıf Fizik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return cizelge4([('fs,max = ks · N', 'Statik eşik sınırı', MAVI, MAVI_A), ('a = g · sin α', 'Sürtünmesiz eğik ivme', YES, YES_A), ('g(sin α - k cos α)', 'Sürtünmeli iniş ivmesi', TUR, TUR_A), ('N = Fyatay', 'Düşey duvar tepkisi', MOR, MOR_A)], 'Sürtünme ve eğik düzlem bağıntıları')
def g1():
    return ikili('DURGUN SANDIKTA STATİK SÜRTÜNME ANALİZİ', 'Verilenler: m = 5 kg, ks = 0,4', 'N = 50 N  =>  fs,max = 0,4 · 50 = 20 N', 'Uygulanan Kuvvet: F = 15 N', '15 N < 20 N (Durur) => fs = 15 N', MAVI, MAVI_A, YES, YES_A, 'Statik sürtünme kuvveti hesabı')
def g2():
    return kart('SÜRTÜNMELİ EĞİK DÜZLEMDE ÇIKIŞ VE İNİŞ İVMELERİ', 'Yukarı Çıkış (Yavaşlama): a_çıkış = g · (sin α + k · cos α) -> Daha Büyük', 'Aşağı İniş (Hızlanma): a_iniş = g · (sin α - k · cos α) -> Daha Küçük', TUR, TUR_A, 'Eğik düzlem çıkış ve iniş ivmesi farkı')
def g3():
    return cizelge4([('fs,max > fk', 'Statik > Kinetik sürtünme', MAVI, MAVI_A), ('Kütle Bağımsız', 'Eğik düzlem ivmesi', YES, YES_A), ('Atwood İvmesi', 'Eşit büyüklükte ortak a', TUR, TUR_A), ('Düşey Duvar', 'Normal kuvvet N = F', MOR, MOR_A)], 'Dinamik kuralları özeti')
def g5():
    return akis4([('1. Ağırlıklar', 'G1 = 80 N, G2 = 20 N', YES, YES_A), ('2. Net Kuvvet', 'Fnet = 80 - 20 = 60 N', MAVI, MAVI_A), ('3. Ortak İvme', 'a = 60 / 10 = 6 m/s²', TUR, TUR_A), ('4. İp Gerilmesi', 'T = 20 + 2·6 = 32 N', MOR, MOR_A)], 'Atwood düzeneği çözüm basamakları')
def g6():
    return ikili('YATAY MASA VE SARKAN KÜTLE SİSTEMİ', 'Sistem: m1 = 3 kg (Masa), m2 = 2 kg', 'Fnet = 20 N => a = 20 / 5 = 4 m/s²', 'İp Gerilmesi (m1 Üzerinden)', 'T = m1 · a = 3 · 4 = 12 N', CAM, CAM_A, MAVI, MAVI_A, 'Masadan sarkan bağlı sistem çözümü')
def g7():
    return kart('EĞİK DÜZLEM TEPKİSİ VE BAĞLI SİSTEM ÖZELLİKLERİ', 'Yüzeye dik tepki: N = m · g · cos α  |  İp gerilmeleri iç kuvvettir.', 'Sürtünmeli eğik düzlemde çıkış süresi iniş süresinden daha kısadır.', YES, YES_A, 'Eğik düzlem ve ip gerilmesi özeti')
def g8():
    return cizelge4([('Gx = mg sin α', 'Paralel kaydırıcı bileşen', MAVI, MAVI_A), ('Gy = mg cos α', 'Yüzeye dik bileşen (N)', YES, YES_A), ('g(sin α + k cos α)', 'Yukarı çıkış yavaşlama', TUR, TUR_A), ('m2·g < T < m1·g', 'Atwood ip gerilme aralığı', MOR, MOR_A)], 'Dinamik bileşenler ve aralıklar')

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
