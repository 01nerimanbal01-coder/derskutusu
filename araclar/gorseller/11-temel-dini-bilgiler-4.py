# -*- coding: utf-8 -*-
"""11. Sınıf Temel Dini Bilgiler — 4. Hafta görsel modülü: İlkeli Yaşamak."""


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
        'text-anchor="middle">İLKELİ YAŞAMANIN TEMELİ: İSTİKAMET VE SIRÂT-I MÜSTAKÎM</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "İstikamet Kavramı (Hûd Suresi 112)", [
        "• İnanç, söz ve davranışta dosdoğru olmaktır",
        "• 'Emrolunduğun gibi dosdoğru ol!' ilahi emridir",
        "• Aşırılıklardan (ifrat ve tefrit) uzak durmaktır",
        "• 'Allah'a inandım de, sonra dosdoğru ol!' hadisidir",
        "• Şartlar değişse de hak ve adaletten sapmamaktır",
        "• Müminin hayat pusulası ve karakter bütünlüğüdür"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "İlkeli Hayatın İnsana Kazandırdıkları", [
        "• Özü ile sözü bir, tutarlı bir şahsiyet inşa eder",
        "• İç huzuru, özgüven ve vicdani rahatlık sağlar",
        "• Toplumda sarsılmaz bir güven ve saygınlık doğurur",
        "• Kararsızlık ve savrulmaları önleyerek hedef verir",
        "• Dünya hayatını anlamlı ve bereketli kılar",
        "• Ahirette ebedi kurtuluş ve rızaya ulaştırır"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">İSLAM AHLAKININ DÖRT TEMEL YAŞAM İLKESİ</text>'
    )
    ic += _kart(25, 50, 170, 175, "#d97706", "1. Sıdk (Doğruluk)", [
        "• Sözde, niyette ve",
        "  davranışta dürüstlük",
        "• Yalandan ve ikiyüzlü",
        "  tutumdan kaçınmak",
        "• Doğrularla beraber",
        "  olmak (Tevbe 119)"
    ])
    ic += _kart(210, 50, 170, 175, "#8b5cf6", "2. Emanet (Güven)", [
        "• Can, mal, sır ve",
        "  görev bilincini korumak",
        "• Emanetleri ehline",
        "  vermek (Nisâ 58)",
        "• El-Emîn peygamberi",
        "  örnek almak"
    ])
    ic += _kart(395, 50, 170, 175, "#ec4899", "3. Adalet (Hakkaniyet)", [
        "• Her hak sahibine",
        "  hakkını tam vermek",
        "• Akraba veya düşman",
        "  ayrımı yapmamak",
        "• Zulümden ve haksız",
        "  kazançtan sakınmak"
    ])
    ic += _kart(580, 50, 155, 175, "#14b8a6", "4. İffet &amp; Merhamet", [
        "• Haramdan ve çirkin",
        "  işlerden korunmak",
        "• Yaratılanlara şefkat",
        "  ve nezaketle yaklaşmak",
        "• Onurlu ve vakur",
        "  bir duruş sergilemek"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">İLKELİ YAŞAMI TEHDİT EDEN DAVRANIŞLARDAN SAKINMAK</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Nifak ve Riyakârlık", [
        "• İçi dışı bir olmamak ve",
        "  gösteriş için iş yapmak",
        "• İhlas (samimiyet) ilkesini",
        "  zedeleyen en büyük engeldir",
        "• Mümin, insanların övgüsünü",
        "  değil Allah'ın rızasını arar"
    ])
    ic += _kart(268, 50, 225, 175, "#0ea5e9", "Çıkarcılık (Makyavelizm)", [
        "• 'Amaca ulaşmak için her yol",
        "  mübahtır' anlayışı yanlıştır",
        "• İslam'da gayenin meşru olması",
        "  kadar aracın da meşru ve",
        "  ahlaki olması şarttır",
        "• Menfaat ilkenin önüne geçemez"
    ])
    ic += _kart(510, 50, 225, 175, "#10b981", "Gaflet ve Özensizlik", [
        "• Zamanı, sağlığı ve gençliği",
        "  amaçsızca tüketmektir",
        "• 'İki günü eşit olan ziyandadır'",
        "  bilinciyle hareket edilmelidir",
        "• Öz denetim (muhasebe) ile",
        "  ilkeler sürekli korunur"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">HAYATIN HER ALANINDA İLKELİ DURUŞ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Bireysel ve Ailevi Hayatta İlkeler", [
        "• İbadetlerde devamlılık ve samimiyet (ihlas)",
        "• Anne-babaya ihsan, eş ve çocuklara merhamet",
        "• Helal lokma ve kanaatkâr tüketim ahlakı",
        "• Söz verdiğinde sözünde durmak (Ahde vefa)",
        "• Dijital mecralarda mahremiyet ve edebi korumak",
        "• Kimsenin görmediği yerde de Allah'tan sakınmak (Takva)"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "Toplumsal ve Mesleki Hayatta İlkeler", [
        "• İşini en güzel ve sağlam biçimde yapmak (İtkan)",
        "• Ticarette ölçü ve tartıyı adaletle tam tutmak",
        "• Kul ve kamu hakkına titizlikle riayet etmek",
        "• Komşuluk, akrabalık ve misafirlik hukukunu gözetmek",
        "• İyiliği emredip kötülükten sakındırmak (Emr-i bi'l-ma'rûf)",
        "• Çevreyi ve tüm canlıları ilahi emanet bilmek"
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