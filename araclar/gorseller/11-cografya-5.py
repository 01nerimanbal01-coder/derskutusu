def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
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
        'EKOSİSTEMİN UNSURLARI VE BESİN ZİNCİRİNDE ENERJİ AKIŞI</text>'
    )
    ic += _kart(20, 44, 310, 190, "EKOSİSTEMİN BİLEŞENLERİ", [
        "1. Canlı (Biyotik) Unsurlar:",
        "   • Üreticiler (Bitkiler, algler, siyanobakteriler)",
        "   • Tüketiciler (Otçullar, etçiller, hepçiller)",
        "   • Ayrıştırıcılar / Saprofitler (Mantar ve bakteriler)",
        "2. Cansız (Abiyotik) Unsurlar:",
        "   • Fiziksel: Işık, sıcaklık, rüzgar, yağış, iklim.",
        "   • Kimyasal: Su, oksijen, CO2, mineral, karbonhidrat."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "BESİN PİRAMİDİ VE %10 YASASI", [
        "• Enerji kaynağı Güneş'tir ve akış TEK YÖNLÜDÜR.",
        "• Üreticiden tüketiciye doğru çıkıldıkça:",
        "   - Aktarılan enerji azalır (Yalnız %10'u aktarılır).",
        "   - Birey sayısı ve toplam biyokütle azalır.",
        "   - Vücut büyüklüğü ve dokularda biriken zehir",
        "     (biyolojik birikim) oranı ARTAR.",
        "• Ayrıştırıcılar piramidin her basamağında görev yapar."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KARBON VE OKSİJEN DÖNGÜSÜ (KARŞILIKLI DENGE)</text>'
    )
    ic += _kart(20, 44, 310, 190, "KARBON DÖNGÜSÜ (CO2 AKIŞI)", [
        "• Karbonun 4 büyük deposu:",
        "   - Litosfer (Kömür, petrol, kireç taşı - En büyük)",
        "   - Hidrosfer (Suda çözünmüş CO2 ve bikarbonat)",
        "   - Atmosfer (CO2 gazı) ve Biyosfer (Organik madde)",
        "• Atmosfere CO2 Verenler: Solunum, fosil yakıt",
        "  tüketimi, orman yangınları, volkanizma, çürüme.",
        "• Atmosferden CO2 Alanlar: Fotosentez, deniz kabukluları."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "OKSİJEN DÖNGÜSÜ (O2 AKIŞI)", [
        "• Atmosferin %21'i serbest oksijen gazından oluşur.",
        "• Oksijen Üreten Süreçler:",
        "   - Fotosentez (Klorofilli bitkiler, algler, planktonlar)",
        "   - Fotoliz (Üst atmosferde su buharının Güneş'in UV",
        "     ışınlarıyla H2 ve O2'ye ayrışması).",
        "• Oksijen Tüketen Süreçler:",
        "   - Canlı solunumu, fosil yakıt yanması, oksidasyon (paslanma)."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'AZOT (N2) DÖNGÜSÜNÜN AŞAMALARI: NİTRİFİKASYON VE DENİTRİFİKASYON</text>'
    )
    adimlar = [
        ("1. AZOT BAĞLANMASI (FİKSASYON)", "Atmosferin %78'ini oluşturan serbest N2; yıldırım/şimşek veya baklagil kökündeki Rhizobium bakterileriyle toprağa bağlanır.", "#2563EB", "#EFF6FF"),
        ("2. NİTRİFİKASYON (BİTKİYE UYGUN HALE GELME)", "Topraktaki amonyağın (NH3) nitrit ve nitrat bakterileri tarafından bitkilerin alabileceği nitrat tuzlarına (NO3) dönüştürülmesidir.", "#059669", "#ECFDF5"),
        ("3. BESİN ZİNCİRİ VE AYRIŞTIRMA (SAPROFİTLER)", "Bitkiler nitratı proteine çevirir; ölen bitki ve hayvan atıklarını ayrıştırıcılar parçalayarak tekrar amonyağa dönüştürür.", "#D97706", "#FEF3C7"),
        ("4. DENİTRİFİKASYON (ATMOSFERE GERİ DÖNÜŞ)", "Denitrifikasyon bakterileri topraktaki nitratı serbest azot gazına (N2) çevirerek atmosfere geri verir ve döngüyü tamamlar.", "#9333EA", "#FAF5FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SU DÖNGÜSÜ (HİDROLOJİK DÖNGÜ) VE İNSAN MÜDAHALELERİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "HİDROLOJİK DÖNGÜNÜN ADIMLARI", [
        "• Buharlaşma ve Terleme (Evapotranspirasyon):",
        "  Güneş enerjisiyle okyanus ve bitkilerden yükselen su.",
        "• Yoğuşma: Yükselen su buharının soğuyarak bulut",
        "  ve sis oluşturması.",
        "• Yağış: Yağmur, kar ve dolu olarak yeryüzüne iniş.",
        "• Yüzeysel Akış ve Sızma (İnfiltrasyon): Yağışın",
        "  akarsularla denizlere ve sızmayla yer altı suyuna karışması."
    ], "#0284C7", "#F0F9FF")
    ic += _kart(350, 44, 310, 190, "MADDE DÖNGÜLERİNDE İNSAN ETKİSİ", [
        "• Aşırı fosil yakıt kullanımı -> Karbon döngüsü bozulur,",
        "  sera etkisi ve küresel ısınma hızlanır.",
        "• Tarımda aşırı yapay azotlu ve fosforlu gübreleme ->",
        "  Göllerde 'Ötrofikasyon' (aşırı alg patlaması) oluşur.",
        "• Kentleşme, betonlaşma ve aşırı yer altı suyu çekimi ->",
        "  Sızma azalır, obruklar oluşur ve sulak alanlar kurur.",
        "• Asit yağmurları (SO2, NOx) orman ve toprağı tahrip eder."
    ], "#E11D48", "#FFF1F2")
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
