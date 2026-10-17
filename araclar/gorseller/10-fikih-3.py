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
    s += Baslik(W, "FIKIH İLMİNİN BEŞ TEMEL İLKESİ (TEŞRÎ İLKELERİ)", "#0f766e")

    ilkeler = [
        ("1. Tekliflerde Kolaylık", "Teysîr / Ref'u'l-Harec: Güç yetirememe ve zorlukta ruhsat (Bakara 185, 286)", "#0284c7", "#e0f2fe", 24, 48, 204),
        ("2. Helallerde Genişlik", "Eşyada asıl olan ibâhadır (mubahlıktır); haramlar sınırlı ve açıktır", "#059669", "#d1fae5", 238, 48, 204),
        ("3. Hükümlerde Tedricîlik", "Ahkâmın insan fıtratına uygun olarak aşama aşama indirilmesi", "#7c3aed", "#f3e8ff", 452, 48, 204),
        ("4. Kamu Yararı ve Zararın Giderilmesi", "Maslahatın gözetilmesi ve mefsedetin (zararın) önlenmesi ilkesi", "#d97706", "#fef3c7", 60, 152, 265),
        ("5. Adalet ve Hakkaniyet", "Hakkaniyet, eşitlik ve suç-ceza dengesinin korunması (Nisâ 58, 135)", "#dc2626", "#fef2f2", 355, 152, 265)
    ]

    for bas, acik, r, ar, x, y, w in ilkeler:
        s += Kutu(x, y, w, 90, ar, r, 2, 10)
        s += Kutu(x, y, w, 28, r, r, 1, 10)
        s += Yazi(x + w // 2, y + 19, bas, 9.5, "#ffffff", "middle", True)
        s += Yazi(x + w // 2, y + 50, acik[:38], 8.8, "#1e293b", "middle", False)
        s += Yazi(x + w // 2, y + 68, acik[38:], 8.8, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KOLAYLIK İLKESİ (TEYSÎR): AZİMET VE RUHSAT UYGULAMALARI", "#1e3a8a")

    s += Kutu(26, 48, 304, 154, "#eff6ff", "#2563eb", 2, 10)
    s += Yazi(178, 70, "AZİMET (Normal Durum Hükmü)", 10.5, "#1d4ed8", "middle", True)
    az = [
        "• Zorluk ve zaruret bulunmayan normal şartlarda",
        "  her mükellefin uyması gereken asli hükümlerdir.",
        "• Örnek 1: Su varken abdest ve gusül almak.",
        "• Örnek 2: Mukimken 4 rekâtlı farz namazı tam kılmak.",
        "• Örnek 3: Ramazan ayında gününde oruç tutmak."
    ]
    for i, m in enumerate(az):
        s += Yazi(38, 94 + i * 20, m, 9, "#1e293b", "start", False)

    s += Ok(332, 125, 348, 125, "#1e3a8a", 2.5)

    s += Kutu(350, 48, 304, 154, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(502, 70, "RUHSAT (Kolaylaştırılmış Hüküm)", 10.5, "#047857", "middle", True)
    rh = [
        "• Hastalık, yolculuk, unutma veya zaruret gibi",
        "  meşakkat durumlarında tanınan geçici kolaylıklardır.",
        "• Örnek 1: Su yokken veya hastalıkta teyemmüm etmek.",
        "• Örnek 2: Yolculukta (seferîlikte) namazı 2 rekât kılmak.",
        "• Örnek 3: Yolcu ve hastanın orucu sonraya ertelemesi."
    ]
    for i, m in enumerate(rh):
        s += Yazi(362, 94 + i * 20, m, 9, "#1e293b", "start", False)

    s += Kutu(26, 212, 628, 30, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(340, 231, "Bakara Suresi 185: \"Allah sizin için kolaylık diler, zorluk dilemez.\" | Mecelle m. 17: \"Meşakkat teysîri celbeder.\"", 9.5, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HÜKÜMLERDE TEDRİCÎLİK (AŞAMALILIK) İLKESİ ÖRNEKLERİ", "#6d28d9")

    adimlar = [
        ("1. AŞAMA (Farkındalık)", "Nahl 67: Hurma ve üzümden", "elde edilen güzel rızık ve içki ayrımı", "#0284c7", "#e0f2fe"),
        ("2. AŞAMA (Zarar Vurgusu)", "Bakara 219: 'Büyük günah ve", "zararı faydasından çok daha büyüktür'", "#d97706", "#fef3c7"),
        ("3. AŞAMA (Kısmi Yasak)", "Nisâ 43: 'Sarhoşken ne dediğinizi", "bilinceye kadar namaza yaklaşmayın'", "#ea580c", "#ffedd5"),
        ("4. AŞAMA (Kesin Yasak)", "Mâide 90: 'İçki ve kumar şeytan", "işi pisliktir; ondan kesin kaçının!'", "#dc2626", "#fef2f2")
    ]

    kw = 148
    gap = 12
    sx = (W - (4 * kw + 3 * gap)) // 2
    for i, (bas, m1, m2, r, ar) in enumerate(adimlar):
        x = sx + i * (kw + gap)
        y = 50
        s += Kutu(x, y, kw, 136, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 20, bas, 9, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 66, m1, 8.8, "#1e293b", "middle", True)
        s += Yazi(x + kw // 2, y + 88, m2, 8.5, "#475569", "middle", False)
        if i < 3:
            s += Ok(x + kw, y + 68, x + kw + gap, y + 68, "#64748b", 2)

    s += Kutu(34, 198, W - 68, 36, "#f3e8ff", "#7c3aed", 1.5, 8)
    s += Yazi(W // 2, 220, "Tedricîlik Hikmeti: Toplumda kökleşmiş alışkanlıkları bir anda değil, zihinleri ve kalpleri hazırlayarak aşamalı değiştirmek.", 9.4, "#4c1d95", "middle", True)
    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "MECELLE'NİN KÜLLÎ KAİDELERİ VE FIKIH İLKELERİYLE İLİŞKİSİ", "#991b1b")

    kaideler = [
        ("Madde 2: \"Bir işten maksat ne ise hüküm ona göredir.\"", "Ameller niyetlere göredir hadisinin hukuki ifadesidir (Sübjektif/Niyet ilkesi).", "#2563eb", "#eff6ff"),
        ("Madde 17: \"Meşakkat teysîri celbeder.\"", "Zorluk kolaylığı getirir; darlık görüldükçe genişlik gösterilir (Kolaylık ilkesi).", "#059669", "#ecfdf5"),
        ("Madde 20-21: \"Zarar izâle olunur / Zaruretler memnû olan şeyleri mubah kılar.\"", "Hayati tehlike ve zaruret anında normalde yasak olan şey zaruret miktarınca caiz olur.", "#d97706", "#fef3c7"),
        ("Madde 58: \"Raiyye (halk) üzerine tasarruf maslahata menuttur.\"", "Yöneticilerin kararları kamu yararına (maslahata) bağlı olmak zorundadır.", "#7c3aed", "#faf5ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(kaideler):
        y = 46 + i * 48
        s += Kutu(24, y, 632, 42, ar, r, 1.5, 8)
        s += Yazi(38, y + 17, bas, 9.6, r, "start", True)
        s += Yazi(38, y + 34, acik, 9, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-fikih-3", 1, gorsel_1())
    kaydet("10-fikih-3", 2, gorsel_2())
    kaydet("10-fikih-3", 3, gorsel_3())
    kaydet("10-fikih-3", 4, gorsel_4())


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
