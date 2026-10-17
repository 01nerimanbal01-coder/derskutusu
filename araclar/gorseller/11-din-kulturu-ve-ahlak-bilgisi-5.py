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
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DÜNYA HAYATININ AMACI VE AHİRET İNANCININ TEMELLERİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "DÜNYA HAYATI: İMTİHAN VE EKİN YERİ", [
        "• İnsan başıboş ve gayesiz yaratılmamıştır (Kıyamet, 36).",
        "• Ölüm ve hayat, kimin daha güzel amel (salih amel)",
        "  işleyeceğini sınamak için yaratılmıştır (Mülk, 2).",
        "• Dünya ahiretin tarlasıdır; burada ekilen iyilik ve",
        "  adalet ahirette ebedi mükafat olarak biçilir.",
        "• Ömür ve gençlik, kulun ahirette hesaba çekileceği",
        "  en kıymetli ilahi emanetlerdir."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "AHİRET İNANCININ İNSANA KAZANDIRDIKLARI", [
        "• Hayatın anlam ve gaye kazanmasını sağlar.",
        "• Yok olma korkusunu giderir, ebediyet ümidi verir.",
        "• Kötülüklerin karşılıksız, iyiliklerin mükafatsız",
        "  kalmayacağı bilinciyle mutlak adalet duygusunu korur.",
        "• İnsanda sorumluluk, merhamet ve öz denetim geliştirir.",
        "• Musibet, hastalık ve kayıplar karşısında sabır ve",
        "  metanet gücü kazandırır."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ÖLÜMDEN EBEDÎ HAYATA: AHİRET HAYATININ AŞAMALARI (MENZİLLERİ)</text>'
    )
    adimlar = [
        ("1. ÖLÜM (ECEL) VE BERZAH ÂLEMİ", "Ruhun bedenden ayrılmasıyla dünya hayatı biter; kıyamete kadar sürecek olan kabir (berzah) hayatı başlar.", "#0891B2", "#ECFEFF"),
        ("2. KIYAMET (SUR'A İLK ÜFÜRÜLÜŞ)", "İsrafil (a.s.)'ın Sur'a ilk üfürmesiyle (Nefha-i Ula) dünya düzeninin bozulup evrendeki tüm canlıların son bulmasıdır.", "#DC2626", "#FEF2F2"),
        ("3. BA'S VE HAŞİR (MAHŞER MEYDANI)", "Sur'a ikinci üfürülüşle (Nefha-i Saniye) yeniden diriliş (Ba's) ve hesap için Mahşer meydanında toplanma (Haşir).", "#7C3AED", "#F5F3FF"),
        ("4. HESAP, MİZAN, SIRAT -> CENNET / CEHENNEM", "Amel defterlerinin verilmesi, Mizan'da tartı ve Sırat köprüsünden geçişin ardından ebedi Cennet veya Cehennem yurdu.", "#059669", "#ECFDF5")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 50
        ic += (
            f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'CENAZE UYGULAMALARI VE VEFAT EDEN MÜSLÜMANIN HAKLARI</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. TECHİZ VE TEKFİN", [
        "• Techiz: Cenazenin yıkama",
        "  kulundan kabre konuluncaya",
        "  kadar tüm hazırlıkları.",
        "• Gassal tarafından usulüne",
        "  uygun yıkanıp abdest",
        "  aldırılması (Gasl).",
        "• Tekfin: Beyaz ve sade bezle",
        "  kefenlenmesi (Erkek 3, kadın 5)."
    ], "#0D9488", "#F0FDFA")
    ic += _kart(237, 44, 205, 190, "2. CENAZE NAMAZI", [
        "• Hükmü: Farz-ı Kifaye",
        "  (Bir kısım Müslüman kılınca",
        "  diğerlerinden sorumluluk düşer).",
        "• Özelliği: Rükû ve secdesi",
        "  YOKTUR; ayakta 4 tekbirle",
        "  kılınır, vefat edene DUA'dır.",
        "• Helallik alınır ve omuzlarda",
        "  kabristana taşınır (Teşyi)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. DEFİN VE TAZİYE", [
        "• Defin: Cenazenin kıbleye",
        "  dönük olarak sağ yanı",
        "  üzerine kabre konulması.",
        "• Varsa borçlarının ve",
        "  vasiyetinin segera ödenmesi.",
        "• Taziye: Yakınlarına sabır",
        "  dilemek ve yemek götürmek.",
        "• Hayır, sadaka ve dua etmek."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'KUR\'AN\'DAN MESAJLAR: BAKARA SURESİ 153-157. AYETLER (SABIR VE İSTİRCA)</text>'
    )
    ic += _kart(20, 44, 310, 190, "İMTİHAN UNSURLARI VE SABIR", [
        "• 'Ey iman edenler! Sabır ve namazla Allah'tan",
        "  yardım isteyin. Şüphesiz Allah sabredenlerle beraberdir.'",
        "• Dünya hayatında insan; biraz korku, açlık, mallardan,",
        "  canlardan ve ürünlerden eksiltmeyle sınanır.",
        "• Sabır; musibet karşısında isyan etmemek, metanetini",
        "  koruyarak Allah'a sığınmak ve üzerine düşeni yapmaktır."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "İSTİRCA İLKESİ (BAKARA, 156)", [
        "• Sabreden müminler bir musibetle veya ölüm haberiyle",
        "  karşılaştıklarında şöyle derler:",
        "  'İnnâ lillâhi ve innâ ileyhi râciûn'",
        "• Anlamı: 'Şüphesiz biz Allah'a aidiz ve sonunda yine",
        "  O'na döneceğiz.'",
        "• Bu bilince 'İstirca' denir; mülkün ve canın gerçek",
        "  sahibinin Allah olduğunu kabul ederek huzur bulmaktır."
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
