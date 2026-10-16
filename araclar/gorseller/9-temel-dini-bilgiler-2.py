"""9-temel-dini-bilgiler-2 için 6 eğitici SVG diyagramı."""
from ozet_gorsel import svg

C = {
    "kirmizi": "#b8362a",
    "mavi": "#245785",
    "yesil": "#246c45",
    "sari": "#9e6b12",
    "mor": "#6b3e8e",
    "lacivert": "#1f2e45",
    "turkuaz": "#1c7278",
    "acik_kirmizi": "#faecea",
    "acik_mavi": "#eaf2fa",
    "acik_yesil": "#e8f5ee",
    "acik_sari": "#fdf5e2",
    "acik_mor": "#f3ecf9",
    "acik_turkuaz": "#e6f4f5",
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
    w, h = 680, 220
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["lacivert"], C["lacivert"], r=6))
    ic.append(metin(340, 36, "İNSAN VE KÂİNATIN YARATILIŞINI MÜŞAHEDE (ZÂRİYÂT 51/20-21)", 13, "#fff", True))

    # Sol: Dış dünya
    ic.append(kutu(20, 62, 200, 140, C["acik_mavi"], C["mavi"]))
    ic.append(metin(120, 86, "1. YERYÜZÜNDEKİ DELİLLER", 11.5, C["mavi"], True))
    ic.append(metin(120, 110, "• Göklerin ve yerin düzeni", 10.5, "#1a1815"))
    ic.append(metin(120, 130, "• Mevsimler ve canlılar", 10.5, "#1a1815"))
    ic.append(metin(120, 150, "• Hassas ölçü (Mîzan)", 10.5, "#1a1815"))
    ic.append(kutu(36, 166, 168, 24, "#fff", C["mavi"], r=4))
    ic.append(metin(120, 182, "Dış Dünyayı Müşahede", 10, C["mavi"], True))

    # Orta: Varoluşsal Tefekkür
    ic.append(kutu(240, 62, 200, 140, C["acik_sari"], C["sari"], kalinlik=2))
    ic.append(metin(340, 86, "TEFEKKÜR VE ANLAM ARAYIŞI", 11.5, C["sari"], True))
    ic.append(metin(340, 110, "“Ben kimim?”", 11, "#1a1815", True))
    ic.append(metin(340, 130, "“Niçin yaratıldım?”", 11, "#1a1815", True))
    ic.append(metin(340, 150, "“Sorumluluğum nedir?”", 11, "#1a1815", True))
    ic.append(kutu(256, 166, 168, 24, "#fff", C["sari"], r=4))
    ic.append(metin(340, 182, "Hakikate ve İmana Ulaşma", 10, C["kirmizi"], True))

    # Sağ: İç dünya
    ic.append(kutu(460, 62, 200, 140, C["acik_yesil"], C["yesil"]))
    ic.append(metin(560, 86, "2. NEFİSLERDEKİ DELİLLER", 11.5, C["yesil"], True))
    ic.append(metin(560, 110, "• Beden ve ruh bütünlüğü", 10.5, "#1a1815"))
    ic.append(metin(560, 130, "• Akıl, vicdan ve irade", 10.5, "#1a1815"))
    ic.append(metin(560, 150, "• En güzel biçim (Ahsenitakvim)", 10.5, "#1a1815"))
    ic.append(kutu(476, 166, 168, 24, "#fff", C["yesil"], r=4))
    ic.append(metin(560, 182, "İç Dünyayı Tefekkür", 10, C["yesil"], True))

    ic.append(ok(220, 132, 240, 132, C["mavi"]))
    ic.append(ok(460, 132, 440, 132, C["yesil"]))

    return svg(w, h, "".join(ic), "Yeryüzündeki ve insanın kendi nefsindeki delillerin müşahede ve tefekkür edilmesi")


def gorsel_2():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["yesil"], C["yesil"], r=6))
    ic.append(metin(340, 36, "İSLAM’DA İNSANIN SEÇKİN DEĞERİ VE DONANIMI", 13, "#fff", True))

    kartlar = [
        (20, "AHSENİTAKVİM", "En Güzel Biçimde Yaratılış", "Bedensel ve ruhsal yönden", "en mükemmel kıvam.", "Tîn suresi, 4. ayet", C["yesil"], C["acik_yesil"]),
        (238, "EŞREFİMAHLUKAT", "Yaratılmışların En Şereflisi", "Şan, şeref ve temiz rızıkla", "üstün kılınan varlık.", "İsrâ suresi, 70. ayet", C["mavi"], C["acik_mavi"]),
        (456, "AKIL, İRADE VE İLİM", "Üstünlüğün Temel Kaynağı", "Eşyanın isimlerini öğrenme,", "düşünme ve seçme yetisi.", "Bakara 2/31 • Zümer 39/9", C["mor"], C["acik_mor"]),
    ]
    for x, bas, alt, s1, s2, ayet, k_renk, d_renk in kartlar:
        ic.append(kutu(x, 60, 204, 150, d_renk, k_renk))
        ic.append(metin(x + 102, 84, bas, 12, k_renk, True))
        ic.append(metin(x + 102, 104, alt, 10.5, "#1a1815", True))
        ic.append(metin(x + 102, 128, s1, 10, "#1a1815"))
        ic.append(metin(x + 102, 146, s2, 10, "#1a1815"))
        ic.append(kutu(x + 18, 166, 168, 28, "#fff", k_renk, r=5))
        ic.append(metin(x + 102, 184, ayet, 10, k_renk, True))

    return svg(w, h, "".join(ic), "Ahsenitakvim, eşrefimahlukat ve insanın akıl-irade-ilim donanımı")


def gorsel_3():
    w, h = 680, 215
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["mor"], C["mor"], r=6))
    ic.append(metin(340, 36, "KENDİNİ BİLMEKTEN MARİFETULLAHA VE KULLUK BİLİNCİNE", 13, "#fff", True))

    adimlar = [
        (18, "1. Kendini Bilmek", "“İlim kendin bilmektir”", "(Yunus Emre)", "Fıtratını ve acziyetini tanıma", C["mavi"], C["acik_mavi"]),
        (238, "2. Marifetullah", "“Kendini bilen Rabbini bilir”", "Allah’ı isim, sıfat ve", "kudretiyle derinlemesine tanıma", C["mor"], C["acik_mor"]),
        (458, "3. Kulluk ve İbadet", "“Cinleri ve insanları ancak bana", "kulluk etsinler diye yarattım.”", "(Zâriyât suresi, 56. ayet)", C["yesil"], C["acik_yesil"]),
    ]
    for x, bas, s1, s2, s3, k_renk, d_renk in adimlar:
        ic.append(kutu(x, 62, 204, 134, d_renk, k_renk))
        ic.append(metin(x + 102, 86, bas, 12, k_renk, True))
        ic.append(metin(x + 102, 114, s1, 10, "#1a1815", True))
        ic.append(metin(x + 102, 136, s2, 10, "#1a1815"))
        ic.append(metin(x + 102, 160, s3, 10, k_renk, True))

    ic.append(ok(222, 129, 238, 129, C["lacivert"]))
    ic.append(ok(442, 129, 458, 129, C["lacivert"]))

    return svg(w, h, "".join(ic), "Kendini tanıma, marifetullah ve kulluk bilinci arasındaki ilişki")


def gorsel_4():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["sari"], C["sari"], r=6))
    ic.append(metin(340, 36, "HİLAFET GÖREVİ VE İLAHİ EMANETİN ÜSTLENİLMESİ", 13, "#fff", True))

    # Üst iki temel şart
    ic.append(kutu(30, 62, 290, 66, C["acik_mavi"], C["mavi"]))
    ic.append(metin(175, 84, "AKIL (Kavrama ve Ayırt Etme)", 11.5, C["mavi"], True))
    ic.append(metin(175, 106, "İyiyi kötüden, doğruyu yanlıştan ayırır (İbrâhim 14/52).", 10, "#1a1815"))

    ic.append(kutu(360, 62, 290, 66, C["acik_turkuaz"], C["turkuaz"]))
    ic.append(metin(505, 84, "İRADE (Özgür Tercih Gücü)", 11.5, C["turkuaz"], True))
    ic.append(metin(505, 106, "Zorlama olmadan doğru yolu seçmeyi sağlar.", 10, "#1a1815"))

    ic.append(ok(175, 128, 250, 148, C["lacivert"]))
    ic.append(ok(505, 128, 430, 148, C["lacivert"]))

    # Alt iki sonuç
    ic.append(kutu(30, 148, 290, 64, C["acik_yesil"], C["yesil"]))
    ic.append(metin(175, 170, "HALİFE (Bakara 2/30)", 11.5, C["yesil"], True))
    ic.append(metin(175, 192, "Yeryüzünü imar etmek ve adaleti hâkim kılmak.", 10, "#1a1815"))

    ic.append(kutu(360, 148, 290, 64, C["acik_kirmizi"], C["kirmizi"]))
    ic.append(metin(505, 170, "EMANET (Ahzâb 33/72)", 11.5, C["kirmizi"], True))
    ic.append(metin(505, 192, "Göklerin ve dağların çekindiği sorumluluğu taşımak.", 10, "#1a1815"))

    return svg(w, h, "".join(ic), "Akıl ve irade temelinde insanın halifelik ve emanet sorumluluğu")


def gorsel_5():
    w, h = 680, 235
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["kirmizi"], C["kirmizi"], r=6))
    ic.append(metin(340, 36, "İNSANIN DÖRT TEMEL SORUMLULUK HALKASI", 13, "#fff", True))

    kartlar = [
        (18, 60, "1. ALLAH’A KARŞI", "• İman ve marifetullah", "• İbadet ve kulluk (Zâriyât 56)", "• Emir ve yasaklara riayet", C["mor"], C["acik_mor"]),
        (348, 60, "2. KENDİSİNE KARŞI", "• Beden ve ruh sağlığını koruma", "• Nefsi arındırma (Şems 9-10)", "• Faydalı ilim ve zaman bilinci", C["mavi"], C["acik_mavi"]),
        (18, 146, "3. AİLE VE TOPLUMA KARŞI", "• Aileyi koruma ve sılayırahim", "• Kardeşlik (Hucurât 10)", "• Kötülüğü önleme (Gemi hadisi)", C["kirmizi"], C["acik_kirmizi"]),
        (348, 146, "4. ÇEVREYE VE KÂİNATA KARŞI", "• Doğadaki mîzanı bozmama", "• İsraftan kaçınma ve merhamet", "• Kıyamet kopsa da fidan dikme", C["yesil"], C["acik_yesil"]),
    ]
    for x, y, bas, s1, s2, s3, k_renk, d_renk in kartlar:
        ic.append(kutu(x, y, 314, 76, d_renk, k_renk))
        ic.append(metin(x + 157, y + 20, bas, 11.5, k_renk, True))
        ic.append(metin(x + 16, y + 38, s1, 10, "#1a1815", False, False))
        ic.append(metin(x + 16, y + 54, s2, 10, "#1a1815", False, False))
        ic.append(metin(x + 16, y + 69, s3, 10, k_renk, True, False))

    return svg(w, h, "".join(ic), "İnsanın Allah’a, kendisine, topluma ve çevreye karşı dört temel sorumluluk alanı")


def gorsel_6():
    w, h = 680, 215
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["turkuaz"], C["turkuaz"], r=6))
    ic.append(metin(340, 36, "KÂİNATTAKİ MÎZAN (DENGE) VE ÇEVRE AHLAKI", 13, "#fff", True))

    ic.append(kutu(20, 62, 305, 136, C["acik_turkuaz"], C["turkuaz"]))
    ic.append(metin(172, 86, "KUR’AN’DA EKOLOJİK DENGE (MÎZAN)", 11.5, C["turkuaz"], True))
    ic.append(metin(172, 112, "“Göğü yükseltti ve dengeyi (mîzanı)", 10.5, "#1a1815", True, True))
    ic.append(metin(172, 130, "O koydu. Sakın dengeyi bozmayın!”", 10.5, "#1a1815", True, True))
    ic.append(metin(172, 152, "(Rahmân suresi, 7-8. ayetler)", 10, C["turkuaz"], True))
    ic.append(metin(172, 178, "Göklerde ve yerdeki nimetler emanettir (Lokmân 20).", 9.5, "#1a1815"))

    ic.append(ok(325, 130, 355, 130, C["yesil"], 2.5))

    ic.append(kutu(355, 62, 305, 136, C["acik_yesil"], C["yesil"]))
    ic.append(metin(507, 86, "SÜNNETTE YERYÜZÜNÜ İMAR BİLİNCİ", 11.5, C["yesil"], True))
    ic.append(metin(507, 112, "“Kıyametin kopacağını bilseniz bile", 10.5, "#1a1815", True, True))
    ic.append(metin(507, 130, "elinizdeki fidanı dikiniz.”", 10.5, "#1a1815", True, True))
    ic.append(metin(507, 152, "(Hadis-i Şerif — Ahmed b. Hanbel)", 10, C["yesil"], True))
    ic.append(metin(507, 178, "Doğayı korumak, halifelik görevinin gereğidir.", 9.5, "#1a1815"))

    return svg(w, h, "".join(ic), "Rahmân suresi 7-8. ayetlerdeki mîzan ilkesi ve Hz. Peygamber’in fidan dikme hadisi")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
