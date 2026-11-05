"""6. sınıf Fen Bilimleri 14. hafta (Işığın Yansıması ve Yansıma Kanunları) görselleri.
SVG; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#475569'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(ic, etiket, w=360, h=115):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;max-height:22mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, boy=9.0, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def ayna_ciz(x1, x2, y):
    ciz = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{LAC}" stroke-width="2.2"/>'
    for tx in range(x1 + 8, x2 - 4, 14):
        ciz += f'<line x1="{tx}" y1="{y}" x2="{tx-6}" y2="{y+7}" stroke="{GRI}" stroke-width="1"/>'
    return ciz


def uygula(o):
    s = o['sorular']

    # s[0]: Temel yansıma modeli (Gelen ışın, Normal N, Yansıyan ışın, i ve r açıları)
    ic0 = kutu(6, 4, 348, 107, GRI_A, GRI)
    ic0 += ayna_ciz(60, 300, 94)
    ic0 += f'<line x1="180" y1="14" x2="180" y2="94" stroke="{MAVI}" stroke-width="1.3" stroke-dasharray="4,3"/>'
    ic0 += yazi(180, 12, 'N (Normal)', 8.5, MAVI)
    # Gelen ve yansıyan ışınlar
    ic0 += f'<line x1="95" y1="24" x2="180" y2="94" stroke="{KIR}" stroke-width="1.8"/>'
    ic0 += f'<polygon points="142,63 132,60 137,53" fill="{KIR}"/>'
    ic0 += f'<line x1="180" y1="94" x2="265" y2="24" stroke="{YES}" stroke-width="1.8"/>'
    ic0 += f'<polygon points="228,55 218,58 223,65" fill="{YES}"/>'
    ic0 += f'<path d="M161,78 A24,24 0 0,1 180,70" fill="none" stroke="{KIR}" stroke-width="1.1"/>'
    ic0 += f'<path d="M180,70 A24,24 0 0,1 199,78" fill="none" stroke="{YES}" stroke-width="1.1"/>'
    ic0 += yazi(164, 64, 'i', 9.5, KIR) + yazi(196, 64, 'r', 9.5, YES)
    ic0 += yazi(82, 42, 'Gelen Işın', 8.5, KIR) + yazi(282, 42, 'Yansıyan Işın', 8.5, YES)
    s[0]['gorsel'] = svg(ic0, 'Düzlem aynada gelen ışın, normal ve yansıyan ışın modeli')

    # s[1]: Ayna yüzeyiyle 25° açı yapan K ışını
    ic1 = kutu(6, 4, 348, 107, MAVI_A, MAVI)
    ic1 += ayna_ciz(50, 310, 92)
    ic1 += f'<line x1="180" y1="16" x2="180" y2="92" stroke="{MAVI}" stroke-width="1.2" stroke-dasharray="4,3"/>'
    ic1 += yazi(180, 13, 'N', 9.0, MAVI)
    ic1 += f'<line x1="72" y1="42" x2="180" y2="92" stroke="{KIR}" stroke-width="1.8"/>'
    ic1 += f'<line x1="180" y1="92" x2="288" y2="42" stroke="{YES}" stroke-width="1.8"/>'
    ic1 += f'<path d="M145,92 A35,35 0 0,1 149,78" fill="none" stroke="{TUR}" stroke-width="1.2"/>'
    ic1 += yazi(124, 86, '25°', 9.5, TUR)
    ic1 += yazi(88, 34, 'K Işını', 8.8, KIR)
    ic1 += yazi(202, 62, 'r = ?', 9.5, YES)
    s[1]['gorsel'] = svg(ic1, 'Ayna ile 25 derece açı yapan K ışını düzeneği')

    # s[2]: Düzgün Yansıma vs Dağınık Yansıma karşılaştırma çizimi
    ic2 = kutu(6, 6, 170, 103, CAM_A, CAM)
    ic2 += yazi(91, 20, 'Düzgün Yansıma (Ayna)', 8.6, CAM)
    ic2 += ayna_ciz(22, 160, 92)
    for dx in (0, 34, 68):
        ic2 += f'<line x1="{30+dx}" y1="34" x2="{58+dx}" y2="92" stroke="{KIR}" stroke-width="1.4"/>'
        ic2 += f'<line x1="{58+dx}" y1="92" x2="{86+dx}" y2="34" stroke="{YES}" stroke-width="1.4"/>'

    ic2 += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic2 += yazi(269, 20, 'Dağınık Yansıma (Pürüzlü)', 8.6, TUR)
    ic2 += f'<polyline points="196,92 218,83 242,95 268,81 294,94 318,82 342,93" fill="none" stroke="{LAC}" stroke-width="2"/>'
    ic2 += f'<line x1="208" y1="34" x2="230" y2="89" stroke="{KIR}" stroke-width="1.4"/><line x1="230" y1="89" x2="215" y2="36" stroke="{MOR}" stroke-width="1.4"/>'
    ic2 += f'<line x1="248" y1="34" x2="270" y2="82" stroke="{KIR}" stroke-width="1.4"/><line x1="270" y1="82" x2="312" y2="34" stroke="{MOR}" stroke-width="1.4"/>'
    ic2 += f'<line x1="288" y1="34" x2="310" y2="86" stroke="{KIR}" stroke-width="1.4"/><line x1="310" y1="86" x2="344" y2="54" stroke="{MOR}" stroke-width="1.4"/>'
    s[2]['gorsel'] = svg(ic2, 'Düzgün ve dağınık yansıma ışın diyagramı')

    # s[5]: Gelen ve yansıyan ışın arası 110°
    ic5 = kutu(6, 4, 348, 107, YES_A, YES)
    ic5 += ayna_ciz(50, 310, 92)
    ic5 += f'<line x1="180" y1="16" x2="180" y2="92" stroke="{MAVI}" stroke-width="1.2" stroke-dasharray="4,3"/>'
    ic5 += f'<line x1="82" y1="30" x2="180" y2="92" stroke="{KIR}" stroke-width="1.8"/>'
    ic5 += f'<line x1="180" y1="92" x2="278" y2="30" stroke="{YES}" stroke-width="1.8"/>'
    ic5 += f'<path d="M148,72 A38,38 0 0,1 212,72" fill="none" stroke="{MOR}" stroke-width="1.3"/>'
    ic5 += yazi(180, 52, 'Toplam = 110°', 9.0, MOR)
    ic5 += yazi(115, 84, 'α = ?', 9.5, TUR)
    s[5]['gorsel'] = svg(ic5, 'Gelen ve yansıyan ışın arası 110 derece olan düzenek')

    # s[6]: Yüzeye dik (90°) gelen lazer ışını
    ic6 = kutu(6, 4, 348, 107, MOR_A, MOR)
    ic6 += ayna_ciz(70, 290, 92)
    ic6 += kutu(162, 10, 36, 18, '#f8fafc', MOR, r=3) + yazi(180, 22, 'LAZER', 7.8, MOR)
    ic6 += f'<line x1="180" y1="28" x2="180" y2="92" stroke="{KIR}" stroke-width="2.2"/>'
    ic6 += f'<polygon points="180,68 175,58 185,58" fill="{KIR}"/>'
    ic6 += f'<polygon points="180,42 175,52 185,52" fill="{YES}"/>'
    ic6 += kutu(180, 82, 10, 10, 'none', LAC, r=0, kalin=1.0)
    ic6 += yazi(256, 54, 'Yüzeye Dik (90°)', 8.8, LAC)
    ic6 += yazi(256, 70, 'Normal (N) Üzerinden', 8.2, SOLUK, ince=True)
    s[6]['gorsel'] = svg(ic6, 'Düzlem aynaya dik gönderilen lazer ışını')

    # s[7]: Mikroskobik pürüzlü yüzeyde yerel normaller (N(a), N(b)) ve i=r kanıtı
    ic7 = kutu(6, 4, 348, 107, TUR_A, TUR)
    ic7 += yazi(180, 18, 'Pürüzlü Yüzeyin Yakın Görünümü (Her Noktada i = r)', 8.5, TUR)
    ic7 += f'<polyline points="40,94 140,76 220,96 320,74" fill="none" stroke="{LAC}" stroke-width="2"/>'
    # Nokta 1 (x=100, y=83)
    ic7 += f'<line x1="100" y1="83" x2="92" y2="38" stroke="{MAVI}" stroke-width="1.1" stroke-dasharray="3,2"/>'
    ic7 += yazi(90, 34, 'N(a)', 8.0, MAVI)
    ic7 += f'<line x1="62" y1="38" x2="100" y2="83" stroke="{KIR}" stroke-width="1.5"/>'
    ic7 += f'<line x1="100" y1="83" x2="126" y2="36" stroke="{YES}" stroke-width="1.5"/>'
    # Nokta 2 (x=260, y=87)
    ic7 += f'<line x1="260" y1="87" x2="250" y2="40" stroke="{MAVI}" stroke-width="1.1" stroke-dasharray="3,2"/>'
    ic7 += yazi(248, 35, 'N(b)', 8.0, MAVI)
    ic7 += f'<line x1="222" y1="42" x2="260" y2="87" stroke="{KIR}" stroke-width="1.5"/>'
    ic7 += f'<line x1="260" y1="87" x2="282" y2="38" stroke="{YES}" stroke-width="1.5"/>'
    s[7]['gorsel'] = svg(ic7, 'Dağınık yansımada farklı eğimli yüzey normalleri')

    # s[8]: K, L, M, P dört ışın kartı
    ic8 = kutu(4, 4, 352, 107, GRI_A, GRI)
    isinlar = [
        ('K Işını', 'Yüzeye dik (90°)', MAVI, MAVI_A),
        ('L Işını', 'Normalle 20°', YES, YES_A),
        ('M Işını', 'Aynayla 50°', TUR, TUR_A),
        ('P Işını', 'Aynayla 30°', MOR, MOR_A),
    ]
    for i, (b, alt, c, d) in enumerate(isinlar):
        x = 10 + i * 86
        ic8 += kutu(x, 13, 80, 89, d, c)
        ic8 += yazi(x + 40, 35, b, 9.0, c)
        ic8 += f'<line x1="{x+8}" y1="46" x2="{x+72}" y2="46" stroke="{c}" stroke-width="0.7"/>'
        ic8 += yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    s[8]['gorsel'] = svg(ic8, 'Dört farklı açıyla gelen K, L, M, P ışın kartları')

    # s[9]: Deneysel ölçüm tablosu (Kanıt kartı)
    ic9 = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic9 += yazi(180, 22, 'Lazer ve İletki Deneyi Ölçüm Sonuçları', 9.2, CAM)
    sutunlar = [
        ('1. Ölçüm', 'Gelme: 20°', 'Yansıma: 20°', MAVI, MAVI_A),
        ('2. Ölçüm', 'Gelme: 45°', 'Yansıma: 45°', YES, YES_A),
        ('3. Ölçüm', 'Gelme: 70°', 'Yansıma: 70°', MOR, MOR_A),
    ]
    for i, (b, g, yan, c, d) in enumerate(sutunlar):
        x = 14 + i * 112
        ic9 += kutu(x, 31, 106, 70, d, c)
        ic9 += yazi(x + 53, 48, b, 8.6, c)
        ic9 += yazi(x + 53, 68, g, 8.4, LAC)
        ic9 += yazi(x + 53, 86, yan, 8.4, c)
    s[9]['gorsel'] = svg(ic9, 'Üç deneysel ölçümde gelme ve yansıma açısı verileri')
