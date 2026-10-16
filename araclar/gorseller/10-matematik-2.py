"""10-matematik-2 için 6 eğitici SVG diyagramı."""
from ozet_gorsel import svg

C = {
    "kirmizi": "#b8362a",
    "mavi": "#245785",
    "yesil": "#246c45",
    "sari": "#9e6b12",
    "mor": "#6b3e8e",
    "lacivert": "#1f2e45",
    "turkuaz": "#1c7278",
    "acik_kirmizi": "#faecea",
    "acik_mavi": "#eaf2fa",
    "acik_yesil": "#e8f5ee",
    "acik_sari": "#fdf5e2",
    "acik_mor": "#f3ecf9",
    "acik_turkuaz": "#e6f4f5",
    "gri": "#68645c",
    "cizgi": "#d8d1c3",
}


def kutu(x, y, w, h, dolgu="#fff", kenar="#d8d1c3", r=8, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'


def metin(x, y, icerik, boyut=12, renk="#1a1815", kalin=False, orta=True, italik=False):
    anc = ' text-anchor="middle"' if orta else ""
    fw = ' font-weight="700"' if kalin else ' font-weight="500"'
    fs = ' font-style="italic"' if italik else ""
    return f'<text x="{x}" y="{y}" font-size="{boyut}" fill="{renk}"{anc}{fw}{fs}>{icerik}</text>'


def cizgi(x1, y1, x2, y2, renk="#68645c", kalinlik=1.8, kesik=False):
    da = ' stroke-dasharray="5,4"' if kesik else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalinlik}"{da}/>'


def ok(x1, y1, x2, y2, renk="#b8362a", kalinlik=2):
    import math
    aci = math.atan2(y2 - y1, x2 - x1)
    u = 8
    px1 = x2 - u * math.cos(aci - 0.45)
    py1 = y2 - u * math.sin(aci - 0.45)
    px2 = x2 - u * math.cos(aci + 0.45)
    py2 = y2 - u * math.sin(aci + 0.45)
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalinlik}"/>'
        f'<polygon points="{x2},{y2} {px1:.1f},{py1:.1f} {px2:.1f},{py2:.1f}" fill="{renk}"/>'
    )


def gorsel_1():
    w, h = 680, 230
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["lacivert"], C["lacivert"], r=6))
    ic.append(metin(340, 36, "GENEL ÜÇGENDE DİKME İNDİREREK TRİGONOMETRİK MODELLEME", 13, "#fff", True))

    # Sol: DAB üçgeni çizimi
    ic.append(kutu(18, 58, 330, 158, "#fff", C["cizgi"]))
    # Üçgen köşeleri: A(45, 185), B(315, 185), D(210, 78), H(210, 185)
    ic.append('<polygon points="45,185 315,185 210,78" fill="#eaf2fa" stroke="#245785" stroke-width="2.2"/>')
    ic.append(cizgi(210, 78, 210, 185, C["kirmizi"], 2.2, True))
    # Diklik işareti
    ic.append('<polyline points="210,173 222,173 222,185" fill="none" stroke="#b8362a" stroke-width="1.5"/>')
    ic.append(metin(35, 192, "A", 12, C["lacivert"], True))
    ic.append(metin(326, 192, "B", 12, C["lacivert"], True))
    ic.append(metin(210, 70, "D (Deniz Feneri)", 11, C["kirmizi"], True))
    ic.append(metin(210, 202, "H", 11.5, C["kirmizi"], True))
    ic.append(metin(92, 178, "22°", 11, C["mavi"], True))
    ic.append(metin(280, 178, "31°", 11, C["yesil"], True))
    ic.append(metin(232, 114, "59°", 10, C["yesil"], True))
    ic.append(metin(192, 138, "h = 4k", 11, C["kirmizi"], True))
    ic.append(metin(128, 202, "|AH| = 10k", 10.5, C["mavi"], True))
    ic.append(metin(265, 202, "|BH| = 20k/3", 10.5, C["yesil"], True))

    # Sağ: Adımlar
    ic.append(kutu(362, 58, 300, 158, C["acik_sari"], C["sari"]))
    ic.append(metin(512, 80, "ÇÖZÜM ADIMLARI (ORTAK DİK KENAR)", 11.5, C["sari"], True))
    ic.append(metin(376, 104, "1. [DH] ⊥ [AB] dikmesi indirilerek iki", 10.5, "#1a1815", False, False))
    ic.append(metin(376, 120, "   dik üçgen (DAH ve DBH) oluşturulur.", 10.5, "#1a1815", False, False))
    ic.append(metin(376, 144, "2. tan 22° = h/|AH| = 4/10 ⇒ h = 4k, |AH| = 10k", 10, C["mavi"], True, False))
    ic.append(metin(376, 166, "3. cot 59° = |BH|/h = 6/10 ⇒ |BH| = 20k/3", 10, C["yesil"], True, False))
    ic.append(metin(376, 190, "4. |AB| = |AH| + |BH| toplamından k ve h", 10.5, C["kirmizi"], True, False))
    ic.append(metin(376, 206, "   (fenerin kıyıya uzaklığı) bulunur.", 10.5, "#1a1815", False, False))

    return svg(w, h, "".join(ic), "Genel üçgende dikme indirerek ortak yükseklik üzerinden trigonometrik problem çözümü")


def gorsel_2():
    w, h = 680, 220
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["mor"], C["mor"], r=6))
    ic.append(metin(340, 36, "TRİGONOMETRİK ÖZDEŞLİKLER VE TAM KARE UYGULAMALARI", 13, "#fff", True))

    ic.append(kutu(20, 60, 308, 144, C["acik_mavi"], C["mavi"]))
    ic.append(metin(174, 82, "1. SİNÜS - KOSİNÜS TAM KARE", 11.5, C["mavi"], True))
    ic.append(kutu(34, 92, 280, 28, "#fff", C["mavi"], r=5))
    ic.append(metin(174, 110, "Temel Özdeşlik: sin²x + cos²x = 1", 11, C["mavi"], True))
    ic.append(metin(174, 136, "(sin x + cos x)² = 1 + 2 · sin x · cos x", 10.5, "#1a1815", True))
    ic.append(metin(174, 158, "(sin x − cos x)² = 1 − 2 · sin x · cos x", 10.5, "#1a1815", True))
    ic.append(metin(174, 184, "Uygulama: Tel çerçeve alanı A = sin x · cos x", 10, C["kirmizi"], True))

    ic.append(kutu(352, 60, 308, 144, C["acik_yesil"], C["yesil"]))
    ic.append(metin(506, 82, "2. TANJANT - KOTANJANT TAM KARE", 11.5, C["yesil"], True))
    ic.append(kutu(366, 92, 280, 28, "#fff", C["yesil"], r=5))
    ic.append(metin(506, 110, "Temel Özdeşlik: tan x · cot x = 1", 11, C["yesil"], True))
    ic.append(metin(506, 136, "(tan x + cot x)² = tan²x + cot²x + 2", 10.5, "#1a1815", True))
    ic.append(metin(506, 158, "(tan x − cot x)² = tan²x + cot²x − 2", 10.5, "#1a1815", True))
    ic.append(metin(506, 184, "Uygulama: tan²x + cot²x = 14 ⇒ Alan = 14 + 2 = 16", 10, C["yesil"], True))

    return svg(w, h, "".join(ic), "Trigonometrik özdeşliklerin tam kare ifadelerle kullanımı")


def gorsel_3():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["yesil"], C["yesil"], r=6))
    ic.append(metin(340, 36, "HİPOTENÜSÜ 1 BİRİM OLAN DİK ÜÇGEN VE YOL EĞİM YÜZDESİ", 12.5, "#fff", True))

    # Sol: Hipotenüsü 1 birim olan dik üçgen
    ic.append(kutu(20, 60, 308, 150, "#fff", C["mavi"]))
    ic.append(metin(174, 80, "HİPOTENÜSÜ 1 BİRİM OLAN DİK ÜÇGEN", 11, C["mavi"], True))
    ic.append('<polygon points="50,182 230,182 230,96" fill="#eaf2fa" stroke="#245785" stroke-width="2.2"/>')
    ic.append('<polyline points="218,182 218,170 230,170" fill="none" stroke="#245785" stroke-width="1.5"/>')
    ic.append(metin(82, 176, "x", 12, C["kirmizi"], True))
    ic.append(metin(132, 128, "Hipotenüs = 1", 11, C["lacivert"], True))
    ic.append(metin(140, 198, "Komşu = cos x", 11, C["mavi"], True))
    ic.append(metin(272, 144, "Karşı = sin x", 11, C["kirmizi"], True))

    # Sağ: Eğim yüzdesi
    ic.append(kutu(352, 60, 308, 150, C["acik_sari"], C["sari"]))
    ic.append(metin(506, 80, "ORANLAR VE YOL EĞİM YÜZDESİ (%)", 11, C["sari"], True))
    ic.append(kutu(368, 92, 276, 32, "#fff", C["sari"], r=5))
    ic.append(metin(506, 112, "tan x = sin x / cos x  •  cot x = cos x / sin x", 10.5, C["lacivert"], True))
    ic.append(metin(506, 142, "Eğim = Yükseklik Farkı / Yatay Uzaklık = tan α", 10.5, "#1a1815", True))
    ic.append(kutu(368, 156, 276, 40, "#fff", C["kirmizi"], r=5))
    ic.append(metin(506, 174, "Eğim Yüzdesi (%) = tan α · 100", 11, C["kirmizi"], True))
    ic.append(metin(506, 190, "Örn: α = 17° için tan 17° ≈ 0,30 ⇒ Eğim ≈ %30", 9.5, "#1a1815"))

    return svg(w, h, "".join(ic), "Hipotenüsü 1 birim olan dik üçgende dik kenarlar ve yol eğim yüzdesi hesabı")


def gorsel_4():
    w, h = 680, 240
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["mavi"], C["mavi"], r=6))
    ic.append(metin(340, 36, "BİRİM ÇEMBER VE NOKTALARIN TRİGONOMETRİK KOORDİNATLARI", 12.5, "#fff", True))

    # Sol: Birim çember çizimi
    ic.append(kutu(18, 58, 290, 168, "#fff", C["cizgi"]))
    cx, cy, r = 155, 144, 64
    ic.append(cizgi(65, cy, 248, cy, C["gri"], 1.5))
    ic.append(cizgi(cx, 66, cx, 220, C["gri"], 1.5))
    ic.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["mavi"]}" stroke-width="2.2"/>')
    # P noktası (yaklaşık 40 derece)
    px, py = cx + 49, cy - 41
    ic.append('<polygon points="155,144 204,144 204,103" fill="#eaf2fa" stroke="#b8362a" stroke-width="1.8"/>')
    ic.append(f'<circle cx="{px}" cy="{py}" r="4" fill="{C["kirmizi"]}"/>')
    ic.append(metin(px + 38, py - 4, "P(cos α, sin α)", 10.5, C["kirmizi"], True))
    ic.append(metin(176, 139, "α", 11, C["lacivert"], True))
    ic.append(metin(180, 157, "cos α", 9.5, C["mavi"], True))
    ic.append(metin(222, 126, "sin α", 9.5, C["kirmizi"], True))
    ic.append(metin(232, 156, "1", 10, C["gri"], True))
    ic.append(metin(80, 156, "−1", 10, C["gri"], True))
    ic.append(metin(145, 76, "1", 10, C["gri"], True))

    # Sağ: Özel açıların birim çember koordinatları
    ic.append(kutu(322, 58, 340, 168, C["acik_mavi"], C["mavi"]))
    ic.append(metin(492, 80, "1. BÖLGEDE ÖZEL AÇILAR: P(cos α, sin α)", 11.5, C["mavi"], True))
    satirlar = [
        (94, "α = 30°", "B( √3/2 , 1/2 )", "cos 30° = √3/2 • sin 30° = 1/2"),
        (134, "α = 45°", "L( √2/2 , √2/2 )", "cos 45° = √2/2 • sin 45° = √2/2"),
        (174, "α = 60°", "N( 1/2 , √3/2 )", "cos 60° = 1/2  • sin 60° = √3/2"),
    ]
    for y, aci, nokta, deger in satirlar:
        ic.append(kutu(336, y, 312, 32, "#fff", C["mavi"], r=5))
        ic.append(metin(375, y + 20, aci, 10.5, C["kirmizi"], True))
        ic.append(metin(455, y + 20, nokta, 10.5, C["lacivert"], True))
        ic.append(metin(576, y + 20, deger, 9.5, C["mavi"], True))

    return svg(w, h, "".join(ic), "Birim çember üzerinde P(cos α, sin α) noktası ve 30°, 45°, 60° koordinatları")


def gorsel_5():
    w, h = 680, 235
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["kirmizi"], C["kirmizi"], r=6))
    ic.append(metin(340, 36, "BİRİM ÇEMBERDE GENİŞ AÇILAR (90° < α < 180°) VE MEKANİK İŞ", 12.5, "#fff", True))

    # Sol: 2. bölgede geniş açı (120°)
    ic.append(kutu(18, 58, 300, 162, "#fff", C["cizgi"]))
    cx, cy, r = 175, 152, 62
    ic.append(cizgi(85, cy, 255, cy, C["gri"], 1.5))
    ic.append(cizgi(cx, 74, cx, 212, C["gri"], 1.5))
    ic.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C["mavi"]}" stroke-width="2"/>')
    # 120° noktası: x = cx - 31, y = cy - 54
    px, py = cx - 31, cy - 54
    ic.append(f'<polygon points="{cx},{cy} {px},{cy} {px},{py}" fill="#faecea" stroke="#b8362a" stroke-width="1.8"/>')
    ic.append(f'<circle cx="{px}" cy="{py}" r="4" fill="{C["kirmizi"]}"/>')
    ic.append(metin(px - 22, py - 8, "B(−1/2, √3/2)", 10, C["kirmizi"], True))
    ic.append(metin(cx - 18, cy - 6, "60°", 9.5, C["kirmizi"], True))
    ic.append(metin(cx + 22, cy - 14, "120°", 10.5, C["mavi"], True))
    ic.append(metin(168, 206, "2. Bölge: cos α < 0 (Negatif), sin α > 0 (Pozitif)", 10, C["lacivert"], True))

    # Sağ: Geniş açı tablosu ve İş formülü
    ic.append(kutu(332, 58, 330, 162, C["acik_kirmizi"], C["kirmizi"]))
    ic.append(metin(497, 78, "GENİŞ AÇI ÖZDEŞLİKLERİ (BÜTÜNLER AÇI)", 11, C["kirmizi"], True))
    ic.append(metin(497, 98, "cos(180° − θ) = −cos θ   •   sin(180° − θ) = +sin θ", 10.5, C["lacivert"], True))
    ic.append(kutu(346, 108, 302, 54, "#fff", C["kirmizi"], r=5))
    ic.append(metin(497, 125, "• 120°: cos 120° = −1/2   |   sin 120° = √3/2", 10, "#1a1815", True))
    ic.append(metin(497, 141, "• 135°: cos 135° = −√2/2  |   sin 135° = √2/2", 10, "#1a1815", True))
    ic.append(metin(497, 156, "• 150°: cos 150° = −√3/2  |   sin 150° = 1/2", 10, "#1a1815", True))
    ic.append(kutu(346, 168, 302, 42, C["acik_sari"], C["sari"], r=5))
    ic.append(metin(497, 184, "Fizikte İş: W = F · d · cos θ", 10.5, C["sari"], True))
    ic.append(metin(497, 200, "θ geniş açı ise cos θ < 0 ⇒ W < 0 (Enerji çekilir)", 9.5, "#1a1815", True))

    return svg(w, h, "".join(ic), "Birim çemberin ikinci bölgesinde geniş açıların sinüs ve kosinüs değerleri")


def gorsel_6():
    w, h = 680, 215
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["turkuaz"], C["turkuaz"], r=6))
    ic.append(metin(340, 36, "YÖNLÜ AÇILAR: POZİTİF (+) VE NEGATİF (−) DÖNÜŞ YÖNLERİ", 13, "#fff", True))

    ic.append(kutu(20, 60, 305, 138, C["acik_yesil"], C["yesil"]))
    ic.append(metin(172, 84, "POZİTİF YÖNLÜ AÇI (+)", 12, C["yesil"], True))
    ic.append(metin(172, 108, "Saat Yönünün Tersine Dönüş", 11, "#1a1815", True))
    ic.append(metin(172, 132, "Başlangıç kolu (+x ekseni) sabitken", 10, "#1a1815"))
    ic.append(metin(172, 150, "saat yönünün tersine dönen ışının açısıdır.", 10, "#1a1815"))
    ic.append(kutu(42, 162, 260, 26, "#fff", C["yesil"], r=5))
    ic.append(metin(172, 179, "Örnek: +20°, +70°, +140°", 10.5, C["yesil"], True))

    ic.append(kutu(355, 60, 305, 138, C["acik_kirmizi"], C["kirmizi"]))
    ic.append(metin(507, 84, "NEGATİF YÖNLÜ AÇI (−)", 12, C["kirmizi"], True))
    ic.append(metin(507, 108, "Saat Yönünde Dönüş", 11, "#1a1815", True))
    ic.append(metin(507, 132, "Başlangıç kolu (+x ekseni) sabitken", 10, "#1a1815"))
    ic.append(metin(507, 150, "saat yönünde dönen ışının açısıdır.", 10, "#1a1815"))
    ic.append(kutu(377, 162, 260, 26, "#fff", C["kirmizi"], r=5))
    ic.append(metin(507, 179, "Örnek: −40°, −50°, −120°, −150°", 10.5, C["kirmizi"], True))

    return svg(w, h, "".join(ic), "Birim çemberde pozitif ve negatif yönlü açıların tanımı ve örnekleri")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
