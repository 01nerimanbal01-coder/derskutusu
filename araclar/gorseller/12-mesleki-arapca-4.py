# -*- coding: utf-8 -*-
"""12. Sınıf Mesleki Arapça — 4. Hafta görsel modülü: Tevhit ve Şirk, İhlâs-Şirk Kavramları ve Mu'tel Fiillerin Çekimi."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">ET-TEVHÎD, EL-İHLÂS VE EŞ-ŞİRK KAVRAMLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "et-Tevhîd ve el-İhlâs (Allah'ı Birlemek)", [
        "• et-Tevhîd: İfrâdu'llâhi bi'l-ibâde (İbadette",
        "  yalnızca Allah'ı birlemek ve eş koşmamak)",
        "• el-İhlâs: Dini ve ibadeti riyadan, şirkten",
        "  arındırarak yalnız Allah için halis kılmak",
        "• el-Muvahhid: Allah'ın birliğine inanan mümin",
        "• Kelimetü't-Tevhîd: Lâ ilâhe illallâh"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "eş-Şirk ve Türleri (Ortak Koşmak)", [
        "• eş-Şirk: İttihâzü şerîkin lillâh (Allah'a zatında,",
        "  sıfatlarında veya ibadetinde ortak koşmak)",
        "• eş-Şirkü'l-Ekber: İnsanı dinden çıkaran büyük şirk",
        "• eş-Şirkü'l-Asğar (er-Riyâ): Gösteriş için ibadet",
        "• 'İnne'ş-şirke le-zulmün azîm' (Lokmân 13):",
        "  Şüphesiz şirk çok büyük bir zulümdür!"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">KUR\'AN\'DA TEVHİT VE ŞİRK AYETLERİ (NİSÂ 48 VE LOKMÂN 13)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Nisâ Suresi 48 ve 116. Ayetler", [
        "• 'İnnallâhe lâ yağfiru en yüşrake bihî'",
        "  (Şüphesiz Allah kendisine ortak koşulmasını bağışlamaz)",
        "• 'Ve yağfiru mâ dûne zâlike li-men yeşâ''",
        "  (Bunun dışındaki günahları dilediği kimse için bağışlar)",
        "• Tövbe edilmeden ölünürse şirk affedilmez",
        "• Tevhit ise cennetin ve mağfiretin anahtarıdır"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "İhlâs Suresi ve Zümer Suresi 3. Ayet", [
        "• 'Kul hüvallâhu ehad, Allâhü's-Samed'",
        "  (De ki: O Allah birdir; Allah Samed'dir)",
        "• 'Lem yelid ve lem yûled ve lem yekün lehû küfüven ehad'",
        "  (Doğurmamış ve doğmamıştır; hiçbir dengi yoktur)",
        "• 'Elâ lillâhi'd-dînü'l-hâlis' (Zümer 3):",
        "  (İyi bilin ki halis din yalnız Allah'ındır)"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">MU\'TEL FİİLLERİN MAZİ, MUZÂRİ VE EMİR ÇEKİM ÖZELLİKLERİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Misal Fiil Çekimi", [
        "• İlk harfi illetli: Vecede",
        "• Mazi: Vecede - Vecedâ - Vecedû",
        "• Muzâri çekiminde başındaki",
        "  'vav' harfi düşer:",
        "  Vecede -> Yecidu (Emir: Cid!)",
        "  Vasale -> Yasilu (Emir: Sil!)"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Ecvef Fiil Çekimi", [
        "• Orta harfi illetli: Kâle, Bâa",
        "• Mazi cemide orta harf düşer:",
        "  Kâle ... Kulne / Kulte / Kultü",
        "• Muzâri: Yekûlu / Yebîu / Yenâmu",
        "• Emirde illet harfi düşer:",
        "  Kâle -> Kul! / Bâa -> Bi'!"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Nâkıs Fiil Çekimi", [
        "• Son harfi illetli: Deâ, Hedâ",
        "• Mazi: Deâ - Deavâ - Deav",
        "• Muzâri: Yed'û / Yehdî / Yerda",
        "• Emir sigasında sondaki illet",
        "  harfi düşer (illet harfi hazfi):",
        "  Deâ -&gt; Ud'u! / Hedâ -&gt; İhdi!"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">1. ÜNİTE KELİME VE FİİL HAZİNESİ ÖZETİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Ünitede Geçen Önemli Mu'tel Fiiller", [
        "• Kâle - Yekûlu - Kul (Ecvef): Söyledi - Söyler - De!",
        "• Kâne - Yekûnu - Kün (Ecvef): Oldu - Olur - Ol!",
        "• Câe - Yecîu - Ci' (Ecvef + Mehmûz): Geldi - Gelir - Gel!",
        "• Şâe - Yeşâu (Ecvef + Mehmûz): Diledi - Diler",
        "• Deâ - Yed'û - Ud'u (Nâkıs): Dua etti / Çağırdı",
        "• Hedâ - Yehdî - İhdi (Nâkıs): Hidayet verdi / Yol gösterdi"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Tevhit ve Şirk Ünitesi Temel Terimleri", [
        "• et-Tevhîd (Birleme) x eş-Şirk (Ortak koşma)",
        "• el-İhlâs (Samimiyet) x er-Riyâ (Gösteriş)",
        "• el-Muvahhid / el-Mü'min x el-Müşrik / el-Kâfir",
        "• el-İbâde (Kulluk), ed-Duâ (Yakarış), et-Tevekkül",
        "• el-Esnâm / el-Evsân (Putlar)",
        "• el-Mağfire (Bağışlanma), ez-Zulmü'l-Azîm (Büyük zulüm)"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]
