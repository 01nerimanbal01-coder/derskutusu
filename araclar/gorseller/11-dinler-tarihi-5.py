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


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">DİNLERİ ÖĞRENMENİN İSLAM AÇISINDAN ÖNEMİ VE GEREKÇELERİ</text>'
    ic += _kart(20, 44, 310, 190, "KUR\'AN\'I ANLAMA VE İLMÎ KEŞİF", [
        "• Kur'an-ı Kerim; Yahudiler, Hristiyanlar, Sâbiîler,",
        "  Mecûsîler ve müşriklerin inançlarından bahseder.",
        "• Bu ayetlerin doğru anlaşılması diğer dinlerin",
        "  tarihini ve kavramlarını bilmeyi gerektirir.",
        "• Müslüman âlimler (Bîrûnî, Şehristânî, İbn Hazm)",
        "  diğer dinleri tarafsız ve ilmî metotla incelemiştir."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "TEBLİĞ VE BİR ARADA YAŞAMA KÜLTÜRÜ", [
        "• İslam'ı farklı inanç mensuplarına hikmetle anlatmak",
        "  (tebliğ) için muhatabın inancını tanımak şarttır.",
        "• Küreselleşen dünyada toplumsal barışı ve bir arada",
        "  yaşama kültürünü güçlendirir.",
        "• Önyargıları kırar, İslam'ın tevhit ve evrensel",
        "  ahlak ilkelerinin üstünlüğünü ortaya koyar."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">KUR\'AN-I KERİM\'DE GEÇEN DİNÎ GRUPLAR (HAC SURESİ, 17)</text>'
    adimlar = [
        ("1. EHL-İ KİTAP (YAHUDİLER VE HRİSTİYANLAR)", "Aslında ilahi vahye (Tevrat ve İncil'e) dayanan, ancak zamanla tahrife uğramış dinlerin mensuplarıdır.", "#2563EB", "#EFF6FF"),
        ("2. SÂBİÎLER", "Kur'an'da Bakara 62, Mâide 69 ve Hac 17. ayetlerde anılan, yıldız/gezeğen kültü veya Yahya (a.s.) ile ilişkilendirilen topluluktur.", "#7C3AED", "#F5F3FF"),
        ("3. MECÛSÎLER (ZERDÜŞTLÜK)", "Hac Suresi 17. ayette zikredilen, eski İran'da iyilik (Hürmüz) ve kötülük (Ehrimen) düalizmine ve ateş kültüne dayanan inançtır.", "#D97706", "#FEF3C7"),
        ("4. MÜŞRİKLER (PUTPERESTLER)", "Allah'ın varlığını kabul etmekle birlikte O'na ibadette ve ilahlıkta ortak koşan (putları aracı kılan) topluluklardır.", "#DC2626", "#FEF2F2")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">İSLAM\'IN DİN ÖZGÜRLÜĞÜ VE EHL-İ KİTAP İLE İLİŞKİ İLKELERİ</text>'
    ic += _kart(20, 44, 310, 190, "DİN VE İNANÇ ÖZGÜRLÜĞÜ İLKESİ", [
        "• 'Dinde zorlama yoktur.' (Bakara, 256) ilkesi",
        "  inanç özgürlüğünün temel dayanağıdır.",
        "• 'Sizin dininiz size, benim dinim banadır.' (Kâfirûn, 6).",
        "• En'âm 108. ayette başkalarının kutsal saydığı",
        "  değerlere hakaret edilmemesi emredilmiştir.",
        "• İman kalbin özgür tasdikiyle geçerlidir."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "EHL-İ KİTAP İLE BEŞERÎ VE HUKUKİ İLİŞKİLER", [
        "• Âl-i İmrân 64. ayette Ehl-i Kitap ortak bir söze",
        "  (yalnız Allah'a kulluk etmeye) davet edilir.",
        "• Mâide 5. ayete göre Ehl-i Kitap mensuplarının kestiği helal",
        "  hayvanların eti yenir, iffetli kadınlarıyla evlenilebilir.",
        "• Komşuluk, ticaret, hasta ziyareti ve taziye gibi",
        "  insani ilişkilerde adalet ve iyilik (birr) esastır."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">MEDİNE VESİKASI VE İSLAM MEDENİYETİNDE ZİMMET HUKUKU</text>'
    ic += _kart(20, 44, 310, 190, "MEDİNE VESİKASI VE NECRÂN HEYETİ", [
        "• Hz. Peygamber Hicret'ten sonra Medine'deki",
        "  Müslümanlar, Yahudiler ve diğer kabilelerle",
        "  'Medine Vesikası'nı imzalamıştır.",
        "• Her topluluğun din ve vicdan hürriyeti güvenceye",
        "  alınmış, şehrin ortak savunması kararlaştırılmıştır.",
        "• Necran Hristiyan heyeti Mescid-i Nebevî'de",
        "  ağırlanmış ve kendilerine ahitname verilmiştir."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "ZİMMÎ HUKUKU VE TARİHÎ UYGULAMALAR", [
        "• İslam devletinin güvencesi altında yaşayan",
        "  gayrimüslim vatandaşlara 'ehl-i zimmet' denir.",
        "• Can, mal, namus, mabet ve ibadet özgürlükleri",
        "  devlet garantisi altına alınmıştır.",
        "• Hz. Ömer'in Kudüs Emanname'si ve Fatih Sultan",
        "  Mehmed'in Bosna/İstanbul ahitnameleri bu",
        "  hoşgörü ve hukuk geleneğinin zirve örnekleridir."
    ], "#059669", "#ECFDF5")
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
