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
        'Newton’ın Üç Temel Hareket Yasası</text>'
        + _kart(18, 42, 205, 145, "1. Eylemsizlik Yasası", [
            "• Net kuvvet sıfır ise (F_net = 0)",
            "  cismin ivmesi sıfırdır (a = 0).",
            "• Duran cisim durmaya devam eder.",
            "• Hareketli cisim sabit hızla",
            "  düzgün doğrusal hareket yapar."
        ], "#2563eb", "#eff6ff")
        + _kart(237, 42, 205, 145, "2. Dinamiğin Temel Yasası", [
            "• Net kuvvet sıfırdan farklı ise",
            "  cisim ivmeli hareket yapar.",
            "• Bağıntı: F_net = m . a",
            "• İvme vektörü her zaman net",
            "  kuvvet vektörü ile aynı yönlüdür."
        ], "#059669", "#ecfdf5")
        + _kart(456, 42, 205, 145, "3. Etki - Tepki Yasası", [
            "• Her etkiye karşılık eşit büyüklükte",
            "  ve zıt yönde bir tepki vardır.",
            "• Bağıntı: F_etki = -F_tepki",
            "• Farklı cisimler üzerine etki eder;",
            "  birbirini dengelemez!"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 202, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Serbest Cisim Diyagramı (SCD) ve Kuvvet Analizi</text>'
        '<line x1="35" y1="145" x2="295" y2="145" stroke="#475569" stroke-width="2.5"/>'
        '<rect x="125" y="95" width="70" height="50" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
        '<text x="160" y="125" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">m</text>'
        '<line x1="160" y1="95" x2="160" y2="45" stroke="#059669" stroke-width="2.5"/>'
        '<polygon points="160,38 155,48 165,48" fill="#059669"/>'
        '<text x="172" y="55" font-family="sans-serif" font-size="12" font-weight="bold" fill="#059669">N (Normal)</text>'
        '<line x1="160" y1="145" x2="160" y2="190" stroke="#dc2626" stroke-width="2.5"/>'
        '<polygon points="160,197 155,187 165,187" fill="#dc2626"/>'
        '<text x="172" y="188" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">G = m.g</text>'
        '<line x1="195" y1="120" x2="265" y2="120" stroke="#2563eb" stroke-width="2.5"/>'
        '<polygon points="272,120 262,115 262,125" fill="#2563eb"/>'
        '<text x="235" y="112" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2563eb">F (Uygulanan)</text>'
        '<line x1="125" y1="140" x2="65" y2="140" stroke="#d97706" stroke-width="2.5"/>'
        '<polygon points="58,140 68,135 68,145" fill="#d97706"/>'
        '<text x="85" y="132" font-family="sans-serif" font-size="12" font-weight="bold" fill="#d97706" text-anchor="middle">f_s</text>'
        + _kart(320, 42, 340, 148, "Serbest Cisim Diyagramı Kuralları", [
            "• Yalnızca cisme dışarıdan etki eden kuvvetler çizilir.",
            "• Düşey denge: N - m.g = 0  =>  N = m.g",
            "• Yatay net kuvvet: F_net = F - f_s = m . a",
            "• Sürtünme kuvveti: f_s = k . N",
            "• m.a (eylemsizlik) bir kuvvet değildir, SCD’de gösterilmez!"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 205, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Eğik Düzlem ve Birbirine Bağlı Cisimlerde Dinamik</text>'
        + _kart(25, 42, 300, 145, "Eğik Düzlemde Kuvvet Bileşenleri", [
            "• Ağırlık (G = m.g) iki dik bileşene ayrılır:",
            "• Eğik düzleme paralel bileşen: G_x = m.g.sin α",
            "• Eğik düzleme dik bileşen: G_y = m.g.cos α",
            "• Yüzeyin normal kuvveti: N = m.g.cos α",
            "• Sürtünmesiz eğik düzlem ivmesi: a = g . sin α"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "Bağlı Cisimler ve Atwood Düzeneği", [
            "• İple bağlı cisimler aynı büyüklükte ivmeyle hareket eder.",
            "• Sistem ivmesi: a = F_net(sistem) / m_toplam",
            "• İp gerilmesi (T), tek bir cismin serbest cisim",
            "  diyagramında F_net = m . a yazılarak bulunur.",
            "• Aynı ipteki gerilme kuvveti her noktada eşittir."
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
