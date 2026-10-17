def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "GENÇLİK YILLARINDA PEYGAMBERİMİZİN (SAV) AHLAKİ ERDEMLERİ", 13, "#166534", "bold")
    cols = [
        (25, "Muhammedü'l-Emîn", "Doğruluk ve Güvenilirlik", "Ticareti ve sözüyle herkesin", "güvendiği emanet ehli"),
        (192, "Hilfü'l-Fudûl Üyesi", "Adalet ve Mazlumun Yanı", "Haksızlığa uğrayanların", "hakkını savunan erdemli genç"),
        (359, "Kâbe Hakemliği", "Hikmet ve Uzlaştırıcılık", "Hacerü'l-Esved krizini", "barışla çözen bilge şahsiyet"),
        (526, "Hira'da Tefekkür", "İffet ve Hakikat Arayışı", "Putlardan uzak durup", "Yaratıcı'yı düşünen kul")
    ]
    for x, b, s1, s2, s3 in cols:
        ic += _kutu(x, 48, 150, 140, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 72, b, 11, "#15803d", "bold")
        ic += _metin(x+75, 96, s1, 10, "#1e293b", "bold")
        ic += _metin(x+75, 122, s2, 10, "#334155")
        ic += _metin(x+75, 142, s3, 10, "#334155")
    return _svg(700, 215, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "TEFEKKÜR SÜRECİNDEN RİSALETE (PEYGAMBERLİĞE) GEÇİŞ", 14, "#1e3a8a", "bold")
    ic += _kutu(30, 50, 190, 130, "#ffffff", "#3b82f6", 9, 1.5)
    ic += _metin(125, 76, "1. Cahiliye'den Uzaklaşma", 11, "#1d4ed8", "bold")
    ic += _metin(125, 104, "Putlara tapmadı, içki ve", 10, "#334155")
    ic += _metin(125, 124, "kumara hiç yaklaşmadı;", 10, "#334155")
    ic += _metin(125, 144, "iffetini ve onurunu korudu.", 10, "#1e40af", "bold")
    ic += _metin(238, 115, "→", 22, "#2563eb", "bold")
    ic += _kutu(255, 50, 190, 130, "#ffffff", "#3b82f6", 9, 1.5)
    ic += _metin(350, 76, "2. Hira'da Tefekkür", 11, "#1d4ed8", "bold")
    ic += _metin(350, 104, "35 yaşından itibaren", 10, "#334155")
    ic += _metin(350, 124, "Nur Dağı Hira Mağarası'nda", 10, "#334155")
    ic += _metin(350, 144, "evreni ve Yaratıcı'yı düşündü.", 10, "#1e40af", "bold")
    ic += _metin(463, 115, "→", 22, "#2563eb", "bold")
    ic += _kutu(480, 50, 190, 130, "#ffffff", "#3b82f6", 9, 1.5)
    ic += _metin(575, 76, "3. Risalet (610 - İlk Vahiy)", 11, "#1d4ed8", "bold")
    ic += _metin(575, 104, "40 yaşında Ramazan ayında", 10, "#334155")
    ic += _metin(575, 124, "Alak suresi 1-5 ('Oku!') ile", 10, "#334155")
    ic += _metin(575, 144, "peygamberlik görevi başladı.", 10, "#1e40af", "bold")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 185, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "İLK VAHİY SONRASINDA HZ. HATİCE'NİN (RA) TARİHİ TESELLİSİ", 13, "#92400e", "bold")
    ic += _kutu(28, 48, 644, 126, "#ffffff", "#f59e0b", 10, 1.5)
    ic += _metin(350, 74, "'Allah'a yemin ederim ki Allah seni asla utandırmaz ve yalnız bırakmaz!'", 12, "#b45309", "bold")
    ic += _metin(350, 100, "Çünkü sen: • Akrabalarını gözetirsin (sıla-i rahim) • Doğru konuşursun", 11, "#334155")
    ic += _metin(350, 122, "• İşini göremeyenlerin yükünü taşırsın • Yoksula kazandırır, misafiri ağırlarsın", 11, "#334155")
    ic += _metin(350, 146, "• Hak yolunda karşılaşılan felaketlerde insanlara yardım edersin! (Buhârî, Bed'ü'l-vahy, 3)", 11, "#92400e", "bold")
    return _svg(700, 205, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 190, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "GENÇLİĞİMİZ İÇİN PEYGAMBERİMİZDEN DÖRT ÖRNEK İLKE", 14, "#6b21a8", "bold")
    items = [
        (25, "Emin Olmak", "Sözünde ve işinde", "her zaman dürüst olmak"),
        (192, "Adil Olmak", "Zorbalığa karşı durup", "mazlumu koruyabilmek"),
        (359, "Üretken Olmak", "Alın teriyle çalışıp", "ailesine destek olmak"),
        (526, "Tefekkür Etmek", "Okumak, düşünmek ve", "zamanı iyi değerlendirmek")
    ]
    for x, b, s1, s2 in items:
        ic += _kutu(x, 48, 150, 134, "#ffffff", "#c084fc", 9, 1.5)
        ic += _metin(x+75, 76, b, 12, "#7e22ce", "bold")
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
