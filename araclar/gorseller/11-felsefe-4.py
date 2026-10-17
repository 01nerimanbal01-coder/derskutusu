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
        'ÇEVRE SORUNLARIYLA İLGİLİ FELSEFİ ARGÜMAN OLUŞTURMA BASAMAKLARI (FEL.11.1.2)</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Problemi ve Kavramları Tanımlama",
        [
            "• İncelenen çevre sorunu (iklim",
            "  krizi, biyoçeşitlilik kaybı,",
            "  su kıtlığı, plastik kirliliği)",
            "  net biçimde ortaya konur.",
            "• İçsel değer, araçsal değer,",
            "  ekosistem ve sorumluluk",
            "  kavramları tanımlanır.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Öncülleri (Dayanakları) Kurma",
        [
            "• 1. Öncül (Etik İlke): Seçilen",
            "  çevre etiği yaklaşımının",
            "  (insan, canlı veya çevre",
            "  merkezci) temel normu yazılır.",
            "• 2. Öncül (Olgusal Durum):",
            "  İncelenen eylemin doğaya",
            "  ve canlılara etkisi belirtilir.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Sonuç Önermesi ve Tutarlılık",
        [
            "• Öncüllerden zorunlu veya",
            "  güçlü olarak çıkan ahlaki",
            "  yargı ('Öyleyse...') kurulur.",
            "• Karşıt görüşlerin olası",
            "  itirazları öngörülerek",
            "  mantıksal tutarlılıkla",
            "  cevaplandırılır.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ÜÇ ÇEVRE ETİĞİ YAKLAŞIMININ AYNI SORUNA FARKLI ARGÜMANLARI</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "İnsan Merkezci (Antroposentrik)",
        [
            "• Soru: Ormanlar neden korunmalı?",
            "• Argüman: 'Ormanlar yok olursa",
            "  insanlığın oksijen, su ve",
            "  ekonomik kaynakları tükenir; bu",
            "  yüzden insan refahı için",
            "  ormanlar korunmalıdır.'",
            "• Doğa: Araçsal değere sahiptir.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        265, 42, 230, 198,
        "Canlı Merkezci (Biyosentrik)",
        [
            "• Temsilciler: Schweitzer, Taylor,",
            "  Singer (Acı Duyma), Regan.",
            "• Argüman: 'Ormandaki her",
            "  ağacın ve hayvanın kendi",
            "  başına yaşama hakkı (içsel",
            "  değeri) vardır; onları yok",
            "  etmek ahlaken yanlıştır.'",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        510, 42, 230, 198,
        "Çevre Merkezci (Ekosentrik)",
        [
            "• Temsilciler: Leopold (Yeryüzü",
            "  Etiği), Naess (Derin Ekoloji).",
            "• Argüman: 'Orman; toprağı, suyu,",
            "  iklimi ve canlılarıyla bölünmez",
            "  bir ekosistem bütünüdür; biyotik",
            "  bütünlüğü bozan her eylem",
            "  ahlaken yanlıştır.'",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'GELECEK KUŞAKLARA KARŞI SORUMLULUK VE İKLİM ADALETİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Hans Jonas ve Sorumluluk İlkesi",
        [
            "• Geleneksel etik yalnızca 'şimdi ve burada'",
            "  yaşayan insanlar arasındaki ilişkiyi düzenliyordu.",
            "• Modern teknoloji ise bütün gezegenin geleceğini",
            "  yok edebilecek bir güce ulaştı.",
            "• Jonas'ın Eko-Koşulsuz Buyruğu:",
            "  'Öyle hareket et ki, eylemlerinin sonuçları yeryüzünde",
            "  gerçek insan yaşamının sürekliliğiyle bağdaşsın!'",
        ],
        "#7c3aed", "#f5f3ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Ekolojik Ayak İzi ve İklim Adaleti Argümanı",
        [
            "• Kuşaklararası Adalet: Dünya bize atalarımızdan",
            "  miras kalmadı; gelecek kuşaklardan ödünç alındı!",
            "• İklim Adaleti (Küresel Hakkaniyet): Sera gazlarını",
            "  en az üreten yoksul toplumlar ve canlı türleri,",
            "  iklim krizinin en ağır bedelini ödemektedir.",
            "• Sürdürülebilirlik, doğanın kendini yenileme",
            "  kapasitesini (taşıma sınırını) aşmamaktır.",
        ],
        "#2563eb", "#eff6ff"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'SIĞI (SHALLOW) EKOLOJİ İLE DERİN (DEEP) EKOLOJİ ARGÜMANLARININ FARKI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Sığ Ekoloji (Reformist / Aydınlanmış İnsan Merkezci)",
        [
            "• Tüketim ve büyüme odaklı mevcut yaşam tarzını",
            "  sorgulamadan yalnızca teknik önlemler (filtre,",
            "  geri dönüşüm, elektrikli araç) önerir.",
            "• Doğayı hâlâ 'insan için yönetilmesi gereken bir",
            "  kaynak stoğu' olarak görür.",
            "• Hedefi: Gelişmiş ülkelerdeki insanların sağlık",
            "  ve refah standartlarını korumaktır.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Derin Ekoloji (Arne Naess - Radikal Ekosentrik)",
        [
            "• Sorunun kökünde 'insanın doğanın efendisi olduğu'",
            "  yanılgısını görür; köklü zihniyet değişimi ister.",
            "• Biyosferik Eşitlik: Tüm yaşam formlarının",
            "  var olma ve serpiliş hakkı eşittir.",
            "• Çeşitlilik ve ortak yaşam (simbiyoz) en yüksek",
            "  değerdir; insan doğanın üstünde değil İÇİNDE",
            "  sıradan bir düğüm noktasıdır.",
        ],
        "#059669", "#ecfdf5"
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