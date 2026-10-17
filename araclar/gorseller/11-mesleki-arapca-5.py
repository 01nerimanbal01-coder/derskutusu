def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">أَرْكَانُ الْإِيمَانِ السِّتَّةُ — İMANIN ALTI ŞARTI (ESASI)</text>'
    adimlar = [
        ("1-2. الإِيمَانُ بِاللّٰهِ وَمَلَائِكَتِهِ (Allah'a ve Meleklerine İman)", "آمَنْتُ بِاللّٰهِ التَّوْحِيدِ، وَبِمَلَائِكَتِهِ الْكِرَامِ (جبريل، ميكائيل، إسرافيل، ملك الموت).", "#059669", "#ECFDF5"),
        ("3-4. وَكُتُبِهِ وَرُسُلِهِ (İlahi Kitaplarına ve Peygamberlerine İman)", "الكُتُبُ السَّمَاوِيَّةُ (التَّوْرَاة، الزَّبُور، الإِنْجِيل، القُرْآن) وَالأَنْبِيَاءُ وَالرُّسُلُ.", "#2563EB", "#EFF6FF"),
        ("5. وَالْيَوْمِ الْآخِرِ (Ahiret Gününe İman)", "الإِيمَانُ بِالْبَعْثِ بَعْدَ الْمَوْتِ، وَالْحِسَابِ، وَالْمِيزَانِ، وَالْجَنَّةِ وَالنَّارِ.", "#7C3AED", "#F5F3FF"),
        ("6. وَبِالْقَدَرِ خَيْرِهِ وَشَرِّهِ (Kaza ve Kadere İman)", "الإِيمَانُ بِالْقَضَاءِ وَالْقَدَرِ أَنَّ خَيْرَهُ وَشَرَّهُ مِنَ اللّٰهِ تَعَالَى.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">الْمَلَائِكَةُ الْأَرْبَعَةُ وَوَظَائِفُهُمْ — DÖRT BÜYÜK MELEK VE GÖREVLERİ</text>'
    ic += _kart(20, 44, 310, 190, "جِبْرِيلُ وَمِيكَائِيلُ (CİBRİL VE MİKÂİL)", [
        "• جِبْرِيلُ (عليه السلام) — Cebrâil (a.s.):",
        "  مَلَكُ الْوَحْيِ: يُبَلِّغُ الْوَحْيَ مِنَ اللّٰهِ إِلَى الرُّسُلِ.",
        "  (Vahiy meleğidir; ilahi vahyi peygamberlere iletir.)",
        "• مِيكَائِيلُ (عليه السلام) — Mikâil (a.s.):",
        "  مَلَكٌ مُوَكَّلٌ بِالْأَرْزَاقِ وَالْأَمْطَارِ وَالْحَوَادِثِ الطَّبِيعِيَّةِ.",
        "  (Rızıklar, yağmurlar ve tabiat olaylarıyla görevlidir.)"
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "إِسْرَافِيلُ وَمَلَكُ الْمَوْتِ (İSRAFİL VE AZRAİL)", [
        "• إِسْرَافِيلُ (عليه السلام) — İsrâfil (a.s.):",
        "  مَلَكٌ مُوَكَّلٌ بِالنَّفْخِ فِي الصُّورِ يَوْمَ الْقِيَامَةِ.",
        "  (Kıyamet ve diriliş için Sûr'a üflemekle görevlidir.)",
        "• مَلَكُ الْمَوْتِ / عَزْرَائِيلُ — Ölüm Meleği (Azrâil):",
        "  مَلَكٌ مُوَكَّلٌ بِقَبْضِ الْأَرْوَاحِ عِنْدَ انْتِهَاءِ الْأَجَلِ.",
        "  (Eceli gelenlerin ruhunu kabzetmekle görevlidir.)"
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">الْكُتُبُ السَّمَاوِيَّةُ وَالرُّسُلُ — İLAHİ KİTAPLAR VE PEYGAMBERLER</text>'
    ic += _kart(20, 44, 310, 190, "الْكُتُبُ الْأَرْبَعَةُ (DÖRT BÜYÜK İLAHİ METİN)", [
        "• التَّوْرَاةُ: أُنْزِلَتْ عَلَى مُوسَى (عليه السلام).",
        "  (Tevrat: Hz. Musa'ya indirilmiştir.)",
        "• الزَّبُورُ: أُنْزِلَ عَلَى دَاوُدَ (عليه السلام).",
        "  (Zebur: Hz. Davud'a indirilmiştir.)",
        "• الْإِنْجِيلُ: أُنْزِلَ عَلَى عِيسَى (عليه السلام).",
        "  (İncil: Hz. İsa'ya indirilmiştir.)",
        "• الْقُرْآنُ الْكَرِيمُ: أُنْزِلَ عَلَى مُحَمَّدٍ (صلى الله عليه وسلم)."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "صِفَاتُ الرُّسُلِ الْوَاجِبَةُ (PEYGAMBER SIFATLARI)", [
        "• الصِّدْقُ (es-Sıdk): Doğruluk (Yalan söylememek).",
        "• الْأَمَانَةُ (el-Emâne): Güvenilir olmak.",
        "• التَّبْلِيغُ (et-Teblîğ): İlahi mesajları eksiksiz iletmek.",
        "• الْفَطَانَةُ (el-Fetâne): Üstün akıl ve zekâ sahibi olmak.",
        "• الْعِصْمَةُ (el-İsme): Günah işlemekten korunmuş olmak.",
        "• خَاتَمُ النَّبِيِّينَ: Son peygamber Hz. Muhammed'dir."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">أَسْمَاءُ اللّٰهِ الْحُسْنَى وَالتَّعْبِيرَاتُ الْعَقَدِيَّةُ</text>'
    ic += _kart(20, 44, 310, 190, "أَسْمَاءُ اللّٰهِ الْحُسْنَى (ESMA-İ HÜSNA)", [
        "• الرَّحْمٰنُ / الرَّحِيمُ: Çok merhametli ve bağışlayıcı.",
        "• الْمَلِكُ / الْقُدُّوسُ: Mülkün sahibi / Eksiklikten uzak.",
        "• السَّلَامُ / الْمُؤْمِنُ: Esenlik veren / Güven veren.",
        "• الْعَزِيزُ / الْحَكِيمُ: Mutlak galip / Hikmet sahibi.",
        "• الْخَالِقُ / الْبَارِئُ / الْمُصَوِّرُ: Yaratan ve şekil veren."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "تَعْبِيرَاتٌ مُهِمَّةٌ (ÖNEMLİ ARAPÇA KALIPLAR)", [
        "• أَرْكَانُ الْإِيمَانِ سِتَّةٌ (İmanın şartları altıdır).",
        "• التَّصْدِيقُ بِالْقَلْبِ وَالْإِقْرَارُ بِاللِّسَانِ (Kalple tasdik, dille ikrar).",
        "• الْيَوْمُ الْآخِرُ وَالْبَعْثُ بَعْدَ الْمَوْتِ (Ahiret günü ve diriliş).",
        "• الْقَضَاءُ وَالْقَدَرُ (Kaza ve kader).",
        "• لَا نُفَرِّقُ بَيْنَ أَحَدٍ مِنْ رُسُلِهِ (Elçileri ayırmayız)."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
