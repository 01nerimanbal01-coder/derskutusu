from ozet_gorsel import svg


def gorsel_1():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">KARAGÖZ OYUNUNUN DÖRT BÖLÜMÜ (YAPI UNSURLARI)</text>
    <rect x="35" y="62" width="145" height="160" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="107" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">1. MUKADDİME</text>
    <text x="107" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#2563eb">(Giriş Bölümü)</text>
    <text x="107" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• Hacivat semai okur</text>
    <text x="107" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• Perde gazeli (tasavvuf)</text>
    <text x="107" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• "Yâr, bana bir eğlence!"</text>
    <text x="107" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e3a8a">Küşterî Meydanı</text>

    <rect x="195" y="62" width="145" height="160" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="267" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#b45309">2. MUHAVERE</text>
    <text x="267" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#d97706">(Söyleşme)</text>
    <text x="267" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">• Karagöz ve Hacivat</text>
    <text x="267" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">• Yanlış anlamalar</text>
    <text x="267" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#92400e">• Söz oyunları / Atışma</text>
    <text x="267" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#78350f">Aydın - Halk Çatışması</text>

    <rect x="355" y="62" width="145" height="160" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="427" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#15803d">3. FASIL</text>
    <text x="427" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#16a34a">(Asıl Oyun)</text>
    <text x="427" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Ana olay (Yazıcılık)</text>
    <text x="427" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Yardımcı tipler gelir</text>
    <text x="427" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Hanım, Laz, Tiryaki,</text>
    <text x="427" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#166534">  Çelebi şive taklitleri</text>

    <rect x="515" y="62" width="150" height="160" rx="10" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
    <text x="590" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="700" fill="#be185d">4. BİTİŞ</text>
    <text x="590" y="106" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#db2777">(Kapanış)</text>
    <text x="590" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#9d174d">• Kısa son konuşma</text>
    <text x="590" y="150" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#9d174d">• "Yıktın perdeyi..."</text>
    <text x="590" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#9d174d">• "Her ne kadar sürc-i</text>
    <text x="590" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" fill="#9d174d">  lisan ettikse affola!"</text>
    """
    return svg(700, 260, ic, "Karagöz Oyununun Bölümleri")


def gorsel_2():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">YAZICI OYUNUNDA DİL ÇATIŞMASI VE YANLIŞ ANLAMALAR</text>
    <rect x="45" y="62" width="275" height="160" rx="12" fill="#ede9fe" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="182" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#5b21b6">SEÇKİN / YABANCI SÖZ VARLIĞI</text>
    <text x="182" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#4c1d95">• Hanım: "Gonce-dehânım"</text>
    <text x="182" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#4c1d95">• Tiryaki: "Yirmi dirhem sinâmeki"</text>
    <text x="182" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#4c1d95">• Tiryaki: "Kırk dirhem havlıcan"</text>
    <text x="182" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#4c1d95">• Çelebi: "Nerede iskân-ı beyt edersiniz?"</text>
    <text x="182" y="208" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#4c1d95">• Çelebi: "Demek hane-ber-dûşsunuz."</text>

    <text x="350" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="22" font-weight="700" fill="#ef4444">➔</text>

    <rect x="380" y="62" width="275" height="160" rx="12" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="517" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">KARAGÖZ'ÜN ÇARPITMASI (MİZAH)</text>
    <text x="517" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#92400e">• "Pencerede hanım"</text>
    <text x="517" y="138" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#92400e">• "Sülüklü'deki sinek Ahmet'i"</text>
    <text x="517" y="162" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#92400e">• "Kırk kere havlıyacağım"</text>
    <text x="517" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#92400e">• "İskelede bitleniyorum."</text>
    <text x="517" y="208" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" fill="#92400e">• "Muş değilim ben."</text>
    """
    return svg(700, 255, ic, "Yazıcı Oyununda Yanlış Anlamalar ve Güldürü")


def gorsel_3():
    ic = """
    <rect x="20" y="15" width="660" height="230" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">MEKTUP VE DİLEKÇENİN BİÇİMSEL YAPI ŞEMASI</text>
    <rect x="40" y="60" width="295" height="165" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="187" y="82" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="700" fill="#1d4ed8">ÖZEL / EDEBÎ MEKTUP PLANI</text>
    <text x="315" y="102" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e40af">Yer ve Tarih (24 Haziran 1940 İstanbul)</text>
    <text x="60" y="120" font-family="Inter,sans-serif" font-size="10.5" font-weight="700" fill="#1e3a8a">Hitap Bölümü (Âli, / Aziz Dostum,)</text>
    <text x="60" y="140" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• Giriş: Mektubun yazılış amacı</text>
    <text x="60" y="158" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• Gelişme: Duygu, düşünce ve edebî tahliller</text>
    <text x="60" y="176" font-family="Inter,sans-serif" font-size="10" fill="#1e40af">• Sonuç: İyi dilek ve selamlar</text>
    <text x="60" y="206" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e3a8a">Sol Alt: Adres</text>
    <text x="315" y="206" text-anchor="end" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#1e3a8a">Sağ Alt: İmza / Ad-Soyadı</text>

    <rect x="365" y="60" width="295" height="165" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="512" y="82" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="700" fill="#15803d">RESMÎ DİLEKÇE PLANI (3071 Sayılı Kanun)</text>
    <text x="512" y="104" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="700" fill="#14532d">KURUM / MAKAM ADI (BÜYÜK HARFLE)</text>
    <text x="385" y="128" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Kısa, açık ve nesnel sorun/talep metni</text>
    <text x="385" y="148" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Üst makama: "Gereğini bilgilerinize arz ederim."</text>
    <text x="385" y="168" font-family="Inter,sans-serif" font-size="10" fill="#166534">• Alt makama: "... rica ederim." (30 gün cevap)</text>
    <text x="385" y="196" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#14532d">Sol Alt: Adres, T.C. No,</text>
    <text x="385" y="210" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#14532d">İletişim ve Ekler</text>
    <text x="640" y="196" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#14532d">Sağ Alt: Tarih, İmza,</text>
    <text x="640" y="210" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#14532d">Adı-Soyadı</text>
    """
    return svg(700, 255, ic, "Mektup ve Dilekçe Yapı Unsurları")


def gorsel_4():
    ic = """
    <rect x="20" y="15" width="660" height="225" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="350" y="42" text-anchor="middle" font-family="Inter,sans-serif" font-size="15" font-weight="700" fill="#1e293b">METİNLERDE FİİLİMSİLER (EYLEMSİLER) VE İŞLEVLERİ</text>
    <rect x="35" y="62" width="200" height="155" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="135" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#1d4ed8">1. İSİM-FİİL (MASTAR)</text>
    <text x="135" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="11" font-weight="600" fill="#2563eb">Ekler: -ma, -ış, -mak</text>
    <text x="135" y="136" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">Örnek: "...burayı beklemek</text>
    <text x="135" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#1e40af">için yüz kuruş ver."</text>
    <text x="135" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#1e3a8a">İşlevi: İsim Görevi</text>

    <rect x="250" y="62" width="200" height="155" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="350" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#b45309">2. SIFAT-FİİL (ORTAÇ)</text>
    <text x="350" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#d97706">-an, -ası, -mez, -ar, -dik, -ecek, -miş</text>
    <text x="350" y="136" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#92400e">• "yazılmış ferman" (Sıfat)</text>
    <text x="350" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#92400e">• "burada oturanlar" (Adlaşmış)</text>
    <text x="350" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#78350f">İşlevi: Sıfat / Adlaşmış Sıfat</text>

    <rect x="465" y="62" width="200" height="155" rx="10" fill="#dcfce7" stroke="#22c55e" stroke-width="1.5"/>
    <text x="565" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="700" fill="#15803d">3. ZARF-FİİL (BAĞ-FİİL)</text>
    <text x="565" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#16a34a">Ekler: -arak, -dıkça, -ken, -ıp...</text>
    <text x="565" y="136" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">• "evden çıkarak" (Durum)</text>
    <text x="565" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" fill="#166534">• "sallandıkça / geçerken"</text>
    <text x="565" y="186" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="600" fill="#14532d">İşlevi: Zarf (Durum / Zaman)</text>
    """
    return svg(700, 250, ic, "Fiilimsi Türleri ve Cümledeki Görevleri")


def uygula(v):
    v["bolumler"][0]["gorsel"] = gorsel_1()
    v["bolumler"][2]["gorsel"] = gorsel_2()
    v["bolumler"][4]["gorsel"] = gorsel_3()
    v["bolumler"][5]["gorsel"] = gorsel_4()
