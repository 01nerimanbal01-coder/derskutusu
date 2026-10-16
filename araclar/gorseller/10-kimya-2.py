from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#0f172a">KİMYADA ÜÇ GÖSTERİM DÜZEYİ (JOHNSTONE ÜÇGENİ): SU (H₂O) ÖRNEĞİ</text>

    <!-- Üçgen kenarları -->
    <polygon points="310,56 145,180 475,180" fill="#eff6ff" stroke="#3b82f6" stroke-width="2.2"/>
    <text x="310" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#1e40af">Birbirini Tamamlayan</text>
    <text x="310" y="153" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#1e40af">Üç Gösterim</text>

    <!-- Üst Köşe: Makroskobik -->
    <rect x="205" y="44" width="210" height="46" rx="9" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
    <text x="310" y="62" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1d4ed8">MAKROSKOBİK GÖSTERİM</text>
    <text x="310" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#1e3a8a">Beş duyu ve ölçüm (Bardaktaki sıvı su)</text>

    <!-- Sol Alt Köşe: Alt Mikroskobik -->
    <rect x="24" y="148" width="228" height="58" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>
    <text x="122" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#15803d">ALT MİKROSKOBİK GÖSTERİM</text>
    <text x="122" y="181" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#14532d">Atom, molekül, elektron modelleri</text>
    <text x="122" y="195" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#166534">(1 kırmızı O, 2 beyaz H küresi)</text>
    <!-- Mini H2O modeli -->
    <circle cx="226" cy="175" r="9" fill="#dc2626"/>
    <circle cx="215" cy="187" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="237" cy="187" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>

    <!-- Sağ Alt Köşe: Sembolik -->
    <rect x="368" y="148" width="228" height="58" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="1.6"/>
    <text x="482" y="166" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#b45309">SEMBOLİK GÖSTERİM</text>
    <text x="482" y="181" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">Formül, denklem ve grafikler</text>
    <text x="482" y="196" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#78350f">2H₂(g) + O₂(g) → 2H₂O(s)</text>
    """
    return svg(w, h, ic, "Kimyada makroskobik, alt mikroskobik ve sembolik gösterim üçgeni")


def _gorsel_2():
    w, h = 620, 235
    ic = f"""
    <rect x="12" y="12" width="596" height="211" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="33" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">METANIN YANMASI: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(s) OLUŞUM SÜRECİ MODELİ</text>

    <!-- 1. Kutucuk: Tepkime Öncesi -->
    <rect x="24" y="46" width="174" height="162" rx="10" fill="#ffffff" stroke="#2563eb" stroke-width="1.5"/>
    <rect x="24" y="46" width="174" height="24" rx="10" fill="#dbeafe"/>
    <text x="111" y="62" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1d4ed8">1. TEPKİME ÖNCESİ</text>

    <!-- CH4 molekülü -->
    <line x1="76" y1="112" x2="60" y2="96" stroke="#475569" stroke-width="2"/>
    <line x1="76" y1="112" x2="92" y2="96" stroke="#475569" stroke-width="2"/>
    <line x1="76" y1="112" x2="60" y2="128" stroke="#475569" stroke-width="2"/>
    <line x1="76" y1="112" x2="92" y2="128" stroke="#475569" stroke-width="2"/>
    <circle cx="76" cy="112" r="11" fill="#1e293b"/>
    <text x="76" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">C</text>
    <circle cx="58" cy="94" r="6.5" fill="#ffffff" stroke="#475569" stroke-width="1.4"/>
    <circle cx="94" cy="94" r="6.5" fill="#ffffff" stroke="#475569" stroke-width="1.4"/>
    <circle cx="58" cy="130" r="6.5" fill="#ffffff" stroke="#475569" stroke-width="1.4"/>
    <circle cx="94" cy="130" r="6.5" fill="#ffffff" stroke="#475569" stroke-width="1.4"/>

    <!-- 2 adet O2 molekülü -->
    <circle cx="144" cy="95" r="8.5" fill="#dc2626"/>
    <circle cx="160" cy="95" r="8.5" fill="#dc2626"/>
    <circle cx="144" cy="130" r="8.5" fill="#dc2626"/>
    <circle cx="160" cy="130" r="8.5" fill="#dc2626"/>

    <text x="111" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">1 CH₄ + 2 O₂ molekülü</text>
    <text x="111" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#475569">C–H ve O=O bağları sağlam</text>
    <text x="111" y="197" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">(1 C, 4 H, 4 O atomu)</text>

    <!-- Ok 1 -->
    <line x1="201" y1="126" x2="219" y2="126" stroke="#64748b" stroke-width="2.2"/>
    <polygon points="219,122 226,126 219,130" fill="#64748b"/>

    <!-- 2. Kutucuk: Tepkime Süreci -->
    <rect x="228" y="46" width="164" height="162" rx="10" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="228" y="46" width="164" height="24" rx="10" fill="#fef3c7"/>
    <text x="310" y="62" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#b45309">2. TEPKİME SÜRECİ</text>

    <!-- Kopan bağlar ve serbestleşen atomlar -->
    <circle cx="310" cy="112" r="10.5" fill="#1e293b"/>
    <text x="310" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">C</text>
    <circle cx="272" cy="92" r="8" fill="#dc2626"/>
    <circle cx="348" cy="92" r="8" fill="#dc2626"/>
    <circle cx="272" cy="134" r="8" fill="#dc2626"/>
    <circle cx="348" cy="134" r="8" fill="#dc2626"/>
    <circle cx="252" cy="112" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <circle cx="292" cy="84" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <circle cx="328" cy="84" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <circle cx="368" cy="112" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <line x1="282" y1="98" x2="300" y2="108" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,2"/>
    <line x1="338" y1="98" x2="320" y2="108" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,2"/>

    <text x="310" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">Etkin Çarpışma</text>
    <text x="310" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#78350f">Eski bağlar kopar, atomlar</text>
    <text x="310" y="197" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b45309">yeniden düzenlenir</text>

    <!-- Ok 2 -->
    <line x1="395" y1="126" x2="413" y2="126" stroke="#64748b" stroke-width="2.2"/>
    <polygon points="413,122 420,126 413,130" fill="#64748b"/>

    <!-- 3. Kutucuk: Tepkime Sonucu -->
    <rect x="422" y="46" width="174" height="162" rx="10" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="422" y="46" width="174" height="24" rx="10" fill="#dcfce7"/>
    <text x="509" y="62" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#15803d">3. TEPKİME SONUCU</text>

    <!-- CO2 doğrusal molekül -->
    <circle cx="489" cy="94" r="8.5" fill="#dc2626"/>
    <circle cx="509" cy="94" r="10.5" fill="#1e293b"/>
    <circle cx="529" cy="94" r="8.5" fill="#dc2626"/>
    <text x="509" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#ffffff">C</text>

    <!-- 2 adet H2O açısal molekül -->
    <circle cx="476" cy="130" r="8.5" fill="#dc2626"/>
    <circle cx="465" cy="142" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <circle cx="487" cy="142" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>

    <circle cx="542" cy="130" r="8.5" fill="#dc2626"/>
    <circle cx="531" cy="142" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>
    <circle cx="553" cy="142" r="6" fill="#ffffff" stroke="#475569" stroke-width="1.3"/>

    <text x="509" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#166534">1 CO₂ + 2 H₂O molekülü</text>
    <text x="509" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#14532d">Yeni C=O ve O–H bağları</text>
    <text x="509" y="197" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">(1 C, 4 H, 4 O korundu)</text>
    """
    return svg(w, h, ic, "Metan gazının yanma tepkimesinin alt mikroskobik oluşum aşamaları")


def _gorsel_5():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">ETİL ALKOL (C₂H₅OH) MOLEKÜLÜNÜN DÖRT FARKLI GÖSTERİM YÖNTEMİ</text>

    <!-- 1. Top-Çubuk -->
    <rect x="22" y="48" width="138" height="154" rx="10" fill="#ffffff" stroke="#3b82f6" stroke-width="1.4"/>
    <text x="91" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1d4ed8">Top-Çubuk Modeli</text>
    <line x1="62" y1="120" x2="90" y2="120" stroke="#64748b" stroke-width="3"/>
    <line x1="90" y1="120" x2="116" y2="108" stroke="#64748b" stroke-width="3"/>
    <line x1="116" y1="108" x2="134" y2="120" stroke="#64748b" stroke-width="2.5"/>
    <line x1="62" y1="120" x2="46" y2="104" stroke="#64748b" stroke-width="2.2"/>
    <line x1="62" y1="120" x2="46" y2="136" stroke="#64748b" stroke-width="2.2"/>
    <line x1="62" y1="120" x2="62" y2="144" stroke="#64748b" stroke-width="2.2"/>
    <line x1="90" y1="120" x2="90" y2="96" stroke="#64748b" stroke-width="2.2"/>
    <line x1="90" y1="120" x2="90" y2="144" stroke="#64748b" stroke-width="2.2"/>
    <circle cx="62" cy="120" r="9" fill="#1e293b"/>
    <circle cx="90" cy="120" r="9" fill="#1e293b"/>
    <circle cx="116" cy="108" r="8.5" fill="#dc2626"/>
    <circle cx="134" cy="120" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="46" cy="104" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="46" cy="136" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="62" cy="144" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="90" cy="96" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="90" cy="144" r="5.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <text x="91" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Atomlar küre, bağlar</text>
    <text x="91" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">çubukla gösterilir</text>

    <!-- 2. Uzay-Dolgu -->
    <rect x="170" y="48" width="138" height="154" rx="10" fill="#ffffff" stroke="#16a34a" stroke-width="1.4"/>
    <text x="239" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#15803d">Uzay-Dolgu Modeli</text>
    <circle cx="204" cy="106" r="9" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="204" cy="134" r="9" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="218" cy="120" r="15" fill="#1e293b"/>
    <circle cx="240" cy="120" r="15" fill="#1e293b"/>
    <circle cx="240" cy="101" r="9" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="240" cy="139" r="9" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <circle cx="261" cy="112" r="13.5" fill="#dc2626"/>
    <circle cx="274" cy="121" r="8.5" fill="#ffffff" stroke="#475569" stroke-width="1.2"/>
    <text x="239" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Çubuksuz, yapışık ve</text>
    <text x="239" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">boyutla orantılı küreler</text>

    <!-- 3. Lewis Nokta Yapısı -->
    <rect x="318" y="48" width="138" height="154" rx="10" fill="#ffffff" stroke="#d97706" stroke-width="1.4"/>
    <text x="387" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b45309">Lewis Nokta Yapısı</text>
    <text x="364" y="96" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1e293b">H   H</text>
    <text x="387" y="120" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="800" fill="#1e293b">H : C : C : O : H</text>
    <text x="364" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1e293b">H   H</text>
    <circle cx="408" cy="105" r="1.6" fill="#dc2626"/>
    <circle cx="414" cy="105" r="1.6" fill="#dc2626"/>
    <circle cx="408" cy="127" r="1.6" fill="#dc2626"/>
    <circle cx="414" cy="127" r="1.6" fill="#dc2626"/>
    <text x="387" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Değerlik elektronları</text>
    <text x="387" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b45309">noktalarla gösterilir</text>

    <!-- 4. Çizgi Bağ Gösterimi -->
    <rect x="466" y="48" width="132" height="154" rx="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.4"/>
    <text x="532" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#6d28d9">Çizgi Bağ Gösterimi</text>
    <line x1="488" y1="132" x2="518" y2="108" stroke="#1e293b" stroke-width="3"/>
    <line x1="518" y1="108" x2="546" y2="124" stroke="#1e293b" stroke-width="3"/>
    <circle cx="488" cy="132" r="3" fill="#6d28d9"/>
    <circle cx="518" cy="108" r="3" fill="#6d28d9"/>
    <text x="564" y="129" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#dc2626">OH</text>
    <text x="532" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Karbonlar köşe noktası,</text>
    <text x="532" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#6d28d9">bağlar çizgi ile gösterilir</text>
    """
    return svg(w, h, ic, "Etil alkol molekülünün top-çubuk, uzay-dolgu, Lewis ve çizgi bağ gösterimleri")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _gorsel_1()
    if len(b) > 2:
        b[2]["gorsel"] = _gorsel_2()
    if len(b) > 4:
        b[4]["gorsel"] = _gorsel_5()
