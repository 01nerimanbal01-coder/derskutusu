def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Yerkürenin İç Yapısı (Geosfer Katmanları): Yoğunluk ve Sıcaklık Artışı</text>'
        + _kart(20, 42, 200, 142, "1. Yer Kabuğu (Litosfer)", [
            "• En ince ve en soğuk katman",
            "• Sial (Kıtasal kabuk): Silisyum",
            "  ve alüminyum; dağlarda kalın",
            "• Sima (Okyanusal kabuk):",
            "  Silisyum-magnezyum; daha yoğun"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. Manto (Üst: Astenosfer)", [
            "• Hacmi en büyük katman (%84)",
            "• Sıcaklığı 2000°C - 3700°C",
            "• Astenosferdeki KONVEKSİYONEL",
            "  AKINTILAR tüm iç kuvvetlerin",
            "  (levha hareketlerinin) kaynağıdır"
        ], "#ea580c", "#fff7ed")
        + _kart(460, 42, 200, 142, "3. Çekirdek (Nife / Ağır Küre)", [
            "• Nikel (Ni) ve Demir (Fe)",
            "• En yoğun ve en sıcak (6000°C)",
            "• Dış Çekirdek: Sıvı / Ergimiş",
            "  (Manyetik alanı oluşturur)",
            "• İç Çekirdek: Basınçtan katı"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Kıtaların Kayması (Wegener) ve Levha Tektoniği Kuramı Kanıtları</text>'
        + _kart(25, 42, 300, 145, "Pangea’dan Günümüze Kıtaların Ayrılması", [
            "• Alfred Wegener (1915): Tek kıta PANGEA ve",
            "  onu çevreleyen tek okyanus PANTHALASSA",
            "• Mezozoyik’te ikiye ayrıldı:",
            "  Kuzeyde Laurasia, Güneyde Gondwana (Arada Tetis)",
            "• Harry Hess ve Morgan: Levha Tektoniği Kuramı"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Levha Tektoniğinin 4 Bilimsel Kanıtı", [
            "• 1. Yapboz uyumu (Güney Amerika - Afrika kıyıları)",
            "• 2. Benzer sürüngen/bitki fosilleri (Mesosaurus)",
            "• 3. Benzer yaşlı kayaç ve sıradağ uzanışları",
            "• 4. Eski buzul izleri ve okyanus tabanı yayılması",
            "  (Sırtlardan uzaklaştıkça kayaç yaşının artması)"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Levha Sınırları ve Levha Hareket Türleri (Yaklaşma, Uzaklaşma, Yanal)</text>'
        + _kart(20, 42, 200, 145, "1. Yaklaşan (Çarpışan)", [
            "• Kıta-Kıta: Sıradağlar oluşur",
            "  (Avrasya-Hindistan -> Himalaya)",
            "• Kıta-Okyanus: Dalma-batma,",
            "  okyanus hendeği, volkanik yay",
            "  (And Dağları, Mariana Çukuru)"
        ], "#dc2626", "#fef2f2")
        + _kart(240, 42, 200, 145, "2. Uzaklaşan (Ayrılan)", [
            "• Okyanus-Okyanus: Okyanus",
            "  ortası sırtlar ve volkanik",
            "  adalar (Atlas Sırtı, İzlanda)",
            "• Kıta-Kıta: Rift vadileri ve",
            "  yeni denizler (Doğu Afrika, Kızıldeniz)"
        ], "#2563eb", "#eff6ff")
        + _kart(460, 42, 200, 145, "3. Yanal Yer Değiştiren", [
            "• Levhalar birbirine sürtünerek",
            "  yanal kayar (Kabuk oluşmaz/yok olmaz)",
            "• Transform fay hatları ve",
            "  yıkıcı depremler oluşur",
            "• Kuzey Anadolu Fayı, San Andreas"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Türkiye’nin Tektonik Konumu ve Çevresindeki Levhalar</text>'
        + _kart(25, 42, 300, 138, "Anadolu Levhasını Sıkıştıran Güçler", [
            "• Kuzeyde: Avrasya Levhası",
            "• Güneyde: Afrika ve Arap Levhaları (Kuzeye doğru",
            "  Anadolu’yu sıkıştırarak batıya doğru iter)",
            "• Alp-Himalaya Kırık ve Kıvrım Kuşağı üzerinde yer alır"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 138, "Türkiye’deki 3 Ana Fay Kuşağı", [
            "• KAF (Kuzey Anadolu Fay Hattı): Saros’tan Van’a",
            "• DAF (Doğu Anadolu Fay Hattı): Hatay’dan Bingöl’e",
            "• BAF (Batı Anadolu Fay Hattı): Kırıklı horst-graben",
            "• Sonuç: Deprem, sıcak su (jeotermal) ve genç arazi"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
