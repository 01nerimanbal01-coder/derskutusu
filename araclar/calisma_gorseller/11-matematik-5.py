# -*- coding: utf-8 -*-
"""11-matematik-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Dörtgen Açılar ve Temel Şema
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="m1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8EAF6"/><stop offset="100%" stop-color="#C5CAE9"/>
    </linearGradient>
  </defs>
  <!-- Dörtgen Çizimi -->
  <polygon points="50,95 180,105 210,35 90,20" fill="url(#m1)" stroke="#3949AB" stroke-width="1.2"/>
  <circle cx="50" cy="95" r="3" fill="#1A237E"/><text x="40" y="105" font-family="Noto Sans" font-size="8" fill="#1A237E">A</text>
  <circle cx="180" cy="105" r="3" fill="#1A237E"/><text x="185" y="115" font-family="Noto Sans" font-size="8" fill="#1A237E">B</text>
  <circle cx="210" cy="35" r="3" fill="#1A237E"/><text x="215" y="30" font-family="Noto Sans" font-size="8" fill="#1A237E">C</text>
  <circle cx="90" cy="20" r="3" fill="#1A237E"/><text x="80" y="18" font-family="Noto Sans" font-size="8" fill="#1A237E">D</text>

  <!-- Sağ Bilgi Paneli -->
  <rect x="235" y="15" width="115" height="95" rx="6" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="292" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#283593" text-anchor="middle">Açı Özellikleri</text>
  <text x="292" y="55" font-family="Noto Sans" font-size="8" fill="#3949AB" text-anchor="middle">İç Açılar = 360°</text>
  <text x="292" y="70" font-family="Noto Sans" font-size="8" fill="#3949AB" text-anchor="middle">Dış Açılar = 360°</text>
  <text x="292" y="88" font-family="Noto Sans" font-size="7" fill="#1A237E" text-anchor="middle">n = 4 Kenarlı Çokgen</text>
</svg>'''

    # S2 (indeks 1): Dik Köşegenli Dörtgen Teoremi
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Dörtgen -->
  <polygon points="60,65 140,110 210,65 140,15" fill="#E1F5FE" stroke="#0288D1" stroke-width="1"/>
  <!-- Köşegenler -->
  <line x1="60" y1="65" x2="210" y2="65" stroke="#D32F2F" stroke-width="1.2"/>
  <line x1="140" y1="15" x2="140" y2="110" stroke="#D32F2F" stroke-width="1.2"/>
  <!-- Diklik Sembolü -->
  <rect x="140" y="55" width="10" height="10" fill="none" stroke="#D32F2F" stroke-width="0.75"/>
  <circle cx="145" cy="60" r="1.5" fill="#D32F2F"/>

  <!-- Kenar Etiketleri -->
  <text x="90" y="95" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B">a = 5</text>
  <text x="180" y="95" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B">b = 7</text>
  <text x="180" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B">c = 8</text>
  <text x="90" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B">d = x (?)</text>

  <!-- Sağ Panel: Teorem -->
  <rect x="235" y="20" width="115" height="85" rx="5" fill="#FFF9C4" stroke="#FFF176" stroke-width="0.75"/>
  <text x="292" y="38" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#F57F17" text-anchor="middle">Dik Köşegen Bağıntısı</text>
  <text x="292" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">a² + c² = b² + d²</text>
  <text x="292" y="75" font-family="Noto Sans" font-size="8" fill="#BF360C" text-anchor="middle">a = 5, b = 7, c = 8</text>
  <text x="292" y="92" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#BF360C" text-anchor="middle">d = x = ? cm</text>
</svg>'''

    # S3 (indeks 2): Varignon Paralelkenarı Şeması
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Dış Dörtgen -->
  <polygon points="40,95 190,110 220,25 70,15" fill="#FAFAFA" stroke="#9E9E9E" stroke-width="0.75"/>
  <!-- Kenar Orta Noktaları -->
  <!-- K(115, 102.5), L(205, 67.5), M(145, 20), N(55, 55) -->
  <polygon points="115,102 205,68 145,20 55,55" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.2"/>
  <circle cx="115" cy="102" r="2.5" fill="#1B5E20"/><text x="115" y="115" font-family="Noto Sans" font-size="7" fill="#1B5E20">K</text>
  <circle cx="205" cy="68" r="2.5" fill="#1B5E20"/><text x="215" y="72" font-family="Noto Sans" font-size="7" fill="#1B5E20">L</text>
  <circle cx="145" cy="20" r="2.5" fill="#1B5E20"/><text x="145" y="12" font-family="Noto Sans" font-size="7" fill="#1B5E20">M</text>
  <circle cx="55" cy="55" r="2.5" fill="#1B5E20"/><text x="45" y="58" font-family="Noto Sans" font-size="7" fill="#1B5E20">N</text>

  <!-- Sağ Panel -->
  <rect x="235" y="15" width="115" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="292" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Varignon Teoremi</text>
  <text x="292" y="52" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">KLMN daima paralelkenardır.</text>
  <text x="292" y="68" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Çevre = e + f</text>
  <text x="292" y="85" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#2E7D32" text-anchor="middle">Alan = Alan(ABCD) / 2</text>
</svg>'''

    # S4 (indeks 3): Komşu İç Açıortaylar Bağıntısı
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Dörtgen Çizgileri -->
  <polygon points="50,105 180,105 200,30 90,20" fill="#F3E5F5" stroke="#8E24AA" stroke-width="0.75"/>
  <!-- Açıortaylar -->
  <line x1="50" y1="105" x2="120" y2="70" stroke="#D32F2F" stroke-width="1.2"/>
  <line x1="180" y1="105" x2="120" y2="70" stroke="#D32F2F" stroke-width="1.2"/>
  <circle cx="120" cy="70" r="3" fill="#D32F2F"/>
  <text x="120" y="62" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#C62828" text-anchor="middle">α</text>

  <!-- Sağ Panel: Formül -->
  <rect x="220" y="25" width="130" height="75" rx="5" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="285" y="45" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#4A148C" text-anchor="middle">Komşu Açıortay Açısı</text>
  <text x="285" y="68" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#6A1B9A" text-anchor="middle">α = (m(C) + m(D)) / 2</text>
  <text x="285" y="88" font-family="Noto Sans" font-size="7" fill="#7B1FA2" text-anchor="middle">Kalan iki açının yarısı</text>
</svg>'''

    # S6 (indeks 5): Dörtgen Çeşitleri Hiyerarşisi
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="15" y="15" width="75" height="95" rx="5" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.75"/>
  <text x="52" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1" text-anchor="middle">Yamuk</text>
  <text x="52" y="55" font-family="Noto Sans" font-size="7" fill="#1565C0" text-anchor="middle">1 çift paralel</text>
  <text x="52" y="70" font-family="Noto Sans" font-size="7" fill="#1565C0" text-anchor="middle">Alt-Üst taban</text>

  <rect x="100" y="15" width="75" height="95" rx="5" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="137" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Paralelkenar</text>
  <text x="137" y="55" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">2 çift paralel</text>
  <text x="137" y="70" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Köşegen ortalar</text>

  <rect x="185" y="15" width="75" height="95" rx="5" fill="#FFF3E0" stroke="#FFCC80" stroke-width="0.75"/>
  <text x="222" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#E65100" text-anchor="middle">Eşkenar Dört.</text>
  <text x="222" y="55" font-family="Noto Sans" font-size="7" fill="#EF6C00" text-anchor="middle">Tüm kenar eşit</text>
  <text x="222" y="70" font-family="Noto Sans" font-size="7" fill="#EF6C00" text-anchor="middle">Köşegen diktir</text>

  <rect x="270" y="15" width="75" height="95" rx="5" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.75"/>
  <text x="307" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#4A148C" text-anchor="middle">Kare</text>
  <text x="307" y="55" font-family="Noto Sans" font-size="7" fill="#6A1B9A" text-anchor="middle">Açı = 90°</text>
  <text x="307" y="70" font-family="Noto Sans" font-size="7" fill="#6A1B9A" text-anchor="middle">Köşegen eşit &amp; dik</text>
</svg>'''

    # S7 (indeks 6): Dik Köşegenle Alan Hesabı
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <polygon points="50,65 130,110 200,65 130,15" fill="#FFFDE7" stroke="#FFF59D" stroke-width="1"/>
  <line x1="50" y1="65" x2="200" y2="65" stroke="#1565C0" stroke-width="1.5"/>
  <line x1="130" y1="15" x2="130" y2="110" stroke="#1565C0" stroke-width="1.5"/>
  <text x="100" y="60" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1">e = 12 cm</text>
  <text x="135" y="40" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1">f = 16 cm</text>

  <!-- Sağ Panel: Alan -->
  <rect x="225" y="25" width="120" height="75" rx="5" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="285" y="45" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B" text-anchor="middle">Alan Formülü (Dik Köşegen)</text>
  <text x="285" y="65" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0277BD" text-anchor="middle">Alan = (e · f) / 2</text>
  <text x="285" y="85" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">= (12 · 16) / 2 = 96 cm²</text>
</svg>'''

    # S9 (indeks 8): Karşılıklı İç Açıortaylar Bağıntısı
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#37474F" text-anchor="middle">Karşılıklı Açıortayların Kesişimi</text>
  <rect x="50" y="48" width="260" height="45" rx="4" fill="#EFEBE9" stroke="#D7CCC8" stroke-width="0.75"/>
  <text x="180" y="70" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#4E342E" text-anchor="middle">α = |m(B) - m(D)| / 2</text>
  <text x="180" y="85" font-family="Noto Sans" font-size="7" fill="#5D4037" text-anchor="middle">A ve C köşelerinden çizilen açıortaylar arasındaki dar açı</text>
</svg>'''

    # S11 (indeks 10): Deltoid Simetri Ekseni
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <polygon points="80,62 140,110 240,62 140,15" fill="#E8F5E9" stroke="#4CAF50" stroke-width="1"/>
  <!-- Simetri Ekseni (Köşegen) -->
  <line x1="80" y1="62" x2="240" y2="62" stroke="#2E7D32" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="140" y1="15" x2="140" y2="110" stroke="#388E3C" stroke-width="1"/>

  <text x="160" y="75" font-family="Noto Sans" font-size="8" fill="#1B5E20">Simetri Ekseni</text>
  <text x="290" y="55" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#2E7D32">Deltoid Özelliği:</text>
  <text x="290" y="70" font-family="Noto Sans" font-size="7" fill="#388E3C">Köşegenler diktir,</text>
  <text x="290" y="82" font-family="Noto Sans" font-size="7" fill="#388E3C">biri diğerini ortalar.</text>
</svg>'''
