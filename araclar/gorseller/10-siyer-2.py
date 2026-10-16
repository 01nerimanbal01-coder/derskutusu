from ozet_gorsel import svg


def _mekke_kronoloji():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">İslam Öncesi Mekke Tarihinde Hâkimiyet ve İnanç Değişimi</text>'
        '<rect x="16" y="44" width="150" height="154" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="91" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-yf">1. Kuruluş &amp; Tevhit</text>'
        '<text x="91" y="88" text-anchor="middle" font-size="10" class="g-y">Zemzem suyunun çıkışı,</text>'
        '<text x="91" y="104" text-anchor="middle" font-size="10" class="g-y">Hz. İbrahim ve Hz. İsmail\'in</text>'
        '<text x="91" y="120" text-anchor="middle" font-size="10" class="g-y">Kâbe\'yi inşası;</text>'
        '<text x="91" y="138" text-anchor="middle" font-size="10" font-weight="700" class="g-yf">Harem Bölgesi ve Tevhit</text>'
        '<rect x="180" y="44" width="150" height="154" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="255" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mf">2. Cürhümlüler</text>'
        '<text x="255" y="88" text-anchor="middle" font-size="10" class="g-y">Hz. İsmail ile akrabalık</text>'
        '<text x="255" y="104" text-anchor="middle" font-size="10" class="g-y">kurarak şehre hâkim</text>'
        '<text x="255" y="120" text-anchor="middle" font-size="10" class="g-y">olan ilk kabile;</text>'
        '<text x="255" y="138" text-anchor="middle" font-size="10" font-weight="700" class="g-mf">Zamanla tevhitten uzaklaşma</text>'
        '<rect x="344" y="44" width="150" height="154" rx="10" class="g-ka" stroke="#b91c1c" stroke-width="1.5"/>'
        '<text x="419" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-kf">3. Huzaalılar (3 Asır)</text>'
        '<text x="419" y="88" text-anchor="middle" font-size="10" class="g-y">Reisleri Amr bin Luhay\'ın</text>'
        '<text x="419" y="104" text-anchor="middle" font-size="10" class="g-y">Şam\'dan put getirip</text>'
        '<text x="419" y="120" text-anchor="middle" font-size="10" class="g-y">Kâbe\'ye yerleştirmesi;</text>'
        '<text x="419" y="138" text-anchor="middle" font-size="10" font-weight="700" class="g-kf">Putperestliğin (Hübel) yayılışı</text>'
        '<rect x="508" y="44" width="156" height="154" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="586" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-sf">4. Kureyşliler</text>'
        '<text x="586" y="88" text-anchor="middle" font-size="10" class="g-y">Darünnedve meclisi,</text>'
        '<text x="586" y="104" text-anchor="middle" font-size="10" class="g-y">Kâbe görev paylaşımı,</text>'
        '<text x="586" y="120" text-anchor="middle" font-size="10" class="g-y">yaz-kış ticaret kervanları</text>'
        '<text x="586" y="138" text-anchor="middle" font-size="10" font-weight="700" class="g-sf">ve Fil Vakası zaferi</text>'
    )
    return svg(680, 212, ic, "İslam öncesi Mekke tarihinde kabile hâkimiyeti ve inanç değişimi")


def _hicaz_uc_sehir():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Hicaz Bölgesinin Üç Önemli Şehri: Mekke, Taif ve Yesrib</text>'
        '<rect x="18" y="42" width="202" height="172" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="119" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-sf">MEKKE</text>'
        '<text x="30" y="90" font-size="10" class="g-y">• Kabile: Kureyş</text>'
        '<text x="30" y="108" font-size="10" class="g-y">• Meclis: Darünnedve</text>'
        '<text x="30" y="126" font-size="10" class="g-y">• İnanç: Putperestlik (Hübel),</text>'
        '<text x="38" y="141" font-size="10" class="g-y">Hristiyanlık ve Hanifler</text>'
        '<rect x="30" y="156" width="178" height="44" rx="6" fill="#fff"/>'
        '<text x="119" y="174" text-anchor="middle" font-size="10" font-weight="700" class="g-sf">Ekonomi: Kervan Ticareti</text>'
        '<text x="119" y="190" text-anchor="middle" font-size="9.5" class="g-y">Kâbe ziyareti ve yaz-kış seferleri</text>'
        '<rect x="239" y="42" width="202" height="172" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="340" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">TAİF (Vec Vadisi)</text>'
        '<text x="251" y="90" font-size="10" class="g-y">• Kabile: Sakif (Amalika/Semud sonrası)</text>'
        '<text x="251" y="108" font-size="10" class="g-y">• İklim: Yüksek, ormanlık ve serin</text>'
        '<text x="251" y="126" font-size="10" class="g-y">• İnanç: Putperestlik (Lat mabedi)</text>'
        '<text x="259" y="141" font-size="10" class="g-y">ve Hanifler</text>'
        '<rect x="251" y="156" width="178" height="44" rx="6" fill="#fff"/>'
        '<text x="340" y="174" text-anchor="middle" font-size="10" font-weight="700" class="g-yf">Ekonomi: Tarım ve Dericilik</text>'
        '<text x="340" y="190" text-anchor="middle" font-size="9.5" class="g-y">Mekke\'ye ekonomik bağımlılık</text>'
        '<rect x="460" y="42" width="202" height="172" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="561" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">YESRİB (Medine)</text>'
        '<text x="472" y="90" font-size="10" class="g-y">• Topluluk: Evs, Hazrec, Yahudiler</text>'
        '<text x="472" y="108" font-size="10" class="g-y">• Coğrafya: Uhud-Air arası, volkanik</text>'
        '<text x="472" y="126" font-size="10" class="g-y">• İnanç: Putperestlik (Menat)</text>'
        '<text x="480" y="141" font-size="10" class="g-y">ve Yahudilik</text>'
        '<rect x="472" y="156" width="178" height="44" rx="6" fill="#fff"/>'
        '<text x="561" y="174" text-anchor="middle" font-size="10" font-weight="700" class="g-mf">Ekonomi: Tarım ve Zanaat</text>'
        '<text x="561" y="190" text-anchor="middle" font-size="9.5" class="g-y">Hurma, kuyumculuk, demircilik</text>'
    )
    return svg(680, 228, ic, "Hicaz bölgesinin üç önemli şehri: Mekke, Taif ve Yesrib")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 1:
        b[1]["gorsel"] = _mekke_kronoloji()
    if len(b) > 5:
        b[5]["gorsel"] = _hicaz_uc_sehir()
