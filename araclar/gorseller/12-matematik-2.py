from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#1e3a8a"/>
    <text x="360" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Üstel Fonksiyonun Tersi Olarak Logaritma: y = logₐ x ⇔ x = aʸ</text>

    <rect x="30" y="78" width="290" height="190" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="175" y="106" text-anchor="middle" font-size="15" font-weight="bold" fill="#1d4ed8">Üstel Fonksiyon (f)</text>
    <text x="175" y="135" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">f : ℝ → ℝ⁺ ,  y = aˣ</text>
    <text x="175" y="165" text-anchor="middle" font-size="12" fill="#1e3a8a">• a &gt; 0 ve a ≠ 1</text>
    <text x="175" y="188" text-anchor="middle" font-size="12" fill="#1e3a8a">• Bire bir ve örten</text>
    <text x="175" y="218" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">Örnek: 2⁵ = 32</text>
    <text x="175" y="242" text-anchor="middle" font-size="12" fill="#1e3a8a">(Taban = 2 , Üs = 5)</text>

    <text x="360" y="175" text-anchor="middle" font-size="24" font-weight="bold" fill="#0f766e">⇄</text>

    <rect x="400" y="78" width="290" height="190" rx="12" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
    <text x="545" y="106" text-anchor="middle" font-size="15" font-weight="bold" fill="#15803d">Logaritma Fonksiyonu (f⁻¹)</text>
    <text x="545" y="135" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534">f⁻¹ : ℝ⁺ → ℝ ,  y = logₐ x</text>
    <text x="545" y="165" text-anchor="middle" font-size="12" fill="#14532d">• Tanım kümesi: ℝ⁺ (x &gt; 0)</text>
    <text x="545" y="188" text-anchor="middle" font-size="12" fill="#14532d">• Görüntü kümesi: ℝ</text>
    <text x="545" y="218" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803d">Örnek: log₂ 32 = 5</text>
    <text x="545" y="242" text-anchor="middle" font-size="12" fill="#14532d">(Taban daima tabanda kalır!)</text>
    """
    return svg(720, 285, ic, "Üstel Fonksiyon ve Logaritma Fonksiyonu İlişkisi")


def gorsel_2():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#4c1d95"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Üstel ve Logaritmik Fonksiyonların Tersini (f⁻¹) Bulma Adımları</text>

    <rect x="30" y="75" width="315" height="195" rx="12" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>
    <text x="187" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">Örnek 1: Üstel Fonksiyonun Tersi</text>
    <text x="48" y="130" font-size="13" font-weight="bold" fill="#6d28d9">f(x) = 2 · 5ˣ⁻³ - 1  ⇒  f⁻¹(x) = ?</text>
    <text x="48" y="158" font-size="12" fill="#4c1d95">1. y = 2 · 5ˣ⁻³ - 1 yazılır.</text>
    <text x="48" y="182" font-size="12" fill="#4c1d95">2. (y + 1) / 2 = 5ˣ⁻³ (Üstel terim yalnız kalır)</text>
    <text x="48" y="206" font-size="12" fill="#4c1d95">3. x - 3 = log₅((y + 1) / 2)</text>
    <text x="48" y="230" font-size="12" fill="#4c1d95">4. x = log₅((y + 1) / 2) + 3</text>
    <text x="48" y="254" font-size="13" font-weight="bold" fill="#5b21b6">Sonuç: f⁻¹(x) = log₅((x + 1) / 2) + 3</text>

    <rect x="375" y="75" width="315" height="195" rx="12" fill="#fdf2f8" stroke="#ec4899" stroke-width="2"/>
    <text x="532" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9d174d">Örnek 2: Logaritmik Fonksiyonun Tersi</text>
    <text x="393" y="130" font-size="13" font-weight="bold" fill="#be185d">f(x) = log₄(x - 3) + 1  ⇒  f⁻¹(x) = ?</text>
    <text x="393" y="158" font-size="12" fill="#831843">1. y = log₄(x - 3) + 1 yazılır.</text>
    <text x="393" y="182" font-size="12" fill="#831843">2. y - 1 = log₄(x - 3) (Logaritma yalnız kalır)</text>
    <text x="393" y="206" font-size="12" fill="#831843">3. x - 3 = 4ʸ⁻¹ (Üstel dönüşüm yapılır)</text>
    <text x="393" y="230" font-size="12" fill="#831843">4. x = 4ʸ⁻¹ + 3</text>
    <text x="393" y="254" font-size="13" font-weight="bold" fill="#9d174d">Sonuç: f⁻¹(x) = 4ˣ⁻¹ + 3</text>
    """
    return svg(720, 285, ic, "Üstel ve Logaritmik Fonksiyonların Tersini Bulma")


def gorsel_3():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#991b1b"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">f(x) = log_{g(x)} h(x) Fonksiyonunun En Geniş Tanım Kümesi Şartları</text>

    <rect x="25" y="75" width="210" height="105" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="130" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">I. İç Kısım Şartı</text>
    <text x="130" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="#dc2626">h(x) &gt; 0</text>
    <text x="130" y="155" text-anchor="middle" font-size="11" fill="#7f1d1d">Logaritması alınan ifade</text>
    <text x="130" y="170" text-anchor="middle" font-size="11" fill="#7f1d1d">kesinlikle pozitif olmalıdır.</text>

    <rect x="255" y="75" width="210" height="105" rx="10" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="360" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">II. Taban Pozitifliği</text>
    <text x="360" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="#ea580c">g(x) &gt; 0</text>
    <text x="360" y="155" text-anchor="middle" font-size="11" fill="#7c2d12">Logaritma tabanı sıfır</text>
    <text x="360" y="170" text-anchor="middle" font-size="11" fill="#7c2d12">veya negatif olamaz.</text>

    <rect x="485" y="75" width="210" height="105" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="590" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">III. Taban ≠ 1 Şartı</text>
    <text x="590" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="#059669">g(x) ≠ 1</text>
    <text x="590" y="155" text-anchor="middle" font-size="11" fill="#064e3b">Taban 1 olursa üstel</text>
    <text x="590" y="170" text-anchor="middle" font-size="11" fill="#064e3b">fonksiyon bire bir olmaz.</text>

    <rect x="25" y="195" width="670" height="75" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="360" y="220" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8">Örnek Uygulama: f(x) = log_{x-1}(9 - x) En Geniş Tanım Kümesi</text>
    <text x="360" y="242" text-anchor="middle" font-size="12" fill="#1e3a8a">1) 9 - x &gt; 0 ⇒ x &lt; 9   |   2) x - 1 &gt; 0 ⇒ x &gt; 1   |   3) x - 1 ≠ 1 ⇒ x ≠ 2</text>
    <text x="360" y="260" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">Çözüm Kümesi: ÇK = (1, 9) - {2}</text>
    """
    return svg(720, 285, ic, "Logaritma Fonksiyonunun En Geniş Tanım Kümesi")


def gorsel_4():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#0f766e"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Logaritma Fonksiyonunun Grafiği ve y = x Doğrusuna Göre Simetri</text>

    <rect x="30" y="75" width="315" height="200" rx="12" fill="#f0fdfa" stroke="#14b8a6" stroke-width="2"/>
    <text x="187" y="98" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f766e">a &gt; 1 İçin Artan (y = 2ˣ ve y = log₂ x)</text>
    <line x1="60" y1="220" x2="310" y2="220" stroke="#64748b" stroke-width="1.5"/>
    <line x1="120" y1="255" x2="120" y2="110" stroke="#64748b" stroke-width="1.5"/>
    <line x1="80" y1="240" x2="290" y2="115" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,5"/>
    <path d="M 85 212 Q 120 190 175 115" fill="none" stroke="#2563eb" stroke-width="2.5"/>
    <path d="M 128 250 Q 150 220 285 165" fill="none" stroke="#059669" stroke-width="2.5"/>
    <circle cx="120" cy="190" r="3.5" fill="#2563eb"/>
    <circle cx="155" cy="220" r="3.5" fill="#059669"/>
    <text x="95" y="188" font-size="10" font-weight="bold" fill="#1d4ed8">(0,1)</text>
    <text x="150" y="236" font-size="10" font-weight="bold" fill="#047857">(1,0)</text>
    <text x="195" y="128" font-size="11" font-weight="bold" fill="#1d4ed8">y = 2ˣ</text>
    <text x="255" y="160" font-size="11" font-weight="bold" fill="#047857">y = log₂ x</text>
    <text x="275" y="112" font-size="10" fill="#475569">y = x</text>

    <rect x="375" y="75" width="315" height="200" rx="12" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
    <text x="532" y="98" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309">0 &lt; a &lt; 1 İçin Azalan (y = log_{1/2} x)</text>
    <line x1="405" y1="190" x2="655" y2="190" stroke="#64748b" stroke-width="1.5"/>
    <line x1="465" y1="255" x2="465" y2="110" stroke="#64748b" stroke-width="1.5"/>
    <path d="M 475 115 Q 500 190 635 245" fill="none" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="515" cy="190" r="3.5" fill="#d97706"/>
    <text x="515" y="180" font-size="10" font-weight="bold" fill="#b45309">(1,0)</text>
    <text x="595" y="225" font-size="11" font-weight="bold" fill="#b45309">y = log_{1/2} x</text>
    <text x="532" y="262" text-anchor="middle" font-size="11" fill="#78350f">x büyüdükçe y değerleri küçülür (Azalan)</text>
    """
    return svg(720, 290, ic, "Artan ve Azalan Logaritma Fonksiyonu Grafikleri")


def gorsel_5():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#7c2d12"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">10 Tabanında (Adi) Logaritma, pH Ölçeği ve Logaritma Tarihi</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#fff7ed" stroke="#f97316" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#9a3412">10 Tabanında Logaritma (log x)</text>
    <text x="45" y="128" font-size="13" font-weight="bold" fill="#c2410c">log₁₀ x = log x = y  ⇔  x = 10ʸ</text>
    <text x="45" y="152" font-size="12" fill="#7c2d12">• log 10 = 1   |   • log 1000 = log(10³) = 3</text>
    <text x="45" y="174" font-size="12" fill="#7c2d12">• log(0,0001) = log(10⁻⁴) = -4</text>
    <rect x="42" y="190" width="286" height="65" rx="8" fill="#ffedd5"/>
    <text x="185" y="210" text-anchor="middle" font-size="12" font-weight="bold" fill="#9a3412">Kimyada pH Ölçeği: pH = -log[H⁺]</text>
    <text x="185" y="228" text-anchor="middle" font-size="11" fill="#7c2d12">0 ← Asidik (pH &lt; 7) | Nötr (7) | Bazik (pH &gt; 7) → 14</text>
    <text x="185" y="245" text-anchor="middle" font-size="11" fill="#7c2d12">Richter Deprem Enerjisi: E = 10^(11,8 + 1,5M)</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">Bilim Tarihinde Öncü İsimler</text>
    <text x="392" y="130" font-size="12" font-weight="bold" fill="#b91c1c">1. John Napier (1550 - 1617)</text>
    <text x="392" y="148" font-size="11" fill="#7f1d1d">• "Logaritma" terimini ve cetvellerini</text>
    <text x="392" y="164" font-size="11" fill="#7f1d1d">büyük hesapları kolaylaştırmak için icat etti.</text>
    <text x="392" y="192" font-size="12" font-weight="bold" fill="#b91c1c">2. Gelenbevî İsmail Efendi (1726 - 1790)</text>
    <text x="392" y="210" font-size="11" fill="#7f1d1d">• Osmanlı'da logaritma risalesi yazdı.</text>
    <text x="392" y="228" font-size="11" fill="#7f1d1d">• Kâğıthane'de III. Selim huzurunda</text>
    <text x="392" y="244" font-size="11" fill="#7f1d1d">humbaracıların top atış açılarını düzeltti.</text>
    """
    return svg(720, 285, ic, "10 Tabanında Logaritma ve Tarihçesi")


def gorsel_6():
    ic = """
    <rect x="20" y="16" width="680" height="44" rx="10" fill="#312e81"/>
    <text x="360" y="44" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffffff">Euler Sayısı (e ≈ 2,71828...) ve Doğal Logaritma Fonksiyonu (ln x)</text>

    <rect x="25" y="75" width="320" height="195" rx="12" fill="#eef2ff" stroke="#6366f1" stroke-width="2"/>
    <text x="185" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#312e81">Euler Sayısı (e) Nedir?</text>
    <text x="45" y="128" font-size="12" font-weight="bold" fill="#4338ca">• (1 + 1/n)ⁿ  (n → ∞ iken yakınsadığı limit)</text>
    <text x="45" y="150" font-size="12" font-weight="bold" fill="#4338ca">• e = 1/0! + 1/1! + 1/2! + 1/3! + ... ≈ 2,71828</text>
    <text x="45" y="176" font-size="11" fill="#3730a3">• Jakob Bernoulli bileşik faizde keşfetti;</text>
    <text x="45" y="194" font-size="11" fill="#3730a3">Leonhard Euler "e" adını verip irrasyonelliğini</text>
    <text x="45" y="212" font-size="11" fill="#3730a3">ispatladı.</text>
    <text x="45" y="238" font-size="12" font-weight="bold" fill="#312e81">• 2 &lt; e &lt; 3  ⇒  y = eˣ grafiği 2ˣ ile 3ˣ arasındadır.</text>

    <rect x="375" y="75" width="320" height="195" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
    <text x="535" y="102" text-anchor="middle" font-size="14" font-weight="bold" fill="#065f46">Doğal Logaritma (f(x) = logₑ x = ln x)</text>
    <text x="395" y="130" font-size="13" font-weight="bold" fill="#047857">ln x = y  ⇔  x = eʸ  (x &gt; 0)</text>
    <text x="395" y="156" font-size="12" fill="#064e3b">• ln 1 = 0        • ln e = 1</text>
    <text x="395" y="180" font-size="12" fill="#064e3b">• ln(e³) = 3      • ln(1 / e²) = ln(e⁻²) = -2</text>
    <text x="395" y="204" font-size="12" fill="#064e3b">• Tabanı e &gt; 1 olduğundan artan fonksiyondur.</text>
    <text x="395" y="228" font-size="12" fill="#064e3b">• Grafiği y = eˣ üstel fonksiyonunun</text>
    <text x="395" y="248" text-anchor="middle" font-size="12" font-weight="bold" fill="#065f46">y = x doğrusuna göre simetriğidir.</text>
    """
    return svg(720, 285, ic, "Euler Sayısı ve Doğal Logaritma Fonksiyonu")


def uygula(v):
    gorseller = [gorsel_1(), gorsel_2(), gorsel_3(), gorsel_4(), gorsel_5(), gorsel_6()]
    for i, g in enumerate(gorseller):
        if i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g