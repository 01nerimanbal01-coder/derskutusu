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
        'Newton’ın Evrensel Kütle Çekim Yasası</text>'
        '<circle cx="75" cy="115" r="28" fill="#dbeafe" stroke="#2563eb" stroke-width="2.2"/>'
        '<text x="75" y="120" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">m_1</text>'
        '<circle cx="245" cy="115" r="22" fill="#dcfce7" stroke="#059669" stroke-width="2.2"/>'
        '<text x="245" y="120" font-family="sans-serif" font-size="13" font-weight="bold" fill="#065f46" text-anchor="middle">m_2</text>'
        '<line x1="103" y1="115" x2="150" y2="115" stroke="#dc2626" stroke-width="2.5"/>'
        '<polygon points="157,115 147,110 147,120" fill="#dc2626"/>'
        '<text x="130" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">F_12</text>'
        '<line x1="223" y1="115" x2="176" y2="115" stroke="#dc2626" stroke-width="2.5"/>'
        '<polygon points="169,115 179,110 179,120" fill="#dc2626"/>'
        '<text x="195" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">F_21</text>'
        '<line x1="75" y1="162" x2="245" y2="162" stroke="#475569" stroke-width="1.6" stroke-dasharray="4,3"/>'
        '<text x="160" y="178" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">d (kütle merkezleri arası uzaklık)</text>'
        + _kart(315, 42, 345, 145, "Evrensel Kütle Çekim Kuvveti Özellikleri", [
            "• Bağıntı: F = G . (m_1 . m_2) / d²",
            "• G = 6,67 . 10^(-11) N.m²/kg² (Evrensel çekim sabiti)",
            "• Kütlelerin çarpımıyla doğru, aradaki uzaklığın",
            "  karesiyle (d²) ters orantılıdır.",
            "• Etki-tepki çiftidir: |F_12| = |F_21| ve F_12 = -F_21"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Kütle Çekim İvmesinin (g) Uzaklığa Göre Değişimi</text>'
        + _kart(25, 42, 300, 145, "Gezegenin İçinde ve Yüzeyinde g", [
            "• Gezegenin tam merkezinde: g = 0",
            "• Merkezden yüzeye doğru (r < R): Uzaklıkla",
            "  DOĞRU orantılı artar -> g_iç = (4/3).π.G.d.r",
            "• Gezegen yüzeyinde (r = R) maksimumdur:",
            "  g_yüzey = G . M / R²"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Yüzeyden Uzaklaştıkça (r > R) ve Uydular", [
            "• Yüzeyden dışarı çıkıldıkça merkezden uzaklığın",
            "  karesiyle TERS orantılı azalır: g(r) = G . M / r²",
            "• Uydu dolanım hızı: F_çekim = F_merkezcil",
            "  G.M.m / r² = m.v² / r  =>  v = kök(G . M / r)",
            "• Uydu hızı uydunun kendi kütlesine (m) bağlı değildir!"
        ], "#d97706", "#fffbeb")
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