def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'BAĞ KIRILMASI (ENDOTERMİK) VE BAĞ OLUŞUMU (EKZOTERMİK) İLKESİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Bağ Kırılması (Kopması) — Endotermik (+)",
        [
            "• Gaz fazındaki bir molekülde atomları bir arada",
            "  tutan kovalent bağı koparmak için dışarıdan",
            "  enerji verilmesi gerekir (Isı alan / ΔH > 0).",
            "• Denklem: X2(g) + ısı → 2X(g)   (ΔH = +E kJ/mol)",
            "• İki atomlu gaz moleküllerinin atomlarına",
            "  ayrışması her zaman ENDOTERMİKTİR.",
            "• Girenlerdeki bağlar kırılırken enerji soğurulur.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Bağ Oluşumu (Sentezi) — Ekzotermik (-)",
        [
            "• Gaz fazındaki serbest atomlar birleşerek",
            "  kovalent bağ oluştururken dışarıya aynı miktarda",
            "  enerji açığa çıkar (Isı veren / ΔH &lt; 0).",
            "• Denklem: 2X(g) → X2(g) + ısı   (ΔH = -E kJ/mol)",
            "• Serbest radikallerden/atomlardan bağ oluşumu",
            "  her zaman EKZOTERMİKTİR.",
            "• Ürünlerdeki bağlar oluşurken enerji salınır.",
        ],
        "#2563eb", "#eff6ff"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'BAĞ UZUNLUĞU, BAĞ DERECESİ VE BAĞ SAĞLAMLIĞI (ENERJİSİ) İLİŞKİSİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Aynı Atomlar Arasında Çoklu Bağlar",
        [
            "• Karbon-karbon bağlarının karşılaştırması:",
            "  Tekli (C-C) &lt; İkili (C=C) &lt; Üçlü (C≡C)",
            "• Bağ Enerjisi (kJ/mol): 347 &lt; 614 < 839",
            "• Bağ Uzunluğu (pm): 154 pm > 134 pm > 120 pm",
            "• KURAL: Bağ sayısı (derecesi) arttıkça atomlar",
            "  birbirine yaklaşır; bağ uzunluğu KISALIR,",
            "  bağ enerjisi ve bağ sağlamlığı ARTAR!",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Atom Yarıçapı ve Bağ Enerjisi İlişkisi",
        [
            "• Halojen hidrojenürlerin (H-X) karşılaştırması:",
            "  Atom yarıçapı: F &lt; Cl &lt; Br &lt; I",
            "• Bağ uzunluğu: H-F &lt; H-Cl &lt; H-Br < H-I",
            "• Bağ enerjisi (kJ/mol): H-F (565) > H-Cl (431)",
            "  > H-Br (364) > H-I (297)",
            "• KURAL: Bağ yapan atomların yarıçapı küçüldükçe",
            "  çekirdekler yaklaşır ve bağ sağlamlığı ARTAR!",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'BAĞ ENERJİLERİYLE TEPKİME ENTALPİSİ (ΔH) HESAPLAMA FORMÜLÜ</text>'
    )
    ic += (
        '<rect x="20" y="42" width="720" height="62" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
        '<text x="380" y="66" fill="#92400e" font-size="14" font-weight="bold" text-anchor="middle">'
        'ΔH°_tepkime = Σ ΔH(Kırılan Bağlar / Girenler)  -  Σ ΔH(Oluşan Bağlar / Ürünler)</text>'
        '<text x="380" y="90" fill="#78350f" font-size="12" text-anchor="middle">'
        '(Dikkat: Oluşum entalpisindeki "Ürünler - Girenler" kuralının tersine burada "Kırılan (Giren) - Oluşan (Ürün)" alınır!)</text>'
    )
    ic += _kart(
        20, 116, 345, 132,
        "Durum 1: E_kırılan > E_oluşan  (ΔH > 0)",
        [
            "• Girenlerdeki bağları kırmak için harcanan enerji,",
            "  ürünlerdeki bağlar oluşurken açığa çıkan enerjiden",
            "  daha büyüktür.",
            "• Tepkime ENDOTERMİKTİR (ΔH işareti pozitif +).",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 116, 345, 132,
        "Durum 2: E_oluşan > E_kırılan  (ΔH &lt; 0)",
        [
            "• Ürünlerdeki yeni bağlar oluşurken açığa çıkan enerji,",
            "  girenlerdeki bağları kırmak için harcanan enerjiden",
            "  daha büyüktür.",
            "• Tepkime EKZOTERMİKTİR (ΔH işareti negatif -).",
        ],
        "#2563eb", "#eff6ff"
    )
    return _svg(760, 270, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÖRNEK MODELLEME: H2(g) + Cl2(g) → 2HCl(g) TEPKİMESİNİN ANALİZİ</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Kırılan Bağlar (Girenler)",
        [
            "• 1 mol H-H bağı kırılır:",
            "  E(H-H) = +436 kJ",
            "• 1 mol Cl-Cl bağı kırılır:",
            "  E(Cl-Cl) = +242 kJ",
            "• Toplam Kırılan Bağ Enerjisi:",
            "  ΣE_kırılan = 436 + 242 = 678 kJ",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Oluşan Bağlar (Ürünler)",
        [
            "• Ürünlerde 2 mol HCl vardır.",
            "• 2 mol H-Cl bağı oluşur:",
            "  E(H-Cl) = 431 kJ/mol",
            "• Toplam Oluşan Bağ Enerjisi:",
            "  ΣE_oluşan = 2 x 431 = 862 kJ",
            "  enerji dışarıya salınır.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Net Entalpi Değişimi (ΔH)",
        [
            "• ΔH = ΣE_kırılan - ΣE_oluşan",
            "• ΔH = 678 - 862 = -184 kJ",
            "• Oluşan bağlar daha sağlam",
            "  olduğu için net 184 kJ ısı",
            "  açığa çıkar (Ekzotermik).",
            "• 1 mol HCl için ΔH = -92 kJ.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][3]["gorsel"] = GORSELLER["b4"]