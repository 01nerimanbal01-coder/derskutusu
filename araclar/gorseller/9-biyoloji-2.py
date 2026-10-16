from ozet_gorsel import svg


def g_kaynak():
    return svg(
        620,
        220,
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">BİLİMSEL KAYNAK GÜVENİLİRLİĞİNİ SORGULAMA ÖLÇÜTLERİ</text>'
        '<rect x="30" y="60" width="176" height="56" rx="9" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>'
        '<text x="118" y="83" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1d4ed8">1. Bilimsel Makale mi?</text>'
        '<text x="118" y="103" text-anchor="middle" font-size="12" fill="#334155">Kanıt ve veriye dayalı yayın</text>'
        '<rect x="222" y="60" width="176" height="56" rx="9" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>'
        '<text x="310" y="83" text-anchor="middle" font-size="12.5" font-weight="700" fill="#15803d">2. Hakem Denetimi</text>'
        '<text x="310" y="103" text-anchor="middle" font-size="12" fill="#334155">Hakem/editör onayı var mı?</text>'
        '<rect x="414" y="60" width="176" height="56" rx="9" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>'
        '<text x="502" y="83" text-anchor="middle" font-size="12.5" font-weight="700" fill="#a16207">3. Resmî Uzantı</text>'
        '<text x="502" y="103" text-anchor="middle" font-size="12" fill="#334155">.edu veya .gov uzantılı mı?</text>'
        '<rect x="110" y="130" width="188" height="56" rx="9" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.4"/>'
        '<text x="204" y="153" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7e22ce">4. Uzman Görüşü</text>'
        '<text x="204" y="173" text-anchor="middle" font-size="12" fill="#334155">Uzman incelemesi içeriyor mu?</text>'
        '<rect x="322" y="130" width="188" height="56" rx="9" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>'
        '<text x="416" y="153" text-anchor="middle" font-size="12.5" font-weight="700" fill="#be123c">5. Güncellik</text>'
        '<text x="416" y="173" text-anchor="middle" font-size="12" fill="#334155">Son gelişmeleri yansıtıyor mu?</text>',
        "Bilimsel kaynakların güvenilirlik ölçütleri",
    )


def g_akis():
    return svg(
        620,
        230,
        '<rect x="16" y="16" width="588" height="198" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="310" y="40" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">BİLİMSEL YÖNTEM BASAMAKLARI VE GERİ BİLDİRİM DÖNGÜSÜ</text>'
        '<rect x="28" y="56" width="128" height="52" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.4"/>'
        '<text x="92" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#1d4ed8">1. Gözlem ve Problem</text>'
        '<text x="92" y="96" text-anchor="middle" font-size="12" fill="#334155">2. Veri Toplama</text>'
        '<rect x="176" y="56" width="128" height="52" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.4"/>'
        '<text x="240" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">3. Hipotez Kurma</text>'
        '<text x="240" y="96" text-anchor="middle" font-size="12" fill="#334155">4. Tahmin Yapma</text>'
        '<rect x="324" y="56" width="128" height="52" rx="8" fill="#fefce8" stroke="#fde047" stroke-width="1.4"/>'
        '<text x="388" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#a16207">5. Kontrollü Deney</text>'
        '<text x="388" y="96" text-anchor="middle" font-size="12" fill="#334155">Değişkenlerin Testi</text>'
        '<rect x="472" y="56" width="120" height="52" rx="8" fill="#faf5ff" stroke="#d8b4fe" stroke-width="1.4"/>'
        '<text x="532" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#7e22ce">6. Analiz/Çıkarım</text>'
        '<text x="532" y="96" text-anchor="middle" font-size="12" fill="#334155">Hipotez Uyumu</text>'
        '<rect x="60" y="132" width="230" height="60" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.4"/>'
        '<text x="175" y="154" text-anchor="middle" font-size="12.5" font-weight="700" fill="#be123c">Bulgular Hipotezi Desteklemezse</text>'
        '<text x="175" y="174" text-anchor="middle" font-size="12" fill="#334155">Hipotez gözden geçirilir / değiştirilir.</text>'
        '<rect x="330" y="132" width="230" height="60" rx="8" fill="#ecfeff" stroke="#67e8f9" stroke-width="1.4"/>'
        '<text x="445" y="154" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0e7490">Bulgular Hipotezi Desteklerse</text>'
        '<text x="445" y="174" text-anchor="middle" font-size="12" fill="#334155">Sonuçlar raporlanıp bilim dünyasına sunulur.</text>',
        "Bilimsel yöntem basamakları akış şeması",
    )


def g_degisken():
    return svg(
        620,
        220,
        '<rect x="16" y="16" width="588" height="188" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">KONTROLLÜ DENEYDE DEĞİŞKENLER (GÜVE ÖRNEĞİ)</text>'
        '<rect x="34" y="62" width="264" height="122" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>'
        '<text x="166" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">Bağımsız Değişken (Etken)</text>'
        '<text x="166" y="108" text-anchor="middle" font-size="12" fill="#334155">Araştırmacının değiştirdiği özellik:</text>'
        '<text x="166" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">Güvenin kanadında göz deseni</text>'
        '<text x="166" y="146" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">bulundurma durumu (var / yok)</text>'
        '<rect x="322" y="62" width="264" height="122" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>'
        '<text x="454" y="86" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">Bağımlı Değişken (Sonuç)</text>'
        '<text x="454" y="108" text-anchor="middle" font-size="12" fill="#334155">Bağımsız değişkene göre değişen:</text>'
        '<text x="454" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">Avcı kuşların bulunduğu ortamda</text>'
        '<text x="454" y="146" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1e293b">hayatta kalan güve sayısı</text>',
        "Kontrollü deneylerde bağımsız değişken, bağımlı değişken ve kontrol grubu",
    )


def g_ekoloji():
    return svg(
        620,
        225,
        '<rect x="16" y="16" width="588" height="193" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="310" y="42" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">ÖRNEK EKOLOJİK ARAŞTIRMALARDA KONTROL VE DENEY GRUPLARI</text>'
        '<rect x="34" y="60" width="265" height="128" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>'
        '<text x="166" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1d4ed8">1. Söğüt Ağaçları Araştırması</text>'
        '<text x="166" y="106" text-anchor="middle" font-size="12" fill="#334155">• Kontrol Grubu: Normal göl suyu</text>'
        '<text x="166" y="124" text-anchor="middle" font-size="12" fill="#334155">• Deney Grubu: Otopark atık sulu su</text>'
        '<text x="166" y="142" text-anchor="middle" font-size="12" fill="#334155">• Bağımsız Değ.: Suyun atık içeriği</text>'
        '<text x="166" y="160" text-anchor="middle" font-size="12" fill="#334155">• Bağımlı Değ.: Klorofil ve kök sağlığı</text>'
        '<rect x="321" y="60" width="265" height="128" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>'
        '<text x="453" y="84" text-anchor="middle" font-size="13.5" font-weight="700" fill="#15803d">2. Deney Ormanı (Nitrat) Çalışması</text>'
        '<text x="453" y="106" text-anchor="middle" font-size="12" fill="#334155">• Kontrol Alanı: Ağaçlı doğal vadi</text>'
        '<text x="453" y="124" text-anchor="middle" font-size="12" fill="#334155">• Deney Alanı: Ağaçları kesilen vadi</text>'
        '<text x="453" y="142" text-anchor="middle" font-size="12" fill="#334155">• Bağımsız Değ.: Ağaç örtüsü varlığı</text>'
        '<text x="453" y="160" text-anchor="middle" font-size="12" fill="#334155">• Bağımlı Değ.: Sudaki nitrat derişimi</text>',
        "Söğüt ağaçları ve deney ormanı araştırmalarında kontrol ve deney grupları",
    )


def uygula(v):
    b = v["bolumler"]
    b[1]["gorsel"] = g_kaynak()
    b[3]["gorsel"] = g_akis()
    b[4]["gorsel"] = g_degisken()
    b[5]["gorsel"] = g_ekoloji()
