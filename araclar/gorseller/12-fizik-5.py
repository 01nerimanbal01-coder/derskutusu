def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563EB", bg="#EFF6FF"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KEPLER YASALARI: GEZEGENLERİN GÜNEŞ ETRAFINDAKİ HAREKETİ</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. YÖRÜNGE YASASI", [
        "• Her gezegen, odaklarından",
        "  birinde Güneş bulunan",
        "  ELİPTİK bir yörüngede",
        "  dolanır.",
        "• Yörünge tam çember değil,",
        "  iki odaklı (F1, F2) elipstir.",
        "• Güneş'e uzaklık yıl",
        "  boyunca değişir."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(237, 44, 205, 190, "2. ALANLAR YASASI", [
        "• Gezegeni Güneş'e birleştiren",
        "  yarıçap vektörü, eşit zaman",
        "  aralıklarında EŞİT ALANLAR",
        "  tarar (Delta_t1 = Delta_t2",
        "  ise A1 = A2).",
        "• Güneş'e yaklaştıkça çizgisel",
        "  hız ve kinetik enerji ARTAR!",
        "• Açısal momentum KORUNUR."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "3. PERİYOTLAR YASASI", [
        "• Aynı yıldız etrafında",
        "  dolanan tüm gezegenler için",
        "  ortalama yörünge yarıçapının",
        "  küpünün, dolanım periyodunun",
        "  karesine oranı SABİTTİR:",
        "  R^3 / T^2 = Sabit",
        "• Güneş'ten uzaklaştıkça",
        "  periyot (T) büyür."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'NEWTON\'UN EVRENSEL KÜTLE ÇEKİM YASASI VE ÇEKİM İVMESİ (g)</text>'
    )
    ic += _kart(20, 44, 310, 190, "KÜTLE ÇEKİM KUVVETİ (F = G.m1.m2 / d^2)", [
        "• Evrendeki her iki kütle birbirini kütlelerinin",
        "  çarpımıyla doğru, merkezleri arasındaki uzaklığın",
        "  karesiyle ters orantılı kuvvetle çeker.",
        "• Etki-tepki çiftidir: Büyüklükleri EŞİT, yönleri ZITTIR",
        "  (|F_12| = |F_21|, kütleler farklı olsa bile!).",
        "• G = 6,67 x 10^(-11) N.m^2/kg^2 (Evrensel çekim sabiti)."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "ÇEKİM ALANI İVMESİ (g = G.M / R^2)", [
        "• Gezegenin merkezinden yüzeyine (r &lt;= R) kadar:",
        "  Çekim ivmesi uzaklıkla DOĞRU orantılı artar",
        "  (Merkezde r = 0 iken g = 0; yüzeyde g_max = G.M / R^2).",
        "  Kürede g = (4/3).pi.G.d.r ('KADER' formülü).",
        "• Yüzeyden dışarı doğru uzaklaştıkça (r &gt; R):",
        "  g = G.M / r^2 (Uzaklığın karesiyle TERS orantılı azalır)."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'UYDULARIN DOLANIM HIZI VE KÜTLE ÇEKİM POTANSİYEL ENERJİSİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "UYDUNUN ÇİZGİSEL HIZI (v = Kök(G.M / r))", [
        "• Kütle çekim kuvveti merkezcil kuvvete eşitlenir:",
        "  G.M.m / r^2 = m.v^2 / r  =&gt;  v = Kök(G.M / r)",
        "• DİKKAT: Uydunun yörüngedeki dolanım hızı (v),",
        "  uydunun kendi kütlesine (m) BAĞLI DEĞİLDİR!",
        "• Yörünge yarıçapı (r) arttıkça çizgisel hız (v)",
        "  ve açısal hız (w) AZALIR, periyot (T) ARTAR."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "BAĞLANMA VE KURTULMA (KAÇIŞ) ENERJİSİ", [
        "• Potansiyel Enerji: E_p = - G.M.m / r",
        "• Kinetik Enerji: E_k = + G.M.m / (2r)",
        "• Toplam Mekanik Enerji: E_top = - G.M.m / (2r)",
        "• Bağlanma Enerjisi: E_bağ = + G.M.m / (2r) (Yörüngeden",
        "  koparmak için gereken enerji).",
        "• Kurtulma Enerjisi: E_kurt = + G.M.m / R (Yüzeyden",
        "  çekim alanından tamamen çıkarmak için gereken enerji)."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ELİPTİK YÖRÜNGEDE VE YARIÇAP DEĞİŞİMİNDE BÜYÜKLÜKLERİN DEĞİŞİMİ</text>'
    )
    satirlar = [
        ("ELİPTİK YÖRÜNGEDE GÜNEŞ'E YAKLAŞIRKEN", "Çizgisel hız (v) ve kinetik enerji ARTAR; potansiyel enerji AZALIR; toplam enerji ve açısal momentum (L) DEĞİŞMEZ!", "#2563EB", "#EFF6FF"),
        ("ELİPTİK YÖRÜNGEDE EYLEMSİZLİK MOMENTİ (I)", "Gezegen Güneş'e yaklaştıkça r azaldığı için eylemsizlik momenti (I = m.r^2) AZALIR, açısal hız (w) ARTAR.", "#059669", "#ECFDF5"),
        ("UYDU DAHA ÜST YÖRÜNGEYE ÇIKARILIRSA (r ARTARSA)", "Çizgisel hız (v) ve kinetik enerji (E_k) AZALIR; ancak başında eksi (-) olduğu için E_p ve E_top ARTAR!", "#D97706", "#FEF3C7"),
        ("HABERLEŞME UYDULARI (YER SABİT / JEOSENKRON)", "Dünya ile aynı periyotta (T = 24 saat) dönerler ve yerden bakıldığında gökyüzünde hep aynı noktada sabit görünürler.", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(satirlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
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
