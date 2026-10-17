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
        'İSLAM\'DA AİLE KURUMUNUN ÖNEMİ VE TEMEL İLKELERİ (RUM SURESİ, 21)</text>'
    )
    ic += _kart(20, 44, 310, 190, "AİLENİN ÜÇ MANEVİ DAYANAĞI", [
        "• Rum Suresi 21. Ayet: Aile Allah'ın varlığının ve",
        "  kudretinin delillerinden (ayetlerinden) biridir.",
        "1. Sekînet (Huzur ve Güven): Eşlerin birbirinde",
        "   ruhen sükûnet ve emniyet bulması.",
        "2. Meveddet (Sevgi ve Muhabbet): Karşılıklı",
        "   samimi sevgi, saygı ve gönül bağı.",
        "3. Rahmet (Merhamet ve Şefkat): Zorluklarda",
        "   ve yaşlılıkta birbirini koruyup kollama."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "AİLENİN BİREY VE TOPLUM İÇİN İŞLEVİ", [
        "• Neslin helal ve meşru yoldan korunmasını sağlar",
        "  (Zarûrât-ı Dîniyye'den 'Neslin Korunması').",
        "• İnsanın fıtri olan sevme, sevilme ve aidiyet",
        "  ihtiyacını karşılar; yalnızlıktan korur.",
        "• Çocukların ilk dini, ahlaki ve kültürel eğitimi",
        "  aldığı 'ilk mektep' (okul) görevi görür.",
        "• Sağlam aile, huzurlu ve güçlü toplumun temelidir."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'EVLİLİK AŞAMALARI VE NİKÂH AKDİNİN UNSURLARI</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. HİTBE (NİŞANLILIK)", [
        "• Evlilik öncesi tarafların",
        "  birbirini tanıması ve",
        "  evlilik vaadidir (Söz/Nişan).",
        "• DİKKAT: Nişanlılık nikâh",
        "  değildir; mahremiyet",
        "  sınırlarını kaldırmaz!",
        "• Başkasının dünür olduğu",
        "  kimseye dünür olunmaz."
    ], "#D97706", "#FEF3C7")
    ic += _kart(237, 44, 205, 190, "2. NİKÂH AKDİNİN ŞARTLARI", [
        "• İcap ve Kabul: Eşlerin özgür",
        "  iradeleriyle 'kabul ettim'",
        "  beyanı (Zorla nikâh geçersizdir).",
        "• Evlenme Engeli Olmaması:",
        "  Kan, sıhriyet (kayın) ve süt",
        "  hısımlığı engeli bulunmaması.",
        "• Aleniyet ve Şahitler:",
        "  Gizli değil, şahitler huzurunda."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. MEHİR VE VELİME", [
        "• Mehir: Erkeğin evlenirken",
        "  eşine verdiği veya taahhüt",
        "  ettiği mal/para (Kadının",
        "  öz malıdır, başlık parası değil!).",
        "   - Mehr-i Muaccel (Peşin)",
        "   - Mehr-i Müeccel (Vadeli)",
        "• Velime: Nikâhı topluma ilan",
        "  eden sünnet düğün yemeği."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'AİLE İÇİ HAK VE SORUMLULUKLAR: EŞLER, EBEVEYN VE ÇOCUKLAR</text>'
    )
    adimlar = [
        ("EŞLERİN KARŞILIKLI HAKLARI", "Sadakat, iffet, güzel geçim (muâşeret-i bil-maruf), istişare, ev işlerinde yardımlaşma ve karşılıklı nezaket.", "#059669", "#ECFDF5"),
        ("ANNE-BABANIN ÇOCUĞA KARŞI GÖREVLERİ", "Güzel isim koymak, helal rızıkla beslemek, iyi bir din/ahlak eğitimi vermek ve çocuklar arasında ADALETLİ davranmak.", "#2563EB", "#EFF6FF"),
        ("ÇOCUĞUN ANNE-BABAYA KARŞI GÖREVLERİ", "İhsan ve itaat (İsra, 23), 'öf' bile dememek, yaşlandıklarında şefkat kanatlarını germek ve vefatlarından sonra dua etmek.", "#D97706", "#FEF3C7"),
        ("AKRABA HAKLARI (SILA-İ RAHİM)", "Büyükleri, teyze, hala, amca ve dayı gibi yakın akrabaları ziyaret etmek, halini sormak ve ihtiyaç anında destek olmak.", "#9333EA", "#FAF5FF")
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
        'HZ. PEYGAMBER\'İN (S.A.V.) AİLE HAYATINDAN ÖRNEK İLKELER</text>'
    )
    ic += _kart(20, 44, 310, 190, "ŞEFKATLİ EŞ VE İSTİŞARE REHBERİ", [
        "• 'Sizin en hayırlınız, ailesine karşı en hayırlı",
        "  (en merhametli ve nazik) olanınızdır.' (Hadis)",
        "• Ev işlerinde eşlerine bizzat yardım eder, kendi",
        "  elbisesini diker, ayakkabısını tamir ederdi.",
        "• Eşlerine asla kaba davranmamış ve sesini yükseltmemiştir.",
        "• Önemli kararlarda eşleriyle istişare etmiştir",
        "  (Örn: Hudeybiye'de Ümmü Seleme annemizin tavsiyesi)."
    ], "#0D9488", "#F0FDFA")
    ic += _kart(350, 44, 310, 190, "MERHAMETLİ BABA VE DEDE", [
        "• Kız çocuklarının hor görüldüğü bir çağda kızı",
        "  Hz. Fatıma geldiğinde ayağa kalkar, alnından öper",
        "  ve kendi yanına oturturdu.",
        "• Torunları Hz. Hasan ve Hz. Hüseyin'i sırtında taşır,",
        "  namazda secdesini onlar için uzatırdı.",
        "• Çocuklarını hiç öpmeyen bir bedeviye: 'Merhamet",
        "  etmeyene merhamet olunmaz!' buyurmuştur."
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