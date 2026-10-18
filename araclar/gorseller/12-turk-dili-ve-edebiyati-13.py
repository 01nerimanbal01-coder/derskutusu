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
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["mor"], kenar=PALET["mor"], r=5)
    _yazi(svg, w / 2, 20, "GARİP AKIMI (I. YENİ - 1941): GELENEKSEL ŞİİRDEN KOPUŞ BİLDİRİSİ", boyut=8.3, renk=PALET["beyaz"], bold=True)

    kw = (w - 34) / 2
    _kutu(svg, 10, 34, kw, h - 42, dolgu=PALET["acik_kirm"], kenar=PALET["kirmizi"], r=6, kalinlik=1.5)
    _kutu(svg, 10, 34, kw, 20, dolgu=PALET["kirmizi"], kenar=PALET["kirmizi"], r=5)
    _yazi(svg, 10 + kw / 2, 47, "REDDEDİLEN GELENEKSEL UNSURLAR", boyut=7.6, renk=PALET["beyaz"], bold=True)

    redler = [
        "• Hece ve aruz ölçüsü kalıpları",
        "• Uyak (kafiye) ve redif zorunluluğu",
        "• Dörtlük ve sabit nazım biçimleri",
        "• Şairanelik ve duygusal abartı",
        "• Teşbih, istiare, mecaz gibi sanatlar",
        "• Şiirin müzik ve resimle iç içe geçmesi",
    ]
    for i, r in enumerate(redler):
        _kutu(svg, 18, 60 + i * 21, kw - 16, 18, dolgu=PALET["beyaz"], kenar=PALET["koyu_kirm"], r=3)
        _yazi(svg, 25, 72 + i * 21, r, boyut=7.1, renk=PALET["koyu"], bold=True, anchor="start")

    rx = 24 + kw
    _kutu(svg, rx, 34, kw, h - 42, dolgu=PALET["acik_yes"], kenar=PALET["yesil"], r=6, kalinlik=1.5)
    _kutu(svg, rx, 34, kw, 20, dolgu=PALET["yesil"], kenar=PALET["yesil"], r=5)
    _yazi(svg, rx + kw / 2, 47, "BENİMSENEN YENİ ŞİİR İLKELERİ", boyut=7.6, renk=PALET["beyaz"], bold=True)

    kabuller = [
        "• Kuralsız ve engelsiz serbest şiir",
        "• Günlük konuşma dilinin doğallığı",
        "• Sıradan insan ('Süleyman Efendi')",
        "• Yaşama sevinci ve gündelik olaylar",
        "• İnce mizah, ironi ve şaşırtmaca (nükte)",
        "• Sürrealizm (bilinçaltı) ve dadaizm etkisi",
    ]
    for i, k in enumerate(kabuller):
        _kutu(svg, rx + 8, 60 + i * 21, kw - 16, 18, dolgu=PALET["beyaz"], kenar=PALET["koyu_yes"], r=3)
        _yazi(svg, rx + 15, 72 + i * 21, k, boyut=7.1, renk=PALET["koyu"], bold=True, anchor="start")
    return svg


def _g2(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_mavi"], kenar=PALET["koyu_mavi"], r=5)
    _yazi(svg, w / 2, 20, "GARİP AKIMININ ÜÇ TEMSİLCİSİ (OMO) VE EDEBİ YÖNELİMLERİ", boyut=8.3, renk=PALET["beyaz"], bold=True)

    sairler = [
        ("ORHAN VELİ KANIK", "(1914–1950)", PALET["kirmizi"], PALET["acik_kirm"],
         "Akımın kuramcısı;", "Garip çizgisini korudu.",
         ["• Garip (Önsöz, 1941)", "• Vazgeçemediğim", "• Destan Gibi, Yenisi", "• Karşı (Son eseri)", "• Kitabe-i Seng-i Mezar"]),
        ("MELİH CEVDET ANDAY", "(1915–2002)", PALET["mavi"], PALET["acik_mavi"],
         "Sonradan mitolojik ve", "felsefi şiire yöneldi.",
         ["• Rahatı Kaçan Ağaç", "• Telgrafhane, Yan Yana", "• Kolları Bağlı Odysseus", "• Teknenin Ölümü", "• Mikado'nun Çöpleri"]),
        ("OKTAY RİFAT HOROZCU", "(1914–1988)", PALET["mor"], PALET["acik_mor"],
         "Perçemli Sokak ile", "II. Yeni'ye yöneldi.",
         ["• Güzelleme", "• Karga ile Tilki", "• Perçemli Sokak (II. Yeni)", "• Elleri Var Özgürlüğün", "• Çobanıl Şiirler"]),
    ]
    kw = (w - 36) / 3
    for i, (ad, yil, renk, acik, o1, o2, eserler) in enumerate(sairler):
        kx = 10 + i * (kw + 8)
        _kutu(svg, kx, 34, kw, h - 42, dolgu=acik, kenar=renk, r=6, kalinlik=1.4)
        _kutu(svg, kx, 34, kw, 28, dolgu=renk, kenar=renk, r=5)
        _yazi(svg, kx + kw / 2, 46, ad, boyut=7.4, renk=PALET["beyaz"], bold=True)
        _yazi(svg, kx + kw / 2, 58, yil, boyut=6.8, renk=PALET["acik_sari"], bold=True)

        _kutu(svg, kx + 6, 66, kw - 12, 26, dolgu=PALET["beyaz"], kenar=renk, r=3)
        _yazi(svg, kx + kw / 2, 77, o1, boyut=6.9, renk=PALET["koyu"], bold=True)
        _yazi(svg, kx + kw / 2, 88, o2, boyut=6.9, renk=PALET["koyu"], italic=True)

        for j, es in enumerate(eserler):
            _yazi(svg, kx + 10, 108 + j * 15, es, boyut=6.9, renk=PALET["koyu"], bold=(j in (0, 2)), anchor="start")
    return svg


def _g3(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_yes"], kenar=PALET["koyu_yes"], r=5)
    _yazi(svg, w / 2, 20, "GARİP DIŞINDA YENİLİĞİ SÜRDÜREN BAĞIMSIZ ŞAİRLER", boyut=8.5, renk=PALET["beyaz"], bold=True)

    bagimsizlar = [
        ("FAZIL HÜSNÜ DAĞLARCA", "Türk Şiirinin Ulu Çınarı", PALET["turuncu"], PALET["acik_tur"],
         "'Türkçem, benim ses", "bayrağım!' (Sezgi + Destan)",
         "• Havaya Çizilen Dünya", "• Çocuk ve Allah", "• Üç Şehitler Destanı"),
        ("BEHÇET NECATİGİL", "Evler Şairi", PALET["mavi"], PALET["acik_mavi"],
         "Orta halli aile yaşamı,", "tevriye ve cinas sanatı",
         "• Kapalı Çarşı, Çevre", "• Evler, Eski Toprak", "• Sevgilerde, Bile/Yazdı"),
        ("CAHİT KÜLEBİ", "Romantik Gerçekçi", PALET["yesil"], PALET["acik_yes"],
         "Karacaoğlan içtenliğiyle", "Anadolu ve memleket",
         "• Adamın Biri, Rüzgâr", "• Yeşeren Otlar, Süt", "• Atatürk Kurtuluş Savaşı'nda"),
        ("DİĞER BAĞIMSIZLAR", "Özgün Sesler", PALET["mor"], PALET["acik_mor"],
         "Soyut-mistik ve özdeyiş", "odaklı modern şiir",
         "• Asaf Halet: He, Lamelif", "• Özdemir Asaf: Lavinia", "• S. K. Aksal: Şarkılı Kahve"),
    ]
    kw = (w - 42) / 4
    for i, (ad, unvan, renk, acik, s1, s2, e1, e2, e3) in enumerate(bagimsizlar):
        kx = 10 + i * (kw + 7.3)
        _kutu(svg, kx, 34, kw, h - 42, dolgu=acik, kenar=renk, r=5, kalinlik=1.3)
        _kutu(svg, kx, 34, kw, 28, dolgu=renk, kenar=renk, r=4)
        _yazi(svg, kx + kw / 2, 46, ad, boyut=6.7, renk=PALET["beyaz"], bold=True)
        _yazi(svg, kx + kw / 2, 58, unvan, boyut=6.5, renk=PALET["sari"], bold=True)

        _kutu(svg, kx + 5, 67, kw - 10, 26, dolgu=PALET["beyaz"], kenar=renk, r=3)
        _yazi(svg, kx + kw / 2, 78, s1, boyut=6.5, renk=PALET["koyu"], bold=True)
        _yazi(svg, kx + kw / 2, 89, s2, boyut=6.5, renk=PALET["koyu"])

        _yazi(svg, kx + 7, 112, e1, boyut=6.5, renk=PALET["koyu"], bold=True, anchor="start")
        _yazi(svg, kx + 7, 128, e2, boyut=6.5, renk=PALET["koyu"], bold=True, anchor="start")
        _yazi(svg, kx + 7, 144, e3, boyut=6.5, renk=PALET["koyu"], bold=True, anchor="start")
    return svg


GORSELLER = {"g1": _g1, "g2": _g2, "g3": _g3}


def uret(gorsel_id: str, genislik: float = 515, yukseklik: float = 200) -> str:
    fn = GORSELLER.get(gorsel_id)
    if fn is None:
        raise ValueError(f"Bilinen görsel yok: {gorsel_id}")
    svg = fn(float(genislik), float(yukseklik))
    return ET.tostring(svg, encoding="unicode")

SVGS = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#8e44ad" stroke="#8e44ad" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.3" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">GARİP AKIMI (I. YENİ - 1941): GELENEKSEL ŞİİRDEN KOPUŞ BİLDİRİSİ</text><rect x="10" y="34" width="240.5" height="158" rx="6" ry="6" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.5" /><rect x="10" y="34" width="240.5" height="20" rx="5" ry="5" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="130.25" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">REDDEDİLEN GELENEKSEL UNSURLAR</text><rect x="18" y="60" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="72" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Hece ve aruz ölçüsü kalıpları</text><rect x="18" y="81" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Uyak (kafiye) ve redif zorunluluğu</text><rect x="18" y="102" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Dörtlük ve sabit nazım biçimleri</text><rect x="18" y="123" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="135" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Şairanelik ve duygusal abartı</text><rect x="18" y="144" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="156" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Teşbih, istiare, mecaz gibi sanatlar</text><rect x="18" y="165" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="25" y="177" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Şiirin müzik ve resimle iç içe geçmesi</text><rect x="264.5" y="34" width="240.5" height="158" rx="6" ry="6" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.5" /><rect x="264.5" y="34" width="240.5" height="20" rx="5" ry="5" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="384.75" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BENİMSENEN YENİ ŞİİR İLKELERİ</text><rect x="272.5" y="60" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="72" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Kuralsız ve engelsiz serbest şiir</text><rect x="272.5" y="81" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Günlük konuşma dilinin doğallığı</text><rect x="272.5" y="102" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="114" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Sıradan insan (\'Süleyman Efendi\')</text><rect x="272.5" y="123" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="135" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Yaşama sevinci ve gündelik olaylar</text><rect x="272.5" y="144" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="156" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• İnce mizah, ironi ve şaşırtmaca (nükte)</text><rect x="272.5" y="165" width="224.5" height="18" rx="3" ry="3" fill="#ffffff" stroke="#1e8449" stroke-width="1.3" /><text x="279.5" y="177" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Sürrealizm (bilinçaltı) ve dadaizm etkisi</text></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1a5276" stroke="#1a5276" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.3" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">GARİP AKIMININ ÜÇ TEMSİLCİSİ (OMO) VE EDEBİ YÖNELİMLERİ</text><rect x="10" y="34" width="159.667" height="158" rx="6" ry="6" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.4" /><rect x="10" y="34" width="159.667" height="28" rx="5" ry="5" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="89.8333" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">ORHAN VELİ KANIK</text><text x="89.8333" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#fef9e7" text-anchor="middle" font-weight="bold" font-style="normal">(1914–1950)</text><rect x="16" y="66" width="147.667" height="26" rx="3" ry="3" fill="#ffffff" stroke="#e74c3c" stroke-width="1.3" /><text x="89.8333" y="77" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Akımın kuramcısı;</text><text x="89.8333" y="88" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="italic">Garip çizgisini korudu.</text><text x="20" y="108" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Garip (Önsöz, 1941)</text><text x="20" y="123" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Vazgeçemediğim</text><text x="20" y="138" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Destan Gibi, Yenisi</text><text x="20" y="153" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Karşı (Son eseri)</text><text x="20" y="168" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Kitabe-i Seng-i Mezar</text><rect x="177.667" y="34" width="159.667" height="158" rx="6" ry="6" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.4" /><rect x="177.667" y="34" width="159.667" height="28" rx="5" ry="5" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="257.5" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">MELİH CEVDET ANDAY</text><text x="257.5" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#fef9e7" text-anchor="middle" font-weight="bold" font-style="normal">(1915–2002)</text><rect x="183.667" y="66" width="147.667" height="26" rx="3" ry="3" fill="#ffffff" stroke="#2980b9" stroke-width="1.3" /><text x="257.5" y="77" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Sonradan mitolojik ve</text><text x="257.5" y="88" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="italic">felsefi şiire yöneldi.</text><text x="187.667" y="108" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Rahatı Kaçan Ağaç</text><text x="187.667" y="123" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Telgrafhane, Yan Yana</text><text x="187.667" y="138" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Kolları Bağlı Odysseus</text><text x="187.667" y="153" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Teknenin Ölümü</text><text x="187.667" y="168" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Mikado\'nun Çöpleri</text><rect x="345.333" y="34" width="159.667" height="158" rx="6" ry="6" fill="#ebdef0" stroke="#8e44ad" stroke-width="1.4" /><rect x="345.333" y="34" width="159.667" height="28" rx="5" ry="5" fill="#8e44ad" stroke="#8e44ad" stroke-width="1.3" /><text x="425.167" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">OKTAY RİFAT HOROZCU</text><text x="425.167" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#fef9e7" text-anchor="middle" font-weight="bold" font-style="normal">(1914–1988)</text><rect x="351.333" y="66" width="147.667" height="26" rx="3" ry="3" fill="#ffffff" stroke="#8e44ad" stroke-width="1.3" /><text x="425.167" y="77" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Perçemli Sokak ile</text><text x="425.167" y="88" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="italic">II. Yeni\'ye yöneldi.</text><text x="355.333" y="108" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Güzelleme</text><text x="355.333" y="123" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Karga ile Tilki</text><text x="355.333" y="138" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Perçemli Sokak (II. Yeni)</text><text x="355.333" y="153" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Elleri Var Özgürlüğün</text><text x="355.333" y="168" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• Çobanıl Şiirler</text></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1e8449" stroke="#1e8449" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.5" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">GARİP DIŞINDA YENİLİĞİ SÜRDÜREN BAĞIMSIZ ŞAİRLER</text><rect x="10" y="34" width="118.25" height="158" rx="5" ry="5" fill="#fdebd0" stroke="#e67e22" stroke-width="1.3" /><rect x="10" y="34" width="118.25" height="28" rx="4" ry="4" fill="#e67e22" stroke="#e67e22" stroke-width="1.3" /><text x="69.125" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">FAZIL HÜSNÜ DAĞLARCA</text><text x="69.125" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">Türk Şiirinin Ulu Çınarı</text><rect x="15" y="67" width="108.25" height="26" rx="3" ry="3" fill="#ffffff" stroke="#e67e22" stroke-width="1.3" /><text x="69.125" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">\'Türkçem, benim ses</text><text x="69.125" y="89" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">bayrağım!\' (Sezgi + Destan)</text><text x="17" y="112" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Havaya Çizilen Dünya</text><text x="17" y="128" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Çocuk ve Allah</text><text x="17" y="144" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Üç Şehitler Destanı</text><rect x="135.55" y="34" width="118.25" height="158" rx="5" ry="5" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.3" /><rect x="135.55" y="34" width="118.25" height="28" rx="4" ry="4" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="194.675" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BEHÇET NECATİGİL</text><text x="194.675" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">Evler Şairi</text><rect x="140.55" y="67" width="108.25" height="26" rx="3" ry="3" fill="#ffffff" stroke="#2980b9" stroke-width="1.3" /><text x="194.675" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Orta halli aile yaşamı,</text><text x="194.675" y="89" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">tevriye ve cinas sanatı</text><text x="142.55" y="112" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Kapalı Çarşı, Çevre</text><text x="142.55" y="128" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Evler, Eski Toprak</text><text x="142.55" y="144" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Sevgilerde, Bile/Yazdı</text><rect x="261.1" y="34" width="118.25" height="158" rx="5" ry="5" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.3" /><rect x="261.1" y="34" width="118.25" height="28" rx="4" ry="4" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="320.225" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">CAHİT KÜLEBİ</text><text x="320.225" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">Romantik Gerçekçi</text><rect x="266.1" y="67" width="108.25" height="26" rx="3" ry="3" fill="#ffffff" stroke="#27ae60" stroke-width="1.3" /><text x="320.225" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Karacaoğlan içtenliğiyle</text><text x="320.225" y="89" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Anadolu ve memleket</text><text x="268.1" y="112" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Adamın Biri, Rüzgâr</text><text x="268.1" y="128" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Yeşeren Otlar, Süt</text><text x="268.1" y="144" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Atatürk Kurtuluş Savaşı\'nda</text><rect x="386.65" y="34" width="118.25" height="158" rx="5" ry="5" fill="#ebdef0" stroke="#8e44ad" stroke-width="1.3" /><rect x="386.65" y="34" width="118.25" height="28" rx="4" ry="4" fill="#8e44ad" stroke="#8e44ad" stroke-width="1.3" /><text x="445.775" y="46" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.7" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">DİĞER BAĞIMSIZLAR</text><text x="445.775" y="58" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">Özgün Sesler</text><rect x="391.65" y="67" width="108.25" height="26" rx="3" ry="3" fill="#ffffff" stroke="#8e44ad" stroke-width="1.3" /><text x="445.775" y="78" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Soyut-mistik ve özdeyiş</text><text x="445.775" y="89" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">odaklı modern şiir</text><text x="393.65" y="112" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Asaf Halet: He, Lamelif</text><text x="393.65" y="128" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Özdemir Asaf: Lavinia</text><text x="393.65" y="144" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.5" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• S. K. Aksal: Şarkılı Kahve</text></svg>']

def uygula(v):
    for i, b in enumerate(v.get('bolumler', [])):
        if i < len(SVGS):
            b['gorsel'] = SVGS[i]
