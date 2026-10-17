def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Hz. Peygamber\'in (s.a.v.) Gençlere Yaklaşımı ve Rehberlik İlkeleri</text>'
    ic += _kart(20, 45, 230, 175, "1. Güven ve Sorumluluk", [
        "• Gençlerin potansiyeline tam güven",
        "• Önemli görevler tevdi etme",
        "• Öğretmenlik, elçilik, komutanlık",
        "• Darü\'l-Erkam\'ın genç kadrosu",
        "• İstişarede gençlere söz hakkı"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "2. Şefkat ve Anlayış", [
        "• Hataları kırmadan düzeltme",
        "• Onur kırıcı sözden kaçınma",
        "• İkna ve hikmetle muamele",
        "• Duygularını ve heyecanını anlama",
        "• Kolaylaştırıcı ve müjdeleyici dil"
    ], "#2563eb", "#eff6ff")
    ic += _kart(510, 45, 230, 175, "3. Kimlik ve Öz Güven İnşası", [
        "• İman ve güzel ahlak bilinci",
        "• İlim ve ibadetle destekleme",
        "• Arş\'ın gölgesindeki genç müjdesi",
        "• Zamanın kıymetini öğretme",
        "• Topluma faydalı birey yetiştirme"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Asr-ı Saadet\'in Öncü Genç Sahabileri ve Görevleri</text>'
    ic += _kart(20, 45, 170, 185, "Mus\'ab b. Umeyr", [
        "• Medine\'nin ilk muallimi",
        "• Zenginliği iman için terk",
        "• Uhud\'da İslam sancaktarı",
        "• Diplomatik nezaket"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(203, 45, 170, 185, "Muâz b. Cebel", [
        "• 21 yaşında Yemen valisi",
        "• Helal-haramı en iyi bilen",
        "• İçtihat ve fıkıh ehli",
        "• Hem kadı hem muallim"
    ], "#059669", "#ecfdf5")
    ic += _kart(386, 45, 170, 185, "Üsâme b. Zeyd", [
        "• 18 yaşında ordu komutanı",
        "• Peygamberimizin çok sevdiği",
        "• Liyakat ve cesaret örneği",
        "• Sahabe büyüklerine komutan"
    ], "#d97706", "#fffbeb")
    ic += _kart(570, 45, 170, 185, "Hz. Ali &amp; Hz. Fatıma", [
        "• İlk genç mümin (Hz. Ali)",
        "• Hicret gecesi fedakarlığı",
        "• İlim kapısı ve kahramanlık",
        "• İffet ve sabır (Hz. Fatıma)"
    ], "#9333ea", "#faf5ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kıyamet Gününde Sorgulanacak 5 Temel Nimet (Tirmizî, Kıyâme, 1)</text>'
    kutular = [
        ("1. ÖMÜR", "Ömrünü nerede", "tükettiğinden", "#0f766e", "#f0fdfa"),
        ("2. GENÇLİK", "Gençliğini nasıl", "yıprattığından", "#1d4ed8", "#eff6ff"),
        ("3. KAZANÇ", "Malını nereden", "kazandığından", "#b45309", "#fffbeb"),
        ("4. HARCAMA", "Malını nereye", "harcadığından", "#7e22ce", "#faf5ff"),
        ("5. İLİM", "Bildikleriyle ne", "amel ettiğinden", "#be123c", "#fff1f2")
    ]
    for i, (b, s1, s2, r, bg) in enumerate(kutular):
        x = 20 + i * 146
        ic += f'<rect x="{x}" y="55" width="136" height="160" rx="10" fill="{bg}" stroke="{r}" stroke-width="2"/>'
        ic += f'<rect x="{x}" y="55" width="136" height="32" rx="10" fill="{r}"/>'
        ic += f'<text x="{x+68}" y="76" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{b}</text>'
        ic += f'<text x="{x+68}" y="120" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">{s1}</text>'
        ic += f'<text x="{x+68}" y="140" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="#1e293b" text-anchor="middle">{s2}</text>'
        ic += f'<text x="{x+68}" y="185" font-family="sans-serif" font-size="10.5" fill="{r}" text-anchor="middle">Hesap Bilinci</text>'
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Nebevi Metodla Gençlik Dönemi İmtihanları ve Çözüm Yolları</text>'
    ic += _kart(20, 45, 350, 175, "İffet, İrade ve Kimlik Korunması", [
        "• İffeti koruma (Hz. Yusuf ve Arş\'ın gölgesindeki genç)",
        "• Gözü, dili ve kalbi haramdan sakınma bilinci",
        "• İرادeyi oruç, ibadet ve salih arkadaş çevresiyle güçlendirme",
        "• Nebevi ikna metodu: Empati kurarak kalbe dokunma",
        "• Kötü alışkanlıklar ve bağımlılıklara karşı bilinçli duruş"
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "İlim, Üretim ve Sosyal Sorumluluk", [
        "• Ashab-ı Suffe modeli: İlim ve hikmetle donanma",
        "• Erdemliler Topluluğu (Hılfü\'l-Fudûl) ruhuyla adaleti savunma",
        "• Yaşlılara hürmet, küçüklere merhamet ve aileye vefa",
        "• Boş vakti (ferağ) ve sağlığı (sıhhat) salih amelle değerlendirme",
        "• Ümmetin ve insanlığın derdiyle dertlenen öncü nesil"
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