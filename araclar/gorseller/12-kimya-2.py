from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Redoks Denkleştirme 1: Yükseltgenme Basamağı Değişim Yöntemi</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="185" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">5 Adımda Denkleştirme (H₂S + HNO₃)</text>
    <text x="42" y="124" font-size="11" fill="#1e3a8a">1. Değerlikleri bul: S²⁻ → S⁰ ve N⁵⁺ → N²⁺</text>
    <text x="42" y="144" font-size="11" fill="#1e3a8a">2. Alınan/verilen e⁻: S (2e⁻ verir), N (3e⁻ alır)</text>
    <text x="42" y="164" font-size="11" fill="#1e3a8a">3. Elektronları eşitle: S × 3  ve  N × 2  (6e⁻)</text>
    <text x="42" y="184" font-size="11" fill="#1e3a8a">4. Katsayıları yaz: 3H₂S + 2HNO₃ → 3S + 2NO + H₂O</text>
    <text x="42" y="204" font-size="11" fill="#1e3a8a">5. H ve O atomlarını eşitle (H₂O katsayısı = 4):</text>
    <rect x="38" y="218" width="294" height="38" rx="8" fill="#dbeafe"/>
    <text x="185" y="242" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">3H₂S + 2HNO₃ → 3S + 2NO + 4H₂O</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="535" y="100" text-anchor="middle" font-size="13" font-weight="bold" fill="#9d174d">Birden Fazla Yükseltgenen Tür: As₂S₃</text>
    <text x="392" y="126" font-size="11" fill="#831843">• As₂³⁺S₃²⁻ + HNO₃ + H₂O → H₃As⁵⁺O₄ + S⁰ + N²⁺O</text>
    <text x="392" y="148" font-size="11" font-weight="bold" fill="#be185d">• 2 As atomu (+3 → +5): 2 × 2 = 4e⁻ verir</text>
    <text x="392" y="168" font-size="11" font-weight="bold" fill="#be185d">• 3 S atomu (−2 → 0): 3 × 2 = 6e⁻ verir</text>
    <text x="392" y="188" font-size="11" fill="#831843">⇒ 1 mol As₂S₃ toplam 10e⁻ verir; HNO₃ ise 3e⁻ alır.</text>
    <text x="392" y="208" font-size="11" fill="#831843">⇒ Katsayılar 3 ve 10 ile çarpılır (30e⁻):</text>
    <rect x="388" y="218" width="294" height="38" rx="8" fill="#fce7f3"/>
    <text x="535" y="242" text-anchor="middle" font-size="11" font-weight="bold" fill="#9d174d">3As₂S₃ + 10HNO₃ + 4H₂O → 6H₃AsO₄ + 9S + 10NO</text>
    """
    return svg(720, 285, ic, "Yükseltgenme Basamağı Değişim Yöntemi ile Redoks Denkleştirme")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Redoks Denkleştirme 2: Yarı Tepkime (Yarı Reaksiyon) Yöntemi</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">Örnek 1: KClO₃ + SO₂ + H₂O → KCl + H₂SO₄</text>
    <text x="42" y="128" font-size="11" fill="#4c1d95">1. Yükseltgenme: SO₂ → H₂SO₄ + 2e⁻   (× 3)</text>
    <text x="42" y="148" font-size="11" fill="#4c1d95">   İndirgenme: KClO₃ + 6e⁻ → KCl    (× 1)</text>
    <text x="42" y="172" font-size="11" fill="#4c1d95">2. Elektronlar (6e⁻) eşitlenip toplanır:</text>
    <text x="42" y="192" font-size="11" fill="#4c1d95">   3SO₂ + KClO₃ → 3H₂SO₄ + KCl</text>
    <text x="42" y="212" font-size="11" fill="#4c1d95">3. H ve O denkliği için 3H₂O eklenir:</text>
    <rect x="38" y="222" width="294" height="34" rx="8" fill="#ede9fe"/>
    <text x="185" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">3SO₂ + KClO₃ + 3H₂O → 3H₂SO₄ + KCl</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="13" font-weight="bold" fill="#065f46">Örnek 2: P + HNO₃ + H₂O → H₃PO₄ + NO</text>
    <text x="392" y="128" font-size="11" fill="#064e3b">1. Yükseltgenme: P⁰ → H₃P⁵⁺O₄ + 5e⁻   (× 3)</text>
    <text x="392" y="148" font-size="11" fill="#064e3b">   İndirgenme: HN⁵⁺O₃ + 3e⁻ → N²⁺O   (× 5)</text>
    <text x="392" y="172" font-size="11" fill="#064e3b">2. Elektronlar (15e⁻) eşitlenip toplanır:</text>
    <text x="392" y="192" font-size="11" fill="#064e3b">   3P + 5HNO₃ → 3H₃PO₄ + 5NO</text>
    <text x="392" y="212" font-size="11" fill="#064e3b">3. H ve O denkliği için 2H₂O eklenir:</text>
    <rect x="388" y="222" width="294" height="34" rx="8" fill="#d1fae5"/>
    <text x="535" y="244" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">3P + 5HNO₃ + 2H₂O → 3H₃PO₄ + 5NO</text>
    """
    return svg(720, 285, ic, "Yarı Tepkime Yöntemi ile Redoks Denkleştirme")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Redoks Tepkimeleri ve Elektrik Enerjisi: Doğrudan ve Dolaylı Temas</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">1. Doğrudan Temas (Aynı Kapta)</text>
    <text x="42" y="128" font-size="12" fill="#134e4a">• CuSO₄ çözeltisine Zn çubuk batırıldığında:</text>
    <text x="42" y="148" font-size="11" fill="#134e4a">  Zn(k) + Cu²⁺(suda) → Zn²⁺(suda) + Cu(k)</text>
    <text x="42" y="170" font-size="11" fill="#134e4a">• Zn üzerinde kızılımsı kahverengi Cu toplanır,</text>
    <text x="42" y="188" font-size="11" fill="#134e4a">  çözeltinin mavi rengi zamanla kaybolur.</text>
    <text x="42" y="212" font-size="11" font-weight="bold" fill="#0f766e">• Elektron alışverişi doğrudan temasla olur;</text>
    <text x="42" y="230" font-size="11" font-weight="bold" fill="#b91c1c">  kullanılabilir elektrik akımı elde edilmez!</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">2. Dolaylı Temas (Daniell Pili ve İstemlilik)</text>
    <text x="392" y="126" font-size="11" fill="#78350f">• John Frederic Daniell: Zn/ZnSO₄ ve Cu/CuSO₄</text>
    <text x="392" y="144" font-size="11" fill="#78350f">  yarı hücrelerini tel ve tuz köprüsüyle bağladı.</text>
    <text x="392" y="168" font-size="12" font-weight="bold" fill="#15803d">• İstemli Redoks (Galvanik Hücre / Pil):</text>
    <text x="392" y="186" font-size="11" fill="#14532d">  Kendiliğinden gerçekleşir (H₂ + ½O₂ → H₂O).</text>
    <text x="392" y="204" font-size="11" font-weight="bold" fill="#15803d">  Kimyasal Enerji → Elektrik Enerjisi</text>
    <text x="392" y="228" font-size="12" font-weight="bold" fill="#b91c1c">• İstemsiz Redoks (Elektroliz):</text>
    <text x="392" y="246" font-size="11" fill="#7f1d1d">  Dış etkiyle gerçekleşir (H₂O → H₂ + ½O₂).</text>
    <text x="392" y="262" font-size="11" font-weight="bold" fill="#b91c1c">  Elektrik Enerjisi → Kimyasal Enerji</text>
    """
    return svg(720, 285, ic, "Doğrudan ve Dolaylı Elektron Alışverişi ile İstemlilik")


def gorsel_4():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#7c2d12"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Galvanik Hücre (Elektrokimyasal Pil) Yapısı ve Temel Kavramlar</text>

    <rect x="30" y="75" width="210" height="195" rx="12" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="135" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">ANOT Yarı Hücresi (−)</text>
    <text x="45" y="126" font-size="12" font-weight="bold" fill="#b91c1c">• Yükseltgenme gerçekleşir:</text>
    <text x="45" y="146" font-size="11" fill="#7f1d1d">  Cu(k) → Cu²⁺(suda) + 2e⁻</text>
    <text x="45" y="170" font-size="11" fill="#7f1d1d">• Elektron kaynağı olduğu için</text>
    <text x="45" y="186" font-size="11" font-weight="bold" fill=\"#991b1b\">  &quot;−&quot; kutup olarak gösterilir.</text>
    <text x="45" y="210" font-size="11" fill="#7f1d1d">• Elektrot kütlesi zamanla azalır.</text>
    <text x="45" y="230" font-size="11" fill="#7f1d1d">• Çözeltide katyon (Cu²⁺) artar.</text>
    <text x="45" y="250" font-size="11" font-weight="bold" fill="#991b1b">• Tuz köprüsünden anyon gelir.</text>

    <rect x="255" y="75" width="210" height="195" rx="12" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
    <text x="360" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Dış Devre ve Tuz Köprüsü</text>
    <rect x="275" y="114" width="170" height="36" rx="8" fill="#dbeafe"/>
    <text x="360" y="136" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">e⁻ akışı: Anot → Katot</text>
    <text x="360" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">Tuz Köprüsü (KNO₃ / KCl):</text>
    <text x="360" y="188" text-anchor="middle" font-size="11" fill="#475569">• Yük denkliğini korur.</text>
    <text x="360" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">• Anyonlar (NO₃⁻) → Anoda</text>
    <text x="360" y="228" text-anchor="middle" font-size="11" font-weight="bold" fill="#15803d">• Katyonlar (K⁺) → Katoda</text>
    <text x="360" y="252" text-anchor="middle" font-size="11" fill="#334155">• İnert elektrot: Pt, Au, Grafit</text>

    <rect x="480" y="75" width="210" height="195" rx="12" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="585" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#15803d">KATOT Yarı Hücresi (+)</text>
    <text x="495" y="126" font-size="12" font-weight="bold" fill="#166534">• İndirgenme gerçekleşir:</text>
    <text x="495" y="146" font-size="11" fill="#14532d">  Ag⁺(suda) + e⁻ → Ag(k)</text>
    <text x="495" y="170" font-size="11" fill="#14532d">• Elektronların gittiği kutup</text>
    <text x="495" y="186" font-size="11" font-weight="bold" fill=\"#15803d\">  olup &quot;+&quot; işaretiyle gösterilir.</text>
    <text x="495" y="210" font-size="11" fill="#14532d">• Elektrot kütlesi zamanla artar.</text>
    <text x="495" y="230" font-size="11" fill="#14532d">• Çözeltide katyon (Ag⁺) azalır.</text>
    <text x="495" y="250" font-size="11" font-weight="bold" fill="#15803d">• Tuz köprüsünden katyon gelir.</text>
    """
    return svg(720, 285, ic, "Galvanik Hücrede Anot, Katot ve Tuz Köprüsü İşleyişi")


def gorsel_5():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#065f46"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Cu / Ag ve Zn / Cu Galvanik Hücrelerinde Zamanla Meydana Gelen Değişimler</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">1. Cu - Ag Elektrokimyasal Pili</text>
    <text x="42" y="128" font-size="12" font-weight="bold" fill="#047857">• Anot (−): Cu(k) → Cu²⁺(suda) + 2e⁻</text>
    <text x="42" y="148" font-size="12" font-weight="bold" fill="#047857">• Katot (+): 2Ag⁺(suda) + 2e⁻ → 2Ag(k)</text>
    <text x="42" y="174" font-size="11" fill="#064e3b">• Cu elektrot kütlesi azalır, [Cu²⁺] derişimi artar.</text>
    <text x="42" y="194" font-size="11" fill="#064e3b">• Ag elektrot kütlesi artar, [Ag⁺] derişimi azalır.</text>
    <text x="42" y="214" font-size="11" fill="#064e3b">• KNO₃ tuz köprüsünde NO₃⁻ iyonları Cu kabına,</text>
    <text x="42" y="232" font-size="11" fill="#064e3b">  K⁺ iyonları Ag kabına göç eder.</text>
    <text x="42" y="254" font-size="11" font-weight="bold" fill="#065f46">• Pil potansiyeli zamanla azalır (Başlangıç: 0,460 V).</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">2. Zn - Cu Elektrokimyasal Pili (Daniell)</text>
    <text x="392" y="128" font-size="12" font-weight="bold" fill="#1e40af">• Anot (−): Zn(k) → Zn²⁺(suda) + 2e⁻</text>
    <text x="392" y="148" font-size="12" font-weight="bold" fill="#1e40af">• Katot (+): Cu²⁺(suda) + 2e⁻ → Cu(k)</text>
    <text x="392" y="174" font-size="11" fill="#1e3a8a">• Zn elektrot aşınır (kütlesi azalır), [Zn²⁺] artar.</text>
    <text x="392" y="194" font-size="11" fill="#1e3a8a">• Cu elektrot üzerinde Cu birikir (kütlesi artar),</text>
    <text x="392" y="212" font-size="11" fill="#1e3a8a">  çözeltideki [Cu²⁺] derişimi azalır.</text>
    <text x="392" y="234" font-size="11" fill="#1e3a8a">• KCl tuz köprüsünde Cl⁻ iyonları Zn yarı hücresine,</text>
    <text x="392" y="252" font-size="11" font-weight="bold" fill="#1d4ed8">  K⁺ iyonları Cu yarı hücresine geçer.</text>
    """
    return svg(720, 285, ic, "Cu-Ag ve Zn-Cu Pillerinde Zamanla Meydana Gelen Değişimler")


def gorsel_6():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Standart Pil Potansiyeli (E°pil) ve Standart Hidrojen Elektrot (SHE)</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#312e81">Standart Koşullar ve E°pil</text>
    <text x="42" y="128" font-size="12" fill="#3730a3">• Sıcaklık: 25 °C   |   Basınç: 1 atm</text>
    <text x="42" y="150" font-size="12" fill="#3730a3">• Çözelti iyon derişimi: 1 M (1 mol/L)</text>
    <rect x="42" y="166" width="286" height="40" rx="8" fill="#e0e7ff"/>
    <text x="185" y="191" text-anchor="middle" font-size="14" font-weight="bold" fill="#312e81">E°pil = E°yükseltgenme + E°indirgenme</text>
    <text x="42" y="228" font-size="11" fill="#3730a3">• Pil potansiyeli derişime, sıcaklığa ve</text>
    <text x="42" y="246" font-size="11" fill="#3730a3">  gaz elektrot varsa gaz basıncına bağlıdır.</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">Referans: Standart Hidrojen Elektrot (SHE)</text>
    <text x="392" y="126" font-size="11" fill="#7c2d12">• 1 M H⁺ asit çözeltisine daldırılmış inert</text>
    <text x="392" y="144" font-size="11" fill="#7c2d12">  Pt elektrot ve 1 atm H₂(g) (25 °C) içerir.</text>
    <text x="392" y="168" font-size="12" font-weight="bold" fill="#c2410c">• Deniz seviyesinin 0 m kabul edilmesi gibi</text>
    <text x="392" y="186" font-size="12" font-weight="bold" fill="#c2410c">  SHE potansiyeli E° = 0,00 V kabul edilir:</text>
    <text x="392" y="212" font-size="11" fill="#7c2d12">• Anot ise: H₂(g) → 2H⁺(suda) + 2e⁻ (E° = 0,00 V)</text>
    <text x="392" y="232" font-size="11" fill="#7c2d12">• Katot ise: 2H⁺(suda) + 2e⁻ → H₂(g) (E° = 0,00 V)</text>
    <text x="392" y="254" font-size="11" font-weight="bold" fill="#9a3412">• Zn-SHE pilinde E°pil = 0,763 V (Zn anot, Pt katot)</text>
    """
    return svg(720, 285, ic, "Standart Pil Potansiyeli ve Standart Hidrojen Elektrot")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
