from ozet_gorsel import svg


def _anlama_adimlari():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Kur’an-ı Kerim’i Anlama Adımları: Tercüme, Meal ve Tefsir</text>'
        '<rect x="18" y="42" width="202" height="168" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="119" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-sf">1. Tercüme (Mütercim)</text>'
        '<text x="119" y="90" text-anchor="middle" font-size="10.5" class="g-y">Bir dilden başka dile çeviri</text>'
        '<rect x="30" y="104" width="178" height="44" rx="6" fill="#fff"/>'
        '<text x="119" y="122" text-anchor="middle" font-size="10" font-weight="700" class="g-sf">Harfî (Lafzi): Bire bir</text>'
        '<text x="119" y="138" text-anchor="middle" font-size="9.5" class="g-y">(Kur\'an için mümkün değildir)</text>'
        '<rect x="30" y="154" width="178" height="44" rx="6" fill="#fff"/>'
        '<text x="119" y="172" text-anchor="middle" font-size="10" font-weight="700" class="g-sf">Tefsirî (Manevi): Anlam</text>'
        '<text x="119" y="188" text-anchor="middle" font-size="9.5" class="g-y">Esas olan manayı açıklamaktır</text>'
        '<rect x="239" y="42" width="202" height="168" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="340" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-mf">2. Meal</text>'
        '<text x="340" y="90" text-anchor="middle" font-size="10.5" class="g-y">Yaklaşık ve Öz Anlam</text>'
        '<rect x="251" y="104" width="178" height="94" rx="6" fill="#fff"/>'
        '<text x="340" y="126" text-anchor="middle" font-size="10" class="g-y">Kelime kelime çevirmeksizin</text>'
        '<text x="340" y="144" text-anchor="middle" font-size="10" class="g-y">asıl anlatılmak isteneni</text>'
        '<text x="340" y="162" text-anchor="middle" font-size="10" class="g-y">kısa ve öz biçimde</text>'
        '<text x="340" y="180" text-anchor="middle" font-size="10" font-weight="700" class="g-mf">başka dile aktarmaktır.</text>'
        '<rect x="460" y="42" width="202" height="168" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="561" y="66" text-anchor="middle" font-size="12.5" font-weight="800" class="g-yf">3. Tefsir (Müfessir)</text>'
        '<text x="561" y="90" text-anchor="middle" font-size="10.5" class="g-y">Derin Açıklama ve Yorum</text>'
        '<rect x="472" y="104" width="178" height="94" rx="6" fill="#fff"/>'
        '<text x="561" y="126" text-anchor="middle" font-size="10" class="g-y">Ayetleri indiriliş sebepleri,</text>'
        '<text x="561" y="144" text-anchor="middle" font-size="10" class="g-y">dil incelikleri, sünnet ve</text>'
        '<text x="561" y="162" text-anchor="middle" font-size="10" class="g-y">hükümler ışığında detaylıca</text>'
        '<text x="561" y="180" text-anchor="middle" font-size="10" font-weight="700" class="g-yf">açıklayıp yorumlamaktır.</text>'
    )
    return svg(680, 224, ic, "Tercüme, meal ve tefsir kavramlarının karşılaştırması")


def _mufessir_ozellikleri():
    ic = (
        '<text x="340" y="24" text-anchor="middle" font-size="14" font-weight="800" class="g-y">Müfessirde Bulunması Gereken Başlıca Özellikler</text>'
        '<rect x="20" y="42" width="200" height="72" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="120" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mf">Dil ve Kur’an Hâkimiyeti</text>'
        '<text x="120" y="86" text-anchor="middle" font-size="10" class="g-y">Arap dilini ve Kur’an’ın</text>'
        '<text x="120" y="101" text-anchor="middle" font-size="10" class="g-y">bütünlüğünü iyi bilmesi</text>'
        '<rect x="240" y="42" width="200" height="72" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="340" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-yf">Vahiy Ortamı (Nüzul)</text>'
        '<text x="340" y="86" text-anchor="middle" font-size="10" class="g-y">Vahyin indiği ortamı ve</text>'
        '<text x="340" y="101" text-anchor="middle" font-size="10" class="g-y">indiriliş sebeplerini bilmesi</text>'
        '<rect x="460" y="42" width="200" height="72" rx="10" class="g-sa" stroke="#b45309" stroke-width="1.5"/>'
        '<text x="560" y="66" text-anchor="middle" font-size="11.5" font-weight="800" class="g-sf">Hadis İlminde Yetkinlik</text>'
        '<text x="560" y="86" text-anchor="middle" font-size="10" class="g-y">Hz. Peygamber’in sünnetine</text>'
        '<text x="560" y="101" text-anchor="middle" font-size="10" class="g-y">ve açıklamalarına vâkıf olması</text>'
        '<rect x="20" y="128" width="200" height="72" rx="10" class="g-moa" stroke="#7e22ce" stroke-width="1.5"/>'
        '<text x="120" y="152" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mof">Kur’an İlimleri</text>'
        '<text x="120" y="172" text-anchor="middle" font-size="10" class="g-y">Muhkem, müteşabih vb.</text>'
        '<text x="120" y="187" text-anchor="middle" font-size="10" class="g-y">Kur’an ilimlerine hâkim olması</text>'
        '<rect x="240" y="128" width="200" height="72" rx="10" class="g-ma" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<text x="340" y="152" text-anchor="middle" font-size="11.5" font-weight="800" class="g-mf">İlk Nesillerin Görüşü</text>'
        '<text x="340" y="172" text-anchor="middle" font-size="10" class="g-y">Sahabe ve tâbiîn âlimlerinin</text>'
        '<text x="340" y="187" text-anchor="middle" font-size="10" class="g-y">yorumlarını bilmesi</text>'
        '<rect x="460" y="128" width="200" height="72" rx="10" class="g-ya" stroke="#15803d" stroke-width="1.5"/>'
        '<text x="560" y="152" text-anchor="middle" font-size="11.5" font-weight="800" class="g-yf">Pozitif ve Sosyal Bilimler</text>'
        '<text x="560" y="172" text-anchor="middle" font-size="10" class="g-y">Tarih, fizik, kimya, biyoloji ve</text>'
        '<text x="560" y="187" text-anchor="middle" font-size="10" class="g-y">astronomi verilerini bilmesi</text>'
    )
    return svg(680, 214, ic, "Müfessirlerde bulunması gereken özellikler")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 2:
        b[2]["gorsel"] = _anlama_adimlari()
    if len(b) > 3:
        b[3]["gorsel"] = _mufessir_ozellikleri()
