from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 235
    ic = f"""
    <rect x="12" y="12" width="596" height="211" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">MALAZGİRT SONRASI ANADOLU'DA KURULAN İLK TÜRK BEYLİKLERİ VE ESERLERİ</text>

    <!-- Üst satır: 3 kutu -->
    <rect x="24" y="48" width="182" height="78" rx="9" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="115" y="65" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#1d4ed8">SALTUKLULAR (1072-1202)</text>
    <text x="115" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1e3a8a">Merkez: Erzurum ve çevresi</text>
    <text x="115" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• İlk kurulan Türk beyliği</text>
    <text x="115" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">• Mama Hatun Külliyesi</text>

    <rect x="219" y="48" width="182" height="78" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
    <text x="310" y="65" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#15803d">DANİŞMENTLİLER (1080-1178)</text>
    <text x="310" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#14532d">Merkez: Sivas, Tokat, Amasya</text>
    <text x="310" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• En güçlü beylik (Haçlı mücadelesi)</text>
    <text x="310" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">• Yağıbasan Medresesi (İlk medrese)</text>

    <rect x="414" y="48" width="182" height="78" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="505" y="65" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b45309">MENGÜCEKLİLER (1080-1228)</text>
    <text x="505" y="80" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#78350f">Merkez: Erzincan ve Divriği</text>
    <text x="505" y="95" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• Gürcü ve Rumlarla mücadele</text>
    <text x="505" y="110" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b45309">• Divriği Ulu Cami Külliyesi</text>

    <!-- Alt satır: 3 kutu -->
    <rect x="24" y="136" width="182" height="76" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="115" y="153" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#b91c1c">ARTUKLULAR (1102-1231)</text>
    <text x="115" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#7f1d1d">Hasankeyf, Mardin, Harput</text>
    <text x="115" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• En uzun ömürlü beylik (3 kol)</text>
    <text x="115" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">• Malabadi Köprüsü (Diyarbakır)</text>

    <rect x="219" y="136" width="182" height="76" rx="9" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>
    <text x="310" y="153" text-anchor="middle" font-family="Inter,sans-serif" font-size="10" font-weight="800" fill="#4338ca">ÇAKA BEYLİĞİ (1081-1093)</text>
    <text x="310" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#312e81">Merkez: İzmir ve çevresi</text>
    <text x="310" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• İlk Türk denizcisi Çaka Bey</text>
    <text x="310" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#4338ca">• İlk Türk donanmasını kurdu</text>

    <rect x="414" y="136" width="182" height="76" rx="9" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="505" y="153" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#6d28d9">TÜRKİYE SELÇUKLU (1075-1308)</text>
    <text x="505" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#4c1d95">Kurucu: Süleyman Şah (İznik)</text>
    <text x="505" y="183" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" fill="#334155">• I. Haçlı'da başkent Konya oldu</text>
    <text x="505" y="198" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#6d28d9">• Anadolu Türk birliğini sağladı</text>
    """
    return svg(w, h, ic, "Anadolu'da kurulan ilk Türk beylikleri ve Türkiye Selçuklu Devleti")


def _gorsel_3():
    w, h = 620, 225
    ic = f"""
    <rect x="12" y="12" width="596" height="201" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">HAÇLI SAVAŞLARI (I - IV) VE 1187 HITTİN ZAFERİ SÜREÇ ŞEMASI</text>

    <!-- 5 Aşamalı Akış -->
    <rect x="20" y="50" width="108" height="146" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.4"/>
    <text x="74" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#991b1b">I. HAÇLI</text>
    <text x="74" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b91c1c">(1096 - 1099)</text>
    <text x="74" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Başkent İznik'ten</text>
    <text x="74" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#7f1d1d">Konya'ya taşındı</text>
    <text x="74" y="132" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Urfa, Antakya,</text>
    <text x="74" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Kudüs, Trablus'ta</text>
    <text x="74" y="156" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">kontluklar kuruldu</text>
    <text x="74" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#15803d">• 1101 orduları</text>
    <text x="74" y="187" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#15803d">Anadolu'da ezildi</text>

    <rect x="137" y="50" width="108" height="146" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.4"/>
    <text x="191" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#14532d">II. HAÇLI</text>
    <text x="191" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#15803d">(1147 - 1149)</text>
    <text x="191" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Neden: 1144'te</text>
    <text x="191" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#14532d">İmadeddin Zengi</text>
    <text x="191" y="126" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Urfa'yı geri aldı</text>
    <text x="191" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#15803d">• Sultan I. Mesud</text>
    <text x="191" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Alman ve Fransız</text>
    <text x="191" y="170" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">ordularını</text>
    <text x="191" y="182" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#15803d">bozguna uğrattı</text>

    <rect x="254" y="50" width="112" height="146" rx="9" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
    <text x="310" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#92400e">HITTİN ZAFERİ</text>
    <text x="310" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#b45309">(1187)</text>
    <text x="310" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#78350f">Selahaddin Eyyubi</text>
    <text x="310" y="118" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Hıttin'de Haçlı</text>
    <text x="310" y="130" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">ordusunu yendi</text>
    <text x="310" y="148" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#b45309">• KUDÜS yeniden</text>
    <text x="310" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="800" fill="#b45309">fethedildi</text>
    <text x="310" y="178" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• İslam dünyasında</text>
    <text x="310" y="189" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">büyük dayanışma</text>

    <rect x="375" y="50" width="108" height="146" rx="9" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
    <text x="429" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#1e3a8a">III. HAÇLI</text>
    <text x="429" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#1d4ed8">(1189 - 1192)</text>
    <text x="429" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Neden: Kudüs'ü</text>
    <text x="429" y="114" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">geri alma isteği</text>
    <text x="429" y="132" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Barbarossa Göksu</text>
    <text x="429" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">Irmağı'nda boğuldu</text>
    <text x="429" y="164" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">• Akka alındı ama</text>
    <text x="429" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">Kudüs alınamadı</text>

    <rect x="492" y="50" width="108" height="146" rx="9" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.4"/>
    <text x="546" y="68" text-anchor="middle" font-family="Inter,sans-serif" font-size="9.5" font-weight="800" fill="#4c1d95">IV. HAÇLI</text>
    <text x="546" y="81" text-anchor="middle" font-family="Inter,sans-serif" font-size="8.5" font-weight="700" fill="#6d28d9">(1202 - 1204)</text>
    <text x="546" y="102" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• Hedefinden saptı:</text>
    <text x="546" y="116" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#6d28d9">İstanbul yağmalandı</text>
    <text x="546" y="134" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">• 1204'te Latin</text>
    <text x="546" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">İmparatorluğu</text>
    <text x="546" y="158" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" fill="#334155">kuruldu</text>
    <text x="546" y="176" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#4c1d95">• Selçuklu ticareti</text>
    <text x="546" y="187" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#4c1d95">güçlendi</text>
    """
    return svg(w, h, ic, "Haçlı Savaşları (I-IV) ve 1187 Hıttin Muharebesi kronolojik özet şeması")


def _gorsel_6():
    w, h = 620, 220
    ic = f"""
    <rect x="12" y="12" width="596" height="196" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="310" y="34" text-anchor="middle" font-family="Inter,sans-serif" font-size="12.5" font-weight="800" fill="#0f172a">1040 - 1299 ARASI ASKERÎ MÜCADELELERİN TARİH ŞERİDİ VE DÖNÜM NOKTALARI</text>

    <!-- Zaman Çizgisi -->
    <line x1="36" y1="112" x2="584" y2="112" stroke="#334155" stroke-width="3"/>

    <!-- Nokta 1: 1040 Dandanakan -->
    <circle cx="56" cy="112" r="7" fill="#2563eb"/>
    <rect x="20" y="50" width="76" height="46" rx="6" fill="#dbeafe" stroke="#2563eb"/>
    <text x="58" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#1d4ed8">1040</text>
    <text x="58" y="79" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#1e3a8a">Dandanakan</text>
    <text x="58" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#334155">Devlet Kuruluşu</text>

    <!-- Nokta 2: 1048 Pasinler -->
    <circle cx="140" cy="112" r="7" fill="#0284c7"/>
    <rect x="102" y="128" width="76" height="46" rx="6" fill="#e0f2fe" stroke="#0284c7"/>
    <text x="140" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#0369a1">1048</text>
    <text x="140" y="157" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#075985">Pasinler</text>
    <text x="140" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#334155">İlk Bizans Savaşı</text>

    <!-- Nokta 3: 1071 Malazgirt -->
    <circle cx="226" cy="112" r="7.5" fill="#16a34a"/>
    <rect x="186" y="50" width="80" height="46" rx="6" fill="#dcfce7" stroke="#16a34a"/>
    <text x="226" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#15803d">1071</text>
    <text x="226" y="79" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#14532d">Malazgirt</text>
    <text x="226" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#166534">Vatan Açan Zafer</text>

    <!-- Nokta 4: 1176 Miryokefalon -->
    <circle cx="330" cy="112" r="7.5" fill="#059669"/>
    <rect x="284" y="128" width="92" height="46" rx="6" fill="#d1fae5" stroke="#059669"/>
    <text x="330" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#047857">1176</text>
    <text x="330" y="157" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#065f46">Miryokefalon</text>
    <text x="330" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#064e3b">Vatan Koruyan Zafer</text>

    <!-- Nokta 5: 1187 Hıttin -->
    <circle cx="436" cy="112" r="7" fill="#d97706"/>
    <rect x="394" y="50" width="84" height="46" rx="6" fill="#fef3c7" stroke="#d97706"/>
    <text x="436" y="66" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#b45309">1187</text>
    <text x="436" y="79" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#92400e">Hıttin Zaferi</text>
    <text x="436" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#78350f">Kudüs'ün Fethi</text>

    <!-- Nokta 6: 1243 Kösedağ -->
    <circle cx="546" cy="112" r="7.5" fill="#dc2626"/>
    <rect x="498" y="128" width="96" height="46" rx="6" fill="#fee2e2" stroke="#dc2626"/>
    <text x="546" y="144" text-anchor="middle" font-family="Inter,sans-serif" font-size="9" font-weight="800" fill="#b91c1c">1243</text>
    <text x="546" y="157" text-anchor="middle" font-family="Inter,sans-serif" font-size="8" font-weight="700" fill="#991b1b">Kösedağ Savaşı</text>
    <text x="546" y="168" text-anchor="middle" font-family="Inter,sans-serif" font-size="7.5" fill="#7f1d1d">Moğol Tahakkümü</text>
    """
    return svg(w, h, ic, "1040 Dandanakan'dan 1243 Kösedağ'a kadar Türk tarihinin seyrini değiştiren mücadeleler")


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = _gorsel_1()
    if len(b) > 2:
        b[2]["gorsel"] = _gorsel_3()
    if len(b) > 5:
        b[5]["gorsel"] = _gorsel_6()
