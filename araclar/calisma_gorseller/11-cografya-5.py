# -*- coding: utf-8 -*-
"""11-cografya-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Göl Oluşum Tipleri
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="c1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E1F5FE"/><stop offset="100%" stop-color="#B3E5FC"/>
    </linearGradient>
    <linearGradient id="c2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8EAF6"/><stop offset="100%" stop-color="#C5CAE9"/>
    </linearGradient>
    <linearGradient id="c3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
    <linearGradient id="c4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0F2F1"/><stop offset="100%" stop-color="#B2DFDB"/>
    </linearGradient>
  </defs>
  <rect x="5" y="10" width="80" height="105" rx="6" fill="url(#c1)" stroke="#4FC3F7" stroke-width="0.75"/>
  <text x="45" y="32" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#01579B" text-anchor="middle">Tektonik</text>
  <path d="M 15 50 L 35 60 L 55 50 L 75 60" stroke="#0288D1" stroke-width="1.2" fill="none"/>
  <text x="45" y="78" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Fay Çöküntüsü</text>
  <text x="45" y="94" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">Tuz Gölü / Van</text>

  <rect x="95" y="10" width="80" height="105" rx="6" fill="url(#c2)" stroke="#7986CB" stroke-width="0.75"/>
  <text x="135" y="32" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#1A237E" text-anchor="middle">Karstik</text>
  <circle cx="135" cy="55" r="14" fill="#9FA8DA" stroke="#3949AB" stroke-width="0.75"/>
  <text x="135" y="78" font-family="Noto Sans" font-size="8" fill="#283593" text-anchor="middle">Eriyen Kayaç</text>
  <text x="135" y="94" font-family="Noto Sans" font-size="7" fill="#1A237E" text-anchor="middle">Obruk / Polye</text>

  <rect x="185" y="10" width="80" height="105" rx="6" fill="url(#c3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="225" y="32" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">Volkanik</text>
  <path d="M 205 65 L 225 45 L 245 65 Z" fill="#FFCC80" stroke="#E65100" stroke-width="0.75"/>
  <text x="225" y="78" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Krater / Kaldera</text>
  <text x="225" y="94" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Nemrut / Meke</text>

  <rect x="275" y="10" width="80" height="105" rx="6" fill="url(#c4)" stroke="#4DB6AC" stroke-width="0.75"/>
  <text x="315" y="32" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#004D40" text-anchor="middle">Set Gölleri</text>
  <rect x="290" y="50" width="50" height="15" rx="3" fill="#80CBC4" stroke="#00796B" stroke-width="0.75"/>
  <text x="315" y="78" font-family="Noto Sans" font-size="8" fill="#00695C" text-anchor="middle">Vadi Tıkanması</text>
  <text x="315" y="94" font-family="Noto Sans" font-size="7" fill="#004D40" text-anchor="middle">Kıyı / Heyelan</text>
</svg>'''

    # S2 (indeks 1): CBS Katman Entegrasyonu
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Katman 3: Arazi Örtüsü (Üst) -->
  <polygon points="50,25 190,15 220,35 80,45" fill="#C8E6C9" stroke="#388E3C" stroke-width="0.75"/>
  <text x="240" y="32" font-family="Noto Sans" font-size="8" fill="#2E7D32">Katman 3: Arazi Örtüsü</text>

  <!-- Katman 2: Hidrografi (Orta) -->
  <polygon points="50,55 190,45 220,65 80,75" fill="#BBDEFB" stroke="#1976D2" stroke-width="0.75"/>
  <text x="240" y="62" font-family="Noto Sans" font-size="8" fill="#1565C0">Katman 2: Akarsu &amp; Göller</text>

  <!-- Katman 1: Yükseklik/Topoğrafya (Alt) -->
  <polygon points="50,85 190,75 220,95 80,105" fill="#FFE0B2" stroke="#F57C00" stroke-width="0.75"/>
  <text x="240" y="92" font-family="Noto Sans" font-size="8" fill="#E65100">Katman 1: Eğim &amp; Sayısal Yükseklik</text>

  <!-- Dikey Birleşim Oku -->
  <line x1="135" y1="20" x2="135" y2="105" stroke="#455A64" stroke-width="1.2" stroke-dasharray="3,2"/>
  <circle cx="135" cy="115" r="4" fill="#37474F"/>
  <text x="135" y="122" font-family="Noto Sans" font-size="7" fill="#263238" text-anchor="middle">CBS Entegrasyonu</text>
</svg>'''

    # S3 (indeks 2): Açık Havza (Gideğenli) vs Kapalı Havza
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Sol: Açık Havza (Tatlı Su) -->
  <rect x="20" y="15" width="150" height="95" rx="6" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <ellipse cx="80" cy="55" rx="35" ry="20" fill="#4FC3F7" stroke="#0288D1" stroke-width="0.75"/>
  <text x="80" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">Tatlı Su Gölü</text>
  <!-- Gideğen Çıkış Oku -->
  <path d="M 115 55 Q 140 50 155 60" stroke="#01579B" stroke-width="2" fill="none"/>
  <text x="140" y="45" font-family="Noto Sans" font-size="7" font-weight="bold" fill="#01579B">Gideğen</text>
  <text x="95" y="98" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Açık Havza (Boşalım var)</text>

  <!-- Sağ: Kapalı Havza (Tuzlu/Acı Su) -->
  <rect x="190" y="15" width="150" height="95" rx="6" fill="#FFF3E0" stroke="#FFCC80" stroke-width="0.75"/>
  <ellipse cx="265" cy="55" rx="35" ry="20" fill="#FFB74D" stroke="#E65100" stroke-width="0.75"/>
  <text x="265" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#BF360C" text-anchor="middle">Tuzlu / Sodalı</text>
  <line x1="300" y1="48" x2="315" y2="62" stroke="#D32F2F" stroke-width="2"/>
  <line x1="300" y1="62" x2="315" y2="48" stroke="#D32F2F" stroke-width="2"/>
  <text x="265" y="98" font-family="Noto Sans" font-size="8" fill="#D84315" text-anchor="middle">Kapalı Havza (Gideğen yok)</text>
</svg>'''

    # S4 (indeks 3): Hidrolojik Döngü Şeması
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Okyanus Zemin -->
  <path d="M 10 100 Q 50 90 90 100 Q 130 110 170 100 L 170 120 L 10 120 Z" fill="#81D4FA"/>
  <text x="60" y="112" font-family="Noto Sans" font-size="8" fill="#01579B">Okyanus</text>

  <!-- Buharlaşma Oku -->
  <path d="M 60 85 L 60 55" stroke="#0288D1" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="75" y="70" font-family="Noto Sans" font-size="7" fill="#0277BD">Buharlaşma</text>

  <!-- Bulut / Yoğuşma -->
  <ellipse cx="140" cy="35" rx="25" ry="12" fill="#ECEFF1" stroke="#B0BEC5" stroke-width="0.75"/>
  <text x="140" y="38" font-family="Noto Sans" font-size="7" fill="#37474F" text-anchor="middle">Yoğuşma</text>

  <!-- Yağış Oku -->
  <path d="M 210 45 L 210 75" stroke="#1976D2" stroke-width="1.5"/>
  <text x="225" y="60" font-family="Noto Sans" font-size="7" fill="#1565C0">Yağış</text>

  <!-- Kara / Dağ -->
  <polygon points="170,115 250,55 350,115" fill="#C8E6C9" stroke="#66BB6A" stroke-width="0.75"/>
  <text x="290" y="105" font-family="Noto Sans" font-size="8" fill="#2E7D32">Yüzeysel Akış &amp; Sızma</text>
</svg>'''

    # S6 (indeks 5): Küresel Su Rezervleri Dağılımı
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.75"/>
  <text x="95" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#0D47A1" text-anchor="middle">Tüm Su Varlığı</text>
  <rect x="40" y="48" width="80" height="20" rx="3" fill="#1E88E5"/>
  <text x="135" y="62" font-family="Noto Sans" font-size="9" fill="#0D47A1">%97,5 Tuzlu</text>
  <rect x="40" y="74" width="20" height="20" rx="3" fill="#43A047"/>
  <text x="135" y="88" font-family="Noto Sans" font-size="9" fill="#1B5E20">%2,5 Tatlı</text>

  <rect x="195" y="15" width="140" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="265" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#1B5E20" text-anchor="middle">Tatlı Suların Payı</text>
  <text x="265" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Buzullar: ~%68,7</text>
  <text x="265" y="72" font-family="Noto Sans" font-size="8" fill="#388E3C" text-anchor="middle">Yeraltı Suları: ~%30,1</text>
  <text x="265" y="89" font-family="Noto Sans" font-size="8" fill="#4CAF50" text-anchor="middle">Yüzey Gölleri/Nehir: ~%1,2</text>
</svg>'''

    # S7 (indeks 6): Kapalı Havza Denge Modeli
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#FFFDE7" stroke="#FFF59D" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#F57F17" text-anchor="middle">Kapalı Havza Su Bilançosu</text>
  <rect x="50" y="48" width="100" height="45" rx="4" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="100" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0277BD" text-anchor="middle">Gelir Unsurları</text>
  <text x="100" y="82" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">Yağış + Akarsu Girişi</text>

  <text x="180" y="73" font-family="Noto Sans" font-size="12" font-weight="bold" fill="#757575" text-anchor="middle">=</text>

  <rect x="210" y="48" width="100" height="45" rx="4" fill="#FBE9E7" stroke="#FFAB91" stroke-width="0.75"/>
  <text x="260" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#D84315" text-anchor="middle">Gider Unsurları</text>
  <text x="260" y="82" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">Şiddetli Buharlaşma</text>
</svg>'''

    # S9 (indeks 8): CBS Uygunluk Haritası Örneği
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="120" height="95" rx="6" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <!-- Hücre Izgarası -->
  <rect x="45" y="25" width="30" height="30" fill="#C8E6C9" stroke="#81C784" stroke-width="0.5"/>
  <rect x="75" y="25" width="30" height="30" fill="#FFF59D" stroke="#FFF176" stroke-width="0.5"/>
  <rect x="105" y="25" width="30" height="30" fill="#FFCDD2" stroke="#E57373" stroke-width="0.5"/>
  <rect x="45" y="55" width="30" height="30" fill="#C8E6C9" stroke="#81C784" stroke-width="0.5"/>
  <rect x="75" y="55" width="30" height="30" fill="#C8E6C9" stroke="#81C784" stroke-width="0.5"/>
  <rect x="105" y="55" width="30" height="30" fill="#FFF59D" stroke="#FFF176" stroke-width="0.5"/>
  <text x="95" y="102" font-family="Noto Sans" font-size="8" fill="#424242" text-anchor="middle">Piksel Tabanlı Analiz</text>

  <!-- Ok -->
  <path d="M 170 62 L 195 62" stroke="#616161" stroke-width="1.2"/>

  <!-- Sağ Panel: Karar Matrisi -->
  <rect x="205" y="15" width="120" height="95" rx="6" fill="#E8EAF6" stroke="#C5CAE9" stroke-width="0.75"/>
  <text x="265" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1A237E" text-anchor="middle">Uygunluk Skoru</text>
  <circle cx="225" cy="52" r="5" fill="#4CAF50"/>
  <text x="240" y="55" font-family="Noto Sans" font-size="8" fill="#1B5E20">Yüksek Uygunluk</text>
  <circle cx="225" cy="70" r="5" fill="#FBC02D"/>
  <text x="240" y="73" font-family="Noto Sans" font-size="8" fill="#F57F17">Orta Uygunluk</text>
  <circle cx="225" cy="88" r="5" fill="#E53935"/>
  <text x="240" y="91" font-family="Noto Sans" font-size="8" fill="#B71C1C">Düşük Uygunluk</text>
</svg>'''

    # S11 (indeks 10): Akifer ve Yeraltı Suyu Tablosu
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="6" fill="#EFEBE9" stroke="#D7CCC8" stroke-width="0.75"/>
  <text x="180" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4E342E" text-anchor="middle">Yeraltı Suyu Kesiti (Akifer Yapısı)</text>
  <!-- Geçirimsiz Tabaka -->
  <rect x="45" y="42" width="270" height="15" fill="#BCAAA4" stroke="#8D6E63" stroke-width="0.5"/>
  <text x="180" y="53" font-family="Noto Sans" font-size="7" fill="#3E2723" text-anchor="middle">Üst Geçirimsiz Katman (Kil)</text>
  <!-- Akifer (Su Deposu) -->
  <rect x="45" y="58" width="270" height="24" fill="#BBDEFB" stroke="#64B5F6" stroke-width="0.5"/>
  <text x="180" y="73" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1" text-anchor="middle">Basınçlı Akifer (Kum - Çakıl Gözenekleri)</text>
  <!-- Alt Geçirimsiz Tabaka -->
  <rect x="45" y="83" width="270" height="18" fill="#BCAAA4" stroke="#8D6E63" stroke-width="0.5"/>
  <text x="180" y="95" font-family="Noto Sans" font-size="7" fill="#3E2723" text-anchor="middle">Taban Ana Kayaç</text>
</svg>'''
