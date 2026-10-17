# -*- coding: utf-8 -*-
"""7. Sınıf Temel Dini Bilgiler — 5. Hafta Görselleri (Mümin Kimliğim: İman, Salih Amel ve Güzel Ahlak)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mümin Kimliğinin Üç Sacayağı: İman, İbadet ve Ahlak</text>',
        _kart(25, 50, 225, 215, "1. Tahkîkî İman (Bilinçli İnanç)", [
            "• Delillere, tefekküre ve bilgiye",
            "  dayanan sarsılmaz inançtır.",
            "• Kalp ile tasdik (onaylama) ve",
            "  dil ile ikrar (söyleme) esastır.",
            "• İmanın altı esasını (Âmentü)",
            "  ayrılmaz bir bütün olarak kabul eder."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. İhlaslı İbadet ve Kulluk", [
            "• Yalnızca Allah'ın rızasını",
            "  kazanmak için yapılan kulluktur.",
            "• Gösterişten (riya) uzak samimiyet",
            "  yani 'İhlas' ibadetin ruhudur.",
            "• Namaz, oruç, zekât ve hac",
            "  mümin kimliğini canlı tutar."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Salih Amel ve Güzel Ahlak", [
            "• İmanın dış dünyadaki meyvesidir.",
            "• Doğruluk (sıdk), emanet bilinci,",
            "  adalet, merhamet ve vefadır.",
            "• İhsan bilinci: Allah'ı görüyormuş",
            "  gibi yaşama sorumluluğu."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Cibrîl Hadisi Işığında İslam, İman ve İhsan Dereceleri</text>',
        _kart(30, 50, 335, 215, "İslam (Teslimiyet) ve İman (Güven)", [
            "• İslam: Kelime-i Şehadet getirmek, namaz",
            "  kılmak, zekât vermek, Ramazan orucunu",
            "  tutmak ve gücü yetenin hacca gitmesidir.",
            "• İman: Allah'a, meleklerine, kitaplarına,",
            "  peygamberlerine, ahiret gününe ve",
            "  kadere (hayır ve şerrin Allah'tan olduğuna) inanmaktır."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "İhsan: Mümin Kimliğinin Zirvesi", [
            "• Tanımı: 'Allah'ı görüyormuşsun gibi O'na",
            "  kulluk etmendir; çünkü sen O'nu görmesen de",
            "  O seni mutlaka görmektedir!' (Hadis-i Şerif)",
            "• İhsan bilincine sahip mümine 'Muhsin' denir.",
            "• Muhsin insan yalnızken de toplum içindeyken",
            "  de dürüstlüğünden ve edebinden ödün vermez."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hucurât Suresi Işığında Müminlerin Kardeşlik Ahlakı</text>',
        _kart(30, 50, 335, 215, "Kaçınılması Gereken Davranışlar", [
            "• Zan (Suizan): İnsanlar hakkında kötü",
            "  düşünmekten ve önyargıdan sakınmak.",
            "• Tecessüs: Başkalarının gizli hallerini",
            "  ve kusurlarını araştırmamak.",
            "• Gıybet (Dedikodu), iftira, alay etme ve",
            "  kötü lakap takmaktan uzak durmak."
        ], "#e11d48", "#fff1f2"),
        _kart(395, 50, 335, 215, "Yaşatılması Gereken Kardeşlik İlkeleri", [
            "• 'Müminler ancak kardeştirler!' (Hucurât, 10).",
            "• Kardeşlerin arasını düzeltmek (ıslah etmek)",
            "  ve toplumsal barışı korumak.",
            "• Hüsnüzan (iyi niyet), affedicilik, tevazu",
            "  ve yardımlaşmayı kuşanmak.",
            "• Üstünlüğün yalnız takvada olduğunu bilmek."
        ], "#0d9488", "#f0fdfa"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mümin Kimliğinin Bireye ve Topluma Kazandırdıkları</text>',
        _kart(30, 50, 335, 195, "Bireysel Huzur ve Anlam Arayışı", [
            "• İnsana nereden gelip nereye gittiğini",
            "  ve hayatın amacını öğretir.",
            "• Tevekkül ve sabırla ruhsal dayanıklılık sağlar.",
            "• Ümitsizlik, karamsarlık ve yalnızlık",
            "  duygusunu ortadan kaldırır."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Toplumsal Güven ve Adalet", [
            "• Kul hakkı bilinciyle kimsenin malına, canına",
            "  ve onuruna zarar verilmemesini sağlar.",
            "• Zekât ve infakla sosyal adaleti güçlendirir.",
            "• Güvenilir insanların oluşturduğu huzurlu",
            "  ve erdemli bir toplum inşa eder."
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
