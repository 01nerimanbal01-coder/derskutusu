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
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">AKIL, İRADE VE SORUMLULUK EKSENİNDE İNSAN</text>'
    ic += _kart(20, 44, 310, 190, "AKIL: DÜŞÜNME VE AYIRT ETME GÜCÜ", [
        "• İnsanı diğer canlılardan ayıran temel özelliktir.",
        "• İyi ile kötüyü, doğru ile yanlışı ayırt etmeyi sağlar.",
        "• Dini yükümlülüğün (mükellefiyetin) ilk şartıdır.",
        "• Kur'an'da 'düşünmez misiniz, akletmez misiniz?'",
        "  buyrularak aklın işletilmesi emredilir.",
        "• Akıl sağlığı yerinde olmayanlar sorumlu tutulmaz."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "İRADE: DİLEME VE SEÇME ÖZGÜRLÜĞÜ", [
        "• İki seçenekten birini tercih etme gücüdür.",
        "• İnsan, eylemlerini baskı altında kalmadan kendi",
        "  özgür iradesiyle seçer ve gerçekleştirir.",
        "• 'Şüphesiz biz ona doğru yolu gösterdik; ister",
        "  şükredici olsun ister nankör.' (İnsan, 3).",
        "• Özgür irade olmadan ahlaki sorumluluk doğmaz."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">KÜLLÎ İRADE VE CÜZ\'Î İRADE KARŞILAŞTIRMASI</text>'
    ic += _kart(20, 44, 310, 190, "KÜLLÎ İRADE (MUTLAK İLAHİ İRADE)", [
        "• Yüce Allah'ın sınırsız ve mutlak dileme gücüdür.",
        "• Evrendeki tüm fiziksel, biyolojik ve toplumsal",
        "  yasalar küllî iradenin tecellisidir.",
        "• İnsanın anne-babası, doğduğu yer, fiziksel",
        "  yapısı ve eceli küllî irade kapsamındadır.",
        "• Bu alanda insanın seçimi olmadığı için kul",
        "  bu durumlardan hesaba çekilmez."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "CÜZ'Î İRADE (İNSANIN SINIRLI İRADESİ)", [
        "• Allah'ın insana bahşettiği sınırlı seçme gücüdür.",
        "• İman-inkâr, iyilik-kötülük, ibadet, ahlak ve",
        "  meslek seçimi cüz'î irade alanına girer.",
        "• Kul cüz'î iradesiyle yönelir ve seçer; Yüce",
        "  Allah da küllî iradesi ve kudretiyle yaratır.",
        "• İnsanın dünyada ve ahirette sorumlu olduğu",
        "  ve hesaba çekileceği alan cüz'î iradedir."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">İNSANIN SORUMLULUK BOYUTLARI VE MÜKELLEFİYET</text>'
    adimlar = [
        ("1. DİNÎ SORUMLULUK (ALLAH'A KARŞI)", "İman esaslarını kabul etmek, ibadetleri yerine getirmek, helal-haram sınırlarını gözetmektir.", "#059669", "#ECFDF5"),
        ("2. AHLAKİ VE VİCDANİ SORUMLULUK", "Doğruluk, adalet, emanete riayet, merhamet ve kendi nefsini kötülüklerden arındırma görevidir.", "#2563EB", "#EFF6FF"),
        ("3. TOPLUMSAL VE HUKUKİ SORUMLULUK", "Kul hakkına girmemek, kamu düzenini korumak, ailesine ve topluma karşı ödevlerini yapmaktır.", "#7C3AED", "#F5F3FF"),
        ("4. ÇEVREYE VE EVRENE KARŞI SORUMLULUK", "Yeryüzünü imar etmek (halife bilinci), doğal dengeyi korumak ve israftan kaçınmaktır.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">KADER-İRADE DENGESİ: AŞIRI UÇLAR VE EHL-İ SÜNNET ÇİZGİSİ</text>'
    ic += _kart(20, 44, 205, 190, "CEBRİYYE (YAZGICILIK)", [
        "• İnsanın hiçbir iradesi",
        "  ve seçme gücü yoktur.",
        "• İnsan rüzgârın önündeki",
        "  yaprak gibidir; her şeyi",
        "  zorunlu olarak yapar.",
        "• 'Kaderim böyleymiş'",
        "  diyerek sorumluluğu reddeder."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(237, 44, 205, 190, "EHL-İ SÜNNET (DENGE)", [
        "• İnsan akıl ve cüz'î",
        "  irade sahibidir; kendi",
        "  fiillerini özgürce seçer.",
        "• Kul diler ve yönelir (kesb),",
        "  Allah ise yaratır (halk).",
        "• Kader, insanın sorumluluğunu",
        "  ortadan kaldırmaz."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "MU'TEZİLE / KADERİYYE", [
        "• İlahi kaderi devre dışı",
        "  bırakan aşırı yaklaşımdır.",
        "• İnsanın kendi fiillerinin",
        "  hem seçicisi hem de",
        "  bağımsız yaratıcısı",
        "  olduğunu ileri sürer.",
        "• Küllî iradeyi sınırlar."
    ], "#2563EB", "#EFF6FF")
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
