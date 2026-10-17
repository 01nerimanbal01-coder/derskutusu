# -*- coding: utf-8 -*-
"""9. Sınıf Arapça — 4. Hafta görsel modülü:
Ünite 1: Haydi Tanışalım — Med Harfleri, Sınıf İçi Yönergeler, Memnuniyet ve Vedalaşma İfadeleri"""

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
    """Arapçada Üç Med (Uzatma) Harfi: Elif (ا), Vav (و) ve Yâ (ي)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Med (Uzatma) Harfleri (حُرُوفُ المَدّ): ا — و — ي</text>',
    ]
    medler = [
        ("Med Harfi: Elif (ا)", "Öncesinde Fetha (Üstün: ـَ) bulunur.", "Harfi «â / a» sesiyle 1 elif uzatır.", "بابٌ (bâbun) — كِتابٌ (kitâbun) — طالِبٌ", C_MAVI, C_ACIK_MAVI, 18),
        ("Med Harfi: Vav (و)", "Öncesinde Damme (Ötre: ـُ) bulunur.", "Harfi «û / u» sesiyle 1 elif uzatır.", "نُورٌ (nûrun) — سُرُورٌ (surûrun) — دُرُوسٌ", C_YESIL, C_ACIK_YESIL, 236),
        ("Med Harfi: Yâ (ي)", "Öncesinde Kesra (Esre: ـِ) bulunur.", "Harfi «î / i» sesiyle 1 elif uzatır.", "كَبِيرٌ (kebîrun) — صَدِيقٌ (sadîkun) — جَمِيلٌ", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, kural, ses, orn, renk, bg, x in medler:
        p.append(f'<rect x="{x}" y="58" width="208" height="176" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="108" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">{kural}</text>')
        p.append(f'<text x="{x+104}" y="130" text-anchor="middle" font-size="10.5" fill="{C_GRI}">{ses}</text>')
        p.append(f'<rect x="{x+12}" y="148" width="184" height="72" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">Örnek Kelimeler:</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="11.5" font-weight="700" fill="{renk}">{orn}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Sınıf İçi Yönergeler / Emir Fiilleri (Eril ve Dişil Hitap)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Sınıf İçi Yönergeler (التَّعْلِيمات الصَّفِّيَّة): Eril ve Dişil Emir Kalıpları</text>',
    ]
    emirler = [
        ("Oku!", "اِقْرَأْ (Erkek)", "اِقْرَئِي (Kız)", "اِقْرَأِ النَّصَّ!", C_MAVI, C_ACIK_MAVI, 16),
        ("Yaz!", "اُكْتُبْ (Erkek)", "اُكْتُبِي (Kız)", "اُكْتُبِ الدَّرْسَ!", C_YESIL, C_ACIK_YESIL, 182),
        ("Dinle!", "اِسْتَمِعْ (Erkek)", "اِسْتَمِعِي (Kız)", "اِسْتَمِعْ إِلى المُعَلِّمِ!", C_MOR, C_ACIK_MOR, 348),
        ("Tekrar Et!", "أَعِدْ (Erkek)", "أَعِيدِي (Kız)", "أَعِدِ الكَلِمَةَ!", C_TURUNCU, C_ACIK_SARI, 514),
    ]
    for tr, eril, disil, orn, renk, bg, x in emirler:
        p.append(f'<rect x="{x}" y="60" width="150" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="79" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{tr}</text>')
        p.append(f'<text x="{x+75}" y="114" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_KOYU}">{eril}</text>')
        p.append(f'<text x="{x+75}" y="142" text-anchor="middle" font-size="12.5" font-weight="700" fill="{renk}">{disil}</text>')
        p.append(f'<rect x="{x+12}" y="164" width="126" height="62" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+75}" y="190" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">{orn}</text>')
        p.append(f'<text x="{x+75}" y="212" text-anchor="middle" font-size="9.5" fill="{C_GRI}">Dişilde sonuna «ـِي» eklenir</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Tanışma Memnuniyet İfadeleri ve Vedalaşma Kalıpları."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Memnuniyet, Teşekkür ve Vedalaşma İfadeleri (عِباراتُ التَّعارُف وَالوَداع)</text>',
        # Sol: Memnuniyet ve Teşekkür
        f'<rect x="18" y="58" width="314" height="182" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Memnuniyet ve Nezaket İfadeleri</text>',
        f'<text x="32" y="108" font-size="12" font-weight="700" fill="{C_KOYU}">• تَشَرَّفْتُ (بِمَعْرِفَتِكَ / بِمَعْرِفَتِكِ)</text>',
        f'<text x="42" y="124" font-size="10.5" fill="{C_GRI}">Tanıştığımıza memnun oldum (şeref duydum).</text>',
        f'<text x="32" y="148" font-size="12" font-weight="700" fill="{C_KOYU}">• فُرْصَةٌ سَعِيدَةٌ  —  وَأَنا أَيْضًا</text>',
        f'<text x="42" y="164" font-size="10.5" fill="{C_GRI}">Memnun oldum (Güzel fırsat) — Ben de öyle!</text>',
        f'<text x="32" y="188" font-size="12" font-weight="700" fill="{C_MOR}">• شُكْرًا (Teşekkürler)  →  عَفْوًا (Rica ederim)</text>',
        f'<text x="32" y="216" font-size="11.5" font-weight="700" fill="{C_KOYU}">• مِنْ فَضْلِكَ / مِنْ فَضْلِكِ (Lütfen)</text>',
        # Sağ: Vedalaşma
        f'<rect x="348" y="58" width="314" height="182" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Vedalaşma İfadeleri (الوَداع)</text>',
        f'<text x="362" y="110" font-size="12.5" font-weight="700" fill="{C_KOYU}">• إِلى اللِّقاءِ (Görüşmek üzere)</text>',
        f'<text x="362" y="142" font-size="12.5" font-weight="700" fill="{C_MAVI}">• مَعَ السَّلامَةِ (Güle güle / Selametle)</text>',
        f'<text x="362" y="174" font-size="12.5" font-weight="700" fill="{C_YESIL}">• في أَمانِ اللّٰهِ (Allah\'a emanet ol)</text>',
        f'<rect x="362" y="192" width="286" height="36" rx="8" fill="#fff" stroke="{C_MAVI}" stroke-width="1.2"/>',
        f'<text x="505" y="215" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MAVI}">Bu üç ifade birbiriyle karşılıklı cevap olarak kullanılır.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Ünite 1 Hadis-i Şerifi ve Veciz Sözü."""
    w, h = 680, 235
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Ünite 1 Hikmetli Sözleri: Selamlaşma ve Güzel Sözün Önemi</text>',
        f'<rect x="18" y="58" width="314" height="160" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Hadis-i Şerif (Sahîh-i Müslim)</text>',
        f'<text x="175" y="118" text-anchor="middle" font-size="15" font-weight="800" fill="{C_KOYU}">«أَفْشُوا السَّلَامَ بَيْنَكُمْ»</text>',
        f'<text x="175" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="{C_TURUNCU}">«Aranızda selamı yayınız!»</text>',
        f'<text x="175" y="182" text-anchor="middle" font-size="10" fill="{C_GRI}">Selamlaşmak sevgi ve kardeşliği güçlendirir.</text>',
        f'<rect x="348" y="58" width="314" height="160" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Hikmetli Veciz Söz</text>',
        f'<text x="505" y="118" text-anchor="middle" font-size="14" font-weight="800" fill="{C_KOYU}">«اَلْكَلِمَةُ الطَّيِّبَةُ مِفْتَاحُ الْقُلُوبِ»</text>',
        f'<text x="505" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="{C_YESIL}">«Güzel söz kalplerin anahtarıdır.»</text>',
        f'<text x="505" y="182" text-anchor="middle" font-size="10" fill="{C_GRI}">اَلْكَلِمَةُ الطَّيِّبَةُ: Güzel söz | مِفْتاح: Anahtar</text>',
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
