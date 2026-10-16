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
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "KUR'AN-I KERİM OKUMA ADABI VE SAYGI İLKELERİ", 13, C["beyaz"], "bold"))

    steps = [
        ("1. Hazırlık", "İbadet bilinciyle", "abdestli olmak", C["mavi"], C["acik_mavi"]),
        ("2. Başlangıç", "Euzübesmele", "ile başlamak", C["yesil"], C["acik_yesil"]),
        ("3. Tilavet", "Samimiyet, huşu", "ve tedebbür", C["mor"], C["acik_sari"]),
        ("4. Tamamlama", "Sadakallahülazim", "diyerek bitirmek", C["turuncu"], C["acik_kirmizi"]),
    ]
    for i, (st, l1, l2, cb, cbg) in enumerate(steps):
        x = 16 + i * 138
        ic.append(kutu(x, 56, 130, 96, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 10, 64, 110, 24, cb, rx=5))
        ic.append(metin(x + 65, 80, st, 10.5, C["beyaz"], "bold"))
        ic.append(metin(x + 65, 108, l1, 10, C["koyu"], "bold"))
        ic.append(metin(x + 65, 126, l2, 10, C["gri"]))

    ic.append(kutu(18, 164, 544, 42, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(290, 182, "Kültürümüzde Mushaf'a Saygı:", 10.5, C["lacivert"], "bold"))
    ic.append(metin(290, 198, "Mushaf'ı belden yukarıda tutmak • Gelin çeyizlerinde Mushaf bulundurmak • Düzenli okumak", 9.8, C["koyu"]))

    return svg(w, h, "".join(ic), "Kur'an-ı Kerim okuma adabı aşamaları ve Mushaf'a saygı ilkeleri")


def gorsel_2():
    w, h = 580, 210
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["yesil"], rx=8))
    ic.append(metin(290, 33, "EUZÜBESMELE VE SADAKALLAHÜLAZİM", 13, C["beyaz"], "bold"))

    ic.append(kutu(20, 56, 260, 138, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(kutu(34, 66, 232, 24, C["yesil"], rx=5))
    ic.append(metin(150, 82, "Okumaya Başlarken: Euzübesmele", 10.5, C["beyaz"], "bold"))
    ic.append(metin(150, 108, "Eûzü billâhi mineşşeytânirracîm", 10, C["koyu"], "bold"))
    ic.append(metin(150, 124, "(Kovulmuş şeytandan Allah'a sığınırım)", 9.5, C["gri"]))
    ic.append(metin(150, 148, "Bismillâhirrahmânirrahîm", 10, C["koyu"], "bold"))
    ic.append(metin(150, 164, "(Rahman ve Rahîm Allah'ın adıyla)", 9.5, C["gri"]))

    ic.append(ok(285, 125, 305, 125, C["lacivert"], 2.2))

    ic.append(kutu(310, 56, 250, 138, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(kutu(324, 66, 222, 24, C["sari"], rx=5))
    ic.append(metin(435, 82, "Okumayı Bitirirken: Tasdik", 10.5, C["beyaz"], "bold"))
    ic.append(metin(435, 114, "Sadakallahülazim", 12, C["kirmizi"], "bold"))
    ic.append(metin(435, 136, "Anlamı: 'Azim olan Allah", 10, C["koyu"], "bold"))
    ic.append(metin(435, 152, "doğru söyledi.'", 10, C["koyu"], "bold"))
    ic.append(metin(435, 174, "İlahi kelama bağlılık ve tasdik ifadesi", 9.5, C["gri"]))

    return svg(w, h, "".join(ic), "Kur'an okumaya başlarken euzübesmele ve bitirirken Sadakallahülazim")


def gorsel_3():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mor"], rx=8))
    ic.append(metin(290, 33, "KÜLTÜRÜMÜZDE KUR'AN-I KERİM OKUNAN ORTAMLAR", 13, C["beyaz"], "bold"))

    ortamlar = [
        ("Aile & Hayat", "Doğum, sünnet,", "nikâh ve düğün", C["mavi"], C["acik_mavi"]),
        ("Vatan Görevi", "Asker uğurlaması", "ve şehitleri anma", C["yesil"], C["acik_yesil"]),
        ("Vefa & Sabır", "Cenaze, taziye ve", "vefat yıl dönümleri", C["turuncu"], C["acik_sari"]),
        ("Mübarek Zaman", "Ramazan ayı ve", "kandil geceleri", C["mor"], C["acik_kirmizi"]),
    ]
    for i, (bas, l1, l2, cb, cbg) in enumerate(ortamlar):
        x = 16 + i * 138
        ic.append(kutu(x, 56, 130, 100, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 10, 65, 110, 24, cb, rx=5))
        ic.append(metin(x + 65, 81, bas, 10.5, C["beyaz"], "bold"))
        ic.append(metin(x + 65, 110, l1, 10, C["koyu"], "bold"))
        ic.append(metin(x + 65, 128, l2, 10, C["koyu"]))

    ic.append(kutu(18, 168, 544, 38, C["acik_gri"], C["lacivert"], 1.2, rx=8))
    ic.append(metin(290, 191, "Katkısı: Toplumsal birlik, beraberlik, dayanışma ve geçmişle gelecek arasında kültür köprüsü", 10, C["koyu"], "bold"))

    return svg(w, h, "".join(ic), "Kültürümüzde Kur'an-ı Kerim okunan merasimler ve toplumsal katkısı")


def gorsel_4():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turkuaz"], rx=8))
    ic.append(metin(290, 33, "MUKABELE VE HATİM GELENEĞİ", 13, C["beyaz"], "bold"))

    ic.append(kutu(20, 56, 260, 144, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(kutu(34, 66, 232, 26, C["mavi"], rx=5))
    ic.append(metin(150, 83, "MUKABELE (Karşılıklı Okuma)", 11, C["beyaz"], "bold"))
    ic.append(metin(150, 110, "• Hz. Peygamber ile Cebrail'in (as)", 10, C["koyu"], "bold"))
    ic.append(metin(150, 126, "ramazan ayındaki arza sünneti", 10, C["koyu"]))
    ic.append(metin(150, 148, "• Hafızların okuması, cemaatin", 10, C["koyu"]))
    ic.append(metin(150, 164, "Mushaf'tan takip edip dinlemesi", 10, C["koyu"]))
    ic.append(metin(150, 184, "• Camilerde ve evlerde her ramazan", 9.5, C["gri"]))

    ic.append(kutu(300, 56, 260, 144, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(kutu(314, 66, 232, 26, C["yesil"], rx=5))
    ic.append(metin(430, 83, "HATİM (Baştan Sona Okuma)", 11, C["beyaz"], "bold"))
    ic.append(metin(430, 110, "• Fatiha suresinden Nâs suresine", 10, C["koyu"], "bold"))
    ic.append(metin(430, 126, "kadar yüzünden / ezbere tamamlama", 10, C["koyu"]))
    ic.append(metin(430, 148, "• Hadiste: 'Yolculuğa başlayıp bitiren", 10, C["koyu"]))
    ic.append(metin(430, 164, "ve tekrar başlayan yolcu' (Tirmizi)", 10, C["koyu"]))
    ic.append(metin(430, 184, "• Hatimle teravih ve hatim duaları", 9.5, C["gri"]))

    return svg(w, h, "".join(ic), "Mukabele ve hatim kavramlarının tanımı, dayanağı ve uygulanışı")


def gorsel_5():
    w, h = 580, 210
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turuncu"], rx=8))
    ic.append(metin(290, 33, "KUR'AN-I KERİM VE HAT SANATI (HÜSNÜHAT)", 13, C["beyaz"], "bold"))

    ic.append(kutu(20, 54, 540, 44, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(290, 74, "\"Kur'an-ı Kerim Hicaz'da nazil oldu, Mısır'da okundu, İstanbul'da yazıldı.\"", 11.5, C["koyu"], "bold"))
    ic.append(metin(290, 91, "Hat Sanatı: Kur'an harflerinin ve ayetlerinin estetik ölçülerle güzel yazılması", 9.8, C["gri"]))

    cards = [
        ("Hicaz", "Vahyin İndirildiği Yer", "Mekke ve Medine'de", "nazil olmuştur", C["yesil"], C["acik_yesil"]),
        ("Mısır", "Güzel Tilavet", "Kıraat ve ses", "üslubuyla okunmuştur", C["mavi"], C["acik_mavi"]),
        ("İstanbul", "Hat Sanatının Merkezi", "Hafız Osman (1698)", "Hamit Aytaç (1982)", C["mor"], C["acik_kirmizi"]),
    ]
    for i, (yer, bas, l1, l2, cb, cbg) in enumerate(cards):
        x = 18 + i * 184
        ic.append(kutu(x, 108, 174, 90, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 12, 116, 150, 22, cb, rx=4))
        ic.append(metin(x + 87, 131, f"{yer}: {bas}", 9.8, C["beyaz"], "bold"))
        ic.append(metin(x + 87, 158, l1, 10, C["koyu"], "bold"))
        ic.append(metin(x + 87, 176, l2, 10, C["koyu"]))

    return svg(w, h, "".join(ic), "Kur'an-ı Kerim ve hat sanatı merkezi olarak İstanbul ve ünlü hattatlar")


def gorsel_6():
    w, h = 580, 210
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mavi"], rx=8))
    ic.append(metin(290, 33, "HAFIZLIK MÜESSESESİ VE HAFIZLIK MERASİMİ", 13, C["beyaz"], "bold"))

    boxes = [
        ("1. Teşvik & Eğitim", "Çocukların cami ve", "Kur'an kurslarında", "eğitim alması", C["mavi"], C["acik_mavi"]),
        ("2. Hafız", "Kur'an'ı baştan sona", "ezberleyen, yaşayan", "ve koruyan kişi", C["yesil"], C["acik_yesil"]),
        ("3. Hafızlık Merasimi", "Büyük camide kurra", "hafızı önderliğinde", "hafızlık belgesi töreni", C["mor"], C["acik_sari"]),
    ]
    for i, (b, l1, l2, l3, cb, cbg) in enumerate(boxes):
        x = 18 + i * 184
        ic.append(kutu(x, 56, 174, 140, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 10, 66, 154, 24, cb, rx=5))
        ic.append(metin(x + 87, 82, b, 10.5, C["beyaz"], "bold"))
        ic.append(metin(x + 87, 114, l1, 10, C["koyu"], "bold"))
        ic.append(metin(x + 87, 132, l2, 10, C["koyu"]))
        ic.append(metin(x + 87, 150, l3, 10, C["koyu"]))
        if i < 2:
            ic.append(ok(x + 175, 126, x + 183, 126, cb, 2))

    return svg(w, h, "".join(ic), "Hafızlık eğitimi, hafız kavramı ve hafızlık merasimi geleneği")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = gorsel_1()
    b[1]["gorsel"] = gorsel_2()
    b[2]["gorsel"] = gorsel_3()
    b[3]["gorsel"] = gorsel_4()
    b[4]["gorsel"] = gorsel_5()
    b[5]["gorsel"] = gorsel_6()
