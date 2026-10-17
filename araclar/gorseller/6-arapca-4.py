def _svg(w, h, ic):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{ic}</svg>'

def _kutu(x, y, w, h, dolgu="#f8fafc", kenar="#cbd5e1", r=10, kalinlik=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kalinlik}"/>'

def _metin(x, y, icerik, boyut=12, renk="#1e293b", kalin="normal", hiza="middle"):
    return f'<text x="{x}" y="{y}" font-family="Inter,system-ui,sans-serif" font-size="{boyut}" fill="{renk}" font-weight="{kalin}" text-anchor="{hiza}">{icerik}</text>'

def gorsel_1():
    ic = _kutu(10, 10, 680, 200, "#fffbeb", "#f59e0b", 12, 2)
    ic += _metin(350, 34, "HARF-İ TARİF (اَلْ) İLE ŞEMSÎ VE KAMERÎ HARFLER", 14, "#92400e", "bold")
    ic += _kutu(28, 48, 310, 144, "#ffffff", "#f59e0b", 10, 1.8)
    ic += _metin(183, 72, "Şemsî Harfler (الْحُرُوفُ الشَّمْسِيَّةُ — 14 Harf)", 11, "#b45309", "bold")
    ic += _metin(183, 96, "ت ث د ذ ر ز س ش ص ض ط ظ ل ن", 12, "#1e293b", "bold")
    ic += _metin(183, 120, "• 'اَلْ' takısındaki 'ل' harfi OKUNMAZ!", 11, "#b91c1c", "bold")
    ic += _metin(183, 142, "• Sonraki harf ŞEDDELİ okunur:", 11, "#334155")
    ic += _metin(183, 166, "اَلشَّمْسُ (eş-şemsü) • اَلطَّبّاخُ (et-tabbâhu) • اَلسّائِقُ", 11, "#92400e", "bold")

    ic += _kutu(362, 48, 310, 144, "#eff6ff", "#3b82f6", 10, 1.8)
    ic += _metin(517, 72, "Kamerî Harfler (الْحُرُوفُ الْقَمَرِيَّةُ — 14 Harf)", 11, "#1d4ed8", "bold")
    ic += _metin(517, 96, "ا ب ج ح خ ع غ ف ق ك م هـ و ي", 12, "#1e293b", "bold")
    ic += _metin(517, 120, "• 'اَلْ' takısındaki 'ل' harfi CEZİMLİ OKUNUR!", 11, "#1d4ed8", "bold")
    ic += _metin(517, 142, "• Sonraki harf şeddelenmez:", 11, "#334155")
    ic += _metin(517, 166, "اَلْقَمَرُ (el-kameru) • اَلْمُعَلِّمُ (el-muallimü) • اَلْعَمُّ", 11, "#1e40af", "bold")
    return _svg(700, 220, ic)

def gorsel_2():
    ic = _kutu(10, 10, 680, 195, "#f0fdf4", "#16a34a", 12, 2)
    ic += _metin(350, 34, "MESLEKLERDE NİTELİK SIFATLARI: مَاهِرٌ (BECERİKLİ) VE نَشِيطٌ (ÇALIŞKAN)", 13, "#166534", "bold")
    cols = [
        (28, "Eril (Müzekker) Cümleler", "عَمّي طَبّاخٌ ماهِرٌ", "(Amcam usta/becerikli bir aşçıdır.)", "خالي فَلّاحٌ نَشيطٌ", "(Dayım çalışkan bir çiftçidir.)"),
        (362, "Dişil (Müennes) Cümleler (+ ة)", "عَمَّتي طَبّاخَةٌ ماهِرَةٌ", "(Halam usta/becerikli bir aşçıdır.)", "خالَتي مُمَرِّضَةٌ نَشيطَةٌ", "(Teyzem çalışkan bir hemşiredir.)")
    ]
    for x, b, s1, s2, s3, s4 in cols:
        ic += _kutu(x, 48, 310, 140, "#ffffff", "#22c55e", 10, 1.8)
        ic += _metin(x+155, 72, b, 12, "#15803d", "bold")
        ic += _metin(x+155, 98, s1, 13, "#1e293b", "bold")
        ic += _metin(x+155, 118, s2, 10, "#475569")
        ic += _metin(x+155, 144, s3, 13, "#1e293b", "bold")
        ic += _metin(x+155, 164, s4, 10, "#475569")
    return _svg(700, 215, ic)

def gorsel_3():
    ic = _kutu(10, 10, 680, 190, "#eff6ff", "#2563eb", 12, 2)
    ic += _metin(350, 34, "OLUMLU VE OLUMSUZ ÇALIŞMA YERİ CÜMLELERİ (يَعْمَلُ / لَا يَعْمَلُ)", 13, "#1e3a8a", "bold")
    rows = [
        (50, "Olumlu (Eril)", "يَعْمَلُ والِدي في الْمَدْرَسَةِ.", "Babam okulda çalışıyor."),
        (98, "Olumsuz (Eril)", "لا يَعْمَلُ والِدي في الْمَطْعَمِ.", "Babam lokantada çalışmıyor."),
        (146, "Olumsuz (Dişil)", "لا تَعْمَلُ والِدَتي في الْمَخْفَرِ.", "Annem karakolda çalışmıyor.")
    ]
    for y, tur, ar, tr in rows:
        ic += _kutu(25, y, 130, 38, "#dbeafe", "#2563eb", 8, 1.5)
        ic += _metin(90, y+24, tur, 11, "#1e40af", "bold")
        ic += _kutu(165, y, 270, 38, "#ffffff", "#93c5fd", 8, 1.2)
        ic += _metin(300, y+24, ar, 13, "#1e293b", "bold")
        ic += _metin(560, y+24, tr, 11, "#334155")
    return _svg(700, 210, ic)

def gorsel_4():
    ic = _kutu(10, 10, 680, 185, "#fdf4ff", "#a855f7", 12, 2)
    ic += _metin(350, 34, "1. ÜNİTE VECİZ SÖZÜ: AKRABAYA İYİLİK ÖNCELİĞİ", 14, "#6b21a8", "bold")
    ic += _kutu(35, 50, 630, 122, "#ffffff", "#c084fc", 10, 1.8)
    ic += _metin(350, 82, "اَلْأَقْرَبُونَ أَوْلَى بِالْمَعْرُوفِ", 18, "#7e22ce", "bold")
    ic += _metin(350, 112, "Okunuşu: el-Akrabûne evlâ bi'l-ma'rûf", 12, "#1e293b", "bold")
    ic += _metin(350, 136, "Anlamı: 'İyilik yapmaya en layık olanlar (öncelikli olanlar) en yakın akrabalardır.'", 11, "#581c87", "bold")
    ic += _metin(350, 158, "Sıla-i rahim (akraba ziyareti ve yardımlaşma) İslam ahlakının temel görevlerindendir.", 11, "#475569")
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
