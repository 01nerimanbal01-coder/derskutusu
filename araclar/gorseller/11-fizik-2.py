from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="15" width="660" height="235" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="40" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">İLK HIZSIZ SERBEST DÜŞMEDE ARDIŞIK YOLLAR (h - 3h - 5h - 7h)</text>
    <line x1="120" y1="55" x2="120" y2="230" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3"/>
    <circle cx="120" cy="60" r="8" fill="#2563eb"/>
    <circle cx="120" cy="80" r="8" fill="#2563eb"/>
    <circle cx="120" cy="120" r="8" fill="#2563eb"/>
    <circle cx="120" cy="175" r="8" fill="#2563eb"/>
    <circle cx="120" cy="230" r="8" fill="#2563eb"/>

    <text x="85" y="64" text-anchor="end" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e3a8a">t = 0</text>
    <text x="85" y="84" text-anchor="end" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e3a8a">t = 1t</text>
    <text x="85" y="124" text-anchor="end" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e3a8a">t = 2t</text>
    <text x="85" y="179" text-anchor="end" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e3a8a">t = 3t</text>
    <text x="85" y="234" text-anchor="end" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e3a8a">t = 4t</text>

    <text x="150" y="64" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#1d4ed8">v = 0</text>
    <text x="150" y="84" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#1d4ed8">v = 1v (10 m/s)</text>
    <text x="150" y="124" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#1d4ed8">v = 2v (20 m/s)</text>
    <text x="150" y="179" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#1d4ed8">v = 3v (30 m/s)</text>
    <text x="150" y="234" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#1d4ed8">v = 4v (40 m/s)</text>

    <rect x="290" y="60" width="170" height="22" rx="5" fill="#dcfce7" stroke="#22c55e"/>
    <text x="375" y="75" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#15803d">1. Aralık: h (5 m)</text>

    <rect x="290" y="88" width="170" height="32" rx="5" fill="#fef3c7" stroke="#f59e0b"/>
    <text x="375" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#b45309">2. Aralık: 3h (15 m)</text>

    <rect x="290" y="126" width="170" height="45" rx="5" fill="#ffedd5" stroke="#f97316"/>
    <text x="375" y="153" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#c2410c">3. Aralık: 5h (25 m)</text>

    <rect x="290" y="177" width="170" height="55" rx="5" fill="#fee2e2" stroke="#ef4444"/>
    <text x="375" y="208" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#b91c1c">4. Aralık: 7h (35 m)</text>

    <rect x="480" y="65" width="180" height="160" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="570" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">TEMEL BAĞINTILAR</text>
    <text x="570" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="600" fill="#1e40af">h = ½ · g · t²</text>
    <text x="570" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="600" fill="#1e40af">v = g · t</text>
    <text x="570" y="174" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="600" fill="#1e40af">v² = 2 · g · h</text>
    <text x="570" y="205" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#1e3a8a">Toplam: h, 4h, 9h, 16h</text>
    """
    return svg(700, 260, ic, "Serbest Düşmede Hız ve Yol İlişkisi")


def gorsel_2():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="40" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">DÜŞEY YUKARI ATIŞ (İLK HIZLI SERBEST DÜŞME: v₀ = 20 m/s)</text>
    <rect x="240" y="55" width="220" height="44" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="350" y="74" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="700" fill="#b45309">TEPE NOKTASI (t = 2 s, h_max = 20 m)</text>
    <text x="350" y="91" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#92400e">Anlık Hız v = 0 m/s | İvme a = -g (-10 m/s²)</text>

    <rect x="45" y="115" width="275" height="105" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="182" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">YÜKSELİŞ SÜRECİ (0 - 2 s)</text>
    <text x="182" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">• Hız (+y) yukarı, ivme (-g) aşağı yönlü</text>
    <text x="182" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">• t = 0 s: v = +20 m/s, y = 0 m</text>
    <text x="182" y="200" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">• t = 1 s: v = +10 m/s, y = +15 m</text>

    <rect x="380" y="115" width="275" height="105" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="517" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#15803d">İNİŞ SÜRECİ (2 - 4 s)</text>
    <text x="517" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">• Hız (-y) ve ivme (-g) aşağı yönlü</text>
    <text x="517" y="180" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">• t = 3 s: v = -10 m/s, y = +15 m</text>
    <text x="517" y="200" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">• t = 4 s: v = -20 m/s, y = 0 m</text>
    """
    return svg(700, 255, ic, "Düşey Yukarı Atışta Hız ve İvme")


def gorsel_3():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="40" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">SERBEST DÜŞME HAREKETİNİN GRAFİKLERİ (v₀ = 0, AŞAĞI YÖN NEGATİF)</text>
    <rect x="35" y="58" width="200" height="170" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="135" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">1. KONUM - ZAMAN (y-t)</text>
    <line x1="65" y1="98" x2="205" y2="98" stroke="#64748b" stroke-width="1.5"/>
    <line x1="65" y1="90" x2="65" y2="195" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 65 98 Q 145 102 195 190" fill="none" stroke="#2563eb" stroke-width="2.5"/>
    <text x="205" y="93" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#475569">t (s)</text>
    <text x="58" y="190" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#1d4ed8">-h</text>
    <text x="135" y="213" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e40af">Parabolik Eğri (Eğim = Hız)</text>

    <rect x="250" y="58" width="200" height="170" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="350" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#15803d">2. HIZ - ZAMAN (v-t)</text>
    <line x1="280" y1="98" x2="420" y2="98" stroke="#64748b" stroke-width="1.5"/>
    <line x1="280" y1="90" x2="280" y2="195" stroke="#64748b" stroke-width="1.5"/>
    <line x1="280" y1="98" x2="410" y2="188" stroke="#16a34a" stroke-width="2.5"/>
    <text x="420" y="93" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#475569">t (s)</text>
    <text x="274" y="190" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#15803d">-v</text>
    <text x="350" y="213" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#166534">Eğim = -g | Alan = Δy</text>

    <rect x="465" y="58" width="200" height="170" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="565" y="78" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#b91c1c">3. İVME - ZAMAN (a-t)</text>
    <line x1="495" y1="98" x2="635" y2="98" stroke="#64748b" stroke-width="1.5"/>
    <line x1="495" y1="90" x2="495" y2="195" stroke="#64748b" stroke-width="1.5"/>
    <line x1="495" y1="155" x2="625" y2="155" stroke="#dc2626" stroke-width="2.5"/>
    <text x="635" y="93" text-anchor="end" font-family="Inter,sans-serif" font-size="10" fill="#475569">t (s)</text>
    <text x="489" y="159" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#dc2626">-g</text>
    <text x="565" y="213" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#991b1b">Sabit İvme (Alan = Δv)</text>
    """
    return svg(700, 260, ic, "Serbest Düşme Konum, Hız ve İvme Grafikleri")


def gorsel_4():
    ic = """
    <rect x="20" y="15" width="660" height="220" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">SERBEST BIRAKILAN (K) VE YATAY ATILAN (L) CİSİMLERİN EŞ ZAMANLILIĞI</text>
    <line x1="80" y1="205" x2="620" y2="205" stroke="#475569" stroke-width="2"/>
    <line x1="140" y1="70" x2="540" y2="70" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="140" y1="95" x2="540" y2="95" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="140" y1="140" x2="540" y2="140" stroke="#cbd5e1" stroke-dasharray="4,4"/>

    <circle cx="150" cy="70" r="8" fill="#2563eb"/>
    <circle cx="150" cy="95" r="8" fill="#2563eb"/>
    <circle cx="150" cy="140" r="8" fill="#2563eb"/>
    <circle cx="150" cy="200" r="8" fill="#2563eb"/>
    <text x="150" y="58" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1d4ed8">K (v₀ = 0)</text>

    <path d="M 210 70 Q 340 72 450 200" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="5,3"/>
    <circle cx="210" cy="70" r="8" fill="#16a34a"/>
    <circle cx="290" cy="95" r="8" fill="#16a34a"/>
    <circle cx="370" cy="140" r="8" fill="#16a34a"/>
    <circle cx="450" cy="200" r="8" fill="#16a34a"/>
    <text x="235" y="58" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#15803d">L (Yatay v₀ₓ)</text>

    <rect x="475" y="80" width="185" height="105" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="567" y="104" text-anchor="middle" font-family="Inter,sans-serif" font-size="11.5" font-weight="700" fill="#b45309">SONUÇ VE KANIT</text>
    <text x="567" y="126" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">Her t anında K ve L'nin</text>
    <text x="567" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">düşey konumları eşittir;</text>
    <text x="567" y="164" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#78350f">Aynı anda yere çarparlar!</text>
    """
    return svg(700, 245, ic, "K ve L Toplarının Düşey Konumlarının Eşitliği")


def uygula(v):
    v["bolumler"][2]["gorsel"] = gorsel_1()
    v["bolumler"][3]["gorsel"] = gorsel_2()
    v["bolumler"][4]["gorsel"] = gorsel_3()
    v["bolumler"][5]["gorsel"] = gorsel_4()
