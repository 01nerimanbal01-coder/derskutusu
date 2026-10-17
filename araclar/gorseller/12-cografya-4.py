# -*- coding: utf-8 -*-
"""12. Sınıf Coğrafya — 4. Hafta görsel modülü: Ekonomik Faaliyetlerin Sosyal ve Kültürel Etkileri ile Bölgesel Kalkınma Projeleri."""


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
        'text-anchor="middle">EKONOMİK FAALİYETLERİN SOSYAL VE KÜLTÜREL ETKİLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Demografik ve Sosyal Dönüşüm", [
        "• Sanayi ve hizmet sektörünün geliştiği yerler göç alır",
        "• Geniş aileden çekirdek aile yapısına geçiş hızlanır",
        "• Kadının iş hayatına ve eğitime katılım oranı artar",
        "• Kentsel nüfus oranı ve okuryazarlık düzeyi yükselir",
        "• Çalışma saatleri ve sosyal güvenlik standartları gelişir",
        "• Tüketim alışkanlıkları ve yaşam tarzı çeşitlenir"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Kültürel Etkileşim ve Mekânsal Değişim", [
        "• Turizm ve ticaret kültürler arası etkileşimi artırır",
        "• Sinema, tiyatro, müze ve spor tesisleri yaygınlaşır",
        "• Batman (petrol), Karabük-Ereğli (demir-çelik), Soma (kömür)",
        "  gibi küçük yerleşmeler hızla büyüyerek şehre dönüşür",
        "• Planlı kentleşme olmazsa çarpık kentleşme, trafik,",
        "  gürültü ve çevre kirliliği gibi sorunlar ortaya çıkar"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">TÜRKİYE\'DE BÖLGESEL KALKINMA PROJELERİNİN HEDEFLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Temel Ekonomik Hedefler", [
        "• Bölgeler arasındaki gelişmişlik farklarını azaltmak",
        "• Her bölgenin doğal ve beşeri potansiyelini harekete geçirmek",
        "• Tarımda sulama, modernizasyon ve verimi artırmak",
        "• Tarıma dayalı sanayi, madencilik ve turizmi geliştirmek",
        "• Yeni istihdam alanları açarak işsizliği düşürmek",
        "• Kişi başına düşen milli geliri ve ihracatı yükseltmek"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Sosyal ve Demografik Hedefler", [
        "• Bölge dışına yapılan göçleri yerinde istihdamla önlemek",
        "• Eğitim, sağlık, ulaşım ve iletişim altyapısını güçlendirmek",
        "• Kırsal kesimde yaşam kalitesini ve refahı yükseltmek",
        "• Kadın ve genç girişimciliğini desteklemek",
        "• Doğal çevreyi ve su kaynaklarını sürdürülebilir korumak",
        "• Tarihi ve kültürel mirası turizme kazandırmak"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">UYGULAMADAKİ BÜYÜK PROJELER: GAP, KOP VE DAP</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "GAP (Güneydoğu Anadolu)", [
        "• 9 il (Gaziantep, Şanlıurfa,",
        "  Diyarbakır, Mardin, Adıyaman...)",
        "• Fırat ve Dicle üzerinde 22 baraj",
        "  ve 19 HES (Atatürk Barajı)",
        "• Pamuk, mısır ve tekstil sanayii",
        "  üretiminde Türkiye lideridir"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "KOP (Konya Ovası Projesi)", [
        "• 8 il (Konya, Karaman, Aksaray,",
        "  Niğde, Nevşehir, Kırıkkale,",
        "  Kırşehir, Yozgat)",
        "• Mavi Tünel ile Göksu sularını",
        "  Konya Ovası'na ulaştırır",
        "• Modern sulama ve obruk önleme"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "DAP (Doğu Anadolu Projesi)", [
        "• 15 il (Erzurum, Kars, Van,",
        "  Malatya, Elazığ, Sivas...)",
        "• Temel odak: Mera ıslahı,",
        "  büyükbaş-küçükbaş hayvancılık,",
        "  et-süt entegre tesisleri ve",
        "  kış turizmi potansiyelidir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">KARADENİZ HAVZASI PROJELERİ: DOKAP, YHGP VE ZBK</text>'
    )
    ic += _kart(25, 50, 225, 175, "#059669", "DOKAP (Doğu Karadeniz)", [
        "• 11 il (Trabzon, Rize, Artvin,",
        "  Ordu, Giresun, Samsun, Tokat,",
        "  Amasya, Çorum, Gümüşhane, Bayburt)",
        "• Yayla turizmi (Yeşil Yol),",
        "  çay ve fındık tarımı,",
        "  balıkçılık ve kıyı ulaşımı"
    ])
    ic += _kart(268, 50, 225, 175, "#0ea5e9", "YHGP (Yeşilırmak Havzası)", [
        "• 4 ortak il: Samsun, Amasya,",
        "  Çorum ve Tokat (DOKAP içinde)",
        "• Yeşilırmak ve kollarında taşkın,",
        "  erozyon ve su kirliliğini önlemek",
        "• Havza bazlı ekolojik tarım",
        "  ve şehircilik planlaması"
    ])
    ic += _kart(510, 50, 225, 175, "#0284c7", "ZBK (Zonguldak-Bartın-Karabük)", [
        "• 3 il: Zonguldak, Bartın, Karabük",
        "• Taş kömürü madenciliği ve",
        "  demir-çelik sanayisini",
        "  modernize etmek",
        "• Filyos Vadisi Projesi ve limanı",
        "  ile ekonomiyi çeşitlendirmek"
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