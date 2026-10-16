from ozet_gorsel import svg


def _sunger_sehir_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'Sünger Şehir Modelinin (Yeşil Altyapı) 5 Temel Bileşeni</text>'
        # Üst 3 kutu
        '<rect x="14" y="32" width="144" height="76" rx="8" class="g-ya"/>'
        '<text x="86" y="49" text-anchor="middle" font-size="10.5" font-weight="700" class="g-yf">'
        '1 · Erken Tasarım</text>'
        '<text x="86" y="65" text-anchor="middle" font-size="9.5" class="g-y">Kentsel dönüşümde</text>'
        '<text x="86" y="79" text-anchor="middle" font-size="9.5" class="g-y">geçirgen ve yeşil dokuyu</text>'
        '<text x="86" y="93" text-anchor="middle" font-size="9.5" class="g-y">baştan plana katmak</text>'

        '<rect x="168" y="32" width="144" height="76" rx="8" class="g-ma"/>'
        '<text x="240" y="49" text-anchor="middle" font-size="10.5" font-weight="700" class="g-mf">'
        '2 · Kaynağında Yönetim</text>'
        '<text x="240" y="65" text-anchor="middle" font-size="9.5" class="g-y">Yağmur suyunu yüzey</text>'
        '<text x="240" y="79" text-anchor="middle" font-size="9.5" class="g-y">akışına geçmeden düştüğü</text>'
        '<text x="240" y="93" text-anchor="middle" font-size="9.5" class="g-y">yerde tutmak</text>'

        '<rect x="322" y="32" width="144" height="76" rx="8" class="g-sa"/>'
        '<text x="394" y="49" text-anchor="middle" font-size="10.5" font-weight="700" class="g-sf">'
        '3 · Su Hasadı</text>'
        '<text x="394" y="65" text-anchor="middle" font-size="9.5" class="g-y">Yüzey suyunu biriktirip</text>'
        '<text x="394" y="79" text-anchor="middle" font-size="9.5" class="g-y">bitkilerle filtreleyerek</text>'
        '<text x="394" y="93" text-anchor="middle" font-size="9.5" class="g-y">yeniden kullanmak</text>'

        # Alt 2 kutu
        '<rect x="44" y="120" width="184" height="74" rx="8" class="g-ta"/>'
        '<text x="136" y="138" text-anchor="middle" font-size="10.5" font-weight="700" class="g-tf">'
        '4 · Doğa Tabanlı Arıtım</text>'
        '<text x="136" y="154" text-anchor="middle" font-size="9.5" class="g-y">Kirli yüzey sularını düşük</text>'
        '<text x="136" y="168" text-anchor="middle" font-size="9.5" class="g-y">maliyetli ekolojik yöntemlerle</text>'
        '<text x="136" y="182" text-anchor="middle" font-size="9.5" class="g-y">iyileştirmek</text>'

        '<rect x="252" y="120" width="184" height="74" rx="8" class="g-ya"/>'
        '<text x="344" y="138" text-anchor="middle" font-size="10.5" font-weight="700" class="g-yf">'
        '5 · Doğal Yeşil Drenaj</text>'
        '<text x="344" y="154" text-anchor="middle" font-size="9.5" class="g-y">Doğal havza akışını taklit</text>'
        '<text x="344" y="168" text-anchor="middle" font-size="9.5" class="g-y">eden sürdürülebilir drenaj</text>'
        '<text x="344" y="182" text-anchor="middle" font-size="9.5" class="g-y">zinciri kurmak</text>'
    )
    return svg(480, 204, ic, "Sünger şehir modelinin beş temel bileşeni")


def _web_cbs_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'Web Tabanlı CBS Uygulamalarının Çalışma Mimarisi</text>'
        # Sol: Kullanıcı
        '<rect x="16" y="38" width="132" height="106" rx="10" class="g-ma"/>'
        '<text x="82" y="58" text-anchor="middle" font-size="11" font-weight="700" class="g-mf">'
        'KULLANICI (İstemci)</text>'
        '<text x="82" y="76" text-anchor="middle" font-size="9.5" class="g-y">• Web Tarayıcısı</text>'
        '<text x="82" y="92" text-anchor="middle" font-size="9.5" class="g-y">• Akıllı Telefon / Tablet</text>'
        '<text x="82" y="108" text-anchor="middle" font-size="9.5" class="g-y">• Veri Girişi / Sorgu</text>'
        '<text x="82" y="124" text-anchor="middle" font-size="9.5" class="g-y">• Harita Görüntüleme</text>'

        # Orta: Genel Ağ
        '<rect x="184" y="54" width="112" height="74" rx="10" class="g-sa"/>'
        '<text x="240" y="80" text-anchor="middle" font-size="11" font-weight="700" class="g-sf">'
        'GENEL AĞ</text>'
        '<text x="240" y="98" text-anchor="middle" font-size="9.5" class="g-y">Web Teknolojileri</text>'
        '<text x="240" y="113" text-anchor="middle" font-size="9.5" class="g-y">ve Bulut İletişimi</text>'

        # Sağ: Sunucu
        '<rect x="332" y="38" width="132" height="106" rx="10" class="g-ya"/>'
        '<text x="398" y="58" text-anchor="middle" font-size="11" font-weight="700" class="g-yf">'
        'SUNUCU (Bulut)</text>'
        '<text x="398" y="76" text-anchor="middle" font-size="9.5" class="g-y">• Veri Depolama</text>'
        '<text x="398" y="92" text-anchor="middle" font-size="9.5" class="g-y">• Mekânsal Çözümleme</text>'
        '<text x="398" y="108" text-anchor="middle" font-size="9.5" class="g-y">• Katmanlar (Vektör/Raster)</text>'
        '<text x="398" y="124" text-anchor="middle" font-size="9.5" class="g-y">• Öz Nitelik Tablosu</text>'

        # Oklar
        '<path d="M 150 74 L 180 74" fill="none" class="g-ms" stroke-width="2"/>'
        '<polygon points="183,74 176,70 176,78" class="g-mf"/>'
        '<text x="166" y="67" text-anchor="middle" font-size="8.5" font-weight="700" class="g-mf">Komut</text>'

        '<path d="M 298 74 L 328 74" fill="none" class="g-ms" stroke-width="2"/>'
        '<polygon points="331,74 324,70 324,78" class="g-mf"/>'
        '<text x="314" y="67" text-anchor="middle" font-size="8.5" font-weight="700" class="g-mf">İstek</text>'

        '<path d="M 330 108 L 300 108" fill="none" class="g-ys" stroke-width="2"/>'
        '<polygon points="297,108 304,104 304,112" class="g-yf"/>'
        '<text x="314" y="121" text-anchor="middle" font-size="8.5" font-weight="700" class="g-yf">Yanıt</text>'

        '<path d="M 182 108 L 152 108" fill="none" class="g-ys" stroke-width="2"/>'
        '<polygon points="149,108 156,104 156,112" class="g-yf"/>'
        '<text x="166" y="121" text-anchor="middle" font-size="8.5" font-weight="700" class="g-yf">Harita</text>'

        # Alt bilgi şeridi
        '<rect x="16" y="156" width="448" height="36" rx="8" class="g-ta"/>'
        '<text x="240" y="172" text-anchor="middle" font-size="10" font-weight="700" class="g-tf">'
        'Katman Yapısı: Vektör (Nokta, Çizgi, Poligon + Öz Nitelik Tablosu) · Raster (Uydu Görüntüsü)</text>'
        '<text x="240" y="186" text-anchor="middle" font-size="9.5" class="g-y">'
        'Çıktı Formatları: Etkileşimli Harita · Grafik · İstatistiksel Tablo</text>'
    )
    return svg(480, 202, ic, "Web tabanlı CBS uygulamalarının temel bileşenleri")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _sunger_sehir_svg()
    if len(b) > 3:
        b[3]["gorsel"] = _web_cbs_svg()
