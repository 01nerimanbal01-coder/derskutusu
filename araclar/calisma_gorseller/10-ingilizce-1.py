"""10. sınıf İngilizce 1. hafta (İngilizce Öğrenme Sürecini Planlama ve Değerlendirme) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178); en_fazla=34."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2, ek=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def g0_okuma_stratejileri():
    ic = kutu(4, 4, 352, 92, GRI_A, GRI)
    kartlar = [
        ('Skimming', 'Ana fikir (Gist)', MAVI, MAVI_A),
        ('Scanning', 'Belirli bilgi bulma', TUR, TUR_A),
        ('Detailed', 'Derinlemesine okuma', YES, YES_A),
        ('Predicting', 'İçeriği tahmin etme', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(kartlar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 80, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Dört temel okuma stratejisi kartı', 34)


def g1_yazma_sureci():
    ic = kutu(4, 4, 352, 92, MAVI_A, MAVI)
    ic += yazi(180, 22, 'WRITING PROCESS: DRAFTING TO FINAL PRODUCT', 11, MAVI)
    ic += kutu(14, 32, 160, 56, '#f4f8fe', MAVI, 6, 1.1)
    ic += yazi(94, 48, '1. First Draft', 11, MAVI)
    ic += yazi(94, 68, 'İlk taslak metni yazma', 9.5, LAC, ince=True)

    ic += kutu(186, 32, 160, 56, YES_A, YES, 6, 1.1)
    ic += yazi(266, 48, '2. Peer Feedback', 11, YES)
    ic += yazi(266, 68, 'Akran dönütüyle geliştirme', 9.5, LAC, ince=True)
    return svg(360, 100, ic, 'Yazma süreci taslak ve geri bildirim aşamaları', 34)


def g2_scanning_gorevi():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    ic += kutu(10, 10, 340, 74, TUR_A, TUR, 8, 1.2)
    ic += yazi(180, 28, 'SCANNING TASK: FINDING DEPARTURE TIME', 11, TUR)
    ic += yazi(180, 50, 'Train to Ankara departs at 08:45 AM from Platform 3', 12.5, LAC)
    ic += yazi(180, 70, 'Belirli bilgiye odaklanarak hızlı arama yapma', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Scanning arama tekniği görev kartı', 34)


def g3_stratejiler():
    ic = kutu(4, 4, 352, 90, GRI_A, GRI)
    ilkeler = [
        ('In Context', 'Bağlamda öğren', MAVI, MAVI_A),
        ('Gist Reading', 'Genel fikir', TUR, TUR_A),
        ('Rubric Guide', 'Ölçüte göre yaz', YES, YES_A),
        ('Peer Review', 'Yapıcı dönüt', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(ilkeler):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 78, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 10.5, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 98, ic, 'Dört temel İngilizce öğrenme ilkesi', 34)


def g5_proje_dongusu():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    adimlari = [
        ('1. Rubric', 'Ölçüt incele', YES, YES_A),
        ('2. Draft', 'Taslak yaz', MAVI, MAVI_A),
        ('3. Edit', 'Dönütle düzelt', TUR, TUR_A),
        ('4. Publish', 'Portfolyo sun', MOR, MOR_A)
    ]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 30, bas, 11, c)
        ic += yazi(x + 40, 55, alt, 9.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x + 82},48 {x + 85},44 {x + 85},52" fill="{GRI}"/>'
    return svg(360, 96, ic, 'Proje tamamlama ve yayınlama adımları', 34)


def g6_aciklama_isteme():
    ic = kutu(4, 4, 352, 88, CAM_A, CAM)
    ic += yazi(180, 24, 'COLLABORATIVE DISCUSSION: ASKING FOR CLARIFICATION', 10.5, CAM)
    ic += kutu(20, 36, 320, 44, '#eaf7fa', CAM, 6, 1.2)
    ic += yazi(180, 54, '"Could you explain what you mean by that example?"', 12, LAC)
    ic += yazi(180, 70, '(Bu örnekle ne demek istediğinizi açıklayabilir misiniz?)', 9.5, SOLUK, ince=True)
    return svg(360, 96, ic, 'Grup çalışmasında nazik açıklama isteme kartı', 34)


def g8_degerlendirme_araclari():
    ic = kutu(4, 4, 352, 88, GRI_A, GRI)
    araclar = [
        ('Checklist', 'Kontrol listesi', MAVI, MAVI_A),
        ('Draft', 'Taslak çalışma', TUR, TUR_A),
        ('Feedback', 'Yapıcı dönüt', YES, YES_A),
        ('Portfolio', 'Dijital arşiv', MOR, MOR_A)
    ]
    for i, (en, tr, c, d) in enumerate(araclar):
        x = 10 + i * 86
        ic += kutu(x, 10, 80, 76, d, c, 6, 1.2)
        ic += yazi(x + 40, 32, en, 11, c)
        ic += f'<line x1="{x + 8}" y1="42" x2="{x + 72}" y2="42" stroke="{c}" stroke-width="0.8"/>'
        ic += yazi(x + 40, 62, tr, 9.5, LAC, ince=True)
    return svg(360, 96, ic, 'Dört değerlendirme ve çalışma aracı', 34)


def g10_sifre_seridi():
    ic = kutu(4, 4, 352, 88, YES_A, YES)
    ic += yazi(180, 22, 'KEYWORD PUZZLE: D - R - A - F - T', 11.5, YES)
    harfler = [('1', 'D'), ('2', 'R'), ('3', 'A'), ('4', 'F'), ('5', 'T')]
    for i, (no, h) in enumerate(harfler):
        x = 45 + i * 55
        ic += kutu(x, 32, 45, 48, '#eaf8f0', YES, 6, 1.2)
        ic += yazi(x + 22.5, 46, no, 9.5, SOLUK, ince=True)
        ic += yazi(x + 22.5, 68, h, 16, LAC)
    return svg(360, 96, ic, 'Draft şifresi anahtar harf kutuları', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0_okuma_stratejileri()
    s[1]['gorsel'] = g1_yazma_sureci()
    s[2]['gorsel'] = g2_scanning_gorevi()
    s[3]['gorsel'] = g3_stratejiler()
    s[5]['gorsel'] = g5_proje_dongusu()
    s[6]['gorsel'] = g6_aciklama_isteme()
    s[8]['gorsel'] = g8_degerlendirme_araclari()
    s[10]['gorsel'] = g10_sifre_seridi()
