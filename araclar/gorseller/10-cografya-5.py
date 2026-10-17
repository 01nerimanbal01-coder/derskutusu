# -*- coding: utf-8 -*-
"""10. Sınıf Coğrafya — 5. Hafta Görselleri
Konu: Mekânsal Verilerin Haritalara Aktarılması: CBS ve Altlık Haritalar Üzerinde Mekânsal Veri Oluşturma
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0284c7", arka="#f0f9ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Vektörel Mekânsal Veri Tipleri: Nokta, Çizgi ve Poligon (Alan) Gösterimi."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Haritalarda Vektörel Mekânsal Veri Geometrileri: Nokta, Çizgi ve Alan (Poligon)", "#0284c7", "#f0f9ff")

    tipler = [
        ("1. Nokta (Point) Veri", "Boyutsuz konum verisidir;", "(x, y) koordinat çiftiyle", "gösterilir.", "Örnek: Okul, hastane, zirve,", "deprem merkez üssü, kuyu.", "#dc2626", "#fef2f2"),
        ("2. Çizgi (Line) Veri", "Tek boyutlu uzunluk verisidir;", "ardışık noktaların", "birleşmesiyle oluşur.", "Örnek: Akarsu, karayolu,", "fay hattı, boru hattı, sınır.", "#0284c7", "#e0f2fe"),
        ("3. Poligon (Alan) Veri", "İki boyutlu kapalı yüzeydir;", "çevre ve alan (km²) hesabı", "yapılabilir.", "Örnek: Göl, orman alanı, il", "sınırı, tarım parseli, baraj.", "#16a34a", "#f0fdf4"),
    ]
    for i, (bas, a1, a2, a3, o1, o2, r, bg) in enumerate(tipler):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="230" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'

        # Sembol çizimi
        if i == 0:
            s += f'<circle cx="{x+65}" cy="115" r="6" fill="{r}"/>'
            s += f'<circle cx="{x+115}" cy="105" r="6" fill="{r}"/>'
            s += f'<circle cx="{x+155}" cy="122" r="6" fill="{r}"/>'
        elif i == 1:
            s += f'<polyline points="{x+45},125 {x+95},100 {x+140},120 {x+180},98" fill="none" stroke="{r}" stroke-width="3.5"/>'
            for px, py in [(x+45, 125), (x+95, 100), (x+140, 120), (x+180, 98)]:
                s += f'<circle cx="{px}" cy="{py}" r="4" fill="#fff" stroke="{r}" stroke-width="2"/>'
        else:
            s += f'<polygon points="{x+55},125 {x+90},95 {x+155},100 {x+175},128 {x+110},135" fill="#bbf7d0" stroke="{r}" stroke-width="2.5"/>'

        s += f'<text x="{x+112}" y="160" text-anchor="middle" fill="#1e293b" font-size="10.5">{a1}</text>'
        s += f'<text x="{x+112}" y="176" text-anchor="middle" fill="#1e293b" font-size="10.5">{a2}</text>'
        s += f'<text x="{x+112}" y="192" text-anchor="middle" fill="#1e293b" font-size="10.5">{a3}</text>'
        s += f'<text x="{x+112}" y="225" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{o1}</text>'
        s += f'<text x="{x+112}" y="241" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{o2}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """CBS'de Vektör Veri Modeli vs Raster (Hücresel/Piksel) Veri Modeli ve Öznitelik Tablosu."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "CBS Veri Modelleri: Vektör - Raster Karşılaştırması ve Öznitelik (Tablo) Verisi", "#4f46e5", "#eef2ff")

    # Sol: Vektör vs Raster
    s += '<rect x="28" y="55" width="340" height="235" rx="10" fill="#fff" stroke="#a5b4fc" stroke-width="1.5"/>'
    s += '<text x="198" y="76" text-anchor="middle" fill="#3730a3" font-size="12" font-weight="700">1. Konumsal (Grafik) Veri Modelleri</text>'

    # Vektör kutusu
    s += '<rect x="42" y="90" width="148" height="182" rx="8" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>'
    s += '<text x="116" y="110" text-anchor="middle" fill="#0369a1" font-size="11" font-weight="700">VEKTÖR VERİ</text>'
    s += '<polygon points="65,160 110,125 160,145 140,185 80,185" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>'
    s += '<text x="116" y="212" text-anchor="middle" fill="#334155" font-size="9.8">• Koordinat tabanlıdır</text>'
    s += '<text x="116" y="228" text-anchor="middle" fill="#334155" font-size="9.8">• Yakınlaşınca bozulmaz</text>'
    s += '<text x="116" y="244" text-anchor="middle" fill="#0369a1" font-size="9.8" font-weight="700">• Kesin sınır ve ağ analizi</text>'

    # Raster kutusu
    s += '<rect x="204" y="90" width="150" height="182" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>'
    s += '<text x="279" y="110" text-anchor="middle" fill="#b45309" font-size="11" font-weight="700">RASTER (HÜCRESEL)</text>'
    # Piksel ızgarası
    for r_i in range(4):
        for c_i in range(5):
            dolgu = "#fbbf24" if (r_i + c_i) in [2, 3, 4] else "#fef9c3"
            s += f'<rect x="{234+c_i*18}" y="{122+r_i*16}" width="18" height="16" fill="{dolgu}" stroke="#d97706" stroke-width="0.8"/>'
    s += '<text x="279" y="212" text-anchor="middle" fill="#334155" font-size="9.8">• Piksel (grid) tabanlıdır</text>'
    s += '<text x="279" y="228" text-anchor="middle" fill="#334155" font-size="9.8">• Uydu / hava fotoğrafı</text>'
    s += '<text x="279" y="244" text-anchor="middle" fill="#b45309" font-size="9.8" font-weight="700">• Sıcaklık, yükselti yüzeyi</text>'

    # Sağ: Öznitelik (Attribute) Tablosu
    s += '<rect x="386" y="55" width="346" height="235" rx="10" fill="#fff" stroke="#a5b4fc" stroke-width="1.5"/>'
    s += '<text x="559" y="76" text-anchor="middle" fill="#3730a3" font-size="12" font-weight="700">2. Öznitelik (Sözel / Tablo) Verisi Eşleşmesi</text>'

    # Tablo başlığı
    s += '<rect x="402" y="92" width="314" height="26" rx="4" fill="#4f46e5"/>'
    s += '<text x="430" y="109" fill="#fff" font-size="10" font-weight="700">ID</text>'
    s += '<text x="485" y="109" fill="#fff" font-size="10" font-weight="700">Göl Adı</text>'
    s += '<text x="580" y="109" fill="#fff" font-size="10" font-weight="700">Alan (km²)</text>'
    s += '<text x="655" y="109" fill="#fff" font-size="10" font-weight="700">Su Özelliği</text>'

    satirlar = [
        ("101", "Van Gölü", "3.713", "Sodalı"),
        ("102", "Tuz Gölü", "1.665", "Tuzlu"),
        ("103", "Beyşehir Gölü", "656", "Tatlı"),
    ]
    for i, (id_no, ad, alan, su) in enumerate(satirlar):
        y = 122 + i * 28
        bg = "#eef2ff" if i % 2 == 0 else "#f8fafc"
        s += f'<rect x="402" y="{y}" width="314" height="26" fill="{bg}" stroke="#c7d2fe" stroke-width="0.8"/>'
        s += f'<text x="430" y="{y+17}" fill="#1e293b" font-size="10">{id_no}</text>'
        s += f'<text x="485" y="{y+17}" fill="#1e293b" font-size="10" font-weight="700">{ad}</text>'
        s += f'<text x="585" y="{y+17}" fill="#1e293b" font-size="10">{alan}</text>'
        s += f'<text x="655" y="{y+17}" fill="#4f46e5" font-size="10" font-weight="700">{su}</text>'

    s += '<rect x="402" y="216" width="314" height="58" rx="6" fill="#e0e7ff" stroke="#6366f1" stroke-width="1"/>'
    s += '<text x="559" y="236" text-anchor="middle" fill="#312e81" font-size="10.5" font-weight="700">CBS\'nin Gücü: Konumsal + Öznitelik Bağlantısı</text>'
    s += '<text x="559" y="253" text-anchor="middle" fill="#334155" font-size="9.8">Haritadaki her poligon/nokta, tablodaki bir satıra bağlıdır;</text>'
    s += '<text x="559" y="267" text-anchor="middle" fill="#334155" font-size="9.8">böylece &quot;Suyu tatlı olan gölleri göster&quot; sorgusu yapılabilir.</text>'

    return _svg(w, h, s)


def gorsel_3():
    """CBS'de Katmanlı (Layer) Harita Oluşturma ve Çakıştırma Analizi."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Altlık Harita Üzerinde Katmanlı (Layer) Mekânsal Veri Üretimi", "#0d9488", "#f0fdfa")

    katmanlar = [
        ("1. Altlık Harita", "Uydu görüntüsü veya", "topoğrafya haritası", "(Referans zemin)", "#475569", "#f1f5f9"),
        ("2. Alan Katmanı", "Arazi kullanımı, göller,", "orman ve mahalle", "poligonları çizilir.", "#16a34a", "#dcfce7"),
        ("3. Çizgi Katmanı", "Ulaşım ağları, akarsular", "ve fay hatları vektörel", "çizgi olarak eklenir.", "#0284c7", "#e0f2fe"),
        ("4. Nokta Katmanı", "Okul, hastane, toplanma", "alanı ve istasyonlar", "nokta olarak işlenir.", "#dc2626", "#fee2e2"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(katmanlar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="170" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        # Paralelkenar katman görseli
        s += f'<polygon points="{x+35},105 {x+145},90 {x+130},130 {x+20},145" fill="{bg}" stroke="{r}" stroke-width="2"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="{r}" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="168" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="184" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="202" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a3}</text>'

    s += '<rect x="26" y="242" width="708" height="42" rx="8" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.3"/>'
    s += '<text x="380" y="261" text-anchor="middle" fill="#0f766e" font-size="11" font-weight="700">Çakıştırma (Overlay) Analizi: Tüm katmanlar aynı koordinat sisteminde üst üste bindirilerek</text>'
    s += '<text x="380" y="277" text-anchor="middle" fill="#115e59" font-size="10.5">en uygun yer seçimi, afet risk haritalaması ve güzergâh planlaması gerçekleştirilir.</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Tematik Harita Yöntemleri: Koroplet (Dereceli Renklendirme), Noktalama, İzoplet ve Akış."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Mekânsal Verilerin Haritaya Aktarılmasında Tematik Harita Yöntemleri", "#d97706", "#fffbeb")

    yontemler = [
        ("Koroplet Harita", "(Dereceli Renk / Ton)", "İdari sınırlar (il, ülke)", "içindeki yoğunluk veya", "oran verilerini renk", "tonlarıyla gösterir.", "#b45309", "#fef3c7"),
        ("Noktalama Haritası", "(Dot Density)", "Belirli sayıda birimi", "temsil eden özdeş", "noktalarla dağılışı", "(tarım, nüfus) gösterir.", "#15803d", "#f0fdf4"),
        ("Orantılı Sembol", "(Dereceli Daire)", "Değerin büyüklüğüyle", "orantılı büyüyen daire", "veya sütunlarla miktarı", "karşılaştırır.", "#0369a1", "#f0f9ff"),
        ("İzoplet &amp; Akış", "(Eş Değer / Yön)", "İzohips ve izoterm gibi", "sürekli yüzeyleri veya", "göç/ticaret yönünü", "oklarla gösterir.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, alt, a1, a2, a3, a4, r, bg) in enumerate(yontemler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="102" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{alt}</text>'
        s += f'<text x="{x+84}" y="130" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="146" text-anchor="middle" fill="#334155" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="162" text-anchor="middle" fill="#334155" font-size="10">{a3}</text>'
        s += f'<text x="{x+84}" y="178" text-anchor="middle" fill="#334155" font-size="10">{a4}</text>'

        # Mini grafik ikonu
        if i == 0:
            s += f'<rect x="{x+34}" y="198" width="32" height="24" fill="#fde68a" stroke="{r}"/>'
            s += f'<rect x="{x+68}" y="198" width="32" height="24" fill="#f59e0b" stroke="{r}"/>'
            s += f'<rect x="{x+102}" y="198" width="32" height="24" fill="#b45309" stroke="{r}"/>'
        elif i == 1:
            for dx, dy in [(48, 205), (62, 215), (78, 202), (92, 218), (108, 206), (120, 214)]:
                s += f'<circle cx="{x+dx}" cy="{dy}" r="3.5" fill="{r}"/>'
        elif i == 2:
            s += f'<circle cx="{x+52}" cy="212" r="7" fill="{r}" opacity="0.7"/>'
            s += f'<circle cx="{x+84}" cy="212" r="12" fill="{r}" opacity="0.7"/>'
            s += f'<circle cx="{x+122}" cy="212" r="17" fill="{r}" opacity="0.7"/>'
        else:
            s += f'<path d="M{x+36},218 Q{x+84},192 {x+132},215" fill="none" stroke="{r}" stroke-width="2.5"/>'
            s += f'<path d="M{x+36},228 Q{x+84},202 {x+132},225" fill="none" stroke="{r}" stroke-width="1.8" stroke-dasharray="4,2"/>'

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
