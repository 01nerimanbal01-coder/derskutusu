"""9. sınıf Arapça 5. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    zamirler = [('Ene (أَنَا)', 'Ben (Ortak)', MAVI, MAVI_A), ('Ente (أَنْتَ)', 'Sen (Müzekker)', YES, YES_A), ('Enti (أَنْتِ)', 'Sen (Müennes)', TUR, TUR_A), ('Huve / Hiye', 'O (Eril / Dişil)', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(zamirler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Arapça tekil şahıs zamirleri tablosu', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'MEMLEKET SORMA · MÜZEKKER VE MÜENNES UYUMU', 10.5, MAVI)
    ic += kutu(16, 36, 158, 64, '#f4f8fe', MAVI) + yazi(95, 58, 'Min eyne ente?', 10.5, MAVI) + yazi(95, 78, '(Nerelisin? - Erkeğe)', 9, SOLUK, ince=True)
    ic += kutu(186, 36, 158, 64, YES_A, YES) + yazi(265, 58, 'Min eyne enti?', 10.5, YES) + yazi(265, 78, '(Nerelisin? - Kadına)', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Memleket sorma kalıpları kartı', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'TÂ-İ MERBÛTA (ة) İLE MÜENNES YAPMA KURALI', 10.5, TUR)
    ic += yazi(180, 58, 'tâlibun ➔ tâlibetun   |   mühendisun ➔ mühendisetun', 10.5, LAC)
    ic += yazi(180, 82, 'Eril meslek ve sıfatların sonuna kapalı tâ (-etun) eklenerek dişil yapılır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Müzekker ve müennes kelime dönüşümü kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ilkeler = [('Hâzâ (هٰذَا)', 'Bu (Müzekker)', MAVI, MAVI_A), ('Hâzihî (هٰذِهِ)', 'Bu (Müennes)', TUR, TUR_A), ('Men (مَنْ)', 'Kim? (Akıllı)', YES, YES_A), ('Mâ (مَا)', 'Ne? (Kavram)', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 10, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'İşaret zamirleri ve soru edatları panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. Selam', 'Es-selâmu aleykum', YES, YES_A), ('2. İsim', 'Mâ ismuke / ismî', MAVI, MAVI_A), ('3. Hal-Hatır', 'Keyfe hâluke?', TUR, TUR_A), ('4. Veda', 'İle\'l-likâ', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 10.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Tanışma diyaloğu basamakları akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'SOSYAL İFADELER · VECİZ SÖZ VE HADİS-İ ŞERİF', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'اَلسَّلَامُ قَبْلَ الْكَلَامِ  (Es-selâmu kable\'l-kelâm)', 11, LAC) + yazi(180, 84, 'İletişim adabında söze başlamadan önce ilk olarak selam verilir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Selam kelamdan öncedir veciz söz panosu', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'CÜMLE KURULUMUNDA ZAMİR VE HARF-İ CER UYUMU', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Huve tâlibun (Eril)  ·  Hâzihî sadîkatî (Dişil)  ·  Ene min Turkiyâ', 10, LAC) + yazi(180, 82, 'Özne zamiri ve işaret ismi yüklemin cinsiyetiyle tam uyum gösterir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Arapça cümle uyumu özet şeması', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    kaliplar = [('Men hâzâ?', 'Bu kimdir? (Eril)', MAVI, MAVI_A), ('Fursatun saîde', 'Memnun oldum', TUR, TUR_A), ('Mesâu\'l-hayr', 'İyi akşamlar', YES, YES_A), ('Ma\'a\'s-selâme', 'Güle güle', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(kaliplar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Günlük selamlaşma ve veda kalıpları kartı', 34)

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
