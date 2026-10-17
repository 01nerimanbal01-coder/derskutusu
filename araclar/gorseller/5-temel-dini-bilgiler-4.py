def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KUR'AN-I KERİM MEALLERİNDE İMAN AYETLERİNE BAŞVURMA ADIMLARI", 13, "#166534", "bold")
    steps = [
        (25, "1. Meali Bulma", "Sure ve ayet numarasına", "göre Kur'an mealinden", "ilgili ayeti açma"),
        (192, "2. Konuyu Belirleme", "Ayette vurgulanan ana", "iman esasını (tevhit,", "ahiret, peygamber) bulma"),
        (359, "3. Sınıflandırma", "Ayetleri konularına", "(evrendeki düzen, nimet,", "sorumluluk) göre ayırma"),
        (526, "4. Çıkarım Yapma", "'Niçin inanıyorum?'", "sorusuna ayet ışığında", "bilinçli cevap verme")
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
    ic += _metin(350, 34, "'NİÇİN İNANIYORUM?' SORUSUNA KUR'AN AYETLERİNDEN CEVAPLAR", 13, "#1e3a8a", "bold")
    cols = [
        (25, "Yaratılış ve Nimetlere Şükür", "Nahl, 16/78 ve Bakara, 2/21-22", "'Sizi yaratan, kulak, göz ve", "kalpler veren Allah'tır...", "Şükredesiniz diye!'"),
        (248, "Evrendeki Eşsiz Düzen", "Enbiyâ, 21/22 ve Mülk, 67/3", "'Yerde ve gökte Allah'tan", "başka ilah olsaydı ikisinin", "de düzeni bozulurdu.'"),
        (471, "Hayatın Anlamı ve Amacı", "Zâriyât, 51/56 ve Kıyamet, 75/36", "'İnsan başıboş bırakılacağını", "mı sanır?' Kulluk, iyilik", "ve ahiret bilinci")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 144, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 70, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+102, 92, s1, 10, "#1e293b", "bold")
        ic += _metin(x+102, 116, s2, 10, "#334155")
        ic += _metin(x+102, 138, s3, 10, "#334155")
        ic += _metin(x+102, 160, s4, 10, "#1e40af", "bold")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "BAKARA SURESİ 285. AYET (ÂMENER-RESÛLÜ): İMAN ESASLARI", 13, "#92400e", "bold")
    ic += _kutu(28, 48, 644, 130, "#ffffff", "#f59e0b", 10, 1.5)
    ic += _metin(350, 74, "'Peygamber, Rabbinden kendisine indirilene iman etti, müminler de (iman ettiler).", 11, "#1e293b", "bold")
    ic += _metin(350, 98, "Her biri; Allah'a, meleklerine, kitaplarına ve peygamberlerine iman ettiler...'", 11, "#b45309", "bold")
    ic += _metin(350, 126, "• Çıkarım 1: İman esasları bir bütündür; peygamberler arasında ayrım yapılmaz.", 11, "#334155")
    ic += _metin(350, 150, "• Çıkarım 2: Müminlerin sözü 'İşittik ve itaat ettik (Semi'nâ ve eta'nâ)' demektir.", 11, "#92400e", "bold")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "KUR'AN'DA MÜMİNLERİN TEMEL ÖZELLİKLERİ (ENFÂL 2-4, ASR 1-3)", 13, "#6b21a8", "bold")
    items = [
        (25, "Kalbi Titreyen", "Allah anıldığında kalpleri", "saygıyla ürperir"),
        (192, "İmanı Artan", "Allah'ın ayetleri okunduğunda", "imanları güçlenir"),
        (359, "Tevekkül Eden", "Üzerine düşeni yapıp", "yalnız Rabbine güvenir"),
        (526, "Hakkı ve Sabrı Tavsiye", "Namaz kılar, paylaşır,", "doğruluğu ve sabrı öğütler")
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
