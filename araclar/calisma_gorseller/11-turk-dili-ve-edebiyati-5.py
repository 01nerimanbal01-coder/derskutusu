# -*- coding: utf-8 -*-
"""11-turk-dili-ve-edebiyati-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): İletişim Engelleri Matrisi
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="td1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEBEE"/><stop offset="100%" stop-color="#FFCDD2"/>
    </linearGradient>
    <linearGradient id="td2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
    <linearGradient id="td3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EDE7F6"/><stop offset="100%" stop-color="#D1C4E9"/>
    </linearGradient>
    <linearGradient id="td4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
  </defs>
  <rect x="5" y="10" width="80" height="105" rx="6" fill="url(#td1)" stroke="#EF5350" stroke-width="0.75"/>
  <text x="45" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">Ön Yargı</text>
  <text x="45" y="55" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">Peşin hüküm</text>
  <text x="45" y="70" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">ve kalıp yargı</text>
  <text x="45" y="90" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">Dinlemeyi keser</text>

  <rect x="95" y="10" width="80" height="105" rx="6" fill="url(#td2)" stroke="#FFA000" stroke-width="0.75"/>
  <text x="135" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">Gürültü</text>
  <text x="135" y="55" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Fiziksel kanal</text>
  <text x="135" y="70" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">parazitleri</text>
  <text x="135" y="90" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">İletiyi bozar</text>

  <rect x="185" y="10" width="80" height="105" rx="6" fill="url(#td3)" stroke="#7E57C2" stroke-width="0.75"/>
  <text x="225" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">Seçici Algı</text>
  <text x="225" y="55" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">Yalnız işine</text>
  <text x="225" y="70" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">geleni duyma</text>
  <text x="225" y="90" font-family="Noto Sans" font-size="7" fill="#4A148C" text-anchor="middle">Eksik dinleme</text>

  <rect x="275" y="10" width="80" height="105" rx="6" fill="url(#td4)" stroke="#66BB6A" stroke-width="0.75"/>
  <text x="315" y="32" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Beden Dili</text>
  <text x="315" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Jest &amp; mimik</text>
  <text x="315" y="70" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">uyumsuzluğu</text>
  <text x="315" y="90" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">Güveni sarsar</text>
</svg>'''

    # S2 (indeks 1): Eğitsel Drama Süreci
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="15" y="25" width="95" height="75" rx="6" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="62" y="48" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">1. Hazırlık / Isınma</text>
  <text x="62" y="68" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Grup oyunları &amp;</text>
  <text x="62" y="82" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Güven egzersizi</text>

  <path d="M 115 62 L 130 62" stroke="#546E7A" stroke-width="1.5"/>

  <rect x="135" y="25" width="95" height="75" rx="6" fill="#FFF8E1" stroke="#FFE082" stroke-width="0.75"/>
  <text x="182" y="48" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">2. Canlandırma</text>
  <text x="182" y="68" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Doğaçlama &amp;</text>
  <text x="182" y="82" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Dramatik çatışma</text>

  <path d="M 235 62 L 250 62" stroke="#546E7A" stroke-width="1.5"/>

  <rect x="255" y="25" width="90" height="75" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="300" y="48" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">3. Değerlendirme</text>
  <text x="300" y="68" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Duygu paylaşımı &amp;</text>
  <text x="300" y="82" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Çözümleme</text>
</svg>'''

    # S3 (indeks 2): Dramatik Çatışma ve Empati
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#FFEBEE" stroke="#EF9A9A" stroke-width="0.75"/>
  <text x="95" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">ÇATIŞMA UNSURU</text>
  <text x="95" y="60" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• Karşıt hedefler</text>
  <text x="95" y="75" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• İletişim kopukluğu</text>
  <text x="95" y="90" font-family="Noto Sans" font-size="8" fill="#B71C1C" text-anchor="middle">• Gerilim ve merak</text>

  <!-- Empati Dönüşüm Oku -->
  <path d="M 175 62 L 195 62" stroke="#7E57C2" stroke-width="1.5"/>

  <rect x="205" y="15" width="130" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="270" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">EMPATİ VE ÇÖZÜM</text>
  <text x="270" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Karşı tarafı anlama</text>
  <text x="270" y="75" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Bakış açısı esnekliği</text>
  <text x="270" y="90" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">• Uzlaşma dili</text>
</svg>'''

    # S4 (indeks 3): İletişim Döngüsü Şeması
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Kaynak -->
  <rect x="20" y="40" width="80" height="45" rx="5" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.75"/>
  <text x="60" y="62" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#01579B" text-anchor="middle">Kaynak (Gönderici)</text>
  <text x="60" y="74" font-family="Noto Sans" font-size="7" fill="#0277BD" text-anchor="middle">Kodlama</text>

  <!-- İleti Oku (Üst) -->
  <path d="M 105 50 L 255 50" stroke="#1565C0" stroke-width="1.5"/>
  <polygon points="255,46 263,50 255,54" fill="#1565C0"/>
  <text x="180" y="42" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1" text-anchor="middle">İleti (Kanal Üzerinden)</text>

  <!-- Alıcı -->
  <rect x="265" y="40" width="80" height="45" rx="5" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="305" y="62" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Alıcı (Hedef)</text>
  <text x="305" y="74" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Anlamlandırma</text>

  <!-- Dönüt Oku (Alt) -->
  <path d="M 265 75 L 115 75" stroke="#2E7D32" stroke-width="1.5"/>
  <polygon points="115,71 107,75 115,79" fill="#2E7D32"/>
  <text x="180" y="92" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Geri Bildirim (Dönüt)</text>
</svg>'''

    # S6 (indeks 5): Sen Dili vs Ben Dili
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="145" height="95" rx="6" fill="#FFEBEE" stroke="#EF9A9A" stroke-width="0.75"/>
  <text x="97" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">SEN DİLİ (Kırıcı)</text>
  <text x="97" y="58" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">"Beni hiç dinlemiyorsun!"</text>
  <text x="97" y="74" font-family="Noto Sans" font-size="7" fill="#D32F2F" text-anchor="middle">• Suçlayıcı ve yargılayıcı</text>
  <text x="97" y="88" font-family="Noto Sans" font-size="7" fill="#D32F2F" text-anchor="middle">• Karşıda savunma yaratır</text>
  <text x="97" y="102" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">• Çatışmayı büyütür</text>

  <rect x="190" y="15" width="145" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="262" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">BEN DİLİ (Yapıcı)</text>
  <text x="262" y="58" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">"Sözüm kesilince üzülüyorum."</text>
  <text x="262" y="74" font-family="Noto Sans" font-size="7" fill="#388E3C" text-anchor="middle">• Duyguyu dürüstçe ifade eder</text>
  <text x="262" y="88" font-family="Noto Sans" font-size="7" fill="#388E3C" text-anchor="middle">• Empati zeminini açar</text>
  <text x="262" y="102" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">• Çözüme odaklandırır</text>
</svg>'''

    # S7 (indeks 6): Sözlü Sunum İlkeleri
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#37474F" text-anchor="middle">Etkili Sözlü Sunumun Sacayakları</text>

  <rect x="45" y="48" width="80" height="45" rx="4" fill="#E3F2FD" stroke="#90CAF9" stroke-width="0.75"/>
  <text x="85" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#0D47A1" text-anchor="middle">Göz Teması</text>
  <text x="85" y="82" font-family="Noto Sans" font-size="7" fill="#1565C0" text-anchor="middle">Güven bağı</text>

  <rect x="140" y="48" width="80" height="45" rx="4" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="180" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Ses Tonu</text>
  <text x="180" y="82" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Dinamik vurgu</text>

  <rect x="235" y="48" width="80" height="45" rx="4" fill="#FFF3E0" stroke="#FFCC80" stroke-width="0.75"/>
  <text x="275" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#E65100" text-anchor="middle">Beden Dili</text>
  <text x="275" y="82" font-family="Noto Sans" font-size="7" fill="#EF6C00" text-anchor="middle">Açık duruş</text>
</svg>'''

    # S9 (indeks 8): Değerlendirme Çemberi
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">Drama Değerlendirme Çemberi</text>
  <circle cx="180" cy="72" r="28" fill="#FFFFFF" stroke="#7E57C2" stroke-width="1"/>
  <text x="180" y="68" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#512DA8" text-anchor="middle">Paylaşım &amp;</text>
  <text x="180" y="80" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#512DA8" text-anchor="middle">Farkındalık</text>
  <circle cx="135" cy="72" r="4" fill="#7E57C2"/>
  <circle cx="225" cy="72" r="4" fill="#7E57C2"/>
  <circle cx="180" cy="38" r="3" fill="#7E57C2"/>
  <circle cx="180" cy="106" r="3" fill="#7E57C2"/>
</svg>'''

    # S11 (indeks 10): Jest ve Mimik Uyumu
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <rect x="50" y="30" width="120" height="42" rx="4" fill="#E0F2F1" stroke="#80CBC4" stroke-width="0.75"/>
  <text x="110" y="48" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#004D40" text-anchor="middle">Jest (El &amp; Beden)</text>
  <text x="110" y="64" font-family="Noto Sans" font-size="7" fill="#00695C" text-anchor="middle">Düşünceyi destekler</text>

  <rect x="190" y="30" width="120" height="42" rx="4" fill="#FCE4EC" stroke="#F48FB1" stroke-width="0.75"/>
  <text x="250" y="48" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#880E4F" text-anchor="middle">Mimik (Yüz İfadesi)</text>
  <text x="250" y="64" font-family="Noto Sans" font-size="7" fill="#AD1457" text-anchor="middle">Duyguyu yansıtır</text>

  <text x="180" y="98" font-family="Noto Sans" font-size="8" fill="#616161" text-anchor="middle">Söz + Ses + Beden = Bütüncül ve Etkili İletişim</text>
</svg>'''
