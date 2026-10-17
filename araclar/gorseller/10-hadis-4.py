# -*- coding: utf-8 -*-
"""10. Sınıf Hadis — 4. Hafta görsel modülü:
1. Hadis İlmine Giriş — Sünnetin Dindeki Yeri ve Bağlayıcılığı, Kur'an-Sünnet Bütünlüğü"""

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
    """Sünnetin Bağlayıcılığını Bildiren Kur'an Ayetleri."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Sünnetin Dindeki Yeri ve Bağlayıcılığının Kur\'anî Delilleri</text>',
    ]
    ayetler = [
        ("1. İtaat Emri (Nisâ, 80)", "'Kim Peygamber'e itaat ederse,", "Allah'a itaat etmiş olur.'", "Resulullah'a itaat farzdır.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("2. Emir ve Yasak Ölçüsü (Haşr, 7)", "'Peygamber size ne verdiyse onu", "alın; neyi yasakladıysa ondan", "sakının (vazgeçin)!'", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("3. En Güzel Örnek (Ahzâb, 21)", "'Andolsun, Allah'ın Resulünde", "sizin için en güzel bir örnek", "(üsve-i hasene) vardır.'", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("4. Beyan Görevi (Nahl, 44)", "'İnsanlara, kendilerine indirileni", "açıklayasın (tebyîn edesin) diye", "sana da bu Kur'an'ı indirdik.'", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in ayetler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Sünnetin Kur'an-ı Kerim Karşısındaki 3 Temel İşlevi (Beyan, Teyit, Teşri)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Sünnetin Kur\'an-ı Kerim Karşısındaki Üç Temel İşlevi</text>',
    ]
    islevler = [
        ("1. Teyit ve Tekit Etme", "Kur'an'daki inanç, ibadet ve", "ahlak hükümlerini pekiştirip", "desteklemesi (Anne-babaya iyilik,", "yalancı şahitlikten kaçınma vb.).", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Beyân (Açıklama / Tefsir)", "Kur'an'da kapalı (mücmel) bırakılan", "emirleri açıklaması ve detaylandırması", "(Namazın rekâtları, zekâtın nisabı,", "haccın menâsiki ve yapılışı).", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Teşrî' (Yeni Hüküm Koyma)", "Kur'an'da açıkça yer almayan", "konularda dini hüküm koyması", "(Yırtıcı hayvan etinin haramlığı,", "fıtır sadakası, nine mirası vb.).", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, s4, renk, bg, x in islevler:
        p.append(f'<rect x="{x}" y="58" width="208" height="174" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="124" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="142" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
        p.append(f'<text x="{x+104}" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s4}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Beyân İşlevinin Alt Türleri: Tafsil, Tahsis ve Takyid."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Sünnetin Kur\'an\'ı Açıklama (Beyân) Yöntemleri</text>',
    ]
    yontemler = [
        ("1. Mücmeli Tafsîl Etme", "Kısa ve öz (mücmel) emirleri", "detaylandırmak: 'Beni nasıl namaz", "kılarken görüyorsanız öyle kılın!'", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Âmmı Tahsîs Etme", "Genel (âmm) bir hükmün kapsamını", "daraltmak ve istisnasını göstermek", "(Ölü hayvanlardan balık istisnası).", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Mutlakı Takyîd Etme", "Kayıtsız/sınırsız (mutlak) geçen", "bir hükmün sınır ve şartını çizmek", "(Vasiyetin malın 1/3'ü ile sınırı).", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in yontemler:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="152" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Hz. Peygamber'in (sav) Tasarruflarının Bağlayıcılık Derecesi."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hz. Peygamber\'in (sav) Fiil ve Uygulamalarının Bağlayıcılık Sınıflandırması</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Dini Nitelikli (Teşrîî) Sünnet</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">• Peygamberlik (risalet) görevi gereği</text>',
        f'<text x="175" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">yaptığı tebliğ, ibadet, helal-haram ve</text>',
        f'<text x="175" y="142" text-anchor="middle" font-size="10.2" fill="{C_GRI}">ahlak açıklamalarıdır.</text>',
        f'<text x="175" y="168" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">• Bütün Müslümanlar için kıyamete kadar</text>',
        f'<text x="175" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">hukuken ve dinen BAĞLAYICIDIR!</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">İnsani / Tecrübi (Cibillî) Fiiller ve Hasâis</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">• Bir insan olarak yeme-içme, giyinme örfü,</text>',
        f'<text x="505" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">tarım ve savaş taktiği gibi dünyevi tecrübe</text>',
        f'<text x="505" y="142" text-anchor="middle" font-size="10.2" fill="{C_GRI}">konuları farz/vacip anlamında bağlayıcı değildir.</text>',
        f'<text x="505" y="168" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">• Sadece O\'na özgü hükümlere (Hasâis-i Nebî:</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">visal orucu, teheccüdün farz oluşu) uyulmaz.</text>',
    ]
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
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
