def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'أَسْمَاءُ اللّٰهِ الْحُسْنَى (Esmâ-i Hüsnâ: Haşr Suresi 22–24. Ayetlerdeki İsimler)</text>'
        + _kart(25, 42, 300, 145, "Rahmet, Hükümranlık ve Güven İsimleri", [
            "• اَلرَّحْمٰنُ (er-Rahmân): Dünyada tüm canlılara merhamet eden",
            "• اَلرَّح۪يمُ (er-Rahîm): Ahirette müminlere merhamet eden",
            "• اَلْمَلِكُ (el-Melik): Mülkün gerçek sahibi ve hükümdarı",
            "• اَلْقُدُّوسُ (el-Kuddûs): Her türlü eksiklikten münezzeh",
            "• اَلسَّلَامُ / اَلْمُؤْمِنُ : Esenlik ve güven veren"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 145, "Kudret ve Yaratma İsimleri", [
            "• اَلْمُهَيْمِنُ (el-Müheymin): Gözetip koruyan",
            "• اَلْعَز۪يزُ / اَلْجَبَّارُ / اَلْمُتَكَبِّرُ : Mutlak galip ve ulu",
            "• اَلْخَالِقُ (el-Hâlık): Takdir ederek yoktan yaratan",
            "• اَلْبَارِئُ (el-Bâri’): Uygun ve kusursuz var eden",
            "• اَلْمُصَوِّرُ / اَلْحَك۪يمُ : Şekil veren ve hikmet sahibi"
        ], "#059669", "#ecfdf5")
    )
    return _svg(680, 200, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'أَرْكَانُ الْإِيمَانِ (İslam İnancının Esasları ve Arapça Kalıplar)</text>'
        + _kart(25, 42, 300, 145, "İmanın Altı Esası (أَرْكَانُ الْإِيمَانِ السِّتَّةُ)", [
            "• 1. اَلْإِيمَانُ بِاللّٰهِ (Allah’a iman)",
            "• 2. اَلْإِيمَانُ بِالْمَلَائِكَةِ (Meleklere iman)",
            "• 3. اَلْإِيمَانُ بِالْكُتُبِ السَّمَاوِيَّةِ (İlahi kitaplara iman)",
            "• 4. اَلْإِيمَانُ بِالرُّسُلِ (Peygamberlere iman)",
            "• 5. اَلْآخِرَةُ  &amp;  6. اَلْقَضَاءُ وَالْقَدَرُ (Ahiret ve Kader)"
        ], "#d97706", "#fffbeb")
        + _kart(355, 42, 300, 145, "Temel Cümle ve Dil Bilgisi Kalıpları", [
            "• آمَنْتُ بِاللّٰهِ وَمَلَائِكَتِهِ... (Allah’a ve meleklerine inandım)",
            "• وَلِلّٰهِ الْأَسْمَاءُ الْحُسْنَى فَادْعُوهُ بِهَا (A’râf, 180)",
            "• هُوَ اللّٰهُ الَّذ۪ي لَا إِلٰهَ إِلَّا هُوَ (O, kendisinden başka",
            "  ilah olmayan Allah’tır - Haşr, 22)",
            "• آمَنَ - يُؤْمِنُ - إِيمَانًا (bâ harf-i cerri ile kullanılır)"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
}


def uygula(v):
    hedefler = [0, 1]
    anahtarlar = ["b1", "b2"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]