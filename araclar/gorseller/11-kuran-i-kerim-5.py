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
        'KEHF SURESİNİN KİMLİĞİ VE TEMEL KONULARI (KISSALARI)</text>'
    )
    ic += _kart(20, 44, 310, 190, "KEHF SURESİNİN GENEL ÖZELLİKLERİ", [
        "• Mekke döneminde indirilmiştir; 110 ayettir.",
        "• Kur'an-ı Kerim'in 18. suresidir (15. ve 16. cüz).",
        "• Adını 9-26. ayetlerde anlatılan 'Ashab-ı Kehf'",
        "  (Mağara Arkadaşları) kıssasından alır.",
        "• Allah'a hamd ile başlayan 5 sureden biridir",
        "  (Fatiha, En'am, Kehf, Sebe', Fatır).",
        "• İlk 10 ayetini ezberleyip okumanın fazileti büyüktür."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "SURENİN DÖRT BÜYÜK KISSASI VE İMTİHANI", [
        "1. Ashab-ı Kehf Kıssası: İnanç (İman) imtihanı;",
        "   putperest baskısına karşı tevhidi koruyan gençler.",
        "2. Bahçe Sahipleri Kıssası: Servet (Mal) imtihanı;",
        "   şımarıklık ve kibre karşı şükür bilinci.",
        "3. Hz. Musa ve Hızır Kıssası: İlim imtihanı;",
        "   zahiri bilginin ötesindeki ilahi hikmet ve tevazu.",
        "4. Zülkarneyn Kıssası: İktidar (Güç) ve adalet imtihanı."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KEHF SURESİ 1-10. AYETLERİN ANA MESAJLARI</text>'
    )
    adimlar = [
        ("1-3. AYETLER: DOSDOĞRU KİTAP (KAYYİM)", "Kuluna içinde hiçbir eğrilik ve çelişki bulunmayan Kitab'ı indiren Allah'a hamdolsun; Kur'an müminleri güzel bir ecr ile müjdeler.", "#059669", "#ECFDF5"),
        ("4-5. AYETLER: TEVHİD VE ŞİRKİN REDDİ", "'Allah evlat edindi' diyenleri uyarır; onların bu iddiada hiçbir ilmi delili yoktur, söyledikleri büyük bir iftiradır.", "#DC2626", "#FEF2F2"),
        ("6-8. AYETLER: DÜNYA SÜSÜ VE İMTİHAN", "Yeryüzündeki her şey kimin daha güzel amel işleyeceğini sınamak için bir süstür (zinet); sonunda hepsi kupkuru toprağa dönecektir.", "#D97706", "#FEF3C7"),
        ("9-10. AYETLER: ASHAB-I KEHF VE RAKÎM", "Mağara ve Rakîm (kitabe) ehli gençlerin mağaraya sığınarak: 'Rabbimiz! Bize katından rahmet ver ve işimizde doğruluk (rüşd) hazırla' duası.", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
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
        'KEHF SURESİ 1. AYETTE ÖZEL TECVİT UYGULAMASI: SEKTE KURALI</text>'
    )
    ic += _kart(20, 44, 310, 190, "SEKTE NEDİR VE NASIL UYGULANIR?", [
        "• Sözlük anlamı: Susmak, sesi kesmek.",
        "• Tecvit tanımı: Kur'an okurken NEFES ALMADAN",
        "  sesi yaklaşık iki elif miktarı (1-2 saniye) kesip",
        "  okumaya devam etmektir.",
        "• Vakıftan farkı: Vakıfta hem ses kesilir hem nefes",
        "  yenilenir; sektede ise NEFES TUTULARAK yalnız ses kesilir.",
        "• Mushafta kelimenin altına/üstüne küçük 'sin' veya 'sekte' yazılır."
    ], "#9333EA", "#FAF5FF")
    ic += _kart(350, 44, 310, 190, "KUR'AN'DAKİ DÖRT SEKTE YERİ (ASIM KIRAATI)", [
        "1. Kehf Suresi 1-2. Ayet geçişi:",
        "   'ivecâ [SEKTE] kayyimen' ('eğrilik olan doğru' gibi",
        "   yanlış bir anlam birleşmesini ve ihfayı önlemek için).",
        "2. Yasin Suresi 52. Ayet: 'min merkadina [SEKTE] haza'",
        "3. Kıyamet Suresi 27. Ayet: 'men [SEKTE] rakin'",
        "4. Mutaffifin Suresi 14. Ayet: 'bel [SEKTE] rane'",
        "• Not: 'ivecâ' kelimesinde durulursa Medd-i İvaz olur."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KEHF SURESİ 1-10. AYETLERDE GEÇEN DİĞER TECVİT KURALLARI</text>'
    )
    ic += _kart(20, 44, 205, 190, "MED VE LAFZATULLAH", [
        "• Elhamdü lillâhi:",
        "  'lillâhi' -> Öncesi esreli",
        "  olduğu için Lafzatullah",
        "  İNCE okunur.",
        "• enzele alâ: Medd-i Tabii.",
        "• mâkisine fîhi: Medd-i",
        "  Tabii ve Zamir uzatması."
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "TENVİN VE SAKİN NUN", [
        "• enzele: Nun + Ze -> İHFA.",
        "• kayyimen li-yünzira:",
        "  Tenvin + Lam -> İDGAM-I",
        "  BİLA GUNNE (Gunnesiz).",
        "• eciran hasenen: Tenvin +",
        "  Ha -> İZHAR.",
        "• kiziben: Vakıfta Medd-i İvaz."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "KALKALE VE İDGAM", [
        "• abdihi: Be harfi sakin ->",
        "  KALKALE.",
        "• şedîden min: Tenvin + Mim",
        "  -> İDGAM-I MEAL GUNNE.",
        "• min ledünke: Nun + Lam ->",
        "  İDGAM-I BİLA GUNNE.",
        "• rahmeten ve: İdgam-ı Meal Gunne."
    ], "#D97706", "#FEF3C7")
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
