def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#0284c7", bg="#f0f9ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İslam Kültür ve Medeniyetinin Karakteristik Özellikleri</text>'
    ic += _kart(20, 45, 230, 185, "Tevhid, İlim ve Hikmet", [
        "• Tevhid: Varlık ve bilgi bütünlüğü",
        "• İlim: Vahiyle başlayan okuma emri",
        "• Akıl ve naklin uyumlu birlikteliği",
        "• Din-bilim çatışmasının olmaması",
        "• Beytü\'l-Hikme ve medrese geleneği"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(265, 45, 230, 185, "Adalet, Hoşgörü ve Barış", [
        "• Hak ve hukukun üstünlüğü (Kıst)",
        "• Farklı inançlara yaşama hakkı",
        "• Medine Vesikası ve Zimmet hukuku",
        "• Zorlama değil, ikna ve davet",
        "• Darü\'s-Selam (esenlik yurdu) ideal"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 185, "Evrensellik, Denge ve Vakıf", [
        "• Irk ve coğrafya üstü kuşatıcılık",
        "• Yerel kültürleri tevhidde mezcediş",
        "• Dünya-ahiret, madde-mana dengesi",
        "• Vakıf ve infak (hayır) medeniyeti",
        "• Estetik ve ihsan bilinci (İmar)"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İslam Medeniyetinin Merkez Havzaları (I): Hicaz, Şam ve Bağdat</text>'
    ic += _kart(20, 45, 230, 185, "1. Hicaz Havzası (Mekke-Medine)", [
        "• Vahyin indiği kurucu merkez",
        "• Kâbe ve Mescid-i Nebevî",
        "• Ashab-ı Suffe (ilk eğitim ocağı)",
        "• Hadis ve fıkıh ilminin doğuşu",
        "• Medine İslam şehir modeli"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(265, 45, 230, 185, "2. Şam ve Mısır Havzası", [
        "• Emevîler, Eyyûbîler ve Memlükler",
        "• Şam Emeviye Camii mimarisi",
        "• Kudüs (Mescid-i Aksa / Kubbetü\'s-Sahra)",
        "• Kahire: Ezher Üniversitesi",
        "• Haçlı ve Moğollara karşı direnç"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 185, "3. Irak / Bağdat Havzası", [
        "• Abbâsîlerin başkenti (Medînetü\'s-Selâm)",
        "• Beytü\'l-Hikme ve Tercüme Hareketi",
        "• Kûfe ve Basra dil-fıkıh ekolleri",
        "• Nizamiye Medreseleri",
        "• Hârizmî, Kindî ve İmam Ebû Hanîfe"
    ], "#2563eb", "#eff6ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İslam Medeniyetinin Merkez Havzaları (II): İran, Maveraünnehir ve Hint</text>'
    ic += _kart(20, 45, 230, 185, "4. İran - Horasan Havzası", [
        "• Nişabur, Merv, Rey ve İsfahan",
        "• Büyük Selçuklu kültür-ilim merkezi",
        "• Rasathaneler ve Nizamiye ağları",
        "• Gazâlî, Ömer Hayyam, التوسî",
        "• Edebiyat, minyatür ve mimari"
    ], "#9333ea", "#faf5ff")
    ic += _kart(265, 45, 230, 185, "5. Maveraünnehir - Türkistan", [
        "• Buhara, Semerkant, Taşkent, Fergana",
        "• Karahanlılar ve Timurlular dönemi",
        "• Buhârî, Tirmizî ve İmam Mâtürîdî",
        "• İbn Sînâ, Fârâbî, Bîrûnî, Uluğ Bey",
        "• Yesevîlik ve tasavvuf irfanı"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "6. Hint Alt Kıtası Havzası", [
        "• Gazneliler, Delhi Sultanlığı, Babürler",
        "• Agra, Delhi ve Lahor şehirleri",
        "• Tac Mahal ve Babür mimarisi",
        "• İmam Rabbânî ve Şah Veliyyullah",
        "• Çok kültürlü birlikte yaşama tecrübesi"
    ], "#be123c", "#fff1f2")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Batı\'ya Açılan İki Zirve: Endülüs ve Anadolu-Balkanlar Havzası</text>'
    ic += _kart(20, 45, 350, 175, "7. Endülüs ve Mağrib Havzası", [
        "• Kurtuba, Gırnata (Granada), İşbîliye (Sevilla), Tuleytula (Toledo)",
        "• Kurtuba Ulu Camii ve Elhamra Sarayı estetiği",
        "• İbn Rüşd, İbn Tufeyl, İbn Haldun, İbnü\'l-Arabî, الزهرâvî",
        "• Avrupa Rönesansı\'na kaynaklık eden kütüphaneler ve tercümeler",
        "• Müslüman, Hristiyan ve Yahudilerin bir arada yaşadığı hoşgörü"
    ], "#059669", "#ecfdf5")
    ic += _kart(390, 45, 350, 175, "8. Anadolu ve Balkanlar Havzası", [
        "• Konya, Bursa, Edirne, İstanbul, Saraybosna, Üsküp",
        "• Anadolu Selçuklu ve Osmanlı medeniyet terkibi",
        "• Mevlânâ, Yunus Emre, Hacı Bektâş-ı Velî, Mimar Sinan",
        "• Külliye, darüşşifa, kervansaray, imaret ve vakıf sistemi",
        "• İstimalet (gönül kazanma) politikası ve millet sistemi"
    ], "#1d4ed8", "#eff6ff")
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
