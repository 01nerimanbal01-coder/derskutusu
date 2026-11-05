"""11. sınıf Felsefe 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kuramlar = [('Antroposentrizm', 'İnsan merkezci etik', MAVI, MAVI_A), ('Biyosentrizm', 'Canlı merkezci etik', YES, YES_A), ('Ekosentrizm', 'Çevre merkezci etik', TUR, TUR_A), ('Özsel Değer', 'Kendinde içsel değer', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kuramlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Çevre etiği yaklaşımları kavram kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'DOĞAYI KORUMA GEREKÇELERİNİN FELSEFİ KARŞILAŞTIRMASI', 10, MAVI)
    ic += kutu(16, 36, 156, 64, '#f4f8fe', MAVI) + yazi(94, 56, 'Araçsal Değer (Fayda)', 10, MAVI) + yazi(94, 78, 'İnsan sağlığı için koruma', 8.5, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, YES_A, YES) + yazi(266, 56, 'Özsel Değer (Saygı)', 10, YES) + yazi(266, 78, 'Canlı ve ekosistem için koruma', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Araçsal ve özsel değer karşılaştırması', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, YES_A, YES, 8)
    ic += yazi(180, 32, 'AHLAKİ DEĞER ÇEMBERİNİN GENİŞLEMESİ', 10.5, YES)
    ic += yazi(180, 58, 'Biyosentrizm: İnsan + Hayvan + Bitki (Tüm canlı organizmalar)', 9.5, LAC)
    ic += yazi(180, 82, 'Ekosentrizm: Canlılar + Toprak, Su, Hava, İklim (Tüm ekosistem bütünü)', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Biyosentrizm ve ekosentrizm kapsam farkı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    dusunurler = [('Bacon/Descartes', 'Mekanik doğa fikri', MAVI, MAVI_A), ('Schweitzer', 'Yaşama saygı etiği', YES, YES_A), ('Arne Naess', 'Derin ekoloji akımı', TUR, TUR_A), ('Hans Jonas', 'Gelecek kuşak ödevi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(dusunurler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Çevre felsefesi düşünürleri panosu', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    evrim = [('1. İlk Çağ', 'Uyumlu kozmos', YES, YES_A), ('2. Modern Çağ', 'Mekanik hakimiyet', MAVI, MAVI_A), ('3. 20. Yüzyıl', 'Ekolojik kriz/etik', TUR, TUR_A), ('4. Bütüncül Etik', 'Biyosferik eşitlik', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(evrim):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'İnsan-doğa ilişkisinin tarihsel dönüşümü', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'ALDO LEOPOLD · YERYÜZÜ (TOPRAK) ETİĞİ İLKESİ', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, '“Biyotik topluluğun bütünlüğünü, dengesini ve güzelliğini koru!”', 9.5, LAC) + yazi(180, 84, 'Toprak, su, bitkiler ve hayvanlar aynı ahlaki topluluğun eşit üyeleridir.', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Aldo Leopold Yeryüzü Etiği kartı', 34)

def g7():
    ic = kutu(4, 4, 352, 107, TUR_A, TUR) + yazi(180, 24, 'DEĞER TÜRLERİ, SÜRDÜRÜLEBİLİRLİK VE TÜRCÜLÜK ELEŞTİRİSİ', 9.5, TUR)
    ic += kutu(16, 36, 328, 64, '#fff8ee', TUR) + yazi(180, 58, 'Araçsal Değer  ·  Sürdürülebilirlik  ·  Türcülük Karşıtlığı (Singer)', 9.5, LAC) + yazi(180, 82, 'Gelecek kuşaklara yaşanabilir bir gezegen bırakmak ahlaki ödevdir.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Sürdürülebilirlik ve çevre etiği kavramları', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    ekoloji = [('Francis Bacon', 'Bilgi güçtür ilkesi', MAVI, MAVI_A), ('Sığ Ekoloji', 'Yüzeysel koruma', TUR, TUR_A), ('Derin Ekoloji', 'İçsel değer/eşitlik', YES, YES_A), ('Paul Taylor', 'Doğaya saygı etiği', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(ekoloji):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Sığ ve derin ekoloji karşılaştırma panosu', 34)

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
