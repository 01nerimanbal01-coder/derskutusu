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
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kelam İlminde Üç Kesin Bilgi Kaynağı (Esbâb-ı İlim)</text>'
    ic += _kart(20, 45, 230, 185, "1. Havâss-ı Selîme (Sağlam Duyular)", [
        "• Kusursuz işleyen beş duyu organı",
        "• Görme, işitme, tatma, koklama, dokunma",
        "• Maddi ve fiziksel âlemi algılar",
        "• Gözlem ve deneyin temel aracıdır",
        "• Zorunlu (zarûrî) bilgi sağlar"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(265, 45, 230, 185, "2. Haber-i Sâdık (Doğru Haber)", [
        "• Yalan ihtimali taşımayan kesin haber",
        "• a) Mütevâtir Haber: Yalan üzere",
        "  birleşmesi imkânsız topluluk haberi",
        "• b) Peygamber Haberi: Mucize ile",
        "  desteklenen vahiy (Gayb bilgisi)"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 185, "3. Akl-ı Selîm (Sağlam Akıl)", [
        "• Önyargı ve taklitten arınmış akıl",
        "• Duyu verilerini ve haberi işler",
        "• Bedîhî (apaçık) ilkelerle hükmeder",
        "• Nazar ve istidlâl (akıl yürütme) yapar",
        "• Dini sorumluluğun (teklîf) şartıdır"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kelam Epistemolojisinde Bilginin Türleri: Kadîm ve Hâdis Bilgi</text>'
    ic += _kart(20, 45, 230, 175, "Kadîm Bilgi (Allah\'ın İlmi)", [
        "• Ezelî ve ebedîdir, sonradan olmaz",
        "• Vasıtasız, küllî ve mutlak bilgidir",
        "• Artma, eksilme ve unutma olmaz",
        "• Gaybı ve şehâdeti eksiksiz kuşatır",
        "• Varlığın sebebidir"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(265, 45, 230, 175, "Zarûrî (Zorunlu) Hâdis Bilgi", [
        "• İnsanda çaba olmadan oluşan bilgi",
        "• Duyu verileri (ateşin yakması vb.)",
        "• Bedîhî aklî ilkeler (Bütün > Parça)",
        "• İç gözlem (açlık, sevinç, acı)",
        "• Mütevâtir haberle oluşan bilgi"
    ], "#d97706", "#fffbeb")
    ic += _kart(510, 45, 230, 175, "Kesbî / İstidlâlî (Kazanılmış) Bilgi", [
        "• Nazar ve tefekkürle elde edilen bilgi",
        "• Öncüllerden sonuca ulaşma (İstidlâl)",
        "• Eserden müessire (Evrenden Allah\'a)",
        "• Peygamber haberi (mucize deliliyle)",
        "• Kelamcıların temel yöntemi"
    ], "#2563eb", "#eff6ff")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kelam Ontolojisinde (Varlık Anlayışında) Varlık Tasnifi</text>'
    ic += _kart(20, 45, 350, 175, "Kadîm / Vâcibü\'l-Vücûd (Zorunlu Varlık: Allah)", [
        "• Varlığı kendindendir (li-zâtihî), başkasına muhtaç değildir",
        "• Başlangıcı (ezelî) ve sonu (ebedî) yoktur; yokluğu düşünülemez",
        "• Zamandan, mekândan ve maddeden münezzehtir",
        "• Tüm mümkün/hâdis varlıkların yegâne yaratıcısıdır",
        "• Eş\'arî ve Mâtürîdîlere göre zâtı ve sıfatlarıyla kadîmdir"
    ], "#1d4ed8", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Hâdis / Mümkünü\'l-Vücûd (Sonradan Olan: Âlem)", [
        "• Allah\'ın yaratmasıyla yokluktan varlığa çıkan her şey (Mâsivâ)",
        "• Varlığı ile yokluğu eşit olup var olmak için Yaratıcıya muhtaçtır",
        "• Bir başlangıcı ve sonu vardır; değişim ve dönüşüm içindedir",
        "• Mütehayyiz (yer kaplayan: cevher/cisim) ve Araz\'dan oluşur",
        "• Hudûs delili: Âlem hâdistir, her hâdisin bir muhdisi (Allah) vardır"
    ], "#15803d", "#f0fdf4")
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Hâdis Varlığın (Âlemin) Yapı Taşları: Cevher, Cisim ve Araz</text>'
    ic += _kart(20, 45, 230, 175, "Cevher (Atom / Cüz\'ün lâ yetecezzâ)", [
        "• Maddenin bölünemeyen en küçük yapı taşı",
        "• Boşlukta yer kaplar (Mütehayyiz)",
        "• Kendi başına varlığını sürdürür",
        "• Arazları (nitelikleri) üzerinde taşır",
        "• Cevher-i ferd olarak da adlandırılır"
    ], "#9333ea", "#faf5ff")
    ic += _kart(265, 45, 230, 175, "Cisim (Birleşik Maddi Varlık)", [
        "• En az iki veya daha fazla cevherin",
        "  bir araya gelmesiyle oluşan varlık",
        "• En, boy ve derinlik (üç boyut) taşır",
        "• Duyularla algılanan maddi nesneler",
        "• Sonlu ve sınırlı yapıya sahiptir"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 175, "Araz (Nitelik ve Haller)", [
        "• Kendi başına boşlukta yer kaplayamaz",
        "• Var olmak için cevher/cisme muhtaçtır",
        "• Renk, tat, koku, hareket, sükûn, ses",
        "• Sürekli yenilenir (iki zamanda baki kalmaz)",
        "• Değişimin ve hudûsun en açık kanıtıdır"
    ], "#be123c", "#fff1f2")
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
