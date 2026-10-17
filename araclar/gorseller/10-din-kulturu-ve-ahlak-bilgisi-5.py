# -*- coding: utf-8 -*-
"""10. Sınıf Din Kültürü ve Ahlak Bilgisi — 5. Hafta Görselleri
Konu: Allah-Âlem İlişkisi: Yaratma, Sünnetullah ve Evrendeki Ölçü ve Düzen
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0d9488", arka="#f0fdfa"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Allah-Âlem İlişkisinin Temel Boyutları (Yaratma, Kudret, İrade, Kayyumiyet)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Allah (c.c.) ve Âlem İlişkisi: Yoktan Yaratma ve Sürekli Yönetim", "#0d9488", "#f0fdfa")

    s += '<rect x="230" y="50" width="300" height="44" rx="10" fill="#0f766e" stroke="#115e59" stroke-width="1.5"/>'
    s += '<text x="380" y="70" text-anchor="middle" fill="#fff" font-size="12.5" font-weight="700">ALLAH (c.c.) — Rabbü\'l-Âlemîn</text>'
    s += '<text x="380" y="86" text-anchor="middle" fill="#99f6e4" font-size="10">Âlemlerin Yaratıcısı, Sahibi ve Yöneticisi</text>'

    for x in [110, 290, 470, 650]:
        s += f'<line x1="380" y1="94" x2="{x}" y2="125" stroke="#14b8a6" stroke-width="1.8"/>'

    boyutlar = [
        ("İbda &amp; Halk (Yaratma)", "El-Bedi / El-Halık", "Âlemi örneksiz ve", "yoktan var etmesi,", "her şeye ölçü vermesi.", "#0284c7", "#e0f2fe"),
        ("Kayyumiyet (Ayakta Tutma)", "El-Kayyum / Er-Rabb", "Yaratılan evreni her an", "koruyup gözetmesi; yaratmanın", "kesintisiz sürmesi.", "#0d9488", "#ccfbf1"),
        ("Rızık ve Rahmet", "Er-Rezzak / Er-Rahman", "Canlıların yaşaması için", "maddi ve manevi tüm", "nimetleri bahşetmesi.", "#16a34a", "#dcfce7"),
        ("Ölçü ve Kader", "El-Hakîm / El-Alîm", "Evrene değişmez yasalar", "(Sünnetullah) ve hassas", "denge koyması.", "#d97706", "#fef3c7"),
    ]
    for i, (bas, esma, a1, a2, a3, r, bg) in enumerate(boyutlar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="125" width="168" height="160" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="125" width="168" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="143" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="170" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{esma}</text>'
        s += f'<text x="{x+84}" y="196" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="214" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="232" text-anchor="middle" fill="#1e293b" font-size="10">{a3}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Âlem Kavramı ve Varlık Âlemlerinin Sınıflandırılması (Şehadet ve Gayb Âlemi)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İslam Düşüncesinde Âlem Kavramı: Şehadet (Görünen) ve Gayb Âlemi", "#1d4ed8", "#eff6ff")

    # Sol: Şehadet Âlemi
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<rect x="30" y="55" width="335" height="30" rx="10" fill="#2563eb"/>'
    s += '<text x="197" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. ŞEHADET (Mülk / Görünen) ÂLEMİ</text>'
    s += '<text x="197" y="102" text-anchor="middle" fill="#1e40af" font-size="10.5" font-weight="700">Duyu organlarıyla veya bilimsel araçlarla algılanabilen âlem</text>'

    sehadet = [
        ("Fiziksel Evren (Kozmos):", "Gök cisimleri, galaksiler, Güneş, Dünya, su ve hava."),
        ("Canlılar Dünyası:", "Bitkiler, hayvanlar, mikroorganizmalar ve insan."),
        ("Bilimsel İnceleme:", "Deney, gözlem ve akılla keşfedilen Kevni ayetler."),
    ]
    for i, (b, ac) in enumerate(sehadet):
        y = 118 + i * 50
        s += f'<rect x="46" y="{y}" width="303" height="42" rx="6" fill="#eff6ff" stroke="#60a5fa" stroke-width="1"/>'
        s += f'<text x="56" y="{y+16}" fill="#1d4ed8" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="56" y="{y+32}" fill="#334155" font-size="9.8">{ac}</text>'

    # Sağ: Gayb Âlemi
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#c4b5fd" stroke-width="1.5"/>'
    s += '<rect x="395" y="55" width="335" height="30" rx="10" fill="#7c3aed"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. GAYB (Melekût / Görünmeyen) ÂLEMİ</text>'
    s += '<text x="562" y="102" text-anchor="middle" fill="#5b21b6" font-size="10.5" font-weight="700">Duyularla algılanamayan, yalnız Vahiy ile bilinen âlem</text>'

    gayb = [
        ("Ruhani Varlıklar:", "Melekler, cinler ve ruh âlemi."),
        ("Ahiret Hayatı:", "Berzah (kabir), kıyamet, haşir, mizân, cennet ve cehennem."),
        ("Bilgi Kaynağı:", "Kur'an-ı Kerim ve sahih sünnet (Haber-i Sadık / Vahiy)."),
    ]
    for i, (b, ac) in enumerate(gayb):
        y = 118 + i * 50
        s += f'<rect x="411" y="{y}" width="303" height="42" rx="6" fill="#f5f3ff" stroke="#a78bfa" stroke-width="1"/>'
        s += f'<text x="421" y="{y+16}" fill="#6d28d9" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="421" y="{y+32}" fill="#334155" font-size="9.8">{ac}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Sünnetullah (Evrendeki İlahi Yasalar): Fiziksel, Biyolojik ve Toplumsal Yasalar."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Sünnetullah: Allah'ın Evrene Koyduğu Değişmez Yasalar (Ölçü ve Düzen)", "#b45309", "#fffbeb")

    yasalar = [
        ("1. Fiziksel Yasalar", "Madde ve Enerji Yasaları", "• Gezegenlerin yörüngesi", "• Suyun kaldırma kuvveti", "• Gece-gündüz ve mevsimler", "Deney ve gözlemle", "kesin ve değişmezdir.", "#0284c7", "#f0f9ff"),
        ("2. Biyolojik Yasalar", "Canlılık ve Yaşam Yasaları", "• Doğum, büyüme ve üreme", "• Fotosentez ve solunum", "• Canlıların çevreye uyumu", "Canlıların yapı ve", "işleyişini düzenler.", "#16a34a", "#f0fdf4"),
        ("3. Toplumsal Yasalar", "İnsan ve Toplum Yasaları", "• Adalet, güven ve barış", "• Zulmün çöküş getirmesi", "• Göç, ticaret ve dayanışma", "Neden-sonuç ilişkisiyle", "toplumları yönlendirir.", "#d97706", "#fffbeb"),
    ]
    for i, (bas, alt, m1, m2, m3, a1, a2, r, bg) in enumerate(yasalar):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="230" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="100" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{alt}</text>'
        s += f'<text x="{x+36}" y="128" fill="#1e293b" font-size="10.2">{m1}</text>'
        s += f'<text x="{x+36}" y="148" fill="#1e293b" font-size="10.2">{m2}</text>'
        s += f'<text x="{x+36}" y="168" fill="#1e293b" font-size="10.2">{m3}</text>'
        s += f'<rect x="{x+18}" y="192" width="188" height="72" rx="8" fill="#fff" stroke="{r}" stroke-width="1"/>'
        s += f'<text x="{x+112}" y="220" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+112}" y="240" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a2}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Allah-Âlem-İnsan İlişkisinde İslam'ın Yaratılış Anlayışı vs Deizm/Materyalizm Karşılaştırması."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İslam'ın Allah-Âlem Tasavvuru ve İnsanın Evrendeki Sorumluluğu (Emanet)", "#047857", "#ecfdf5")

    # Sol: İslam'ın Yaratma Anlayışı
    s += '<rect x="28" y="55" width="340" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="198" y="78" text-anchor="middle" fill="#065f46" font-size="12" font-weight="700">İslam\'da Sürekli Yaratma (Hallâk &amp; Kayyûm)</text>'

    ilkeler = [
        ("Tesadüf Değil, Hikmet:", "Evrendeki hiçbir varlık boşuna ve gayesiz yaratılmamıştır."),
        ("Müdahil Yaratıcı:", "Allah âlemi yaratıp kendi hâline bırakmamıştır; her an yönetir."),
        ("Kevni Ayetler Kitabı:", "Evren okunması gereken büyük bir Kur'an, doğa ise ayettir."),
    ]
    for i, (b, ac) in enumerate(ilkeler):
        y = 94 + i * 58
        s += f'<rect x="44" y="{y}" width="308" height="48" rx="6" fill="#f0fdf4" stroke="#10b981" stroke-width="1"/>'
        s += f'<text x="54" y="{y+18}" fill="#065f46" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="54" y="{y+36}" fill="#334155" font-size="9.8">{ac}</text>'

    # Sağ: İnsanın Âlemdeki Konumu
    s += '<rect x="392" y="55" width="340" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="562" y="78" text-anchor="middle" fill="#065f46" font-size="12" font-weight="700">İnsanın Âlemdeki Konumu: Halife ve Emanetçi</text>'

    gorevler = [
        ("Tefekkür ve Bilim:", "Evrendeki düzeni (Mizan) akılla inceleyip Yaratıcıyı tanımak."),
        ("İmar ve Islah:", "Yeryüzünü yaşanabilir kılmak, adaleti ve iyiliği yaymak."),
        ("Mizanı Bozmmamak:", "Doğal dengeyi (ekolojiyi) korumak, israf ve fesattan kaçınmak."),
    ]
    for i, (b, ac) in enumerate(gorevler):
        y = 94 + i * 58
        s += f'<rect x="408" y="{y}" width="308" height="48" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1"/>'
        s += f'<text x="418" y="{y+18}" fill="#047857" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="418" y="{y+36}" fill="#334155" font-size="9.8">{ac}</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
