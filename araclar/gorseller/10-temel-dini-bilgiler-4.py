# -*- coding: utf-8 -*-
"""10. Sınıf Temel Dini Bilgiler — 4. Hafta görsel modülü:
1. Ünite: Hayatın Anlamı — Dünya ve Ahiret Dengesi, Kulluk Bilinci, Salih Amel ve İstikamet"""

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
    """İslam'da Dünya ve Ahiret Dengesi (Kasas Suresi 77. Ayet)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İslam\'da Dünya ve Ahiret Dengesi (Kasas Suresi, 77. Ayet İlkesi)</text>',
        f'<rect x="18" y="56" width="208" height="182" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="208" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="122" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Dünya Hayatı (Tarla)</text>',
        f'<text x="122" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">• Geçici imtihan ve amel yurdudur.</text>',
        f'<text x="122" y="126" text-anchor="middle" font-size="10" fill="{C_GRI}">• Helal rızık kazanmak, üretmek,</text>',
        f'<text x="122" y="144" text-anchor="middle" font-size="10" fill="{C_GRI}">ilim öğrenmek ve yeryüzünü imar</text>',
        f'<text x="122" y="162" text-anchor="middle" font-size="10" fill="{C_GRI}">etmek dini bir sorumluluktur.</text>',
        f'<text x="122" y="186" text-anchor="middle" font-size="10" font-weight="700" fill="{C_MAVI}">\'Dünyadan nasibini unutma!\'</text>',
        f'<rect x="236" y="56" width="208" height="182" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="236" y="56" width="208" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="340" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">İtidalli Denge (Vasat Ümmet)</text>',
        f'<text x="340" y="106" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">Ne dünyayı tamamen terk eden</text>',
        f'<text x="340" y="124" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">ruhbanlık, ne de ahireti unutan</text>',
        f'<text x="340" y="142" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">dünyevileşme (sekülerleşme)!</text>',
        f'<text x="340" y="168" text-anchor="middle" font-size="10" fill="{C_GRI}">Bakara 201: \'Rabbimiz! Bize</text>',
        f'<text x="340" y="186" text-anchor="middle" font-size="10" font-weight="700" fill="{C_YESIL}">dünyada da ahirette de iyilik ver.\'</text>',
        f'<rect x="454" y="56" width="208" height="182" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="454" y="56" width="208" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="558" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Ahiret Hayatı (Hasat)</text>',
        f'<text x="558" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">• Ebedî karşılık ve adalet yurdudur.</text>',
        f'<text x="558" y="126" text-anchor="middle" font-size="10" fill="{C_GRI}">• Dünyada yapılan her iyilik ve</text>',
        f'<text x="558" y="144" text-anchor="middle" font-size="10" fill="{C_GRI}">kötülüğün eksiksiz karşılık</text>',
        f'<text x="558" y="162" text-anchor="middle" font-size="10" fill="{C_GRI}">bulacağı gerçek hayattır.</text>',
        f'<text x="558" y="186" text-anchor="middle" font-size="10" font-weight="700" fill="{C_MOR}">\'Ahiret yurdunu kazanmaya çalış!\'</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Hayatı Anlamlandıran Dört Temel Kavram: Ubudiyet, İstikamet, İhlas, Takva."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hayatı Anlamlandıran Dört Temel Kavram</text>',
    ]
    kavramlar = [
        ("1. Ubûdiyet (Kulluk)", "Yalnız Allah\'a boyun eğerek", "hayatın tamamını O\'nun rızasına", "uygun yaşama bilinci (Zâriyât, 56).", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("2. İstikamet (Doğruluk)", "'Emrolunduğun gibi dosdoğru ol'", "ilkesiyle inanç, söz ve davranışta", "sırat-ı müstakim üzere kalmak.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("3. İhlas (Samimiyet)", "İbadet ve iyilikleri gösterişten", "(riyadan) uzak tutarak yalnızca", "Allah rızası için yapmak.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("4. Takvâ (Sorumluluk Bilinci)", "Allah\'ın sevgisini kaybetmekten", "sakınarak haramlardan kaçınmak", "ve emirlerini titizlikle korumak.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in kavramlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Asr Suresi Işığında İnsanlığın Kurtuluş Reçetesi (4 İlke)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Asr Suresi Işığında Ziyandan (Hüsrandan) Kurtuluşun 4 Şartı</text>',
    ]
    sartlar = [
        ("1. İman Etmek (آمَنُوا)", "Tevhid inancını kalbiyle tasdik", "edip hayatına temel yapmak.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("2. Salih Amel İşlemek (عَمِلُوا الصَّالِحَاتِ)", "Kendisine, ailesine ve tüm", "insanlığa faydalı iyi işler üretmek.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("3. Hakkı Tavsiye Etmek (تَوَاصَوْا بِالْحَقِّ)", "Toplumsal hayatta doğruluğu,", "adaleti ve hakikati savunmak.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("4. Sabrı Tavsiye Etmek (تَوَاصَوْا بِالصَّبْرِ)", "Zorluklara ve günahlara karşı", "birlikte direnç ve metanet göstermek.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, renk, bg, x, y in sartlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+66}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Amel Defterini Kapatmayan Kalıcı İyilik: Sadaka-i Câriye."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Vefattan Sonra da Sevabı Kesilmeyen Üç Amel (Müslim, Vasiyyet, 14)</text>',
    ]
    ameller = [
        ("1. Sadaka-i Câriye", "İnsanların yararlanmaya devam", "ettiği okul, çeşme, hastane,", "cami, köprü ve ağaç dikmek.", C_YESIL, C_ACIK_YESIL, 18),
        ("2. Faydalı İlim", "İnsanlığa ışık tutan bilimsel/dini", "eser bırakmak veya talebe", "(öğrenci) yetiştirmek.", C_MAVI, C_ACIK_MAVI, 236),
        ("3. Hayırlı Evlat", "Anne ve babasının arkasından", "hayır dua eden, güzel ahlaklı", "ve salih evlat yetiştirmek.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in ameller:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="152" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
