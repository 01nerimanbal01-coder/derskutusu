"""9. sınıf Fizik 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    dallar = [('Mekanik', 'Kuvvet ve hareket', MAVI, MAVI_A), ('Termodinamik', 'Isı ve enerji iletimi', YES, YES_A), ('Optik', 'Işık ve yansıma', TUR, TUR_A), ('Elektromanyetizma', 'Elektrik ve manyetizma', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(dallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Fizik alt dalları ve inceleme alanları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'KATI HÂL FİZİĞİ · YARI İLETKEN TEKNOLOJİSİ', 11, MAVI)
    ic += kutu(20, 32, 150, 56, '#f4f8fe', MAVI) + yazi(95, 48, 'Silisyum Tabanlı Mikroçip', 10, LAC) + yazi(95, 68, 'Kristal örgü ve yarı iletkenlik', 8.5, SOLUK, ince=True)
    ic += kutu(190, 32, 150, 56, YES_A, YES) + yazi(265, 48, 'Uygulama Alanı', 10, YES) + yazi(265, 68, 'Transistörler ve güneş pilleri', 9, LAC, ince=True)
    return svg(360, 100, ic, 'Katı hâl fiziği silisyum mikroçip şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'PLAZMA VE YÜKSEK ENERJİ FİZİĞİ', 11, TUR)
    ic += yazi(180, 48, 'Güneş Patlamaları · Kutup Işıkları (Aurora) · Füzyon Enerjisi', 10.5, LAC)
    ic += yazi(180, 68, 'İyonize olmuş yüksek enerjili gaz hâlini inceler.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Plazma ve yüksek enerji fiziği kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Mekanik', 'Newton yasaları', MAVI, MAVI_A), ('Optik', 'Snell ve yansıma', TUR, TUR_A), ('Termodinamik', 'Korunum ilkeleri', YES, YES_A), ('Nükleer', 'Çekirdek enerjisi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'Fizik alt dalları temel yasaları', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Mekanik', 'Makro boyut', YES, YES_A), ('2. Termodinamik', 'Isıl sistemler', MAVI, MAVI_A), ('3. Atom Fiziği', 'Elektron kabuğu', TUR, TUR_A), ('4. Nükleer', 'Çekirdek (mikro)', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Makrodan mikroya fizik alt dalları sıralama akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'TIBBİ GÖRÜNTÜLEME · MANYETİK REZONANS (MR)', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Güçlü manyetik alan ve radyo dalgaları ile görüntüleme yapılır.', 10.5, LAC) + yazi(180, 70, 'Elektromanyetizma alt dalının sağlık teknolojisindeki uygulamasıdır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'MR cihazı elektromanyetizma panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    esles = [('Fiber Optik', 'Optik kablo', MAVI, MAVI_A), ('Pusula İğnesi', 'Elektromanyetizma', TUR, TUR_A), ('Termos', 'Termodinamik yalıtım', YES, YES_A), ('Kule Vinç', 'Mekanik denge', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(esles):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Fiziğin günlük hayat örnekleri kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: F - İ - Z - İ - K', 11.5, YES)
    harfler = [('1', 'F'), ('2', 'İ'), ('3', 'Z'), ('4', 'İ'), ('5', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Fizik şifresi harf kutuları', 34)

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
