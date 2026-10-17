# -*- coding: utf-8 -*-
"""9. Sınıf Temel Dini Bilgiler — 4. Hafta görsel modülü:
1. Ünite: Hayatın Anlamı — İlkeli Yaşamak ve Allah (cc), İnsan ve Kâinat İlişkisi"""

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
    """İlkeli Yaşamanın (İstikamet Üzere Olmanın) Dört Temel Boyutu."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İlkeli Yaşamak (İstikamet): İnanç, İbadet ve Ahlak Bütünlüğü</text>',
    ]
    boyutlar = [
        ("1. İnançta İstikamet (Tevhid)", "Şirkten ve hurafelerden uzak", "durarak yalnız Allah'a (cc)", "güvenip bağlanmak", C_MAVI, C_ACIK_MAVI, 16),
        ("2. İbadette Devamlılık (İhlas)", "Gösterişten (riya) uzak,", "samimi ve sürekli kulluk", "(Hûd Suresi, 112)", C_YESIL, C_ACIK_YESIL, 182),
        ("3. Ahlakta Doğruluk (Sıdk)", "Özü ve sözü bir olmak,", "emaneti korumak ve adaletten", "asla ayrılmamak", C_MOR, C_ACIK_MOR, 348),
        ("4. İtidalli Olmak (Denge)", "İfrat (aşırılık) ve tefritten", "(ihmarkârlık) kaçınıp orta", "yolu (vasat) tutmak", C_TURUNCU, C_ACIK_SARI, 514),
    ]
    for baslik, s1, s2, s3, renk, bg, x in boyutlar:
        p.append(f'<rect x="{x}" y="60" width="150" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="79" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+75}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+75}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+75}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+12}" y="182" width="126" height="44" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+75}" y="209" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">İlkeli Hayat</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Allah (cc), İnsan ve Kâinat İlişkisinde Aklî ve Naklî Deliller."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Allah (cc), İnsan ve Kâinat İlişkisinde Aklî ve Naklî Deliller</text>',
        # Sol: Aklî Deliller
        f'<rect x="18" y="58" width="314" height="182" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Aklî Deliller (Kâinat Kitabını Tefekkür)</text>',
        f'<text x="32" y="108" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Gaye ve Nizam Delili (Teleolojik Delil):</text>',
        f'<text x="42" y="124" font-size="10" fill="{C_GRI}">Evrendeki kusursuz ölçü (sünnetullah) ve amaçlılık.</text>',
        f'<text x="32" y="148" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Hudûs ve İmkân Delili (Kozmolojik Delil):</text>',
        f'<text x="42" y="164" font-size="10" fill="{C_GRI}">Sonradan var olan her şeyin bir Yaratıcıya muhtaç olması.</text>',
        f'<text x="32" y="188" font-size="10.5" font-weight="700" fill="{C_MAVI}">• Fıtrat ve Ahlak Delili:</text>',
        f'<text x="42" y="204" font-size="10" fill="{C_GRI}">İnsanın doğuştan inanma ve adalet arayışı.</text>',
        # Sağ: Naklî Deliller
        f'<rect x="348" y="58" width="314" height="182" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Naklî Deliller (Vahiy: Kur\'an ve Sünnet)</text>',
        f'<text x="362" y="108" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Kamer Suresi, 49. Ayet:</text>',
        f'<text x="372" y="124" font-size="10" fill="{C_GRI}">«Şüphesiz biz her şeyi bir ölçüye (kadere) göre yarattık.»</text>',
        f'<text x="362" y="148" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Mülk Suresi, 3–4. Ayetler:</text>',
        f'<text x="372" y="164" font-size="10" fill="{C_GRI}">«Rahmân\'ın yaratışında hiçbir düzensizlik göremezsin.»</text>',
        f'<text x="362" y="188" font-size="10.5" font-weight="700" fill="{C_YESIL}">• Enbiyâ Suresi, 22. Ayet (Temânu\' Delili):</text>',
        f'<text x="372" y="204" font-size="10" fill="{C_GRI}">«Yerde ve gökte Allah\'tan başka ilah olsaydı düzen bozulurdu.»</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """İstikamet İlkesi: İfrat, Tefrit ve Sırat-ı Müstakim (İtidal)."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İlkeli Yaşamda Denge: İfrat ve Tefritten Uzak «Sırat-ı Müstakim»</text>',
        # Sol: Tefrit
        f'<rect x="18" y="58" width="190" height="166" rx="10" fill="{C_ACIK_KIRMIZI}" stroke="{C_KIRMIZI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="190" height="28" rx="10" fill="{C_KIRMIZI}"/>',
        f'<text x="113" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Tefrit (Eksiklik / İhmal)</text>',
        f'<text x="113" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">• Korkaklık, cimrilik,</text>',
        f'<text x="113" y="132" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">tembellik ve duyarsızlık</text>',
        f'<text x="113" y="160" text-anchor="middle" font-size="10.5" fill="{C_KIRMIZI}" font-weight="700">• Sorumlulukları terk etme</text>',
        # Orta: İtidal (Sırat-ı Müstakim)
        f'<rect x="224" y="58" width="232" height="166" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="2"/>',
        f'<rect x="224" y="58" width="232" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="340" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">İtidal / İstikamet (Orta Yol)</text>',
        f'<text x="340" y="110" text-anchor="middle" font-size="11" font-weight="700" fill="{C_YESIL}">الصِّراطَ الْمُسْتَقِيمَ (Fâtiha, 6)</text>',
        f'<text x="340" y="132" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">• Cesaret, cömertlik, hikmet ve</text>',
        f'<text x="340" y="150" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">dünya-ahiret dengesi (Kasas, 77)</text>',
        f'<text x="340" y="182" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_YESIL}">«Emrolunduğun gibi dosdoğru ol!»</text>',
        f'<text x="340" y="200" text-anchor="middle" font-size="10" fill="{C_KOYU}">(Hûd Suresi, 112)</text>',
        # Sağ: İfrat
        f'<rect x="472" y="58" width="190" height="166" rx="10" fill="{C_ACIK_KIRMIZI}" stroke="{C_KIRMIZI}" stroke-width="1.6"/>',
        f'<rect x="472" y="58" width="190" height="28" rx="10" fill="{C_KIRMIZI}"/>',
        f'<text x="567" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">İfrat (Aşırılık / Taşkınlık)</text>',
        f'<text x="567" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">• Saldırganlık, savurganlık</text>',
        f'<text x="567" y="132" text-anchor="middle" font-size="10.5" fill="{C_KOYU}">(israf), kibir ve bağnazlık</text>',
        f'<text x="567" y="160" text-anchor="middle" font-size="10.5" fill="{C_KIRMIZI}" font-weight="700">• Ölçüyü ve sınırı aşma</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """İlkeli Bir Müslümanın Hayat Pusulası."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İlkeli Yaşamın Bireysel ve Toplumsal Meyveleri</text>',
    ]
    meyveler = [
        ("Allah'a Karşı (Ubudiyet)", "İhlas, takva, şükür,", "sabır ve tevekkül bilinciyle", "anlamlı bir ömür sürmek", C_MAVI, C_ACIK_MAVI, 18),
        ("İnsanlara Karşı (Muamelat)", "Kul hakkını gözetmek,", "sözünde durmak, adalet", "ve merhametle davranmak", C_YESIL, C_ACIK_YESIL, 236),
        ("Kâinata Karşı (Emanet)", "Doğayı ve canlıları Allah'ın", "emaneti görüp israftan ve", "bozgunculuktan kaçınmak", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in meyveler:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">Huzurlu Birey ve Toplum</text>')
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
