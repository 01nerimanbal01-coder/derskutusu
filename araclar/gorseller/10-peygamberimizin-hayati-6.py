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
        'Taif’in İslamlaşma Süreci: Hüzün Yılından (620) Hicri 9. Yıla (630)</text>'
        + _kart(18, 42, 152, 142, "1. Taif Yolculuğu (620)", [
            "• Hüzün Yılı sonrası",
            "  Hz. Zeyd ile gidiş",
            "• Taşlanma ve ağır tepki",
            "• Beddua yerine hidayet",
            "  duası ve Addâs’ın imanı"
        ], "#dc2626", "#fef2f2")
        + _kart(180, 42, 152, 142, "2. Huneyn ve Kuşatma", [
            "• Mekke’nin Fethi (630)",
            "  sonrası Hevâzin ve",
            "  Sakîf’in Huneyn Savaşı",
            "• Taif Kalesi’nin",
            "  kuşatılması ve dua"
        ], "#d97706", "#fffbeb")
        + _kart(342, 42, 152, 142, "3. Urve b. Mes’ûd", [
            "• Sakîf reisi Urve’nin",
            "  Müslüman olması",
            "• Kavmine İslam’ı tebliğ",
            "  ederken şehit edilmesi",
            "• Taiflilerin pişmanlığı"
        ], "#7c3aed", "#f5f3ff")
        + _kart(504, 42, 158, 142, "4. Sakîf Heyeti (630)", [
            "• Abdüyâlîl başkanlığında",
            "  Medine’ye heyet gelişi",
            "• Lât putunun yıkılması",
            "• Osman b. Ebü’l-Âs’ın",
            "  vali atanması"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Taiflilerin İslam’a Direnme Nedenleri ve Peygamberimizin Stratejisi</text>'
        + _kart(25, 42, 300, 145, "Sakîf Kabilesinin Direnme Sebepleri", [
            "• Mekkeli Kureyş müşrikleriyle kurdukları sıkı",
            "  akrabalık, ticari ve siyasi çıkar ortaklığı",
            "• Taif’teki ”Lât” putunun sağladığı dini ve",
            "  ekonomik ayrıcalığı kaybetme korkusu",
            "• Kabile asabiyeti ve kibir (Zuhruf 31 itirazı)"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 145, "Hz. Peygamber’in (sav) Hikmetli Yaklaşımı", [
            "• Taif kuşatmasını kaldırırken: ”Allah’ım! Sakîf",
            "  kabilesine hidayet ver ve onları bana getir!” duası",
            "• Huneyn esirlerini ve ganimetlerini bağışlayarak",
            "  kalpleri İslam’a ısındırması (Müellefe-i Kulûb)",
            "• Gönüllü olarak Medine’ye gelmelerini sağlaması"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Sakîf Heyetinin Medine’de İleri Sürdüğü Şartlar ve Peygamberimizin Cevabı</text>'
        + _kart(25, 42, 300, 145, "Kabul Edilmeyen Taviz Talepleri (Tevhit ve Ahlak)", [
            "• 1. ”Lât putu 3 yıl yıkılmasın” -> KESİNLİKLE REDDEDİLDİ",
            "  (Tevhit inancında şirke 1 ay bile müsamaha yoktur!)",
            "• 2. ”Namazdan muaf tutulalım” -> REDDEDİLDİ",
            "  (”Rükûsu/namazı olmayan dinde hayır yoktur!”)",
            "• 3. ”Faiz (riba) ve zinaya izin verilsin” -> REDDEDİLDİ"
        ], "#dc2626", "#fef2f2")
        + _kart(355, 42, 300, 145, "Kabul Edilen İnsani ve İdari Talepler", [
            "• ”Lât putunu kendi ellerimizle biz yıkmayalım” ->",
            "  KABUL EDİLDİ (Ebû Süfyân ve Muğîre b. Şu’be yıktı)",
            "• Taif vadisinin (Vec Vadisi) doğal dokusunun,",
            "  ağaçlarının ve av hayvanlarının koruma altına",
            "  alınması -> KABUL EDİLDİ (Ahitname yazıldı)"
        ], "#2563eb", "#eff6ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'İslamlaşma Sonrası Taif ve Yetiştirdiği Öncü Sahabiler</text>'
        + _kart(25, 42, 300, 138, "Genç Vali: Osman b. Ebü’l-Âs es-Sekafî", [
            "• Heyetteki en genç üye olmasına rağmen Kur’an",
            "  öğrenme gayretiyle Taif’e vali/lider atandı",
            "• Hz. Ebû Bekir döneminde Ridde (irtidat) olaylarında",
            "  Taif halkının İslam’da sabit kalmasını sağladı"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 138, "10 Yıllık Sürecin Verdiği Ders", [
            "• 620’de Hz. Peygamber’i taşlayan Taif’in çocukları,",
            "  630’da İslam’ın en sadık savunucuları oldu",
            "• Peygamberimizin 620’deki ”Soylarından yalnız",
            "  Allah’a ibadet edecek nesiller çıkar” duası kabul oldu"
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
