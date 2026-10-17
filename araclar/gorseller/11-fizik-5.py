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
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">NEWTON\'IN HAREKET YASALARI (DİNAMİĞİN TEMEL İLKELERİ)</text>'
    ic += _kart(20, 44, 205, 190, "1. EYLEMSİZLİK YASASI", [
        "• Net kuvvet sıfır ise:",
        "  ΣF = 0  =>  a = 0",
        "• Duran cisim durmaya",
        "  devam eder (v = 0).",
        "• Hareketli cisim sabit",
        "  hızla (düzgün doğrusal)",
        "  hareketini sürdürür.",
        "• Kütle, eylemsizliğin ölçüsüdür."
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "2. TEMEL YASA (Fnet = m·a)", [
        "• Net kuvvet sıfırdan farklı",
        "  ise cisim ivmeli hareket",
        "  yapar: Fnet = m · a",
        "• İvme (a), net kuvvetle",
        "  aynı yönlü ve doğru",
        "  orantılıdır.",
        "• Sabit kuvvette ivme,",
        "  kütle ile ters orantılıdır."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. ETKİ-TEPKİ YASASI", [
        "• Her etki kuvvetine eşit",
        "  büyüklükte ve zıt yönde",
        "  bir tepki kuvveti vardır:",
        "  F₁₂ = -F₂₁",
        "• Etki ve tepki kuvvetleri",
        "  FARKLI cisimler üzerindedir.",
        "• Bu nedenle birbirini",
        "  dengelemez (bileşkesi alınmaz)."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SERBEST CİSİM DİYAGRAMI (SCD) VE TEMEL KUVVETLER</text>'
    ic += _kart(20, 44, 310, 190, "SERBEST CİSİM DİYAGRAMI KURALLARI", [
        "• Cisim noktasal bir kütle veya sade bir kutu olarak",
        "  temsil edilir; çevre nesnelerden soyutlanır.",
        "• Sadece CİSMİN KENDİSİNE etki eden dış kuvvet",
        "  vektörleri (G, N, F, T, fs) diyagramda gösterilir.",
        "• Cismin başka yüzeylere uyguladığı etki kuvvetleri",
        "  veya m·a (net kuvvet) ayrı bir vektör olarak çizilmez."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "YATAY VE EĞİK DÜZLEMDE KUVVETLER", [
        "• Ağırlık (G = m·g): Daima yerin merkezine (düşey",
        "  aşağı) doğrudur.",
        "• Normal Kuvvet (N): Yüzeyin cisme dik olarak",
        "  uyguladığı tepki kuvvetidir (Yatayda N = m·g).",
        "• Eğik düzlemde (eğim α): Yüzeye paralel bileşen",
        "  Gx = m·g·sinα; yüzeye dik bileşen Gy = m·g·cosα."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">EĞİK DÜZLEM VE BİRBİRİNE BAĞLI CİSİM SİSTEMLERİ</text>'
    adimlar = [
        ("1. SÜRTÜNMESİZ EĞİK DÜZLEMDE İVME", "Eğik düzlemdeki cismi aşağı çeken net kuvvet Fnet = m·g·sinα olduğundan ivme kütleden bağımsızdır: a = g·sinα.", "#059669", "#ECFDF5"),
        ("2. SÜRTÜNMELİ YATAY DÜZLEMDE HAREKET", "Yatay F kuvvetiyle çekilen cisimde fs = k·m·g sürtünmesi varsa: Fnet = F - k·m·g = m·a bağıntısı uygulanır.", "#2563EB", "#EFF6FF"),
        ("3. İPLE BAĞLI CİSİMLERDE SİSTEM İVMESİ", "Birlikte hareket eden cisimlerin ivme büyüklüğü ortaktır: a_sistem = Fnet_toplam / m_toplam.", "#7C3AED", "#F5F3FF"),
        ("4. İP GERİLMESİ (T) HESABI", "Sistem ivmesi bulunduktan sonra tek bir cisim için serbest cisim diyagramı yazılıp T gerilmesi hesaplanır.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">ATWOOD ALETİ VE MAKARA SİSTEMLERİNDE DİNAMİK ANALİZ</text>'
    ic += _kart(20, 44, 310, 190, "SABİT MAKARADA İKİ KÜTLE (m₁ &gt; m₂)", [
        "• Sürtünmesiz sabit makaraya asılı m₁ ve m₂ kütleli",
        "  cisimlerden m₁ &gt; m₂ ise sistem m₁ yönünde ivmelenir.",
        "• Net kuvvet: Fnet = m₁·g - m₂·g = (m₁ - m₂)·g",
        "• Sistemin ortak ivmesi:",
        "  a = [(m₁ - m₂) / (m₁ + m₂)] · g",
        "• İp gerilmesi T, m₂·g den büyük, m₁·g den küçüktür."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "MASA ÜZERİNDEKİ CİSİM VE SARKAN KÜTLE", [
        "• Sürtünmesiz yatay masadaki m₁ kütlesi, makaradan",
        "  sarkan m₂ kütlesine iple bağlı olsun.",
        "• Sistemi harekete geçiren net kuvvet sarkan cismin",
        "  ağırlığıdır: Fnet = m₂·g",
        "• Ortak ivme: a = (m₂·g) / (m₁ + m₂)",
        "• Yataydaki m₁ cismi için ip gerilmesi: T = m₁ · a."
    ], "#059669", "#ECFDF5")
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
