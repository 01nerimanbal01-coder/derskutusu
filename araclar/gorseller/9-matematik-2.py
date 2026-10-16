from ozet_gorsel import svg


def g1():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">ÜSLÜ VE KÖKLÜ GÖSTERİMLERİN DÖNÜŞÜMÜ</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">Rasyonel Üs ↔ Kök</text>',
        '<text x="166" y="108" text-anchor="middle" font-size="13" font-weight="600" fill="#334155">x^(m/n) = ⁿ√(x^m)</text>',
        '<text x="166" y="132" text-anchor="middle" font-size="12" fill="#334155">• 2^(3/2) = √(2³) = √8</text>',
        '<text x="166" y="150" text-anchor="middle" font-size="12" fill="#334155">• 5^(2/3) = ³√(5²) = ³√25</text>',
        '<text x="166" y="168" text-anchor="middle" font-size="12" fill="#334155">• ⁶√(5⁴) = 5^(4/6) = ³√25</text>',
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">Tek ve Çift Derece Kuralı</text>',
        '<text x="453" y="108" text-anchor="middle" font-size="12.5" font-weight="600" fill="#334155">ⁿ√(a^n) İfadesinin Değeri:</text>',
        '<text x="453" y="132" text-anchor="middle" font-size="12" fill="#334155">• n tek ise: ⁿ√(a^n) = a</text>',
        '<text x="453" y="150" text-anchor="middle" font-size="12" fill="#334155">• n çift ise: ⁿ√(a^n) = |a|</text>',
        '<text x="453" y="168" text-anchor="middle" font-size="12" fill="#334155">• Örnek: ³√(-27) = -3, ⁴√16 = 2</text>',
    ]
    return svg(w, h, "".join(ic), "Üslü ve köklü gösterimlerin dönüşümü ve tek-çift derece kuralı")


def g2():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">KÖKLÜ İFADELERDE DÖRT İŞLEM VE KÖKÜN KÖKÜ</text>',
        '<rect x="30" y="60" width="180" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="120" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">Toplama ve Çıkarma</text>',
        '<text x="120" y="108" text-anchor="middle" font-size="12" fill="#334155">Derece ve kök içi</text>',
        '<text x="120" y="126" text-anchor="middle" font-size="12" fill="#334155">aynı olmalıdır:</text>',
        '<text x="120" y="148" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">4³√5 + 2³√5 = 6³√5</text>',
        '<rect x="220" y="60" width="180" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">Çarpma ve Bölme</text>',
        '<text x="310" y="108" text-anchor="middle" font-size="12" fill="#334155">Eşit derecede ortak</text>',
        '<text x="310" y="126" text-anchor="middle" font-size="12" fill="#334155">kök içine alınır:</text>',
        '<text x="310" y="148" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">ⁿ√x · ⁿ√y = ⁿ√(x·y)</text>',
        '<rect x="410" y="60" width="180" height="128" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="500" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#a16207">Kökün Kökü</text>',
        '<text x="500" y="108" text-anchor="middle" font-size="12" fill="#334155">İç içe köklerde</text>',
        '<text x="500" y="126" text-anchor="middle" font-size="12" fill="#334155">dereceler çarpılır:</text>',
        '<text x="500" y="148" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">ᵐ√(ⁿ√x) = ᵐ·ⁿ√x</text>',
    ]
    return svg(w, h, "".join(ic), "Köklü ifadelerde toplama, çarpma ve kökün kökü kuralları")


def g3():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">FARKLI DERECELİ KÖKLERDE EŞİTLEME VE SIRALAMA</text>',
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">Çarpma Örneği: ⁶√2 · ³√5</text>',
        '<text x="166" y="110" text-anchor="middle" font-size="12" fill="#334155">1. Dereceler 6’da eşitlenir:</text>',
        '<text x="166" y="128" text-anchor="middle" font-size="12" fill="#334155">³√5 = ³·²√(5²) = ⁶√25</text>',
        '<text x="166" y="148" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">2. Sonuç: ⁶√2 · ⁶√25 = ⁶√50</text>',
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="454" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#7e22ce">Sıralama: a=³√3, b=⁶√2, c=⁹√7</text>',
        '<text x="454" y="110" text-anchor="middle" font-size="12" fill="#334155">Dereceler 18’de eşitlenir:</text>',
        '<text x="454" y="128" text-anchor="middle" font-size="12" fill="#334155">a = ¹⁸√729, b = ¹⁸√8, c = ¹⁸√49</text>',
        '<text x="454" y="148" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">Sıralama: b &lt; c &lt; a</text>',
    ]
    return svg(w, h, "".join(ic), "Kök dereceleri farklı olan ifadelerde çarpma ve sıralama")


def g4():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">PAYDAYI RASYONEL YAPMA (EŞLENİK İLE ÇARPMA)</text>',
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="166" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">Tek Terimli Payda: 1 / √a</text>',
        '<text x="166" y="110" text-anchor="middle" font-size="12" fill="#334155">Pay ve payda √a ile çarpılır:</text>',
        '<text x="166" y="130" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">1 / √3 = √3 / (√3 · √3) = √3 / 3</text>',
        '<text x="166" y="152" text-anchor="middle" font-size="12" fill="#334155">Payda rasyonel sayıya dönüşür.</text>',
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="454" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#be123c">İki Terimli Payda: 1 / (√a − √b)</text>',
        '<text x="454" y="110" text-anchor="middle" font-size="12" fill="#334155">Eşleniği (√a + √b) ile çarpılır:</text>',
        '<text x="454" y="130" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">1 / (√5 − √2) = (√5 + √2) / 3</text>',
        '<text x="454" y="152" text-anchor="middle" font-size="12" fill="#334155">İki kare farkı: (√a)² − (√b)² = a − b</text>',
    ]
    return svg(w, h, "".join(ic), "Köklü ifadelerde eşlenik ve paydayı rasyonel yapma")


def uygula(v):
    b = v["bolumler"]
    b[1]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[3]["gorsel"] = g3()
    b[4]["gorsel"] = g4()
