"""11. sınıf Fizik 4. hafta (Yatay ve Eğik Atış Problemleri) görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza="middle", ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kok_ciz(cx, y, on_metin, ic_metin, son_metin='', renk=LAC, boy=8.0, ince=False):
    ic_str = str(ic_metin)
    on_str = str(on_metin) if on_metin else ''
    son_str = str(son_metin) if son_metin else ''
    w_ic = max(10, len(ic_str) * (boy * 0.62) + 4)
    w_on = len(on_str) * (boy * 0.56) + (2 if on_str else 0)
    w_son = len(son_str) * (boy * 0.56) + (2 if son_str else 0)
    toplam_w = w_on + 9 + w_ic + w_son
    sol = cx - toplam_w / 2
    out = ''
    if on_str:
        out += yazi(sol + w_on - 1, y, on_str, boy, renk, 'end', ince=ince)
    rx = sol + w_on
    ust_y = y - boy * 0.95
    orta_y = y - boy * 0.38
    alt_y = y + 1.2
    out += (f'<path d="M{rx:.1f} {orta_y:.1f} L{rx + 2.2:.1f} {orta_y - 1.2:.1f} '
            f'L{rx + 5.0:.1f} {alt_y:.1f} L{rx + 8.5:.1f} {ust_y:.1f} '
            f'H{rx + 9 + w_ic:.1f}" fill="none" stroke="{renk}" stroke-width="0.75" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    out += yazi(rx + 9 + w_ic / 2, y, ic_str, boy, renk, 'middle', ince=ince)
    if son_str:
        out += yazi(rx + 9 + w_ic + 1, y, son_str, boy, renk, 'start', ince=ince)
    return out


def kinematik_baginti_kartlari():
    kartlar = [
        ("1. h_max", "V₀y² / 2g Formülü", YES, YES_A),
        ("2. t_uçuş", "2.V₀y / g Süresi", MAVI, MAVI_A),
        ("3. X_menzil", "V₀x . t_uçuş Yolu", TUR, TUR_A),
        ("4. V_bileşke", None, MOR, MOR_A),
    ]
    ic = ""
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, "#ffffff")
        ic += yazi(x + 41, 62, ad, 8.4, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        if oz is None:
            ic += kok_ciz(x + 41, 92, '', 'Vx² + Vy²', '', LAC, 7.8, ince=True)
        else:
            ic += yazi(x + 41, 92, oz, 7.8, LAC, ince=True)
    return svg(360, 125, ic, "Atış hareketleri formül kartları.", 34)


def egik_atis_hmax_modeli():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "EĞİK ATIŞ: V₀ = 50 m/s (53°) KİNEMATİK ÇÖZÜMÜ", 9.8, TUR)
    ic += kutu(20, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(92, 56, "Hız Bileşenleri", 9.2, TUR)
    ic += yazi(92, 76, "V₀x = 50.0,6 = 30 m/s", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "V₀y = 50.0,8 = 40 m/s", 8.4, TUR, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", YES)
    ic += yazi(267, 56, "h_max Hesabı", 9.2, YESIL_K)
    ic += yazi(267, 76, "h = (40)² / (2.10)", 8.6, LAC, ince=True)
    ic += yazi(267, 92, "h_max = 80 metre", 8.8, YES, ince=True)
    return svg(360, 125, ic, "Eğik atış maksimum yükseklik hesabı.", 34)


def yatay_atis_carpan_kesiti():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, "YATAY ATIŞ: h = 80 m, V₀ = 20 m/s ÇARPMA HIZI", 9.8, MAVI)
    ic += kutu(16, 36, 96, 70, "#ffffff", MAVI)
    ic += yazi(64, 56, "Düşme Süresi", 9.0, MAVI)
    ic += yazi(64, 76, "80 = 5.t²", 8.4, LAC, ince=True)
    ic += yazi(64, 92, "t = 4 saniye", 8.4, MAVI, ince=True)
    ic += kutu(132, 36, 96, 70, "#ffffff", TUR)
    ic += yazi(180, 56, "Düşey Hız", 9.0, TUR)
    ic += yazi(180, 76, "Vy = 10.4", 8.4, LAC, ince=True)
    ic += yazi(180, 92, "Vy = 40 m/s", 8.4, TUR, ince=True)
    ic += kutu(248, 36, 96, 70, "#ffffff", YES)
    ic += yazi(296, 56, "Bileşke Hız", 9.0, YESIL_K)
    ic += kok_ciz(296, 76, "V = ", "20² + 40²", "", LAC, 8.0, ince=True)
    ic += kok_ciz(296, 92, "V = 20", "5", " m/s", YES, 8.2, ince=True)
    return svg(360, 125, ic, "Yatay atış bileşke hız hesabı.", 34)


def tumler_aci_menzil_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, "TÜMLER AÇILARDA (θ₁ + θ₂ = 90°) EŞİT MENZİL KURALI", 9.8, YESIL_K)
    adımlar = [
        ("30° Açı", "Düşük tepe, eşit menzil", 16),
        ("45° Açı", "Maksimum yatay menzil", 102),
        ("60° Açı", "Yüksek tepe, eşit menzil", 188),
        ("Kural", "Sin(2θ₁) = Sin(2θ₂)", 274),
    ]
    for b, a, x in adımlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", YESIL_K)
        ic += yazi(x + 35, 54, b, 8.2, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Tümler açılarda menzil eşitliği şeması.", 34)


def atis_karsilastirma_tablosu():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, "ÖZEL AÇILAR VE KİNEMATİK PARAMETRELER TABLOSU", 9.8, MOR)
    satirlar = [
        ("Fırlatma Açısı", "Uçuş Süresi (t)", "Tepe Yüksekliği (h)", "Yatay Menzil (X)", MOR),
        ("30 Derece", "V₀ / g", "V₀² / 8g", ("", "3", " V₀² / 2g"), MAVI),
        ("45 Derece", ("", "2", " V₀ / g"), "V₀² / 4g", "V₀² / g (Maksimum)", YESIL_K),
        ("60 Derece", ("", "3", " V₀ / g"), "3V₀² / 8g", ("", "3", " V₀² / 2g"), TUR),
    ]
    for i, (k1, k2, k3, k4, r) in enumerate(satirlar):
        y = 30 + i * 20
        bg = "#ffffff" if i > 0 else MOR_A
        ic += kutu(16, y, 328, 18, bg, r, r=2)
        ic += yazi(55, y + 13, k1, 8.0, r)
        ic += kok_ciz(130, y + 13, k2[0], k2[1], k2[2], LAC, 7.8, ince=True) if isinstance(k2, tuple) else yazi(130, y + 13, k2, 7.8, LAC, ince=(i > 0))
        ic += yazi(210, y + 13, k3, 7.8, LAC, ince=(i > 0))
        ic += kok_ciz(295, y + 13, k4[0], k4[1], k4[2], LAC, 7.8, ince=True) if isinstance(k4, tuple) else yazi(295, y + 13, k4, 7.8, LAC, ince=(i > 0))
    return svg(360, 125, ic, "Özel açılar kinematik tablosu.", 34)


def surtunmeli_atis_kesiti():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 22, "HAVA SÜRTÜNMESİNİN ATIŞ YÖRÜNGESİNE ETKİSİ", 9.8, CAM)
    ic += kutu(20, 36, 145, 70, "#ffffff", YES)
    ic += yazi(92, 56, "İdeal Sürtünmesiz", 9.2, YESIL_K)
    ic += yazi(92, 76, "Simetrik parabol yörünge", 8.4, LAC, ince=True)
    ic += yazi(92, 92, "Maksimum menzil &amp; yükseklik", 8.2, YES, ince=True)
    ic += kutu(195, 36, 145, 70, "#ffffff", TUR)
    ic += yazi(267, 56, "Gerçek Sürtünmeli", 9.2, TUR)
    ic += yazi(267, 76, "Asimetrik basık yörünge", 8.4, LAC, ince=True)
    ic += yazi(267, 92, "Daha kısa menzil ve süre", 8.2, TUR, ince=True)
    return svg(360, 125, ic, "Sürtünmeli ve ideal yörünge kesiti.", 34)


def atis_adim_kartlari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, "İKİ BOYUTTA PROBLEM ÇÖZME STRATEJİSİ", 10.0, TUR)
    kartlar = [
        ("1. Bileşenler", "V₀x ve V₀y ayrılır", 16),
        ("2. Zaman (t)", "Düşey hareketten bulunur", 102),
        ("3. Yol (X)", "Yatayda X = V₀x.t", 188),
        ("4. Vektör", "Pisagorla çarpma hızı", 274),
    ]
    for b, a, x in kartlar:
        ic += kutu(x, 36, 70, 70, "#ffffff", TUR)
        ic += yazi(x + 35, 54, b, 8.2, TUR)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{TUR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, a, 7.6, LAC, ince=True)
    return svg(360, 125, ic, "Atış problemi çözüm adımları kartı.", 34)


def kinematik_akis_kutulari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 24, "İKİ BOYUTLU HAREKETİN VEKTÖREL SENTEZİ", 10.0, YESIL_K)
    kutular = ["Fırlatma Hızı", "Eksen Ayırımı", "Ortak Süre (t)", "Konum Vektörü"]
    for i, k in enumerate(kutular):
        x = 16 + i * 85
        ic += kutu(x, 42, 75, 52, "#ffffff", YESIL_K, r=4)
        ic += yazi(x + 37, 66, f"Faz {i + 1}", 8.0, TUR)
        ic += yazi(x + 37, 82, k, 8.2, YESIL_K)
    return svg(360, 125, ic, "Kinematik sentez akış kutuları.", 34)


def uygula(o):
    s = o["sorular"]
    s[0]["gorsel"] = kinematik_baginti_kartlari()
    s[0]["en_fazla"] = 34
    s[1]["gorsel"] = egik_atis_hmax_modeli()
    s[1]["en_fazla"] = 34
    s[2]["gorsel"] = yatay_atis_carpan_kesiti()
    s[2]["en_fazla"] = 34
    s[3]["gorsel"] = tumler_aci_menzil_semasi()
    s[3]["en_fazla"] = 34
    s[5]["gorsel"] = atis_karsilastirma_tablosu()
    s[5]["en_fazla"] = 34
    s[6]["gorsel"] = surtunmeli_atis_kesiti()
    s[6]["en_fazla"] = 34
    s[8]["gorsel"] = atis_adim_kartlari()
    s[8]["en_fazla"] = 34
    s[10]["gorsel"] = kinematik_akis_kutulari()
    s[10]["en_fazla"] = 34
