"""9. sınıf Türk Dili ve Edebiyatı 4. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def g0():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    asamalar = [('Hazırlık', 'Tema ve amaç seçimi', MAVI, MAVI_A), ('Planlama', 'Paragraf kurgusu', YES, YES_A), ('Taslak', 'İlk metni yazma', TUR, TUR_A), ('Düzeltme', 'İmla ve akıcılık', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(asamalar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 11, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Yazma süreci basamakları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'ŞİİRDEN BETİMLEMEYE DÖNÜŞÜM ATÖLYESİ', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 48, 'Şiirin Ana Duygusu, İmgeleri ve Renkleri Nesre Aktarılır', 11, LAC) + yazi(180, 70, 'Duyusal ayrıntılarla zenginleştirilmiş özgün tasvir paragrafı kurulur.', 9, SOLUK, ince=True)
    return svg(360, 100, ic, 'Şiir dönüştürme yazma panosu', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'BETİMLEYİCİ ANLATIM (TASVİR)', 11, TUR)
    ic += yazi(180, 48, 'Varlıkları okuyucunun zihninde resim çizer gibi canlandırma sanatıdır.', 10.5, LAC)
    ic += yazi(180, 68, 'Görme, işitme, koklama gibi duyusal ayrıntılar ve niteleme sıfatları kullanılır.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Betimleme anlatım biçimi kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Duruluk', 'Gereksiz sözcük yok', MAVI, MAVI_A), ('Akıcılık', 'Takılmadan okuma', TUR, TUR_A), ('Açıklık', 'Tek ve net anlam', YES, YES_A), ('Özgünlük', 'Yazara has üslup', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Metnin anlatım ilkeleri panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Okuma', 'Şiiri ve temayı anla', YES, YES_A), ('2. Plan', 'Mekân ve imgeyi seç', MAVI, MAVI_A), ('3. Taslak', 'Duyusal tasviri yaz', TUR, TUR_A), ('4. Düzeltme', 'İmla ve akıcılığı sına', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Şiiri betimlemeye dönüştürme akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'EDEBÎ TASVİR KESİTİ · GÜN BATIMI', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, '"Güneşin son kızıl ışıkları, sarp kayalıkların ardına altın bir tül gibi seriliyordu."', 9.5, LAC) + yazi(180, 70, 'Görsel ayrıntılar ve benzetmelerle okuyucunun zihninde canlı manzara kurulur.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Betimleme örneği panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    anlatim = [('Duruluk', 'Gereksiz sözcüksüzlük', MAVI, MAVI_A), ('Akıcılık', 'Ritmik ses uyumu', TUR, TUR_A), ('Açıklık', 'Tek anlamlılık', YES, YES_A), ('Özgünlük', 'Yazara has söyleyiş', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(anlatim):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Anlatım nitelikleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: B - E - T - İ - M', 11.5, YES)
    harfler = [('1', 'B'), ('2', 'E'), ('3', 'T'), ('4', 'İ'), ('5', 'M')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Betim şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
