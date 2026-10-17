def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÂL-İ İMRÂN SURESİ 7-9. AYETLER BAĞLAMI: RÂSİHÛN (İLİMDE DERİNLEŞENLER)</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Kalplerinde Eğrilik (Zeyğ) Olanlar",
        [
            "• Âl-i İmrân 7. ayette Kur'an ayetlerinin",
            "  'Muhkem' (açık/kesin) ve 'Müteşâbih' (çok",
            "  anlamlı/yoruma açık) olduğu bildirilir.",
            "• Kalplerinde eğrilik (zeyğ) bulunanlar,",
            "  fitne çıkarmak ve kendi arzularına göre",
            "  tevil etmek için müteşâbihlerin peşine düşer.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Râsihûn fi'l-İlm ve Ulü'l-Elbâb'ın Duası",
        [
            "• İlimde derinleşip kök salanlar (er-Râsihûn)",
            "  ve selim akıl sahipleri (Ulü'l-Elbâb):",
            "  'Ona inandık, hepsi Rabbimiz katındandır' der.",
            "• Ardından 8 ve 9. ayetlerdeki 'Rabbenâ lâ",
            "  tüziğ kulûbenâ...' duasıyla kalplerinin",
            "  hidayet üzere sabit kalması için yakarırlar.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÂL-İ İMRÂN SURESİ 8. AYETİN BÖLÜMLERİ VE KAVRAM ANALİZİ</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Hidayet ve Sebat Talebi",
        [
            "• 'Rabbenâ lâ tüziğ kulûbenâ",
            "  ba'de iz hedeytenâ'",
            "• Meal: 'Rabbimiz! Bizi hidayete",
            "  (doğru yola) erdirdikten sonra",
            "  kalplerimizi eğriltme (saptırma)!'",
            "• Anahtar Kavram: Zeyğ (Haktan",
            "  sapma) ve Hidayet (Doğru yol).",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. İlahi Rahmet İsteği",
        [
            "• 'Ve heb lenâ min ledünke",
            "  rahmeh'",
            "• Meal: 'Ve bize kendi katından",
            "  (ledünnünden) bir rahmet",
            "  bağışla (lütfet)!'",
            "• Anahtar Kavram: Hibe (Karşılıksız",
            "  ihsan) ve Rahmet (Şefkat).",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. el-Vehhâb Esmaülhüsnası",
        [
            "• 'İnneke ente'l-Vehhâb'",
            "• Meal: 'Şüphesiz ki Sen,",
            "  karşılıksız olarak çokça",
            "  bağışlayansın (el-Vehhâb)!'",
            "• Dua Edebi: İstekten hemen",
            "  sonra o istekle uyumlu",
            "  Esmaülhüsna ile Allah'ı övmek.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÂL-İ İMRÂN SURESİ 9. AYET: AHİRET BİLİNCİ VE İLAHİ VAAT</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Yevmü'l-Cem' (Toplanma / Mahşer Günü)",
        [
            "• 'Rabbenâ inneke câmiu'n-nâsi li-yevmin",
            "  lâ raybe fîh'",
            "• Meal: 'Rabbimiz! Şüphesiz Sen, gerçekleşmesinde",
            "  hiçbir şüphe (rayb) olmayan bir günde",
            "  insanları bir araya toplayacak olansın.'",
            "• Haşir ve hesap gününe sarsılmaz iman ikrarıdır.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Mîâd (Sözünde Durma ve Vaat)",
        [
            "• 'İnnallâhe lâ yuhlifü'l-mîâd'",
            "• Meal: 'Şüphesiz Allah vaadinden (verdiği",
            "  sözden) asla dönmez!'",
            "• Müminlere müjde: Allah, imanlarında sebat",
            "  edenleri mükâfatlandıracağı ve dualarını",
            "  kabul edeceği sözünden asla caymaz.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'KUR\'AN MEALLERİNDEN DUAYI ANLAMA VE SINIFLANDIRMA SÜRECİ (KK.11.1.4)</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "a-b) Meal Bulma ve Konu Tespiti",
        [
            "• Farklı güvenilir meallerden",
            "  (Diyanet, Elmalılı vb.) Âl-i",
            "  İmrân 8-9. ayetler incelenir.",
            "• Temel konular: İman, hidayette",
            "  sebat, kalbin korunması,",
            "  ilahi rahmet ve ahirete iman.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "c) İçeriklerine Göre Sınıflandırma",
        [
            "• 1. Talep (İstek) Cümleleri:",
            "  'Kalplerimizi kaydırma' ve",
            "  'Bize rahmet bağışla'.",
            "• 2. Sena (Övgü) ve İkrar:",
            "  'Sen el-Vehhâb'sın', 'İnsanları",
            "  toplayacaksın', 'Vaadinden dönmez'.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "ç-d) Çıkarım ve Hayata Yansıtma",
        [
            "• Hidayete ermek kadar hidayeti",
            "  korumak (istikamet) da önemlidir.",
            "• Hz. Peygamber'in (sav): 'Ey",
            "  kalpleri evirip çeviren Allah'ım!",
            "  Kalbimi dinin üzere sabit kıl'",
            "  duasıyla bütünleştirilir.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


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