def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Lale Devri (1718–1730): Siyasi Çerçeve ve Diplomatik Dönüşüm</text>'
        + _kart(25, 42, 300, 145, "Dönemin Temel Aktörleri ve Başlangıcı", [
            "• Başlangıç: 1718 Pasarofça Antlaşması",
            "• Bitiş: 1730 Patrona Halil İsyanı",
            "• Padişah: III. Ahmed  |  Sadrazam: Nevşehirli",
            "  Damat İbrahim Paşa",
            "• Dönemin Şairi: Nedîm  |  Nakkaşı: Levnî"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Diplomasi ve Batı’yı Tanıma Politikası", [
            "• Fetih politikası yerine barışı koruma ve diplomasi",
            "• Avrupa başkentlerine ilk geçici elçilikler:",
            "  Viyana, Paris, Moskova, Lehistan",
            "• Paris Sefiri Yirmisekiz Çelebi Mehmed Efendi’nin",
            "  Sefâretnâme’si yenileşmeye rehberlik etmiştir."
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Lale Devri’nde Bilim, Kültür, Sanat ve Toplumsal Yenilikler</text>'
        + _kart(18, 42, 205, 145, "Matbaa ve Bilim", [
            "• İlk Türk matbaası (1727):",
            "  İbrahim Müteferrika ve",
            "  Said Efendi tarafından kuruldu.",
            "• İlk basılan eser: Vankulu Lügati",
            "• Tercüme Heyeti ve kütüphaneler"
        ], "#d97706", "#fffbeb")
        + _kart(237, 42, 205, 145, "Şehircilik ve Ekonomi", [
            "• Tulumbacılar Ocağı (1720):",
            "  İlk düzenli itfaiye teşkilatı",
            "• Çiçek aşısı uygulaması",
            "• Yalova’da kâğıt, İstanbul’da",
            "  kumaş ve çini imalathaneleri"
        ], "#7c3aed", "#f5f3ff")
        + _kart(456, 42, 205, 145, "Mimari ve Toplum Hayatı", [
            "• Sivil mimari ve kamusal mekânlar",
            "• III. Ahmed Çeşmesi ve",
            "  Sadâbâd Kasrı (Kâğıthane)",
            "• Askerî ıslahat yapılmamış,",
            "  1730’da isyanla sona ermiştir."
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 202, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
}


def uygula(v):
    hedefler = [0, 1]
    anahtarlar = ["b1", "b2"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]