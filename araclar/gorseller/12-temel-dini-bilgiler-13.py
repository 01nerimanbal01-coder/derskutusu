import xml.etree.ElementTree as ET

PALET = {
    "kirmizi":   "#e74c3c",
    "koyu_kirm": "#c0392b",
    "acik_kirm": "#fadbd8",
    "mavi":      "#2980b9",
    "koyu_mavi": "#1a5276",
    "acik_mavi": "#d4e6f1",
    "yesil":     "#27ae60",
    "koyu_yes":  "#1e8449",
    "acik_yes":  "#d5f5e3",
    "turuncu":   "#e67e22",
    "acik_tur":  "#fdebd0",
    "mor":       "#8e44ad",
    "acik_mor":  "#ebdef0",
    "sari":      "#f1c40f",
    "acik_sari": "#fef9e7",
    "gri":       "#7f8c8d",
    "acik_gri":  "#ecf0f1",
    "koyu":      "#2c3e50",
    "beyaz":     "#ffffff",
}

FONT = "DejaVu Sans, Arial, sans-serif"


def _svg_kok(w: float, h: float) -> ET.Element:
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": f"0 0 {w:g} {h:g}",
        "width": "100%",
        "height": "100%",
    })
    defs = ET.SubElement(svg, "defs")
    for ad, renk in [("koyu", PALET["koyu"]), ("kirmizi", PALET["kirmizi"]),
                     ("mavi", PALET["mavi"]), ("yesil", PALET["yesil"]),
                     ("turuncu", PALET["turuncu"]), ("mor", PALET["mor"])]:
        m = ET.SubElement(defs, "marker", {
            "id": f"ok-{ad}", "viewBox": "0 0 10 10",
            "refX": "8", "refY": "5",
            "markerWidth": "5.5", "markerHeight": "5.5",
            "orient": "auto-start-reverse",
        })
        ET.SubElement(m, "path", {"d": "M 0 1.5 L 9 5 L 0 8.5 z", "fill": renk})
    return svg


def _yazi(ebeveyn, x, y, metin, boyut=8.5, renk=PALET["koyu"],
          bold=False, anchor="middle", italic=False):
    if not metin:
        return None
    el = ET.SubElement(ebeveyn, "text", {
        "x": f"{x:g}", "y": f"{y:g}",
        "font-family": FONT, "font-size": f"{boyut:g}",
        "fill": renk, "text-anchor": anchor,
        "font-weight": "bold" if bold else "normal",
        "font-style": "italic" if italic else "normal",
    })
    el.text = str(metin)
    return el


def _kutu(ebeveyn, x, y, w, h, dolgu=PALET["acik_mavi"],
          kenar=PALET["mavi"], r=5, kalinlik=1.3):
    return ET.SubElement(ebeveyn, "rect", {
        "x": f"{x:g}", "y": f"{y:g}", "width": f"{w:g}", "height": f"{h:g}",
        "rx": f"{r:g}", "ry": f"{r:g}",
        "fill": dolgu, "stroke": kenar, "stroke-width": f"{kalinlik:g}",
    })


def _cizgi(ebeveyn, x1, y1, x2, y2, renk=PALET["koyu"],
           kalinlik=1.4, kesikli=False, ok=None):
    attr = {
        "x1": f"{x1:g}", "y1": f"{y1:g}", "x2": f"{x2:g}", "y2": f"{y2:g}",
        "stroke": renk, "stroke-width": f"{kalinlik:g}",
        "stroke-linecap": "round",
    }
    if kesikli:
        attr["stroke-dasharray"] = "4,3"
    if ok:
        attr["marker-end"] = f"url(#ok-{ok})"
    return ET.SubElement(ebeveyn, "line", attr)


def _g1(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_yes"], kenar=PALET["koyu_yes"], r=5)
    _yazi(svg, w / 2, 20, "KUR'AN VE SÜNNETTE NAMAZ (SALÂT) İBADETİNİN ÖNEMİ", boyut=8.5, renk=PALET["beyaz"], bold=True)

    cx, cy = w / 2, 105
    _kutu(svg, cx - 72, cy - 26, 144, 52, dolgu=PALET["yesil"], kenar=PALET["koyu_yes"], r=10, kalinlik=1.8)
    _yazi(svg, cx, cy - 8, "SALÂT (NAMAZ)", boyut=9.0, renk=PALET["beyaz"], bold=True)
    _yazi(svg, cx, cy + 6, "Tekbirle başlayıp selamla", boyut=7.0, renk=PALET["acik_sari"])
    _yazi(svg, cx, cy + 17, "biten farz-ı ayın ibadet", boyut=7.0, renk=PALET["acik_sari"], bold=True)

    kartlar = [
        (12, 36, "MİRAÇ HEDİYESİ", PALET["mavi"], PALET["acik_mavi"],
         "Hicretten önce Miraç", "gecesinde doğrudan Allah", "tarafından farz kılındı."),
        (w - 162, 36, "KUR'AN'DA NAMAZ", PALET["turuncu"], PALET["acik_tur"],
         "Bakara 43 & Ankebût 45:", "'Namazı dosdoğru kılın,", "zekâtı verin.'"),
        (12, 122, "HADİSLERDE KONUMU", PALET["mor"], PALET["acik_mor"],
         "'Namaz dinin direğidir.'", "'Namaz müminin miracı", "ve gözümün nurudur.'"),
        (w - 162, 122, "AHİRETTE İLK HESAP", PALET["kirmizi"], PALET["acik_kirm"],
         "Kıyamet gününde kulun", "ilk hesaba çekileceği", "ameli namazdır."),
    ]
    for kx, ky, bas, renk, acik, s1, s2, s3 in kartlar:
        _kutu(svg, kx, ky, 150, 66, dolgu=acik, kenar=renk, r=5, kalinlik=1.3)
        _kutu(svg, kx, ky, 150, 17, dolgu=renk, kenar=renk, r=4)
        _yazi(svg, kx + 75, ky + 12, bas, boyut=7.2, renk=PALET["beyaz"], bold=True)
        _yazi(svg, kx + 75, ky + 30, s1, boyut=7.0, renk=PALET["koyu"], bold=True)
        _yazi(svg, kx + 75, ky + 42, s2, boyut=6.9, renk=PALET["koyu"])
        _yazi(svg, kx + 75, ky + 54, s3, boyut=6.9, renk=PALET["koyu"])

    _cizgi(svg, 162, 69, cx - 72, cy - 10, renk=PALET["mavi"], kalinlik=1.4, ok="mavi")
    _cizgi(svg, w - 162, 69, cx + 72, cy - 10, renk=PALET["turuncu"], kalinlik=1.4, ok="turuncu")
    _cizgi(svg, 162, 155, cx - 72, cy + 10, renk=PALET["mor"], kalinlik=1.4, ok="mor")
    _cizgi(svg, w - 162, 155, cx + 72, cy + 10, renk=PALET["kirmizi"], kalinlik=1.4, ok="kirmizi")
    return svg


def _g2(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_mavi"], kenar=PALET["koyu_mavi"], r=5)
    _yazi(svg, w / 2, 20, "NAMAZ İBADETİNİN BİREYSEL VE TOPLUMSAL HİKMETLERİ", boyut=8.5, renk=PALET["beyaz"], bold=True)

    kw = (w - 30) / 2
    _kutu(svg, 10, 34, kw, h - 42, dolgu=PALET["acik_yes"], kenar=PALET["yesil"], r=6, kalinlik=1.5)
    _kutu(svg, 10, 34, kw, 20, dolgu=PALET["yesil"], kenar=PALET["yesil"], r=5)
    _yazi(svg, 10 + kw / 2, 47, "BİREYSEL VE AHLAKİ HİKMETLERİ", boyut=7.8, renk=PALET["beyaz"], bold=True)

    bireysel = [
        ("Manevi Huzur ve Zikir", "Günde 5 vakit Rabbiyle buluşarak kalp huzuru bulma"),
        ("Ahlaki Kalkan (Ankebût 45)", "Hayasızlıktan (fahşâ) ve kötülükten (münker) korunma"),
        ("Temizlik Alışkanlığı", "Abdest ve taharetle sürekli beden ve elbise temizliği"),
        ("Zaman Bilinci ve Disiplin", "Belirli vakitlerde ibadetle hayatı planlama disiplini"),
    ]
    for i, (b, a) in enumerate(bireysel):
        by = 60 + i * 32
        _kutu(svg, 18, by, kw - 16, 27, dolgu=PALET["beyaz"], kenar=PALET["koyu_yes"], r=4)
        _yazi(svg, 10 + kw / 2, by + 11, b, boyut=7.3, renk=PALET["koyu_yes"], bold=True)
        _yazi(svg, 10 + kw / 2, by + 22, a, boyut=6.7, renk=PALET["koyu"])

    rx = 20 + kw
    _kutu(svg, rx, 34, kw, h - 42, dolgu=PALET["acik_mavi"], kenar=PALET["mavi"], r=6, kalinlik=1.5)
    _kutu(svg, rx, 34, kw, 20, dolgu=PALET["mavi"], kenar=PALET["mavi"], r=5)
    _yazi(svg, rx + kw / 2, 47, "TOPLUMSAL VE SOSYAL HİKMETLERİ", boyut=7.8, renk=PALET["beyaz"], bold=True)

    toplumsal = [
        ("Eşitlik ve Tevazu", "Aynı safta makam, servet ve statü farkı olmadan durma"),
        ("Kardeşlik ve Kaynaşma", "Cemaat, cuma ve bayram namazlarıyla komşuluk bağı"),
        ("Yardımlaşma ve Dayanışma", "Sevinç ve sıkıntıları paylaşarak sosyal yardımlaşma"),
        ("Ortak Ümmet Bilinci", "Dünyanın her yerinde aynı kıbleye (Kâbe) yönelme"),
    ]
    for i, (b, a) in enumerate(toplumsal):
        by = 60 + i * 32
        _kutu(svg, rx + 8, by, kw - 16, 27, dolgu=PALET["beyaz"], kenar=PALET["koyu_mavi"], r=4)
        _yazi(svg, rx + kw / 2, by + 11, b, boyut=7.3, renk=PALET["koyu_mavi"], bold=True)
        _yazi(svg, rx + kw / 2, by + 22, a, boyut=6.7, renk=PALET["koyu"])
    return svg


def _g3(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu"], kenar=PALET["koyu"], r=5)
    _yazi(svg, w / 2, 20, "NAMAZIN 12 FARZI: DIŞINDAKİ ŞARTLAR (6) VE İÇİNDEKİ RÜKÜNLER (6)", boyut=8.3, renk=PALET["sari"], bold=True)

    kw = (w - 30) / 2
    _kutu(svg, 10, 33, kw, h - 40, dolgu=PALET["acik_tur"], kenar=PALET["turuncu"], r=6, kalinlik=1.5)
    _kutu(svg, 10, 33, kw, 19, dolgu=PALET["turuncu"], kenar=PALET["turuncu"], r=5)
    _yazi(svg, 10 + kw / 2, 46, "NAMAZIN DIŞINDAKİ FARZLAR (6 ŞART)", boyut=7.6, renk=PALET["beyaz"], bold=True)

    sartlar = [
        ("1. Hadesten Taharet", "Abdest, gusül veya teyemmüm almak"),
        ("2. Necasetten Taharet", "Beden, elbise ve yeri temizlemek"),
        ("3. Setr-i Avret", "Örtülmesi gereken bölgeleri örtmek"),
        ("4. İstikbal-i Kıble", "Mekke'deki Kâbe yönüne dönmek"),
        ("5. Vakit", "Namazın kendi vaktinin girmesi"),
        ("6. Niyet", "Kılınacak namaza kalben niyet etmek"),
    ]
    for i, (ad, ac) in enumerate(sartlar):
        sy = 57 + i * 22
        _kutu(svg, 16, sy, kw - 12, 19, dolgu=PALET["beyaz"], kenar=PALET["turuncu"], r=3)
        _yazi(svg, 22, sy + 13, ad, boyut=7.0, renk=PALET["koyu_kirm"], bold=True, anchor="start")
        _yazi(svg, 112, sy + 13, f": {ac}", boyut=6.7, renk=PALET["koyu"], anchor="start")

    rx = 20 + kw
    _kutu(svg, rx, 33, kw, h - 40, dolgu=PALET["acik_yes"], kenar=PALET["yesil"], r=6, kalinlik=1.5)
    _kutu(svg, rx, 33, kw, 19, dolgu=PALET["yesil"], kenar=PALET["yesil"], r=5)
    _yazi(svg, rx + kw / 2, 46, "NAMAZIN İÇİNDEKİ FARZLAR (6 RÜKÜN)", boyut=7.6, renk=PALET["beyaz"], bold=True)

    rukunler = [
        ("1. İftitah Tekbiri", "'Allâhü ekber' diyerek başlamak"),
        ("2. Kıyam", "Namazda ayakta durmak"),
        ("3. Kıraat", "Ayaktayken Kur'an'dan ayet okumak"),
        ("4. Rükû", "Elleri dizlere koyup düz eğilmek"),
        ("5. Sücûd (Secde)", "Alın, burun, el ve dizle kapanmak"),
        ("6. Ka'de-i Âhire", "Sonunda teşehhüd miktarı oturmak"),
    ]
    for i, (ad, ac) in enumerate(rukunler):
        sy = 57 + i * 22
        _kutu(svg, rx + 6, sy, kw - 12, 19, dolgu=PALET["beyaz"], kenar=PALET["yesil"], r=3)
        _yazi(svg, rx + 12, sy + 13, ad, boyut=7.0, renk=PALET["koyu_yes"], bold=True, anchor="start")
        _yazi(svg, rx + 98, sy + 13, f": {ac}", boyut=6.7, renk=PALET["koyu"], anchor="start")
    return svg


GORSELLER = {"g1": _g1, "g2": _g2, "g3": _g3}


def uret(gorsel_id: str, genislik: float = 515, yukseklik: float = 200) -> str:
    fn = GORSELLER.get(gorsel_id)
    if fn is None:
        raise ValueError(f"Bilinen görsel yok: {gorsel_id}")
    svg = fn(float(genislik), float(yukseklik))
    return ET.tostring(svg, encoding="unicode")

SVGS = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1e8449" stroke="#1e8449" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.5" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">KUR\'AN VE SÜNNETTE NAMAZ (SALÂT) İBADETİNİN ÖNEMİ</text><rect x="185.5" y="79" width="144" height="52" rx="10" ry="10" fill="#27ae60" stroke="#1e8449" stroke-width="1.8" /><text x="257.5" y="97" font-family="DejaVu Sans, Arial, sans-serif" font-size="9" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">SALÂT (NAMAZ)</text><text x="257.5" y="111" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#fef9e7" text-anchor="middle" font-weight="normal" font-style="normal">Tekbirle başlayıp selamla</text><text x="257.5" y="122" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#fef9e7" text-anchor="middle" font-weight="bold" font-style="normal">biten farz-ı ayın ibadet</text><rect x="12" y="36" width="150" height="66" rx="5" ry="5" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.3" /><rect x="12" y="36" width="150" height="17" rx="4" ry="4" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="87" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">MİRAÇ HEDİYESİ</text><text x="87" y="66" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Hicretten önce Miraç</text><text x="87" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">gecesinde doğrudan Allah</text><text x="87" y="90" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">tarafından farz kılındı.</text><rect x="353" y="36" width="150" height="66" rx="5" ry="5" fill="#fdebd0" stroke="#e67e22" stroke-width="1.3" /><rect x="353" y="36" width="150" height="17" rx="4" ry="4" fill="#e67e22" stroke="#e67e22" stroke-width="1.3" /><text x="428" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">KUR\'AN\'DA NAMAZ</text><text x="428" y="66" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Bakara 43 &amp; Ankebût 45:</text><text x="428" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">\'Namazı dosdoğru kılın,</text><text x="428" y="90" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">zekâtı verin.\'</text><rect x="12" y="122" width="150" height="66" rx="5" ry="5" fill="#ebdef0" stroke="#8e44ad" stroke-width="1.3" /><rect x="12" y="122" width="150" height="17" rx="4" ry="4" fill="#8e44ad" stroke="#8e44ad" stroke-width="1.3" /><text x="87" y="134" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">HADİSLERDE KONUMU</text><text x="87" y="152" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">\'Namaz dinin direğidir.\'</text><text x="87" y="164" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">\'Namaz müminin miracı</text><text x="87" y="176" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ve gözümün nurudur.\'</text><rect x="353" y="122" width="150" height="66" rx="5" ry="5" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.3" /><rect x="353" y="122" width="150" height="17" rx="4" ry="4" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="428" y="134" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">AHİRETTE İLK HESAP</text><text x="428" y="152" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Kıyamet gününde kulun</text><text x="428" y="164" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ilk hesaba çekileceği</text><text x="428" y="176" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ameli namazdır.</text><line x1="162" y1="69" x2="185.5" y2="95" stroke="#2980b9" stroke-width="1.4" stroke-linecap="round" marker-end="url(#ok-mavi)" /><line x1="353" y1="69" x2="329.5" y2="95" stroke="#e67e22" stroke-width="1.4" stroke-linecap="round" marker-end="url(#ok-turuncu)" /><line x1="162" y1="155" x2="185.5" y2="115" stroke="#8e44ad" stroke-width="1.4" stroke-linecap="round" marker-end="url(#ok-mor)" /><line x1="353" y1="155" x2="329.5" y2="115" stroke="#e74c3c" stroke-width="1.4" stroke-linecap="round" marker-end="url(#ok-kirmizi)" /></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1a5276" stroke="#1a5276" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.5" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">NAMAZ İBADETİNİN BİREYSEL VE TOPLUMSAL HİKMETLERİ</text><rect x="10" y="34" width="242.5" height="158" rx="6" ry="6" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.5" /><rect x="10" y="34" width="242.5" height="20" rx="5" ry="5" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="131.25" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.8" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BİREYSEL VE AHLAKİ HİKMETLERİ</text><rect x="18" y="60" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="131.25" y="71" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1e8449" text-anchor="middle" font-weight="bold" font-style="normal">Manevi Huzur ve Zikir</text><text x="131.25" y="82" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Günde 5 vakit Rabbiyle buluşarak kalp huzuru bulma</text><rect x="18" y="92" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="131.25" y="103" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1e8449" text-anchor="middle" font-weight="bold" font-style="normal">Ahlaki Kalkan (Ankebût 45)</text><text x="131.25" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Hayasızlıktan (fahşâ) ve kötülükten (münker) korunma</text><rect x="18" y="124" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="131.25" y="135" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1e8449" text-anchor="middle" font-weight="bold" font-style="normal">Temizlik Alışkanlığı</text><text x="131.25" y="146" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Abdest ve taharetle sürekli beden ve elbise temizliği</text><rect x="18" y="156" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="131.25" y="167" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1e8449" text-anchor="middle" font-weight="bold" font-style="normal">Zaman Bilinci ve Disiplin</text><text x="131.25" y="178" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Belirli vakitlerde ibadetle hayatı planlama disiplini</text><rect x="262.5" y="34" width="242.5" height="158" rx="6" ry="6" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.5" /><rect x="262.5" y="34" width="242.5" height="20" rx="5" ry="5" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="383.75" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.8" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">TOPLUMSAL VE SOSYAL HİKMETLERİ</text><rect x="270.5" y="60" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1a5276" stroke-width="1.3" /><text x="383.75" y="71" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1a5276" text-anchor="middle" font-weight="bold" font-style="normal">Eşitlik ve Tevazu</text><text x="383.75" y="82" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Aynı safta makam, servet ve statü farkı olmadan durma</text><rect x="270.5" y="92" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1a5276" stroke-width="1.3" /><text x="383.75" y="103" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1a5276" text-anchor="middle" font-weight="bold" font-style="normal">Kardeşlik ve Kaynaşma</text><text x="383.75" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Cemaat, cuma ve bayram namazlarıyla komşuluk bağı</text><rect x="270.5" y="124" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1a5276" stroke-width="1.3" /><text x="383.75" y="135" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1a5276" text-anchor="middle" font-weight="bold" font-style="normal">Yardımlaşma ve Dayanışma</text><text x="383.75" y="146" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Sevinç ve sıkıntıları paylaşarak sosyal yardımlaşma</text><rect x="270.5" y="156" width="226.5" height="27" rx="4" ry="4" fill="#ffffff" stroke="#1a5276" stroke-width="1.3" /><text x="383.75" y="167" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.3" fill="#1a5276" text-anchor="middle" font-weight="bold" font-style="normal">Ortak Ümmet Bilinci</text><text x="383.75" y="178" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Dünyanın her yerinde aynı kıbleye (Kâbe) yönelme</text></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#2c3e50" stroke="#2c3e50" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.3" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">NAMAZIN 12 FARZI: DIŞINDAKİ ŞARTLAR (6) VE İÇİNDEKİ RÜKÜNLER (6)</text><rect x="10" y="33" width="242.5" height="160" rx="6" ry="6" fill="#fdebd0" stroke="#e67e22" stroke-width="1.5" /><rect x="10" y="33" width="242.5" height="19" rx="5" ry="5" fill="#e67e22" stroke="#e67e22" stroke-width="1.3" /><text x="131.25" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">NAMAZIN DIŞINDAKİ FARZLAR (6 ŞART)</text><rect x="16" y="57" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="70" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">1. Hadesten Taharet</text><text x="112" y="70" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Abdest, gusül veya teyemmüm almak</text><rect x="16" y="79" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="92" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">2. Necasetten Taharet</text><text x="112" y="92" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Beden, elbise ve yeri temizlemek</text><rect x="16" y="101" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">3. Setr-i Avret</text><text x="112" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Örtülmesi gereken bölgeleri örtmek</text><rect x="16" y="123" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="136" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">4. İstikbal-i Kıble</text><text x="112" y="136" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Mekke\'deki Kâbe yönüne dönmek</text><rect x="16" y="145" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="158" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">5. Vakit</text><text x="112" y="158" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Namazın kendi vaktinin girmesi</text><rect x="16" y="167" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="22" y="180" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#c0392b" text-anchor="start" font-weight="bold" font-style="normal">6. Niyet</text><text x="112" y="180" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Kılınacak namaza kalben niyet etmek</text><rect x="262.5" y="33" width="242.5" height="160" rx="6" ry="6" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.5" /><rect x="262.5" y="33" width="242.5" height="19" rx="5" ry="5" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="383.75" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">NAMAZIN İÇİNDEKİ FARZLAR (6 RÜKÜN)</text><rect x="268.5" y="57" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="70" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">1. İftitah Tekbiri</text><text x="360.5" y="70" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: \'Allâhü ekber\' diyerek başlamak</text><rect x="268.5" y="79" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="92" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">2. Kıyam</text><text x="360.5" y="92" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Namazda ayakta durmak</text><rect x="268.5" y="101" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">3. Kıraat</text><text x="360.5" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Ayaktayken Kur\'an\'dan ayet okumak</text><rect x="268.5" y="123" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="136" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">4. Rükû</text><text x="360.5" y="136" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Elleri dizlere koyup düz eğilmek</text><rect x="268.5" y="145" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="158" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">5. Sücûd (Secde)</text><text x="360.5" y="158" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Alın, burun, el ve dizle kapanmak</text><rect x="268.5" y="167" width="230.5" height="19" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="274.5" y="180" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#1e8449" text-anchor="start" font-weight="bold" font-style="normal">6. Ka\'de-i Âhire</text><text x="360.5" y="180" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">: Sonunda teşehhüd miktarı oturmak</text></svg>']

def uygula(v):
    for i, b in enumerate(v.get('bolumler', [])):
        if i < len(SVGS):
            b['gorsel'] = SVGS[i]
