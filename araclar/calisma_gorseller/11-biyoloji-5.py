# -*- coding: utf-8 -*-
"""11-biyoloji-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Hormonlar Şeması
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
    <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#BBDEFB"/>
    </linearGradient>
    <linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
    <linearGradient id="g4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE4EC"/><stop offset="100%" stop-color="#F8BBD0"/>
    </linearGradient>
  </defs>
  <rect x="5" y="10" width="80" height="105" rx="6" fill="url(#g1)" stroke="#81C784" stroke-width="0.75"/>
  <text x="45" y="32" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#1B5E20" text-anchor="middle">Oksin</text>
  <text x="45" y="55" font-family="Noto Sans" font-size="9" fill="#2E7D32" text-anchor="middle">Tepe Meristemi</text>
  <text x="45" y="75" font-family="Noto Sans" font-size="9" fill="#388E3C" text-anchor="middle">Hücre Uzaması</text>
  <text x="45" y="95" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">Apikal Baskınlık</text>

  <rect x="95" y="10" width="80" height="105" rx="6" fill="url(#g2)" stroke="#64B5F6" stroke-width="0.75"/>
  <text x="135" y="32" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#0D47A1" text-anchor="middle">Sitokinin</text>
  <text x="135" y="55" font-family="Noto Sans" font-size="9" fill="#1565C0" text-anchor="middle">Kök Uçları</text>
  <text x="135" y="75" font-family="Noto Sans" font-size="9" fill="#1976D2" text-anchor="middle">Hücre Bölünmesi</text>
  <text x="135" y="95" font-family="Noto Sans" font-size="8" fill="#0D47A1" text-anchor="middle">Ksilemle Taşınım</text>

  <rect x="185" y="10" width="80" height="105" rx="6" fill="url(#g3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="225" y="32" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#E65100" text-anchor="middle">Giberellin</text>
  <text x="225" y="55" font-family="Noto Sans" font-size="9" fill="#EF6C00" text-anchor="middle">Genç Yaprak / Embriyo</text>
  <text x="225" y="75" font-family="Noto Sans" font-size="9" fill="#F57C00" text-anchor="middle">Tohum Çimlenmesi</text>
  <text x="225" y="95" font-family="Noto Sans" font-size="8" fill="#E65100" text-anchor="middle">Gövde Uzaması</text>

  <rect x="275" y="10" width="80" height="105" rx="6" fill="url(#g4)" stroke="#F06292" stroke-width="0.75"/>
  <text x="315" y="32" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#880E4F" text-anchor="middle">ABA / Etilen</text>
  <text x="315" y="55" font-family="Noto Sans" font-size="9" fill="#AD1457" text-anchor="middle">Stres &amp; Olgunlaşma</text>
  <text x="315" y="75" font-family="Noto Sans" font-size="9" fill="#C2185B" text-anchor="middle">Stoma Kapanması</text>
  <text x="315" y="95" font-family="Noto Sans" font-size="8" fill="#880E4F" text-anchor="middle">Gaz Halde Etki</text>
</svg>'''

    # S2 (indeks 1): Koleoptil Fototropizma Deneyi
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="kol1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C8E6C9"/><stop offset="100%" stop-color="#A5D6A7"/>
    </linearGradient>
  </defs>
  <!-- Işık kaynağı oku -->
  <path d="M 20 62 L 60 62" stroke="#F57F17" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="15" cy="62" r="8" fill="#FFF59D" stroke="#FBC02D" stroke-width="0.75"/>
  <text x="15" y="85" font-family="Noto Sans" font-size="9" fill="#F57F17" text-anchor="middle">Işık</text>

  <!-- Düz Koleoptil -->
  <rect x="100" y="30" width="28" height="75" rx="5" fill="url(#kol1)" stroke="#4CAF50" stroke-width="0.75"/>
  <path d="M 100 45 Q 114 20 128 45 Z" fill="#81C784" stroke="#388E3C" stroke-width="0.75"/>
  <text x="114" y="118" font-family="Noto Sans" font-size="9" fill="#2E7D32" text-anchor="middle">Kontrol (Düz)</text>

  <!-- Işığa Yönelen Koleoptil -->
  <path d="M 190 105 C 190 70, 170 50, 150 40 C 158 35, 175 42, 218 105 Z" fill="url(#kol1)" stroke="#388E3C" stroke-width="0.75"/>
  <text x="195" y="118" font-family="Noto Sans" font-size="9" fill="#1B5E20" text-anchor="middle">Işığa Yönelim</text>

  <!-- Oksin Dağılımı Kutusu -->
  <rect x="250" y="20" width="100" height="85" rx="6" fill="#F1F8E9" stroke="#AED581" stroke-width="0.75"/>
  <text x="300" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#33691E" text-anchor="middle">Oksin Göçü</text>
  <circle cx="270" cy="55" r="3" fill="#689F38"/>
  <circle cx="280" cy="60" r="3" fill="#689F38"/>
  <circle cx="290" cy="55" r="3" fill="#689F38"/>
  <circle cx="310" cy="70" r="4" fill="#33691E"/>
  <circle cx="325" cy="75" r="4" fill="#33691E"/>
  <text x="300" y="95" font-family="Noto Sans" font-size="8" fill="#558B2F" text-anchor="middle">Gölgede yoğunlaşır</text>
</svg>'''

    # S3 (indeks 2): Doku Kültürü Kallus ve Farklılaşma
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="tup" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ECEFF1"/><stop offset="100%" stop-color="#CFD8DC"/>
    </linearGradient>
  </defs>
  <!-- Tüp 1: Kallus -->
  <rect x="35" y="20" width="40" height="75" rx="8" fill="url(#tup)" stroke="#90A4AE" stroke-width="0.75"/>
  <circle cx="55" cy="70" r="12" fill="#FFE082" stroke="#FFB300" stroke-width="0.75"/>
  <text x="55" y="110" font-family="Noto Sans" font-size="9" fill="#37474F" text-anchor="middle">Kallus (Denge)</text>

  <!-- Ok 1 -->
  <path d="M 85 57 L 115 57" stroke="#78909C" stroke-width="1.2" stroke-dasharray="3,2"/>

  <!-- Tüp 2: Sürgün Oluşumu (Sitokinin > Oksin) -->
  <rect x="130" y="20" width="40" height="75" rx="8" fill="url(#tup)" stroke="#90A4AE" stroke-width="0.75"/>
  <circle cx="150" cy="75" r="10" fill="#FFE082" stroke="#FFB300" stroke-width="0.75"/>
  <path d="M 150 65 Q 140 45 135 35 Q 150 48 150 65 Q 155 45 165 32 Q 155 50 150 65" fill="#81C784"/>
  <text x="150" y="110" font-family="Noto Sans" font-size="9" fill="#1B5E20" text-anchor="middle">Sitokinin &gt; Oksin</text>
  <text x="150" y="120" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">(Sürgün)</text>

  <!-- Ok 2 -->
  <path d="M 180 57 L 210 57" stroke="#78909C" stroke-width="1.2" stroke-dasharray="3,2"/>

  <!-- Tüp 3: Kök Oluşumu (Oksin > Sitokinin) -->
  <rect x="225" y="20" width="40" height="75" rx="8" fill="url(#tup)" stroke="#90A4AE" stroke-width="0.75"/>
  <circle cx="245" cy="55" r="10" fill="#FFE082" stroke="#FFB300" stroke-width="0.75"/>
  <path d="M 245 65 L 240 85 M 245 65 L 250 88 M 245 65 L 245 90" stroke="#8D6E63" stroke-width="1.5"/>
  <text x="245" y="110" font-family="Noto Sans" font-size="9" fill="#4E342E" text-anchor="middle">Oksin &gt; Sitokinin</text>
  <text x="245" y="120" font-family="Noto Sans" font-size="8" fill="#5D4037" text-anchor="middle">(Kök)</text>

  <!-- Bilgi Paneli -->
  <rect x="285" y="25" width="65" height="70" rx="5" fill="#E8EAF6" stroke="#C5CAE9" stroke-width="0.75"/>
  <text x="317" y="45" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1A237E" text-anchor="middle">Organogenes</text>
  <text x="317" y="62" font-family="Noto Sans" font-size="7" fill="#283593" text-anchor="middle">Hormon oranı</text>
  <text x="317" y="75" font-family="Noto Sans" font-size="7" fill="#3949AB" text-anchor="middle">farklılaşmayı</text>
  <text x="317" y="88" font-family="Noto Sans" font-size="7" fill="#303F9F" text-anchor="middle">belirler</text>
</svg>'''

    # S4 (indeks 3): Dormansi ve Çimlenme Karşılaştırması
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="seed1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D7CCC8"/><stop offset="100%" stop-color="#A1887F"/>
    </linearGradient>
  </defs>
  <!-- Sol Kutu: Dormansi -->
  <rect x="20" y="15" width="145" height="95" rx="6" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="0.75"/>
  <ellipse cx="65" cy="55" rx="20" ry="14" fill="url(#seed1)" stroke="#6D4C41" stroke-width="0.75"/>
  <text x="115" y="42" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#4E342E">DORMANSİ</text>
  <text x="115" y="60" font-family="Noto Sans" font-size="8" fill="#5D4037">Yüksek ABA</text>
  <text x="115" y="75" font-family="Noto Sans" font-size="8" fill="#6D4C41">Düşük Su / Uyku</text>
  <text x="115" y="90" font-family="Noto Sans" font-size="7" fill="#8D6E63">Metabolizma yavaş</text>

  <!-- Sağ Kutu: Çimlenme -->
  <rect x="195" y="15" width="145" height="95" rx="6" fill="#F1F8E9" stroke="#C5E1A5" stroke-width="0.75"/>
  <ellipse cx="235" cy="60" rx="18" ry="13" fill="url(#seed1)" stroke="#6D4C41" stroke-width="0.75"/>
  <path d="M 235 50 Q 240 30 250 25 Q 245 40 235 50" fill="#66BB6A" stroke="#2E7D32" stroke-width="0.75"/>
  <text x="285" y="42" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#1B5E20">ÇİMLENME</text>
  <text x="285" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32">Yüksek Giberellin</text>
  <text x="285" y="75" font-family="Noto Sans" font-size="8" fill="#388E3C">Amilaz Sentezi</text>
  <text x="285" y="90" font-family="Noto Sans" font-size="7" fill="#4CAF50">Besin hidrolizi</text>
</svg>'''

    # S6 (indeks 5): Kuraklık Stresi ve Stoma Mekanizması
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Açık Stoma -->
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <ellipse cx="70" cy="55" rx="12" ry="24" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.75"/>
  <ellipse cx="90" cy="55" rx="12" ry="24" fill="#C8E6C9" stroke="#2E7D32" stroke-width="0.75"/>
  <ellipse cx="80" cy="55" rx="4" ry="16" fill="#1B5E20"/>
  <text x="80" y="100" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Açık Stoma (Normal Su)</text>

  <!-- Ok -->
  <path d="M 175 62 L 195 62" stroke="#455A64" stroke-width="1.2"/>
  <text x="185" y="52" font-family="Noto Sans" font-size="8" fill="#D84315" text-anchor="middle">+ ABA</text>

  <!-- Kapalı Stoma -->
  <rect x="205" y="15" width="130" height="95" rx="6" fill="#FFF3E0" stroke="#FFCC80" stroke-width="0.75"/>
  <ellipse cx="260" cy="55" rx="13" ry="24" fill="#FFE0B2" stroke="#E65100" stroke-width="0.75"/>
  <ellipse cx="272" cy="55" rx="13" ry="24" fill="#FFE0B2" stroke="#E65100" stroke-width="0.75"/>
  <line x1="266" y1="35" x2="266" y2="75" stroke="#BF360C" stroke-width="1.5"/>
  <text x="270" y="100" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#BF360C" text-anchor="middle">Kapalı Stoma (Kuraklık)</text>
</svg>'''

    # S7 (indeks 6): Apikal Baskınlık (Oksin Sentezi)
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Durum A: Uç Tomurcuk Sağlam -->
  <rect x="25" y="12" width="140" height="100" rx="6" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <line x1="85" y1="100" x2="85" y2="25" stroke="#5D4037" stroke-width="3"/>
  <circle cx="85" cy="24" r="6" fill="#4CAF50" stroke="#2E7D32" stroke-width="0.75"/>
  <!-- Uyuyan yan tomurcuklar -->
  <ellipse cx="78" cy="60" rx="3" ry="2" fill="#81C784"/>
  <ellipse cx="92" cy="75" rx="3" ry="2" fill="#81C784"/>
  <text x="85" y="118" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Tepe tomurcuğu var (Baskı)</text>

  <!-- Durum B: Uç Tomurcuk Kesilmiş -->
  <rect x="195" y="12" width="140" height="100" rx="6" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <line x1="255" y1="100" x2="255" y2="40" stroke="#5D4037" stroke-width="3"/>
  <line x1="251" y1="38" x2="259" y2="38" stroke="#D32F2F" stroke-width="1.5"/>
  <!-- Gelişen yan dallar -->
  <path d="M 255 60 Q 235 50 225 45" stroke="#388E3C" stroke-width="2" fill="none"/>
  <path d="M 255 75 Q 275 65 285 58" stroke="#388E3C" stroke-width="2" fill="none"/>
  <text x="255" y="118" font-family="Noto Sans" font-size="8" fill="#1565C0" text-anchor="middle">Uç kesildi (Yan dallar gelişir)</text>
</svg>'''

    # S9 (indeks 8): Meyve Olgunlaşması ve Etilen Salgısı
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <radialGradient id="appleG" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#C8E6C9"/><stop offset="100%" stop-color="#4CAF50"/>
    </radialGradient>
    <radialGradient id="appleR" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#FFCDD2"/><stop offset="100%" stop-color="#E53935"/>
    </radialGradient>
  </defs>
  <!-- Ham Meyve -->
  <circle cx="80" cy="58" r="28" fill="url(#appleG)" stroke="#388E3C" stroke-width="0.75"/>
  <rect x="78" y="24" width="4" height="10" rx="2" fill="#5D4037"/>
  <text x="80" y="105" font-family="Noto Sans" font-size="9" fill="#2E7D32" text-anchor="middle">Ham Meyve (Sert / Nişasta)</text>

  <!-- Etilen Gazı Dalgası -->
  <path d="M 125 50 Q 150 40 175 50 Q 150 60 125 50" fill="#FFF9C4" stroke="#FBC02D" stroke-width="0.75"/>
  <text x="150" y="42" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#F57F17" text-anchor="middle">C₂H₄ (Etilen Gazı)</text>
  <path d="M 135 68 L 165 68" stroke="#F57F17" stroke-width="1.2"/>

  <!-- Olgun Meyve -->
  <circle cx="230" cy="58" r="28" fill="url(#appleR)" stroke="#C62828" stroke-width="0.75"/>
  <rect x="228" y="24" width="4" height="10" rx="2" fill="#5D4037"/>
  <text x="230" y="105" font-family="Noto Sans" font-size="9" fill="#B71C1C" text-anchor="middle">Olgun Meyve (Tatlı / Yumuşak)</text>

  <!-- Bilgi Paneli -->
  <rect x="280" y="20" width="70" height="78" rx="5" fill="#FFFDE7" stroke="#FFF59D" stroke-width="0.75"/>
  <text x="315" y="38" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#F57F17" text-anchor="middle">Otomatik</text>
  <text x="315" y="52" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Katalizleme:</text>
  <text x="315" y="66" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">Etilen üretimi</text>
  <text x="315" y="80" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">hızla yayılır</text>
</svg>'''

    # S11 (indeks 10): Fitohormon İletim Yolları
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <!-- Ksilem Yolu (Mavi) -->
  <rect x="55" y="30" width="105" height="45" rx="5" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="107" y="48" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0277BD" text-anchor="middle">Ksilem Borusu</text>
  <text x="107" y="64" font-family="Noto Sans" font-size="8" fill="#01579B" text-anchor="middle">Kökten yukarı: Sitokinin</text>

  <!-- Floem / Parankima Yolu (Yeşil) -->
  <rect x="195" y="30" width="115" height="45" rx="5" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="252" y="48" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">Parankima &amp; Floem</text>
  <text x="252" y="64" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">Kutupsal iletim: Oksin</text>

  <text x="180" y="98" font-family="Noto Sans" font-size="8" fill="#616161" text-anchor="middle">Hormonlar özelleşmiş iletim hatlarıyla hedef dokulara ulaştırılır.</text>
</svg>'''
