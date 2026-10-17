# -*- coding: utf-8 -*-
"""12. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük — 4. Hafta görsel modülü: Mondros Ateşkes Antlaşması ve İşgaller."""


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
        'text-anchor="middle">WİLSON İLKELERİ (8 OCAK 1918) VE OSMANLI\'YA ETKİSİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Wilson İlkelerinin Temel Maddeleri", [
        "• Yenen devletler yenilenlerden toprak ve savaş",
        "  tazminatı almayacaktır (Manda ve onarım adı",
        "  altında İtilaf Devletlerince delinmiştir)",
        "• Gizli antlaşmalar yapılmayacaktır",
        "• Uluslararası barış için Cemiyet-i Akvam kurulacaktır",
        "• Boğazlar tüm devletlerin ticaret gemilerine açık olacaktır"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "12. Madde (Self-Determinasyon İlkesi)", [
        "• Osmanlı Devleti'nde Türklerin çoğunlukta olduğu",
        "  bölgelerde kesin Türk egemenliği tanınacaktır",
        "• Türk olmayan azınlıklara ise çoğunlukta oldukları",
        "  yerlerde kendilerini yönetme hakkı verilecektir",
        "• Osmanlı bu ilkeye güvenerek ateşkes imzalamış;",
        "  ancak azınlıklar bunu bahane ederek ayaklanmıştır"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">MONDROS ATEŞKES ANTLAŞMASI (30 EKİM 1918)</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "7. ve 24. Maddeler (İşgallerin Hukuki Kılıfı)", [
        "• 7. Madde: İtilaf Devletleri, güvenliklerini tehdit",
        "  eden bir durum ortaya çıkarsa herhangi bir",
        "  stratejik noktayı işgal edebilecektir",
        "• 24. Madde: Vilâyât-ı Sitte'de (Altı Doğu İli:",
        "  Erzurum, Van, Harput/Elazığ, Diyarbakır, Sivas,",
        "  Bitlis) karışıklık çıkarsa işgal edilebilecektir"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Askeri, İletişim ve Ekonomik Hükümler", [
        "• Osmanlı ordusu derhal terhis edilecek, silah ve",
        "  cephanelerine el konulacaktır (Savunmasız bırakma)",
        "• Telsiz, telgraf ve Toros tünelleri denetime alınacaktır",
        "  (İşgallere karşı halkın haberleşmesini engelleme)",
        "• Boğazlar açılacak, yer altı kaynakları denetlenecektir",
        "• Osmanlı Devleti fiilen sona ermiştir"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">MONDROS SONRASI İŞGALLER VE PARİS BARIŞ KONFERANSI</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "İlk İşgaller", [
        "• İlk işgal edilen Osmanlı",
        "  toprağı: MUSUL (3 Kasım 1918,",
        "  İngiltere tarafından)",
        "• Anadolu'da ilk direniş:",
        "  Hatay / Dörtyol (19 Aralık 1918,",
        "  Kara Mehmet Çavuş - Fransızlara)"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Paris Barış Konferansı", [
        "• 18 Ocak 1919'da toplandı",
        "• Gizli antlaşmalarda İtalya'ya",
        "  vaat edilen İZMİR ve çevresi,",
        "  İngiltere'nin desteğiyle",
        "  Yunanistan'a verildi",
        "• İtilaf Devletlerinde ilk görüş ayrılığı!"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "İzmir'in İşgali (15 Mayıs 1919)", [
        "• Yunan ordusu İzmir'i işgal etti",
        "• Gazeteci Hasan Tahsin (Osman",
        "  Nevres) ilk kurşunu sıkarak",
        "  şehit düştü",
        "• Kuva-yı Milliye ruhu doğdu,",
        "  milli bilinç şahlandı"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">CEMİYETLER (ZARARLI VE MİLLÎ CEMİYETLER) VE KUVA-YI MİLLİYE</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Millî (Yararlı) Cemiyetler", [
        "• Trakya-Paşaeli Müdafaa-i Hukuk Cemiyeti",
        "• İzmir Müdafaa-i Hukuk ve Redd-i İlhak Cemiyeti",
        "• Şark Vilayetleri (Doğu Anadolu) Müdafaa-i Hukuk",
        "• Trabzon Muhafaza-i Hukuk-ı Milliye Cemiyeti",
        "• Kilikyalılar Cemiyeti (Çukurova/Adana savunması)",
        "• Milli Kongre Cemiyeti (Basın-yayın yoluyla mücadele)"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Zararlı Cemiyetler (Azınlık ve Milli Varlığa Düşman)", [
        "• Rum Azınlık: Mavri Mira, Etnik-i Eterya, Pontus Rum",
        "• Ermeni Azınlık: Hınçak ve Taşnak Cemiyetleri",
        "• Yahudi Azınlık: Alyans İsrailit ve Makabi Cemiyetleri",
        "• Milli Varlığa Düşman: İngiliz Muhipleri, Wilson",
        "  Prensipleri, İslam Teali, Kürt Teali, Sulh ve Selamet",
        "• Sivas Kongresi'nde yararlı cemiyetler birleştirilmiştir"
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
