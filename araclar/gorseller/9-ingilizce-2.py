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


def cizgi(x1, y1, x2, y2, stroke="#64748b", sw=1.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'


def ok(x1, y1, x2, y2, stroke="#1e293b", sw=2):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'
        f'<polygon points="{x2},{y2} {x2-6},{y2-4} {x2-6},{y2+4}" fill="{stroke}"/>'
    )


def gorsel_1():
    w, h = 580, 230
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "REVISION 1: SCHOOL EVENTS, OBLIGATIONS & QUESTION TAGS", 13, C["beyaz"], "bold"))

    ic.append(kutu(18, 56, 265, 160, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(150, 76, "Key Vocabulary (School Event)", 12, C["lacivert"], "bold"))
    words = [
        ("assignment", "verilen ödev / görev"),
        ("lecture", "öğretici resmi konuşma / ders"),
        ("perform", "sahnelemek (oyun / şarkı)"),
        ("script", "oyun / film metni (senaryo)"),
        ("creative", "yaratıcı, özgün fikirli"),
    ]
    for i, (en, tr) in enumerate(words):
        y = 98 + i * 22
        ic.append(kutu(28, y - 13, 85, 18, C["mavi"], rx=4))
        ic.append(metin(70, y, en, 10, C["beyaz"], "bold"))
        ic.append(metin(122, y, tr, 10, C["koyu"], "normal", "start"))

    ic.append(kutu(297, 56, 265, 160, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(430, 76, "Obligations & Question Tags", 12, C["koyu"], "bold"))
    ic.append(kutu(309, 86, 240, 54, C["beyaz"], C["sari"], 1, rx=6))
    ic.append(metin(429, 103, "must / have to / need to + V1", 11, C["kirmizi"], "bold"))
    ic.append(metin(429, 120, "Geçmiş zorunluluk: had to + V1", 10, C["koyu"]))
    ic.append(metin(429, 134, "We must set the stage today.", 9.5, C["gri"]))

    ic.append(kutu(309, 148, 240, 58, C["beyaz"], C["yesil"], 1, rx=6))
    ic.append(metin(429, 165, "Question Tags (+ → - / - → +)", 11, C["yesil"], "bold"))
    ic.append(metin(429, 182, "You are ready, aren't you?", 10, C["koyu"]))
    ic.append(metin(429, 198, "She didn't forget the script, did she?", 9.5, C["gri"]))

    return svg(w, h, "".join(ic), "Revision 1 okul etkinlikleri kelimeleri, zorunluluk kipleri ve eklenti soruları")


def gorsel_2():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mor"], rx=8))
    ic.append(metin(290, 33, "A WEEKEND WITHOUT PHONES: USED TO vs. PAST TENSES", 13, C["beyaz"], "bold"))

    ic.append(kutu(20, 56, 250, 148, C["acik_kirmizi"], C["kirmizi"], 1.5, rx=8))
    ic.append(metin(145, 76, "PAST HABITS (used to + V1)", 12, C["kirmizi"], "bold"))
    ic.append(metin(145, 96, "Eskiden yapılan alışkanlıklar", 10, C["gri"]))
    ic.append(kutu(32, 108, 226, 38, C["beyaz"], C["kirmizi"], 1, rx=5))
    ic.append(metin(145, 124, "We used to look at our screens", 10, C["koyu"], "bold"))
    ic.append(metin(145, 139, "quietly at breakfast.", 10, C["koyu"]))
    ic.append(kutu(32, 154, 226, 38, C["beyaz"], C["kirmizi"], 1, rx=5))
    ic.append(metin(145, 170, "I used to stay alone in my room", 10, C["koyu"], "bold"))
    ic.append(metin(145, 185, "when guests came.", 10, C["koyu"]))

    ic.append(ok(275, 130, 305, 130, C["lacivert"], 2.5))

    ic.append(kutu(310, 56, 250, 148, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(metin(435, 76, "PHONE-FREE WEEKEND", 12, C["yesil"], "bold"))
    ic.append(metin(435, 96, "Past Continuous & Past Simple", 10, C["gri"]))
    ic.append(kutu(322, 108, 226, 38, C["beyaz"], C["yesil"], 1, rx=5))
    ic.append(metin(435, 124, "While we were eating breakfast,", 10, C["koyu"], "bold"))
    ic.append(metin(435, 139, "we talked and laughed together.", 10, C["koyu"]))
    ic.append(kutu(322, 154, 226, 38, C["beyaz"], C["yesil"], 1, rx=5))
    ic.append(metin(435, 170, "We spent time with guests and", 10, C["koyu"], "bold"))
    ic.append(metin(435, 185, "visited Cousin Tom's smart home.", 10, C["koyu"]))

    return svg(w, h, "".join(ic), "Telefonsuz hafta sonu metninde used to ile geçmiş zamanların karşılaştırması")


def gorsel_3():
    w, h = 580, 225
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turkuaz"], rx=8))
    ic.append(metin(290, 33, "REVISION 2: COUNTRYSIDE vs. CITY & PRESENT PERFECT", 13, C["beyaz"], "bold"))

    ic.append(kutu(18, 56, 175, 155, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(metin(105, 76, "COUNTRYSIDE (Kırsal)", 11.5, C["yesil"], "bold"))
    ic.append(metin(105, 98, "+ Less noise & stress", 10, C["koyu"]))
    ic.append(metin(105, 116, "+ More peace & nature", 10, C["koyu"]))
    ic.append(metin(105, 134, "+ Affordable housing", 10, C["koyu"]))
    ic.append(cizgi(30, 146, 180, 146, C["yesil"], 1))
    ic.append(metin(105, 164, "- Fewer medical services", 9.5, C["kirmizi"]))
    ic.append(metin(105, 182, "- Fewer transport options", 9.5, C["kirmizi"]))

    ic.append(kutu(202, 56, 175, 155, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(290, 76, "CITY (Şehir)", 11.5, C["mavi"], "bold"))
    ic.append(metin(290, 98, "+ More hospitals", 10, C["koyu"]))
    ic.append(metin(290, 116, "+ More public transport", 10, C["koyu"]))
    ic.append(metin(290, 134, "+ Sports & food festivals", 10, C["koyu"]))
    ic.append(cizgi(214, 146, 364, 146, C["mavi"], 1))
    ic.append(metin(290, 164, "- Noise & air pollution", 9.5, C["kirmizi"]))
    ic.append(metin(290, 182, "- Heavy traffic & stress", 9.5, C["kirmizi"]))

    ic.append(kutu(386, 56, 176, 155, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(474, 76, "EXPERIENCE vs. PAST", 11, C["koyu"], "bold"))
    ic.append(kutu(396, 86, 156, 54, C["beyaz"], C["sari"], 1, rx=5))
    ic.append(metin(474, 102, "Present Perfect", 10, C["mor"], "bold"))
    ic.append(metin(474, 118, "Have you ever tried", 9.5, C["koyu"]))
    ic.append(metin(474, 132, "spicy Turkish kebab?", 9.5, C["koyu"]))
    ic.append(kutu(396, 148, 156, 54, C["beyaz"], C["turuncu"], 1, rx=5))
    ic.append(metin(474, 164, "Past Simple (Belirli Zaman)", 9.5, C["turuncu"], "bold"))
    ic.append(metin(474, 180, "I tried it in İstanbul", 9.5, C["koyu"]))
    ic.append(metin(474, 194, "last year.", 9.5, C["koyu"]))

    return svg(w, h, "".join(ic), "Kırsal ve şehir yaşamı karşılaştırması ile Present Perfect ve Past Simple farkı")


def gorsel_4():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["yesil"], rx=8))
    ic.append(metin(290, 33, "OUR EARTH NEEDS US: DISASTERS & FUTURE TECH", 13, C["beyaz"], "bold"))

    ic.append(kutu(18, 55, 265, 150, C["acik_kirmizi"], C["kirmizi"], 1.5, rx=8))
    ic.append(metin(150, 75, "Natural Disasters & Aid", 12, C["kirmizi"], "bold"))
    disasters = [
        "earthquake (deprem) • flood (sel)",
        "landslide (heyelan) • volcano (yanardağ)",
        "forest fire (orman yangını)",
        "storm / hurricane • tsunami",
    ]
    for i, d in enumerate(disasters):
        ic.append(metin(150, 96 + i * 19, d, 10, C["koyu"]))
    ic.append(kutu(30, 170, 240, 26, C["beyaz"], C["kirmizi"], 1, rx=5))
    ic.append(metin(150, 187, "rescue teams & charities → help homeless", 9.5, C["kirmizi"], "bold"))

    ic.append(kutu(297, 55, 265, 150, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(430, 75, "Future Predictions & Type 1 If", 12, C["lacivert"], "bold"))
    ic.append(kutu(309, 86, 240, 50, C["beyaz"], C["mavi"], 1, rx=5))
    ic.append(metin(429, 103, "will + V1 (Gelecek Teknolojileri)", 10, C["mavi"], "bold"))
    ic.append(metin(429, 118, "Drones & robots will find people.", 9.5, C["koyu"]))
    ic.append(metin(429, 131, "Air-taxis will use batteries, not fuel.", 9.5, C["koyu"]))

    ic.append(kutu(309, 144, 240, 52, C["beyaz"], C["yesil"], 1, rx=5))
    ic.append(metin(429, 161, "If + Present Simple, will/can + V1", 10, C["yesil"], "bold"))
    ic.append(metin(429, 177, "If we plant trees and use clean energy,", 9.5, C["koyu"]))
    ic.append(metin(429, 190, "we will protect our Earth.", 9.5, C["koyu"]))

    return svg(w, h, "".join(ic), "Doğal afetler söz varlığı ile gelecek zaman ve birinci tip koşul cümleleri")


def gorsel_5():
    w, h = 580, 230
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "GRAMMAR SUMMARY (REVISION 1 & REVISION 2)", 13, C["beyaz"], "bold"))

    rows = [
        ("Must / Have to / Need to", "Zorunluluk ve gereklilik", "We must follow the rules. / He had to study.", C["mavi"]),
        ("Used to + V1", "Geçmişteki alışkanlıklar", "I used to play outside every day.", C["mor"]),
        ("Past Simple vs. Continuous", "Tamamlanan vs. süregelen", "While we were eating, we talked.", C["turuncu"]),
        ("Present Perfect Tense", "Deneyim / yakın geçmiş", "Have you ever tried it? / I have just arrived.", C["yesil"]),
        ("Will & First Conditional", "Gelecek tahmini ve koşul", "If we use batteries, we will stop pollution.", C["turkuaz"]),
    ]
    for i, (title, desc, ex, col) in enumerate(rows):
        y = 54 + i * 33
        ic.append(kutu(18, y, 165, 28, col, rx=5))
        ic.append(metin(100, y + 18, title, 10, C["beyaz"], "bold"))
        ic.append(kutu(188, y, 145, 28, C["acik_gri"], col, 1, rx=5))
        ic.append(metin(260, y + 18, desc, 9.5, C["koyu"], "bold"))
        ic.append(kutu(338, y, 224, 28, C["beyaz"], col, 1, rx=5))
        ic.append(metin(450, y + 18, ex, 9.5, C["koyu"]))

    return svg(w, h, "".join(ic), "Revision 1 ve Revision 2 dil bilgisi yapılarının özet tablosu")


def gorsel_6():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turuncu"], rx=8))
    ic.append(metin(290, 33, "KEY COLLOCATIONS & EXPRESSIONS", 13, C["beyaz"], "bold"))

    cols = [
        ("School & Projects", C["mavi"], C["acik_mavi"], [
            "perform a musical play",
            "set the stage",
            "practise the script/lines",
            "collect data via a survey",
        ]),
        ("Lifestyle & Health", C["mor"], C["acik_sari"], [
            "spend time with family",
            "apply for a swimming race",
            "try local cuisines",
            "put on weight / lose weight",
        ]),
        ("Environment & Tech", C["yesil"], C["acik_yesil"], [
            "natural disasters",
            "rescue teams & charities",
            "noise / air pollution",
            "self-driving electric cars",
        ]),
    ]
    for i, (head, c_border, c_bg, items) in enumerate(cols):
        x = 18 + i * 184
        ic.append(kutu(x, 54, 174, 148, c_bg, c_border, 1.5, rx=8))
        ic.append(kutu(x + 8, 62, 158, 24, c_border, rx=5))
        ic.append(metin(x + 87, 78, head, 10.5, C["beyaz"], "bold"))
        for j, it in enumerate(items):
            ic.append(metin(x + 87, 106 + j * 23, "• " + it, 9.8, C["koyu"], "bold"))

    return svg(w, h, "".join(ic), "Revision 1 ve Revision 2 ünitelerindeki önemli eşdizimli ifadeler")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = gorsel_1()
    b[1]["gorsel"] = gorsel_2()
    b[2]["gorsel"] = gorsel_3()
    b[3]["gorsel"] = gorsel_4()
    b[4]["gorsel"] = gorsel_5()
    b[5]["gorsel"] = gorsel_6()
