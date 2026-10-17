def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KEHF SURESİ 60-82. AYETLER: HZ. MUSA VE HIZIR (A.S.) KISSASI</text>'
    )
    ic += _kart(20, 44, 310, 190, "İLİM YOLCULUĞU VE MECMAU'L-BAHREYN", [
        "• Hz. Musa'nın genç yardımcısı (Yûşa bin Nûn) ile",
        "  'iki denizin birleştiği yere' (Mecmau'l-Bahreyn)",
        "  doğru çıktığı zahmetli ilim yolculuğu.",
        "• Buluşma işareti: Azık olarak aldıkları balığın",
        "  kaya yanında canlanıp denize dalması.",
        "• Allah'ın katından rahmet ve özel bir ilim (İlm-i Ledün)",
        "  verdiği salih kul (Hızır a.s.) ile karşılaşma."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "ÖĞRENCİ - MUALLİM ADABI (66-70. AYETLER)", [
        "• Hz. Musa'nın tevazu dolu talebi: 'Sana öğretilen",
        "  doğru bilgiden (rüşd) bana da öğretmen için sana",
        "  tabi olabilir miyim?'",
        "• Hızır (a.s.)'ın uyarısı: 'İç yüzünü (hikmetini)",
        "  kavrayamadığın bir şeye nasıl sabredeceksin?'",
        "• Şart: 'Ben sana açıklayıncaya kadar bana hiçbir",
        "  şey sorma!' (İlimde sabır ve teslimiyet şartı)."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'YOLCULUKTAKİ ÜÇ OLAY: ZAHİRİ GÖRÜNÜŞ VE BATINİ HİKMET (71-82. AYETLER)</text>'
    )
    olaylar = [
        ("1. OLAY: GEMİNİN DELİNMESİ (71, 79. AYETLER)", "Zahirde kusur gibi görünen olayın hikmeti: İlerideki zalim kral sağlam gemilere zorla el koyuyordu; yoksul balıkçıların gemisi kurtarıldı.", "#0284C7", "#F0F9FF"),
        ("2. OLAY: ÇOCUĞUN ÖLDÜRÜLMESİ (74, 80-81. AYETLER)", "Hikmeti: Anne ve babası salih müminlerdi; çocuğun ileride azgınlık ve küfürle onları saptırmasından korkuldu, hayırlı evlat dilendi.", "#DC2626", "#FEF2F2"),
        ("3. OLAY: YIKILMAK ÜZERE OLAN DUVARIN ONARILMASI (77, 82. AYETLER)", "Hikmeti: Duvar şehirdeki iki yetim çocuğa aitti, altında onlara ait bir hazine vardı ve babaları salih bir kimseydi.", "#059669", "#ECFDF5"),
        ("SONUÇ İLKESİ (82. AYET SONU)", "'Ben bunları kendiliğimden yapmadım; işte hakkında sabredemediğin olayların iç yüzü (te'vili) budur!'", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(olaylar):
        y = 44 + i * 50
        ic += (
            f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KISSADAN ÇIKARILACAK EVRENSEL İLKELER VE İLM-İ LEDÜN</text>'
    )
    ic += _kart(20, 44, 310, 190, "ZAHİRİ İLİM VE BATINİ HİKMET (İLM-İ LEDÜN)", [
        "• Hz. Musa: Şeriat ve zahiri (görünür) hükümlerle",
        "  sorumlu Ulu'l-Azm bir peygamberdir; bu yüzden",
        "  görünürde haksızlık gibi duran olaylara hemen itiraz etmiştir.",
        "• Hızır (a.s.): Allah'ın kendisine olayların perde",
        "  arkasını (İlm-i Ledün) bildirdiği özel kuldur.",
        "• Mesaj: 'Her bilenin üstünde daha iyi bir bilen vardır'",
        "  (Yusuf, 76); ilimde kibir ve 'en çok ben bilirim' denmez."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "KADER, HAYIR-ŞER VE SALİH BABANIN MİRASI", [
        "• İnsanların şer (kötülük) sandığı pek çok olayın",
        "  arkasında Allah'ın takdir ettiği büyük bir hayır ve",
        "  rahmet bulunabilir (Bakara, 216).",
        "• Yetimlerin duvarının korunma sebebi: 'Babaları",
        "  salih (iyi ve dürüst) bir insandı' (Kehf, 82).",
        "• Ebeveynin dürüstlüğü, takvası ve helal lokması,",
        "  vefatından sonra bile evlatlarının korunmasına vesile olur."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KEHF SURESİ 60-82. AYETLERDE TECVİT UYGULAMALARI</text>'
    )
    ic += _kart(20, 44, 205, 190, "MED VE HEMZELER", [
        "• lâ ebrahu: Medd-i Munfasıl",
        "  ve be harfinde Kalkale.",
        "• e-raeyte iz eveynâ:",
        "  Medd-i Lin ve Medd-i Tabii.",
        "• mâ ente: Medd-i Munfasıl",
        "  ve nun + te -> İhfa.",
        "• şey'en imrâ: İzhar ve İvaz."
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "İDGAM VE İHFA", [
        "• rahmeten min indinâ:",
        "  Tenvin + Mim -> İdgam-ı",
        "  Meal Gunne; Nun + İ -> İzhar;",
        "  Nun + Dal -> İhfa.",
        "• min ledünnâ: Nun + Lam ->",
        "  İdgam-ı Bila Gunne.",
        "• nefse(n) zekiyyeten: İhfa."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "KALKALE VE VAKIF", [
        "• mecmea, ebluğa, hukubâ,",
        "  kıdراً, sabrâ, ecrâ:",
        "  B, C, D, K, T harfleri sakin",
        "  okunduğunda KALKALE.",
        "• Ayet sonları üstün tenvin",
        "  (hukubâ, سربâ, kasasâ, imrâ):",
        "  Durulduğunda MEDD-İ İVAZ."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
