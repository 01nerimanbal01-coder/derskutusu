# -*- coding: utf-8 -*-
"""5. Sınıf Arapça — 5. Hafta Görselleri (1. Ünite: Merhaba - Diyaloglar, Cezm ve Şedde)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Tanışma, Hal-Hatır Sorma ve Vedalaşma Diyalog Zinciri</text>',
        _kart(25, 50, 225, 215, "1. Selam ve Tanışma", [
            "• es-Selâmü aleyküm (Allah'ın selamı)",
            "• ve Aleykümü's-selâm (Cevap)",
            "• Mâ ismüke? (Adın ne? - Erkek)",
            "• Mâ ismüki? (Adın ne? - Kız)",
            "• İsmî Ahmed / İsmî Zeyneb",
            "• Teşerraftü (Memnun oldum)"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Hal-Hatır ve Nezaket", [
            "• Keyfe hâlüke? (Nasılsın? - Erkek)",
            "• Keyfe hâlüki? (Nasılsın? - Kız)",
            "• Ene bi-hayr, el-hamdü lillâh",
            "• Min fadlike / Min fadliki (Lütfen)",
            "• Şükran (Teşekkür ederim)",
            "• Afven (Rica ederim / Bir şey değil)"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Vedalaşma İfadeleri", [
            "• İle'l-likâ' (Görüşmek üzere)",
            "• Mea's-selâme (Güle güle / Selametle)",
            "• Fî emânillâh (Allah'a emanet ol)",
            "• Leyle saîde (İyi geceler)",
            "• Nehâruke saîd (İyi günler)",
            "• İletişimi hayır duayla bitirme"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Sınıf İçi Yönergeler: Müzekker (Erkek) ve Müennes (Kız) Karşılaştırması</text>',
        _kart(30, 50, 335, 215, "Erkek Öğrenciye Yönergeler (Müzekker)", [
            "• İclis! (Otur!) — Kum! (Ayağa kalk!)",
            "• İkra'! (Oku!) — Üktüb! (Yaz!)",
            "• İstemi'! (Dinle!) — Ünzur! (Bak!)",
            "• İftah! (Aç!) — Ağlik! (Kapat!)",
            "• Teâl! (Gel!) — İzheb! (Git!)",
            "• Fiil sonunda ek uzatma harfi bulunmaz."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Kız Öğrenciye Yönergeler (Müennes -î)", [
            "• İclisî! (Otur!) — Kûmî! (Ayağa kalk!)",
            "• İkra'î! (Oku!) — Üktübî! (Yaz!)",
            "• İstemi'î! (Dinle!) — Ünzurî! (Bak!)",
            "• İftahî! (Aç!) — Ağlikî! (Kapat!)",
            "• Teâley! (Gel!) — İzhebî! (Git!)",
            "• Emir fiilin sonuna muhataba yâ'sı (-î) eklenir."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Harekeleri Tamamlayan İşaretler: Cezm (Sükûn) ve Şedde</text>',
        _kart(30, 50, 335, 215, "Cezm / Sükûn (Küçük Daire İşareti)", [
            "• Harfin üzerine konulan küçük dairedir.",
            "• Üzerinde cezm olan harf sesli okunmaz;",
            "  kendinden önceki harekeli harfe tutunur.",
            "• Örnek: Men (Kim?) — Hel (Mı/Mi?) — Min (-den)",
            "• Örnek: Key-fe (Nasıl?) — En-te (Sen)",
            "• Türkçedeki sessiz harfle biten hece gibidir."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Şedde (Dişli Kuvvetlendirme İşareti)", [
            "• Harfin üzerine konulan 'w' benzeri işarettir.",
            "• Üzerinde bulunduğu harfi İKİ KEZ okutur:",
            "  Birincisi cezimli (tutunarak), ikincisi harekeli!",
            "• Örnek: Üm-mün (Anne)",
            "• Örnek: Ced-dün (Dede)",
            "• Örnek: Mu-al-li-mün (Öğretmen)"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">1. Ünite Değerlendirme: Selamlaşma ve Güzel Sözün Önemi</text>',
        _kart(30, 50, 335, 195, "es-Selâmü Kable'l-Kelâm", [
            "• Anlamı: 'Önce selam, sonra kelam (söz).'",
            "• İletişimin anahtarı içten bir selamdır.",
            "• Selam barış, güven ve esenlik dileğidir.",
            "• Tanıdık-tanımadık herkese selam verilir.",
            "• Selam alanı daha güzeliyle selamlamak sünnettir."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "el-Kelimetü't-Tayyibetü Sadakatün", [
            "• Anlamı: 'Güzel söz sadakadır.' (Hadis-i Şerif)",
            "• 'Şükran', 'Afven', 'Min fadlike' demek",
            "  hem nezaket kuralı hem de sevaptır.",
            "• Güler yüz ve tatlı dil kalpleri birleştirir.",
            "• Sınıf içinde saygılı hitap huzur sağlar."
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
