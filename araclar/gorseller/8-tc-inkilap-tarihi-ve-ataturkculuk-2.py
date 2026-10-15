from ozet_gorsel import svg


def g1():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-m"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-mf">MUSTAFA KEMAL\'İN DOĞDUĞU ORTAM VE AİLESİ (1881 - SELÂNİK)</text>'
        '<rect x="14" y="54" width="258" height="152" rx="8" class="g-ma"/>'
        '<text x="143" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">SELÂNİK ŞEHRİNİN ÖZELLİKLERİ</text>'
        '<rect x="26" y="88" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="143" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">İşlek Liman ve Demir Yolu Ağı</text>'
        '<rect x="26" y="126" width="234" height="32" rx="6" class="g-s"/>'
        '<text x="143" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">Çok Uluslu Yapı → Hoşgörü Ortamı</text>'
        '<rect x="26" y="164" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="143" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-tf">Azınlık İsyanları → Millî Bilinç</text>'
        '<rect x="288" y="54" width="258" height="152" rx="8" class="g-la"/>'
        '<text x="417" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">AİLE YAPISI (TÜRKMEN KÖKENİ)</text>'
        '<rect x="300" y="88" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="417" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">Babası: Ali Rıza Efendi (Yenilikçi)</text>'
        '<rect x="300" y="126" width="234" height="32" rx="6" class="g-l"/>'
        '<text x="417" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-lf">Annesi: Zübeyde Hanım (Kültürlü)</text>'
        '<rect x="300" y="164" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="417" y="185" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">Yaşayan Kardeşi: Makbule Hanım</text>'
    )
    return svg(w, h, ic, "Mustafa Kemal'in doğduğu Selânik ortamı ve ailesi şeması")


def g2():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-t"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">İLK VE ORTAÖĞRENİM BASAMAKLARI (1886 - 1896)</text>'
        '<rect x="14" y="54" width="124" height="152" rx="8" class="g-sa"/>'
        '<text x="76" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">1886</text>'
        '<text x="76" y="100" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Mahalle</text>'
        '<text x="76" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Mektebi</text>'
        '<text x="76" y="148" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Annesinin</text>'
        '<text x="76" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">İsteğiyle</text>'
        '<text x="76" y="190" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">(Geleneksel)</text>'
        '<rect x="150" y="54" width="124" height="152" rx="8" class="g-ya"/>'
        '<text x="212" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-yf">1886</text>'
        '<text x="212" y="100" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Şemsi Efendi</text>'
        '<text x="212" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Mektebi</text>'
        '<text x="212" y="148" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Babasının</text>'
        '<text x="212" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">İsteğiyle</text>'
        '<text x="212" y="190" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">(Modern Usul)</text>'
        '<rect x="286" y="54" width="124" height="152" rx="8" class="g-la"/>'
        '<text x="348" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">1894</text>'
        '<text x="348" y="100" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Selânik Mülkiye</text>'
        '<text x="348" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Rüştiyesi</text>'
        '<text x="348" y="148" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Kısa Süreli</text>'
        '<text x="348" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Sivil Ortaokul</text>'
        '<text x="348" y="190" text-anchor="middle" font-size="12" font-weight="600" class="g-lf">(Sivil Eğitim)</text>'
        '<rect x="422" y="54" width="124" height="152" rx="8" class="g-ma"/>'
        '<text x="484" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">1894</text>'
        '<text x="484" y="100" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Selânik Askerî</text>'
        '<text x="484" y="118" text-anchor="middle" font-size="12" font-weight="700" class="g-y">Rüştiyesi</text>'
        '<text x="484" y="148" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Kendi Kararı</text>'
        '<text x="484" y="166" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">ve Sınavla</text>'
        '<text x="484" y="190" text-anchor="middle" font-size="12" font-weight="600" class="g-mf">("Kemal" Adı)</text>'
    )
    return svg(w, h, ic, "Mustafa Kemal'in ilk ve ortaöğrenim basamakları şeması")


def g3():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-y"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-yf">MANASTIR ASKERÎ İDADİSİNDE (1896) ETKİLENDİĞİ ŞAHSİYETLER</text>'
        '<rect x="14" y="54" width="258" height="72" rx="8" class="g-ma"/>'
        '<text x="143" y="78" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">Mehmet Tevfik (Bilge) Bey</text>'
        '<text x="143" y="100" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Tarih Öğretmeni → Tarih Bilinci</text>'
        '<text x="143" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">"Bana yeni bir ufuk açtı."</text>'
        '<rect x="288" y="54" width="258" height="72" rx="8" class="g-ta"/>'
        '<text x="417" y="78" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">Ömer Naci (Sınıf Arkadaşı)</text>'
        '<text x="417" y="100" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Edebiyat ve Şiir Sevgisi</text>'
        '<text x="417" y="118" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Namık Kemal ve Tevfik Fikret</text>'
        '<rect x="14" y="134" width="258" height="72" rx="8" class="g-sa"/>'
        '<text x="143" y="158" text-anchor="middle" font-size="12" font-weight="700" class="g-sf">Ali Fethi (Okyar) (Arkadaşı)</text>'
        '<text x="143" y="180" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Fransızca ve Batı Düşünürleri</text>'
        '<text x="143" y="198" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Rousseau, Montesquieu, Voltaire</text>'
        '<rect x="288" y="134" width="258" height="72" rx="8" class="g-la"/>'
        '<text x="417" y="158" text-anchor="middle" font-size="12" font-weight="700" class="g-lf">Mehmet Asım Efendi</text>'
        '<text x="417" y="180" text-anchor="middle" font-size="12" font-weight="600" class="g-y">Hitabet Öğretmeni → Hitabet Sanatı</text>'
        '<text x="417" y="198" text-anchor="middle" font-size="12" font-weight="600" class="g-gf">Askerlik ve Güzel Konuşma Dengesi</text>'
    )
    return svg(w, h, ic, "Manastır Askerî İdadisinde Mustafa Kemal'in etkilendiği şahsiyetler")


def g4():
    w, h = 560, 220
    ic = (
        '<rect x="14" y="12" width="532" height="32" rx="8" class="g-l"/>'
        '<text x="280" y="33" text-anchor="middle" font-size="13" font-weight="700" class="g-lf">YÜKSEKÖĞRENİM YILLARI: İSTANBUL (1899 - 1905)</text>'
        '<rect x="14" y="54" width="258" height="152" rx="8" class="g-ma"/>'
        '<text x="143" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">İSTANBUL HARP OKULU (1899-1902)</text>'
        '<rect x="26" y="88" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="143" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">Öğretmen: Yüzbaşı Naci (Eldeniz)</text>'
        '<rect x="26" y="126" width="234" height="32" rx="6" class="g-s"/>'
        '<text x="143" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-sf">Faaliyet: Okul Gazetesi Çıkarması</text>'
        '<rect x="26" y="164" width="234" height="32" rx="6" class="g-m"/>'
        '<text x="143" y="185" text-anchor="middle" font-size="12" font-weight="700" class="g-mf">1902 Mezuniyeti: Teğmen Rütbesi</text>'
        '<rect x="288" y="54" width="258" height="152" rx="8" class="g-ta"/>'
        '<text x="417" y="76" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">HARP AKADEMİSİ (1902-1905)</text>'
        '<rect x="300" y="88" width="234" height="32" rx="6" class="g-y"/>'
        '<text x="417" y="109" text-anchor="middle" font-size="12" font-weight="600" class="g-yf">Öğretmen: Taktikçi Yarbay Nuri Bey</text>'
        '<rect x="300" y="126" width="234" height="32" rx="6" class="g-l"/>'
        '<text x="417" y="147" text-anchor="middle" font-size="12" font-weight="600" class="g-lf">Mezuniyet: Kurmay Yüzbaşı (1905)</text>'
        '<rect x="300" y="164" width="234" height="32" rx="6" class="g-t"/>'
        '<text x="417" y="185" text-anchor="middle" font-size="12" font-weight="700" class="g-tf">İlk Görev Yeri: Şam 5. Ordu</text>'
    )
    return svg(w, h, ic, "Mustafa Kemal'in İstanbul Harp Okulu ve Harp Akademisi yılları şeması")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[2]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()

