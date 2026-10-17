# -*- coding: utf-8 -*-
"""8. Sınıf Temel Dini Bilgiler — 4. Hafta görsel modülü:
1. Ünite: İslam ve Ahlak — Peygamberimize (sav) Karşı Ahlaki Sorumluluklarımız"""

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
    """Peygamberimize (sav) Karşı Beş Temel Sorumluluğumuz."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Peygamberimiz Hz. Muhammed\'e (sav) Karşı Temel Görev ve Sorumluluklarımız</text>',
    ]
    kartlar = [
        ("1. İman ve Tasdik", "Onun Allah'ın kulu", "ve son elçisi olduğuna", "gönülden inanmak", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Sevgi ve Saygı", "Onu herkesten çok", "sevmek ve hatırasına", "hürmet göstermek", C_KIRMIZI, C_ACIK_KIRMIZI, 148),
        ("3. İtaat ve Bağlılık", "Getirdiği emir ve", "yasaklara samimiyetle", "uymak (Nisâ, 80)", C_YESIL, C_ACIK_YESIL, 280),
        ("4. Üsve-i Hasene", "Güzel ahlakını ve", "Sünnetini hayat", "rehberi edinmek", C_TURUNCU, C_ACIK_SARI, 412),
        ("5. Salât ve Selâm", "Adı anıldığında", "salavat getirerek", "dua etmek (Ahzâb, 56)", C_MOR, C_ACIK_MOR, 544),
    ]
    for baslik, s1, s2, s3, renk, bg, x in kartlar:
        p.append(f'<rect x="{x}" y="60" width="120" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="120" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+60}" y="79" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+60}" y="116" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+60}" y="136" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+60}" y="156" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+10}" y="182" width="100" height="44" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        alt = "Kelime-i Şehâdet" if x == 16 else ("Muhabbet" if x == 148 else ("İttibâ" if x == 280 else ("Örnek Alma" if x == 412 else "Salavat-ı Şerife")))
        p.append(f'<text x="{x+60}" y="209" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{alt}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Allah Sevgisi ile Peygamberimize İtaat Arasındaki Bağ (Âl-i İmrân, 31 & Nisâ, 80)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Allah\'ı (cc) Sevmenin Ölçüsü: Peygamberimize (sav) İtaat ve İttibâ</text>',
    ]
    kutular = [
        ("Allah'ı (cc) Sevmek", "«De ki: Eğer Allah'ı", "seviyorsanız...»", "(Âl-i İmrân Suresi, 31)", C_MAVI, C_ACIK_MAVI, 20),
        ("Peygambere Uymak (İttibâ)", "«...bana uyun ki ({ar:فَاتَّبِعُونِي})»", "Sünneti ve ahlakı", "yaşayarak göstermek", C_YESIL, C_ACIK_YESIL, 240),
        ("İlahi Sevgi ve Mağfiret", "«...Allah da sizi sevsin ve", "günahlarınızı bağışlasın.»", "(En büyük mükâfat)", C_MOR, C_ACIK_MOR, 460),
    ]
    for i, (baslik, s1, s2, s3, renk, bg, x) in enumerate(kutular):
        p.append(f'<rect x="{x}" y="60" width="200" height="168" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="200" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+100}" y="80" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+100}" y="118" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="700">{s1}</text>')
        p.append(f'<text x="{x+100}" y="140" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+100}" y="168" text-anchor="middle" font-size="10.5" fill="{renk}" font-weight="700">{s3}</text>')
        if i < 2:
            p.append(f'<text x="{x+210}" y="145" text-anchor="middle" font-size="20" font-weight="800" fill="{C_GRI}">→</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Üsve-i Hasene (En Güzel Örnek) Olarak Peygamberimizin Ahlakı."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Üsve-i Hasene (أُسْوَةٌ حَسَنَةٌ): Sünneti Yaşamak ve Ahlakını Örnek Almak</text>',
        f'<rect x="16" y="58" width="648" height="44" rx="8" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.4"/>',
        f'<text x="340" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="{C_YESIL}">«Onun ahlakı Kur\'an idi.» (Hz. Âişe [ra]) — Ahzâb Suresi, 21 ve Kalem Suresi, 4</text>',
        f'<text x="340" y="94" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Peygamberimizi sevmek, onun doğruluk, merhamet, adalet ve nezaketini kendi hayatımıza taşımaktır.</text>',
    ]
    alanlar = [
        ("İbadet Hayatı", "Namazı, duayı ve", "zikri onun öğrettiği", "gibi huşuyla kılmak", C_MAVI, C_ACIK_MAVI, 18),
        ("Aile ve Komşuluk", "Aile bireylerine şefkatli,", "komşulara ve büyüklere", "saygılı davranmak", C_MOR, C_ACIK_MOR, 180),
        ("Doğruluk (El-Emîn)", "Sözünde durmak,", "emaneti korumak ve", "asla yalan söylememek", C_TURUNCU, C_ACIK_SARI, 342),
        ("Merhamet ve Adalet", "Yetimi, mazlumu ve", "tüm canlıları koruyup", "hakkaniyetli olmak", C_KIRMIZI, C_ACIK_KIRMIZI, 504),
    ]
    for baslik, s1, s2, s3, renk, bg, x in alanlar:
        p.append(f'<rect x="{x}" y="114" width="156" height="120" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<rect x="{x}" y="114" width="156" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+78}" y="132" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+78}" y="160" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+78}" y="178" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+78}" y="196" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Salât ve Selâm (Salavat-ı Şerife) Kültürümüz."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Salât ve Selâm (Salavat-ı Şerife): Peygamberimize (sav) Dua ve Vefa</text>',
        # Üst ayet kutusu
        f'<rect x="18" y="56" width="644" height="54" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.5"/>',
        f'<text x="340" y="76" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_TURUNCU}">Ahzâb Suresi, 56. Ayet: «Şüphesiz Allah ve melekleri Peygamber\'e salât ederler.»</text>',
        f'<text x="340" y="96" text-anchor="middle" font-size="11" fill="{C_KOYU}">«Ey iman edenler! Siz de ona salât edin ve tam bir teslimiyetle selâm verin.»</text>',
        # Sol ve sağ salavat örnekleri
        f'<rect x="18" y="122" width="314" height="106" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.5"/>',
        f'<rect x="18" y="122" width="314" height="26" rx="10" fill="{C_MOR}"/>',
        f'<text x="175" y="140" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Kısa Salavat İfadeleri</text>',
        f'<text x="175" y="168" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_KOYU}">صَلَّى اللّٰهُ عَلَيْهِ وَسَلَّمَ (sav)</text>',
        f'<text x="175" y="190" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_MOR}">اللّٰهُمَّ صَلِّ عَلى سَيِّدِنا مُحَمَّدٍ</text>',
        f'<text x="175" y="212" text-anchor="middle" font-size="10.5" fill="{C_GRI}">«Allah\'ım! Efendimiz Muhammed\'e rahmet ve selâm eyle.»</text>',
        f'<rect x="348" y="122" width="314" height="106" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.5"/>',
        f'<rect x="348" y="122" width="314" height="26" rx="10" fill="{C_MAVI}"/>',
        f'<text x="505" y="140" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Kültürümüzde Peygamber Sevgisi</text>',
        f'<text x="505" y="168" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">• Namazlarda Salli-Bârik dualarını okumak</text>',
        f'<text x="505" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">• Mevlid, Naat, Hilye-i Şerif ve Kırk Hadis geleneği</text>',
        f'<text x="505" y="212" text-anchor="middle" font-size="11" font-weight="700" fill="{C_MAVI}">• Çocuklara Muhammed, Ahmet, Mustafa adı vermek</text>',
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
