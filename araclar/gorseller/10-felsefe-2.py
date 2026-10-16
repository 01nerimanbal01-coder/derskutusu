from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 235
    ic = f"""
    <rect x="12" y="12" width="596" height="211" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">DÜŞÜNCE DENEYLERİ, GÜNCEL VAKALAR VE REFLEKSİF SORGULAMA KARTI</text>

    <!-- Sol: 4 Vaka / Düşünce Deneyi -->
    <rect x="24" y="48" width="336" height="160" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <rect x="34" y="58" width="154" height="64" rx="7" fill="#fee2e2" stroke="#dc2626"/>
    <text x="111" y="74" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#991b1b">1. HeLa Hücre Hattı</text>
    <text x="111" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Rıza alınmadan toplanan</text>
    <text x="111" y="100" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">doku vs. tıbbi fayda</text>
    <text x="111" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#b91c1c">(Biyoetik / Mahremiyet)</text>

    <rect x="196" y="58" width="154" height="64" rx="7" fill="#dbeafe" stroke="#2563eb"/>
    <text x="273" y="74" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#1e3a8a">2. Theseus'un Gemisi</text>
    <text x="273" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Tüm parçaları değişen gemi</text>
    <text x="273" y="100" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">aynı gemi midir?</text>
    <text x="273" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">(Ontoloji / Özdeşlik)</text>

    <rect x="34" y="132" width="154" height="64" rx="7" fill="#dcfce7" stroke="#16a34a"/>
    <text x="111" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#14532d">3. Tecrübe Makinesi</text>
    <text x="111" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Robert Nozick: Simülasyon</text>
    <text x="111" y="174" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">mutluluğu vs. gerçek yaşam</text>
    <text x="111" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#15803d">(Gerçeklik ve Değer)</text>

    <rect x="196" y="132" width="154" height="64" rx="7" fill="#fef3c7" stroke="#d97706"/>
    <text x="273" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#78350f">4. Otonom Araç İkilemi</text>
    <text x="273" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Algoritmanın kaza anında</text>
    <text x="273" y="174" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">kimi koruyacağı kararı</text>
    <text x="273" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#b45309">(Yapay Zekâ Etiği)</text>

    <!-- Sağ: Refleksif Sorgulama Kartı -->
    <rect x="372" y="48" width="224" height="160" rx="10" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.6"/>
    <rect x="372" y="48" width="224" height="24" rx="10" fill="#7c3aed"/>
    <text x="484" y="64" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">REFLEKSİF SORGULAMA KARTI</text>

    <rect x="384" y="80" width="200" height="34" rx="6" fill="#ffffff" stroke="#c4b5fd"/>
    <text x="484" y="94" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#5b21b6">1. Sorunun Amacı</text>
    <text x="484" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Neyi açığa çıkarmayı hedefliyoruz?</text>

    <rect x="384" y="120" width="200" height="34" rx="6" fill="#ffffff" stroke="#c4b5fd"/>
    <text x="484" y="134" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#5b21b6">2. Ön Kabul</text>
    <text x="484" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Peşinen doğru saydığımız düşünce nedir?</text>

    <rect x="384" y="160" width="200" height="38" rx="6" fill="#ffffff" stroke="#c4b5fd"/>
    <text x="484" y="174" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#5b21b6">3. Anahtar Kavramlar + Sokratik Yöntem</text>
    <text x="484" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Kavram anlamları ve diyalogla geliştirme</text>
    """
    return svg(w, h, ic, "Dört temel düşünce deneyi/vaka ve refleksif sorgulama kartı")


def _gorsel_4():
    w, h = 620, 235
    ic = f"""
    <rect x="12" y="12" width="596" height="211" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">FELSEFENİN BİLİM, DİN VE SANAT İLE İLİŞKİSİ (BENZERLİKLER VE FARKLILIKLAR)</text>

    <!-- Merkez: FELSEFE -->
    <rect x="235" y="46" width="150" height="36" rx="18" fill="#4f46e5"/>
    <text x="310" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#ffffff">FELSEFE (Akıl &amp; Bütüncül)</text>

    <!-- 1. Bilim -->
    <rect x="22" y="96" width="184" height="114" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="114" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1d4ed8">FELSEFE — BİLİM</text>
    <text x="114" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">Benzerlik:</text>
    <text x="114" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Akla dayanır, sistemlidir,</text>
    <text x="114" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">evren ve insanı açıklar.</text>
    <text x="114" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Farklılık:</text>
    <text x="114" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Bilim varlığı parçalara ayırır,</text>
    <text x="114" y="194" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">deney-gözlemle kanıtlar;</text>
    <text x="114" y="205" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1e3a8a">felsefe bütüncül yaklaşır.</text>

    <!-- 2. Din -->
    <rect x="218" y="96" width="184" height="114" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="310" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#b45309">FELSEFE — DİN</text>
    <text x="310" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">Benzerlik:</text>
    <text x="310" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">İnsanı, evreni ve hayatın</text>
    <text x="310" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">anlamını konu edinir.</text>
    <text x="310" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Farklılık:</text>
    <text x="310" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Felsefe akla ve eleştiriye,</text>
    <text x="310" y="194" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">din ise vahye ve sorgulanmadan</text>
    <text x="310" y="205" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#78350f">kabul edilen inanca dayanır.</text>

    <!-- 3. Sanat -->
    <rect x="414" y="96" width="184" height="114" rx="10" fill="#fce7f3" stroke="#db2777" stroke-width="1.5"/>
    <text x="506" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#be185d">FELSEFE — SANAT</text>
    <text x="506" y="131" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">Benzerlik:</text>
    <text x="506" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Sonuçları özneldir ve yaratıcı</text>
    <text x="506" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">hayal gücünün ürünüdür.</text>
    <text x="506" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Farklılık:</text>
    <text x="506" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Felsefe akılla soyut düşünce,</text>
    <text x="506" y="194" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">sanat duyguyla güzellik ve</text>
    <text x="506" y="205" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#9d174d">somut sanat eseri üretir.</text>
    """
    return svg(w, h, ic, "Felsefenin bilim, din ve sanat ile benzerlik ve farklılıkları")


def _gorsel_5():
    w, h = 620, 220
    ic = f"""
    <rect x="12" y="12" width="596" height="196" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">FELSEFENİN BİREYSEL VE TOPLUMSAL İŞLEVLERİ</text>

    <!-- Sol: Bireysel İşlevler -->
    <rect x="24" y="48" width="276" height="146" rx="10" fill="#ecfdf5" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="24" y="48" width="276" height="24" rx="10" fill="#16a34a"/>
    <text x="162" y="64" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">BİREYSEL İŞLEVLERİ</text>
    <text x="162" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#14532d">• Kendini ve çevresini derinlemesine tanıma</text>
    <text x="162" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Olayları çok yönlü bakış açısıyla değerlendirme</text>
    <text x="162" y="124" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Sorunlara alternatif ve gerekçeli çözümler üretme</text>
    <text x="162" y="142" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Ön yargılardan ve dogmalardan uzaklaşma</text>
    <rect x="38" y="154" width="248" height="30" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="162" y="173" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">Örnek: P4C (Çocuklar İçin Felsefe) ve IQ artışı</text>

    <!-- Sağ: Toplumsal İşlevler -->
    <rect x="320" y="48" width="276" height="146" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <rect x="320" y="48" width="276" height="24" rx="10" fill="#2563eb"/>
    <text x="458" y="64" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#ffffff">TOPLUMSAL İŞLEVLERİ</text>
    <text x="458" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#1e3a8a">• Demokrasi, hoşgörü ve birlikte yaşama kültürü</text>
    <text x="458" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Sosyal adalet, insan hakları ve kapsayıcı toplum</text>
    <text x="458" y="124" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Bilimlerin gelişmesine ve etik ilkelere rehberlik</text>
    <text x="458" y="142" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#334155">• Tıp etiği, yapay zekâ etiği ve sürdürülebilirlik</text>
    <rect x="334" y="154" width="248" height="30" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="458" y="173" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">Örnek: UNESCO Dünya Felsefe Günü ve Sempozyumlar</text>
    """
    return svg(w, h, ic, "Felsefenin bireysel ve toplumsal işlevleri şeması")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _gorsel_1()
    if len(b) > 3:
        b[3]["gorsel"] = _gorsel_4()
    if len(b) > 4:
        b[4]["gorsel"] = _gorsel_5()
