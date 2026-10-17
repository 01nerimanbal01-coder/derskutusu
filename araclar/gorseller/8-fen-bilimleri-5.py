# -*- coding: utf-8 -*-
"""8. Sınıf Fen Bilimleri — 5. Hafta Görselleri (DNA ve Genetik Kod; Kalıtıma Giriş)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kalıtsal Yapıların Büyükten Küçüğe Sıralaması (KeDiGeNi)</text>',
        _kart(25, 50, 225, 215, "1. Kromozom ve DNA", [
            "• Kromozom: DNA'nın özel protein",
            "  kılıfla sarılmış en büyük halidir.",
            "• İnsanda 2n = 46 kromozom bulunur.",
            "• DNA: Hücrenin yönetici molekülüdür;",
            "  çift zincirli sarmal yapıdadır.",
            "• Kalıtsal bilgileri taşır."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Gen ve Nükleotid", [
            "• Gen: DNA üzerinde belirli görevleri",
            "  (göz rengi, kan grubu) şifreleyen",
            "  anlamlı görev birimleridir.",
            "• Nükleotid: DNA'nın en küçük",
            "  temel yapı birimidir.",
            "• Sıralama: Kromozom &gt; DNA &gt; Gen &gt; Nükleotid"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Nükleotidin Yapısı ve Eşleşme", [
            "• Nükleotid = Fosfat (P) + Deoksiriboz",
            "  Şekeri (D) + Organik Baz (A, T, G, C)",
            "• Adenin (A) &lt;-&gt; Timin (T) (İkili bağ)",
            "• Guanin (G) &lt;-&gt; Sitozin (C) (Üçlü bağ)",
            "• Toplam Nükleotid = Şeker = Fosfat",
            "• A + G = T + C"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">DNA\'nın Kendini Eşlemesi (Replikasyon) Basamakları</text>',
        _kart(30, 50, 335, 215, "Eşleme Süreci (Hücre Bölünmesi Öncesi)", [
            "• 1. DNA'nın çift zinciri fermuar gibi açılır.",
            "• 2. Sitoplazmada serbest halde bulunan",
            "  uygun nükleotidler çekirdeğin içine girer.",
            "• 3. Açılan zincirlerde A karşısına T,",
            "  G karşısına C gelecek şekilde yerleşir.",
            "• 4. Sonuçta başlangıçtakiyle BİREBİR AYNI",
            "  2 yeni DNA molekülü oluşur."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "DNA Eşleme Hataları ve Onarım", [
            "• Tek zincirde nükleotid eksikliği veya",
            "  yanlış eşleşme (örneğin A karşısına G)",
            "  varsa bu hata ONARILABİLİR!",
            "• Ancak karşılıklı İKİ ZİNCİRDE birden",
            "  aynı hizada nükleotid eksikse bu hata",
            "  ONARILAMAZ ve mutasyona yol açar!"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kalıtım (Genetik) İle İlgili Temel Kavramlar</text>',
        _kart(30, 50, 335, 215, "Baskın, Çekinik ve Alel Gen", [
            "• Alel Gen: Biri anneden diğeri babadan gelen",
            "  bir karakterin gen çiftidir.",
            "• Baskın (Dominant) Gen: Etkisini her durumda",
            "  dış görünüşte gösterir; BÜYÜK harfle (A, B, U).",
            "• Çekinik (Resesif) Gen: Sadece saf (homozigot)",
            "  durumda etkisini gösterir; küçük harfle (a, b, u)."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Saf/Melez Döl, Genotip ve Fenotip", [
            "• Saf (Arı / Homozigot) Döl: AA veya aa",
            "• Melez (Heterozigot) Döl: Aa (biri büyük biri küçük)",
            "• Genotip: Canlının sahip olduğu gen yapısı",
            "  (AA, Aa, aa).",
            "• Fenotip: Genotipin ve çevrenin etkisiyle",
            "  oluşan dış görünüş (Mor çiçek, Beyaz çiçek)."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Gregor Mendel ve Bezelye Çaprazlamalarına Giriş</text>',
        _kart(30, 50, 335, 195, "Mendel Neden Bezelye Bitkisini Seçti?", [
            "• Yılda birden fazla döl verebilmesi.",
            "• Kolay yetiştirilmesi ve ucuz olması.",
            "• Çok sayıda zıt karaktere (tohum rengi,",
            "  çiçek rengi, boy uzunluğu) sahip olması.",
            "• Kendi kendine tozlaşmaya uygun kapalı çiçek yapısı."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "İnsanlarda ve Bezelyelerde Baskın Özellikler", [
            "• Bezelyede: Mor çiçek &gt; Beyaz, Sarı tohum &gt; Yeşil,",
            "  Düzgün tohum &gt; Buruşuk, Uzun boy &gt; Kısa boy.",
            "• İnsanda: Koyu göz rengi &gt; Açık göz, Kıvırcık saç &gt; Düz,",
            "  Ayrık kulak memesi &gt; Yapışık kulak memesi."
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
