def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KUR'AN KÜLTÜRÜ KAVRAMLARIMIZ: TİLAVET, HATİM, HAFIZ VE MUKABELE", 13, "#166534", "bold")
    cols = [
        (25, "Tilavet (التِّلَاوَةُ)", "Kur'an'ı anlamını", "düşünerek, kurallarına", "uygun güzel okuma"),
        (192, "Hatim (الْخَتْمُ)", "Kur'an-ı Kerim'i", "Fâtiha'dan Nâs'a kadar", "baştan sona okuma"),
        (359, "Hafız (الْحَافِظُ)", "Kur'an-ı Kerim'in", "tamamını ezberleyip", "koruyan kimse"),
        (526, "Mukabele (الْمُقَابَلَةُ)", "Biri okurken diğerlerinin", "mushaftan takip etmesi", "(Ramazan geleneği)")
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
    ic += _metin(350, 34, "BAKARA SURESİ 164-186. AYETLERİN ANA KONU BAŞLIKLARI", 13, "#1e3a8a", "bold")
    cols = [
        (25, "Ayet 164-176: Tevhit & Helal Rızık", "• Evrendeki tevhit delilleri (164)", "• Helal ve temiz (tayyib) gıdalardan", "  yiyip Allah'a şükretme (168, 172)", "• Haram kılınan gıdalar (173)"),
        (248, "Ayet 177: İyilik (Birr) Âyeti", "• Gerçek iyilik (el-Birr): İman,", "  mal sevgisine rağmen akraba, yetim,", "  yoksul ve yolcuya infak, namaz,", "  zekât, sözde durma ve sabır"),
        (471, "Ayet 183-186: Oruç & Dua", "• Ramazan orucunun farz kılınışı", "  ve Kur'an'ın bu ayda inişi (183-185)", "• 'Kullarım beni sana sorarsa,", "  ben onlara çok yakınım!' (186)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 70, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+102, 94, s1, 10, "#334155")
        ic += _metin(x+102, 116, s2, 10, "#334155")
        ic += _metin(x+102, 138, s3, 10, "#334155")
        ic += _metin(x+102, 160, s4, 10, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "SECÂVEND (DURAK) İŞARETLERİ VE VAKIF KURALLARI", 14, "#92400e", "bold")
    cols = [
        (25, "م (Durmak Lazım)", "Vakf-ı Lâzım:", "Geçilirse anlam bozulur,", "mutlaka durulmalıdır!"),
        (192, "ط (Vakf-ı Mutlak)", "Tam cümle sonudur;", "durmak güzeldir,", "anlam tamamlanmıştır."),
        (359, "ج / ز / قف", "Vakf-ı Câiz:", "Durmak da geçmek de", "uygundur (Cîm'de durmak evlâ)."),
        (526, "لا (Durulmaz!)", "Anlam devam etmektedir;", "durulmaz, durulursa", "geriden alınıp geçilir.")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#b45309", "bold")
        ic += _metin(x+75, 98, s1, 10, "#1e293b", "bold")
        ic += _metin(x+75, 120, s2, 10, "#334155")
        ic += _metin(x+75, 142, s3, 10, "#334155")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "BAKARA SURESİ 186. AYET: ALLAH KULLARINA ÇOK YAKINDIR", 13, "#6b21a8", "bold")
    ic += _kutu(28, 48, 644, 126, "#ffffff", "#c084fc", 10, 1.5)
    ic += _metin(350, 74, "وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ أُجِيبُ دَعْوَةَ الدَّاعِ إِذَا دَعَانِ", 14, "#7e22ce", "bold")
    ic += _metin(350, 104, "'Kullarım sana beni sorduklarında (söyle onlara): Şüphesiz ben çok yakınım;", 11, "#1e293b", "bold")
    ic += _metin(350, 126, "bana dua ettiği zaman dua edenin çağrısına karşılık veririm!' (Bakara, 2/186)", 11, "#1e293b", "bold")
    ic += _metin(350, 152, "Mesaj: Kul ile Allah arasında hiçbir aracı yoktur; Allah samimi duaları işitir ve kabul eder.", 11, "#581c87")
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
