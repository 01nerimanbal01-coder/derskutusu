# -*- coding: utf-8 -*-
"""5. Sınıf Kur'an-ı Kerim — 5. Hafta Görselleri (Harfleri Yazma: Kelime Birleştirme, Med, Cezm ve Şedde)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Harfleri Birleştirerek Kelime Yazma Adımları</text>',
        _kart(25, 50, 225, 215, "1. Adım: Harfleri Tanıma", [
            "• Harflerin müstakil (tek başına) şekli",
            "  belirlenir: ك - ت - ب",
            "• Sağdan sola yazılış sırası izlenir.",
            "• Noktaların sayısı ve yeri (üst/alt)",
            "  dikkatle kontrol edilir.",
            "• Satır çizgisi referans alınır."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Adım: Gövde Birleştirme", [
            "• Baştaki ve ortadaki harflerin kuyruk",
            "  kısımları atılarak gövdeleri kalır.",
            "• كَ + تَ + بَ -> كَتَبَ (Ketebe)",
            "• سَ + جَ + دَ -> سَجَدَ (Secede)",
            "• Sondaki harf asli şeklini korur.",
            "• Bağlantı çizgisi satırda düz ilerler."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Adım: Nokta ve Hareke", [
            "• Önce kelimenin ana iskeleti çizilir.",
            "• Ardından harflerin noktaları konur.",
            "• En son harekeler (üstün, esre, ötre)",
            "  harflerin üstüne veya altına eklenir.",
            "• Böylece el kaldırmadan akıcı ve",
            "  okunaklı hat yazımı sağlanır."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Birleşmeyen 6 Harf (Elif, Dâl, Zâl, Râ, Zây, Vâv) İle Kelime Yazımı</text>',
        _kart(30, 50, 335, 215, "Kural: Sağdan Birleşir, Soldan Birleşmez", [
            "• Bu 6 harf: ا - د - ذ - ر - ز - و",
            "• Kendinden ÖNCEKİ (sağdaki) harfe tutunur.",
            "• Kendinden SONRAKİ (soldaki) harfe el uzatmaz!",
            "• Bu harflerden sonra gelen harf, kelime",
            "  ortasında olsa bile BAŞTA yazılıyormuş",
            "  gibi yeni bir bağlantı başlatır."
        ], "#e11d48", "#fff1f2"),
        _kart(395, 50, 335, 215, "Uygulamalı Kelime Örnekleri", [
            "• دَرَسَ (De-ra-se): Üçü de birleşmeyen harf",
            "  olduğu için hepsi ayrı yazılır!",
            "• وَجَدَ (Ve-ce-de): Vâv soldan birleşmez,",
            "  Cîm ile Dâl birleşir.",
            "• قَرَأَ (Ka-ra-e): Kâf ile Râ birleşir,",
            "  Râ'dan sonraki Hemze ayrı yazılır."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Uzatma Harfleri (Med Harfleri: Elif, Vâv, Yâ) ve Yazımı</text>',
        _kart(25, 50, 225, 215, "Med Harfi: Elif (ا)", [
            "• Harekeli harfin üstünü (fetha) varsa",
            "  ve ardından harekesiz Elif gelirse",
            "  harf bir elif miktarı uzatılır (â/ê).",
            "• Örnek: قَالَ (Kâle)",
            "• Örnek: كَانَ (Kâne)",
            "• Lâm-Elif birleşimi: لَا (Lâ) şeklinde!"
        ], "#2563eb", "#eff6ff"),
        _kart(267, 50, 225, 215, "Med Harfi: Vâv (و)", [
            "• Harekeli harfin ötresi (damme) varsa",
            "  ve ardından harekesiz Vâv gelirse",
            "  harf uzatılarak okunur (û/ü).",
            "• Örnek: نُورٌ (Nûrun)",
            "• Örnek: يَقُولُ (Yekûlü)",
            "• Vâv kendinden sonrakine birleşmez."
        ], "#0d9488", "#f0fdfa"),
        _kart(510, 50, 225, 215, "Med Harfi: Yâ (ي)", [
            "• Harekeli harfin esresi (kesra) varsa",
            "  ve ardından harekesiz Yâ gelirse",
            "  harf uzatılarak okunur (î).",
            "• Örnek: كَرِيمٌ (Kerîmün)",
            "• Örnek: سَمِيعٌ (Semî'un)",
            "• Yâ ortada iki tarafa da birleşir."
        ], "#4f46e5", "#eef2ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Cezm, Şedde ve Tenvinli Kelimeleri Yazma Kuralları</text>',
        _kart(30, 50, 335, 195, "Cezm ve Şedde Yazımı", [
            "• Cezmli harf tek başına hece oluşturmaz;",
            "  önceki harfle birleştirilerek yazılır: الحَمْدُ",
            "• Şeddeli harf iki kez okunur ama yazıda",
            "  TEK HARF yazılıp üzerine şedde konur: رَبِّ",
            "• Şeddenin üstüne üstün/ötre, altına esre konur."
        ], "#16a34a", "#f0fdf4"),
        _kart(395, 50, 335, 195, "İki Üstün (Tenvin) ve Elif Desteği", [
            "• Kelime sonuna iki esre (-in) ve iki ötre (-ün)",
            "  doğrudan son harfin altına/üstüne yazılır.",
            "• İki üstün (-en/-an) yazılırken ise (yuvarlak tâ",
            "  ve hemze hariç) kelimenin sonuna bir destek",
            "  Elif'i eklenir: كِتَابًا (Kitâben) — عِلْمًا (İlmen)"
        ], "#9333ea", "#faf5ff"),
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
