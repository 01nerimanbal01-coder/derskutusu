from ozet_gorsel import svg


def g1():
    w, h = 620, 240
    ic = [
        '<rect x="16" y="16" width="588" height="208" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">FİZİK BİLİMİNİN SEKİZ ALT DALI (GENEL BAKIŞ)</text>',
        '<rect x="28" y="58" width="134" height="68" rx="9" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>',
        '<text x="95" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1d4ed8">1. Mekanik</text>',
        '<text x="95" y="102" text-anchor="middle" font-size="12" fill="#334155">Kuvvet, hareket,</text>',
        '<text x="95" y="117" text-anchor="middle" font-size="12" fill="#334155">denge ve enerji</text>',
        '<rect x="172" y="58" width="134" height="68" rx="9" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>',
        '<text x="239" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">2. Elektromanyetizma</text>',
        '<text x="239" y="102" text-anchor="middle" font-size="12" fill="#334155">Elektrik yükleri,</text>',
        '<text x="239" y="117" text-anchor="middle" font-size="12" fill="#334155">akım ve mıknatıs</text>',
        '<rect x="316" y="58" width="134" height="68" rx="9" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>',
        '<text x="383" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#be123c">3. Termodinamik</text>',
        '<text x="383" y="102" text-anchor="middle" font-size="12" fill="#334155">Isı, sıcaklık ve</text>',
        '<text x="383" y="117" text-anchor="middle" font-size="12" fill="#334155">ısı alışverişi</text>',
        '<rect x="460" y="58" width="132" height="68" rx="9" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>',
        '<text x="526" y="82" text-anchor="middle" font-size="12.5" font-weight="700" fill="#a16207">4. Optik</text>',
        '<text x="526" y="102" text-anchor="middle" font-size="12" fill="#334155">Işık, yansıma,</text>',
        '<text x="526" y="117" text-anchor="middle" font-size="12" fill="#334155">kırılma ve renk</text>',
        '<rect x="28" y="138" width="134" height="68" rx="9" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.4"/>',
        '<text x="95" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7e22ce">5. Katı Hâl Fiziği</text>',
        '<text x="95" y="182" text-anchor="middle" font-size="12" fill="#334155">Kristal yapı ve</text>',
        '<text x="95" y="197" text-anchor="middle" font-size="12" fill="#334155">yarı iletkenler</text>',
        '<rect x="172" y="138" width="134" height="68" rx="9" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.4"/>',
        '<text x="239" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0e7490">6. Atom Fiziği</text>',
        '<text x="239" y="182" text-anchor="middle" font-size="12" fill="#334155">Atom yapısı ve</text>',
        '<text x="239" y="197" text-anchor="middle" font-size="12" fill="#334155">elektron dizilimi</text>',
        '<rect x="316" y="138" width="134" height="68" rx="9" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.4"/>',
        '<text x="383" y="162" text-anchor="middle" font-size="12.5" font-weight="700" fill="#92400e">7. Nükleer Fizik</text>',
        '<text x="383" y="182" text-anchor="middle" font-size="12" fill="#334155">Atom çekirdeği</text>',
        '<text x="383" y="197" text-anchor="middle" font-size="12" fill="#334155">ve radyasyon</text>',
        '<rect x="460" y="138" width="132" height="68" rx="9" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.4"/>',
        '<text x="526" y="162" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">8. Yüksek Enerji</text>',
        '<text x="526" y="182" text-anchor="middle" font-size="12" fill="#334155">Atom altı parçacık</text>',
        '<text x="526" y="197" text-anchor="middle" font-size="12" fill="#334155">ve plazma hâli</text>',
    ]
    return svg(w, h, "".join(ic), "Fizik biliminin sekiz alt dalı ve inceleme konuları")


def g2():
    w, h = 620, 220
    ic = [
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">MEKANİK, ELEKTROMANYETİZMA, TERMODİNAMİK VE OPTİK</text>',
        '<rect x="30" y="62" width="270" height="56" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>',
        '<text x="165" y="83" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8">Mekanik Örnekleri</text>',
        '<text x="165" y="103" text-anchor="middle" font-size="12" fill="#334155">Bisiklet, rüzgârgülü, İHA, gezegen hareketi</text>',
        '<rect x="320" y="62" width="270" height="56" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>',
        '<text x="455" y="83" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">Elektromanyetizma Örnekleri</text>',
        '<text x="455" y="103" text-anchor="middle" font-size="12" fill="#334155">Pusula, mıknatısla metal ayrıştırma, yıldırım</text>',
        '<rect x="30" y="130" width="270" height="56" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>',
        '<text x="165" y="151" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">Termodinamik Örnekleri</text>',
        '<text x="165" y="171" text-anchor="middle" font-size="12" fill="#334155">Bina ısı yalıtımı, yemek pişirme, klima</text>',
        '<rect x="320" y="130" width="270" height="56" rx="8" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>',
        '<text x="455" y="151" text-anchor="middle" font-size="13" font-weight="700" fill="#a16207">Optik Örnekleri</text>',
        '<text x="455" y="171" text-anchor="middle" font-size="12" fill="#334155">Gökkuşağı, serap, gözlük, fiber optik kablo</text>',
    ]
    return svg(w, h, "".join(ic), "Mekanik, elektromanyetizma, termodinamik ve optik uygulama örnekleri")


def g3():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">KATI HÂL FİZİĞİ İLE ATOM FİZİĞİ KARŞILAŞTIRMASI</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#7e22ce">KATI HÂL FİZİĞİ</text>',
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">• Kristal yapılı katılar ve atom dizilişi</text>',
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">• Yarı iletkenlik ve süper iletkenlik</text>',
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">• Şarjlı piller, hafızalı metaller</text>',
        '<text x="166" y="160" text-anchor="middle" font-size="12" fill="#334155">• LCD ekran, dokunmatik ekran, maglev</text>',
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#0e7490">ATOM FİZİĞİ</text>',
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">• Atomun yapısı ve enerji düzeyleri</text>',
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">• Elektron dizilimi ve molekül etkileşimi</text>',
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">• Lazer ve elektron mikroskobu</text>',
        '<text x="453" y="160" text-anchor="middle" font-size="12" fill="#334155">• Kuantum bilgisayar, yapay zekâ, 3D yazıcı</text>',
    ]
    return svg(w, h, "".join(ic), "Katı hâl fiziği ile atom fiziği karşılaştırma şeması")


def g4():
    w, h = 620, 225
    ic = [
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">NÜKLEER FİZİK VE YÜKSEK ENERJİ-PLAZMA FİZİĞİ</text>',
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#fef3c7" stroke="#fcd34d" stroke-width="1.5"/>',
        '<text x="166" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#92400e">NÜKLEER (ÇEKİRDEK) FİZİK</text>',
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">• Proton ve nötronları tutan kuvvetler</text>',
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">• Çekirdek tepkimeleri ve radyasyon</text>',
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">• Nükleer tıp ve BT (tomografi) cihazı</text>',
        '<text x="166" y="160" text-anchor="middle" font-size="12" fill="#334155">• Karbon-14 yaş tayini, gıda raf ömrü</text>',
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>',
        '<text x="453" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">YÜKSEK ENERJİ VE PLAZMA FİZİĞİ</text>',
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">• Atom altı parçacıklar ve etkileşimleri</text>',
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">• Maddenin 4. hâli: Plazma hâli</text>',
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">• Kutup ışıkları, floresan ve neon lamba</text>',
        '<text x="453" y="160" text-anchor="middle" font-size="12" fill="#334155">• Uzay-roket teknolojisi ve atık arıtımı</text>',
    ]
    return svg(w, h, "".join(ic), "Nükleer fizik ile yüksek enerji ve plazma fiziği karşılaştırması")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[3]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
