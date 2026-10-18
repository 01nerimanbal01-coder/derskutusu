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
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_kirm"], kenar=PALET["koyu_kirm"], r=5)
    _yazi(svg, w / 2, 20, "BAŞKOMUTANLIK KANUNU VE TEKÂLİF-İ MİLLİYE EMİRLERİ (AĞUSTOS 1921)", boyut=8.5, renk=PALET["beyaz"], bold=True)

    _kutu(svg, 16, 35, w - 32, 34, dolgu=PALET["acik_kirm"], kenar=PALET["kirmizi"], r=5, kalinlik=1.5)
    _yazi(svg, w / 2, 48, "5 AĞUSTOS 1921 — BAŞKOMUTANLIK KANUNU", boyut=8.2, renk=PALET["koyu_kirm"], bold=True)
    _yazi(svg, w / 2, 61, "TBMM yetkilerinin 3 ay süreyle Mustafa Kemal Paşa'ya devredilmesi (Hızlı ve merkezî karar)", boyut=7.4, renk=PALET["koyu"])

    _cizgi(svg, w / 2, 69, w / 2, 82, renk=PALET["kirmizi"], kalinlik=1.8, ok="kirmizi")
    _kutu(svg, w / 2 - 135, 82, 270, 20, dolgu=PALET["koyu"], kenar=PALET["koyu"], r=4)
    _yazi(svg, w / 2, 95, "7–8 AĞUSTOS 1921 — TEKÂLİF-İ MİLLİYE EMİRLERİ", boyut=8.0, renk=PALET["sari"], bold=True)

    kartlar = [
        ("GİYECEK", PALET["mavi"], PALET["acik_mavi"],
         "Her haneden 1 kat", "çamaşır, 1 çift çorap", "ve çarık teslimi"),
        ("GIDA VE MALZEME", PALET["yesil"], PALET["acik_yes"],
         "Un, buğday, arpa,", "şeker, bez, kösele", "stoklarının %40'ı"),
        ("SİLAH VE CEPHANE", PALET["kirmizi"], PALET["acik_kirm"],
         "Halkın elindeki silah", "ve cephanenin 3 gün", "içinde teslimi"),
        ("ULAŞIM VE ZANAAT", PALET["mor"], PALET["acik_mor"],
         "Ayda 1 kez 100 km", "ücretsiz nakliyat;", "demirci ve dökümcüler"),
    ]
    kw = (w - 42) / 4
    for i, (bas, renk, acik, s1, s2, s3) in enumerate(kartlar):
        kx = 12 + i * (kw + 6)
        _cizgi(svg, w / 2, 102, kx + kw / 2, 114, renk=renk, kalinlik=1.2, ok="koyu")
        _kutu(svg, kx, 115, kw, h - 147, dolgu=acik, kenar=renk, r=5, kalinlik=1.3)
        _kutu(svg, kx, 115, kw, 18, dolgu=renk, kenar=renk, r=4)
        _yazi(svg, kx + kw / 2, 127, bas, boyut=7.2, renk=PALET["beyaz"], bold=True)
        _yazi(svg, kx + kw / 2, 145, s1, boyut=7.0, renk=PALET["koyu"], bold=True)
        _yazi(svg, kx + kw / 2, 157, s2, boyut=7.0, renk=PALET["koyu"])
        _yazi(svg, kx + kw / 2, 169, s3, boyut=7.0, renk=PALET["koyu"])

    _kutu(svg, 12, h - 26, w - 24, 20, dolgu=PALET["acik_sari"], kenar=PALET["turuncu"], r=4)
    _yazi(svg, w / 2, h - 13, "Topyekûn Seferberlik: Her ilçede Tekâlif-i Milliye Komisyonları ve İstiklal Mahkemeleri görevlendirildi.", boyut=7.4, renk=PALET["koyu"], bold=True)
    return svg


def _g2(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_mavi"], kenar=PALET["koyu_mavi"], r=5)
    _yazi(svg, w / 2, 20, "SAKARYA MEYDAN MUHAREBESİ (23 AĞUSTOS – 13 EYLÜL 1921) VE SONUÇLARI", boyut=8.2, renk=PALET["beyaz"], bold=True)

    lw = w * 0.43 - 12
    _kutu(svg, 10, 34, lw, h - 42, dolgu=PALET["acik_kirm"], kenar=PALET["kirmizi"], r=6, kalinlik=1.5)
    _kutu(svg, 10, 34, lw, 20, dolgu=PALET["kirmizi"], kenar=PALET["kirmizi"], r=5)
    _yazi(svg, 10 + lw / 2, 47, "ASKERÎ STRATEJİ VE ÖZELLİKLER", boyut=7.8, renk=PALET["beyaz"], bold=True)

    _kutu(svg, 18, 60, lw - 16, 42, dolgu=PALET["beyaz"], kenar=PALET["koyu_kirm"], r=4)
    _yazi(svg, 10 + lw / 2, 73, "'Hattı müdafaa yoktur,", boyut=7.6, renk=PALET["koyu_kirm"], bold=True, italic=True)
    _yazi(svg, 10 + lw / 2, 84, "sathı müdafaa vardır.", boyut=7.6, renk=PALET["koyu_kirm"], bold=True, italic=True)
    _yazi(svg, 10 + lw / 2, 95, "O satıh bütün vatandır!'", boyut=7.6, renk=PALET["koyu_kirm"], bold=True, italic=True)

    maddeler = [
        "• 22 gün 22 gece aralıksız çarpışma",
        "• Subaylar Savaşı / Melhame-i Kübra",
        "• 1683 II. Viyana'dan beri süren",
        "  geri çekilişin sona ermesi",
        "• 19 Eylül 1921: Mareşallik ve Gazilik",
    ]
    for i, m in enumerate(maddeler):
        _yazi(svg, 20, 116 + i * 13, m, boyut=7.1, renk=PALET["koyu"], bold=(i in (1, 4)), anchor="start")

    rx = 18 + lw
    rw = w - rx - 10
    _cizgi(svg, 10 + lw, h / 2 + 10, rx, h / 2 + 10, renk=PALET["koyu"], kalinlik=1.8, ok="koyu")
    _kutu(svg, rx, 34, rw, h - 42, dolgu=PALET["acik_mavi"], kenar=PALET["mavi"], r=6, kalinlik=1.5)
    _kutu(svg, rx, 34, rw, 20, dolgu=PALET["mavi"], kenar=PALET["mavi"], r=5)
    _yazi(svg, rx + rw / 2, 47, "DİPLOMATİK VE SİYASİ KAZANIMLAR", boyut=7.8, renk=PALET["beyaz"], bold=True)

    sonuclar = [
        ("13 Ekim 1921 — KARS ANTLAŞMASI", "Azerbaycan, Ermenistan ve Gürcistan ile imzalandı; Doğu sınırımız kesinleşti.", PALET["yesil"], PALET["acik_yes"]),
        ("20 Ekim 1921 — ANKARA ANTLAŞMASI", "Fransa TBMM'yi tanıyan ilk İtilaf Devleti oldu; Güney Cephesi kapandı (Hatay hariç).", PALET["turuncu"], PALET["acik_tur"]),
        ("İTALYA VE İNGİLTERE İLE İLİŞKİLER", "İtalya Anadolu'yu tamamen boşalttı; İngiltere ile Malta esir değişimi yapıldı.", PALET["mor"], PALET["acik_mor"]),
    ]
    for i, (bas, acik, renk, bg) in enumerate(sonuclar):
        sy = 60 + i * 42
        _kutu(svg, rx + 8, sy, rw - 16, 36, dolgu=bg, kenar=renk, r=4, kalinlik=1.2)
        _yazi(svg, rx + rw / 2, sy + 13, bas, boyut=7.4, renk=renk, bold=True)
        _yazi(svg, rx + rw / 2, sy + 27, acik, boyut=6.8, renk=PALET["koyu"])
    return svg


def _g3(w: float, h: float) -> ET.Element:
    svg = _svg_kok(w, h)
    _kutu(svg, 6, 6, w - 12, 22, dolgu=PALET["koyu_yes"], kenar=PALET["koyu_yes"], r=5)
    _yazi(svg, w / 2, 20, "BÜYÜK TAARRUZ'DAN MUDANYA ATEŞKES ANTLAŞMASI'NA ZAFER SÜRECİ (1922)", boyut=8.2, renk=PALET["beyaz"], bold=True)

    adimlar = [
        ("26 AĞUSTOS 1922", "BÜYÜK TAARRUZ", PALET["kirmizi"], PALET["acik_kirm"],
         "Afyon Kocatepe'den", "topçu ateşiyle taarruz", "harekâtı başladı."),
        ("30 AĞUSTOS 1922", "BAŞKOMUTANLIK", PALET["turuncu"], PALET["acik_tur"],
         "Dumlupınar'da Yunan", "ordusu imha edildi;", "hedef Akdeniz gösterildi."),
        ("9–18 EYLÜL 1922", "KURTULUŞ", PALET["mavi"], PALET["acik_mavi"],
         "9 Eylül'de İzmir, 18", "Eylül'de tüm Batı", "Anadolu kurtarıldı."),
        ("11 EKİM 1922", "MUDANYA ATEŞKESİ", PALET["yesil"], PALET["acik_yes"],
         "İsmet Paşa imzaladı;", "Doğu Trakya ve İstanbul", "savaşsız kurtarıldı."),
    ]
    kw = (w - 48) / 4
    for i, (tar, bas, renk, acik, s1, s2, s3) in enumerate(adimlar):
        kx = 10 + i * (kw + 9)
        _kutu(svg, kx, 36, kw, 98, dolgu=acik, kenar=renk, r=5, kalinlik=1.4)
        _kutu(svg, kx, 36, kw, 28, dolgu=renk, kenar=renk, r=4)
        _yazi(svg, kx + kw / 2, 48, tar, boyut=6.9, renk=PALET["sari"], bold=True)
        _yazi(svg, kx + kw / 2, 60, bas, boyut=7.2, renk=PALET["beyaz"], bold=True)
        _yazi(svg, kx + kw / 2, 80, s1, boyut=7.0, renk=PALET["koyu"], bold=True)
        _yazi(svg, kx + kw / 2, 93, s2, boyut=7.0, renk=PALET["koyu"])
        _yazi(svg, kx + kw / 2, 106, s3, boyut=7.0, renk=PALET["koyu"])
        if i < 3:
            _cizgi(svg, kx + kw + 1, 85, kx + kw + 8, 85, renk=PALET["koyu"], kalinlik=1.6, ok="koyu")

    _kutu(svg, 10, 142, w - 20, h - 150, dolgu=PALET["acik_sari"], kenar=PALET["turuncu"], r=5, kalinlik=1.4)
    _yazi(svg, w / 2, 156, "MUDANYA ATEŞKES ANTLAŞMASI'NIN (11 EKİM 1922) TARİHİ ÖNEMİ", boyut=7.8, renk=PALET["koyu_kirm"], bold=True)
    _yazi(svg, w / 2, 170, "• Yunan ordusu Meriç Nehri'nin batısına çekildi; Doğu Trakya 15 gün içinde TBMM'ye (Refet Bele) teslim edildi.", boyut=7.1, renk=PALET["koyu"])
    _yazi(svg, w / 2, 183, "• İstanbul ve Boğazların yönetimi TBMM Hükûmeti'ne bırakılarak Osmanlı Devleti HUKUKEN sona erdi.", boyut=7.1, renk=PALET["koyu"], bold=True)
    return svg


GORSELLER = {"g1": _g1, "g2": _g2, "g3": _g3}


def uret(gorsel_id: str, genislik: float = 515, yukseklik: float = 200) -> str:
    fn = GORSELLER.get(gorsel_id)
    if fn is None:
        raise ValueError(f"Bilinen görsel yok: {gorsel_id}")
    svg = fn(float(genislik), float(yukseklik))
    return ET.tostring(svg, encoding="unicode")

SVGS = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#c0392b" stroke="#c0392b" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.5" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BAŞKOMUTANLIK KANUNU VE TEKÂLİF-İ MİLLİYE EMİRLERİ (AĞUSTOS 1921)</text><rect x="16" y="35" width="483" height="34" rx="5" ry="5" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.5" /><text x="257.5" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.2" fill="#c0392b" text-anchor="middle" font-weight="bold" font-style="normal">5 AĞUSTOS 1921 — BAŞKOMUTANLIK KANUNU</text><text x="257.5" y="61" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">TBMM yetkilerinin 3 ay süreyle Mustafa Kemal Paşa\'ya devredilmesi (Hızlı ve merkezî karar)</text><line x1="257.5" y1="69" x2="257.5" y2="82" stroke="#e74c3c" stroke-width="1.8" stroke-linecap="round" marker-end="url(#ok-kirmizi)" /><rect x="122.5" y="82" width="270" height="20" rx="4" ry="4" fill="#2c3e50" stroke="#2c3e50" stroke-width="1.3" /><text x="257.5" y="95" font-family="DejaVu Sans, Arial, sans-serif" font-size="8" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">7–8 AĞUSTOS 1921 — TEKÂLİF-İ MİLLİYE EMİRLERİ</text><line x1="257.5" y1="102" x2="71.125" y2="114" stroke="#2980b9" stroke-width="1.2" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="12" y="115" width="118.25" height="53" rx="5" ry="5" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.3" /><rect x="12" y="115" width="118.25" height="18" rx="4" ry="4" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="71.125" y="127" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">GİYECEK</text><text x="71.125" y="145" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Her haneden 1 kat</text><text x="71.125" y="157" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">çamaşır, 1 çift çorap</text><text x="71.125" y="169" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ve çarık teslimi</text><line x1="257.5" y1="102" x2="195.375" y2="114" stroke="#27ae60" stroke-width="1.2" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="136.25" y="115" width="118.25" height="53" rx="5" ry="5" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.3" /><rect x="136.25" y="115" width="118.25" height="18" rx="4" ry="4" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="195.375" y="127" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">GIDA VE MALZEME</text><text x="195.375" y="145" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Un, buğday, arpa,</text><text x="195.375" y="157" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">şeker, bez, kösele</text><text x="195.375" y="169" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">stoklarının %40\'ı</text><line x1="257.5" y1="102" x2="319.625" y2="114" stroke="#e74c3c" stroke-width="1.2" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="260.5" y="115" width="118.25" height="53" rx="5" ry="5" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.3" /><rect x="260.5" y="115" width="118.25" height="18" rx="4" ry="4" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="319.625" y="127" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">SİLAH VE CEPHANE</text><text x="319.625" y="145" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Halkın elindeki silah</text><text x="319.625" y="157" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ve cephanenin 3 gün</text><text x="319.625" y="169" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">içinde teslimi</text><line x1="257.5" y1="102" x2="443.875" y2="114" stroke="#8e44ad" stroke-width="1.2" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="384.75" y="115" width="118.25" height="53" rx="5" ry="5" fill="#ebdef0" stroke="#8e44ad" stroke-width="1.3" /><rect x="384.75" y="115" width="118.25" height="18" rx="4" ry="4" fill="#8e44ad" stroke="#8e44ad" stroke-width="1.3" /><text x="443.875" y="127" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">ULAŞIM VE ZANAAT</text><text x="443.875" y="145" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Ayda 1 kez 100 km</text><text x="443.875" y="157" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ücretsiz nakliyat;</text><text x="443.875" y="169" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">demirci ve dökümcüler</text><rect x="12" y="174" width="491" height="20" rx="4" ry="4" fill="#fef9e7" stroke="#e67e22" stroke-width="1.3" /><text x="257.5" y="187" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Topyekûn Seferberlik: Her ilçede Tekâlif-i Milliye Komisyonları ve İstiklal Mahkemeleri görevlendirildi.</text></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1a5276" stroke="#1a5276" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">SAKARYA MEYDAN MUHAREBESİ (23 AĞUSTOS – 13 EYLÜL 1921) VE SONUÇLARI</text><rect x="10" y="34" width="209.45" height="158" rx="6" ry="6" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.5" /><rect x="10" y="34" width="209.45" height="20" rx="5" ry="5" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="114.725" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.8" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">ASKERÎ STRATEJİ VE ÖZELLİKLER</text><rect x="18" y="60" width="193.45" height="42" rx="4" ry="4" fill="#ffffff" stroke="#c0392b" stroke-width="1.3" /><text x="114.725" y="73" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#c0392b" text-anchor="middle" font-weight="bold" font-style="italic">\'Hattı müdafaa yoktur,</text><text x="114.725" y="84" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#c0392b" text-anchor="middle" font-weight="bold" font-style="italic">sathı müdafaa vardır.</text><text x="114.725" y="95" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.6" fill="#c0392b" text-anchor="middle" font-weight="bold" font-style="italic">O satıh bütün vatandır!\'</text><text x="20" y="116" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• 22 gün 22 gece aralıksız çarpışma</text><text x="20" y="129" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• Subaylar Savaşı / Melhame-i Kübra</text><text x="20" y="142" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">• 1683 II. Viyana\'dan beri süren</text><text x="20" y="155" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="normal" font-style="normal">  geri çekilişin sona ermesi</text><text x="20" y="168" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="start" font-weight="bold" font-style="normal">• 19 Eylül 1921: Mareşallik ve Gazilik</text><line x1="219.45" y1="110" x2="227.45" y2="110" stroke="#2c3e50" stroke-width="1.8" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="227.45" y="34" width="277.55" height="158" rx="6" ry="6" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.5" /><rect x="227.45" y="34" width="277.55" height="20" rx="5" ry="5" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="366.225" y="47" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.8" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">DİPLOMATİK VE SİYASİ KAZANIMLAR</text><rect x="235.45" y="60" width="261.55" height="36" rx="4" ry="4" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.2" /><text x="366.225" y="73" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#27ae60" text-anchor="middle" font-weight="bold" font-style="normal">13 Ekim 1921 — KARS ANTLAŞMASI</text><text x="366.225" y="87" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Azerbaycan, Ermenistan ve Gürcistan ile imzalandı; Doğu sınırımız kesinleşti.</text><rect x="235.45" y="102" width="261.55" height="36" rx="4" ry="4" fill="#fdebd0" stroke="#e67e22" stroke-width="1.2" /><text x="366.225" y="115" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#e67e22" text-anchor="middle" font-weight="bold" font-style="normal">20 Ekim 1921 — ANKARA ANTLAŞMASI</text><text x="366.225" y="129" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Fransa TBMM\'yi tanıyan ilk İtilaf Devleti oldu; Güney Cephesi kapandı (Hatay hariç).</text><rect x="235.45" y="144" width="261.55" height="36" rx="4" ry="4" fill="#ebdef0" stroke="#8e44ad" stroke-width="1.2" /><text x="366.225" y="157" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.4" fill="#8e44ad" text-anchor="middle" font-weight="bold" font-style="normal">İTALYA VE İNGİLTERE İLE İLİŞKİLER</text><text x="366.225" y="171" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.8" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">İtalya Anadolu\'yu tamamen boşalttı; İngiltere ile Malta esir değişimi yapıldı.</text></svg>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 515 200" width="100%" height="100%"><defs><marker id="ok-koyu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2c3e50" /></marker><marker id="ok-kirmizi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e74c3c" /></marker><marker id="ok-mavi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2980b9" /></marker><marker id="ok-yesil" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#27ae60" /></marker><marker id="ok-turuncu" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#e67e22" /></marker><marker id="ok-mor" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse"><path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#8e44ad" /></marker></defs><rect x="6" y="6" width="503" height="22" rx="5" ry="5" fill="#1e8449" stroke="#1e8449" stroke-width="1.3" /><text x="257.5" y="20" font-family="DejaVu Sans, Arial, sans-serif" font-size="8.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BÜYÜK TAARRUZ\'DAN MUDANYA ATEŞKES ANTLAŞMASI\'NA ZAFER SÜRECİ (1922)</text><rect x="10" y="36" width="116.75" height="98" rx="5" ry="5" fill="#fadbd8" stroke="#e74c3c" stroke-width="1.4" /><rect x="10" y="36" width="116.75" height="28" rx="4" ry="4" fill="#e74c3c" stroke="#e74c3c" stroke-width="1.3" /><text x="68.375" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">26 AĞUSTOS 1922</text><text x="68.375" y="60" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BÜYÜK TAARRUZ</text><text x="68.375" y="80" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Afyon Kocatepe\'den</text><text x="68.375" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">topçu ateşiyle taarruz</text><text x="68.375" y="106" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">harekâtı başladı.</text><line x1="127.75" y1="85" x2="134.75" y2="85" stroke="#2c3e50" stroke-width="1.6" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="135.75" y="36" width="116.75" height="98" rx="5" ry="5" fill="#fdebd0" stroke="#e67e22" stroke-width="1.4" /><rect x="135.75" y="36" width="116.75" height="28" rx="4" ry="4" fill="#e67e22" stroke="#e67e22" stroke-width="1.3" /><text x="194.125" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">30 AĞUSTOS 1922</text><text x="194.125" y="60" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">BAŞKOMUTANLIK</text><text x="194.125" y="80" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">Dumlupınar\'da Yunan</text><text x="194.125" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">ordusu imha edildi;</text><text x="194.125" y="106" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">hedef Akdeniz gösterildi.</text><line x1="253.5" y1="85" x2="260.5" y2="85" stroke="#2c3e50" stroke-width="1.6" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="261.5" y="36" width="116.75" height="98" rx="5" ry="5" fill="#d4e6f1" stroke="#2980b9" stroke-width="1.4" /><rect x="261.5" y="36" width="116.75" height="28" rx="4" ry="4" fill="#2980b9" stroke="#2980b9" stroke-width="1.3" /><text x="319.875" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">9–18 EYLÜL 1922</text><text x="319.875" y="60" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">KURTULUŞ</text><text x="319.875" y="80" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">9 Eylül\'de İzmir, 18</text><text x="319.875" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Eylül\'de tüm Batı</text><text x="319.875" y="106" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Anadolu kurtarıldı.</text><line x1="379.25" y1="85" x2="386.25" y2="85" stroke="#2c3e50" stroke-width="1.6" stroke-linecap="round" marker-end="url(#ok-koyu)" /><rect x="387.25" y="36" width="116.75" height="98" rx="5" ry="5" fill="#d5f5e3" stroke="#27ae60" stroke-width="1.4" /><rect x="387.25" y="36" width="116.75" height="28" rx="4" ry="4" fill="#27ae60" stroke="#27ae60" stroke-width="1.3" /><text x="445.625" y="48" font-family="DejaVu Sans, Arial, sans-serif" font-size="6.9" fill="#f1c40f" text-anchor="middle" font-weight="bold" font-style="normal">11 EKİM 1922</text><text x="445.625" y="60" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.2" fill="#ffffff" text-anchor="middle" font-weight="bold" font-style="normal">MUDANYA ATEŞKESİ</text><text x="445.625" y="80" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">İsmet Paşa imzaladı;</text><text x="445.625" y="93" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">Doğu Trakya ve İstanbul</text><text x="445.625" y="106" font-family="DejaVu Sans, Arial, sans-serif" font-size="7" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">savaşsız kurtarıldı.</text><rect x="10" y="142" width="495" height="50" rx="5" ry="5" fill="#fef9e7" stroke="#e67e22" stroke-width="1.4" /><text x="257.5" y="156" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.8" fill="#c0392b" text-anchor="middle" font-weight="bold" font-style="normal">MUDANYA ATEŞKES ANTLAŞMASI\'NIN (11 EKİM 1922) TARİHİ ÖNEMİ</text><text x="257.5" y="170" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="middle" font-weight="normal" font-style="normal">• Yunan ordusu Meriç Nehri\'nin batısına çekildi; Doğu Trakya 15 gün içinde TBMM\'ye (Refet Bele) teslim edildi.</text><text x="257.5" y="183" font-family="DejaVu Sans, Arial, sans-serif" font-size="7.1" fill="#2c3e50" text-anchor="middle" font-weight="bold" font-style="normal">• İstanbul ve Boğazların yönetimi TBMM Hükûmeti\'ne bırakılarak Osmanlı Devleti HUKUKEN sona erdi.</text></svg>']

def uygula(v):
    for i, b in enumerate(v.get('bolumler', [])):
        if i < len(SVGS):
            b['gorsel'] = SVGS[i]
