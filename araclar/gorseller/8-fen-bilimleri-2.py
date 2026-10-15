from ozet_gorsel import svg


def g1():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-m"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">IŞIK AÇISI DENEY DÜZENEĞİ VE DEĞİŞKEN ANALİZİ</text>'
        '<rect x="14" y="54" width="168" height="152" rx="8" class="g-sa"/>'
        '<text x="98" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">1. DÜZENEK (EĞİK)</text>'
        '<line x1="36" y1="92" x2="150" y2="122" class="g-ss" stroke-width="2" stroke-dasharray="4 3"/>'
        '<line x1="36" y1="106" x2="150" y2="136" class="g-ss" stroke-width="2" stroke-dasharray="4 3"/>'
        '<text x="98" y="160" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Geniş Alan · Az Enerji</text>'
        '<text x="98" y="184" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">Düşük Sıcaklık Artışı</text>'
        '<rect x="192" y="54" width="168" height="152" rx="8" class="g-ta"/>'
        '<text x="276" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">2. DÜZENEK (DİK)</text>'
        '<line x1="256" y1="90" x2="256" y2="134" class="g-ts" stroke-width="2" stroke-dasharray="4 3"/>'
        '<line x1="296" y1="90" x2="296" y2="134" class="g-ts" stroke-width="2" stroke-dasharray="4 3"/>'
        '<text x="276" y="160" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Dar Alan · Çok Enerji</text>'
        '<text x="276" y="184" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">Yüksek Sıcaklık Artışı</text>'
        '<rect x="370" y="54" width="176" height="46" rx="8" class="g-ma"/>'
        '<text x="458" y="73" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">BAĞIMSIZ DEĞİŞKEN</text>'
        '<text x="458" y="91" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Işığın Düşme Açısı</text>'
        '<rect x="370" y="107" width="176" height="46" rx="8" class="g-ya"/>'
        '<text x="458" y="126" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">BAĞIMLI DEĞİŞKEN</text>'
        '<text x="458" y="144" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Termometre Sıcaklığı</text>'
        '<rect x="370" y="160" width="176" height="46" rx="8" class="g-la"/>'
        '<text x="458" y="179" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">KONTROL DEĞİŞKENİ</text>'
        '<text x="458" y="197" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Mesafe ve Süre (10 dk)</text>'
    )
    return svg(w, h, ic, "Işık açısı deney düzeneği ve değişken analizi şeması")


def g2():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-t"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">DÖNENCELER VE GÜNEŞ IŞINLARININ DİK DÜŞTÜĞÜ TARİHLER</text>'
        '<rect x="14" y="54" width="532" height="34" rx="6" class="g-la"/>'
        '<text x="280" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">Kuzey Orta Kuşak (Türkiye): Işınlar hiçbir zaman dik (90°) düşmez (0 kez)</text>'
        '<rect x="14" y="96" width="532" height="34" rx="6" class="g-sa"/>'
        '<text x="280" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">Yengeç Dönencesi (Kuzey): Yılda 1 kez dik düşer (21 Haziran öğle vakti)</text>'
        '<rect x="14" y="138" width="532" height="34" rx="6" class="g-ya"/>'
        '<text x="280" y="160" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">Ekvator Çizgisi: Yılda 2 kez dik düşer (21 Mart ve 23 Eylül öğle vakti)</text>'
        '<rect x="14" y="180" width="532" height="34" rx="6" class="g-ma"/>'
        '<text x="280" y="202" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">Oğlak Dönencesi (Güney): Yılda 1 kez dik düşer (21 Aralık öğle vakti)</text>'
    )
    return svg(w, h, ic, "Dönenceler ve Güneş ışınlarının dik düştüğü tarihler şeması")


def g3():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-y"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-yf">KUZEY YARIM KÜRE GECE VE GÜNDÜZ SÜRESİ DEĞİŞİMİ</text>'
        '<rect x="14" y="54" width="124" height="96" rx="8" class="g-ta"/>'
        '<text x="76" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">21 HAZİRAN</text>'
        '<text x="76" y="98" text-anchor="middle" font-size="12" font-weight="700" class="g-y">En Uzun Gündüz</text>'
        '<text x="76" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Yaz Başlangıcı</text>'
        '<text x="76" y="138" text-anchor="middle" font-size="12" font-weight="600" class="g-tf">(Yengeç\'e Dik)</text>'
        '<rect x="150" y="54" width="124" height="96" rx="8" class="g-sa"/>'
        '<text x="212" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">23 EYLÜL</text>'
        '<text x="212" y="98" text-anchor="middle" font-size="12" font-weight="700" class="g-y">12 Saat Eşitlik</text>'
        '<text x="212" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Sonbahar Başlar</text>'
        '<text x="212" y="138" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">(Ekvator\'a Dik)</text>'
        '<rect x="286" y="54" width="124" height="96" rx="8" class="g-ma"/>'
        '<text x="348" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">21 ARALIK</text>'
        '<text x="348" y="98" text-anchor="middle" font-size="12" font-weight="700" class="g-y">En Uzun Gece</text>'
        '<text x="348" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Kış Başlangıcı</text>'
        '<text x="348" y="138" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">(Oğlak\'a Dik)</text>'
        '<rect x="422" y="54" width="124" height="96" rx="8" class="g-ya"/>'
        '<text x="484" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">21 MART</text>'
        '<text x="484" y="98" text-anchor="middle" font-size="12" font-weight="700" class="g-y">12 Saat Eşitlik</text>'
        '<text x="484" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">İlkbahar Başlar</text>'
        '<text x="484" y="138" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">(Ekvator\'a Dik)</text>'
        '<rect x="14" y="160" width="260" height="48" rx="8" class="g-la"/>'
        '<text x="144" y="180" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">21 Haziran → 21 Aralık Arası</text>'
        '<text x="144" y="198" text-anchor="middle" font-size="12" font-weight="600" class="g-y">KYK\'de gündüzler kısalır, geceler uzar</text>'
        '<rect x="286" y="160" width="260" height="48" rx="8" class="g-ya"/>'
        '<text x="416" y="180" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">21 Aralık → 21 Haziran Arası</text>'
        '<text x="416" y="198" text-anchor="middle" font-size="12" font-weight="600" class="g-y">KYK\'de gündüzler uzar, geceler kısalır</text>'
    )
    return svg(w, h, ic, "Kuzey Yarım Küre gece ve gündüz süresi değişimi şeması")


def g4():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-l"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-lf">YARIM KÜRELERE GÖRE ÖĞLE VAKTİ GÖLGE BOYU VE SICAKLIK</text>'
        '<rect x="14" y="54" width="258" height="152" rx="8" class="g-ma"/>'
        '<text x="143" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">KUZEY YARIM KÜRE (TÜRKİYE)</text>'
        '<rect x="26" y="88" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="143" y="109" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">21 Haziran: En Kısa Gölge (Yaz)</text>'
        '<rect x="26" y="128" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="143" y="149" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">21 Aralık: En Uzun Gölge (Kış)</text>'
        '<text x="143" y="186" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Haziran-Temmuz-Ağustos En Sıcak</text>'
        '<rect x="288" y="54" width="258" height="152" rx="8" class="g-sa"/>'
        '<text x="417" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">GÜNEY YARIM KÜRE</text>'
        '<rect x="300" y="88" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="417" y="109" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">21 Haziran: En Uzun Gölge (Kış)</text>'
        '<rect x="300" y="128" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="417" y="149" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">21 Aralık: En Kısa Gölge (Yaz)</text>'
        '<text x="417" y="186" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Aralık-Ocak-Şubat En Sıcak</text>'
    )
    return svg(w, h, ic, "Yarım kürelere göre öğle vakti gölge boyu ve sıcaklık karşılaştırması")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[1]["gorsel"] = g2()
    b[2]["gorsel"] = g3()
    b[4]["gorsel"] = g4()

