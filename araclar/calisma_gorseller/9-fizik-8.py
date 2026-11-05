"""9. sınıf Fizik 8. hafta görselleri (SVG; insan figürü yok K024; K178 beyaz bant yok; max-height:24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'
STIL = 'width:100%;max-height:24mm;display:block;margin:1mm auto;'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="{STIL}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 77, a, c, 5, 0.75)
        ic += yazi(x + 40, 46, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="54" x2="{x + 72}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 90, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, c1)
    ic += kutu(12, 28, 162, 77, a1, c1, 6, 0.75)
    ic += yazi(93, 46, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="54" x2="164" y2="54" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 72, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 91, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 28, 162, 77, a2, c2, 6, 0.75)
    ic += yazi(267, 46, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="54" x2="338" y2="54" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 72, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 91, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 77, a, c, 6, 0.75)
        ic += yazi(x + 54, 46, b, 8.6, c)
        ic += f'<line x1="{x + 10}" y1="54" x2="{x + 98}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 91, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 8 + i * 87
        ic += kutu(x, 28, 79, 77, a, c, 5, 0.75)
        ic += yazi(x + 39.5, 46, b, 8.2, c)
        ic += yazi(x + 39.5, 70, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39.5, 89, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ox = x + 80.5
            ic += f'<polygon points="{ox:.1f},62 {ox+5:.1f},66.5 {ox:.1f},71" fill="{ana_renk}"/>'
    return svg(ic, etiket)

def g0():
    return kart4('ÖZEL AÇILI EŞİT VEKTÖRLERİN (F1 = F2 = F) BİLEŞKESİ', [
        ('α = 0° (Aynı Yön)', 'R_max = 2F', 'Doğrudan toplanır'),
        ('α = 60° Özel Açısı', 'R = F·kok3', 'Açıortay üzerinde'),
        ('α = 90° (Dik Açı)', 'R = F·kok2', 'Pisagor bağıntısı'),
        ('α = 120° Özel Açısı', 'R = F', 'α = 180° ise R_min = 0')
    ], '9-fizik-8 özel açılar')

def g1():
    ic = kutu(4, 4, 352, 107, GRI_A, MAVI, 6, 0.75)
    ic += yazi(180, 20, 'AYNI DOĞRULTULU VEKTÖRLERİN BİLEŞKESİ (R)', 9.8, MAVI)
    ic += kutu(14, 28, 332, 76, '#f8fafc', MAVI, 6, 0.75)
    ic += f'<line x1="30" y1="54" x2="170" y2="54" stroke="{MAVI}" stroke-width="0.75"/>'
    ic += f'<polygon points="170,50 178,54 170,58" fill="{MAVI}"/>'
    ic += yazi(100, 46, 'F1 = 12 N (+x)', 8.5, MAVI)
    ic += f'<line x1="185" y1="54" x2="255" y2="54" stroke="{YES}" stroke-width="0.75"/>'
    ic += f'<polygon points="255,50 263,54 255,58" fill="{YES}"/>'
    ic += yazi(222, 46, 'F2 = 5 N (+x)', 8.5, YES)
    ic += f'<line x1="160" y1="82" x2="70" y2="82" stroke="{KIR}" stroke-width="0.75"/>'
    ic += f'<polygon points="70,78 62,82 70,86" fill="{KIR}"/>'
    ic += yazi(115, 75, 'F3 = 7 N (-x)', 8.5, KIR)
    ic += yazi(265, 82, 'R = (12 + 5) - 7 = +10 N (+x)', 8.5, LAC)
    return svg(ic, '9-fizik-8 aynı doğrultulu vektörler')

def g2():
    return karsilastir2('VEKTÖRÜN DİK BİLEŞENLERİNE AYRILMASI (F = 20 N, α = 37°)',
        'Yatay Bileşen (Fx = F · cos α)', 'cos 37° = 0,8', 'Fx = 20 · 0,8 = 16 N (+x yönünde)',
        'Düşey Bileşen (Fy = F · sin α)', 'sin 37° = 0,6', 'Fy = 20 · 0,6 = 12 N (+y yönünde)',
        '9-fizik-8 dik bileşenler')

def g3():
    return uclu_sema('UÇ UCA EKLEME VE PARALELKENAR KURALI ÖZELLİKLERİ', [
        ('Uç Uca Ekleme', 'İlk başlangıçtan', 'Son bitiş ucuna R çizilir'),
        ('Kapalı Çokgen', 'Başlangıca dönerse', 'Bileşke R = 0 olur'),
        ('Açı ve Büyüklük', 'Açı büyüdükçe R küçülür', 'R büyük vektöre yakındır')
    ], '9-fizik-8 vektör kuralları')

def g5():
    return akis4('DİK BİLEŞENLERLE BİLEŞKE HESAPLAMA ADIMLARI', [
        ('1. Bileşene Ayır', 'Fx = F·cos α', 'Fy = F·sin α'),
        ('2. Yatay Toplam', 'Rx = ΣFx', '(+x ve -x toplamı)'),
        ('3. Düşey Toplam', 'Ry = ΣFy', '(+y ve -y toplamı)'),
        ('4. Pisagor (R)', 'R^2 = Rx^2 + Ry^2', 'Net bileşke boyu')
    ], '9-fizik-8 bileşen adımları')

def g6():
    return karsilastir2('PARALELKENAR YÖNTEMİNDE α = 120° ÖZEL DURUMU',
        'Verilen Vektörler', 'F1 = 10 N ve F2 = 10 N (Eşit)', 'Başlangıç noktaları ortak, α = 120°',
        'Bileşke Vektör (R)', 'R = F = 10 N büyüklüğündedir', 'Tam açıortay (60° - 60°) üzerindedir',
        '9-fizik-8 120 derece', MOR, MOR_A, YES, YES_A)

def g7():
    return karsilastir2('İKİ VEKTÖRÜN BİLEŞKE SINIRLARI (7 N ve 9 N)',
        'Minimum Bileşke (α = 180°, Zıt Yön)', 'R_min = |F1 - F2| = |9 - 7| = 2 N', 'Bileşke 2 N’den küçük OLAMAZ!',
        'Maksimum Bileşke (α = 0°, Aynı Yön)', 'R_max = F1 + F2 = 9 + 7 = 16 N', 'Değer aralığı: 2 N <= R <= 16 N',
        '9-fizik-8 bileşke sınırları', CAM, CAM_A, TUR, TUR_A)

def g10():
    return karsilastir2('UÇ UCA EKLEME İLE PARALELKENAR YÖNTEMİ FARKI',
        'Uç Uca Ekleme Yöntemi', '2. vektörün başlangıcı 1.’nin ucuna gelir', 'İlk başlangıçtan son uca R çizilir',
        'Paralelkenar Yöntemi', 'İki vektörün başlangıç noktası birleştirilir', 'Ortak başlangıçtan köşegen R çizilir',
        '9-fizik-8 iki yöntem', MAVI, MAVI_A, MOR, MOR_A)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[10]['gorsel'] = g10()
