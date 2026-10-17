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
    s += Baslik(W, "SIMPLE PRESENT TENSE (GENİŞ ZAMAN) YAPI TABLOSU", "#1d4ed8")

    kartlar = [
        ("OLUMLU (+) CÜMLE", "#059669", "#ecfdf5", [
            "I / You / We / They + V1",
            "• I attend the robotics club.",
            "He / She / It + V-s / -es / -ies",
            "• She studies chemistry on Mondays."
        ]),
        ("OLUMSUZ (-) CÜMLE", "#dc2626", "#fef2f2", [
            "I / You / We / They + don't + V1",
            "• We don't wear a uniform on Fridays.",
            "He / She / It + doesn't + V1",
            "• He doesn't take the school bus."
        ]),
        ("SORU (?) CÜMLESİ", "#7c3aed", "#f3e8ff", [
            "Do + I / you / we / they + V1?",
            "• Do you revise your notes daily?",
            "Does + he / she / it + V1?",
            "• What time does the lesson start?"
        ])
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, r, ar, maddeler) in enumerate(kartlar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 162, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 10, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            kalin = j % 2 == 0
            renk = r if kalin else "#1e293b"
            s += Yazi(x + 12, y + 56 + j * 28, m, 9.2, renk, "start", kalin)

    s += Kutu(34, 220, W - 68, 28, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(W // 2, 238, "Dikkat: Olumsuz (doesn't) ve soru (Does...?) cümlelerinde fiildeki -s/-es/-ies takısı düşer, fiil yalın (V1) döner!", 9.6, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ADVERBS OF FREQUENCY (SIKLIK ZARFLARI) VE CÜMLEDEKİ YERİ", "#0f766e")

    zarflar = [
        ("ALWAYS", "%100", "Her zaman", "#047857", 60),
        ("USUALLY", "%85", "Genellikle", "#059669", 165),
        ("OFTEN", "%70", "Sık sık", "#0284c7", 270),
        ("SOMETIMES", "%50", "Bazen", "#d97706", 375),
        ("SELDOM / RARELY", "%15", "Nadiren", "#ea580c", 480),
        ("NEVER", "%0", "Asla / Hiç", "#dc2626", 585)
    ]

    for ad, yuzde, tr, r, cx in zarflar:
        s += Kutu(cx - 46, 50, 92, 96, "#ffffff", r, 2, 8)
        s += Kutu(cx - 46, 50, 92, 26, r, r, 1, 8)
        s += Yazi(cx, 67, yuzde, 10, "#ffffff", "middle", True)
        s += Yazi(cx, 100, ad, 9, r, "middle", True)
        s += Yazi(cx, 126, tr, 9, "#334155", "middle", False)

    s += Kutu(26, 158, 304, 84, "#eff6ff", "#2563eb", 1.5, 8)
    s += Yazi(178, 178, "1. Asıl Fiilden ÖNCE (Before Main Verb)", 10, "#1d4ed8", "middle", True)
    s += Yazi(178, 202, "Özne + Sıklık Zarfı + Fiil", 9.5, "#1e293b", "middle", True)
    s += Yazi(178, 224, "• I usually revise my lessons before exams.", 9.2, "#334155", "middle", False)

    s += Kutu(350, 158, 304, 84, "#fdf4ff", "#9333ea", 1.5, 8)
    s += Yazi(502, 178, "2. 'To Be' (am/is/are) Fiilinden SONRA", 10, "#7e22ce", "middle", True)
    s += Yazi(502, 202, "Özne + am / is / are + Sıklık Zarfı", 9.5, "#1e293b", "middle", True)
    s += Yazi(502, 224, "• She is never late for morning classes.", 9.2, "#334155", "middle", False)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "SCHOOL LIFE: DERSLER, OKUL KULÜPLERİ VE GÜNLÜK RUTİNLER", "#6d28d9")

    gruplar = [
        ("School Subjects (Dersler)", "#2563eb", "#dbeafe", [
            "Literature (Edebiyat) • History (Tarih)",
            "Geography (Coğrafya) • Philosophy (Felsefe)",
            "Physics / Chemistry / Biology (Fen)",
            "Physical Education / P.E. (Beden Eğitimi)"
        ]),
        ("School Clubs (Okul Kulüpleri)", "#059669", "#d1fae5", [
            "Science & Robotics Club (Bilim ve Robotik)",
            "Drama & Theatre Club (Tiyatro Kulübü)",
            "Debate Club (Münazara) • Chess Club (Satranç)",
            "Environmental / Eco Club (Çevre Kulübü)"
        ]),
        ("School Routines (Okul Rutinleri)", "#d97706", "#fef3c7", [
            "attend classes (derslere katılmak)",
            "take notes / revise for exams (tekrar yapmak)",
            "do experiments in the lab (deney yapmak)",
            "participate in extracurricular activities"
        ]),
        ("Time Prepositions (Zaman Edatları)", "#9333ea", "#f3e8ff", [
            "AT: saatler, night, noon, the weekend (at 8:30)",
            "ON: günler ve tarihler (on Monday, on Friday)",
            "IN: aylar, mevsimler, günün bölümleri",
            "   (in the morning, in October, in autumn)"
        ])
    ]

    kw, kh = 306, 94
    for i, (bas, r, ar, maddeler) in enumerate(gruplar):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 12)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 12, y + 20, bas, 10.2, r, "start", True)
        for j, m in enumerate(maddeler):
            s += Yazi(x + 12, y + 38 + j * 16, m, 8.8, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 245
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HE / SHE / IT ÖZNESİNDE FİİLE GELEN -S / -ES / -IES KURALLARI", "#b45309")

    kurallar = [
        ("1. Genel Kural (+s)", "Çoğu fiil doğrudan -s alır", "read → reads\nwork → works\nplay → plays", "#2563eb", "#eff6ff"),
        ("2. Sonu -ss, -sh, -ch, -x, -o (+es)", "Bu harflerle bitenler -es alır", "go → goes\nwatch → watches\nbrush → brushes", "#059669", "#ecfdf5"),
        ("3. Ünsüz + y (-ies)", "y düşer, yerine -ies gelir", "study → studies\ntry → tries\nfly → flies", "#9333ea", "#faf5ff"),
        ("4. Düzensiz (Have → Has)", "'have' fiili 'has' olur", "I have lunch.\nShe has lunch\nat the canteen.", "#dc2626", "#fef2f2")
    ]

    kw = 150
    gap = 12
    sx = (W - (4 * kw + 3 * gap)) // 2
    for i, (bas, acik, orn, r, ar) in enumerate(kurallar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 178, ar, r, 1.5, 8)
        s += Kutu(x, y, kw, 32, r, r, 1, 8)
        s += Yazi(x + kw // 2, y + 20, bas, 8.8, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 54, acik, 8.8, "#475569", "middle", False)
        for j, satir in enumerate(orn.split("\n")):
            s += Yazi(x + kw // 2, y + 88 + j * 24, satir, 9.8, r, "middle", True)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-ingilizce-3", 1, gorsel_1())
    kaydet("10-ingilizce-3", 2, gorsel_2())
    kaydet("10-ingilizce-3", 3, gorsel_3())
    kaydet("10-ingilizce-3", 4, gorsel_4())


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
