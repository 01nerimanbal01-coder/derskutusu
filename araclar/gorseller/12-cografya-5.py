def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#0284C7", bg="#F0F9FF"):
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
        'HİZMET SEKTÖRÜNÜN EKONOMİDEKİ YERİ VE ULAŞIMI ETKİLEYEN FAKTÖRLER</text>'
    )
    ic += _kart(20, 44, 310, 190, "HİZMET SEKTÖRÜ VE ÖNEMİ", [
        "• Üçüncül ekonomik faaliyet grubudur (Eğitim, sağlık,",
        "  ulaşım, ticaret, turizm, bankacılık, finans, sigorta).",
        "• Gelişmiş ülkelerde hem çalışan nüfus içinde hem de",
        "  Gayrisafi Yurt İçi Hasıla (GSYİH) içinde en yüksek",
        "  paya (%70 ve üzeri) hizmet sektörü sahiptir.",
        "• Türkiye'de de GSYİH ve istihdamda 1. sıradadır."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "ULAŞIMI ETKİLEYEN DOĞAL VE BEŞERÎ FAKTÖRLER", [
        "1. Doğal Faktörler:",
        "   • Coğrafi konum (Boğazlar, kanallar, merkezi konum)",
        "   • Yeryüzü şekilleri (Dağların uzanışı, geçitler, eğim)",
        "   • İklim koşulları (Sis, buzlanma, kar, fırtına).",
        "2. Beşerî ve Ekonomik Faktörler:",
        "   • Nüfus ve yerleşme dağılışı, sanayi ve ticaret,",
        "   • Sermaye birikimi ve teknolojik gelişmişlik (Tünel, viyadük)."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ULAŞIM SİSTEMLERİNİN MALİYET VE ÖZELLİK KARŞILAŞTIRMASI</text>'
    )
    modlar = [
        ("1. DENİZ YOLU ULAŞIMI (EN UCUZ YÜK TAŞIMACILIĞI)", "Tek seferde çok büyük miktarda yük taşınır, yol yapım/bakım maliyeti yoktur; uluslararası ticarette 1. sıradadır!", "#0284C7", "#F0F9FF"),
        ("2. DEMİR YOLU ULAŞIMI (KARADA EN EKONOMİK YÜK)", "Deniz yolundan sonra en ucuz taşıma türüdür; ağır maden ve tarım ürünlerinin iç bölgelerden limanlara taşınmasını sağlar.", "#059669", "#ECFDF5"),
        ("3. KARA YOLU ULAŞIMI (KAPI-KAPI ESNEK ERİŞİM)", "Evden eve kesintisiz ulaşım sağlar, diğer ulaşım türlerini birbirine bağlar; yurt içi yolcu ve yük taşımada 1. sıradadır.", "#D97706", "#FEF3C7"),
        ("4. HAVA YOLU VE BORU HATLARI", "Hava yolu en hızlı ve en pahalı yolcu taşımacılığıdır; Boru hatları ise petrol ve doğal gazın en güvenli/kesintisiz aktarım yoludur.", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(modlar):
        y = 44 + i * 50
        ic += (
            f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DÜNYA DENİZ ULAŞIMINDA STRATEJİK BOĞAZLAR VE KANALLAR</text>'
    )
    ic += _kart(20, 44, 310, 190, "DOĞAL SU YOLLARI (BOĞAZLAR)", [
        "• İstanbul ve Çanakkale Boğazları: Karadeniz ülkelerinin",
        "  Akdeniz ve okyanuslara açılan TEK çıkış kapısıdır.",
        "• Cebelitarık Boğazı: Akdeniz'i Atlas Okyanusu'na bağlar.",
        "• Babülmendep Boğazı: Kızıldeniz'i Hint Okyanusu'na bağlar.",
        "• Hürmüz Boğazı: Basra Körfezi'ni Umman Denizi'ne bağlar",
        "  (Dünya petrol ticaretinin en kritik boğazı!).",
        "• Malakka (Asya) ve Dover / Bering Boğazları."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "BEŞERÎ SU YOLLARI (KANALLAR - SONRADAN AÇILAN)", [
        "• Süveyş Kanalı (Mısır - 1869): Akdeniz ile Kızıldeniz'i",
        "  birleştirdi; Ümit Burnu yolunu kısaltarak Akdeniz'in",
        "  önemini yeniden artırdı (Kapak/havuz sistemi YOKTUR).",
        "• Panama Kanalı (1914): Atlas ile Büyük Okyanus'u bağlar",
        "  (Macellan Boğazı'nın önemini azalttı; havuzludur).",
        "• Kiel Kanalı (Almanya): Baltık ve Kuzey Denizi'ni bağlar.",
        "• Korint Kanalı (Yunanistan): Ege ve İyon Denizi'ni bağlar."
    ], "#E11D48", "#FFF1F2")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DÜNYADA BAŞLICA DENİZ, DEMİR VE HAVA YOLU KUŞAKLARI</text>'
    )
    ic += _kart(20, 44, 310, 190, "EN İŞLEK DENİZ YOLU: KUZEY ATLANTİK", [
        "• Kuzey Atlantik Yolu: Batı Avrupa limanları (Rotterdam,",
        "  Hamburg, Londra) ile Kuzey Amerika'nın doğu kıyılarını",
        "  (New York) birbirine bağlayan DÜNYANIN EN İŞLEK",
        "  deniz ticaret yoludur.",
        "• Batı Avrupa - Akdeniz - Süveyş - Kızıldeniz - Hint",
        "  Okyanusu - Doğu Asya (Çin, Japonya) Yolu ikinci",
        "  en yoğun ticaret güzergahıdır."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "KARA, DEMİR VE HAVA YOLU YOĞUNLUĞU", [
        "• Demir ve Kara Yolu Ağı En Sık Bölgeler:",
        "  ABD'nin doğusu, Batı Avrupa, Hindistan ve Japonya.",
        "• Trans-Sibirya Demir Yolu: Moskova'dan Vladivostok'a",
        "  uzanan dünyanın en uzun demir yolu hattıdır.",
        "• Hava Yolu Trafiği En Yoğun Bölgeler:",
        "  Kuzey Amerika (ABD), Batı Avrupa ve Güneydoğu Asya;",
        "  Türkiye (İstanbul Havalimanı) küresel aktarma merkezidir."
    ], "#059669", "#ECFDF5")
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