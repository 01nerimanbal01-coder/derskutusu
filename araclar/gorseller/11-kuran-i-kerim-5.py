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
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">ELİF LÂM (ال) TAKISININ İKİ OKUNUŞ HÂLİ</text>'
    ic += _kart(20, 44, 310, 190, "1. İZHAR-I KAMERİYYE (AÇIK OKUMA)", [
        "• Elif-Lâm (ال) takısından sonra 14 kamerî harften",
        "  biri geldiğinde uygulanır.",
        "• Lâm (ل) harfi üzerine cezim (sükûn: ْ ) konur ve",
        "  lâm sesi gizlenmeden AÇIKÇA okunur.",
        "• Temsilî kelime: اَلْقَمَرُ (el-Kameru: Ay).",
        "• Örnekler: اَلْحَمْدُ (el-Hamdü), اَلْكِتَابُ (el-Kitâbü),",
        "  اَلْعَالَمِينَ (el-Âlemîne), اَلْغَفُورُ (el-Ğafûru)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "2. İDGAM-I ŞEMSİYYE (ŞEDDELİ OKUMA)", [
        "• Elif-Lâm (ال) takısından sonra 14 şemsî harften",
        "  biri geldiğinde uygulanır.",
        "• Lâm (ل) harfi yazılır ancak OKUNMAZ; şemsî harfe",
        "  katılarak (idgam edilerek) şemsî harf ŞEDDELİ okunur.",
        "• Temsilî kelime: اَلشَّمْسُ (eş-Şemsü: Güneş).",
        "• Örnekler: اَلرَّحْمٰنُ (er-Rahmânü), اَلنَّاسُ (en-Nâsü),",
        "  اَلصِّرَاطَ (es-Sırâta), اَلتَّوَّابُ (et-Tevvâbü)."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">14 KAMERÎ HARF VE 14 ŞEMSÎ HARF TABLOSU</text>'
    ic += _kart(20, 44, 310, 190, "14 KAMERÎ HARF (EBĞÎ HACCEKE...)", [
        "• Kodlama cümlesi:",
        "  اَبْغِ حَجَّكَ وَخَفْ عَقِيمَهُ",
        "  (Ebğî hacceke ve haf akîmeh)",
        "• Harfler: ا ب غ ح ج ك و خ ف ع ق ي م هـ",
        "  (Elif, Bâ, Ğayn, Hâ, Cîm, Kâf, Vâv, Hı,",
        "   Fâ, Ayn, Kâf, Yâ, Mîm, He).",
        "• Bu harflerde lâm CEZİMLİ (اَلْـ) okunur."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "14 ŞEMSÎ HARF (DİL UCU / DİŞ HARFLERİ)", [
        "• Harfler: ت ث د ذ ر ز س ش ص ض ط ظ ل ن",
        "  (Tâ, Sâ, Dâl, Zâl, Râ, Zây, Sîn, Şîn,",
        "   Sâd, Dâd, Tı, Zı, Lâm, Nûn).",
        "• Mahreçleri lâm (ل) harfine çok yakın olduğu",
        "  için lâm harfi bu harflerin içine idgam edilir.",
        "• Bu harflerde lâm okunmaz, harf ŞEDDELİ okunur."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">MUSHAFTA İZHAR-I KAMERİYYE VE İDGAM-I ŞEMSİYYE İPUÇLARI</text>'
    adimlar = [
        ("1. LÂM HARFİNİN ÜZERİNDE CEZİM ( ْ ) VARSA", "İzhar-ı Kameriyye vardır; lâm harfi açıkça seslendirilir: اَلْـمُلْكُ (el-Mülkü), اَلْـيَوْمَ (el-Yevme).", "#059669", "#ECFDF5"),
        ("2. LÂM HAREKESİZ VE SONRAKİ HARF ŞEDDELİ ( ّ ) İSE", "İdgam-ı Şemsiyye vardır; lâm okunmadan şemsî harfe geçilir: اَلـسَّلَامُ (es-Selâmü), اَلـدِّينِ (ed-Dîni).", "#2563EB", "#EFF6FF"),
        ("3. GEÇİŞ (VASIL) HALİNDE HEMZE-İ VASIL DÜŞER", "Önceki kelimeden Elif-Lâm'a geçilirken baştaki elif okunmaz: رَبُّ الْعَالَمِينَ (Rabbü'l-âlemîn), مِنَ الشَّيْطَانِ (mine'ş-şeytân).", "#7C3AED", "#F5F3FF"),
        ("4. NÛN (ن) VE LÂM (ل) İLE BAŞLAYAN ŞEMSÎ KELİMELER", "اَلنُّورُ (en-Nûr) kelimesinde idgam-ı şemsiyye meal-ğunne; اَللَّيْلُ (el-Leyl) kelimesinde iki lâm idgamı yapılır.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">FATİHA VE İHLAS/FELAK/NAS SURELERİNDEN UYGULAMA ÖRNEKLERİ</text>'
    ic += _kart(20, 44, 310, 190, "İZHAR-I KAMERİYYE ÖRNEKLERİ", [
        "• اَلْحَمْدُ (el-Hamdü) -> ح (Hâ) kamerî harftir.",
        "• اَلْعَالَمِينَ (el-Âlemîn) -> ع (Ayn) kamerî harftir.",
        "• اَلْمُسْتَقِيمَ (el-Müstekîm) -> م (Mîm) kamerîdir.",
        "• اَلْفَلَقِ (el-Felak) -> ف (Fâ) kamerî harftir.",
        "• اَلْوَسْوَاسِ (el-Vesvâs) -> و (Vâv) kamerî harftir.",
        "• اَلْخَنَّاسِ (el-Hannâs) -> خ (Hı) kamerî harftir."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "İDGAM-I ŞEMSİYYE ÖRNEKLERİ", [
        "• اَلرَّحْمٰنِ (er-Rahmân) -> ر (Râ) şemsî harftir.",
        "• اَلرَّحِيمِ (er-Rahîm) -> ر (Râ) şemsî harftir.",
        "• اَلدِّينِ (ed-Dîn) -> د (Dâl) şemsî harftir.",
        "• اَلصِّرَاطَ (es-Sırât) -> ص (Sâd) şemsî harftir.",
        "• اَلصَّمَدُ (es-Samed) -> ص (Sâd) şemsî harftir.",
        "• اَلنَّاسِ (en-Nâs) -> ن (Nûn) şemsî harftir."
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
