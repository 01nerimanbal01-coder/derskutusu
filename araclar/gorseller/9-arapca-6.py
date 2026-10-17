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
        'Arapçada Tekil Şahıs Zamirleri (الضَّمَائِرُ الْمُنْفَصِلَة) ve İşaret İsimleri</text>'
        + _kart(25, 42, 300, 145, "Ayrık Şahıs Zamirleri (Tekil)", [
            "• أَنَا (Ene): Ben (Eril ve dişil ortak)",
            "• أَنْتَ (Ente): Sen (Müzekker / Eril için)",
            "• أَنْتِ (Enti): Sen (Müennes / Dişil için)",
            "• هُوَ (Hüve): O (Müzekker / Eril için)",
            "• هِيَ (Hiye): O (Müennes / Dişil için)"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Yakın İşaret İsimleri (هٰذَا / هٰذِهِ)", [
            "• هٰذَا (Hâzâ): Bu (Müzekker / Eril varlıklar için)",
            "  Örnek: هٰذَا طَالِبٌ (Bu bir erkek öğrencidir)",
            "• هٰذِهِ (Hâzihî): Bu (Müennes / Dişil varlıklar için)",
            "  Örnek: هٰذِهِ طَالِبَةٌ (Bu bir kız öğrencidir)",
            "• Müennes kelimelerin sonunda genelde (ـة / ة) bulunur"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Belirlilik Takısı (ال / El-Takısı): Şemsî ve Kamerî Harfler</text>'
        + _kart(25, 42, 300, 145, "Kamerî Harfler (الْحُرُوفُ الْقَمَرِيَّة)", [
            "• El- (ال) takısındaki Lam (ل) harfi cezimli okunur",
            "• Örnek: اَلْقَمَرُ (el-kameru), اَلْمُعَلِّمُ (el-muallimu)",
            "• اَلْكِتَابُ (el-kitâbu), اَلْمَدْرَسَةُ (el-medresetü)",
            "• Belirlilik takısı alan kelimenin sonundaki tenvin",
            "  düşer, tek hareke kalır: كِتَابٌ -> اَلْكِتَابُ"
        ], "#0284c7", "#f0f9ff")
        + _kart(355, 42, 300, 145, "Şemsî Harfler (الْحُرُوفُ الشَّمْسِيَّة)", [
            "• El- (ال) takısındaki Lam (ل) okunmaz, sonraki",
            "  harf şeddeli okunur",
            "• Örnek: اَلشَّمْسُ (eş-şemsü), اَلطَّالِبُ (et-tâlibü)",
            "• اَلسَّلَامُ (es-selâmü), اَلصَّفُّ (es-saffü)",
            "• ت، ث، د، ذ، ر، ز، س، ش، ص، ض، ط، ظ، ل، ن"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Sınıf İçi Yönergelerde Emir Fiiller (Müzekker ve Müennes Hitap)</text>'
        + _kart(25, 42, 300, 145, "Müzekker (Erkek Öğrenciye) Emir", [
            "• اِجْلِسْ (İclis): Otur!  |  قُمْ (Kum): Kalk!",
            "• اِفْتَحْ (İftah): Aç!   |  أَغْلِقْ (Ağlik): Kapat!",
            "• اِقْرَأْ (İkra’): Oku!   |  اُكْتُبْ (Üktüb): Yaz!",
            "• اِسْتَمِعْ (İstemi’): Dinle! | اُنْظُرْ (Ünzur): Bak!",
            "• Son harfi cezimli (sükûnlu) olarak söylenir"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Müennes (Kız Öğrenciye) Emir (-î / ي Eki)", [
            "• اِجْلِسِي (İclisî): Otur! | قُومِي (Kûmî): Kalk!",
            "• اِفْتَحِي (İftahî): Aç!  | أَغْلِقِي (Ağlikî): Kapat!",
            "• اِقْرَئِي (İkraî): Oku!  | اُكْتُبِي (Üktübî): Yaz!",
            "• اِسْتَمِعِي (İstemiî): Dinle! | اُنْظُرِي (Ünzurî): Bak!",
            "• Müzekker emrin sonuna muhataba yâ’sı (ـِي) eklenir"
        ], "#ea580c", "#fff7ed")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Tanışma (التَّعَارُف) Diyaloğu ve Temel Soru Kalıpları</text>'
        + _kart(20, 42, 200, 138, "İsim ve Hal Sorma", [
            "• مَا اسْمُكَ؟ (Mesmüke? - Eril)",
            "• مَا اسْمُكِ؟ (Mesmüki? - Dişil)",
            "• اِسْمِي أَحْمَد / زَيْنَب",
            "• كَيْفَ حَالُكَ؟ -> بِخَيْرٍ، وَالْحَمْدُ لِلّٰه"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 138, "Kim ve Nereli Sorma", [
            "• مَنْ هٰذَا؟ (Men hâzâ? - Bu kim?)",
            "• مَنْ هٰذِهِ؟ (Men hâzihî?)",
            "• مِنْ أَيْنَ أَنْتَ؟ (Nerelisin?)",
            "• أَنَا مِنْ تُرْكِيَا (Türkiyeliyim)"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 138, "Memnuniyet ve Veda", [
            "• تَشَرَّفْتُ بِمَعْرِفَتِكَ",
            "  (Tanıştığımıza memnun oldum)",
            "• فُرْصَةٌ سَعِيدَةٌ (Güzel fırsat)",
            "• إِلَى اللِّقَاءِ / مَعَ السَّلَامَةِ"
        ], "#d97706", "#fffbeb")
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
