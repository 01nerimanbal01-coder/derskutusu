def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 200, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "İSLAM MEDENİYETİNDE DİNÎ İLİMLER VE ÖNCÜ ÂLİMLER", 14, "#166534", "bold")
    cols = [
        (25, "Tefsir İlmi", "Kur'an ayetlerini", "açıklama ve yorumlama", "Taberî, Zemahşerî,", "Râzî, Elmalılı Hamdi"),
        (192, "Hadis İlmi", "Hz. Peygamber'in söz", "ve fiillerini derleme", "Buhârî, Müslim,", "Tirmizî (Kütüb-i Sitte)"),
        (359, "Kelam İlmi", "İnanç esaslarını akıl", "ve nakille savunma", "Ebû Hanîfe, Mâtürîdî,", "Eş'arî, Gazzâlî"),
        (526, "Fıkıh İlmi", "İbadet ve hukuk", "hükümlerini belirleme", "Ebû Hanîfe, Şâfiî,", "Mâlik, Ahmed b. Hanbel")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 150, 148, "#ffffff", "#22c55e", 9, 1.5)
        ic += _metin(x+75, 70, b, 12, "#15803d", "bold")
        ic += _metin(x+75, 94, s1, 11, "#334155")
        ic += _metin(x+75, 112, s2, 11, "#334155")
        ic += _kutu(x+8, 126, 134, 58, "#dcfce7", "#86efac", 6, 1)
        ic += _metin(x+75, 148, s3, 10, "#14532d", "bold")
        ic += _metin(x+75, 168, s4, 10, "#166534")
    return _svg(700, 220, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 200, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "SOSYAL VE BEŞERÎ BİLİMLERDE MÜSLÜMAN BİLİM İNSANLARI", 14, "#1e3a8a", "bold")
    cols = [
        (25, "Coğrafya ve Seyahat", "Pîrî Reis (Kitâb-ı Bahriye)", "İdrîsî (Dünya Haritası)", "Evliya Çelebi, İbn Battûta", "Belhî, Mes'ûdî"),
        (248, "Tarih ve Sosyoloji", "İbn Haldûn (Mukaddime)", "Taberî (Târîhu'l-Ümem)", "İbnü'l-Esîr (el-Kâmil)", "Kâtip Çelebi (Cihannüma)"),
        (471, "Felsefe ve Hikmet", "Kindî (İlk İslam filozof)", "Fârâbî (Muallim-i Sânî)", "İbn Sînâ (eş-Şifâ)", "İbn Rüşd (Batı'da Averroes)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 148, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 72, b, 12, "#1d4ed8", "bold")
        ic += _metin(x+102, 98, "• " + s1, 11, "#1e293b", "bold")
        ic += _metin(x+102, 122, "• " + s2, 11, "#334155")
        ic += _metin(x+102, 146, "• " + s3, 11, "#334155")
        ic += _metin(x+102, 170, "• " + s4, 11, "#475569")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 205, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "FEN, DOĞA BİLİMLERİ VE TIP ALANINDA ÖNCÜ MÜSLÜMAN ÂLİMLER", 13, "#92400e", "bold")
    cols = [
        (25, "Matematik & Astronomi", "Hârizmî (Cebir ve 0 rakamı)", "Ömer Hayyam, البيروني (Bîrûnî)", "Uluğ Bey, Ali Kuşçu,", "Ferganî, Battânî"),
        (248, "Tıp ve Eczacılık", "İbn Sînâ (el-Kânûn fi't-Tıb)", "Ebû Bekir er-Râzî (Çiçek-Kızamık)", "Zehrâvî (Cerrahi Aletler)", "İbnü'n-Nefîs (Küçük Kan Dolaşımı), Akşemseddin"),
        (471, "Fizik, Kimya & Mühendislik", "İbnü'l-Heysem (Optik-Kitâbü'l-Menâzır)", "Câbir b. Hayyân (Kimyanın Babası)", "Cezerî (Sibernetik ve Robotik)", "Hazînî (Hassas Teraziler)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 152, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+102, 70, b, 11, "#b45309", "bold")
        ic += _metin(x+102, 96, s1, 10, "#1e293b", "bold")
        ic += _metin(x+102, 120, s2, 10, "#334155")
        ic += _metin(x+102, 144, s3, 10, "#334155")
        ic += _metin(x+102, 168, s4, 10, "#475569")
    return _svg(700, 225, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "KUR'AN'DAN MESAJLAR: FÂTIR SURESİ 27-28. AYETLER", 14, "#6b21a8", "bold")
    ic += _kutu(28, 48, 644, 62, "#ffffff", "#c084fc", 8, 1.5)
    ic += _metin(350, 72, "Evrendeki Renk, Çeşitlilik ve Düzen (Yağmur, Meyveler, Dağlar, Canlılar)", 12, "#7e22ce", "bold")
    ic += _metin(350, 94, "Tabiattaki tefekkür alanları insanı Yaratıcı'nın kudretini ve sanatını tanımaya yöneltir.", 11, "#334155")
    ic += _kutu(28, 120, 644, 62, "#faf5ff", "#9333ea", 8, 1.8)
    ic += _metin(350, 144, "Temel İlke: 'Kulları içinden ancak âlimler Allah'tan (gereğince) خشية (haşyet) duyar.'", 12, "#581c87", "bold")
    ic += _metin(350, 166, "Gerçek ilim, insanı kibre değil; Allah'a derin bir saygı, sevgi ve sorumluluk bilincine (haşyet) ulaştırır.", 11, "#334155")
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
