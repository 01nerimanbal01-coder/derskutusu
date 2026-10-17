# -*- coding: utf-8 -*-
"""10. Sınıf Biyoloji — 5. Hafta Görselleri
Konu: Fotosentezde Kullanılan ve Üretilen Maddelerle İlgili Deney Tasarımı ve Analizi
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#16a34a", arka="#f0fdf4"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Fotosentez Deneylerinde Değişkenler ve Ayıraçlar (İyot, KOH, Ba(OH)2)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Fotosentez Deney Tasarımında Değişkenler ve Kimyasal Ayıraçlar", "#16a34a", "#f0fdf4")

    # Sol: Değişkenler
    s += '<rect x="30" y="55" width="335" height="235" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<text x="197" y="78" text-anchor="middle" fill="#166534" font-size="12.5" font-weight="700">1. Bilimsel Deney Değişkenleri</text>'

    deg = [
        ("Bağımsız Değişken", "Araştırmacının değiştirdiği etken", "(Işık şiddeti, dalga boyu, CO2, sıcaklık)", "#0284c7", "#e0f2fe"),
        ("Bağımlı Değişken", "Bağımsız değişkene bağlı sonuç", "(Üretilen O2 kabarcığı sayısı, nişasta miktarı)", "#16a34a", "#dcfce7"),
        ("Kontrol Değişkeni", "Her iki düzenekte sabit tutulanlar", "(Bitki türü, yaprak sayısı, su miktarı, süre)", "#d97706", "#fef3c7"),
    ]
    for i, (ad, acik, orn, r, bg) in enumerate(deg):
        y = 92 + i * 62
        s += f'<rect x="44" y="{y}" width="307" height="52" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.2"/>'
        s += f'<text x="56" y="{y+18}" fill="{r}" font-size="11.5" font-weight="700">{ad}:</text>'
        s += f'<text x="168" y="{y+18}" fill="#1e293b" font-size="10.5">{acik}</text>'
        s += f'<text x="56" y="{y+38}" fill="#475569" font-size="10">{orn}</text>'

    # Sağ: Kimyasal Ayıraçlar ve Tutucular
    s += '<rect x="385" y="55" width="345" height="235" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<text x="557" y="78" text-anchor="middle" fill="#166534" font-size="12.5" font-weight="700">2. Deneylerde Kullanılan Ayıraç ve Tutucular</text>'

    ayirac = [
        ("Lugol (İyot) Çözeltisi", "Nişasta ayıracıdır; fotosentez yapan yaprağı", "MAVİ-MOR renge boyar.", "#4f46e5", "#eef2ff"),
        ("KOH / NaOH / Ca(OH)2", "Karbondioksit (CO2) tutucudur; ortamdaki", "CO2 gazını bağlayarak fotosentezi durdurur.", "#dc2626", "#fef2f2"),
        ("Kireç Suyu / Ba(OH)2", "CO2 varlığında bulanır; nemli havadaki", "CO2'yi yakalar ve deneyi kontrol eder.", "#0d9488", "#f0fdfa"),
    ]
    for i, (ad, s1, s2, r, bg) in enumerate(ayirac):
        y = 92 + i * 62
        s += f'<rect x="400" y="{y}" width="315" height="52" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.2"/>'
        s += f'<text x="412" y="{y+18}" fill="{r}" font-size="11.5" font-weight="700">{ad}</text>'
        s += f'<text x="412" y="{y+34}" fill="#334155" font-size="10">{s1}</text>'
        s += f'<text x="412" y="{y+47}" fill="{r}" font-size="10" font-weight="700">{s2}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Yaprakta Nişasta Tayini (Işık ve Klorofil Gereksinimi - Siyah Bant Deneyi)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Yaprakta Nişasta Sentezi ve Siyah Bant (Işık) Deneyi", "#0284c7", "#f0f9ff")

    adimlar = [
        ("1. Karanlıkta Bekletme", "Bitki 24-48 saat", "karanlıkta tutulur;", "yapraklardaki mevcut", "nişasta sıfırlanır.", "#475569", "#f8fafc"),
        ("2. Siyah Bant & Işık", "Yaprağın orta kısmı", "ışık geçirmeyen siyah", "bantla kapatılıp", "ışıkta bekletilir.", "#d97706", "#fffbeb"),
        ("3. Kaynar Su & Alkol", "Hücre çeperi yumuşatılır;", "sıcak etil alkolde", "klorofil çözülerek", "yaprak beyazlatılır.", "#0d9488", "#f0fdfa"),
        ("4. İyot (Lugol) Damlatma", "Işık alan uçlar", "MAVİ-MOR olur;", "siyah bantlı orta kısım", "SARI-KAHVE kalır!", "#4f46e5", "#eef2ff"),
    ]
    for i, (bas, a1, a2, a3, a4, r, bg) in enumerate(adimlar):
        x = 28 + i * 178
        s += f'<rect x="{x}" y="58" width="166" height="175" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="166" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+83}" y="77" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+83}" y="110" text-anchor="middle" fill="#1e293b" font-size="10.5">{a1}</text>'
        s += f'<text x="{x+83}" y="128" text-anchor="middle" fill="#1e293b" font-size="10.5">{a2}</text>'
        s += f'<text x="{x+83}" y="146" text-anchor="middle" fill="#1e293b" font-size="10.5">{a3}</text>'
        s += f'<text x="{x+83}" y="166" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{a4}</text>'
        # Küçük yaprak ikonu
        if i == 1:
            s += f'<ellipse cx="{x+83}" cy="202" rx="42" ry="16" fill="#22c55e" stroke="#15803d"/>'
            s += f'<rect x="{x+68}" y="185" width="30" height="34" fill="#1e293b"/>'
        elif i == 3:
            s += f'<ellipse cx="{x+83}" cy="202" rx="42" ry="16" fill="#4f46e5" stroke="#312e81"/>'
            s += f'<rect x="{x+68}" y="186" width="30" height="32" fill="#fde047"/>'
        else:
            renk_yaprak = "#16a34a" if i == 0 else "#f1f5f9"
            s += f'<ellipse cx="{x+83}" cy="202" rx="42" ry="16" fill="{renk_yaprak}" stroke="#64748b"/>'

    s += '<rect x="28" y="246" width="700" height="38" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2"/>'
    s += '<text x="378" y="270" text-anchor="middle" fill="#0369a1" font-size="11.5" font-weight="700">Sonuç: Işık almayan siyah bantlı bölgede fotosentez ve nişasta sentezi gerçekleşmemiştir.</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Elodea Su Bitkisi Deneyi (Oksijen Çıkışı ve NaHCO3 Etkisi)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Elodea (Su Bitkisi) Deneyi: O2 Üretimi ve Fotosentez Hızı Ölçümü", "#0d9488", "#f0fdfa")

    # Sol: Deney Düzeneği Şeması
    s += '<rect x="30" y="55" width="330" height="235" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<text x="195" y="76" text-anchor="middle" fill="#0f766e" font-size="12.5" font-weight="700">Ters Huni ve Deney Tüpü Düzeneği</text>'

    # Işık kaynağı
    s += '<circle cx="85" cy="145" r="22" fill="#fef08a" stroke="#eab308" stroke-width="2"/>'
    s += '<text x="85" y="149" text-anchor="middle" fill="#854d0e" font-size="10" font-weight="700">IŞIK</text>'
    s += '<line x1="112" y1="135" x2="148" y2="150" stroke="#eab308" stroke-width="2" stroke-dasharray="4,3"/>'
    s += '<line x1="112" y1="155" x2="148" y2="170" stroke="#eab308" stroke-width="2" stroke-dasharray="4,3"/>'

    # Beher ve su
    s += '<rect x="155" y="125" width="120" height="125" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'
    # Ters huni ve Elodea
    s += '<polygon points="170,240 260,240 223,165 207,165" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5"/>'
    s += '<path d="M215,235 Q205,210 218,190 Q228,210 215,235" fill="#16a34a"/>'
    s += '<text x="215" y="266" text-anchor="middle" fill="#0f766e" font-size="10.5" font-weight="700">Su + NaHCO3 (CO2 kaynağı)</text>'

    # Tüp ve O2 kabarcıkları
    s += '<rect x="203" y="92" width="24" height="85" rx="10" fill="#f8fafc" stroke="#475569" stroke-width="1.8"/>'
    s += '<circle cx="215" cy="155" r="3.5" fill="#0284c7"/>'
    s += '<circle cx="212" cy="138" r="4" fill="#0284c7"/>'
    s += '<circle cx="217" cy="120" r="4.5" fill="#0284c7"/>'
    s += '<text x="292" y="112" fill="#dc2626" font-size="10.5" font-weight="700">Toplanan O2 Gazı</text>'
    s += '<text x="292" y="127" fill="#475569" font-size="9.5">(Parlak koru alevlendirir)</text>'

    # Sağ: Kabarcık Sayısını Artıran Etkenler
    s += '<rect x="380" y="55" width="350" height="235" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<text x="555" y="76" text-anchor="middle" fill="#0f766e" font-size="12.5" font-weight="700">Birim Zamandaki O2 Kabarcık Sayısını Artıranlar</text>'

    maddeler = [
        ("1. Işık Kaynağını Yaklaştırma", "Işık şiddeti artar -> Birim zamanda çıkan O2 kabarcığı artar."),
        ("2. Suya NaHCO3 (Yemek Sodası) Ekleme", "Suda çözünen CO2 miktarı artar -> Fotosentez hızlanır."),
        ("3. Mor veya Kırmızı Işık Kullanma", "Klorofilin en çok soğurduğu dalga boylarıdır (Yeşil ışıkta en az!)."),
        ("4. Sıcaklığı Optimuma (25-30 °C) Getirme", "Enzimler optimum hızda çalışır (Kaynatılırsa enzimler bozulur!)."),
    ]
    for i, (b, ac) in enumerate(maddeler):
        y = 90 + i * 47
        s += f'<rect x="394" y="{y}" width="322" height="40" rx="6" fill="#f0fdfa" stroke="#14b8a6" stroke-width="1"/>'
        s += f'<text x="404" y="{y+16}" fill="#0f766e" font-size="11" font-weight="700">{b}</text>'
        s += f'<text x="404" y="{y+32}" fill="#334155" font-size="10">{ac}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Engelmann Deneyi ve CO2 Tutucu (KOH) Kontrollü Fanus Deneyleri."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Engelmann (Dalga Boyu) Deneyi ve KOH Kontrollü Fanus Analizi", "#7c3aed", "#f5f3ff")

    # Sol: Engelmann Deneyi
    s += '<rect x="28" y="55" width="340" height="230" rx="10" fill="#fff" stroke="#c4b5fd" stroke-width="1.5"/>'
    s += '<text x="198" y="76" text-anchor="middle" fill="#5b21b6" font-size="12.5" font-weight="700">Engelmann Deneyi (İpliksi Alg + Aerob Bakteri)</text>'

    # Spektrum kutuları
    renkler = [
        ("Mor", "#7c3aed", 65),
        ("Mavi", "#2563eb", 60),
        ("Yeşil", "#16a34a", 18),
        ("Sarı", "#eab308", 25),
        ("Kırmızı", "#dc2626", 62),
    ]
    for i, (ad, r, yuk) in enumerate(renkler):
        x = 46 + i * 60
        # Bakteri yoğunluğu çubuğu
        s += f'<rect x="{x+8}" y="{190-yuk}" width="38" height="{yuk}" rx="4" fill="{r}" opacity="0.8"/>'
        s += f'<text x="{x+27}" y="{184-yuk}" text-anchor="middle" fill="{r}" font-size="9.5" font-weight="700">{"ÇOK" if yuk > 40 else "AZ"}</text>'
        # Işık spektrumu tabanı
        s += f'<rect x="{x}" y="195" width="54" height="24" rx="4" fill="{r}"/>'
        s += f'<text x="{x+27}" y="211" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">{ad}</text>'

    s += '<text x="198" y="242" text-anchor="middle" fill="#334155" font-size="10.5">Aerob (O2 seven) bakteriler en çok MOR, MAVİ ve KIRMIZI</text>'
    s += '<text x="198" y="258" text-anchor="middle" fill="#5b21b6" font-size="10.5" font-weight="700">bölgelerde toplanır; YEŞİL ışık yansıtıldığı için en azdır.</text>'

    # Sağ: KOH Fanus Deneyi
    s += '<rect x="388" y="55" width="344" height="230" rx="10" fill="#fff" stroke="#c4b5fd" stroke-width="1.5"/>'
    s += '<text x="560" y="76" text-anchor="middle" fill="#5b21b6" font-size="12.5" font-weight="700">CO2 Gereksinimi: KOH Kontrollü Cam Fanus</text>'

    # Fanus 1: Kontrol
    s += '<rect x="404" y="92" width="150" height="135" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>'
    s += '<text x="479" y="112" text-anchor="middle" fill="#166534" font-size="11" font-weight="700">1. Fanus (Kontrol)</text>'
    s += '<text x="479" y="135" text-anchor="middle" fill="#1e293b" font-size="10">Saksı Bitkisi + Işık</text>'
    s += '<text x="479" y="153" text-anchor="middle" fill="#16a34a" font-size="10" font-weight="700">Ortamda CO2 VAR</text>'
    s += '<rect x="418" y="170" width="122" height="44" rx="6" fill="#dcfce7"/>'
    s += '<text x="479" y="189" text-anchor="middle" fill="#15803d" font-size="10" font-weight="700">Fotosentez YAPAR</text>'
    s += '<text x="479" y="205" text-anchor="middle" fill="#15803d" font-size="9.5">İyotla Mavi-Mor (+)</text>'

    # Fanus 2: Deney (KOH)
    s += '<rect x="566" y="92" width="152" height="135" rx="10" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>'
    s += '<text x="642" y="112" text-anchor="middle" fill="#991b1b" font-size="11" font-weight="700">2. Fanus (+ KOH Kabı)</text>'
    s += '<text x="642" y="135" text-anchor="middle" fill="#1e293b" font-size="10">Bitki + Işık + KOH</text>'
    s += '<text x="642" y="153" text-anchor="middle" fill="#dc2626" font-size="10" font-weight="700">KOH, CO2\'yi TUTAR!</text>'
    s += '<rect x="580" y="170" width="124" height="44" rx="6" fill="#fee2e2"/>'
    s += '<text x="642" y="189" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="700">Fotosentez DURUR</text>'
    s += '<text x="642" y="205" text-anchor="middle" fill="#b91c1c" font-size="9.5">Nişasta Sentezlenemez (-)</text>'

    s += '<text x="560" y="252" text-anchor="middle" fill="#475569" font-size="10.5">Bağımsız değişken: Ortamdaki CO2 varlığı (KOH kullanımı)</text>'
    s += '<text x="560" y="268" text-anchor="middle" fill="#5b21b6" font-size="10.5" font-weight="700">Kanıt: Karbondioksit olmadan fotosentez gerçekleşmez.</text>'

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
