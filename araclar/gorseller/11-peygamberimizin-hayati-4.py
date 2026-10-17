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
        'AKABE BİATLERİNE GÖTÜREN SEBEPLER (MEKKE VE YESRİB ŞARTLARI)</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Mekke'deki Tıkanıklık ve Yeni Merkez Arayışı",
        [
            "• 616-619 Boykot Yılları ve 620 Hüzün Yılı",
            "  (Ebû Tâlib ve Hz. Hatice'nin vefatı).",
            "• 620 Taif Yolculuğu'nun reddedilişle sonuçlanması.",
            "• Hz. Peygamber'in (sav) hac ve panayır mevsiminde",
            "  Mekke dışından gelen kabilelere İslam'ı tebliğ",
            "  etmesi ve güvenli bir hicret yurdu araması.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Yesrib'in (Medine) İslam'a Hazır Oluşu",
        [
            "• Evs ve Hazrec kabileleri arasında 120 yıl süren",
            "  savaşların ve 617 Buâs Savaşı'nın yorgunluğu.",
            "• İki tarafı uzlaştıracak adil bir lider arayışı.",
            "• Yesrib'deki Yahudi âlimlerden 'Son Peygamber'in",
            "  gönderilme vaktinin geldiğini' duymuş olmaları.",
            "• Hz. Peygamber'in (sav) dayılarının (Benî Neccâr)",
            "  Yesrib'de bulunması ve akrabalık bağı.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'AKABE GÖRÜŞMELERİ VE BİATLERİNİN KRONOLOJİK EVRELERİ (620-622)</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. İlk Akabe Görüşmesi (620)",
        [
            "• Nübüvvetin 11. yılı hac mevsimi.",
            "• Mina yakınlarındaki Akabe'de",
            "  Hazrec kabilesinden 6 kişiyle",
            "  (Es'ad b. Zürâre vb.) buluşma.",
            "• İlk Müslüman Yesribliler şehre",
            "  dönüp İslam'ı her evde",
            "  anlatmaya başladılar.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Birinci Akabe Biati (621)",
        [
            "• Nübüvvetin 12. yılı (10 Hazrec",
            "  + 2 Evs = 12 kişi).",
            "• Savaş şartı içermeyen ahlaki",
            "  sözleşme ('Bey'atü'n-Nisâ').",
            "• Mus'ab b. Umeyr (ra), ilk",
            "  öğretmen (Mukrî) olarak",
            "  Yesrib'e gönderildi.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. İkinci Akabe Biati (622)",
        [
            "• Nübüvvetin 13. yılı (73 erkek",
            "  + 2 kadın = 75 kişi).",
            "• Hz. Peygamber'i (sav) canları",
            "  ve malları pahasına koruma",
            "  sözü ('Bey'atü'l-Harb').",
            "• 12 Temsilci (Nakîb) seçildi ve",
            "  HİCRET kararı kesinleşti!",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'BİRİNCİ VE İKİNCİ AKABE BİATLERİNİN ÖZELLİKLERİNİN KARŞILAŞTIRMASI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Birinci Akabe Biati Maddeleri (İman &amp; Ahlak)",
        [
            "• 1) Allah'a hiçbir şeyi ortak koşmamak (Tevhid),",
            "• 2) Hırsızlık yapmamak ve zina etmemek,",
            "• 3) Çocukları öldürmemek,",
            "• 4) Kimseye iftira atmamak (bühtan etmemek),",
            "• 5) İyi ve hayırlı işlerde (ma'rûfta) Hz. Peygamber'e",
            "  itaat edip karşı gelmemek (Mümtehine, 12).",
            "• Özelliği: İnanç ve ahlak temellidir (Savaş yok).",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "İkinci Akabe Biati Maddeleri (Siyasi &amp; Askerî)",
        [
            "• 1) Hz. Peygamber Yesrib'e hicret ettiğinde onu",
            "  kendi canlarını, eşlerini ve evlatlarını korudukları",
            "  gibi koruyup savunmak,",
            "• 2) Bollukta ve darlıkta mali destekte bulunmak,",
            "• 3) İyiliği emredip kötülükten sakındırmak,",
            "• 4) Allah yolunda hiçbir kınayıcının kınamasından",
            "  korkmadan hakkı söylemek.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'İSLAM\'IN İLK MUALLİMİ: MUS\'AB BİN UMEYR (RA) VE YESRİB\'İN FETHİ</text>'
    )
    ic += _kart(
        20, 42, 720, 198,
        "Yesrib'in Kılıçla Değil Kur'an ve Güzel Ahlakla Fethi",
        [
            "• Birinci Akabe Biati (621) sonrasında Hz. Peygamber (sav), genç sahabi Mus'ab b. Umeyr'i (ra)",
            "  Yesrib'e Kur'an öğretmeni (el-Mukrî) ve İslam davetçisi olarak gönderdi.",
            "• Mus'ab b. Umeyr (ra), Es'ad b. Zürâre'nin (ra) evinde misafir kalarak tatlı dili, nezaketi ve",
            "  hikmetli tebliğiyle Evs ve Hazrec kabileleri arasındaki düşmanlığı kardeşliğe dönüştürdü.",
            "• Evs kabilesinin liderleri olan Üseyd b. Hudayr ve Sa'd b. Muâz'ın (ra) Müslüman olmasıyla",
            "  Yesrib'de (Benî Abdüleşhel yurdunda) İslam'ın girmediği tek bir ev bile kalmadı!",
            "• Ayrıca Es'ad b. Zürâre öncülüğünde İslam tarihinin İLK CUMA NAMAZI Yesrib'de kılındı.",
        ],
        "#059669", "#ecfdf5"
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
