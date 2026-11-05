# -*- coding: utf-8 -*-
"""11-fizik-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Newton Yasaları Özeti
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="fi1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#BBDEFB"/>
    </linearGradient>
    <linearGradient id="fi2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
    <linearGradient id="fi3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="95" height="95" rx="6" fill="url(#fi1)" stroke="#64B5F6" stroke-width="0.75"/>
  <text x="62" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0D47A1" text-anchor="middle">1. Eylemsizlik</text>
  <text x="62" y="60" font-family="Noto Sans" font-size="8" fill="#1565C0" text-anchor="middle">F_net = 0</text>
  <text x="62" y="75" font-family="Noto Sans" font-size="8" fill="#1976D2" text-anchor="middle">v = 0 veya</text>
  <text x="62" y="90" font-family="Noto Sans" font-size="8" fill="#0D47A1" text-anchor="middle">sabit hızlı</text>

  <rect x="132" y="15" width="95" height="95" rx="6" fill="url(#fi2)" stroke="#81C784" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">2. Temel Yasa</text>
  <text x="180" y="60" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">F_net = m · a</text>
  <text x="180" y="75" font-family="Noto Sans" font-size="8" fill="#388E3C" text-anchor="middle">a = F / m</text>
  <text x="180" y="90" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">İvmeli hareket</text>

  <rect x="250" y="15" width="95" height="95" rx="6" fill="url(#fi3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="297" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">3. Etki - Tepki</text>
  <text x="297" y="60" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">F₁₂ = -F₂₁</text>
  <text x="297" y="75" font-family="Noto Sans" font-size="8" fill="#F57C00" text-anchor="middle">Zıt yönlü</text>
  <text x="297" y="90" font-family="Noto Sans" font-size="8" fill="#E65100" text-anchor="middle">Farklı cisimlerde</text>
</svg>'''

    # S2 (indeks 1): Yatay Düzlemde İvme Deneyi
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Zemin Çizgisi -->
  <line x1="30" y1="95" x2="330" y2="95" stroke="#757575" stroke-width="1.2"/>
  <line x1="30" y1="98" x2="330" y2="98" stroke="#BDBDBD" stroke-width="0.5"/>

  <!-- Blok -->
  <rect x="120" y="45" width="70" height="50" rx="4" fill="#BBDEFB" stroke="#1976D2" stroke-width="0.75"/>
  <text x="155" y="74" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#0D47A1" text-anchor="middle">m = 4 kg</text>

  <!-- Uygulanan Kuvvet -->
  <path d="M 190 70 L 250 70" stroke="#D32F2F" stroke-width="2"/>
  <polygon points="250,66 258,70 250,74" fill="#D32F2F"/>
  <text x="225" y="62" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#C62828">F = 24 N</text>

  <!-- İvme Oku -->
  <path d="M 130 30 L 180 30" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="3,2"/>
  <polygon points="180,27 186,30 180,33" fill="#2E7D32"/>
  <text x="155" y="24" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">a = ? (6 m/s²)</text>
</svg>'''

    # S3 (indeks 2): Serbest Cisim Diyagramı (SCD)
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Blok Noktası / Kütle -->
  <rect x="150" y="45" width="60" height="35" rx="3" fill="#E0E0E0" stroke="#757575" stroke-width="0.75"/>
  <circle cx="180" cy="62" r="3" fill="#212121"/>

  <!-- N (Normal Kuvvet - Yukarı) -->
  <path d="M 180 62 L 180 18" stroke="#1976D2" stroke-width="1.5"/>
  <polygon points="177,18 180,12 183,18" fill="#1976D2"/>
  <text x="190" y="24" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0D47A1">N (Tepki)</text>

  <!-- G (Ağırlık - Aşağı) -->
  <path d="M 180 62 L 180 106" stroke="#D32F2F" stroke-width="1.5"/>
  <polygon points="177,106 180,112 183,106" fill="#D32F2F"/>
  <text x="190" y="105" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C">G = m·g</text>

  <!-- Yan Bilgi Paneli -->
  <rect x="250" y="25" width="95" height="75" rx="5" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="297" y="45" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#37474F" text-anchor="middle">SCD Kuralı:</text>
  <text x="297" y="60" font-family="Noto Sans" font-size="7" fill="#546E7A" text-anchor="middle">Yalnızca kitaba</text>
  <text x="297" y="72" font-family="Noto Sans" font-size="7" fill="#546E7A" text-anchor="middle">etki eden</text>
  <text x="297" y="85" font-family="Noto Sans" font-size="7" fill="#546E7A" text-anchor="middle">kuvvetler çizilir</text>
</svg>'''

    # S4 (indeks 3): Statik ve Kinetik Sürtünme Grafiği
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Eksenler -->
  <line x1="50" y1="105" x2="310" y2="105" stroke="#424242" stroke-width="1.2"/>
  <line x1="50" y1="105" x2="50" y2="20" stroke="#424242" stroke-width="1.2"/>
  <text x="325" y="108" font-family="Noto Sans" font-size="8" fill="#424242">F_uygulanan</text>
  <text x="45" y="16" font-family="Noto Sans" font-size="8" fill="#424242" text-anchor="end">F_s</text>

  <!-- Sürtünme Eğrisi -->
  <line x1="50" y1="105" x2="160" y2="40" stroke="#D32F2F" stroke-width="1.5"/>
  <line x1="160" y1="40" x2="175" y2="55" stroke="#D32F2F" stroke-width="1.5"/>
  <line x1="175" y1="55" x2="300" y2="55" stroke="#1976D2" stroke-width="1.5"/>

  <text x="110" y="60" font-family="Noto Sans" font-size="8" fill="#C62828">Statik Bölge</text>
  <text x="230" y="48" font-family="Noto Sans" font-size="8" fill="#0D47A1">Kinetik Bölge (Sabit f_k)</text>
  <circle cx="160" cy="40" r="3" fill="#D32F2F"/>
  <text x="160" y="32" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">f_s (maks)</text>
</svg>'''

    # S6 (indeks 5): Eğik Düzlem Bileşenleri
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Üçgen Eğik Düzlem -->
  <polygon points="40,105 240,105 240,30" fill="#ECEFF1" stroke="#90A4AE" stroke-width="0.75"/>
  <text x="80" y="100" font-family="Noto Sans" font-size="8" fill="#37474F">θ = 30°</text>

  <!-- Blok -->
  <polygon points="120,68 145,55 160,75 135,88" fill="#FFE082" stroke="#FFA000" stroke-width="0.75"/>

  <!-- Kaydıran Kuvvet Oku -->
  <path d="M 140 72 L 95 95" stroke="#D32F2F" stroke-width="1.5"/>
  <text x="85" y="80" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#C62828">m·g·sinθ</text>

  <!-- Dik Bileşen -->
  <path d="M 140 72 L 165 105" stroke="#1976D2" stroke-width="1.2"/>
  <text x="175" y="105" font-family="Noto Sans" font-size="8" fill="#1565C0">m·g·cosθ</text>
</svg>'''

    # S7 (indeks 6): Bağlı Kütleler ve İp Gerilmesi
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Zemin -->
  <line x1="30" y1="95" x2="330" y2="95" stroke="#9E9E9E" stroke-width="1"/>

  <!-- m1 Bloğu -->
  <rect x="60" y="55" width="45" height="40" rx="3" fill="#C8E6C9" stroke="#388E3C" stroke-width="0.75"/>
  <text x="82" y="78" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">m₁</text>

  <!-- İp T -->
  <line x1="105" y1="75" x2="165" y2="75" stroke="#424242" stroke-width="2"/>
  <text x="135" y="68" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#212121" text-anchor="middle">T</text>

  <!-- m2 Bloğu -->
  <rect x="165" y="50" width="55" height="45" rx="3" fill="#BBDEFB" stroke="#1976D2" stroke-width="0.75"/>
  <text x="192" y="76" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0D47A1" text-anchor="middle">m₂</text>

  <!-- Çeken F Kuvveti -->
  <path d="M 220 72 L 275 72" stroke="#D32F2F" stroke-width="2"/>
  <polygon points="275,68 283,72 275,76" fill="#D32F2F"/>
  <text x="250" y="64" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#C62828">F</text>
</svg>'''

    # S9 (indeks 8): Asansör ve Görünür Ağırlık
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Asansör Kabini -->
  <rect x="110" y="15" width="140" height="95" rx="5" fill="#FAFAFA" stroke="#757575" stroke-width="1"/>
  <!-- İp ve Kütle -->
  <line x1="180" y1="15" x2="180" y2="45" stroke="#424242" stroke-width="1.5"/>
  <circle cx="180" cy="55" r="10" fill="#FFCDD2" stroke="#D32F2F" stroke-width="0.75"/>
  <text x="180" y="58" font-family="Noto Sans" font-size="7" font-weight="bold" fill="#B71C1C" text-anchor="middle">m</text>

  <!-- İvme Oku (Yukarı) -->
  <path d="M 80 80 L 80 40" stroke="#2E7D32" stroke-width="2"/>
  <polygon points="76,40 80,32 84,40" fill="#2E7D32"/>
  <text x="65" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20">a (↑)</text>

  <!-- Sonuç Formülü -->
  <rect x="260" y="30" width="85" height="65" rx="4" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="302" y="50" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">İp Gerilmesi:</text>
  <text x="302" y="68" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">T = m(g + a)</text>
  <text x="302" y="82" font-family="Noto Sans" font-size="7" fill="#388E3C" text-anchor="middle">Ağırlık artar</text>
</svg>'''

    # S11 (indeks 10): Sürtünme Bağıntısı ve Normal Kuvvet
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#37474F" text-anchor="middle">Kinetik Sürtünme Bağıntısı</text>
  <rect x="65" y="48" width="230" height="45" rx="5" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="180" y="70" font-family="Noto Sans" font-size="12" font-weight="bold" fill="#0277BD" text-anchor="middle">f_k = k · N</text>
  <text x="180" y="85" font-family="Noto Sans" font-size="8" fill="#01579B" text-anchor="middle">k: Kinetik sürtünme katsayısı  |  N: Yüzeyin dik tepki kuvveti</text>
</svg>'''
