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
        'Kur’an’dan Mesajlar: İsrâ Suresi 36. Ayet ve Mülk Suresi 23. Ayet</text>'
        + _kart(25, 42, 300, 145, "İsrâ Suresi 36. Ayet: Bilgi Ahlakı ve Sorumluluk", [
            "• ”Hakkında kesin bilgin olmayan şeyin peşine düşme!”",
            "• Zan, tahmin, iftira ve yalan haberden sakınma",
            "• ”Çünkü kulak, göz ve kalp (akıl), bunların hepsi",
            "  ondan (yaptıklarından) sorumludur!”",
            "• Bilgiyi doğrulama (tebeyyün / tahkik) emri"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Mülk Suresi 23. Ayet: Bilgi Araçları ve Şükür", [
            "• ”O, sizi inşa eden (yaratan), size kulaklar,",
            "  gözler ve kalpler (akıllar) verendir.”",
            "• ”Ne kadar da az şükrediyorsunuz!”",
            "• Duyuların ve aklın yaratılış amacına uygun",
            "  kullanılması gerçek şükrün gereğidir"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Ayetlerde Vurgulanan 3 Temel Bilgi Edinim ve Sorumluluk Organı</text>'
        + _kart(20, 42, 200, 140, "1. es-Sem’ (Kulak / İşitme)", [
            "• Sözlü vahyi (nakli), ilmi ve",
            "  hakikati dinleme aracıdır",
            "• Anne karnında ilk gelişen",
            "  duyu olduğu için ayetlerde",
            "  ilk sırada zikredilir"
        ], "#0284c7", "#f0f9ff")
        + _kart(240, 42, 200, 140, "2. el-Ebsâr (Gözler / Görme)", [
            "• Şehadet âlemini (evreni)",
            "  gözlemleme ve okuma aracıdır",
            "• Kevnî ayetleri inceleyerek",
            "  deneysel bilgiye ulaşmayı",
            "  sağlayan sağlam duyulardır"
        ], "#d97706", "#fffbeb")
        + _kart(460, 42, 200, 140, "3. el-Ef’ide (Kalp / Akıl)", [
            "• Duyulardan gelen verileri",
            "  işleyen, muhakeme eden,",
            "  hak ile batılı ayıran merkez",
            "• İman, hikmet, vicdan ve",
            "  sorumluluk merkezidir"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 195, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'İslam Bilgi Ahlakı: Kesin Bilgi (İlim) ile Zan Arasındaki Fark</text>'
        + _kart(25, 42, 300, 142, "Kaçınılması Gereken Tutumlar (İsrâ 36)", [
            "• Bilmediği konuda kesin hüküm vermek",
            "• Yalancı şahitlik yapmak ve iftira atmak",
            "• Sosyal medyada doğrulanmamış haber yaymak",
            "• Kötü zanda (suizan) bulunmak ve tecessüs",
            "• Körü körüne taklit ve taassup"
        ], "#dc2626", "#fef2f2")
        + _kart(355, 42, 300, 142, "Müminin Bilgi Karşısındaki İlkeleri", [
            "• Haberi kaynağından araştırıp doğrulamak (Hucurât 6)",
            "• Akıl, sağlam duyular ve sadık habere dayanmak",
            "• Bilmediği konuda ”Bilmiyorum” diyebilmek",
            "• Kulak, göz ve kalp nimetlerini hayırda kullanmak",
            "• Emanet bilinciyle ahiret hesabını unutmamak"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Kur’an-ı Kerim Meallerinden Yararlanma Yöntemi</text>'
        + _kart(25, 42, 300, 138, "Meal ve Tefsir Nedir?", [
            "• Meal: Kur’an ayetlerinin başka bir dile yaklaşık",
            "  anlamlarıyla aktarılmasıdır (Özet çeviri)",
            "• Tefsir: Ayetlerin iniş sebepleri (esbâb-ı nüzûl),",
            "  bağlamı ve hükümleriyle geniş açıklamasıdır"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Ayetleri Doğru Anlama İlkeleri", [
            "• Ayeti öncesi ve sonrasıyla (siyak-sibak) okumak",
            "• Aynı konudaki diğer ayetlerle birlikte düşünmek",
            "• Farklı güvenilir mealleri karşılaştırmak",
            "• Hz. Peygamber’in (sav) sünnetine başvurmak"
        ], "#ea580c", "#fff7ed")
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
