# -*- coding: utf-8 -*-
"""9. Sınıf Fizik — 4. Hafta görsel modülü:
Fizik Bilimi ve Kariyer Keşfi — Bilim ve Teknoloji Araştırma Merkezleri ve Kariyer Olanakları"""

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
    """Türkiye'deki Bilim ve Teknoloji Araştırma Merkezleri (TÜBİTAK, TENMAK, TUA, ASELSAN)."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Türkiye\'deki Bilim ve Teknoloji Araştırma Merkezleri (Ulusal Kuruluşlar)</text>',
    ]
    kurumlar = [
        ("TÜBİTAK (1963)", "Türkiye Bilimsel ve Teknolojik Araştırma Kurumu", "Temel bilimler, uzay, savunma ve Ar-Ge projelerini destekler.", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("TENMAK (2020)", "Türkiye Enerji, Nükleer ve Maden Araştırma Kurumu", "Nükleer enerji, radyasyon, bor ve nadir toprak elementleri çalışır.", C_YESIL, C_ACIK_YESIL, 348, 58),
        ("TUA (2018)", "Türkiye Uzay Ajansı", "Millî Uzay Programı, uydu teknolojileri ve uzay araştırmalarını yürütür.", C_MOR, C_ACIK_MOR, 18, 158),
        ("ASELSAN (1975)", "Askerî Elektronik Sanayi", "Radar, elektro-optik, haberleşme ve savunma teknolojileri geliştirir.", C_TURUNCU, C_ACIK_SARI, 348, 158),
    ]
    for baslik, acilim, gorev, renk, bg, x, y in kurumlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="88" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">{acilim}</text>')
        p.append(f'<text x="{x+157}" y="{y+68}" text-anchor="middle" font-size="10" fill="{C_GRI}">{gorev}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Uluslararası Bilim Araştırma Merkezleri (CERN, NASA, ESA)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Uluslararası Bilim ve Araştırma Merkezleri (CERN, NASA, ESA)</text>',
    ]
    merkezler = [
        ("CERN (1954)", "Avrupa Nükleer Araştırma Merkezi", "İsviçre-Fransa sınırında Büyük Hadron", "Çarpıştırıcısı (LHC) ile parçacık fiziği.", C_MOR, C_ACIK_MOR, 18),
        ("NASA (1958)", "Ulusal Havacılık ve Uzay Dairesi (ABD)", "Uzay teleskopları (James Webb, Hubble),", "gezegen keşifleri ve astrofizik.", C_MAVI, C_ACIK_MAVI, 236),
        ("ESA (1975)", "Avrupa Uzay Ajansı", "Avrupa ülkelerinin ortak uydu, roket", "ve derin uzay araştırma programı.", C_YESIL, C_ACIK_YESIL, 454),
    ]
    for baslik, acilim, s1, s2, renk, bg, x in merkezler:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="106" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">{acilim}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="150" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">{s2}</text>')
        alt = "Yüksek Enerji ve Plazma Fiziği" if x == 18 else ("Astrofizik ve Uzay Teknolojisi" if x == 236 else "Uydu ve Yer Gözlem Sistemleri")
        p.append(f'<rect x="{x+14}" y="172" width="180" height="42" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="197" text-anchor="middle" font-size="9.5" font-weight="700" fill="{renk}">{alt}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Fizik Alt Dalları ile Kariyer ve Mühendislik Alanlarının Eşleşmesi."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Fizik Bilimiyle İlişkili Kariyer ve Uzmanlık Alanları</text>',
    ]
    alanlar = [
        ("Medikal Fizik Uzmanı", "Nükleer Fizik & Optik", "Radyoterapi, MR, tomografi", "ve tıbbi görüntüleme", C_KIRMIZI, C_ACIK_KIRMIZI, 16),
        ("Nanoteknoloji Uzmanı", "Katıhâl & Atom Fiziği", "Yarı iletken çipler, akıllı", "malzemeler ve kuantum", C_MAVI, C_ACIK_MAVI, 182),
        ("Uzay ve Havacılık Müh.", "Mekanik & Termodinamik", "Aerodinamik, roket itki", "sistemleri ve uydular", C_MOR, C_ACIK_MOR, 348),
        ("Optik ve Fotonik Müh.", "Optik & Elektromanyetizma", "Lazer, fiber optik iletişim", "ve mercek sistemleri", C_TURUNCU, C_ACIK_SARI, 514),
    ]
    for baslik, dal, s1, s2, renk, bg, x in alanlar:
        p.append(f'<rect x="{x}" y="60" width="150" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="79" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+75}" y="108" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{dal}</text>')
        p.append(f'<text x="{x+75}" y="138" text-anchor="middle" font-size="10" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+75}" y="156" text-anchor="middle" font-size="10" fill="{C_KOYU}">{s2}</text>')
        p.append(f'<rect x="{x+14}" y="180" width="122" height="44" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+75}" y="206" text-anchor="middle" font-size="9.5" font-weight="700" fill="{renk}">Disiplinlerarası Kariyer</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Bilim İnsanının Özellikleri ve Kariyer Planlama Adımları."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Fizik Temelli Kariyer Keşfi ve Bilimsel Çalışma İlkeleri</text>',
    ]
    adimlar = [
        ("1. Merak ve Sorgulama", "Doğa olaylarını gözlemleme,", "problem çözme ve analitik", "düşünme becerisi", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Ekip Çalışması ve Etik", "Büyük araştırma merkezlerinde", "farklı disiplinlerle iş birliği", "ve bilimsel dürüstlük", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Teknolojiye Dönüştürme", "Temel fizik yasalarını", "mühendislik, tıp ve savunma", "teknolojilerine aktarma", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in adimlar:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">Geleceğin Bilim İnsanı</text>')
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
