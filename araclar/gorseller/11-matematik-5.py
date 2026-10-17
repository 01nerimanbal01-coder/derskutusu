# -*- coding: utf-8 -*-
"""11. Sınıf Matematik — 5. Hafta Görselleri
Konu: Yönlü Açılar, Açı Ölçü Birimleri (Derece-Radyan), Esas Ölçü ve Birim Çember
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#2563eb", arka="#eff6ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Yönlü Açılar: Pozitif Yön (Saat Yönünün Tersi) ve Negatif Yön (Saat Yönü)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Yönlü Açılar: Başlangıç Kenarı, Bitim Kenarı ve Açı Yönleri", "#2563eb", "#eff6ff")

    # Sol: Pozitif Yönlü Açı
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<text x="197" y="78" text-anchor="middle" fill="#16a34a" font-size="12.5" font-weight="700">1. Pozitif (+) Yönlü Açı (Saat Yönünün Tersi)</text>'
    s += '<line x1="85" y1="210" x2="295" y2="210" stroke="#1e293b" stroke-width="2.5"/>'
    s += '<line x1="85" y1="210" x2="245" y2="105" stroke="#16a34a" stroke-width="2.5"/>'
    s += '<path d="M165,210 A80,80 0 0,0 148,168" fill="none" stroke="#16a34a" stroke-width="2.5"/>'
    s += '<polygon points="145,165 156,169 149,176" fill="#16a34a"/>'
    s += '<text x="220" y="228" fill="#1e293b" font-size="10.5" font-weight="700">[OA (Başlangıç Kenarı)</text>'
    s += '<text x="195" y="102" fill="#16a34a" font-size="10.5" font-weight="700">[OB (Bitim Kenarı)</text>'
    s += '<text x="197" y="262" text-anchor="middle" fill="#15803d" font-size="10.5" font-weight="700">Saatin dönme yönünün TERSİ (+) yöndür.</text>'

    # Sağ: Negatif Yönlü Açı
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<text x="562" y="78" text-anchor="middle" fill="#dc2626" font-size="12.5" font-weight="700">2. Negatif (-) Yönlü Açı (Saat Yönü)</text>'
    s += '<line x1="450" y1="120" x2="660" y2="120" stroke="#1e293b" stroke-width="2.5"/>'
    s += '<line x1="450" y1="120" x2="610" y2="225" stroke="#dc2626" stroke-width="2.5"/>'
    s += '<path d="M530,120 A80,80 0 0,1 513,162" fill="none" stroke="#dc2626" stroke-width="2.5"/>'
    s += '<polygon points="510,165 521,161 514,154" fill="#dc2626"/>'
    s += '<text x="585" y="110" fill="#1e293b" font-size="10.5" font-weight="700">[OA (Başlangıç Kenarı)</text>'
    s += '<text x="570" y="242" fill="#dc2626" font-size="10.5" font-weight="700">[OB (Bitim Kenarı)</text>'
    s += '<text x="562" y="262" text-anchor="middle" fill="#b91c1c" font-size="10.5" font-weight="700">Saatin dönme yönüyle AYNI yön (-) yöndür.</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Derece, Dakika, Saniye ve Radyan Dönüşüm Tablosu."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Açı Ölçü Birimleri: Derece - Radyan Dönüşümü ve Alt Birimler", "#7c3aed", "#f5f3ff")

    # Üst Denklem Kutusu
    s += '<rect x="30" y="55" width="700" height="58" rx="10" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>'
    s += '<text x="380" y="80" text-anchor="middle" fill="#5b21b6" font-size="14" font-weight="700">Temel Dönüşüm Orantısı:   D / 180  =  R / pi     (Tam Çember: 360° = 2.pi radyan,  180° = pi radyan)</text>'
    s += '<text x="380" y="101" text-anchor="middle" fill="#4c1d95" font-size="10.5">Derece Alt Birimleri:  1° = 60\' (dakika) = 3600\'\' (saniye)   |   1\' = 60\'\' (saniye)</text>'

    acilar = [
        ("30°", "pi / 6 rad", "#0284c7"),
        ("45°", "pi / 4 rad", "#0d9488"),
        ("60°", "pi / 3 rad", "#16a34a"),
        ("90°", "pi / 2 rad", "#d97706"),
        ("180°", "pi rad", "#dc2626"),
        ("270°", "3.pi / 2 rad", "#7c3aed"),
    ]
    for i, (der, rad, r) in enumerate(acilar):
        x = 30 + i * 118
        s += f'<rect x="{x}" y="130" width="108" height="150" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="130" width="108" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+54}" y="149" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">{der}</text>'
        s += f'<text x="{x+54}" y="198" text-anchor="middle" fill="{r}" font-size="13" font-weight="700">{rad}</text>'
        s += f'<text x="{x+54}" y="245" text-anchor="middle" fill="#64748b" font-size="9.5">180° = pi</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Esas Ölçü Bulma Yöntemi (Derece ve Radyan Cinsinden)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Açının Esas Ölçüsü: [0°, 360°) ve [0, 2.pi) Aralığına İndirgeme", "#0d9488", "#f0fdfa")

    kutular = [
        ("1. Pozitif Derecede Esas Ölçü", "Açı 360°'ye bölünür; kalan", "değer esas ölçüdür:", "alfa = beta + k . 360° (0° &lt;= alfa &lt; 360°)", "Örnek: 1120° = 3 . 360° + 40° => 40°", "#0d9488", "#ccfbf1"),
        ("2. Negatif Derecede Esas Ölçü", "Mutlak değerce 360°'ye bölünür;", "kalan 360°'den çıkarılır!", "Örnek: -800° -> 800 = 2.360 + 80", "Esas ölçü: 360° - 80° = 280°", "#dc2626", "#fee2e2"),
        ("3. Radyan Cinsinden (A . pi / B)", "Pay (A), paydanın 2 katına (2B)", "bölünür; kalan paya yazılır!", "Örnek: 23.pi / 4 -> 23 : 8 => Kalan 7", "Esas ölçü: 7.pi / 4 radyan", "#2563eb", "#dbeafe"),
    ]
    for i, (bas, a1, a2, a3, ex, r, bg) in enumerate(kutular):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="58" width="224" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="77" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="112" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+112}" y="130" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+112}" y="156" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a3}</text>'
        s += f'<rect x="{x+12}" y="180" width="200" height="82" rx="8" fill="#fff" stroke="{r}"/>'
        s += f'<text x="{x+112}" y="225" text-anchor="middle" fill="#1e293b" font-size="10.2" font-weight="700">{ex}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Birim Çember (x² + y² = 1) ve Trigonometrik Koordinatlar P(cos alfa, sin alfa)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Birim Çember (x² + y² = 1) ve P(cos alfa, sin alfa) Noktası", "#d97706", "#fffbeb")

    # Sol: Birim Çember Çizimi
    s += '<rect x="30" y="52" width="330" height="242" rx="10" fill="#fff" stroke="#fcd34d" stroke-width="1.5"/>'
    cx, cy, r = 195, 175, 82
    s += f'<line x1="75" y1="{cy}" x2="315" y2="{cy}" stroke="#64748b" stroke-width="1.5"/>'
    s += f'<line x1="{cx}" y1="65" x2="{cx}" y2="280" stroke="#64748b" stroke-width="1.5"/>'
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2563eb" stroke-width="2.5"/>'
    # P noktası (yaklaşık 40 derece)
    px, py = cx + 63, cy - 53
    s += f'<line x1="{cx}" y1="{cy}" x2="{px}" y2="{py}" stroke="#dc2626" stroke-width="2.2"/>'
    s += f'<line x1="{px}" y1="{py}" x2="{px}" y2="{cy}" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="4,2"/>'
    s += f'<circle cx="{px}" cy="{py}" r="4.5" fill="#dc2626"/>'
    s += f'<text x="{px+8}" y="{py-6}" fill="#dc2626" font-size="10.5" font-weight="700">P(cos a, sin a)</text>'
    s += f'<text x="{cx+88}" y="{cy+14}" fill="#1e293b" font-size="9.5">A(1,0)</text>'
    s += f'<text x="{cx-35}" y="{cy-86}" fill="#1e293b" font-size="9.5">B(0,1)</text>'
    s += f'<text x="{cx-118}" y="{cy+14}" fill="#1e293b" font-size="9.5">A\'(-1,0)</text>'
    s += f'<text x="{cx+6}" y="{cy+96}" fill="#1e293b" font-size="9.5">B\'(0,-1)</text>'

    # Sağ: Birim Çember Özellikleri
    s += '<rect x="380" y="52" width="350" height="242" rx="10" fill="#fff" stroke="#fcd34d" stroke-width="1.5"/>'
    s += '<text x="555" y="75" text-anchor="middle" fill="#92400e" font-size="12" font-weight="700">Birim Çemberin Temel Bağıntıları</text>'

    maddeler = [
        ("1. Birim Çember Denklemi:", "Merkezi O(0,0) ve yarıçapı r = 1 br olan çember: x² + y² = 1"),
        ("2. Bitim Noktası Koordinatları:", "P(x, y) = P(cos(alfa), sin(alfa)) -> Apsis = cos, Ordinat = sin"),
        ("3. Temel Pisagor Özdeşliği:", "cos²(alfa) + sin²(alfa) = 1   (-1 &lt;= sin(alfa), cos(alfa) &lt;= 1)"),
        ("4. Bölgelerde İşaretler (A-S-T-C):", "1. Bölge (+,+), 2. Bölge (-,+), 3. Bölge (-,-), 4. Bölge (+,-)"),
    ]
    for i, (b, ac) in enumerate(maddeler):
        y = 90 + i * 48
        s += f'<rect x="394" y="{y}" width="322" height="40" rx="6" fill="#fffbeb" stroke="#f59e0b"/>'
        s += f'<text x="404" y="{y+16}" fill="#b45309" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="404" y="{y+32}" fill="#1e293b" font-size="9.8">{ac}</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
