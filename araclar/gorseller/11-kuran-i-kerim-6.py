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
        'Sakin Mimin (مْ) Üç Okunuş Şekli (Dudak/Şefevî Tecvit Kuralları)</text>'
        + _kart(18, 42, 205, 148, "1. İdgam-ı Misleyn", [
            "• Kural: Sakin mimden (مْ)",
            "  sonra harekeli MİM (م) gelirse",
            "• İki mim birleştirilerek",
            "  şeddeli ve gunneli (1,5 elif)",
            "  okunur: لَكُمْ مَا -> لَكُمَّا"
        ], "#2563eb", "#eff6ff")
        + _kart(237, 42, 205, 148, "2. İhfa-i Şefevi", [
            "• Kural: Sakin mimden (مْ)",
            "  sonra harekeli BÂ (ب) gelirse",
            "• Dudaklar hafifçe değdirilip",
            "  mimin sesi gunneli olarak",
            "  gizlenir: تَرْم۪يهِمْ بِحِجَارَةٍ"
        ], "#059669", "#ecfdf5")
        + _kart(456, 42, 205, 148, "3. İzhar-ı Şefevi", [
            "• Kural: Sakin mimden (مْ)",
            "  sonra م ve ب dışındaki",
            "  diğer 26 harften biri gelirse",
            "• Sakin mim gunnesiz ve",
            "  açıkça okunur: اَلَمْ تَرَ"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 205, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="25" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Sakin Mim ile Sakin Nun Kurallarının Karşılaştırılması</text>'
        + _kart(25, 42, 300, 145, "Neden “Şefevî” (Dudakla İlgili) Denir?", [
            "• Mim (م) ve Bâ (ب) harflerinin mahreci (çıkış",
            "  yeri) dudaklardır (şefe = dudak).",
            "• Bu yüzden sakin mimin ihfasına İhfa-i Şefevi,",
            "  izharına ise İzhar-ı Şefevi adı verilir.",
            "• Vav (و) ve Fâ (ف) harflerinde izhar-ı şefeviye",
            "  daha çok dikkat edilir!"
        ], "#7c3aed", "#f5f3ff")
        + _kart(355, 42, 300, 145, "Kur’an-ı Kerim’den Uygulama Örnekleri", [
            "• İdgam-ı Misleyn: عَلَيْهِمْ مُؤْصَدَةٌ  /  لَهُمْ مَغْفِرَةٌ",
            "• İhfa-i Şefevi: رَبُّهُمْ بِذَنْبِهِمْ  /  وَمَا هُمْ بِمُؤْمِن۪ينَ",
            "• İzhar-ı Şefevi: اَنْعَمْتَ عَلَيْهِمْ  /  هُمْ ف۪يهَا",
            "• İklab (نْ + ب -> م) ile İhfa-i Şefevi’nin",
            "  okunuş keyfiyeti birbiriyle aynıdır."
        ], "#0284c7", "#f0f9ff")
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
