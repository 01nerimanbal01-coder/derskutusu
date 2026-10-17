# -*- coding: utf-8 -*-
"""9. Sınıf Kur'an-ı Kerim — 4. Hafta görsel modülü:
1. Tema: Kur'an-ı Kerim'i Tanıyorum — İbrahim Suresi 40-41. Ayetler (Rabbenâ Duaları) ve Harflerin Telaffuzu"""

C_MOR = "#6c3483"
C_MAVI = "#1a5276"
C_YESIL = "#1e8449"
C_TURUNCU = "#b9770e"
C_KIRMIZI = "#922b21"
C_ACIK_MOR = "#f5eef8"
C_ACIK_MAVI = "#eaf2f8"
C_ACIK_YESIL = "#e9f7ef"
C_ACIK_SARI = "#fef9e7"
C_ACIK_KIRMIZI = "#fdedec"
C_KOYU = "#1c2833"
C_GRI = "#566573"
C_SINIR = "#d5d8dc"


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def gorsel_1():
    """İbrahim Suresi 40. Ayet: Namazı Dosdoğru Kılma Duası (Rabbenâec'alnî)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İbrahim Suresi, 40. Ayet: Hz. İbrahim\'in (as) Namaz ve Nesil Duası</text>',
        f'<rect x="18" y="56" width="644" height="62" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<text x="340" y="82" text-anchor="middle" font-size="14.5" font-weight="800" fill="{C_MAVI}">رَبِّ اجْعَلْنِي مُقِيمَ الصَّلَاةِ وَمِنْ ذُرِّيَّتِي ۚ رَبَّنَا وَتَقَبَّلْ دُعَاءِ</text>',
        f'<text x="340" y="106" text-anchor="middle" font-size="11" font-weight="600" fill="{C_KOYU}">«Ey Rabbim! Beni ve soyumdan gelecekleri namazı dosdoğru kılanlardan eyle! Ey Rabbimiz, duamı kabul buyur!»</text>',
    ]
    kelimeler = [
        ("رَبِّ اجْعَلْنِي", "Rabbim! Beni kıl / eyle", C_MAVI, C_ACIK_MAVI, 18),
        ("مُقِيمَ الصَّلَاةِ", "Namazı dosdoğru kılan", C_YESIL, C_ACIK_YESIL, 180),
        ("وَمِنْ ذُرِّيَّتِي", "ve soyumdan/neslimden olanları da", C_MOR, C_ACIK_MOR, 342),
        ("رَبَّنَا وَتَقَبَّلْ دُعَاءِ", "Rabbimiz! Duamı kabul buyur", C_TURUNCU, C_ACIK_SARI, 504),
    ]
    for ar, tr, renk, bg, x in kelimeler:
        p.append(f'<rect x="{x}" y="130" width="156" height="108" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<rect x="{x}" y="130" width="156" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+78}" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ar}</text>')
        p.append(f'<text x="{x+78}" y="190" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">{tr}</text>')
        p.append(f'<text x="{x+78}" y="220" text-anchor="middle" font-size="9.5" fill="{renk}" font-weight="700">İbrahim Suresi, 40</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """İbrahim Suresi 41. Ayet: Mağfiret (Bağışlanma) Duası (Rabbenağfirlî)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İbrahim Suresi, 41. Ayet: Anne-Baba ve Müminler İçin Bağışlanma Duası</text>',
        f'<rect x="18" y="56" width="644" height="62" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<text x="340" y="82" text-anchor="middle" font-size="14.5" font-weight="800" fill="{C_YESIL}">رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ</text>',
        f'<text x="340" y="106" text-anchor="middle" font-size="11" font-weight="600" fill="{C_KOYU}">«Ey Rabbimiz! Hesap kurulacağı (kıyamet) gününde beni, anne-babamı ve bütün müminleri bağışla!»</text>',
    ]
    kelimeler = [
        ("رَبَّنَا اغْفِرْ لِي", "Ey Rabbimiz! Beni bağışla", C_YESIL, C_ACIK_YESIL, 18),
        ("وَلِوَالِدَيَّ", "ve annemi-babamı da (bağışla)", C_MAVI, C_ACIK_MAVI, 180),
        ("وَلِلْمُؤْمِنِينَ", "ve bütün müminleri de", C_MOR, C_ACIK_MOR, 342),
        ("يَوْمَ يَقُومُ الْحِسَابُ", "Hesabın görüleceği günde (Ahiret)", C_KIRMIZI, C_ACIK_KIRMIZI, 504),
    ]
    for ar, tr, renk, bg, x in kelimeler:
        p.append(f'<rect x="{x}" y="130" width="156" height="108" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<rect x="{x}" y="130" width="156" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+78}" y="150" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ar}</text>')
        p.append(f'<text x="{x+78}" y="190" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">{tr}</text>')
        p.append(f'<text x="{x+78}" y="220" text-anchor="middle" font-size="9.5" fill="{renk}" font-weight="700">İbrahim Suresi, 41</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Kur'an Meallerinden Yararlanma İlkeleri ve Dua Bilinci."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kur\'an-ı Kerim Meallerine Başvurma ve Dua Adabı</text>',
        f'<rect x="18" y="58" width="314" height="172" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Meal ve Tefsir Nedir?</text>',
        f'<text x="32" y="106" font-size="10.5" fill="{C_KOYU}">• Meal: Kur\'an ayetlerinin başka bir dile</text>',
        f'<text x="42" y="122" font-size="10.5" fill="{C_KOYU}">yaklaşık anlamlarıyla çevrilmesidir.</text>',
        f'<text x="32" y="146" font-size="10.5" fill="{C_KOYU}">• Tefsir: Ayetlerin iniş sebepleri (esbâb-ı nüzul)</text>',
        f'<text x="42" y="162" font-size="10.5" fill="{C_KOYU}">ve hükümleriyle geniş olarak açıklanmasıdır.</text>',
        f'<text x="32" y="192" font-size="10.5" font-weight="700" fill="{C_MOR}">→ Okuduğumuz duaların mealini bilmek</text>',
        f'<text x="42" y="208" font-size="10.5" font-weight="700" fill="{C_MOR}">namazdaki huşu ve samimiyeti artırır.</text>',
        f'<rect x="348" y="58" width="314" height="172" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">İbrahim Suresi Dualarının 4 Mesajı</text>',
        f'<text x="362" y="108" font-size="10.5" font-weight="700" fill="{C_KOYU}">1) İbadette devamlılık (مُقِيمَ الصَّلَاةِ)</text>',
        f'<text x="362" y="132" font-size="10.5" font-weight="700" fill="{C_KOYU}">2) Aile ve nesil sorumluluğu (وَمِنْ ذُرِّيَّتِي)</text>',
        f'<text x="362" y="156" font-size="10.5" font-weight="700" fill="{C_KOYU}">3) Anne-babaya vefa ve dua (وَلِوَالِدَيَّ)</text>',
        f'<text x="362" y="180" font-size="10.5" font-weight="700" fill="{C_KOYU}">4) Ümmet kardeşliği ve ahiret bilinci</text>',
        f'<text x="372" y="202" font-size="10.5" font-weight="700" fill="{C_TURUNCU}">(وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ)</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Kur'an Harflerinin Çıkış Yerleri (Mahâric-i Hurûf) ve Özellikleri."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tecvit Temeli: Harflerin Çıkış Bölgeleri (Mahreç) ve Ayırt Edici Özellikleri</text>',
    ]
    mahrecler = [
        ("1. Boğaz Harfleri (الحَلْق)", "ء - هـ  |  ع - ح  |  غ - خ", "Boğazın alt, orta ve üst", "kısmından çıkan 6 harf.", C_KIRMIZI, C_ACIK_KIRMIZI, 18),
        ("2. Peltek Harfler (اللِّثَوِيَّة)", "ث — ذ — ظ", "Dil ucunun üst ön dişlerin", "ucuna değmesiyle çıkar.", C_MAVI, C_ACIK_MAVI, 236),
        ("3. Kalın (İsti'lâ) Harfler", "خ - ص - ض - غ - ط - ق - ظ", "«خُصَّ ضَغْطٍ قِظْ» (7 harf)", "Fetha ile «a/o» arası kalın okunur.", C_YESIL, C_ACIK_YESIL, 454),
    ]
    for baslik, harfler, s1, s2, renk, bg, x in mahrecler:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<rect x="{x+14}" y="96" width="180" height="38" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.3"/>')
        p.append(f'<text x="{x+104}" y="121" text-anchor="middle" font-size="14" font-weight="800" fill="{renk}">{harfler}</text>')
        p.append(f'<text x="{x+104}" y="158" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="178" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="212" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">Doğru Telaffuz (Tashîh-i Hurûf)</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
    return v
