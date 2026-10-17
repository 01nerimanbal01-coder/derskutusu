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
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'de Üç Temel Hareke ve Telaffuz Özellikleri</text>'
    ic += _kart(20, 45, 230, 185, "1. Üstün (Fetha — َ )", [
        "• Harfin ÜZERİNE yazılan yatık çizgi",
        "• İnce harfleri \'e\' sesiyle okutur:",
        "  بَ (be), تَ (te), كَ (ke), مَ (me)",
        "• Kalın harfleri \'a\' sesiyle okutur:",
        "  خَ (ha), صَ (sa), قَ (ka), طَ (ta)"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "2. Esre (Kesra — ِ )", [
        "• Harfin ALTINA yazılan yatık çizgi",
        "• İnce harfleri \'i\' sesiyle okutur:",
        "  بِ (bi), سِ (si), لِ (li), مِ (mi)",
        "• Kalın harfleri \'ı-i\' arası okutur:",
        "  صِ (sı/si), ضِ (dı/di), طِ (tı/ti)"
    ], "#2563eb", "#eff6ff")
    ic += _kart(510, 45, 230, 185, "3. Ötre (Damme — ُ )", [
        "• Harfin ÜZERİNE yazılan küçük vav (و)",
        "• İnce harfleri \'ü-u\' arası okutur:",
        "  بُ (bü/bu), تُ (tü/tu), كُ (kü/ku)",
        "• Kalın harfleri tok \'u\' ile okutur:",
        "  خُ (hu), صُ (su), قُ (ku), طُ (tu)"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kalın Okunan 7 Harf (Hurûf-u İstî\'lâ) ve Peltek Okunan 3 Harf</text>'
    ic += _kart(20, 45, 350, 175, "Her Zaman Kalın Okunan 7 Harf", [
        "• Harfler: خ — ص — ض — غ — ط — ق — ظ",
        "• Kodlama: \'Hussa Dagıt Kaz\' (خُصَّ ضَغْطٍ قِظْ)",
        "• Bu 7 harf üstün aldığında tok \'a\' sesiyle okunur:",
        "  خَ (ha), صَ (sa), ضَ (da), غَ (ğa), طَ (ta), قَ (ka), ظَ (za)",
        "• Ayrıca ر (Râ) harfi üstün ve ötreli iken kalın (ra, ru) okunur"
    ], "#d97706", "#fffbeb")
    ic += _kart(390, 45, 350, 175, "Dil Ucuyla Peltek Okunan 3 Harf", [
        "• 1. ث (Sê): İnce ve peltek okunur -> ثَ (se), ثِ (si), ثُ (sü)",
        "• 2. ذ (Zel): İnce ve peltek okunur -> ذَ (ze), ذِ (zi), ذُ (zü)",
        "• 3. ظ (Zı): Kalın ve peltek okunur -> ظَ (za), ظِ (zı), ظُ (zu)",
        "• Peltek harflerde dilin ucu üst ön dişlerin ucuna hafifçe değer",
        "• س - ث - ص ve ز - ذ - ظ ayrımlarına dikkat edilmelidir!"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Boğaz Harfleri (Hurûf-u Halk) ve Benzer Sesli Harflerin Telaffuzu</text>'
    ic += _kart(20, 45, 350, 175, "6 Boğaz Harfi (Boğazın 3 Bölgesinden Çıkanlar)", [
        "• Boğazın Göğse Bitişik Alt Kısmı: ء (Hemze) ve ه (Hê)",
        "• Boğazın Orta Kısmı (Sıkarak): ع (Ayn) ve ح (Hâ)",
        "  -> عَ (a\'), عِ (i\'), عُ (u\') / حَ (ha), حِ (hi), حُ (hu)",
        "• Boğazın Ağıza Yakın Üst Kısmı (Hırıltılı): غ (Gayn) ve خ (Hı)",
        "  -> غَ (ğa), غِ (ğı), غُ (ğu) / خَ (ha), خِ (hı), خُ (hu)"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Birbirine Karıştırılmaması Gereken Harf Grupları", [
        "• ت (Tê: İnce) ile ط (Tı: Kalın ve tok)",
        "• د (Dâl: İnce) ile ض (Dâd: Kalın, yan dişlerden)",
        "• ك (Kêf: İnce \'ke\') ile ق (Kâf: Kalın, küçük dilden \'ka\')",
        "• ه (Hê: Göğüsten yumuşak) - ح (Hâ: Boğaz ortası) - خ (Hı: Hırıltılı)",
        "• ء (Hemze: Keskin) ile ع (Ayn: Boğaz ortasından çatallı)"
    ], "#0f766e", "#f0fdfa")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Üç Harekeli Kelime Okuma Alıştırmaları (Sağdan Sola!)</text>'
    ic += _kart(20, 45, 230, 175, "Yalnızca Üstünlü Kelimeler", [
        "• كَتَبَ -> ke - te - be (Yazdı)",
        "• خَلَقَ -> ha - le - ka (Yarattı)",
        "• رَزَقَ -> ra - ze - ka (Rızık verdi)",
        "• صَدَقَ -> sa - de - ka (Doğru söyledi)",
        "• نَصَرَ -> na - sa - ra (Yardım etti)"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "Üstün ve Esreli Kelimeler", [
        "• عَلِمَ -> a\' - li - me (Bildi)",
        "• سَمِعَ -> se - mi - a\' (İşitti)",
        "• حَمِدَ -> ha - mi - de (Hamdetti)",
        "• شَهِدَ -> şe - hi - de (Şahit oldu)",
        "• عَمِلَ -> a\' - mi - le (Amel etti)"
    ], "#2563eb", "#eff6ff")
    ic += _kart(510, 45, 230, 175, "Ötre, Esre ve Üstünlü Kelimeler", [
        "• كُتِبَ -> kü - ti - be (Yazıldı)",
        "• خُلِقَ -> hu - li - ka (Yaratıldı)",
        "• قُرِئَ -> ku - ri - e (Okundu)",
        "• رُسُلُ -> ru - sü - lü (Elçiler)",
        "• كُتُبُ -> kü - tü - bü (Kitaplar)"
    ], "#7c3aed", "#f5f3ff")
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
