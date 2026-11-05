"""9. sınıf Din Kültürü ve Ahlak Bilgisi 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    kavramlar = [('Vahiy', 'Allah\'tan ilahi mesaj', MAVI, MAVI_A), ('İbadet', 'Kulluk ve itaat cevabı', YES, YES_A), ('Fiilî Dua', 'Emek ve sebeplere uyum', TUR, TUR_A), ('Kavlî Dua', 'Dil ve kalple yakarış', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kavramlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Allah-insan iletişim yolları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'İBADETLERİN ALLAH KATINDA KABUL OLMA ŞARTLARI', 10.5, MAVI)
    ic += kutu(16, 36, 104, 64, '#f4f8fe', MAVI) + yazi(68, 56, '1. İMAN', 10.5, MAVI) + yazi(68, 78, 'Tevhid inancı', 9, SOLUK, ince=True)
    ic += kutu(128, 36, 104, 64, YES_A, YES) + yazi(180, 56, '2. İHLAS', 10.5, YES) + yazi(180, 78, 'Yalnız Allah rızası', 9, SOLUK, ince=True)
    ic += kutu(240, 36, 104, 64, TUR_A, TUR) + yazi(292, 56, '3. SÜNNET', 10.5, TUR) + yazi(292, 78, 'Peygamber uygulaması', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'İbadetin üç kabul şartı şeması', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'DAR (ÖZEL) VE GENİŞ (GENEL) ANLAMDA İBADET', 10.5, TUR)
    ic += yazi(180, 58, 'Dar Anlam: Namaz, Oruç, Zekât, Hac   |   Geniş Anlam: Her Salih Amel', 10, LAC)
    ic += yazi(180, 82, 'Allah rızası gözetilerek yapılan çalışma, ilim ve merhamet geniş anlamda ibadettir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'İbadetin dar ve geniş kapsamı kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('İhlas', 'Samimi kulluk', MAVI, MAVI_A), ('Riya Yasağı', 'Gösterişten kaçınma', KIR, KIR_A), ('Fiilî + Kavlî', 'Çaba ve yakarış', YES, YES_A), ('Süreklilik', 'Darlıkta ve bollukta', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'İbadet ve dua ilkeleri panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Fiilî Dua', 'Sebeplere sarıl', YES, YES_A), ('2. Hamd/Salavat', 'Duaya edeple başla', MAVI, MAVI_A), ('3. Kavlî Yakarış', 'Esmaülhüsna ile iste', TUR, TUR_A), ('4. Tevekkül', 'Takdire razı ol', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Dua adabı ve aşamaları akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'İNSANIN YARATILIŞ GAYESİ · ZÂRİYÂT SURESİ 56. AYET', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, '"Ben cinleri ve insanları, ancak bana kulluk etsinler diye yarattım."', 10.5, LAC) + yazi(180, 84, 'İbadet; Yaratıcıyı tanımak, O\'na iman etmek ve rızasına uygun yaşamaktır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Zariyat Suresi 56. ayet yaratılış gayesi panosu', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'DUANIN RUHU VE KUR\'AN\'DA DUA EDEBİ', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Dua (İbadetin Özü)  ·  Esmaülhüsna (Güzel İsimler)  ·  Havf ve Reca', 10, LAC) + yazi(180, 82, 'Mümin korku ile ümit dengesinde, gizlice ve alçakgönüllülükle dua eder.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Dua adabı kavramları özet şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ayetler = [('Fâtiha 1/5', 'İbadet ve istiane', MAVI, MAVI_A), ('Ankebût 29/45', 'Namaz kötülüğü önler', TUR, TUR_A), ('Bakara 2/186', 'Allah kuluna yakındır', YES, YES_A), ('Bakara 2/201', 'Dünya-ahiret iyiliği', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ayetler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'İbadet ve dua ayetleri özet kartı', 34)

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
