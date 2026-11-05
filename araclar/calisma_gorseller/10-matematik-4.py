"""10. sınıf Matematik 4. hafta (Üçgende Yardımcı Elemanların Özellikleri ve Üçgenin Alanı) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('&amp;amp;', '&amp;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kok_ciz(cx, y, on_metin, ic_metin, son_metin='', renk=LAC, boy=7.8, ince=False):
    ic_str = str(ic_metin)
    on_str = str(on_metin) if on_metin else ''
    son_str = str(son_metin) if son_metin else ''
    w_ic = max(10, len(ic_str) * (boy * 0.62) + 4)
    w_on = len(on_str) * (boy * 0.56) + (2 if on_str else 0)
    w_son = len(son_str) * (boy * 0.56) + (2 if son_str else 0)
    toplam_w = w_on + 9 + w_ic + w_son
    sol = cx - toplam_w / 2
    out = ''
    if on_str:
        out += yazi(sol + w_on - 1, y, on_str, boy, renk, 'end', ince=ince)
    rx = sol + w_on
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.2
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.2:.1f} {orta_y - 1.2:.1f} '
            f'L{rx + 5.0:.1f} {alt_y:.1f} L{rx + 8.5:.1f} {ust_y:.1f} '
            f'H{rx + 9 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="1.1" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 9 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    if son_str:
        out += yazi(rx + 9 + w_ic + 1, y, son_str, boy, renk, 'start', ince=ince)
    return out


def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [('Temel Alan', 'Alan = (Taban · Yükseklik) / 2', '#2451d6', '#e8eefe'), ('Eşkenar Alan', None, '#12a150', '#e3f6ea'), ('Sinüs Alan', 'Alan = ½ · a · b · sin(C)', '#ee7d12', '#fff1df'), ('Kenarortay & Alan', 'G üçgeni 6 eşit alana böler', '#7c3aed', '#f0e9fe')]
    for i, (b, d, c, a) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, a, c, 6, 1.2)
        ic += yazi(x + 40, 30, b, 9, c)
        ic += f'<line x1="{x + 8}" y1="40" x2="{x + 72}" y2="40" stroke="{c}" stroke-width="0.8"/>'
        if d is None:
            ic += kok_ciz(x + 40, 62, 'Alan = a² · ', '3', ' / 4', LAC, 7.5, ince=True)
        else:
            ic += yazi(x + 40, 62, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 temel kurallar ve kavramlar kartı', 34)
def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'ÜÇGENDE TEMEL ALAN BAĞINTISI VE YÜKSEKLİK', 10.5, MAVI)
    boxes = [('[BC] = 14 cm, h = 6 cm', 'Alan = (14 · 6) / 2 = 42 cm²', '#2451d6'), ('Dik Üçgen Alanı: Dik kenarlar çarpımı / 2', 'Alan = (b · c) / 2', '#12a150')]
    for i, (b, d, c) in enumerate(boxes):
        x = 16 + i * 168
        ic += kutu(x, 34, 160, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 80, 52, b, 8.5, c)
        ic += yazi(x + 80, 72, d, 7, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 ana konu ve kavramsal model şeması', 34)
def g2():
    ic = kutu(4, 4, 352, 92, YES_A, YES)
    ic += yazi(180, 22, 'Eşkenar Üçgenin Alanı ve Kök 3 Bağıntısı', 11, YES)
    ic += kutu(16, 34, 156, 54, '#ffffff', '#12a150', 6, 1.2)
    ic += yazi(94, 52, 'Bir Kenarı a = 6 cm', 9, '#12a150')
    ic += kok_ciz(94, 72, 'Alan = 36 / 4 · ', '3', ' = 9 kök 3 cm²', LAC, 7.4, ince=True)
    ic += kutu(188, 34, 156, 54, '#ffffff', '#2451d6', 6, 1.2)
    ic += yazi(266, 52, 'Bir Kenarı a = 4 cm', 9, '#2451d6')
    ic += kok_ciz(266, 72, 'Alan = 16 / 4 · ', '3', ' = 4 kök 3 cm²', LAC, 7.4, ince=True)
    return svg(360, 100, ic, '10-matematik-4 model ve yasa karşılaştırma şeması', 34)
def g3():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR)
    ic += yazi(180, 22, 'Yükseklikleri Eşit Üçgenlerde Taban-Alan Oranı', 10.5, TUR)
    boxes = [('Taban 3 cm', 'Alan = 15 cm² (1k)', '#2451d6'), ('Taban 6 cm', 'Alan = 30 cm² (2k)', '#12a150'), ('Sonuç', 'Alanlar oranı tabanlar oranına eşittir', '#ee7d12')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 sınıflandırma ve ayrıntı şeması', 34)
def g5():
    ic = kutu(4, 4, 352, 92, MOR_A, MOR)
    ic += yazi(180, 22, 'SİNÜS ALAN TEOREMİ İLE ALAN HESAPLAMA AKIŞI', 10.5, MOR)
    steps = [('1. Kenarlar', 'İki kenar boyu a ve b'), ('2. Açı', 'Aralarındaki açı α'), ('3. Sinüs', 'sin(α) trigonometrik değer'), ('4. Çarpım', 'Alan = ½ · a · b · sin(α)')]
    for i, (b, d) in enumerate(steps):
        x = 10 + i * 86
        ic += kutu(x, 34, 80, 54, '#ffffff', MOR, 6, 1.2)
        ic += yazi(x + 40, 50, b, 8.5, MOR)
        ic += yazi(x + 40, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 süreç ve akış basamakları modeli', 34)
def g6():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    ic += yazi(180, 22, 'Kenarortayların Üçgeni 6 Eşit Alana Bölmesi (6S)', 10.5, LAC)
    boxes = [('Ağırlık Merkezi (G)', '3 kenarortayın kesişim noktası', '#2451d6'), ('Her Bölge = S', 'Tüm 6 üçgenin alanı birbirine eşit', '#12a150'), ('Toplam Alan', 'Alan(ABC) = 6 · S', '#7c3aed')]
    for i, (b, d, c) in enumerate(boxes):
        x = 14 + i * 112
        ic += kutu(x, 34, 104, 54, '#ffffff', c, 6, 1.2)
        ic += yazi(x + 52, 50, b, 8.5, c)
        ic += yazi(x + 52, 70, d, 6.5, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 karşılaştırma ve ilişki diyagramı', 34)
def g8():
    ic = kutu(4, 4, 352, 92, CAM_A, CAM)
    cards = [('Alan', 'İki boyutlu yüzey büyüklüğü'), ('Yükseklik (h)', 'Köşeden kenara inen dikme'), ('Ağırlık Merkezi', 'Kenarortay kesim noktası'), ('Sinüs Alan', 'Açılı üçgen alan formülü')]
    for i, (b, d) in enumerate(cards):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, '#ffffff', CAM, 6, 1.2)
        ic += yazi(x + 40, 32, b, 9.5, CAM)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{CAM}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 64, d, 7.5, LAC, ince=True)
    return svg(360, 100, ic, '10-matematik-4 temel terminoloji kavram kartları', 34)
def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'ANAHTAR KAVRAM ŞİFRE ŞERİDİ: T - A - B - A - N', 11.5, YES)
    harfler = [('1', 'T'), ('2', 'A'), ('3', 'B'), ('4', 'A'), ('5', 'N')]
    for i, (no, h) in enumerate(harfler):
        x = 48 + i * 55
        ic += kutu(x, 32, 48, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 24, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 24, 68, h, 16, LAC)
    return svg(360, 96, ic, '10-matematik-4 dersi şifre anahtar harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[10]['gorsel'] = g10()
