def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Kur\'an-ı Kerim Harflerinin 5 Temel Mahreç (Çıkış) Bölgesi (KK.9.2.1)</text>'
    c += _kart(18, 54, 206, 180, "1. Cevf ve 2. Boğaz (Halk)", [
        "• Cevf (Ağız-Boğaz Boşluğu):",
        "  Med (uzatma) harfleri (Elif, Vav, Yâ).",
        "• Boğaz (Halk — 6 Harf):",
        "  Alt boğaz: Hemze, Hâ",
        "  Orta boğaz: Ayn, Hâ (noktasız)",
        "  Üst boğaz: Gayn, Hı (noktalı)"
    ], "#1a5276", "#eaf2f8")
    c += _kart(237, 54, 206, 180, "3. Dil (Lisan — 18 Harf)", [
        "• En fazla harfin çıktığı bölgedir.",
        "• Dil kökü: Kâf, Kef",
        "• Dil ortası: Cîm, Şîn, Yâ",
        "• Dil yanları: Dâd, Lâm",
        "• Dil ucu: Nûn, Râ, Tâ, Dâl, Te,",
        "  Sâd, Zây, Sîn, Zı, Zâl, Peltek Se"
    ], "#117864", "#e8f8f5")
    c += _kart(456, 54, 206, 180, "4. Dudak ve 5. Geniz", [
        "• Dudak (Şefetân — 4 Harf):",
        "  Fâ (üst ön dişler + alt dudak),",
        "  Bâ, Mîm, Vâv (iki dudak).",
        "• Geniz (Hayşûm):",
        "  Gunne sıfatının çıkış yeridir",
        "  (Mîm ve Nûn harflerindeki geniz sesi)."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Telaffuz Özelliklerine Göre Kalın, İnce ve Peltek Harfler</text>'
    c += _kart(18, 54, 314, 170, "Kalın (İstila) Harfler (7 Harf)", [
        "• Dil kökünün üst damağa yükselmesiyle tok ve",
        "  dolgun sesle okunan harflerdir.",
        "• 7 Kalın Harf: Hı, Sâd, Dâd, Gayn, Tı, Kâf, Zı",
        "• Kodlama: \'Hussa Dagtın Kız\'",
        "• Üstün harekede \'a\', esrede \'ı\', ötrede \'u\' okunur."
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 170, "Peltek Harfler (3 Harf) ve İnce Harfler", [
        "• Peltek Harfler (3 Harf): Dil ucunun üst ön dişlerin",
        "  ucuna hafifçe değdirilmesiyle çıkarılan harflerdir:",
        "  1) Se (İnce peltek), 2) Zâl (İnce peltek),",
        "  3) Zı (Kalın peltek).",
        "• İnce Harfler: Kalın harfler dışındaki harflerdir."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#922b21"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Birbirine Benzer Sesli Harflerin Ayırt Edilmesi (Tashih-i Huruf)</text>'
    c += _kart(18, 54, 206, 170, "Se - Sîn - Sâd Ayrımı", [
        "• Se: İnce ve PELTEK okunur.",
        "• Sîn: İnce ve KESKİN (ıslıklı)",
        "  okunur.",
        "• Sâd: KALIN ve tok okunur.",
        "• Karıştırılması anlamı bozar!"
    ], "#922b21", "#fdedec")
    c += _kart(237, 54, 206, 170, "Zâl - Zây - Zı - Dâd Ayrımı", [
        "• Zâl: İnce ve PELTEK okunur.",
        "• Zây: İnce ve KESKİN (vızıltılı)",
        "  okunur.",
        "• Zı: KALIN ve PELTEK okunur.",
        "• Dâd: Dil yanından kalın çıkar."
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 170, "Hâ - Ha - Hı ve Hemze - Ayn", [
        "• Hâ (Alt boğaz): Göğüsten ince.",
        "• Ha (Orta boğaz): Boğaz hafif",
        "  sıkılarak ince ve sürtünmeli.",
        "• Hı (Üst boğaz): Kalın ve hırıltılı.",
        "• Ayn: Orta boğazdan tok ses."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#2874a6"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Hem Kalın Hem İnce Okunabilen Harfler ve Tertil İlkesi</text>'
    c += _kart(18, 54, 314, 165, "Duruma Göre Kalın veya İnce Okunanlar", [
        "• Râ Harfi: Üstün ve ötreli iken kalın; esreli",
        "  iken ince okunur.",
        "• Lafzatullah\'ın (Allah Lafzının) Lâm\'ı: Kendisinden",
        "  önceki harf üstün/ötre ise KALIN (Allâh), esre ise",
        "  İNCE (Lillâhi / Bismillâhi) okunur."
    ], "#2874a6", "#eaf2f8")
    c += _kart(348, 54, 314, 165, "Tertil İle Okumanın Önemi", [
        "• \'Kur\'an\'ı tertîl ile (harflerin hakkını vererek,",
        "  tane tane ve düşünerek) oku!\' (Müzzemmil, 73/4).",
        "• Harfleri doğru mahreç ve sıfatla telaffuz etmek,",
        "  kelimelerin anlamını korumanın ilk şartıdır.",
        "• Fem-i Muhsin: Kur\'an\'ı güzel okuyan üstat ağız."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
