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
        'Türkistan’dan Türkiye’ye (1040-1299) Sosyal Yaşam ve Yerleşme Biçimleri</text>'
        + _kart(20, 42, 200, 140, "1. Konargöçerler (Oğuz Boyları)", [
            "• Yaylak ve kışlak yaşamı",
            "• Hayvancılık, halı ve kilim",
            "  dokumacılığı",
            "• Uç bölgelerinin güvenliği ve",
            "  Anadolu’nun Türkleşmesi"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 140, "2. Köylüler (Reaya)", [
            "• İkta topraklarında yerleşik",
            "  tarımsal üretim",
            "• Tahıl, pamuk, bağ-bahçe",
            "• Çift resmi ve öşür vergisi",
            "  ile devlete katkı"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 140, "3. Şehirliler (Zanaatkâr-Tüccar)", [
            "• Konya, Sivas, Kayseri, Erzurum",
            "• Ahilik teşkilatı ve loncalar",
            "• İlim, kültür, mimari ve",
            "  uluslararası ticaret merkezi"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 195, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Türkiye Selçuklularında Ticareti Geliştirme Politikaları</text>'
        + _kart(25, 42, 300, 145, "Kara ve Deniz Ticareti Hamleleri", [
            "• Kervansaraylar (Ribât / Han) ağının kurulması",
            "  (Yolcuların 3 gün ücretsiz konaklaması)",
            "• Antalya, Alanya, Sinop ve Suğdak limanlarının fethi",
            "• Kıbrıs Krallığı ve Venedik ile ticaret antlaşmaları",
            "• Gümrük vergilerinin düşürülmesi"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Dünya Tarihinde İlk Devlet Sigortası ve İkta", [
            "• Eşkiya veya korsan saldırısında tüccarın zararının",
            "  devlet hazinesinden karşılanması (Devlet Sigortası)",
            "• İkta Sistemi: Toprağın gelirinin askere/memura",
            "  verilmesiyle üretimin sürekliliği ve güvenlik",
            "• Yabanlu Pazarı gibi uluslararası fuarların kurulması"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">'
        'Ahilik Teşkilatı ve Anadolu’nun İmarında Tasavvufi Zümreler</text>'
        + _kart(25, 42, 300, 145, "Ahilik Teşkilatı (Ahi Evran - Kırşehir)", [
            "• Esnaf ve zanaatkârların mesleki-ahlaki örgütü",
            "• Fütüvvetname kuralları ve usta-kalfa-çırak eğitimi",
            "• Kalite, fiyat (narh) ve standart denetimi (pabucu",
            "  dama atılmak deyimi)",
            "• Bacıyan-ı Rum (Fatma Bacı): Kadınların örgütlenmesi"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "Horasan Erenleri ve Manevi Rehberler", [
            "• Hoca Ahmed Yesevî’nin (Pîr-i Türkistan) etkisi",
            "• Mevlânâ Celâleddîn-i Rûmî, Yunus Emre,",
            "  Hacı Bektâş-ı Velî",
            "• Abdalan-ı Rum ve Gaziyan-ı Rum (Alperenler)",
            "• Zaviyeler kurarak ıssız yerleri şenlendirme (iskân)"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Türk-İslam Şehirleşmesi ve Vakıf Medeniyeti Kurumları</text>'
        + _kart(20, 42, 200, 138, "Dini ve İlmi Yapılar", [
            "• Ulu Camiler ve Külliyeler",
            "• Medreseler (Yağıbasan,",
            "  Gevher Nesibe, Karatay,",
            "  İnce Minareli, Gök Medrese)"
        ], "#ea580c", "#fff7ed")
        + _kart(240, 42, 200, 138, "Sosyal Yardım (Vakıf)", [
            "• Darüşşifa / Bimarhane",
            "  (Ücretsiz hastane ve tıp)",
            "• İmaret (Aşevi), çeşme,",
            "  köprü ve zaviyeler"
        ], "#16a34a", "#f0fdf4")
        + _kart(460, 42, 200, 138, "Ticari Mekanlar", [
            "• Bedesten (Değerli eşya)",
            "• Arasta (Aynı esnaf çarşısı)",
            "• Kapan (Toptan gıda hali)",
            "• Sultan Hanları"
        ], "#2563eb", "#eff6ff")
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
