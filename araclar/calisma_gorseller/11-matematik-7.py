"""11. sınıf Matematik 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return cizelge4([('|KL| = |a-c|/2', 'Köşegenler arası orta parça', MAVI, MAVI_A), ('h² = a · c', 'Dik yamukta dik köşegen', YES, YES_A), ('S² = Salt · Süst', 'Yamukta köşegen alanları', TUR, TUR_A), ('Alan(AEB) = A/2', 'Paralelkenarda yarı alan', MOR, MOR_A)], 'Yamuk ve paralelkenar bağıntıları')
def g1():
    return ikili('YAMUKTA KÖŞEGENLERİN ALAN PAYLAŞIMI', 'Üst Alan = 9 cm² · Alt Alan = 25 cm²', 'Yan Alanlar: S² = 9 · 25 = 225 => S = 15 cm²', 'Tüm Yamuğun Alanı', 'Alan = 9 + 25 + 15 + 15 = 64 cm²', MAVI, MAVI_A, YES, YES_A, 'Yamukta köşegen alan hesabı')
def g2():
    return kart('PARALELKENARDA ARDIŞIK AÇIORTAYLARIN DİK KESİŞİMİ', 'Ardışık açılar toplamı: 2α + 2β = 180° => α + β = 90° (Dik kesişim: 90°).', 'Dik kesişim noktası daima paralelkenarın orta taban doğrusu üzerindedir.', TUR, TUR_A, 'Paralelkenarda açıortay özelliği')
def g3():
    return cizelge4([('İkizkenar Yamuk', '|AC| = |BD| eş köşegen', MAVI, MAVI_A), ('Dik Kesişen İkiz.', 'Yükseklik h = (a + c) / 2', YES, YES_A), ('Paralelkenar', 'Köşegenler birbirini ortalar', TUR, TUR_A), ('4 Eş Üçgen Alan', 'Köşegenler S, S, S, S böler', MOR, MOR_A)], 'Özel dörtgenlerin köşegen özellikleri')
def g5():
    return akis4([('1. Dikme İndir', 'Ortada c = 10 cm kalır', YES, YES_A), ('2. Yan Parçalar', '(22 - 10) / 2 = 6 cm', MAVI, MAVI_A), ('3. Yükseklik (h)', '6-8-10 üçgeninden h = 8', TUR, TUR_A), ('4. Yamuk Alanı', '16 · 8 = 128 cm²', MOR, MOR_A)], 'İkizkenar yamukta alan bulma adımları')
def g6():
    return ikili('PARALELKENARDA ÜÇGEN ALANI VE YÜKSEKLİK', 'Alan(AEB) = 36 cm² => Alan(ABCD) = 72 cm²', 'Üçgen alanı paralelkenarın yarısıdır', 'Taban |AB| = 12 cm İse Yükseklik', '72 = 12 · h  =>  h = 6 cm', CAM, CAM_A, MAVI, MAVI_A, 'Paralelkenarda yarı alan ve yükseklik')
def g7():
    return kart('YAMUK VE PARALELKENARDA TEMEL BAĞINTILAR', 'Karşı durumlu açılar toplamı 180° · Açıortay kesimi orta taban üzerindedir.', 'Paralelkenarda köşegen-kenar bağıntısı: e² + f² = 2 · (a² + b²).', YES, YES_A, 'Açı ve köşegen kareleri bağıntısı')
def g8():
    return cizelge4([('Dikme Tabanı', '|AH| = |KB| = (a - c) / 2', MAVI, MAVI_A), ('Kelebek Oranı', 'k = c / a · Alan oranı k²', TUR, TUR_A), ('Köşegen Kesimi', '|AO| = |OC| ve |BO| = |OD|', YES, YES_A), ('Alan Eşitliği', 'Alan = a · ha = b · hb', MOR, MOR_A)], 'Geometrik özellikler tablosu')

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
