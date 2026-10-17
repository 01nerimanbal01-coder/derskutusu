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
        'Dünya Dinlerinin Ortaya Çıktığı Üç Ana Coğrafi Havza</text>'
        + _kart(18, 42, 205, 148, "1. Orta Doğu (Sâmî) Havzası", [
            "• İlahi / Vahye Dayalı Dinler:",
            "  İslamiyet, Hristiyanlık,",
            "  Yahudilik (ve Sâbiîlik)",
            "• Doğuş Yeri: Hicaz, Filistin,",
            "  Kudüs ve Mezopotamya"
        ], "#2563eb", "#eff6ff")
        + _kart(237, 42, 205, 148, "2. Güney Asya (Hint) Havzası", [
            "• Hint Kökenli Dinler:",
            "  Hinduizm, Budizm,",
            "  Cayinizm ve Sihizm",
            "• Doğuş Yeri: İndus ve Ganj",
            "  nehirleri havzası (Hindistan)"
        ], "#059669", "#ecfdf5")
        + _kart(456, 42, 205, 148, "3. Doğu Asya (Çin-Japon) Havzası", [
            "• Uzak Doğu Dinleri:",
            "  Konfüçyanizm, Taoizm",
            "  ve Şintoizm",
            "• Doğuş Yeri: Sarı Irmak havzası",
            "  (Çin) ve Japon takımadaları"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Günümüzde Dinlerin Yayılış Bölgeleri ve Demografik Özellikleri</text>'
        + _kart(25, 42, 300, 145, "Evrensel Dinlerin Yayılış Coğrafyası", [
            "• İslamiyet: Orta Doğu, Kuzey Afrika, Türkistan,",
            "  Güney/Güneydoğu Asya (Endonezya, Pakistan), Balkanlar",
            "• Hristiyanlık: Avrupa, Kuzey/Güney Amerika, Sahra",
            "  Altı Afrika ve Okyanusya (Avustralya)",
            "• Budizm: Çin, Tayland, Myanmar, Japonya, Sri Lanka"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Millî / Bölgesel Kalan Dinler", [
            "• Yahudilik: İsrail, ABD ve Avrupa (diaspora)",
            "• Hinduizm ve Cayinizm: Büyük oranda Hindistan ve",
            "  Nepal (Sihizm -> Pencap bölgesi)",
            "• Taoizm ve Konfüçyanizm: Çin, Tayvan, Kore",
            "• Şintoizm: Yalnızca Japonya’ya özgü millî din"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
}


def uygula(v):
    hedefler = [0, 1]
    anahtarlar = ["b1", "b2"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]