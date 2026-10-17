# -*- coding: utf-8 -*-
"""8. Sınıf Kur'an-ı Kerim — 4. Hafta görsel modülü:
1. Ünite: Kur'an-ı Kerim'i Tanıyalım — Hz. Yakup (as) ve Hz. Yusuf (as) Kıssaları"""

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
    """Kur'an Kıssalarının Amacı ve 'Ahsenü'l-Kasas' (Yusuf Suresi)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kur\'an Kıssalarının Amacı ve Ahsenü\'l-Kasas (Kıssaların En Güzeli)</text>',
        # Merkez üst kutu
        f'<rect x="140" y="56" width="400" height="52" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.8"/>',
        f'<text x="340" y="77" text-anchor="middle" font-size="13" font-weight="700" fill="{C_MAVI}">أَحْسَنُ الْقَصَصِ — Kıssaların En Güzeli (Yûsuf Suresi, 3. Ayet)</text>',
        f'<text x="340" y="97" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">Hz. Yakup (as) ve Hz. Yusuf\'un (as) kıssası Kur\'an\'da baştan sona tek surede anlatılır.</text>',
    ]
    kutular = [
        ("İbret ve Öğüt (عِبْرَة)", "Geçmiş toplumların ve peygamberlerin", "hayatından ders çıkarmak", C_YESIL, C_ACIK_YESIL, 18),
        ("Tevhid ve Teslimiyet", "Zorluklar karşısında yalnızca", "Allah'a (cc) güvenip dayanmak", C_MOR, C_ACIK_MOR, 180),
        ("Sabır ve İffet", "Sıkıntılara sabr-ı cemîl ile", "direnmek ve ahlakı korumak", C_TURUNCU, C_ACIK_SARI, 342),
        ("Affedicilik ve Merhamet", "Kötülüğe iyilikle karşılık verip", "kardeşliği yeniden kurmak", C_KIRMIZI, C_ACIK_KIRMIZI, 504),
    ]
    for baslik, s1, s2, renk, bg, x in kutular:
        p.append(f'<rect x="{x}" y="124" width="156" height="110" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<rect x="{x}" y="124" width="156" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+78}" y="143" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+78}" y="176" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+78}" y="194" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+78}" y="220" text-anchor="middle" font-size="10" fill="{renk}" font-weight="700">Kur\'anî Mesaj</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Hz. Yakup (as): Şefkat, Sabr-ı Cemîl ve Hikmetli Öğütler."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hz. Yakup (as) Kıssası: Peygamber Soyu, Sabr-ı Cemîl ve Allah\'tan Ümit Kesmeme</text>',
    ]
    ozellikler = [
        ("Soyu ve Lakabı", "Hz. İbrahim'in (as) torunu,", "Hz. İshak'ın (as) oğludur.", "Lakabı: İsrâîl (Allah'ın kulu)", C_MAVI, C_ACIK_MAVI, 18),
        ("Sabr-ı Cemîl (صَبْرٌ جَمِيلٌ)", "Şikâyet ve isyan etmeden,", "yalnızca Allah'a sığınarak", "gösterilen güzel sabır.", C_YESIL, C_ACIK_YESIL, 236),
        ("Ümit ve Tevekkül", "«Allah'ın rahmetinden ümit", "kesmeyin!» (Yûsuf, 87) diyerek", "evlatlarına umut aşılamıştır.", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in ozellikler:
        p.append(f'<rect x="{x}" y="58" width="208" height="176" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<rect x="{x+14}" y="156" width="180" height="62" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="191" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Hz. Yusuf'un (as) Hayat Yolculuğu: Kuyudan Mısır Hazine Bakanlığına."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hz. Yusuf\'un (as) İmtihan ve Başarı Yolculuğu (Yûsuf Suresi)</text>',
    ]
    adimlar = [
        ("1. Rüya", "11 yıldız, Güneş", "ve Ay'ın secde", "etmesi (Yûsuf, 4)", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Kuyu İmtihanı", "Kardeşlerinin", "kıskançlığı ve", "kuyuya atılması", C_KIRMIZI, C_ACIK_KIRMIZI, 148),
        ("3. Mısır ve İffet", "İftiraya karşı", "iffetini koruyup", "zindana girmesi", C_TURUNCU, C_ACIK_SARI, 280),
        ("4. İlim ve Yönetim", "Kralın rüyasını", "yorumlayıp Mısır", "veziri olması", C_YESIL, C_ACIK_YESIL, 412),
        ("5. Büyük Affediş", "Kardeşlerini", "affedip ailesine", "kavuşması", C_MOR, C_ACIK_MOR, 544),
    ]
    for i, (baslik, s1, s2, s3, renk, bg, x) in enumerate(adimlar):
        p.append(f'<rect x="{x}" y="62" width="120" height="178" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="62" width="120" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+60}" y="81" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+60}" y="118" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+60}" y="138" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+60}" y="158" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<circle cx="{x+60}" cy="206" r="16" fill="#fff" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+60}" y="211" text-anchor="middle" font-size="12" font-weight="800" fill="{renk}">{i+1}</text>')
        if i < 4:
            p.append(f'<text x="{x+126}" y="150" text-anchor="middle" font-size="16" font-weight="800" fill="{C_GRI}">→</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Hz. Yakup ve Hz. Yusuf Kıssalarından Çıkarılacak İlkeler."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kıssadan Hisse: Hayatımıza Yansıyan Ahlaki İlkeler</text>',
    ]
    ilkeler = [
        ("Hasetten Sakınmak", "Kıskançlık kardeşliği zedeler;", "sevgi ve adalet aileyi korur.", C_KIRMIZI, C_ACIK_KIRMIZI, 18, 56),
        ("İffet ve Dürüstlük", "Günaha davet karşısında", "«Allah'a sığınırım (مَعاذَ اللّٰهِ)» demek.", C_MAVI, C_ACIK_MAVI, 348, 56),
        ("Planlılık ve Emanet", "Bolluk yıllarında tasarruf edip", "kıtlık yıllarına hazırlık yapmak.", C_YESIL, C_ACIK_YESIL, 18, 148),
        ("Koşulsuz Affedicilik", "«Bugün size kınama yoktur!»", "(Yûsuf, 92) diyerek bağışlamak.", C_MOR, C_ACIK_MOR, 348, 148),
    ]
    for baslik, s1, s2, renk, bg, x, y in ilkeler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="80" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+65}" text-anchor="middle" font-size="11" fill="{renk}" font-weight="700">{s2}</text>')
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
