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
        'Kur’an Harflerinin 5 Temel Mahreç (Çıkış) Bölgesi</text>'
        + _kart(18, 42, 122, 135, "1. Cevf (Boşluk)", [
            "• Ağız ve boğaz",
            "  boşluğu",
            "• Med harfleri:",
            "  Elif, Vav, Ya"
        ], "#2563eb", "#eff6ff")
        + _kart(148, 42, 122, 135, "2. Halk (Boğaz)", [
            "• 6 Boğaz harfi:",
            "• Hemze, He",
            "• Ayn, Ha",
            "• Gayn, Hı"
        ], "#059669", "#ecfdf5")
        + _kart(278, 42, 124, 135, "3. Lisan (Dil)", [
            "• En çok harfin",
            "  çıktığı bölge",
            "• Kaf, Kef, Cim",
            "• Şın, Dad, Lam..."
        ], "#d97706", "#fffbeb")
        + _kart(410, 42, 122, 135, "4. Şefeteyn", [
            "• İki dudak:",
            "• Fe (Üst diş-dudak)",
            "• Be, Mim, Vav",
            "  (İki dudak)"
        ], "#7c3aed", "#f5f3ff")
        + _kart(540, 42, 122, 135, "5. Hayşûm", [
            "• Geniz boşluğu",
            "• Gunne sesinin",
            "  çıkış yeridir",
            "• Nun ve Mim’de"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 192, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Peltek Harfler ve Kalın-İnce Harf Ayrımı</text>'
        + _kart(25, 42, 300, 145, "Peltek Okunan 3 Harf (Dil Ucu - Ön Diş)", [
            "• Peltek Se (ث): İnce ve yumuşak okunur",
            "• Peltek Zel (ذ): İnce ve keskin olmadan",
            "• Peltek Zı (ظ): Kalın ve dolgun okunur",
            "• Dil ucu üst ön dişlerin ucuna hafifçe değer",
            "• Sin (س), Keskin Ze (ز) ve Dad (ض) ile karışmamalı"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Kalın (İsti’la) Harfleri: Hussa Dağatın Kız", [
            "• Hı (خ), Sad (ص), Dad (ض), Gayn (غ)",
            "• Tı (ط), Kaf (ق), Zı (ظ) -> 7 Kalın Harf",
            "• Üstün harekede ”a-o” arası tok sesle okunur",
            "• Diğer 20 harf ince (istifal) harflerdir",
            "• Ra (ر) ve Lam (ل) duruma göre kalın/ince olur"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Okunuşu Özel Olan Harf ve İşaretler (Elifba Özel Durumlar)</text>'
        + _kart(20, 42, 200, 140, "Okunmayan Elif / Vav / Ya", [
            "• Lafzatullah’ta (اللّٰه) vav/elif",
            "• Çoğul vav’ından sonraki elif",
            "• (كَتَبُوا) -> Sondaki elif okunmaz",
            "• Altında ”kasr” yazan uzatmalar"
        ], "#d97706", "#fffbeb")
        + _kart(240, 42, 200, 140, "Vasıl Hemzesi ve Med-Kasr", [
            "• Söz başında okunur, geçişte",
            "  düşer (وَاسْجُدْ -> Vescüd)",
            "• Altında ”med” (مَدّ) varsa uzatılır",
            "• Altında ”kasr” (قَصْر) varsa kısa"
        ], "#7c3aed", "#f5f3ff")
        + _kart(460, 42, 200, 140, "Kur’an’da 4 Özel Uygulama", [
            "• İmale (Hûd 41: Mecrêhâ)",
            "• İşmam (Yûsuf 11: Lâ te’mennâ)",
            "• Teshil (Fussilet 44: E’acemiyyün)",
            "• Sekte (Yâsîn, Kehf, Kıyâme, Mut.)"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 195, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Mushaflarda Rastlanan Özel Semboller ve Vakıf (Durak) İşaretleri</text>'
        + _kart(25, 42, 300, 135, "Sıfır (०) İşareti ve Uzatma Çizgisi (~)", [
            "• Harfin üzerindeki yuvarlak sıfır (०):",
            "  O harfin okunmayacağını (ziyade olduğunu) gösterir",
            "• ”Ene” (اَنَا۠) kelimesinde geçerken elif uzatılmaz",
            "• Çeker (~) işareti harfi 4 elif miktarı uzatır"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 135, "Temel Vakıf (Durak) İşaretleri", [
            "• Mim (مـ): Vakf-ı Lâzım (Kesinlikle durulmalı)",
            "• Tı (ط) ve Cim (ج): Durulması uygun duraklar",
            "• Lâ (لا): Durulmamalı (Ayet sonu hariç)",
            "• Ayn (ع): Rükû / konu bütünlüğü sonu işareti"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 190, ic)


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
