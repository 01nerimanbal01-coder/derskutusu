def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'İMAN BAKIMINDAN İNSANLAR (MÜMİN, KÂFİR, MÜŞRİK, MÜNAFIK)</text>'
    )
    ic += _kart(20, 44, 310, 200, "1. MÜMİN VE 2. MÜŞRİK", [
        "• MÜMİN (İman Eden):",
        "  Allah'tan gelen vahyi ve zarûrât-ı dîniyyeyi kalbiyle",
        "  tasdik edip diliyle ikrar eden kimsedir.",
        "• MÜŞRİK (Allah'a Ortak Koşan):",
        "  Allah'ın varlığını kabul etmekle birlikte zatında,",
        "  sıfatlarında veya ibadette O'na ortak koşan kimsedir.",
        "  Şirk, tövbe edilmezse affedilmeyen en büyük zulümdür",
        "  (Nisâ, 48; Lokmân, 13)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 200, "3. KÂFİR VE 4. MÜNAFIK", [
        "• KÂFİR (İnkâr Eden / Hakikati Örten):",
        "  İslam'ın inanç esaslarından birini veya tamamını",
        "  kalbiyle tasdik etmeyen, bilerek reddeden kimsedir.",
        "• MÜNAFIK (İkiyüzlü / Nifak Ehli):",
        "  Kalbiyle inanmadığı halde sırf dünyevi çıkar için",
        "  diliyle 'inandım' diyerek Müslüman görünen kimsedir.",
        "  İtikadî nifak (inançta) cehennemin en alt tabakasındadır;",
        "  Amelî nifak (yalan, emanete hıyanet) ise büyük günahtır."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KÜFÜR (İNKÂR) ÇEŞİTLERİ: AKAİD İLMİNDE DÖRT KÜFÜR TÜRÜ</text>'
    )
    adimlar = [
        ("1. KÜFR-İ İNKÂRÎ", "Allah'ı, peygamberi ve iman esaslarını hem kalbiyle bilmemek/reddetmek hem de diliyle açıkça inkâr etmektir.", "#DC2626", "#FEF2F2"),
        ("2. KÜFR-İ CÜHÛDÎ", "Hakikati kalbiyle bilip tanıdığı halde kibir, haset veya makam korkusuyla bile bile inkâr etmektir (İblis ve Firavun gibi).", "#D97706", "#FEF3C7"),
        ("3. KÜFR-İ İNÂDÎ", "İslam'ın hak din olduğunu bildiği ve itiraf ettiği halde kavmiyetçilik veya kınanma korkusuyla iman etmemektir (Ebu Talib gibi).", "#7C3AED", "#F5F3FF"),
        ("4. KÜFR-İ NİFÂKÎ", "Kalbiyle hiç inanmadığı halde Müslümanları aldatmak için diliyle inandığını söylemektir (Münafıkların küfrü).", "#2563EB", "#EFF6FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'İMAN - AMEL İLİŞKİSİ VE BÜYÜK GÜNAH (KEBÂİR) İŞLEYENİN DURUMU</text>'
    )
    ic += _kart(20, 44, 310, 190, "EHL-İ SÜNNET'İN İMAN-AMEL GÖRÜŞÜ", [
        "• Amel (ibadet ve ahlak), imanın özünden bir CÜZ",
        "  (parça) değildir; fakat imanı koruyan ve olgunlaştıran",
        "  en önemli tamamlayıcıdır.",
        "• İbadetleri terk eden veya büyük günah (kebâir)",
        "  işleyen mümin; günahı helal saymadıkça (istihlal",
        "  yapmadıkça) DİNDEN ÇIKMAZ ve kâfir olmaz!",
        "• Bu kişiye 'Fâsık (Günahkâr) Mümin' adı verilir."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "TEKFİRCİLİĞİN TEHLİKESİ VE EHL-İ KIBLE", [
        "• Hariciler: Büyük günah işleyeni kâfir saydılar.",
        "• Mu'tezile: Ne mümin ne kâfir ('el-Menzile beyne'l-",
        "  menzileteyn' - iki yer arasında bir yer) dediler.",
        "• Ehl-i Sünnet (Maturidi ve Eş'ari): 'Ehl-i kıble",
        "  (Kâbe'ye yönelip namaz kılan ve kelime-i şehadet",
        "  getiren kimse) büyük günah işlese de tekfir edilemez!'",
        "• Günahkâr müminin ahiret durumu Allah'ın iradesindedir."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'İMANI KORUMA BİLİNCİ: İRTİDAD, ELFÂZ-I KÜFÜR VE TECEDDÜD-İ İMAN</text>'
    )
    ic += _kart(20, 44, 310, 190, "İRTİDAD VE ELFÂZ-I KÜFÜR", [
        "• İrtidad (Ridde): Bir Müslümanın kendi iradesiyle",
        "  İslam dininden çıkmasıdır; bu kişiye 'Mürted' denir.",
        "• Elfâz-ı Küfür: Dinin kesin hükümlerini (zarûrât-ı",
        "  dîniyyeyi) alaya alan, küçümseyen veya haramı helal",
        "  sayan ve söyleyeni imandan çıkaran sözlerdir.",
        "• İmanı korumak için dini değerlerle şaka dahi",
        "  yapmaktan titizlikle kaçınmak gerekir."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "HAVF VE RECA DENGESİ", [
        "• Mümin, Allah'ın azabından korku (Havf) ile",
        "  rahmetinden ümit (Reca) arasında dengede yaşar",
        "  ('Beyne'l-havfi ve'r-recâ').",
        "• Allah'ın rahmetinden ümit kesmek (Ye's) de,",
        "  azabından tamamen emin olmak (Emn) da yanlıştır.",
        "• Salih amel, ihlas, sahih ilim ve tövbe-istiğfar",
        "  iman nurunu koruyan en güçlü kalkandır."
    ], "#0D9488", "#F0FDFA")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
