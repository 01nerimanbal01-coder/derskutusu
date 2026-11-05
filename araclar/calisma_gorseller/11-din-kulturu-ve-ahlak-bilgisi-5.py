# -*- coding: utf-8 -*-
"""11-din-kulturu-ve-ahlak-bilgisi-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): İnsan ve Mükellefiyet Bileşenleri
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="d1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
    <linearGradient id="d2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E3F2FD"/><stop offset="100%" stop-color="#BBDEFB"/>
    </linearGradient>
    <linearGradient id="d3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="95" height="95" rx="6" fill="url(#d1)" stroke="#81C784" stroke-width="0.75"/>
  <text x="62" y="40" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#1B5E20" text-anchor="middle">AKIL</text>
  <text x="62" y="65" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">İyiyi Kötüden</text>
  <text x="62" y="80" font-family="Noto Sans" font-size="8" fill="#388E3C" text-anchor="middle">Ayırt Etme Gücü</text>

  <text x="125" y="65" font-family="Noto Sans" font-size="14" font-weight="bold" fill="#757575" text-anchor="middle">+</text>

  <rect x="135" y="15" width="95" height="95" rx="6" fill="url(#d2)" stroke="#64B5F6" stroke-width="0.75"/>
  <text x="182" y="40" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#0D47A1" text-anchor="middle">İRADE</text>
  <text x="182" y="65" font-family="Noto Sans" font-size="8" fill="#1565C0" text-anchor="middle">Özgürce Seçim</text>
  <text x="182" y="80" font-family="Noto Sans" font-size="8" fill="#1976D2" text-anchor="middle">Yapabilme Yetisi</text>

  <text x="245" y="65" font-family="Noto Sans" font-size="14" font-weight="bold" fill="#757575" text-anchor="middle">=</text>

  <rect x="255" y="15" width="90" height="95" rx="6" fill="url(#d3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="300" y="40" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">MESULİYET</text>
  <text x="300" y="65" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Ahlaki &amp; Dinî</text>
  <text x="300" y="80" font-family="Noto Sans" font-size="8" fill="#F57C00" text-anchor="middle">Hesap Verme</text>
</svg>'''

    # S2 (indeks 1): Tercih ve Yöneliş Diyagramı
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="40" width="80" height="45" rx="6" fill="#EDE7F6" stroke="#B39DDB" stroke-width="0.75"/>
  <text x="65" y="62" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">Cüz’î İrade</text>
  <text x="65" y="75" font-family="Noto Sans" font-size="7" fill="#6A1B9A" text-anchor="middle">(Seçme Gücü)</text>

  <!-- Oklar -->
  <path d="M 115 52 L 175 32" stroke="#2E7D32" stroke-width="1.5"/>
  <path d="M 115 72 L 175 92" stroke="#C62828" stroke-width="1.5"/>

  <!-- Hayır Yolu -->
  <rect x="185" y="15" width="150" height="38" rx="5" fill="#E8F5E9" stroke="#81C784" stroke-width="0.75"/>
  <text x="260" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Hayır ve Adalet Yolu</text>
  <text x="260" y="45" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Sevap ve Manevi Huzur</text>

  <!-- Şer Yolu -->
  <rect x="185" y="75" width="150" height="38" rx="5" fill="#FFEBEE" stroke="#E57373" stroke-width="0.75"/>
  <text x="260" y="92" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">Haksızlık ve Kötülük</text>
  <text x="260" y="105" font-family="Noto Sans" font-size="7" fill="#C62828" text-anchor="middle">Ahlaki Kusur ve Günah</text>
</svg>'''

    # S3 (indeks 2): Küllî vs Cüz’î İrade Karşılaştırması
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Dış Halka: Küllî İrade -->
  <rect x="20" y="10" width="320" height="105" rx="10" fill="#F3E5F5" stroke="#BA68C8" stroke-width="0.75"/>
  <text x="180" y="28" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#6A1B9A" text-anchor="middle">KÜLLÎ İRADE (Yüce Allah’ın Mutlak İradesi)</text>
  <text x="180" y="42" font-family="Noto Sans" font-size="8" fill="#8E24AA" text-anchor="middle">Evrendeki fiziki, biyolojik yasalar ve insan iradesi dışındaki alanlar</text>

  <!-- İç Kutu: Cüz’î İrade -->
  <rect x="65" y="52" width="230" height="52" rx="6" fill="#EDE7F6" stroke="#7E57C2" stroke-width="0.75"/>
  <text x="180" y="70" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4527A0" text-anchor="middle">CÜZ’Î İRADE (İnsanın Seçim Sahası)</text>
  <text x="180" y="85" font-family="Noto Sans" font-size="8" fill="#5E35B1" text-anchor="middle">Doğru-yanlış, niyet, ahlak ve tercihler (Sorumluluk Alanı)</text>
</svg>'''

    # S4 (indeks 3): Tevekkül Dengesi
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#E0F2F1" stroke="#80CBC4" stroke-width="0.75"/>
  <text x="95" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#004D40" text-anchor="middle">1. ADIM: TEDBİR</text>
  <text x="95" y="60" font-family="Noto Sans" font-size="8" fill="#00695C" text-anchor="middle">Aklın gerektirdiği tüm</text>
  <text x="95" y="75" font-family="Noto Sans" font-size="8" fill="#00796B" text-anchor="middle">çabayı sarf etmek,</text>
  <text x="95" y="90" font-family="Noto Sans" font-size="8" fill="#004D40" text-anchor="middle">sebeplere sarılmak</text>

  <!-- Ok -->
  <path d="M 175 62 L 195 62" stroke="#004D40" stroke-width="1.5"/>

  <rect x="205" y="15" width="130" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="270" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#1B5E20" text-anchor="middle">2. ADIM: TEVEKKÜL</text>
  <text x="270" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Sonucu Allah’a</text>
  <text x="270" y="75" font-family="Noto Sans" font-size="8" fill="#388E3C" text-anchor="middle">bırakıp güvenmek,</text>
  <text x="270" y="90" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">iç huzurunu korumak</text>
</svg>'''

    # S6 (indeks 5): İrade Sınırları Ayrımı
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="95" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#37474F" text-anchor="middle">Seçime Dayalı Olmayan</text>
  <text x="95" y="55" font-family="Noto Sans" font-size="8" fill="#546E7A" text-anchor="middle">• Doğum zamanı ve yeri</text>
  <text x="95" y="70" font-family="Noto Sans" font-size="8" fill="#546E7A" text-anchor="middle">• Genetik ve ırki yapı</text>
  <text x="95" y="85" font-family="Noto Sans" font-size="8" fill="#546E7A" text-anchor="middle">• Biyolojik fıtrat</text>
  <text x="95" y="100" font-family="Noto Sans" font-size="7" fill="#78909C" text-anchor="middle">(Sorumluluk yoktur)</text>

  <rect x="195" y="15" width="140" height="95" rx="6" fill="#F1F8E9" stroke="#C5E1A5" stroke-width="0.75"/>
  <text x="265" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">İradi Tercihler</text>
  <text x="265" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• İman ve ahlaki tutum</text>
  <text x="265" y="70" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Adalet ve dürüstlük</text>
  <text x="265" y="85" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Yardımlaşma ve niyet</text>
  <text x="265" y="100" font-family="Noto Sans" font-size="7" fill="#33691E" text-anchor="middle">(Tam sorumluluk vardır)</text>
</svg>'''

    # S7 (indeks 6): Cebriye Eleştirisi
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">Kadercilik (Cebriye) Yanılgısı</text>
  <text x="180" y="55" font-family="Noto Sans" font-size="8" fill="#BF360C" text-anchor="middle">"Rüzgâr önündeki yaprak gibi iradesizim" iddiası geçersizdir.</text>
  <line x1="50" y1="65" x2="310" y2="65" stroke="#FFCC80" stroke-width="0.75"/>
  <text x="180" y="80" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#D84315" text-anchor="middle">İslam’ın Ehl-i Sünnet İlkesi:</text>
  <text x="180" y="95" font-family="Noto Sans" font-size="8" fill="#E65100" text-anchor="middle">Kulu fiillerinde tercih sahibi kılan Yüce Allah, hesabı da bu tercihe göre sorar.</text>
</svg>'''

    # S9 (indeks 8): Zilzâl Suresi Ayeti İlkesi
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="310" height="95" rx="8" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">İlahi Adalet ve Hassas Terazi</text>
  <rect x="45" y="48" width="115" height="45" rx="4" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="102" y="65" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Zerre Kadar Hayır</text>
  <text x="102" y="80" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Mükâfatla karşılık bulur</text>

  <rect x="200" y="48" width="115" height="45" rx="4" fill="#FFEBEE" stroke="#FFCDD2" stroke-width="0.75"/>
  <text x="257" y="65" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#B71C1C" text-anchor="middle">Zerre Kadar Şer</text>
  <text x="257" y="80" font-family="Noto Sans" font-size="7" fill="#C62828" text-anchor="middle">Hesapla karşılık bulur</text>
</svg>'''

    # S11 (indeks 10): Ahlak ve Niyet Bütünlüğü
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <circle cx="100" cy="62" r="30" fill="#E1F5FE" stroke="#4FC3F7" stroke-width="0.75"/>
  <text x="100" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0277BD" text-anchor="middle">Samimi</text>
  <text x="100" y="70" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0277BD" text-anchor="middle">Niyet</text>

  <path d="M 140 62 L 175 62" stroke="#546E7A" stroke-width="1.5"/>

  <circle cx="215" cy="62" r="30" fill="#E8F5E9" stroke="#81C784" stroke-width="0.75"/>
  <text x="215" y="58" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">Salih</text>
  <text x="215" y="70" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">Amel</text>

  <rect x="260" y="35" width="55" height="55" rx="4" fill="#FFF9C4" stroke="#FFF176" stroke-width="0.75"/>
  <text x="287" y="55" font-family="Noto Sans" font-size="7" font-weight="bold" fill="#F57F17" text-anchor="middle">Manevi</text>
  <text x="287" y="70" font-family="Noto Sans" font-size="7" fill="#F57F17" text-anchor="middle">Değer</text>
</svg>'''
