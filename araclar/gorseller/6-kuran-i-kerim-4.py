def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KUR'AN-I KERİM'İN İÇ DÜZENİ: AYET, SURE, HİZİP VE CÜZ", 14, "#166534", "bold")
    cols = [
        (25, "1. Ayet (الْآيَةُ)", "Sureleri oluşturan", "her bir cümle/işaret", "(Yaklaşık 6236 ayet)"),
        (192, "2. Sure (السُّورَةُ)", "Ayetlerden oluşan", "bağımsız bölümler", "(Toplam 114 sure)"),
        (359, "3. Hizip (الْحِزْبُ)", "Her cüzün 5'er sayfalık", "dört alt bölümü", "(1 cüz = 4 hizip)"),
        (526, "4. Cüz (الْجُزْءُ)", "20 sayfadan oluşan", "ana bölümler", "(Toplam 30 cüz = 600 s.)")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#15803d", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 120, s2, 10, "#334155")
        ic += _metin(x+75, 146, s3, 10, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "BAKARA SURESİ 84-105. AYETLERİN ANA MESAJLARI", 14, "#1e3a8a", "bold")
    cols = [
        (25, "Ayet 84-86: Sözleşme (Mîsâk)", "İsrailoğullarından alınan söz:", "Kan dökmemek, yurtlarından", "çıkarmamak ve hükümlerin", "tamamına inanmak"),
        (248, "Ayet 87-96: Peygamberler", "Hz. Musa ve Hz. İsa'ya verilen", "mucizeler; kibirlenip", "hakkı reddetmenin", "tehlikesi"),
        (471, "Ayet 97-105: Meleklere İman", "Cebrâil ve Mîkâil'in", "görevleri; sihirden uzak", "durma ve konuşmada", "edep ('unzurnâ' ilkesi)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 72, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+102, 98, s1, 10, "#1e293b", "bold")
        ic += _metin(x+102, 120, s2, 10, "#334155")
        ic += _metin(x+102, 140, s3, 10, "#334155")
        ic += _metin(x+102, 160, s4, 10, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "BAKARA 84-105. AYETLERDE ÖNE ÇIKAN TECVİT UYGULAMALARI", 13, "#92400e", "bold")
    cols = [
        (25, "Medd-i Tabiî", "Harf-i med (ا و ي) olup", "sebeb-i med yoksa 1 elif", "uzatılır: قَالُوا - كِتَابٌ"),
        (192, "Medd-i Muttasıl", "Harf-i med ile hemze", "AYNI kelimedeyse 4 elif:", "دِمَاءَكُمْ - أُولَٰئِكَ - جَاءَ"),
        (359, "Medd-i Munfasıl", "Harf-i med ile hemze", "AYRI kelimelerdeyse:", "بِمَا أَنْزَلَ - قَالُوا آمَنَّا"),
        (526, "İzhar ve İhfa", "Boğaz harflerinde İzhar,", "15 ihfa harfinde genizden", "İhfa: أَنْزَلَ - مِنْ قَبْلُ")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+75, 72, b, 12, "#b45309", "bold")
        ic += _metin(x+75, 100, s1, 10, "#334155")
        ic += _metin(x+75, 120, s2, 10, "#334155")
        ic += _metin(x+75, 146, s3, 11, "#92400e", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "BAKARA 104. AYET: PEYGAMBERİMİZE HİTAP EDEBİ VE SALAVAT", 13, "#6b21a8", "bold")
    ic += _kutu(28, 48, 644, 126, "#ffffff", "#c084fc", 10, 1.5)
    ic += _metin(350, 74, "يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَقُولُوا رَاعِنَا وَقُولُوا انْظُرْنَا وَاسْمَعُوا", 14, "#7e22ce", "bold")
    ic += _metin(350, 102, "'Ey iman edenler! (Peygamber'e hitap ederken) râinâ demeyin, unzurnâ (bize bak/bizi gözet) deyin", 11, "#1e293b", "bold")
    ic += _metin(350, 124, "ve onu can kulağıyla dinleyin!' (Bakara, 2/104)", 11, "#1e293b", "bold")
    ic += _metin(350, 152, "Mesaj: Müminler konuşmalarında kibar ve saygılı kelimeler seçer, Peygamberimize salavat getirirler.", 11, "#581c87")
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
