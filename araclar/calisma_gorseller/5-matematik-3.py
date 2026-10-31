"""5. sınıf Matematik 3. hafta (Açı Ölçme: Derece ve Açıölçer — tam/doğru/dik/dar/geniş açı, açıölçerle ölçme ve çizme, eş açılar) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""
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


def nk(cx, cy, r, aci):
    a = math.radians(aci)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def yay(cx, cy, r, a1, a2, renk, dolgu=None, kal=2):
    x1, y1 = nk(cx, cy, r, a1)
    x2, y2 = nk(cx, cy, r, a2)
    buyuk = 1 if (a2 - a1) % 360 > 180 else 0
    s = ''
    if dolgu:
        s += f'<path d="M{cx:.1f} {cy:.1f} L{x1:.1f} {y1:.1f} A{r} {r} 0 {buyuk} 0 {x2:.1f} {y2:.1f} Z" fill="{dolgu}"/>'
    return s + f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {buyuk} 0 {x2:.1f} {y2:.1f}" fill="none" stroke="{renk}" stroke-width="{kal}"/>'


def aciolcer_okuma_svg():
    cx, cy, r = 200, 102, 86
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy} Z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.8"/>'
    for d in [0, 30, 60, 90, 115, 150, 180]:
        x1, y1 = nk(cx, cy, r, d)
        x2, y2 = nk(cx, cy, r - 8, d)
        ic += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{MAVI}" stroke-width="1.4"/>'
        tx, ty = nk(cx, cy, r - 20, d)
        ic += yazi(tx, ty + 4, f'{d}°', 10, KIR if d == 115 else LAC)
    # Açı kolları: KM (0°) ve KL (115°)
    ic += yay(cx, cy, 32, 0, 115, TUR, '#ee7d1233', 2)
    lx, ly = nk(cx, cy, 94, 115)
    mx, my = nk(cx, cy, 96, 0)
    ic += f'<line x1="{cx}" y1="{cy}" x2="{mx:.1f}" y2="{my:.1f}" stroke="{TUR}" stroke-width="2.6"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{TUR}" stroke-width="2.6"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.8" fill="{LAC}"/>'
    ic += yazi(cx, cy + 14, 'K (merkez)', 10.8, LAC)
    ic += yazi(mx + 12, my + 4, 'M', 11.5, TUR)
    ic += yazi(lx - 10, ly - 2, 'L', 11.5, TUR)
    # Sağ açıklama kutusu
    ic += f'<rect x="334" y="18" width="244" height="88" rx="8" fill="#fff" stroke="{TUR}" stroke-width="1.5"/>'
    ic += yazi(456, 38, 'Açıölçer Okuma Bilgisi', 11.5, TUR)
    ic += yazi(348, 58, 'Köşe K noktası merkezdedir.', 10.8, LAC, 'start', ince=True)
    ic += yazi(348, 76, 'KM ışını 0° çizgisi üzerindedir.', 10.8, LAC, 'start', ince=True)
    ic += yazi(348, 94, 'KL ışını 115° çizgisinden geçer.', 10.8, LAC, 'start', ince=True)
    return svg(600, 126, ic, 'Açıölçer üzerinde K köşesi merkezde, KM kolu 0 derecede, KL kolu 115 derecede olan LKM açısı.', 24)


def dort_aci_kartlari():
    kartlar = [
        ('1. Kart: A Açısı', 65, 38, 0, '65° (Kısa kol)', MAVI, MAVI_A),
        ('2. Kart: B Açısı', 125, 48, 0, '125° (Uzun kol)', TUR, TUR_A),
        ('3. Kart: C Açısı', 65, 52, 115, '65° (Uzun kol)', YES, YES_A),
        ('4. Kart: D Açısı', 90, 44, 0, '90° (Dik açı)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, olcu, boy, bas_aci, etiket, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="6" width="136" height="106" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 22, bas, 11, renk)
        cx, cy = x + 64, 78
        ic += yay(cx, cy, 18, bas_aci, bas_aci + olcu, renk, '#ffffffaa', 1.8)
        x1, y1 = nk(cx, cy, boy, bas_aci)
        x2, y2 = nk(cx, cy, boy, bas_aci + olcu)
        ic += f'<line x1="{cx}" y1="{cy}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{renk}" stroke-width="2.4"/>'
        ic += f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="2.4"/>'
        ic += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{LAC}"/>'
        ic += yazi(x + 68, 102, etiket, 10.5, LAC)
    return svg(600, 118, ic, 'Dört açı kartı: 1. Kart A=65 derece kısa kollu, 2. Kart B=125 derece, 3. Kart C=65 derece uzun kollu, 4. Kart D=90 derece.', 23)


def donme_modelleri_svg():
    modeller = [
        ('1. Model', 'Çeyrek tur', 90, YES, YES_A),
        ('2. Model', 'Yarım tur', 180, TUR, TUR_A),
        ('3. Model', 'Tam tur', 360, MAVI, MAVI_A),
        ('4. Model', '55° dönüş', 55, MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, aci, renk, arka) in enumerate(modeller):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="6" width="136" height="102" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 22, bas, 11.2, renk)
        cx, cy = x + 68, 66
        if aci == 360:
            ic += f'<circle cx="{cx}" cy="{cy}" r="20" fill="#ffffffaa" stroke="{renk}" stroke-width="1.8"/>'
            ic += f'<line x1="{cx}" y1="{cy}" x2="{cx + 32}" y2="{cy}" stroke="{renk}" stroke-width="2.4"/>'
        else:
            ic += yay(cx, cy, 20, 0, aci, renk, '#ffffffaa', 1.8)
            x1, y1 = nk(cx, cy, 32, 0)
            x2, y2 = nk(cx, cy, 32, aci)
            ic += f'<line x1="{cx}" y1="{cy}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{renk}" stroke-width="2.4"/>'
            ic += f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{renk}" stroke-width="2.4"/>'
        ic += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{LAC}"/>'
        ic += yazi(x + 68, 100, alt, 10.5, LAC)
    return svg(600, 114, ic, 'Dört dönme modeli: 1. çeyrek tur, 2. yarım tur, 3. tam tur, 4. 55 derece dönüş.', 23)


def hatali_olcum_svg():
    cx, cy, r = 175, 92, 74
    ic = f'<rect x="6" y="6" width="588" height="108" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.5"/>'
    ic += f'<path d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy} Z" fill="#fff" stroke="{MAVI}" stroke-width="1.8"/>'
    ic += yazi(cx + r - 16, cy - 6, '0°', 10.5, MAVI)
    ic += yazi(cx, cy - r + 14, '90°', 10.5, MAVI)
    ic += yazi(cx - r + 18, cy - 6, '180°', 10.5, MAVI)
    # DEF açısı: EF kolu 25°'de, ED kolu 95°'de (0° çizgisinde değil!)
    ic += yay(cx, cy, 28, 25, 95, KIR, '#d63a3a22', 2)
    fx, fy = nk(cx, cy, 82, 25)
    dx, dy = nk(cx, cy, 82, 95)
    ic += f'<line x1="{cx}" y1="{cy}" x2="{fx:.1f}" y2="{fy:.1f}" stroke="{KIR}" stroke-width="2.5"/>'
    ic += f'<line x1="{cx}" y1="{cy}" x2="{dx:.1f}" y2="{dy:.1f}" stroke="{KIR}" stroke-width="2.5"/>'
    ic += f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{LAC}"/>'
    ic += yazi(cx, cy + 14, 'E (merkez)', 10.5, LAC)
    ic += yazi(fx + 10, fy + 4, 'F (25°)', 10.5, KIR)
    ic += yazi(dx - 18, dy + 6, 'D (95°)', 10.5, KIR)
    # Sağ uyarı kartı
    ic += f'<rect x="296" y="18" width="282" height="84" rx="8" fill="#fff" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(437, 38, 'Tuna’nın Açıölçer Yerleşimi', 11.5, KIR)
    ic += yazi(312, 58, 'E köşesi merkeze yerleştirilmiş.', 10.8, LAC, 'start', ince=True)
    ic += yazi(312, 76, 'EF kolu 25° çizgisinde, ED kolu 95° çizgisinde.', 10.8, LAC, 'start', ince=True)
    ic += yazi(312, 94, 'Tuna açıyı doğrudan 95° olarak yazmıştır.', 10.8, KIR, 'start')
    return svg(600, 120, ic, 'Tuna’nın hatalı açıölçer yerleşimi: E köşesi merkezde ancak EF kolu 0 derece yerine 25 derece çizgisinde.', 23)


def aci_cizim_adimlari_svg():
    adimlar = [
        ('Işın ve Köşe Çizimi', 'LM ışını ve L köşesi', MAVI, MAVI_A),
        ('Merkez ve 0° Ayarı', 'L merkeze, LM 0°’ye', MOR, MOR_A),
        ('75° Noktası İşareti', '75° hizasına K noktası', TUR, TUR_A),
        ('İkinci Işının Çizimi', 'LK ışını → 75° açı', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="82" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11, renk)
        ic += yazi(x + 68, 62, alt, 10.5, LAC, ince=True)
    return svg(600, 98, ic, '75 derecelik açı çizim aşamaları: ışın çizimi, açıölçer yerleştirme, 75 dereceyi işaretleme ve ikinci ışını çizme.', 22)


def kagit_dilim_deneyi():
    ic = f'<rect x="8" y="6" width="282" height="104" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'Mert’in Birimi (8 Eş Dilim)', 11.5, MAVI)
    cx1, cy1 = 68, 66
    ic += f'<circle cx="{cx1}" cy="{cy1}" r="28" fill="#fff" stroke="{MAVI}" stroke-width="1.6"/>'
    for k in range(4):
        x1, y1 = nk(cx1, cy1, 28, k * 45)
        x2, y2 = nk(cx1, cy1, 28, k * 45 + 180)
        ic += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{MAVI}" stroke-width="1.1"/>'
    ic += yazi(190, 56, 'Büyük dilim birimi', 10.8, LAC, ince=True)
    ic += yazi(190, 76, 'Pergel açıklığı: 2 birim', 11, MAVI)

    ic += f'<rect x="310" y="6" width="282" height="104" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Zeynep’in Birimi (12 Eş Dilim)', 11.5, TUR)
    cx2, cy2 = 370, 66
    ic += f'<circle cx="{cx2}" cy="{cy2}" r="28" fill="#fff" stroke="{TUR}" stroke-width="1.6"/>'
    for k in range(6):
        x1, y1 = nk(cx2, cy2, 28, k * 30)
        x2, y2 = nk(cx2, cy2, 28, k * 30 + 180)
        ic += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{TUR}" stroke-width="1.1"/>'
    ic += yazi(492, 56, 'Küçük dilim birimi', 10.8, LAC, ince=True)
    ic += yazi(492, 76, 'Pergel açıklığı: 3 birim', 11, TUR)
    return svg(600, 116, ic, 'Mert 8 eş dilimli, Zeynep 12 eş dilimli daire kâğıdıyla aynı pergel açıklığını farklı birim sayılarıyla ölçer.', 23)


def aci_sirala_panosu():
    veriler = [
        ('K Açısı', '145°', TUR, TUR_A),
        ('L Açısı', '90°', YES, YES_A),
        ('M Açısı', '180°', MOR, MOR_A),
        ('N Açısı', '360°', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (ad, olcu, renk, arka) in enumerate(veriler):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="82" rx="10" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 68, 34, ad, 11.5, renk)
        ic += f'<line x1="{x + 20}" y1="44" x2="{x + 116}" y2="44" stroke="{renk}" stroke-width="1.2"/>'
        ic += yazi(x + 68, 72, olcu, 12.5, LAC)
    return svg(600, 98, ic, 'Dört açı kartı: K=145 derece, L=90 derece, M=180 derece, N=360 derece.', 22)


def pergel_kol_uzatma():
    ic = f'<rect x="8" y="6" width="276" height="102" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(146, 24, '1. Adım: Kolları 5 cm Olan Açı', 11.2, MAVI)
    cx1, cy1 = 76, 86
    ic += yay(cx1, cy1, 22, 0, 50, MAVI, '#ffffffaa', 1.8)
    x1, y1 = nk(cx1, cy1, 46, 50)
    ic += f'<line x1="{cx1}" y1="{cy1}" x2="{cx1 + 46}" y2="{cy1}" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += f'<line x1="{cx1}" y1="{cy1}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{MAVI}" stroke-width="2.5"/>'
    ic += yazi(200, 62, 'm(ABC) = 50°', 11.5, LAC)
    ic += yazi(200, 82, '(Kol uzunluğu: 5 cm)', 10.5, LAC, ince=True)

    ic += f'<rect x="304" y="6" width="288" height="102" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(448, 24, '2. Adım: Kolları 10 cm’ye Uzatılan Açı', 11.2, YESIL_K)
    cx2, cy2 = 348, 92
    ic += yay(cx2, cy2, 22, 0, 50, YES, '#ffffffaa', 1.8)
    x2, y2 = nk(cx2, cy2, 74, 50)
    ic += f'<line x1="{cx2}" y1="{cy2}" x2="{cx2 + 74}" y2="{cy2}" stroke="{YES}" stroke-width="2.5"/>'
    ic += f'<line x1="{cx2}" y1="{cy2}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{YES}" stroke-width="2.5"/>'
    ic += yazi(508, 62, 'm(ABC) = ?', 11.5, YESIL_K)
    ic += yazi(508, 82, '(Kol uzunluğu: 10 cm)', 10.5, LAC, ince=True)
    return svg(600, 114, ic, '1. adımda kolları 5 cm olan 50 derecelik ABC açısı, 2. adımda kolları 10 cm’ye uzatılan ABC açısı.', 23)


def tahmin_kontrol_karti():
    ic = f'<rect x="8" y="6" width="282" height="100" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 24, 'İstenen Açı: 140° (Tahmin: Geniş Açı)', 11.2, YESIL_K)
    cx1, cy1 = 150, 86
    ic += yay(cx1, cy1, 20, 0, 140, YES, '#ffffffaa', 1.8)
    x1, y1 = nk(cx1, cy1, 48, 140)
    ic += f'<line x1="{cx1}" y1="{cy1}" x2="{cx1 + 48}" y2="{cy1}" stroke="{YES}" stroke-width="2.4"/>'
    ic += f'<line x1="{cx1}" y1="{cy1}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{YES}" stroke-width="2.4"/>'

    ic += f'<rect x="310" y="6" width="282" height="100" rx="10" fill="#fdeaea" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(451, 24, 'Arda’nın Çizdiği: 40° (Dar Açı)', 11.2, KIR)
    cx2, cy2 = 420, 86
    ic += yay(cx2, cy2, 20, 0, 40, KIR, '#ffffffaa', 1.8)
    x2, y2 = nk(cx2, cy2, 48, 40)
    ic += f'<line x1="{cx2}" y1="{cy2}" x2="{cx2 + 48}" y2="{cy2}" stroke="{KIR}" stroke-width="2.4"/>'
    ic += f'<line x1="{cx2}" y1="{cy2}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{KIR}" stroke-width="2.4"/>'
    return svg(600, 112, ic, 'İstenen 140 derecelik geniş açı ile Arda’nın yanlışlıkla çizdiği 40 derecelik dar açı karşılaştırması.', 22)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = aciolcer_okuma_svg()
    s[4]['gorsel'] = dort_aci_kartlari()
    s[5]['gorsel'] = donme_modelleri_svg()
    s[6]['gorsel'] = hatali_olcum_svg()
    s[7]['gorsel'] = aci_cizim_adimlari_svg()
    s[8]['gorsel'] = kagit_dilim_deneyi()
    s[9]['gorsel'] = aci_sirala_panosu()
    s[10]['gorsel'] = pergel_kol_uzatma()
    s[12]['gorsel'] = tahmin_kontrol_karti()
