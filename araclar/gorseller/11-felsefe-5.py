def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#7C3AED", bg="#F5F3FF"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MİTOS\'TAN LOGOS\'A GEÇİŞ VE İYONlA DOĞA FELSEFESİ (MÖ 6. YÜZYIL)</text>'
    )
    ic += _kart(20, 44, 310, 190, "NEDEN İYONYA (BATI ANADOLU)?", [
        "• Milet, Efes, Sisam gibi liman kentlerinde canlı ticaret.",
        "• Mezopotamya, Mısır ve Yunan kültürlerinin kesişimi.",
        "• Ekonomik refah, boş zaman ve özgür tartışma ortamı.",
        "• Din adamları sınıfının baskıcı otoritesinin olmayışı.",
        "• Mitos (efsanevi/doğaüstü açıklamalar) yerine",
        "  Logos (akıl, gözlem ve doğal nedenlerle açıklama).",
        "• İlk problem: Varlığın ana maddesi (Arkhe) nedir?"
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "ARKHE (İLK NEDEN) KAVRAMI", [
        "• Evrendeki çokluğun kendisinden doğduğu ve tekrar",
        "  kendisine döndüğü değişmeyen ilk töz / ana unsur.",
        "• Doğa filozofları (Fizikçiler), doğayı yine doğanın",
        "  içindeki unsurlarla açıklamaya çalışmışlardır.",
        "• Monist (Tekçi) Yaklaşım: Tek bir ana madde (Su, Hava).",
        "• Pluralist (Çokçu) Yaklaşım: Birden çok unsur (4 Element,",
        "  Atomlar, Tohumlar) birleşerek evreni oluşturur."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'İLK DOĞA FİLOZOFLARI VE ARKHE (ANA MADDE) GÖRÜŞLERİ</text>'
    )
    ic += _kart(20, 44, 205, 200, "MİLET OKULU", [
        "• Thales (Felsefenin Kurucusu):",
        "  Arkhe = SU (Yaşamın kaynağı,",
        "  üç halde bulunabilen töz).",
        "• Anaksimandros:",
        "  Arkhe = APEİRON (Sınırsız,",
        "  belirsiz, sonsuz ilk soyut ilke).",
        "• Anaksimenes:",
        "  Arkhe = HAVA (Seyrelme ve",
        "  sıkışma ile her şeye dönüşür)."
    ], "#0284C7", "#F0F9FF")
    ic += _kart(237, 44, 205, 200, "SAYI VE ÇOKÇU FİLOZOFLAR", [
        "• Pythagoras (Pisagor):",
        "  Arkhe = SAYILAR (Evrenin",
        "  matematiği ve uyumu/harmoni).",
        "• Empedokles (Dört Element):",
        "  Su, Hava, Toprak ve Ateş.",
        "  İtici güç: Sevgi ve Nefret.",
        "• Anaksagoras:",
        "  Arkhe = Spermalar (Tohumlar)",
        "  ve düzenleyici akıl (NOUS)."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 200, "ATOMCU MATERYALİZM", [
        "• Leukippos ve Demokritos:",
        "  Arkhe = ATOM (Bölünemeyen",
        "  en küçük maddi parçacıklar).",
        "• Boşlukta hareket eden",
        "  atomların mekanik çarpışması",
        "  ve birleşmesi varlığı doğurur.",
        "• Ayrışması ise yok oluşu",
        "  meydana getirir (İlk doğa",
        "  materyalizmi ve determinizm)."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DEĞİŞİM PROBLEMI: HERAKLEİTOS (OLUŞ) VE PARMENİDES (VARLIK)</text>'
    )
    ic += _kart(20, 44, 310, 190, "HERAKLEİTOS: HER ŞEY AKAR (PANTA REİ)", [
        "• Efesli filozof; Arkhe = ATEŞ (Canlı ve dönüştürücü).",
        "• 'Aynı ırmağa iki kez girilmez; çünkü hem ırmağın",
        "  suları hem de giren insan değişmiştir.'",
        "• Evrende durağan hiçbir şey yoktur; tek gerçek OLUŞ",
        "  ve kesintisiz değişimdir.",
        "• Zıtların Birliği (Diyalektik): Savaş/çatışma her şeyin",
        "  babasıdır (Gece-gündüz, yaşam-ölüm); düzeni LOGOS korur."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "PARMENİDES: DEĞİŞİM BİR YANILSAMADIR", [
        "• Elea Okulu kurucusu; Herakleitos'un tam karşıtıdır.",
        "• 'Varlık vardır, yokluk (hiçlik) yoktur.'",
        "• Değişim, bir şeyin olduğu şey olmaktan çıkıp",
        "  olmadığı şeye (yokluğa) geçmesidir; yokluk",
        "  düşünülemeyeceği için değişim mantıksal olarak imkansızdır.",
        "• Varlık; BİR, bölünmez, ezeli-ebedi ve HAREKETSİZDİR.",
        "• Duyularımız değişim yanılsaması verir; hakikat AKILDADIR."
    ], "#4F46E5", "#EEF2FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DOĞA FELSEFESİNDEN ÇEVRE FELSEFESİNE: İNSAN VE DOĞA İLİŞKİSİ</text>'
    )
    adimlar = [
        ("ANTİK DOĞA ANLAYIŞI (KOZMOS)", "İlk Çağ filozoflarına göre doğa canlı bir bütündür (hylozoizm); insan doğanın efendisi değil, Kozmos'un uyumlu bir parçasıdır.", "#059669", "#ECFDF5"),
        ("ANTROPOSENTRİZM (İNSAN MERKEZCİLİK)", "Modern çağda doğayı yalnızca insanın çıkarı için tüketilecek mekanik bir hammadde deposu gören araçsal yaklaşım.", "#DC2626", "#FEF2F2"),
        ("EKOSENTRİZM (ÇEVRE MERKEZCİLİK)", "Canlı ve cansız tüm ekosistem bileşenlerinin kendi başına içsel değer taşıdığını savunan bütüncül (Derin Ekoloji) yaklaşım.", "#2563EB", "#EFF6FF"),
        ("SÜRDÜRÜLEBİLİR EKOLOJİK BİLİNÇ", "Gelecek kuşakların yaşam hakkını koruyan, iklim adaleti ve ekolojik ayak izi sorumluluğuna dayalı çağdaş çevre etiği.", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
