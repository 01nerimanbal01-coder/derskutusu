# -*- coding: utf-8 -*-
import html as _html


def svg_basla(w, h):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{w}px;display:block;margin:12px auto;font-family:system-ui,-apple-system,sans-serif;">'


def svg_bitir():
    return '</svg>'


def Arka(w, h, renk="#f8fafc"):
    return f'<rect width="{w}" height="{h}" rx="14" fill="{renk}" stroke="#cbd5e1" stroke-width="1.5"/>'


def Baslik(w, metin, renk="#1e3a8a"):
    return (f'<rect x="16" y="10" width="{w-32}" height="28" rx="7" fill="{renk}"/>'
            f'<text x="{w//2}" y="29" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">{_html.escape(str(metin))}</text>')


def Kutu(x, y, w, h, dolgu="#ffffff", kenar="#94a3b8", kw=1.5, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'


def Yazi(x, y, metin, punto=10, renk="#1e293b", hiza="middle", kalin=False):
    fw = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{punto}" fill="{renk}"{fw}>{_html.escape(str(metin))}</text>'


def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BİTKİSEL HORMONLAR (FİTOHORMONLAR) VE TEMEL İŞLEVLERİ", "#15803d")

    s += Kutu(22, 46, 412, 198, "#f0fdf4", "#16a34a", 2, 10)
    s += Yazi(228, 66, "A) BÜYÜMEYİ VE GELİŞMEYİ TEŞVİK EDEN HORMONLAR", 10.2, "#15803d", "middle", True)

    tesvik = [
        ("1. OKSİN", "Sürgün ucunda (koleoptil) üretilir; hücre uzamasını, fototropizma ve geotropizma yönelimlerini ve köklenmeyi sağlar.", "#059669", "#dcfce7"),
        ("2. GİBERELLİN", "Gövde uzamasını, tohumun uyku hâlinden (dormansi) çıkıp çimlenmesini ve çekirdeksiz meyve büyümesini uyarır.", "#0284c7", "#e0f2fe"),
        ("3. SİTOKİNİN", "Kök uçlarında sentezlenir, ksilemle taşınır; hücre bölünmesini (mitoz), yan dal oluşumunu sağlar ve yaşlanmayı geciktirir.", "#7c3aed", "#f3e8ff")
    ]
    for i, (ad, acik, r, ar) in enumerate(tesvik):
        y = 78 + i * 52
        s += Kutu(34, y, 388, 44, ar, r, 1.4, 6)
        s += Yazi(44, y + 16, ad, 9.5, r, "start", True)
        s += Yazi(44, y + 31, acik[:66], 8.2, "#1e293b", "start", False)
        s += Yazi(44, y + 41, acik[66:], 8.2, "#1e293b", "start", False)

    s += Kutu(446, 46, 212, 198, "#fef2f2", "#dc2626", 2, 10)
    s += Yazi(552, 66, "B) ENGELLEYİCİ / OLGUNLAŞTIRICI", 9.5, "#b91c1c", "middle", True)

    engel = [
        ("4. ETİLEN (Gaz Hormon)", "Meyve olgunlaşmasını (nişasta → şeker) ve yaprak dökümünü hızlandırır.", "#d97706", "#fef3c7"),
        ("5. ABSİSİK ASİT (ABA)", "Stres hormonudur; kuraklıkta stomaları kapatır, dormansiyi sürdürür.", "#dc2626", "#fee2e2")
    ]
    for i, (ad, acik, r, ar) in enumerate(engel):
        y = 82 + i * 76
        s += Kutu(458, y, 188, 66, ar, r, 1.4, 6)
        s += Yazi(466, y + 18, ad, 9, r, "start", True)
        s += Yazi(466, y + 35, acik[:32], 8.2, "#1e293b", "start", False)
        s += Yazi(466, y + 48, acik[32:64], 8.2, "#1e293b", "start", False)
        s += Yazi(466, y + 60, acik[64:], 8.2, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "OKSİN HORMONU VE ASİMETRİK BÜYÜME (FOTOTROPİZMA MEKANİZMASI)", "#1d4ed8")

    adimlar = [
        ("1. DİK IŞIK", "Oksin simetrik dağılır", "Koleoptil yukarı doğru", "dik uzar (yönelim yok)", "#059669", "#ecfdf5"),
        ("2. YANDAN IŞIK", "Oksin ışıktan kaçar", "Karanlık (gölge) tarafta", "oksin yoğunluğu artar", "#d97706", "#fef3c7"),
        ("3. FARKLI UZAMA", "Oksin çok olan gölge", "taraftaki hücreler daha", "hızlı ve fazla uzar", "#2563eb", "#dbeafe"),
        ("4. IŞIĞA YÖNELİM", "Gövde/koleoptil ışığa", "doğru bükülür (Pozitif", "Fototropizma)", "#7c3aed", "#f3e8ff")
    ]

    kw = 148
    gap = 12
    sx = (W - (4 * kw + 3 * gap)) // 2
    for i, (bas, m1, m2, m3, r, ar) in enumerate(adimlar):
        x = sx + i * (kw + gap)
        y = 50
        s += Kutu(x, y, kw, 144, ar, r, 2, 10)
        s += Kutu(x, y, kw, 30, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 20, bas, 9.2, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 58, m1, 9, r, "middle", True)
        s += Yazi(x + kw // 2, y + 84, m2, 8.8, "#1e293b", "middle", False)
        s += Yazi(x + kw // 2, y + 104, m3, 8.8, "#1e293b", "middle", False)

    s += Kutu(28, 206, W - 56, 34, "#eff6ff", "#2563eb", 1.5, 8)
    s += Yazi(W // 2, 227, "Darwin ve Boysen-Jensen Deneyleri: Oksin suda ve agar blokta çözünüp geçer; mika ve jelatin olmayan engelden geçemez!", 9.4, "#1e40af", "middle", True)
    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BİTKİLERDE TEPKİ HAREKETLERİ: TROPİZMA VE NASTİ KARŞILAŞTIRMASI", "#0f766e")

    s += Kutu(24, 48, 306, 192, "#ecfdf5", "#059669", 2, 10)
    s += Kutu(24, 48, 306, 32, "#059669", "#059669", 1, 10)
    s += Yazi(177, 69, "1. TROPİZMA (YÖNELİM HAREKETLERİ)", 10, "#ffffff", "middle", True)
    t_mad = [
        "• Uyaranın GELDİĞİ YÖNE bağlıdır.",
        "• Uyaran yönüne doğruysa Pozitif (+), zıt yöneyse",
        "  Negatif (-) tropizma adını alır.",
        "• Oksin hormonunun düzensiz dağılımı ve",
        "  ASİMETRİK BÜYÜME (hücre bölünmesi/uzaması) ile olur.",
        "• Yavaş ve geri dönüşsüz büyüme hareketidir."
    ]
    for i, m in enumerate(t_mad):
        s += Yazi(38, 100 + i * 21, m, 9, "#1e293b", "start", i in (0, 4))

    s += Kutu(350, 48, 306, 192, "#fffbeb", "#d97706", 2, 10)
    s += Kutu(350, 48, 306, 32, "#d97706", "#d97706", 1, 10)
    s += Yazi(503, 69, "2. NASTİ (IRGANIM HAREKETLERİ)", 10, "#ffffff", "middle", True)
    n_mad = [
        "• Uyaranın yönüne BAĞLI DEĞİLDİR.",
        "• Pozitif (+) veya negatif (-) ayrımı YOKTUR.",
        "• Hücrelerdeki su basıncının, yani TURGOR",
        "  BASINCININ ani değişimiyle gerçekleşir.",
        "• Tropizmaya göre çok daha HIZLI ve",
        "  geri dönüşlü (tersinir) bir harekettir."
    ]
    for i, m in enumerate(n_mad):
        s += Yazi(364, 100 + i * 21, m, 9, "#1e293b", "start", i in (0, 3))

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BAŞLICA TROPİZMA VE NASTİ ÇEŞİTLERİ", "#6d28d9")

    turler = [
        ("Fototropizma (Işık)", "Gövde ışığa (+), kök ışıktan uzağa (-) yönelir.", "#059669", "#d1fae5"),
        ("Geotropizma / Gravitropizma", "Kök yer çekimine (+), gövde zıt yöne (-) yönelir.", "#0284c7", "#e0f2fe"),
        ("Hidrotropizma ve Kemotropizma", "Kök suya (+) ve gübreye (+), kirece/tuza (-) yönelir.", "#2563eb", "#dbeafe"),
        ("Haptotropizma / Tigmotropizma", "Sarmaşık ve asma filizlerinin desteğe sarılması (+).", "#4f46e5", "#e0e7ff"),
        ("Fotonasti ve Termonasti", "Akşamsefasının karanlıkta, lalenin sıcakta (15-20°C) açması.", "#d97706", "#fef3c7"),
        ("Sismonasti / Tigmonasti", "Küstüm otunun (Mimosa) dokununca yaprak kapatması, böcekkapan.", "#dc2626", "#fee2e2")
    ]

    kw, kh = 306, 58
    for i, (bas, acik, r, ar) in enumerate(turler):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 10)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 12, y + 21, bas, 9.8, r, "start", True)
        s += Yazi(x + 12, y + 42, acik, 8.8, "#1e293b", "start", False)

    s += svg_bitir()
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
