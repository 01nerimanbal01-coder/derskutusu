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
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Sabit İvmeli Hareket Grafiklerinden Matematiksel Modellere Geçiş</text>'
        + _kart(20, 42, 200, 142, "1. Hız-Zaman Denklemi", [
            "• İvme-zaman (a-t) grafiğinin",
            "  altındaki alan Δv = a.t verir",
            "• v = v₀ + a.t (Hızlanan)",
            "• v = v₀ - a.t (Yavaşlayan)",
            "• İlk hız sıfırsa: v = a.t"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. Konum-Zaman Denklemi", [
            "• Hız-zaman (v-t) grafiğinin",
            "  altındaki yamuk alanı Δx verir",
            "• Δx = ((v₀ + v) / 2) . t",
            "• Δx = v₀.t + (1/2).a.t²",
            "• İlk hız sıfırsa: Δx = (1/2).a.t²"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 142, "3. Zamansız Hız Denklemi", [
            "• t = (v - v₀) / a ifadesi",
            "  Δx denkleminde yerine konursa:",
            "• v² = v₀² + 2.a.Δx (Hızlanan)",
            "• v² = v₀² - 2.a.Δx (Yavaşlayan)",
            "• Zaman verilmediğinde kullanılır"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'İlk Hızsız Düzgün Hızlanan Hareket: Ardışık Zamanlarda Alınan Yollar (x - 3x - 5x)</text>'
        + _kart(25, 42, 300, 145, "Toplam Yer Değiştirme (t² ile Orantılı)", [
            "• 0 - t aralığında toplam yol: x = (1/2).a.t²",
            "• 0 - 2t aralığında toplam yol: 4x = (1/2).a.(2t)²",
            "• 0 - 3t aralığında toplam yol: 9x = (1/2).a.(3t)²",
            "• 0 - 4t aralığında toplam yol: 16x = (1/2).a.(4t)²",
            "• Konum zamanın karesiyle (1 - 4 - 9 - 16) artar"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Her Saniye İçinde Alınan Yol (Tek Sayılar)", [
            "• 1. t süresinde (0 - t): Δx₁ = x",
            "• 2. t süresinde (t - 2t): Δx₂ = 3x",
            "• 3. t süresinde (2t - 3t): Δx₃ = 5x",
            "• 4. t süresinde (3t - 4t): Δx₄ = 7x",
            "• Ardışık eşit sürelerde yollar x, 3x, 5x, 7x... gider"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Düzgün Yavaşlayan Hareket ve Fren (Durma) Mesafesi Analizi</text>'
        + _kart(25, 42, 300, 145, "Düzgün Yavaşlayıp Duran Araç (v_son = 0)", [
            "• Hız ile ivme vektörleri ZIT yönlüdür",
            "• Durma süresi: t_durma = v₀ / a",
            "• Ortalama hız: v_ort = v₀ / 2",
            "• Durma mesafesi: Δx_durma = v₀² / (2.a)",
            "• İlk hız 2 katına çıkarsa durma mesafesi 4 katına çıkar!"
        ], "#dc2626", "#fef2f2")
        + _kart(355, 42, 300, 145, "Trafik Güvenliği ve Takip Mesafesi", [
            "• Sürücünün tehlikeyi görüp frene basma süresi:",
            "  İntikal (Tepki) Süresi (Sabit hızla yol alır)",
            "• Toplam Durma Mesafesi = Tepki Mesafesi + Fren Mesafesi",
            "• Yağışlı ve buzlu zeminde ivme (a) küçüldüğü için",
            "  fren mesafesi uzar"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Konum-Zaman (x-t) Parabolleri: ”Genç K” ve ”Yaşlı K” Kuralı</text>'
        + _kart(25, 42, 300, 138, "Düzgün Hızlanan (Eğim Artar - Dikleşir)", [
            "• Grafik kolları düşey eksene yaklaşır (Genç K)",
            "• (+x) yönünde hızlanan: Yukarı doğru dikleşen eğri",
            "• (-x) yönünde hızlanan: Aşağı doğru dikleşen eğri",
            "• Hız ve ivme vektörleri AYNI işaretlidir"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Düzgün Yavaşlayan (Eğim Azalır - Yataylaşır)", [
            "• Grafik kolları zaman eksenine paralel olur (Yaşlı K)",
            "• (+x) yönünde yavaşlayan: Yukarı çıkarken boynu bükülen",
            "• (-x) yönünde yavaşlayan: Aşağı inerken yataylaşan",
            "• Hız ve ivme vektörleri ZIT işaretlidir"
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
