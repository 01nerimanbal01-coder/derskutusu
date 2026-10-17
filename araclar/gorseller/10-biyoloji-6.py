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
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Fotosentezin İki Evresi: Işığa Bağımlı ve Işıktan Bağımsız Tepkimeler</text>'
        + _kart(25, 42, 300, 145, "1. Işığa Bağımlı Tepkimeler (Grana / Tilakoit)", [
            "• Kloroplastın tilakoit zarlarında (grana) gerçekleşir",
            "• Klorofil ve ETS görev yapar; ışık DOĞRUDAN şarttır",
            "• Su (H₂O) fotolize uğrar -> Oksijen (O₂) atmosfere verilir",
            "• Işık enerjisiyle ATP (Fotofosforilasyon) ve",
            "  NADPH molekülleri üretilip stromaya aktarılır"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "2. Işıktan Bağımsız Evre / Calvin Döngüsü (Stroma)", [
            "• Kloroplastın sıvı kısmında (stroma) gerçekleşir",
            "• Işık doğrudan gerekmez ama gündüz gerçekleşir",
            "• Enzim kontrolündedir -> Sıcaklık değişimine çok duyarlıdır",
            "• CO₂ tutulur; ATP ve NADPH harcanarak PGAL’den",
            "  glikoz, amino asit, yağ asidi ve vitamin sentezlenir"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Fotosentezde Atomların İzlediği Yol (Ağır Oksijen ¹⁸O Deneyi)</text>'
        + _kart(25, 42, 300, 140, "6 CO₂ + 12 H₂O  -->  C₆H₁₂O₆ + 6 O₂ + 6 H₂O", [
            "• Karbondioksitteki Karbon (C) -> Glikozun yapısına (C₆)",
            "• Karbondioksitteki Oksijen (O) -> Glikozun (O₆) ve",
            "  ürünlerdeki suyun yapısına katılır",
            "• Karbondioksitteki oksijen ATMOSFERE VERİLMEZ!"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 140, "Sudaki (H₂O) Atomların Hedefi", [
            "• Sudaki Hidrojen (H) -> NADPH aracılığıyla glikozun",
            "  (H₁₂) ve çıkan suyun yapısına katılır",
            "• Sudaki Oksijen (¹⁸O) -> Fotoliz sonucu TAMAMEN",
            "  atmosfere serbest O₂ gazı olarak verilir!"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 195, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Fotosentez Hızına Etki Eden Çevresel Faktörler ve Minimum Yasası</text>'
        + _kart(20, 42, 200, 140, "Işık Şiddeti ve Dalga Boyu", [
            "• Işık şiddeti arttıkça hız",
            "  belirli değere kadar artar,",
            "  sonra sabitlenir",
            "• Mor ve kırmızıda EN YÜKSEK;",
            "  yeşil ışıkta EN DÜŞÜK hız"
        ], "#d97706", "#fffbeb")
        + _kart(240, 42, 200, 140, "CO₂ Yoğunluğu ve Su", [
            "• CO₂ belirli eşik değerin",
            "  altındaysa fotosentez durur",
            "• Su miktarı %15’in altına",
            "  inerse enzimler çalışamaz",
            "  ve stomalar kapanır"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 140, "Sıcaklık (Optimum: 25-35°C)", [
            "• Çan eğrisi grafiği gösterir",
            "• Optimuma kadar hızı artırır",
            "• Yüksek sıcaklıkta (45°C+)",
            "  enzimler denatüre olur ve",
            "  fotosentez tamamen durur"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 195, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Fotosentez (Fotoototrof) ve Kemosentez (Kemoototrof) Karşılaştırması</text>'
        + _kart(25, 42, 300, 145, "Fotosentez (Bitki, Alg, Öglena, Siyanobakteri)", [
            "• Enerji kaynağı: IŞIK ENERJİSİ",
            "• Klorofil pigmenti şarttır",
            "• Yalnızca ışık varlığında (gündüz) gerçekleşir",
            "• Hem prokaryot hem ökaryot canlılarda görülür",
            "• Atmosfere bol miktarda O₂ kazandırır"
        ], "#16a34a", "#f0fdf4")
        + _kart(355, 42, 300, 145, "Kemosentez (Nitrit, Nitrat, Kükürt, Demir Bakt.)", [
            "• Enerji kaynağı: İNORGANİK MADDE OKSİDASYONU",
            "  (NH₃, NO₂⁻, H₂S, Fe²⁺, H₂ oksitlenerek enerji üretilir)",
            "• Klorofil ve ışık GEREKMEZ; gece-gündüz 24 saat sürer",
            "• YALNIZCA bazı prokaryotlarda (bakteri ve arkeler) görülür",
            "• Madde döngülerinde (Azot döngüsü) hayati rol oynar"
        ], "#ea580c", "#fff7ed")
    )
    return _svg(680, 200, ic)


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
