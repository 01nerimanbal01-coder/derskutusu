def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Geniş Aile ve Akraba İsimleri (أَسْمَاءُ الْأَقَارِبِ)</text>'
    ic += _kart(20, 45, 230, 185, "Çekirdek Aile Bireyleri", [
        "• وَالِدٌ (أَبٌ) : Baba",
        "• وَالِدَةٌ (أُمٌّ) : Anne",
        "• وَلَدٌ (اِبْنٌ) : Erkek çocuk / Oğul",
        "• بِنْتٌ (اِبْنَةٌ) : Kız çocuk / Kız",
        "• أَخٌ : Erkek kardeş • أُخْتٌ : Kız kardeş"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "Büyükbaba, Büyükanne ve Torun", [
        "• جَدٌّ : Dede (Büyükbaba)",
        "• جَدَّةٌ : Nine (Anneanne / Babaanne)",
        "• حَفِيدٌ : Erkek torun",
        "• حَفِيدَةٌ : Kız torun",
        "• أُسْرَةٌ (عَائِلَةٌ) : Aile"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "Baba ve Anne Tarafı Akrabalar", [
        "• عَمٌّ : Amca (Babanın erkek kardeşi)",
        "• عَمَّةٌ : Hala (Babanın kız kardeşi)",
        "• خَالٌ : Dayı (Annenin erkek kardeşi)",
        "• خَالَةٌ : Teyze (Annenin kız kardeşi)",
        "• أَقَارِبُ : Akrabalar"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Meslekler (الْمِهَنُ) — Müzekker (Eril) ve Müennes (Dişil) Karşılıkları</text>'
    ic += _kart(20, 45, 230, 185, "Eğitim, Sağlık ve Hukuk", [
        "• مُعَلِّمٌ / مُعَلِّمَةٌ : Öğretmen",
        "• مُمَرِّضٌ / مُمَرِّضَةٌ : Hemşire",
        "  (Hasta bakıcı / sağlık görevlisi)",
        "• بَيْطَرِيٌّ / بَيْطَرِيَّةٌ : Veteriner",
        "• مُحَامٍ / مُحَامِيَةٌ : Avukat"
    ], "#2563eb", "#eff6ff")
    ic += _kart(265, 45, 230, 185, "Güvenlik, Ulaşım ve Üretim", [
        "• شُرْطِيٌّ / شُرْطِيَّةٌ : Polis",
        "• ضَابِطٌ / ضَابِطَةٌ : Subay / Komiser",
        "• سَائِقٌ / سَائِقَةٌ : Şoför / Sürücü",
        "• فَلَّاحٌ / فَلَّاحَةٌ : Çiftçi",
        "• طَبَّاخٌ / طَبَّاخَةٌ : Aşçı"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 185, "Meslek Niteleme Sıfatları", [
        "• مَاهِرٌ (Erkek) / مَاهِرَةٌ (Kadın):",
        "  Yetenekli, usta, becerikli",
        "• نَشِيطٌ (Erkek) / نَشِيطَةٌ (Kadın):",
        "  Çalışkan, gayretli, enerjik",
        "• عَمِّي طَبَّاخٌ مَاهِرٌ (Amcam usta aşçıdır)"
    ], "#0f766e", "#f0fdfa")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Hedef Dil Yapıları: Meslek, Çalışma Yeri ve Sayı Sorma</text>'
    ic += _kart(20, 45, 350, 175, "Meslek ve Çalışma Yeri Kalıpları", [
        "• مَا مِهْنَتُهُ؟ (Onun [E] mesleği ne?) -> هُوَ فَلَّاحٌ.",
        "• مَا مِهْنَتُهَا؟ (Onun [K] mesleği ne?) -> هِيَ مُمَرِّضَةٌ.",
        "• أَيْنَ يَعْمَلُ عَمُّكَ؟ (Amcan nerede çalışıyor?)",
        "  -> هُوَ يَعْمَلُ فِي الْمَطْعَمِ / فِي الْمَزْرَعَةِ.",
        "• أَيْنَ تَعْمَلُ خَالَتُكَ؟ -> هِيَ تَعْمَلُ فِي الْمُسْتَشْفَى."
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Olumsuz Cümle ve كَمْ (Kaç?) Soru Kalıbı", [
        "• لَا يَعْمَلُ فِي... (Erkek ...-de çalışmıyor)",
        "• لَا تَعْمَلُ فِي... (Kadın ...-de çalışmıyor)",
        "• أَيْنَ الْوَالِدُ؟ -> هُوَ فِي الْعَمَلِ (O iştedir).",
        "• كَمْ عَمًّا لَكَ؟ (Senin kaç amcan var?) -> لِي عَمَّانِ.",
        "• كَمْ أَخًا لِأَحْمَدَ؟ (Ahmet\'in kaç kardeşi var?)"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Harf-i Ta\'rîf (اَلْ) ile Şemsî ve Kamerî Harfler</text>'
    ic += _kart(20, 45, 350, 175, "Şemsî Harfler (الْحُرُوفُ الشَّمْسِيَّةُ - 14 Harf)", [
        "• ت، ث، د، ذ، ر، ز، س، ش، ص، ض، ط، ظ، ل، ن",
        "• Başına اَلْ geldiğinde \'Lâm\' (ل) harfi OKUNMAZ!",
        "• Lâm\'dan sonraki harf ŞEDDELİ (ّ ) okunur:",
        "• Örnekler: اَلشُّرْطِيُّ (Eş-şurtiyyü), اَلضَّابِطُ (Ed-dâbitu),",
        "  اَلطَّبَّاخُ (Et-tabbâhu), اَلسَّائِقُ (Es-sâiku)"
    ], "#d97706", "#fffbeb")
    ic += _kart(390, 45, 350, 175, "Kamerî Harfler (الْحُرُوفُ الْقَمَرِيَّةُ - 14 Harf)", [
        "• ا، ب، ج، ح، خ، ع، غ، ف، ق، ك، م، و، ه، ي",
        "• Başına اَلْ geldiğinde \'Lâm\' (لْ) harfi CEZİMLİ OKUNUR!",
        "• Sonraki harf şeddelenmez, kendi harekesiyle okunur:",
        "• Örnekler: اَلْجَدُّ (El-ceddü), اَلْعَمُّ (El-\'ammü),",
        "  اَلْخَالُ (El-hâlü), اَلْمُعَلِّمُ (El-mu\'allimü), اَلْفَلَّاحُ"
    ], "#15803d", "#f0fdf4")
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
