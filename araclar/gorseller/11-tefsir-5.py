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
        'HZ. PEYGAMBER (S.A.V.) DÖNEMİNDE TEFSİR VE BEYAN GÖREVİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "İLK MÜFESSİR: HZ. MUHAMMED (S.A.V.)", [
        "• Nahl Suresi 44. Ayet: 'İnsanlara, kendilerine",
        "  indirileni açıklayasın (li-tübeyyine) diye sana da",
        "  Zikr'i (Kur'an'ı) indirdik.'",
        "• Sahabiler ana dilleri Arapça olduğu için ayetlerin",
        "  çoğunu doğrudan anlıyor; yalnızca kapalı veya",
        "  hüküm içeren ayetleri Hz. Peygamber'e soruyorlardı.",
        "• Bu dönemde Kur'an baştan sona değil, ihtiyaç kadar tefsir edildi."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "TEFSİRü'N-NEBİ'NİN DÖRT BEYAN ŞEKLİ", [
        "1. Mücmeli Tebyin: Namaz, hac, zekat gibi özlü emirlerin",
        "   uygulanışını bizzat göstererek açıklaması.",
        "2. Müphemi Tayin: 'Orta namaz' -> İkindi namazı;",
        "   'Zulüm' -> Şirk (Lokman, 13) olarak açıklaması.",
        "3. Umumun Tahsisi: Genel hükmün istisnasını bildirmesi.",
        "4. Müşkili Tavzih: 'Ak iplik - kara iplik' ifadesini",
        "   fecrin aydınlığı ve gecenin karanlığı olarak açıklaması."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SAHABE DÖNEMİNDE TEFSİR KAYNAKLARI VE ÖNDE GELEN MÜFESSİR SAHABİLER</text>'
    )
    ic += _kart(20, 44, 310, 190, "SAHABENİN DÖRT TEFSİR KAYNAĞI", [
        "1. Kur'an'ın Kur'an ile Tefsiri (En güvenilir kaynak).",
        "2. Hz. Peygamber'in (s.a.v.) Sünneti ve açıklamaları.",
        "3. İçtihat ve Kuvvetli Arap Dili / Şiiri Bilgisi",
        "   (Esbab-ı nüzule bizzat şahit olmalarının avantajı).",
        "4. Ehl-i Kitap Kültüründen (İsrâiliyyât) Sınırlı Bilgiler",
        "   (Yalnız kıssaların teferruatında, inanca aykırı olmayacak şekilde)."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "EN ÇOK TEFSİR RİVAYET EDEN SAHABİLER", [
        "• Abdullah bin Abbas (r.a.): 'Tercümânü'l-Kur'an' ve",
        "  'Habrü'l-Ümme' (Hz. Peygamber'in özel duasına mazhar).",
        "• Abdullah bin Mes'ud (r.a.): Kûfe ekolünün kurucusu.",
        "• Übey bin Ka'b (r.a.): Medine ekolünün ve kıraatin öncüsü.",
        "• Hz. Ali (r.a.): Dört Halife içinde en çok rivayeti olan.",
        "• Hz. Aişe, Zeyd bin Sabit, Ebu Musa el-Eş'ari ve",
        "  Abdullah bin Ömer (r.a.)."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'TABİÎN DÖNEMİNDE ÜÇ BÜYÜK TEFSİR EKOLÜ (MEKKE, MEDİNE, KÛFE)</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. MEKKE EKOLÜ", [
        "• Sahabi Hocası:",
        "  ABDULLAH BİN ABBAS",
        "  (Tercümânü'l-Kur'an).",
        "• Tabiîn Temsilcileri:",
        "  - Mücahid bin Cebr",
        "  - Said bin Cübeyr",
        "  - İkrime",
        "  - Ata bin Ebi Rabah",
        "  - Tavus bin Keysan."
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "2. MEDİNE EKOLÜ", [
        "• Sahabi Hocası:",
        "  ÜBEY BİN KA'B",
        "  (Seyyidü'l-Kurrâ).",
        "• Tabiîn Temsilcileri:",
        "  - Ebu'l-Aliye er-Riyahi",
        "  - Muhammed bin Ka'b",
        "    el-Kurazi",
        "  - Zeyd bin Eslem",
        "• Rivayet ve kıraat ağırlıklıdır."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. KÛFE (IRAK) EKOLÜ", [
        "• Sahabi Hocası:",
        "  ABDULLAH BİN MES'UD.",
        "• Tabiîn Temsilcileri:",
        "  - Alkame bin Kays",
        "  - Mesruk",
        "  - Esved bin Yezid",
        "  - İbrahim en-ehaî",
        "  - Katâde ve Hasan-ı Basrî.",
        "• Re'y ve fıkhi içtihat güçlüdür."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'TEDVİN DÖNEMİNE GEÇİŞ VE İLK TAM KUR\'AN TEFSİRLERİ</text>'
    )
    adimlar = [
        ("1. ŞİFAHİ (SÖZLÜ) DÖNEMDEN YAZIYA GEÇİŞ", "Hz. Peygamber ve Sahabe döneminde şifahi olan tefsir, Tabiîn ve Etbau't-Tabiîn döneminde hadis babları içinde yazılmaya başlandı.", "#0891B2", "#ECFEFF"),
        ("2. İLK TAM MUSHAF TEFSİRİ: MUKATİL BİN SÜLEYMAN (Ö. 150/767)", "'et-Tefsîru'l-Kebîr' adlı eseriyle Kur'an'ı Fatiha'dan Nas Suresine kadar baştan sona tefsir eden İLK müfessirdir.", "#059669", "#ECFDF5"),
        ("3. DİL BİLİMSEL TEFSİR: FERRA VE EBU UBEYDE", "Ferra'nın 'Meâni'l-Kur'an' ve Ebu Ubeyde'nin 'Mecâzü'l-Kur'an' eserleri filolojik (dil bilimsel) tefsirin ilk örnekleridir.", "#D97706", "#FEF3C7"),
        ("4. RİVAYET TEFSİRİNİN ZİRVESİ: TABERÎ (Ö. 310/923)", "İbn Cerîr et-Taberî'nin 'Câmiu'l-Beyân' (Taberî Tefsiri) adlı eseri klasik rivayet tefsirlerinin en büyük şaheseridir.", "#2563EB", "#EFF6FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
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
