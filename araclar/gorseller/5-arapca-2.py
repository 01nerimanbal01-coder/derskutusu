# -*- coding: utf-8 -*-
"""5. Sınıf Arapça — 2. Hafta (Selamlaşma-Tanışma Diyalogları ve İkinci Harf Grubu: د ذ ر ز س ش ص ض) Görselleri"""

GORSELLER = {
    "b1": '''<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="250" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">KARŞILAŞMA VE TANIŞMA DİYALOGLARINI DİNLEME ADIMLARI (الْمُقَابَلَة وَالتَّعَارُف)</text>
  <rect x="20" y="48" width="230" height="184" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <rect x="20" y="48" width="230" height="28" rx="8" fill="#2563eb"/>
  <text x="135" y="67" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">1. TAHMİN ET (خَمِّنْ)</text>
  <text x="32" y="96" font-size="11" fill="#1e3a8a">• Görseldeki kişilerin</text>
  <text x="40" y="112" font-size="11" fill="#1e3a8a">karşılaşıyor mu yoksa</text>
  <text x="40" y="128" font-size="11" fill="#1e3a8a">vedalaşıyor mu olduğuna bak.</text>
  <text x="32" y="152" font-size="11" fill="#1e3a8a">• Günün vaktini (sabah/akşam)</text>
  <text x="40" y="168" font-size="11" fill="#1e3a8a">ve hitap edilen kişiyi</text>
  <text x="40" y="184" font-size="11" font-weight="700" fill="#1d4ed8">(erkek: كَ / kadın: كِ) belirle.</text>

  <rect x="265" y="48" width="230" height="184" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
  <rect x="265" y="48" width="230" height="28" rx="8" fill="#059669"/>
  <text x="380" y="67" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">2. DİNLE VE DÜŞÜN (اِسْتَمِعْ)</text>
  <text x="277" y="96" font-size="11" fill="#065f46">• Selamlaşma: السَّلَامُ عَلَيْكُمْ</text>
  <text x="285" y="114" font-size="11" fill="#065f46">→ وَعَلَيْكُمُ السَّلَامُ</text>
  <text x="277" y="138" font-size="11" fill="#065f46">• Ad sorma: مَا اسْمُكَ؟ / مَا اسْمُكِ؟</text>
  <text x="285" y="156" font-size="11" fill="#065f46">→ اِسْمِي ...</text>
  <text x="277" y="180" font-size="11" fill="#065f46">• Memnuniyet: تَشَرَّفْتُ /</text>
  <text x="285" y="198" font-size="11" font-weight="700" fill="#047857">فُرْصَةٌ سَعِيدَةٌ</text>

  <rect x="510" y="48" width="230" height="184" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <rect x="510" y="48" width="230" height="28" rx="8" fill="#d97706"/>
  <text x="625" y="67" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">3. KARŞILIK VER (قُلِ الرَّدَّ)</text>
  <text x="522" y="96" font-size="11" fill="#78350f">• أَهْلًا وَسَهْلًا → أَهْلًا بِكَ / بِكِ</text>
  <text x="522" y="120" font-size="11" fill="#78350f">• صَبَاحُ الْخَيْرِ → صَبَاحُ النُّورِ</text>
  <text x="522" y="144" font-size="11" fill="#78350f">• كَيْفَ حَالُكَ؟ → بِخَيْرٍ، الْحَمْدُ لِلَّهِ</text>
  <text x="522" y="168" font-size="11" fill="#78350f">• شُكْرًا → عَفْوًا</text>
  <text x="522" y="192" font-size="11" font-weight="700" fill="#92400e">• إِلَى اللِّقَاءِ → مَعَ السَّلَامَةِ</text>
</svg>''',

    "b2": '''<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="240" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">KARŞILIKLI KONUŞMA KALIBI: ERKEK VE KADIN HİTABI (الْمُحَادَثَة ٢)</text>
  <rect x="24" y="48" width="340" height="174" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="194" y="72" text-anchor="middle" font-size="13" font-weight="800" fill="#1e3a8a">Erkek Öğrenci Diyaloğu (مُذَكَّر)</text>
  <text x="38" y="98" font-size="11.5" fill="#1e40af">• <tspan font-weight="700">أَحْمَد:</tspan> السَّلَامُ عَلَيْكُمْ، أَنَا أَحْمَد. مَا اسْمُكَ؟</text>
  <text x="38" y="122" font-size="11.5" fill="#1e40af">• <tspan font-weight="700">عَلِيّ:</tspan> وَعَلَيْكُمُ السَّلَامُ، اِسْمِي عَلِيّ. كَيْفَ حَالُكَ؟</text>
  <text x="38" y="146" font-size="11.5" fill="#1e40af">• <tspan font-weight="700">أَحْمَد:</tspan> بِخَيْرٍ، الْحَمْدُ لِلَّهِ. تَشَرَّفْتُ يَا عَلِيّ.</text>
  <text x="38" y="170" font-size="11.5" fill="#1e40af">• <tspan font-weight="700">عَلِيّ:</tspan> فُرْصَةٌ سَعِيدَةٌ، إِلَى اللِّقَاءِ.</text>
  <text x="38" y="198" font-size="11" font-weight="700" fill="#1d4ed8">İpucu: Erkeğe sorarken sonda üstünlü «ـكَ» kullanılır.</text>

  <rect x="396" y="48" width="340" height="174" rx="10" fill="#fce7f3" stroke="#db2777" stroke-width="2"/>
  <text x="566" y="72" text-anchor="middle" font-size="13" font-weight="800" fill="#9d174d">Kız Öğrenci Diyaloğu (مُؤَنَّث)</text>
  <text x="410" y="98" font-size="11.5" fill="#831843">• <tspan font-weight="700">زَيْنَب:</tspan> صَبَاحُ الْخَيْرِ، أَنَا زَيْنَب. مَا اسْمُكِ؟</text>
  <text x="410" y="122" font-size="11.5" fill="#831843">• <tspan font-weight="700">مَرْيَم:</tspan> صَبَاحُ النُّورِ، اِسْمِي مَرْيَم. كَيْفَ حَالُكِ؟</text>
  <text x="410" y="146" font-size="11.5" fill="#831843">• <tspan font-weight="700">زَيْنَب:</tspan> بِخَيْرٍ، وَأَنْتِ؟ أَهْلًا بِكِ يَا مَرْيَم.</text>
  <text x="410" y="170" font-size="11.5" fill="#831843">• <tspan font-weight="700">مَرْيَم:</tspan> شُكْرًا، مَعَ السَّلَامَةِ.</text>
  <text x="410" y="198" font-size="11" font-weight="700" fill="#be185d">İpucu: Kadına sorarken sonda esreli «ـكِ» kullanılır.</text>
</svg>''',

    "b3": '''<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="260" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">İKİNCİ HARF GRUBU: د ذ ر ز س ش ص ض (4 KARDEŞ ÇİFT)</text>
  <rect x="20" y="48" width="170" height="192" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <rect x="20" y="48" width="170" height="28" rx="8" fill="#2563eb"/>
  <text x="105" y="67" text-anchor="middle" font-size="13" font-weight="800" fill="#ffffff">1. د ve ذ ÇİFTİ</text>
  <text x="105" y="105" text-anchor="middle" font-size="26" font-weight="800" fill="#1e3a8a">د   /   ذ</text>
  <text x="30" y="138" font-size="10.5" fill="#1e3a8a">• <tspan font-weight="700">د (Dal):</tspan> Noktasızdır;</text>
  <text x="38" y="152" font-size="10.5" fill="#1e3a8a">ince "d" sesi verir.</text>
  <text x="30" y="174" font-size="10.5" fill="#1e3a8a">• <tspan font-weight="700">ذ (Zel):</tspan> Üstte 1 noktalıdır;</text>
  <text x="38" y="188" font-size="10.5" font-weight="700" fill="#1d4ed8">peltek ve ince "z" okunur.</text>
  <text x="30" y="216" font-size="10.5" fill="#1e3a8a">• Harekeli: دَ دُ دِ / ذَ ذُ ذِ</text>

  <rect x="203" y="48" width="170" height="192" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
  <rect x="203" y="48" width="170" height="28" rx="8" fill="#059669"/>
  <text x="288" y="67" text-anchor="middle" font-size="13" font-weight="800" fill="#ffffff">2. ر ve ز ÇİFTİ</text>
  <text x="288" y="105" text-anchor="middle" font-size="26" font-weight="800" fill="#065f46">ر   /   ز</text>
  <text x="213" y="138" font-size="10.5" fill="#065f46">• <tspan font-weight="700">ر (Ra):</tspan> Noktasızdır;</text>
  <text x="221" y="152" font-size="10.5" fill="#065f46">satır altına kavisle iner.</text>
  <text x="213" y="174" font-size="10.5" fill="#065f46">• <tspan font-weight="700">ز (Ze):</tspan> Üstte 1 noktalıdır;</text>
  <text x="221" y="188" font-size="10.5" font-weight="700" fill="#047857">keskin ve ince "z" okunur.</text>
  <text x="213" y="216" font-size="10.5" fill="#065f46">• Harekeli: رَ رُ رِ / زَ زُ زِ</text>

  <rect x="386" y="48" width="170" height="192" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <rect x="386" y="48" width="170" height="28" rx="8" fill="#d97706"/>
  <text x="471" y="67" text-anchor="middle" font-size="13" font-weight="800" fill="#ffffff">3. س ve ش ÇİFTİ</text>
  <text x="471" y="105" text-anchor="middle" font-size="26" font-weight="800" fill="#92400e">س   /   ش</text>
  <text x="396" y="138" font-size="10.5" fill="#78350f">• <tspan font-weight="700">س (Sin):</tspan> Üç dişlidir,</text>
  <text x="404" y="152" font-size="10.5" fill="#78350f">noktasızdır; ince "s" okunur.</text>
  <text x="396" y="174" font-size="10.5" fill="#78350f">• <tspan font-weight="700">ش (Şın):</tspan> Üstte 3 noktalıdır;</text>
  <text x="404" y="188" font-size="10.5" font-weight="700" fill="#b45309">"ş" sesi verir.</text>
  <text x="396" y="216" font-size="10.5" fill="#78350f">• Harekeli: سَ سُ سِ / شَ شُ شِ</text>

  <rect x="570" y="48" width="170" height="192" rx="10" fill="#f3e8ff" stroke="#a855f7" stroke-width="2"/>
  <rect x="570" y="48" width="170" height="28" rx="8" fill="#7c3aed"/>
  <text x="655" y="67" text-anchor="middle" font-size="13" font-weight="800" fill="#ffffff">4. ص ve ض ÇİFTİ</text>
  <text x="655" y="105" text-anchor="middle" font-size="26" font-weight="800" fill="#581c87">ص   /   ض</text>
  <text x="580" y="138" font-size="10.5" fill="#581c87">• <tspan font-weight="700">ص (Sad):</tspan> Noktasızdır;</text>
  <text x="588" y="152" font-size="10.5" font-weight="700" fill="#6b21a8">kalın "s" sesiyle okunur.</text>
  <text x="580" y="174" font-size="10.5" fill="#581c87">• <tspan font-weight="700">ض (Dad):</tspan> Üstte 1 noktalıdır;</text>
  <text x="588" y="188" font-size="10.5" font-weight="700" fill="#6b21a8">kalın "d-z" arası okunur.</text>
  <text x="580" y="216" font-size="10.5" fill="#581c87">• Harekeli: صَ صُ صِ / ضَ ضُ ضِ</text>
</svg>''',

    "b4": '''<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="240" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">HAREKELERİNE GÖRE HARFLERİ GRUPLAMA (الْمَفْتُوحَة / الْمَضْمُومَة / الْمَكْسُورَة)</text>
  <rect x="20" y="48" width="230" height="174" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-size="12.5" font-weight="800" fill="#166534">1. Fethalı (Üstünlü - الْمَفْتُوحَة)</text>
  <text x="135" y="108" text-anchor="middle" font-size="20" font-weight="800" fill="#14532d">دَ  ذَ  رَ  زَ  سَ  شَ  صَ  ضَ</text>
  <text x="34" y="142" font-size="10.5" fill="#15803d">• İşaret harfin <tspan font-weight="700">üstünde</tspan> eğik çizgidir.</text>
  <text x="34" y="162" font-size="10.5" fill="#15803d">• İnce harfleri <tspan font-weight="700">«-e»</tspan> (دَ، ذَ، زَ، سَ، شَ),</text>
  <text x="42" y="178" font-size="10.5" fill="#15803d">kalın harfleri <tspan font-weight="700">«-a»</tspan> (رَ، صَ، ضَ) okutur.</text>

  <rect x="265" y="48" width="230" height="174" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="380" y="72" text-anchor="middle" font-size="12.5" font-weight="800" fill="#1e3a8a">2. Dammalı (Ötreli - الْمَضْمُومَة)</text>
  <text x="380" y="108" text-anchor="middle" font-size="20" font-weight="800" fill="#1e3a8a">دُ  ذُ  رُ  زُ  سُ  شُ  صُ  ضُ</text>
  <text x="279" y="142" font-size="10.5" fill="#1e40af">• İşaret harfin <tspan font-weight="700">üstünde</tspan> vav benzeridir.</text>
  <text x="279" y="162" font-size="10.5" fill="#1e40af">• İnce harfleri <tspan font-weight="700">«-ü / -u»</tspan>,</text>
  <text x="287" y="178" font-size="10.5" fill="#1e40af">kalın harfleri tok <tspan font-weight="700">«-u»</tspan> sesiyle okutur.</text>

  <rect x="510" y="48" width="230" height="174" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="625" y="72" text-anchor="middle" font-size="12.5" font-weight="800" fill="#92400e">3. Kesralı (Esreli - الْمَكْسُورَة)</text>
  <text x="625" y="108" text-anchor="middle" font-size="20" font-weight="800" fill="#78350f">دِ  ذِ  رِ  زِ  سِ  شِ  صِ  ضِ</text>
  <text x="524" y="142" font-size="10.5" fill="#78350f">• İşaret harfin <tspan font-weight="700">altında</tspan> eğik çizgidir.</text>
  <text x="524" y="162" font-size="10.5" fill="#78350f">• İnce harfleri <tspan font-weight="700">«-i»</tspan> (دِ، ذِ، رِ، زِ، سِ، شِ),</text>
  <text x="532" y="178" font-size="10.5" fill="#78350f">kalın harfleri <tspan font-weight="700">«-ı / -i»</tspan> (صِ، ضِ) okutur.</text>
</svg>''',

    "b5": '''<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="250" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">SOLA BİRLEŞMEYEN HARFLER VE ÜÇ HARFLİ KELİMELER (Etkinlik 10–11)</text>
  <rect x="20" y="48" width="350" height="184" rx="10" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
  <rect x="20" y="48" width="350" height="28" rx="8" fill="#dc2626"/>
  <text x="195" y="67" text-anchor="middle" font-size="12.5" font-weight="800" fill="#ffffff">SOLA BİRLEŞMEYEN HARFLERLE KELİMELER</text>
  <text x="34" y="96" font-size="11" fill="#7f1d1d">• <tspan font-weight="700">ا، د، ذ، ر، ز</tspan> harfleri kendinden sonra gelen</text>
  <text x="42" y="112" font-size="11" fill="#7f1d1d">(soldaki) harfle birleşmez; ayrı durur:</text>
  <text x="195" y="148" text-anchor="middle" font-size="19" font-weight="800" fill="#991b1b">دَرَسَ  •  دَرَجَ  •  أَدُبَ  •  زَرَعَ</text>
  <text x="195" y="182" text-anchor="middle" font-size="19" font-weight="800" fill="#991b1b">رَأَسَ  •  ذَرَأَ  •  رَدِفَ  •  دَرِبَ</text>
  <text x="195" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="#7f1d1d">Sağdan sola harf harf seslendir: دَ + رَ + سَ = دَرَسَ</text>

  <rect x="390" y="48" width="350" height="184" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
  <rect x="390" y="48" width="350" height="28" rx="8" fill="#2563eb"/>
  <text x="565" y="67" text-anchor="middle" font-size="12.5" font-weight="800" fill="#ffffff">BİRLEŞEN HARFLERLE KELİMELER</text>
  <text x="404" y="96" font-size="11" fill="#1e3a8a">• <tspan font-weight="700">ب، ت، ث، ج، ح، خ، س، ش، ص، ض</tspan> harfleri</text>
  <text x="412" y="112" font-size="11" fill="#1e3a8a">başta ve ortada kuyruk kısmını bırakıp birleşir:</text>
  <text x="565" y="148" text-anchor="middle" font-size="19" font-weight="800" fill="#1e3a8a">شَرِبَ  •  شَرَحَ  •  صَبَرَ  •  خَرَجَ</text>
  <text x="565" y="182" text-anchor="middle" font-size="19" font-weight="800" fill="#1e3a8a">حَرِجَ  •  رَبِحَ  •  بَرَدَ  •  جَبَرَ</text>
  <text x="565" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="#1d4ed8">Örnek: شَ + رِ + بَ → شَرِبَ  |  صَ + بَ + رَ → صَبَرَ</text>
</svg>''',

    "b6": '''<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;display:block;margin:14px auto;font-family:system-ui,-apple-system,sans-serif;">
  <rect width="760" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="380" y="28" text-anchor="middle" font-size="15" font-weight="800" fill="#1e293b">YAZMA KURALLARI (الْكِتَابَة ٢) VE ÜNİTENİN VECİZ SÖZÜ</text>
  <rect x="20" y="48" width="440" height="164" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
  <text x="240" y="72" text-anchor="middle" font-size="13" font-weight="800" fill="#065f46">Satır Çizgisine Göre Yazılış (Kitap s. 38–39)</text>
  <text x="34" y="100" font-size="11" fill="#064e3b">• <tspan font-weight="700">د ve ذ:</tspan> Yukarıdan aşağı eğik inip satır çizgisi üstünde sola döner.</text>
  <text x="34" y="124" font-size="11" fill="#064e3b">• <tspan font-weight="700">ر ve ز:</tspan> Satır üstünden başlayıp kavis çizerek <tspan font-weight="700">satır altına</tspan> iner.</text>
  <text x="34" y="148" font-size="11" fill="#064e3b">• <tspan font-weight="700">س ve ش:</tspan> Sağdan sola 3 küçük diş satır üstünde, geniş çanak satır altında.</text>
  <text x="34" y="172" font-size="11" fill="#064e3b">• <tspan font-weight="700">ص ve ض:</tspan> Kapalı damla halkası satır üstünde, çanak kısmı satır altında.</text>
  <text x="34" y="196" font-size="11" font-weight="700" fill="#047857">• Önce gövde çizilir, ardından nokta ve en son hareke konur.</text>

  <rect x="480" y="48" width="260" height="164" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <text x="610" y="76" text-anchor="middle" font-size="13" font-weight="800" fill="#92400e">Ünitenin Veciz Sözü</text>
  <text x="610" y="120" text-anchor="middle" font-size="22" font-weight="800" fill="#78350f">اَلسَّلَامُ قَبْلَ الْكَلَامِ</text>
  <text x="610" y="156" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">«Selam, kelamdan (sözden)</text>
  <text x="610" y="174" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">öncedir.»</text>
  <text x="610" y="198" text-anchor="middle" font-size="10.5" fill="#78350f">Konuşmaya başlamadan önce selam verilir.</text>
</svg>'''
}
