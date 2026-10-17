def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Genel Dörtgenlerde Açı, Köşegen ve Alan Özellikleri</text>'
        '<polygon points="45,170 275,175 245,55 85,65" fill="#eff6ff" stroke="#2563eb" stroke-width="2.2"/>'
        '<line x1="45" y1="170" x2="245" y2="55" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="5,3"/>'
        '<line x1="85" y1="65" x2="275" y2="175" stroke="#059669" stroke-width="1.8" stroke-dasharray="5,3"/>'
        '<text x="32" y="175" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e3a8a">A</text>'
        '<text x="283" y="180" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e3a8a">B</text>'
        '<text x="252" y="52" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e3a8a">C</text>'
        '<text x="70" y="60" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e3a8a">D</text>'
        '<text x="168" y="112" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">α</text>'
        + _kart(320, 42, 340, 145, "Temel Dörtgen Bağıntıları", [
            "• İç açılar toplamı: m(A)+m(B)+m(C)+m(D) = 360°",
            "• Dış açılar toplamı her konveks çokgende 360°’dir.",
            "• Köşegenli alan: Alan = (1/2) . |AC| . |BD| . sin α",
            "• Köşegenler dik kesişirse (α = 90°): a² + c² = b² + d²",
            "• Kenar orta noktaları birleştirilirse paralelkenar oluşur."
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Yamuk ve İkizkenar Yamuğun Temel Özellikleri</text>'
        '<polygon points="45,175 285,175 235,60 95,60" fill="#ecfdf5" stroke="#059669" stroke-width="2.2"/>'
        '<line x1="70" y1="117.5" x2="260" y2="117.5" stroke="#d97706" stroke-width="2" stroke-dasharray="5,3"/>'
        '<text x="32" y="180" font-family="sans-serif" font-size="12" font-weight="bold" fill="#065f46">A</text>'
        '<text x="292" y="180" font-family="sans-serif" font-size="12" font-weight="bold" fill="#065f46">B</text>'
        '<text x="242" y="56" font-family="sans-serif" font-size="12" font-weight="bold" fill="#065f46">C</text>'
        '<text x="80" y="56" font-family="sans-serif" font-size="12" font-weight="bold" fill="#065f46">D</text>'
        '<text x="165" y="53" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">c (üst taban)</text>'
        '<text x="165" y="192" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">a (alt taban)</text>'
        '<text x="165" y="112" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#d97706" text-anchor="middle">Orta taban: e = (a+c)/2</text>'
        + _kart(320, 42, 340, 145, "Yamukta Uzunluk ve Alan", [
            "• [AB] // [DC] => m(A)+m(D) = 180°, m(B)+m(C) = 180°",
            "• Orta taban uzunluğu: |EF| = (a + c) / 2",
            "• Köşegenlerin orta tabanda ayırdığı parça: |KL| = |a - c| / 2",
            "• Yamuğun alanı: Alan = ((a + c) / 2) . h",
            "• İkizkenar yamukta |AD| = |BC| ve |AC| = |BD|’dir."
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 205, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Paralelkenar ve Eşkenar Dörtgenin Özellikleri</text>'
        + _kart(25, 42, 300, 145, "Paralelkenar Özellikleri", [
            "• Karşılıklı kenarlar paralel ve eşit uzunluktadır.",
            "• Karşılıklı açılar eşit, ardışık açılar bütünlerdir (180°).",
            "• Köşegenler birbirini ortalar (|AO|=|OC|, |BO|=|OD|).",
            "• Alan = a . h_a = b . h_b = a . b . sin A",
            "• Köşegenler alanı 4 eşit üçgensel bölgeye ayırır."
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "Eşkenar Dörtgen ve Dikdörtgen", [
            "• Eşkenar dörtgende 4 kenar eşittir; köşegenler dik",
            "  kesişir ve iç açıortaydır: Alan = (|AC|.|BD|)/2",
            "• Dikdörtgende açılar 90° ve köşegen uzunlukları",
            "  birbirine eşittir (|AC| = |BD|); Alan = a . b",
            "• Kare hem dikdörtgen hem eşkenar dörtgendir."
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
}


def uygula(v):
    hedefler = [0, 1, 2]
    anahtarlar = ["b1", "b2", "b3"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]