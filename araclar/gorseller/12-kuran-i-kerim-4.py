# -*- coding: utf-8 -*-
"""12. Sınıf Kur'an-ı Kerim — 4. Hafta görsel modülü: Meal ve Tefsirlerden Yararlanma İlkeleri, Kehf 32-59 ve Mülk 11-20."""


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
        'text-anchor="middle">TERCÜME, MEAL VE TEFSİR KAVRAMLARININ FARKI</text>'
    )
    ic += _kart(25, 50, 225, 175, "#0284c7", "Tercüme (Çeviri)", [
        "• Bir metnin başka bir dile",
        "  birebir ve tam karşılıkla",
        "  aktarılmasıdır",
        "• Kur'an'ın eşsiz belagati ve",
        "  çok katmanlı anlamı birebir",
        "  tercümeye sığmaz"
    ])
    ic += _kart(268, 50, 225, 175, "#10b981", "Meal (Yaklaşık Anlam)", [
        "• Ayetlerin başka bir dile",
        "  yaklaşık ve özet anlamıyla",
        "  aktarılmasıdır",
        "• Mütercimin tercihi olan",
        "  tek bir anlamı yansıtır",
        "• Kur'an'ın bizzat kendisi değildir"
    ])
    ic += _kart(510, 50, 225, 175, "#8b5cf6", "Tefsir (Geniş Açıklama)", [
        "• Ayetlerin iniş sebepleri,",
        "  dil özellikleri, Hz. Peygamber'in",
        "  sünneti ve tarihsel bağlamıyla",
        "  genişçe açıklanmasıdır",
        "• Derin ve bütüncül anlam",
        "  için tefsire başvurulur"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">MEAL VE TEFSİRLERDEN YARARLANMA İLKELERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "1. Bağlam ve Bütünlük İlkesi", [
        "• Ayetleri öncesi ve sonrasıyla (siyak-sibak)",
        "  ve konu bütünlüğü içinde okumak",
        "• Aynı konudaki diğer ayetleri ve sahih hadisleri",
        "  (Sünnet-i Seniyye'yi) birlikte değerlendirmek",
        "• Ayetlerin iniş sebeplerini (Esbâb-ı Nüzûl) ve",
        "  Mekkî-Medenî özelliklerini dikkate almak"
    ])
    ic += _kart(395, 50, 340, 175, "#059669", "2. Ehil Kaynak ve Okuma Bilinci", [
        "• Alanında uzman âlimlerin ve güvenilir kurumların",
        "  (Diyanet İşleri Başkanlığı, Elmalılı Hamdi Yazır,",
        "  Kur'an Yolu vb.) meal ve tefsirlerini seçmek",
        "• Tek bir mealle yetinmeyip açıklamalı meallere",
        "  ve tefsirlere başvurmak",
        "• Ayetlerden kendi hayatımız için öğüt çıkarmak"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">KEHF SURESİ 32-59. AYETLER: İKİ BAHÇE SAHİBİ KISSASI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#6366f1", "Şımaran Bahçe Sahibi ve Mümin Arkadaşı", [
        "• Kehf 32-44: Kendisine üzüm bağları ve hurmalıklar",
        "  verilen adam, servetiyle kibirlenip ahireti inkâr etti",
        "• Mümin arkadaşı onu uyardı: 'Bağına girdiğinde",
        "  Mâşâallah, lâ kuvvete illâ billâh (Allah ne güzel",
        "  dilemiş, güç yalnız Allah'ındır) deseydin ya!'",
        "• Bahçesi afetle helak olunca pişman oldu"
    ])
    ic += _kart(395, 50, 340, 175, "#ec4899", "Dünya Hayatının Geçiciliği ve Bâkî Salih Ameller", [
        "• Kehf 45: Dünya hayatı gökten indirdiğimiz suyla",
        "  yeşerip sonra kuruyup savrulan bitkiye benzer",
        "• Kehf 46: Mal ve oğullar dünya hayatının süsüdür;",
        "  kalıcı olan salih ameller (el-Bâkıyâtü's-Sâlihât)",
        "  ise Rabbin katında sevap ve ümitçe daha hayırlıdır",
        "• Kehf 49: Amel defteri küçük-büyük her şeyi saymıştır"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">MÜLK SURESİ 11-20. AYETLERİN ANA MESAJLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#14b8a6", "Gaybda Rablerinden Haşyet Duyanlar (11-15)", [
        "• Görmedikleri halde Rablerinden derin saygıyla",
        "  korkanlar için bağışlanma ve büyük mükâfat vardır",
        "• Allah gizlenen sözleri de kalplerin özünü de bilir",
        "• 'Yaratan bilmez mi? O Latîf'tir, Habîr'dir' (Ayet 14)",
        "• Yeryüzünü size boyun eğdiren (zelûl kılan) O'dur;",
        "  üzerinde yürüyün ve O'nun rızkından yiyin (Ayet 15)"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "İlahi Kudret ve Uçan Kuşlar İbreti (16-20)", [
        "• Yerin sizi yutmayacağından veya gökten taş",
        "  fırtınası gelmeyeceğinden emin misiniz? (Ayet 16-17)",
        "• Üstlerinde kanatlarını açıp kapayarak uçan",
        "  kuşları görmüyorlar mı? Onları havada Rahmân'dan",
        "  başkası tutmuyor (Ayet 19)",
        "• Rahmân'dan başka size yardım edecek kimdir? (Ayet 20)"
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
