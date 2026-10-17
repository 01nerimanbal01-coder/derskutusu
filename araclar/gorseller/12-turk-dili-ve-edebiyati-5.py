def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563EB", bg="#EFF6FF"):
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
        'CUMHURİYET DÖNEMİ İLK YILLARDA ŞİİR: SAF (ÖZ) ŞİİR ANLAYIŞI</text>'
    )
    ic += _kart(20, 44, 310, 190, "SAF (ÖZ) ŞİİRİN TEMEL İLKELERİ", [
        "• Kaynağı: Fransız sembolistleri (Baudelaire, Mallarme,",
        "  Valery) ve Ahmet Haşim ile Yahya Kemal'in mirası.",
        "• Amaç: İdeoloji ve öğreticilik değil, ESTETİK HAZ",
        "  ve 'güzel şiir' yazmaktır ('Şiir, kelimelerle güzel",
        "  şekiller kurma sanatıdır').",
        "• Ahenk: Musiki, iç ses, ölçü, uyak ve imge ön plandadır.",
        "• Temalar: Bireysel duygular, ölüm, sonsuzluk, rüya, zaman."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "ÖNDE GELEN TEMSİLCİLERİ VE ESERLERİ", [
        "• Necip Fazıl Kısakürek: 'Kaldırımlar Şairi'; Çile,",
        "  Örümcek Ağı, Ben ve Ötesi, Sonsuzluk Kervanı.",
        "• Ahmet Hamdi Tanpınar: 'Bursa'da Zaman'; rüya,",
        "  musiki ve Bergson'un zaman kavramı.",
        "• Ahmet Muhip Dıranas: 'Fahriye Abla', 'Olvido', 'Kar'.",
        "• Cahit Sıtkı Tarancı: 'Otuz Beş Yaş', 'Desem ki'.",
        "• Asaf Halet Çelebi: Sezgi ve Doğu mistisizmi (He, Om Mani)."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'YEDİ MEŞALECİLER (1928): "CANLILIK, SAMİMİYET VE DAİMA YENİLİK"</text>'
    )
    ic += _kart(20, 44, 310, 190, "TOPLULUĞUN ÖZELLİKLERİ", [
        "• Cumhuriyet Dönemi'nde bir bildiri (manifesto) ile",
        "  ortaya çıkan İLK edebi topluluktur (1928).",
        "• Beş Hececilerin memleket edebiyatını 'sığ ve",
        "  taklitçi' bularak 'Canlılık, samimiyet ve daima",
        "  yenilik' sloganıyla çıktılar.",
        "• Saf şiir anlayışına ve Fransız sembolizmine",
        "  yöneldiler, şiirde resimsel izlenimler kurdular."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "YEDİ MEŞALE SANATÇILARI (CEVİZ Yasağı Kodu)", [
        "1. Ziya Osman Saba: Grubun şiire en sadık şairi",
        "   (Sebil ve Güvercinler, Geçen Zaman, Nefes Almak).",
        "2. Yaşar Nabi Nayır: Varlık dergisinin kurucusu.",
        "3. Sabri Esat Siyavuşgil (Odalar ve Sofalar).",
        "4. Cevdet Kudret Solok (Birinci Perde).",
        "5. Vasfi Mahir Kocatürk (Tunç Sesleri).",
        "6. Muammer Lütfi Bahşi | 7. Kenan Hulusi Koray (Tek hikayeci!)."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MİLLÎ EDEBİYAT ANLAYIŞINI YANSITAN ŞİİR VE BEŞ HECECİLER</text>'
    )
    ic += _kart(20, 44, 310, 190, "MEMLEKETÇİ ŞİİRİN ÖZELLİKLERİ", [
        "• Kaynağı: Ziya Gökalp ve Mehmet Emin Yurdakul'un",
        "  başlattığı Milli Edebiyat akımı ile Halk şiiri geleneği.",
        "• Ölçü ve Nazım Birimi: Hece ölçüsü ve dörtlük.",
        "• Dil: İstanbul Türkçesine dayalı sade, duru halk dili.",
        "• Temalar: Anadolu insanı ve coğrafyası, Kurtuluş",
        "  Savaşı, vatan sevgisi, tarih bilinci ve kahramanlık.",
        "• Hitabet ve coşku (lirik-epik/hamasi) tonu güçlüdür."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "BEŞ HECECİLER (HEYOF) VE DİĞER TEMSİLCİLER", [
        "• Beş Hececiler:",
        "   - Faruk Nafiz Çamlıbel ('Sanat' şiiri, Han Duvarları)",
        "   - Enis Behiç Koryürek, Halit Fahri Ozansoy,",
        "     Orhan Seyfi Orhon, Yusuf Ziya Ortaç.",
        "• Diğer Memleketçi Şairler:",
        "   - Kemalettin Kamu ('Gurbet Şairi' - Bingöl Çobanları)",
        "   - Ahmet Kutsi Tecer (Orda Bir Köy Var Uzakta, Âşık Veysel)",
        "   - Arif Nihat Asya ('Bayrak Şairi'), Ömer Bedrettin Uşaklı."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SAF ŞİİR VE MİLLÎ EDEBİYAT ANLAYIŞINI YANSITAN ŞİİR KARŞILAŞTIRMASI</text>'
    )
    satirlar = [
        ("SANAT ANLAYIŞI", "Saf Şiir: 'Sanat, sanat içindir' (Estetik gayeli) | Milli Şiir: 'Sanat, toplum ve millet içindir' (Ülkü gayeli).", "#7C3AED", "#F5F3FF"),
        ("TEMA VE İÇERİK", "Saf Şiir: Bireysel iç dünya, ölüm, zaman, rüya, metafizik | Milli Şiir: Anadolu, yurt güzellikleri, tarih ve kahramanlık.", "#2563EB", "#EFF6FF"),
        ("DİL VE İMGE", "Saf Şiir: İmge, sembol, çağrışım ve musiki yoğun | Milli Şiir: Açık, yalın, konuşma diline yakın ve anlaşılır.", "#059669", "#ECFDF5"),
        ("ORTAK YÖNLERİ", "Her iki anlayış da Cumhuriyet'in ilk yıllarında hece ölçüsünü, dörtlük/bent biçimlerini ve Türkçenin ses güzelliğini işlemiştir.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(satirlar):
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
