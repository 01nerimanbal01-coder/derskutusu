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
        'CANLILARDA ENERJİ DÖNÜŞÜMLERİ VE ATP (ADENOZİN TRİFOSFAT) YAPISI</text>'
    )
    ic += _kart(20, 44, 310, 190, "ATP MOLEKÜLÜNÜN BİLEŞENLERİ", [
        "• Azotlu Organik Baz: Adenozin içindeki ADENİN (Pürin).",
        "• Beş Karbonlu Şeker (Pentoz): RİBOZ şekeri (RNA ile ortak).",
        "• Adenin + Riboz (Glikozit bağı) = ADENOZİN (Nükleozit).",
        "• 3 Adet İnorganik Fosfat Grubu (H3PO4):",
        "   - Riboz ile 1. fosfat arasında: ESTER (Fosfoester) bağı.",
        "   - Fosfatlar arasında: 2 adet YÜKSEK ENERJİLİ FOSFAT bağı.",
        "• Adenozin + 1P = AMP | + 2P = ADP | + 3P = ATP."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "ATP\'NİN TEMEL ÖZELLİKLERİ", [
        "• Hücre zarından dışarı ÇIKAMAZ; hücreden hücreye",
        "  aktarılamaz, her canlı hücre kendi ATP'sini üretir.",
        "• Hücrede DEPOLANAMAZ; üretildiği anda hızla tüketilir.",
        "• Evrensel enerji molekülüdür (Tüm canlılarda aynıdır).",
        "• ATP Üretimi (Sentezi): FOSFORİLASYON (Endergonik).",
        "• ATP Yıkımı (Hidrolizi): DEFOSFORİLASYON (Ekzergonik).",
        "• ATP + H2O -&gt; ADP + P_i + Serbest Enerji (7300 cal)."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ENDERGONİK (ATP HARCANAN) VE EKZERGONİK (ATP ÜRETİLEN) OLAYLAR</text>'
    )
    ic += _kart(20, 44, 310, 190, "ATP HARCANAN (BİYOSENTEZ VE İŞ) OLAYLARI", [
        "• Biyosentez (Dehidrasyon): Protein, DNA, RNA, nişasta,",
        "  glikojen ve yağ sentezi.",
        "• Aktif Taşıma ve Endositoz / Ekzositoz olayları.",
        "• Sinirsel İmpuls İletimi (Na+-K+ pompası) ve Kas Kasılması.",
        "• Hücre Bölünmesi (Mitoz/Mayozda iğ iplikleri ve eşlenme).",
        "• Aktivasyon Enerjisi (Glikoliz başlangıcında 2 ATP).",
        "• DİKKAT: Hidroliz (Sindirim), Difüzyon ve Ozmozda ATP HARCANMAZ!"
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "FOSFORİLASYON (ATP ÜRETİM) ÇEŞİTLERİ", [
        "1. Substrat Düzeyinde Fosforilasyon (SDF):",
        "   Enzim yardımıyla organik substrattan ADP'ye fosfat",
        "   aktarımı (Glikoliz ve Krebs; TÜM CANLILARDA ORTAK!).",
        "2. Oksidatif Fosforilasyon (OF):",
        "   ETS'de elektron taşınırken ATP sentezi (Oksijenli/",
        "   Oksijensiz solunum ve Kemosentez).",
        "3. Fotofosforilasyon (FF): Klorofil ve ışıkla ATP sentezi."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'FOTOSENTEZİN GENEL DENKLEMİ VE KLOROPLASTIN YAPISI</text>'
    )
    ic += _kart(20, 44, 310, 190, "KLOROPLASTIN BÖLÜMLERİ", [
        "• Çift katlı zarla çevrilidir; kendine ait halkasal",
        "  DNA, RNA, ribozom ve ETS elemanları vardır.",
        "• GRANA (Tilakoit Zar Sistemi):",
        "  Klorofil pigmentleri ve ETS burada bulunur; IŞIĞA",
        "  BAĞIMLI REAKSİYONLAR burada gerçekleşir.",
        "• STROMA (Renksiz Sıvı Kısım):",
        "  Enzimler, DNA ve ribozomlar buradadır; IŞIKTAN",
        "  BAĞIMSIZ REAKSİYONLAR (Calvin Döngüsü) burada olur."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "HIDROJEN KAYNAĞINA GÖRE FOTOSENTEZ", [
        "• Karbon kaynağı tüm fotosentetiklerde AYNIDIR: CO2.",
        "1. Hidrojen kaynağı H2O olanlar (Bitkiler, Algler,",
        "   Siyanobakteriler, Öglena):",
        "   6CO2 + 6H2O -&gt; C6H12O6 + 6O2 (Yan ürün OKSİJEN!).",
        "   (Atmosfere verilen O2'nin kaynağı H2O'dur!).",
        "2. Hidrojen kaynağı H2S olanlar (Mor Kükürt Bakterileri):",
        "   6CO2 + 12H2S -&gt; C6H12O6 + 6H2O + 12S (Yan ürün Kükürt!)."
    ], "#0284C7", "#F0F9FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'IŞIK SPEKTRUMU, PIGMENTLER VE ENGELMANN DENEYİ</text>'
    )
    adimlar = [
        ("GÖRÜNÜR IŞIK (380 - 750 nm)", "Fotosentez yalnız görünür ışıkta gerçekleşir; mor-mavi ve kırmızı ışık en çok soğurulur, yeşil ışık ise yansıtılır.", "#2563EB", "#EFF6FF"),
        ("FOTOSENTEZ HIZI SIRALAMASI", "Işığın enerjisiyle değil klorofil tarafından SOĞURULMA oranıyla belirlenir: Mor - Mavi &gt; Kırmızı &gt; Sarı &gt; Yeşil (En düşük).", "#059669", "#ECFDF5"),
        ("YARDIMCI PİGMENTLER (KAROTENOİTLER)", "Karoten (turuncu), Ksantofil (sarı), Likopen (kırmızı); farklı dalga boylarını soğurup klorofile aktarır ve klorofili korur.", "#D97706", "#FEF3C7"),
        ("ENGELMANN\'IN İPLİKSİ ALG DENEYİ", "Prizmadan geçirilen ışıkta oksijenli solunum yapan bakteriler en çok MOR, MAVİ ve KIRMIZI bölgelerde toplanmıştır.", "#7C3AED", "#F5F3FF")
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
