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


def Daire(cx, cy, r, dolgu="#3b82f6", kenar="#1d4ed8", kw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'


def Cizgi(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'


def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İKİ NİCEL DEĞİŞKENLİ VERİLER VE SERPİLME DİYAGRAMI (SAÇILIM GRAFİĞİ)", "#1d4ed8")

    # 3 Küçük Serpilme Grafiği: Pozitif, Negatif, İlişki Yok
    grafikler = [
        ("1. Pozitif Doğrusal İlişki", "x arttıkça y de artar (r > 0)", "#059669", "#ecfdf5",
         [(40, 145), (60, 132), (80, 118), (100, 108), (120, 92), (140, 78), (160, 68)], (35, 150, 168, 62)),
        ("2. Negatif Doğrusal İlişki", "x arttıkça y azalır (r < 0)", "#dc2626", "#fef2f2",
         [(40, 68), (60, 82), (80, 96), (100, 108), (120, 122), (140, 134), (160, 146)], (35, 64, 168, 150)),
        ("3. Doğrusal İlişki Yok", "Noktalar rastgele dağılır (r ≈ 0)", "#475569", "#f1f5f9",
         [(45, 80), (65, 140), (85, 95), (105, 135), (125, 72), (145, 128), (160, 98)], None)
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, alt, r, ar, pts, dogru_c) in enumerate(grafikler):
        ox = sx + i * (kw + gap)
        oy = 48
        s += Kutu(ox, oy, kw, 168, ar, r, 1.8, 10)
        s += Yazi(ox + kw // 2, oy + 20, bas, 9.5, r, "middle", True)
        # Eksenler
        s += Cizgi(ox + 28, oy + 44, ox + 28, oy + 136, "#334155", 1.8)
        s += Cizgi(ox + 28, oy + 136, ox + 178, oy + 136, "#334155", 1.8)
        if dogru_c:
            x1, y1, x2, y2 = dogru_c
            s += Cizgi(ox + x1, oy + y1 - 24, ox + x2, oy + y2 - 24, r, 1.8)
        for px, py in pts:
            s += Daire(ox + px, oy + py - 24, 3.8, r, "#ffffff", 1)
        s += Yazi(ox + kw // 2, oy + 156, alt, 8.8, "#1e293b", "middle", True)

    s += Kutu(30, 224, W - 60, 26, "#eff6ff", "#2563eb", 1.5, 6)
    s += Yazi(W // 2, 241, "Bağımsız (açıklayıcı) değişken yatay eksende (x), bağımlı (yanıt) değişken düşey eksende (y) gösterilir.", 9.4, "#1e40af", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "PEARSON KORELASYON KATSAYISI (r) ÖLÇEĞİ VE YORUMU (-1 ≤ r ≤ +1)", "#0f766e")

    # Sayı doğrusu ölçeği
    s += Kutu(26, 48, 628, 92, "#ffffff", "#0f766e", 1.8, 10)
    s += Cizgi(66, 94, 594, 94, "#334155", 3)
    noktalar = [
        (66, "r = -1,0", "Tam Negatif", "#b91c1c"),
        (172, "-0,7", "Güçlü Negatif", "#dc2626"),
        (250, "-0,3", "Zayıf Negatif", "#d97706"),
        (330, "r = 0", "İlişki Yok", "#475569"),
        (410, "+0,3", "Zayıf Pozitif", "#0284c7"),
        (488, "+0,7", "Güçlü Pozitif", "#059669"),
        (594, "r = +1,0", "Tam Pozitif", "#047857")
    ]
    for nx, etiket, yorum, r in noktalar:
        s += Daire(nx, 94, 6, r, "#ffffff", 1.5)
        s += Yazi(nx, 76, etiket, 9.2, r, "middle", True)
        s += Yazi(nx, 118, yorum, 8.5, "#1e293b", "middle", True)

    s += Kutu(26, 150, 304, 86, "#ecfdf5", "#059669", 1.5, 8)
    s += Yazi(178, 170, "İlişkinin YÖNÜNÜ Belirleyen: İşaret (+ / -)", 9.6, "#047857", "middle", True)
    s += Yazi(178, 192, "• r > 0 ise: Aynı yönlü (Pozitif) ilişki", 9, "#1e293b", "middle", False)
    s += Yazi(178, 212, "• r &lt; 0 ise: Ters yönlü (Negatif) ilişki", 9, "#1e293b", "middle", False)

    s += Kutu(350, 150, 304, 86, "#eff6ff", "#2563eb", 1.5, 8)
    s += Yazi(502, 170, "İlişkinin GÜCÜNÜ Belirleyen: |r| Mutlak Değeri", 9.6, "#1d4ed8", "middle", True)
    s += Yazi(502, 192, "• |r| değeri 1'e yaklaştıkça ilişki GÜÇLENİR.", 9, "#1e293b", "middle", False)
    s += Yazi(502, 212, "• Örn: r = -0,85 ilişkisi, r = +0,60'tan daha güçlüdür!", 9, "#1e40af", "middle", True)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "EN UYGUN DOĞRU (REGRESYON / EĞİLİM DOĞRUSU) VE DENKLEMİ", "#6d28d9")

    s += Kutu(24, 48, 308, 192, "#faf5ff", "#7c3aed", 1.8, 10)
    s += Yazi(178, 68, "En Uygun Doğru Modeli: y = a + b·x", 10.2, "#6d28d9", "middle", True)
    maddeler = [
        "• Serpilme diyagramındaki noktaların genel",
        "  eğilimini en az hatayla temsil eden doğrudur.",
        "• Doğru mutlaka (x_ort, y_ort) ortalama",
        "  noktasından (ağırlık merkezinden) geçer!",
        "• b (Eğim): x değişkeni 1 birim arttığında",
        "  y değişkenindeki ortalama değişim miktarıdır.",
        "• a (Sabit Terim): x = 0 iken y eksenini kestiği değer."
    ]
    for i, m in enumerate(maddeler):
        s += Yazi(38, 92 + i * 20, m, 8.9, "#1e293b", "start", i in (2, 4, 6))

    s += Kutu(348, 48, 308, 192, "#fffbeb", "#d97706", 1.8, 10)
    s += Yazi(502, 68, "Tahmin Türleri ve Aykırı Değer", 10.2, "#b45309", "middle", True)
    t_mad = [
        "• İç Değer Tahmini (İnterpolasyon): Gözlenen",
        "  veri aralığının İÇİNDEKİ bir x değeri için",
        "  tahmin yapmaktır (Güvenilirliği yüksektir).",
        "• Dış Değer Tahmini (Ekstrapolasyon): Gözlenen",
        "  veri aralığının DIŞINDAKİ bir x değeri için",
        "  tahmin yapmaktır (Yanıltıcı olabilir!).",
        "• Aykırı Değer: Genel eğilimden çok uzaktaki nokta."
    ]
    for i, m in enumerate(t_mad):
        s += Yazi(362, 92 + i * 20, m, 8.9, "#1e293b", "start", i in (0, 3, 6))

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 245
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ALTIN KURAL: KORELASYON (İLİŞKİ) NEDENSELLİK DEMEK DEĞİLDİR!", "#991b1b")

    s += Kutu(26, 48, 628, 86, "#fef2f2", "#dc2626", 2, 10)
    s += Yazi(340, 70, "Yanıltıcı İlişki Örneği: Dondurma Satışları (x) ile Denizde Boğulma Vakaları (y)", 10.2, "#b91c1c", "middle", True)
    s += Yazi(340, 94, "• İki değişken arasında güçlü pozitif korelasyon (r ≈ +0,85) vardır.", 9.4, "#1e293b", "middle", False)
    s += Yazi(340, 114, "• Ancak dondurma yemek boğulmaya NEDEN OLMAZ! İkisini de artıran gizli değişken HAVA SICAKLIĞIDIR (Yaz Mevsimi).", 9.4, "#991b1b", "middle", True)

    s += Kutu(26, 146, 628, 84, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(340, 168, "İstatistiksel Karar Verme İlkeleri", 10.2, "#047857", "middle", True)
    s += Yazi(340, 190, "1. Korelasyon yalnızca iki değişkenin birlikte değişim eğilimini gösterir; neden-sonuç için kontrollü deney gerekir.", 9.2, "#1e293b", "middle", False)
    s += Yazi(340, 210, "2. Veri setindeki aykırı değerler korelasyon katsayısını (r) ve eğilim doğrusunun eğimini ciddi biçimde saptırabilir.", 9.2, "#1e293b", "middle", False)

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