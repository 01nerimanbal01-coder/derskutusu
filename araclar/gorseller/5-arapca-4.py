def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "ARAPÇADA NEZAKET VE SOSYAL İFADELER", 14, "#166534", "bold")
    cols = [
        (25, "شُكْرًا — عَفْوًا", "Şükran — Afven", "Teşekkür ederim —", "Rica ederim / Bir şey değil"),
        (192, "مِنْ فَضْلِكَ / كِ", "Min fadlike / Min fadliki", "Lütfen (Erkek / Kız", "muhatap için)"),
        (359, "تَشَرَّفْتُ / فُرْصَة سَعيدَة", "Teşerraftü / Fursa saîde", "Tanıştığıma memnun", "oldum (Şeref duydum)"),
        (526, "يا أُسْتاذي / يا صَديقي", "Yâ üstâzî / Yâ sadîkî", "Ey öğretmenim! /", "Ey arkadaşım! (Hitap)")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 74, b, 13, "#15803d", "bold")
        ic += _metin(x+75, 100, s1, 10, "#1e293b", "bold")
        ic += _metin(x+75, 124, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#334155")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "SINIF İÇİ YÖNERGELER (الْأَوامِرُ الصَّفِّيَّةُ — ERİL VE DİŞİL)", 13, "#1e3a8a", "bold")
    cols = [
        (25, "Ayağa Kalk!", "Erkek: قُمْ (Kum)", "Kız: قومي (Kûmî)", "Sonuna 'ي' eklenir"),
        (192, "Otur!", "Erkek: اِجْلِسْ (İclis)", "Kız: اِجْلِسي (İclisî)", "Sonuna 'ي' eklenir"),
        (359, "Oku!", "Erkek: اِقْرَأْ (İkra')", "Kız: اِقْرَئي (İkra'î)", "Sonuna 'ي' eklenir"),
        (526, "Yaz!", "Erkek: اُكْتُبْ (Üktüb)", "Kız: اُكْتُبي (Üktübî)", "Sonuna 'ي' eklenir")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+75, 100, s1, 11, "#1e293b", "bold")
        ic += _metin(x+75, 124, s2, 11, "#7e22ce", "bold")
        ic += _metin(x+75, 152, s3, 10, "#475569")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "ARAPÇADA ÜÇ TEMEL HAREKE (الْحَرَكاتُ الثَّلاثُ)", 14, "#92400e", "bold")
    cols = [
        (25, "1. الْفَتْحَةُ (Fetha / Üstün)", "Harfin ÜSTÜNE konur", "İnce harfleri 'e', kalın", "harfleri 'a' sesiyle okutur: أَ - بَ - تَ"),
        (248, "2. الْكَسْرَةُ (Kesra / Esre)", "Harfin ALTINA konur", "İnce harfleri 'i', kalın", "harfleri 'ı-i' sesiyle okutur: إِ - بِ - تِ"),
        (471, "3. الضَّمَّةُ (Damme / Ötre)", "Harfin ÜSTÜNE (و gibi) konur", "Harfleri 'u / ü' sesiyle", "okutur: أُ - بُ - تُ")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+102, 72, b, 12, "#b45309", "bold")
        ic += _metin(x+102, 98, s1, 11, "#1e293b", "bold")
        ic += _metin(x+102, 124, s2, 10, "#334155")
        ic += _metin(x+102, 148, s3, 11, "#92400e", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "ÜNİTE VECİZ SÖZÜ VE HADİS-İ ŞERİF", 14, "#6b21a8", "bold")
    ic += _kutu(35, 50, 630, 122, "#ffffff", "#c084fc", 10, 1.8)
    ic += _metin(350, 82, "اَلسَّلَامُ قَبْلَ الْكَلَامِ", 18, "#7e22ce", "bold")
    ic += _metin(350, 112, "Okunuşu: es-Selâmü kable'l-kelâm", 12, "#1e293b", "bold")
    ic += _metin(350, 136, "Anlamı: 'Selam, kelamdan (konuşmadan) öncedir.' (Tirmizî, İsti'zân, 11)", 12, "#581c87", "bold")
    ic += _metin(350, 158, "İslam adabında bir ortama girildiğinde veya bir soru sorulacağında önce selam verilir.", 11, "#475569")
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
