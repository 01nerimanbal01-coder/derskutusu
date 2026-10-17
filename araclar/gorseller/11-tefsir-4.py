# -*- coding: utf-8 -*-
"""11. Sınıf Tefsir — 4. Hafta görsel modülü: Kur'an İlimleri (Ulûmü'l-Kur'ân)."""


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
        'text-anchor="middle">MEKKÎ VE MEDENÎ ÂYETLERİN TEMEL ÖZELLİKLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Mekkî Vahiy (Hicret Öncesi)", [
        "• Hicretten önce inen sure ve ayetlerdir",
        "• Tevhid, nübüvvet ve ahiret inancı merkezdedir",
        "• Şirkle mücadele ve ahlaki ilkeler vurgulanır",
        "• Ayetler genellikle kısa, veciz ve etkileyicidir",
        "• 'Ey insanlar!' hitabı ve yeminler sıkça geçer",
        "• Geçmiş peygamber kıssalarıyla teselli verilir"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Medenî Vahiy (Hicret Sonrası)", [
        "• Hicretten sonra inen sure ve ayetlerdir",
        "• İbadet, hukuk, aile ve toplum düzeni anlatılır",
        "• Ehl-i Kitap ile diyalog ve münafıklar ele alınır",
        "• Ayetler daha uzun ve açıklayıcı üsluptadır",
        "• 'Ey iman edenler!' hitabı yoğun olarak görülür",
        "• İslam toplumunun kurumsal inşasını tamamlar"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">MUHKEM - MÜTEŞÂBİH VE NÂSİH - MENSÛH KAVRAMLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Muhkem ve Müteşâbih (Âl-i İmrân 7)", [
        "• Muhkem: Anlamı açık, net ve yoruma kapalı",
        "  ayetlerdir; Kitab'ın anası (Ümmü'l-Kitâb) sayılır",
        "• İnanç, ibadet ve ahlakın temel hükümleridir",
        "• Müteşâbih: Birden fazla manaya ihtimali olan,",
        "  temsil ve mecaz içeren derin ayetlerdir",
        "• Müteşâbihler muhkemlerin ışığında anlaşılır"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Nâsih ve Mensûh (Tedricîlik İlkesi)", [
        "• Nesih: Bir şer'î hükmün daha sonra inen",
        "  başka bir delille yürürlükten kaldırılmasıdır",
        "• Mensûh: Hükmü kaldırılan önceki ayet/hüküm",
        "• Nâsih: Yeni hükmü getiren sonraki ayettir",
        "• İnanç ve ahlak ilkelerinde nesih olmaz",
        "• Toplumu aşamalı olarak eğitmeyi (tedric) sağlar"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">KUR\'AN\'IN DİL VE ANLATIM İLİMLERİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Garîbü'l-Kur'ân", [
        "• Kur'an'da az kullanılan veya",
        "  farklı lehçelerden gelen",
        "  kelimeleri açıklayan ilimdir",
        "• Cahiliye şiiri ve sahabe",
        "  rivayetlerinden yararlanır",
        "• Râgıb el-İsfahânî'nin",
        "  el-Müfredât'ı temel eserdir"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Vücûh ve Nezâir", [
        "• Vücûh: Aynı kelimenin farklı",
        "  ayetlerde farklı anlamlara",
        "  gelmesidir (Örn: Hüdâ, Ümmet)",
        "• Nezâir: Farklı kelimelerin",
        "  aynı anlamı karşılamasıdır",
        "• Bağlamsal tefsirin anahtarıdır"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Emsâlü'l-Kur'ân", [
        "• Soyut hakikatleri somut",
        "  benzetme ve temsillerle",
        "  anlatan Kur'an ilmidir",
        "• Tevhid, riyakârlık ve dünya",
        "  hayatını canlı tablolarla",
        "  zihinlerde kalıcı kılar"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">İ\'CÂZÜ\'L-KUR\'ÂN VE KUR\'AN İLİMLERİNİN BÜTÜNLÜĞÜ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "İ'câzü'l-Kur'ân (Eşsizlik)", [
        "• Kur'an'ın lafız, üslup ve mana bakımından",
        "  benzerinin getirilemez oluşunu inceler",
        "• Edebi belagat ve fesahat zirvesidir",
        "• Gaybî haberler ve çelişkisiz bütünlük içerir",
        "• Evrensel hukuk ve ahlak ilkeleri sunar",
        "• Hz. Muhammed'in en büyük mucizesidir"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Kur'an İlimlerinin İşbirliği", [
        "• Esbâb-ı Nüzûl ve Mekkî-Medenî tarihsel",
        "  bağlamı ve nüzul ortamını aydınlatır",
        "• Garîbü'l-Kur'ân ve Vücûh dilsel yapıyı çözer",
        "• Muhkem-Müteşâbih ve Nâsih-Mensûh fıkhî ve",
        "  itikadî hükümlerin doğru çıkarılmasını sağlar",
        "• Hepsi birlikte sahih tefsire ulaştırır"
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
