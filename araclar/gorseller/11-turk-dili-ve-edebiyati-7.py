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


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">ÇOK MODLU METİN ÇÖZÜMLEME VE DİNLEME/İZLEME SÜRECİ</text>'
    ic += _kart(20, 44, 310, 190, "ÇOK MODLU METNİN BİLEŞENLERİ", [
        "• Yazılı / Sözel Mod: Konuşma metni, altyazı, başlıklar.",
        "• Görsel Mod: Fotoğraf, video görüntüsü, renk, ışık,",
        "  kamera açısı, grafik ve semboller.",
        "• İşitsel Mod: Ses tonu, vurgu, fon müziği, ses efektleri.",
        "• Mekânsal ve Jestüel Mod: Beden dili, mimik, mizansen.",
        "• Tüm bu modlar ana düşünceyi desteklemek için birleşir."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "DİNLEME / İZLEME ÇÖZÜMLEME ADIMLARI", [
        "• İzleme öncesi: Başlık ve görsellerden hareketle",
        "  içeriğe dair tahminlerde bulunma ve amaç belirleme.",
        "• İzleme sırası: Açık ve örtük iletileri, ana düşünceyi",
        "  ve düşünceyi geliştirme yollarını not alma.",
        "• İzleme sonrası: Görsel ve işitsel unsurların metnin",
        "  iletisine katkısını ve tutarlılığını değerlendirme."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">MEKTUP TÜRÜ VE ÇEŞİTLERİ (ÖZEL, EDEBÎ, RESMÎ VE İŞ MEKTUBU)</text>'
    ic += _kart(20, 44, 310, 190, "ÖZEL MEKTUP VE EDEBÎ MEKTUP", [
        "• Özel Mektup: Akraba ve dostlar arasında samimi,",
        "  içten ve doğal bir üslupla yazılan mektuplardır.",
        "• Edebî Mektup: Sanatçı, şair ve düşünürlerin edebiyat,",
        "  sanat ve fikir konularını estetik bir üslupla tartıştığı",
        "  mektuplardır (Ör. Mehmet Kaplan - Âli'ye Mektuplar,",
        "  Nurullah Ataç - Okuruma Mektuplar, Cahit Sıtkı - Ziya'ya)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "RESMÎ MEKTUP VE İŞ MEKTUBU", [
        "• Resmî Mektup: Devlet kurumlarının kendi aralarında",
        "  veya vatandaşlarla yaptığı resmî yazışmalardır.",
        "• İş Mektubu: Ticari kurumlar, şirketler ve bireyler",
        "  arasında sipariş, başvuru, alacak-verecek gibi iş",
        "  konularında açık, kısa ve ciddi bir dille yazılır.",
        "• Mektup planı: Tarih, Hitap, Giriş-Gelişme-Sonuç, İmza."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">RESMÎ DİLEKÇE ŞABLONU VE YAZIM KURALLARI (3071 SAYILI KANUN)</text>'
    ic += (
        '<rect x="35" y="44" width="610" height="200" rx="8" fill="#FFFFFF" stroke="#0891B2" stroke-width="1.8"/>'
        '<text x="340" y="68" font-size="11.5" font-weight="bold" fill="#0F172A" text-anchor="middle">... LİSESİ MÜDÜRLÜĞÜNE / ... BELEDİYE BAŞKANLIĞINA (Büyük Harfle Makam Adı)</text>'
        '<text x="480" y="84" font-size="10.5" font-weight="bold" fill="#0891B2">İLÇE / İL</text>'
        '<text x="60" y="108" font-size="10.5" fill="#1E293B">Okulunuzun 11/A sınıfı ... numaralı öğrencisiyim. ... konusunda yaşadığım</text>'
        '<text x="60" y="124" font-size="10.5" fill="#1E293B">sorunun/talebin incelenerek çözülmesini istiyorum. (Kısa, açık, yalın ve resmî üslup)</text>'
        '<text x="60" y="144" font-size="10.5" font-weight="bold" fill="#059669">Gereğini bilgilerinize arz ederim. (Üst makama ARZ, alt makama RİCA edilir)</text>'
        '<text x="510" y="168" font-size="10.5" font-weight="bold" fill="#1E293B">26 / 10 / 2026 (Tarih)</text>'
        '<text x="510" y="190" font-size="10.5" font-weight="bold" fill="#DC2626">İmza</text>'
        '<text x="510" y="212" font-size="10.5" font-weight="bold" fill="#0F172A">Adı ve Soyadı (Sağ Alt)</text>'
        '<text x="60" y="176" font-size="10.5" font-weight="bold" fill="#1E293B">Adres: ... Mah. ... Sok. (Sol Alt)</text>'
        '<text x="60" y="194" font-size="10.5" fill="#1E293B">T.C. Kimlik No / Tel:</text>'
        '<text x="60" y="212" font-size="10.5" fill="#1E293B">Ekler: 1- Belge (Varsa)</text>'
    )
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">KURUMSAL E-POSTA (ELEKTRONİK POSTA) YAZIM İLKELERİ</text>'
    ic += _kart(20, 44, 310, 190, "ALICI (KİME / CC / BCC) VE KONU SATIRI", [
        "• Kime (To): E-postanın doğrudan muhatabı olan kişi.",
        "• Bilgi (CC): Bilgilendirilmesi gereken diğer kişiler.",
        "• Gizli (BCC): Alıcıların birbirini görmemesi gerektiğinde.",
        "• Konu (Subject): Boş bırakılmaz! İçeriği özetleyen",
        "  2-5 kelimelik net bir başlık yazılır",
        "  (Ör: '11-A Sınıfı Edebiyat Proje Teslimi Hakkında')."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "HİTAP, METİN GÖVDESİ VE İMZA BLOĞU", [
        "• Hitap: 'Sayın Yetkili,', 'Değerli Hocam,' gibi saygılı",
        "  ve kurumsal bir hitapla başlanır.",
        "• Gövde: Yazım ve noktalama kurallarına uyulur; tamamı",
        "  büyük harfle yazılmaz (bağırma anlamına gelir).",
        "• Kapanış ve İmza: 'Saygılarımla / İyi çalışmalar'",
        "  ifadesinin altına Ad-Soyad, unvan ve iletişim yazılır."
    ], "#2563EB", "#EFF6FF")
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
