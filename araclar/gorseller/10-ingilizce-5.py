# -*- coding: utf-8 -*-
"""10. Sınıf İngilizce — 5. Hafta Görselleri
Konu: Theme 1: School Life — School Rules, Obligations (Must / Have to) and Future Plans in School Clubs
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#2563eb", arka="#eff6ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Obligation and Prohibition at School: Must / Have to vs Mustn't / Don't have to."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "School Rules &amp; Obligations: Must / Have to / Mustn't / Don't Have to", "#2563eb", "#eff6ff")

    kutular = [
        ("1. MUST + V1", "Internal Obligation / Strong Rule", "We must respect our teachers", "and classmates.", "(İçsel sorumluluk / Güçlü kural)", "#1d4ed8", "#dbeafe"),
        ("2. HAVE TO / HAS TO + V1", "External Rule / Law / Authority", "Students have to wear school", "uniforms at this high school.", "(Dış kaynaklı okul kuralı)", "#0d9488", "#ccfbf1"),
        ("3. MUSTN'T + V1", "Prohibition (Yasak!)", "You mustn't use mobile phones", "during the exam!", "(Yapılması kesinlikle yasak)", "#dc2626", "#fee2e2"),
        ("4. DON'T / DOESN'T HAVE TO", "Lack of Necessity (Zorunlu Değil)", "We don't have to go to school", "on Saturdays.", "(Gerek yok, istersek yaparız)", "#16a34a", "#dcfce7"),
    ]
    for i, (bas, alt, ex1, ex2, tr, r, bg) in enumerate(kutular):
        x = 28 + (i % 2) * 358
        y = 55 + (i // 2) * 122
        s += f'<rect x="{x}" y="{y}" width="344" height="110" rx="10" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="{y}" width="344" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+172}" y="{y+18}" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas} — {alt}</text>'
        s += f'<text x="{x+172}" y="{y+48}" text-anchor="middle" fill="#1e293b" font-size="10.5" font-weight="700">&quot;{ex1}</text>'
        s += f'<text x="{x+172}" y="{y+64}" text-anchor="middle" fill="#1e293b" font-size="10.5" font-weight="700">{ex2}&quot;</text>'
        s += f'<text x="{x+172}" y="{y+90}" text-anchor="middle" fill="{r}" font-size="10">{tr}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Expressing Future Plans & Decisions in School Projects: Be Going To vs Will vs Present Continuous."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Future Plans in School Life: Be Going To vs. Will vs. Present Continuous", "#7c3aed", "#f5f3ff")

    yapilar = [
        ("BE GOING TO + V1", "Prior Plans &amp; Intentions", "(Önceden Planlanmış Niyetler)", "&quot;Our science club is going to", "organize a robotics fair", "next month.&quot;", "#7c3aed", "#f5f3ff"),
        ("WILL + V1", "Spontaneous Decisions &amp; Promises", "(Konuşma Anı Kararları / Tahmin)", "&quot;Your project bag looks heavy;", "I will help you carry it to", "the laboratory!&quot;", "#0284c7", "#f0f9ff"),
        ("PRESENT CONTINUOUS", "Fixed Arrangements (Time/Place)", "(Kesinleşmiş Randevu / Program)", "&quot;We are meeting the exchange", "students in the conference", "hall at 2 p.m. tomorrow.&quot;", "#059669", "#ecfdf5"),
    ]
    for i, (bas, en, tr, e1, e2, e3, r, bg) in enumerate(yapilar):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="58" width="224" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="77" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="105" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{en}</text>'
        s += f'<text x="{x+112}" y="122" text-anchor="middle" fill="#475569" font-size="9.5">{tr}</text>'
        s += f'<rect x="{x+14}" y="140" width="196" height="122" rx="8" fill="#fff" stroke="{r}" stroke-width="1"/>'
        s += f'<text x="{x+112}" y="172" text-anchor="middle" fill="#1e293b" font-size="10.2">{e1}</text>'
        s += f'<text x="{x+112}" y="192" text-anchor="middle" fill="#1e293b" font-size="10.2">{e2}</text>'
        s += f'<text x="{x+112}" y="212" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{e3}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """School Life Vocabulary & Collocations (Academic & Extracurricular)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Key School Life Collocations &amp; Extracurricular Expressions", "#0d9488", "#f0fdfa")

    kelimeler = [
        ("compulsory / elective subjects", "zorunlu / seçmeli dersler"),
        ("revise for an exam", "sınav için tekrar yapmak"),
        ("meet the deadline", "teslim tarihine yetişmek"),
        ("do / hand in an assignment", "ödev yapmak / teslim etmek"),
        ("attend extracurricular clubs", "ders dışı kulüplere katılmak"),
        ("obey / follow school rules", "okul kurallarına uymak"),
        ("take part in a tournament", "bir turnuvada yer almak"),
        ("student exchange programme", "öğrenci değişim programı"),
    ]
    for i, (en, tr) in enumerate(kelimeler):
        x = 28 + (i % 2) * 358
        y = 58 + (i // 2) * 58
        s += f'<rect x="{x}" y="{y}" width="344" height="46" rx="8" fill="#fff" stroke="#14b8a6" stroke-width="1.3"/>'
        s += f'<text x="{x+16}" y="{y+20}" fill="#0f766e" font-size="11" font-weight="700">{en}</text>'
        s += f'<text x="{x+16}" y="{y+36}" fill="#475569" font-size="10">{tr}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Writing a School Club Announcement / Poster Structure."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Writing Skill: Designing a School Club Announcement &amp; Invitation", "#d97706", "#fffbeb")

    s += '<rect x="40" y="58" width="680" height="225" rx="12" fill="#fff" stroke="#f59e0b" stroke-width="1.8"/>'
    s += '<rect x="40" y="58" width="680" height="34" rx="12" fill="#f59e0b"/>'
    s += '<text x="380" y="80" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">JOIN THE DEBATE &amp; MUN CLUB! (Münazara Kulübü Duyuru Şablonu)</text>'

    parcalar = [
        ("1. Catchy Question:", "&quot;Are you interested in world affairs and public speaking?&quot;"),
        ("2. Club Activities:", "&quot;We are going to hold weekly debates and attend the National MUN Conference.&quot;"),
        ("3. Rules &amp; Requirements:", "&quot;Members have to attend Wednesday meetings and prepare a short speech.&quot;"),
        ("4. Time, Place &amp; Contact:", "&quot;Every Wednesday at 15:45 in Room 204 — Contact: Elif Kaya (10-B)&quot;"),
    ]
    for i, (b, ex) in enumerate(parcalar):
        y = 104 + i * 42
        s += f'<rect x="60" y="{y}" width="640" height="34" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>'
        s += f'<text x="75" y="{y+21}" fill="#b45309" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="235" y="{y+21}" fill="#1e293b" font-size="10.5">{ex}</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
