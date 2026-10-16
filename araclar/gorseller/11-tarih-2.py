from ozet_gorsel import svg


def _kronoloji_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        'XVIII. Yüzyıl Osmanlı Siyasi ve Askerî Mücadeleleri (1711–1774)</text>'
        # 1711 Prut
        '<rect x="14" y="32" width="218" height="78" rx="8" class="g-ya"/>'
        '<text x="123" y="50" text-anchor="middle" font-size="11" font-weight="700" class="g-yf">'
        '1711 · Prut Antlaşması</text>'
        '<text x="123" y="66" text-anchor="middle" font-size="9.5" class="g-y">• Baltacı Mehmed Paşa kuşatması</text>'
        '<text x="123" y="81" text-anchor="middle" font-size="9.5" class="g-y">• Azak Kalesi geri alındı</text>'
        '<text x="123" y="96" text-anchor="middle" font-size="9.5" class="g-y">• Rusya\'nın Lehistan\'a müdahalesi önlendi</text>'

        # 1718 Pasarofça
        '<rect x="248" y="32" width="218" height="78" rx="8" class="g-ta"/>'
        '<text x="357" y="50" text-anchor="middle" font-size="11" font-weight="700" class="g-tf">'
        '1718 · Pasarofça Antlaşması</text>'
        '<text x="357" y="66" text-anchor="middle" font-size="9.5" class="g-y">• Mora Venedik\'ten geri alındı</text>'
        '<text x="357" y="81" text-anchor="middle" font-size="9.5" class="g-y">• Belgrad ve Temeşvar kaybedildi</text>'
        '<text x="357" y="96" text-anchor="middle" font-size="9.5" class="g-y">• Savunma siyaseti ve Lale Devri başladı</text>'

        # 1739 Belgrad
        '<rect x="14" y="122" width="218" height="78" rx="8" class="g-ma"/>'
        '<text x="123" y="140" text-anchor="middle" font-size="11" font-weight="700" class="g-mf">'
        '1739 · Belgrad Antlaşması</text>'
        '<text x="123" y="156" text-anchor="middle" font-size="9.5" class="g-y">• Hendesehane (1734) ve iki cephede zafer</text>'
        '<text x="123" y="171" text-anchor="middle" font-size="9.5" class="g-y">• Belgrad ve Tuna hattı geri alındı</text>'
        '<text x="123" y="186" text-anchor="middle" font-size="9.5" class="g-y">• Karadeniz son kez Türk gölü sayıldı</text>'

        # 1774 Küçük Kaynarca
        '<rect x="248" y="122" width="218" height="78" rx="8" class="g-ka"/>'
        '<text x="357" y="140" text-anchor="middle" font-size="11" font-weight="700" class="g-kf">'
        '1774 · Küçük Kaynarca Antlaşması</text>'
        '<text x="357" y="156" text-anchor="middle" font-size="9.5" class="g-y">• 1770 Çeşme ve Kartal (Kagul) yenilgileri</text>'
        '<text x="357" y="171" text-anchor="middle" font-size="9.5" class="g-y">• Kırım bağımsız oldu (Halifelik maddesi)</text>'
        '<text x="357" y="186" text-anchor="middle" font-size="9.5" class="g-y">• Ortodoks himayesi ve Rus gemi geçişi</text>'
    )
    return svg(480, 210, ic, "1711-1774 arası dört temel antlaşmanın karşılaştırması")


def _kucuk_kaynarca_svg():
    ic = (
        '<text x="240" y="20" text-anchor="middle" font-size="13" font-weight="700" class="g-y">'
        '1774 Küçük Kaynarca Antlaşması\'nın Çok Boyutlu Etkileri</text>'
        '<rect x="16" y="34" width="448" height="38" rx="8" class="g-ka"/>'
        '<text x="28" y="51" font-size="11" font-weight="700" class="g-kf">1 · Kırım ve Halifelik Boyutu</text>'
        '<text x="28" y="65" font-size="10" class="g-y">'
        'Kırım siyasi bakımdan bağımsız oldu (1783\'te ilhak edildi); dinî yönden Halife\'ye bağlı kaldı.</text>'

        '<rect x="16" y="80" width="448" height="38" rx="8" class="g-ta"/>'
        '<text x="28" y="97" font-size="11" font-weight="700" class="g-tf">2 · Denizler ve Ticaret Boyutu</text>'
        '<text x="28" y="111" font-size="10" class="g-y">'
        'Azak, Kerç ve Yenikale Rusya\'ya verildi; Rus ticaret gemilerine Karadeniz ve Boğazlar açıldı.</text>'

        '<rect x="16" y="126" width="448" height="38" rx="8" class="g-sa"/>'
        '<text x="28" y="143" font-size="11" font-weight="700" class="g-sf">3 · Diplomatik Müdahale Boyutu</text>'
        '<text x="28" y="157" font-size="10" class="g-y">'
        'Osmanlı Ortodoks tebaasının koruyuculuğu maddesiyle Rusya iç işlere karışma zemini buldu.</text>'

        '<rect x="16" y="172" width="448" height="34" rx="8" class="g-ma"/>'
        '<text x="28" y="188" font-size="11" font-weight="700" class="g-mf">4 · Mali Boyut:</text>'
        '<text x="120" y="188" font-size="10" class="g-y">'
        'Osmanlı Devleti tarihinde ilk kez Rusya\'ya ağır bir savaş tazminatı ödemeyi kabul etti.</text>'
    )
    return svg(480, 214, ic, "Küçük Kaynarca Antlaşması'nın dört temel sonucu")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 2:
        b[2]["gorsel"] = _kronoloji_svg()
    if len(b) > 4:
        b[4]["gorsel"] = _kucuk_kaynarca_svg()
