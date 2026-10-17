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
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Mol Kavramı Dönüşüm Köprüsü: Tanecik Sayısı - Kütle - Gaz Hacmi</text>'
        + _kart(20, 42, 200, 142, "1. Tanecik Sayısı - Mol", [
            "• n = N / N_A",
            "• N: Tanecik sayısı",
            "• N_A: Avogadro sayısı",
            "  (6,02 . 10²³ tanecik/mol)",
            "• 1 mol = N_A tane tanecik"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. Kütle - Mol Bağıntısı", [
            "• n = m / M_A",
            "• m: Maddenin kütlesi (g)",
            "• M_A: Mol kütlesi (g/mol)",
            "• 1 tanecik kütlesi = M_A akb",
            "• 1 g = N_A akb"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 142, "3. Gaz Hacmi - Mol (Avogadro)", [
            "• Normal Koşullar (NK: 0°C, 1 atm):",
            "  n = V / 22,4  (1 mol gaz = 22,4 L)",
            "• Oda Koşulları (OK: 25°C, 1 atm):",
            "  n = V / 24,5  (1 mol gaz = 24,5 L)",
            "• YALNIZCA GAZLAR için geçerlidir!"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        '1 Mol Bileşikte Atom-Mol ve Kütlece Yüzde Analizi: 1 Mol H₂SO₄ Örneği</text>'
        + _kart(25, 42, 300, 145, "Tanecik ve Atom Mol Sayısı Analizi", [
            "• 1 mol H₂SO₄ bileşiği (Toplam 7 mol atom içerir):",
            "• 2 mol H atomu (2 . N_A tane H atomu)",
            "• 1 mol S atomu (1 . N_A tane S atomu)",
            "• 4 mol O atomu (4 . N_A tane O atomu)",
            "• Toplam 7 . N_A tane atom; 1 . N_A tane molekül"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Kütle Dağılımı Analizi (H=1, S=32, O=16)", [
            "• 1 mol H₂SO₄ kütlesi (M_A) = 98 gram/mol",
            "• İçindeki H kütlesi: 2 . 1 = 2 gram",
            "• İçindeki S kütlesi: 1 . 32 = 32 gram",
            "• İçindeki O kütlesi: 4 . 16 = 64 gram",
            "• 1 tane H₂SO₄ molekülü = 98 akb = 98 / N_A gram"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Normal Koşullar (0°C, 1 atm) ve Oda Koşulları (25°C, 1 atm) Karşılaştırması</text>'
        + _kart(25, 42, 300, 142, "Normal Koşullar (NŞA / NK: 0°C, 1 atm)", [
            "• 1 mol ideal gaz = 22,4 Litre hacim kaplar",
            "• 0,5 mol N₂ gazı = 11,2 L  |  0,25 mol CH₄ = 5,6 L",
            "• Dikkat: H₂O (su) 0°C’de katı/sıvı olduğu için",
            "  1 mol H₂O(s) NK’de 22,4 L hacim KAPLAMAZ!",
            "• Gaz yoğunluğu: d = M_A / 22,4 (g/L)"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 142, "Standart (Oda) Koşulları (OK: 25°C, 1 atm)", [
            "• 1 mol ideal gaz = 24,5 Litre hacim kaplar",
            "• 0,2 mol He gazı = 4,9 L  |  2 mol CO₂ = 49 L",
            "• Avogadro Yasası: Aynı sıcaklık ve basınçta eşit",
            "  hacimli gazlarda eşit sayıda molekül (mol) vardır",
            "• Gaz yoğunluğu: d = M_A / 24,5 (g/L)"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Gaz Karışımlarında ve İzotop Atomlarda Mol Problemleri</text>'
        + _kart(25, 42, 300, 138, "Karışım Problemleri Çözüm Adımları", [
            "• 1. Bileşenlerin mol sayılarına x mol ve y mol denir",
            "• 2. Toplam mol: x + y = n_toplam denklemi kurulur",
            "• 3. Toplam kütle veya toplam atom mol sayısı için",
            "  ikinci denklem kurulup iki bilinmeyenli sistem çözülür"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Ortalama Atom Kütlesi (İzotoplar)", [
            "• Doğada birden fazla izotopu bulunan elementlerin",
            "  mol kütlesi bolluk yüzdeleriyle ağırlıklı hesaplanır:",
            "• Ort. A.K. = (A₁ . %Bolluk₁ + A₂ . %Bolluk₂) / 100",
            "• Örn: ³⁵Cl (%75) ve ³⁷Cl (%25) -> M_A = 35,5 g/mol"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


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
