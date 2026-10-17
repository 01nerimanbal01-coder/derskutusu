# -*- coding: utf-8 -*-
"""9. Sınıf Biyoloji — 3. Hafta Görselleri (Bilimsel Araştırma Süreçlerinde Bilimin Doğası)"""

GORSELLER = {
    "b1": '''<svg viewBox="0 0 660 270" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="270" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#059669"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMİN DOĞASININ TEMEL ÖZELLİKLERİ (GENEL BAKIŞ)</text>

  <g transform="translate(18,62)">
    <rect width="198" height="90" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#065f46" font-size="12" font-weight="800">1. KANITA DAYALILIK</text>
    <text x="99" y="48" text-anchor="middle" fill="#064e3b" font-size="11">Deneysel veriler ve</text>
    <text x="99" y="66" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">doğrudan/dolaylı gözlemler</text>
  </g>

  <g transform="translate(231,62)">
    <rect width="198" height="90" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#1e40af" font-size="12" font-weight="800">2. DEĞİŞEBİLİRLİK</text>
    <text x="99" y="48" text-anchor="middle" fill="#1e3a8a" font-size="11">Mutlak doğru değildir;</text>
    <text x="99" y="66" text-anchor="middle" fill="#1d4ed8" font-size="11" font-weight="700">yeni kanıtlarla güncellenir</text>
  </g>

  <g transform="translate(444,62)">
    <rect width="198" height="90" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#92400e" font-size="12" font-weight="800">3. GÖZLEM VE ÇIKARIM</text>
    <text x="99" y="48" text-anchor="middle" fill="#78350f" font-size="11">Duyu/ölçüm verisi (gözlem)</text>
    <text x="99" y="66" text-anchor="middle" fill="#b45309" font-size="11" font-weight="700">ve bunun yorumu (çıkarım)</text>
  </g>

  <g transform="translate(18,164)">
    <rect width="304" height="90" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="152" y="24" text-anchor="middle" fill="#5b21b6" font-size="12" font-weight="800">4. HAYAL GÜCÜ, YARATICILIK VE ÖZNELLİK</text>
    <text x="152" y="48" text-anchor="middle" fill="#4c1d95" font-size="11">Deney tasarımı ve veri yorumlamada bilim insanının</text>
    <text x="152" y="66" text-anchor="middle" fill="#6d28d9" font-size="11" font-weight="700">birikimi, yaratıcılığı ve bakış açısı etkilidir.</text>
  </g>

  <g transform="translate(338,164)">
    <rect width="304" height="90" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="1.5"/>
    <text x="152" y="24" text-anchor="middle" fill="#9d174d" font-size="12" font-weight="800">5. SOSYAL VE KÜLTÜREL ETKİLEŞİM</text>
    <text x="152" y="48" text-anchor="middle" fill="#831843" font-size="11">Bilim, içinde geliştiği toplumun ihtiyaçlarından,</text>
    <text x="152" y="66" text-anchor="middle" fill="#be185d" font-size="11" font-weight="700">kültüründen ve teknolojik düzeyinden etkilenir.</text>
  </g>
</svg>''',

    "b2": '''<svg viewBox="0 0 660 265" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="265" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#1d4ed8"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMSEL SÜREÇTE GÖZLEM (NİTEL / NİCEL) VE ÇIKARIM FARKI</text>

  <g transform="translate(18,62)">
    <rect width="304" height="188" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#1e40af" font-size="13" font-weight="800">GÖZLEM (OBSERVATION)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="152" y="58" text-anchor="middle" fill="#1e3a8a" font-size="11.5">Duyu organları veya ölçüm araçlarıyla</text>
    <text x="152" y="76" text-anchor="middle" fill="#1e3a8a" font-size="11.5">doğrudan toplanan verilerdir.</text>
    <text x="152" y="104" text-anchor="middle" fill="#1d4ed8" font-size="11.5" font-weight="700">• Nitel Gözlem (Ölçüm aletsiz):</text>
    <text x="152" y="122" text-anchor="middle" fill="#334155" font-size="11">"Bitkinin yaprakları sararmış ve toprağı kuru."</text>
    <text x="152" y="148" text-anchor="middle" fill="#1d4ed8" font-size="11.5" font-weight="700">• Nicel Gözlem (Ölçüm aletli / Sayısal):</text>
    <text x="152" y="166" text-anchor="middle" fill="#334155" font-size="11">"Bitkinin boyu 18 cm, ortam sıcaklığı 32 °C."</text>
  </g>

  <g transform="translate(338,62)">
    <rect width="304" height="188" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#92400e" font-size="13" font-weight="800">ÇIKARIM (INFERENCE)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#fcd34d" stroke-width="1.2"/>
    <text x="152" y="58" text-anchor="middle" fill="#78350f" font-size="11.5">Yapılan gözlemlerin önceki bilgilerle</text>
    <text x="152" y="76" text-anchor="middle" fill="#78350f" font-size="11.5">birleştirilerek yorumlanması ve açıklanmasıdır.</text>
    <text x="152" y="106" text-anchor="middle" fill="#b45309" font-size="11.5" font-weight="700">• Örnek Çıkarım 1:</text>
    <text x="152" y="124" text-anchor="middle" fill="#334155" font-size="11">"Bitki uzun süre sulanmadığı için yaprakları solmuş."</text>
    <text x="152" y="150" text-anchor="middle" fill="#b45309" font-size="11.5" font-weight="700">• Örnek Çıkarım 2:</text>
    <text x="152" y="168" text-anchor="middle" fill="#334155" font-size="11">"Azot eksikliği klorofil sentezini yavaşlatmıştır."</text>
  </g>
</svg>''',

    "b3": '''<svg viewBox="0 0 660 270" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="270" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#6d28d9"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMSEL TEORİ (KURAM) VE BİLİMSEL KANUN (YASA) KARŞILAŞTIRMASI</text>

  <g transform="translate(18,62)">
    <rect width="304" height="192" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#5b21b6" font-size="13" font-weight="800">BİLİMSEL TEORİ (KURAM)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#c4b5fd" stroke-width="1.2"/>
    <text x="152" y="58" text-anchor="middle" fill="#4c1d95" font-size="11.5" font-weight="700">Soru: Doğa olayı "NEDEN" gerçekleşir?</text>
    <text x="152" y="82" text-anchor="middle" fill="#4c1d95" font-size="11">• Çok sayıda deney, gözlem ve kanıtla desteklenen</text>
    <text x="152" y="100" text-anchor="middle" fill="#4c1d95" font-size="11">kapsamlı bilimsel açıklamalardır.</text>
    <text x="152" y="122" text-anchor="middle" fill="#4c1d95" font-size="11">• Basit bir tahmin değildir; güçlü delillere dayanır.</text>
    <text x="152" y="146" text-anchor="middle" fill="#6d28d9" font-size="11" font-weight="700">Örnek: Hücre Teorisi, Kromozom Teorisi</text>
    <text x="152" y="170" text-anchor="middle" fill="#dc2626" font-size="11" font-weight="700">DİKKAT: Teoriler kanıtlanınca kanuna DÖNÜŞMEZ!</text>
  </g>

  <g transform="translate(338,62)">
    <rect width="304" height="192" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#065f46" font-size="13" font-weight="800">BİLİMSEL KANUN (YASA)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#6ee7b7" stroke-width="1.2"/>
    <text x="152" y="58" text-anchor="middle" fill="#064e3b" font-size="11.5" font-weight="700">Soru: Doğa olayı "NASIL" gerçekleşir?</text>
    <text x="152" y="82" text-anchor="middle" fill="#064e3b" font-size="11">• Belirli koşullar altında tekrarlanan gözlemlerle</text>
    <text x="152" y="100" text-anchor="middle" fill="#064e3b" font-size="11">doğadaki ilişkileri betimler (genellikle formülle).</text>
    <text x="152" y="122" text-anchor="middle" fill="#064e3b" font-size="11">• Olayın nedenini açıklamaz, işleyiş örüntüsünü verir.</text>
    <text x="152" y="146" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">Örnek: Mendel'in Benzerlik ve Ayrılma Yasaları</text>
    <text x="152" y="170" text-anchor="middle" fill="#065f46" font-size="11" font-weight="700">Teori ve kanun farklı bilimsel bilgi türleridir.</text>
  </g>
</svg>''',

    "b4": '''<svg viewBox="0 0 660 265" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="265" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#b45309"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMSEL BİLGİNİN DEĞİŞEBİLİRLİĞİ: HÜCRE TEORİSİNİN GELİŞİMİ</text>

  <g transform="translate(18,62)">
    <rect width="198" height="188" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#92400e" font-size="12" font-weight="800">1. İLK KEŞİF (1665)</text>
    <line x1="18" y1="34" x2="180" y2="34" stroke="#fcd34d" stroke-width="1.2"/>
    <text x="99" y="58" text-anchor="middle" fill="#78350f" font-size="11" font-weight="700">Robert Hooke &amp; Leeuwenhoek</text>
    <text x="99" y="82" text-anchor="middle" fill="#78350f" font-size="11">Hooke şişe mantarında</text>
    <text x="99" y="100" text-anchor="middle" fill="#78350f" font-size="11">boş odacıklara "hücre" dedi;</text>
    <text x="99" y="122" text-anchor="middle" fill="#78350f" font-size="11">Leeuwenhoek ilk kez canlı</text>
    <text x="99" y="140" text-anchor="middle" fill="#78350f" font-size="11">tek hücrelileri gözlemledi.</text>
  </g>

  <g transform="translate(231,62)">
    <rect width="198" height="188" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#1e40af" font-size="12" font-weight="800">2. KLASİK TEORİ (1838–1858)</text>
    <line x1="18" y1="34" x2="180" y2="34" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="99" y="58" text-anchor="middle" fill="#1e3a8a" font-size="11" font-weight="700">Schleiden, Schwann, Virchow</text>
    <text x="99" y="82" text-anchor="middle" fill="#1e3a8a" font-size="11">• Tüm canlılar hücrelerden</text>
    <text x="99" y="100" text-anchor="middle" fill="#1e3a8a" font-size="11">oluşur; hücre temel birimdir.</text>
    <text x="99" y="122" text-anchor="middle" fill="#1e3a8a" font-size="11">• Yeni hücreler önceki hücrenin</text>
    <text x="99" y="140" text-anchor="middle" fill="#1e3a8a" font-size="11">bölünmesiyle oluşur (Virchow).</text>
  </g>

  <g transform="translate(444,62)">
    <rect width="198" height="188" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="99" y="24" text-anchor="middle" fill="#065f46" font-size="12" font-weight="800">3. MODERN EKLENTİLER (20. YY)</text>
    <line x1="18" y1="34" x2="180" y2="34" stroke="#6ee7b7" stroke-width="1.2"/>
    <text x="99" y="58" text-anchor="middle" fill="#064e3b" font-size="11" font-weight="700">Elektron Mikroskobu &amp; Moleküler</text>
    <text x="99" y="82" text-anchor="middle" fill="#064e3b" font-size="11">• Hücreler kalıtım materyali</text>
    <text x="99" y="100" text-anchor="middle" fill="#064e3b" font-size="11">(DNA) içerir ve yavruya aktarır.</text>
    <text x="99" y="122" text-anchor="middle" fill="#064e3b" font-size="11">• Tüm metabolik olaylar</text>
    <text x="99" y="140" text-anchor="middle" fill="#064e3b" font-size="11">hücre içinde gerçekleşir.</text>
  </g>
</svg>''',

    "b5": '''<svg viewBox="0 0 660 265" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="265" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#be185d"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMDE ÖZNELLİK, YARATICILIK VE SOSYO-KÜLTÜREL BAĞLAM</text>

  <g transform="translate(18,62)">
    <rect width="304" height="188" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#9d174d" font-size="12.5" font-weight="800">HAYAL GÜCÜ, YARATICILIK VE ÖZNELLİK</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#f9a8d4" stroke-width="1.2"/>
    <text x="152" y="60" text-anchor="middle" fill="#831843" font-size="11.5">• Hipotez kurma, deney düzeneği tasarlama ve</text>
    <text x="152" y="78" text-anchor="middle" fill="#831843" font-size="11.5">model oluşturma (ör. Watson ve Crick'in DNA</text>
    <text x="152" y="96" text-anchor="middle" fill="#831843" font-size="11.5">çift sarmal modeli) hayal gücü gerektirir.</text>
    <text x="152" y="124" text-anchor="middle" fill="#831843" font-size="11.5">• Aynı veriyi inceleyen iki bilim insanı geçmiş</text>
    <text x="152" y="142" text-anchor="middle" fill="#831843" font-size="11.5">eğitim ve deneyimlerine göre farklı yorumlayabilir.</text>
  </g>

  <g transform="translate(338,62)">
    <rect width="304" height="188" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#1e40af" font-size="12.5" font-weight="800">TOPLUM, KÜLTÜR VE BİLİM ETKİLEŞİMİ</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#93c5fd" stroke-width="1.2"/>
    <text x="152" y="60" text-anchor="middle" fill="#1e3a8a" font-size="11.5">• Bilimsel araştırmalar toplumun önceliklerinden,</text>
    <text x="152" y="78" text-anchor="middle" fill="#1e3a8a" font-size="11.5">ekonomik kaynaklardan ve etik değerlerden etkilenir.</text>
    <text x="152" y="106" text-anchor="middle" fill="#1e3a8a" font-size="11.5">• Örneğin salgın hastalık dönemlerinde aşı ve ilaç</text>
    <text x="152" y="124" text-anchor="middle" fill="#1e3a8a" font-size="11.5">araştırmalarına, kuraklıkta ise kuraklığa dayanıklı</text>
    <text x="152" y="142" text-anchor="middle" fill="#1e3a8a" font-size="11.5">tarım biyoteknolojisine öncelik verilir.</text>
  </g>
</svg>''',

    "b6": '''<svg viewBox="0 0 660 265" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:14px auto;font-family:'Plus Jakarta Sans',sans-serif;">
  <rect width="660" height="265" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="16" y="14" width="628" height="36" rx="8" fill="#0f172a"/>
  <text x="330" y="37" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">BİLİMİN DOĞASINA İLİŞKİN YAYGIN KAVRAM YANILGILARI VE DOĞRULARI</text>

  <g transform="translate(18,62)">
    <rect width="304" height="188" rx="10" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#991b1b" font-size="12.5" font-weight="800">YAYGIN KAVRAM YANILGILARI (YANLIŞ)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#fca5a5" stroke-width="1.2"/>
    <text x="152" y="62" text-anchor="middle" fill="#7f1d1d" font-size="11">1. "Hipotezler kanıtlanınca teoriye, teoriler de</text>
    <text x="152" y="78" text-anchor="middle" fill="#7f1d1d" font-size="11">kesinleşince kanuna (yasaya) dönüşür."</text>
    <text x="152" y="108" text-anchor="middle" fill="#7f1d1d" font-size="11">2. "Bilimsel bilgiler ve kanunlar mutlak doğrudur,</text>
    <text x="152" y="124" text-anchor="middle" fill="#7f1d1d" font-size="11">hiçbir zaman değişmez."</text>
    <text x="152" y="154" text-anchor="middle" fill="#7f1d1d" font-size="11">3. "Bilimde hayal gücü ve yaratıcılığa yer yoktur;</text>
    <text x="152" y="170" text-anchor="middle" fill="#7f1d1d" font-size="11">tüm araştırmalarda tek bir basamaklı yöntem izlenir."</text>
  </g>

  <g transform="translate(338,62)">
    <rect width="304" height="188" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="152" y="26" text-anchor="middle" fill="#065f46" font-size="12.5" font-weight="800">BİLİMSEL DOĞRULAR (DOĞRU)</text>
    <line x1="24" y1="36" x2="280" y2="36" stroke="#6ee7b7" stroke-width="1.2"/>
    <text x="152" y="62" text-anchor="middle" fill="#064e3b" font-size="11">1. Teori (neden) ve kanun (nasıl) farklı bilgi</text>
    <text x="152" y="78" text-anchor="middle" fill="#064e3b" font-size="11">türleridir; birbirine asla dönüşmez.</text>
    <text x="152" y="108" text-anchor="middle" fill="#064e3b" font-size="11">2. Teoriler ve kanunlar dâhil tüm bilimsel bilgiler</text>
    <text x="152" y="124" text-anchor="middle" fill="#064e3b" font-size="11">yeni kanıtlar karşısında değişebilir.</text>
    <text x="152" y="154" text-anchor="middle" fill="#064e3b" font-size="11">3. Bilim insanları her aşamada hayal gücü kullanır</text>
    <text x="152" y="170" text-anchor="middle" fill="#064e3b" font-size="11">ve farklı araştırma yöntemleri izleyebilir.</text>
  </g>
</svg>'''
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
