# -*- coding: utf-8 -*-
"""10. Sınıf Tarih — 5. Hafta Görselleri
Konu: Türkistan’dan Türkiye’ye Uzanan Süreçte Türk Devlet ve Ordu Teşkilatında Meydana Gelen Değişim ve Süreklilik
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#b45309", arka="#fffbeb"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Türk Devlet Anlayışında Süreklilik ve Değişim Tablosu (Kut, Cihan Hakimiyeti, Hükümdarlık Sembolleri)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Türkistan'dan Türkiye'ye Devlet Anlayışında Süreklilik ve Değişim", "#b45309", "#fffbeb")

    # Sol: Süreklilik (Korunan Türk Gelenekleri)
    s += '<rect x="28" y="55" width="340" height="235" rx="10" fill="#fff" stroke="#fcd34d" stroke-width="1.5"/>'
    s += '<rect x="28" y="55" width="340" height="30" rx="10" fill="#d97706"/>'
    s += '<text x="198" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">SÜREKLİLİK (Korunan Kadim Türk Gelenekleri)</text>'

    sur = [
        ("Kut Anlayışı:", "Yönetme yetkisinin İlahi kaynaklı olması"),
        ("Ülke Hanedanın Ortak Malı:", "Veraset sistemi ve taht kavgalarının sürmesi"),
        ("Töre ve Adalet:", "Örfi hukukun (Töre) devletin temeli kalması"),
        ("Türk Cihan Hâkimiyeti:", "Kızılelma ve dünyaya nizam verme ülküsü"),
        ("Semboller:", "Otağ, taht, tuğ, sancak, nevbet (davul), ok-yay"),
    ]
    for i, (b, ac) in enumerate(sur):
        y = 96 + i * 36
        s += f'<circle cx="44" cy="{y+8}" r="4" fill="#d97706"/>'
        s += f'<text x="56" y="{y+12}" fill="#92400e" font-size="11" font-weight="700">{b}</text>'
        s += f'<text x="56" y="{y+26}" fill="#334155" font-size="10">{ac}</text>'

    # Sağ: Değişim (İslamiyet ve İran/Abbasi Etkisiyle Eklenenler)
    s += '<rect x="392" y="55" width="340" height="235" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<rect x="392" y="55" width="340" height="30" rx="10" fill="#059669"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">DEĞİŞİM (İslami Dönem ve Yeni Kurumlar)</text>'

    deg = [
        ("Kut -> Allah'ın Takdiri:", "Gök Tanrı yerine 'Zillullah fi'l-arz' (Allah'ın gölgesi)"),
        ("Cihat ve Gaza Ruhuna Geçiş:", "Cihan hâkimiyeti ülküsünün İla-yı Kelimetullah olması"),
        ("Yeni Unvanlar:", "Sultan, Padişah, Şah, Keyhüsrev, Keykubat, Keykavus"),
        ("İslami Hükümdarlık Alametleri:", "Hutbe okutmak, Halifeden menşur almak, Tıraz/Hil'at"),
        ("Kurumsal Divan Teşkilatı:", "Kurultay (Toy) yerine uzmanlaşmış Divan-ı Saltanat"),
    ]
    for i, (b, ac) in enumerate(deg):
        y = 96 + i * 36
        s += f'<circle cx="408" cy="{y+8}" r="4" fill="#059669"/>'
        s += f'<text x="420" y="{y+12}" fill="#065f46" font-size="11" font-weight="700">{b}</text>'
        s += f'<text x="420" y="{y+26}" fill="#334155" font-size="10">{ac}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Büyük Selçuklu ve Türkiye Selçuklu Divan Teşkilatı Şeması."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Selçuklularda Merkez Yönetim: Divan-ı Saltanat (Büyük Divan) ve Alt Divanlar", "#1d4ed8", "#eff6ff")

    # Üst Merkez: Divan-ı Saltanat
    s += '<rect x="240" y="52" width="280" height="48" rx="10" fill="#1e40af" stroke="#1e3a8a" stroke-width="1.5"/>'
    s += '<text x="380" y="73" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">DİVAN-I SALTANAT (Büyük Divan)</text>'
    s += '<text x="380" y="91" text-anchor="middle" fill="#bfdbfe" font-size="10.5">Başkanı: Vezir (Sahib-i Divan-ı Devlet)</text>'

    # Bağlantı çizgileri
    for x in [105, 288, 472, 655]:
        s += f'<line x1="380" y1="100" x2="{x}" y2="132" stroke="#3b82f6" stroke-width="1.6"/>'

    divanlar = [
        ("Divan-ı İnşa (Tuğra)", "Başkan: Tuğrai / Münşi", "İç ve dış yazışmaları,", "ferman ve menşurları", "hazırlar.", "#0284c7", "#e0f2fe"),
        ("Divan-ı İstifa", "Başkan: Müstevfi", "Devletin mali işlerini,", "gelir-gider bütçesini ve", "vergileri yönetir.", "#16a34a", "#dcfce7"),
        ("Divan-ı İşraf", "Başkan: Müşrif", "İdari ve mali kurumları", "denetler (Ordu ve", "yargıyı denetlemez!).", "#d97706", "#fef3c7"),
        ("Divan-ı Arz (Ceyş)", "Başkan: Emir-i Arz", "Ordunun maaş, teçhizat,", "ikta ve asker kayıt", "işlerine bakar.", "#dc2626", "#fef2f2"),
    ]
    for i, (ad, bsk, a1, a2, a3, r, bg) in enumerate(divanlar):
        x = 24 + i * 181
        s += f'<rect x="{x}" y="132" width="168" height="118" rx="9" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="132" width="168" height="26" rx="9" fill="{r}"/>'
        s += f'<text x="{x+84}" y="149" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{ad}</text>'
        s += f'<text x="{x+84}" y="172" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{bsk}</text>'
        s += f'<text x="{x+84}" y="192" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="207" text-anchor="middle" fill="#334155" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="222" text-anchor="middle" fill="#334155" font-size="10">{a3}</text>'

    # Alt Bilgi: Türkiye Selçuklu Farkları (Niyabet-i Saltanat ve Pervane)
    s += '<rect x="24" y="260" width="712" height="36" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.2"/>'
    s += '<text x="380" y="282" text-anchor="middle" fill="#1e3a8a" font-size="11" font-weight="700">Türkiye Selçuklularında Eklenenler: Niyabet-i Saltanat (Naib) ve Divan-ı Pervane (Pervaneci: İkta/Dirlik dağıtımı)</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Türk Ordu Teşkilatının Evrimi (Bozkır Atlılarından Gulam ve İkta Ordusuna)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Türk Ordu Teşkilatında Değişim: Millet Ordusundan Gulam ve İkta Sistemine", "#b91c1c", "#fef2f2")

    # Üst Kuşak: İlk Türk Devletleri vs Selçuklu Dönemi
    s += '<rect x="28" y="52" width="704" height="38" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>'
    s += '<text x="380" y="75" text-anchor="middle" fill="#991b1b" font-size="11.5" font-weight="700">İlk Türk Devletlerinde: Ücretsiz &quot;Ordu-Millet&quot; + Onlu Sistem  ===&gt;  Selçuklularda: Profesyonel Maaşlı (Gulam) + Toprağa Dayalı (İkta) Ordu</text>'

    birimler = [
        ("1. Gulaman-ı Saray", "Hükümdarın Özel Muhafızları", "Farklı milletlerden seçilip", "gulamhanede eğitilen, 3 ayda", "bir BİSTEGANİ maaşı alan", "daimi merkez ordusu.", "#991b1b", "#fff1f2"),
        ("2. Hassa Ordusu", "Merkez Süvari Kuvvetleri", "Doğrudan sultana bağlı,", "savaşta sultanın yakınında", "yer alan seçkin atlı", "türkmen ve gulam birlikleri.", "#b45309", "#fffbeb"),
        ("3. İkta (Sipahi) Askerleri", "Ordunun En Kalabalık Kısmı", "Hazinaden maaş almazlar!", "Kendilerine tahsis edilen ikta", "toprağının vergisiyle beslenen", "TAMAMEN TÜRK atlı askerler.", "#15803d", "#f0fdf4"),
        ("4. Türkmenler & Donanma", "Uç Kuvvetleri ve Deniz Gücü", "Sınır boylarında (Uç) gaza", "yapan Türkmenler ile Türkiye", "Selçuklularında kurulan", "DONANMA (Reisü'l-Bahr).", "#0369a1", "#f0f9ff"),
    ]
    for i, (bas, alt, a1, a2, a3, a4, r, bg) in enumerate(birimler):
        x = 26 + i * 179
        s += f'<rect x="{x}" y="102" width="171" height="190" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="102" width="171" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+85}" y="121" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+85}" y="146" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{alt}</text>'
        s += f'<text x="{x+85}" y="170" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+85}" y="186" text-anchor="middle" fill="#334155" font-size="10">{a2}</text>'
        s += f'<text x="{x+85}" y="202" text-anchor="middle" fill="#334155" font-size="10">{a3}</text>'
        s += f'<text x="{x+85}" y="218" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a4}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """İkta Sistemi Döngüsü ve Atabeylik Kurumu."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İkta Sisteminin İşleyişi ve Taşra Yönetiminde Atabeylik", "#047857", "#ecfdf5")

    # Sol: İkta Sistemi Döngüsü
    s += '<rect x="28" y="55" width="420" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="238" y="76" text-anchor="middle" fill="#065f46" font-size="12.5" font-weight="700">İkta (Dirlik) Sisteminin 4 Temel Kazanımı</text>'

    kazanim = [
        ("1. Üretimde Süreklilik:", "Mülkiyeti devlete (Miri) ait topraklar boş kalmaz, köylü toprağı işler."),
        ("2. Vergi Tahsilatı:", "Vergiler merkez hazineyi yormadan yerinde ikta sahibince toplanır."),
        ("3. Hazineden Para Çıkmadan Ordu:", "Toplanan vergilerle Cebeli (atlı sipahi) asker beslenir."),
        ("4. Taşra Güvenliği ve İskân:", "Bölgenin asayişi sağlanır, göçebe Türkmenler yerleşik hayata geçer."),
    ]
    for i, (b, ac) in enumerate(kazanim):
        y = 92 + i * 44
        s += f'<rect x="42" y="{y}" width="392" height="36" rx="6" fill="#f0fdf4" stroke="#10b981" stroke-width="1"/>'
        s += f'<text x="52" y="{y+15}" fill="#065f46" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="52" y="{y+29}" fill="#334155" font-size="9.8">{ac}</text>'

    # Sağ: Melik ve Atabeylik
    s += '<rect x="466" y="55" width="266" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="599" y="76" text-anchor="middle" fill="#065f46" font-size="12.5" font-weight="700">Eyalet Yönetimi: Melik &amp; Atabey</text>'

    s += '<rect x="482" y="92" width="234" height="80" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>'
    s += '<text x="599" y="112" text-anchor="middle" fill="#92400e" font-size="11" font-weight="700">İlk Türklerde: Şad / Tigin + Ataman (İnal)</text>'
    s += '<text x="599" y="132" text-anchor="middle" fill="#b45309" font-size="11" font-weight="700">Selçuklularda: Melik + ATABEY</text>'
    s += '<text x="599" y="152" text-anchor="middle" fill="#475569" font-size="9.8">Hanedan üyesi Melikler eyaletlere vali</text>'
    s += '<text x="599" y="165" text-anchor="middle" fill="#475569" font-size="9.8">atanır, tecrübeli komutan Atabey onları eğitir.</text>'

    s += '<rect x="482" y="184" width="234" height="86" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.2"/>'
    s += '<text x="599" y="204" text-anchor="middle" fill="#991b1b" font-size="11" font-weight="700">UYARI: Merkezi Otorite Zayıflarsa</text>'
    s += '<text x="599" y="224" text-anchor="middle" fill="#334155" font-size="9.8">Büyük Selçuklu\'da Atabeyler bağımsız</text>'
    s += '<text x="599" y="239" text-anchor="middle" fill="#334155" font-size="9.8">devletçikler (Zengiler, İldenizliler, Salgurlular)</text>'
    s += '<text x="599" y="255" text-anchor="middle" fill="#dc2626" font-size="10" font-weight="700">kurarak devletin parçalanmasını hızlandırmıştır.</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
