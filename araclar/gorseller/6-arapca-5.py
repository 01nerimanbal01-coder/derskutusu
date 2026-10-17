# -*- coding: utf-8 -*-
"""6. Sınıf Arapça — 5. Hafta Görselleri (1. Ünite: Akrabalarım - Çalışma Yerleri, Fiil Cümlesi ve Sıla-i Rahim)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Akrabaların Meslekleri ve Çalıştıkları Yerler (Eyne Ya\'melü?)</text>',
        _kart(25, 50, 225, 215, "Okul ve Hastane", [
            "• el-Medresetü (Okul):",
            "  Muallim / Muallime (Öğretmen)",
            "• el-Müsteşfâ (Hastane):",
            "  Tabîb / Tabîbe (Doktor)",
            "  Mümerrid / Mümerride (Hemşire)",
            "• 'fî' harf-i cerri: '-de / -da' anlamı"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "Şirket, Fabrika ve Çiftlik", [
            "• eş-Şeriketü (Şirket):",
            "  Mühendis / Mühendise",
            "• el-Masna'u (Fabrika):",
            "  Âmil / Âmile (İşçi)",
            "• el-Mezra'atü (Çiftlik / Tarla):",
            "  Fellâh / Fellâha (Çiftçi)"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "Fırın, Lokanta ve Adliye", [
            "• el-Furnu (Fırın): Habbâz (Fırıncı)",
            "• el-Mat'amu (Lokanta): Tabbâh (Aşçı)",
            "• el-Mahkemetü (Mahkeme): Hâkim",
            "• el-Mektebü (Ofis): Muvazzaf (Memur)",
            "• es-Saydeliyyetü (Eczane): Saydelî",
            "• Her meslek topluma hizmet üretir."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Nerede Çalışıyor? Müzekker (Ya\'melü) ve Müennes (Ta\'melü) Kalıbı</text>',
        _kart(30, 50, 335, 215, "Erkek Akrabalar İçin (Ya'melü fî...)", [
            "• Soru: Eyne ya'melü ammüke?",
            "  (Amcan nerede çalışıyor?)",
            "• Cevap: Huve ya'melü fi'l-müsteşfâ.",
            "  (O, hastanede çalışıyor.)",
            "• Örnek: Hâlî ya'melü fi'l-medreseti.",
            "  (Dayım okulda çalışıyor.)"
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Kadın Akrabalar İçin (Ta'melü fî...)", [
            "• Soru: Eyne ta'melü ammetüke?",
            "  (Halan nerede çalışıyor?)",
            "• Cevap: Hiye ta'melü fi'ş-şeriketi.",
            "  (O, şirkette çalışıyor.)",
            "• Örnek: Hâletî ta'melü fi'l-müsteşfâ.",
            "  (Teyzem hastanede çalışıyor.)"
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">fî Harf-i Cerri İle Şemsî ve Kamerî Harflerin Bağlantılı Okunuşu</text>',
        _kart(30, 50, 335, 215, "fî + Kamerî Harfli Kelime (Lâm Okunur)", [
            "• fî + el-Müsteşfâ -> fi'l-müsteşfâ",
            "• fî + el-Medreseti -> fi'l-medreseti",
            "• fî + el-Masna'i -> fi'l-masna'i",
            "• fî + el-Mezra'ati -> fi'l-mezra'ati",
            "• Kural: 'fî' uzatması düşer, doğrudan",
            "  cezimli Lâm harfine bağlanarak okunur."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "fî + Şemsî Harfli Kelime (Şeddeli Geçiş)", [
            "• fî + eş-Şeriketi -> fi'ş-şeriketi",
            "• fî + es-Saydeliyyeti -> fi's-saydeliyyeti",
            "• fî + ed-Dükkâni -> fi'd-dükkâni",
            "• fî + et-Tâirati -> fi't-tâirati",
            "• Kural: Hem 'fî' uzatması hem de Lâm okunmaz;",
            "  doğrudan şeddeli şemsî harfe çarpılır!"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">1. Ünite Değerlendirme: Sıla-i Rahim ve Akrabalık Hukuku</text>',
        _kart(30, 50, 335, 195, "el-Akrabûne Evlâ bi'l-Ma'rûf", [
            "• Anlamı: 'İyiliğe en layık olanlar,",
            "  en yakın akrabalardır.'",
            "• Baba tarafı: Ceddün, Ceddetün, Ammün, Ammetün",
            "• Anne tarafı: Ceddün, Ceddetün, Hâlün, Hâletün",
            "• Tüm akrabalarımız bizim geniş ailemizdir."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Sıla-i Rahim (Akraba Ziyareti)", [
            "• Akrabaları ziyaret etmek, hal-hatırlarını",
            "  sormak ve yardımlaşmak 'Sıla-i Rahim'dir.",
            "• Bayramlarda, hastalıkta ve sevinçli",
            "  günlerde akrabalarla bağları koparmamak",
            "  rızkı bereketlendirir ve sevgiyi artırır."
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
