# -*- coding: utf-8 -*-
"""9. Sınıf İngilizce — 4. Hafta görsel modülü:
Theme 1: School Life — Daily Routines, Simple Present Tense, Adverbs of Frequency & Prepositions of Time"""

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
    """Simple Present Tense (Geniş Zaman): Olumlu, Olumsuz ve Soru Yapıları."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Simple Present Tense (Geniş Zaman): Günlük Rutinler ve Alışkanlıklar</text>',
    ]
    kutular = [
        ("Affirmative (+)", "I / You / We / They + V₁", "He / She / It + V-s/-es/-ies", "She attends club meetings.", C_YESIL, C_ACIK_YESIL, 18),
        ("Negative (−)", "I / You / We / They + don't + V₁", "He / She / It + doesn't + V₁", "He doesn't wake up late.", C_KIRMIZI, C_ACIK_KIRMIZI, 236),
        ("Interrogative (?)", "Do + I/you/we/they + V₁ ?", "Does + he/she/it + V₁ ?", "Does she study regularly?", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, k1, k2, orn, renk, bg, x in kutular:
        p.append(f'<rect x="{x}" y="58" width="208" height="184" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="110" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">{k1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">{k2}</text>')
        p.append(f'<rect x="{x+12}" y="152" width="184" height="74" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="176" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_KOYU}">Example:</text>')
        p.append(f'<text x="{x+104}" y="196" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">«{orn}»</text>')
        p.append(f'<text x="{x+104}" y="214" text-anchor="middle" font-size="9.5" fill="{C_GRI}">Dikkat: doesn\'t / does ile fiil yalındır!</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Adverbs of Frequency (Sıklık Zarfları) Yüzde Skalası ve Cümledeki Yeri."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Adverbs of Frequency (Sıklık Zarfları) — How often do you...?</text>',
    ]
    zarflar = [
        ("100%", "always", "daima", C_YESIL, 18),
        ("85%", "usually", "genellikle", C_MAVI, 126),
        ("70%", "often", "sık sık", C_MOR, 234),
        ("50%", "sometimes", "bazen", C_TURUNCU, 342),
        ("15%", "rarely / seldom", "nadiren", C_KIRMIZI, 450),
        ("0%", "never", "asla (olumlu fiille!)", "#2c3e50", 558),
    ]
    for yuzde, en, tr, renk, x in zarflar:
        p.append(f'<rect x="{x}" y="58" width="104" height="92" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="104" height="24" rx="8" fill="{renk}"/>')
        p.append(f'<text x="{x+52}" y="75" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{yuzde}</text>')
        p.append(f'<text x="{x+52}" y="106" text-anchor="middle" font-size="11" font-weight="800" fill="{renk}">{en}</text>')
        p.append(f'<text x="{x+52}" y="128" text-anchor="middle" font-size="9.5" font-weight="600" fill="{C_KOYU}">{tr}</text>')
    p.append(f'<rect x="18" y="162" width="644" height="78" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.5"/>')
    p.append(f'<text x="340" y="185" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_MOR}">Cümle İçindeki Konum Kuralı (Word Order):</text>')
    p.append(f'<text x="340" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">1) Ana fiilden ÖNCE: «I always revise my lessons.»   |   2) am/is/are\'dan SONRA: «She is never late for school.»</text>')
    p.append(f'<text x="340" y="226" text-anchor="middle" font-size="10.5" font-weight="600" fill="{C_GRI}">Zaman ifadeleri (every day, once a week, twice a month) ise cümlenin SONUNDA yer alır.</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Prepositions of Time: IN, ON, AT Kullanımı."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Prepositions of Time (Zaman Edatları): AT — ON — IN</text>',
    ]
    edatlar = [
        ("AT (Saatler ve Belirli Anlar)", "• at 8 o'clock / at 07:30", "• at noon / at night / at midnight", "• at the weekend / at break time", C_KIRMIZI, C_ACIK_KIRMIZI, 18),
        ("ON (Günler ve Tarihler)", "• on Monday / on Fridays", "• on weekdays (hafta içi günlerde)", "• on May 19th / on my birthday", C_MAVI, C_ACIK_MAVI, 236),
        ("IN (Günün Bölümleri, Aylar, Yıllar)", "• in the morning / afternoon / evening", "• in October / in 2026", "• in autumn / in the 21st century", C_YESIL, C_ACIK_YESIL, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in edatlar:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+16}" y="114" font-size="10.5" font-weight="700" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+16}" y="140" font-size="10.5" font-weight="700" fill="{C_KOYU}">{s2}</text>')
        p.append(f'<text x="{x+16}" y="166" font-size="10.5" font-weight="700" fill="{C_KOYU}">{s3}</text>')
        ipucu = "En dar zaman (Saat)" if x == 18 else ("Gün içeren her ifade" if x == 236 else "Geniş zaman dilimleri")
        p.append(f'<text x="{x+104}" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">({ipucu})</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """School Life Vocabulary & Everyday Expressions (Okul Hayatı Kelimeleri ve İfadeleri)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'School Life Collocations &amp; Idioms (Okul Hayatı Kelime Kalıpları)</text>',
    ]
    kaliplar = [
        ("attend classes / clubs", "derslere / kulüplere katılmak", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("do / revise homework", "ödev yapmak / tekrar yapmak", C_YESIL, C_ACIK_YESIL, 236, 58),
        ("take / pass / fail an exam", "sınava girmek / geçmek / kalmak", C_MOR, C_ACIK_MOR, 454, 58),
        ("hit the books (idiom)", "sıkı ders çalışmaya başlamak", C_TURUNCU, C_ACIK_SARI, 18, 124),
        ("pass with flying colours", "sınavı çok yüksek notla geçmek", C_KIRMIZI, C_ACIK_KIRMIZI, 236, 124),
        ("an eager beaver (idiom)", "çok çalışkan ve hevesli öğrenci", C_MAVI, C_ACIK_MAVI, 454, 124),
        ("obey / follow school rules", "okul kurallarına uymak", C_YESIL, C_ACIK_YESIL, 18, 190),
        ("wear a school uniform", "okul üniforması giymek", C_MOR, C_ACIK_MOR, 236, 190),
        ("take notes in class", "derste not tutmak", C_TURUNCU, C_ACIK_SARI, 454, 190),
    ]
    for en, tr, renk, bg, x, y in kaliplar:
        p.append(f'<rect x="{x}" y="{y}" width="208" height="52" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+104}" y="{y+20}" text-anchor="middle" font-size="11" font-weight="700" fill="{renk}">{en}</text>')
        p.append(f'<text x="{x+104}" y="{y+39}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{tr}</text>')
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
