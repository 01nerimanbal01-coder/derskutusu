# -*- coding: utf-8 -*-
"""9. Sınıf Türk Dili ve Edebiyatı — 4. Hafta görsel modülü:
1. Tema: Sözün İnceliği — Edebî Söyleyişin İnceliği ve Okuduğu Şiiri Betimleme Paragrafına Dönüştürme"""

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
    """Yazma Sürecini Yönetme Aşamaları (Planlama, Taslak Oluşturma, Düzenleme, Paylaşma)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Edebî Yazma Sürecinin Yönetimi: Dört Temel Aşama</text>',
    ]
    asamalar = [
        ("1. Hazırlık ve Seçim", "Yazma amacını, hedef", "kitleyi, türü ve dil", "işlevini belirleme", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Planlama ve Taslak", "Ana duygu/düşünceyi,", "imgeleri ve duyusal", "ögeleri yapılandırma", C_YESIL, C_ACIK_YESIL, 182),
        ("3. Metinleştirme", "Zengin söz varlığı ve", "betimleyici anlatımla", "paragrafı yazma", C_TURUNCU, C_ACIK_SARI, 348),
        ("4. Gözden Geçirme", "Akıcılık, bağdaşıklık,", "yazım ve noktalama", "denetimi ve sunum", C_MOR, C_ACIK_MOR, 514),
    ]
    for i, (baslik, s1, s2, s3, renk, bg, x) in enumerate(asamalar):
        p.append(f'<rect x="{x}" y="60" width="150" height="178" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="79" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+75}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+75}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+75}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<circle cx="{x+75}" cy="204" r="15" fill="#fff" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+75}" y="209" text-anchor="middle" font-size="11.5" font-weight="800" fill="{renk}">{i+1}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Okunan Şiiri Betimleyici Paragrafa Dönüştürme Modeli."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Şiirden Betimleme Paragrafına Dönüşüm Köprüsü</text>',
        # Sol: Şiir
        f'<rect x="18" y="58" width="200" height="180" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="200" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="118" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">1. Kaynak: Şiir Metni</text>',
        f'<text x="118" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Dizeler ve ahenk unsurları</text>',
        f'<text x="118" y="130" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• İmgeler ve söz sanatları</text>',
        f'<text x="118" y="152" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Temel duygu (tema)</text>',
        f'<text x="118" y="174" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Mekân, zaman ve varlıklar</text>',
        f'<text x="118" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MOR}">Nazım (Manzum) Biçim</text>',
        # Orta: Dönüşüm
        f'<rect x="240" y="58" width="200" height="180" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="240" y="58" width="200" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">2. Çözümleme ve Kurgu</text>',
        f'<text x="340" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Şiirdeki sahneyi zihinde</text>',
        f'<text x="340" y="124" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">canlandırma (Görselleştirme)</text>',
        f'<text x="340" y="148" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Beş duyuya ait ayrıntıları</text>',
        f'<text x="340" y="164" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">(renk, ses, koku, doku) seçme</text>',
        f'<text x="340" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_TURUNCU}">Sözcüklerle Resim Çizme</text>',
        # Sağ: Betimleme Paragrafı
        f'<rect x="462" y="58" width="200" height="180" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="462" y="58" width="200" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="562" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">3. Ürün: Betimleme Paragrafı</text>',
        f'<text x="562" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Niteleme sıfatları ve zarflar</text>',
        f'<text x="562" y="130" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Sanatsal (izlenimsel) tasvir</text>',
        f'<text x="562" y="152" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Ana duyguyu koruyan üslup</text>',
        f'<text x="562" y="174" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">• Akıcı düzyazı bütünlüğü</text>',
        f'<text x="562" y="214" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_YESIL}">Nesir (Düzyazı) Biçim</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Betimleyici Anlatım Türleri: İzlenimsel (Sanatsal) ve Açıklayıcı (Bilgi Verici) Betimleme."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Betimleyici (Tasvir Edici) Anlatımın İki Temel Türü</text>',
        # Sol: Sanatsal
        f'<rect x="18" y="58" width="314" height="172" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">İzlenimsel (Sanatsal / Edebî) Betimleme</text>',
        f'<text x="32" y="106" font-size="10.5" fill="{C_KOYU}">• Okurda estetik heyecan ve izlenim uyandırır.</text>',
        f'<text x="32" y="126" font-size="10.5" fill="{C_KOYU}">• Öznel algılar, mecazlar ve imgeler ön plandadır.</text>',
        f'<text x="32" y="146" font-size="10.5" fill="{C_KOYU}">• Dil «sanatsal (şiirsel) işlevde» kullanılır.</text>',
        f'<text x="32" y="166" font-size="10.5" fill="{C_KOYU}">• Şiiri betimleme paragrafına dönüştürürken</text>',
        f'<text x="42" y="182" font-size="10.5" font-weight="700" fill="{C_MOR}">kullanacağımız asıl betimleme türüdür!</text>',
        # Sağ: Açıklayıcı
        f'<rect x="348" y="58" width="314" height="172" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Açıklayıcı (Bilgi Verici) Betimleme</text>',
        f'<text x="362" y="106" font-size="10.5" fill="{C_KOYU}">• Varlığı veya mekânı olduğu gibi tanıtır.</text>',
        f'<text x="362" y="126" font-size="10.5" fill="{C_KOYU}">• Nesnel gözlemler ve gerçek anlamlı sözcükler vardır.</text>',
        f'<text x="362" y="146" font-size="10.5" fill="{C_KOYU}">• Dil «göndergesel (bilgi verme) işlevde» kullanılır.</text>',
        f'<text x="362" y="166" font-size="10.5" fill="{C_KOYU}">• Gezi rehberleri, coğrafya metinleri ve</text>',
        f'<text x="372" y="182" font-size="10.5" font-weight="700" fill="{C_MAVI}">teknik tanıtım yazılarında tercih edilir.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Portre Türleri (Fiziksel ve Ruhsal Portre) ve Duyusal Ayrıntılar."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Betimlemede Beş Duyu ve İnsan Tasviri (Portre)</text>',
    ]
    kutular = [
        ("Beş Duyu Ayrıntıları", "Görme (renk, ışık), İşitme", "(uğultu, fısıltı), Koklama,", "Dokunma (serinlik) ve Tatma", C_MAVI, C_ACIK_MAVI, 18),
        ("Fiziksel (Dış) Portre", "Kişinin boyu, yüz hatları,", "bakışları, giyimi ve fiziksel", "görünüşünün betimlenmesi", C_YESIL, C_ACIK_YESIL, 236),
        ("Ruhsal (İç / Tinsel) Portre", "Kişinin karakteri, iç dünyası,", "duyguları, alışkanlıkları ve", "mizacının betimlenmesi", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in kutular:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">Sözün İnceliği</text>')
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
