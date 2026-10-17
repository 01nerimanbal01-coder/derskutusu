def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Present Continuous Tense (Şimdiki Zaman): Yapı ve Kullanım</text>'
    c += _kart(18, 54, 206, 175, "Olumlu Cümle (+)", [
        "• I + am + V-ing",
        "  (I am studying for the exam.)",
        "• He / She / It + is + V-ing",
        "  (She is doing an experiment.)",
        "• We / You / They + are + V-ing",
        "  (They are playing chess now.)"
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 175, "Olumsuz Cümle (-)", [
        "• I am not + V-ing",
        "• He/She/It isn\'t + V-ing",
        "• We/You/They aren\'t + V-ing",
        "• Örnek: He isn\'t sleeping",
        "  right now; he is reading",
        "  a book in the library."
    ], "#922b21", "#fdedec")
    c += _kart(456, 54, 206, 175, "Soru Cümlesi (?)", [
        "• Am / Is / Are + S + V-ing?",
        "• Wh- + am/is/are + S + V-ing?",
        "• Örnek: Are you working on",
        "  the science project?",
        "  — Yes, I am. / No, I\'m not.",
        "• What is she doing at the moment?"
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Simple Present vs. Present Continuous (Geniş Zaman ve Şimdiki Zaman Karşılaştırması)</text>'
    c += _kart(18, 54, 314, 175, "Simple Present Tense (Geniş Zaman)", [
        "• Kullanım: Günlük rutinler, alışkanlıklar,",
        "  okul ders programı ve genel doğrular.",
        "• Yapı: V1 / V-s (do / does, don\'t / doesn\'t)",
        "• Zaman İfadeleri: every day, usually, always,",
        "  often, on Mondays, at weekends.",
        "• Örn: We have Biology on Tuesdays."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 175, "Present Continuous Tense (Şimdiki Zaman)", [
        "• Kullanım: Konuşma anında devam eden eylemler",
        "  ve bu günlerdeki geçici okul projeleri.",
        "• Yapı: am / is / are + V-ing",
        "• Zaman İfadeleri: now, right now, at the moment,",
        "  at present, today, this week, Look!, Listen!",
        "• Örn: Look! The teacher is entering the lab."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">State / Non-Progressive Verbs (-ing Almayan Durum Fiilleri)</text>'
    c += _kart(18, 54, 314, 170, "Duygu ve Düşünce Bildiren Durum Fiilleri", [
        "• Duygu: like, love, hate, want, need, prefer",
        "• Zihin / Düşünce: know, understand, believe,",
        "  remember, forget, mean, think (kanaat anlamında)",
        "• Bu fiiller \'now / at the moment\' olsa bile",
        "  -ing ALMAZ; Simple Present ile kullanılır!"
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 170, "Sahiplik ve Algı Fiilleri + Doğru Örnekler", [
        "• Sahiplik / Durum: have (sahip olmak), belong,",
        "  own, seem, cost, bisogno/need.",
        "• Doğru: \'I understand the lesson now.\'",
        "  (Yanlış: I am understanding the lesson now.)",
        "• Doğru: \'She needs a dictionary right now.\'"
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">School Clubs, Extracurricular Activities &amp; Campus Vocabulary</text>'
    c += _kart(18, 54, 314, 165, "School Clubs &amp; Activities (Okul Kulüpleri)", [
        "• Robotics &amp; Coding Club (Robotik ve Kodlama)",
        "• Drama &amp; Theatre Club (Tiyatro Kulübü)",
        "• Debating Society (Münazara Kulübü)",
        "• Astronomy / Environmental Club (Çevre Kulübü)",
        "• Attend a club / take part in a tournament"
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 165, "Study Habits &amp; Useful Expressions", [
        "• Revise regularly: Düzenli tekrar yapmak",
        "• Take notes in class: Derste not tutmak",
        "• Meet deadlines: Teslim tarihlerine uymak",
        "• Exchange student: Değişim öğrencisi",
        "• Compulsory / Optional (Elective) subjects"
    ], "#1e8449", "#e9f7ef")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
