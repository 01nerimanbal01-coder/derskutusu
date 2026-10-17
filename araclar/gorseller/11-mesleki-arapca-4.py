# -*- coding: utf-8 -*-
"""11. Sınıf Mesleki Arapça — 4. Hafta görsel modülü: İman Esasları ve Esmaülhüsna."""


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
        'text-anchor="middle">ERKÂNÜ\'L-ÎMÂN (İMAN ESASLARI KAVRAM HARİTASI)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "İman Esaslarının İlk Üç Rüknü", [
        "• el-Îmânu billâh: Allah'a iman (Tevhid)",
        "• el-Îmânu bi'l-Melâike: Meleklere iman",
        "• el-Îmânu bi'l-Kütübi's-Semâviyye: İlahi kitaplar",
        "• Âmentü billâhi ve melâiketihî ve kütübihî",
        "• Âmene - Yü'minu - Îmânun (bi harf-i cerri ile)",
        "• Tasdîk bi'l-kalb ve ikrâr bi'l-lisân"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "İman Esaslarının Diğer Üç Rüknü", [
        "• el-Îmânu bi'r-Rusül: Peygamberlere iman",
        "• el-Îmânu bi'l-Yevmi'l-Âhir: Ahiret gününe iman",
        "• el-Îmânu bi'l-Kadâi ve'l-Kader: Kaza ve kader",
        "• Ve rusülihî ve'l-yevmi'l-âhiri ve bi'l-kaderi",
        "• Hayrihî ve şerrihî minallâhi Teâlâ",
        "• Bakara Suresi 177 ve 285. ayetlerdeki esaslar"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">ESMÂÜ\'L-HÜSNÂ: HAŞR SURESİ 22-24. AYETLERDEKİ İSİMLER</text>'
    )
    ic += _kart(25, 50, 225, 175, "#d97706", "Rahmet ve Hükümranlık", [
        "• er-Rahmân: Dünyada tüm",
        "  varlıklara merhamet eden",
        "• er-Rahîm: Ahirette müminlere",
        "  özel merhamet gösteren",
        "• el-Melik: Mülkün gerçek sahibi",
        "• el-Kuddûs: Eksiklikten münezzeh"
    ])
    ic += _kart(268, 50, 225, 175, "#8b5cf6", "Güven, Kudret ve İzzet", [
        "• es-Selâm: Esenlik kaynağı",
        "• el-Mü'min: Güven veren",
        "• el-Müheymin: Gözetip koruyan",
        "• el-Azîz: Mutlak galip ve üstün",
        "• el-Cebbâr: İradesini yürüten",
        "• el-Mütekebbir: Büyüklükte eşsiz"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Yaratma ve Hikmet", [
        "• el-Hâlık: Yoktan var eden,",
        "  takdir ve tayin eden",
        "• el-Bâri': Uygun ve örneksiz",
        "  biçimde yaratan",
        "• el-Musavvir: Şekil ve suret veren",
        "• el-Hakîm: Her işi hikmetli olan"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">MELEKLER, İLAHİ KİTAPLAR VE PEYGAMBERLER</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "el-Melâike (Melekler)", [
        "• Nûrdan yaratılmış lâtif",
        "  ve itaatkâr varlıklardır",
        "• Cibrîl (vahiy), Mîkâîl (tabiat)",
        "• İsrâfîl (sûr), Melekü'l-Mevt",
        "• Kirâmen Kâtibîn (yazıcılar)",
        "• Müfred: Melek / Cemi: Melâike"
    ])
    ic += _kart(268, 50, 225, 175, "#14b8a6", "el-Kütübü's-Semâviyye", [
        "• es-Suhuf: Hz. İbrahim, Musa",
        "• et-Tevrât: Hz. Musa (a.s.)",
        "• ez-Zebûr: Hz. Davud (a.s.)",
        "• el-İncîl: Hz. İsa (a.s.)",
        "• el-Kur'ânü'l-Kerîm: Son kitap,",
        "  Hz. Muhammed (s.a.v.)"
    ])
    ic += _kart(510, 50, 225, 175, "#0ea5e9", "er-Rusül ve'l-Enbiyâ", [
        "• Müfred: Resûl / Cemi: Rusül",
        "• Müfred: Nebî / Cemi: Enbiyâ",
        "• Sıfatları: Sıdk (doğruluk),",
        "  Emânet (güvenilirlik), Teblîğ,",
        "  Fetânet (zeka), İsmet (günahsızlık)",
        "• Hâtemü'n-Nebiyyîn: Hz. Muhammed"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">EL-ÂHİRE (AHİRET) VE EL-KADÂ VE\'L-KADER TERİMLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "el-Yevmü'l-Âhir (Ahiret Kavramları)", [
        "• el-Ba's ba'de'l-mevt: Ölümden sonra diriliş",
        "• el-Haşr ve'l-Hisâb: Toplanma ve hesap verme",
        "• el-Mîzân ve's-Sırât: Amellerin tartılması",
        "• el-Cenne ve'n-Nâr: Cennet ve Cehennem yurdu",
        "• ed-Dâru'l-Âhira: Ebedi ahiret hayatı",
        "• Dünyadaki sorumluluk bilincini güçlendirir"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "el-Kadâ ve'l-Kader (Kaza ve Kader)", [
        "• el-Kader: Allah'ın ezeli ilmiyle ölçüyle takdir etmesi",
        "• el-Kadâ: Takdir edilen şeyin zamanı gelince yaratılması",
        "• el-İrâdetü'l-Cüz'iyye: İnsanın seçme özgürlüğü",
        "• el-Mes'ûliyye: İnsanın tercihlerinden sorumluluğu",
        "• et-Tevekkül: Tedbir aldıktan sonra Allah'a güvenmek",
        "• el-Îmânu bi'l-kaderi hayrihî ve şerrihî"
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