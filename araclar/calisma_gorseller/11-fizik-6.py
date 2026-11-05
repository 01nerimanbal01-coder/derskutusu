"""11. sınıf Fizik 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    yasalar = [('1. Eylemsizlik', 'F_net = 0 => a = 0', MAVI, MAVI_A), ('2. Temel Yasa', 'F_net = m . a', YES, YES_A), ('3. Etki-Tepki', 'F_AB = -F_BA', TUR, TUR_A), ('Sürtünme', 'f_s = k . N', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(yasalar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Newton hareket yasaları özet kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 22, 'SERBEST CİSİM DİYAGRAMI · YATAY SÜRTÜNMELİ DÜZLEM', 10, MAVI)
    ic += f'<line x1="24" y1="88" x2="336" y2="88" stroke="{LAC}" stroke-width="1.5"/>'
    ic += kutu(130, 44, 100, 44, YES_A, YES) + yazi(180, 64, 'm = 4 kg', 10.5, YES) + yazi(180, 80, 'k = 0,25 (N = 40 N)', 8.5, LAC, ince=True)
    ic += f'<line x1="230" y1="64" x2="305" y2="64" stroke="{MAVI}" stroke-width="2"/><polygon points="312,64 303,60 303,68" fill="{MAVI}"/>' + yazi(275, 54, 'F = 30 N', 10, MAVI)
    ic += f'<line x1="130" y1="78" x2="65" y2="78" stroke="{KIR}" stroke-width="2"/><polygon points="58,78 67,74 67,82" fill="{KIR}"/>' + yazi(90, 68, 'f_s = 10 N', 9.5, KIR)
    return svg(360, 115, ic, 'Yatay sürtünmeli düzlemde kuvvet diyagramı', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, TUR_A, TUR, 8)
    ic += yazi(180, 32, 'ETKİ - TEPKİ ÇİFTİ KURALI', 10.5, TUR)
    ic += yazi(180, 58, 'Ağırlık (G) ve Normal Kuvvet (N) aynı cisme etki eder; etki-tepki çifti değildir!', 9.5, LAC)
    ic += yazi(180, 82, 'Etki ve tepki kuvvetleri daima iki farklı cisim üzerine uygulanır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Etki-tepki çifti kuralı bilgi kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    kurallar = [('Sabit Hız', 'İvme ve F_net sıfır', MAVI, MAVI_A), ('SCD Kuralı', 'm.a vektörü çizilmez', KIR, KIR_A), ('Eğik Düzlem', 'a = g . sin α', YES, YES_A), ('İp Gerilmesi', 'Her zaman çeker', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(kurallar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Serbest cisim diyagramı temel kuralları', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlari = [('1. SCD Çizimi', 'Gerçek kuvvetler', YES, YES_A), ('2. Sürtünme', 'f_s = k . N hesabı', MAVI, MAVI_A), ('3. Ortak İvme', 'a = F_net / m_top', TUR, TUR_A), ('4. İp Gerilmesi', 'Tek kütlede T bul', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlari):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Bağlı cisimlerde dinamik problem çözümü', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 22, 'SÜRTÜNMESİZ YATAY DÜZLEMDE İPLE BAĞLI CİSİMLER', 10, CAM)
    ic += f'<line x1="20" y1="88" x2="340" y2="88" stroke="{LAC}" stroke-width="1.5"/>'
    ic += kutu(40, 48, 76, 40, MAVI_A, MAVI) + yazi(78, 72, 'm1 = 2 kg', 10, MAVI)
    ic += f'<line x1="116" y1="68" x2="180" y2="68" stroke="{TUR}" stroke-width="2"/>' + yazi(148, 58, 'İp (T = ?)', 9.5, TUR)
    ic += kutu(180, 44, 86, 44, YES_A, YES) + yazi(223, 70, 'm2 = 3 kg', 10, YES)
    ic += f'<line x1="266" y1="66" x2="324" y2="66" stroke="{KIR}" stroke-width="2"/><polygon points="331,66 322,62 322,70" fill="{KIR}"/>' + yazi(298, 54, 'F = 30 N', 9.5, KIR)
    return svg(360, 115, ic, 'İple bağlı iki kütle ve gerilme kuvveti düzeneği', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'EYLEMSİZLİK, NET KUVVET YÖNÜ VE KİNETİK SÜRTÜNME', 10, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Eylemsizlik (Durumu Koruma) · F_net // a · Kinetik Sürtünme', 9.5, LAC) + yazi(180, 82, 'İvme vektörü her zaman net kuvvet vektörü ile aynı yönlüdür.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Eylemsizlik ve ivme yönü özeti', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    bilesen = [('Ağırlık (G)', 'G = m . g düşey', MAVI, MAVI_A), ('Paralel (G_x)', 'm . g . sin α', TUR, TUR_A), ('Normal (N)', 'm . g . cos α', YES, YES_A), ('Kütle (m)', 'm = F_net / a', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(bilesen):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Eğik düzlem kuvvet bileşenleri panosu', 34)

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
