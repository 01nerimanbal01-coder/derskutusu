"""9. sınıf Fizik 3. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    bilginler = [('Arşimet', 'Kaldırma kuvveti prensibi', MAVI, MAVI_A), ('Galileo', 'Eylemsizlik ve serbest düşme', YES, YES_A), ('Newton', 'Kütle çekimi ve dinamik', TUR, TUR_A), ('İbnü\'l-Heysem', 'Deneysel optik ve kırılma', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(bilginler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Fizik bilimine yön veren bilginler kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'İBNÜ\'L-HEYSEM · KİTÂBÜ\'L-MENÂZIR VE OPTİK', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, 'Işık Nesnelerden Yansıyarak Göze Ulaşır', 12, LAC) + yazi(180, 70, 'Gözden ışın çıktığı yanılgısını çürüten ilk deneysel optik keşfidir.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'İbnül Heysem optik ışık şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'EYLEMSİZLİK PRENSİBİ (NEWTON 1. YASA)', 11, TUR)
    ic += yazi(180, 48, 'Net kuvvet sıfırsa (F_net = 0): Duran durur, hareketli sabit hızla gider.', 10, LAC)
    ic += yazi(180, 68, 'Cisimlerin mevcut hareket durumunu koruma isteğidir.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Eylemsizlik prensibi denge kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    yasalar = [('Eylemsizlik', 'Durumunu koruma', MAVI, MAVI_A), ('Temel Yasa', 'F = m · a bağıntısı', TUR, TUR_A), ('Etki-Tepki', 'Eşit ve zıt kuvvet', YES, YES_A), ('Kütle Çekim', 'Evrensel çekim kuvveti', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(yasalar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Newton dinamik yasaları panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Arşimet', 'Kaldırma kuvveti', YES, YES_A), ('2. Cezeri', 'Mekanik otomatlar', MAVI, MAVI_A), ('3. Galileo', 'Deneysel dinamik', TUR, TUR_A), ('4. Newton', 'Hareket yasaları', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Mekanik bilimi öncüleri akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'EL-CEZERİ · SİBERNETİK VE MEKANİK OTOMATLAR', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Dişli Çarklar · Su Saatleri · Krank Mili Mekanizması', 11, LAC) + yazi(180, 70, 'Robotik sistemler ve otomasyon mühendisliğinin ilk kurucusudur.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'El-Cezeri sibernetik mekanik panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    modern = [('Faraday', 'Elektromanyetik indüksiyon', MAVI, MAVI_A), ('Maxwell', 'Elektromanyetik dalgalar', TUR, TUR_A), ('Einstein', 'Görelilik teorisi', YES, YES_A), ('Curie', 'Radyoaktivite araştırması', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(modern):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Fizik öncüleri buluş eşleştirme kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: K - U - V - V - E - T', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'U'), ('3', 'V'), ('4', 'V'), ('5', 'E'), ('6', 'T')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES) + yazi(x + 21, 46, no, 9, SOLUK, ince=True) + yazi(x + 21, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Kuvvet şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
