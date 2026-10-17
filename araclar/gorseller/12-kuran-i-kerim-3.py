def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KEHF SURESİ VE DÖRT BÜYÜK İMTİHAN KISSASI", 14, "#166534", "bold")
    cols = [
        (25, "1. Ashâb-ı Kehf", "İnanç İmtihanı", "Tevhidi korumak için", "mağaraya sığınan gençler"),
        (192, "2. Bahçe Sahibi", "Mal ve Servet İmtihanı", "Şükürsüzlük ve kibre", "karşı ahiret bilinci"),
        (359, "3. Hz. Musa &amp; Hızır", "İlim İmtihanı", "Bilginin sınırları ve", "ilahi hikmete teslimiyet"),
        (526, "4. Hz. Zülkarneyn", "İktidar ve Güç İmtihanı", "Gücü adalet ve mazlumları", "korumak için kullanma")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#15803d", "bold")
        ic += _metin(x+75, 96, s1, 11, "#1e293b", "bold")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 142, s3, 10, "#334155")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "KEHF SURESİ 1-31. AYETLER: ASHÂB-I KEHF KISSASININ AŞAMALARI", 13, "#1e3a8a", "bold")
    steps = [
        (25, "1. Tevhit Duruşu", "Putperest hükümdara karşı", "'Rabbimiz göklerin ve", "yerin Rabbidir' ilanı"),
        (192, "2. Mağaraya Hicret", "İmanlarını korumak için", "mağaraya sığınma ve", "rahmet duası (Kehf, 10)"),
        (359, "3. Mucizevi Uyku", "300 + 9 yıl (309 kamerî yıl)", "uyutulma; güneşin ve", "bedenlerin korunması"),
        (526, "4. Diriliş Delili", "Uyandırılmalarıyla", "öldükten sonra dirilişin", "(ba's) hak olduğunun ispatı")
    ]
    for x, b, s1, s2, s3 in steps:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "KEHF SURESİ 23-24. AYETLER: 'İNŞALLAH' BİLİNCİ VE EDEBİ", 14, "#92400e", "bold")
    ic += _kutu(30, 50, 640, 126, "#ffffff", "#f59e0b", 10, 1.5)
    ic += _metin(350, 78, "وَلَا تَقُولَنَّ لِشَيْءٍ إِنِّي فَاعِلٌ ذَٰلِكَ غَدًا إِلَّا أَنْ يَشَاءَ اللَّهُ", 13, "#b45309", "bold")
    ic += _metin(350, 106, "'Allah'ın dilemesine bağlamaksızın (İnşallah demeden) hiçbir şey için", 11, "#1e293b", "bold")
    ic += _metin(350, 128, "Bunu yarın mutlaka yapacağım deme!' (Kehf, 18/23-24)", 11, "#1e293b", "bold")
    ic += _metin(350, 154, "Mesaj: Kul tedbirini alır ve planını yapar, ancak her işin gerçekleşmesini Allah'ın iradesine bağlar.", 11, "#475569")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 195, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "EZBER VE ANLAM: MÜLK SURESİ 1-10. AYETLERİN ANA KONULARI", 13, "#6b21a8", "bold")
    cols = [
        (25, "Ayet 1-2: Hayat ve Ölüm", "Mülk Allah'ın elindedir.", "Ölüm ve hayat, 'hanginizin", "daha güzel amel yapacağını'", "sınamak için yaratılmıştır."),
        (248, "Ayet 3-5: Kusursuz Evren", "Yedi kat gökte hiçbir", "çatlak ve düzensizlik yoktur.", "Gök, yıldızlarla (kandillerle)", "süslenmiş ve korunmuştur."),
        (471, "Ayet 6-10: Ahiret Uyarısı", "İnkârcıların cehennemdeki", "pişmanlığı: 'Keşke dinleseydik", "veya aklımızı kullansaydık!'", "itirafı (Mülk, 67/10)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#c084fc", 9, 1.5)
        ic += _metin(x+102, 72, b, 11, "#7e22ce", "bold")
        ic += _metin(x+102, 98, s1, 10, "#1e293b", "bold")
        ic += _metin(x+102, 120, s2, 10, "#334155")
        ic += _metin(x+102, 142, s3, 10, "#334155")
        ic += _metin(x+102, 164, s4, 10, "#6b21a8", "bold")
    return _svg(700, 215, ic)

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