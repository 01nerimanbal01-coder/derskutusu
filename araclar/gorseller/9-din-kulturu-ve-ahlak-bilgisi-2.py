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
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "EVRENDEKİ ÖLÇÜ, AHENK VE YARATILIŞ GAYESİ", 13, C["beyaz"], "bold"))

    cards = [
        ("Kamer 54/49", "Her Şey Ölçüyledir", "Arıların tozlaşması ve", "mercanların ekosistemi", C["mavi"], C["acik_mavi"]),
        ("Rahmân 55/5", "Şaşmaz Hesap", "Güneş ve Ay'ın belli", "yörüngede hareketi", C["mor"], C["acik_sari"]),
        ("Enbiyâ 21/16", "Hikmet ve Gaye", "Gök ve yer oyun olsun", "diye yaratılmamıştır", C["yesil"], C["acik_yesil"]),
    ]
    for i, (ayet, bas, s1, s2, cb, cbg) in enumerate(cards):
        x = 18 + i * 184
        ic.append(kutu(x, 55, 174, 145, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 12, 65, 150, 24, cb, rx=5))
        ic.append(metin(x + 87, 81, ayet, 11, C["beyaz"], "bold"))
        ic.append(metin(x + 87, 108, bas, 11.5, C["koyu"], "bold"))
        ic.append(metin(x + 87, 132, s1, 10, C["koyu"]))
        ic.append(metin(x + 87, 148, s2, 10, C["koyu"]))
        ic.append(kutu(x + 18, 164, 138, 24, C["beyaz"], cb, 1, rx=4))
        ic.append(metin(x + 87, 180, "Tesadüf Değil, Nizam", 9.5, cb, "bold"))

    return svg(w, h, "".join(ic), "Evrendeki ölçü, hesap ve yaratılış gayesini gösteren ayetler şeması")


def gorsel_2():
    w, h = 580, 225
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["turkuaz"], rx=8))
    ic.append(metin(290, 33, "İNSANIN YARATILIŞ EVRELERİ (MÜ'MİNÛN 23/12-14 & HAC 22/5)", 12.5, C["beyaz"], "bold"))

    stages = [
        ("1. Öz", "Çamurdan", "süzülmüş öz", C["turuncu"]),
        ("2. Nutfe", "Sağlam", "karargâhta su", C["mavi"]),
        ("3. Alaka", "Aşılanmış", "yumurta", C["mor"]),
        ("4. Mudga", "Bir çiğnemlik", "et parçası", C["kirmizi"]),
        ("5. İskelet", "Kemikler ve", "etle kaplanma", C["yesil"]),
        ("6. İnsan", "Ruh üflenmesi", "yeni yaratılış", C["lacivert"]),
    ]
    for i, (st, l1, l2, col) in enumerate(stages):
        x = 16 + i * 92
        ic.append(kutu(x, 58, 84, 98, C["beyaz"], col, 2, rx=8))
        ic.append(kutu(x + 6, 65, 72, 22, col, rx=4))
        ic.append(metin(x + 42, 80, st, 10, C["beyaz"], "bold"))
        ic.append(metin(x + 42, 108, l1, 9.5, C["koyu"], "bold"))
        ic.append(metin(x + 42, 124, l2, 9.5, C["gri"]))
        if i < 5:
            ic.append(ok(x + 85, 107, x + 91, 107, col, 1.8))

    ic.append(kutu(18, 170, 544, 40, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(290, 187, "Fâtır 35/11 • İnfitâr 82/7 • Hac 22/5", 10.5, C["koyu"], "bold"))
    ic.append(metin(290, 203, "Dengeli ve ölçülü biçimlendirme → Öldükten sonra dirilişin (ba's) açık delili", 10, C["koyu"]))

    return svg(w, h, "".join(ic), "Müminun 12-14 ve Hac 5 ayetlerine göre insanın yaratılış evreleri")


def gorsel_3():
    w, h = 580, 215
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mor"], rx=8))
    ic.append(metin(290, 33, "AHSEN-İ TAKVİM VE MÜKERREM VARLIK OLARAK İNSAN", 13, C["beyaz"], "bold"))

    ic.append(kutu(20, 56, 260, 144, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(150, 76, "Tîn Suresi 4. Ayet", 12, C["lacivert"], "bold"))
    ic.append(kutu(36, 86, 228, 28, C["mavi"], rx=5))
    ic.append(metin(150, 104, "AHSEN-İ TAKVİM (En Güzel Biçim)", 10.5, C["beyaz"], "bold"))
    ic.append(metin(150, 132, "• Düzgün ve dengeli fiziki yapı", 10, C["koyu"]))
    ic.append(metin(150, 152, "• Akıl, kalp, vicdan ve irade", 10, C["koyu"]))
    ic.append(metin(150, 172, "• Düşünme ve konuşma kabiliyeti", 10, C["koyu"]))

    ic.append(kutu(300, 56, 260, 144, C["acik_yesil"], C["yesil"], 1.5, rx=8))
    ic.append(metin(430, 76, "İsrâ Suresi 70. Ayet", 12, C["yesil"], "bold"))
    ic.append(kutu(316, 86, 228, 28, C["yesil"], rx=5))
    ic.append(metin(430, 104, "MÜKERREM (Onurlu ve Üstün)", 10.5, C["beyaz"], "bold"))
    ic.append(metin(430, 132, "• Karada ve denizde taşınma imkânı", 10, C["koyu"]))
    ic.append(metin(430, 152, "• Temiz ve güzel rızıklarla beslenme", 10, C["koyu"]))
    ic.append(metin(430, 172, "• Pek çok varlıktan üstün kılınma", 10, C["koyu"]))

    return svg(w, h, "".join(ic), "Tin 4 ve İsra 70 ayetleri ışığında ahsen-i takvim ve mükerrem varlık kavramları")


def gorsel_4():
    w, h = 580, 210
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["mavi"], rx=8))
    ic.append(metin(290, 33, "İSİMLERİN ÖĞRETİLMESİ VE ÖĞRENEN VARLIK İNSAN (BAKARA 2/31-33)", 12, C["beyaz"], "bold"))

    ic.append(kutu(20, 56, 245, 138, C["acik_sari"], C["sari"], 1.5, rx=8))
    ic.append(metin(142, 78, "Diğer Canlılar ve Melekler", 11.5, C["koyu"], "bold"))
    ic.append(metin(142, 104, "• Canlılar içgüdüleriyle hareket eder", 10, C["koyu"]))
    ic.append(metin(142, 124, "• Melekler: 'Bize öğrettiğinden", 10, C["koyu"]))
    ic.append(metin(142, 140, "başka bilgimiz yoktur.' (Bakara 32)", 10, C["koyu"]))
    ic.append(metin(142, 164, "• Sabit ve değişmeyen görev alanı", 10, C["gri"]))

    ic.append(ok(270, 125, 308, 125, C["lacivert"], 2.5))

    ic.append(kutu(315, 56, 245, 138, C["acik_mavi"], C["mavi"], 1.5, rx=8))
    ic.append(metin(437, 78, "Hz. Âdem ve İnsan Nesli", 11.5, C["lacivert"], "bold"))
    ic.append(metin(437, 104, "• Eşyanın isimlerini ve mahiyetini bilme", 10, C["koyu"], "bold"))
    ic.append(metin(437, 124, "• Kavramlarla düşünme ve dil yetisi", 10, C["koyu"]))
    ic.append(metin(437, 144, "• Bilim, sanat ve teknoloji üretme", 10, C["koyu"]))
    ic.append(metin(437, 164, "• Şehirler ve medeniyetler kurma", 10, C["mavi"], "bold"))

    return svg(w, h, "".join(ic), "Bakara 31-33 ayetlerine göre Hz. Adem'e isimlerin öğretilmesi ve insanın öğrenme yetisi")


def gorsel_5():
    w, h = 580, 220
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["yesil"], rx=8))
    ic.append(metin(290, 33, "HALİFELİK, EMANET VE BİLİNÇLİ KULLUK", 13, C["beyaz"], "bold"))

    boxes = [
        ("HALİFELİK", "Bakara 2/30", "Yeryüzünü imar etme,", "adalet ve iyiliği", "yaşatma görevi", C["mavi"], C["acik_mavi"]),
        ("EMANET", "Ahzâb 33/72", "Göklerin ve dağların", "çekindiği irade ve", "sorumluluk yükü", C["turuncu"], C["acik_sari"]),
        ("KULLUK & TESPİH", "Zâriyât 56 & İsrâ 44", "Evrenin fıtrî tespihine", "hür irade ve bilinçli", "ibadetle katılma", C["yesil"], C["acik_yesil"]),
    ]
    for i, (b, ay, l1, l2, l3, cb, cbg) in enumerate(boxes):
        x = 18 + i * 184
        ic.append(kutu(x, 56, 174, 150, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 12, 66, 150, 24, cb, rx=5))
        ic.append(metin(x + 87, 82, b, 11, C["beyaz"], "bold"))
        ic.append(metin(x + 87, 105, ay, 10, cb, "bold"))
        ic.append(metin(x + 87, 128, l1, 10, C["koyu"]))
        ic.append(metin(x + 87, 145, l2, 10, C["koyu"]))
        ic.append(metin(x + 87, 162, l3, 10, C["koyu"]))

    return svg(w, h, "".join(ic), "Halifelik, emanet ve kulluk bilincinin ayetlerle ilişkisi")


def gorsel_6():
    w, h = 580, 225
    ic = []
    ic.append(kutu(15, 12, 550, 32, C["lacivert"], rx=8))
    ic.append(metin(290, 33, "SOSYAL VARLIK OLARAK İNSANIN 4 SORUMLULUK ALANI (FURKAN 25/54)", 12, C["beyaz"], "bold"))

    quads = [
        (20, 54, "1. Allah'a (cc) Karşı", "İman, salih amel, ibadet ve", "verilen nimetlere şükür", C["mavi"], C["acik_mavi"]),
        (300, 54, "2. Kendisine Karşı", "Beden ve ruh sağlığını koruma,", "ilim ve güzel ahlak edinme", C["mor"], C["acik_sari"]),
        (20, 138, "3. Ailesine Karşı", "Anne babaya ihsan ve saygı,", "akrabalık (sıla-i rahim) bağı", C["yesil"], C["acik_yesil"]),
        (300, 138, "4. Topluma Karşı", "Kul ve insan haklarına saygı,", "adalet, dürüstlük ve yardımlaşma", C["turuncu"], C["acik_kirmizi"]),
    ]
    for x, y, title, l1, l2, cb, cbg in quads:
        ic.append(kutu(x, y, 260, 74, cbg, cb, 1.5, rx=8))
        ic.append(kutu(x + 10, y + 8, 240, 22, cb, rx=4))
        ic.append(metin(x + 130, y + 23, title, 10.5, C["beyaz"], "bold"))
        ic.append(metin(x + 130, y + 46, l1, 9.8, C["koyu"], "bold"))
        ic.append(metin(x + 130, y + 62, l2, 9.8, C["koyu"]))

    return svg(w, h, "".join(ic), "Sosyal bir varlık olan insanın Allah'a, kendisine, ailesine ve topluma karşı sorumlulukları")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = gorsel_1()
    b[1]["gorsel"] = gorsel_2()
    b[2]["gorsel"] = gorsel_3()
    b[3]["gorsel"] = gorsel_4()
    b[4]["gorsel"] = gorsel_5()
    b[5]["gorsel"] = gorsel_6()
