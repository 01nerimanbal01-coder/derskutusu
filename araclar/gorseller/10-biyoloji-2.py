from ozet_gorsel import svg


def _gorsel_2():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">GÖRÜNÜR IŞIK SPEKTRUMU (380 - 750 nm) VE ENGELMANN DENEYİ</text>

    <!-- Sol: Görünür Spektrum ve Dalga Boyu -->
    <rect x="24" y="48" width="276" height="150" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="162" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1e293b">Elektromanyetik Spektrum ve Görünür Işık</text>

    <!-- Renk barları -->
    <rect x="38" y="82" width="40" height="24" fill="#7c3aed"/>
    <rect x="78" y="82" width="40" height="24" fill="#2563eb"/>
    <rect x="118" y="82" width="48" height="24" fill="#16a34a"/>
    <rect x="166" y="82" width="38" height="24" fill="#eab308"/>
    <rect x="204" y="82" width="38" height="24" fill="#f97316"/>
    <rect x="242" y="82" width="44" height="24" fill="#dc2626"/>

    <text x="58" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Mor</text>
    <text x="98" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Mavi</text>
    <text x="142" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Yeşil</text>
    <text x="185" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Sarı</text>
    <text x="223" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Turuncu</text>
    <text x="264" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Kırmızı</text>

    <text x="40" y="120" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#6d28d9">380 nm (Yüksek enerji)</text>
    <text x="284" y="120" text-anchor="end" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#b91c1c">750 nm (Düşük enerji)</text>

    <rect x="38" y="132" width="248" height="54" rx="7" fill="#f0fdf4" stroke="#16a34a"/>
    <text x="162" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">Klorofil: Mor, Mavi ve Kırmızıyı Çok Soğurur</text>
    <text x="162" y="163" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#166534">Yeşil ışığı yansıtır/geçirir (En düşük hız)</text>
    <text x="162" y="177" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#14532d">Karoten, ksantofil, likopen: Yardımcı pigmentler</text>

    <!-- Sağ: Engelmann Deneyi ve Fotosentez Hızı Eğrisi -->
    <rect x="314" y="48" width="282" height="150" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="455" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1e293b">Engelmann Deneyi ve Dalga Boyu - Hız Grafiği</text>

    <!-- Eksenler -->
    <line x1="348" y1="154" x2="574" y2="154" stroke="#334155" stroke-width="1.5"/>
    <line x1="348" y1="154" x2="348" y2="78" stroke="#334155" stroke-width="1.5"/>
    <text x="342" y="84" text-anchor="end" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#334155">Hız</text>

    <!-- Fotosentez hızı eğrisi (mor-mavi yüksek, yeşil çukur, kırmızı yüksek) -->
    <path d="M 356,92 C 385,84 405,90 425,138 C 445,148 475,146 500,122 C 525,92 545,88 564,100" fill="none" stroke="#16a34a" stroke-width="3"/>

    <!-- Aerobik bakteri kümeleri -->
    <circle cx="372" cy="144" r="3" fill="#dc2626"/>
    <circle cx="380" cy="140" r="3" fill="#dc2626"/>
    <circle cx="388" cy="145" r="3" fill="#dc2626"/>
    <circle cx="396" cy="141" r="3" fill="#dc2626"/>
    <circle cx="456" cy="148" r="3" fill="#dc2626"/>
    <circle cx="532" cy="143" r="3" fill="#dc2626"/>
    <circle cx="540" cy="139" r="3" fill="#dc2626"/>
    <circle cx="548" cy="145" r="3" fill="#dc2626"/>

    <text x="384" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#4338ca">Mor-Mavi</text>
    <text x="456" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#15803d">Yeşil</text>
    <text x="540" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#dc2626">Kırmızı</text>
    <text x="455" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#991b1b">● O₂ seven bakteriler mor-mavi ve kırmızıda kümelenir</text>
    """
    return svg(w, h, ic, "Görünür ışık spektrumu, dalga boyu-hız grafiği ve Engelmann deneyi")


def _gorsel_4():
    w, h = 620, 240
    ic = f"""
    <rect x="12" y="12" width="596" height="216" rx="14" fill="#f0fdf4" stroke="#86efac" stroke-width="1.8"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#064e3b">KLOROPLASTTA FOTOSENTEZ MODELİ: GRANUM VE STROMA ARASINDAKİ DÖNGÜ</text>

    <!-- Sol Kutu: Granum (Işığın Kullanıldığı Tepkimeler) -->
    <rect x="26" y="54" width="218" height="142" rx="12" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="135" y="73" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#14532d">IŞIĞIN KULLANILDIĞI</text>
    <text x="135" y="87" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#14532d">TEPKİMELER (GRANUM)</text>
    <text x="135" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#166534">• Klorofil ışıkla uyarılır, ETS çalışır</text>
    <text x="135" y="121" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#15803d">• Fotoliz: H₂O → 2e⁻ + 2H⁺ + ½O₂</text>
    <text x="135" y="136" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#166534">• ATP ve NADPH sentezlenir</text>

    <!-- Giren H2O ve Işık / Çıkan O2 -->
    <rect x="38" y="148" width="90" height="36" rx="6" fill="#fef9c3" stroke="#eab308"/>
    <text x="83" y="163" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#854d0e">GİRENLER:</text>
    <text x="83" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#713f12">Işık + H₂O</text>

    <rect x="138" y="148" width="94" height="36" rx="6" fill="#dbeafe" stroke="#2563eb"/>
    <text x="185" y="163" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#1e40af">ÇIKAN:</text>
    <text x="185" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">O₂ (Atmosfere)</text>

    <!-- Orta: ATP & NADPH Gidiş / ADP, Pi, NADP+ Dönüş -->
    <rect x="256" y="64" width="108" height="48" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="310" y="82" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b45309">ATP ve NADPH</text>
    <text x="310" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#92400e">──────►</text>

    <rect x="256" y="132" width="108" height="48" rx="8" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>
    <text x="310" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#3730a3">◄──────</text>
    <text x="310" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#4338ca">ADP + Pᵢ + NADP⁺</text>

    <!-- Sağ Kutu: Stroma (Calvin Döngüsü) -->
    <rect x="376" y="54" width="218" height="142" rx="12" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
    <text x="485" y="73" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#065f46">IŞIĞIN KULLANILMADIĞI</text>
    <text x="485" y="87" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#065f46">TEPKİMELER (STROMA)</text>
    <text x="485" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#047857">• Calvin Döngüsü (Enzim kontrolü)</text>
    <text x="485" y="121" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#065f46">• CO₂ indirgenir, PGAL üretilir</text>
    <text x="485" y="136" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#065f46">• Klorofil ve ETS görev almaz</text>

    <rect x="388" y="148" width="90" height="36" rx="6" fill="#fee2e2" stroke="#dc2626"/>
    <text x="433" y="163" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#991b1b">GİREN:</text>
    <text x="433" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">CO₂ (Havadan)</text>

    <rect x="488" y="148" width="94" height="36" rx="6" fill="#dcfce7" stroke="#16a34a"/>
    <text x="535" y="163" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#14532d">ÇIKAN ÜRÜN:</text>
    <text x="535" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">PGAL → C₆H₁₂O₆</text>

    <text x="310" y="214" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#064e3b">Genel Denklem: 6CO₂ + 6H₂O ──[ Işık / Klorofil ]──► C₆H₁₂O₆ (Glikoz) + 6O₂</text>
    """
    return svg(w, h, ic, "Kloroplastın granum ve stroma kısımlarında gerçekleşen fotosentez tepkimeleri modeli")


def _gorsel_5():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">PGAL (FOSFOGLİSERALDEHİT) MOLEKÜLÜNDEN SENTEZLENEN ORGANİK BİLEŞİKLER</text>

    <!-- Merkez: PGAL -->
    <rect x="245" y="50" width="130" height="42" rx="10" fill="#16a34a" stroke="#14532d" stroke-width="2"/>
    <text x="310" y="69" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="800" fill="#ffffff">PGAL (3C)</text>
    <text x="310" y="84" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#dcfce7">Temel Organik Öncül</text>

    <!-- Sol Kol: Azot Tuzu Gerektirmeyenler -->
    <line x1="245" y1="71" x2="155" y2="98" stroke="#2563eb" stroke-width="2.2"/>
    <rect x="26" y="100" width="260" height="98" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="156" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1d4ed8">AZOT TUZU GEREKTİRMEYENLER (C, H, O)</text>
    <rect x="38" y="128" width="112" height="58" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="94" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e3a8a">Glikoz (6C)</text>
    <text x="94" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">→ Sükroz (taşınır)</text>
    <text x="94" y="172" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">→ Nişasta (depolanır)</text>

    <rect x="160" y="128" width="114" height="58" rx="7" fill="#ffffff" stroke="#93c5fd"/>
    <text x="217" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e3a8a">Yağ Asidi + Gliserol</text>
    <text x="217" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">→ Trigliserit (Yağ)</text>
    <text x="217" y="174" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">(Hücre zarı ve depo)</text>

    <!-- Sağ Kol: Topraktan Azot Tuzu Gerektirenler -->
    <line x1="375" y1="71" x2="465" y2="98" stroke="#d97706" stroke-width="2.2"/>
    <rect x="334" y="100" width="260" height="98" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="464" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b45309">+ AZOT TUZLARI EKLENEREK (C, H, O, N)</text>

    <rect x="346" y="128" width="236" height="58" rx="7" fill="#ffffff" stroke="#fcd34d"/>
    <text x="464" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">• Amino asit ──► Protein sentezi</text>
    <text x="464" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">• Vitaminler (Büyüme ve düzenleme)</text>
    <text x="464" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">• Azotlu Organik Bazlar (A, G, C, T, U)</text>
    """
    return svg(w, h, ic, "PGAL molekülünden karbohidrat, yağ, amino asit, vitamin ve organik bazların sentezi")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 1:
        b[1]["gorsel"] = _gorsel_2()
    if len(b) > 3:
        b[3]["gorsel"] = _gorsel_4()
    if len(b) > 4:
        b[4]["gorsel"] = _gorsel_5()
