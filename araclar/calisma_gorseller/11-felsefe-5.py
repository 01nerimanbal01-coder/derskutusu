# -*- coding: utf-8 -*-
"""11-felsefe-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Çevre Etiği Kademeleri
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="fe1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEBEE"/><stop offset="100%" stop-color="#FFCDD2"/>
    </linearGradient>
    <linearGradient id="fe2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF8E1"/><stop offset="100%" stop-color="#FFE082"/>
    </linearGradient>
    <linearGradient id="fe3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="95" height="95" rx="6" fill="url(#fe1)" stroke="#EF5350" stroke-width="0.75"/>
  <text x="62" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">Antroposentrizm</text>
  <text x="62" y="58" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">İnsan Merkezci</text>
  <text x="62" y="74" font-family="Noto Sans" font-size="7" fill="#D32F2F" text-anchor="middle">Doğa araçsal</text>
  <text x="62" y="88" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">değere sahiptir</text>

  <rect x="132" y="15" width="95" height="95" rx="6" fill="url(#fe2)" stroke="#FFA000" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">Biyosentrizm</text>
  <text x="180" y="58" font-family="Noto Sans" font-size="8" fill="#F57C00" text-anchor="middle">Canlı Merkezci</text>
  <text x="180" y="74" font-family="Noto Sans" font-size="7" fill="#EF6C00" text-anchor="middle">Tüm canlılar</text>
  <text x="180" y="88" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">özsel değer taşır</text>

  <rect x="250" y="15" width="95" height="95" rx="6" fill="url(#fe3)" stroke="#66BB6A" stroke-width="0.75"/>
  <text x="297" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Ekosentrizm</text>
  <text x="297" y="58" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Çevre Merkezci</text>
  <text x="297" y="74" font-family="Noto Sans" font-size="7" fill="#388E3C" text-anchor="middle">Ekosistem bütünü</text>
  <text x="297" y="88" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">ahlaki öznedir</text>
</svg>'''

    # S2 (indeks 1): Mekanik Doğa vs Ekolojik Doğa
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="20" y="15" width="145" height="95" rx="6" fill="#ECEFF1" stroke="#CFD8DC" stroke-width="0.75"/>
  <text x="92" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#37474F" text-anchor="middle">Mekanik Doğa (17. Yy)</text>
  <circle cx="92" cy="60" r="14" fill="#B0BEC5" stroke="#78909C" stroke-width="0.75"/>
  <!-- Çark dişleri -->
  <line x1="92" y1="42" x2="92" y2="78" stroke="#455A64" stroke-width="1.5"/>
  <line x1="74" y1="60" x2="110" y2="60" stroke="#455A64" stroke-width="1.5"/>
  <text x="92" y="92" font-family="Noto Sans" font-size="7" fill="#455A64" text-anchor="middle">"Doğaya egemen ol"</text>
  <text x="92" y="103" font-family="Noto Sans" font-size="7" fill="#607D8B" text-anchor="middle">(Descartes &amp; Bacon)</text>

  <!-- Karşıtlık Oku -->
  <path d="M 175 62 L 185 62" stroke="#78909C" stroke-width="1.2"/>

  <rect x="195" y="15" width="145" height="95" rx="6" fill="#E8F5E9" stroke="#C8E6C9" stroke-width="0.75"/>
  <text x="267" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Organik / Ekolojik Doğa</text>
  <circle cx="267" cy="60" r="14" fill="#A5D6A7" stroke="#388E3C" stroke-width="0.75"/>
  <text x="267" y="92" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">"Doğayla uyum içinde yaşa"</text>
  <text x="267" y="103" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">(Yaşam Ağı &amp; Bütünlük)</text>
</svg>'''

    # S3 (indeks 2): Değer Türleri Karşılaştırması
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#FBE9E7" stroke="#FFCCBC" stroke-width="0.75"/>
  <text x="95" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#D84315" text-anchor="middle">ARAÇSAL DEĞER</text>
  <text x="95" y="60" font-family="Noto Sans" font-size="8" fill="#E64A19" text-anchor="middle">• Fayda sağladığı için</text>
  <text x="95" y="75" font-family="Noto Sans" font-size="8" fill="#E64A19" text-anchor="middle">• İnsan ihtiyacına göre</text>
  <text x="95" y="90" font-family="Noto Sans" font-size="8" fill="#BF360C" text-anchor="middle">• Tüketim metaı olarak</text>

  <rect x="195" y="15" width="140" height="95" rx="6" fill="#E8F5E9" stroke="#C8E6C9" stroke-width="0.75"/>
  <text x="265" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#1B5E20" text-anchor="middle">ÖZSEL DEĞER</text>
  <text x="265" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Kendinde varoluş kıymeti</text>
  <text x="265" y="75" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Çıkardan bağımsız hak</text>
  <text x="265" y="90" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">• Biyo-merkezli etik</text>
</svg>'''

    # S4 (indeks 3): Biyosferik Eşitlik Şeması
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#E0F2F1" stroke="#80CBC4" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#004D40" text-anchor="middle">Derin Ekoloji: Biyosferik Eşitlik</text>
  <circle cx="80" cy="70" r="22" fill="#B2DFDB" stroke="#00796B" stroke-width="0.75"/>
  <text x="80" y="73" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#004D40" text-anchor="middle">Bitkiler</text>
  <circle cx="145" cy="70" r="22" fill="#B2DFDB" stroke="#00796B" stroke-width="0.75"/>
  <text x="145" y="73" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#004D40" text-anchor="middle">Hayvanlar</text>
  <circle cx="210" cy="70" r="22" fill="#B2DFDB" stroke="#00796B" stroke-width="0.75"/>
  <text x="210" y="73" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#004D40" text-anchor="middle">İnsanlar</text>
  <circle cx="275" cy="70" r="22" fill="#B2DFDB" stroke="#00796B" stroke-width="0.75"/>
  <text x="275" y="73" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#004D40" text-anchor="middle">Ekosistem</text>
  <text x="180" y="103" font-family="Noto Sans" font-size="7" fill="#00695C" text-anchor="middle">Hiçbir tür diğerinden ontolojik olarak üstün değildir.</text>
</svg>'''

    # S6 (indeks 5): Hans Jonas Gelecek Sorumluluğu
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="140" height="95" rx="6" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.75"/>
  <text x="95" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">Bugünkü Kuşaklar</text>
  <text x="95" y="60" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">• Teknolojik güç</text>
  <text x="95" y="75" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">• Kaynak tüketimi</text>
  <text x="95" y="90" font-family="Noto Sans" font-size="8" fill="#4A148C" text-anchor="middle">• Ekolojik ayak izi</text>

  <!-- Sorumluluk Bağı Oku -->
  <path d="M 175 62 L 195 62" stroke="#5E35B1" stroke-width="1.5"/>

  <rect x="205" y="15" width="130" height="95" rx="6" fill="#F3E5F5" stroke="#E1BEE7" stroke-width="0.75"/>
  <text x="270" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">Gelecek Nesiller</text>
  <text x="270" y="60" font-family="Noto Sans" font-size="8" fill="#7B1FA2" text-anchor="middle">• Yaşanabilir dünya</text>
  <text x="270" y="75" font-family="Noto Sans" font-size="8" fill="#7B1FA2" text-anchor="middle">• Temiz su &amp; hava</text>
  <text x="270" y="90" font-family="Noto Sans" font-size="8" fill="#4A148C" text-anchor="middle">• Varoluş hakkı</text>
</svg>'''

    # S7 (indeks 6): Sığ ve Derin Ekoloji Zıtlığı
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="140" height="95" rx="6" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="0.75"/>
  <text x="100" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">Sığ Ekoloji</text>
  <text x="100" y="55" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">• Çevre kirliliğini önle</text>
  <text x="100" y="70" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">• Ama tüketimi sürdür</text>
  <text x="100" y="85" font-family="Noto Sans" font-size="8" fill="#BF360C" text-anchor="middle">• İnsan refahı öncelikli</text>

  <rect x="190" y="15" width="140" height="95" rx="6" fill="#E8F5E9" stroke="#C8E6C9" stroke-width="0.75"/>
  <text x="260" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Derin Ekoloji</text>
  <text x="260" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Paradigmayı değiştir</text>
  <text x="260" y="70" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Tüketim çılgınlığını durdur</text>
  <text x="260" y="85" font-family="Noto Sans" font-size="8" fill="#1B5E20" text-anchor="middle">• Biyosfere saygı duy</text>
</svg>'''

    # S9 (indeks 8): Yaşama Saygı İlkesi (Schweitzer)
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#F1F8E9" stroke="#DCEDC8" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#33691E" text-anchor="middle">"Yaşama Saygı" Etiği (Albert Schweitzer)</text>
  <text x="180" y="60" font-family="Noto Sans" font-size="8" fill="#558B2F" text-anchor="middle">"Ben yaşamak isteyen başka yaşamlar arasında yaşamak isteyen bir yaşamım."</text>
  <line x1="60" y1="72" x2="300" y2="72" stroke="#AED581" stroke-width="0.75"/>
  <text x="180" y="90" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Etik İlke: Canı korumak iyi, cana zarar vermek kötüdür.</text>
</svg>'''

    # S11 (indeks 10): Ekolojik Bütüncülük Matrisi
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <rect x="45" y="30" width="120" height="40" rx="4" fill="#E8EAF6" stroke="#C5CAE9" stroke-width="0.75"/>
  <text x="105" y="55" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1A237E" text-anchor="middle">Bireyci Yaklaşım</text>
  <text x="105" y="65" font-family="Noto Sans" font-size="7" fill="#283593" text-anchor="middle">(Yalnız tekil organizma)</text>

  <rect x="195" y="30" width="120" height="40" rx="4" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="255" y="55" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Bütüncül Yaklaşım</text>
  <text x="255" y="65" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">(Toprak, su, türler ağı)</text>

  <text x="180" y="95" font-family="Noto Sans" font-size="8" fill="#616161" text-anchor="middle">Aldo Leopold: "Bir şey biyotik topluluğun bütünlüğünü koruyorsa doğrudur."</text>
</svg>'''
