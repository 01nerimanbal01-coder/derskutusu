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

def Cokgen(noktalar, dolgu="#bbf7d0", kenar="#15803d", kw=2):
    pts = " ".join(f"{x},{y}" for x, y in noktalar)
    return f'<polygon points="{pts}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Ok(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'

def kaydet(*args):
    pass



def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KUR'AN-I KERİM'DE 'RAB (رَبّ)' KAVRAMI VE BOYUTLARI", "#0f766e")

    merkez_x, merkez_y = 340, 128
    s += Kutu(230, 96, 220, 64, "#059669", "#047857", 2, 12)
    s += Yazi(merkez_x, 122, "ER-RAB (الرَّبُّ)", 13, "#ffffff", "middle", True)
    s += Yazi(merkez_x, 144, "Âlemlerin Rabbi (رَبُّ الْعَالَمِينَ)", 10, "#d1fae5", "middle", True)

    kutular = [
        (24, 48, "1. Terbiye Eden ve Yetiştiren", "Varlıkları aşama aşama olgunluğa eriştiren", "#0284c7", "#e0f2fe"),
        (436, 48, "2. Koruyan ve Gözeten", "Yarattıklarını başıboş bırakmayıp himaye eden", "#2563eb", "#dbeafe"),
        (24, 168, "3. Nimet ve Rızık Veren", "Maddi ve manevi tüm ihtiyaçları karşılayan", "#d97706", "#fef3c7"),
        (436, 168, "4. Mutlak Sahip ve Hükümran", "Vahiyle yol gösteren, emir ve yasak koyan", "#7c3aed", "#f3e8ff")
    ]

    for x, y, bas, acik, r, ar in kutular:
        s += Kutu(x, y, 220, 64, ar, r, 1.5, 8)
        s += Yazi(x + 110, y + 24, bas, 9.8, r, "middle", True)
        s += Yazi(x + 110, y + 46, acik, 8.8, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KUR'AN-I KERİM'DE 'İFFET (عِفَّة)' KAVRAMI VE ÖRNEK ŞAHSİYETLER", "#6d28d9")

    s += Kutu(24, 48, 304, 194, "#faf5ff", "#7c3aed", 2, 10)
    s += Yazi(176, 70, "İFFET KAVRAMININ KAPSAMI", 11, "#6d28d9", "middle", True)
    maddeler = [
        "• Sözlük anlamı: Haramlardan, çirkin söz ve",
        "  davranışlardan uzak durmak, temiz kalmak.",
        "• Namus, haya (utanma duygusu) ve edebi korumak.",
        "• Gözü, dili, kalbi ve bedeni günahtan sakınmak.",
        "• Mala ve dünyevi arzulara karşı ölçülü, tok gözlü",
        "  ve kanaatkâr olmak (İstîfâf — Bakara, 2/273)."
    ]
    for i, m in enumerate(maddeler):
        s += Yazi(38, 94 + i * 22, m, 9.2, "#1e293b", "start", False)

    s += Kutu(348, 48, 308, 92, "#ecfdf5", "#059669", 1.5, 10)
    s += Yazi(502, 70, "Hz. Yusuf (as) — İffet ve Sadakat Abidesi", 10.2, "#047857", "middle", True)
    s += Yazi(502, 92, "• Günaha çağrıldığında \"Allah'a sığınırım (Maâzallah)!\"", 9, "#1e293b", "middle", False)
    s += Yazi(502, 110, "  diyerek zindanı günaha tercih etmiştir (Yûsuf, 12/23-33).", 9, "#1e293b", "middle", False)

    s += Kutu(348, 150, 308, 92, "#eff6ff", "#2563eb", 1.5, 10)
    s += Yazi(502, 172, "Hz. Meryem — Tertemiz İffet Timsali", 10.2, "#1d4ed8", "middle", True)
    s += Yazi(502, 194, "• Kur'an'da iffetini ve namusunu titizlikle koruyan", 9, "#1e293b", "middle", False)
    s += Yazi(502, 212, "  müminlerin zirve örneği olarak övülmüştür (Tahrîm, 66/12).", 9, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "'RAB' VE 'İFFET' KAVRAMLARININ KARŞILAŞTIRMALI AYRIMI", "#1e3a8a")

    s += Kutu(26, 48, 304, 186, "#ecfdf5", "#059669", 2, 10)
    s += Kutu(26, 48, 304, 32, "#059669", "#059669", 1, 10)
    s += Yazi(178, 69, "RAB (رَبّ) KAVRAMI", 10.5, "#ffffff", "middle", True)
    r_mad = [
        "• İlişkili Alan: İnanç (Akâid / Kelam) ve Tevhid",
        "• Öznesi: Yüce Allah'ın (cc) güzel isimlerindendir",
        "• Kapsamı: Yaratma, terbiye etme, rızık verme, yönetme",
        "• Kulda Uyandırdığı Bilinç: Yalnız Allah'a kulluk,",
        "  dua, tevekkül, şükür ve rubûbiyeti tasdik (Fâtiha, 1/2)"
    ]
    for i, m in enumerate(r_mad):
        s += Yazi(40, 102 + i * 24, m, 9.2, "#1e293b", "start", i < 2)

    s += Kutu(350, 48, 304, 186, "#f3e8ff", "#7c3aed", 2, 10)
    s += Kutu(350, 48, 304, 32, "#7c3aed", "#7c3aed", 1, 10)
    s += Yazi(502, 69, "İFFET (عِفَّة) KAVRAMI", 10.5, "#ffffff", "middle", True)
    i_mad = [
        "• İlişkili Alan: İslam Ahlakı (Fazilet / Erdem)",
        "• Öznesi: Mümin insanın kazanması gereken erdemdir",
        "• Kapsamı: Haya, namus, haramdan sakınma, kanaat",
        "• Kulda Uyandırdığı Bilinç: Nefsin aşırı arzularını",
        "  dizginleme, mahremiyete saygı ve onurlu duruş (Nûr, 24/30)"
    ]
    for i, m in enumerate(i_mad):
        s += Yazi(364, 102 + i * 24, m, 9.2, "#1e293b", "start", i < 2)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 245
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KUR'AN OKUMA (TİLAVET VE KIRAAT) TEMEL KAVRAMLARI", "#b45309")

    kavramlar = [
        ("TİLAVET (تِلَاوَة)", "Kur'an'ı anlamını düşünerek ve hayata geçirmek üzere saygıyla okumak", "#0284c7", "#e0f2fe"),
        ("TERTÎL (تَرْتِيل)", "Harflerin mahreç ve tecvid kurallarına uyarak tane tane, acele etmeden okumak", "#059669", "#ecfdf5"),
        ("KIRAAT (قِرَاءَة)", "Kur'an kelimelerinin okunuş keyfiyetini ve farklı vecihlerini inceleyen ilim", "#7c3aed", "#f3e8ff"),
        ("ÂSIM KIRAATİ — HAFS RİVAYETİ", "Ülkemizde ve İslam dünyasının büyük kısmında okunan sahih kıraat/rivayet", "#d97706", "#fef3c7")
    ]

    for i, (bas, acik, r, ar) in enumerate(kavramlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 86
        s += Kutu(x, y, 312, 72, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 24, bas, 10, r, "start", True)
        s += Yazi(x + 14, y + 48, acik[:50], 9, "#1e293b", "start", False)
        s += Yazi(x + 14, y + 62, acik[50:], 9, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-kuran-i-kerim-3", 1, gorsel_1())
    kaydet("10-kuran-i-kerim-3", 2, gorsel_2())
    kaydet("10-kuran-i-kerim-3", 3, gorsel_3())
    kaydet("10-kuran-i-kerim-3", 4, gorsel_4())


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
