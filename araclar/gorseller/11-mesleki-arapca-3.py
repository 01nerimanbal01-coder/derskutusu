# -*- coding: utf-8 -*-
"""11. Sınıf Mesleki Arapça - 3. Hafta Görselleri (İman Esasları ve Esmaülhüsna)"""


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
    """Erkânü'l-Îmân: Arapça Altı İman Esası (آمنت بالله...)"""
    g, y = 740, 265
    s = _baslik(g, "ERKÂNÜ'L-ÎMÂN: ARAPÇADA ALTI İMAN ESASI (أَرْكَانُ الْإِيمَانِ السِّتَّةُ)", "#0f766e")
    s += _kutu(18, 52, 228, 92, "#ecfdf5", "#10b981", "1. Allah'a İman", [
        "الْإِيمَانُ بِاللّٰهِ",
        "(el-Îmânü billâhi)"
    ], "#065f46")
    s += _kutu(256, 52, 228, 92, "#eff6ff", "#3b82f6", "2. Meleklere İman", [
        "الْإِيمَانُ بِالْمَلَائِكَةِ",
        "(el-Îmânü bi'l-melâiketi)"
    ], "#1e40af")
    s += _kutu(494, 52, 228, 92, "#fefce8", "#eab308", "3. Kitaplara İman", [
        "الْإِيمَانُ بِالْكُتُبِ",
        "(el-Îmânü bi'l-kütübi)"
    ], "#854d0e")
    s += _kutu(18, 156, 228, 92, "#f5f3ff", "#8b5cf6", "4. Peygamberlere İman", [
        "الْإِيمَانُ بِالرُّسُلِ",
        "(el-Îmânü bi'r-rusüli)"
    ], "#5b21b6")
    s += _kutu(256, 156, 228, 92, "#fff7ed", "#f97316", "5. Ahiret Gününe İman", [
        "الْإِيمَانُ بِالْيَوْمِ الْآخِرِ",
        "(el-Îmânü bi'l-yevmi'l-âhiri)"
    ], "#9a3412")
    s += _kutu(494, 156, 228, 92, "#fef2f2", "#ef4444", "6. Kader ve Kazaya İman", [
        "الْإِيمَانُ بِالْقَدَرِ خَيْرِهِ وَشَرِّهِ",
        "(el-Îmânü bi'l-kaderi)"
    ], "#991b1b")
    return _svg(g, y, s)


def gorsel_2():
    """Âmene Fiilinin 'bi-' (بِـ) Harf-i Cerri İle Kullanımı ve Cümle Kalıpları"""
    g, y = 740, 255
    s = _baslik(g, "DİL BİLGİSİ: 'ÂMENE - YÜ'MİNÜ - ÎMÂNEN' FİİLİ VE 'Bİ-' HARF-İ CERRİ", "#1d4ed8")
    s += _kutu(20, 52, 340, 185, "#eff6ff", "#3b82f6", "FİİL ÇEKİMİ VE HARF-İ CER KURALI", [
        "• Mazi: آمَنَ (Âmene - İman etti)",
        "• Muzari: يُؤْمِنُ (Yü'minü - İman ediyor / eder)",
        "• Masdar: إِيمَانٌ (Îmânün)  |  İsm-i Fail: مُؤْمِنٌ (Mü'minün)",
        "• KURAL: Bu fiil iman edilen nesneyi daima 'بِـ' (bi-)",
        "  harf-i cerri ile alır ve sonunu ESRE (mecrur) yapar!"
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 185, "#f0fdf4", "#16a34a", "ÖRNEK ARAPÇA CÜMLELER", [
        "• آمَنْتُ بِاللّٰهِ وَمَلَائِكَتِهِ (Allah'a ve meleklerine inandım)",
        "• يُؤْمِنُ الْمُسْلِمُ بِالْيَوْمِ الْآخِرِ (Müslüman ahiret gününe inanır)",
        "• أَرْكَانُ الْإِيمَانِ سِتَّةٌ (İmanın şartları altıdır)",
        "• الْإِيمَانُ تَصْدِيقٌ بِالْقَلْبِ وَإِقْرَارٌ بِاللِّسَانِ",
        "  (İman kalple tasdik ve dille ikrardır.)"
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_3():
    """Esmaülhüsna (أَسْمَاءُ اللّٰهِ الْحُسْنَى) Kavramları ve Anlamları"""
    g, y = 740, 260
    s = _baslik(g, "ESMAÜLHÜSNA: ALLAH'IN EN GÜZEL İSİMLERİ (أَسْمَاءُ اللّٰهِ الْحُسْنَى)", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "YARATMA, RIZIK VE MERHAMET İSİMLERİ", [
        "• الرَّحْمٰنُ (er-Rahmân): Dünyada tüm varlıklara merhamet eden",
        "• الرَّحِيمُ (er-Rahîm): Ahirette yalnız müminlere merhamet eden",
        "• الْخَالِقُ (el-Hâlık): Yoktan var eden, yaratan",
        "• الرَّزَّاقُ (er-Rezzâk): Tüm canlıların rızkını veren",
        "• الْغَفَّارُ / الْغَفُورُ (el-Gaffâr / el-Gafûr): Günahları bağışlayan"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "İLİM, KUDRET VE ADALET İSİMLERİ", [
        "• الْعَلِيمُ (el-Alîm): Gizli ve açık her şeyi hakkıyla bilen",
        "• السَّمِيعُ (es-Semî'): Her şeyi işiten",
        "• الْبَصِيرُ (el-Basîr): Her şeyi gören",
        "• الْقَدِيرُ (el-Kadîr): Her şeye gücü yeten, mutlak kudret sahibi",
        "• الْعَدْلُ / الْحَكِيمُ (el-Adl / el-Hakîm): Adil ve hikmet sahibi"
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Haşr Suresi 22-24. Ayetlerde (Hüvallâhüllezî) Geçen Esmaülhüsna"""
    g, y = 740, 245
    s = _baslik(g, "HAŞR SURESİ 22-24. AYETLERDE GEÇEN ESMAÜLHÜSNA LAFIZLARI", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "Haşr, 22-23. Ayetlerdeki İsimler", [
        "• عَالِمُ الْغَيْبِ وَالشَّهَادَةِ (Gaybı ve görüneni bilen)",
        "• الرَّحْمٰنُ الرَّحِيمُ (er-Rahmân, er-Rahîm)",
        "• الْمَلِكُ (el-Melik - Mülkün gerçek hükümdarı)",
        "• الْقُدُّوسُ (el-Kuddûs - Her eksiklikten münezzeh)",
        "• السَّلَامُ الْمُؤْمِنُ الْمُهَيْمِنُ الْعَزِيزُ الْجَبَّارُ الْمُتَكَبِّرُ"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#fff7ed", "#f97316", "Haşr, 24. Ayetteki Yaratma İsimleri", [
        "• هُوَ اللّٰهُ الْخَالِقُ الْبَارِئُ الْمُصَوِّرُ لَهُ الْأَسْمَاءُ الْحُسْنَى",
        "• الْخَالِقُ (el-Hâlık): Takdir edip yoktan var eden",
        "• الْبَارِئُ (el-Bâri'): Uygun ve kusursuz biçimde yaratan",
        "• الْمُصَوِّرُ (el-Musavvir): Varlıklara şekil ve suret veren",
        "• الْعَزِيزُ الْحَكِيمُ (Mutlak galip ve hikmet sahibi)"
    ], "#9a3412")
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
