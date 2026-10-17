# -*- coding: utf-8 -*-
"""8. Sınıf Temel Dini Bilgiler — 5. Hafta Görselleri (Kur'an-ı Kerim'e Karşı Ahlaki Sorumluluklarımız)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'e Karşı 5 Temel Ahlaki Sorumluluğumuz</text>',
        _kart(25, 50, 225, 215, "1. İman ve Teslimiyet", [
            "• Kur'an-ı Kerim'in hiçbir değişikliğe",
            "  uğramamış son ilahi kitap (Allah",
            "  kelamı) olduğuna şüphesiz inanmak.",
            "• İçindeki tüm emir, yasak ve",
            "  haberlerin hak olduğunu kabul",
            "  etmek (Hicr, 9)."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Okuma (Tilavet) ve Anlama", [
            "• Kur'an'ı tecvit kurallarına uygun",
            "  ve tertîl üzere (tane tane) okumak.",
            "• Meal ve tefsirlerinden yararlanarak",
            "  ayetlerin anlamını öğrenmek ve",
            "  üzerinde derinlemesine düşünmek",
            "  (Tedebbür - Sâd, 29)."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Yaşama ve Öğretme", [
            "• Kur'an'ın ahlak ilkelerini kendi",
            "  hayatımıza uygulamak (Amel etmek).",
            "• 'Sizin en hayırlınız Kur'an'ı",
            "  öğrenen ve öğretendir!' (Hadis)",
            "• Mushaf'a abdestli dokunmak ve",
            "  okunduğunda susup dinlemek."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'i Okuma ve Dinleme Edebi (Tilavet Âdâbı)</text>',
        _kart(30, 50, 335, 215, "Okurken Uyulması Gereken Edepler", [
            "• Abdestli olmak, temiz kıyafet giymek ve",
            "  mümkünse kıbleye yönelerek oturmak.",
            "• Okumaya 'Eûzü-Besmele' çekerek başlamak",
            "  (Nahl suresi 98. ayet emri).",
            "• Acele etmeden, tecvitli ve 'tertîl' üzere",
            "  (harflerin hakkını vererek tane tane) okumak."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Dinlerken ve Korurken Edepler", [
            "• 'Kur'an okunduğu zaman onu dinleyin ve",
            "  susun ki size merhamet edilsin!' (A'râf, 204).",
            "• Mushaf-ı Şerif'i bel hizasından aşağıda veya",
            "  yerde bırakmamak; yüksek ve temiz yerde tutmak.",
            "• Rahle veya kürsü üzerinde saygıyla okumak."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Tedebbür (Anlayarak Düşünme) ve Hayat Kitabı Bilinci</text>',
        _kart(30, 50, 335, 215, "Sâd Suresi 29. Ayet: İndiriliş Amacı", [
            "• 'Bu Kur'an, ayetlerini derinlemesine",
            "  düşünsünler (li-yeddebberû âyâtihî) ve akıl",
            "  sahipleri öğüt alsınlar diye sana indirdiğimiz",
            "  mübarek bir kitaptır.' (Sâd, 38/29).",
            "• Kur'an sadece sevap için okunan değil, anlamı",
            "  düşünülüp rehber edinilen bir hayat kitabıdır."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Kur'an'ı Yalnız ve Mahzun Bırakmamak", [
            "• Furkân suresi 30. ayette Peygamberimizin",
            "  'Rabbim! Kavmim bu Kur'an'ı terk edilmiş",
            "  (mehcûr) bıraktı!' uyarısı yer alır.",
            "• Kur'an'ı duvara asıp okumamak veya okuyup",
            "  ahlakıyla amel etmemek onu mahzun bırakmaktır."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Yürüyen Kur\'an: Hz. Peygamber\'in (sav) Ahlakı</text>',
        _kart(30, 50, 335, 195, "Hz. Âişe'nin Tarihi Tanımı", [
            "• Sahabiler Hz. Âişe validemize Peygamberimizin",
            "  ahlakını sorduklarında şu cevabı vermiştir:",
            "• 'Siz hiç Kur'an okumuyor musunuz? Onun",
            "  ahlakı Kur'an'dı!' (Müslim, Müsâfirîn, 139).",
            "• Peygamberimiz yaşayan (canlı) bir Kur'an'dı."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "1. Ünite Değerlendirme: Üç Büyük Sorumluluk", [
            "• 1. Allah'a Karşı: İman, ibadet, şükür ve ihlas.",
            "• 2. Peygamberimize Karşı: Sevgi, itaat, sünnete",
            "  uyma ve salavat getirme.",
            "• 3. Kur'an-ı Kerim'e Karşı: İnanma, okuma,",
            "  anlama, yaşama ve saygı gösterme."
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
