def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Nefis Tezkiyesi ve Güzel Ahlak Temel Kavramları (التَّزْكِيَةُ وَالْأَخْلَاقُ)</text>'
    ic += _kart(20, 45, 230, 185, "Nefis ve Tezkiye Kavramları", [
        "• تَزْكِيَةُ النَّفْسِ : Nefis tezkiyesi (arınma)",
        "• مُحَاسَبَةُ النَّفْسِ : Nefis muhasebesi",
        "• التَّقْوَى : Takva (Allah\'a karşı sorumluluk)",
        "• الْإِخْلَاصُ : İhlas (samimiyet)",
        "• التَّوْبَةُ : Tövbe ve istiğfar"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "Övülen Ahlak (الْأَخْلَاقُ الْحَمِيدَةُ)", [
        "• الصِّدْقُ : Doğruluk ve dürüstlük",
        "• التَّوَاضُعُ : Tevazu (alçakgönüllülük)",
        "• الصَّبْرُ وَالْحِلْمُ : Sabır ve yumuşak huyluluk",
        "• الْعَفْوُ وَالْإِحْسَانُ : Affedicilik ve ihsan",
        "• الْحَيَاءُ وَالْعِفَّةُ : Haya ve iffet"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "Yerilen Huylar (الْأَخْلَاقُ الذَّمِيمَةُ)", [
        "• الْكِبْرُ وَالْغُرُورُ : Kibir ve gurur",
        "• الْحَسَدُ وَالْبُغْضُ : Haset ve kin",
        "• الْغِيبَةُ وَالنَّمِيمَةُ : Gıybet ve koğuculuk",
        "• الرِّيَاءُ وَالنِّفَاقُ : Gösteriş ve münafıklık",
        "• الْبُخْلُ وَالْإِسْرَافُ : Cimrilik ve israf"
    ], "#be123c", "#fff1f2")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Sülâsî Mezîd Fiiller (I): Rubâî (4 Harfli) Bâblar (أَفْعَلَ - فَعَّلَ - فَاعَلَ)</text>'
    ic += _kart(20, 45, 230, 185, "1. İf\'âl Bâbı (إِفْعَالٌ)", [
        "• Mazi: أَفْعَلَ (أَحْسَنَ - أَكْرَمَ)",
        "• Muzari: يُفْعِلُ (يُحْسِنُ - يُكْرِمُ)",
        "• Emir: أَفْعِلْ (أَحْسِنْ - أَكْرِمْ)",
        "• Mastar: إِفْعَالٌ (إِحْسَانٌ - إِكْرَامٌ)",
        "• Anlam: Geçişlilik (Tadiye)"
    ], "#2563eb", "#eff6ff")
    ic += _kart(265, 45, 230, 185, "2. Tef\'îl Bâbı (تَفْعِيلٌ)", [
        "• Mazi: فَعَّلَ (زَكَّى - طَهَّرَ - هَذَّبَ)",
        "• Muzari: يُفَعِّلُ (يُزَكِّي - يُطَهِّرُ)",
        "• Emir: فَعِّلْ (زَكِّ - طَهِّرْ)",
        "• Mastar: تَفْعِيلٌ / تَفْعِلَةٌ (تَزْكِيَةٌ - تَطْهِيرٌ)",
        "• Anlam: Çokluk (Teksîr) ve geçişlilik"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 185, "3. Müfâale Bâbı (مُفَاعَلَةٌ)", [
        "• Mazi: فَاعَلَ (حَاسَبَ - جَاهَدَ - صَابَرَ)",
        "• Muzari: يُفَاعِلُ (يُحَاسِبُ - يُجَاهِدُ)",
        "• Emir: فَاعِلْ (حَاسِبْ - جَاهِدْ)",
        "• Mastar: مُفَاعَلَةٌ / فِعَالٌ (مُحَاسَبَةٌ - جِهَادٌ)",
        "• Anlam: İşteşlik (Müşâreke) ve gayret"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Sülâsî Mezîd Fiiller (II): Humâsî (5 Harfli) ve Südâsî (6 Harfli) Bâblar</text>'
    ic += _kart(20, 45, 230, 185, "Tefe\'\'ul ve Tefâ\'ul Bâbları", [
        "• تَفَعَّلَ - يَتَفَعَّلُ - تَفَعُّلٌ",
        "  Örn: تَخَلَّقَ (Ahlaklandı), تَكَبَّرَ",
        "• تَفَاعَلَ - يَتَفَاعَلُ - تَفَاعُلٌ",
        "  Örn: تَوَاضَعَ (Tevazu gösterdi), تَسَامَحَ",
        "• Anlam: Dönüşlülük (Mutâvaat) ve işteşlik"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(265, 45, 230, 185, "İfti\'âl ve İnfi\'âl Bâbları", [
        "• اِفْتَعَلَ - يَفْتَعِلُ - اِفْتِعَالٌ",
        "  Örn: اِجْتَنَبَ (Kaçındı), اِتَّقَى (Sakındı)",
        "• اِنْفَعَلَ - يَنْفَعِلُ - اِنْفِعَالٌ",
        "  Örn: اِنْطَلَقَ (Yola koyuldu), اِنْكَسَرَ",
        "• Anlam: Gayret ve dönüşlülük"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 185, "İstif\'âl Bâbı (6 Harfli)", [
        "• Mazi: اِسْتَفْعَلَ (اِسْتَغْفَرَ - اِسْتَقَامَ)",
        "• Muzari: يَسْتَفْعِلُ (يَسْتَغْفِرُ - يَسْتَقِيمُ)",
        "• Emir: اِسْتَفْعِلْ (اِسْتَغْفِرْ - اِسْتَقِمْ)",
        "• Mastar: اِسْتِفْعَالٌ (اِسْتِغْفَارٌ - اِسْتِقَامَةٌ)",
        "• Anlam: Talep / İsteme (Mağfiret dileme)"
    ], "#9333ea", "#faf5ff")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Nefis Tezkiyesi ve Güzel Ahlak İle İlgili Ayet ve Hadis Kalıpları</text>'
    ic += _kart(20, 45, 350, 175, "Kur\'an-ı Kerim\'de Nefis Tezkiyesi (Şems, 9-10)", [
        "• قَدْ أَفْلَحَ مَنْ زَكَّاهَا : Nefsini arındıran kurtuluşa ermiştir",
        "• وَقَدْ خَابَ مَنْ دَسَّاهَا : Onu günaha gömen ise ziyan etmiştir",
        "• أَفْلَحَ : İf\'âl bâbı mazi fiil (Kurtuluşa erdi)",
        "• زَكَّى : Tef\'îl bâbı nakıs mazi fiil (Arındırdı / Temizledi)",
        "• مَنْ + مَاضٍ : Şart-cevap üslubu ile kesin ilahi hüküm"
    ], "#15803d", "#f0fdf4")
    ic += _kart(390, 45, 350, 175, "Hadis-i Şeriflerde Güzel Ahlak Kalıpları", [
        "• إِنَّمَا بُعِثْتُ لِأُتَمِّمَ مَكَارِمَ الْأَخْلَاقِ (Güzel ahlakı tamamlamak)",
        "• اِتَّقِ اللَّهَ حَيْثُمَا كُنْتَ (Nerede olursan ol Allah\'tan sakın)",
        "• وَخَالِقِ النَّاسَ بِخُلُقٍ حَسَنٍ (İnsanlara güzel ahlakla muamele et)",
        "• حَاسِبُوا أَنْفُسَكُمْ قَبْلَ أَنْ تُحَاسَبُوا (Hesaba çekilmeden muhasebe yapın)",
        "• أُتَمِّمَ (Tef\'îl), خَالِقْ ve حَاسِبُوا (Müfâale), اِتَّقِ (İfti\'âl)"
    ], "#0369a1", "#f0f9ff")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]