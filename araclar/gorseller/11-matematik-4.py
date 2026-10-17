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
        'BAŞKALARI TARAFINDAN OLUŞTURULAN VERİLERİ TARTIŞMANIN 3 ADIMI (MAT.11.1.2)</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. İstatistiksel Temellendirme",
        [
            "• Veri kaynağı güvenilir mi?",
            "• Örneklem büyüklüğü (n) ve",
            "  temsil gücü yeterli mi?",
            "• Serpilme diyagramı ve r değeri",
            "  iddia edilen yön/güç ile",
            "  gerçekten uyumlu mu?",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Hata ve Yanlılık Tespiti",
        [
            "• Seçim yanlılığı var mı?",
            "• Eksen ölçekleriyle oynanarak",
            "  görsel yanıltma yapılmış mı?",
            "• Korelasyon, sebep-sonuç",
            "  (nedensellik) sanılmış mı?",
            "• Aralık dışı tahmin hatası var mı?",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Kabul Etme veya Çürütme",
        [
            "• Yöntem bilimsel, örneklem",
            "  temsili ve r yorumu doğruysa",
            "  sonuç KABUL EDİLİR.",
            "• Yanlı örneklem, gizli değişken",
            "  veya model hatası varsa",
            "  kanıtlarla ÇÜRÜTÜLÜR.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'EN YAYGIN İSTATİSTİKSEL YANILGI: KORELASYON NEDENSELLİK DEĞİLDİR!</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Korelasyon (Birlikte Değişim)",
        [
            "• İki nicel değişkenin (X ve Y) birlikte artma",
            "  veya azalma eğilimini gösterir (-1 <= r <= +1).",
            "• Ancak r'nin yüksek çıkması (örn. r = +0,88),",
            "  X'in doğrudan Y'nin sebebi olduğu anlamına",
            "  GELMEZ!",
            "• Örnek: Dondurma satışı (X) ile vantilatör",
            "  satışı (Y) arasında güçlü pozitif korelasyon vardır.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Gizli / Karıştırıcı Değişken (Z) Etkisi",
        [
            "• Hem X hem de Y değişkenini aynı anda etkileyen",
            "  üçüncü değişkene 'gizli (karıştırıcı) değişken' denir.",
            "• Dondurma satışı vantilatör satışına sebep olmaz;",
            "  her ikisini de artıran gerçek neden 'Hava Sıcaklığı'",
            "  (Z gizli değişkeni) artışıdır!",
            "• Gizli değişken göz ardı edilerek kurulan",
            "  sebep-sonuç iddiaları istatistiksel olarak ÇÜRÜTÜLÜR.",
        ],
        "#dc2626", "#fef2f2"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÖRNEKLEM YANLILIĞI, AYKIRI DEĞERLER VE GRAFİKSEL MANİPÜLASYON</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Örneklem Yanlılığı ve Aykırı Değer Etkisi",
        [
            "• Seçim Yanlılığı: Sadece spor kulübü üyelerinden",
            "  veri toplayıp tüm toplum için 'yaş ile koşu hızı'",
            "  modeli kurmak yanlıdır (temsil gücü yoktur).",
            "• Yetersiz Örneklem: 3-4 gözlemle genel yasa",
            "  iddia edilemez.",
            "• Aykırı Değer (Outlier): Tek bir uç nokta r'yi",
            "  yapay olarak yükseltebilir veya sıfıra çekebilir.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Eksen Kesme ve Ölçek Manipülasyonu",
        [
            "• Serpilme diyagramında dikey ekseni 0'dan",
            "  başlatmayıp çok dar bir aralıkta (örn. 98,1 - 98,5)",
            "  kesmek, çok önemsiz bir değişimi dev bir",
            "  artışmış gibi gösterir.",
            "• Yatay ekseni aşırı sıkıştırmak doğrunun eğimini",
            "  olduğundan çok dik gösterir.",
            "• İncelemede ilk iş eksen birimlerini kontrol etmektir!",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'DOĞRUSAL MODELDE TAHMİN SINIRLARI: İNTERPOLASYON VE EKSTRAPOLASYON</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "İnterpolasyon (Aralık İçi Tahmin - Güvenilir)",
        [
            "• Gözlemlenen en küçük ve en büyük veri aralığının",
            "  [x_min, x_max] İÇİNDEKİ bir değer için doğrusal",
            "  regresyon denklemiyle (y = a + bx) tahmin yapmaktır.",
            "• Örnek: 5-15 yaş arası çocukların boy verisinden",
            "  10 yaşındaki bir çocuğun boyunu tahmin etmek.",
            "• Model güçlü (|r| yüksek) ise KABUL EDİLİR.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Ekstrapolasyon (Aralık Dışı Tahmin - Riskli!)",
        [
            "• Gözlemlenen veri aralığının [x_min, x_max] ÇOK",
            "  DIŞINDAKİ bir değer için aynı doğrusal eğilimin",
            "  sonsuza dek süreceğini varsaymaktır.",
            "• Örnek: 0-15 yaş boy artış modelini (y = 50 + 6x)",
            "  kullanarak 50 yaşındaki kişinin 350 cm olacağını",
            "  iddia etmek! Bu tür iddialar ÇÜRÜTÜLÜR.",
        ],
        "#dc2626", "#fef2f2"
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
