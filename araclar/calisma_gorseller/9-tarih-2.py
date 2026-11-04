"""9. sınıf Tarih 2. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    kavramlar = [('Kaynak (Belge)', 'Geçmişten kalan iz', MAVI, MAVI_A), ('Tenkit (Eleştiri)', 'Güvenilirlik sınama', YES, YES_A), ('Tasnif', 'Konu/zaman sınıflama', TUR, TUR_A), ('Kronoloji', 'Zaman dizini bilimi', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kavramlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c) + yazi(x + 40, 30, b, 9.5, c) + f'<line x1="{x+8}" y1="40" x2="{x+72}" y2="40" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 100, ic, 'Tarih araştırması temel kavramları kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI) + yazi(180, 22, 'TARİHÎ HAFIZA MEKÂNI · ÇANAKKALE ŞEHİTLER ABİDESİ', 11, MAVI)
    ic += kutu(20, 32, 320, 54, '#f4f8fe', MAVI) + yazi(180, 50, 'Ortak Aidiyet Duygusu ve Millî Bilincin Canlı Tutulması', 11.5, LAC) + yazi(180, 70, 'Hafıza mekânları geçmiş ile gelecek arasında köprü kurar.', 9.5, SOLUK, ince=True)
    return svg(360, 100, ic, 'Tarihî anıt ve hafıza mekânı panosu', 34)

def g2():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI) + kutu(10, 10, 340, 74, TUR_A, TUR, 8)
    ic += yazi(180, 28, 'TARİHSEL EMPATİ VE DÖNEMSELLİK İLKESİ', 11, TUR)
    ic += yazi(180, 48, 'Olaylar bugünün ahlak ve anlayışıyla değil, dönemin koşullarıyla değerlendirilir.', 10, LAC)
    ic += yazi(180, 68, 'Tarihsel yanılgı (anakronizm) nesnel araştırmayı engeller.', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Tarihsel empati ve anakronizm ilkesi', 34)

def g3():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [('Yer &amp; Zaman', 'Somut bağlam', MAVI, MAVI_A), ('Neden &amp; Sonuç', 'Nedensellik bağı', TUR, TUR_A), ('Belgeye Dayanma', 'Kanıtsız tarih olmaz', YES, YES_A), ('Objektiflik', 'Tarafsız bakış açısı', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c) + yazi(x + 40, 30, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, alt, 8.5, LAC, ince=True)
    return svg(360, 98, ic, 'Tarih biliminin dört temel araştırma ilkesi', 34)

def g5():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [('1. Tarama', 'Kaynak arama', YES, YES_A), ('2. Tasnif', 'Sınıflandırma', MAVI, MAVI_A), ('3. Tahlil', 'Çözümleme', TUR, TUR_A), ('4. Tenkit', 'Eleştiri (iç-dış)', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 30, bas, 10.5, c) + yazi(x + 40, 55, alt, 9, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},48 {x+85},44 {x+85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Bilimsel tarih araştırması basamakları akış şeması', 34)

def g6():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM) + yazi(180, 24, 'NÜMİZMATİK · TARİHÎ SİKKE (MADENİ PARA) ANALİZİ', 11, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM) + yazi(180, 52, 'Hükümdar Tuğrası · Basım Yılı ve Yeri · Maden Türü', 10.5, LAC) + yazi(180, 70, 'Ekonomik güç, devlet teşkilatı ve egemenlik sembolü hakkında bilgi verir.', 9, SOLUK, ince=True)
    return svg(360, 96, ic, 'Tarihî sikke nümizmatik analiz panosu', 34)

def g8():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    bilimler = [('Arkeoloji', 'Kazı bilimi', MAVI, MAVI_A), ('Paleografya', 'Eski yazı bilimi', TUR, TUR_A), ('Nümizmatik', 'Eski madeni paralar', YES, YES_A), ('Filoloji', 'Dil ve metin bilimi', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(bilimler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c) + yazi(x + 40, 32, b, 10, c) + f'<line x1="{x+8}" y1="42" x2="{x+72}" y2="42" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 62, tr, 8.5, LAC, ince=True)
    return svg(360, 96, ic, 'Tarihe yardımcı bilim dalları kartı', 34)

def g10():
    ic = kutu(4, 4, 352, 88, YES_A, YES) + yazi(180, 22, 'ANAHTAR KAVRAM: M - İ - R - A - S', 11.5, YES)
    harfler = [('1', 'M'), ('2', 'İ'), ('3', 'R'), ('4', 'A'), ('5', 'S')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES) + yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True) + yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Miras şifresi harf kutuları', 34)

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
