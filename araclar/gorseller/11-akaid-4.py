# -*- coding: utf-8 -*-
"""11. Sınıf Akaid — 4. Hafta görsel modülü: İman ve İmanın Mahiyeti."""


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
        'text-anchor="middle">İMANIN MAHİYETİ: KALP İLE TASDİK VE DİL İLE İKRAR</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Kalp ile Tasdik (Asli Rükün)", [
        "• İmanın özü ve değişmez temel şartıdır",
        "• Hz. Peygamber'in tebliğ ettiği hakikatleri",
        "  kalpten kesin olarak onaylamaktır",
        "• Şüphe barındırmayan yakînî kabuldür",
        "• Allah katında mümin olmanın ölçüsüdür",
        "• Mâtürîdî ve Eş'arî'nin ortak görüşüdür"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Dil ile İkrar (Dünyevi Şart)", [
        "• Kalpteki imanı dil ile ifade etmektir",
        "• Kelime-i Tevhid ve Şehadet getirmektir",
        "• İslam toplumunda mümin tanınmayı sağlar",
        "• Nikâh, miras ve cenaze hükümleri uygulanır",
        "• İkrah (zorlama) altında terk edilebilir",
        "• Kalpte tasdik yoksa tek başına yetmez"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">TAKLİDÎ İMAN İLE TAHKİKÎ İMAN KARŞILAŞTIRMASI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Taklidî İman (Çevresel Kabul)", [
        "• Delillere dayanmadan çevreyi taklit etmektir",
        "• Anne-baba ve toplumdan görerek inanmaktır",
        "• Ehli Sünnet'e göre geçerli (sahih) sayılır",
        "• Ancak şüphe ve inkâr karşısında zayıftır",
        "• Akıl yürütme terk edildiği için sorumluluk doğurur",
        "• Tahkikî imana yükseltilmesi tavsiye edilir"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Tahkikî İman (Delilli İman)", [
        "• Akli ve nakli delillerle araştırarak inanmaktır",
        "• Evrendeki düzen ve ayetler üzerinde tefekkürdür",
        "• Şüphe ve itirazlar karşısında sarsılmaz",
        "• İmanı bilgi, bilinç ve hikmetle bütünleştirir",
        "• Salih amellere ve güzel ahlaka yönlendirir",
        "• Kur'an'ın müminlerden istediği ideal imandır"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">İMAN - İSLAM VE İMAN - AMEL İLİŞKİSİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "İman ve İslam", [
        "• İman kalbin içsel tasdiki,",
        "  İslam dışsal teslimiyettir",
        "• Mâtürîdî'ye göre dinî açıdan",
        "  iman ve İslam bir bütündür",
        "• Her mümin aynı zamanda",
        "  müslümandır"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "İman ve Amel", [
        "• Amel imanın cüzü (parçası)",
        "  değil, kemal şartıdır",
        "• İbadetler imanı korur, besler",
        "  ve kalpte kökleştirir",
        "• Amelsiz iman zayıflar;",
        "  imansız amel ahirette geçmez"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Büyük Günah (Kebîre)", [
        "• İnkar etmedikçe büyük günah",
        "  işleyen dinden çıkmaz",
        "• Günahkâr mümine 'fâsık'",
        "  (asi mümin) adı verilir",
        "• Tövbe kapısı açıktır; karar",
        "  Allah'ın rahmet ve adaletindedir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">İCMÂLÎ VE TAFSÎLÎ İMAN BASAMAKLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "İcmâlî İman (Öz ve Bütüncül)", [
        "• İman esaslarına toptan ve özetle inanmaktır",
        "• Kelime-i Tevhid ve Kelime-i Şehadet'tir",
        "• Allah'ı ve Hz. Muhammed'in peygamberliğini",
        "  kabul etmekle gerçekleşir",
        "• İslam'a girişin ilk ve temel adımıdır",
        "• Ayrıntıları öğrenme iradesini içinde taşır"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Tafsîlî İman (Ayrıntılı Kabul)", [
        "• İman esaslarını tek tek bilip onaylamaktır",
        "• Âmentü'de yer alan 6 iman esasını kapsar",
        "• Allah, melekler, kitaplar, peygamberler,",
        "  ahiret günü ve kadere ayrı ayrı inanmaktır",
        "• Zarûrât-ı dîniyye (kesin hükümler) dahildir",
        "• Müminin dinî bilgisini kemale erdirir"
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