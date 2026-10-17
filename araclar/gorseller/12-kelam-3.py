def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "KELAM İLMİNİN ÜÇ ANA KONU ALANI (USÛL-İ SELÂSE VE VESÂİL)", 13, "#1e3a8a", "bold")
    cols = [
        (25, "1. İlâhiyyât", "Allah'ın varlığı, birliği,", "zâtî ve sübûtî sıfatları,", "kader ve yaratma fiili"),
        (248, "2. Nübüvvât", "Peygamberlik müessesesi,", "vahiy, mucize, ilahi kitaplar", "ve peygamberlerin sıfatları"),
        (471, "3. Sem'iyyât (Meâd)", "Nakil yoluyla bilinen konular:", "Ahiret, kıyamet, haşir,", "hesap, cennet ve cehennem")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 74, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+102, 104, s1, 11, "#334155")
        ic += _metin(x+102, 126, s2, 11, "#334155")
        ic += _metin(x+102, 148, s3, 11, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "KELAM İLMİNDE BİLGİ KAYNAKLARI (ESBÂB-I İLİM)", 14, "#166534", "bold")
    cols = [
        (25, "1. Havâss-ı Selîme", "Sağlam Duyu Organları", "Beş duyu ile dış dünyayı", "gözlemleme ve algılama"),
        (248, "2. Akl-ı Selîm", "Sağduyu ve Akıl Yürütme", "Zorunlu ve çıkarımsal (istidlâlî)", "bilgi üretme, delillendirme"),
        (471, "3. Haber-i Sâdık", "Doğru Haber", "• Mütevâtir Haber", "• Peygamber Haberi (Vahiy)")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 204, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+102, 72, b, 12, "#15803d", "bold")
        ic += _metin(x+102, 96, s1, 11, "#1e293b", "bold")
        ic += _metin(x+102, 122, s2, 11, "#334155")
        ic += _metin(x+102, 146, s3, 11, "#334155")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "EHL-İ SÜNNET KELAM EKOLLERİ: MÂTÜRÎDÎLİK VE EŞ'ARÎLİK", 14, "#92400e", "bold")
    ic += _kutu(28, 48, 310, 140, "#ffffff", "#f59e0b", 10, 1.8)
    ic += _metin(183, 72, "Mâtürîdîlik (İmam Mâtürîdî - Semerkant)", 11, "#b45309", "bold")
    ic += _metin(183, 98, "• Akıl ile nakil arasında tam uyum gözetir", 11, "#334155")
    ic += _metin(183, 120, "• Akıl tek başına iyiyi ve kötüyü (hüsün-kubuh) bilir", 10, "#334155")
    ic += _metin(183, 142, "• İnsanın cüz'î iradesini ve sorumluluğunu vurgular", 10, "#334155")
    ic += _metin(183, 166, "Temel Eser: Kitâbü't-Tevhîd", 11, "#92400e", "bold")

    ic += _kutu(362, 48, 310, 140, "#ffffff", "#f59e0b", 10, 1.8)
    ic += _metin(517, 72, "Eş'arîlik (İmam Eş'arî - Basra/Bağdat)", 11, "#b45309", "bold")
    ic += _metin(517, 98, "• Nakli merkeze alır, aklı nakli desteklemede kullanır", 10, "#334155")
    ic += _metin(517, 120, "• Bir şeyin iyi veya kötü oluşu vahiy ile (şer'an) bilinir", 10, "#334155")
    ic += _metin(517, 142, "• Kulun fiillerini 'kesb' (kazanma) teorisiyle açıklar", 10, "#334155")
    ic += _metin(517, 166, "Temel Eserler: el-İbâne, el-Lüma'", 11, "#92400e", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "KUR'AN'DAN MESAJLAR: BAKARA SURESİ 163-164. AYETLER", 14, "#6b21a8", "bold")
    ic += _kutu(28, 48, 644, 58, "#ffffff", "#c084fc", 8, 1.5)
    ic += _metin(350, 70, "Bakara 163: 'İlahınız bir tek ilahtır. O'ndan başka ilah yoktur. O Rahmân'dır, Rahîm'dir.'", 11, "#7e22ce", "bold")
    ic += _metin(350, 92, "Tevhit ilkesi bildirildikten hemen sonra 164. ayette evrendeki kozmolojik deliller sıralanır:", 11, "#334155")
    ic += _kutu(28, 114, 644, 60, "#faf5ff", "#9333ea", 8, 1.5)
    ic += _metin(350, 136, "Göklerin ve yerin yaratılışı • Gece-gündüzün ardışıklığı • Denizdeki gemiler • Yağmurla dirilen toprak", 10, "#581c87", "bold")
    ic += _metin(350, 158, "Rüzgârların ve bulutların yönetimi → 'Aklını kullanan bir topluluk için kesin deliller (âyât) vardır.'", 11, "#1e293b", "bold")
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