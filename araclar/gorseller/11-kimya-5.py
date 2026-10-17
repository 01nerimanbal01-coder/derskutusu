def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">BAĞ KIRILMASI VE BAĞ OLUŞUMUNDA ENERJİ DEĞİŞİMİ</text>'
    ic += _kart(20, 44, 310, 190, "BAĞ KIRILMASI (ENDOTERMİK OLAY)", [
        "• Gaz fazındaki bir molekülde 1 mol kovalent bağı",
        "  kırmak için dışarıdan enerji (ısı) verilmelidir.",
        "• Örnek: H₂(g) + 436 kJ/mol  ->  2H(g)  (ΔH = +436 kJ)",
        "• Örnek: O₂(g) + 498 kJ/mol  ->  2O(g)  (ΔH = +498 kJ)",
        "• Bağ enerjisi ne kadar büyükse bağ o kadar sağlam",
        "  ve molekül o kadar kararlıdır."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "BAĞ OLUŞUMU (EKZOTERMİK OLAY)", [
        "• Gaz halindeki serbest atomlar kararlı hale geçmek",
        "  için aralarında kimyasal bağ kurarken ısı açığa çıkar.",
        "• Örnek: 2H(g)  ->  H₂(g) + 436 kJ/mol  (ΔH = -436 kJ)",
        "• Örnek: 2N(g)  ->  N₂(g) + 946 kJ/mol  (ΔH = -946 kJ)",
        "• Aynı iki atom arasındaki bağ sayısı arttıkça",
        "  (C-C &lt; C=C &lt; C≡C) bağ kısalır ve bağ enerjisi artar."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">BAĞ ENERJİLERİYLE TEPKİME ENTALPİSİNİN HESAPLANMASI</text>'
    ic += _kart(20, 44, 640, 190, "ΔH°_tepkime = Σ ΔH(Kırılan Bağlar)  -  Σ ΔH(Oluşan Bağlar)", [
        "• Tepkimeye giren taneciklerdeki bağlar KIRILIR (+, endotermik); ürünlerdeki bağlar OLUŞUR (-, ekzotermik).",
        "• Formül: ΔH° = [ Girenlerdeki kırılan bağ enerjileri toplamı ] - [ Ürünlerdeki oluşan bağ enerjileri toplamı ]",
        "• EĞER Σ(Kırılan) &gt; Σ(Oluşan) ise ΔH &gt; 0 (Tepkime endotermiktir).",
        "• EĞER Σ(Oluşan) &gt; Σ(Kırılan) ise ΔH &lt; 0 (Tepkime ekzotermiktir).",
        "• Örnek: H₂(g) + Cl₂(g) -> 2HCl(g) tepkimesinde (H-H: 436, Cl-Cl: 242, H-Cl: 431 kJ/mol):",
        "  ΔH° = (1·436 + 1·242) - (2·431) = 678 - 862 = -184 kJ bulunur."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">STANDART MOLAR OLUŞUM ENTALPİSİ (ΔH°f) KURALLARI</text>'
    ic += _kart(20, 44, 310, 190, "STANDART KOŞULLAR VE TANIM", [
        "• Standart koşullar: 25 °C (298 K) sıcaklık ve 1 atm basınç.",
        "• 1 mol bileşiğin, standart şartlarda kendi elementlerinin",
        "  en kararlı allotroplarından oluşması sırasındaki ısı",
        "  değişimine Standart Molar Oluşum Entalpisi (ΔH°f) denir.",
        "• Örnek: C(grafit) + O₂(g) -> CO₂(g)  ΔH°f = -393,5 kJ/mol.",
        "• CO(g) + 1/2 O₂(g) -> CO₂(g) tepkimesi ΔH°f DEĞİLDİR",
        "  (çünkü girenlerde element değil CO bileşiği vardır!)."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "KARARLI ELEMENTLERDE ΔH°f = 0 KURALI", [
        "• Standart şartlarda (25 °C, 1 atm) doğadaki en kararlı",
        "  fiziksel halinde bulunan elementlerin oluşum entalpisi",
        "  SIFIR kabul edilir: ΔH°f = 0 kJ/mol.",
        "• Örnek (ΔH°f = 0 olanlar): H₂(g), O₂(g), N₂(g), Fe(k),",
        "  Hg(s), Br₂(s), I₂(k), C(grafit).",
        "• Kararsız allotrop veya farklı fiziksel hallerde sıfır",
        "  değildir: O₃(g) ≠ 0, C(elmas) ≠ 0, H₂O(g) ≠ H₂O(s)."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">OLUŞUM ENTALPİLERİYLE TEPKİME ENTALPİSİ HESABI</text>'
    ic += _kart(20, 44, 640, 190, "ΔH°_tepkime = Σ n · ΔH°f(Ürünler)  -  Σ m · ΔH°f(Girenler)", [
        "• DİKKAT: Bağ enerjisinde (Kırılan/Giren - Oluşan/Ürün) alınırken, oluşum entalpisinde (ÜRÜNLER - GİRENLER) alınır!",
        "• Denkleştirilmiş tepkimede her maddenin ΔH°f değeri kendi stokiyometrik katsayısıyla (mol sayısıyla) çarpılır.",
        "• Tepkimede yer alan kararlı elementlerin (O₂(g), N₂(g), Al(k) vb.) ΔH°f değeri 0 alınır.",
        "• Örnek: CH₄(g) + 2O₂(g) -> CO₂(g) + 2H₂O(s) tepkimesinde:",
        "  ΔH°_tepkime = [ 1·ΔH°f(CO₂) + 2·ΔH°f(H₂O) ] - [ 1·ΔH°f(CH₄) + 2·0 ]"
    ], "#0891B2", "#ECFEFF")
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
