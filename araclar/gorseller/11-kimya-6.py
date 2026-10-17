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
        'Standart Oluşum Entalpisi (ΔH°_f) ve Kararlı Elementler</text>'
        + _kart(25, 42, 300, 145, "Standart Oluşum Entalpisi Tanımı", [
            "• 25 °C (298 K) ve 1 atm (standart koşullar)",
            "• 1 mol bileşiğin kendi elementlerinin en kararlı",
            "  allotrop ve fiziksel hâllerinden oluşması",
            "  sırasındaki entalpi değişimidir (ΔH°_f).",
            "• Birimi genellikle kJ/mol’dür."
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "ΔH°_f = 0 Kabul Edilen Maddeler", [
            "• O_2(g), N_2(g), H_2(g), Cl_2(g)  =>  ΔH°_f = 0",
            "• C(grafit, k) => 0  (C(elmas) != 0)",
            "• O_3(ozon, g) != 0,  S(rombik) = 0",
            "• Fe(k), Cu(k), Na(k), Hg(s) => ΔH°_f = 0",
            "• H_2O(s), CO(g) gibi bileşiklerin ΔH°_f != 0"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Oluşum Entalpileri Yardımıyla Tepkime Entalpisinin Hesaplanması</text>'
        '<rect x="40" y="42" width="600" height="48" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>'
        '<text x="340" y="71" font-family="sans-serif" font-size="15" font-weight="bold" fill="#b45309" text-anchor="middle">'
        'ΔH°_tepkime = Σ n . ΔH°_f(Ürünler)  −  Σ m . ΔH°_f(Girenler)</text>'
        + _kart(40, 102, 285, 92, "Ekzotermik Tepkime (ΔH° < 0)", [
            "• Σ ΔH°_f(Ürünler) < Σ ΔH°_f(Girenler)",
            "• Ortama ısı verilir; düşük enerjili",
            "  ürünler enerji bakımından daha kararlıdır."
        ], "#dc2626", "#fef2f2")
        + _kart(355, 102, 285, 92, "Endotermik Tepkime (ΔH° > 0)", [
            "• Σ ΔH°_f(Ürünler) > Σ ΔH°_f(Girenler)",
            "• Ortamdan ısı alınır; yüksek sıcaklıklarda",
            "  ürünler, düşük sıcaklıkta girenler kararlıdır."
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 205, ic)


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
