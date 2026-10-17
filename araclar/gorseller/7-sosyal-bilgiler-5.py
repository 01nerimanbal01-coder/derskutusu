# -*- coding: utf-8 -*-
"""7. Sınıf Sosyal Bilgiler — 5. Hafta Görselleri (Millî Meseleler Karşısında Türk Toplumunun Tutum ve Davranışları)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Millî Mesele Nedir? Toplumu Birleştiren Ortak Değerler</text>',
        _kart(25, 50, 225, 215, "1. Bağımsızlık ve Egemenlik", [
            "• Vatan topraklarının bütünlüğü",
            "• Bayrak, İstiklâl Marşı ve devletin",
            "  bağımsızlığına yönelik tehditler",
            "• Millî iradeye ve demokrasiye",
            "  sahip çıkma bilinci",
            "• 'Ya istiklal ya ölüm!' kararlılığı"
        ], "#e11d48", "#fff1f2"),
        _kart(267, 50, 225, 215, "2. Toplumsal Dayanışma ve Afetler", [
            "• Deprem, sel, yangın gibi büyük",
            "  doğal afetlerde tek yürek olma",
            "• Kızılay, AFAD ve sivil toplum",
            "  kuruluşlarıyla yardım seferberliği",
            "• 'Birlikten kuvvet doğar' anlayışıyla",
            "  yaraları birlikte sarma"
        ], "#0284c7", "#f0f9ff"),
        _kart(510, 50, 225, 215, "3. Kültürel ve Bilimsel Atılımlar", [
            "• Türk dilinin, tarihinin ve kültürel",
            "  mirasının korunup yaşatılması",
            "• Millî Teknoloji Hamlesi ve yerli",
            "  üretimle ekonomik bağımsızlık",
            "• Uluslararası spor ve bilim",
            "  başarılarında ortak gurur"
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Tarihten Günümüze Millî Birlik ve Fedakârlık Örnekleri</text>',
        _kart(30, 50, 335, 215, "Millî Mücadele ve Tekâlif-i Milliye", [
            "• Çanakkale ve Kurtuluş Savaşı'nda kadın, erkek,",
            "  genç, yaşlı tüm milletin cepheye koşması.",
            "• Tekâlif-i Milliye Emirleri (1921) ile halkın",
            "  elindeki erzak, giysi ve ulaşım araçlarını",
            "  gönüllü olarak ordusuyla paylaşması.",
            "• Şerife Bacı, Halime Çavuş, Sütçü İmam ruhu."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Cumhuriyet Dönemi ve Yakın Tarih", [
            "• Hatay'ın Anavatana katılması (1939) ve",
            "  Kıbrıs Barış Harekâtı'nda (1974) millî kenetlenme.",
            "• 15 Temmuz Demokrasi ve Millî Birlik Günü'nde",
            "  milletin egemenliğine sahip çıkması.",
            "• 6 Şubat 2023 Kahramanmaraş depremlerinde",
            "  85 milyonun sergilediği asrın dayanışması."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Türk Toplumunun Millî Meselelerdeki Karakteristik Tutumları</text>',
        _kart(30, 50, 335, 215, "Vatanseverlik ve Özveri (Fedakârlık)", [
            "• Kişisel çıkarları bir kenara bırakıp milletin",
            "  ve vatanın ortak menfaatini üstün tutma.",
            "• Zor zamanlarda ayrılıkları unutup ortak",
            "  hedefte kenetlenme (Millî birlik ve beraberlik).",
            "• Şehitlik ve gazilik kavramlarına duyulan",
            "  derin saygı ve minnet duygusu."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Yardımlaşma Kültürü (İmece ve Vakıf)", [
            "• Kökleri Orta Asya ve İslam medeniyetine",
            "  uzanan İmece, Ahilik ve Vakıf kültürü.",
            "• Komşusu açken tok yatmayan merhamet anlayışı.",
            "• Mazlum ve mağdur milletlere de yardım",
            "  eli uzatan insani diplomasi geleneği.",
            "• Gönüllülük ve sosyal sorumluluk bilinci."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Etkin Bir Vatandaş Olarak Millî Meselelere Katkımız</text>',
        _kart(30, 50, 335, 195, "Bilinçli ve Sorumlu Vatandaşlık", [
            "• Tarihimizi ve millî değerlerimizi doğru kaynaklardan",
            "  öğrenmek ve dezenformasyona karşı uyanık olmak.",
            "• Doğal kaynakları koruyup tasarruflu kullanmak.",
            "• Vergi, seçim, kanunlara uyma gibi vatandaşlık",
            "  görevlerini özenle yerine getirmek."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "İşini En İyi Yapmak: Gerçek Vatanseverlik", [
            "• Atatürk'ün sözü: 'Vatanını en çok seven,",
            "  görevini en iyi yapandır!'",
            "• Öğrenci olarak derslerimize çalışmak, bilim,",
            "  sanat ve sporda ülkemizi en iyi şekilde",
            "  temsil etmek en büyük millî katkıdır."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
