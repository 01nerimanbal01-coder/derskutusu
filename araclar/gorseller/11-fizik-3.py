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
    s += Baslik(W, "SERBEST DÜŞME HAREKETİ (g = 10 m/s² İKEN HIZ VE YOL TABLOSU)", "#1d4ed8")

    # Sol: Düşey yörünge (Galileo tek sayılar kuralı)
    s += Kutu(24, 48, 300, 196, "#eff6ff", "#2563eb", 1.8, 10)
    s += Yazi(174, 68, "Düşey Konum ve Hız (h = 5t²)", 10.5, "#1e40af", "middle", True)
    anlar = [
        ("t = 0 s", "v = 0 m/s", "h = 0 m", 88),
        ("t = 1 s", "v = 10 m/s", "Δh₁ = 5 m (h = 5 m)", 122),
        ("t = 2 s", "v = 20 m/s", "Δh₂ = 15 m (h = 20 m)", 158),
        ("t = 3 s", "v = 30 m/s", "Δh₃ = 25 m (h = 45 m)", 196),
        ("t = 4 s", "v = 40 m/s", "Δh₄ = 35 m (h = 80 m)", 230)
    ]
    s += Cizgi(64, 88, 64, 230, "#2563eb", 2.5)
    for t_ad, v_ad, h_ad, y in anlar:
        s += Daire(64, y, 5, "#dc2626", "#991b1b", 1.5)
        s += Yazi(82, y + 4, f"{t_ad}  →  {v_ad}  |  {h_ad}", 9.2, "#1e293b", "start", True)

    # Sağ: Temel Bağıntılar
    s += Kutu(344, 48, 312, 196, "#ecfdf5", "#059669", 1.8, 10)
    s += Yazi(500, 68, "Serbest Düşme Denklemleri (v₀ = 0)", 10.5, "#047857", "middle", True)
    denk = [
        ("1. Hız Denklemi:", "v = g · t", "#059669", "#d1fae5"),
        ("2. Alınan Yol (Yükseklik):", "h = (1/2) · g · t²", "#0284c7", "#e0f2fe"),
        ("3. Zamansız Hız Denklemi:", "v² = 2 · g · h", "#7c3aed", "#f3e8ff"),
        ("4. Ardışık Saniye Yolları:", "h, 3h, 5h, 7h... (5m, 15m, 25m...)", "#d97706", "#fef3c7")
    ]
    for i, (bas, form, r, ar) in enumerate(denk):
        y = 82 + i * 38
        s += Kutu(360, y, 280, 32, ar, r, 1.4, 6)
        s += Yazi(372, y + 20, bas, 9.2, "#1e293b", "start", True)
        s += Yazi(628, y + 20, form, 9.8, r, "end", True)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İKİ BOYUTTA HAREKETİN TEMEL İLKESİ: BAĞIMSIZLIK İLKESİ", "#0f766e")

    s += Kutu(26, 48, 304, 156, "#e0f2fe", "#0284c7", 2, 10)
    s += Kutu(26, 48, 304, 32, "#0284c7", "#0284c7", 1, 10)
    s += Yazi(178, 69, "1. YATAY BİLEŞEN (x Ekseni)", 10.5, "#ffffff", "middle", True)
    x_mad = [
        "• Yatay doğrultuda net kuvvet sıfırdır (F_x = 0).",
        "• Yatay ivme sıfırdır (a_x = 0).",
        "• Yatay hız hareket boyunca SABİTTİR (v_x = v₀x).",
        "• Yatayda Düzgün Doğrusal Hareket yapılır:",
        "  x = v₀x · t   ve   x_menzil = v₀x · t_uçuş"
    ]
    for i, m in enumerate(x_mad):
        s += Yazi(38, 100 + i * 20, m, 9.2, "#1e293b", "start", i in (2, 4))

    s += Kutu(350, 48, 304, 156, "#fef3c7", "#d97706", 2, 10)
    s += Kutu(350, 48, 304, 32, "#d97706", "#d97706", 1, 10)
    s += Yazi(502, 69, "2. DÜŞEY BİLEŞEN (y Ekseni)", 10.5, "#ffffff", "middle", True)
    y_mad = [
        "• Düşeyde yalnız yer çekimi kuvveti etki eder (G = m·g).",
        "• Düşey ivme sabit ve aşağı yönlüdür (a_y = g).",
        "• Düşey hız her saniye g kadar değişir.",
        "• Düşeyde Sabit İvmeli Hareket yapılır:",
        "  v_y = v₀y ∓ g·t   |   h = v₀y·t ∓ (1/2)g·t²"
    ]
    for i, m in enumerate(y_mad):
        s += Yazi(362, 100 + i * 20, m, 9.2, "#1e293b", "start", i in (1, 4))

    s += Kutu(26, 214, 628, 32, "#ecfdf5", "#059669", 1.5, 8)
    s += Yazi(340, 234, "Yatay ve düşey hareketleri birbirine bağlayan tek ortak fiziksel nicelik UÇUŞ SÜRESİDİR (t)!", 9.8, "#065f46", "middle", True)
    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "YATAY ATIŞ HAREKETİ ANALİZİ", "#6d28d9")

    s += Kutu(26, 48, 310, 192, "#faf5ff", "#7c3aed", 1.8, 10)
    s += Yazi(181, 68, "Yatay Atış Yörüngesi", 10.5, "#6d28d9", "middle", True)
    # Kule ve parabolik yörünge
    s += Kutu(54, 90, 32, 118, "#cbd5e1", "#64748b", 1.5, 2)
    s += Daire(86, 90, 6, "#dc2626", "#991b1b", 1.5)
    s += Cizgi(86, 90, 146, 90, "#2563eb", 2.5)
    s += Yazi(120, 82, "v₀ (yatay)", 9, "#1d4ed8", "middle", True)
    s += '<path d="M 86 90 Q 190 95 270 208" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="5,4"/>'
    s += Cizgi(54, 208, 310, 208, "#334155", 2)
    s += Yazi(44, 152, "h", 11, "#dc2626", "middle", True)
    s += Yazi(178, 224, "x (Menzil) = v₀ · t", 9.8, "#1e40af", "middle", True)

    s += Kutu(352, 48, 302, 192, "#ffffff", "#7c3aed", 1.8, 10)
    s += Yazi(503, 68, "Yatay Atış Özellikleri", 10.5, "#6d28d9", "middle", True)
    maddeler = [
        "• İlk düşey hız sıfırdır (v₀y = 0).",
        "• Uçuş süresi yalnız h yüksekliğine ve g'ye bağlıdır:",
        "  h = (1/2) · g · t²   (v₀ hızı süreyi etkilemez!)",
        "• Aynı yükseklikten serbest bırakılan cisimle",
        "  yatay atılan cisim AYNI ANDA yere çarpar.",
        "• Yere çarpma hızı Pisagor bağıntısıyla bulunur:",
        "  v² = v_x² + v_y²   (v_x = v₀,  v_y = g · t)"
    ]
    for i, m in enumerate(maddeler):
        s += Yazi(366, 92 + i * 20, m, 9, "#1e293b", "start", i in (2, 4, 6))

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "EĞİK ATIŞ HAREKETİ VE ÖZEL AÇI KURALLARI", "#b45309")

    s += Kutu(24, 48, 312, 192, "#fffbeb", "#d97706", 1.8, 10)
    s += Yazi(180, 68, "Eğik Atış Yörüngesi ve Tepe Noktası (T)", 10, "#b45309", "middle", True)
    s += Cizgi(44, 204, 316, 204, "#334155", 2)
    s += '<path d="M 56 204 Q 180 42 304 204" fill="none" stroke="#d97706" stroke-width="2.5"/>'
    s += Daire(180, 123, 5, "#dc2626", "#991b1b", 1.5)
    s += Cizgi(180, 123, 224, 123, "#2563eb", 2.5)
    s += Yazi(202, 114, "v_T = v₀x (v_y = 0)", 8.5, "#1d4ed8", "middle", True)
    s += Cizgi(180, 123, 180, 204, "#dc2626", 1.5)
    s += Yazi(198, 168, "h_max", 9.5, "#dc2626", "start", True)
    s += Yazi(180, 222, "x_menzil = v₀x · t_uçuş", 9.5, "#92400e", "middle", True)

    s += Kutu(352, 48, 304, 192, "#f0fdf4", "#16a34a", 1.8, 10)
    s += Yazi(504, 68, "Eğik Atış Formülleri ve Özel Durumlar", 10, "#15803d", "middle", True)
    kurallar = [
        "• Hız Bileşenleri: v₀x = v₀·cosα  |  v₀y = v₀·sinα",
        "• Çıkış ve Uçuş Süresi: t_ç = v₀y / g  |  t_u = 2·t_ç",
        "• Maksimum Yükseklik: h_max = v₀y² / (2·g)",
        "• Tepe noktasında düşey hız sıfırdır (v_y = 0),",
        "  ancak cismin hızı sıfır DEĞİLDİR (v_min = v₀x)!",
        "• α = 45° iken yatay menzil MAKSİMUM olur.",
        "• α + β = 90° ve v₀ eşit ise menziller EŞİTTİR (x₁ = x₂)."
    ]
    for i, m in enumerate(kurallar):
        s += Yazi(366, 92 + i * 20, m, 8.9, "#1e293b", "start", i in (4, 5, 6))

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
