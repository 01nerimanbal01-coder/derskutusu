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
        'Üçgende Yükseklik Yardımıyla Sinüs Teoreminin Doğrulanması</text>'
        '<polygon points="60,175 280,175 190,55" fill="#eff6ff" stroke="#2563eb" stroke-width="2.2"/>'
        '<line x1="190" y1="55" x2="190" y2="175" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>'
        '<rect x="190" y="163" width="12" height="12" fill="none" stroke="#dc2626" stroke-width="1.5"/>'
        '<text x="190" y="46" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">A</text>'
        '<text x="45" y="180" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a">B</text>'
        '<text x="290" y="180" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a">C</text>'
        '<text x="190" y="192" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">H</text>'
        '<text x="115" y="108" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e293b">c</text>'
        '<text x="245" y="108" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e293b">b</text>'
        '<text x="170" y="192" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#1e293b">a</text>'
        '<text x="200" y="122" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">h_a</text>'
        + _kart(330, 42, 330, 145, "Dik Üçgenlerden Sinüs Teoremine", [
            "• ABH dik üçgeninde: sin B = h_a / c  =>  h_a = c . sin B",
            "• ACH dik üçgeninde: sin C = h_a / b  =>  h_a = b . sin C",
            "• İki ifade eşitlenirse: c . sin B = b . sin C",
            "• b / sin B = c / sin C = a / sin A = 2R",
            "• (R: ABC üçgeninin çevrel çemberinin yarıçapı)"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Pisagor Bağıntısından Kosinüs Teoreminin İspatı</text>'
        '<polygon points="50,175 290,175 200,55" fill="#ecfdf5" stroke="#059669" stroke-width="2.2"/>'
        '<line x1="200" y1="55" x2="200" y2="175" stroke="#d97706" stroke-width="2" stroke-dasharray="5,4"/>'
        '<rect x="200" y="163" width="12" height="12" fill="none" stroke="#d97706" stroke-width="1.5"/>'
        '<text x="200" y="46" font-family="sans-serif" font-size="13" font-weight="bold" fill="#065f46" text-anchor="middle">A</text>'
        '<text x="35" y="180" font-family="sans-serif" font-size="13" font-weight="bold" fill="#065f46">B</text>'
        '<text x="300" y="180" font-family="sans-serif" font-size="13" font-weight="bold" fill="#065f46">C</text>'
        '<text x="200" y="192" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">H</text>'
        '<text x="125" y="192" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e293b">a - x</text>'
        '<text x="245" y="192" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e293b">x = b.cos C</text>'
        '<text x="208" y="120" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#d97706">b.sin C</text>'
        + _kart(330, 42, 330, 145, "Kosinüs Teoremi Formülleri", [
            "• ABH’de Pisagor: c² = (b.sin C)² + (a - b.cos C)²",
            "• sin²C + cos²C = 1 özdeşliği kullanıldığında:",
            "• c² = a² + b² - 2.a.b.cos C",
            "• a² = b² + c² - 2.b.c.cos A",
            "• b² = a² + c² - 2.a.c.cos B"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 205, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Hangi Durumda Hangi Teorem Kullanılır? (Problem Çözme Rehberi)</text>'
        + _kart(25, 42, 300, 145, "Sinüs Teoremi Kullanılan Durumlar", [
            "• İki açı ve bir kenar biliniyorsa (AÇK / KAA)",
            "• İki kenar ve bunlardan birinin karşısındaki",
            "  açı biliniyorsa (KKA)",
            "• Çevrel çemberin yarıçapı (R) soruluyorsa",
            "• Alan = (1/2).a.b.sin C bağıntısıyla alan hesabında"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "Kosinüs Teoremi Kullanılan Durumlar", [
            "• İki kenar ve aralarındaki açı biliniyorsa (KAK)",
            "  -> Karşıdaki üçüncü kenarı bulmak için",
            "• Üç kenar uzunluğu da biliniyorsa (KKK)",
            "  -> Herhangi bir iç açının kosinüsünü bulmak için",
            "• Açı 90° ise cos 90° = 0 olduğundan Pisagor’a dönüşür"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Kenar-Açı İlişkisi ve Özel Açıların Trigonometrik Değerleri</text>'
        + _kart(25, 42, 300, 138, "Dar, Dik ve Geniş Açıda Kosinüs İşareti", [
            "• m(A) < 90° (Dar açı)  => cos A > 0  => a² < b² + c²",
            "• m(A) = 90° (Dik açı)  => cos 90° = 0 => a² = b² + c²",
            "• m(A) > 90° (Geniş açı)=> cos A < 0  => a² > b² + c²",
            "• Bütünler açılar: cos(180° - α) = -cos α"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 138, "Bütünler Açıların Sinüs Özelliği", [
            "• sin(180° - α) = sin α (Birbirini 180°’ye tamamlayan",
            "  iki açının sinüs değerleri birbirine eşittir)",
            "• Örnek: sin 120° = sin 60° = kök(3) / 2",
            "• Örnek: cos 120° = -cos 60° = -1 / 2"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
