def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Mol Kavramı ve Avogadro Sayısı (NA) (10.1.4)</text>'
    c += _kart(18, 54, 314, 175, "Günlük Hayattan Kimyaya Sayma Birimleri", [
        "• 1 çift = 2 adet  |  1 düzine = 12 adet",
        "• Atom ve moleküller çok küçük olduğu için",
        "  tek tek sayılamaz; \'mol\' paketiyle ifade edilir.",
        "• 1 mol = 6,02 × 10²³ adet tanecik içerir.",
        "• Bu sayıya Avogadro Sayısı (NA veya N0) denir."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 175, "1 Mol Taneciğin Operasyonel Tanımı", [
        "• Standart referans izotop: Karbon-12 (¹²C).",
        "• Tam 12 gram ¹²C izotopunun içerdiği atom",
        "  sayısı kadar (6,02 × 10²³ tane) tanecik içeren",
        "  madde miktarına 1 MOL denir.",
        "• Mol sayısı \'n\' sembolü ile gösterilir."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Bağıl Atom Kütlesi, Atomik Kütle Birimi (akb) ve Mol Kütlesi (MA)</text>'
    c += _kart(18, 54, 314, 175, "Atomik Kütle Birimi (akb / u)", [
        "• 1 tane ¹²C atomunun kütlesinin 1/12\'sine",
        "  1 atomik kütle birimi (1 akb) denir.",
        "• 1 tane ¹⁶O atomunun kütlesi = 16 akb\'dir.",
        "• 1 tane H2O molekülünün kütlesi = 18 akb\'dir.",
        "• Dönüşüm: 1 gram = NA akb = 6,02 × 10²³ akb!"
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 175, "Mol Kütlesi (MA — g/mol)", [
        "• 1 mol (6,02 × 10²³ tane) maddenin gram",
        "  cinsinden kütlesine MOL KÜTLESİ (MA) denir.",
        "• 1 mol O atomu = 16 g/mol",
        "• 1 mol H2O molekülü = 2(1) + 16 = 18 g/mol",
        "• 1 mol CaCO3 = 40 + 12 + 3(16) = 100 g/mol."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Mol Sayısı (n), Kütle (m) ve Tanecik Sayısı (N) Dönüşüm Bağıntıları</text>'
    c += _kart(18, 54, 314, 170, "1. Tanecik Sayısı İle Mol İlişkisi", [
        "• n = N / NA",
        "  (Mol sayısı = Tanecik sayısı / Avogadro sayısı)",
        "• N = n · NA",
        "• Örnek: 3,01 × 10²³ tane He atomu",
        "  n = (3,01 × 10²³) / (6,02 × 10²³) = 0,5 moldür."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 170, "2. Kütle İle Mol İlişkisi", [
        "• n = m / MA",
        "  (Mol sayısı = Verilen kütle [g] / Mol kütlesi [g/mol])",
        "• m = n · MA",
        "• Örnek: 0,5 mol H2O (MA = 18 g/mol) kütlesi",
        "  m = 0,5 · 18 = 9 gramdır."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#2874a6"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Bileşiklerin 1 Molündeki Atom Mol Sayısı Analizi</text>'
    c += _kart(18, 54, 314, 165, "1 Mol CH4 (Metan) Molekülü Analizi", [
        "• 1 mol (NA tane) CH4 molekülü içerir.",
        "• 1 mol C atomu (12 gram) içerir.",
        "• 4 mol H atomu (4 gram) içerir.",
        "• Toplam 1 + 4 = 5 mol (5·NA tane) atom içerir.",
        "• Toplam kütlesi MA = 12 + 4 = 16 gramdır."
    ], "#2874a6", "#eaf2f8")
    c += _kart(348, 54, 314, 165, "Aynı Sayıda Tanecik İçeren Örnekler", [
        "• Eşit molde alınan farklı maddelerin içerdiği",
        "  molekül sayıları eşittir ancak kütleleri farklıdır!",
        "• Örn: 1 mol H2 = 2 g iken 1 mol O2 = 32 gramdır;",
        "  kütle oranı (2/32 = 1/16) doğrudan taneciklerin",
        "  bağıl kütleleri oranına eşittir."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
