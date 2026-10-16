from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">EDEBÎ METİNLERDE VE GÜNLÜK YAŞAMDA MEKÂNSAL ÖGELERİN COĞRAFİ ANALİZİ</text>

    <!-- Sol: Fiziki Coğrafya Unsurları -->
    <rect x="24" y="48" width="276" height="150" rx="10" fill="#ecfdf5" stroke="#16a34a" stroke-width="1.6"/>
    <rect x="24" y="48" width="276" height="26" rx="10" fill="#16a34a"/>
    <text x="162" y="65" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">FİZİKİ COĞRAFYA ÖGELERİ (DOĞAL ORTAM)</text>

    <rect x="36" y="84" width="252" height="30" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="162" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#14532d">Jeomorfoloji (Yer Şekilleri)</text>
    <text x="162" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Dağlar, ovalar, yaylalar, Hasan Dağı (Aksaray)</text>

    <rect x="36" y="120" width="252" height="30" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="162" y="134" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#14532d">Hidrografya (Sular Coğrafyası)</text>
    <text x="162" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Mavi sular, sarı seller, Manavgat Şelalesi</text>

    <rect x="36" y="156" width="252" height="30" rx="6" fill="#ffffff" stroke="#86efac"/>
    <text x="162" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#14532d">Klimatoloji (İklim Bilimi)</text>
    <text x="162" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Boz dumanlar (sis), karların erimesi, kuraklık</text>

    <!-- Sağ: Beşerî ve Ekonomik Coğrafya Unsurları -->
    <rect x="320" y="48" width="276" height="150" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
    <rect x="320" y="48" width="276" height="26" rx="10" fill="#2563eb"/>
    <text x="458" y="65" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#ffffff">BEŞERÎ VE EKONOMİK COĞRAFYA ÖGELERİ</text>

    <rect x="332" y="84" width="252" height="30" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="458" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#1e3a8a">Yerleşme Coğrafyası</text>
    <text x="458" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Köyler, kerpiç evler, yayla yerleşmeleri, Şirince</text>

    <rect x="332" y="120" width="252" height="30" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="458" y="134" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#1e3a8a">Tarım ve Enerji Coğrafyası</text>
    <text x="458" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Ekilen ekinler, yoncalar, Muğla tarımı, Keban Barajı</text>

    <rect x="332" y="156" width="252" height="30" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="458" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#1e3a8a">Ulaşım ve Turizm Coğrafyası</text>
    <text x="458" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Köy yolları, kağnılar, Varda Köprüsü, Konyaaltı Plajı</text>
    """
    return svg(w, h, ic, "Edebî metinlerde ve günlük yaşamda fiziki ve beşerî coğrafya unsurları")


def _gorsel_3():
    w, h = 620, 230
    ic = f"""
    <rect x="12" y="12" width="596" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">SÜVEYŞ KANALI (EVER GIVEN) ÖRNEK OLAYI: YERELDEN KÜRESELE COĞRAFİ BAĞLANTILAR</text>

    <!-- Sol: Konum ve Doğal Faktör -->
    <rect x="24" y="50" width="182" height="150" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="115" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b45309">1. KONUM VE DOĞAL NEDEN</text>
    <text x="115" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#78350f">• Mısır (30°K - 30°D civarı)</text>
    <text x="115" y="103" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• Akdeniz ile Kızıldeniz'i</text>
    <text x="115" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">birbirine bağlayan su yolu</text>
    <rect x="34" y="128" width="162" height="60" rx="6" fill="#ffffff" stroke="#fcd34d"/>
    <text x="115" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#92400e">Doğal Etken (24 Mart 2021):</text>
    <text x="115" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Çöl iklimine bağlı kum fırtınası</text>
    <text x="115" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">ve şiddetli rüzgâr görüşü</text>
    <text x="115" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#b45309">düşürdü → Gemi sıkıştı</text>

    <!-- Orta: Bölgesel Ölçek -->
    <rect x="219" y="50" width="182" height="150" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <text x="310" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1d4ed8">2. YEREL VE BÖLGESEL ETKİ</text>
    <text x="310" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1e3a8a">• Kanal 5 gün kapalı kaldı</text>
    <text x="310" y="103" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• Mısır'ın 3. büyük döviz</text>
    <text x="310" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">kaynağı (~6 milyar $/yıl)</text>
    <rect x="229" y="128" width="162" height="60" rx="6" fill="#ffffff" stroke="#93c5fd"/>
    <text x="310" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">Bölgesel Sonuç:</text>
    <text x="310" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Kızıldeniz ve Akdeniz</text>
    <text x="310" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">girişlerinde yüzlerce gemi</text>
    <text x="310" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1e40af">beklemek zorunda kaldı</text>

    <!-- Sağ: Küresel Ölçek -->
    <rect x="414" y="50" width="182" height="150" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="505" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b91c1c">3. KÜRESEL ETKİ VE ÖLÇEK</text>
    <text x="505" y="88" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#7f1d1d">• Küresel ticaretin %12'si</text>
    <text x="505" y="103" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• Günde ~10 milyar dolarlık</text>
    <text x="505" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">mal akışı (Hareket)</text>
    <rect x="424" y="128" width="162" height="60" rx="6" fill="#ffffff" stroke="#fca5a5"/>
    <text x="505" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Küresel Sonuç:</text>
    <text x="505" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Ham petrol ve LNG sevkiyatı</text>
    <text x="505" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">aksadı, küresel tedarik zinciri</text>
    <text x="505" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#991b1b">ve enerji fiyatları etkilendi</text>
    """
    return svg(w, h, ic, "Süveyş Kanalı Ever Given gemi kazasının yerel, bölgesel ve küresel etkileri")


def _gorsel_4():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">ARAL GÖLÜ (1989 - 2018) VE MEKSİKA KÖRFEZİ (2010) ÇEVRE FELAKETLERİ</text>

    <!-- Sol: Aral Gölü -->
    <rect x="24" y="48" width="276" height="150" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="162" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#b45309">ARAL GÖLÜ'NÜN KURUMASI (1989-2018)</text>

    <!-- 4 mini kutu ile küçülme temsili -->
    <rect x="38" y="78" width="52" height="44" rx="5" fill="#fef3c7" stroke="#b45309"/>
    <ellipse cx="64" cy="96" rx="18" ry="12" fill="#2563eb"/>
    <text x="64" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#78350f">1989</text>

    <rect x="98" y="78" width="52" height="44" rx="5" fill="#fef3c7" stroke="#b45309"/>
    <ellipse cx="124" cy="96" rx="13" ry="9" fill="#3b82f6"/>
    <text x="124" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#78350f">2000</text>

    <rect x="158" y="78" width="52" height="44" rx="5" fill="#fef3c7" stroke="#b45309"/>
    <ellipse cx="184" cy="96" rx="8" ry="6" fill="#60a5fa"/>
    <text x="184" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#78350f">2006</text>

    <rect x="218" y="78" width="68" height="44" rx="5" fill="#fee2e2" stroke="#dc2626"/>
    <ellipse cx="252" cy="96" rx="3.5" ry="3" fill="#93c5fd"/>
    <text x="252" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#b91c1c">2018 (Çöl)</text>

    <text x="162" y="139" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#92400e">Ülkeler: Kazakistan ve Özbekistan</text>
    <text x="162" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Neden: Amuderya ve Sırderya sularının aşırı</text>
    <text x="162" y="167" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">pamuk sulamasında kullanılması + kuraklık</text>
    <text x="162" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Sonuç: Çoraklaşma, balıkçılığın bitmesi, göç</text>

    <!-- Sağ: Meksika Körfezi -->
    <rect x="320" y="48" width="276" height="150" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="458" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="10.5" font-weight="800" fill="#1d4ed8">MEKSİKA KÖRFEZİ PETROL SIZINTISI</text>

    <rect x="336" y="78" width="244" height="44" rx="6" fill="#dbeafe" stroke="#3b82f6"/>
    <circle cx="378" cy="100" r="14" fill="#1e293b" opacity="0.85"/>
    <circle cx="378" cy="100" r="6" fill="#dc2626"/>
    <text x="480" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#1e3a8a">Deepwater Horizon (20 Nisan 2010)</text>
    <text x="480" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">49 milyon varil petrol → 149.000 km² alan</text>

    <text x="458" y="139" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1e40af">Kavramlar: İnsan-Çevre, Dağılış, Hareket, Ölçek</text>
    <text x="458" y="154" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">Doğal Etki: Deniz suyu, kıyılar, mercanlar, kuşlar</text>
    <text x="458" y="167" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">ve deniz canlılarının yaşam alanı tahrip oldu</text>
    <text x="458" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">Beşerî Etki: 11 can kaybı, balıkçılık ve turizm zararı</text>
    """
    return svg(w, h, ic, "Aral Gölü'nün kuruması ve Meksika Körfezi Deepwater Horizon petrol sızıntısı")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _gorsel_1()
    if len(b) > 2:
        b[2]["gorsel"] = _gorsel_3()
    if len(b) > 3:
        b[3]["gorsel"] = _gorsel_4()
