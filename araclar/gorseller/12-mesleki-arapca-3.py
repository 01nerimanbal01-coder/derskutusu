def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "الْأَسْمَاءُ الْحُسْنَى (EL-ESMÂÜ'L-HÜSNÂ: ALLAH'IN GÜZEL İSİMLERİ)", 13, "#166534", "bold")
    cols = [
        (25, "الرَّحْمٰنُ - الرَّحِيمُ", "er-Rahmân / er-Rahîm", "Sonsuz merhamet ve", "şefkat sahibi"),
        (192, "الْمَلِكُ - الْقُدُّوسُ", "el-Melik / el-Kuddûs", "Mülkün sahibi, her türlü", "eksiklikten münezzeh"),
        (359, "السَّلَامُ - الْمُؤْمِنُ", "es-Selâm / el-Mü'min", "Esenlik veren, kalplere", "güven ve emniyet bağışlayan"),
        (526, "الْعَزِيزُ - الْحَكِيمُ", "el-Azîz / el-Hakîm", "Mutlak güç ve", "hikmet sahibi")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 74, b, 13, "#15803d", "bold")
        ic += _metin(x+75, 100, s1, 11, "#1e293b", "bold")
        ic += _metin(x+75, 124, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#334155")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 200, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "أَقْسَامُ الْفِعْلِ الْمُعْتَلِّ (MU'TEL FİİLİN DÖRT KISMI)", 14, "#1e3a8a", "bold")
    cols = [
        (25, "1. الْمِثَالُ (Misal)", "İlk harfi illetli", "وَعَدَ - وَجَدَ - يَئِسَ", "(Fâü'l-fiili illetli)"),
        (192, "2. الْأَجْوَفُ (Ecvef)", "Orta harfi illetli", "قَالَ - بَاعَ - خَافَ", "(Aynü'l-fiili illetli)"),
        (359, "3. النَّاقِصُ (Nâkıs)", "Son harfi illetli", "دَعَا - رَمَى - رَضِيَ", "(Lâmü'l-fiili illetli)"),
        (526, "4. اللَّفِيفُ (Lefîf)", "İki harfi illetli", "وَفَى (Mefrûk)", "طَوَى - رَوَى (Makrûn)")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 144, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+75, 98, s1, 11, "#334155")
        ic += _metin(x+75, 126, s2, 13, "#1e40af", "bold")
        ic += _metin(x+75, 152, s3, 10, "#475569")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "LEFÎF FİİLİN İKİ TÜRÜ: LEFÎF-İ MEFRÛK VE LEFÎF-İ MAKRÛN", 13, "#92400e", "bold")
    ic += _kutu(28, 48, 310, 132, "#ffffff", "#f59e0b", 10, 1.8)
    ic += _metin(183, 72, "اللَّفِيفُ الْمَفْرُوقُ (Lefîf-i Mefrûk)", 12, "#b45309", "bold")
    ic += _metin(183, 98, "1. ve 3. kök harfi illetli, ortası sahih:", 11, "#334155")
    ic += _metin(183, 124, "وَقَى (korudu) • وَفَى (sözünü tuttu) • وَعَى (kavradı)", 12, "#1e293b", "bold")
    ic += _metin(183, 150, "(İki illet harfinin arası ayrılmış: Mefrûk)", 10, "#64748b")

    ic += _kutu(362, 48, 310, 132, "#ffffff", "#f59e0b", 10, 1.8)
    ic += _metin(517, 72, "اللَّفِيفُ الْمَقْرُونُ (Lefîf-i Makrûn)", 12, "#b45309", "bold")
    ic += _metin(517, 98, "2. ve 3. kök harfi peş peşe illetli:", 11, "#334155")
    ic += _metin(517, 124, "طَوَى (katladı) • رَوَى (rivayet etti) • نَوَى (niyet etti)", 12, "#1e293b", "bold")
    ic += _metin(517, 150, "(İki illet harfi yan yana gelmiş: Makrûn)", 10, "#64748b")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "SAHİH VE MU'TEL FİİL KARŞILAŞTIRMASI (ÖZET TABLO)", 14, "#6b21a8", "bold")
    ic += _kutu(28, 48, 310, 126, "#ffffff", "#c084fc", 9, 1.5)
    ic += _metin(183, 72, "الْفِعْلُ الصَّحِيحُ (Sahih Fiil)", 12, "#7e22ce", "bold")
    ic += _metin(183, 98, "Kök harflerinde illet harfi (و - ا - ي) YOKTUR:", 11, "#334155")
    ic += _metin(183, 124, "1. Sâlim (كَتَبَ)  2. Mehmûz (أَخَذَ)  3. Mudâaf (مَدَّ)", 11, "#1e293b", "bold")

    ic += _kutu(362, 48, 310, 126, "#ffffff", "#c084fc", 9, 1.5)
    ic += _metin(517, 72, "الْفِعْلُ الْمُعْتَلُّ (Mu'tel Fiil)", 12, "#7e22ce", "bold")
    ic += _metin(517, 98, "Kök harflerinde illet harfi (و - ا - ي) VARDIR:", 11, "#334155")
    ic += _metin(517, 124, "1. Misal (وَعَدَ) 2. Ecvef (قَالَ) 3. Nâkıs (دَعَا) 4. Lefîf (وَقَى)", 11, "#1e293b", "bold")
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