from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Yatay Düzlemde Düzgün Çembersel Hareket ve Serbest Cisim Diyagramı</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">1. Sürtünmesiz Yatay Düzlem (İpli)</text>
    <line x1="55" y1="185" x2="315" y2="185" stroke="#64748b" stroke-width="2"/>
    <circle cx="95" cy="185" r="5" fill="#1e293b"/>
    <text x="95" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">O</text>
    <line x1="95" y1="185" x2="235" y2="185" stroke="#2563eb" stroke-width="2.5"/>
    <rect x="235" y="167" width="36" height="36" rx="6" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
    <text x="253" y="190" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">m</text>
    <line x1="253" y1="167" x2="253" y2="125" stroke="#16a34a" stroke-width="2.5"/>
    <text x="268" y="135" font-size="12" font-weight="bold" fill="#15803d">N</text>
    <line x1="253" y1="203" x2="253" y2="245" stroke="#dc2626" stroke-width="2.5"/>
    <text x="275" y="242" font-size="12" font-weight="bold" fill="#b91c1c">m·g</text>
    <text x="165" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">← T = Fm</text>
    <text x="185" y="260" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af">N = m·g   ve   T = Fm = m·v²/r = m·ω²·r</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#15803d">2. Sürtünmeli Döner Tabla Üzeri</text>
    <line x1="405" y1="185" x2="665" y2="185" stroke="#64748b" stroke-width="2"/>
    <circle cx="445" cy="185" r="5" fill="#1e293b"/>
    <text x="445" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">O</text>
    <rect x="575" y="167" width="36" height="36" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
    <text x="593" y="190" text-anchor="middle" font-size="12" font-weight="bold" fill="#14532d">m</text>
    <line x1="575" y1="185" x2="510" y2="185" stroke="#ea580c" stroke-width="2.5"/>
    <text x="535" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="#c2410c">← Fs = Fm</text>
    <line x1="593" y1="167" x2="593" y2="125" stroke="#16a34a" stroke-width="2.5"/>
    <text x="608" y="135" font-size="12" font-weight="bold" fill="#15803d">N</text>
    <line x1="593" y1="203" x2="593" y2="245" stroke="#dc2626" stroke-width="2.5"/>
    <text x="615" y="242" font-size="12" font-weight="bold" fill="#b91c1c">m·g</text>
    <text x="535" y="260" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">Fs = Fm = m·ω²·r ≤ k·m·g</text>
    """
    return svg(720, 285, ic, "Yatay Düzlemde Çembersel Hareket ve Serbest Cisim Diyagramı")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Konik Sarkaç (Lunapark Zincirli Salıncağı) ve Aynı İpte İki Cisim</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="185" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">Konik Sarkaç / Zincirli Salıncak</text>
    <line x1="120" y1="115" x2="120" y2="220" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="120" y1="115" x2="220" y2="205" stroke="#6d28d9" stroke-width="2.5"/>
    <line x1="120" y1="205" x2="220" y2="205" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="220" cy="205" r="10" fill="#7c3aed"/>
    <text x="135" y="145" font-size="12" font-weight="bold" fill="#5b21b6">α</text>
    <text x="182" y="155" font-size="12" font-weight="bold" fill="#6d28d9">T (L)</text>
    <text x="170" y="220" text-anchor="middle" font-size="11" fill="#4c1d95">r = L·sinα</text>
    <text x="185" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#4c1d95">Ty = T·cosα = m·g  |  Tx = T·sinα = Fm</text>
    <text x="185" y="258" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">tanα = v² / (g·r) = (ω²·r) / g</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="535" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#9d174d">Aynı İp Üzerinde Dönen K ve L Cisimleri</text>
    <circle cx="415" cy="160" r="5" fill="#1e293b"/>
    <text x="415" y="180" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">O</text>
    <line x1="415" y1="160" x2="535" y2="160" stroke="#db2777" stroke-width="2.5"/>
    <circle cx="535" cy="160" r="12" fill="#f472b6" stroke="#9d174d" stroke-width="2"/>
    <text x="535" y="164" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">K</text>
    <line x1="547" y1="160" x2="645" y2="160" stroke="#db2777" stroke-width="2.5"/>
    <circle cx="645" cy="160" r="12" fill="#be185d" stroke="#831843" stroke-width="2"/>
    <text x="645" y="164" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">L</text>
    <text x="475" y="148" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">T₁ (rK)</text>
    <text x="595" y="148" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">T₂ (rL)</text>
    <text x="535" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#831843">Açısal hızlar eşittir: ωK = ωL = ω</text>
    <text x="535" y="230" text-anchor="middle" font-size="12" fill="#831843">• Dış ip: T₂ = FL = mL · ω² · rL</text>
    <text x="535" y="252" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">• İç ip: T₁ = T₂ + FK = T₂ + mK · ω² · rK</text>
    """
    return svg(720, 285, ic, "Konik Sarkaç ve Aynı İpte Dönen Cisimlerin İp Gerilmeleri")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#991b1b"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Düşey Düzlemde Düzgün Çembersel Harekette İp Gerilmesi Analizi</text>

    <rect x="25" y="75" width="280" height="195" rx="12" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <circle cx="165" cy="172" r="68" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>
    <circle cx="165" cy="172" r="4" fill="#1e293b"/>
    <text x="152" y="176" font-size="11" font-weight="bold" fill="#1e293b">O</text>
    <circle cx="165" cy="104" r="9" fill="#ef4444"/>
    <text x="165" y="90" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Üst (Tmin)</text>
    <circle cx="165" cy="240" r="9" fill="#b91c1c"/>
    <text x="165" y="262" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">Alt (Tmax)</text>
    <circle cx="97" cy="172" r="9" fill="#f97316"/>
    <text x="72" y="176" text-anchor="middle" font-size="11" font-weight="bold" fill="#c2410c">K</text>
    <circle cx="215" cy="218" r="9" fill="#0d9488"/>
    <text x="235" y="225" font-size="11" font-weight="bold" fill="#0f766e">L (θ)</text>
    <line x1="165" y1="172" x2="165" y2="240" stroke="#64748b" stroke-width="1.5"/>
    <line x1="165" y1="172" x2="215" y2="218" stroke="#0d9488" stroke-width="2"/>

    <rect x="325" y="75" width="370" height="195" rx="12" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="510" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">Noktalara Göre Merkezcil Kuvvet ve İp Gerilmesi</text>
    <text x="342" y="128" font-size="12" font-weight="bold" fill="#b91c1c">• En Üst Nokta (En Küçük Gerilme):</text>
    <text x="355" y="146" font-size="12" fill="#7f1d1d">Fm = Tüst + m·g   ⇒   Tüst = Fm − m·g</text>
    <text x="342" y="170" font-size="12" font-weight="bold" fill="#c2410c">• Yatay Hiza K Noktası:</text>
    <text x="355" y="188" font-size="12" fill="#7c2d12">Fm = TK   (m·g merkeze diktir, T'ye katılmaz)</text>
    <text x="342" y="212" font-size="12" font-weight="bold" fill="#15803d">• En Alt Nokta (En Büyük Gerilme):</text>
    <text x="355" y="230" font-size="12" fill="#14532d">Fm = Talt − m·g   ⇒   Talt = Fm + m·g</text>
    <text x="342" y="254" font-size="12" font-weight="bold" fill="#0f766e">• L Noktası: Fm = TL − m·g·cosθ  ⇒  TL = Fm + m·g·cosθ</text>
    """
    return svg(720, 285, ic, "Düşey Düzlemde Çembersel Harekette İp Gerilmeleri")


def _kok_satir(xc, y, parcalar, boyut=14, renk="#065f46"):
    gen = {" ": 0.30, "·": 0.34, "=": 0.58, "/": 0.42, "|": 0.34, "i": 0.32, "n": 0.54, "m": 0.78, "a": 0.52, "x": 0.52, "t": 0.38}
    def mw(s):
        return sum(gen.get(c, 0.55) for c in s) * boyut
    def pw(p):
        if isinstance(p, str):
            return mw(p)
        return boyut * 0.60 + boyut * 0.08 + mw(p[1]) + boyut * 0.10
    toplam = sum(pw(p) for p in parcalar)
    cx = xc - toplam / 2.0
    out = []
    for p in parcalar:
        if isinstance(p, str):
            out.append(f'<text x="{cx:.1f}" y="{y:.1f}" font-size="{boyut}" font-weight="bold" fill="{renk}">{p}</text>')
        else:
            ic = p[1]
            yt = y - boyut * 0.90
            x_ic = cx + boyut * 0.60 + boyut * 0.08
            x_son = x_ic + mw(ic) + boyut * 0.10
            d = (
                f"M{cx:.1f} {y - boyut * 0.30:.1f} "
                f"L{cx + boyut * 0.12:.1f} {y - boyut * 0.38:.1f} "
                f"L{cx + boyut * 0.32:.1f} {y + boyut * 0.10:.1f} "
                f"L{cx + boyut * 0.60:.1f} {yt:.1f} "
                f"H{x_son:.1f}"
            )
            out.append(
                f'<path d="{d}" fill="none" stroke="{renk}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<text x="{x_ic:.1f}" y="{y:.1f}" font-size="{boyut}" font-weight="bold" fill="{renk}">{ic}</text>'
            )
        cx += pw(p)
    return "".join(out)


def gorsel_4():
    f1 = _kok_satir(185, 242, ["vmax = ", ("k", "k · g · r")], 15, "#065f46")
    ic = f"""
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#065f46"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Yatay Zeminde (Virajda) Araçların Emniyetli Dönüş Şartı</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">Yatay Viraj Kuvvet Analizi</text>
    <text x="45" y="130" font-size="12" fill="#064e3b">• Aracı viraj merkezine doğru tutan merkezcil</text>
    <text x="45" y="148" font-size="12" fill="#064e3b">  kuvvet, statik sürtünme kuvvetidir (Fs).</text>
    <text x="45" y="176" font-size="13" font-weight="bold" fill="#047857">• Güvenli dönüş şartı: Fs ≥ Fm</text>
    <text x="45" y="202" font-size="13" font-weight="bold" fill="#065f46">  k · m · g ≥ m · v² / r</text>
    <rect x="45" y="216" width="280" height="40" rx="8" fill="#d1fae5"/>
    {f1}

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">Önemli Fiziksel Sonuçlar</text>
    <text x="395" y="130" font-size="12" font-weight="bold" fill="#92400e">1. Kütleden Bağımsızdır (m sadeleşir):</text>
    <text x="395" y="148" font-size="11" fill="#78350f">• Viraj girişlerinde kamyon, otobüs ve</text>
    <text x="395" y="164" font-size="11" fill="#78350f">  otomobiller için tek bir azami sürat</text>
    <text x="395" y="180" font-size="11" fill="#78350f">  levhası yer alır.</text>
    <text x="395" y="206" font-size="12" font-weight="bold" fill="#92400e">2. Sınır Aşılırsa Ne Olur?</text>
    <text x="395" y="224" font-size="11" fill="#78350f">• v &gt; vmax ise araç virajın dışına savrulur.</text>
    <text x="395" y="244" font-size="11" fill="#78350f">• Buzlu/yağışlı havada k azaldığından</text>
    <text x="395" y="260" font-size="11" font-weight="bold" fill="#b45309">  güvenli dönüş sürati (vmax) düşer!</text>
    """
    return svg(720, 285, ic, "Yatay Zeminde Araçların Emniyetli Dönüş Şartı")


def gorsel_5():
    f1 = _kok_satir(185, 211, ["v = ", ("k", "g · r · tanθ")], 14, "#0f766e")
    f2 = _kok_satir(535, 211, ["vmin = ", ("k", "g·r / k"), "  |  ωmin = ", ("k", "g / k·r")], 12.5, "#1e40af")
    ic = f"""
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Eğimli Virajda ve Düşey Silindirde Emniyetli Dönüş Bağıntıları</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">1. Sürtünmesiz Eğimli Viraj (Veledrom)</text>
    <text x="45" y="128" font-size="12" fill="#134e4a">• Düşey denge: Ny = N · cosθ = m · g</text>
    <text x="45" y="150" font-size="12" fill="#134e4a">• Merkezcil kuvvet: Nx = N · sinθ = m · v² / r</text>
    <text x="45" y="174" font-size="12" font-weight="bold" fill="#0f766e">• İki denklem oranlandığında (tanθ = v² / g·r):</text>
    <rect x="45" y="186" width="280" height="36" rx="8" fill="#ccfbf1"/>
    {f1}
    <text x="45" y="242" font-size="11" fill="#134e4a">• v büyükse yukarı, küçükse aşağı kayar.</text>
    <text x="45" y="258" font-size="11" font-weight="bold" fill="#0f766e">• Kütleden bağımsızdır!</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">2. Düşey Silindirde Dönüş (Akrobat)</text>
    <text x="395" y="128" font-size="12" fill="#1e3a8a">• Merkezcil kuvvet duvar tepkisidir: N = Fm</text>
    <text x="395" y="150" font-size="12" fill="#1e3a8a">• Düşeyde kaymama şartı: Fs = k · N ≥ m · g</text>
    <text x="395" y="174" font-size="12" font-weight="bold" fill="#1d4ed8">• k · (m · v² / r) ≥ m · g  ⇒  En küçük hız:</text>
    <rect x="395" y="186" width="280" height="36" rx="8" fill="#dbeafe"/>
    {f2}
    <text x="395" y="242" font-size="11" fill="#1e3a8a">• v &lt; vmin olursa cisim aşağı kayar.</text>
    <text x="395" y="258" font-size="11" font-weight="bold" fill="#1d4ed8">• Kütleden bağımsızdır!</text>
    """
    return svg(720, 285, ic, "Eğimli Virajda ve Düşey Silindirde Emniyetli Dönüş")


def gorsel_6():
    f1 = _kok_satir(130, 206, ["vmax = ", ("k", "k · g · r")], 13.5, "#312e81")
    f2 = _kok_satir(360, 206, ["v = ", ("k", "g · r · tanθ")], 13.5, "#14532d")
    f3 = _kok_satir(590, 206, ["vmin = ", ("k", "g · r / k")], 13.5, "#9a3412")
    ic = f"""
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Düzgün Çembersel Hareket Uygulamaları Özet Karşılaştırma Tablosu</text>

    <rect x="25" y="75" width="210" height="195" rx="10" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="130" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="#312e81">Yatay Viraj</text>
    <text x="130" y="128" text-anchor="middle" font-size="12" fill="#3730a3">Merkezcil Kuvvet:</text>
    <text x="130" y="148" text-anchor="middle" font-size="13" font-weight="bold" fill="#4338ca">Fs (Sürtünme)</text>
    <text x="130" y="180" text-anchor="middle" font-size="12" fill="#3730a3">Emniyetli Sınır Hız:</text>
    {f1}
    <text x="130" y="240" text-anchor="middle" font-size="11" fill="#4338ca">(En büyük güvenli sürat)</text>

    <rect x="255" y="75" width="210" height="195" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="360" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803d">Eğimli Viraj / Konik Sarkaç</text>
    <text x="360" y="128" text-anchor="middle" font-size="12" fill="#166534">Merkezcil Kuvvet:</text>
    <text x="360" y="148" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803d">N·sinθ veya T·sinα</text>
    <text x="360" y="180" text-anchor="middle" font-size="12" fill="#166534">Emniyetli Dönüş Hızı:</text>
    {f2}
    <text x="360" y="240" text-anchor="middle" font-size="11" fill="#15803d">(İdeal sürtünmesiz sürat)</text>

    <rect x="485" y="75" width="210" height="195" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="590" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="#9a3412">Düşey Silindir (Akrobat)</text>
    <text x="590" y="128" text-anchor="middle" font-size="12" fill="#7c2d12">Merkezcil Kuvvet:</text>
    <text x="590" y="148" text-anchor="middle" font-size="13" font-weight="bold" fill="#c2410c">N (Yüzey Normal Kuvveti)</text>
    <text x="590" y="180" text-anchor="middle" font-size="12" fill="#7c2d12">Emniyetli Sınır Hız:</text>
    {f3}
    <text x="590" y="240" text-anchor="middle" font-size="11" fill="#c2410c">(En küçük güvenli sürat)</text>
    """
    return svg(720, 285, ic, "Yatay, Eğimli ve Düşey Zeminlerde Emniyetli Dönüş Karşılaştırması")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g