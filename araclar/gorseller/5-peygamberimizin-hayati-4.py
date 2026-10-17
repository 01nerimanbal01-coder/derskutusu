def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "FİL VAKASI (OLAYI) VE FİL SURESİ (MİLADİ 571)", 14, "#92400e", "bold")
    steps = [
        (25, "1. Ebrehe'nin Ordusu", "Yemen Valisi Ebrehe,", "Kâbe'yi yıkmak için", "filli ordusuyla yürüdü."),
        (192, "2. Abdülmuttalib'in Sözü", "'Ben develerin sahibiyim;", "Kâbe'nin de onu koruyacak", "bir Rabbi vardır!'"),
        (359, "3. Fil Mahmûd Durdu", "Mekke sınırında (Muhassır)", "öndeki fil Кâbe yönüne", "adım atmadı."),
        (526, "4. Ebâbîl Kuşları", "Allah sürü sürü kuşlarla", "(pişkin taşlarla) orduyu", "yenik ekin yaprağına çevirdi.")
    ]
    for x, b, s1, s2, s3 in steps:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#b45309", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 144, s3, 10, "#92400e", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "PEYGAMBERİMİZİN (SAV) KUTLU DOĞUMU: KİMLİK KARTI", 14, "#166534", "bold")
    cols = [
        (25, "Doğum Yeri ve Yılı", "Mekke-i Mükerreme", "Fil Olayı'ndan 50-55 gün", "sonra: 20 Nisan 571"),
        (248, "Hicrî Takvim Tarihi", "12 Rebîülevvel Pazartesi", "Sabaha karşı seher vakti", "(Mevlid Kandili)"),
        (471, "Ailesi ve İsmi", "Babası: Abdullah (önceden vefat)", "Annesi: Âmine Hatun", "Dedesi 'Muhammed' adını verdi")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+102, 74, b, 12, "#15803d", "bold")
        ic += _metin(x+102, 102, s1, 11, "#1e293b", "bold")
        ic += _metin(x+102, 126, s2, 11, "#334155")
        ic += _metin(x+102, 150, s3, 11, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 185, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "PEYGAMBERİMİZİN GÜZEL İSİMLERİ: MUHAMMED VE AHMED", 14, "#1e3a8a", "bold")
    ic += _kutu(28, 48, 310, 126, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(183, 74, "مُحَمَّد (Muhammed)", 14, "#1d4ed8", "bold")
    ic += _metin(183, 102, "Veren: Dedesi Abdülmuttalib", 11, "#1e293b", "bold")
    ic += _metin(183, 126, "Anlamı: 'Yerde ve gökte çokça övülen,", 11, "#334155")
    ic += _metin(183, 146, "bütün güzel huyları kendinde toplayan'", 11, "#334155")

    ic += _kutu(362, 48, 310, 126, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(517, 74, "أَحْمَد (Ahmed)", 14, "#1d4ed8", "bold")
    ic += _metin(517, 102, "Veren: Annesi Hz. Âmine", 11, "#1e293b", "bold")
    ic += _metin(517, 126, "Anlamı: 'Allah'a herkesten çok hamdeden,", 11, "#334155")
    ic += _metin(517, 146, "övgüye en layık olan'", 11, "#334155")
    return _svg(700, 205, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "KÜLTÜRÜMÜZDE MEVLİD GELENEĞİ VE MEVLİD HAFTASI", 14, "#6b21a8", "bold")
    ic += _kutu(30, 48, 640, 130, "#ffffff", "#c084fc", 10, 1.5)
    ic += _metin(350, 74, "Mevlid: 'Doğum zamanı ve doğum yeri' demektir.", 12, "#7e22ce", "bold")
    ic += _metin(350, 100, "• Süleyman Çelebi'nin yazdığı 'Vesîletü'n-Necât' (Kurtuluş Vesilesi / Mevlid) eseri", 11, "#334155")
    ic += _metin(350, 122, "  asırlar boyunca milletimizin Peygamber sevgisinin sembolü olmuştur.", 11, "#334155")
    ic += _metin(350, 146, "• Rebîülevvel ayının 12. gecesi 'Mevlid Kandili' ve o hafta 'Mevlid-i Nebî Haftası' olarak", 11, "#334155")
    ic += _metin(350, 166, "  salavatlar, dualar ve yardımlaşma etkinlikleriyle kutlanır.", 11, "#581c87", "bold")
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
