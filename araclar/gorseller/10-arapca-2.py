from ozet_gorsel import svg


def _gorsel_1():
    w, h = 620, 230
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">MUHATAP (2. ŞAHIS) VE MÜTEKELLİM (1. ŞAHIS) ZAMİRLERİYLE MESLEKLER</text>')
    # Sol: Muhatap
    ic.append('<rect x="22" y="45" width="335" height="165" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>')
    ic.append('<text x="190" y="65" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">MUHATAP ZAMİRLERİ (Karşımızdaki Kişiler)</text>')
    rows = [
        ("أَنْتَ (Sen - Erkek)", "أَنْتَ مُتَقَاعِدٌ / أَنْتَ مُدَرِّسٌ"),
        ("أَنْتِ (Sen - Kadın)", "أَنْتِ مُوَظَّفَةٌ / أَنْتِ مُدَرِّسَةٌ"),
        ("أَنْتُمَا (İkiniz - Eril/Dişil)", "أَنْتُمَا مُهَنْدِسَانِ / طَبِيبَتَانِ"),
        ("أَنْتُمْ (Siz - Erkekler)", "أَنْتُمْ مُدَرِّسُونَ / عَامِلُونَ"),
        ("أَنْتُنَّ (Siz - Kadınlar)", "أَنْتُنَّ مُهَنْدِسَاتٌ / طَبِيبَاتٌ"),
    ]
    for idx, (z, ex) in enumerate(rows):
        y = 84 + idx * 25
        ic.append(f'<text x="34" y="{y}" font-size="9.5" font-weight="700" fill="#1e3a8a">{z}:</text>')
        ic.append(f'<text x="175" y="{y}" font-size="10" fill="#1e293b">{ex}</text>')
    # Sağ: Mütekellim
    ic.append('<rect x="368" y="45" width="230" height="165" rx="10" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>')
    ic.append('<text x="483" y="65" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">MÜTEKELLİM (Ben / Biz)</text>')
    ic.append('<rect x="380" y="76" width="206" height="52" rx="6" fill="#ffffff" stroke="#86efac"/>')
    ic.append('<text x="483" y="94" text-anchor="middle" font-size="10" font-weight="700" fill="#166534">أَنَا (Ben — Tekil Eril/Dişil)</text>')
    ic.append('<text x="483" y="112" text-anchor="middle" font-size="9.5" fill="#1e293b">أَنَا مُدَرِّسٌ / أَنَا مُدَرِّسَةٌ</text>')
    ic.append('<rect x="380" y="136" width="206" height="64" rx="6" fill="#ffffff" stroke="#86efac"/>')
    ic.append('<text x="483" y="154" text-anchor="middle" font-size="10" font-weight="700" fill="#166534">نَحْنُ (Biz — İkil ve Çoğul!)</text>')
    ic.append('<text x="483" y="172" text-anchor="middle" font-size="9.5" fill="#1e293b">İkil: نَحْنُ مُهَنْدِسَانِ / مُهَنْدِسَتَانِ</text>')
    ic.append('<text x="483" y="188" text-anchor="middle" font-size="9.5" fill="#1e293b">Çoğul: نَحْنُ طَبَّاخُونَ / طَبَّاخَاتٌ</text>')
    return svg(w, h, "".join(ic), "Muhatap ve mütekellim zamirleriyle meslek uyum tablosu")


def _gorsel_2():
    w, h = 620, 235
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">هَيَّا نَتَعَرَّفْ عَلَى أُسْرَتِي — AİLE BİREYLERİ, MESLEKLERİ VE GÖREVLERİ</text>')
    cards = [
        (25, 46, "وَالِدِي (Babam)", "مُحَامٍ (Avukat)", "يُدَافِعُ عَنِ الْعَدَالَةِ", "#eff6ff", "#3b82f6", "#1d4ed8"),
        (220, 46, "وَالِدَتِي (Annem)", "رَبَّةُ الْبَيْتِ (Ev hanımı)", "تَهْتَمُّ بِعَائِلَتِنَا", "#fdf2f8", "#ec4899", "#be185d"),
        (415, 46, "أَخِي وَأُخْتِي (Kardeşlerim)", "طَبِيبٌ / مُدَرِّسَةٌ", "يَفْحَصُ الْمَرْضَى / تُدَرِّسُ", "#f0fdf4", "#22c55e", "#15803d"),
        (25, 134, "عَمِّي (Amcam)", "شُرْطِيٌّ (Polis)", "يُحَافِظُ عَلَى الْوَطَنِ", "#fffbeb", "#f59e0b", "#b45309"),
        (220, 134, "عَمَّتِي (Halam)", "مُهَنْدِسَةٌ (Mühendis)", "تَعْمَلُ فِي الشَّرِكَةِ", "#faf5ff", "#a855f7", "#7e22ce"),
        (415, 134, "أَنَا (Ben)", "سَائِقٌ (Şoför)", "أَسُوقُ سَيَّارَةَ أُجْرَةٍ", "#ecfeff", "#06b6d4", "#0e7490"),
    ]
    for x, y, person, job, act, bg, st, tc in cards:
        ic.append(f'<rect x="{x}" y="{y}" width="180" height="76" rx="10" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+90}" y="{y+20}" text-anchor="middle" font-size="10" font-weight="700" fill="{tc}">{person}</text>')
        ic.append(f'<text x="{x+90}" y="{y+40}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#1e293b">{job}</text>')
        ic.append(f'<text x="{x+90}" y="{y+60}" text-anchor="middle" font-size="9.5" fill="#475569">{act}</text>')
    return svg(w, h, "".join(ic), "Ailemle Tanışalım metnindeki akrabalar, meslekleri ve görevleri")


def _gorsel_3():
    w, h = 620, 220
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#fffbeb" stroke="#fcd34d"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#92400e">MÜZARİ FİİLLERDE TEKİL (MÜFRED) VE İKİL (MÜSENNA) DÖNÜŞÜMÜ</text>')
    pairs = [
        (25, 48, "3. Şahıs Eril (هُوَ → هُمَا)", "هُوَ يَسُوقُ سَيَّارَةَ أُجْرَةٍ", "هُمَا يَسُوقَانِ سَيَّارَةَ أُجْرَةٍ"),
        (320, 48, "3. Şahıs Dişil (هِيَ → هُمَا)", "هِيَ تُحَافِظُ عَلَى الْوَطَنِ", "هُمَا تُحَافِظَانِ عَلَى الْوَطَنِ"),
        (25, 130, "2. Şahıs Eril (أَنْتَ → أَنْتُمَا)", "أَنْتَ تَفْحَصُ الْمَرْضَى", "أَنْتُمَا تَفْحَصَانِ الْمَرْضَى"),
        (320, 130, "2. Şahıs Dişil (أَنْتِ → أَنْتُمَا)", "أَنْتِ تُدَرِّسِينَ الدُّرُوسَ", "أَنْتُمَا تُدَرِّسَانِ الدُّرُوسَ"),
    ]
    for x, y, title, s1, s2 in pairs:
        ic.append(f'<rect x="{x}" y="{y}" width="275" height="70" rx="8" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+137}" y="{y+18}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#b45309">{title}</text>')
        ic.append(f'<text x="{x+137}" y="{y+38}" text-anchor="middle" font-size="9.5" fill="#1e293b">Tekil: {s1}</text>')
        ic.append(f'<text x="{x+137}" y="{y+56}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#15803d">İkil: {s2}</text>')
    return svg(w, h, "".join(ic), "Müzari fiillerin tekil ve ikil çekim örnekleri")


def _gorsel_4():
    w, h = 620, 225
    ic = []
    ic.append(f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>')
    ic.append(f'<text x="{w//2}" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#1e293b">MESLEKLERİN ÇOĞULLARI (الْمُفْرَد وَالْجَمْع) VE İBRAHİM SURESİ 41. AYET</text>')
    cols = [
        (25, "Kurallı Eril (ـونَ)", "#eff6ff", "#3b82f6", "#1d4ed8", ["مُدَرِّسٌ ← مُدَرِّسُونَ", "سَائِقٌ ← سَائِقُونَ", "مُوَظَّفٌ ← مُوَظَّفُونَ"]),
        (220, "Kurallı Dişil (ـاتٌ)", "#fdf2f8", "#ec4899", "#be185d", ["مُهَنْدِسَةٌ ← مُهَنْدِسَاتٌ", "مُمَرِّضَةٌ ← مُمَرِّضَاتٌ", "مُوَظَّفَةٌ ← مُوَظَّفَاتٌ"]),
        (415, "Kırık Çoğul (التَّكْسِير)", "#f0fdf4", "#22c55e", "#15803d", ["طَبِيبٌ ← أَطِبَّاءُ (Doktorlar)", "عَامِلٌ ← عُمَّالٌ (İşçiler)", "(Ezberlenmesi gerekir!)"]),
    ]
    for x, title, bg, st, tc, lines in cols:
        ic.append(f'<rect x="{x}" y="44" width="180" height="96" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.5"/>')
        ic.append(f'<text x="{x+90}" y="62" text-anchor="middle" font-size="10" font-weight="700" fill="{tc}">{title}</text>')
        for i, ln in enumerate(lines):
            ic.append(f'<text x="{x+90}" y="{82+i*19}" text-anchor="middle" font-size="9.5" fill="#1e293b">{ln}</text>')
    # Alt: İbrahim 41
    ic.append('<rect x="25" y="150" width="570" height="56" rx="10" fill="#fefce8" stroke="#eab308" stroke-width="1.5"/>')
    ic.append('<text x="310" y="172" text-anchor="middle" font-size="11.5" font-weight="700" fill="#854d0e">﴿ رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ ﴾ (سورة إبراهيم، ٤١)</text>')
    ic.append('<text x="310" y="194" text-anchor="middle" font-size="9.5" fill="#1e293b">"Rabbimiz! Hesap kurulacağı gün beni, ana-babamı ve müminleri bağışla!" (İbrahim suresi, 41. ayet)</text>')
    return svg(w, h, "".join(ic), "Mesleklerin çoğul türleri ve İbrahim suresi 41. ayet duası")


def uygula(v):
    gorseller = [_gorsel_1(), _gorsel_2(), _gorsel_3(), None, _gorsel_4(), None]
    for i, g in enumerate(gorseller):
        if g and i < len(v["bolumler"]):
            v["bolumler"][i]["gorsel"] = g
