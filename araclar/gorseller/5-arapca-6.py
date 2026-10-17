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
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Selamlaşma, Karşılama ve Vakit Selamları (التَّحِيَّاتُ)</text>'
    ic += _kart(20, 45, 230, 185, "İslam Selamı ve Veciz Söz", [
        "• اَلسَّلَامُ عَلَيْكُمْ : Selam üzerinize olsun",
        "• وَعَلَيْكُمُ السَّلَامُ : Sizin de üzerinize",
        "• Veciz Söz (Hadis):",
        "  اَلسَّلَامُ قَبْلَ الْكَلَامِ",
        "  (Selam, kelamdan/sözden öncedir!)"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "Karşılama İfadeleri", [
        "• مَرْحَبًا : Merhaba",
        "• مَرْحَبًا بِكَ (Erkeğe) / بِكِ (Kıza)",
        "• أَهْلًا وَسَهْلًا : Hoş geldiniz",
        "• أَهْلًا بِكَ (Erkeğe) / بِكِ (Kıza):",
        "  Hoş bulduk"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "Sabah ve Akşam Selamları", [
        "• صَبَاحُ الْخَيْرِ : Günaydın (Hayırlı sabahlar)",
        "• صَبَاحُ النُّورِ : Günaydın (Nurlu sabahlar)",
        "• مَسَاءُ الْخَيْرِ : İyi akşamlar",
        "• مَسَاءُ النُّورِ : İyi akşamlar (cevap)",
        "• شُكْرًا (Teşekkürler) -> عَفْوًا (Rica ederim)"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Tanışma, Hal-Hatır Sorma ve Memnuniyet İfadeleri</text>'
    ic += _kart(20, 45, 350, 175, "İsim Sorma ve Hal-Hatır (المُتَعَارَفَةُ)", [
        "• مَا اسْمُكَ؟ (Erkeğe: Adın ne?) -> اِسْمِي أَحْمَدُ (Adım Ahmet)",
        "• مَا اسْمُكِ؟ (Kıza: Adın ne?) -> اِسْمِي زَيْنَبُ (Adım Zeynep)",
        "• كَيْفَ حَالُكَ؟ (Erkeğe: Nasılsın?)",
        "• كَيْفَ حَالُكِ؟ (Kıza: Nasılsın?)",
        "• Cevap: أَنَا بِخَيْرٍ، وَالْحَمْدُ لِلَّهِ (İyiyim, Allah\'a hamdolsun)"
    ], "#2563eb", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Tanışma Memnuniyeti ve Vedalaşma", [
        "• تَشَرَّفْتُ (بِمَعْرِفَتِكَ / كِ) : Tanıştığımıza memnun oldum",
        "• فُرْصَةٌ سَعِيدَةٌ : Memnun oldum (Mutlu bir fırsat)",
        "• إِلَى اللِّقَاءِ : Görüşmek üzere",
        "• مَعَ السَّلَامَةِ : Güle güle (Selametle)",
        "• فِي أَمَانِ اللَّهِ : Allah\'a emanet ol"
    ], "#d97706", "#fffbeb")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Soru Kalıbı (هَلْ أَنْتَ / هَلْ أَنْتِ...؟) ve Sınıf Yönergeleri</text>'
    ic += _kart(20, 45, 350, 175, "هَلْ (Mı / Mi?) Soru Kalıbı ve Cevapları", [
        "• هَلْ أَنْتَ طَالِبٌ؟ (Sen erkek öğrenci misin?)",
        "  -> نَعَمْ، أَنَا طَالِبٌ. (Evet, ben öğrenciyim.)",
        "• هَلْ أَنْتِ طَالِبَةٌ؟ (Sen kız öğrenci misin?)",
        "  -> نَعَمْ، أَنَا طَالِبَةٌ. (Evet, ben kız öğrenciyim.)",
        "• Olumsuz cevap: لَا، أَنَا مُعَلِّمٌ / مُعَلِّمَةٌ (Hayır, öğretmenim.)"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 175, "Sınıf İçi Yönergeler (Müzekker ve Müennes)", [
        "• قُمْ! (Erkek: Ayağa kalk!) — قُومِي! (Kız: Ayağa kalk!)",
        "• اِجْلِسْ! (Erkek: Otur!) — اِجْلِسِي! (Kız: Otur!)",
        "• اِقْرَأْ! (Erkek: Oku!) — اِقْرَئِي! (Kız: Oku!)",
        "• اُكْتُبْ! (Erkek: Yaz!) — اُكْتُبِي! (Kız: Yaz!)",
        "• مِنْ فَضْلِكَ / مِنْ فَضْلِكِ : Lütfen! • يَا أَحْمَدُ : Ey Ahmet!"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">1. Ünite Genel Tekrarı: Müzekker (Eril) ve Müennes (Dişil) Zamir Farkı</text>'
    ic += _kart(20, 45, 350, 175, "Erkek Muhatap İçin (المُذَكَّرُ — كَ / أَنْتَ)", [
        "• أَنْتَ (Ente): Sen (Erkek)",
        "• مَا اسْمُكَ؟ (Mesmüke?): Senin adın ne?",
        "• كَيْفَ حَالُكَ؟ (Keyfe hâlüke?): Nasılsın?",
        "• مَرْحَبًا بِكَ / أَهْلًا بِكَ : Hoş bulduk",
        "• قُمْ، اِجْلِسْ، اِقْرَأْ، اُكْتُبْ (Sonu cezimli emir)"
    ], "#1d4ed8", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Kız Muhatap İçin (المُؤَنَّثُ — كِ / أَنْتِ)", [
        "• أَنْتِ (Enti): Sen (Kız)",
        "• مَا اسْمُكِ؟ (Mesmüki?): Senin adın ne?",
        "• كَيْفَ حَالُكِ؟ (Keyfe hâlüki?): Nasılsın?",
        "• مَرْحَبًا بِكِ / أَهْلًا بِكِ : Hoş bulduk",
        "• قُومِي، اِجْلِسِي، اِقْرَئِي، اُكْتُبِي (Sonu ي uzatmalı emir)"
    ], "#9333ea", "#faf5ff")
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
