"""12. sınıf Coğrafya 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.0, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.0, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.0, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.5, kc) + yazi(x + 52, 78, alt, 8.0, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Türkiye işlevsel bölge sınıflandırması', [('Yönetsel', '81 İl · Valilik/Bel.', MAVI, MAVI_A), ('Hizmet Bölgesi', 'DSİ · Karayolları', YES, YES_A), ('İstatistiki', 'TÜİK Düzey 1-2-3', TUR, TUR_A), ('Plan Bölgesi', 'GAP · DAP · KOP', MOR, MOR_A)])

def g1():
    return uclu('Bölgesel kalkınma projeleri hedefleri', 'TÜRKİYE BÖLGESEL KALKINMA PROJELERİ (PLAN BÖLGELERİ)', ('GAP (9 İl)', '22 Baraj · 19 HES', MAVI, MAVI_A), ('KOP (8 İl)', 'Mavi Tünel · Göksu', YES, YES_A), ('ZBK (3 İl)', 'Taş Kömürü · Filyos', TUR, TUR_A), MAVI, MAVI_A)

def g2():
    return pano('Dağların uzanışı ve ulaşım doğrultusu', 'YERYÜZÜ ŞEKİLLERİNİN TÜRKİYE ULAŞIMINA ETKİSİ', 'Doğu-Batı Doğrultusu: Dağlar paralel uzanır → Ulaşım kolay ve ucuz', 'Kuzey-Güney Doğrultusu: Dağlar dik kesilir → Geçit ve tüneller gerekir', CAM, CAM_A, '#eaf7fa')

def g3():
    return kart4('İşlevsel bölge ve proje bilgileri', [('Hizmet Sınırı', 'İl sınırıyla çakışmaz', KIR, KIR_A), ('DAP Kapsamı', '15 il (En fazla il)', MAVI, MAVI_A), ('TÜİK Düzey 3', '81 il birimi', YES, YES_A), ('YHGP (4 İl)', 'Amasya·Çorum·Samsun·Tokat', MOR, MOR_A)])

def g5():
    return akis4('TÜİK İBBS kademeleri birim sayısı', [('1. Ülke', 'Türkiye (1 birim)', MOR, MOR_A), ('2. Düzey 1', '12 bölge birimi', MAVI, MAVI_A), ('3. Düzey 2', '26 alt bölge', TUR, TUR_A), ('4. Düzey 3', '81 il birimi', YES, YES_A)])

def g6():
    return uclu('Ulaşım mühendislik projeleri', 'DOĞAL ENGELLERİ AŞAN ULAŞIM PROJELERİ', ('Ovit / Zigana', 'Kuzey-Güney dağ tüneli', YES, YES_A), ('Marmaray / Avrasya', 'Boğaz tüp geçitleri', MAVI, MAVI_A), ('Çanakkale / Osmangazi', 'Boğaz ve körfez köprü', TUR, TUR_A), MOR, MOR_A)

def g7():
    return pano('İşlevsel bölge, Yeşil Yol ve Filyos Limanı', 'KALKINMA PROJELERİNDE ÖNE ÇIKAN UYGULAMALAR', 'İşlevsel Bölge Odakları · DOKAP Yeşil Yol · ZBK Filyos Limanı', 'Her kalkınma projesi bölgenin coğrafi potansiyelini ekonomiye kazandırır.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Ulaşımı etkileyen doğal ve beşerî faktörler', [('Coğrafi Konum', '3 kıta + Boğazlar', MAVI, MAVI_A), ('İklim Etkisi', 'Kar, buzlanma, sis', CAM, CAM_A), ('Sermaye-Teknoloji', 'YHT, otoyol, köprü', TUR, TUR_A), ('YHGP Hedefi', 'Havza ıslahı ve taşkın', YES, YES_A)])

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
