from ozet_gorsel import svg


def g1():
    w, h = 620, 235
    ic = [
        '<rect x="16" y="16" width="588" height="203" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">MEKKE DÖNEMİ KRONOLOJİSİ (610 – 622)</text>',
        '<rect x="30" y="58" width="176" height="68" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="118" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">610 – 613: İlk Vahiy</text>',
        '<text x="118" y="102" text-anchor="middle" font-size="12" fill="#334155">Hira’da ilk vahiy ve</text>',
        '<text x="118" y="118" text-anchor="middle" font-size="12" fill="#334155">Darülerkâm’da gizli davet</text>',
        '<rect x="222" y="58" width="176" height="68" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="310" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">615 – 616: Habeşistan</text>',
        '<text x="310" y="102" text-anchor="middle" font-size="12" fill="#334155">İlk hicret kafileleri</text>',
        '<text x="310" y="118" text-anchor="middle" font-size="12" fill="#334155">Kral Necaşi’nin himayesi</text>',
        '<rect x="414" y="58" width="176" height="68" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="502" y="82" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">616 – 619: Boykot</text>',
        '<text x="502" y="102" text-anchor="middle" font-size="12" fill="#334155">Haşimoğullarına 3 yıl</text>',
        '<text x="502" y="118" text-anchor="middle" font-size="12" fill="#334155">sosyal-ekonomik kuşatma</text>',
        '<rect x="30" y="138" width="176" height="68" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="118" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">620: Hüzün ve Miraç</text>',
        '<text x="118" y="182" text-anchor="middle" font-size="12" fill="#334155">Hüzün Yılı, Taif ve</text>',
        '<text x="118" y="198" text-anchor="middle" font-size="12" fill="#334155">İsra-Miraç mucizesi</text>',
        '<rect x="222" y="138" width="176" height="68" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="310" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">621 – 622: Akabe</text>',
        '<text x="310" y="182" text-anchor="middle" font-size="12" fill="#334155">I. ve II. Akabe Biatleri</text>',
        '<text x="310" y="198" text-anchor="middle" font-size="12" fill="#334155">Musab bin Umeyr</text>',
        '<rect x="414" y="138" width="176" height="68" rx="10" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.5"/>',
        '<text x="502" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0e7490">622: Medine’ye Hicret</text>',
        '<text x="502" y="182" text-anchor="middle" font-size="12" fill="#334155">Sevr, Kuba, Ranuna ve</text>',
        '<text x="502" y="198" text-anchor="middle" font-size="12" fill="#334155">Medine’ye varış</text>',
    ]
    return svg(w, h, "".join(ic), "Peygamberimizin Mekke yılları ve hicret kronolojisi")


def g2():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">620 YILI: HÜZÜN YILINDAN İLAHİ TESELLİYE</text>',
        '<rect x="34" y="64" width="166" height="118" rx="10" fill="#fff1f2" stroke="#fda4af" stroke-width="1.5"/>',
        '<text x="117" y="90" text-anchor="middle" font-size="13.5" font-weight="700" fill="#be123c">HÜZÜN YILI</text>',
        '<text x="117" y="114" text-anchor="middle" font-size="12" fill="#334155">Ebu Talib ve</text>',
        '<text x="117" y="132" text-anchor="middle" font-size="12" fill="#334155">Hz. Hatice’nin</text>',
        '<text x="117" y="150" text-anchor="middle" font-size="12" fill="#334155">peş peşe vefatı</text>',
        '<line x1="202" y1="123" x2="224" y2="123" stroke="#e11d48" stroke-width="2"/>',
        '<polygon points="226,123 218,118 218,128" fill="#e11d48"/>',
        '<rect x="228" y="64" width="164" height="118" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="310" y="90" text-anchor="middle" font-size="13.5" font-weight="700" fill="#a16207">TAİF YOLCULUĞU</text>',
        '<text x="310" y="114" text-anchor="middle" font-size="12" fill="#334155">Zeyd bin Harise ile</text>',
        '<text x="310" y="132" text-anchor="middle" font-size="12" fill="#334155">tebliğ girişimi, sabır</text>',
        '<text x="310" y="150" text-anchor="middle" font-size="12" fill="#334155">ve hidayet duası</text>',
        '<line x1="394" y1="123" x2="416" y2="123" stroke="#ca8a04" stroke-width="2"/>',
        '<polygon points="418,123 410,118 410,128" fill="#ca8a04"/>',
        '<rect x="420" y="64" width="166" height="118" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="503" y="90" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">İSRA VE MİRAÇ</text>',
        '<text x="503" y="114" text-anchor="middle" font-size="12" fill="#334155">Beş vakit namaz</text>',
        '<text x="503" y="132" text-anchor="middle" font-size="12" fill="#334155">Bakara son 2 ayet</text>',
        '<text x="503" y="150" text-anchor="middle" font-size="12" fill="#334155">Cennet müjdesi</text>',
    ]
    return svg(w, h, "".join(ic), "Hüzün Yılı, Taif yolculuğu ve İsra-Miraç mucizesi şeması")


def g3():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">AKABE BİATLERİ (MEDİNE’YE HİCRETE HAZIRLIK)</text>',
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="166" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8">I. AKABE BİATİ (621)</text>',
        '<text x="166" y="112" text-anchor="middle" font-size="12" fill="#334155">• 12 Medineli Müslüman katıldı.</text>',
        '<text x="166" y="132" text-anchor="middle" font-size="12" fill="#334155">• Tevhit ve ahlak ilkelerine söz verildi.</text>',
        '<text x="166" y="152" text-anchor="middle" font-size="12" fill="#334155">• Musab bin Umeyr öğretmen seçildi.</text>',
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="454" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">II. AKABE BİATİ (622)</text>',
        '<text x="454" y="112" text-anchor="middle" font-size="12" fill="#334155">• 2’si kadın 75 Medineli katıldı.</text>',
        '<text x="454" y="132" text-anchor="middle" font-size="12" fill="#334155">• Peygamberimizi koruma sözü verildi.</text>',
        '<text x="454" y="152" text-anchor="middle" font-size="12" fill="#334155">• Medine’ye hicret daveti yapıldı.</text>',
    ]
    return svg(w, h, "".join(ic), "Birinci ve İkinci Akabe Biatleri karşılaştırması")


def g4():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">MEKKE’DEN MEDİNE’YE HİCRET YOLCULUĞU (622)</text>',
        '<rect x="28" y="64" width="128" height="122" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="92" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">1. Mekke &amp; Sevr</text>',
        '<text x="92" y="114" text-anchor="middle" font-size="12" fill="#334155">Hz. Ali emanet için</text>',
        '<text x="92" y="132" text-anchor="middle" font-size="12" fill="#334155">kalır; Sevr’de 3 gün</text>',
        '<text x="92" y="150" text-anchor="middle" font-size="12" fill="#334155">(Tevbe suresi 40)</text>',
        '<rect x="172" y="64" width="128" height="122" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>',
        '<text x="236" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">2. Kuba Mescidi</text>',
        '<text x="236" y="114" text-anchor="middle" font-size="12" fill="#334155">8 günlük yolculuk</text>',
        '<text x="236" y="132" text-anchor="middle" font-size="12" fill="#334155">sonrası ilk mescidin</text>',
        '<text x="236" y="150" text-anchor="middle" font-size="12" fill="#334155">inşa edilmesi</text>',
        '<rect x="316" y="64" width="128" height="122" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>',
        '<text x="380" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">3. Ranuna Vadisi</text>',
        '<text x="380" y="114" text-anchor="middle" font-size="12" fill="#334155">İlk cuma hutbesi</text>',
        '<text x="380" y="132" text-anchor="middle" font-size="12" fill="#334155">ve ilk cuma</text>',
        '<text x="380" y="150" text-anchor="middle" font-size="12" fill="#334155">namazının kılınması</text>',
        '<rect x="460" y="64" width="132" height="122" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="526" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="#7e22ce">4. Medine (24 Eyl)</text>',
        '<text x="526" y="114" text-anchor="middle" font-size="12" fill="#334155">Ebu Eyyüb el-Ensari</text>',
        '<text x="526" y="132" text-anchor="middle" font-size="12" fill="#334155">misafirliği; Muhacir</text>',
        '<text x="526" y="150" text-anchor="middle" font-size="12" fill="#334155">ve Ensar kardeşliği</text>',
    ]
    return svg(w, h, "".join(ic), "Mekke'den Medine'ye hicret yolculuğu durakları")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[3]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
