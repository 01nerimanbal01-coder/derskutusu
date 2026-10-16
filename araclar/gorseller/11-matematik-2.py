from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="40" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">SERPME DİYAGRAMINDA (SAÇILIM GRAFİĞİ) İLİŞKİNİN YÖNÜ</text>
    <rect x="35" y="58" width="200" height="170" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="135" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#15803d">POZİTİF YÖNLÜ İLİŞKİ</text>
    <line x1="65" y1="190" x2="205" y2="190" stroke="#64748b" stroke-width="1.5"/>
    <line x1="65" y1="190" x2="65" y2="95" stroke="#64748b" stroke-width="1.5"/>
    <line x1="75" y1="180" x2="195" y2="105" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,3"/>
    <circle cx="82" cy="175" r="4" fill="#16a34a"/>
    <circle cx="100" cy="162" r="4" fill="#16a34a"/>
    <circle cx="118" cy="154" r="4" fill="#16a34a"/>
    <circle cx="136" cy="140" r="4" fill="#16a34a"/>
    <circle cx="155" cy="130" r="4" fill="#16a34a"/>
    <circle cx="174" cy="118" r="4" fill="#16a34a"/>
    <circle cx="190" cy="108" r="4" fill="#16a34a"/>
    <text x="135" y="212" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#166534">x ve y birlikte artar (r &gt; 0)</text>

    <rect x="250" y="58" width="200" height="170" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="350" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#b91c1c">NEGATİF YÖNLÜ İLİŞKİ</text>
    <line x1="280" y1="190" x2="420" y2="190" stroke="#64748b" stroke-width="1.5"/>
    <line x1="280" y1="190" x2="280" y2="95" stroke="#64748b" stroke-width="1.5"/>
    <line x1="290" y1="105" x2="410" y2="180" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,3"/>
    <circle cx="295" cy="110" r="4" fill="#dc2626"/>
    <circle cx="312" cy="122" r="4" fill="#dc2626"/>
    <circle cx="330" cy="130" r="4" fill="#dc2626"/>
    <circle cx="350" cy="144" r="4" fill="#dc2626"/>
    <circle cx="368" cy="155" r="4" fill="#dc2626"/>
    <circle cx="386" cy="166" r="4" fill="#dc2626"/>
    <circle cx="404" cy="176" r="4" fill="#dc2626"/>
    <text x="350" y="212" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#991b1b">Biri artarken diğeri azalır (r &lt; 0)</text>

    <rect x="465" y="58" width="200" height="170" rx="10" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
    <text x="565" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#334155">İLİŞKİ YOK</text>
    <line x1="495" y1="190" x2="635" y2="190" stroke="#64748b" stroke-width="1.5"/>
    <line x1="495" y1="190" x2="495" y2="95" stroke="#64748b" stroke-width="1.5"/>
    <circle cx="515" cy="115" r="4" fill="#475569"/>
    <circle cx="540" cy="170" r="4" fill="#475569"/>
    <circle cx="560" cy="125" r="4" fill="#475569"/>
    <circle cx="585" cy="160" r="4" fill="#475569"/>
    <circle cx="610" cy="112" r="4" fill="#475569"/>
    <circle cx="620" cy="172" r="4" fill="#475569"/>
    <circle cx="530" cy="142" r="4" fill="#475569"/>
    <text x="565" y="212" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#334155">Rastgele dağılım (r ≈ 0)</text>
    """
    return svg(700, 260, ic, "Serpme Diyagramında İlişkinin Yönü")


def gorsel_2():
    ic = """
    <rect x="20" y="15" width="660" height="225" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">SERPME DİYAGRAMINDA İLİŞKİNİN GÜCÜ (EĞİLİM ÇİZGİSİNE YAKINLIK)</text>
    <rect x="40" y="62" width="195" height="155" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="137" y="84" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">GÜÇLÜ İLİŞKİ (0,70 ≤ |r| &lt; 1)</text>
    <line x1="70" y1="180" x2="205" y2="105" stroke="#93c5fd" stroke-width="2"/>
    <circle cx="80" cy="173" r="4" fill="#1d4ed8"/>
    <circle cx="102" cy="164" r="4" fill="#1d4ed8"/>
    <circle cx="125" cy="148" r="4" fill="#1d4ed8"/>
    <circle cx="148" cy="138" r="4" fill="#1d4ed8"/>
    <circle cx="172" cy="122" r="4" fill="#1d4ed8"/>
    <circle cx="194" cy="112" r="4" fill="#1d4ed8"/>
    <text x="137" y="202" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">Çizgiye çok yakın ve sıkı</text>

    <rect x="252" y="62" width="195" height="155" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="350" y="84" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#b45309">ORTA İLİŞKİ (0,30 ≤ |r| &lt; 0,70)</text>
    <line x1="282" y1="180" x2="417" y2="105" stroke="#fcd34d" stroke-width="2"/>
    <circle cx="290" cy="165" r="4" fill="#d97706"/>
    <circle cx="312" cy="175" r="4" fill="#d97706"/>
    <circle cx="335" cy="138" r="4" fill="#d97706"/>
    <circle cx="360" cy="155" r="4" fill="#d97706"/>
    <circle cx="382" cy="115" r="4" fill="#d97706"/>
    <circle cx="406" cy="128" r="4" fill="#d97706"/>
    <text x="350" y="202" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">Çizgiden kısmen uzaklaşmış</text>

    <rect x="465" y="62" width="195" height="155" rx="10" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
    <text x="562" y="84" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#be185d">ZAYIF İLİŞKİ (0 &lt; |r| &lt; 0,30)</text>
    <line x1="495" y1="180" x2="630" y2="105" stroke="#f9a8d4" stroke-width="2"/>
    <circle cx="500" cy="145" r="4" fill="#db2777"/>
    <circle cx="525" cy="182" r="4" fill="#db2777"/>
    <circle cx="548" cy="112" r="4" fill="#db2777"/>
    <circle cx="572" cy="168" r="4" fill="#db2777"/>
    <circle cx="595" cy="105" r="4" fill="#db2777"/>
    <circle cx="620" cy="142" r="4" fill="#db2777"/>
    <text x="562" y="202" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#9d174d">Çizgiden uzak ve seyrek</text>
    """
    return svg(700, 250, ic, "İlişkinin Gücü ve Eğilim Çizgisi")


def gorsel_3():
    ic = """
    <rect x="20" y="15" width="660" height="220" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">KORELASYON KATSAYISI (r) SAYI DOĞRUSU CETVELİ (-1 ≤ r ≤ 1)</text>
    <rect x="50" y="85" width="90" height="45" fill="#dc2626"/>
    <rect x="140" y="85" width="120" height="45" fill="#f87171"/>
    <rect x="260" y="85" width="90" height="45" fill="#fca5a5"/>
    <rect x="350" y="85" width="90" height="45" fill="#86efac"/>
    <rect x="440" y="85" width="120" height="45" fill="#4ade80"/>
    <rect x="560" y="85" width="90" height="45" fill="#16a34a"/>

    <text x="95" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#ffffff">Güçlü (-)</text>
    <text x="200" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#ffffff">Orta (-)</text>
    <text x="305" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#7f1d1d">Zayıf (-)</text>
    <text x="395" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#14532d">Zayıf (+)</text>
    <text x="500" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#14532d">Orta (+)</text>
    <text x="605" y="112" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="700" fill="#ffffff">Güçlü (+)</text>

    <text x="50" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#991b1b">-1</text>
    <text x="140" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#991b1b">-0,70</text>
    <text x="260" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#991b1b">-0,30</text>
    <text x="350" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1e293b">0</text>
    <text x="440" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#166534">0,30</text>
    <text x="560" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#166534">0,70</text>
    <text x="650" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#166534">+1</text>

    <text x="65" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#b91c1c">Negatif Mükemmel</text>
    <text x="350" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#475569">İlişki Yok</text>
    <text x="635" y="175" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#15803d">Pozitif Mükemmel</text>
    <text x="350" y="205" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#334155">Not: |r| değeri 1'e yaklaştıkça doğrusal ilişki güçlenir, 0'a yaklaştıkça zayıflar.</text>
    """
    return svg(700, 245, ic, "Korelasyon Katsayısı (r) Cetveli")


def gorsel_4():
    ic = """
    <rect x="20" y="15" width="660" height="220" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">KORELASYON ≠ NEDENSELLİK (GİZLİ DEĞİŞKEN ETKİSİ)</text>
    <rect x="235" y="58" width="230" height="54" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
    <text x="350" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#b45309">GİZLİ (KARIŞTIRICI) DEĞİŞKEN</text>
    <text x="350" y="99" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#92400e">Ekonomik Refah / Açık Hava Süresi</text>

    <path d="M 275 112 L 175 145" stroke="#d97706" stroke-width="2"/>
    <path d="M 425 112 L 525 145" stroke="#d97706" stroke-width="2"/>

    <rect x="55" y="148" width="210" height="62" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="160" y="172" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">1. NİCEL DEĞİŞKEN (X)</text>
    <text x="160" y="193" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">Güneşli Gün Sayısı</text>

    <rect x="435" y="148" width="210" height="62" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="540" y="172" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#15803d">2. NİCEL DEĞİŞKEN (Y)</text>
    <text x="540" y="193" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">Mutluluk Endeksi Oranı</text>

    <line x1="270" y1="179" x2="430" y2="179" stroke="#ef4444" stroke-width="2" stroke-dasharray="5,4"/>
    <text x="350" y="171" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#dc2626">Gözlenen Korelasyon</text>
    <text x="350" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#991b1b">(Doğrudan Neden-Sonuç Değildir!)</text>
    """
    return svg(700, 245, ic, "Korelasyon ve Gizli Değişken İlişkisi")


def uygula(v):
    v["bolumler"][1]["gorsel"] = gorsel_1()
    v["bolumler"][2]["gorsel"] = gorsel_2()
    v["bolumler"][4]["gorsel"] = gorsel_3()
    v["bolumler"][5]["gorsel"] = gorsel_4()
