# -*- coding: utf-8 -*-
"""7. Sınıf Kur'an-ı Kerim — 5. Hafta Görselleri (Bakara Suresi 177-186. Ayetler: Birr, Oruç ve Dua)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara Suresi 177. Ayet: Gerçek İyilik (el-Birr) Nedir?</text>',
        _kart(25, 50, 225, 215, "1. İman Boyutu", [
            "• İyilik sadece yüzü doğuya veya",
            "  batıya çevirmek değildir.",
            "• Allah'a, ahiret gününe,",
            "  meleklere, kitaplara ve",
            "  peygamberlere gönülden",
            "  iman etmektir."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. İnfak ve İbadet Boyutu", [
            "• Sevdiği maldan akrabalara,",
            "  yetimlere, yoksullara, yolda",
            "  kalmışlara ve özgürlüğünü",
            "  kaybedenlere harcamaktır.",
            "• Namazı dosdoğru kılmak",
            "  ve zekâtı vermektir."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Ahlak ve Sabır Boyutu", [
            "• Söz verdiğinde sözünde durmak",
            "  (el-mûfûne bi-ahdihim).",
            "• Sıkıntı, hastalık ve zorluk",
            "  zamanlarında sabretmek.",
            "• İşte doğru olanlar (sâdıklar) ve",
            "  takva sahipleri (müttakiler) bunlardır!"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara Suresi 183-186. Ayetler: Oruç, Kur\'an Ayı Ramazan ve Dua</text>',
        _kart(30, 50, 335, 215, "183-185. Ayetler: Oruç ve Ramazan", [
            "• 'Ey iman edenler! Sizden öncekilere farz",
            "  kılındığı gibi sakınasınız (takvaya eresiniz)",
            "  diye oruç size de farz kılındı.' (Bakara, 183)",
            "• Ramazan ayı, insanlara hidayet rehberi olan",
            "  Kur'an-ı Kerim'in indirildiği mübarek aydır.",
            "• Hasta ve yolculara kolaylık (ruhsat) tanınmıştır."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "186. Ayet: Allah'ın Kullarına Yakınlığı ve Dua", [
            "• 'Kullarım sana beni sorarlarsa bilsinler ki",
            "  ben onlara çok yakınım (fe-innî karîb)!'",
            "• 'Bana dua edince dua edenin duasına",
            "  icabet ederim (karşılık veririm).'",
            "• Müminler de yalnızca Allah'a yönelmeli",
            "  ve O'na güvenmelidir (Bakara, 186)."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Bakara 177-186. Ayetlerde Râ Harfinin Okunuşu ve Zamir Kuralları</text>',
        _kart(30, 50, 335, 215, "Râ Harfinin Kalın ve İnce Okunuşu", [
            "• Kalın Râ: Râ üstün veya ötreli ise,",
            "  ya da sakin olup öncesi üstün/ötre ise kalın okunur:",
            "  Örnek: el-Bakra — Şehrü Ramadâne — el-Furkân",
            "• İnce Râ: Râ esreli ise veya sakin olup öncesi",
            "  asli esre / med harfi ise ince okunur:",
            "  Örnek: el-Birra — el-Âhiri — Habîrun — Kâdirun"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Zamir (Hû / Hî) Uzatma Kuralı", [
            "• Kelime sonundaki tekil erkek zamiri (-hû/-hî):",
            "• Kendinden ÖNCEKİ harf harekeli ise UZATILIR:",
            "  Örnek: İnnahû — Rabbihî — Aleyhi (istisna)",
            "• Kendinden ÖNCEKİ harf cezimli veya med harfi",
            "  ise UZATILMAZ (kısa okunur):",
            "  Örnek: Minhü — Fîhi — Aleyhi — İleyhi"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">178-182. Ayetler: Adalet, Vasiyet ve Toplumsal Barış</text>',
        _kart(30, 50, 335, 195, "Adalet ve Hakkaniyet İlkesi", [
            "• Bakara 178-179. ayetlerde suç ve cezada",
            "  denklik, adalet ve bağışlama teşvik edilir.",
            "• Cahiliye dönemindeki sınırsız intikam ve",
            "  kan davaları kaldırılarak hayat hakkı",
            "  güvence altına alınmıştır."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Vasiyet, Helal Kazanç ve Islah", [
            "• 180-182. ayetlerde vasiyette adaletli",
            "  davranmak, hak yememek ve anlaşmazlıkları",
            "  barışla düzeltmek (ıslah) öğütlenir.",
            "• Yüce Allah bağışlayandır (Gafûr) ve",
            "  merhamet edendir (Rahîm)."
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
