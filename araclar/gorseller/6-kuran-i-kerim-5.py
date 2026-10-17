# -*- coding: utf-8 -*-
"""6. Sınıf Kur'an-ı Kerim — 5. Hafta Görselleri (Bakara Suresi 95-105. Ayetler, Tecvit ve Mesajlar)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara Suresi 95-105. Ayetlerin Ana Konuları</text>',
        _kart(25, 50, 225, 215, "95-96. Ayetler: Ahiret Bilinci", [
            "• İnsanın kendi elleriyle işlediği",
            "  günahlardan dolayı hesaptan korkması",
            "• Yalnızca dünya hayatına bağlanıp",
            "  ahireti unutmanın yanılgısı",
            "• Allah'ın yapılan her şeyi",
            "  hakkıyla görmesi (el-Basîr)"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "97-101. Ayetler: Meleklere İman", [
            "• Cebrâil (Cibrîl) ve Mikâil'in",
            "  Allah'ın şerefli melekleri oluşu",
            "• Cebrâil'in Kur'an'ı müminlere",
            "  hidayet ve müjde olarak indirmesi",
            "• Melekler ve peygamberler arasında",
            "  ayrım yapmadan hepsine iman"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "102-105. Ayetler: Hz. Peygamber'e Saygı", [
            "• Batıl inançlardan ve sihirden uzak",
            "  durup yalnızca Allah'a sığınma",
            "• İman ve takvanın kazandırdığı sevap",
            "• Müminlerin Hz. Peygamber'e hitap",
            "  ederken 'Ünzurnâ' (Bize bak/gözet)",
            "  diyerek edepli ve saygılı olması"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara 95-105. Ayetlerde Sakin Mîm ve Kalkale Uygulamaları</text>',
        _kart(30, 50, 335, 215, "Sakin Mîm (Cezimli Mîm) Kuralları", [
            "• 1. İdgam-ı Misleyn: Sakin Mîm + Mîm -> Gunneli",
            "  Örnek: Lehüm mâ — Kulûbihim meradun",
            "• 2. İhfâ-i Şefevî: Sakin Mîm + Bâ -> Dudak ihfası",
            "  Örnek: Ve mâ hüm bi-dârrîne (Bakara, 102)",
            "• 3. İzhar-ı Şefevî: Sakin Mîm + diğer 26 harf",
            "  Örnek: Eydîhim ve mâ — Aleyhim ve lâ"
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Kalkale Harfleri (Kâf, Tı, Bâ, Cîm, Dâl)", [
            "• Kodlaması: 'Kutbu Cedin' (5 harf).",
            "• Kelime ortasında veya sonunda cezimli (sakin)",
            "  geldiğinde mahrecinden çarptırılarak okunur.",
            "• Örnek: Ve lekad — Min kablü (Bakara, 97-100)",
            "• Örnek: Halâkin — Ebeden (durulduğunda)",
            "• Sesin hapsedilmeyip hafifçe sıçratılmasıdır."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Lafzatullah (Allah Lafzı) ve Vakıf (Durak) İşaretleri</text>',
        _kart(30, 50, 335, 215, "Lafzatullah (Allah Lafzı) Okunuşu", [
            "• 'Allah' lafzından önceki harfin harekesi",
            "  ÜSTÜN veya ÖTRE ise KALIN ('Allâh') okunur:",
            "  Örnek: İndallâhi — Rasûlullâhi — Fadlullâhi",
            "• 'Allah' lafzından önceki harfin harekesi",
            "  ESRE ise İNCE ('Lillâh / Billâh') okunur:",
            "  Örnek: Bi-iznillâhi — Lillâhi — Min indillâh"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Vakıf (Durak) İşaretleri ve Nefes Yönetimi", [
            "• Mîm (Lâzım durak): Kesinlikle durulmalı.",
            "• Tı ve Kaf-Fâ: Durmak daha uygundur.",
            "• Cîm (Câiz durak): Durulabilir de geçilebilir de.",
            "• Zây ve Sâd: Geçmek daha uygundur.",
            "• Lâ (Lâm-Elif): Ayet ortasında durulmamalıdır.",
            "• Durulan kelimenin son harekesi sükûnlu okunur."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara Suresi 104. Ayet: Konuşma ve Hitap Edebi</text>',
        _kart(30, 50, 335, 195, "Râinâ Demeyin, Ünzurnâ Deyin!", [
            "• 'Ey iman edenler! (Peygamber'e) Râinâ demeyin,",
            "  Ünzurnâ (Bize bak, bizi gözet) deyin",
            "  ve onu can kulağıyla dinleyin!' (Bakara, 104)",
            "• Yanlış anlaşılabilecek kaba sözler yerine",
            "  saygılı ve açık ifadeler seçilmelidir."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Peygamberimize ve Büyüklerimize Edep", [
            "• Hz. Peygamber'i (sav) dinlemek ve sünnetine",
            "  uymak müminin en temel sorumluluğudur.",
            "• Günlük hayatta öğretmenlerimize, ailemize",
            "  ve arkadaşlarımıza hitap ederken de",
            "  bu Kur'an edebini kuşanmalıyız."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
