"""5. sınıf Matematik 7. hafta (Üçgenlerin Kenar ve Açı Özellikleri ile Pergel ve Cetvel Kullanarak Üçgen İnşası) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def es_cember_eskenar_svg():
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    r = 46
    kx, ky = 152, 74
    lx, ly = kx + r, ky
    mx = (kx + lx) / 2
    my = ky - r * math.sin(math.radians(60))
    ic += f'<circle cx="{kx}" cy="{ky}" r="{r}" fill="{MAVI_A}" fill-opacity="0.55" stroke="{MAVI}" stroke-width="1.6" stroke-dasharray="5 3"/>'
    ic += f'<circle cx="{lx}" cy="{ly}" r="{r}" fill="{TUR_A}" fill-opacity="0.55" stroke="{TUR}" stroke-width="1.6" stroke-dasharray="5 3"/>'
    ic += f'<polygon points="{kx},{ky} {lx},{ly} {mx:.1f},{my:.1f}" fill="#12a15022" stroke="{YES}" stroke-width="2.4"/>'
    ic += f'<circle cx="{kx}" cy="{ky}" r="3.5" fill="{LAC}"/>' + yazi(kx - 12, ky + 4, 'K', 11.5, MAVI)
    ic += f'<circle cx="{lx}" cy="{ly}" r="3.5" fill="{LAC}"/>' + yazi(lx + 12, ly + 4, 'L', 11.5, TUR)
    ic += f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="3.5" fill="{LAC}"/>' + yazi(mx, my - 8, 'M', 11.5, YESIL_K)
    ic += yazi((kx + lx) / 2, ky + 15, '8 cm', 10.8, LAC)

    ic += f'<rect x="300" y="18" width="276" height="88" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(438, 38, 'Çember Merkezleri ve Kesişim Bilgisi', 10.6, YESIL_K)
    ic += yazi(314, 58, 'K ve L merkezli çemberler birbirinin merkezinden geçer.', 9.4, LAC, 'start', ince=True)
    ic += yazi(314, 76, 'Yarıçap uzunluğu |KL| = 8 cm olarak verilmiştir.', 9.6, LAC, 'start', ince=True)
    ic += yazi(314, 94, 'M noktası iki çember yayının kesişim noktasıdır.', 9.6, LAC, 'start', ince=True)
    return svg(600, 126, ic, 'Merkezleri K ve L olan 8 cm yarıçaplı iki eş çemberin M kesişim noktasıyla oluşturduğu KLM üçgeni.', 23)


def pergel_insa_kartlari_svg():
    kartlar = [
        ('1. Kart', 'Taban |AB| = 6 cm', 'Yaylar: 6 cm ve 6 cm', MAVI, MAVI_A),
        ('2. Kart', 'Taban |PR| = 4 cm', 'Yaylar: 7 cm ve 7 cm', YES, YES_A),
        ('3. Kart', 'Taban |KL| = 8 cm', 'Yaylar: 5 cm ve 6 cm', KIR, '#fdeaea'),
        ('4. Kart', 'Taban |DE| = 5 cm', 'Yaylar: 5 cm ve 8 cm', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 10.8, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.2, LAC)
        ic += yazi(x + 68, 74, s2, 9.6, LAC, ince=True)
    return svg(600, 104, ic, 'Dört üçgen inşa kartında taban uzunlukları ve uç noktalardan çizilen yayların yarıçapları.', 22)


def dort_ucgen_aci_modelleri_svg():
    modeller = [
        ('1. Üçgen', '60° ve 60°', '3. açı: ?', YES, YES_A, '42,80 110,80 76,34'),
        ('2. Üçgen', '90° ve 45°', '3. açı: ?', MAVI, MAVI_A, '44,80 108,80 44,34'),
        ('3. Üçgen', '110° ve 35°', '3. açı: ?', TUR, TUR_A, '32,80 120,80 76,46'),
        ('4. Üçgen', '50° ve 60°', '3. açı: ?', MOR, MOR_A, '38,80 114,80 68,36'),
    ]
    ic = ''
    for i, (bas, acilar, soru, renk, arka, pts) in enumerate(modeller):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="6" width="136" height="104" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 22, bas, 11, renk)
        kay_pts = ' '.join(f'{ int(p.split(",")[0]) + x },{ p.split(",")[1] }' for p in pts.split())
        ic += f'<polygon points="{kay_pts}" fill="#ffffffbb" stroke="{renk}" stroke-width="2"/>'
        ic += yazi(x + 68, 96, f'{acilar} ({soru})', 10.3, LAC)
    return svg(600, 116, ic, 'İki iç açısı verilen dört üçgen modeli: 1. 60-60, 2. 90-45, 3. 110-35, 4. 50-60 derece.', 23)


def ikizkenar_tepe_acisi_svg():
    ic = f'<rect x="6" y="6" width="588" height="106" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    px, py = 150, 25
    rx, ry = 104, 96
    sx, sy = 196, 96
    ic += f'<polygon points="{px},{py} {rx},{ry} {sx},{sy}" fill="#fff" stroke="{MAVI}" stroke-width="2.4"/>'
    # Eşit kenar çentikleri
    ic += f'<line x1="122" y1="56" x2="132" y2="60" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<line x1="178" y1="56" x2="168" y2="60" stroke="{KIR}" stroke-width="2"/>'
    ic += yazi(px, py - 6, 'P (40°)', 10.4, MAVI)
    ic += yazi(rx - 14, ry + 4, 'R (?)', 10.8, KIR)
    ic += yazi(sx + 16, sy + 4, 'S (?)', 10.8, KIR)

    ic += f'<rect x="282" y="18" width="294" height="82" rx="8" fill="#fff" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(429, 38, 'PRS İkizkenar Üçgeni Verileri', 11.2, MAVI)
    ic += yazi(298, 58, 'Eşit yan kenarlar: |PR| = |PS|', 10.6, LAC, 'start', ince=True)
    ic += yazi(298, 76, 'Tepe açısı: s(P) = 40°', 10.6, LAC, 'start', ince=True)
    ic += yazi(298, 92, 'Taban açıları: s(R) = s(S) = ?', 10.6, KIR, 'start')
    return svg(600, 118, ic, 'PRS ikizkenar üçgeninde PR=PS, P tepe açısı 40 derece, R ve S taban açıları soru işareti.', 23)


def eskenar_insa_adimlari_svg():
    adimlar = [
        ('Taban Çizimi', 'Cetvelle 5 cm [AB]', MAVI, MAVI_A),
        ('A Merkezli Yay', 'Pergel 5 cm (A ucu)', MOR, MOR_A),
        ('B Merkezli Yay', 'Aynı açıklıkla 2. yay', TUR, TUR_A),
        ('Kesişimi Birleştir', 'C noktasından ABC', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="82" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11, renk)
        ic += yazi(x + 68, 62, alt, 10.4, LAC, ince=True)
    return svg(600, 98, ic, 'Pergel ve cetvelle 5 cm kenarlı eşkenar üçgen inşa etme adımları.', 22)


def siniflandirma_tablosu_svg():
    ic = f'<rect x="8" y="6" width="584" height="104" rx="9" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    sut_x = [180, 320, 460]
    basliklar = ['Dar Açılı', 'Dik Açılı', 'Geniş Açılı']
    for sx, b in zip(sut_x, basliklar):
        ic += f'<rect x="{sx}" y="12" width="124" height="22" rx="5" fill="{MAVI}"/>'
        ic += yazi(sx + 62, 27, b, 10.6, '#fff')
    satirlar = [
        ('Eşkenar Üçgen', [('Uygun (60°-60°-60°)', YES, YES_A), ('X (Çizilemez)', KIR, '#fdeaea'), ('Y (Çizilemez)', KIR, '#fdeaea')]),
        ('İkizkenar Üçgen', [('Uygun (70°-70°-40°)', YES, YES_A), ('Uygun (90°-45°-45°)', YES, YES_A), ('Uygun (120°-30°-30°)', YES, YES_A)]),
        ('Çeşitkenar Üçgen', [('Uygun (50°-60°-70°)', YES, YES_A), ('Uygun (90°-60°-30°)', YES, YES_A), ('Uygun (110°-40°-30°)', YES, YES_A)]),
    ]
    for r_i, (ad, hucreler) in enumerate(satirlar):
        y = 38 + r_i * 23
        ic += f'<rect x="18" y="{y}" width="154" height="20" rx="4" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.1"/>'
        ic += yazi(95, y + 14, ad, 10.4, LAC)
        for sx, (met, renk, arka) in zip(sut_x, hucreler):
            ic += f'<rect x="{sx}" y="{y}" width="124" height="20" rx="4" fill="{arka}" stroke="{renk}" stroke-width="1.2"/>'
            ic += yazi(sx + 62, y + 14, met, 10, renk)
    return svg(600, 116, ic, 'Üçgenlerin kenar ve açılarına göre sınıflandırma tablosu; eşkenar-dik (X) ve eşkenar-geniş (Y) çizilemez.', 23)


def farkli_cember_cesitkenar_svg():
    ic = f'<rect x="6" y="6" width="588" height="110" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ax, ay = 116, 78
    bx, by = 216, 78
    cx, cy = 178, 32
    ic += f'<circle cx="{ax}" cy="{ay}" r="42" fill="{MAVI_A}" fill-opacity="0.5" stroke="{MAVI}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += f'<circle cx="{bx}" cy="{by}" r="32" fill="{TUR_A}" fill-opacity="0.5" stroke="{TUR}" stroke-width="1.5" stroke-dasharray="4 3"/>'
    ic += f'<polygon points="{ax},{ay} {bx},{by} {cx},{cy}" fill="#7c3aed22" stroke="{MOR}" stroke-width="2.2"/>'
    ic += f'<circle cx="{ax}" cy="{ay}" r="3.2" fill="{LAC}"/>' + yazi(ax - 12, ay + 4, 'A', 11, MAVI)
    ic += f'<circle cx="{bx}" cy="{by}" r="3.2" fill="{LAC}"/>' + yazi(bx + 12, by + 4, 'B', 11, TUR)
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{LAC}"/>' + yazi(cx, cy - 7, 'C', 11, MOR)
    ic += yazi(134, 51, '9 cm', 9.8, MAVI)
    ic += yazi(216, 40, '6 cm', 9.8, TUR)
    ic += yazi(171, 91, '10 cm', 9.8, LAC)

    ic += f'<rect x="292" y="18" width="286" height="86" rx="8" fill="#fff" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(435, 38, 'İki Farklı Çemberle İnşa Verileri', 11.2, MOR)
    ic += yazi(308, 58, 'A merkezli çemberin yarıçapı: |AC| = 9 cm', 10.4, LAC, 'start', ince=True)
    ic += yazi(308, 76, 'B merkezli çemberin yarıçapı: |BC| = 6 cm', 10.4, LAC, 'start', ince=True)
    ic += yazi(308, 94, 'Merkezler arası doğru parçası: |AB| = 10 cm', 10.4, LAC, 'start', ince=True)
    return svg(600, 122, ic, 'A merkezli 9 cm ve B merkezli 6 cm yarıçaplı iki çemberin C kesişimiyle oluşan 9-6-10 cm kenarlı ABC üçgeni.', 23)


def dogrusal_iki_ucgen_svg():
    ic = f'<rect x="6" y="6" width="588" height="108" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    bx, by = 60, 92
    cx, cy = 148, 92
    dx, dy = 236, 92
    ax, ay = 104, 24
    ex, ey = 148, 24
    ic += f'<line x1="36" y1="{cy}" x2="262" y2="{cy}" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<polygon points="{bx},{by} {cx},{cy} {ax},{ay}" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2.2"/>'
    ic += f'<polygon points="{cx},{cy} {dx},{dy} {ex},{ey}" fill="{TUR_A}" stroke="{TUR}" stroke-width="2.2"/>'
    ic += f'<rect x="{cx}" y="{cy - 12}" width="12" height="12" fill="none" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(bx, by + 15, 'B', 10.8, LAC)
    ic += yazi(cx, cy + 15, 'C', 10.8, LAC)
    ic += yazi(dx, dy + 15, 'D', 10.8, LAC)
    ic += yazi(ax - 8, ay - 4, 'A', 10.8, MAVI)
    ic += yazi(ex + 8, ey - 4, 'E', 10.8, TUR)
    ic += yazi(104, 72, 'Eşkenar', 10.2, MAVI)
    ic += yazi(134, 48, '?', 11.5, KIR)

    ic += f'<rect x="284" y="18" width="292" height="84" rx="8" fill="#fff" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(430, 38, 'B, C ve D Doğrusal Noktaları (180°)', 11.2, YESIL_K)
    ic += yazi(300, 58, 'ABC eşkenar üçgen (her iç açısı 60°)', 10.4, LAC, 'start', ince=True)
    ic += yazi(300, 76, 'CDE ikizkenar dik üçgen ve s(DCE) = 90°', 10.4, LAC, 'start', ince=True)
    ic += yazi(300, 94, 'Aradaki s(ACE) açısının ölçüsü = ?', 10.4, KIR, 'start')
    return svg(600, 120, ic, 'B-C-D doğrusu üzerinde ABC eşkenar üçgeni ve CDE dik üçgeni arasında kalan ACE açısı.', 23)


def bora_iddia_karti_svg():
    ic = f'<rect x="8" y="8" width="584" height="88" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(300, 28, 'Bora’nın İkizkenar Üçgen İddia Kartı', 11.5, KIR)
    ic += f'<line x1="36" y1="36" x2="564" y2="36" stroke="{KIR}" stroke-width="1.1"/>'
    ic += yazi(300, 58, '“Bir ikizkenar üçgende eşit kenarların karşısındaki eş taban açılarından', 10.8, LAC, ince=True)
    ic += yazi(300, 78, 'her birinin ölçüsü 95° (geniş açı) olabilir.”', 11, KIR)
    return svg(600, 104, ic, 'Bora’nın ikizkenar üçgenin eş taban açılarının 95 derece olabileceği yönündeki hatalı iddia kartı.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = es_cember_eskenar_svg()
    s[4]['gorsel'] = pergel_insa_kartlari_svg()
    s[5]['gorsel'] = dort_ucgen_aci_modelleri_svg()
    s[6]['gorsel'] = ikizkenar_tepe_acisi_svg()
    s[7]['gorsel'] = eskenar_insa_adimlari_svg()
    s[8]['gorsel'] = siniflandirma_tablosu_svg()
    s[9]['gorsel'] = farkli_cember_cesitkenar_svg()
    s[10]['gorsel'] = dogrusal_iki_ucgen_svg()
    s[12]['gorsel'] = bora_iddia_karti_svg()
