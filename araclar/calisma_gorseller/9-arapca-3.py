"""9. sınıf Arapça 3. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    zamirler = [('أَنَا', 'Ben (Tekil)', MAVI, MAVI_A), ('أَنْتَ', 'Sen (Erkek)', YES, YES_A), ('أَنْتِ', 'Sen (Kız)', TUR, TUR_A), ('هُوَ', 'O (Erkek)', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(zamirler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 36, ar, 15, c) + f'<line x1="{x+10}" y1="46" x2="{x+70}" y2="46" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 66, tr, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Arapça tekil kişi zamirleri kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, TUR_A, TUR) + yazi(180, 22, 'MEMLEKET SORMA: KIZ MUHATAP (MÜENNES)', 11, TUR)
    ic += kutu(20, 32, 320, 54, '#fff9f2', TUR) + yazi(180, 50, 'مِنْ أَيْنَ أَنْتِ؟', 16, LAC) + yazi(180, 72, '(Nerelisin? - Sen zamiri esreli okunur)', 10, SOLUK, ince=True)
    return svg(360, 100, ic, 'Müennes memleket sorma soru kartı', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, MAVI_A, MAVI, 8)
    ic += yazi(180, 28, 'İŞARET İSİMLERİ (BU): MÜZEKKER &amp; MÜENNES', 11, MAVI)
    ic += yazi(180, 50, 'هٰذَا (Eril)  ·  هٰذِهِ (Dişil)', 15, LAC)
    ic += yazi(180, 70, 'Müennes isimler işaret edilirken هٰذِهِ kullanılır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Arapça işaret isimleri kural kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    kurallar = [('Müzekker', 'Eril varlıklar', MAVI, MAVI_A), ('Müennes', 'Dişil varlıklar', TUR, TUR_A), ('ـِي Eki', 'Benim iyelik', YES, YES_A), ('ـكَ / ـكِ', 'Senin iyelik', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10.5, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 9, LAC, ince=True)
    return svg(360, 98, ic, 'Arapça zamir ve cinsiyet kuralları panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Selam', 'السَّلَامُ عَلَيْكُمْ', YES, YES_A), ('2. İsim', 'مَا اسْمُكَ؟', MAVI, MAVI_A), ('3. Ülke', 'مِنْ أَيْنَ أَنْتَ؟', TUR, TUR_A), ('4. Memnuniyet', 'فُرْصَة سَعِيدَة', MOR, MOR_A)]
    for i, (bas, ar, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 28, bas, 10, c) + yazi(x + 40, 54, ar, 11.5, LAC)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Arapça tanışma diyaloğu akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'MÜENNES SIFAT TAMLAMASI UYUMU', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'هٰذِهِ طَالِبَةٌ جَدِيدَةٌ', 15, LAC) + yazi(180, 70, 'Müennes isim olan طَالِبَةٌ sıfatı da dişil ek (ـة) alır.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Sıfat tamlaması müennes uyumu panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    sorular = [('مَا اسْمُكَ؟', 'Adın nedir?', MAVI, MAVI_A), ('مِنْ أَيْنَ؟', 'Nerelisin?', TUR, TUR_A), ('جِنْسِيَّتُكَ؟', 'Uyruğun?', YES, YES_A), ('كَيْفَ حَالُكَ؟', 'Nasılsın?', MOR, MOR_A)]
    for i, (ar, tr, c, d) in enumerate(sorular):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, ar, 12, c) + f'<line x1="{x+8}" y1="44" x2="{x+72}" y2="44" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 64, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Arapça soru kalıpları eşleştirme kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: T - A - N - I - Ş - M - A', 11.5, YES)
    harfler = [('1', 'T'), ('2', 'A'), ('3', 'N'), ('4', 'I'), ('5', 'Ş'), ('6', 'M'), ('7', 'A')]
    for i, (no, h) in enumerate(harfler):
        x = 20 + i * 46
        ic += kutu(x, 32, 40, 48, '#eaf8f0', YES) + yazi(x + 20, 46, no, 9, SOLUK, ince=True) + yazi(x + 20, 68, h, 15, LAC)
    return svg(360, 96, ic, 'Tanışma şifresi harf kutuları', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
