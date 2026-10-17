def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KUR'AN MEALLERİNDEN İMAN ÇIKARIMI YAPMA BASAMAKLARI", 13, "#166534", "bold")
    steps = [
        (25, "1. Meali Bulma", "Sure ve ayet numarası", "veya konu fihristiyle", "iman ayetlerine ulaşma"),
        (192, "2. Konuyu Saptama", "Ayetin vurguladığı ana", "mesajı (tevhit, düzen,", "ahiret, ahlak) belirleme"),
        (359, "3. Sınıflandırma", "Ayetleri konusal", "gruplara (kozmik düzen,", "nimet, sorumluluk) ayırma"),
        (526, "4. Çıkarım ve Uygulama", "'Niçin inanıyorum?'", "sorusuna delilli cevap", "verip hayata aktarma")
    ]
    for x, b, s1, s2, s3 in steps:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#15803d", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 200, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "KUR'AN-I KERİM'DE İMAN AYETLERİNİN DÖRT TEMEL GRUBU", 13, "#1e3a8a", "bold")
    cols = [
        (25, "1. Tevhit & Esmâ-i Hüsnâ", "İhlâs, 112/1-4", "Haşr, 59/22-24", "Bakara, 2/163, 255"),
        (192, "2. Evrendeki Kevnî Deliller", "Bakara, 2/164", "Âl-i İmrân, 3/190-191", "Gاشiye, 88/17-20"),
        (359, "3. Nimet, Fıtrat & Şükür", "Rûm, 30/30", "Nahl, 16/18, 78", "Lokmân, 31/20"),
        (526, "4. İman, Amel & Ahiret", "Bakara, 2/177, 285", "Mü'minûn, 23/1-11", "Zilzâl, 99/7-8")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 144, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+75, 102, "• " + s1, 10, "#1e293b", "bold")
        ic += _metin(x+75, 126, "• " + s2, 10, "#334155")
        ic += _metin(x+75, 150, "• " + s3, 10, "#334155")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "ÂL-İ İMRÂN SURESİ 190-191. AYETLER: TEFEKKÜR VE İMAN", 13, "#92400e", "bold")
    ic += _kutu(28, 48, 644, 130, "#ffffff", "#f59e0b", 10, 1.5)
    ic += _metin(350, 72, "'Göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardınca gelişinde", 11, "#1e293b", "bold")
    ic += _metin(350, 94, "akl-ı selim sahipleri (ulü'l-elbâb) için kesin deliller vardır.' (Âl-i İmrân, 3/190)", 11, "#b45309", "bold")
    ic += _metin(350, 120, "'Onlar ayaktayken, otururken ve yanları üzerine yatarken Allah'ı anarlar; göklerin ve yerin", 10, "#334155")
    ic += _metin(350, 140, "yaratılışı üzerinde düşünürler: Rabbimiz! Bunu boşuna (bâtıl) yaratmadın, seni tenzih ederiz!' (3/191)", 10, "#92400e", "bold")
    ic += _metin(350, 164, "Çıkarım: Tefekkür eden akıl, evrenin boşuna yaratılmadığını kavrayarak imana ulaşır.", 11, "#1e293b", "bold")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "MÜ'MİNÛN SURESİ 1-11. AYETLER: KURTULUŞA EREN MÜMİNLER", 13, "#6b21a8", "bold")
    items = [
        (25, "Huşu İle Namaz", "Namazlarını derin bir", "saygı ve bilinçle kılarlar"),
        (192, "Boş İşten Yüz Çevirme", "Faydasız ve kırıcı sözlerden", "(lağv) uzak dururlar"),
        (359, "Zekât ve İffet", "Paylaşırlar ve iffetlerini", "titizlikle korurlar"),
        (526, "Emanet ve Ahit", "Emanetlerine ve verdikleri", "sözlere sadık kalırlar")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 48, 150, 134, "#ffffff", "#c084fc", 9, 1.5)
        ic += _metin(x+75, 76, b, 11, "#7e22ce", "bold")
        ic += _metin(x+75, 108, s1, 10, "#334155")
        ic += _metin(x+75, 130, s2, 10, "#334155")
    return _svg(700, 210, ic)

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
