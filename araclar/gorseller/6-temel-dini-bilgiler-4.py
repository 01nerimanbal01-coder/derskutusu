def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "KUR'AN-I KERİM MEALLERİNDEN İMAN AYETLERİNİ İNCELEME SÜRECİ", 13, "#1e3a8a", "bold")
    steps = [
        (25, "1. Ayeti Bulma", "Sure ve ayet numarasıyla", "veya kavram fihristiyle", "mealden ayete ulaşma"),
        (192, "2. Konuyu Belirleme", "Ayette işlenen temel", "inanç konusunu", "tespit etme"),
        (359, "3. Sınıflandırma", "Tevhit, nimet, düzen,", "ahiret ve sorumluluk", "başlıklarına ayırma"),
        (526, "4. Çıkarım Yapma", "'Niçin inanıyorum?'", "sorusuna ayet deliliyle", "bilinçli cevap üretme")
    ]
    for x, b, s1, s2, s3 in steps:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 200, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "İMAN KONULU AYETLERİN İÇERİKLERİNE GÖRE SINIFLANDIRILMASI", 13, "#166534", "bold")
    cols = [
        (25, "1. Tevhit ve İman Esasları", "• İhlâs, 112/1-4", "• Bakara, 2/255 (Âyetü'l-Kürsî)", "• Bakara, 2/285; Nisâ, 4/136", "Çıkarım: Allah bir ve tektir."),
        (248, "2. Evrendeki Ölçü ve Nimet", "• Kamer, 54/49; Mülk, 67/3", "• Nahl, 16/78; İbrahim, 14/34", "• Enbiyâ, 21/22", "Çıkarım: Düzen ve şükür bilinci."),
        (471, "3. İman-Amel ve Sorumluluk", "• Zâriyât, 51/56; Asr, 103/1-3", "• Hucurât, 49/13-15", "• Enfâl, 8/2-4; Ankebût, 29/2", "Çıkarım: Salih amel ve ahlak.")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 144, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+102, 70, b, 11, "#15803d", "bold")
        ic += _metin(x+102, 94, s1, 10, "#334155")
        ic += _metin(x+102, 116, s2, 10, "#334155")
        ic += _metin(x+102, 138, s3, 10, "#334155")
        ic += _metin(x+102, 162, s4, 10, "#166534", "bold")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "HUCURÂT SURESİ 15. AYET: GERÇEK MÜMİNLERİN TANIMI", 14, "#92400e", "bold")
    ic += _kutu(28, 48, 644, 130, "#ffffff", "#f59e0b", 10, 1.5)
    ic += _metin(350, 74, "'Müminler ancak Allah'a ve Resulüne iman eden, ondan sonra asla şüpheye düşmeyen,", 11, "#1e293b", "bold")
    ic += _metin(350, 98, "Allah yolunda mallarıyla ve canlarıyla gayret gösteren kimselerdir. İşte doğrular (sâdıklar) onlardır.'", 11, "#b45309", "bold")
    ic += _metin(350, 126, "• Çıkarım 1: Gerçek iman kalpte şüphe barındırmayan kesin tasdiktir.", 11, "#334155")
    ic += _metin(350, 150, "• Çıkarım 2: İman, fedakârlık ve güzel davranışlarla (sadakatle) doğrulanır.", 11, "#92400e", "bold")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "İMAN, İSLAM, MÜMİN VE SÜNNET KAVRAM HARİTASI", 14, "#6b21a8", "bold")
    items = [
        (25, "İman", "Kalp ile tasdik,", "dil ile ikrar (İnanç)"),
        (192, "İslam", "Allah'a teslimiyet ve", "ibadetlerle yaşama"),
        (359, "Mümin", "Şüphesiz inanan ve", "güven veren insan"),
        (526, "Sünnet", "Peygamberimizin (sav)", "örnek yaşam yolu")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 48, 150, 126, "#ffffff", "#c084fc", 9, 1.5)
        ic += _metin(x+75, 76, b, 12, "#7e22ce", "bold")
        ic += _metin(x+75, 106, s1, 10, "#334155")
        ic += _metin(x+75, 128, s2, 10, "#334155")
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
