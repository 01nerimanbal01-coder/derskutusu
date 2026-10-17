# -*- coding: utf-8 -*-
"""11. Sınıf İngilizce - 3. Hafta Görselleri (Theme 1: Future Jobs - Future Continuous & Job Interviews)"""


def _svg(g, y, icerik):
    return (
        f'<svg viewBox="0 0 {g} {y}" width="100%" xmlns="http://www.w3.org/2000/svg" '
        f'style="max-width:{g}px;display:block;margin:14px auto;background:#fff;'
        f'border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _baslik(g, metin, renk="#1e293b"):
    return (
        f'<rect x="0" y="0" width="{g}" height="38" rx="10" fill="{renk}"/>'
        f'<rect x="0" y="20" width="{g}" height="18" fill="{renk}"/>'
        f'<text x="{g//2}" y="25" font-family="Arial,sans-serif" font-size="14" '
        f'font-weight="bold" fill="#ffffff" text-anchor="middle">{metin}</text>'
    )


def _kutu(x, y, g, yk, r_ark, r_ken, baslik, satirlar, r_bas="#0f172a"):
    ic = f'<rect x="{x}" y="{y}" width="{g}" height="{yk}" rx="8" fill="{r_ark}" stroke="{r_ken}" stroke-width="1.8"/>'
    ic += f'<text x="{x+g//2}" y="{y+22}" font-family="Arial,sans-serif" font-size="12.5" font-weight="bold" fill="{r_bas}" text-anchor="middle">{baslik}</text>'
    ic += f'<line x1="{x+10}" y1="{y+30}" x2="{x+g-10}" y2="{y+30}" stroke="{r_ken}" stroke-width="1"/>'
    for i, s in enumerate(satirlar):
        ic += f'<text x="{x+g//2}" y="{y+48+i*18}" font-family="Arial,sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s}</text>'
    return ic


def gorsel_1():
    """Future Continuous Tense (will be + V-ing) Structure & Usage"""
    g, y = 740, 260
    s = _baslik(g, "FUTURE CONTINUOUS TENSE: WILL BE + V-ING", "#1d4ed8")
    s += _kutu(20, 52, 340, 190, "#eff6ff", "#3b82f6", "GRAMMAR STRUCTURE (YAPI)", [
        "(+) Subject + WILL BE + V-ing",
        "    Ex: I will be working as a software engineer in 2030.",
        "(-) Subject + WON'T BE + V-ing",
        "    Ex: She won't be attending the meeting at 10 a.m.",
        "(?) WILL + Subject + BE + V-ing?",
        "    Ex: What will you be doing this time next year?"
    ], "#1e40af")
    s += _kutu(380, 52, 340, 190, "#f0fdf4", "#16a34a", "TIME EXPRESSIONS & USAGE", [
        "• Gelecekte belirli bir anda devam ediyor olacak eylemler:",
        "• This time tomorrow / next week / next year",
        "• At 9 o'clock tomorrow morning",
        "• In ten years' time / In 2035",
        "• Between 2 p.m. and 4 p.m. tomorrow",
        "• Nazikçe karşı tarafın planını sorma: 'Will you be using...?'"
    ], "#15803d")
    return _svg(g, y, s)


def gorsel_2():
    """Comparing Future Forms: Will vs. Be Going To vs. Present Continuous vs. Future Continuous"""
    g, y = 740, 265
    s = _baslik(g, "COMPARING FOUR FUTURE FORMS IN ENGLISH", "#0f766e")
    s += _kutu(16, 52, 168, 195, "#fef2f2", "#ef4444", "WILL + V1", [
        "• Spontaneous decisions",
        "  (Anlık kararlar)",
        "• Promises & Offers",
        "• Predictions with",
        "  think / hope / believe",
        "Ex: 'I'll answer the phone.'"
    ], "#991b1b")
    s += _kutu(196, 52, 168, 195, "#fff7ed", "#f97316", "BE GOING TO + V1", [
        "• Prior plans & intentions",
        "  (Önceden planlanan niyet)",
        "• Predictions based on",
        "  present evidence (kanıt)",
        "Ex: 'She is going to",
        "apply for the scholarship.'"
    ], "#9a3412")
    s += _kutu(376, 52, 168, 195, "#fefce8", "#eab308", "PRESENT CONT.", [
        "• Fixed personal",
        "  arrangements",
        "  (Kesinleşmiş randevu)",
        "• Time & place are set",
        "Ex: 'I am meeting the HR",
        "manager at 3 p.m. today.'"
    ], "#854d0e")
    s += _kutu(556, 52, 168, 195, "#eff6ff", "#3b82f6", "FUTURE CONT.", [
        "• Actions in progress at",
        "  a specific future time",
        "  (Gelecekte sürerlik)",
        "• WILL BE + V-ing",
        "Ex: 'At 3 p.m. tomorrow,",
        "I'll be having my interview.'"
    ], "#1e40af")
    return _svg(g, y, s)


def gorsel_3():
    """Job Interview Questions & Professional Responses"""
    g, y = 740, 260
    s = _baslik(g, "JOB INTERVIEW: KEY QUESTIONS AND PROFESSIONAL RESPONSES", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "INTERVIEWER'S QUESTIONS (Mülakat Soruları)", [
        "1. Can you tell us a little about yourself?",
        "2. Why do you want to work for our company?",
        "3. What are your greatest strengths and weaknesses?",
        "4. Where do you see yourself in five years' time?",
        "5. Why should we hire you for this position?",
        "6. How do you handle working under pressure?"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "CANDIDATE'S EXPRESSIONS (Aday İfadeleri)", [
        "• I have a degree in... / I have two years' experience under my belt.",
        "• I am a team player, detail-oriented, and adaptable.",
        "• In five years' time, I will be leading innovative projects.",
        "• I believe my qualifications match your requirements.",
        "• I stay calm and prioritize tasks when working under deadlines.",
        "• Thank you for giving me this opportunity."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """CV (Resume) vs. Letter of Intent (Cover Letter) Checklist"""
    g, y = 740, 250
    s = _baslik(g, "JOB APPLICATION TOOLKIT: CV vs. LETTER OF INTENT", "#15803d")
    s += _kutu(20, 52, 340, 180, "#f0fdf4", "#22c55e", "CURRICULUM VITAE (CV / RESUME)", [
        "• Contact Information (Ad, Telefon, E-posta, Adres)",
        "• Education Background (Mezun olunan okullar, GPA)",
        "• Work / Internship Experience (İş ve staj deneyimi)",
        "• Hard & Soft Skills (Yabancı dil, yazılım, iletişim)",
        "• References ('Available upon request')"
    ], "#166534")
    s += _kutu(380, 52, 340, 180, "#ecfeff", "#06b6d4", "LETTER OF INTENT (COVER LETTER)", [
        "• Opening: 'Dear Hiring Manager,' + başvurulan pozisyon",
        "• Body 1: Eğitim ve deneyimlerin pozisyonla uyumu",
        "• Body 2: Kuruma katacağı değer ve gelecek vizyonu",
        "• Closing: 'I look forward to hearing from you.'",
        "• Sign-off: 'Yours faithfully / Sincerely,' + İmza"
    ], "#0e7490")
    return _svg(g, y, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for k, sv in GORSELLER.items():
        idx = int(k[1:]) - 1
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = sv
    return v
