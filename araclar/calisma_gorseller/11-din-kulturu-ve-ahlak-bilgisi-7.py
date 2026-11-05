"""11. sınıf Din Kültürü 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return cizelge4([('Vüs’at (Güç)', 'Kapasite ve takat sınırı', MAVI, MAVI_A), ('Kesb (Kazanma)', 'Fıtrata uygun iyilik', YES, YES_A), ('İktisâb (Yük)', 'Zorlamayla işlenen günah', TUR, TUR_A), ('Isr (Ağır Yük)', 'Zorlu mükellefiyetler', MOR, MOR_A)], 'Bakara Suresi 286. ayet kavramları')
def g1():
    return ikili('BAKARA 286: TEKLİF VE GÜÇ DENGESİ İLKESİ', 'İlahi Adalet Kuralı', 'Gücün yettiğinden fazlası yüklenmez', 'Kelamdaki Karşılığı', 'Teklîf-i mâ lâ yutâk caiz değildir', YES, YES_A, MAVI, MAVI_A, 'Teklif-güç dengesi ve ilahi adalet')
def g2():
    return kart('KESB VE İKTİSÂB KAVRAMLARININ BELÂGAT İNCELİĞİ', 'Kesb (İyilik): Temiz fıtrata uygundur; niyet edilince dahi sevap yazılır.', 'İktisâb (Kötülük): Fıtrata aykırıdır; nefsin zorlamasıyla eyleme dökülünce yazılır.', TUR, TUR_A, 'Kesb ve iktisab farkı')
def g3():
    return cizelge4([('Dinde Kolaylık', 'Hasta oturarak kılar', YES, YES_A), ('Cüz’î İrade', 'Cebriye görüşü reddedilir', MAVI, MAVI_A), ('Nisyân ve Hata', 'Unutma/yanılma affı', TUR, TUR_A), ('Kad Fealtü', 'Duaların kabul müjdesi', MOR, MOR_A)], 'Bakara 286 fıkhi ve kelami ilkeleri')
def g5():
    return akis4([('1. Vüs’at İlkesi', 'Güç ölçüsünde teklif', YES, YES_A), ('2. Kesb-İktisâb', 'Bireysel sorumluluk', MAVI, MAVI_A), ('3. Rabbenâ Duası', 'Hata ve ağır yükten af', TUR, TUR_A), ('4. Af ve Nusret', 'Afv, mağfiret ve yardım', MOR, MOR_A)], 'Bakara 286. ayetin anlam akışı')
def g6():
    return ikili('MÜMİNLERİN ÜÇ BÜYÜK RABBENÂ DUASI', '1. Nisyân ve Hata Duası', 'Unutursak bizi sorumlu tutma!', '2-3. Isr ve Takat Duası', 'Ağır yük ve takat üstü taşıtma!', CAM, CAM_A, MOR, MOR_A, 'Rabbena dualarının içeriği')
def g7():
    return kart('ÂMENERRASÛLÜ VE İLAHİ YARDIM (NUSRET) BİLİNCİ', 'Bakara Suresi 285-286. ayetler Âmenerrasûlü olarak okunur.', 'İyilik niyetle sevap olur, kötülük eylemle yazılır; Allah’tan nusret dilenir.', YES, YES_A, 'Amenerrasulü ve nusret kavramı')
def g8():
    return cizelge4([('İn nesînâ', 'Unutma ve yanılma affı', MAVI, MAVI_A), ('Velâ tahmil ısran', 'Ağır yüklerden korunma', TUR, TUR_A), ('Mâ lâ tâkate', 'Takat üstünden sığınma', YES, YES_A), ('Fensurnâ', 'İnkârcılara karşı yardım', MOR, MOR_A)], 'Rabbena duaları eşleştirmesi')

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
