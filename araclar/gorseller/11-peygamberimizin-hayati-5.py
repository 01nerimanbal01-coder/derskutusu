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
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'HİCRET YOLCULUĞU: EMANET, PLANLAMA VE TEVEKKÜL (622)</text>'
    )
    ic += _kart(20, 44, 310, 200, "HİCRET HAZIRLIĞI VE EMANET BİLİNCİ", [
        "• Darü'n-Nedve'de müşriklerin suikast kararı alması.",
        "• Hz. Ali'nin (r.a.) canını ortaya koyarak Peygamberimizin",
        "  yatağında yatması ve Mekkelilerin emanetlerini",
        "  sahiplerine teslim etmek üzere görevlendirilmesi.",
        "• Yol arkadaşı: Hz. Ebu Bekir (es-Sıddık).",
        "• Kuzey (Medine) yerine önce Güneydeki Sevr Mağarası'na",
        "  gidilmesi: Kusursuz tedbir, gizlilik ve stratejik planlama."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 200, "SEVR MAĞARASI VE YOLCULUK EKİBİ", [
        "• Tevbe Suresi 40. Ayet: 'Üzülme! Şüphesiz Allah",
        "  bizimle beraberdir (Lâ tahzen innallâhe meanâ).'",
        "• Hz. Esma (Zâtü'n-Nitâkayn): Mağaraya azık taşıdı.",
        "• Abdullah bin Ebu Bekir: Mekke'den istihbarat getirdi.",
        "• Amir bin Füheyre: Koyun otlatarak ayak izlerini sildi.",
        "• Abdullah bin Uraykıt: Güvenilir ve uzman yol rehberi.",
        "• Süraka bin Malik'in takibi ve mucizevi şekilde vazgeçişi."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KUBA MESCİDİ, İLK CUMA NAMAZI VE MEDİNE\'YE VARIŞ</text>'
    )
    adimlar = [
        ("1. KUBA'YA VARIŞ VE KUBA MESCİDİ", "İslam tarihinde takva üzerine kurulan İLK MESCİT olan Kuba Mescidi inşa edildi (Tevbe, 108); burada 14 gün kalındı.", "#059669", "#ECFDF5"),
        ("2. RANUNA VADİSİ VE İLK CUMA NAMAZI", "Kuba'dan Medine'ye ilerlerken Salim bin Avf yurdundaki Ranuna Vadisi'nde İslam tarihinin İLK CUMA HUTBESİ ve NAMAZI kılındı.", "#2563EB", "#EFF6FF"),
        ("3. YESRİB'İN 'MEDİNETÜ'N-NEBİ' OLUŞU", "Medineliler büyük bir coşkuyla Peygamberimizi karşıladı; Yesrib şehri 'Medinetü'n-Nebi' (Peygamber Şehri / Medine) adını aldı.", "#7C3AED", "#F5F3FF"),
        ("4. EBU EYYUB EL-ENSARİ'YE MİSAFİRLİK", "Devesi Kasva'nın çöktüğü arsa satın alınarak Mescid-i Nebi tamamlanana kadar 7 ay Ebu Eyyub el-Ensari'nin evinde misafir kalındı.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MEDİNE\'DE İSLAM TOPLUMUNUN VE DEVLETİNİN KURUCU ADIMLARI</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. MESCİD-İ NEBİ VE SUFFE", [
        "• İbadet, yönetim, adalet",
        "  ve istişare merkezi.",
        "• Suffe: Mescidin bitişiğinde",
        "  kurulan İslam'ın ilk yatılı",
        "  eğitim kurumu (Üniversite).",
        "• Ashab-ı Suffe: İlim öğrenip",
        "  öğretmen olarak yetişen",
        "  sahabiler (Örn: Ebu Hüreyre)."
    ], "#0D9488", "#F0FDFA")
    ic += _kart(237, 44, 205, 190, "2. MUÂHÂT (KARDEŞLEŞTİRME)", [
        "• Mekkeli Muhacirler ile",
        "  Medineli Ensar arasında",
        "  ilan edilen iman kardeşliği.",
        "• Evs ve Hazrec arasındaki",
        "  120 yıllık Buas savaşları",
        "  son buldu.",
        "• Mallar ve imkanlar îsâr",
        "  ahlakıyla paylaşıldı."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. MEDİNE VESİKASI VE ÇARŞI", [
        "• Medine Sözleşmesi: Müslüman",
        "  ve Yahudilerin haklarını",
        "  belirleyen İLK YAZILI ANAYASA.",
        "• Medine İslam Devleti resmen",
        "  kuruldu.",
        "• İlk nüfus sayımı (1500 kişi).",
        "• Dürüst ticaret için yeni",
        "  Medine Pazarı kuruldu."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'HİCRETİN İSLAM TARİHİNDEKİ SONUÇLARI VE ÖNEMİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "DİNİ VE SOSYAL SONUÇLARI", [
        "• Müslümanlar müşriklerin baskı ve işkencesinden",
        "  kurtularak dinlerini özgürce yaşama imkanı buldu.",
        "• İslam dini Mekke sınırlarını aşarak bütün Arap",
        "  Yarımadası'na ve dünyaya yayılma zemini kazandı.",
        "• Kabilecilik (asabiyet) anlayışının yerini 'Ensar-Muhacir'",
        "  merkezli evrensel 'Ümmet ve İman Kardeşliği' aldı."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "SİYASİ VE KÜLTÜREL SONUÇLARI", [
        "• Medine'de 'İslam Şehir Devleti' kuruldu; Hz. Peygamber",
        "  hem dini rehber hem de devlet başkanı oldu.",
        "• Ezan uygulaması başladı (Abdullah bin Zeyd'in rüyası",
        "  ve ilk müezzin Bilal-i Habeşi).",
        "• Hz. Ömer'in halifeliği döneminde Hicret yılı (622),",
        "  'Hicri Takvim'in başlangıcı olarak kabul edildi."
    ], "#D97706", "#FEF3C7")
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