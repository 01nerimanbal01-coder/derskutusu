def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KUR'AN HARFLERİNİN KELİME İÇİNDEKİ KONUMLARI", 14, "#166534", "bold")
    cols = [
        (25, "1. Müstakil (Tek Başına)", "Harfin asıl şeklidir:", "ب — ج — ع — ك — هـ", "Noktalar ve gövde tamdır"),
        (192, "2. Kelime Başında", "Kuyruk kısmı gider,", "solundaki harfe bağlanır:", "بـ — جـ — عـ — كـ — هـ"),
        (359, "3. Kelime Ortasında", "Hem sağından hem", "solundan kol uzatır:", "ـبـ — ـجـ — ـعـ — ـكـ — ـهـ"),
        (526, "4. Kelime Sonunda", "Sağdan bağlanır ve asıl", "kuyruk şekline döner:", "ـب — ـج — ـع — ـك — ـه")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#15803d", "bold")
        ic += _metin(x+75, 98, s1, 10, "#334155")
        ic += _metin(x+75, 124, s2, 13, "#1e293b", "bold")
        ic += _metin(x+75, 150, s3, 10, "#166534")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#fef2f2", "#ef4444", 12, 2)
    ic += _metin(350, 34, "KENDİNDEN SONRAKİ HARFLE BİRLEŞMEYEN 6 HARF", 14, "#991b1b", "bold")
    harfler = [
        (30, "ا", "Elif"),
        (140, "د", "Dâl"),
        (250, "ذ", "Zel"),
        (360, "ر", "Râ"),
        (470, "ز", "Zây"),
        (580, "و", "Vâv")
    ]
    for x, h, ad in harfler:
        ic += _kutu(x, 48, 90, 90, "#ffffff", "#f87171", 10, 1.8)
        ic += _metin(x+45, 92, h, 26, "#b91c1c", "bold")
        ic += _metin(x+45, 122, ad, 12, "#1e293b", "bold")
    ic += _kutu(30, 148, 640, 42, "#fee2e2", "#ef4444", 8, 1.2)
    ic += _metin(350, 174, "Kural: Bu 6 harf sağdan gelen harfle birleşir (ـا ـد ـذ ـر ـز ـو), fakat solundaki harfe kol uzatmaz!", 11, "#991b1b", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "BAŞTA, ORTADA VE SONDA ŞEKLİ BELİRGİN DEĞİŞEN HARFLER", 13, "#1e3a8a", "bold")
    cols = [
        (25, "Kâf (ك) Harfi", "Başta: كـ (كَتَبَ)", "Ortada: ـكـ (شَكَرَ)", "Sonda: ـك / ك (مَلِكٌ)"),
        (192, "Ayn (ع) ve Gayn (غ)", "Başta: عـ (عَلِمَ)", "Ortada: ـعـ (جَعَلَ)", "Sonda: ـع (سَمِعَ)"),
        (359, "Hâ (هـ) Harfi", "Başta: هـ (هَدَى)", "Ortada: ـهـ (فَهِمَ)", "Sonda: ـه / ه (لَهُ)"),
        (526, "Mîm (م) ve Yâ (ي)", "Başta: مـ / يـ", "Ortada: ـمـ / ـيـ", "Sonda: ـم / ـي")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+75, 102, s1, 11, "#334155")
        ic += _metin(x+75, 126, s2, 11, "#334155")
        ic += _metin(x+75, 150, s3, 11, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "HARFLERİ BİRLEŞTİREREK KELİME YAZMA ÖRNEKLERİ", 14, "#92400e", "bold")
    rows = [
        (50, "كَ + تَ + بَ", "→", "كَتَبَ (Ketebe)", "Üç harf de birbiriyle birleşir."),
        (98, "دَ + رَ + سَ", "→", "دَرَسَ (Derese)", "د ve ر kendinden sonrakine birleşmez!"),
        (146, "شَ + كَ + رَ", "→", "شَكَرَ (Şekera)", "ش ve ك birleşir; sondaki ر sağdan bağlanır.")
    ]
    for y, sol, ok, sag, acik in rows:
        ic += _kutu(28, y, 160, 38, "#ffffff", "#f59e0b", 8, 1.5)
        ic += _metin(108, y+24, sol, 13, "#b45309", "bold")
        ic += _metin(210, y+24, ok, 16, "#d97706", "bold")
        ic += _kutu(232, y, 170, 38, "#fef3c7", "#d97706", 8, 1.5)
        ic += _metin(317, y+24, sag, 13, "#92400e", "bold")
        ic += _metin(545, y+24, acik, 11, "#334155")
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
