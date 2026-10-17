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
        'GERÇEK SAYI DİZİLERİ: TANIM KÜMESİ VE GENEL TERİM (a_n)</text>'
    )
    ic += _kart(20, 44, 310, 190, "DİZİ TANIMI (f: Z+ -> R)", [
        "• Tanım kümesi pozitif tam sayılar kümesi",
        "  Z+ = {1, 2, 3, ..., n, ...} olan her fonksiyona",
        "  'Gerçek Sayı Dizisi' denir.",
        "• f(n) = a_n dizinin 'n. terimi' veya 'genel terimi'dir.",
        "• (a_n) = (a_1, a_2, a_3, ..., a_n, ...) şeklinde yazılır.",
        "• DİKKAT: n yerine yalnızca 1, 2, 3, ... pozitif tam",
        "  sayıları yazılabilir (0, negatif veya kesir yazılamaz!)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "HANGİ İFADELER DİZİ BELİRTMEZ?", [
        "• Paydayı pozitif bir tam sayıda sıfır yapan ifadeler:",
        "  Örn: a_n = (2n + 1) / (n - 4) -> n = 4 için tanımsız!",
        "• Çift dereceli kök içini pozitif tam sayıda negatif",
        "  yapan ifadeler: Örn: b_n = Kök(5 - n) -> n = 6 için",
        "  gerçek sayı değil (ancak 5 elemanlı sonlu dizi olabilir).",
        "• Logaritma içini n eleman Z+ için 0 veya negatif",
        "  yapan ifadeler sonsuz gerçek sayı dizisi belirtmez."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SONLU DİZİ, SABİT DİZİ VE EŞİT DİZİLER</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. SONLU DİZİ", [
        "• Tanım kümesi A_k = {1, 2, ..., k}",
        "  olan k elemanlı dizidir.",
        "• f: A_k -> R",
        "• Örn: a_n = Kök(6 - n) ifadesi",
        "  en çok 6 elemanlı (A_6) bir",
        "  sonlu dizi belirtebilir",
        "  (n = 1, 2, 3, 4, 5, 6)."
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "2. SABİT DİZİ", [
        "• Bütün terimleri birbirine",
        "  eşit olan dizidir: a_n = c.",
        "• Kesirli rasyonel dizide:",
        "  a_n = (p.n + r) / (s.n + t)",
        "  sabit dizi ise katsayılar",
        "  oranı birbirine eşittir:",
        "  p / s = r / t = a_n."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. EŞİT DİZİLER", [
        "• Her n eleman Z+ için",
        "  a_n = b_n oluyorsa",
        "  (a_n) = (b_n) denir.",
        "• Örn: a_n = (-1)^(2n) = 1",
        "  ve b_n = cos(2.n.pi) = 1",
        "  dizileri birbirine eşittir.",
        "• Sıralı her terim aynıdır."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'İNDİRGEMELİ DİZİLER VE İLK n TERİM TOPLAMI (S_n) İLİŞKİSİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "İNDİRGEMELİ (ÖZYİNELEMELİ) DİZİLER", [
        "• Herhangi bir terimi kendisinden önceki bir veya",
        "  birkaç terim cinsinden tanımlanan dizilerdir.",
        "• Örn: a_1 = 3 ve a_(n+1) = a_n + 4 bağlantısında",
        "  n = 1, 2, ..., (k-1) yazılıp taraf tarafa toplanarak",
        "  teleskopik sadeleştirme ile k. terim bulunur.",
        "• Çarpım biçimindeyse: a_(n+1) = n . a_n ifadesinde",
        "  taraf tarafa ÇARPILARAK genel terime ulaşılır."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "İLK n TERİM TOPLAMI (S_n) VE a_n BAĞINTISI", [
        "• S_n = a_1 + a_2 + ... + a_(n-1) + a_n",
        "• S_(n-1) = a_1 + a_2 + ... + a_(n-1)",
        "• Taraf tarafa çıkarılırsa ALTIN FORMÜL elde edilir:",
        "  a_n = S_n - S_(n-1)   (n &gt;= 2 için)",
        "  a_1 = S_1",
        "• Örn: S_n = n^2 + 2n ise a_5 = S_5 - S_4",
        "  a_5 = (25 + 10) - (16 + 8) = 35 - 24 = 11."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ÖZEL SAYI DİZİLERİ: ÜÇGENSEL, KARESEL VE FİBONACCİ DİZİSİ</text>'
    )
    diziler = [
        ("ÜÇGENSEL SAYI DİZİSİ", "Genel terimi a_n = n.(n + 1) / 2 olan dizidir: (1, 3, 6, 10, 15, 21, 28, ...). 1'den n'ye kadar ardışık toplam.", "#2563EB", "#EFF6FF"),
        ("KARESEL SAYI DİZİSİ", "Genel terimi a_n = n^2 olan dizidir: (1, 4, 9, 16, 25, 36, ...). Ardışık iki üçgensel sayının toplamı karesel sayıdır!", "#059669", "#ECFDF5"),
        ("FİBONACCİ SAYI DİZİSİ", "F_1 = 1, F_2 = 1 ve F_(n+2) = F_(n+1) + F_n kuralıyla oluşan dizidir: (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...).", "#7C3AED", "#F5F3FF"),
        ("PARÇALI DİZİLER", "n'nin tek veya çift olmasına (ya da mod değerine) göre farklı kurallarla tanımlanan dizilerdir.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(diziler):
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
