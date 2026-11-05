# -*- coding: utf-8 -*-
"""11-ingilizce-5 Görsel Modülü"""

def uygula(o):
    s = o["sorular"]
    # S1 (indeks 0): Used to vs Would Şeması
    s[0]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <defs>
    <linearGradient id="in1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E1F5FE"/><stop offset="100%" stop-color="#B3E5FC"/>
    </linearGradient>
    <linearGradient id="in2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8F5E9"/><stop offset="100%" stop-color="#C8E6C9"/>
    </linearGradient>
    <linearGradient id="in3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0"/><stop offset="100%" stop-color="#FFE0B2"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="95" height="95" rx="6" fill="url(#in1)" stroke="#4FC3F7" stroke-width="0.75"/>
  <text x="62" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">USED TO + V1</text>
  <text x="62" y="58" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Past Actions &amp;</text>
  <text x="62" y="72" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">Stative Verbs</text>
  <text x="62" y="90" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">(have, be, like)</text>

  <rect x="132" y="15" width="95" height="95" rx="6" fill="url(#in2)" stroke="#81C784" stroke-width="0.75"/>
  <text x="180" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">WOULD + V1</text>
  <text x="180" y="58" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Repeated Actions</text>
  <text x="180" y="72" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">ONLY (Habits)</text>
  <text x="180" y="90" font-family="Noto Sans" font-size="7" fill="#B71C1C" text-anchor="middle">NO stative verbs</text>

  <rect x="250" y="15" width="95" height="95" rx="6" fill="url(#in3)" stroke="#FFB74D" stroke-width="0.75"/>
  <text x="297" y="38" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#E65100" text-anchor="middle">FLYING COLOURS</text>
  <text x="297" y="58" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Idiom for High</text>
  <text x="297" y="72" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">Distinction &amp;</text>
  <text x="297" y="90" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Great Success</text>
</svg>'''

    # S2 (indeks 1): Stative Verb Kuralı
    s[1]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="25" y="15" width="310" height="95" rx="8" fill="#FAFAFA" stroke="#E0E0E0" stroke-width="0.75"/>
  <text x="180" y="35" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#37474F" text-anchor="middle">Grammar Rule: Stative Verbs in Past Habits</text>

  <rect x="40" y="48" width="130" height="48" rx="4" fill="#E8F5E9" stroke="#81C784" stroke-width="0.75"/>
  <text x="105" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#1B5E20" text-anchor="middle">CORRECT (Used to)</text>
  <text x="105" y="82" font-family="Noto Sans" font-size="7" fill="#2E7D32" text-anchor="middle">Steven used to have an 8mm camera.</text>

  <rect x="190" y="48" width="130" height="48" rx="4" fill="#FFEBEE" stroke="#E57373" stroke-width="0.75"/>
  <text x="255" y="66" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#B71C1C" text-anchor="middle">INCORRECT (Would)</text>
  <text x="255" y="82" font-family="Noto Sans" font-size="7" fill="#C62828" text-anchor="middle">Steven would have an 8mm camera.</text>
</svg>'''

    # S3 (indeks 2): Hobby to Profession Yolculuğu
    s[2]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="20" y="15" width="95" height="95" rx="6" fill="#FFF9C4" stroke="#FFF176" stroke-width="0.75"/>
  <text x="67" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#F57F17" text-anchor="middle">Teenage Hobby</text>
  <text x="67" y="58" font-family="Noto Sans" font-size="8" fill="#F57F17" text-anchor="middle">Boy Scout films</text>
  <text x="67" y="72" font-family="Noto Sans" font-size="8" fill="#F57F17" text-anchor="middle">Family vacations</text>
  <text x="67" y="88" font-family="Noto Sans" font-size="7" fill="#E65100" text-anchor="middle">Passion &amp; practice</text>

  <!-- Ok 1 -->
  <path d="M 125 62 L 145 62" stroke="#F57F17" stroke-width="1.5"/>

  <rect x="150" y="15" width="95" height="95" rx="6" fill="#E0F7FA" stroke="#80DEEA" stroke-width="0.75"/>
  <text x="197" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#00838F" text-anchor="middle">Persistence</text>
  <text x="197" y="58" font-family="Noto Sans" font-size="8" fill="#00838F" text-anchor="middle">Universal Studio</text>
  <text x="197" y="72" font-family="Noto Sans" font-size="8" fill="#00838F" text-anchor="middle">Amblin' short film</text>
  <text x="197" y="88" font-family="Noto Sans" font-size="7" fill="#006064" text-anchor="middle">First contract</text>

  <!-- Ok 2 -->
  <path d="M 255 62 L 275 62" stroke="#00838F" stroke-width="1.5"/>

  <rect x="280" y="15" width="70" height="95" rx="6" fill="#EDE7F6" stroke="#B39DDB" stroke-width="0.75"/>
  <text x="315" y="38" font-family="Noto Sans" font-size="8" font-weight="bold" fill="#4A148C" text-anchor="middle">Profession</text>
  <text x="315" y="58" font-family="Noto Sans" font-size="7" fill="#4A148C" text-anchor="middle">Jaws, E.T.</text>
  <text x="315" y="72" font-family="Noto Sans" font-size="7" fill="#4A148C" text-anchor="middle">Jurassic Park</text>
  <text x="315" y="88" font-family="Noto Sans" font-size="7" fill="#311B92" text-anchor="middle">Oscar Icon</text>
</svg>'''

    # S4 (indeks 3): Film Kamerası İllüstrasyonu
    s[3]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <!-- Klasik Film Kamerası -->
  <rect x="130" y="45" width="70" height="50" rx="5" fill="#455A64" stroke="#263238" stroke-width="1"/>
  <!-- Film Makaraları -->
  <circle cx="145" cy="30" r="15" fill="#78909C" stroke="#37474F" stroke-width="0.75"/>
  <circle cx="185" cy="30" r="15" fill="#78909C" stroke="#37474F" stroke-width="0.75"/>
  <circle cx="145" cy="30" r="4" fill="#ECEFF1"/>
  <circle cx="185" cy="30" r="4" fill="#ECEFF1"/>

  <!-- Mercek -->
  <polygon points="200,60 230,45 230,85 200,70" fill="#90A4AE" stroke="#37474F" stroke-width="0.75"/>

  <!-- Işık Işınları -->
  <path d="M 235 50 L 320 25 M 235 80 L 320 105" stroke="#FFE082" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="280" y="68" font-family="Noto Sans" font-size="10" font-weight="bold" fill="#F57F17">CINEMA</text>
</svg>'''

    # S6 (indeks 5): Prefer vs Would Rather Yapıları
    s[5]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="25" y="15" width="145" height="95" rx="6" fill="#E8EAF6" stroke="#C5CAE9" stroke-width="0.75"/>
  <text x="97" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1A237E" text-anchor="middle">PREFER + V-ing TO V-ing</text>
  <text x="97" y="60" font-family="Noto Sans" font-size="8" fill="#283593" text-anchor="middle">I prefer directing</text>
  <text x="97" y="74" font-family="Noto Sans" font-size="8" fill="#283593" text-anchor="middle">to acting.</text>
  <text x="97" y="92" font-family="Noto Sans" font-size="7" fill="#3949AB" text-anchor="middle">(General preference)</text>

  <rect x="190" y="15" width="145" height="95" rx="6" fill="#F3E5F5" stroke="#E1BEE7" stroke-width="0.75"/>
  <text x="262" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#4A148C" text-anchor="middle">WOULD RATHER + V1 THAN V1</text>
  <text x="262" y="60" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">I would rather film</text>
  <text x="262" y="74" font-family="Noto Sans" font-size="8" fill="#6A1B9A" text-anchor="middle">than edit today.</text>
  <text x="262" y="92" font-family="Noto Sans" font-size="7" fill="#7B1FA2" text-anchor="middle">(Specific preference)</text>
</svg>'''

    # S7 (indeks 6): Could vs Was Able To
    s[6]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="30" y="15" width="140" height="95" rx="6" fill="#F1F8E9" stroke="#DCEDC8" stroke-width="0.75"/>
  <text x="100" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#33691E" text-anchor="middle">COULD (General)</text>
  <text x="100" y="60" font-family="Noto Sans" font-size="8" fill="#558B2F" text-anchor="middle">General past ability</text>
  <text x="100" y="75" font-family="Noto Sans" font-size="8" fill="#558B2F" text-anchor="middle">over a long period</text>
  <text x="100" y="92" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">"He could run fast."</text>

  <rect x="190" y="15" width="140" height="95" rx="6" fill="#E1F5FE" stroke="#B3E5FC" stroke-width="0.75"/>
  <text x="260" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#01579B" text-anchor="middle">WAS ABLE TO (Single)</text>
  <text x="260" y="60" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">One-time success</text>
  <text x="260" y="75" font-family="Noto Sans" font-size="8" fill="#0277BD" text-anchor="middle">in a difficult spot</text>
  <text x="260" y="92" font-family="Noto Sans" font-size="7" fill="#01579B" text-anchor="middle">"They were able to escape."</text>
</svg>'''

    # S9 (indeks 8): Be vs Get Used To
    s[8]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="35" y="15" width="135" height="95" rx="6" fill="#FFF3E0" stroke="#FFE0B2" stroke-width="0.75"/>
  <text x="102" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#E65100" text-anchor="middle">GET USED TO</text>
  <text x="102" y="60" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">The ongoing process</text>
  <text x="102" y="75" font-family="Noto Sans" font-size="8" fill="#EF6C00" text-anchor="middle">of adaptation</text>
  <text x="102" y="92" font-family="Noto Sans" font-size="7" fill="#BF360C" text-anchor="middle">"I am getting used to it."</text>

  <rect x="190" y="15" width="135" height="95" rx="6" fill="#E8F5E9" stroke="#C8E6C9" stroke-width="0.75"/>
  <text x="257" y="38" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#1B5E20" text-anchor="middle">BE USED TO</text>
  <text x="257" y="60" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">Fully accustomed</text>
  <text x="257" y="75" font-family="Noto Sans" font-size="8" fill="#2E7D32" text-anchor="middle">and comfortable</text>
  <text x="257" y="92" font-family="Noto Sans" font-size="7" fill="#1B5E20" text-anchor="middle">"She is used to noise."</text>
</svg>'''

    # S11 (indeks 10): Film Klaketi İkonu
    s[10]["gorsel"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 125" style="max-height:34mm">
  <rect x="40" y="15" width="280" height="95" rx="8" fill="#263238" stroke="#37474F" stroke-width="1"/>
  <!-- Klaket Çizgileri -->
  <rect x="50" y="22" width="260" height="20" fill="#37474F"/>
  <polygon points="60,22 75,22 90,42 75,42" fill="#ECEFF1"/>
  <polygon points="105,22 120,22 135,42 120,42" fill="#ECEFF1"/>
  <polygon points="150,22 165,22 180,42 165,42" fill="#ECEFF1"/>
  <polygon points="195,22 210,22 225,42 210,42" fill="#ECEFF1"/>
  <polygon points="240,22 255,22 270,42 255,42" fill="#ECEFF1"/>

  <!-- Klaket Yazıları -->
  <text x="65" y="65" font-family="Noto Sans" font-size="9" font-weight="bold" fill="#ECEFF1">PROD: HOLLYWOOD</text>
  <text x="65" y="82" font-family="Noto Sans" font-size="8" fill="#B0BEC5">SCENE: 24</text>
  <text x="150" y="82" font-family="Noto Sans" font-size="8" fill="#B0BEC5">TAKE: 03</text>
  <text x="230" y="82" font-family="Noto Sans" font-size="8" fill="#B0BEC5">ROLL: A1</text>
  <text x="65" y="98" font-family="Noto Sans" font-size="8" fill="#81D4FA">DIRECTOR: S. SPIELBERG</text>
</svg>'''
