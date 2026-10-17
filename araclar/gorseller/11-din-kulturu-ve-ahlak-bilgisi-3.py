# -*- coding: utf-8 -*-
"""11. Sınıf Din Kültürü ve Ahlak Bilgisi - 3. Hafta Görselleri (Akıl, İrade ve Sorumluluk)"""


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
    """Dini Sorumluluğun (Teklifin) İki Temel Şartı: Akıl ve İrade"""
    g, y = 740, 255
    s = _baslik(g, "İNSANI MÜKELLEF KILAN İKİ TEMEL NİTELİK: AKIL VE İRADE", "#0f766e")
    s += _kutu(20, 52, 220, 182, "#ecfdf5", "#10b981", "1. AKIL (Temyiz Gücü)", [
        "• İyiyi kötüden, hakkı batıldan",
        "  ayırt etme yetisidir.",
        "• 'Aklı olmayanın dini",
        "  (sorumluluğu) de yoktur.'",
        "• Vahyin muhatabı olma şartıdır."
    ], "#065f46")
    s += _kutu(260, 52, 220, 182, "#eff6ff", "#3b82f6", "2. İRADE (Seçme Özgürlüğü)", [
        "• Alternatifler arasında baskı",
        "  olmadan tercih yapabilme",
        "  ve karar verme gücüdür.",
        "• Zorlama (ikrah) altında",
        "  ahlaki sorumluluk doğmaz."
    ], "#1e40af")
    s += _kutu(500, 52, 220, 182, "#fefce8", "#eab308", "3. SORUMLULUK (Mes'ûliyet)", [
        "• Akıl + Cüz'î İrade = MÜKELLEF",
        "• Kişinin kendi hür seçimiyle",
        "  yaptığı amellerin dünyada ve",
        "  ahirette sonucunu üstlenmesidir.",
        "• (İnsan, 3 / Kehf, 29 / Zilzâl, 7-8)"
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_2():
    """Küllî İrade - Cüz'î İrade ve İnsan Fiillerinin Sınıflandırılması"""
    g, y = 740, 265
    s = _baslik(g, "İRADE TÜRLERİ VE İNSAN FİİLLERİNİN SINIFLANDIRILMASI", "#1d4ed8")
    s += _kutu(20, 52, 340, 195, "#eff6ff", "#3b82f6", "KÜLLÎ İRADE VE CÜZ'Î İRADE", [
        "• KÜLLÎ İRADE: Yüce Allah'ın sınırsız, mutlak ve",
        "  her şeyi kuşatan iradesidir ('Ol' der ve olur - Yâsîn, 82).",
        "• CÜZ'Î İRADE: Allah'ın insana imtihan sırrı gereği",
        "  bahşettiği sınırlı seçme ve yönelme özgürlüğüdür.",
        "• Cüz'î irade, Küllî iradenin insana tanıdığı",
        "  özgürlük alanı içinde işler."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 195, "#f0fdf4", "#16a34a", "İNSAN FİİLLERİNİN İKİ KATEGORİSİ", [
        "1. ZORUNLU (IZTIRÂRÎ) FİİLLER: Kalp atışı, göz rengi,",
        "   doğduğu yer/zaman -> İrade dışı -> SORUMLULUK YOK.",
        "2. SEÇİME DAYALI (İHTİYARÎ) FİİLLER: İman/inkâr,",
        "   ibadet, dürüstlük, yardımseverlik -> Cüz'î irade ile",
        "   seçilir -> DÜNYA VE AHİRETTE TAM SORUMLULUK VAR."
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_3():
    """İslam Düşüncesinde İnsan Fiilleri Mezhepleri: Cebriye - Ehl-i Sünnet - Mu'tezile"""
    g, y = 740, 265
    s = _baslik(g, "İSLAM DÜŞÜNCESİNDE İNSAN FİİLLERİ VE İRADE TARTIŞMALARI", "#6d28d9")
    s += _kutu(18, 52, 228, 195, "#fef2f2", "#ef4444", "CEBRİYE (İfrat Uç)", [
        "• İnsanın hiçbir iradesi ve",
        "  seçme gücü yoktur.",
        "• İnsan, 'rüzgârın önündeki",
        "  kuru yaprak' gibidir.",
        "• Eleştiri: İmtihanı, sevabı ve",
        "  cezayı anlamsız kılar."
    ], "#991b1b")
    s += _kutu(256, 52, 228, 195, "#ecfdf5", "#10b981", "EHL-İ SÜNNET (Orta Yol)", [
        "• Mâtürîdîlik ve Eş'arîlik.",
        "• Kul cüz'î iradesiyle SEÇER",
        "  ve KESB eder (kazanır);",
        "  Yüce Allah ise küllî iradesi",
        "  ve kudretiyle YARATIR (halk).",
        "• Sorumluluk seçen kula aittir."
    ], "#065f46")
    s += _kutu(494, 52, 228, 195, "#fff7ed", "#f97316", "MU'TEZİLE (Tefrit Uç)", [
        "• İnsan tam ve bağımsız",
        "  irade sahibidir.",
        "• Kul, kendi ihtiyari fiillerinin",
        "  bizzat YARATICISIDIR.",
        "• Eleştiri: 'Allah her şeyin",
        "  yaratıcısıdır' ilkesini zedeler."
    ], "#9a3412")
    return _svg(g, y, s)


def gorsel_4():
    """Mâtürîdîlik ve Eş'arîlikte Kesb ve İrade Nüansı"""
    g, y = 740, 245
    s = _baslik(g, "EHL-İ SÜNNET İÇİNDE MÂTÜRÎDÎLİK VE EŞ'ARÎLİK YAKLAŞIMI", "#0f172a")
    s += _kutu(20, 52, 340, 175, "#f0fdf4", "#16a34a", "İMAM MÂTÜRÎDÎ (Mâtürîdîlik)", [
        "• İnsanda müstakil bir 'cüz'î irade (külli iradeden",
        "  bağımsız yönelim/azim)' bulunduğunu vurgular.",
        "• Kul cüz'î iradesiyle fiile yönelir (kesb), Allah da",
        "  kulun bu tercihine göre fiili yaratır (halk).",
        "• İnsan özgürlüğünü ve sorumluluğunu en güçlü temellendirir."
    ], "#15803d")
    s += _kutu(380, 52, 340, 175, "#eff6ff", "#3b82f6", "İMAM EŞ'ARÎ (Eş'arîlik)", [
        "• Allah'ın mutlak kudretini ve iradesini merkeze alır.",
        "• Fiil anında Allah'ın insanda yarattığı geçici güçle",
        "  kulun o fiile sahip çıkmasına 'kesb' adını verir.",
        "• Her iki Sünnî ekol de fiilin yaratıcısının (Hâlık)",
        "  yalnızca Allah olduğu konusunda tam ittifak hâlindedir."
    ], "#1e40af")
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