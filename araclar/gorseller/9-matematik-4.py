# -*- coding: utf-8 -*-
"""9. Sınıf Matematik — 4. Hafta görsel modülü:
Sayılar — Gerçek Sayı Aralıklarının Gösterimi ve Aralıklarla İlgili İşlemlerde Küme Sembolleri"""

C_MOR = "#6c3483"
C_MAVI = "#1a5276"
C_YESIL = "#1e8449"
C_TURUNCU = "#b9770e"
C_KIRMIZI = "#922b21"
C_ACIK_MOR = "#f5eef8"
C_ACIK_MAVI = "#eaf2f8"
C_ACIK_YESIL = "#e9f7ef"
C_ACIK_SARI = "#fef9e7"
C_ACIK_KIRMIZI = "#fdedec"
C_KOYU = "#1c2833"
C_GRI = "#566573"
C_SINIR = "#d5d8dc"


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def gorsel_1():
    """Sınırlı Gerçek Sayı Aralıkları: Kapalı [a,b], Açık (a,b) ve Yarı Açık [a,b), (a,b]."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Gerçek Sayı Aralıklarının Gösterimi: Kapalı, Açık ve Yarı Açık Aralıklar</text>',
    ]
    araliklar = [
        ("Kapalı Aralık: [a, b]", "a ≤ x ≤ b", True, True, C_MAVI, C_ACIK_MAVI, 18, 58),
        ("Açık Aralık: (a, b)", "a < x < b", False, False, C_KIRMIZI, C_ACIK_KIRMIZI, 348, 58),
        ("Yarı Açık Aralık: [a, b)", "a ≤ x < b", True, False, C_YESIL, C_ACIK_YESIL, 18, 158),
        ("Yarı Açık Aralık: (a, b]", "a < x ≤ b", False, True, C_MOR, C_ACIK_MOR, 348, 158),
    ]
    for baslik, esit, sol_dolu, sag_dolu, renk, bg, x, y in araliklar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="90" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}   →   {esit}</text>')
        # Sayı doğrusu
        y_dogru = y + 54
        p.append(f'<line x1="{x+30}" y1="{y_dogru}" x2="{x+284}" y2="{y_dogru}" stroke="{C_GRI}" stroke-width="2"/>')
        p.append(f'<line x1="{x+85}" y1="{y_dogru}" x2="{x+229}" y2="{y_dogru}" stroke="{renk}" stroke-width="5"/>')
        sol_fill = renk if sol_dolu else "#fff"
        sag_fill = renk if sag_dolu else "#fff"
        p.append(f'<circle cx="{x+85}" cy="{y_dogru}" r="6.5" fill="{sol_fill}" stroke="{renk}" stroke-width="2.5"/>')
        p.append(f'<circle cx="{x+229}" cy="{y_dogru}" r="6.5" fill="{sag_fill}" stroke="{renk}" stroke-width="2.5"/>')
        p.append(f'<text x="{x+85}" y="{y_dogru+22}" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">a</text>')
        p.append(f'<text x="{x+229}" y="{y_dogru+22}" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">b</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Sınırsız Gerçek Sayı Aralıkları: [a, ∞), (a, ∞), (-∞, b], (-∞, b)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Sınırsız Gerçek Sayı Aralıkları (−∞ ve +∞ Her Zaman Açık Parantezle Gösterilir)</text>',
    ]
    kartlar = [
        ("[a, ∞)  →  x ≥ a", True, "sag", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("(a, ∞)  →  x > a", False, "sag", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("(−∞, a]  →  x ≤ a", True, "sol", C_TURUNCU, C_ACIK_SARI, 18, 150),
        ("(−∞, a)  →  x < a", False, "sol", C_KIRMIZI, C_ACIK_KIRMIZI, 348, 150),
    ]
    for baslik, dolu, yon, renk, bg, x, y in kartlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="82" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        yd = y + 50
        p.append(f'<line x1="{x+30}" y1="{yd}" x2="{x+284}" y2="{yd}" stroke="{C_GRI}" stroke-width="2"/>')
        if yon == "sag":
            p.append(f'<line x1="{x+110}" y1="{yd}" x2="{x+280}" y2="{yd}" stroke="{renk}" stroke-width="5"/>')
            p.append(f'<polygon points="{x+284},{yd} {x+272},{yd-6} {x+272},{yd+6}" fill="{renk}"/>')
            fill = renk if dolu else "#fff"
            p.append(f'<circle cx="{x+110}" cy="{yd}" r="6.5" fill="{fill}" stroke="{renk}" stroke-width="2.5"/>')
            p.append(f'<text x="{x+110}" y="{yd+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">a</text>')
            p.append(f'<text x="{x+268}" y="{yd+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{renk}">+∞</text>')
        else:
            p.append(f'<line x1="{x+34}" y1="{yd}" x2="{x+204}" y2="{yd}" stroke="{renk}" stroke-width="5"/>')
            p.append(f'<polygon points="{x+30},{yd} {x+42},{yd-6} {x+42},{yd+6}" fill="{renk}"/>')
            fill = renk if dolu else "#fff"
            p.append(f'<circle cx="{x+204}" cy="{yd}" r="6.5" fill="{fill}" stroke="{renk}" stroke-width="2.5"/>')
            p.append(f'<text x="{x+204}" y="{yd+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">a</text>')
            p.append(f'<text x="{x+46}" y="{yd+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{renk}">−∞</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Aralıklarda Küme İşlemleri: Birleşim (∪), Kesişim (∩), Fark (\\) ve Tümleyen (A')."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Gerçek Sayı Aralıklarında Küme İşlemleri: A = [−2, 4) ve B = (1, 6]</text>',
    ]
    islemler = [
        ("Kesişim (A ∩ B)", "Her iki aralıkta ortak olan", "elemanlar: A ∩ B = (1, 4)", "Alt sınırların büyüğü, üst sınırların küçüğü", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("Birleşim (A ∪ B)", "En az birinde bulunan tüm", "elemanlar: A ∪ B = [−2, 6]", "Kesişen aralıklarda en uç sınırlar alınır", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("Fark (A \\ B)", "A'da olup B'de olmayanlar:", "A \\ B = [−2, 1]", "DİKKAT: 1 sayısı B'de olmadığı için A\\B'ye DÂHİLDİR!", C_KIRMIZI, C_ACIK_KIRMIZI, 18, 158),
        ("Tümleyen (A')", "ℝ'de olup A = [−2, 4)'te olmayanlar:", "A' = (−∞, −2) ∪ [4, ∞)", "Kapalı uç açık uca, açık uç kapalı uca dönüşür!", C_MOR, C_ACIK_MOR, 348, 158),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in islemler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="92" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+44}" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+63}" text-anchor="middle" font-size="11.5" font-weight="800" fill="{renk}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+81}" text-anchor="middle" font-size="9.5" font-weight="700" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Fark ve Tümleyen İşlemlerinde Uç Noktaların Ters Dönme Kuralı."""
    w, h = 680, 235
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Altın Kural: Tümleyen (A\') ve Fark (A \\ B) İşlemlerinde Sınır Noktası Değişimi</text>',
        f'<rect x="18" y="58" width="644" height="160" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<text x="340" y="86" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_KOYU}">Bir sınır noktası çıkarılan kümede VARSA sonuçta YOKTUR; çıkarılan kümede YOKSA sonuçta VARDIR!</text>',
        f'<rect x="40" y="104" width="280" height="94" rx="8" fill="#fff" stroke="{C_MAVI}" stroke-width="1.5"/>',
        f'<text x="180" y="128" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_MAVI}">Kapalı Uç  [ veya ]   ⟷   Açık Uç  ( veya )</text>',
        f'<text x="180" y="154" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">≤  tersi  &gt;     |     ≥  tersi  &lt;</text>',
        f'<text x="180" y="180" text-anchor="middle" font-size="10.5" fill="{C_GRI}">Örn: [3, ∞)\'un tümleyeni (−∞, 3) olur.</text>',
        f'<rect x="360" y="104" width="280" height="94" rx="8" fill="#fff" stroke="{C_YESIL}" stroke-width="1.5"/>',
        f'<text x="500" y="128" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_YESIL}">Küme Sembolleri Özeti</text>',
        f'<text x="500" y="152" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">∈ : Elemanıdır  |  ⊂ : Alt kümesidir</text>',
        f'<text x="500" y="172" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">∪ : Birleşim  |  ∩ : Kesişim  |  \\ : Fark</text>',
        f'<text x="500" y="190" text-anchor="middle" font-size="10" fill="{C_GRI}">ℝ : Gerçek sayılar (Evrensel küme)</text>',
    ]
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
    return v
