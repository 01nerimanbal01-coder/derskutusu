"""10-turk-dili-ve-edebiyati-2 için 6 eğitici SVG diyagramı."""
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
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["lacivert"], C["lacivert"], r=6))
    ic.append(metin(340, 36, "ŞİİRDE AHENK, RİTİM, EZGİ VE YAPI UNSURLARI", 13, "#fff", True))

    kartlar = [
        (18, "AHENK • RİTİM • EZGİ", "• Ahenk: Kelime ve ses uyumu", "• Ritim: Vurgu/durak tekrarı", "• Ezgi: Müzikal ses dizisi", C["mavi"], C["acik_mavi"]),
        (236, "ÖLÇÜ • KAFİYE • REDİF", "• Ölçü: Hece, Aruz, Serbest", "• Redif: Aynı görevli ek/kelime", "• Kafiye: Yarım, Tam, Zengin, Cinas", C["yesil"], C["acik_yesil"]),
        (454, "YAPI VE GELENEK", "• Nazım Birimi: Dörtlük / Bent", "• Nakarat / Kavuştak (Bağlama)", "• Mahlas / Tapşırma (Son dörtlük)", C["mor"], C["acik_mor"]),
    ]
    for x, bas, s1, s2, s3, k_renk, d_renk in kartlar:
        ic.append(kutu(x, 60, 206, 118, d_renk, k_renk))
        ic.append(metin(x + 103, 82, bas, 11.5, k_renk, True))
        ic.append(metin(x + 14, 108, s1, 10, "#1a1815", False, False))
        ic.append(metin(x + 14, 130, s2, 10, "#1a1815", False, False))
        ic.append(metin(x + 14, 152, s3, 10, k_renk, True, False))

    ic.append(kutu(18, 188, 642, 26, C["acik_sari"], C["sari"], r=5))
    ic.append(metin(339, 205, "Aliterasyon: Dize içi ünsüz ses tekrarı • Asonans: Dize içi ünlü ses tekrarı • Tema: Şiirdeki ana duygu", 10.5, C["sari"], True))

    return svg(w, h, "".join(ic), "Şiirde ahenk, ritim, ezgi ve yapı unsurları şeması")


def gorsel_2():
    w, h = 680, 230
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["yesil"], C["yesil"], r=6))
    ic.append(metin(340, 36, "KOŞUK NAZIM BİÇİMİ VE TÜRKÇE KELİMELERİN TARİHSEL EVRİMİ", 12.5, "#fff", True))

    # Üst: "iyi" sözcüğünün 4 aşaması
    ic.append(metin(340, 68, "“İYİ” SÖZCÜĞÜNÜN YAZILI METİNLERDEKİ TARİHSEL YOLCULUĞU", 11, C["lacivert"], True))
    asama = [
        (22, "edgü", "VIII. Yüzyıl", "Orhun Abideleri", C["kirmizi"], C["acik_kirmizi"]),
        (190, "eygü", "XIV. Yüzyıl", "Garibnâme (Âşık Paşa)", C["sari"], C["acik_sari"]),
        (358, "eyü", "XVIII. Yüzyıl", "Hayriyye (Nâbî)", C["mavi"], C["acik_mavi"]),
        (526, "iyi", "XX. Yüzyıl", "Safahat (Mehmet Âkif)", C["yesil"], C["acik_yesil"]),
    ]
    for x, kel, yy, eser, k_renk, d_renk in asama:
        ic.append(kutu(x, 78, 134, 72, d_renk, k_renk))
        ic.append(metin(x + 67, 100, kel, 13, k_renk, True))
        ic.append(metin(x + 67, 120, yy, 10, "#1a1815", True))
        ic.append(metin(x + 67, 138, eser, 9.5, "#1a1815"))

    ic.append(ok(156, 114, 190, 114, C["lacivert"]))
    ic.append(ok(324, 114, 358, 114, C["lacivert"]))
    ic.append(ok(492, 114, 526, 114, C["lacivert"]))

    # Alt: Koşuktaki kelimeler
    ic.append(kutu(22, 162, 638, 54, C["acik_turkuaz"], C["turkuaz"]))
    ic.append(metin(341, 182, "Koşukta Geçen Kelimelerin Günümüz Türkiye Türkçesindeki Karşılıkları (Biçim Değişir, Anlam Korunur)", 10.5, C["turkuaz"], True))
    ic.append(metin(341, 202, "yaşıl → yeşil  •  tag → dağ  •  buka → boğa  •  töpü → tepe  •  kayguk → kayık  •  yinçü → inci", 11, "#1a1815", True))

    return svg(w, h, "".join(ic), "Koşuktaki kelimelerin ve iyi sözcüğünün tarihsel değişimi")


def gorsel_3():
    w, h = 680, 230
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["mor"], C["mor"], r=6))
    ic.append(metin(340, 36, "SÖZLÜ GELENEKTE EVRİM: KOŞUK VE KOŞMA KARŞILAŞTIRMASI", 13, "#fff", True))

    ic.append(kutu(20, 60, 290, 156, C["acik_sari"], C["sari"]))
    ic.append(metin(165, 82, "KOŞUK (İslamiyet Öncesi)", 12, C["sari"], True))
    ic.append(metin(165, 104, "• Şair: Ozan, Kam, Baksı (Anonim)", 10.5, "#1a1815"))
    ic.append(metin(165, 124, "• Çalgı: Kopuz eşliğinde söylenir", 10.5, "#1a1815"))
    ic.append(metin(165, 144, "• Biçim: Dörtlük • 7, 8, 11’li hece", 10.5, "#1a1815"))
    ic.append(metin(165, 164, "• Kafiye: aaab, cccb, dddb...", 10.5, "#1a1815"))
    ic.append(metin(165, 186, "• Konu: Bahar, doğa, aşk, yiğitlik", 10.5, C["sari"], True))
    ic.append(metin(165, 204, "(Dîvânu Lugâti’t-Türk Örnekleri)", 9.5, C["gri"]))

    ic.append(ok(310, 138, 370, 138, C["mor"], 2.5))
    ic.append(metin(340, 126, "Evrilir", 10, C["mor"], True))

    ic.append(kutu(370, 60, 290, 156, C["acik_mor"], C["mor"]))
    ic.append(metin(515, 82, "KOŞMA (Âşık Edebiyatı)", 12, C["mor"], True))
    ic.append(metin(515, 104, "• Şair: Âşık (Son dörtlükte tapşırma)", 10.5, "#1a1815"))
    ic.append(metin(515, 124, "• Çalgı: Saz (bağlama) eşliği", 10.5, "#1a1815"))
    ic.append(metin(515, 144, "• Biçim: Dörtlük • 11’li hece ölçüsü", 10.5, "#1a1815"))
    ic.append(metin(515, 164, "• Kafiye: aaab (abab), cccb, dddb...", 10.5, "#1a1815"))
    ic.append(metin(515, 186, "• Türler: Güzelleme, Koçaklama,", 10.5, C["mor"], True))
    ic.append(metin(515, 204, "Taşlama ve Ağıt (Karacaoğlan, Köroğlu)", 10, C["mor"], True))

    return svg(w, h, "".join(ic), "Koşuk ve koşma nazım biçimlerinin karşılaştırılması")


def gorsel_4():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["kirmizi"], C["kirmizi"], r=6))
    ic.append(metin(340, 36, "TÜRKÜNÜN YAPISI (BENT - KAVUŞTAK) VE VARYANTLAŞMA", 13, "#fff", True))

    # Sol: Turnalar Türküsü Yapısı
    ic.append(kutu(20, 60, 310, 150, C["acik_kirmizi"], C["kirmizi"]))
    ic.append(metin(175, 82, "TURNALAR TÜRKÜSÜNÜN BÖLÜMLERİ", 11.5, C["kirmizi"], True))
    ic.append(kutu(34, 92, 282, 54, "#fff", C["mavi"], r=5))
    ic.append(metin(175, 110, "BENT (Asıl Konunun İşlendiği Bölüm - 3 Dize)", 10, C["mavi"], True))
    ic.append(metin(175, 128, "“İki turnam gelir aklı karalı / Birin şahin vurmuş...”", 9.5, "#1a1815", False, True))
    ic.append(kutu(34, 152, 282, 48, "#fff", C["kirmizi"], r=5))
    ic.append(metin(175, 170, "KAVUŞTAK / BAĞLAMA (Tekrarlanan 2 Dize)", 10, C["kirmizi"], True))
    ic.append(metin(175, 188, "“Katar katar olmuş gelir, turnalar...”", 9.5, "#1a1815", False, True))

    # Sağ: Yayılma ve Varyant
    ic.append(kutu(350, 60, 310, 150, C["acik_mavi"], C["mavi"]))
    ic.append(metin(505, 82, "YAYILMA VE VARYANT OLUŞUMU", 11.5, C["mavi"], True))
    ic.append(metin(505, 106, "1. Göçler, kervanlar, askerler ve gezgin", 10, "#1a1815"))
    ic.append(metin(505, 122, "âşıklar türküleri yöreden yöreye taşır.", 10, "#1a1815"))
    ic.append(metin(505, 146, "2. Kaynak kişiler söz ve ezgide kendi", 10, "#1a1815"))
    ic.append(metin(505, 162, "duygu ve yeteneklerine göre değişiklik yapar.", 10, "#1a1815"))
    ic.append(kutu(368, 174, 274, 26, "#fff", C["mavi"], r=5))
    ic.append(metin(505, 191, "Sonuç: Türkünün VARYANTLARI doğar.", 10.5, C["mavi"], True))

    return svg(w, h, "".join(ic), "Türkünün bent ve kavuştak bölümleri ile varyantlaşma süreci")


def gorsel_5():
    w, h = 680, 225
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["turkuaz"], C["turkuaz"], r=6))
    ic.append(metin(340, 36, "TÜRKÜ İLE NİNNİ KARŞILAŞTIRMASI VE SÖZLÜ KÜLTÜR MİRASI", 12.5, "#fff", True))

    ic.append(kutu(20, 60, 200, 118, C["acik_mavi"], C["mavi"]))
    ic.append(metin(120, 82, "TURNALAR (Türkü)", 11.5, C["mavi"], True))
    ic.append(metin(120, 104, "• Tema: Özlem ve gurbet", 10, "#1a1815"))
    ic.append(metin(120, 124, "• Amaç: Duyguyu paylaşmak", 10, "#1a1815"))
    ic.append(metin(120, 144, "• Yapı: Bent + Kavuştak", 10, "#1a1815"))
    ic.append(metin(120, 164, "• Ölçü: 11’li hece ölçüsü", 10, C["mavi"], True))

    ic.append(kutu(240, 60, 200, 118, C["acik_yesil"], C["yesil"]))
    ic.append(metin(340, 82, "ORTAK YÖNLER", 11.5, C["yesil"], True))
    ic.append(metin(340, 104, "• Anonim halk şiiri ürünü", 10, "#1a1815", True))
    ic.append(metin(340, 124, "• Ezgiyle (melodiyle) söylenir", 10, "#1a1815", True))
    ic.append(metin(340, 144, "• Hece ölçüsü ve sade dil", 10, "#1a1815", True))
    ic.append(metin(340, 164, "• Tekrarlarla güçlü ahenk", 10, C["yesil"], True))

    ic.append(kutu(460, 60, 200, 118, C["acik_sari"], C["sari"]))
    ic.append(metin(560, 82, "ATEM TUTAM (Ninni)", 11.5, C["sari"], True))
    ic.append(metin(560, 104, "• Tema: Evlat sevgisi / şefkat", 10, "#1a1815"))
    ic.append(metin(560, 124, "• Amaç: Bebeği uyutmak", 10, "#1a1815"))
    ic.append(metin(560, 144, "• Hitap: Küçük çocuk (oğul)", 10, "#1a1815"))
    ic.append(metin(560, 164, "• Ölçü: 7’li / 8’li hece ölçüsü", 10, C["sari"], True))

    ic.append(kutu(20, 188, 640, 26, C["acik_turkuaz"], C["turkuaz"], r=5))
    ic.append(metin(340, 205, "Diğer Sözlü Kültür Ürünleri: Masal • Âşıklık • Dede Korkut Hikâyeleri • Karagöz • Meddah • Nasreddin Hoca", 10, C["turkuaz"], True))

    return svg(w, h, "".join(ic), "Turnalar türküsü ile Atem Tutam Men Seni ninnisinin karşılaştırılması")


def gorsel_6():
    w, h = 680, 215
    ic = []
    ic.append(kutu(14, 14, 652, 34, C["sari"], C["sari"], r=6))
    ic.append(metin(340, 36, "DİLİMİZİN İNCELİKLERİ: ŞİİRDE İSİM VE SIFAT TAMLAMALARI", 13, "#fff", True))

    ic.append(kutu(20, 62, 305, 136, C["acik_mavi"], C["mavi"]))
    ic.append(metin(172, 84, "SIFAT TAMLAMASI ÖRNEKLERİ", 11.5, C["mavi"], True))
    ic.append(metin(172, 106, "(Sıfat + İsim → Varlığı niteler veya belirtir)", 10, C["gri"]))
    ic.append(metin(172, 128, "• Koşuk: “kara bulut”, “mavi bulut”, “semiz at”", 10, "#1a1815", True))
    ic.append(metin(172, 148, "• Koşma: “deli gönül”, “yalan dünya”, “kanlı yaş”", 10, "#1a1815", True))
    ic.append(metin(172, 168, "• Lisan: “açık söz”, “yeni sözler”", 10, "#1a1815", True))
    ic.append(metin(172, 188, "İşlevi: Görsel betimlemeyi ve coşkuyu güçlendirir.", 9.5, C["mavi"], True))

    ic.append(kutu(355, 62, 305, 136, C["acik_yesil"], C["yesil"]))
    ic.append(metin(507, 84, "İSİM TAMLAMASI ÖRNEKLERİ", 11.5, C["yesil"], True))
    ic.append(metin(507, 106, "(Tamlayan + Tamlanan → Aitlik kurar)", 10, C["gri"]))
    ic.append(metin(507, 128, "• Koşuk: “dağların suyu”, “inci kabı”, “göl suları”", 10, "#1a1815", True))
    ic.append(metin(507, 148, "• Koşma: “ecel şerbeti”, “dağların seli / yeli”", 10, "#1a1815", True))
    ic.append(metin(507, 168, "• Lisan: “halkın yolları”", 10, "#1a1815", True))
    ic.append(metin(507, 188, "İşlevi: Kavramlar arası bağı ve imgeyi derinleştirir.", 9.5, C["yesil"], True))

    return svg(w, h, "".join(ic), "Şiirde sıfat ve isim tamlamalarının örnekleri ve anlatıma katkısı")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
