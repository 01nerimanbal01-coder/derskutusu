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
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">HZ. PEYGAMBER VE SAHABE DÖNEMİNDE TEFSİRİN KAYNAKLARI</text>'
    ic += _kart(20, 44, 310, 190, "HZ. PEYGAMBER\'İN TEBYÎN GÖREVİ", [
        "• Kur'an-ı Kerim'in ilk ve en yetkin müfessiri bizzat",
        "  Hz. Muhammed'dir (s.a.v.) (Nahl Suresi, 44).",
        "• Mücmel (kapalı/özet) ayetleri açıklamış (namaz, hac).",
        "• Umum bildiren ayetleri tahsis etmiş (Zulüm -> Şirk).",
        "• Müşkil (anlaşılması güç) lafızları beyan etmiştir",
        "  (Beyaz ve siyah iplik -> Fecrin aydınlığı ve gece)."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "SAHABE TEFSİRİNİN 4 TEMEL KAYNAĞI", [
        "1. Kur'an'ın Kur'an'la Tefsiri (En sağlam kaynak).",
        "2. Hz. Peygamber'in Sünneti ve Hadisleri.",
        "3. Sahabenin İçtihadı ve Rey (Akıl yürütme) gücü.",
        "4. Arap Dili, Cahiliye Şiiri ve Esbâb-ı Nüzûl bilgisi.",
        "• Öne çıkan 4 büyük müfessir sahabi: Abdullah b. Abbas,",
        "  Abdullah b. Mes'ud, Hz. Ali ve Übey b. Kâ'b."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SAHABE DÖNEMİNİN ÖNDE GELEN MÜFESSİRLERİ</text>'
    ic += _kart(20, 44, 310, 190, "ABDULLAH B. ABBAS VE İBN MES\'UD", [
        "• Abdullah b. Abbas (r.a.): Hz. Peygamber'in",
        "  'Allah'ım ona dinde derin anlayış ver ve tevili öğret'",
        "  duasına mazhar olmuştur. 'Tercümânü'l-Kur'an' ve",
        "  'Habrü'l-Ümme' unvanlarıyla Mekke ekolünü kurdu.",
        "• Abdullah b. Mes'ud (r.a.): İlk Müslümanlardan olup",
        "  yetmişten fazla sureyi bizzat Resulullah'ın ağzından",
        "  öğrenmiş ve Kûfe (Irak) tefsir ekolünü kurmuştur."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "ÜBEY B. KÂ\'B VE HZ. ALİ", [
        "• Übey b. Kâ'b (r.a.): Vahiy kâtiplerinin önde geleni",
        "  ve 'Seyyidü'l-Kurrâ' (Kârîlerin efendisi) unvanlı",
        "  sahabidir; Medine tefsir ekolünün kurucusudur.",
        "• Hz. Ali (r.a.): Hulefâ-yi Râşidîn içinde kendisinden",
        "  en çok tefsir rivayeti nakledilen sahabidir; ayetlerin",
        "  nerede ve ne zaman indiğini en iyi bilenlerdendir."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">TÂBİÎN DÖNEMİ ÜÇ BÜYÜK TEFSİR MEDRESESİ (EKOLÜ)</text>'
    ic += _kart(20, 44, 205, 190, "1. MEKKE EKOLÜ", [
        "• Kurucu Sahabi:",
        "  Abdullah b. Abbas (r.a.)",
        "• Tâbiîn Temsilcileri:",
        "  - Mücâhid b. Cebr",
        "  - Atâ b. Ebî Rebâh",
        "  - İkrime",
        "  - Saîd b. Cübeyr",
        "  - Tâvûs b. Keysân"
    ], "#059669", "#ECFDF5")
    ic += _kart(237, 44, 205, 190, "2. MEDİNE EKOLÜ", [
        "• Kurucu Sahabi:",
        "  Übey b. Kâ'b (r.a.)",
        "• Tâbiîn Temsilcileri:",
        "  - Ebu'l-Âliye er-Riyâhî",
        "  - Muhammed b. Kâ'b el-Kurazî",
        "  - Zeyd b. Eslem",
        "• Sünnet ve kıraat mirasını",
        "  titizlikle korumuştur."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(455, 44, 205, 190, "3. KÛFE (IRAK) EKOLÜ", [
        "• Kurucu Sahabi:",
        "  Abdullah b. Mes'ud (r.a.)",
        "• Tâbiîn Temsilcileri:",
        "  - Alkame b. Kays",
        "  - Mesrûk b. Ecda'",
        "  - Katâde b. Diâme",
        "  - Hasan-ı Basrî",
        "• Rey ve fıkhî tefsir güçlüdür."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">TEFSİR TARİHİNİN GELİŞİM AŞAMALARI (ŞİFAHÎ DÖNEMDEN TEDVİNE)</text>'
    adimlar = [
        ("1. HZ. PEYGAMBER DÖNEMİ (NÜZÛL VE TEBYÎN)", "Ayetlerin doğrudan vahyin muhatabı olan Resulullah (s.a.v.) tarafından sözlü ve uygulamalı olarak açıklanması.", "#059669", "#ECFDF5"),
        ("2. SAHABE DÖNEMİ (NÜZÛL ORTAMINA ŞAHİTLİK)", "Ayetlerin iniş sebeplerini (esbâb-ı nüzûl) ve Arap dilinin inceliklerini bilen sahabilerin Kur'an'ı açıklaması.", "#2563EB", "#EFF6FF"),
        ("3. TÂBİÎN DÖNEMİ (TEFSİR MEDRESELERİ VE GENİŞLEME)", "Mekke, Medine ve Kûfe ekollerinin kurulması; Kur'an'ın baştan sona tefsir edilmesi ve görüş ayrılıklarının başlaması.", "#7C3AED", "#F5F3FF"),
        ("4. TEDVİN DÖNEMİ (YAZILI ESERLERE GEÇİŞ — HİCRİ 2. YÜZYIL)", "Şifahî (sözlü) nakillerin hadis cüzleri içinde ve ardından müstakil tefsir kitaplarında (Mukâtil, Taberî vb.) toplanması.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
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
