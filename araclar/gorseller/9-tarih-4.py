# -*- coding: utf-8 -*-
"""9. Sınıf Tarih — 4. Hafta görsel modülü:
1. Ünite: Geçmişin İnşa Sürecinde Tarih — Tarihin Doğası, Kaynak Türleri ve Tarihsel Bilginin Üretim Süreci"""

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
    """Birincil (Ana) Kaynaklar ve İkincil (İkinci Elden) Kaynaklar."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tarihsel Kaynakların Oluştuğu Döneme Göre Sınıflandırılması</text>',
        # Sol: Birincil
        f'<rect x="18" y="58" width="314" height="182" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Birincil (Ana / İlk Elden) Kaynaklar</text>',
        f'<text x="32" y="106" font-size="10.5" font-weight="700" fill="{C_KOYU}">Olayın geçtiği döneme ait özgün kanıtlardır:</text>',
        f'<text x="32" y="128" font-size="10.5" fill="{C_KOYU}">• Kadeş Antlaşması tableti, Orhun Yazıtları</text>',
        f'<text x="32" y="148" font-size="10.5" fill="{C_KOYU}">• Atatürk\'ün Nutuk adlı eseri, dönemin paraları</text>',
        f'<text x="32" y="168" font-size="10.5" fill="{C_KOYU}">• Arkeolojik buluntular, fermanlar ve arşiv belgeleri</text>',
        f'<rect x="32" y="184" width="286" height="42" rx="8" fill="#fff" stroke="{C_MAVI}" stroke-width="1.2"/>',
        f'<text x="175" y="210" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MAVI}">Olayın bizzat tanığı veya o çağın ürünüdür.</text>',
        # Sağ: İkincil
        f'<rect x="348" y="58" width="314" height="182" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">İkincil (İkinci Elden) Kaynaklar</text>',
        f'<text x="362" y="106" font-size="10.5" font-weight="700" fill="{C_KOYU}">Birincil kaynaklara dayanılarak sonradan üretilenler:</text>',
        f'<text x="362" y="128" font-size="10.5" fill="{C_KOYU}">• Halil İnalcık\'ın «Devlet-i Aliyye» kitabı</text>',
        f'<text x="362" y="148" font-size="10.5" fill="{C_KOYU}">• Tarih ders kitapları ve akademik makaleler</text>',
        f'<text x="362" y="168" font-size="10.5" fill="{C_KOYU}">• Ansiklopediler ve tarihsel belgeseller</text>',
        f'<rect x="362" y="184" width="286" height="42" rx="8" fill="#fff" stroke="{C_YESIL}" stroke-width="1.2"/>',
        f'<text x="505" y="210" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_YESIL}">Ana kaynakların incelenip yorumlanmasıyla yazılır.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Malzeme Türüne Göre Tarihsel Kaynaklar (Sözlü, Yazılı, Görsel/İşitsel, Kalıntılar)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Türlerine Göre Tarihsel Kaynaklar</text>',
    ]
    turler = [
        ("Yazılı Kaynaklar", "Kitabeler, fermanlar,", "antlaşmalar, paralar,", "kronikler ve gazeteler", C_MAVI, C_ACIK_MAVI, 16),
        ("Sözlü Kaynaklar", "Destanlar, efsaneler,", "mitler, atasözleri ve", "halk hikâyeleri", C_TURUNCU, C_ACIK_SARI, 182),
        ("Kalıntılar (Arkeolojik)", "Silahlar, kap-kacak,", "mimari yapılar, mezarlar", "ve fosil/iskeletler", C_YESIL, C_ACIK_YESIL, 348),
        ("Görsel / İşitsel / Dijital", "Fotoğraflar, filmler, ses", "kayıtları, haritalar ve", "dijital arşivler", C_MOR, C_ACIK_MOR, 514),
    ]
    for baslik, s1, s2, s3, renk, bg, x in turler:
        p.append(f'<rect x="{x}" y="58" width="150" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="77" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+75}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+75}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+75}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+75}" y="206" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">Tarihsel Kanıt</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Tarihsel Bilginin Üretim Süreci (5T Yöntemi)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tarihsel Bilginin Üretim Aşamaları (5T Yöntemi)</text>',
    ]
    adimlar = [
        ("1. Tarama", "Kaynak Arama", "Konuyla ilgili tüm", "belge ve buluntuları", "toplama", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Tasnif", "Sınıflandırma", "Kaynakları zamana,", "mekâna ve konuya", "göre ayırma", C_YESIL, C_ACIK_YESIL, 148),
        ("3. Tahlil", "Çözümleme", "Eldeki verilerin", "araştırma için yeterli", "olup olmadığını ölçme", C_TURUNCU, C_ACIK_SARI, 280),
        ("4. Tenkit", "Eleştiri (İç/Dış)", "Kaynağın orijinalliğini", "ve yazarın tarafsızlığını", "sorgulama", C_KIRMIZI, C_ACIK_KIRMIZI, 412),
        ("5. Terkip", "Sentez (Yazım)", "Doğrulanmış bilgileri", "birleştirip eseri", "kaleme alma", C_MOR, C_ACIK_MOR, 544),
    ]
    for i, (baslik, alt, s1, s2, s3, renk, bg, x) in enumerate(adimlar):
        p.append(f'<rect x="{x}" y="60" width="120" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="120" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+60}" y="79" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+60}" y="106" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">({alt})</text>')
        p.append(f'<text x="{x+60}" y="132" text-anchor="middle" font-size="10" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+60}" y="150" text-anchor="middle" font-size="10" fill="{C_KOYU}">{s2}</text>')
        p.append(f'<text x="{x+60}" y="168" text-anchor="middle" font-size="10" fill="{C_KOYU}">{s3}</text>')
        p.append(f'<circle cx="{x+60}" cy="212" r="14" fill="#fff" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+60}" y="217" text-anchor="middle" font-size="11" font-weight="800" fill="{renk}">{i+1}T</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Tarihe Yardımcı Bilim Dalları."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tarihçinin Kaynak İncelemesinde Yararlandığı Yardımcı Bilim Dalları</text>',
    ]
    bilimler = [
        ("Arkeoloji", "Kazı Bilimi (Toprak/su altı)", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("Paleografya", "Eski Yazıları Okuma Bilimi", C_YESIL, C_ACIK_YESIL, 236, 58),
        ("Epigrafi", "Anıt ve Kitabeler Bilimi", C_MOR, C_ACIK_MOR, 454, 58),
        ("Nümizmatik", "Eski Paralar (Meskûkât) Bilimi", C_TURUNCU, C_ACIK_SARI, 18, 124),
        ("Diplomatik", "Resmî Belge ve Ferman Bilimi", C_KIRMIZI, C_ACIK_KIRMIZI, 236, 124),
        ("Kronoloji", "Zaman ve Takvim Bilimi", C_MAVI, C_ACIK_MAVI, 454, 124),
        ("Antropoloji / Kimya", "Irk/İskelet ve Karbon-14 Yaşı", C_YESIL, C_ACIK_YESIL, 18, 190),
        ("Filoloji", "Dillerin Tarihi ve Gelişimi", C_MOR, C_ACIK_MOR, 236, 190),
        ("Heraldik / Sigilografya", "Armalar ve Mühürler Bilimi", C_TURUNCU, C_ACIK_SARI, 454, 190),
    ]
    for ad, aciklama, renk, bg, x, y in bilimler:
        p.append(f'<rect x="{x}" y="{y}" width="208" height="54" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+104}" y="{y+21}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{renk}">{ad}</text>')
        p.append(f'<text x="{x+104}" y="{y+40}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{aciklama}</text>')
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
