# -*- coding: utf-8 -*-
"""12. Sınıf Peygamberimizin Hayatı — 4. Hafta görsel modülü: İbadetlerde ve Günlük Hayatta Sünnete Uygunluk, Bid'at ve Sa'd b. Ebî Vakkâs."""


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
        'text-anchor="middle">İBADETLERDE SÜNNETE UYMA VE İTİDAL (DENGE) İLKESİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "İbadetlerin Keyfiyetini Belirleyen Sünnet", [
        "• 'Beni nasıl namaz kılıyor görüyorsanız öyle kılın!'",
        "• 'Haccınızın kurallarını benden öğrenin!'",
        "• Kur'an'da mücmel (özet) bırakılan ibadetleri",
        "  Sünnet-i Seniyye ayrıntılarıyla açıklamıştır",
        "• İbadetlerde kişisel hevâ ile şekil değiştirilemez",
        "• İhlas ve sünnete uygunluk kabul şartıdır"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Sünnette İtidal (Aşırılıktan Kaçınma)", [
        "• Üç sahabinin 'hiç uyumadan namaz kılma, her gün",
        "  oruç tutma ve hiç evlenmeme' kararını Hz. Peygamber",
        "  düzeltmiştir: 'Ben hem namaz kılar hem uyurum;",
        "  hem oruç tutar hem iftar ederim ve evlenirim!'",
        "• 'Kim benim sünnetimden yüz çevirirse benden değildir'",
        "• Dinde ruhbanlık ve nefsi helak etmek yoktur"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">SÜNNETİN ZIDDI OLARAK BİD\'AT VE HURAFE KAVRAMLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Bid'at Nedir ve Neleri Kapsar?", [
        "• Hz. Peygamber ve sahabe döneminde olmayan, sonradan",
        "  'dinin ve ibadetin bir parçasıymış gibi' uydurulan",
        "  inanç ve uygulamalara BİD'AT denir",
        "• 'Kim bizim bu işimizde (dinimizde) olmayan bir şey",
        "  ihdas ederse o reddedilmiştir' (Buhârî, Sulh, 5)",
        "• İbadetlere ekleme veya çıkarma yapmak bid'attir"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Teknolojik Yenilikler Bid'at Değildir!", [
        "• Uçakla hacca gitmek, mikrofonla ezan okumak,",
        "  matbaada Mushaf basmak veya dijital uygulamalar",
        "  dini bir hüküm uydurmak değil 'vesile ve araçtır'",
        "• Bunlar bid'at kapsamına girmez, meşru kolaylıktır",
        "• Türbelere çaput bağlamak, kurşun döktürmek ve",
        "  falcılık ise İslam'ın reddettiği 'hurafe'dir"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">SAHABEDEN ÖRNEK ŞAHSİYET: SA\'D B. EBÎ VAKKÂS (R.A.)</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "İlk Müslümanlardan Oluşu", [
        "• 17 yaşında ilk Müslüman",
        "  olan öncü sahabilerdendir",
        "• Annesi Hamne'nin açlık",
        "  grevine rağmen imanından",
        "  taviz vermemiştir (Lokman 15)",
        "• Aşere-i Mübeşşere'dendir"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Okçuluğu ve Duası", [
        "• İslam'da Allah yolunda ilk",
        "  ok atan sahabidir",
        "• Uhud'da Hz. Peygamber ona",
        "  'Anam babam sana feda olsun",
        "  ey Sa'd, at!' buyurmuştur",
        "• Duası makbul sahabidir"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Vasiyet ve Sünnet Bilinci", [
        "• Kadisiye Savaşı komutanı",
        "  ve İran fatihidir",
        "• Hastalığında malının tümünü",
        "  bağışlamak isteyince Resûlullah",
        "  'Üçte bir (1/3) yeterlidir'",
        "  sünnetini vazetmiştir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">GÜNLÜK HAYATTA SÜNNET-İ SENİYYE BİLİNCİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Ahlaki ve Toplumsal Sünnetler", [
        "• Hayırlı işlere 'Bismillah' ile ve sağdan başlamak",
        "• Karşılaşılan mümine tebessüm edip selam vermek",
        "• Anne-babaya, komşuya ve misafire ikramda bulunmak",
        "• Hasta ziyareti yapmak ve cenazeye katılmak",
        "• Yeme-içmede israftan kaçınmak ve şükretmek",
        "• Sözünde durmak ve emaneti korumak"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Sünnete Bağlılığın Kazandırdıkları", [
        "• Sıradan günlük davranışları ibadet sevabına dönüştürür",
        "• Mümini bid'at, hurafe ve aşırılıklardan korur",
        "• Allah'ın sevgisini ve mağfiretini kazandırır (Âl-i İmrân 31)",
        "• İslam ümmetinde ibadet ve kültür birliği sağlar",
        "• Bireye dengeli (itidalli) ve huzurlu bir hayat sunar",
        "• Hz. Peygamber'in şefaatine nail olmaya vesile olur"
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
