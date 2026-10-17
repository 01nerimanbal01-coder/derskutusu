# -*- coding: utf-8 -*-
"""9. Sınıf Biyoloji — 4. Hafta görsel modülü:
Yaşam — Bilimsel Araştırma Süreçlerinde Bilimin Doğası, Gözlem-Çıkarım, Hipotez, Teori ve Kanun"""

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
    """Bilimin Doğası ve Bilimsel Bilginin Temel Özellikleri."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Bilimin Doğası: Bilimsel Bilginin 6 Temel Özelliği</text>',
    ]
    kartlar = [
        ("1. Deneysel ve Kanıta Dayalı", "Doğal dünyadaki gözlem ve", "deney verilerine dayanır.", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("2. Değişebilir ve Gelişebilir", "Mutlak doğru değildir; yeni", "kanıtlarla güncellenir.", C_YESIL, C_ACIK_YESIL, 236, 58),
        ("3. Öznel ve Yaratıcı Boyut", "Bilim insanının hayal gücü", "ve birikiminden etkilenir.", C_MOR, C_ACIK_MOR, 454, 58),
        ("4. Gözlem ≠ Çıkarım", "Gözlem duyu/araçla toplanan veri,", "çıkarım ise bu verinin yorumudur.", C_TURUNCU, C_ACIK_SARI, 18, 156),
        ("5. Tek Bir Yöntem Yoktur", "Her araştırma aynı basamakları", "birebir izlemek zorunda değildir.", C_KIRMIZI, C_ACIK_KIRMIZI, 236, 156),
        ("6. Sosyokültürel Etkileşim", "Bilim, içinde geliştiği toplumun", "ihtiyaç ve değerleriyle etkileşir.", C_MAVI, C_ACIK_MAVI, 454, 156),
    ]
    for baslik, s1, s2, renk, bg, x, y in kartlar:
        p.append(f'<rect x="{x}" y="{y}" width="208" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="208" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="{y+18}" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="{y+48}" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="{y+68}" text-anchor="middle" font-size="10.5" fill="{renk}" font-weight="700">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Nitel/Nicel Gözlem ve Çıkarım Ayrımı."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Gözlem (Nitel / Nicel) ve Çıkarım Arasındaki Fark</text>',
    ]
    kutular = [
        ("Nitel Gözlem", "Yalnızca beş duyu organıyla", "yapılan, ölçüm aracı içermeyen", "gözlemdir: «Yaprak sararmış.»", C_TURUNCU, C_ACIK_SARI, 18),
        ("Nicel Gözlem", "Ölçü aletleri ve sayılarla", "ifade edilen nesnel gözlemdir:", "«Sıcaklık 37,5 °C ölçüldü.»", C_MAVI, C_ACIK_MAVI, 236),
        ("Çıkarım (Yorum)", "Gözlem verilerinin akıl ve", "ön bilgilerle yorumlanmasıdır:", "«Bitki susuz kaldığı için solmuş.»", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in kutular:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="110" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="130" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<rect x="{x+12}" y="150" width="184" height="62" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="185" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Kontrollü Deney: Bağımsız, Bağımlı ve Kontrol Değişkenleri."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kontrollü Deney Tasarımı ve Değişken Türleri</text>',
    ]
    degiskenler = [
        ("Bağımsız Değişken (Neden)", "Araştırmacının etkisini test", "etmek için bilerek değiştirdiği", "faktör (Örn: Işık rengi)", C_MAVI, C_ACIK_MAVI, 18),
        ("Bağımlı Değişken (Sonuç)", "Bağımsız değişkene bağlı", "olarak değişen ve ölçülen", "sonuç (Örn: Fotosentez hızı)", C_YESIL, C_ACIK_YESIL, 236),
        ("Kontrol (Sabit) Değişkenler", "Deney ve kontrol grubunda", "eşit tutulan tüm şartlar", "(Örn: Su, sıcaklık, toprak)", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in degiskenler:
        p.append(f'<rect x="{x}" y="58" width="208" height="176" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<rect x="{x+14}" y="154" width="180" height="62" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="189" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Teori (Kuram) ve Kanun (Yasa) Karşılaştırması — Bilimsel Yanılgı."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_KIRMIZI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Bilimsel Teori (Kuram) ve Kanun (Yasa): Farklı Bilgi Türleri!</text>',
        f'<rect x="18" y="58" width="290" height="170" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="290" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="163" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Bilimsel Teori (Kuram) — NEDEN / NASIL?</text>',
        f'<text x="163" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Doğa olaylarının neden ve nasıl gerçekleştiğini</text>',
        f'<text x="163" y="126" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">çok yönlü kanıtlarla açıklayan kapsamlı sistemdir.</text>',
        f'<text x="163" y="154" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MAVI}">Örn: Hücre Teorisi, Evrim Teorisi</text>',
        f'<text x="163" y="195" text-anchor="middle" font-size="11" font-weight="800" fill="{C_KIRMIZI}">DİKKAT: Teoriler kanıtlanınca</text>',
        f'<text x="163" y="213" text-anchor="middle" font-size="11" font-weight="800" fill="{C_KIRMIZI}">KANUNA DÖNÜŞMEZ!</text>',
        f'<rect x="372" y="58" width="290" height="170" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="372" y="58" width="290" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="517" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Bilimsel Kanun (Yasa) — NE / NASIL İLİŞKİ?</text>',
        f'<text x="517" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Doğadaki olgular arasındaki düzenliliği genellikle</text>',
        f'<text x="517" y="126" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">matematiksel bağıntılarla betimleyen ifadedir.</text>',
        f'<text x="517" y="154" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_YESIL}">Örn: Mendel Kalıtım Yasaları, Kütleçekim Yasası</text>',
        f'<text x="517" y="195" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">Hem teori hem kanun bilimseldir</text>',
        f'<text x="517" y="213" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">ve yeni kanıtlarla değişebilir.</text>',
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
