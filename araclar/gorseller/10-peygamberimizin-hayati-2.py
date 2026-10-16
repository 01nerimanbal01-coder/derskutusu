from ozet_gorsel import svg


def _mekke_taif_karsilastirma():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">İslam Öncesinde Mekke ve Taif Şehirlerinin Karşılaştırılması</text>'
        '<rect x="20" y="42" width="305" height="172" rx="12" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="172" y="66" text-anchor="middle" font-size="13" font-weight="800" class="g-sf">MEKKE</text>'
        '<text x="36" y="90" font-size="10.5" class="g-y">• Hicaz\'ın batısında; sıcak ve kurak çöl iklimi</text>'
        '<text x="36" y="110" font-size="10.5" class="g-y">• Hâkim kabile: Kureyş Kabilesi</text>'
        '<text x="36" y="130" font-size="10.5" class="g-y">• Kâbe ve hac merkezi; kervan ticareti</text>'
        '<text x="36" y="150" font-size="10.5" class="g-y">• Baharat, kumaş ve değerli taş ticareti</text>'
        '<rect x="36" y="164" width="273" height="36" rx="6" fill="#fff"/>'
        '<text x="172" y="186" text-anchor="middle" font-size="10" font-weight="700" class="g-sf">Su kaynakları sınırlı, tarıma elverişsiz</text>'
        '<rect x="355" y="42" width="305" height="172" rx="12" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="507" y="66" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">TAİF (Vec Vadisi)</text>'
        '<text x="371" y="90" font-size="10.5" class="g-y">• Mekke\'nin 90 km doğusunda; 1,7 km rakım</text>'
        '<text x="371" y="110" font-size="10.5" class="g-y">• Hâkim kabile: Sakif Kabilesi (Hevazin kolu)</text>'
        '<text x="371" y="130" font-size="10.5" class="g-y">• Lat putu ve Beytürrabbe tapınağı</text>'
        '<text x="371" y="150" font-size="10.5" class="g-y">• Üzüm, zeytin, bal, dericilik ve Ukaz Panayırı</text>'
        '<rect x="371" y="164" width="273" height="36" rx="6" fill="#fff"/>'
        '<text x="507" y="186" text-anchor="middle" font-size="10" font-weight="700" class="g-yf">Bol yağışlı, yazları serin, zengin su ve tarım</text>'
    )
    return svg(680, 228, ic, "İslam öncesi Mekke ve Taif karşılaştırması")


def _taif_yolculugu_sureci():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Taif Yolculuğu Öncesi ve Sırasındaki Gelişmeler (616–620)</text>'
        '<rect x="16" y="44" width="150" height="156" rx="10" class="g-ka" stroke="#b91c1c" stroke-width="1.5"/>'
        '<text x="91" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-kf">1. Boykot (616-619)</text>'
        '<text x="91" y="90" text-anchor="middle" font-size="10" class="g-y">Ebu Talib Mahallesi\'nde</text>'
        '<text x="91" y="106" text-anchor="middle" font-size="10" class="g-y">3 yıl ekonomik ve</text>'
        '<text x="91" y="122" text-anchor="middle" font-size="10" class="g-y">sosyal abluka;</text>'
        '<text x="91" y="138" text-anchor="middle" font-size="10" class="g-y">güve olayı ile</text>'
        '<text x="91" y="154" text-anchor="middle" font-size="10" class="g-y">619\'da sona erdi.</text>'
        '<rect x="180" y="44" width="150" height="156" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="255" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-sf">2. Hüzün Yılı (620)</text>'
        '<text x="255" y="90" text-anchor="middle" font-size="10" class="g-y">Hz. Hatice ve</text>'
        '<text x="255" y="106" text-anchor="middle" font-size="10" class="g-y">Ebu Talib\'in vefatı;</text>'
        '<text x="255" y="122" text-anchor="middle" font-size="10" class="g-y">Mekke\'de baskıların</text>'
        '<text x="255" y="138" text-anchor="middle" font-size="10" class="g-y">artması ve yeni</text>'
        '<text x="255" y="154" text-anchor="middle" font-size="10" class="g-y">merkez arayışı.</text>'
        '<rect x="344" y="44" width="150" height="156" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="419" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mf">3. Taif Ziyareti (620)</text>'
        '<text x="419" y="90" text-anchor="middle" font-size="10" class="g-y">Zeyd b. Harise ile</text>'
        '<text x="419" y="106" text-anchor="middle" font-size="10" class="g-y">Sakif liderlerine davet;</text>'
        '<text x="419" y="122" text-anchor="middle" font-size="10" class="g-y">Abdi Yalil, Mesud ve</text>'
        '<text x="419" y="138" text-anchor="middle" font-size="10" class="g-y">Habib\'in reddi ve</text>'
        '<text x="419" y="154" text-anchor="middle" font-size="10" class="g-y">taşlı saldırı.</text>'
        '<rect x="508" y="44" width="156" height="156" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="586" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-yf">4. Dua ve Dönüş</text>'
        '<text x="586" y="90" text-anchor="middle" font-size="10" class="g-y">Utbe ve Şeybe\'nin</text>'
        '<text x="586" y="106" text-anchor="middle" font-size="10" class="g-y">bağında dua; Addas\'ın</text>'
        '<text x="586" y="122" text-anchor="middle" font-size="10" class="g-y">imanı; helak yerine</text>'
        '<text x="586" y="138" text-anchor="middle" font-size="10" class="g-y">hidayet duası ve Mut\'im</text>'
        '<text x="586" y="154" text-anchor="middle" font-size="10" class="g-y">b. Adiy\'in emanı.</text>'
    )
    return svg(680, 214, ic, "Taif yolculuğu süreci ve aşamaları")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 1:
        b[1]["gorsel"] = _mekke_taif_karsilastirma()
    if len(b) > 4:
        b[4]["gorsel"] = _taif_yolculugu_sureci()
