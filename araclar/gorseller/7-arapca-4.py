def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "GELECEK ZAMAN VE MESLEK HEDEFİ (مَاذَا سَتُصْبِحُ فِي الْمُسْتَقْبَلِ؟)", 13, "#1e3a8a", "bold")
    cols = [
        (28, "Yakın Gelecek Eki: سَـ (Se-)", "Muzâri fiilin başına gelir,", "'-ecek / -acak' anlamı katar:", "أَكونُ → سَأَكونُ (Olacağım)", "أُصْبِحُ → سَأُصْبِحُ (Olacağım)"),
        (362, "Örnek Soru ve Cevaplar", "ماذا سَتُصْبِحُ في الْمُسْتَقْبَلِ؟", "(Gelecekte ne olacaksın?)", "→ سَأُصْبِحُ طَبيبَةً في الْمُسْتَقْبَلِ.", "→ سَأَكونُ مُهَنْدِسًا ناجِحًا.")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
        ic += _metin(x+155, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+155, 98, s1, 11, "#1e293b", "bold")
        ic += _metin(x+155, 120, s2, 11, "#334155")
        ic += _metin(x+155, 144, s3, 12, "#1e40af", "bold")
        ic += _metin(x+155, 166, s4, 12, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "ARAPÇADA TEMEL BAĞLAÇLAR (حُرُوفُ الْعَطْفِ: وَ - أَوْ - أَمْ - ثُمَّ)", 13, "#166534", "bold")
    cols = [
        (25, "وَ (Ve)", "'Ve / ile' anlamında", "iki kelimeyi birleştirir:", "أَبي مُهَنْدِسٌ وَأُمّي مُدَرِّسَةٌ"),
        (192, "أَوْ (Ev)", "'Veya / ya da' anlamında", "düz cümlede seçenek sunar:", "سَأَكونُ طَبيبًا أَوْ صَيْدَلِيًّا"),
        (359, "أَمْ (Em)", "'Yoksa' anlamında", "أَ / هَلْ sorusunda kullanılır:", "أَأَنْتَ طالِبٌ أَمْ مُعَلِّمٌ؟"),
        (526, "ثُمَّ (Sümme)", "'Sonra / daha sonra'", "zaman aralıklı sıralama:", "أَدْرُسُ ثُمَّ أَنامُ")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 13, "#15803d", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 120, s2, 10, "#334155")
        ic += _metin(x+75, 148, s3, 10, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "GÜNLÜK KONUŞMADA ÜNLEM VE TEPKİ İFADELERİ", 14, "#92400e", "bold")
    items = [
        (25, "يا سَلام! (Yâ selâm!)", "Ne güzel! / Harika!", "(Beğeni ve hayranlık)"),
        (192, "حَقًّا؟ (Hakkan?)", "Gerçekten mi? / Ciddi misin?", "(Şaşkınlık ve doğrulama)"),
        (359, "آسِف / آسِفَة", "Âsif (E) / Âsife (K)", "Üzgünüm / Özür dilerim"),
        (526, "آه! (Âh!)", "Ah! / Eyvah! / Haa!", "(Hatırlama veya üzüntü)")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 48, 150, 132, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+75, 76, b, 12, "#b45309", "bold")
        ic += _metin(x+75, 108, s1, 10, "#1e293b", "bold")
        ic += _metin(x+75, 130, s2, 10, "#64748b")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "MESLEK TEMASI DEĞERLERİMİZ: AZİM, SAYGI VE TEVEKKÜL", 13, "#6b21a8", "bold")
    rows = [
        (50, "Saygı (الْاِحْتِرامُ)", "اَلطّالِبُ يَحْتَرِمُ الْمُدَرِّسَ.", "Öğrenci öğretmene saygı duyar."),
        (96, "Azim (الْعَزْمُ)", "اَلطّالِبُ عازِمٌ عَلى النَّجاحِ.", "Öğrenci başarmaya azimlidir (kararlıdır)."),
        (142, "Tevekkül (التَّوَكُّلُ)", "اَلْمُسْلِمُ يَتَوَكَّلُ عَلى اللّٰهِ.", "Müslüman (çalışıp) Allah'a tevekkül eder.")
    ]
    for y, tur, ar, tr in rows:
        ic += _kutu(25, y, 130, 38, "#f3e8ff", "#9333ea", 8, 1.5)
        ic += _metin(90, y+24, tur, 11, "#581c87", "bold")
        ic += _kutu(165, y, 260, 38, "#ffffff", "#d8b4fe", 8, 1.2)
        ic += _metin(295, y+24, ar, 13, "#1e293b", "bold")
        ic += _metin(560, y+24, tr, 11, "#334155")
    return _svg(700, 205, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
