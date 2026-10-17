def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Güzel Davranışlarım (مُعَامَلَاتِي الْحَسَنَة) ve Sosyal İfadeler</text>'
        + _kart(25, 42, 300, 145, "Temel Fiiller ve Kavramlar", [
            "• يَرْحَمُ (Merhamet eder) | يَشْكُرُ (Şükreder/Teşekkür eder)",
            "• يُكْرِمُ (İkram eder)   | يُسَاعِدُ (Yardım eder)",
            "• كِبَار / مُسِنِّين (Büyükler / Yaşlılar) | صِغَار (Küçükler)",
            "• ضُيُوف (Misafirler) | جَار (Komşu) | مُحْتَاجِين (Muhtaçlar)",
            "• تَعَاوُن (Yardımlaşma) | صَادِق (Dürüst) | صَبُور (Sabırlı)"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Dualar, Tebrikler ve Hadis-i Şerif", [
            "• جَزَاكَ اللّٰهُ خَيْرًا (Allah seni hayırla mükâfatlandırsın)",
            "• بَارَكَ اللّٰهُ فِيكَ (Allah seni mübarek kılsın)",
            "• كُلُّ عَامٍ وَأَنْتُمْ بِخَيْرٍ (Bayramınız kutlu olsun / Nice yıllara)",
            "• Hadis: «تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ صَدَقَةٌ»",
            "  (Kardeşinin yüzüne tebessüm etmen sadakadır)"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Çoğul Şahıs Zamirleri ve Müzari (Geniş/Şimdiki Zaman) Fiil Çekimi</text>'
        + _kart(25, 42, 300, 145, "Çoğul Ayrık Zamirler (الضَّمَائِر)", [
            "• نَحْنُ (Nahnü): Biz (Eril ve dişil ortak)",
            "• أَنْتُمْ (Entüm): Siz (Eril çoğul - erkekler)",
            "• أَنْتُنَّ (Entünne): Siz (Dişil çoğul - kadınlar)",
            "• هُمْ (Hüm): Onlar (Eril çoğul - erkekler)",
            "• هُنَّ (Hünne): Onlar (Dişil çoğul - kadınlar)"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 145, "Müzari Fiil Çoğul Çekimi (يَذْهَبُ - Gider)", [
            "• نَحْنُ نَذْهَبُ (Biz gidiyoruz - Başına نـ gelir)",
            "• أَنْتُمْ تَذْهَبُونَ (Siz gidiyorsunuz [E] -> تَـ ... ـُونَ)",
            "• أَنْتُنَّ تَذْهَبْنَ (Siz gidiyorsunuz [K] -> تَـ ... ـْنَ)",
            "• هُمْ يَذْهَبُونَ (Onlar gidiyorlar [E] -> يَـ ... ـُونَ)",
            "• هُنَّ يَذْهَبْنَ (Onlar gidiyorlar [K] -> يَـ ... ـْنَ)"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Gereklilik ve Öğüt Kalıpları: كُنْ / لَا تَكُنْ ve يَجِبُ أَنْ</text>'
        + _kart(25, 42, 300, 142, "Olumlu ve Olumsuz Öğüt (كُنْ ... وَلَا تَكُنْ)", [
            "• كُنْ صَادِقًا وَلَا تَكُنْ كَاذِبًا!",
            "  (Dürüst ol, yalancı olma!)",
            "• كُنْ صَبُورًا وَلَا تَكُنْ عَجُولًا!",
            "  (Sabırlı ol, aceleci olma!)",
            "• كُنْ / تَكُنْ fiilinin haberi mansup (ـًا) gelir"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 142, "Gereklilik Kalıbı (يَجِبُ أَنْ / أَلَّا)", [
            "• يَجِبُ أَنْ نُسَاعِدَ الْمُحْتَاجِينَ (Muhtaçlara yardım",
            "  etmemiz gerekir)",
            "• يَجِبُ أَنْ يَكُونَ الْمُسْلِمُ أَمِينًا (Müslümanın",
            "  güvenilir olması gerekir)",
            "• دَائِمًا (Daima / Her zaman) | أَبَدًا (Asla)"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Zaman Zarfları (مَتَى / قَبْلَ / بَعْدَ) ve Duygu Sıfatları</text>'
        + _kart(25, 42, 300, 138, "Zaman Sorma: مَتَى (Ne Zaman?)", [
            "• مَتَى تَزُورُ أَقْرِبَاءَكَ؟ (Akrabalarını ne zaman",
            "  ziyaret edersin?)",
            "• قَبْلَ الدَّرْسِ (Dersten önce) | بَعْدَ الصَّلَاةِ (Namazdan sonra)",
            "• فِي أَيَّامِ الْأَعْيَادِ (Bayram günlerinde)"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Duygu ve Durum Sıfatları", [
            "• مَبْسُوط / سَعِيد (Mutlu, sevinçli)",
            "• حَزِين (Üzgün)  |  غَضْبَان (Öfkeli, kızgın)",
            "• قَلِق (Endişeli, kaygılı)  |  مُتَعَجِّب (Şaşkın)",
            "• هَلْ يُمْكِنُ أَنْ تُسَاعِدَنِي؟ (Bana yardım edebilir misin?)"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
