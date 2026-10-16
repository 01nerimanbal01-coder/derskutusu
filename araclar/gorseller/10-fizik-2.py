from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#0f172a">İKİ KADEMELİ TAŞIYICI BANT SİSTEMİ VE PARÇALI x-t GRAFİĞİ</text>

    <!-- Sol: İki taşıyıcı bant şeması -->
    <rect x="26" y="48" width="270" height="154" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="161" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e293b">Ardışık İki Taşıyıcı Bant (Kademe 1 ve 2)</text>

    <!-- Bant 1 -->
    <rect x="38" y="112" width="105" height="22" rx="11" fill="#dbeafe" stroke="#2563eb" stroke-width="1.8"/>
    <circle cx="50" cy="123" r="6" fill="#2563eb"/>
    <circle cx="131" cy="123" r="6" fill="#2563eb"/>
    <rect x="68" y="88" width="32" height="22" rx="4" fill="#3b82f6"/>
    <text x="84" y="103" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#ffffff">Koli</text>
    <text x="90" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#1d4ed8">1. Bant: Δx₁ = 12 m</text>
    <text x="90" y="164" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#1e40af">Δt₁ = 4 s ⇒ v₁ = 3 m/s</text>

    <!-- Bant 2 -->
    <rect x="149" y="112" width="135" height="22" rx="11" fill="#dcfce7" stroke="#16a34a" stroke-width="1.8"/>
    <circle cx="161" cy="123" r="6" fill="#16a34a"/>
    <circle cx="272" cy="123" r="6" fill="#16a34a"/>
    <rect x="195" y="88" width="32" height="22" rx="4" fill="#16a34a"/>
    <text x="211" y="103" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#ffffff">Koli</text>
    <text x="216" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#15803d">2. Bant: Δx₂ = 24 m</text>
    <text x="216" y="164" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#166534">Δt₂ = 6 s ⇒ v₂ = 4 m/s</text>

    <rect x="42" y="175" width="238" height="20" rx="5" fill="#fef3c7"/>
    <text x="161" y="189" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#92400e">0 - 9 s arası: Δx = 12 + (4 · 5) = 32 m</text>

    <!-- Sağ: Parçalı x-t grafiği -->
    <rect x="312" y="48" width="280" height="154" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="452" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e293b">Parçalı Konum-Zaman (x-t) Grafiği</text>

    <!-- Eksenler -->
    <line x1="352" y1="176" x2="568" y2="176" stroke="#334155" stroke-width="1.5"/>
    <line x1="352" y1="176" x2="352" y2="76" stroke="#334155" stroke-width="1.5"/>
    <text x="574" y="179" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">t (s)</text>
    <text x="346" y="73" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">x (m)</text>

    <!-- Kılavuz çizgileri -->
    <line x1="352" y1="146" x2="424" y2="146" stroke="#94a3b8" stroke-dasharray="3,3"/>
    <line x1="424" y1="146" x2="424" y2="176" stroke="#94a3b8" stroke-dasharray="3,3"/>
    <line x1="352" y1="86" x2="532" y2="86" stroke="#94a3b8" stroke-dasharray="3,3"/>
    <line x1="532" y1="86" x2="532" y2="176" stroke="#94a3b8" stroke-dasharray="3,3"/>

    <!-- Doğrular -->
    <line x1="352" y1="176" x2="424" y2="146" stroke="#2563eb" stroke-width="3"/>
    <line x1="424" y1="146" x2="532" y2="86" stroke="#16a34a" stroke-width="3"/>
    <circle cx="424" cy="146" r="4" fill="#dc2626"/>
    <circle cx="532" cy="86" r="4" fill="#16a34a"/>

    <!-- Etiketler -->
    <text x="346" y="149" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">12</text>
    <text x="346" y="89" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#16a34a">36</text>
    <text x="424" y="190" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">4</text>
    <text x="532" y="190" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#16a34a">10</text>
    <text x="388" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#1d4ed8">Eğim = 3</text>
    <text x="492" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#15803d">Eğim = 4 (daha dik)</text>
    """
    return svg(w, h, ic, "Parçalı sabit hızlı harekette iki taşıyıcı bant ve kırılmalı x-t grafiği")


def _gorsel_2():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#0f172a">ÇOK BÖLMELİ KONUM-ZAMAN (x-t) GRAFİĞİNDE DURMA VE YÖN DEĞİŞTİRME</text>

    <!-- Grafik Alanı -->
    <rect x="26" y="46" width="340" height="158" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="64" y1="172" x2="344" y2="172" stroke="#334155" stroke-width="1.5"/>
    <line x1="64" y1="172" x2="64" y2="62" stroke="#334155" stroke-width="1.5"/>
    <text x="350" y="175" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">t (s)</text>
    <text x="58" y="62" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">x (m)</text>

    <!-- Kılavuzlar -->
    <line x1="64" y1="82" x2="224" y2="82" stroke="#cbd5e1" stroke-dasharray="3,3"/>
    <line x1="144" y1="82" x2="144" y2="172" stroke="#cbd5e1" stroke-dasharray="3,3"/>
    <line x1="224" y1="82" x2="224" y2="172" stroke="#cbd5e1" stroke-dasharray="3,3"/>
    <line x1="64" y1="148" x2="314" y2="148" stroke="#cbd5e1" stroke-dasharray="3,3"/>
    <line x1="314" y1="148" x2="314" y2="172" stroke="#cbd5e1" stroke-dasharray="3,3"/>

    <!-- 3 Bölge Çizgileri -->
    <line x1="64" y1="172" x2="144" y2="82" stroke="#2563eb" stroke-width="3.2"/>
    <line x1="144" y1="82" x2="224" y2="82" stroke="#f59e0b" stroke-width="3.2"/>
    <line x1="224" y1="82" x2="314" y2="148" stroke="#dc2626" stroke-width="3.2"/>

    <circle cx="144" cy="82" r="4" fill="#2563eb"/>
    <circle cx="224" cy="82" r="4.5" fill="#dc2626"/>
    <circle cx="314" cy="148" r="4" fill="#dc2626"/>

    <text x="56" y="86" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">+24</text>
    <text x="56" y="151" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">+6</text>
    <text x="56" y="175" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">0</text>
    <text x="144" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">3</text>
    <text x="224" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#d97706">5</text>
    <text x="314" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">8</text>

    <text x="95" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1d4ed8">I (+x yönü)</text>
    <text x="184" y="74" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#b45309">II (Duruyor)</text>
    <text x="282" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#b91c1c">III (-x yönü)</text>

    <!-- Sağ: Çözüm Özeti -->
    <rect x="380" y="46" width="214" height="158" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <rect x="390" y="56" width="194" height="32" rx="6" fill="#eff6ff"/>
    <text x="487" y="70" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1d4ed8">I. Bölge (0-3 s): Δx₁ = +24 m</text>
    <text x="487" y="82" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#1e40af">v₁ = +24 / 3 = +8 m/s (+x yönü)</text>

    <rect x="390" y="94" width="194" height="32" rx="6" fill="#fef3c7"/>
    <text x="487" y="108" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#b45309">II. Bölge (3-5 s): Δx₂ = 0 m</text>
    <text x="487" y="120" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#92400e">v₂ = 0 m/s (Yatay doğru = Bekleme)</text>

    <rect x="390" y="132" width="194" height="32" rx="6" fill="#fee2e2"/>
    <text x="487" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#b91c1c">III. Bölge (5-8 s): Δx₃ = -18 m</text>
    <text x="487" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#991b1b">v₃ = -18 / 3 = -6 m/s (Geri dönüş)</text>

    <text x="487" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#0f172a">Yol: d = 24 + 0 + 18 = 42 m</text>
    <text x="487" y="196" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">Yer Değiştirme: Δx = +6 - 0 = +6 m</text>
    """
    return svg(w, h, ic, "Çok bölmeli konum-zaman grafiğinde ilerleme, durma ve geri dönüş bölgeleri")


def _gorsel_3():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#0f172a">İKİ HAREKETLİNİN KARŞILAŞMASI VE ORTAK KONUM-ZAMAN (x-t) GRAFİĞİ</text>

    <!-- Sol: Karşılaşma şeması -->
    <rect x="26" y="48" width="276" height="154" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="164" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e293b">Birbirine Doğru Gelen İki Scooter</text>

    <line x1="44" y1="126" x2="284" y2="126" stroke="#475569" stroke-width="2.5"/>
    <circle cx="52" cy="126" r="5" fill="#2563eb"/>
    <circle cx="276" cy="126" r="5" fill="#dc2626"/>
    <circle cx="152" cy="126" r="5" fill="#16a34a"/>

    <!-- Ayla ve Burak okları -->
    <rect x="44" y="92" width="66" height="22" rx="5" fill="#dbeafe" stroke="#2563eb"/>
    <text x="77" y="107" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1d4ed8">v₁ = +5 m/s</text>
    <line x1="114" y1="103" x2="140" y2="103" stroke="#2563eb" stroke-width="2.2"/>
    <polygon points="140,99 148,103 140,107" fill="#2563eb"/>

    <rect x="214" y="92" width="68" height="22" rx="5" fill="#fee2e2" stroke="#dc2626"/>
    <text x="248" y="107" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#b91c1c">v₂ = -7 m/s</text>
    <line x1="210" y1="103" x2="184" y2="103" stroke="#dc2626" stroke-width="2.2"/>
    <polygon points="184,99 176,103 184,107" fill="#dc2626"/>

    <text x="52" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">K (0 m)</text>
    <text x="152" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">200 m</text>
    <text x="276" y="143" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">L (480 m)</text>

    <rect x="40" y="156" width="248" height="36" rx="6" fill="#ecfdf5" stroke="#10b981"/>
    <text x="164" y="171" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#047857">t = d / (v₁ + v₂) = 480 / (5 + 7) = 40 s</text>
    <text x="164" y="185" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" fill="#065f46">Karşılaşma Konumu: x = 5 · 40 = 200 m</text>

    <!-- Sağ: Ortak x-t grafiği -->
    <rect x="316" y="48" width="276" height="154" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="454" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1e293b">Ortak x-t Grafiğinde Kesişim Noktası</text>

    <line x1="358" y1="174" x2="564" y2="174" stroke="#334155" stroke-width="1.5"/>
    <line x1="358" y1="174" x2="358" y2="76" stroke="#334155" stroke-width="1.5"/>
    <text x="570" y="177" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">t (s)</text>
    <text x="352" y="75" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#334155">x (m)</text>

    <!-- Kesişen doğrular -->
    <line x1="358" y1="174" x2="486" y2="132" stroke="#2563eb" stroke-width="2.8"/>
    <line x1="358" y1="84" x2="486" y2="132" stroke="#dc2626" stroke-width="2.8"/>

    <line x1="358" y1="132" x2="486" y2="132" stroke="#16a34a" stroke-dasharray="3,3"/>
    <line x1="486" y1="132" x2="486" y2="174" stroke="#16a34a" stroke-dasharray="3,3"/>
    <circle cx="486" cy="132" r="5" fill="#16a34a"/>

    <text x="352" y="88" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">480</text>
    <text x="352" y="135" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">200</text>
    <text x="352" y="177" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">0</text>
    <text x="486" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">40</text>
    <text x="532" y="128" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#15803d">Karşılaşma</text>
    <text x="532" y="140" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#15803d">Noktası</text>
    """
    return svg(w, h, ic, "Birbirine doğru gelen iki hareketlinin karşılaşma süresi ve ortak x-t grafiği")


def _gorsel_5():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="800" fill="#0f172a">KONUM-ZAMAN (x-t) VE HIZ-ZAMAN (v-t) GRAFİKLERİ ARASINDA DÖNÜŞÜM</text>

    <!-- Sol: x-t grafiği -->
    <rect x="26" y="48" width="218" height="150" rx="10" fill="#ffffff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="135" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#1d4ed8">Konum-Zaman (x-t) Grafiği</text>
    <line x1="56" y1="158" x2="224" y2="158" stroke="#334155" stroke-width="1.4"/>
    <line x1="56" y1="178" x2="56" y2="78" stroke="#334155" stroke-width="1.4"/>
    <line x1="56" y1="138" x2="188" y2="88" stroke="#2563eb" stroke-width="3"/>
    <circle cx="56" cy="138" r="3.5" fill="#2563eb"/>
    <circle cx="188" cy="88" r="3.5" fill="#2563eb"/>
    <text x="48" y="141" text-anchor="end" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#2563eb">x₀</text>
    <text x="48" y="91" text-anchor="end" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#2563eb">x</text>
    <text x="188" y="172" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#334155">t</text>
    <text x="135" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#1e40af">Eğim = (x - x₀) / t = v</text>

    <!-- Orta: Dönüşüm okları -->
    <rect x="254" y="68" width="112" height="46" rx="8" fill="#dbeafe" stroke="#2563eb"/>
    <text x="310" y="86" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1d4ed8">EĞİM AL ──►</text>
    <text x="310" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#1e3a8a">v = Δx / Δt</text>

    <rect x="254" y="130" width="112" height="52" rx="8" fill="#dcfce7" stroke="#16a34a"/>
    <text x="310" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#15803d">◄── ALAN BUL</text>
    <text x="310" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" fill="#14532d">Δx = v · Δt</text>
    <text x="310" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#166534">x_son = x₀ + Δx</text>

    <!-- Sağ: v-t grafiği -->
    <rect x="376" y="48" width="218" height="150" rx="10" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
    <text x="485" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#15803d">Hız-Zaman (v-t) Grafiği</text>
    <line x1="406" y1="158" x2="574" y2="158" stroke="#334155" stroke-width="1.4"/>
    <line x1="406" y1="178" x2="406" y2="78" stroke="#334155" stroke-width="1.4"/>
    <rect x="406" y="102" width="132" height="56" fill="#bbf7d0" opacity="0.7"/>
    <line x1="406" y1="102" x2="538" y2="102" stroke="#16a34a" stroke-width="3"/>
    <line x1="538" y1="102" x2="538" y2="158" stroke="#16a34a" stroke-dasharray="3,3"/>
    <text x="398" y="105" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#15803d">v</text>
    <text x="538" y="172" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#334155">t</text>
    <text x="472" y="134" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#14532d">Alan = Δx = v · t</text>
    <text x="485" y="188" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="700" fill="#166534">Eğim = 0 (Sabit Hız)</text>
    """
    return svg(w, h, ic, "Konum-zaman ve hız-zaman grafikleri arasında eğim ve alan ile çift yönlü dönüşüm")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _gorsel_1()
    if len(b) > 1:
        b[1]["gorsel"] = _gorsel_2()
    if len(b) > 2:
        b[2]["gorsel"] = _gorsel_3()
    if len(b) > 4:
        b[4]["gorsel"] = _gorsel_5()
