def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Çokgenlerde Kenar Sayısı, Köşe Sayısı ve İç Açı Sayısı İlişkisi</text>'
    sekiller = [
        ("Üçgen", "3 Kenar • 3 Köşe", "3 İç Açı • 0 Köşegen", '<polygon points="95,70 45,155 145,155" fill="#dbeafe" stroke="#2563eb" stroke-width="2.5"/>', "#2563eb", 20),
        ("Dörtgen", "4 Kenar • 4 Köşe", "4 İç Açı • 2 Köşegen", '<polygon points="235,75 315,75 325,155 225,155" fill="#dcfce7" stroke="#059669" stroke-width="2.5"/>', "#059669", 203),
        ("Beşgen", "5 Kenar • 5 Köşe", "5 İç Açı • 5 Köşegen", '<polygon points="460,68 510,105 492,158 428,158 410,105" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>', "#d97706", 386),
        ("Altıgen", "6 Kenar • 6 Köşe", "6 İç Açı • 9 Köşegen", '<polygon points="625,70 675,70 700,112 675,155 625,155 600,112" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2.5"/>', "#7c3aed", 570)
    ]
    for ad, s1, s2, poly, r, x in sekiller:
        ic += f'<rect x="{x}" y="45" width="170" height="185" rx="10" fill="#ffffff" stroke="{r}" stroke-width="2"/>'
        ic += poly
        ic += f'<text x="{x+85}" y="182" font-family="sans-serif" font-size="13" font-weight="bold" fill="{r}" text-anchor="middle">{ad}</text>'
        ic += f'<text x="{x+85}" y="200" font-family="sans-serif" font-size="11" fill="#1e293b" text-anchor="middle">{s1}</text>'
        ic += f'<text x="{x+85}" y="218" font-family="sans-serif" font-size="11" fill="#475569" text-anchor="middle">{s2}</text>'
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Açılarına ve Kenarlarına Göre Üçgen Çeşitleri</text>'
    ic += _kart(20, 45, 350, 185, "Açılarına Göre Üçgenler", [
        "• Dar Açılı Üçgen: Üç iç açısı da 90°\'den küçüktür",
        "  (Örn: 50°, 60°, 70°)",
        "• Dik Açılı Üçgen: Bir iç açısı tam 90°\'dir",
        "  (Diğer iki açısı dar açıdır)",
        "• Geniş Açılı Üçgen: Bir iç açısı 90°\'den büyüktür",
        "  (Bir üçgende en fazla 1 dik veya 1 geniş açı olur!)"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(390, 45, 350, 185, "Kenarlarına Göre Üçgenler", [
        "• Eşkenar Üçgen: Üç kenar uzunluğu birbirine eşittir",
        "  (Üç iç açısı da eşittir ve her biri 60°\'dir)",
        "• İkizkenar Üçgen: İki kenar uzunluğu birbirine eşittir",
        "  (Eşit kenarları gören iki taban açısı da eşittir)",
        "• Çeşitkenar Üçgen: Üç kenar uzunluğu da farklıdır",
        "  (Üç iç açısının ölçüsü de birbirinden farklıdır)"
    ], "#059669", "#ecfdf5")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Özel Dörtgenlerin Kenar ve Açı Özellikleri</text>'
    ic += _kart(20, 45, 230, 185, "Kare ve Dikdörtgen", [
        "• Karşılıklı kenarları paraleldir",
        "• Bütün iç açıları 90° (dik açı)",
        "• Karede 4 kenar uzunluğu eşittir",
        "• Dikdörtgende karşılıklı kenarlar",
        "  birbirine eşittir",
        "• Köşegen uzunlukları birbirine eşittir"
    ], "#2563eb", "#eff6ff")
    ic += _kart(265, 45, 230, 185, "Paralelkenar ve Eşkenar Dörtgen", [
        "• Karşılıklı kenarları paraleldir",
        "• Karşılıklı açı ölçüleri eşittir",
        "• Eşkenar dörtgende 4 kenar eşittir",
        "• Paralelkenarda karşılıklı kenarlar",
        "  birbirine eşittir",
        "• Açıları 90° olmak zorunda değildir"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 185, "Yamuk", [
        "• En az bir çift karşılıklı kenarı",
        "  birbirine paralel olan dörtgendir",
        "• İkizkenar yamukta paralel olmayan",
        "  yan kenarlar birbirine eşittir",
        "• Dik yamukta iki açısı 90°\'dir",
        "• 2 tane köşegeni vardır"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Düzgün Çokgenler ve Günlük Yaşamda Çokgen Modelleri</text>'
    ic += _kart(20, 45, 350, 175, "Düzgün Çokgen Nedir?", [
        "• Bütün kenar uzunlukları birbirine eşit VE",
        "• Bütün iç açılarının ölçüleri birbirine eşit olan çokgendir",
        "• Eşkenar Üçgen = 3 kenarlı düzgün çokgen (60°)",
        "• Kare = 4 kenarlı düzgün çokgen (90°)",
        "• Düzgün Beşgen (108°) ve Düzgün Altıgen (120°)"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 175, "Dikkat: Her Eşit Kenarlı Çokgen Düzgün müdür?", [
        "• Dikdörtgenin açıları eşit (90°) ama kenarları eşit değil -> Düzgün DEĞİL",
        "• Eşkenar dörtgenin kenarları eşit ama açıları eşit değil -> Düzgün DEĞİL",
        "• Bal peteği: Doğadaki en güzel düzgün altıgen modelidir",
        "• Trafik levhaları: Üçgen (uyarı), Sekizgen (DUR levhası)",
        "• Futbol topu yüzeyinde düzgün beşgen ve altıgenler kullanılır"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]
