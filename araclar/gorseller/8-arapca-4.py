# -*- coding: utf-8 -*-
"""8. Sınıf Arapça — 4. Hafta görsel modülü:
1. Ünite: Etkinlikler — Tiyatro, Soru Edatları, Bağlaçlar, Saatler ve Yönler"""

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
    """Tiyatro (المَسْرَح) ve Sahne Sanatları Kelime Kartları."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tiyatro ve Sahne Sanatları Kelimeleri (المَسْرَح وَالفُنُون المَسْرَحِيَّة)</text>',
    ]
    kartlar = [
        ("المَسْرَح", "Tiyatro / Sahne", "المَسْرَحُ جَمِيلٌ", C_MOR, C_ACIK_MOR, 18, 58),
        ("المَسْرَحِيَّة", "Tiyatro Oyunu", "شاهَدْتُ مَسْرَحِيَّةً", C_MAVI, C_ACIK_MAVI, 236, 58),
        ("المُمَثِّل / المُمَثِّلَة", "Erkek / Kadın Oyuncu", "المُمَثِّلُ ماهِرٌ", C_YESIL, C_ACIK_YESIL, 454, 58),
        ("الدَّوْر", "Rol", "لَعِبَ دَوْرًا مُهِمًّا", C_TURUNCU, C_ACIK_SARI, 18, 156),
        ("الخَشَبَة / الصّالَة", "Sahne / Salon", "عَلى خَشَبَةِ المَسْرَحِ", C_KIRMIZI, C_ACIK_KIRMIZI, 236, 156),
        ("التَّذْكِرَة / الجُمْهُور", "Bilet / Seyirci", "اِشْتَرَيْتُ تَذْكِرَةً", C_MOR, C_ACIK_MOR, 454, 156),
    ]
    for ar, tr, orn, renk, bg, x, y in kartlar:
        p.append(f'<rect x="{x}" y="{y}" width="208" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="{y+19}" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">{ar}</text>')
        p.append(f'<text x="{x+104}" y="{y+48}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">{tr}</text>')
        p.append(f'<text x="{x+104}" y="{y+70}" text-anchor="middle" font-size="11.5" fill="{renk}" font-weight="600">{orn}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Soru Edatları (أَدَواتُ الِاسْتِفْهام) ve Bağlaçlar (الرَّوابِط)."""
    w, h = 680, 290
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Soru Edatları (أَدَواتُ الِاسْتِفْهام) ve Cümle Bağlaçları (الرَّوابِط)</text>',
        # Sol kutu: Soru Edatları
        f'<rect x="16" y="56" width="320" height="220" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="16" y="56" width="320" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="176" y="75" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">Temel Soru Edatları</text>',
        # Sağ kutu: Bağlaçlar
        f'<rect x="348" y="56" width="316" height="220" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="316" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="506" y="75" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">Sebep-Sonuç ve Zıtlık Bağlaçları</text>',
    ]
    sorular = [
        ("هَلْ", "Mı / Mi? (Evet/Hayır)", "هَلْ تُحِبُّ المَسْرَحَ؟"),
        ("مَنْ", "Kim? (Akıllı varlıklar)", "مَنْ هٰذا المُمَثِّلُ؟"),
        ("ماذا / ما", "Ne? (Eylem / Kavram)", "ماذا تُشاهِدُ اليَوْمَ؟"),
        ("لِماذا", "Niçin / Neden?", "لِماذا تَذْهَبُ إِلى المَسْرَحِ؟"),
        ("كَيْفَ / مَتى", "Nasıl? / Ne zaman?", "مَتى تَبْدَأُ المَسْرَحِيَّةُ؟"),
    ]
    for i, (edat, anlam, orn) in enumerate(sorular):
        y = 94 + i * 35
        p.append(f'<rect x="26" y="{y}" width="68" height="27" rx="6" fill="#fff" stroke="{C_MAVI}" stroke-width="1.2"/>')
        p.append(f'<text x="60" y="{y+18}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_MAVI}">{edat}</text>')
        p.append(f'<text x="102" y="{y+13}" font-size="10.5" font-weight="700" fill="{C_KOYU}">{anlam}</text>')
        p.append(f'<text x="102" y="{y+25}" font-size="10.5" fill="{C_GRI}">{orn}</text>')

    baglaclar = [
        ("لِأَنَّ", "Çünkü (Sebep bildirir)", "أُحِبُّ المَسْرَحَ لِأَنَّهُ مُفِيدٌ"),
        ("لِذٰلِكَ", "Bu yüzden / Bundan dolayı", "العَرْضُ مُبَكِّرٌ لِذٰلِكَ خَرَجْتُ سَرِيعًا"),
        ("لٰكِنْ / لٰكِنَّ", "Fakat / Ama (Zıtlık bildirir)", "أُرِيدُ الذَّهابَ لٰكِنْ لا تُوجَدُ تَذْكِرَةٌ"),
        ("إِذَنْ", "Öyleyse / O hâlde (Çıkarım)", "أَنْتَ مُسْتَعِدٌّ، إِذَنْ هَيّا نَذْهَبْ"),
    ]
    for i, (bag, anlam, orn) in enumerate(baglaclar):
        y = 96 + i * 43
        p.append(f'<rect x="358" y="{y}" width="80" height="34" rx="6" fill="#fff" stroke="{C_YESIL}" stroke-width="1.2"/>')
        p.append(f'<text x="398" y="{y+22}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_YESIL}">{bag}</text>')
        p.append(f'<text x="446" y="{y+15}" font-size="10.5" font-weight="700" fill="{C_KOYU}">{anlam}</text>')
        p.append(f'<text x="446" y="{y+29}" font-size="10.5" fill="{C_GRI}">{orn}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Saatler (السّاعات): Tam, Buçuk, Çeyrek Geçiyor ve Çeyrek Var."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Arapçada Saatler (السّاعات): Tam, Buçuk, Çeyrek Geçiyor ve Çeyrek Var</text>',
    ]
    saatler = [
        ("03:00", "Tam Saat (تَمامًا)", "السّاعَةُ الثّالِثَةُ تَمامًا", "Saat tam üç", C_MAVI, C_ACIK_MAVI, 18),
        ("03:15", "Çeyrek Geçiyor (وَالرُّبْع)", "السّاعَةُ الثّالِثَةُ وَالرُّبْعُ", "Saat üçü çeyrek geçiyor", C_YESIL, C_ACIK_YESIL, 180),
        ("03:30", "Buçuk (وَالنِّصْف)", "السّاعَةُ الثّالِثَةُ وَالنِّصْفُ", "Saat üç buçuk", C_MOR, C_ACIK_MOR, 342),
        ("02:45", "Çeyrek Var (إِلّا الرُّبْع)", "السّاعَةُ الثّالِثَةُ إِلّا الرُّبْعَ", "Saat üçe çeyrek var", C_KIRMIZI, C_ACIK_KIRMIZI, 504),
    ]
    for dijital, baslik, ar, tr, renk, bg, x in saatler:
        p.append(f'<rect x="{x}" y="58" width="156" height="176" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="156" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+78}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<rect x="{x+34}" y="96" width="88" height="34" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+78}" y="119" text-anchor="middle" font-size="16" font-weight="800" fill="{renk}">{dijital}</text>')
        p.append(f'<text x="{x+78}" y="156" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_KOYU}">{ar}</text>')
        p.append(f'<text x="{x+78}" y="182" text-anchor="middle" font-size="10.5" fill="{C_GRI}" font-weight="600">{tr}</text>')
        ipucu = "وَ = geçiyor" if "وَ" in ar else ("إِلّا = var" if "إِلّا" in ar else "تَمامًا = tam")
        p.append(f'<text x="{x+78}" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">({ipucu})</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Ana Yönler (الجِهاتُ الأَرْبَع) ve Şehir Konumu Betimleme."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Dört Ana Yön (الجِهاتُ الأَرْبَع) ve Konum Cümleleri (تَقَعُ مَدِينَةُ...)</text>',
        # Pusula merkezi
        f'<circle cx="165" cy="150" r="46" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="2"/>',
        f'<text x="165" y="147" text-anchor="middle" font-size="12" font-weight="700" fill="{C_MAVI}">الجِهات</text>',
        f'<text x="165" y="163" text-anchor="middle" font-size="10" fill="{C_KOYU}">Ana Yönler</text>',
        # Kuzey
        f'<rect x="115" y="58" width="100" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="165" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">الشَّمال (Kuzey)</text>',
        f'<text x="165" y="88" text-anchor="middle" font-size="9.5" fill="#d6eaf8">شَمالَ تُرْكِيا</text>',
        # Güney
        f'<rect x="115" y="206" width="100" height="34" rx="8" fill="{C_KIRMIZI}"/>',
        f'<text x="165" y="223" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">الجَنُوب (Güney)</text>',
        f'<text x="165" y="236" text-anchor="middle" font-size="9.5" fill="#fadbd8">جَنُوبَ تُرْكِيا</text>',
        # Batı
        f'<rect x="16" y="133" width="90" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="61" y="150" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">الغَرْب (Batı)</text>',
        f'<text x="61" y="162" text-anchor="middle" font-size="9" fill="#ebdef0">غَرْبَ البلاد</text>',
        # Doğu
        f'<rect x="224" y="133" width="90" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="269" y="150" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">الشَّرْق (Doğu)</text>',
        f'<text x="269" y="162" text-anchor="middle" font-size="9" fill="#fdebd0">شَرْقَ البلاد</text>',
        # Sağ örnek kutusu
        f'<rect x="336" y="58" width="328" height="182" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="336" y="58" width="328" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="500" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Konum ve Şehir Betimleme Kalıpları</text>',
    ]
    ornekler = [
        ("تَقَعُ طَرابْزُون في شَمالِ تُرْكِيا.", "Trabzon Türkiye'nin kuzeyinde yer alır."),
        ("تَقَعُ أَنْطالْيا في جَنُوبِ تُرْكِيا.", "Antalya Türkiye'nin güneyinde yer alır."),
        ("تَقَعُ إِزْمِير في غَرْبِ تُرْكِيا.", "İzmir Türkiye'nin batısında yer alır."),
        ("تَقَعُ وان في شَرْقِ تُرْكِيا.", "Van Türkiye'nin doğusunda yer alır."),
    ]
    for i, (ar, tr) in enumerate(ornekler):
        y = 96 + i * 34
        p.append(f'<text x="350" y="{y+12}" font-size="12" font-weight="700" fill="{C_KOYU}">• {ar}</text>')
        p.append(f'<text x="362" y="{y+26}" font-size="10.5" fill="{C_GRI}">{tr}</text>')
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
