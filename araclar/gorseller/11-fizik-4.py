def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'İKİ BOYUTTA HAREKETİN BAĞIMSIZLIĞI VE BİLEŞEN ANALİZİ</text>'
    )
    ic += _kart(
        20, 42, 345, 205,
        "Yatay Bileşen (x Ekseni - Sabit Hızlı)",
        [
            "• Yatay doğrultuda net kuvvet sıfırdır (Fx = 0).",
            "• Yatay ivme sıfırdır: ax = 0.",
            "• Yatay hız hareket boyunca değişmez:",
            "  vx(t) = v0x = v0 · cos(a) = sabit",
            "• Eşit zaman aralıklarında eşit yatay yollar alınır:",
            "  x = v0x · t   ve   x_menzil = v0x · t_ucus",
            "• Tepe noktasında cismin toplam hızı v0x'e eşittir.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        395, 42, 345, 205,
        "Düşey Bileşen (y Ekseni - Sabit İvmeli)",
        [
            "• Düşeyde yalnız ağırlık kuvveti etki eder (Fy = -m·g).",
            "• Düşey ivme yer çekimi ivmesidir: ay = -g.",
            "• Düşey hız her saniye g (10 m/s) kadar değişir:",
            "  vy(t) = v0y - g · t   (v0y = v0 · sin(a))",
            "• Çıkış süresi: t_cikis = v0y / g,  t_ucus = 2 · t_cikis",
            "• Maksimum yükseklik: h_max = (v0y)^2 / (2·g)",
            "• Herhangi bir anda hız: v = ((vx)^2 + (vy)^2)^(1/2)",
        ],
        "#dc2626", "#fef2f2"
    )
    return _svg(760, 270, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'YATAY ATIŞTA TÜMEVARIMSAL ÖRÜNTÜ: EŞİT ZAMAN ARALIKLARINDA KONUM</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Saniye Sonu (t = 1 s)",
        [
            "• Yatay konum: x1 = v0 · 1 = x",
            "• Düşey hız: vy = g · 1 = 10 m/s",
            "• Alınan düşey yol: h1 = h (5 m)",
            "• Toplam düşey konum: y1 = h (5 m)",
            "• Yatayda x giderken düşeyde 1h",
            "  kadar aşağı iner.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Saniye Sonu (t = 2 s)",
        [
            "• Yatay konum: x2 = v0 · 2 = 2x",
            "• Düşey hız: vy = g · 2 = 20 m/s",
            "• 2. saniyede düşey yol: 3h (15 m)",
            "• Toplam düşey konum: y2 = 4h (20 m)",
            "• Yatayda 2x olduğunda düşeyde",
            "  toplam 4h (2^2 · h) düşmüştür.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "n. Saniye Sonu (Tümevarım Kuralı)",
        [
            "• Yatay konum: xn = n · x  (x ile doğru)",
            "• Düşey konum: yn = n^2 · h (t^2 ile doğru)",
            "• Yörünge denklemi (parabol):",
            "  y = (g / (2 · v0^2)) · x^2",
            "• Sonuç: Yatay yer değiştirmelerin",
            "  oranı x1/x2 = t1/t2 = (h1/h2)^(1/2)",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'EĞİK ATIŞTA TÜMLER AÇILAR, MAKSİMUM MENZİL VE ALTIN ORAN BAĞINTISI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Menzil Bağıntısı ve Tümler Açılar (a + b = 90°)",
        [
            "• Menzil formülü: x_menzil = (v0^2 · sin(2a)) / g",
            "• Maksimum menzil: a = 45° iken sin(90°) = 1 olur",
            "  ve x_max = v0^2 / g değerine ulaşır.",
            "• Eşit büyüklükte ilk hızla (v0) atılan cisimlerde",
            "  atış açıları toplamı 90° ise (örn. 30° ve 60°,",
            "  20° ve 70°) yatay menzilleri EŞİTTİR (x1 = x2).",
            "• Ancak büyük açıyla atılan daha yükseğe çıkar.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Yükseklik - Menzil Oranı ve Simetri İlkesi",
        [
            "• h_max / x_menzil oranı sadece atış açısına bağlıdır:",
            "  h_max / x_menzil = (1 / 4) · tan(a)",
            "• Özel durum: a = 45° için h_max = x_menzil / 4",
            "• Tepe noktasından sonrası tam bir YATAY ATIŞTIR!",
            "• Çıkış ve iniş simetriktir: Yerden aynı yükseklikteki",
            "  noktalardan geçerken süratler birbirine eşittir.",
            "• Tepe noktasında hız ile ivme birbirine DİKTİR (90°).",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="250" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÖZEL UYGULAMA: SERBEST DÜŞEN HEDEFE NİŞAN ALMA DENEYİ</text>'
    )
    ic += _kart(
        20, 42, 720, 192,
        "Aynı Anda Bırakılan Hedef ve Eğik Atılan Mermi Neden Havada Çarpışır?",
        [
            "• K noktasından bir mermi doğrudan L noktasındaki hedefe nişan alınarak t = 0 anında v0 hızıyla fırlatılsın.",
            "• Tam aynı anda (t = 0) L noktasındaki hedef de ilk hızsız serbest düşmeye bırakılsın.",
            "• Yer çekimi olmasaydı mermi doğrusal gidip t sürede L noktasına varacaktı; ancak yer çekimi nedeniyle",
            "  t sürede doğrusal nişan doğrultusundan Δy = (1/2)·g·t^2 kadar aşağı sarkar.",
            "• Aynı t sürede L'den serbest düşen hedef de tam olarak h = (1/2)·g·t^2 kadar aşağı düşer!",
            "• SONUÇ: Her iki cisim de aynı sürede yer çekimi yüzünden eşit miktarda ((1/2)·g·t^2) aşağı sarktığı için,",
            "  mermi yere çarpmadan önce havada mutlaka hedefi vurur! (İlk hız v0 artarsa daha yukarıda çarpışırlar.)",
        ],
        "#2563eb", "#eff6ff"
    )
    return _svg(760, 260, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][3]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]