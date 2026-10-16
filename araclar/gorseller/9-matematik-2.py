from ozet_gorsel import svg

_GEN = {
    " ": 0.30, ",": 0.30, ".": 0.30, "·": 0.34, "(": 0.36, ")": 0.36,
    "=": 0.60, "+": 0.60, "−": 0.60, "-": 0.50, "/": 0.42, ":": 0.32,
    "|": 0.32, "•": 0.48, "1": 0.50, "l": 0.30, "i": 0.30, "İ": 0.36,
    "ı": 0.30, "t": 0.36, "r": 0.38, "f": 0.36, "²": 0.42, "³": 0.42, "⁴": 0.42,
}


def _cw(ch):
    if ch in "023456789":
        return 0.58
    return _GEN.get(ch, 0.56)


def _mw(s, boy):
    s = s.replace("&lt;", "<").replace("&gt;", ">")
    return sum(_cw(c) for c in s) * boy


def _pw(p, boy):
    if isinstance(p, str):
        return _mw(p, boy)
    tur = p[0]
    if tur == "k":
        ic = p[1]
        der = p[2] if len(p) > 2 else ""
        dw = max(0.0, _mw(der, boy * 0.62) - boy * 0.18) if der else 0.0
        return dw + boy * 0.60 + boy * 0.08 + _mw(ic, boy) + boy * 0.10
    if tur == "kk":
        ic, d1, d2 = p[1], p[2], p[3]
        dw1 = max(0.0, _mw(d1, boy * 0.62) - boy * 0.18)
        dw2 = max(0.0, _mw(d2, boy * 0.62) - boy * 0.18)
        return dw1 + boy * 0.60 + dw2 + boy * 0.60 + boy * 0.08 + _mw(ic, boy) + boy * 0.14
    return 0.0


def _kok_svg(x, y, ic, boy, renk, kalin, der=""):
    out = []
    dw = max(0.0, _mw(der, boy * 0.62) - boy * 0.18) if der else 0.0
    rx = x + dw
    if der:
        out.append(
            f'<text x="{rx + boy * 0.08:.1f}" y="{y - boy * 0.48:.1f}" text-anchor="end" '
            f'font-size="{boy * 0.62:.1f}" font-weight="{kalin}" fill="{renk}">{der}</text>'
        )
    yt = y - boy * 0.90
    x_ic = rx + boy * 0.60 + boy * 0.08
    x_son = x_ic + _mw(ic, boy) + boy * 0.10
    d = (
        f"M{rx:.1f} {y - boy * 0.30:.1f} "
        f"L{rx + boy * 0.12:.1f} {y - boy * 0.38:.1f} "
        f"L{rx + boy * 0.32:.1f} {y + boy * 0.10:.1f} "
        f"L{rx + boy * 0.60:.1f} {yt:.1f} "
        f"H{x_son:.1f}"
    )
    sw = max(1.3, boy * 0.10)
    out.append(
        f'<path d="{d}" fill="none" stroke="{renk}" stroke-width="{sw:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    out.append(
        f'<text x="{x_ic:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" fill="{renk}">{ic}</text>'
    )
    return "".join(out)


def _ic_ice_kok_svg(x, y, ic, d1, d2, boy, renk, kalin):
    out = []
    dw1 = max(0.0, _mw(d1, boy * 0.62) - boy * 0.18)
    rx1 = x + dw1
    out.append(
        f'<text x="{rx1 + boy * 0.08:.1f}" y="{y - boy * 0.56:.1f}" text-anchor="end" '
        f'font-size="{boy * 0.62:.1f}" font-weight="{kalin}" fill="{renk}">{d1}</text>'
    )
    dw2 = max(0.0, _mw(d2, boy * 0.62) - boy * 0.18)
    rx2 = rx1 + boy * 0.60 + dw2
    out.append(
        f'<text x="{rx2 + boy * 0.08:.1f}" y="{y - boy * 0.44:.1f}" text-anchor="end" '
        f'font-size="{boy * 0.62:.1f}" font-weight="{kalin}" fill="{renk}">{d2}</text>'
    )
    yt_ic = y - boy * 0.84
    yt_dis = y - boy * 1.08
    x_ic = rx2 + boy * 0.60 + boy * 0.08
    x_son = x_ic + _mw(ic, boy) + boy * 0.12
    sw = max(1.3, boy * 0.10)
    d_dis = (
        f"M{rx1:.1f} {y - boy * 0.34:.1f} "
        f"L{rx1 + boy * 0.12:.1f} {y - boy * 0.42:.1f} "
        f"L{rx1 + boy * 0.32:.1f} {y + boy * 0.12:.1f} "
        f"L{rx1 + boy * 0.60:.1f} {yt_dis:.1f} "
        f"H{x_son:.1f}"
    )
    d_ic = (
        f"M{rx2:.1f} {y - boy * 0.28:.1f} "
        f"L{rx2 + boy * 0.12:.1f} {y - boy * 0.36:.1f} "
        f"L{rx2 + boy * 0.32:.1f} {y + boy * 0.08:.1f} "
        f"L{rx2 + boy * 0.60:.1f} {yt_ic:.1f} "
        f"H{x_son - 1:.1f}"
    )
    out.append(
        f'<path d="{d_dis}" fill="none" stroke="{renk}" stroke-width="{sw:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    out.append(
        f'<path d="{d_ic}" fill="none" stroke="{renk}" stroke-width="{sw:.1f}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )
    out.append(
        f'<text x="{x_ic:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" fill="{renk}">{ic}</text>'
    )
    return "".join(out)


def _satir(xc, y, parcalar, boy=12, renk="#334155", kalin=400):
    toplam = sum(_pw(p, boy) for p in parcalar)
    cx = xc - toplam / 2.0
    out = []
    for p in parcalar:
        if isinstance(p, str):
            out.append(
                f'<text x="{cx:.1f}" y="{y:.1f}" font-size="{boy:g}" font-weight="{kalin}" fill="{renk}">{p}</text>'
            )
        elif p[0] == "k":
            der = p[2] if len(p) > 2 else ""
            out.append(_kok_svg(cx, y, p[1], boy, renk, kalin, der))
        elif p[0] == "kk":
            out.append(_ic_ice_kok_svg(cx, y, p[1], p[2], p[3], boy, renk, kalin))
        cx += _pw(p, boy)
    return "".join(out)


def g1():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">ÜSLÜ VE KÖKLÜ GÖSTERİMLERİN DÖNÜŞÜMÜ</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">Rasyonel Üs ↔ Kök</text>',
        _satir(166, 108, ["x^(m/n) = ", ("k", "x^m", "n")], 13, "#334155", 600),
        _satir(166, 132, ["• 2^(3/2) = ", ("k", "2³"), " = ", ("k", "8")], 12, "#334155", 400),
        _satir(166, 150, ["• 5^(2/3) = ", ("k", "5²", "3"), " = ", ("k", "25", "3")], 12, "#334155", 400),
        _satir(166, 168, ["• ", ("k", "5⁴", "6"), " = 5^(4/6) = ", ("k", "25", "3")], 12, "#334155", 400),
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">Tek ve Çift Derece Kuralı</text>',
        _satir(453, 108, [("k", "a^n", "n"), " İfadesinin Değeri:"], 12.5, "#334155", 600),
        _satir(453, 132, ["• n tek ise: ", ("k", "a^n", "n"), " = a"], 12, "#334155", 400),
        _satir(453, 150, ["• n çift ise: ", ("k", "a^n", "n"), " = |a|"], 12, "#334155", 400),
        _satir(453, 168, ["• Örnek: ", ("k", "-27", "3"), " = -3, ", ("k", "16", "4"), " = 2"], 12, "#334155", 400),
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
        _satir(120, 150, ["4", ("k", "5", "3"), " + 2", ("k", "5", "3"), " = 6", ("k", "5", "3")], 12, "#1e293b", 700),
        '<rect x="220" y="60" width="180" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">Çarpma ve Bölme</text>',
        '<text x="310" y="108" text-anchor="middle" font-size="12" fill="#334155">Eşit derecede ortak</text>',
        '<text x="310" y="126" text-anchor="middle" font-size="12" fill="#334155">kök içine alınır:</text>',
        _satir(310, 150, [("k", "x", "n"), " · ", ("k", "y", "n"), " = ", ("k", "x·y", "n")], 12, "#1e293b", 700),
        '<rect x="410" y="60" width="180" height="128" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="500" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#a16207">Kökün Kökü</text>',
        '<text x="500" y="108" text-anchor="middle" font-size="12" fill="#334155">İç içe köklerde</text>',
        '<text x="500" y="126" text-anchor="middle" font-size="12" fill="#334155">dereceler çarpılır:</text>',
        _satir(500, 150, [("kk", "x", "m", "n"), " = ", ("k", "x", "m·n")], 12, "#1e293b", 700),
    ]
    return svg(w, h, "".join(ic), "Köklü ifadelerde toplama, çarpma ve kökün kökü kuralları")


def g3():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">FARKLI DERECELİ KÖKLERDE EŞİTLEME VE SIRALAMA</text>',
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        _satir(166, 86, ["Çarpma Örneği: ", ("k", "2", "6"), " · ", ("k", "5", "3")], 13, "#1d4ed8", 700),
        '<text x="166" y="110" text-anchor="middle" font-size="12" fill="#334155">1. Dereceler 6’da eşitlenir:</text>',
        _satir(166, 130, [("k", "5", "3"), " = ", ("k", "5²", "3·2"), " = ", ("k", "25", "6")], 12, "#334155", 400),
        _satir(166, 152, ["2. Sonuç: ", ("k", "2", "6"), " · ", ("k", "25", "6"), " = ", ("k", "50", "6")], 12, "#1e293b", 700),
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        _satir(454, 86, ["Sıralama: a=", ("k", "3", "3"), ", b=", ("k", "2", "6"), ", c=", ("k", "7", "9")], 12.5, "#7e22ce", 700),
        '<text x="454" y="110" text-anchor="middle" font-size="12" fill="#334155">Dereceler 18’de eşitlenir:</text>',
        _satir(454, 130, ["a = ", ("k", "729", "18"), ", b = ", ("k", "8", "18"), ", c = ", ("k", "49", "18")], 11.5, "#334155", 400),
        '<text x="454" y="152" text-anchor="middle" font-size="12" font-weight="700" fill="#1e293b">Sıralama: b &lt; c &lt; a</text>',
    ]
    return svg(w, h, "".join(ic), "Kök dereceleri farklı olan ifadelerde çarpma ve sıralama")


def g4():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">PAYDAYI RASYONEL YAPMA (EŞLENİK İLE ÇARPMA)</text>',
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        _satir(166, 86, ["Tek Terimli Payda: 1 / ", ("k", "a")], 13, "#15803d", 700),
        _satir(166, 110, ["Pay ve payda ", ("k", "a"), " ile çarpılır:"], 12, "#334155", 400),
        _satir(166, 132, ["1 / ", ("k", "3"), " = ", ("k", "3"), " / (", ("k", "3"), " · ", ("k", "3"), ") = ", ("k", "3"), " / 3"], 12, "#1e293b", 700),
        '<text x="166" y="154" text-anchor="middle" font-size="12" fill="#334155">Payda rasyonel sayıya dönüşür.</text>',
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        _satir(454, 86, ["İki Terimli Payda: 1 / (", ("k", "a"), " − ", ("k", "b"), ")"], 12.5, "#be123c", 700),
        _satir(454, 110, ["Eşleniği (", ("k", "a"), " + ", ("k", "b"), ") ile çarpılır:"], 12, "#334155", 400),
        _satir(454, 132, ["1 / (", ("k", "5"), " − ", ("k", "2"), ") = (", ("k", "5"), " + ", ("k", "2"), ") / 3"], 12, "#1e293b", 700),
        _satir(454, 154, ["İki kare farkı: (", ("k", "a"), ")² − (", ("k", "b"), ")² = a − b"], 11.5, "#334155", 400),
    ]
    return svg(w, h, "".join(ic), "Köklü ifadelerde eşlenik ve paydayı rasyonel yapma")


def uygula(v):
    b = v["bolumler"]
    b[1]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[3]["gorsel"] = g3()
    b[4]["gorsel"] = g4()

