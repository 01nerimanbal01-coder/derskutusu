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
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Tecvidde Med (Uzatma) Kavramı, Harf-i Med ve Sebeb-i Med</text>'
        + _kart(25, 42, 300, 145, "3 Med Harfi (Harf-i Med: ا - و - ي)", [
            "• Elif (ا): Kendisi sakin, önceki harf üstünlü (قَالَ)",
            "• Vav (و): Kendisi sakin, önceki harf ötreli (يَقُولُ)",
            "• Ya (ي): Kendisi sakin, önceki harf esreli (قِيلَ)",
            "• Sebeb-i med yoksa 1 elif miktarı uzatılır:",
            "  Buna ”Medd-i Tabiî” (Doğal Uzatma) denir"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "2 Sebeb-i Med (Hemze ve Sükûn)", [
            "• Aslî uzatmayı 1 eliften 2, 3 veya 4 elife çıkaran",
            "  iki temel sebep vardır:",
            "• 1. Hemze (ء / أ): Uzun veya kırık hemze",
            "• 2. Sükûn (ْ / ّ ): Cezim veya şedde",
            "  (Lâzım sükûn: kalıcı | Ârızî sükûn: duruşta oluşan)"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Sebebi Hemze Olan Medler: Medd-i Muttasıl ve Medd-i Munfasıl</text>'
        + _kart(25, 42, 300, 145, "Medd-i Muttasıl (Bitişik Uzatma - Vacip)", [
            "• Harf-i med ile hemze AYNI kelimede yan yana",
            "• Örnek: جَآءَ (câe), سُوءَ (sûe), شِيءَ (şîe)",
            "• اَلْمَلٰٓئِكَةُ (el-melâiketü), شُهَدَآءُ (şühedâü)",
            "• Hükmü: Vaciptir (Asım kıraatinde 4 elif uzatılır)",
            "• Kısaltılması (kasr) caiz değildir"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Medd-i Munfasıl (Ayrık Uzatma - Caiz)", [
            "• Harf-i med birinci kelimenin sonunda, hemze ise",
            "  ikinci kelimenin başında (AYRI kelimelerde)",
            "• Örnek: يَآ أَيُّهَا (yâ eyyühâ), إِنَّآ أَعْطَيْنَاكَ",
            "• قُوا أَنْفُسَكُمْ، وَفِي أَنْفُسِكُمْ",
            "• Hükmü: Caizdir (Hafs rivayetinde 4 elif; hızlıda 2)"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Sebebi Sükûn Olan Medler: Medd-i Lâzım, Medd-i Ârız ve Medd-i Lîn</text>'
        + _kart(20, 42, 200, 142, "1. Medd-i Lâzım", [
            "• Harf-i medden sonra",
            "  LÂZIM (kalıcı) sükûn",
            "  (durulsa da geçilse de var)",
            "• Örnek: اَلْحَآقَّةُ، الضَّآلِّينَ، الٓمٓ",
            "• Hükmü: Lâzım (4 elif)"
        ], "#dc2626", "#fef2f2")
        + _kart(240, 42, 200, 142, "2. Medd-i Ârız", [
            "• Harf-i medden sonra",
            "  ÂRIZÎ (duruşla oluşan)",
            "  sükûn gelirse oluşur",
            "• Örnek: اَلْعَالَمِينَ -> el-âlemîn",
            "• Hükmü: Caiz (tûl/tevassut/kasr)"
        ], "#7c3aed", "#f5f3ff")
        + _kart(460, 42, 200, 142, "3. Medd-i Lîn", [
            "• Üstünlü harften sonra",
            "  cezimli Vav (وْ) veya Ya (يْ)",
            "  (Harf-i Lîn) + sükûn",
            "• Örnek: قُرَيْشٍ، الصَّيْفِ، خَوْفٍ",
            "• Durulduğunda uzatılır"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 198, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Med Çeşitlerini Hızlı Ayırt Etme Şeması</text>'
        + _kart(25, 42, 300, 138, "Adım 1: Harf-i Medden Sonra Ne Var?", [
            "• Hiçbir sebep yoksa -> Medd-i Tabiî (1 elif)",
            "• Aynı kelimede Hemze varsa -> Medd-i Muttasıl",
            "• Ayrı kelimede Hemze varsa -> Medd-i Munfasıl"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Adım 2: Sükûn Kalıcı mı, Geçici mi?", [
            "• Geçişte de düşmeyen cezim/şedde -> Medd-i Lâzım",
            "• Sadece durulunca oluşan sükûn -> Medd-i Ârız",
            "• Öncesi üstünlü وْ / يْ + duruş -> Medd-i Lîn"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
