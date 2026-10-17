from ozet_gorsel import svg


def _gorsel_1():
    w, h = 680, 250
    ic = """
    <rect x="15" y="15" width="650" height="220" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">İNSANIN YAŞAM ALANI VE ÇEVRE SORUNLARININ BOYUTLARI</text>

    <!-- Sol: Fiziksel ve Sosyokültürel Çevre -->
    <rect x="30" y="52" width="295" height="168" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="177" y="74" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#065f46">ÇEVRENİN İKİ TEMEL BOYUTU</text>

    <rect x="44" y="84" width="128" height="62" rx="7" fill="#ffffff" stroke="#34d399"/>
    <text x="108" y="102" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">Doğal Çevre</text>
    <text x="108" y="118" text-anchor="middle" font-size="9.5" fill="#334155">Dağ, orman, nehir,</text>
    <text x="108" y="132" text-anchor="middle" font-size="9.5" fill="#334155">iklim, yaban hayatı</text>

    <rect x="183" y="84" width="128" height="62" rx="7" fill="#ffffff" stroke="#34d399"/>
    <text x="247" y="102" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">Yapay Çevre</text>
    <text x="247" y="118" text-anchor="middle" font-size="9.5" fill="#334155">Bina, köprü, baraj,</text>
    <text x="247" y="132" text-anchor="middle" font-size="9.5" fill="#334155">otoyol, kent dokusu</text>

    <rect x="44" y="154" width="267" height="54" rx="7" fill="#d1fae5" stroke="#059669"/>
    <text x="177" y="172" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">Sosyokültürel Çevre</text>
    <text x="177" y="188" text-anchor="middle" font-size="9.5" fill="#1e293b">Değerler, ahlaki normlar, gelenekler ve kurumlar</text>
    <text x="177" y="201" text-anchor="middle" font-size="9" fill="#047857">(Fiziksel çevreyle sürekli karşılıklı etkileşim hâlindedir)</text>

    <!-- Sağ: İnsan Kaynaklı Felaketler ve Çözüm Kavramları -->
    <rect x="355" y="52" width="295" height="168" rx="10" fill="#fff1f2" stroke="#f43f5e" stroke-width="2"/>
    <text x="502" y="74" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#9f1239">İNSAN KAYNAKLI EKOLOJİK KRİZLER</text>

    <rect x="369" y="84" width="128" height="62" rx="7" fill="#ffffff" stroke="#fb7185"/>
    <text x="433" y="102" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#be123c">1984 Bhopal Felaketi</text>
    <text x="433" y="117" text-anchor="middle" font-size="9.5" fill="#334155">Hindistan'da 40 ton</text>
    <text x="433" y="131" text-anchor="middle" font-size="9.5" fill="#334155">zehirli gaz sızıntısı</text>

    <rect x="508" y="84" width="128" height="62" rx="7" fill="#ffffff" stroke="#fb7185"/>
    <text x="572" y="102" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#be123c">Aral Gölü'nün Kuruması</text>
    <text x="572" y="117" text-anchor="middle" font-size="9.5" fill="#334155">Nehirlerin yönünün</text>
    <text x="572" y="131" text-anchor="middle" font-size="9.5" fill="#334155">değiştirilmesi (%90 kayıp)</text>

    <rect x="369" y="154" width="267" height="54" rx="7" fill="#ffe4e6" stroke="#e11d48"/>
    <text x="502" y="172" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#881337">Küresel Önlemler ve Yeni Kavramlar</text>
    <text x="502" y="187" text-anchor="middle" font-size="9.5" fill="#1e293b">Montreal (1987) • Karadeniz (1992) • Kyoto (1997)</text>
    <text x="502" y="201" text-anchor="middle" font-size="9" fill="#9f1239">Sıfır Atık • Ekolojik Koridor • Mikromobilite • Biyorafineri</text>
    """
    return svg(w, h, ic, "Çevrenin Boyutları ve İnsan Kaynaklı Ekolojik Krizler")


def _gorsel_2():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#78350f">KADİM KÜLTÜRLERDE DOĞA BİLİNCİ VE SÜRDÜRÜLEBİLİR MİMARİ</text>

    <!-- 4 Kutu -->
    <rect x="28" y="54" width="148" height="154" rx="10" fill="#ffffff" stroke="#d97706" stroke-width="1.8"/>
    <circle cx="102" cy="80" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="102" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">1</text>
    <text x="102" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">Öküz Dağı (Mencius)</text>
    <text x="102" y="128" text-anchor="middle" font-size="9.5" fill="#334155">MÖ 4. yy Çin düşüncesi:</text>
    <text x="102" y="143" text-anchor="middle" font-size="9.5" fill="#334155">Ormanı tahrip eden</text>
    <text x="102" y="158" text-anchor="middle" font-size="9.5" fill="#334155">insan kendi ahlaki</text>
    <text x="102" y="173" text-anchor="middle" font-size="9.5" fill="#334155">doğasını da kurutur.</text>

    <rect x="186" y="54" width="148" height="154" rx="10" fill="#ffffff" stroke="#0284c7" stroke-width="1.8"/>
    <circle cx="260" cy="80" r="16" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
    <text x="260" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#075985">2</text>
    <text x="260" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#0c4a6e">Gölpınar Hitit Barajı</text>
    <text x="260" y="128" text-anchor="middle" font-size="9.5" fill="#334155">MÖ 13. yy Çorum/Alaca:</text>
    <text x="260" y="143" text-anchor="middle" font-size="9.5" fill="#334155">Kuraklığa karşı su</text>
    <text x="260" y="158" text-anchor="middle" font-size="9.5" fill="#334155">kaynaklarını koruyan</text>
    <text x="260" y="173" text-anchor="middle" font-size="9.5" fill="#334155">3200 yıllık su mirası.</text>

    <rect x="344" y="54" width="148" height="154" rx="10" fill="#ffffff" stroke="#059669" stroke-width="1.8"/>
    <circle cx="418" cy="80" r="16" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
    <text x="418" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#065f46">3</text>
    <text x="418" y="110" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#064e3b">Gurabahane-i Laklakan</text>
    <text x="418" y="128" text-anchor="middle" font-size="9.5" fill="#334155">Osmanlı Vakıf Geleneği:</text>
    <text x="418" y="143" text-anchor="middle" font-size="9.5" fill="#334155">Bursa'da yaralı göçmen</text>
    <text x="418" y="158" text-anchor="middle" font-size="9.5" fill="#334155">leyleklerin tedavi edildiği</text>
    <text x="418" y="173" text-anchor="middle" font-size="9.5" fill="#334155">şefkat hastanesi.</text>

    <rect x="502" y="54" width="150" height="154" rx="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
    <circle cx="577" cy="80" r="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="577" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">4</text>
    <text x="577" y="110" text-anchor="middle" font-size="11" font-weight="bold" fill="#4c1d95">Süleymaniye Külliyesi</text>
    <text x="577" y="128" text-anchor="middle" font-size="9.5" fill="#334155">Mimar Sinan'ın Dehası:</text>
    <text x="577" y="143" text-anchor="middle" font-size="9.5" fill="#334155">Kandil isinden mürekkep</text>
    <text x="577" y="158" text-anchor="middle" font-size="9.5" fill="#334155">(is odası), doğal iklimlendirme</text>
    <text x="577" y="173" text-anchor="middle" font-size="9.5" fill="#334155">ve sıfır atık mimarisi.</text>
    """
    return svg(w, h, ic, "Kadim Kültürlerde Doğa Bilinci ve Sürdürülebilir Mimari Örnekleri")


def _gorsel_3():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">İLK ÇAĞ VE ORTA ÇAĞ FELSEFESİNDE İNSAN-DOĞA İLİŞKİSİ</text>

    <!-- İlk Çağ -->
    <rect x="30" y="54" width="300" height="154" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="180" y="76" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1d4ed8">İLK ÇAĞ FELSEFESİ: KOZMOS VE UYUM</text>
    <text x="45" y="98" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#1e40af">Hilozoizm (Canlıcılık):&lt;/tspan> Thales, Empedokles,</text>
    <text x="55" y="113" font-size="10" fill="#475569">Herakleitos — Doğa canlı bir bütündür (Arkhe).</text>
    <text x="45" y="133" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#1e40af">Taoizm (Lao Tse):&lt;/tspan> Evrensel yasa Tao ile uyum.</text>
    <text x="45" y="153" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#1e40af">Aristoteles:&lt;/tspan> Doğadaki varlıklar insan içindir.</text>
    <text x="45" y="173" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#1e40af">Kynikler ve Stoacılar:&lt;/tspan> Mutluluk, doğanın</text>
    <text x="55" y="188" font-size="10" fill="#475569">yasalarına uygun ve sade yaşamakla mümkündür.</text>

    <!-- Orta Çağ -->
    <rect x="350" y="54" width="300" height="154" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <text x="500" y="76" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#15803d">ORTA ÇAĞ FELSEFESİ: İLAHİ DÜZEN VE EMANET</text>
    <text x="365" y="98" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#166534">Saint Augustinus:&lt;/tspan> Doğa, Tanrı'nın bilgeliğini</text>
    <text x="375" y="113" font-size="10" fill="#475569">ve kusursuz düzenini yansıtan bir kitaptır.</text>
    <text x="365" y="133" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#166534">Farabi ve İbni Sina:&lt;/tspan> Sudûr (taşma) öğretisiyle</text>
    <text x="375" y="148" font-size="10" fill="#475569">her varlık kozmik düzende anlamlı bir yere sahiptir.</text>
    <text x="365" y="168" font-size="10.5" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#166534">Emanet ve Tasavvuf (Yunus Emre):&lt;/tspan> Doğa mülk</text>
    <text x="375" y="183" font-size="10" fill="#475569">değil emanettir; israftan kaçınmak ahlaki ödevdir.</text>
    """
    return svg(w, h, ic, "İlk Çağ ve Orta Çağ Felsefesinde Doğa Anlayışı")


def _gorsel_4():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">MODERN MEKANİK DOĞA GÖRÜŞÜ VE 20. YÜZYIL ELEŞTİRİLERİ</text>

    <!-- Sol: 17. Yüzyıl Mekanik Doğa -->
    <rect x="28" y="54" width="290" height="154" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="173" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">17-18. YY: MEKANİK VE ARAÇSAL DOĞA</text>
    <text x="42" y="97" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#991b1b">Francis Bacon:&lt;/tspan> "Bilgi güçtür." Bilimin amacı</text>
    <text x="52" y="111" font-size="9.5" fill="#475569">doğanın sırlarını çözüp ona hükmetmektir.</text>
    <text x="42" y="131" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#991b1b">René Descartes ve Thomas Hobbes:&lt;/tspan></text>
    <text x="52" y="145" font-size="9.5" fill="#475569">Akılcı-mekanik evren: Düşünen özne (insan)</text>
    <text x="52" y="159" font-size="9.5" fill="#475569">karşısında ruhsuz bir saat gibi işleyen madde.</text>
    <rect x="42" y="170" width="262" height="26" rx="6" fill="#fee2e2"/>
    <text x="173" y="187" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#991b1b">Sonuç: Doğanın sömürülecek kaynağa indirgenmesi</text>

    <!-- Ok -->
    <line x1="324" y1="130" x2="356" y2="130" stroke="#475569" stroke-width="2.5"/>
    <polygon points="356,125 366,130 356,135" fill="#475569"/>

    <!-- Sağ: 20. Yüzyıl Eleştirileri -->
    <rect x="372" y="54" width="280" height="154" rx="10" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="512" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">20. YY: MODERNİTE VE TEKNİK ELEŞTİRİSİ</text>
    <text x="386" y="97" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">Martin Heidegger:&lt;/tspan> Modern bilim varlığı</text>
    <text x="396" y="111" font-size="9.5" fill="#475569">matematiksel fiziğe indirgemiş; doğayı devasa</text>
    <text x="396" y="125" font-size="9.5" fill="#475569">bir makine görerek ötekileştirmiştir.</text>
    <text x="386" y="145" font-size="10" fill="#1e293b">• &lt;tspan font-weight="bold" fill="#6d28d9">Theodor Adorno:&lt;/tspan> Doğaya egemen olma</text>
    <text x="396" y="159" font-size="9.5" fill="#475569">çabası yabancılaşma doğurmuştur: "Durdurulamaz</text>
    <text x="396" y="173" font-size="9.5" fill="#475569">ilerlemenin laneti durdurulamaz gerilemedir."</text>
    """
    return svg(w, h, ic, "Modern Mekanik Doğa Anlayışı ve 20. Yüzyıl Felsefi Eleştirileri")


def _gorsel_5():
    w, h = 680, 240
    ic = """
    <rect x="15" y="15" width="650" height="210" rx="14" fill="#f0fdfa" stroke="#14b8a6" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#134e4a">ÇEVRE ETİĞİNİN TEMEL KAVRAMLARI VE "SON İNSAN" DENEYİ</text>

    <!-- Sol: Araçsal vs İçsel Değer -->
    <rect x="28" y="54" width="310" height="154" rx="10" fill="#ffffff" stroke="#0d9488" stroke-width="1.8"/>
    <rect x="40" y="66" width="138" height="72" rx="8" fill="#fef3c7" stroke="#f59e0b"/>
    <text x="109" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">Araçsal Değer</text>
    <text x="109" y="101" text-anchor="middle" font-size="9.5" fill="#334155">Varlığın yalnızca insana</text>
    <text x="109" y="115" text-anchor="middle" font-size="9.5" fill="#334155">sağladığı fayda ve çıkar</text>
    <text x="109" y="129" text-anchor="middle" font-size="9.5" fill="#334155">ölçüsünde değerli olması</text>

    <rect x="188" y="66" width="138" height="72" rx="8" fill="#dcfce7" stroke="#10b981"/>
    <text x="257" y="84" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">İçsel (Özsel) Değer</text>
    <text x="257" y="101" text-anchor="middle" font-size="9.5" fill="#334155">İnsana faydası olmasa</text>
    <text x="257" y="115" text-anchor="middle" font-size="9.5" fill="#334155">bile sırf var olduğu için</text>
    <text x="257" y="129" text-anchor="middle" font-size="9.5" fill="#334155">kendi başına değerli olması</text>

    <rect x="40" y="148" width="286" height="48" rx="8" fill="#ccfbf1" stroke="#14b8a6"/>
    <text x="183" y="166" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#115e59">Sürdürülebilirlik ve Nesiller Arası Eşitlik</text>
    <text x="183" y="183" text-anchor="middle" font-size="9.5" fill="#1e293b">Doğayı gelecek kuşakların hakkını tüketmeden korumak</text>

    <!-- Sağ: Richard Routley Son İnsan Deneyi -->
    <rect x="352" y="54" width="300" height="154" rx="10" fill="#ffffff" stroke="#0284c7" stroke-width="1.8"/>
    <text x="502" y="75" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#0369a1">Richard Routley: "Son İnsan" Düşünce Deneyi</text>
    <text x="366" y="96" font-size="9.8" fill="#334155">• Küresel felaket sonrası dünyada kalan &lt;tspan font-weight="bold">son insan&lt;/tspan>,</text>
    <text x="376" y="111" font-size="9.8" fill="#334155">ölmeden önce tüm ağaçları ve canlıları yok eder.</text>
    <text x="366" y="130" font-size="9.8" fill="#334155">• Zarar görecek başka hiçbir insan kalmamıştır.</text>
    <text x="366" y="149" font-size="9.8" fill="#334155">• &lt;tspan font-weight="bold" fill="#b91c1c">Soru:&lt;/tspan> Bu eylem neden yine de ahlaken yanlıştır?</text>
    <rect x="366" y="161" width="272" height="35" rx="7" fill="#e0f2fe"/>
    <text x="502" y="177" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#0c4a6e">Çıkarım: Doğanın değeri insana sağladığı yarardan</text>
    <text x="502" y="190" text-anchor="middle" font-size="9.5" font-weight="bold" fill="#0c4a6e">ibaret değildir; doğa kendi başına içsel değer taşır.</text>
    """
    return svg(w, h, ic, "Çevre Etiği Kavramları ve Son İnsan Düşünce Deneyi")


def _gorsel_6():
    w, h = 680, 260
    ic = """
    <rect x="15" y="15" width="650" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="340" y="38" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">AHLAKİ SORUMLULUK ÇEMBERİNİN GENİŞLEMESİ</text>

    <!-- İç içe halkalar (Sol) -->
    <ellipse cx="195" cy="142" rx="150" ry="88" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="195" y="69" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#166534">EKOSENTRİK (Çevre Merkezci)</text>
    <text x="195" y="83" text-anchor="middle" font-size="9" fill="#15803d">Canlılar + Toprak, Su, Hava, Ekosistem</text>

    <ellipse cx="195" cy="152" rx="108" ry="62" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
    <text x="195" y="106" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#854d0e">BİYOSENTRİK (Canlı Merkezci)</text>
    <text x="195" y="119" text-anchor="middle" font-size="9" fill="#a16207">İnsan + Hayvan + Bitki (Tüm Canlılar)</text>

    <ellipse cx="195" cy="166" rx="64" ry="36" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="195" y="163" text-anchor="middle" font-size="10" font-weight="bold" fill="#991b1b">ANTROPOSENTRİK</text>
    <text x="195" y="177" text-anchor="middle" font-size="9" fill="#b91c1c">(Yalnızca İnsan)</text>

    <!-- Sağ: Temsilciler ve Diğer Yaklaşımlar -->
    <rect x="365" y="54" width="285" height="175" rx="10" fill="#ffffff" stroke="#64748b" stroke-width="1.5"/>
    <text x="507" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">ÇAĞDAŞ ÇEVRE ETİĞİ YAKLAŞIMLARI</text>

    <text x="378" y="96" font-size="10" fill="#334155">• &lt;tspan font-weight="bold" fill="#b91c1c">İnsan Merkezci:&lt;/tspan> Doğa araçsal değer taşır.</text>
    <text x="378" y="116" font-size="10" fill="#334155">• &lt;tspan font-weight="bold" fill="#854d0e">Canlı Merkezci (Paul W. Taylor):&lt;/tspan> Doğaya</text>
    <text x="388" y="130" font-size="9.5" fill="#475569">Saygı etiği; her canlı kendi iyiliğine yönelir.</text>
    <text x="378" y="150" font-size="10" fill="#334155">• &lt;tspan font-weight="bold" fill="#166534">Çevre Merkezci (Aldo Leopold):&lt;/tspan> Toprak etiği;</text>
    <text x="388" y="164" font-size="9.5" fill="#475569">cansız unsurlar dahil tüm ekosistem değerlidir.</text>
    <text x="378" y="184" font-size="10" fill="#334155">• &lt;tspan font-weight="bold" fill="#0369a1">Derin Ekoloji (Arne Naess):&lt;/tspan> Biyosferik eşitlik.</text>
    <text x="378" y="204" font-size="10" fill="#334155">• &lt;tspan font-weight="bold" fill="#6d28d9">Fütüristik Yaklaşım:&lt;/tspan> Gelecek kuşakların hakkı.</text>
    """
    return svg(w, h, ic, "Çevre Etiği Yaklaşımlarının Ahlaki Kapsam Halkaları")


def uygula(v):
    gorseller = [
        _gorsel_1(),
        _gorsel_2(),
        _gorsel_3(),
        _gorsel_4(),
        _gorsel_5(),
        _gorsel_6(),
    ]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g