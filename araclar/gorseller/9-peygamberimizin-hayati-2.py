"""9-peygamberimizin-hayati-2 için 6 eğitici SVG diyagramı."""
from ozet_gorsel import svg

C = {
    "kirmizi": "#b8362a",
    "mavi": "#245785",
    "yesil": "#246c45",
    "sari": "#9e6b12",
    "mor": "#6b3e8e",
    "lacivert": "#1f2e45",
    "turkuaz": "#1c7278",
    "toprak": "#734e30",
    "acik_kirmizi": "#faecea",
    "acik_mavi": "#eaf2fa",
    "acik_yesil": "#e8f5ee",
    "acik_sari": "#fdf5e2",
    "acik_mor": "#f3ecf9",
    "acik_turkuaz": "#e6f4f5",
    "acik_toprak": "#f5ede6",
    "gri": "#68645c",
    "cizgi": "#d8d1c3",
}


def kutu(x, y, w, h, dolgu="#fff", kenar="#d8d1c3", r=8, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'


def metin(x, y, icerik, boyut=12, renk="#1a1815", kalin=False, orta=True, italik=False):
    anc = ' text-anchor="middle"' if orta else ""
    fw = ' font-weight="700"' if kalin else ' font-weight="500"'
    fs = ' font-style="italic"' if italik else ""
    return f'<text x="{x}" y="{y}" font-size="{boyut}" fill="{renk}"{anc}{fw}{fs}>{icerik}</text>'


def cizgi(x1, y1, x2, y2, renk="#68645c", kalinlik=1.8, kesik=False):
    da = ' stroke-dasharray="5,4"' if kesik else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalinlik}"{da}/>'


def ok(x1, y1, x2, y2, renk="#b8362a", kalinlik=2):
    import math
    aci = math.atan2(y2 - y1, x2 - x1)
    u = 8
    px1 = x2 - u * math.cos(aci - 0.45)
    py1 = y2 - u * math.sin(aci - 0.45)
    px2 = x2 - u * math.cos(aci + 0.45)
    py2 = y2 - u * math.sin(aci + 0.45)
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kalinlik}"/>'
        f'<polygon points="{x2},{y2} {px1:.1f},{py1:.1f} {px2:.1f},{py2:.1f}" fill="{renk}"/>'
    )


def gorsel_1():
    w, h = 680, 230
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["lacivert"], C["lacivert"], r=6))
    ic.append(metin(340, 36, "HİCAZ BÖLGESİ VE KUR’AN-I KERİM’DE MEKKE’NİN İSİMLERİ", 13, "#fff", True))

    # Sol: Hicaz 3 şehir
    ic.append(kutu(18, 60, 200, 154, C["acik_toprak"], C["toprak"]))
    ic.append(metin(118, 82, "HİCAZ’IN 3 ANA ŞEHRİ", 12, C["toprak"], True))
    ic.append(kutu(34, 94, 168, 30, "#fff", C["toprak"], r=5))
    ic.append(metin(118, 114, "1. Mekke (Dini ve Ticari Merkez)", 10.5, C["lacivert"], True))
    ic.append(kutu(34, 132, 168, 30, "#fff", C["toprak"], r=5))
    ic.append(metin(118, 152, "2. Medine / Yesrib (Kuzeyde)", 10.5, C["lacivert"], False))
    ic.append(kutu(34, 170, 168, 30, "#fff", C["toprak"], r=5))
    ic.append(metin(118, 190, "3. Taif (Güneydoğuda)", 10.5, C["lacivert"], False))

    # Sağ: Mekke'nin İsimleri ve Harem Vasfı
    kartlar = [
        (234, "BEKKE", "Kalabalık, ziyaretçisi bol", "Âl-i İmran 3/96", C["mavi"], C["acik_mavi"]),
        (382, "ÜMMÜLKURA", "Şehirlerin anası / merkezi", "En’âm 6/92, Şûrâ 42/7", C["yesil"], C["acik_yesil"]),
        (530, "BELEDÜLEMİN", "Güvenli belde (Harem)", "Tîn 95/3, İbrahim 14/35", C["kirmizi"], C["acik_kirmizi"]),
    ]
    for x, bas, acik, ayet, k_renk, d_renk in kartlar:
        ic.append(kutu(x, 60, 134, 102, d_renk, k_renk))
        ic.append(metin(x + 67, 84, bas, 12, k_renk, True))
        ic.append(metin(x + 67, 110, acik, 10, "#1a1815", False))
        ic.append(kutu(x + 10, 126, 114, 24, "#fff", k_renk, r=4))
        ic.append(metin(x + 67, 142, ayet, 9.5, k_renk, True))

    ic.append(kutu(234, 172, 430, 42, C["acik_sari"], C["sari"]))
    ic.append(metin(449, 190, "Coğrafya: “Ekin bitmeyen vadi” (İbrahim 37) • Kurak çöl iklimi ve ani seller", 10.5, C["sari"], True))
    ic.append(metin(449, 206, "İslam coğrafyacılarının (9. yy) dairevi dünya haritalarında Kâbe dünyanın merkezidir.", 10, "#1a1815", False))

    return svg(w, h, "".join(ic), "Hicaz bölgesinin üç önemli şehri ve Kur’an-ı Kerim’de Mekke için kullanılan isimler")


def gorsel_2():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["yesil"], C["yesil"], r=6))
    ic.append(metin(340, 36, "ZEMZEMİN BULUNUŞU VE KÂBE’NİN YENİDEN İNŞASI (TEVHİT MERKEZİ)", 12.5, "#fff", True))

    adimlar = [
        (18, "1. Hicret ve İskan", "Hz. İbrahim, eşi Hz. Hacer", "ve oğlu Hz. İsmail’i", "Mekke vadisine bıraktı.", C["mavi"], C["acik_mavi"]),
        (180, "2. Zemzem Mucizesi", "Su tükenince ilahi yardımla", "zemzem suyu çıktı;", "yerleşim başladı.", C["turkuaz"], C["acik_turkuaz"]),
        (342, "3. Kâbe’nin İnşası", "Hz. Âdem’den kalan temeller", "üzerine baba-oğul Kâbe’yi", "yeniden yükseltti.", C["sari"], C["acik_sari"]),
        (504, "4. Mimari Özellikler", "• Yaklaşık 7 m yükseklik", "• Harçsız taş, üstü açık", "• 2 kapı ve mahzen çukuru", C["yesil"], C["acik_yesil"]),
    ]
    for x, bas, s1, s2, s3, k_renk, d_renk in adimlar:
        ic.append(kutu(x, 62, 154, 112, d_renk, k_renk))
        ic.append(metin(x + 77, 84, bas, 11.5, k_renk, True))
        ic.append(metin(x + 77, 108, s1, 10, "#1a1815"))
        ic.append(metin(x + 77, 126, s2, 10, "#1a1815"))
        ic.append(metin(x + 77, 144, s3, 10, k_renk, True))

    ic.append(ok(172, 118, 180, 118, C["lacivert"]))
    ic.append(ok(334, 118, 342, 118, C["lacivert"]))
    ic.append(ok(496, 118, 504, 118, C["lacivert"]))

    ic.append(kutu(18, 184, 640, 30, C["acik_mor"], C["mor"], r=6))
    ic.append(metin(338, 204, "Sonuç: Kâbe’nin yeniden inşasıyla Mekke, Allah’ın birliği esasına dayanan tevhit inancının merkezi oldu.", 11, C["mor"], True))

    return svg(w, h, "".join(ic), "Zemzemin bulunuşu ve Hz. İbrahim ile Hz. İsmail’in Kâbe’yi inşa süreci")


def gorsel_3():
    w, h = 680, 230
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["mor"], C["mor"], r=6))
    ic.append(metin(340, 36, "PUTPERESTLİĞİN YAYILMASI VE KUSAY BİN KİLAB DÖNEMİ", 13, "#fff", True))

    # Sol: Huzaa ve Putlar
    ic.append(kutu(18, 60, 312, 156, C["acik_kirmizi"], C["kirmizi"]))
    ic.append(metin(174, 82, "HUZAA KABİLESİ VE BAŞLICA PUTLAR", 12, C["kirmizi"], True))
    ic.append(metin(174, 102, "Mekke’ye putperestliği Huzaa kabilesi getirdi.", 10.5, "#1a1815", True))
    ic.append(kutu(32, 114, 284, 28, "#fff", C["kirmizi"], r=5))
    ic.append(metin(174, 132, "Hübel: Kâbe’deki en büyük ve insan şeklindeki put", 10, C["kirmizi"], True))
    ic.append(kutu(32, 148, 284, 28, "#fff", C["kirmizi"], r=5))
    ic.append(metin(174, 166, "Lat, Uzza ve Menat: Hicaz’da değer verilen 3 put", 10, "#1a1815", False))
    ic.append(kutu(32, 182, 284, 26, "#fff", C["kirmizi"], r=5))
    ic.append(metin(174, 199, "İsaf (Safa Tepesi) ve Naila (Merve Tepesi)", 10, "#1a1815", False))

    ic.append(ok(330, 138, 350, 138, C["lacivert"], 2.5))

    # Sağ: Kusay bin Kilab ve Darünnedve
    ic.append(kutu(350, 60, 312, 156, C["acik_mavi"], C["mavi"]))
    ic.append(metin(506, 82, "KUSAY BİN KİLAB VE DARÜNNEDVE", 12, C["mavi"], True))
    ic.append(metin(506, 102, "Huzaa’dan Mekke yönetimini devraldı.", 10.5, "#1a1815", True))
    ic.append(kutu(364, 114, 284, 28, "#fff", C["mavi"], r=5))
    ic.append(metin(506, 132, "Dağınık yaşayan Kureyş kollarını birleştirdi.", 10, C["mavi"], True))
    ic.append(kutu(364, 148, 284, 28, "#fff", C["mavi"], r=5))
    ic.append(metin(506, 166, "Darünnedve (Nedve Evi) meclisini kurdu.", 10, "#1a1815", True))
    ic.append(kutu(364, 182, 284, 26, "#fff", C["mavi"], r=5))
    ic.append(metin(506, 199, "Siyasi, sosyal ve ticari kararlar burada alındı.", 10, "#1a1815", False))

    return svg(w, h, "".join(ic), "Mekke’de putperestliğin yayılması ve Kusay bin Kilab’ın Kureyş birliğini kurması")


def gorsel_4():
    w, h = 680, 235
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["sari"], C["sari"], r=6))
    ic.append(metin(340, 36, "İLAF ANLAŞMALARI, YAZ-KIŞ KERVANLARI VE PANAYIRLAR", 13, "#fff", True))

    # Kuzey (Yaz)
    ic.append(kutu(22, 62, 196, 116, C["acik_mavi"], C["mavi"]))
    ic.append(metin(120, 84, "YAZ SEFERLERİ (KUZEY)", 11.5, C["mavi"], True))
    ic.append(metin(120, 106, "Suriye (Şam, Busra, Gazze)", 10.5, "#1a1815", True))
    ic.append(metin(120, 126, "ve Anadolu Güzergâhı", 10.5, "#1a1815"))
    ic.append(metin(120, 152, "(Serin İklim Bölgesi)", 10, C["mavi"], True))

    # Merkez (Mekke & İlaf)
    ic.append(kutu(242, 62, 196, 116, C["acik_sari"], C["sari"], kalinlik=2))
    ic.append(metin(340, 84, "MEKKE (KUREYŞ)", 12, C["sari"], True))
    ic.append(metin(340, 106, "Haşim bin Abdümenaf", 10.5, "#1a1815", True))
    ic.append(metin(340, 126, "İLAF ANLAŞMALARI", 11, C["kirmizi"], True))
    ic.append(metin(340, 150, "(Yol Güvenliği & Ticaret)", 10, "#1a1815"))

    # Güney (Kış)
    ic.append(kutu(462, 62, 196, 116, C["acik_yesil"], C["yesil"]))
    ic.append(metin(560, 84, "KIŞ SEFERLERİ (GÜNEY)", 11.5, C["yesil"], True))
    ic.append(metin(560, 106, "Yemen (Sana, Aden)", 10.5, "#1a1815", True))
    ic.append(metin(560, 126, "ve Habeşistan Güzergâhı", 10.5, "#1a1815"))
    ic.append(metin(560, 152, "(Sıcak İklim Bölgesi)", 10, C["yesil"], True))

    ic.append(ok(242, 120, 218, 120, C["mavi"]))
    ic.append(ok(438, 120, 462, 120, C["yesil"]))

    # Alt bant: Panayırlar
    ic.append(kutu(22, 190, 636, 32, C["acik_turkuaz"], C["turkuaz"], r=6))
    ic.append(metin(340, 210, "Hac Mevsimi Panayırları: UKAZ • MECENNE • ZÜLMECAZ (En büyük ticari pay Kureyş’indir)", 11, C["turkuaz"], True))

    return svg(w, h, "".join(ic), "Haşim bin Abdümenaf’ın ilaf anlaşmaları, Kureyş’in yaz-kış kervanları ve panayırlar")


def gorsel_5():
    w, h = 680, 220
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["kirmizi"], C["kirmizi"], r=6))
    ic.append(metin(340, 36, "FİL VAKASI (M. 571): SEBEP, GELİŞME VE SONUÇ", 13, "#fff", True))

    kutular = [
        (20, "1. SEBEP: KULLEYS", "Yemen Valisi Ebrehe,", "hac ziyaretlerini Sana’daki", "Kulleys kilisesine", "çekmek istedi.", C["sari"], C["acik_sari"]),
        (238, "2. SEFER: FİL ORDUSU", "Araplar Kâbe’den", "vazgeçmeyince Ebrehe,", "fillerle destekli ordusuyla", "Kâbe’yi yıkmaya yürüdü.", C["kirmizi"], C["acik_kirmizi"]),
        (456, "3. SONUÇ: İLAHİ YARDIM", "Ebâbîl kuşlarının attığı", "taşlarla ordu helak oldu;", "Kâbe ve Kureyş’in itibarı", "daha da yükseldi.", C["yesil"], C["acik_yesil"]),
    ]
    for x, bas, s1, s2, s3, s4, k_renk, d_renk in kutular:
        ic.append(kutu(x, 62, 204, 142, d_renk, k_renk))
        ic.append(metin(x + 102, 84, bas, 11.5, k_renk, True))
        ic.append(metin(x + 102, 110, s1, 10.5, "#1a1815"))
        ic.append(metin(x + 102, 130, s2, 10.5, "#1a1815"))
        ic.append(metin(x + 102, 150, s3, 10.5, "#1a1815", True))
        ic.append(metin(x + 102, 170, s4, 10.5, k_renk, True))

    ic.append(ok(224, 133, 238, 133, C["lacivert"]))
    ic.append(ok(442, 133, 456, 133, C["lacivert"]))

    return svg(w, h, "".join(ic), "Ebrehe’nin Kulleys kilisesi girişimi ve Fil Vakası’nın aşamaları")


def gorsel_6():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["turkuaz"], C["turkuaz"], r=6))
    ic.append(metin(340, 36, "ABDÜLMUTTALİB’İN ZEMZEMİ YENİDEN AÇMASI VE KURBAN ADAĞI", 12.5, "#fff", True))

    asama = [
        (18, "1. Zemzemin Açılması", "Abdülmuttalib (Şeybe),", "tek oğlu Haris ile kazı", "yaparak kayıp zemzem", "kuyusunu yeniden buldu.", C["turkuaz"], C["acik_turkuaz"]),
        (236, "2. On Oğul Adağı", "Kureyş’in baskısı üzerine", "“On oğlum olursa birini", "kurban edeceğim” diye", "adakta bulundu.", C["mor"], C["acik_mor"]),
        (454, "3. Abdullah ve 100 Deve", "Kurada en küçük oğlu", "Abdullah çıkınca istişareyle", "Abdullah’ın yerine", "100 deve kurban edildi.", C["yesil"], C["acik_yesil"]),
    ]
    for x, bas, s1, s2, s3, s4, k_renk, d_renk in asama:
        ic.append(kutu(x, 60, 206, 118, d_renk, k_renk))
        ic.append(metin(x + 103, 82, bas, 11.5, k_renk, True))
        ic.append(metin(x + 103, 106, s1, 10, "#1a1815"))
        ic.append(metin(x + 103, 124, s2, 10, "#1a1815"))
        ic.append(metin(x + 103, 142, s3, 10, "#1a1815", True))
        ic.append(metin(x + 103, 160, s4, 10, k_renk, True))

    ic.append(ok(224, 119, 236, 119, C["lacivert"]))
    ic.append(ok(442, 119, 454, 119, C["lacivert"]))

    ic.append(kutu(18, 188, 642, 26, C["acik_sari"], C["sari"], r=5))
    ic.append(metin(339, 205, "Hz. Muhammed (s.a.v.), Hz. İsmail ve babası Abdullah sebebiyle “iki kurbanlığın oğlu” olarak anılmıştır.", 10.5, C["sari"], True))

    return svg(w, h, "".join(ic), "Abdülmuttalib’in zemzem kuyusunu yeniden açması ve oğlu Abdullah için yüz deve kurban etmesi")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
