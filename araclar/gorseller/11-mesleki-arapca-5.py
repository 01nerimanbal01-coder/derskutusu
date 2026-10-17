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
        'MESLEKİ ARAPÇA: İBADET VE TAHARET (TEMİZLİK) KAVRAMLARI</text>'
    )
    ic += _kart(20, 44, 310, 190, "EL-İBADETÜ VE ET-TAHARETÜ", [
        "• el-İbâdetü (tekil) / el-İbâdâtü (çoğul): İbadet(ler).",
        "• et-Tahâretü: Maddi ve manevi temizlik.",
        "• Hadis: 'et-Tuhûru şatru'l-îmân'",
        "  (Temizlik imanın yarısıdır).",
        "• Tahâret minel-hades: Abdestsizlik ve cünüplükten",
        "  arınma (Hükmi temizlik: Abdest, Gusül, Teyemmüm).",
        "• Tahâret minen-necâse: Beden, elbise ve mekan temizliği."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "SULAR VE TEMİZLENME YOLLARI", [
        "• el-Mâu't-Tahûr: Kendisi temiz ve temizleyici su.",
        "• el-Vudûu: Abdest (Namaz için temel temizlik).",
        "• el-Guslü: Boy abdesti (Bütün bedeni yıkamak).",
        "• et-Teyemmümü: Su bulunmadığında veya suyu kullanma",
        "  imkanı olmadığında temiz toprakla yapılan temizlik.",
        "• el-Meshu ale'l-huffeyn: Mestler üzerine mesh etmek."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'FERÂİDU\'L-VUDÛ (ABDESTİN FARZLARI - MAİDE SURESİ, 6)</text>'
    )
    farzlar = [
        ("1. GASLÜ'L-VECHİ (YÜZÜ YIKAMAK)", "Alın saç bitiminden çene altına ve iki kulak yumuşağı arasına kadar yüzü bir kez yıkamak.", "#059669", "#ECFDF5"),
        ("2. GASLÜ'L-YEDEYNİ İLE'L-MİRFEKAYNİ (KOLLARI YIKAMAK)", "İki eli dirseklerle (el-mirfekayn) birlikte bir kez yıkamak.", "#2563EB", "#EFF6FF"),
        ("3. MESHU Bİ-RUB'İ'R-RE'Sİ (BAŞI MESH ETMEK)", "Başın (er-re's) en az dörtte birini ıslak elle bir kez mesh etmek (sıvazlamak).", "#7C3AED", "#F5F3FF"),
        ("4. GASLÜ'R-RİCLEYNİ İLE'L-KA'BEYNİ (AYAKLARI YIKAMAK)", "İki ayağı topuk kemikleriyle (el-ka'beyn) birlikte bir kez yıkamak.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(farzlar):
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
        'GUSLÜN VE TEYEMMÜMÜN FARZLARI (ARAPÇA FIKIH TERİMLERİ)</text>'
    )
    ic += _kart(20, 44, 310, 190, "FERÂİDU'L-GUSLİ (GUSLÜN 3 FARZI)", [
        "1. el-Madmadatu (Mazmaza):",
        "   Ağza bolca su alıp çalkalamak.",
        "2. el-İstinşâku (İstinşak):",
        "   Buruna su çekip temizlemek.",
        "3. Gaslü cemîi'l-bedeni:",
        "   İğne ucu kadar kuru yer kalmayacak şekilde",
        "   bütün bedeni yıkamak."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "FERÂİDU'T-TEYEMMÜMİ (TEYEMMÜMÜN 2 FARZI)", [
        "1. en-Niyyetü: Allah rızası ve ibadet için niyet etmek.",
        "2. ed-Darbetâni (İki Vuruş ve Mesh):",
        "   • Birinci vuruş: Elleri temiz toprağa (es-saîdü't-tayyib)",
        "     vurup yüzün tamamını mesh etmek.",
        "   • İkinci vuruş: Elleri tekrar toprağa vurup kolları",
        "     dirseklerle beraber mesh etmek.",
        "• Suyu görünce veya kullanıma güç yetince teyemmüm bozulur."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'CÜMLE KALIPLARI VE DİL BİLGİSİ: YECİBÜ ALÂ VE EN + MUZARİ (MASDAR-I MÜEVVEL)</text>'
    )
    ic += _kart(20, 44, 310, 190, "GEREKLİLİK KALIPLARI (YECİBÜ / YÜSTüHABBÜ)", [
        "• Yecibü ale'l-müslimi en + (mansub muzari fiil):",
        "  'Müslümanın ... yapması gerekir / farzdır.'",
        "• Örn: Yecibü ale'l-müslimi en yetevaddaa kable's-salâti.",
        "  (Müslümanın namazdan önce abdest alması gerekir).",
        "• Yüstehabbü / Yüsennü: Müstehaptır / Sünnettir.",
        "• Yecûzü: Caizdir / La yecûzü: Caiz değildir."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "TEMEL FİİLLER VE ORGAN İSİMLERİ", [
        "• Fiiller: Gasele - Yagsilü (Yıkamak) | Meseha - Yemsehu",
        "  (Mesh etmek) | Tevaddaa - Yetevaddau (Abdest almak)",
        "  | İğtesele (Gusletmek) | Teyemmeme (Teyemmüm etmek).",
        "• Organlar: el-Vech (Yüz), el-Yed / el-Yedeyn (El / İki el),",
        "  el-Mirfek (Dirsek), er-Re's (Baş), el-Üzün (Kulak),",
        "  er-Ricl / er-Ricleyn (Ayak / İki ayak), el-Ka'b (Topuk)."
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
