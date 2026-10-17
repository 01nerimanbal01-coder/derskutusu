# -*- coding: utf-8 -*-
"""10. Sınıf Felsefe — 4. Hafta görsel modülü:
Felsefenin Diğer Alanlarla (Bilim, Sanat, Din) İlişkisi ve Bireysel-Toplumsal İşlevleri"""

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
    """Felsefe ve Bilim İlişkisi: Benzerlikler ve Farklılıklar."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Felsefe ile Bilim Arasındaki İlişki ve Temel Farklar</text>',
        f'<rect x="18" y="56" width="208" height="186" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="208" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="122" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Felsefe</text>',
        f'<text x="122" y="104" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Varlığı bütüncül inceler.</text>',
        f'<text x="122" y="126" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Akıl ve mantık ilkelerine dayanır.</text>',
        f'<text x="122" y="148" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Özneldir; kesin sonuç yoktur.</text>',
        f'<text x="122" y="170" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Olması gerekeni de sorgular.</text>',
        f'<text x="122" y="192" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MAVI}">• Kümülatiftir (yığılımlı ilerler).</text>',
        f'<rect x="236" y="56" width="208" height="186" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="236" y="56" width="208" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="340" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Ortak Noktalar</text>',
        f'<text x="340" y="106" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">• Merak ve hayretten doğar.</text>',
        f'<text x="340" y="130" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Evreni ve insanı anlamaya çalışır.</text>',
        f'<text x="340" y="154" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Rasyonel (akılcı) ve sistemlidir.</text>',
        f'<text x="340" y="178" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Eleştirel ve sorgulayıcıdır.</text>',
        f'<text x="340" y="202" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">• Dogmatik kalıpları reddeder.</text>',
        f'<rect x="454" y="56" width="208" height="186" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="454" y="56" width="208" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="558" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Bilim</text>',
        f'<text x="558" y="104" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Varlığı parçalara ayırarak inceler.</text>',
        f'<text x="558" y="126" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Deney ve gözleme dayanır.</text>',
        f'<text x="558" y="148" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Nesneldir; genelgeçer yasalar arar.</text>',
        f'<text x="558" y="170" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">• Yalnızca olgusal olanı inceler.</text>',
        f'<text x="558" y="192" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">• Birikimli olarak ilerler, öndeyi sağlar.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Felsefe - Sanat ve Felsefe - Din İlişkisi."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Felsefenin Sanat ve Din Alanlarıyla Etkileşimi</text>',
        f'<rect x="18" y="56" width="314" height="184" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Felsefe ve Sanat İlişkisi (Estetik)</text>',
        f'<text x="175" y="104" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">• Her ikisi de öznel, özgün ve yaratıcıdır.</text>',
        f'<text x="175" y="126" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Felsefe akıl ve kavramlarla hakikati arar;</text>',
        f'<text x="175" y="144" text-anchor="middle" font-size="10.2" fill="{C_GRI}">sanat ise duygu, hayal gücü ve sezgiyle</text>',
        f'<text x="175" y="162" text-anchor="middle" font-size="10.2" fill="{C_GRI}">güzeli (estetik hazzı) somut esere dönüştürür.</text>',
        f'<text x="175" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MOR}">• Sanat felsefesi ile estetik kesişim alanıdır.</text>',
        f'<rect x="348" y="56" width="314" height="184" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Felsefe ve Din İlişkisi</text>',
        f'<text x="505" y="104" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">• Her ikisi de evrenin kaynağını, hayatın</text>',
        f'<text x="505" y="120" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">anlamını ve iyi-kötü davranışları açıklar.</text>',
        f'<text x="505" y="144" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Din vahye ve imana (inanca) dayanır;</text>',
        f'<text x="505" y="162" text-anchor="middle" font-size="10.2" fill="{C_GRI}">felsefe ise serbest akla ve şüpheye dayanır.</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">• Din felsefesi dini kavramları akılla inceler.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Felsefenin Bireysel İşlevleri."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Felsefenin Bireysel İşlevleri (İnsana Kazandırdıkları)</text>',
    ]
    islevler = [
        ("Kendini Tanıma ve Anlam", "'Sorgulanmamış hayat yaşanmaya", "değmez' ilkesiyle bireyin yaşam", "amacını keşfetmesini sağlar.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("Eleştirel ve Bağımsız Düşünme", "Ön yargılardan, dogmalardan ve", "bilgi kirliliğinden kurtularak", "kendi aklıyla karar vermeyi öğretir.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("Çok Yönlü Bakış ve Hoşgörü", "Olaylara tek pencereden değil,", "farklı fikir ve perspektiflerden", "saygıyla bakabilmeyi kazandırır.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("Tutarlılık ve Kavramsal Dil", "Düşüncelerini çelişkiye düşmeden,", "güçlü argümanlarla ve doğru", "kavramlarla ifade etmeyi sağlar.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in islevler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Felsefenin Toplumsal İşlevleri."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Felsefenin Toplumsal İşlevleri (Medeniyete ve Topluma Katkıları)</text>',
    ]
    toplum = [
        ("Demokrasi ve İnsan Hakları", "Özgürlük, eşitlik, adalet ve hukuk", "devleti kavramlarını temellendirerek", "demokratik kültürü inşa eder.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("Bilimlerin Doğuşu ve Gelişimi", "Yeni sorular ve hipotezlerle", "bilimsel devrimlere ve teknolojik", "gelişmelere öncülük eder.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("Ortak Yaşama Kültürü ve Barış", "Farklı inanç ve kültürlerin bir", "arada barış ve hoşgörü içinde", "yaşamasının zeminini kurar.", C_MOR, C_ACIK_MOR, 18, 152),
        ("Toplumsal Değişim ve Etik", "Yapay zekâ, biyoetik ve çevre", "krizleri gibi çağdaş sorunlara", "ahlaki ve hukuki ilkeler üretir.", C_TURUNCU, C_ACIK_SARI, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in toplum:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][3]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
