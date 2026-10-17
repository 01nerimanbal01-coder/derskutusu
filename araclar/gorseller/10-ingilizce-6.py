def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Expressing Preferences: Prefer / Would Rather / Would Prefer</text>'
        + _kart(20, 42, 200, 142, "1. Prefer (Genel Tercih)", [
            "• prefer + V-ing + TO + V-ing",
            "• ”I prefer studying in the",
            "  library to studying at home.”",
            "• prefer + Noun + TO + Noun",
            "• ”She prefers math to art.”"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. Would Rather (Anlık/Özel)", [
            "• would rather + V₁ + THAN + V₁",
            "  (Yalın fiil kullanılır!)",
            "• ”I’d rather join the drama",
            "  club than play chess.”",
            "• Olumsuz: would rather NOT + V₁"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 142, "3. Would Prefer (Belirli Durum)", [
            "• would prefer + TO V₁",
            "  + RATHER THAN + V₁",
            "• ”I’d prefer to prepare a",
            "  poster rather than give a",
            "  speech.”"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'School Life: Comparing Education Systems &amp; Exchange Programs</text>'
        + _kart(25, 42, 300, 145, "Exchange &amp; Project Vocabulary", [
            "• Exchange student: Değişim öğrencisi (Erasmus+)",
            "• Host family: Ev sahibi aile",
            "• Compulsory subject: Zorunlu ders",
            "• Elective / Optional course: Seçmeli ders",
            "• Extracurricular activity: Ders dışı kulüp etkinliği"
        ], "#059669", "#ecfdf5")
        + _kart(355, 42, 300, 145, "Academic &amp; Assessment Expressions", [
            "• Revise for an exam: Sınav için tekrar yapmak",
            "• Hand in / Submit an assignment: Ödev teslim etmek",
            "• Meet the deadline: Son teslim tarihine yetişmek",
            "• Do research / Make a presentation: Sunum yapmak",
            "• Scholarship / Term / Timetable: Burs / Dönem / Program"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 200, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Present Simple vs. Present Continuous vs. Future Tenses Review</text>'
        + _kart(20, 42, 200, 142, "Present Simple", [
            "• Rutinler ve ders programı:",
            "• ”Our first lesson starts",
            "  at 8:30 every morning.”",
            "• Always, usually, on Mondays,",
            "  twice a week"
        ], "#0284c7", "#f0f9ff")
        + _kart(240, 42, 200, 142, "Present Continuous", [
            "• Şu an veya bu dönem yapılan:",
            "• ”We are preparing a science",
            "  project this week.”",
            "• Now, at the moment, right",
            "  now, nowadays, currently"
        ], "#ea580c", "#fff7ed")
        + _kart(460, 42, 200, 142, "Be Going To vs. Will", [
            "• Be going to: Plan ve niyet",
            "  ”I am going to study abroad.”",
            "• Will: Anlık karar, söz, tahmin",
            "  ”Don’t worry, I will help you",
            "  with your homework!”"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 198, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Writing an Informative Paragraph / Blog Post About School Life</text>'
        + _kart(25, 42, 300, 138, "Paragraph Structure (Başlık - Giriş - Gelişme)", [
            "• 1. Topic Sentence: Okulunuzu ve kendinizi tanıtın",
            "• 2. Supporting Sentences: Günlük rutinler, en sevilen",
            "  dersler, kulüpler ve tercihler (prefer / would rather)",
            "• 3. Concluding Sentence: Gelecek hedefleri ve kapanış"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Useful Linking Words (Bağlaçlar)", [
            "• Ekleme: Also, besides, in addition, furthermore",
            "• Zıtlık: However, but, although, on the other hand",
            "• Sebep-Sonuç: Because, since, so, therefore",
            "• Sıralama: First of all, then, after that, finally"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
