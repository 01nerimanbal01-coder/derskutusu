def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_Yuk = 32
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_Yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_Yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_Yuk + 20
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="12">'
            f'{st}</text>'
        )
        yy += 19
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="270" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="30" fill="#0f172a" font-size="15" font-weight="bold" text-anchor="middle">'
        'RİSALET ÖNCESİ HZ. MUHAMMED\'İN (SAV) ÇOCUKLUK VE GENÇLİK EVRELERİ</text>'
    )
    ic += _kart(
        20, 45, 230, 105,
        "1. Doğum ve Sütanne (571-575)",
        [
            "• 20 Nisan 571 (12 Rebîülevvel) Mekke",
            "• Babası Abdullah, doğumdan önce vefat",
            "• Beni Sa'd yurdu: Sütannesi Halîme",
            "• Çöl havası ve fasih Arapça eğitimi",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 45, 230, 105,
        "2. Anne ve Dede Himayesi (575-579)",
        [
            "• 6 yaşında Ebvâ'da annesi Âmine'nin vefatı",
            "• Dadısı Ümmü Eymen'in (Bereke) şefkati",
            "• 6-8 yaş: Dedesi Abdülmuttalib himayesi",
            "• Dedesinin vefatıyla amcasına emanet",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 45, 230, 105,
        "3. Ebû Tâlib ve Gençlik (579+)",
        [
            "• Amcası Ebû Tâlib ve Fâtıma binti Esed",
            "• Çobanlık yaparak alın teri ve sabır",
            "• 12 yaşında Busra ticaret yolculuğu",
            "• Dürüst ticaret ve 'el-Emîn' unvanı",
        ],
        "#d97706", "#fffbeb"
    )
    ic += (
        '<rect x="20" y="165" width="720" height="95" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>'
        '<text x="380" y="188" fill="#5b21b6" font-size="13" font-weight="bold" text-anchor="middle">'
        'CAHİLİYE KARANLIĞINDA KORUNMUŞ BİR HAYAT (İSMET VE EMÂNET)</text>'
        '<text x="35" y="210" fill="#1e293b" font-size="12">'
        '• Hz. Muhammed (sav) risalet öncesinde de putlara asla tapmamış, içki, kumar ve panayır eğlencelerinden uzak durmuştur.</text>'
        '<text x="35" y="230" fill="#1e293b" font-size="12">'
        '• Mekke halkı en kıymetli emanetlerini ona teslim etmiş ve oybirliğiyle ona "Muhammedü\'l-Emîn" (Güvenilir Muhammed) demiştir.</text>'
        '<text x="35" y="250" fill="#475569" font-size="11.5" font-style="italic">'
        '• Çocuk yaşta yetim ve öksüz kalması, onun mazlumlara, yetimlere ve kimsesizlere karşı eşsiz bir merhamet geliştirmesini sağlamıştır.</text>'
    )
    return _svg(760, 280, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="30" fill="#0f172a" font-size="15" font-weight="bold" text-anchor="middle">'
        'TOPLUMSAL BARIŞ VE ADALET ADIMLARI: FİCÂR SAVAŞI VE HİLFÜ\'L-FUDÛL</text>'
    )
    ic += _kart(
        20, 48, 345, 195,
        "Ficâr Savaşları'nda (580-590) Tutumu",
        [
            "• Haram aylarda (Zilkade, Zilhicce, Muharrem, Receb)",
            "  kan döküldüğü için 'Ficâr (Günah/İhlal)' denmiştir.",
            "• Kureyş-Kinâne ile Kays-Aylân kabileleri arasında",
            "  çıkan bu savaşta Hz. Peygamber (sav) kan dökmemiştir.",
            "• Yalnızca amcalarının yanında bulunup atılan okları",
            "  toplamış ve kalkanlarla savunmaya destek olmuştur.",
            "• Savaş yerine sulh ve uzlaşı kültürünü savunmuştur.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 48, 345, 195,
        "Hilfü'l-Fudûl (Erdemliler Cemiyeti - 590)",
        [
            "• Yemenli Zebîd kabilesinden bir tacirin Âs b. Vâil",
            "  tarafından gasp edilen hakkını aramasıyla doğdu.",
            "• Zübeyr b. Abdülmuttalib öncülüğünde Abdullah b.",
            "  Cüd'ân'ın evinde toplanan erdemli insanlar kurdu.",
            "• İlke: 'Mekke'de yerli veya yabancı hiçbir mazlum",
            "  hakkını alıncaya kadar yalnız bırakılmayacaktır!'",
            "• Hz. Peygamber: 'İslam'da da çağrılsam yine icabet ederim.'",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 270, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="30" fill="#0f172a" font-size="15" font-weight="bold" text-anchor="middle">'
        'DÜRÜST TİCARET (MUDÂREBE) VE HZ. HATİCE (RA) İLE ÖRNEK AİLE HAYATI</text>'
    )
    ic += _kart(
        20, 48, 345, 195,
        "Şam Ticaret Kervanı ve Mudârebe (595)",
        [
            "• Mekke'nin iffetli ve saygın taciri Hz. Hatice (Tâhire),",
            "  Hz. Muhammed'e (sav) kervan ortaklığı teklif etti.",
            "• Yardımcı Meysere, yolculuk boyunca onun dürüstlüğüne,",
            "  tatlı diline ve ticaret ahlakına hayran kaldı.",
            "• Hile yapmadan ve yemin etmeden en bereketli kâr elde",
            "  edildi; güven (emânet) en büyük sermaye oldu.",
            "• Dönüşte Meysere'nin gözlemleri evlilik kapısını açtı.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 48, 345, 195,
        "Mübarek Evlilik ve Neslin Devamı (595)",
        [
            "• Hz. Muhammed (sav) 25, Hz. Hatice (ra) 40 yaşındayken",
            "  ebedî vefa ve sevgi temeli üzerine evlendiler.",
            "• 25 yıl süren bu evlilikte sadakat, istişare ve huzur",
            "  hâkim oldu; Zeyd b. Hârise ve Hz. Ali himaye edildi.",
            "• Çocukları: Kâsım (Ebü'l-Kâsım künyesi), Abdullah,",
            "  Zeyneb, Rukiyye, Ümmü Gülsûm ve Fâtıma (ra).",
            "• Soyu (Ehl-i Beyt) kızı Hz. Fâtıma üzerinden devam etti.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 270, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="30" fill="#0f172a" font-size="15" font-weight="bold" text-anchor="middle">'
        'KÂBE HAKEMLİĞİ (605) VE HİRÂ\'DA İNZİVA (TEFEKKÜR DÖNEMİ)</text>'
    )
    ic += _kart(
        20, 48, 345, 195,
        "Kâbe'nin Tamiri ve Hacerü'l-Esved Hakemliği",
        [
            "• 605 yılında Kâbe duvarları yenilenirken Hacerü'l-Esved'i",
            "  yerine hangi kabilenin koyacağı krize dönüştü.",
            "• Kan dökülmek üzereyken Benî Şeybe kapısından ilk",
            "  giren kişi olan 'el-Emîn' (Hz. Muhammed) hakem seçildi.",
            "• Taşı bir yaygının (ridâ) ortasına koyup tüm kabile",
            "  reislerine uçlarından tutturarak ortak onur sağladı.",
            "• Taşı mübarek elleriyle yerine koyup savaşı önledi.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        395, 48, 345, 195,
        "Hanîf Arayışı ve Hirâ Mağarası'nda Tehannüs",
        [
            "• 35 yaşından itibaren Mekke'nin putperestliğinden ve",
            "  sosyal zulmünden uzaklaşıp yalnızlığı (uzlet) seçti.",
            "• Özellikle Ramazan aylarında Nur Dağı'ndaki (Cebel-i",
            "  Nûr) Hirâ Mağarası'nda tefekkür ve ibadet (tehannüs) etti.",
            "• Hz. İbrâhim'in tevhid dini (Hanîflik) üzere kâinatın",
            "  yaratılış gayesini ve hakikati derinlemesine düşündü.",
            "• Sadık rüyalar (rü'yâ-yı sâdıka) ile vahye hazırlandı.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 270, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][3]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]

