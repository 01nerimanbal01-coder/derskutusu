# -*- coding: utf-8 -*-
"""9. Sınıf Kimya — 4. Hafta görsel modülü:
Etkileşim — Atom Teorileri (Bohr, Modern Atom Teorisi), Atomun Yapısı ve Bilimsel Bilginin Değişebilirliği"""

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
    """Bohr Atom Modeli: Enerji Düzeyleri, Absorpsiyon ve Emisyon."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Bohr Atom Modeli (1913): Yörüngeler, Absorpsiyon (Soğurma) ve Emisyon (Yayma)</text>',
        # Sol yörünge şeması
        f'<circle cx="155" cy="155" r="18" fill="{C_KIRMIZI}"/>',
        f'<text x="155" y="159" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">+p, n</text>',
        f'<circle cx="155" cy="155" r="42" fill="none" stroke="{C_MAVI}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        f'<circle cx="155" cy="155" r="68" fill="none" stroke="{C_YESIL}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        f'<circle cx="155" cy="155" r="94" fill="none" stroke="{C_MOR}" stroke-width="1.6" stroke-dasharray="4,3"/>',
        f'<text x="199" y="152" font-size="10" font-weight="700" fill="{C_MAVI}">n=1 (K)</text>',
        f'<text x="225" y="138" font-size="10" font-weight="700" fill="{C_YESIL}">n=2 (L)</text>',
        f'<text x="251" y="124" font-size="10" font-weight="700" fill="{C_MOR}">n=3 (M)</text>',
        f'<circle cx="155" cy="113" r="6" fill="{C_MAVI}"/>',
        f'<circle cx="155" cy="61" r="6" fill="{C_MOR}"/>',
        # Sağ açıklama kutuları
        f'<rect x="300" y="60" width="362" height="86" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="300" y="60" width="362" height="26" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="481" y="78" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Absorpsiyon (Soğurma): Temel Hâl → Uyarılmış Hâl</text>',
        f'<text x="481" y="106" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Düşük enerjili yörüngedeki (n=1) elektron dışarıdan enerji</text>',
        f'<text x="481" y="126" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_TURUNCU}">alarak yüksek enerjili yörüngeye (n=3) geçer (Kararsızdır).</text>',
        f'<rect x="300" y="158" width="362" height="86" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="300" y="158" width="362" height="26" rx="10" fill="{C_MOR}"/>',
        f'<text x="481" y="176" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Emisyon (Işıma): Uyarılmış Hâl → Temel Hâl</text>',
        f'<text x="481" y="204" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Uyarılmış elektron temel hâle dönerken aldığı enerji farkını</text>',
        f'<text x="481" y="224" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MOR}">foton (ışık / çizgi spektrumu) olarak dışarı yayar.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Bohr Yörünge Modeli ile Modern Atom Teorisi (Bulut/Orbital Modeli) Karşılaştırması."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Yörüngeden Orbitale: Bohr Atom Modeli ve Modern Atom Teorisi</text>',
        # Sol: Bohr
        f'<rect x="18" y="58" width="314" height="176" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Bohr Atom Modeli (Yörünge / Katman)</text>',
        f'<text x="32" y="108" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Elektronlar çizgisel, dairesel yörüngede döner.</text>',
        f'<text x="32" y="130" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Elektronun yeri ve hızı kesin kabul edilir.</text>',
        f'<text x="32" y="152" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Tek elektronlu türleri (₁H, ₂He⁺, ₃Li²⁺) açıklar.</text>',
        f'<text x="32" y="174" font-size="10.5" fill="{C_KIRMIZI}" font-weight="700">• Sınırlılık: Çok elektronlu atomları ve elektronun</text>',
        f'<text x="42" y="192" font-size="10.5" fill="{C_KIRMIZI}" font-weight="700">dalga-tanecik ikili doğasını açıklayamaz.</text>',
        # Sağ: Modern Atom
        f'<rect x="348" y="58" width="314" height="176" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Modern Atom Teorisi (Bulut / Orbital)</text>',
        f'<text x="362" y="108" font-size="10.5" fill="{C_KOYU}" font-weight="600">• De Broglie: Elektronlar dalga özelliğine de sahiptir.</text>',
        f'<text x="362" y="130" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Heisenberg Belirsizlik İlkesi: Elektronun konumu</text>',
        f'<text x="372" y="146" font-size="10.5" fill="{C_KOYU}" font-weight="600">ve hızı aynı anda kesin olarak ölçülemez.</text>',
        f'<text x="362" y="170" font-size="10.5" fill="{C_YESIL}" font-weight="700">• Schrödinger: Elektronların bulunma olasılığının</text>',
        f'<text x="372" y="188" font-size="10.5" fill="{C_YESIL}" font-weight="700">yüksek olduğu 3 boyutlu bölgelere ORBİTAL denir.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Atom Altı Temel Tanecikler ve Sembol Gösterimi."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Atomun Yapısı: Proton, Nötron, Elektron ve Element Sembolü Köşeleri</text>',
        # Sol sembol kutusu
        f'<rect x="18" y="58" width="250" height="180" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<text x="143" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="{C_TURUNCU}">İyon/Atom Gösterimi</text>',
        f'<text x="143" y="160" text-anchor="middle" font-size="48" font-weight="800" fill="{C_KOYU}">X</text>',
        f'<text x="95" y="122" text-anchor="end" font-size="13" font-weight="700" fill="{C_KIRMIZI}">A (Kütle No)</text>',
        f'<text x="95" y="188" text-anchor="end" font-size="13" font-weight="700" fill="{C_MAVI}">Z (Atom No)</text>',
        f'<text x="185" y="122" font-size="13" font-weight="700" fill="{C_MOR}">q (İyon Yükü)</text>',
        f'<text x="185" y="188" font-size="13" font-weight="700" fill="{C_YESIL}">e⁻ (Elektron)</text>',
        f'<text x="143" y="222" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">A = Z + n   ve   Z = q + e⁻</text>',
        # Sağ tablo
        f'<rect x="284" y="58" width="380" height="180" rx="10" fill="#fff" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="284" y="58" width="380" height="30" rx="10" fill="{C_MAVI}"/>',
        f'<text x="345" y="78" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Tanecik</text>',
        f'<text x="445" y="78" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Yükü</text>',
        f'<text x="535" y="78" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Bağıl Kütle</text>',
        f'<text x="618" y="78" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Bölgesi</text>',
    ]
    satirlar = [
        ("Proton (p⁺)", "+1", "≈ 1 akb", "Çekirdek", C_KIRMIZI, 114),
        ("Nötron (n⁰)", "0 (Yüksüz)", "≈ 1 akb", "Çekirdek", C_YESIL, 156),
        ("Elektron (e⁻)", "−1", "≈ 1/1836 akb", "Orbital (Bulut)", C_MAVI, 198),
    ]
    for ad, yuk, kutle, bolge, renk, y in satirlar:
        p.append(f'<line x1="292" y1="{y-22}" x2="656" y2="{y-22}" stroke="{C_SINIR}" stroke-width="1"/>')
        p.append(f'<text x="345" y="{y}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{renk}">{ad}</text>')
        p.append(f'<text x="445" y="{y}" text-anchor="middle" font-size="11" font-weight="600" fill="{C_KOYU}">{yuk}</text>')
        p.append(f'<text x="535" y="{y}" text-anchor="middle" font-size="11" font-weight="600" fill="{C_KOYU}">{kutle}</text>')
        p.append(f'<text x="618" y="{y}" text-anchor="middle" font-size="11" font-weight="700" fill="{renk}">{bolge}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Atom Modellerinin Tarihsel Gelişimi ve Bilimsel Bilginin Değişebilirliği."""
    w, h = 680, 235
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Atom Modellerinin Gelişimi ve Bilimsel Bilginin Değişebilir Doğası</text>',
    ]
    modeller = [
        ("Dalton (1803)", "İçi dolu berk küre", "Bölünemez varsayımı", C_GRI, "#f2f4f4", 16),
        ("Thomson (1897)", "Üzümlü kek modeli", "e⁻ ve + yük keşfi", C_TURUNCU, C_ACIK_SARI, 148),
        ("Rutherford (1911)", "Çekirdekli model", "Altın levha deneyi", C_KIRMIZI, C_ACIK_KIRMIZI, 280),
        ("Bohr (1913)", "Yörüngeli model", "Enerji katmanları", C_MAVI, C_ACIK_MAVI, 412),
        ("Modern Teori", "Bulut / Orbital", "Olasılık bölgeleri", C_YESIL, C_ACIK_YESIL, 544),
    ]
    for i, (baslik, s1, s2, renk, bg, x) in enumerate(modeller):
        p.append(f'<rect x="{x}" y="60" width="120" height="156" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="120" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+60}" y="79" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+60}" y="118" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+60}" y="142" text-anchor="middle" font-size="9.5" fill="{C_GRI}">{s2}</text>')
        p.append(f'<circle cx="{x+60}" cy="184" r="14" fill="#fff" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+60}" y="189" text-anchor="middle" font-size="11" font-weight="800" fill="{renk}">{i+1}</text>')
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
