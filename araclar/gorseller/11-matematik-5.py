def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">DIŞBÜKEY VE İÇBÜKEY DÖRTGENLER İLE AÇI ÖZELLİKLERİ</text>'
    ic += _kart(20, 44, 310, 190, "DIŞBÜKEY (KONVEKS) VE İÇBÜKEY DÖRTGEN", [
        "• Dışbükey (Konveks): Her bir iç açısının ölçüsü",
        "  180° den küçük olan ve köşegenlerinin ikisi de",
        "  iç bölgede kesişen dörtgendir.",
        "• İçbükey (Konkav): En az bir iç açısının ölçüsü",
        "  180° den büyük olan dörtgendir.",
        "• İçbükey dörtgende şalvar (bumerang) kuralı:",
        "  Girintili dış açı = α + β + θ toplamına eşittir."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "İÇ VE DIŞ AÇILAR TOPLAMI (360°)", [
        "• Bir köşeden çizilen köşegen dörtgeni 2 üçgene ayırır.",
        "• İç açılar toplamı: (4 - 2) · 180° = 2 · 180° = 360°.",
        "• m(A) + m(B) + m(C) + m(D) = 360°.",
        "• Dış açılar toplamı da tüm çokgenlerde olduğu",
        "  gibi 360° ye eşittir:",
        "  m(A\') + m(B\') + m(C\') + m(D\') = 360°."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">DÖRTGENDE AÇIORTAYLARIN OLUŞTURDUĞU AÇILAR</text>'
    ic += _kart(20, 44, 310, 190, "1. ARDIŞIK İKİ İÇ AÇIORTAYIN AÇISI", [
        "• ABCD dörtgeninde komşu A ve B açılarının",
        "  iç açıortayları E noktasında kesişsin.",
        "• Açıortaylar arasındaki açının ölçüsü, diğer iki",
        "  köşedeki iç açıların aritmetik ortalamasıdır:",
        "• m(AEB) = [ m(C) + m(D) ] / 2",
        "• Örnek: m(C) = 110° ve m(D) = 70° ise",
        "  m(AEB) = (110° + 70°) / 2 = 90° bulunur."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "2. KARŞILIKLI İKİ İÇ AÇIORTAYIN AÇISI", [
        "• ABCD dörtgeninde karşılıklı A ve C açılarının",
        "  iç açıortayları arasındaki dar açının ölçüsü α olsun.",
        "• Bu dar açı, diğer iki karşılıklı açının farkının",
        "  mutlak değerinin yarısına eşittir:",
        "• α = | m(B) - m(D) | / 2",
        "• Örnek: m(B) = 130° ve m(D) = 80° ise",
        "  α = |130° - 80°| / 2 = 25° bulunur."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">DİK KESİŞEN KÖŞEGENLER VE KENAR ORTA NOKTALARI (VARİGNON)</text>'
    ic += _kart(20, 44, 310, 190, "KÖŞEGENLERİ DİK KESİŞEN DÖRTGENLER", [
        "• [AC] ⊥ [BD] olan bir ABCD dörtgeninde karşılıklı",
        "  kenarların uzunluklarının kareleri toplamı eşittir:",
        "• a² + c² = b² + d²",
        "• İspat, dik kesişen köşegenlerin oluşturduğu dört",
        "  dik üçgende Pisagor teoremi uygulanarak yapılır.",
        "• İçbükey dörtgende de köşegen doğrultuları dik",
        "  kesişiyorsa aynı a² + c² = b² + d² bağıntısı geçerlidir."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "ORTA NOKTALAR TEOREMİ (VARİGNON)", [
        "• Herhangi bir dörtgenin kenarlarının orta noktaları",
        "  (K, L, M, N) birleştirildiğinde PARALELKENAR oluşur.",
        "• Çevre(KLMN) = |AC| + |BD| (köşegenler toplamı).",
        "• |AC| = |BD| ise KLMN bir EŞKENAR DÖRTGEN olur.",
        "• [AC] ⊥ [BD] ise KLMN bir DİKDÖRTGEN olur.",
        "• Hem |AC| = |BD| hem [AC] ⊥ [BD] ise KARE olur."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">GENEL DÖRTGENLERDE ALAN BAĞINTILARI</text>'
    ic += _kart(20, 44, 310, 190, "KÖŞEGENLERLE ALAN HESABI", [
        "• Köşegen uzunlukları |AC| = e ve |BD| = f olan",
        "  ve köşegenleri arasındaki açı α olan dörtgenin alanı:",
        "• Alan(ABCD) = (1/2) · |AC| · |BD| · sin(α)",
        "• Köşegenler dik kesişiyorsa (α = 90°, sin90° = 1):",
        "• Alan(ABCD) = (|AC| · |BD|) / 2",
        "• Orta noktalar paralelkenarı: Alan(KLMN) = Alan(ABCD) / 2."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "KÖŞEGENLERİN AYIRDIĞI ÜÇGEN ALANLARI", [
        "• Köşegenlerin kesişmesiyle oluşan 4 üçgenin alanları",
        "  sırasıyla S₁, S₂, S₃ ve S₄ olsun.",
        "• Karşılıklı üçgenlerin alanları çarpımı birbirine eşittir:",
        "• S₁ · S₃ = S₂ · S₄",
        "• Kenar orta noktalarında köşelerde kalan 4 küçük",
        "  üçgen için: A₁ + A₃ = A₂ + A₄ = Alan(ABCD) / 4."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
