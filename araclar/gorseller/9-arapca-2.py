from ozet_gorsel import svg

C = {
    "lacivert": "#1e293b",
    "mavi": "#1d4ed8",
    "acik_mavi": "#eff6ff",
    "yesil": "#15803d",
    "acik_yesil": "#f0fdf4",
    "sari": "#a16207",
    "acik_sari": "#fefce8",
    "kirmizi": "#b91c1c",
    "acik_kirmizi": "#fef2f2",
    "mor": "#7e22ce",
    "turkuaz": "#0f766e",
    "turuncu": "#c2410c",
    "beyaz": "#ffffff",
    "koyu": "#1e293b",
    "gri": "#475569",
    "acik_gri": "#f8fafc",
}


def kutu(x, y, w, h, fill, stroke="none", sw=1, rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def metin(x, y, t, size=11, fill="#1e293b", weight="normal", anchor="middle"):
    fw = "700" if weight == "bold" else "400"
    t_esc = str(t).replace("&", "&amp;")
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{fw}" fill="{fill}">{t_esc}</text>'


def ok(x1, y1, x2, y2, stroke="#1e293b", sw=2):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'
        f'<polygon points="{x2},{y2} {x2-6},{y2-4} {x2-6},{y2+4}" fill="{stroke}"/>'
    )


def gorsel_1():
    w, h = 580, 225
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "SELAMLAŞMA, HÂL HATIR SORMA VE VEDA (التَّحِيَّة)", 13, C["beyaz"], "bold"))

    pairs = [
        ("Genel Selam", "السَّلَامُ عَلَيْكُمْ", "وَعَلَيْكُمُ السَّلَامُ", C["mavi"], C["acik_mavi"]),
        ("Sabah Selamı", "صَبَاحُ الْخَيْرِ", "صَبَاحُ النُّورِ", C["turuncu"], C["acik_sari"]),
        ("Karşılama", "أَهْلًا وَسَهْلًا / مَرْحَبًا", "أَهْلًا بِكَ / أَهْلًا بِكِ", C["yesil"], C["acik_yesil"]),
        ("Hâl Hatır", "كَيْفَ حَالُكَ؟", "أَنَا بِخَيْرٍ، الْحَمْدُ لِلَّهِ", C["mor"], C["acik_mavi"]),
        ("Vedalaşma", "إِلَى اللِّقَاءِ", "فِي أَمَانِ اللَّهِ / مَعَ السَّلَامَةِ", C["turkuaz"], C["acik_yesil"]),
    ]
    for i, (etiket, sol, sag, cb, cbg) in enumerate(pairs):
        y = 52 + i * 33
        ic.append(kutu(18, y, 120, 27, cb, rx=5))
        ic.append(metin(78, y + 18, etiket, 10, C["beyaz"], "bold"))
        ic.append(kutu(146, y, 190, 27, cbg, cb, 1, rx=5))
        ic.append(metin(241, y + 18, sol, 11.5, C["koyu"], "bold"))
        ic.append(ok(340, y + 14, 364, y + 14, cb, 1.8))
        ic.append(kutu(368, y, 194, 27, C["beyaz"], cb, 1.2, rx=5))
        ic.append(metin(465, y + 18, sag, 11.5, cb, "bold"))

    return svg(w, h, "".join(ic), "Arapça selamlaşma, karşılama, hâl hatır sorma ve vedalaşma kalıpları")


def gorsel_2():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mor"], rx=8))
    ic.append(metin(290, 33, "SINIF İÇİ YÖNERGELER: MÜZEKKER VE MÜENNES HİTAP", 12.5, C["beyaz"], "bold"))

    ic.append(kutu(18, 54, 265, 152, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(150, 74, "Erkeğe Hitap (Sonu Sükûnlu: ـْ)", 11, C["mavi"], "bold"))
    m_list = [
        ("اِسْتَمِعْ يَا أَحْمَدُ", "Dinle ey Ahmed!"),
        ("أَعِدْ يَا خَالِدُ", "Tekrar et ey Hâlid!"),
        ("اِقْرَأْ يَا عَلِيُّ", "Oku ey Ali!"),
        ("اُكْتُبْ يَا مُحَمَّدُ", "Yaz ey Muhammed!"),
    ]
    for i, (ar, tr) in enumerate(m_list):
        y = 98 + i * 26
        ic.append(kutu(28, y - 14, 125, 21, C["beyaz"], C["mavi"], 1, rx=4))
        ic.append(metin(90, y, ar, 11, C["koyu"], "bold"))
        ic.append(metin(162, y, tr, 9.8, C["gri"], "normal", "start"))

    ic.append(kutu(297, 54, 265, 152, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(metin(430, 74, "Kadına Hitap (Sonu Yâ'lı: ـِي)", 11, C["yesil"], "bold"))
    f_list = [
        ("يَا زَيْنَبُ اِسْتَمِعِي", "Ey Zeyneb dinle!"),
        ("يَا عَائِشَةُ أَعِيدِي", "Ey Âişe tekrar et!"),
        ("يَا فَاطِمَةُ اِقْرَئِي", "Ey Fâtıma oku!"),
        ("يَا مَرْيَمُ اُكْتُبِي", "Ey Meryem yaz!"),
    ]
    for i, (ar, tr) in enumerate(f_list):
        y = 98 + i * 26
        ic.append(kutu(307, y - 14, 130, 21, C["beyaz"], C["yesil"], 1, rx=4))
        ic.append(metin(372, y, ar, 11, C["koyu"], "bold"))
        ic.append(metin(445, y, tr, 9.8, C["gri"], "normal", "start"))

    return svg(w, h, "".join(ic), "Sınıf içi emir fiillerinin müzekker ve müennes hitap biçimleri")


def gorsel_3():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turkuaz"], rx=8))
    ic.append(metin(290, 33, "KENDİNDEN SONRAKİ HARFE BİTİŞMEYEN 6 HARF (ا د ذ ر ز و)", 12, C["beyaz"], "bold"))

    harfler = [
        ("ا / أ", "أَكَلَ • سَأَلَ", C["mavi"]),
        ("د", "دَخَلَ • لَدَبَ", C["yesil"]),
        ("ذ", "ذَهَبَ • أَخَذَ", C["mor"]),
        ("ر", "بَطَرَ • حَرَشَ", C["turuncu"]),
        ("ز", "هَرَزَ • لَزَنَ", C["kirmizi"]),
        ("و", "وَصَلَ • دَوَجَ", C["lacivert"]),
    ]
    for i, (h_ar, ex, col) in enumerate(harfler):
        x = 16 + i * 92
        ic.append(kutu(x, 56, 84, 96, C["beyaz"], col, 2, rx=8))
        ic.append(kutu(x + 8, 64, 68, 28, col, rx=5))
        ic.append(metin(x + 42, 83, h_ar, 13, C["beyaz"], "bold"))
        ic.append(metin(x + 42, 115, "Örnek:", 9.5, C["gri"]))
        ic.append(metin(x + 42, 136, ex, 10.5, C["koyu"], "bold"))

    ic.append(kutu(18, 164, 544, 38, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(290, 187, "Kural: Bu 6 harf sağdan önceki harfe bitişir, soldan sonraki harfe bitişmez.", 10.5, C["koyu"], "bold"))

    return svg(w, h, "".join(ic), "Kendisinden sonraki harfe bitişmeyen altı harf ve kelime örnekleri")


def gorsel_4():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mavi"], rx=8))
    ic.append(metin(290, 33, "KISA ÜNLÜLER (الحَرَكَات) VE SÜKÛN (السُّكُون)", 13, C["beyaz"], "bold"))

    boxes = [
        ("Fetha (ـَ)", "e / a sesi verir", "كَتَبَ • قَرَأَ • سَلِمَ", C["turuncu"], C["acik_sari"]),
        ("Damme (ـُ)", "u / ü sesi verir", "حَسُنَ • ضُرِبَ • شُكِرَ", C["mavi"], C["acik_mavi"]),
        ("Kesra (ـِ)", "i / ı sesi verir", "عَلِمَ • سَمِعَ • حَمِدَ", C["yesil"], C["acik_yesil"]),
        ("Sükûn (ـْ)", "Ünlüsüz bağlantı", "أَيْ • لَمْ • أَنْ • هَلْ • قِفْ", C["mor"], C["acik_kirmizi"]),
    ]
    for i, (title, sub, ex, cb, cbg) in enumerate(boxes):
        x = 16 + i * 138
        ic.append(kutu(x, 56, 130, 144, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 8, 65, 114, 26, cb, rx=5))
        ic.append(metin(x + 65, 82, title, 11, C["beyaz"], "bold"))
        ic.append(metin(x + 65, 112, sub, 10, C["koyu"], "bold"))
        ic.append(kutu(x + 8, 128, 114, 56, C["beyaz"], cb, 1, rx=5))
        ic.append(metin(x + 65, 160, ex, 11, cb, "bold"))

    return svg(w, h, "".join(ic), "Kısa ünlüler fetha, damme, kesra ve sükûn örnekleri")


def gorsel_5():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["yesil"], rx=8))
    ic.append(metin(290, 33, "ŞEDDE (الشَّدَّة — ـّ): İKİ AYNI HARFİN BİRLEŞMESİ", 13, C["beyaz"], "bold"))

    items = [
        ("مَ + دْ + دَ", "مَدَّ", "Uzattı", C["mavi"]),
        ("شَ + دْ + دَ", "شَدَّ", "Sıktı / Bağladı", C["mor"]),
        ("كُ + لْ + لُ", "كُلُّ", "Hepsi / Her", C["yesil"]),
        ("صَ + دْ + دَ + قَ", "صَدَّقَ", "Doğruladı", C["turuncu"]),
    ]
    for i, (acik, birlesik, anlam, col) in enumerate(items):
        x = 16 + i * 138
        ic.append(kutu(x, 56, 130, 144, C["acik_gri"], col, 1.5, rx=8))
        ic.append(metin(x + 65, 78, acik, 11.5, C["koyu"], "bold"))
        ic.append(metin(x + 65, 98, "↓", 13, col, "bold"))
        ic.append(kutu(x + 18, 106, 94, 34, col, rx=6))
        ic.append(metin(x + 65, 128, birlesik, 14, C["beyaz"], "bold"))
        ic.append(metin(x + 65, 166, anlam, 10, C["gri"], "bold"))
        ic.append(metin(x + 65, 184, "(1. sükûn + 2. hareke)", 8.8, C["gri"]))

    return svg(w, h, "".join(ic), "Şeddeli kelimelerin harf çözümlemesi ve birleştirilmesi")


def gorsel_6():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turuncu"], rx=8))
    ic.append(metin(290, 33, "TENVİN (التَّنْوِين): ÜÇ TENVİN TÜRÜ VE YAZIM KURALI", 13, C["beyaz"], "bold"))

    cols = [
        ("Tenvînü'l-Feth (ـًا / ـً)", "-en / -an sesi", C["kirmizi"], C["acik_kirmizi"], [
            "أَبًا • بَيْتًا • قَوْمًا",
            "مَرْحَبًا • أَهْلًا",
            "زَهْرَةً • مُدَرِّسَةً (elif yok!)",
        ]),
        ("Tenvînü'd-Damm (ـٌ)", "-un / -ün sesi", C["mavi"], C["acik_mavi"], [
            "أَبٌ • بَيْتٌ • دَرْسٌ",
            "قَلَمٌ • دَفْتَرٌ • بِنْتٌ",
            "زَهْرَةٌ • مُدَرِّسَةٌ",
        ]),
        ("Tenvînü'l-Kesr (ـٍ)", "-in / -ın sesi", C["yesil"], C["acik_yesil"], [
            "أَبٍ • بَيْتٍ • خَوْفٍ",
            "نَفْسٍ • بِخَيْرٍ",
            "زَهْرَةٍ • وَرْدَةٍ",
        ]),
    ]
    for i, (head, sub, cb, cbg, exs) in enumerate(cols):
        x = 18 + i * 184
        ic.append(kutu(x, 54, 174, 152, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 8, 62, 158, 24, cb, rx=5))
        ic.append(metin(x + 87, 78, head, 10, C["beyaz"], "bold"))
        ic.append(metin(x + 87, 102, sub, 10, cb, "bold"))
        for j, ex in enumerate(exs):
            ic.append(kutu(x + 8, 112 + j * 28, 158, 23, C["beyaz"], cb, 1, rx=4))
            ic.append(metin(x + 87, 128 + j * 28, ex, 10, C["koyu"], "bold"))

    return svg(w, h, "".join(ic), "Fetha, damme ve kesra tenvini örnekleri ve yuvarlak ta kuralı")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = gorsel_1()
    b[1]["gorsel"] = gorsel_2()
    b[2]["gorsel"] = gorsel_3()
    b[3]["gorsel"] = gorsel_4()
    b[4]["gorsel"] = gorsel_5()
    b[5]["gorsel"] = gorsel_6()
