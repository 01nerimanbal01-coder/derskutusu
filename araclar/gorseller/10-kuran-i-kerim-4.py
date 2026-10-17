# -*- coding: utf-8 -*-
"""10. Sınıf Kur'an-ı Kerim — 4. Hafta görsel modülü:
Kur'an-ı Kerim'den Bir Dua: Tâhâ Suresi 25-28. Ayetleri (Hz. Musa'nın Duası) ve Kur'an Öğretim İlkeleri"""

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
    """Tâhâ Suresi 25-28. Ayetler: Hz. Musa'nın (as) Duası (Rabbişrahlî)."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tâhâ Suresi 25-28. Ayetler: Hz. Musa\'nın (as) Duası (Rabbişrahlî)</text>',
    ]
    ayetler = [
        ("25. قَالَ رَبِّ اشْرَحْ لِي صَدْرِي", "Rabbişrahlî sadrî", "Rabbim! Gönlüme (göğsüme) genişlik / ferahlık ver.", C_YESIL, C_ACIK_YESIL, 18, 56),
        ("26. وَيَسِّرْ لِي أَمْرِي", "Ve yessir lî emrî", "İşimi (görevimi) bana kolaylaştır.", C_MAVI, C_ACIK_MAVI, 348, 56),
        ("27. وَاحْلُلْ عُقْدَةً مِنْ لِسَانِي", "Vahlül ukdeten min lisânî", "Dilimdeki düğümü (tutukluğu) çöz.", C_TURUNCU, C_ACIK_SARI, 18, 158),
        ("28. يَفْقَهُوا قَوْلِي", "Yefkahû kavlî", "Ki sözümü (tebliğimi) iyi anlasınlar.", C_MOR, C_ACIK_MOR, 348, 158),
    ]
    for ar, okunus, meal, renk, bg, x, y in ayetler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="92" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+19}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{ar}</text>')
        p.append(f'<text x="{x+157}" y="{y+48}" text-anchor="middle" font-size="10.8" font-weight="700" fill="{C_KOYU}">Okunuşu: {okunus}</text>')
        p.append(f'<text x="{x+157}" y="{y+72}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{meal}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Hz. Musa'nın Duasının Dört Temel Boyutu ve Mesajı."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tâhâ Suresi 25-28. Ayetlerdeki İsteklerin Psikolojik ve Manevi Analizi</text>',
    ]
    boyutlar = [
        ("1. İnşirah (İç Huzuru)", "Zor bir görev öncesinde", "korku, daralma ve heyecandan", "kurtulup öz güven kazanma.", C_YESIL, C_ACIK_YESIL, 18),
        ("2. Teysîr (Kolaylık)", "Karşılaşılan engellerin", "aşılması ve hayırlı işlerin", "bereketle sonuçlanması.", C_MAVI, C_ACIK_MAVI, 236),
        ("3. Etkili İletişim ve Anlaşılma", "Meramını açık, fasih ve", "ikna edici bir dille anlatıp", "muhatabın gönlüne ulaşma.", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in boyutlar:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="152" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Kur'an Öğretiminde Temel İlkeler (Tashih-i Huruf, Tedricilik, Tertil)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kur\'an-ı Kerim Öğretiminde Gözetilen Temel İlkeler</text>',
    ]
    ilkeler = [
        ("1. Tedrîcîlik (Aşamalı Öğretim)", "Kolaydan zora, basitten karmaşığa", "doğru kademeli bir sıra izlenmesi.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("2. Tashîh-i Hurûf ve Tecvit", "Harflerin mahreç ve sıfatlarına", "uygun, hatasız (tertîl ile) okunması.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("3. Anlama ve Tefekkür", "Okunan ayetlerin meal ve tefsiriyle", "mesajının düşünülüp içselleştirilmesi.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("4. İhlas ve Edep (Ta'zîm)", "Allah\'ın kelamına saygı, abdest", "ve samimi kulluk bilinciyle yaklaşma.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, renk, bg, x, y in ilkeler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+66}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Kur'an Öğretiminde Geleneksel ve Klasik Yöntemler (Fem-i Muhsin, Sema', Arz, المشافهة)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kur\'an Öğretiminde Temel Yöntemler (Fem-i Muhsin ve Müşâfehe Geleneği)</text>',
        f'<rect x="18" y="56" width="208" height="178" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="208" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="122" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">1. Semâ\' (Dinleme)</text>',
        f'<text x="122" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">Öğrencinin, üstadın (Fem-i</text>',
        f'<text x="122" y="124" text-anchor="middle" font-size="10" fill="{C_GRI}">Muhsin\'in) okuyuşunu dikkatle</text>',
        f'<text x="122" y="142" text-anchor="middle" font-size="10" fill="{C_GRI}">dinleyerek harflerin çıkışını</text>',
        f'<text x="122" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{C_MAVI}">ve edasını kavramasıdır.</text>',
        f'<rect x="236" y="56" width="208" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="236" y="56" width="208" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="340" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">2. Arz (Hocaya Okuma)</text>',
        f'<text x="340" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">Öğrencinin hazırladığı dersi</text>',
        f'<text x="340" y="124" text-anchor="middle" font-size="10" fill="{C_GRI}">hocasının huzurunda bizzat</text>',
        f'<text x="340" y="142" text-anchor="middle" font-size="10" fill="{C_GRI}">okuyarak hatalarını düzelttirmesi</text>',
        f'<text x="340" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{C_YESIL}">ve onay almasıdır.</text>',
        f'<rect x="454" y="56" width="208" height="178" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="454" y="56" width="208" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="558" y="75" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">3. Edâ (Müşâfehe / Telakki)</text>',
        f'<text x="558" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">Semâ\' ve Arz\'ın birleşimi:</text>',
        f'<text x="558" y="124" text-anchor="middle" font-size="10" fill="{C_GRI}">Önce hocanın okuması, hemen</text>',
        f'<text x="558" y="142" text-anchor="middle" font-size="10" fill="{C_GRI}">ardından öğrencinin yüz yüze</text>',
        f'<text x="558" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{C_MOR}">tekrar etmesidir (Cibril-Nebi usulü).</text>',
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
    v["bolumler"][3]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
