def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'WEB TABANLI CBS İLE HARİTA UYGULAMA SÜRECİNİN 4 ADIMI (COĞ.11.2.1)</text>'
    )
    ic += _kart(
        20, 42, 345, 95,
        "a) Harita Okuma (Katman ve Sembol Tanıma)",
        [
            "• Altlık harita (uydu, topoğrafya, sokak) seçimi,",
            "• Lejant (harita anahtarı), ölçek ve koordinat okuma,",
            "• Nokta, çizgi ve alan katmanlarını ayırt etme.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        395, 42, 345, 95,
        "b) Harita Çözümleme (Sorgulama ve Ölçüm)",
        [
            "• Mesafe, alan ve yükseklik profili ölçümü yapma,",
            "• Öznitelik tablosundan (veri tabanı) filtreleme,",
            "• Çoklu katmanları (örn. eğim + heyelan) çakıştırma.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        20, 148, 345, 95,
        "c) Haritadan Çıkarım Yapma (Mekânsal Yorum)",
        [
            "• Dağılış örüntülerinden neden-sonuç ilişkisi kurma,",
            "• Riskli alanları ve uygun yer seçimi bölgelerini",
            "  belirleyerek geleceğe yönelik tahmin üretme.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        395, 148, 345, 95,
        "ç) Basit Harita Oluşturma (Sayısallaştırma)",
        [
            "• Nokta (okul/deprem), çizgi (yol/akarsu) ve poligon",
            "  (göl/orman) çizerek öznitelik verisi girme,",
            "• Semboloji, lejant ve başlık ekleyip paylaşma.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'CBS VERİ MODELLERİ: VEKTÖR VERİ (NOKTA, ÇİZGİ, POLİGON) VE RASTER VERİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Vektör Veri Modeli (Koordinat Tabanlı)",
        [
            "• Coğrafi unsurları (x, y) koordinat çiftleriyle",
            "  keskin sınırlarla temsil eder:",
            "  - Nokta (Point): Kuyu, okul, hastane, deprem.",
            "  - Çizgi (Line): Akarsu, karayolu, fay hattı, boru.",
            "  - Alan / Poligon (Polygon): Göl, il sınırı, orman.",
            "• Her şeklin arkasında satır ve sütunlardan oluşan",
            "  bir 'Öznitelik Tablosu (Attribute Table)' bulunur.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Raster (Hücresel / Piksel) Veri Modeli",
        [
            "• Mekânı eşit boyutlu kare hücrelerden (piksel /",
            "  grid) oluşan bir matris olarak temsil eder.",
            "• Her piksel tek bir sayısal değer (yükselti,",
            "  sıcaklık, yağış, yansıma değeri) taşır.",
            "• Örnekler: Uydu görüntüleri, hava fotoğrafları,",
            "  Sayısal Yükselti Modeli (SYM / DEM).",
            "• Sürekli yüzey analizlerinde (eğim, bakı) kullanılır.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'WEB TABANLI CBS\'DE MEKÂNSAL ANALİZ TEKNİKLERİ</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Çakıştırma (Overlay) Analizi",
        [
            "• Farklı tematik katmanların",
            "  üst üste bindirilerek ortak",
            "  koşulları sağlayan alanların",
            "  bulunmasıdır.",
            "• Örnek: Fay hattı + Alüvyal",
            "  zemin + Nüfus yoğunluğu →",
            "  Deprem Risk Haritası!",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Tampon Bölge (Buffer) Analizi",
        [
            "• Bir nokta, çizgi veya alanın",
            "  çevresinde belirli bir mesafe",
            "  (yarıçap/koridor) belirlenerek",
            "  etki alanının çizilmesidir.",
            "• Örnek: Akarsu yatağının sağ",
            "  ve solunda 500 m taşkın",
            "  koruma bandı oluşturma.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Ağ (Network) ve Yakınlık",
        [
            "• Ulaşım veya altyapı ağları",
            "  üzerinde en kısa / en hızlı",
            "  rotanın hesaplanmasıdır.",
            "• Örnek: İtfaiye veya ambulansın",
            "  olay yerine en kısa sürede",
            "  ulaşacağı güzergâhı bulma.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'TÜRKİYE VE DÜNYADA BAŞLICA WEB TABANLI CBS PORTALLARI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Türkiye'nin Milli Web CBS Platformları",
        [
            "• ATLAS (atlas.gov.tr) & TUCBS: Çevre, Şehircilik ve",
            "  İklim Değişikliği Bakanlığı Türkiye Ulusal CBS.",
            "• HGM Küre ve Atlas: Harita Genel Müdürlüğünün",
            "  3B dijital küre ve topoğrafik harita uygulaması.",
            "• MTA Yerbilimleri Portalı: Diri fay hatları, jeoloji",
            "  ve heyelan katmanlarının sorgulandığı portal.",
            "• TKGM Parsel Sorgu ve AFAD TDTH.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Küresel Açık Kaynak ve Bulut CBS Araçları",
        [
            "• ArcGIS Online & StoryMaps: Bulut tabanlı",
            "  etkileşimli harita ve hikâye haritası üretimi.",
            "• Google Earth Web & Google My Maps: Uydu",
            "  görüntüsü okuma ve kişisel harita katmanı çizme.",
            "• OpenStreetMap (OSM) & uMap: Kitle kaynaklı",
            "  (crowdsourced) özgür dünya haritası üretimi.",
            "• Copernicus Browser: Avrupa Uzay Ajansı uyduları.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
