def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'SÖZLÜ İLETİŞİM ENGELLERİNİN KAYNAKLARINA GÖRE SINIFLANDIRILMASI</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Fiziksel ve Teknik Engeller",
        [
            "• Ortamdaki aşırı gürültü ve uğultu,",
            "• Yetersiz aydınlatma, aşırı sıcak/",
            "  soğuk ve mesafe uzaklığı,",
            "• Mikrofon, telefon veya bağlantı",
            "  arızaları (kanal gürültüsü),",
            "• İşitme veya konuşma güçlükleri.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Psikolojik ve Sosyal Engeller",
        [
            "• Ön yargılar ve kalıp yargılar,",
            "• Empati yoksunluğu ve benmerkezcilik,",
            "• Statü farkı, kibir ve üstenci dil,",
            "• Aşırı heyecan, kaygı, öfke veya",
            "  geçmiş olumsuz deneyimler,",
            "• Dinliyormuş gibi görünme (sahte).",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Dil ve Anlatım (Semantik) Engelleri",
        [
            "• Ortak dil/kod eksikliği, aşırı terim",
            "  veya yabancı kelime kullanımı,",
            "• Çok anlamlılık ve anlatım bozukluğu,",
            "• Bozuk diksiyon, yanlış vurgu/tonlama,",
            "• Beden dili ile sözün çelişmesi,",
            "• Karagöz-Hacivat tipi yanlış anlamalar.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'GORDON\'UN İLETİŞİM ENGELLERİ VE ÇÖZÜM YOLU: SEN DİLİ YERİNE BEN DİLİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Yıkıcı İletişim Engelleri (Sen Dili)",
        [
            "• Emir verme ve yönlendirme ('Hemen sus ve otur!')",
            "• Gözdağı verme / Tehdit ('Bir daha konuşursan...')",
            "• Suçlama, yargılama ve eleştirme ('Sen hep böylesin!')",
            "• Ad takma ve alay etme ('Acemi, laf anlamaz!')",
            "• Konuyu saptırma ve sorguya çekme",
            "• SONUÇ: Savunmaya geçme, küskünlük ve çatışma.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Yapıcı Çözüm: Ben Dili ve Etkin Dinleme",
        [
            "• Kişiliği değil, davranışı ve yarattığı duyguyu anlatır:",
            "  (Davranış + Somut Etki + Hissettirdiği Duygu)",
            "• Örnek: 'Sözüm kesildiğinde (davranış) düşüncemi",
            "  unutuyorum (etki) ve üzülüyorum (duygu).'",
            "• Göz teması kurma ve açık uçlu geri bildirim verme,",
            "• SONUÇ: Empati, karşılıklı saygı ve uzlaşı.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'KONUŞMAYI YÖNETME VE İÇERİK OLUŞTURMA SÜRECİ (TDE3.1 & TDE3.2)</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Seçim Yapma ve Alan Sınıflandırması",
        [
            "• Konuşma Amacı: İkna etme, bilgilendirme, estetik",
            "  zevk verme veya toplumsal farkındalık oluşturma.",
            "• Türü: Hazırlıklı konuşma / Hazırlıksız (doğaçlama).",
            "• Dilin Kullanım Alanına Göre İçerik Seçimi:",
            "  - Özel alan (aile/arkadaş - samimi üslup)",
            "  - Kamusal, Mesleki ve Eğitim alanı (resmî/ölçünlü dil).",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Ses, Beden Dili ve Görsel Ögelerle Sunum",
        [
            "• Diksiyon ve Boğumlama: Sesleri doğru çıkarma,",
            "  vurgu, tonlama ve durakları yerinde kullanma.",
            "• Beden Dili: Jest (el-kol-baş) ve mimikleri (yüz)",
            "  sözlü mesajla uyumlu ve doğal kullanma.",
            "• Dil İşlevleri: Göndergesel, alıcıyı harekete geçirme,",
            "  heyecana bağlı ve kanalı kontrol işlevlerinden yararlanma.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'İLETİŞİM ENGELLERİNİ KONU ALAN DRAMA (CANLANDIRMA) AŞAMALARI</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Hazırlık ve Isınma (Kurgu)",
        [
            "• Günlük yaşamdan bir iletişim",
            "  çatışması (örn. hasta-doktor,",
            "  veli-öğrenci, gişe memuru)",
            "  durumu seçilir.",
            "• Roller, mekân ve hedef kitle",
            "  belirlenir; konuşma taslağı",
            "  ve stratejisi oluşturulur.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Canlandırma (Rol Oynama)",
        [
            "• İlk sahnede iletişim engeli",
            "  (ön yargı, terim boğuntusu,",
            "  dinlememe) ve yol açtığı",
            "  yanlış anlaşılma sergilenir.",
            "• İkinci sahnede engel empati,",
            "  ortak dil ve etkin dinlemeyle",
            "  çözüme kavuşturulur.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Değerlendirme ve Yansıtma",
        [
            "• Dereceli puanlama anahtarı",
            "  ölçütleri: İçeriğe uygunluk,",
            "  özgünlük, canlandırma becerisi,",
            "  diksiyon ve beden dili uyumu.",
            "• Akran ve öz değerlendirme",
            "  geri bildirimleriyle konuşma",
            "  planına son şekli verilir.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
