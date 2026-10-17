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
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Günlük Hayatta Mümin Kimliğini Gözlemleme (Müşahede Alanları)</text>'
    ic += _kart(20, 45, 230, 185, "1. Söz ve Dilde Mümin Kimliği", [
        "• Besmele (Bismillah) ile başlama",
        "• Hamdele (Elhamdülillah) ile şükür",
        "• Selamlaşma (Esselâmü aleyküm)",
        "• Doğru sözlülük (Sıdk)",
        "• Kırıcı ve yalan sözden kaçınma"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "2. Davranışta Mümin Kimliği", [
        "• Emaneti koruma ve güvenilir olma",
        "• Söz verdiğinde sözünde durma",
        "• Adaletli ve merhametli davranma",
        "• Anne-babaya ve büyüklere saygı",
        "• İhtiyaç sahiplerine yardımseverlik"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "3. İbadet ve Çevrede Kimlik", [
        "• Namaz, oruç ve dua bilinci",
        "• Beden, elbise ve çevre temizliği",
        "• Suyu ve ekmeği israf etmeme",
        "• Hayvanlara ve doğaya şefkat",
        "• Kul hakkına titizlikle uyma"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Müminin İki Temel Alameti: Sıdk (Doğruluk) ve Emanet (Güvenilirlik)</text>'
    ic += _kart(20, 45, 350, 175, "Mümin Kimdir? (Emîn ve GüvenVeren İnsan)", [
        "• \'Mümin\' kelimesi \'emân\' (güven) kökünden gelir",
        "• Allah\'a güvenip inanan ve çevresine güven veren kişidir",
        "• Hadis-i Şerif: \'Müslüman, elinden ve dilinden diğer",
        "  insanların güvende olduğu (zarar görmediği) kimsedir.\'",
        "• \'Mümin ise insanların canları ve malları konusunda",
        "  kendisine güvendikleri kimsedir.\'"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 175, "Müminin Kaçındığı 3 Olumsuz Davranış", [
        "• 1. Konuştuğunda yalan söylemekten sakınır (Daima dürüsttür)",
        "• 2. Söz verdiğinde sözünden dönmez (Vefalıdır)",
        "• 3. Kendisine bir şey emanet edildiğinde hıyanet etmez",
        "• Peygamberimiz: \'Bizi aldatan bizden değildir!\' buyurmuştur",
        "• Mümin özü ile sözü bir olan (ihlaslı) insandır"
    ], "#be123c", "#fff1f2")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Mümin Kimliğinin Günlük Dili: Dini İfadelerimiz</text>'
    kutular = [
        ("Besmele", "Hayırlı işe", "başlarken", "Bismillah", "#059669", "#ecfdf5"),
        ("Hamdele", "Nimetlere", "şükrederken", "Elhamdülillah", "#0284c7", "#f0f9ff"),
        ("Selam", "Karşılaşınca", "esenlik duası", "Selâmün aleyküm", "#d97706", "#fffbeb"),
        ("İnşallah", "Gelecekteki", "bir iş için", "Allah dilerse", "#7c3aed", "#f5f3ff"),
        ("İstiğfar", "Hata yapınca", "af dilerken", "Estağfirullah", "#be123c", "#fff1f2")
    ]
    for i, (b, s1, s2, s3, r, bg) in enumerate(kutular):
        x = 20 + i * 146
        ic += f'<rect x="{x}" y="50" width="136" height="165" rx="10" fill="{bg}" stroke="{r}" stroke-width="2"/>'
        ic += f'<rect x="{x}" y="50" width="136" height="30" rx="10" fill="{r}"/>'
        ic += f'<text x="{x+68}" y="70" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{b}</text>'
        ic += f'<text x="{x+68}" y="110" font-family="sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s1}</text>'
        ic += f'<text x="{x+68}" y="130" font-family="sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s2}</text>'
        ic += f'<text x="{x+68}" y="175" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="{r}" text-anchor="middle">{s3}</text>'
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Müminlerin Kardeşliği ve Toplumsal Değerler</text>'
    ic += _kart(20, 45, 350, 175, "Müminler Ancak Kardeştir (Hucurât, 10)", [
        "• Müminler birbirini Allah için sever ve korur",
        "• Birbirinin kusurunu araştırmaz, gıybet etmez",
        "• Birbirine lakap takmaz ve alay etmez",
        "• Küs durmaz, aralarını düzeltir (ıslah eder)",
        "• Tarak dişleri gibi birbirine destek olur"
    ], "#1d4ed8", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Mümin Kimliğini Besleyen 4 Temel Değer", [
        "• 1. Adalet: Herkese hakkını vermek, haksızlık yapmamak",
        "• 2. Saygı: Anne-babaya, öğretmene ve tüm insanlara hürmet",
        "• 3. Sorumluluk: Kulluk, öğrencilik ve çevre görevlerini yapmak",
        "• 4. Yardımseverlik: Komşusu açken tok yatmamak, paylaşmak",
        "• Mümin, bal arısı gibi güzel şeyler alır ve güzellik üretir"
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
