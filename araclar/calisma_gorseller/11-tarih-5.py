# -*- coding: utf-8 -*-
"""11-tarih-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Lale Devri Islahatları Şeması
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="t1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EFEBE9"/><stop offset="100%" stop-color="#D7CCC8"/>
    </linearGradient>
    <linearGradient id="t2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8EAF6"/><stop offset="100%" stop-color="#C5CAE9"/>
    </linearGradient>
    <linearGradient id="t3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
    <linearGradient id="t4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E0F2F1"/><stop offset="100%" stop-color="#B2DFDB"/>
    </linearGradient>
  </defs>
  <rect x="5" y="10" width="80" height="105" rx="6" fill="url(#t1)" stroke="#BCAAA4" stroke-width="0.75"/>
  <text x="45" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4E342E" text-anchor="middle">Matbaa (1727)</text>
  <text x="45" y="55" font-family="Noto Sans" font-size="8" fill="#5D4037" text-anchor="middle">İ. Müteferrika</text>
  <text x="45" y="70" font-family="Noto Sans" font-size="8" fill="#5D4037" text-anchor="middle">Din dışı eser</text>
  <text x="45" y="90" font-family="Noto Sans" font-size="7" fill="#3E2723" text-anchor="middle">Vankulu Lugatı</text>

  <rect x="95" y="10" width="80" height="105" rx="6" fill="url(#t2)" stroke="#9FA8DA" stroke-width="0.75"/>
  <text x="135" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1A237E" text-anchor="middle">Elçilikler</text>
  <text x="135" y="55" font-family="Noto Sans" font-size="8" fill="#283593" text-anchor="middle">28 Çelebi Mehmed</text>
  <text x="135" y="70" font-family="Noto Sans" font-size="8" fill="#283593" text-anchor="middle">Paris Sefareti</text>
  <text x="135" y="90" font-family="Noto Sans" font-size="7" fill="#1A237E" text-anchor="middle">Batı’yı Tanıma</text>

  <rect x="185" y="10" width="80" height="105" rx="6" fill="url(#t3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="225" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">İtfaiye</text>
  <text x="225" y="55" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Tulumbacılar</text>
  <text x="225" y="70" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Yangın timi</text>
  <text x="225" y="90" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">Yeniçeri erleri</text>

  <rect x="275" y="10" width="80" height="105" rx="6" fill="url(#t4)" stroke="#80CBC4" stroke-width="0.75"/>
  <text x="315" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#004D40" text-anchor="middle">Sağlık &amp; Sanayi</text>
  <text x="315" y="55" font-family="Noto Sans" font-size="8" fill="#00695C" text-anchor="middle">Çiçek aşısı</text>
  <text x="315" y="70" font-family="Noto Sans" font-size="8" fill="#00695C" text-anchor="middle">Yalova kâğıt</text>
  <text x="315" y="90" font-family="Noto Sans" font-size="7" fill="#004D40" text-anchor="middle">Tekfur çinisi</text>
</svg>'''

    # S2 (indeks 1): 1718 Pasarofça Antlaşması Sonucu
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="145" height="95" rx="6" fill="#FFEBEE" stroke="#EF9A9A" stroke-width="0.75"/>
  <text x="97" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">Önceki Siyaset (1699 Öncesi)</text>
  <text x="97" y="55" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• Fetih ve Gaza anlayışı</text>
  <text x="97" y="70" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• Batı’yı kendinden aşağı görme</text>
  <text x="97" y="85" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• Sürekli sefer politikası</text>

  <!-- Dönüşüm Oku -->
  <path d="M 175 62 L 185 62" stroke="#455A64" stroke-width="1.2"/>

  <rect x="190" y="15" width="145" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="262" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Pasarofça Sonrası (1718)</text>
  <text x="262" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Barışı koruma ve savunma</text>
  <text x="262" y="70" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Batı üstünlüğünü kabul</text>
  <text x="262" y="85" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Diplomatik temsilcilikler</text>
</svg>'''

    # S3 (indeks 2): Paris Sefaretnamesi Kitabı
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="40" y="20" width="85" height="85" rx="4" fill="#5D4037" stroke="#3E2723" stroke-width="1"/>
  <rect x="48" y="25" width="70" height="75" fill="#D7CCC8"/>
  <text x="83" y="48" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#3E2723" text-anchor="middle">PARİS</text>
  <text x="83" y="62" font-family="Noto Sans" font-size="7" font-weight="bold" fill="#3E2723" text-anchor="middle">SEFARET-</text>
  <text x="83" y="74" font-family="Noto Sans" font-size="7" font-weight="bold" fill="#3E2723" text-anchor="middle">NAMESİ</text>
  <text x="83" y="90" font-family="Noto Sans" font-size="6" fill="#4E342E" text-anchor="middle">1720 - 1721</text>

  <!-- Sağ Panel: Gözlemler -->
  <rect x="145" y="15" width="180" height="95" rx="6" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="235" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#283593" text-anchor="middle">Raporlanan Alanlar</text>
  <text x="235" y="55" font-family="Noto Sans" font-size="8" fill="#3949AB" text-anchor="middle">• Barok ve Rokoko mimarisi</text>
  <text x="235" y="70" font-family="Noto Sans" font-size="8" fill="#3949AB" text-anchor="middle">• Rasathane ve askeri kışlalar</text>
  <text x="235" y="85" font-family="Noto Sans" font-size="8" fill="#3949AB" text-anchor="middle">• Şehir bahçeleri &amp; matbaalar</text>
  <text x="235" y="100" font-family="Noto Sans" font-size="7" fill="#1A237E" text-anchor="middle">Yazar: 28 Çelebi Mehmed Efendi</text>
</svg>'''

    # S4 (indeks 3): Müteferrika Matbaa Makinesi
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Ahşap Matbaa Presi -->
  <rect x="80" y="30" width="10" height="75" fill="#4E342E"/>
  <rect x="150" y="30" width="10" height="75" fill="#4E342E"/>
  <rect x="75" y="25" width="90" height="12" fill="#5D4037"/>
  <rect x="90" y="55" width="60" height="8" fill="#8D6E63"/>
  <line x1="120" y1="37" x2="120" y2="55" stroke="#212121" stroke-width="4"/>

  <!-- Basılan Kâğıt -->
  <rect x="95" y="75" width="50" height="20" fill="#FFF9C4" stroke="#FBC02D" stroke-width="0.5"/>
  <text x="120" y="88" font-family="Noto Sans" font-size="6" fill="#F57F17" text-anchor="middle">Kâğıt Baskı</text>

  <!-- Sağ Panel -->
  <rect x="195" y="15" width="135" height="95" rx="6" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="0.75"/>
  <text x="262" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#3E2723" text-anchor="middle">İlk Osmanlı Matbaası</text>
  <text x="262" y="55" font-family="Noto Sans" font-size="8" fill="#4E342E" text-anchor="middle">Yıl: 1727 İstanbul</text>
  <text x="262" y="70" font-family="Noto Sans" font-size="8" fill="#4E342E" text-anchor="middle">Kurucu: İ. Müteferrika</text>
  <text x="262" y="85" font-family="Noto Sans" font-size="7" fill="#5D4037" text-anchor="middle">Hattatlar korundu,</text>
  <text x="262" y="98" font-family="Noto Sans" font-size="7" fill="#5D4037" text-anchor="middle">yalnız bilimsel basıldı.</text>
</svg>'''

    # S6 (indeks 5): Lale Devri Öncüleri Portre Kartları
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="15" y="15" width="75" height="95" rx="5" fill="#FFF8E1" stroke="#FFE082" stroke-width="0.75"/>
  <text x="52" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#F57F17" text-anchor="middle">III. Ahmed</text>
  <text x="52" y="55" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Padişah</text>
  <text x="52" y="75" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Kültür ve sanat</text>
  <text x="52" y="90" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">hamisi</text>

  <rect x="100" y="15" width="75" height="95" rx="5" fill="#E8F5E9" stroke="#C8E6C9" stroke-width="0.75"/>
  <text x="137" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Damat İbrahim</text>
  <text x="137" y="55" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Sadrazam</text>
  <text x="137" y="75" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Barış diplomasisi</text>
  <text x="137" y="90" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">mimarı</text>

  <rect x="185" y="15" width="75" height="95" rx="5" fill="#E1F5FE" stroke="#B3E5FC" stroke-width="0.75"/>
  <text x="222" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B" text-anchor="middle">Nedim</text>
  <text x="222" y="55" font-family="Noto Sans" font-size="7" fill="#0277BD" text-anchor="middle">Divan Şairi</text>
  <text x="222" y="75" font-family="Noto Sans" font-size="7" fill="#0277BD" text-anchor="middle">Lirik şarkılar</text>
  <text x="222" y="90" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">ve zevk tasviri</text>

  <rect x="270" y="15" width="75" height="95" rx="5" fill="#F3E5F5" stroke="#E1BEE7" stroke-width="0.75"/>
  <text x="307" y="35" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#4A148C" text-anchor="middle">Levni</text>
  <text x="307" y="55" font-family="Noto Sans" font-size="7" fill="#6A1B9A" text-anchor="middle">Minyatür Ustası</text>
  <text x="307" y="75" font-family="Noto Sans" font-size="7" fill="#6A1B9A" text-anchor="middle">Surname-i Vehbi</text>
  <text x="307" y="90" font-family="Noto Sans" font-size="7" fill="#4A148C" text-anchor="middle">tasvirleri</text>
</svg>'''

    # S7 (indeks 6): Patrona Halil İsyanı Nedenleri
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#E65100" text-anchor="middle">1730 Patrona Halil İsyanı ve Dönemin Sonu</text>

  <rect x="45" y="48" width="125" height="45" rx="4" fill="#FFEBEE" stroke="#EF9A9A" stroke-width="0.75"/>
  <text x="107" y="65" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#B71C1C" text-anchor="middle">Saray Zümresi</text>
  <text x="107" y="80" font-family="Noto Sans" font-size="7" fill="#C62828" text-anchor="middle">Aşırı lüks, köşkler &amp; israf</text>

  <line x1="175" y1="70" x2="195" y2="70" stroke="#B71C1C" stroke-width="1.5"/>

  <rect x="200" y="48" width="120" height="45" rx="4" fill="#EFEBE9" stroke="#BCAAA4" stroke-width="0.75"/>
  <text x="260" y="65" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#4E342E" text-anchor="middle">Halk &amp; Esnaf</text>
  <text x="260" y="80" font-family="Noto Sans" font-size="7" fill="#5D4037" text-anchor="middle">Ağır vergiler &amp; hayat pahalılığı</text>
</svg>'''

    # S9 (indeks 8): İlk Basılan Eser: Vankulu Lugatı
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#3E2723" text-anchor="middle">Matbaada Basılan İlk Kitap (1729)</text>
  <rect x="65" y="48" width="230" height="45" rx="4" fill="#EFEBE9" stroke="#D7CCC8" stroke-width="0.75"/>
  <text x="180" y="68" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#4E342E" text-anchor="middle">VANKULU LUGATI (2 Cilt)</text>
  <text x="180" y="84" font-family="Noto Sans" font-size="8" fill="#5D4037" text-anchor="middle">Sıhâh-ı Cevherî Tercümesi - Mehmet Vankulu Efendi</text>
</svg>'''

    # S11 (indeks 10): Barok Çeşme Mimarisi
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#FFFDE7" stroke="#FFF59D" stroke-width="0.75"/>
  <!-- III. Ahmed Çeşmesi Kubbe Taslağı -->
  <path d="M 90 85 C 90 40 140 25 180 25 C 220 25 270 40 270 85 Z" fill="#FFF9C4" stroke="#FBC02D" stroke-width="1"/>
  <rect x="110" y="55" width="140" height="45" fill="#FFFDE7" stroke="#FBC02D" stroke-width="0.75"/>
  <text x="180" y="75" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#F57F17" text-anchor="middle">III. Ahmed Çeşmesi (1728)</text>
  <text x="180" y="90" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Türk-İslam motifleriyle harmanlanan Avrupa Barok üslubu</text>
</svg>'''
