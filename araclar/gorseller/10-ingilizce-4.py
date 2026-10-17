# -*- coding: utf-8 -*-
"""10. Sınıf İngilizce — 4. Hafta görsel modülü:
Theme 1: School Life — Adverbs of Frequency, Simple Present vs. Present Continuous, Everyday Expressions"""

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
    """Adverbs of Frequency (Sıklık Zarfları) ve Cümledeki Yeri."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Adverbs of Frequency (Sıklık Zarfları: How often...?)</text>',
    ]
    zarflar = [
        ("100%  always (daima)", "I always get up at 7:00 a.m.", C_YESIL, C_ACIK_YESIL, 56),
        ("85%   usually (genellikle)", "She usually walks to school.", C_MAVI, C_ACIK_MAVI, 92),
        ("70%   often (sık sık)", "We often study in the library.", C_MOR, C_ACIK_MOR, 128),
        ("50%   sometimes (bazen)", "They sometimes play chess.", C_TURUNCU, C_ACIK_SARI, 164),
        ("10%   seldom / rarely (nadiren)  |  0% never (asla)", "He is never late for class.", C_KIRMIZI, C_ACIK_KIRMIZI, 200),
    ]
    for sol, sag, renk, bg, y in zarflar:
        p.append(f'<rect x="20" y="{y}" width="640" height="30" rx="7" fill="{bg}" stroke="{renk}" stroke-width="1.4"/>')
        p.append(f'<text x="34" y="{y+20}" font-size="11" font-weight="700" fill="{renk}">{sol}</text>')
        p.append(f'<text x="646" y="{y+20}" text-anchor="end" font-size="11" font-weight="600" fill="{C_KOYU}">{sag}</text>')
    p.append(f'<text x="340" y="248" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_MAVI}">Kural: Asıl fiilden ÖNCE (I always study), am/is/are yardımcı fiilinden SONRA (He is always punctual) gelir!</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Simple Present Tense vs. Present Continuous Tense Karşılaştırması."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Simple Present (Geniş Zaman) vs. Present Continuous (Şimdiki Zaman)</text>',
        f'<rect x="18" y="56" width="314" height="184" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Simple Present Tense (Geniş Zaman)</text>',
        f'<text x="175" y="102" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">Yapı: V₁ / V-s  |  don\'t / doesn\'t + V₁</text>',
        f'<text x="175" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Günlük rutinler, alışkanlıklar, ders programı.</text>',
        f'<text x="175" y="144" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Zaman zarfları: every day, on Mondays,</text>',
        f'<text x="175" y="160" text-anchor="middle" font-size="10.2" fill="{C_GRI}">at weekends, once a week, always, usually.</text>',
        f'<text x="175" y="184" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MAVI}">Örn: I wear a uniform every weekday.</text>',
        f'<rect x="348" y="56" width="314" height="184" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Present Continuous (Şimdiki Zaman)</text>',
        f'<text x="505" y="102" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">Yapı: am / is / are + V-ing</text>',
        f'<text x="505" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Konuşma anında devam eden ve geçici eylemler.</text>',
        f'<text x="505" y="144" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Zaman zarfları: now, right now, at the moment,</text>',
        f'<text x="505" y="160" text-anchor="middle" font-size="10.2" fill="{C_GRI}">at present, today, these days, Look!, Listen!</text>',
        f'<text x="505" y="184" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">Örn: We are studying for the exam right now.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Stative Verbs (Durum Fiilleri) ve Sevilen/Sevilmeyen Aktiviteler (Likes & Dislikes)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Stative Verbs (Durum Fiilleri) ve Likes / Dislikes Kalıpları (+ V-ing)</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Stative Verbs (-ing Almayan Fiiller)</text>',
        f'<text x="175" y="104" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">Duygu, düşünce ve sahiplik bildiren</text>',
        f'<text x="175" y="120" text-anchor="middle" font-size="10" fill="{C_GRI}">fiiller Present Continuous\'ta kullanılmaz:</text>',
        f'<text x="175" y="144" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">know, understand, believe, remember,</text>',
        f'<text x="175" y="162" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">want, need, like, love, hate, belong</text>',
        f'<text x="175" y="186" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KIRMIZI}">Doğru: I understand now. (NOT understanding)</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Expressing Likes, Dislikes &amp; Interests</text>',
        f'<text x="505" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="{C_YESIL}">(+) love / enjoy / like / be keen on + V-ing</text>',
        f'<text x="505" y="124" text-anchor="middle" font-size="10" font-weight="700" fill="{C_MAVI}">(+) be interested in / be good at + V-ing</text>',
        f'<text x="505" y="144" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KIRMIZI}">(-) dislike / hate / can\'t stand + V-ing</text>',
        f'<text x="505" y="168" text-anchor="middle" font-size="10" fill="{C_KOYU}">Örn: I am keen on playing basketball,</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10" fill="{C_KOYU}">but I can\'t stand waking up early.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Okul Hayatında Deyimler (Idioms) ve Kendini Tanıtma Paragrafı."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'School Life Idioms &amp; Everyday Expressions (Okul Deyimleri)</text>',
    ]
    deyimler = [
        ("eager beaver", "Çok hevesli ve çalışkan", "öğrenci ('inek/gayretli').", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("hit the books", "Sıkı ders çalışmaya", "başlamak (kitaplara gömülmek).", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("pass with flying colours", "Bir sınavı çok yüksek", "notla, üstün başarıyla geçmek.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("learn by heart / over the moon", "Ezberlemek (learn by heart) /", "Çok mutlu olmak (over the moon).", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, renk, bg, x, y in deyimler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+66}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
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
