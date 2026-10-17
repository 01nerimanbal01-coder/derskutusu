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
        '<rect x="5" y="5" width="750" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'KOLEOPTİL DENEYLERİ: DARWIN, BOYSEN-JENSEN VE WENT BULGULARI</text>'
    )
    ic += _kart(
        20, 42, 230, 203,
        "1. Darwin Deneyi (Uç Algısı)",
        [
            "• Ucu kesilen veya ışık geçirmeyen",
            "  başlıkla kapatılan koleoptil",
            "  ışığa YÖNELMEZ.",
            "• Alt kısmı kapatılıp ucu açık",
            "  bırakılan koleoptil ışığa",
            "  YÖNELİR.",
            "• Sonuç: Işık koleoptil ucunda",
            "  algılanır.",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 203,
        "2. Boysen-Jensen (Mika/Agar)",
        [
            "• Uç ile gövde arasına jelatin/",
            "  agar konursa oksin geçer ve",
            "  ışığa YÖNELİR.",
            "• Mika (geçirimsiz) levha ışık",
            "  alan tarafa konursa YÖNELİR;",
            "  karanlık tarafa konursa oksin",
            "  inemez ve YÖNELMEZ!",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 203,
        "3. Paál ve Went (Asimetri)",
        [
            "• Karanlık ortamda ucu kesilen",
            "  koleoptilin soluna oksinli agar",
            "  bloğu konursa sol taraf hızlı",
            "  uzar ve SAĞA yönelir!",
            "• Sonuç: Yönelmenin sebebi",
            "  oksin hormonunun asimetrik",
            "  dağılımı ve mitoz/uzamadır.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 270, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'GEOTROPİZMA DENEYLERİ VE KLİNOSTAT DÜZENEĞİNİN İŞLEVİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Sabit Yatay Saksı (Normal Geotropizma)",
        [
            "• Yatay yatırılan sabit saksıda yer çekimi etkisiyle",
            "  oksin hormonu hem gövdede hem kökte alt",
            "  yüzeyde daha yoğun birikir.",
            "• Gövdede yüksek oksin büyümeyi hızlandırır →",
            "  Gövde yukarı kıvrılır (Negatif Geotropizma).",
            "• Kökte yüksek oksin büyümeyi baskılar (üst yüzey",
            "  daha hızlı uzar) → Kök aşağı kıvrılır (Pozitif).",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Klinostat Düzeneği (Dönen Saksı Deneyi)",
        [
            "• Klinostat: Bitkiyi yatay eksende sabit hızla",
            "  döndürerek yer çekiminin veya ışığın tek yönlü",
            "  etkisini ortadan kaldıran laboratuvar cihazıdır.",
            "• Yatay dönen klinostatta oksin hormonu gövde",
            "  ve kökün her tarafına EŞİT (simetrik) dağılır.",
            "• SONUÇ: Asimetrik büyüme olmaz; gövde ve kök",
            "  kıvrılmadan yatay doğrultuda DÜZ uzamaya devam eder!",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'TROPİZMA DENEY TASARIMINDA DEĞİŞKENLERİN BELİRLENMESİ</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Bağımsız Değişken (Neden)",
        [
            "• Araştırmacının deneyde bilerek",
            "  değiştirdiği uyaran faktörüdür.",
            "• Fototropizma deneyinde:",
            "  Işığın geliş yönü (tek yönlü",
            "  ışık / üstten ışık).",
            "• Geotropizmada: Yer çekimi",
            "  vektörünün yönü (sabit/klinostat).",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Bağımlı Değişken (Sonuç)",
        [
            "• Bağımsız değişkene bağlı olarak",
            "  gözlemlenen ve ölçülen tepkidir.",
            "• Deneydeki karşılığı:",
            "  Bitki sürgün veya kökünün",
            "  yönelme (kıvrılma) açısı,",
            "  yönelme yönü ve asimetrik",
            "  uzama miktarı.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Kontrol Değişkenleri (Sabit)",
        [
            "• Deney ve kontrol gruplarında",
            "  eşit tutulan tüm şartlardır:",
            "  - Tohum/fide türü ve yaşı",
            "  - Ortam sıcaklığı ve nemi",
            "  - Toprak miktarı ve minerali",
            "  - Verilen su miktarı ve ışık",
            "    şiddeti / dalga boyu.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'REKABET DENEYLERİ: HİDROTROPİZMA > GEOTROPİZMA VE KEMOTROPİZMA</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Tel Elek Deneyi (Hidrotropizma vs Geotropizma)",
        [
            "• Nemli talaş dolu eğimli tel eleğe çimlenen",
            "  fasulye tohumları yerleştirilir.",
            "• Kök uçları önce yer çekimi etkisiyle tel",
            "  deliklerinden aşağı doğru çıkar (+ Geotropizma).",
            "• Ancak dışarıdaki kuru havayla karşılaşınca",
            "  tekrar yukarıdaki nemli talaşa doğru kıvrılır!",
            "• KANIT: Kökte Hidrotropizma > Geotropizmadır!",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Saksı İçi Kimyasal Uyaran (Kemotropizma)",
        [
            "• Saksının bir yanına mineral gübre (amonyum/",
            "  nitrat), diğer yanına kireç veya tuz konur.",
            "• Bitki kökleri gübreye doğru yönelirken",
            "  (+ Kemotropizma), kireç/tuzdan uzaklaşır",
            "  (- Kemotropizma).",
            "• Polen tüpünün dişicik borusunda yumurtaya",
            "  doğru büyümesi de pozitif kemotropizmadır.",
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
    v["bolumler"][3]["gorsel"] = GORSELLER["b4"]