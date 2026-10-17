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
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'İslam Öncesi Mekke’de Toplumsal Tabakalaşma ve Kabile Yapısı</text>'
        + _kart(20, 42, 200, 138, "1. Hürler (Eşrâf / Ahrâr)", [
            "• Kabile reisleri ve zenginler",
            "• Dârünnedve üyeleri",
            "• Tüm siyasi ve ticari haklara",
            "  sahip ayrıcalıklı sınıf"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 138, "2. Mevalî (Azatlılar / Mülteci)", [
            "• Azat edilmiş eski köleler",
            "• Veya kabile korumasındaki",
            "  yabancılar (Halîf)",
            "• Kısıtlı toplumsal haklar"
        ], "#d97706", "#fffbeb")
        + _kart(460, 42, 200, 138, "3. Köle ve Cariyeler (Esirler)", [
            "• Savaş esirleri veya borçlular",
            "• Alınıp satılan eşya statüsü",
            "• Hiçbir hukuki güvencesi",
            "  olmayan ezilen kesim"
        ], "#dc2626", "#fef2f2")
    )
    return _svg(680, 195, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Cahiliye Kültüründe Temel Sorunlar ve Asabiyet Anlayışı</text>'
        + _kart(25, 42, 300, 145, "Kabilecilik (Asabiyet) ve Kan Davaları", [
            "• ”Zalim de olsa mazlum da olsa kabilene yardım et!”",
            "• Haklılık değil, kabile bağı ölçü alınırdı",
            "• Yıllarca süren Eyyâmü’l-Arab (Arap savaşları)",
            "• Haram aylarda yapılan الفجار (Ficâr) Savaşları",
            "• Güçlünün zayıfı ezdiği kuralsız düzen"
        ], "#dc2626", "#fef2f2")
        + _kart(355, 42, 300, 145, "Ahlaki Çöküntü ve Kadının Konumu", [
            "• Kız çocuklarının diri diri gömülmesi (Ve’d-i benât)",
            "• Kadınların mirastan pay alamaması",
            "• İçki, kumar (meysir), tefecilik (riba) ve fal okları",
            "• Putperestlik ve Kâbe’nin 360 putla doldurulması",
            "• Batıl inançlar, kâhinlik ve büyücülük"
        ], "#9333ea", "#faf5ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'Cahiliye Dönemindeki Olumlu Hasletler ve Erdemli Kurumlar</text>'
        + _kart(25, 42, 300, 145, "Hilfü’l-Fudûl (Erdemliler Topluluğu)", [
            "• Mekke’de zulme uğrayan yabancı tüccarları ve",
            "  mazlumları korumak için kurulan cemiyet",
            "• Abdullah b. Cüd’an’ın evinde toplanıldı",
            "• Hz. Muhammed (sav) 20 yaşındayken katıldı",
            "• Peygamberlikten sonra da övgüyle anmıştır"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Korunan Güzel Gelenekler ve Haniflik", [
            "• Misafirperverlik ve cömertlik (Kerem)",
            "• Sözünde durma ve emanete riayet (Ahde vefa)",
            "• Şiir, hitabet ve belagat sanatı (Ukâz Panayırı)",
            "• Hz. İbrahim’in tevhit dinini yaşatan Hanifler",
            "• (Zeyd b. Amr, Kus b. Sâide, Varaka b. Nevfel)"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 200, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Cahiliye Zihniyeti ile İslam’ın Getirdiği Evrensel İlkeler Karşılaştırması</text>'
        + _kart(25, 42, 300, 135, "Cahiliye Zihniyeti", [
            "• Soy, kabile ve servet üstünlüğü",
            "• Kan davası ve sınırsız intikam",
            "• Kadının ve yetimin haklarının gaspı",
            "• Putlara tapınma ve şirk inancı"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 135, "İslam’ın Tevhit ve Adalet Düzeni", [
            "• Üstünlük yalnızca takva (sorumluluk) iledir",
            "• Hukuk, adalet, sulh ve can güvenliği",
            "• Kadın, çocuk, yetim ve köle haklarının korunması",
            "• Yalnızca Allah’a (cc) kulluk (Tevhit)"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 190, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
