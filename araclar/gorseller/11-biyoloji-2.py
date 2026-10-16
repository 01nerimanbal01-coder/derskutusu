from ozet_gorsel import svg


def _bitkisel_hormonlar_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'Bitkisel Hormonların Temel İşlevleri</text>'
        # Büyümeyi teşvik edenler (Üst sıra - 3 kutu)
        '<rect x="14" y="32" width="144" height="78" rx="8" class="g-ya"/>'
        '<text x="86" y="50" text-anchor="middle" font-size="11" font-weight="700" class="g-yf">OKSİN</text>'
        '<text x="86" y="66" text-anchor="middle" font-size="9.5" class="g-y">• Boyca uzama ve ışığa yönelme</text>'
        '<text x="86" y="81" text-anchor="middle" font-size="9.5" class="g-y">• Yan kök ve çelik köklendirme</text>'
        '<text x="86" y="96" text-anchor="middle" font-size="9.5" class="g-y">• Çilekte aken kaynaklı büyüme</text>'

        '<rect x="168" y="32" width="144" height="78" rx="8" class="g-ma"/>'
        '<text x="240" y="50" text-anchor="middle" font-size="11" font-weight="700" class="g-mf">SİTOKİNİN</text>'
        '<text x="240" y="66" text-anchor="middle" font-size="9.5" class="g-y">• Hücre bölünmesi (sitokinez)</text>'
        '<text x="240" y="81" text-anchor="middle" font-size="9.5" class="g-y">• Yan tomurcuktan dal gelişimi</text>'
        '<text x="240" y="96" text-anchor="middle" font-size="9.5" class="g-y">• Yaşlanmayı geciktirme</text>'

        '<rect x="322" y="32" width="144" height="78" rx="8" class="g-sa"/>'
        '<text x="394" y="50" text-anchor="middle" font-size="11" font-weight="700" class="g-sf">GİBERELLİN</text>'
        '<text x="394" y="66" text-anchor="middle" font-size="9.5" class="g-y">• Gövde uzaması (cüceliği önler)</text>'
        '<text x="394" y="81" text-anchor="middle" font-size="9.5" class="g-y">• Dormansiyi kırıp çimlendirme</text>'
        '<text x="394" y="96" text-anchor="middle" font-size="9.5" class="g-y">• İri ve çekirdeksiz üzüm</text>'

        # Stres ve olgunlaşma (Alt sıra - 2 kutu)
        '<rect x="36" y="122" width="192" height="78" rx="8" class="g-ta"/>'
        '<text x="132" y="140" text-anchor="middle" font-size="11" font-weight="700" class="g-tf">'
        'ABSİSİK ASİT (ABA)</text>'
        '<text x="132" y="156" text-anchor="middle" font-size="9.5" class="g-y">• Kuraklıkta stomaları kapatır</text>'
        '<text x="132" y="171" text-anchor="middle" font-size="9.5" class="g-y">• Büyümeyi ve çimlenmeyi durdurur</text>'
        '<text x="132" y="186" text-anchor="middle" font-size="9.5" class="g-y">• Tohum/tomurcukta uyku hâli (dormansi)</text>'

        '<rect x="252" y="122" width="192" height="78" rx="8" class="g-ka"/>'
        '<text x="348" y="140" text-anchor="middle" font-size="11" font-weight="700" class="g-kf">'
        'ETİLEN (Gaz Hormon)</text>'
        '<text x="348" y="156" text-anchor="middle" font-size="9.5" class="g-y">• Difüzyonla havaya yayılır</text>'
        '<text x="348" y="171" text-anchor="middle" font-size="9.5" class="g-y">• Meyveyi yumuşatır ve tatlandırır</text>'
        '<text x="348" y="186" text-anchor="middle" font-size="9.5" class="g-y">• Stres tepkisi ve yaprak dökümü</text>'
    )
    return svg(480, 210, ic, "Beş temel bitkisel hormon ve görevleri")


def _tropizma_nasti_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'Bitkilerde Tepki Mekanizmaları: Tropizma ve Nasti</text>'
        # Sol: Tropizma
        '<rect x="16" y="32" width="218" height="168" rx="10" class="g-ya"/>'
        '<text x="125" y="50" text-anchor="middle" font-size="11.5" font-weight="700" class="g-yf">'
        'TROPİZMA (Yönelim)</text>'
        '<text x="125" y="66" text-anchor="middle" font-size="10" font-weight="600" class="g-y">'
        'Uyaranın yönüne bağlıdır (+ / -)</text>'
        '<text x="125" y="81" text-anchor="middle" font-size="9.5" class="g-y">'
        'Hormon (oksin) ve asimetrik büyüme</text>'
        '<line x1="30" y1="90" x2="220" y2="90" class="g-ys" stroke-width="1"/>'
        '<text x="30" y="107" font-size="9.5" class="g-y">• Fototropizma: Işığa yönelim</text>'
        '<text x="30" y="124" font-size="9.5" class="g-y">• Geotropizma: Yer çekimine yönelim</text>'
        '<text x="30" y="141" font-size="9.5" class="g-y">• Hidrotropizma: Suya yönelim</text>'
        '<text x="30" y="158" font-size="9.5" class="g-y">• Kemotropizma: Kimyasala yönelim</text>'
        '<text x="30" y="175" font-size="9.5" class="g-y">• Haptotropizma: Desteğe sarılma</text>'

        # Sağ: Nasti
        '<rect x="246" y="32" width="218" height="168" rx="10" class="g-ma"/>'
        '<text x="355" y="50" text-anchor="middle" font-size="11.5" font-weight="700" class="g-mf">'
        'NASTİ (Irganım)</text>'
        '<text x="355" y="66" text-anchor="middle" font-size="10" font-weight="600" class="g-y">'
        'Uyaranın yönüne bağlı değildir</text>'
        '<text x="355" y="81" text-anchor="middle" font-size="9.5" class="g-y">'
        'Ani turgor basıncı değişimi (Hızlı)</text>'
        '<line x1="260" y1="90" x2="450" y2="90" class="g-ms" stroke-width="1"/>'
        '<text x="260" y="112" font-size="9.5" class="g-y">• Fotonasti: Akşamsefası çiçeğinin</text>'
        '<text x="268" y="126" font-size="9.5" class="g-y">düşük ışıkta açılıp yüksekte kapanması</text>'
        '<text x="260" y="146" font-size="9.5" class="g-y">• Sismonasti: Küstüm otu ve Venüs</text>'
        '<text x="268" y="160" font-size="9.5" class="g-y">sinekkapanın dokunmayla kapanması</text>'
        '<text x="260" y="180" font-size="9.5" class="g-y">• Termonasti: Lale ve safranın 15-20 °C</text>'
        '<text x="268" y="194" font-size="9.5" class="g-y">sıcaklıkta açılıp 5-10 °C\'ta kapanması</text>'
    )
    return svg(480, 210, ic, "Tropizma ve nasti hareketlerinin karşılaştırılması")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 2:
        b[2]["gorsel"] = _bitkisel_hormonlar_svg()
    if len(b) > 5:
        b[5]["gorsel"] = _tropizma_nasti_svg()
