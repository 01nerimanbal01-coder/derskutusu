# -*- coding: utf-8 -*-
"""12. Sınıf Türk Dili ve Edebiyatı — 4. Hafta görsel modülü: 1960 Sonrası Türk Hikâyesi ve Küçürek Hikâye."""


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
        'text-anchor="middle">1960 SONRASI TÜRK HİKÂYESİNDE TEMEL EĞİLİMLER</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Toplumcu &amp; Millî-Dinî Eğilimler", [
        "• Toplumcu Gerçekçiler: Köyden kente göç,",
        "  gecekondulaşma, işçi sorunları, Almanya göçü",
        "  Temsilciler: Fakir Baykurt, Bekir Yıldız,",
        "  Füruzan, Adalet Ağaoğlu, Muzaffer İzgü",
        "• Millî ve Dinî Duyarlılık: Doğu-Batı çatışması,",
        "  manevi değerler -> Mustafa Kutlu, Rasim Özdenören"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Bireyin İç Dünyası &amp; Modernist Eğilim", [
        "• Bireyin yalnızlığı, yabancılaşma, bunalım,",
        "  modern şehir hayatında sıkışmışlık işlenir",
        "• Varoluşçuluk (Egzistansiyalizm) etkisi görülür",
        "• Geleneksel olay örgüsü ve kronolojik zaman kırılır",
        "• Temsilciler: Oğuz Atay, Yusuf Atılgan, Ferit Edgü,",
        "  Bilge Karasu, Adalet Ağaoğlu, Nazlı Eray"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">MODERNİST VE POSTMODERNİST ANLATIM TEKNİKLERİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#d97706", "Bilinç Akışı &amp; İç Çözümleme", [
        "• Bilinç Akışı: Kahramanın",
        "  zihninden geçen düşünceler",
        "  mantıksal sıra olmadan,",
        "  çağrışımlarla aktarılır",
        "• İç Monolog: Karakterin",
        "  kendi kendisiyle konuşmasıdır"
    ])
    ic += _kart(268, 50, 225, 175, "#8b5cf6", "Metinlerarasılık &amp; Pastiş", [
        "• Metinlerarasılık: Önceki",
        "  edebi metinlere, masallara",
        "  veya mitlere gönderme yapma",
        "• Pastiş: Başka bir yazarın",
        "  üslup ve dilini taklit etme",
        "• Parodi: Ciddi metni tiye alma"
    ])
    ic += _kart(510, 50, 225, 175, "#ec4899", "Üstkurmaca &amp; Leitmotiv", [
        "• Üstkurmaca: Yazarın eserin",
        "  yazılış sürecini hikâyenin",
        "  konusu haline getirmesi",
        "• Leitmotiv: Bir söz veya",
        "  imgenin metin boyunca",
        "  tekrarlanarak simgeleşmesi"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">KÜÇÜREK (MİNİMAL) HİKÂYE VE ÖZELLİKLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#6366f1", "Küçürek Hikâyenin Yapısal Özellikleri", [
        "• Çok kısa, yoğun ve damıtılmış anlatılardır",
        "• Genellikle birkaç cümle veya bir paragraftır",
        "• Uzun betimlemeler ve kişi tanıtımları yapılmaz",
        "• Şiirsel, imgesel ve sembolik bir dil kullanılır",
        "• Söylenmeyeni tamamlama görevi okura bırakılır",
        "• Çarpıcı ve beklenmedik bir sonla biter"
    ])
    ic += _kart(395, 50, 340, 175, "#14b8a6", "Dünya ve Türk Edebiyatında Temsilcileri", [
        "• Dünya Edebiyatı: Franz Kafka, Julio Cortazar,",
        "  Jorge Luis Borges, Oscar Wilde, Max Jacob",
        "• Türk Edebiyatı Öncüsü: Ferit Edgü (Doğu Öyküleri,",
        "  İşte Deniz, Maria), Necati Tosuner",
        "• Diğer Temsilciler: Hulki Aktunç, Haydar Ergülen,",
        "  Rasim Özdenören, Vüs'at O. Bener, Murat Yalçın"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">1960 SONRASI ÖNE ÇIKAN YAZARLAR VE HİKÂYE KİTAPLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Modernist ve Bireysel Hikâyeciler", [
        "• Oğuz Atay: Korkuyu Beklerken",
        "• Yusuf Atılgan: Bodur Minareden Öte, Eylemci",
        "• Bilge Karasu: Troya'da Ölüm Vardı, Göçmüş Kediler Bahçesi",
        "• Ferit Edgü: Kaçkınlar, Bozgun, Bir Gemide, Çığlık",
        "• Adalet Ağaoğlu: Yüksek Gerilim, Sessizliğin İlk Sesi",
        "• Tomris Uyar: İpek ve Bakır, Yürekte Bukağı"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Millî-Dinî ve Toplumcu Hikâyeciler", [
        "• Mustafa Kutlu: Ortadaki Adam, Uzun Hikâye,",
        "  Ya Tahammül Ya Sefer, Yoksulluk İçimizde",
        "• Rasim Özdenören: Hastalar ve Işıklar, Çözülme,",
        "  Çok Sesli Bir Ölüm, Çarpılmışlar, Kuyu",
        "• Sevinç Çokum: Eğik Ağaçlar, Bölüşmek, Makina",
        "• Füruzan: Parasız Yatılı, Kuşatma, Benim Sinemalarım"
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