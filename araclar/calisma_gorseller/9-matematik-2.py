"""9. sınıf Matematik 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kurallar = [('√a · √b', '√(a·b)', MAVI, MAVI_A), ('(√a)²', 'a (a ≥ 0)', YES, YES_A), ('√(a/b)', '√a / √b', TUR, TUR_A), ('a^(1/2)', '√a', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 12, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 11, LAC, ince=True)
    return svg(360, 100, ic, 'Köklü sayı kuralları eşitlik kartları', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'KÖKLÜ İFADELERDE ÇIKARMA VE SADELEŞTİRME', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, '√75 − √12  =  5√3 − 2√3  =  3√3', 14, LAC) + yazi(180, 72, 'Kök içleri eşitlendiğinde katsayılar arasında çıkarma yapılır.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Köklü ifade çıkarma işlemi çözümü', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'KÖK DIŞINA ÇIKARMA · a√b BİÇİMİ', 11, TUR)
    ic += yazi(180, 50, '√48  =  √(16 · 3)  =  √16 · √3  =  4√3', 13.5, LAC)
    ic += yazi(180, 70, 'Tam kare çarpan kök dışına katsayı olarak çıkar.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Kök dışına çıkarma kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Toplama', 'Kök içleri aynı', MAVI, MAVI_A), ('Çarpma', 'Kök derecesi aynı', TUR, TUR_A), ('Eşlenik', 'Paydayı kurtar', YES, YES_A), ('Mutlak Değer', '√(x²) = |x|', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'Köklü sayılar işlem kuralları panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Kesir', 'Paydayı incele', YES, YES_A), ('2. Eşlenik', '√b ile çarp', MAVI, MAVI_A), ('3. Genişlet', 'Pay ve paydayı', TUR, TUR_A), ('4. Sadeleştir', 'Rasyonel payda', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Paydayı rasyonel yapma basamakları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 22, 'SAYI DOĞRUSUNDA √50 DEĞERİ', 11, CAM)
    ic += f'<line x1="30" y1="52" x2="330" y2="52" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<circle cx="80" cy="52" r="3" fill="{LAC}"/><circle cx="180" cy="52" r="3" fill="{LAC}"/><circle cx="280" cy="52" r="3" fill="{LAC}"/>'
    ic += yazi(80, 42, '6 = √36', 10, SOLUK, ince=True) + yazi(180, 42, '7 = √49', 10, LAC) + yazi(280, 42, '8 = √64', 10, SOLUK, ince=True)
    ic += f'<polygon points="195,47 190,38 200,38" fill="{KIR}"/>'
    ic += yazi(195, 72, '√50 (7 ile 8 arasında, 7\'ye çok yakın)', 10, KIR)
    return svg(360, 96, ic, 'Sayı doğrusunda kök 50 konumu şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    islemler = [('√2 · √8', '= √16 = 4', MAVI, MAVI_A), ('√50 / √2', '= √25 = 5', TUR, TUR_A), ('√27 / 3', '= 3√3 / 3 = √3', YES, YES_A), ('(√5)²', '= 5', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(islemler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 11, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Köklü sayı işlem sonuçları eşleştirme kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: K - Ö - K - L - Ü', 11.5, YES)
    harfler = [('1', 'K'), ('2', 'Ö'), ('3', 'K'), ('4', 'L'), ('5', 'Ü')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Köklü şifresi harf kutuları', 34)

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
