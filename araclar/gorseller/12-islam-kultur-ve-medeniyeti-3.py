def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 200, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "İSLAM MEDENİYETİNİN İLK MERKEZ HAVZALARI (HİCAZ, ŞAM, IRAK)", 13, "#92400e", "bold")
    cols = [
        (25, "1. Hicaz Havzası", "Mekke, Medine, Taif", "Vahyin ve sünnetin doğuşu", "Kâbe, Mescid-i Nebevî, Suffe", "Medine Vesikası"),
        (248, "2. Şam (Bilâdü'ş-Şam)", "Dımaşk, Kudüs, Halep", "Emevîlerin başkenti", "Mescid-i Aksâ, Kubbetü's-Sahra", "Emeviyye Camii"),
        (471, "3. Irak (Bağdat-Kûfe-Basra)", "Abbasîlerin başkenti", "Beytü'l-Hikme ve Nizâmiye", "Fıkıh ve dil mektepleri", "Medînetü's-Selâm (Bağdat)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 148, "#ffffff", "#f59e0b", 9, 1.5)
        ic += _metin(x+102, 72, b, 12, "#b45309", "bold")
        ic += _metin(x+102, 98, s1, 11, "#1e293b", "bold")
        ic += _metin(x+102, 122, s2, 11, "#334155")
        ic += _metin(x+102, 144, s3, 10, "#334155")
        ic += _metin(x+102, 168, s4, 10, "#92400e", "bold")
    return _svg(700, 220, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 200, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "DOĞU VE BATI BİLİM HAVZALARI (HORASAN-MÂVERÂÜNNEHİR, MISIR, ENDÜLÜS)", 12, "#1e3a8a", "bold")
    cols = [
        (25, "Horasan & Mâverâünnehir", "Buhara, Semerkant, Merv, Belh", "Buhârî, Mâtürîdî, İbn Sînâ,", "Fârâbî, Hârizmî, Uluğ Bey", "Türk-İslam rönesans merkezi"),
        (248, "Mısır ve Kuzey Afrika", "Kahire, İskenderiye, Kayrevan", "el-Ezher Camii ve Üniversitesi", "Fâtımî, Eyyûbî, Memlûk, Osmanlı", "Zeytûne ve Karaviyyîn"),
        (471, "Endülüs Havzası", "Kurtuba, Gırnata, İşbîliye", "Kurtuba Camii, el-Hamrâ Sarayı", "İbn Rüşd, Zehrâvî, İbn Hazm", "Avrupa'ya bilimin geçiş köprüsü")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 204, 148, "#ffffff", "#3b82f6", 9, 1.5)
        ic += _metin(x+102, 72, b, 11, "#1d4ed8", "bold")
        ic += _metin(x+102, 98, s1, 10, "#1e293b", "bold")
        ic += _metin(x+102, 122, s2, 10, "#334155")
        ic += _metin(x+102, 144, s3, 10, "#334155")
        ic += _metin(x+102, 168, s4, 10, "#1e40af", "bold")
    return _svg(700, 220, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "ANADOLU, BALKANLAR VE HİNT ALT KITASI HAVZALARI", 14, "#166534", "bold")
    ic += _kutu(28, 48, 310, 140, "#ffffff", "#22c55e", 10, 1.8)
    ic += _metin(183, 72, "Anadolu ve Balkanlar Havzası", 12, "#15803d", "bold")
    ic += _metin(183, 98, "• Selçuklu, Beylikler ve Osmanlı mirası", 11, "#334155")
    ic += _metin(183, 120, "• Konya, Bursa, Edirne, İstanbul, Saraybosna", 11, "#334155")
    ic += _metin(183, 142, "• Mevlânâ, Yunus Emre, Hacı Bektaş-ı Velî", 11, "#334155")
    ic += _metin(183, 166, "• Süleymaniye ve Selimiye Külliyeleri", 11, "#166534", "bold")

    ic += _kutu(362, 48, 310, 140, "#ffffff", "#22c55e", 10, 1.8)
    ic += _metin(517, 72, "Hint Alt Kıtası Havzası", 12, "#15803d", "bold")
    ic += _metin(517, 98, "• Gazneliler, Delhi Sultanlığı ve Babürlüler", 11, "#334155")
    ic += _metin(517, 120, "• Delhi, Agra ve Lahor kültür merkezleri", 11, "#334155")
    ic += _metin(517, 142, "• İmam Rabbânî, Şah Veliyyullah ed-Dihlevî", 11, "#334155")
    ic += _metin(517, 166, "• Tac Mahal (Babür İslam mimarisi şaheseri)", 11, "#166534", "bold")
    return _svg(700, 215, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "FARKLI COĞRAFYALARDA ORTAK MEDENİYET RUHU: KESRETTE VAHDET", 13, "#6b21a8", "bold")
    ic += _kutu(30, 50, 640, 122, "#ffffff", "#c084fc", 10, 1.5)
    ic += _metin(350, 78, "Ortak Temel: Tevhit İnancı + Kur'an ve Sünnet + Adalet ve Vakıf Ruhu", 12, "#7e22ce", "bold")
    ic += _metin(350, 108, "Kurtuba'dan Semerkant'a, Saraybosna'dan Agra'ya kadar yerel mimari, dil ve sanat", 11, "#334155")
    ic += _metin(350, 130, "unsurları dışlanmamış; tevhit potasında birleşerek 'çokluk içinde birlik' (kesrette vahdet)", 11, "#334155")
    ic += _metin(350, 152, "anlayışıyla evrensel İslam medeniyeti meydana getirilmiştir.", 11, "#581c87", "bold")
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
