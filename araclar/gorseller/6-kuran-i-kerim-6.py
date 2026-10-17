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
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Salâtü Selam (Salavat) Nedir ve Salli-Barik Duaları Nerede Okunur?</text>'
    ic += _kart(20, 45, 230, 175, "Salavat (Salâtü Selam) Kavramı", [
        "• Hz. Peygamber\'e (s.a.v.) ve ailesine",
        "  Allah\'tan rahmet ve bereket duası",
        "• Ahzâb Suresi 56. ayetin emri",
        "• Peygamberimize sevgi ve bağlılık",
        "• En kapsamlısı: Salli ve Barik duaları"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 175, "Namazda Okunduğu Yerler", [
        "• Bütün namazların SON OTURUŞUNDA",
        "  (Ka\'de-i Ahîre\'de) Ettehiyyâtü\'den",
        "  hemen sonra okunur",
        "• İkindi (sünnet) ve Yatsı (ilk sünnet)",
        "  namazlarının İLK OTURUŞUNDA okunur"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 175, "Diğer İbadetlerde Okunuşu", [
        "• Cenaze namazında 2. tekbirden",
        "  sonra ayakta okunur",
        "• Peygamberimizin adı anıldığında",
        "• Duaların başında ve sonunda",
        "• Cuma günü ve kandil gecelerinde"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Allâhümme Salli Duasının Okunuşu ve Anlamı</text>'
    ic += _kart(20, 45, 350, 185, "Allâhümme Salli Okunuşu", [
        "• Allâhümme salli \'alâ Muhammedin",
        "  ve \'alâ âli Muhammed,",
        "• kemâ salleyte \'alâ İbrâhîme",
        "  ve \'alâ âli İbrâhîm,",
        "• inneke Hamîdün Mecîd.",
        "• Anahtar kelime: Salli / Salleyte (Rahmet et)"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 185, "Allâhümme Salli Anlamı", [
        "• \'Allah\'ım! Hz. İbrahim\'e ve Hz. İbrahim\'in",
        "  ailesine (âline / ümmetine) rahmet ettiğin gibi,",
        "• Hz. Muhammed\'e ve Hz. Muhammed\'in ailesine",
        "  (âline / ümmetine) de rahmet eyle (şerefini yücelt).",
        "• Şüphesiz Sen Hamîd\'sin (övülmeye en layık olansın),",
        "  Mecîd\'sin (şan ve şerefi çok yüce olansın).\'"
    ], "#1d4ed8", "#eff6ff")
    return _svg(760, 250, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Allâhümme Bârik Duasının Okunuşu ve Anlamı</text>'
    ic += _kart(20, 45, 350, 185, "Allâhümme Bârik Okunuşu", [
        "• Allâhümme bârik \'alâ Muhammedin",
        "  ve \'alâ âli Muhammed,",
        "• kemâ bârekte \'alâ İbrâhîme",
        "  ve \'alâ âli İbrâhîm,",
        "• inneke Hamîdün Mecîd.",
        "• Anahtar kelime: Bârik / Bârekte (Mübarek kıl)"
    ], "#d97706", "#fffbeb")
    ic += _kart(390, 45, 350, 185, "Allâhümme Bârik Anlamı", [
        "• \'Allah\'ım! Hz. İbrahim\'i ve Hz. İbrahim\'in",
        "  ailesini (âlini) mübarek kıldığın (bereketlendirdiğin) gibi,",
        "• Hz. Muhammed\'i ve Hz. Muhammed\'in ailesini",
        "  (âlini / ümmetini) de mübarek kıl (bereketlendir).",
        "• Şüphesiz Sen Hamîd\'sin (övülmeye en layık olansın),",
        "  Mecîd\'sin (şan ve şerefi çok yüce olansın).\'"
    ], "#9333ea", "#faf5ff")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Salli ve Barik Dualarında Geçen Önemli Kavramlar ve İsimler</text>'
    ic += _kart(20, 45, 350, 175, "Dualarda Anılan İki Ulu\'l-Azm Peygamber", [
        "• 1. Hz. Muhammed (s.a.v.): Son peygamberimiz",
        "• 2. Hz. İbrahim (a.s.): Kâbe\'yi inşa eden, tevhid mücadelesinin",
        "  öncüsü ve Peygamberimizin büyük atası (Halîlullah)",
        "• Âl (آل): Peygamberin ailesi, ev halkı (Ehl-i Beyt) ve",
        "  onun yolundan giden samimi müminler (ümmeti)"
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Duaların Sonundaki İki Esma-i Hüsna", [
        "• el-Hamîd (الْحَمِيدُ): Her türlü hamde, övgüye ve şükre",
        "  en layık olan, bütün varlıkların övdüğü Yüce Allah",
        "• el-Mecîd (الْمَجِيدُ): Şanı, şerefi, keremi ve cömertliği",
        "  sonsuz derecede yüce ve ulu olan Allah",
        "• Salli\'de \'rahmet\', Barik\'te \'bereket\' dilenir"
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
