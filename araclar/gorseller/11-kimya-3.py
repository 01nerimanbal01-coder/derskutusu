# -*- coding: utf-8 -*-
import html as _html


def svg_basla(w, h):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{w}px;display:block;margin:12px auto;font-family:system-ui,-apple-system,sans-serif;">'


def svg_bitir():
    return '</svg>'


def Arka(w, h, renk="#f8fafc"):
    return f'<rect width="{w}" height="{h}" rx="14" fill="{renk}" stroke="#cbd5e1" stroke-width="1.5"/>'


def Baslik(w, metin, renk="#1e3a8a"):
    return (f'<rect x="16" y="10" width="{w-32}" height="28" rx="7" fill="{renk}"/>'
            f'<text x="{w//2}" y="29" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">{_html.escape(str(metin))}</text>')


def Kutu(x, y, w, h, dolgu="#ffffff", kenar="#94a3b8", kw=1.5, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'


def Yazi(x, y, metin, punto=10, renk="#1e293b", hiza="middle", kalin=False):
    fw = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{punto}" fill="{renk}"{fw}>{_html.escape(str(metin))}</text>'


def Cizgi(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'


def Ok(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'


def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "YANMA TEPKİMELERİ VE EKZOTERMİK ENERJİ DÖNÜŞÜMÜ", "#b91c1c")

    # Sol: Yanma Üçgeni / Koşulları
    s += Kutu(24, 48, 304, 196, "#fef2f2", "#dc2626", 2, 10)
    s += Yazi(176, 70, "Yanma Tepkimesinin 3 Temel Koşulu", 10.5, "#991b1b", "middle", True)
    kosullar = [
        ("1. YANICI MADDE (Yakıt)", "C ve H içeren organik bileşikler, H₂, CO, kömür", "#dc2626", "#fee2e2"),
        ("2. YAKICI MADDE (Oksijen Gazı — O₂)", "Havadaki oksijen gazı (elektron alan yükseltgen)", "#0284c7", "#e0f2fe"),
        ("3. TUTUŞMA SICAKLIĞI (Aktivasyon)", "Tepkimenin başlaması için gereken minimum sıcaklık", "#d97706", "#fef3c7")
    ]
    for i, (bas, acik, r, ar) in enumerate(kosullar):
        y = 84 + i * 50
        s += Kutu(40, y, 272, 42, ar, r, 1.5, 6)
        s += Yazi(176, y + 16, bas, 9.2, r, "middle", True)
        s += Yazi(176, y + 33, acik, 8.5, "#1e293b", "middle", False)

    # Sağ: Ekzotermik vs Endotermik Yanma
    s += Kutu(348, 48, 308, 196, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(502, 70, "Yanma Tepkimelerinde Enerji Değişimi", 10.5, "#047857", "middle", True)

    s += Kutu(364, 84, 276, 78, "#ffffff", "#059669", 1.5, 8)
    s += Yazi(502, 104, "Genel Kural: EKZOTERMİK (ΔH < 0)", 9.8, "#047857", "middle", True)
    s += Yazi(502, 124, "CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(s) + 890 kJ", 9.2, "#1e293b", "middle", True)
    s += Yazi(502, 144, "Oluşan bağlar kırılan bağlardan daha sağlamdır.", 8.8, "#475569", "middle", False)

    s += Kutu(364, 172, 276, 58, "#fffbeb", "#d97706", 1.5, 8)
    s += Yazi(502, 192, "Tek İstisna: AZOT GAZININ YANMASI (ΔH > 0)", 9.5, "#b45309", "middle", True)
    s += Yazi(502, 212, "N₂(g) + O₂(g) + Isı → 2NO(g)  (Endotermik — Yakıt olamaz!)", 8.8, "#1e293b", "middle", True)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "MOLEKÜL YAPISI İLE YANMA ISISI (ENERJİ POTANSİYELİ) İLİŞKİSİ", "#1e3a8a")

    s += Kutu(24, 48, 312, 192, "#eff6ff", "#2563eb", 1.8, 10)
    s += Yazi(180, 68, "Hidrokarbonlarda C ve H Sayısının Etkisi", 10, "#1d4ed8", "middle", True)
    barlar = [
        ("Metan (CH₄)", 890, 90, "#60a5fa"),
        ("Etan (C₂H₆)", 1560, 145, "#3b82f6"),
        ("Propan (C₃H₈)", 2220, 200, "#2563eb"),
        ("Bütan (C₄H₁₀)", 2878, 250, "#1d4ed8")
    ]
    for i, (ad, deger, bw, r) in enumerate(barlar):
        y = 84 + i * 32
        s += Yazi(36, y + 15, ad, 9, "#1e293b", "start", True)
        s += Kutu(120, y + 2, bw * 0.65, 20, r, r, 1, 4)
        s += Yazi(126 + bw * 0.65, y + 16, f"{deger} kJ/mol", 8.8, "#1e3a8a", "start", True)
    s += Yazi(180, 226, "Hipotez 1: 1 mol hidrokarbonda C ve H sayısı arttıkça mol yanma ısısı artar.", 8.4, "#1e40af", "middle", True)

    s += Kutu(352, 48, 304, 192, "#f0fdf4", "#16a34a", 1.8, 10)
    s += Yazi(504, 68, "Kütlesel Isıl Değer (kJ/g) ve H/C Oranı", 10, "#15803d", "middle", True)
    maddeler = [
        "• Hidrojenin 1 gramı yandığında ~142 kJ, karbonun",
        "  1 gramı yandığında ise ~32,8 kJ enerji açığa çıkar.",
        "• Bu nedenle bileşikteki H / C oranı büyüdükçe",
        "  1 gram yakıtın verdiği enerji (kütlesel ısıl değer) ARTAR!",
        "• Sıralama (kJ/g): H₂ (142) > CH₄ (55,6) > C₂H₆ (52)",
        "  > C₃H₈ (50,4) > Benzin (47) > Taş Kömürü (30)",
        "• En yüksek kütlesel enerji potansiyeli H₂ gazındadır."
    ]
    for i, m in enumerate(maddeler):
        s += Yazi(366, 92 + i * 20, m, 8.9, "#1e293b", "start", i in (3, 4, 6))

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BAĞ ENERJİLERİ VE BİLEŞİĞİN YÜKSELTGENME BASAMAĞI ETKİSİ", "#6d28d9")

    s += Kutu(24, 48, 308, 186, "#faf5ff", "#7c3aed", 1.8, 10)
    s += Yazi(178, 70, "Karbonun Yükseltgenme Basamağı ve Yanma", 10, "#6d28d9", "middle", True)
    basamaklar = [
        ("CH₄ (Karbon: -4)", "En düşük basamak → En yüksek yanma enerjisi", "#059669", "#d1fae5"),
        ("CH₃OH (Karbon: -2)", "Kısmen yükseltgenmiş → Orta düzey enerji", "#0284c7", "#e0f2fe"),
        ("CO (Karbon: +2)", "Tek basamak daha yanabilir → Düşük enerji", "#d97706", "#fef3c7"),
        ("CO₂ (Karbon: +4 — Maks.)", "Maksimum basamak → YANMAZ (Yangın söndürücü!)", "#dc2626", "#fef2f2")
    ]
    for i, (ad, acik, r, ar) in enumerate(basamaklar):
        y = 84 + i * 36
        s += Kutu(38, y, 280, 30, ar, r, 1.3, 6)
        s += Yazi(46, y + 19, ad + " : " + acik, 8.4, "#1e293b", "start", True)

    s += Kutu(348, 48, 308, 186, "#fff7ed", "#ea580c", 1.8, 10)
    s += Yazi(502, 70, "Bağ Enerjilerinden ΔH Hesabı", 10, "#c2410c", "middle", True)
    s += Kutu(364, 84, 276, 42, "#ffedd5", "#ea580c", 1.5, 8)
    s += Yazi(502, 109, "ΔH = Σ E(Kırılan Bağlar) - Σ E(Oluşan Bağlar)", 9.5, "#9a3412", "middle", True)
    b_mad = [
        "• Bağ kırılması ENDOTERMİK (+), bağ oluşumu",
        "  ise EKZOTERMİK (-) bir süreçtir.",
        "• Bir maddenin iyi bir enerji kaynağı olması için:",
        "  Oluşan ürün bağlarının (C=O ve O-H), kırılan",
        "  giren bağlarından (C-H ve O=O) çok daha güçlü",
        "  olması gerekir (Σ E_oluşan > Σ E_kırılan)."
    ]
    for i, m in enumerate(b_mad):
        s += Yazi(364, 144 + i * 15, m, 8.8, "#1e293b", "start", i == 5)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "YAKIT TÜRLERİNİN ENERJİ VE ÇEVRE AÇISINDAN KARŞILAŞTIRMASI", "#0f766e")

    yakitlar = [
        ("1. Fosil Yakıtlar (Kömür, Petrol, Doğal Gaz)", "Yüksek enerji sağlar ancak CO₂ (sera gazı), SO₂ ve NOₓ (asit yağmurları) salar. Doğal gaz (CH₄) en temiz fosil yakıttır.", "#475569", "#f1f5f9"),
        ("2. Biyoyakıtlar (Biyoetanol, Biyodizel, Biyogaz)", "Bitkisel/organik atıklardan üretilen yenilenebilir yakıtlardır; karbon ayak izini azaltır.", "#65a30d", "#f7fee7"),
        ("3. Hidrojen Enerjisi (H₂ — Geleceğin Yakıtı)", "Birim kütle başına en yüksek enerjiyi (142 kJ/g) verir; yandığında yalnızca su buharı (H₂O) oluşur, sıfır emisyonludur.", "#0284c7", "#e0f2fe"),
        ("4. Besinlerin Hücresel Yanması (Glikoz — C₆H₁₂O₆)", "Canlı vücudunda yavaş ve enzimatik yanmayla (solunum) ATP enerjisi üretir (1 g karbonhidrat ≈ 17 kJ, 1 g yağ ≈ 38 kJ).", "#059669", "#ecfdf5")
    ]

    for i, (bas, acik, r, ar) in enumerate(yakitlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 92
        s += Kutu(x, y, 312, 80, ar, r, 1.5, 8)
        s += Yazi(x + 12, y + 20, bas, 9.4, r, "start", True)
        s += Yazi(x + 12, y + 42, acik[:52], 8.6, "#1e293b", "start", False)
        s += Yazi(x + 12, y + 58, acik[52:104], 8.6, "#1e293b", "start", False)
        s += Yazi(x + 12, y + 72, acik[104:], 8.6, "#1e293b", "start", False)

    s += svg_bitir()
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]