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
        'MÜSLÜMAN BİLİM İNSANLARININ DİNİ VE SOSYAL BİLİMLERDEKİ ÖNCÜ ÇALIŞMALARI</text>'
    )
    ic += _kart(20, 44, 310, 190, "TEFSİR, HADİS, KELAM VE FIKIH", [
        "• Tefsir: Taberî (Câmiu'l-Beyân), Zemahşerî (el-Keşşâf),",
        "  Fahreddin er-Râzî (Mefâtîhu'l-Gayb), Elmalılı Hamdi Yazır.",
        "• Hadis: Buhârî, Müslim, Tirmizî, Ebu Davud, Nesâî,",
        "  İbn Mâce (Kütüb-i Sitte müellifleri).",
        "• Kelam: İmam Mâtürîdî (Kitâbü't-Tevhîd), İmam Eş'arî,",
        "  İmam Gazzâlî (İhyâu Ulûmi'd-Dîn).",
        "• Fıkıh: Ebu Hanife (Fıkh-ı Ekber), İmam Şâfiî (er-Risâle)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "TARİH, COĞRAFYA, FELSEFE VE DİL", [
        "• Tarih ve Sosyoloji: İbn Haldun (Mukaddime - Modern",
        "  sosyolojinin ve tarih felsefesinin kurucusu).",
        "• Coğrafya: İdrîsî (Dünya haritası), Pîrî Reis (Kitâb-ı",
        "  Bahriye ve Dünya Haritası), Kâtip Çelebi (Cihannüma),",
        "  Evliya Çelebi (Seyahatname), Belhî ve Mes'ûdî.",
        "• Felsefe: Kindî, Fârâbî (Muallim-i Sânî), İbn Sînâ, İbn Rüşd.",
        "• Dil: Kaşgarlı Mahmud (Dîvânu Lugâti't-Türk), Sîbeveyh."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MÜSLÜMAN BİLİM İNSANLARININ FEN VE DOĞA BİLİMLERİNDEKİ ÖNCÜLÜKLERİ</text>'
    )
    alanlar = [
        ("TIP VE ECZACILIK", "İbn Sînâ (el-Kânûn fi't-Tıb - Batı'da 600 yıl ders kitabı), Ebû Bekir er-Râzî (Çiçek-kızamık), İbnü'n-Nefîs (Küçük kan dolaşımı), Akşemseddin (Mikrop).", "#DC2626", "#FEF2F2"),
        ("MATEMATİK VE ASTRONOMİ", "Hârizmî (Cebirin kurucusu ve '0' rakamı - Kitâbü'l-Cebr), Ömer Hayyam, Uluğ Bey (Semerkant Rasathanesi), Ali Kuşçu (Risâle fi'l-Hey'e), Ферganî, Battânî.", "#2563EB", "#EFF6FF"),
        ("FİZİK, OPTİK VE MEKANİK", "İbnü'l-Heysem (Optik ilminin ve karanlık oda/kamera kurucusu - Kitâbü'l-Menâzır), Cezerî (Sibernetik ve robotik biliminin öncüsü - Kitâbü'l-Hiyel).", "#7C3AED", "#F5F3FF"),
        ("KİMYA VE BİYOLOJİ", "Câbir bin Hayyân (Modern kimyanın babası; imbik, kristalleştirme, nitrik ve sülfürik asit keşfi), Bîrûnî (Özgül ağırlık hesabı), Câhız (Kitâbü'l-Hayevân).", "#059669", "#ECFDF5")
    ]
    for i, (b, m, r, bg) in enumerate(alanlar):
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
        'BATI DÜNYASINI ETKİLEYEN BÜYÜK ESERLER VE UNVANLAR</text>'
    )
    ic += _kart(20, 44, 205, 190, "AVİCENNA VE AL-KHWARIZMI", [
        "• İbn Sînâ (Batı'da Avicenna):",
        "  'el-Kânûn fi't-Tıb' ve",
        "  'Kitâbü'ş-Şifâ'.",
        "• Hârizmî (Algoritmi):",
        "  Cebir ve Algoritma",
        "  kavramlarının isim babası;",
        "  'Kitâbü'l-Cebr ve'l-Mukâbele'."
    ], "#0D9488", "#F0FDFA")
    ic += _kart(237, 44, 205, 190, "ALHAZEN VE GEBER", [
        "• İbnü'l-Heysem (Alhazen):",
        "  'Kitâbü'l-Menâzır' ile görme",
        "  olayını doğru açıkladı.",
        "• Câbir bin Hayyân (Geber):",
        "  Deneysel kimyanın kurucusu;",
        "  atomun parçalanabileceğini",
        "  asyrlar önce öngördü."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "CEZERÎ VE Zehrâvî", [
        "• el-Cezerî (Cizreli):",
        "  Su saatleri, şifreli kilitler",
        "  ve krank mili (Sibernetik).",
        "• ez-Zehrâvî (Abulcasis):",
        "  Cerrahi aletlerin mucidi",
        "  (Kitâbü't-Tasrîf); kedi",
        "  bağırsağından dikiş ipliği."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KUR\'AN\'DAN MESAJLAR: FÂTIR SURESİ 27-28. AYETLER (KEVNÎ AYETLER VE HUŞÛ)</text>'
    )
    ic += _kart(20, 44, 310, 190, "DOĞADAKİ ÇEŞİTLİLİK VE BİLİM (FÂTIR, 27)", [
        "• Gökten indirilen su ile rengârenk meyvelerin",
        "  yetiştirilmesi (Botanik ve Tarım bilimi).",
        "• Dağlarda beyaz, kırmızı, simsiyah çeşitli renklerde",
        "  yolların ve kayaç katmanlarının bulunması (Jeoloji).",
        "• İnsanların, canlıların ve hayvanların da türlü",
        "  renk ve özelliklerde yaratılması (Biyoloji ve Genetik)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "ALİMLERİN HAŞYETİ (FÂTIR, 28)", [
        "• 'Kulları içinden ancak âlimler (bilenler), Allah'tan",
        "  (gereği gibi) korkar / derin saygı (haşyet) duyar.'",
        "  (İnnemâ yahşallâhe min ibâdihi'l-ulemâu).",
        "• 'Ulemâ' yalnız din alimlerini değil, evrendeki kevnî",
        "  ayetleri inceleyerek Allah'ın sonsuz ilim ve kudretine",
        "  hayran kalan tüm doğa ve fen bilimcilerini de kapsar!"
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
