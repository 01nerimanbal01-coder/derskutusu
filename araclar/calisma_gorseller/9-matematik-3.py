"""9. sınıf Matematik 3. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    araliklar = [('[2, 5]', '2 ve 5 dahil', MAVI, MAVI_A), ('(2, 5)', '2 ve 5 hariç', YES, YES_A), ('[2, 5)', '2 dahil, 5 hariç', TUR, TUR_A), ('(2, 5]', '2 hariç, 5 dahil', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(araliklar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 12, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 100, ic, 'Gerçek sayı aralık gösterimleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 20, 'SAYI DOĞRUSUNDA ARALIK KESİŞİMİ: A ∩ B', 10.5, MAVI)
    ic += f'<line x1="30" y1="42" x2="330" y2="42" stroke="{GRI}" stroke-width="1.2"/>'
    ic += f'<line x1="75" y1="42" x2="210" y2="42" stroke="{TUR}" stroke-width="3"/>'
    ic += yazi(142, 35, 'A = [-3, 4)', 9.5, TUR)
    ic += f'<line x1="30" y1="65" x2="330" y2="65" stroke="{GRI}" stroke-width="1.2"/>'
    ic += f'<line x1="150" y1="65" x2="300" y2="65" stroke="{YES}" stroke-width="3"/>'
    ic += yazi(225, 58, 'B = [1, 7]', 9.5, YES)
    ic += yazi(180, 84, 'Kesişim Kümesi: A ∩ B = [1, 4)', 11, LAC)
    return svg(360, 100, ic, 'Aralık kesişim kümesi sayı doğrusu şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'EŞİTSİZLİĞİN ARALIK DÖNÜŞÜMÜ', 11, TUR)
    ic += yazi(180, 50, '-2 &lt; x ≤ 5   ⟹   x ∈ (-2, 5]', 14, LAC)
    ic += yazi(180, 70, '-2 küçük (açık parantez), 5 küçük eşit (köşeli parantez) alır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Eşitsizlik ve yarı açık aralık kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    kurallar = [('Taban Aynı', 'a^m · a^n = a^(m+n)', MAVI, MAVI_A), ('Bölme', 'a^m / a^n = a^(m-n)', TUR, TUR_A), ('Üssün Üssü', '(a^m)^n = a^(m·n)', YES, YES_A), ('Kesişim', 'A ∩ B ortak eleman', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Üslü sayılar ve aralık işlem kuralları', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Çözüm', 'Bilinmeyeni yalnız bırak', YES, YES_A), ('2. Uç Nokta', 'Sınırları belirle', MAVI, MAVI_A), ('3. Dahillik', 'Açık / dolu nokta', TUR, TUR_A), ('4. Aralık', 'Ayraçla göster', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10, c) + yazi(x + 40, 55, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Eşitsizlik çözüm kümesi adımları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 22, 'ÜSLÜ İŞLEM SADELEŞTİRME', 11, CAM)
    ic += kutu(20, 32, 320, 48, '#eaf7fa', CAM) + yazi(180, 50, '(2⁵ · 2³) / 2⁴  =  2⁸ / 2⁴  =  2⁴  =  16', 13, LAC) + yazi(180, 70, 'Çarpmada üsler toplanır, bölmede pay üssünden payda üssü çıkarılır.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Üslü sayı işlem adımları panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    usler = [('2⁶', '= 64', MAVI, MAVI_A), ('3⁴', '= 81', TUR, TUR_A), ('5³', '= 125', YES, YES_A), ('10³', '= 1000', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(usler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 12, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 11, LAC, ince=True)
    return svg(360, 96, ic, 'Üslü sayı değerleri eşleştirme kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: A - R - A - L - I - K', 11.5, YES)
    harfler = [('1', 'A'), ('2', 'R'), ('3', 'A'), ('4', 'L'), ('5', 'I'), ('6', 'K')]
    for i, (no, h) in enumerate(harfler):
        x = 35 + i * 50
        ic += kutu(x, 32, 42, 48, '#eaf8f0', YES) + yazi(x + 21, 46, no, 9, SOLUK, ince=True) + yazi(x + 21, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Aralık şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
