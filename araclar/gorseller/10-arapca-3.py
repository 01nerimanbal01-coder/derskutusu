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
    s += Baslik(W, "ARAPÇADA AKRABA İSİMLERİ (أَقَارِبِي — AKRABALARIM)", "#0f766e")

    sol = [
        ("Baba Tarafı (طَرَفُ الْأَبِ)", "#0284c7", "#e0f2fe", [
            "الْجَدُّ (el-ceddü): Dede",
            "الْجَدَّةُ (el-ceddetü): Babaanne / Nine",
            "الْعَمُّ (el-ammü): Amca",
            "الْعَمَّةُ (el-ammetü): Hala"
        ]),
        ("Anne Tarafı (طَرَفُ الْأُمِّ)", "#059669", "#d1fae5", [
            "الْخَالُ (el-hâlü): Dayı",
            "الْخَالَةُ (el-hâletü): Teyze",
            "اِبْنُ الْخَالِ (ibnü'l-hâl): Dayı oğlu",
            "بِنْتُ الْخَالَةِ (bintü'l-hâle): Teyze kızı"
        ])
    ]

    for i, (bas, r, ar, maddeler) in enumerate(sol):
        x = 26 + i * 320
        y = 48
        s += Kutu(x, y, 308, 156, ar, r, 2, 10)
        s += Kutu(x, y, 308, 32, r, r, 1, 10)
        s += Yazi(x + 154, y + 21, bas, 10.5, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            s += Yazi(x + 18, y + 58 + j * 26, "• " + m, 9.8, "#1e293b", "start", True)

    s += Kutu(26, 214, 628, 34, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(340, 235, "Diğer Akrabalar: الْحَفِيدُ (Erkek torun) • الْحَفِيدَةُ (Kız torun) • اِبْنُ الْعَمِّ (Amca oğlu / Kuzen)", 9.8, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 265
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TEKİL (مُفْرَد), İKİL (مُثَنَّى) VE KURALLI ÇOĞUL (جَمْع) İSİMLER", "#1d4ed8")

    kolonlar = [
        ("1. TEKİL (الْمُفْرَدُ)", "#475569", "#f1f5f9", [
            "Bir varlığı gösterir:",
            "• مُعَلِّمٌ (Bir erkek öğretmen)",
            "• مُعَلِّمَةٌ (Bir kadın öğretmen)",
            "• مُهَنْدِسٌ (Bir erkek mühendis)",
            "• طَبِيبَةٌ (Bir kadın doktor)"
        ]),
        ("2. İKİL / TESNİYE (الْمُثَنَّى)", "#2563eb", "#dbeafe", [
            "Sonuna ـَانِ (-âni) eklenir:",
            "• مُعَلِّمَانِ (İki erkek öğretmen)",
            "• مُعَلِّمَتَانِ (İki kadın öğretmen)",
            "• مُهَنْدِسَانِ (İki erkek mühendis)",
            "• طَبِيبَتَانِ (İki kadın doktor)"
        ]),
        ("3. KURALLI ÇOĞUL (الْجَمْعُ)", "#059669", "#d1fae5", [
            "Eril: ـُونَ (-ûne) | Dişil: ـَاتٌ (-âtün):",
            "• مُعَلِّمُونَ (Erkek öğretmenler)",
            "• مُعَلِّمَاتٌ (Kadın öğretmenler)",
            "• مُهَنْدِسُونَ (Erkek mühendisler)",
            "• طَبِيبَاتٌ (Kadın doktorlar)"
        ])
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, r, ar, maddeler) in enumerate(kolonlar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 200, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 10, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            s += Yazi(x + 12, y + 58 + j * 30, m, 9.5, "#1e293b", "start", j == 0)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İŞARET İSİMLERİ (أَسْمَاءُ الْإِشَارَةِ) VE KİŞİ ZAMİRLERİ", "#6d28d9")

    satirlar = [
        ("TEKİL ERİL (المفرد المذكر)", "هٰذَا (Hâzâ - Bu)", "هُوَ (Hüve - O)", "هٰذَا عَمِّي، هُوَ مُهَنْدِسٌ.", "#2563eb", "#eff6ff"),
        ("TEKİL DİŞİL (المفرد المؤنث)", "هٰذِهِ (Hâzihî - Bu)", "هِيَ (Hiye - O)", "هٰذِهِ خَالَتِي، هِيَ مُمَرِّضَةٌ.", "#0891b2", "#ecfeff"),
        ("İKİL ERİL (المثنى المذكر)", "هٰذَانِ (Hâzâni - Bu ikisi)", "هُمَا (Hümâ - O ikisi)", "هٰذَانِ عَمَّانِ، هُمَا فَلَّاحَانِ.", "#059669", "#ecfdf5"),
        ("İKİL DİŞİL (المثنى المؤنث)", "هٰتَانِ (Hâtâni - Bu ikisi)", "هُمَا (Hümâ - O ikisi)", "هٰتَانِ خَالَتَانِ، هُمَا خَيَّاطَتَانِ.", "#d97706", "#fffbeb"),
        ("ÇOĞUL (الجمع العاقل)", "هٰؤُلَاءِ (Hâülâi - Bunlar)", "هُمْ / هُنَّ (Hüm / Hünne)", "هٰؤُلَاءِ أَقَارِبِي، هُمْ طَيَّارُونَ.", "#9333ea", "#faf5ff")
    ]

    for i, (tur, isaret, zamir, orn, r, ar) in enumerate(satirlar):
        y = 46 + i * 38
        s += Kutu(22, y, 636, 32, ar, r, 1.5, 6)
        s += Yazi(34, y + 20, tur, 9.2, r, "start", True)
        s += Yazi(220, y + 20, isaret, 9.5, "#1e293b", "start", True)
        s += Yazi(375, y + 20, zamir, 9.5, "#1e293b", "start", True)
        s += Yazi(644, y + 20, orn, 9.8, "#0f172a", "end", True)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "MESLEKLER (الْمِهَنُ) VE ÇALIŞMA YERLERİ (أَمَاكِنُ الْعَمَلِ)", "#b45309")

    meslekler = [
        ("طَبِيبٌ / مُمَرِّضَةٌ (Doktor / Hemşire)", "يَعْمَلُ فِي الْمُسْتَشْفَى (Hastanede çalışır)", "#dc2626", "#fef2f2"),
        ("مُعَلِّمٌ / مُدَرِّسَةٌ (Öğretmen)", "يَعْمَلُ فِي الْمَدْرَسَةِ (Okulda çalışır)", "#2563eb", "#eff6ff"),
        ("مُهَنْدِسٌ / عَامِلٌ (Mühendis / İşçi)", "يَعْمَلُ فِي الْمَصْنَعِ / الشَّرِكَةِ (Fabrikada / Şirkette)", "#d97706", "#fef3c7"),
        ("طَيَّارٌ / مُضِيفٌ (Pilot / Hostes)", "يَعْمَلُ فِي الْمَطَارِ / الطَّائِرَةِ (Havalimanında / Uçakta)", "#0284c7", "#e0f2fe"),
        ("فَلَّاحٌ / مُزَارِعٌ (Çiftçi)", "يَعْمَلُ فِي الْحَقْلِ / الْمَزْرَعَةِ (Tarlada / Çiftlikte)", "#059669", "#ecfdf5"),
        ("خَبَّازٌ / خَيَّاطٌ (Fırıncı / Terzi)", "يَعْمَلُ فِي الْمَخْبَزِ / الدُّكَّانِ (Fırında / Dükkânda)", "#7c3aed", "#f3e8ff")
    ]

    kw, kh = 306, 56
    for i, (m, yer, r, ar) in enumerate(meslekler):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 10)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 12, y + 21, m, 9.5, r, "start", True)
        s += Yazi(x + 12, y + 41, yer, 9.2, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-arapca-3", 1, gorsel_1())
    kaydet("10-arapca-3", 2, gorsel_2())
    kaydet("10-arapca-3", 3, gorsel_3())
    kaydet("10-arapca-3", 4, gorsel_4())


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
