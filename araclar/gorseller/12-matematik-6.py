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
        'Üstel Büyüme ve Üstel Bozunma (Azalma) Modelleri</text>'
        + _kart(25, 42, 300, 145, "Üstel Büyüme (Nüfus, Bakteri, Bileşik Faiz)", [
            "• Genel Model: N(t) = N_0 . e^(k.t)  (k > 0)",
            "• Periyotlu Artış: N(t) = N_0 . (1 + r)^t",
            "• Bakteri Bölünmesi: N(t) = N_0 . 2^(t/T)",
            "• Bileşik Faiz: A(t) = P . (1 + r/n)^(n.t)",
            "• Zaman ilerledikçe artış hızı katlanarak büyür."
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Üstel Azalma (Radyoaktif Yarılanma / Soğuma)", [
            "• Genel Model: M(t) = M_0 . e^(-k.t)  (k > 0)",
            "• Yarı Ömür (T_1/2) Modeli: M(t) = M_0 . (1/2)^(t / T)",
            "• Karbon-14 (C-14) ile arkeolojik yaş tayini",
            "• İlaç etken maddesinin kandan atılım hızı",
            "• Newton’ın Soğuma Yasası: T(t) = T_ortam + (T_0 - T_ortam).e^(-k.t)"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Logaritmik Ölçeklerle Gerçek Hayat Modellemesi (Richter, pH, Desibel)</text>'
        + _kart(18, 42, 205, 145, "1. Richter Deprem Ölçeği", [
            "• Bağıntı: M = log(I / I_0)",
            "• M: Deprem büyüklüğü",
            "• I: Deprem yoğunluğu (genlik)",
            "• Büyüklük 1 birim artarsa",
            "  sarsıntı şiddeti 10 kat artar!"
        ], "#dc2626", "#fef2f2")
        + _kart(237, 42, 205, 145, "2. Kimyada pH Ölçeği", [
            "• Bağıntı: pH = -log[H+]",
            "• [H+]: Hidrojen iyonu molar",
            "  derişimi (mol/L)",
            "• [H+] = 10^(-pH) M",
            "• pH < 7 asit, pH > 7 baz"
        ], "#d97706", "#fffbeb")
        + _kart(456, 42, 205, 145, "3. Ses Şiddeti (Desibel)", [
            "• Bağıntı: L = 10 . log(I / I_0)",
            "• L: Ses düzeyi (dB)",
            "• I_0 = 10^(-12) W/m² (eşik)",
            "• Ses düzeyi 10 dB artarsa",
            "  ses şiddeti 10 katına çıkar!"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 202, ic)


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