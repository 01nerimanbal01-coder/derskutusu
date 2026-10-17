def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "ALLAH'A İMAN VE TEVHİT İLKESİ (İHLÂS SURESİ)", 14, "#166534", "bold")
    cols = [
        (25, "Zâtında Birlik", "Allah tektir (Ehad);", "eşi, benzeri ve ortağı", "yoktur (Küfüven ehad)."),
        (248, "Sıfatlarında Birlik", "Kudret, ilim ve iradesinde", "hiçbir varlık O'na", "denk olamaz (Samed)."),
        (471, "İbadette Birlik", "Yalnızca Allah'a kulluk", "edilir ve yalnız O'ndan", "yardım dilenir.")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+102, 74, b, 12, "#15803d", "bold")
        ic += _metin(x+102, 104, s1, 11, "#334155")
        ic += _metin(x+102, 126, s2, 11, "#334155")
        ic += _metin(x+102, 148, s3, 11, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "ALLAH'IN SIFATLARI: ZÂTÎ VE SÜBÛTÎ SIFATLAR", 14, "#1e3a8a", "bold")
    ic += _kutu(28, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(183, 72, "Zâtî Sıfatlar (Yalnız Allah'a Özgü)", 12, "#1d4ed8", "bold")
    ic += _metin(183, 98, "• Vücûd (Var olmak) • Kıdem (Ezeli olmak)", 11, "#334155")
    ic += _metin(183, 122, "• Bekâ (Ebedi olmak) • Vahdâniyyet (Bir olmak)", 11, "#334155")
    ic += _metin(183, 146, "• Muhâlefetün li'l-havâdis (Sonradan olana benzememek)", 10, "#334155")
    ic += _metin(183, 168, "• Kıyâm bi-nefsihî (Hiçbir şeye muhtaç olmamak)", 10, "#1e40af", "bold")

    ic += _kutu(362, 48, 310, 140, "#ffffff", "#3b82f6", 10, 1.8)
    ic += _metin(517, 72, "Sübûtî Sıfatlar (Kemal Sıfatları)", 12, "#1d4ed8", "bold")
    ic += _metin(517, 98, "• Hayat (Diri olmak) • İlim (Her şeyi bilmek)", 11, "#334155")
    ic += _metin(517, 122, "• Semi' (İşitmek) • Basar (Görmek)", 11, "#334155")
    ic += _metin(517, 146, "• İrade (Dilemek) • Kudret (Gücü yetmek)", 11, "#334155")
    ic += _metin(517, 168, "• Kelam (Konuşmak) • Tekvîn (Yoktan yaratmak)", 11, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "İMAN - SALİH AMEL - GÜZEL AHLAK BÜTÜNLÜĞÜ", 14, "#92400e", "bold")
    ic += _kutu(35, 55, 190, 118, "#ffffff", "#f59e0b", 9, 1.5)
    ic += _metin(130, 82, "1. Sahih İman", 12, "#b45309", "bold")
    ic += _metin(130, 108, "Ağacın kökü gibidir;", 11, "#334155")
    ic += _metin(130, 130, "kalpte tasdik ve güven", 11, "#334155")
    ic += _metin(240, 115, "→", 22, "#d97706", "bold")
    ic += _kutu(255, 55, 190, 118, "#ffffff", "#f59e0b", 9, 1.5)
    ic += _metin(350, 82, "2. Salih Amel", 12, "#b45309", "bold")
    ic += _metin(350, 108, "Ağacın gövdesi ve", 11, "#334155")
    ic += _metin(350, 130, "dallarıdır; ibadet ve iyilik", 11, "#334155")
    ic += _metin(460, 115, "→", 22, "#d97706", "bold")
    ic += _kutu(475, 55, 190, 118, "#ffffff", "#f59e0b", 9, 1.5)
    ic += _metin(570, 82, "3. Güzel Ahlak", 12, "#b45309", "bold")
    ic += _metin(570, 108, "Ağacın tatlı meyvesidir;", 11, "#334155")
    ic += _metin(570, 130, "huzur ve adalet üretir", 11, "#334155")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "İMANI KORUMAK VE GÜÇLENDİRMEK İÇİN TEMEL YOLLAR", 14, "#6b21a8", "bold")
    items = [
        (25, "Sahih İlim", "Kur'an ve sünnete", "dayalı tahkiki iman"),
        (192, "İbadet & Dua", "Allah ile bağı", "canlı tutmak"),
        (359, "Şirkten Sakınma", "Hurafe, batıl inanç ve", "riyadan uzak durmak"),
        (526, "Salih Çevre", "Doğru, dürüst ve", "erdemli dostlarla olmak")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 50, 150, 130, "#ffffff", "#c084fc", 9, 1.5)
        ic += _metin(x+75, 78, b, 12, "#7e22ce", "bold")
        ic += _metin(x+75, 110, s1, 11, "#334155")
        ic += _metin(x+75, 132, s2, 11, "#334155")
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
