# -*- coding: utf-8 -*-
"""11-kimya-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Bağ Enerjisi ve Entalpi Özeti
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <defs>
    <linearGradient id="ki1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
    <linearGradient id="ki2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E1F5FE"/><stop offset="100%" stop-color="#B3E5FC"/>
    </linearGradient>
    <linearGradient id="ki3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="95" height="95" rx="6" fill="url(#ki1)" stroke="#81C784" stroke-width="0.75"/>
  <text x="62" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">Bağ Kırılması</text>
  <text x="62" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Endotermik</text>
  <text x="62" y="75" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#2E7D32" text-anchor="middle">ΔH &gt; 0</text>
  <text x="62" y="92" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">Isı Alınır</text>

  <rect x="132" y="15" width="95" height="95" rx="6" fill="url(#ki2)" stroke="#4FC3F7" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">Bağ Oluşumu</text>
  <text x="180" y="60" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Ekzotermik</text>
  <text x="180" y="75" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#0277BD" text-anchor="middle">ΔH &lt; 0</text>
  <text x="180" y="92" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">Isı Salınır</text>

  <rect x="250" y="15" width="95" height="95" rx="6" fill="url(#ki3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="297" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">Tepkime ΔH</text>
  <text x="297" y="58" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Σ Kırılan Bağ</text>
  <text x="297" y="72" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">- Σ Oluşan Bağ</text>
  <text x="297" y="90" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">(Gaz Fazı)</text>
</svg>'''

    # S2 (indeks 1): Bağ Enerjisi Formülü Şeması
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#37474F" text-anchor="middle">Bağ Enerjileriyle Tepkime Entalpisi Hesabı</text>
  <rect x="50" y="48" width="260" height="42" rx="4" fill="#E8F5E9" stroke="#81C784" stroke-width="0.75"/>
  <text x="180" y="73" font-family="Noto Sans" font-size="11" font-weight="bold" fill="#1B5E20" text-anchor="middle">ΔH = Σ BE(Kırılan Bağlar) - Σ BE(Oluşan Bağlar)</text>
  <text x="180" y="102" font-family="Noto Sans" font-size="7" fill="#616161" text-anchor="middle">* Yalnızca gaz fazında yer alan türler için uygulanır.</text>
</svg>'''

    # S3 (indeks 2): Standart Oluşum Entalpisi Sıfır Olan Elementler
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="145" height="95" rx="6" fill="#E8F5E9" stroke="#81C784" stroke-width="0.75"/>
  <text x="97" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">ΔH°_f = 0 (Kararlı Hal)</text>
  <text x="97" y="55" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• O₂(g) [Oksijen gazı]</text>
  <text x="97" y="70" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• C(k, grafit) [Grafit]</text>
  <text x="97" y="85" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• Fe(k) [Demir metali]</text>
  <text x="97" y="100" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">• N₂(g) [Azot gazı]</text>

  <rect x="190" y="15" width="145" height="95" rx="6" fill="#FFEBEE" stroke="#E57373" stroke-width="0.75"/>
  <text x="262" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">ΔH°_f ≠ 0 (Kararsız Hal)</text>
  <text x="262" y="55" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• O₃(g) [Ozon gazı]</text>
  <text x="262" y="70" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• C(k, elmas) [Elmas]</text>
  <text x="262" y="85" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• Fe(s) [Sıvı demir]</text>
  <text x="262" y="100" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">• O(g) [Monoatomik gaz]</text>
</svg>'''

    # S4 (indeks 3): Potansiyel Enerji Diyagramı
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <!-- Eksenler -->
  <line x1="50" y1="105" x2="310" y2="105" stroke="#424242" stroke-width="1"/>
  <line x1="50" y1="105" x2="50" y2="20" stroke="#424242" stroke-width="1"/>
  <text x="315" y="108" font-family="Noto Sans" font-size="7" fill="#424242">Tepkime İlerlemesi</text>
  <text x="45" y="18" font-family="Noto Sans" font-size="7" fill="#424242" text-anchor="end">PE (kJ)</text>

  <!-- Ekzotermik Eğri -->
  <line x1="50" y1="50" x2="110" y2="50" stroke="#1976D2" stroke-width="2"/>
  <text x="80" y="44" font-family="Noto Sans" font-size="7" fill="#0D47A1">Girenler</text>

  <path d="M 110 50 Q 150 25 180 50 Q 210 75 250 85" stroke="#D32F2F" stroke-width="1.5" fill="none"/>

  <line x1="250" y1="85" x2="300" y2="85" stroke="#388E3C" stroke-width="2"/>
  <text x="275" y="79" font-family="Noto Sans" font-size="7" fill="#1B5E20">Ürünler</text>

  <!-- ΔH Oku -->
  <line x1="220" y1="50" x2="220" y2="85" stroke="#D84315" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="235" y="70" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#D84315">ΔH &lt; 0</text>
</svg>'''

    # S6 (indeks 5): Yanma ve Oluşum Karşılaştırması
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="145" height="95" rx="6" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="0.75"/>
  <text x="97" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">Molar Oluşum</text>
  <text x="97" y="58" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">1 mol bileşik</text>
  <text x="97" y="72" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Kararlı elementlerden</text>
  <text x="97" y="90" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">25 °C ve 1 atm</text>

  <rect x="190" y="15" width="145" height="95" rx="6" fill="#FBE9E7" stroke="#FFCCBC" stroke-width="0.75"/>
  <text x="262" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#D84315" text-anchor="middle">Molar Yanma</text>
  <text x="262" y="58" font-family="Noto Sans" font-size="8" fill="#E64A19" text-anchor="middle">1 mol yakıtın</text>
  <text x="262" y="72" font-family="Noto Sans" font-size="8" fill="#E64A19" text-anchor="middle">O₂ ile tam tepkimesi</text>
  <text x="262" y="90" font-family="Noto Sans" font-size="7" fill="#D84315" text-anchor="middle">Daima ekzotermik (N₂ hariç)</text>
</svg>'''

    # S7 (indeks 6): N2 Üçlü Bağ Gücü
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="30" y="15" width="300" height="95" rx="8" fill="#EDE7F6" stroke="#D1C4E9" stroke-width="0.75"/>
  <circle cx="100" cy="62" r="24" fill="#7E57C2" stroke="#512DA8" stroke-width="0.75"/>
  <text x="100" y="67" font-family="Noto Sans" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">N</text>

  <!-- Üçlü Kovalent Bağ Çizgileri -->
  <line x1="126" y1="54" x2="174" y2="54" stroke="#D32F2F" stroke-width="2"/>
  <line x1="126" y1="62" x2="174" y2="62" stroke="#D32F2F" stroke-width="2"/>
  <line x1="126" y1="70" x2="174" y2="70" stroke="#D32F2F" stroke-width="2"/>

  <circle cx="200" cy="62" r="24" fill="#7E57C2" stroke="#512DA8" stroke-width="0.75"/>
  <text x="200" y="67" font-family="Noto Sans" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">N</text>

  <rect x="235" y="35" width="85" height="55" rx="4" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="277" y="52" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#311B92" text-anchor="middle">Bağ Enerjisi</text>
  <text x="277" y="68" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#C62828" text-anchor="middle">946 kJ/mol</text>
  <text x="277" y="82" font-family="Noto Sans" font-size="7" fill="#4527A0" text-anchor="middle">Yüksek Asallık</text>
</svg>'''

    # S9 (indeks 8): Kovalent Bağ Sayısı vs Enerji
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="25" y="15" width="95" height="95" rx="6" fill="#E8F5E9" stroke="#A5D6A7" stroke-width="0.75"/>
  <text x="72" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">C - C Tekli</text>
  <text x="72" y="58" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Bağ boyu: Uzun</text>
  <text x="72" y="74" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Enerji: ~347 kJ</text>
  <text x="72" y="90" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">En esnek bağ</text>

  <rect x="132" y="15" width="95" height="95" rx="6" fill="#FFF3E0" stroke="#FFCC80" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">C = C İkili</text>
  <text x="180" y="58" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Bağ boyu: Orta</text>
  <text x="180" y="74" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Enerji: ~614 kJ</text>
  <text x="180" y="90" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Daha güçlü</text>

  <rect x="240" y="15" width="95" height="95" rx="6" fill="#FFEBEE" stroke="#EF9A9A" stroke-width="0.75"/>
  <text x="287" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#B71C1C" text-anchor="middle">C ≡ C Üçlü</text>
  <text x="287" y="58" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">Bağ boyu: En kısa</text>
  <text x="287" y="74" font-family="Noto Sans" font-size="8" fill="#C62828" text-anchor="middle">Enerji: ~839 kJ</text>
  <text x="287" y="90" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">En sağlam bağ</text>
</svg>'''

    # S11 (indeks 10): Hess Yasası Basamakları
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:24mm">
  <rect x="35" y="15" width="290" height="95" rx="8" fill="#F5F5F5" stroke="#E0E0E0" stroke-width="0.75"/>
  <rect x="50" y="28" width="260" height="22" rx="3" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.5"/>
  <text x="180" y="42" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">1. Basamak: C(k) + 0,5 O₂(g) → CO(g)  [ΔH₁ = -110 kJ]</text>

  <rect x="50" y="54" width="260" height="22" rx="3" fill="#E1F5FE" stroke="#81D4FA" stroke-width="0.5"/>
  <text x="180" y="68" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">2. Basamak: CO(g) + 0,5 O₂(g) → CO₂(g)  [ΔH₂ = -283 kJ]</text>

  <rect x="50" y="80" width="260" height="22" rx="3" fill="#E8F5E9" stroke="#81C784" stroke-width="0.5"/>
  <text x="180" y="94" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">Net: C(k) + O₂(g) → CO₂(g)  [ΔH = -393 kJ]</text>
</svg>'''
