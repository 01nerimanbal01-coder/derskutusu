# -*- coding: utf-8 -*-
"""11. Sınıf Tefsir - 3. Hafta Görselleri (Kur'an İlimleri / Ulûmü'l-Kur'ân ve Birbiriyle İlişkisi)"""


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
    """Ulûmü'l-Kur'ân (Kur'an İlimleri) Sınıflandırması"""
    g, y = 740, 265
    s = _baslik(g, "ULÛMÜ'L-KUR'ÂN: KUR'AN İLİMLERİNİN DÖRT ANA GRUBU", "#0f766e")
    s += _kutu(16, 52, 168, 195, "#ecfdf5", "#10b981", "1. NÜZUL TARİHİ", [
        "(İniş Süreci İlimleri)",
        "• Esbâb-ı Nüzûl",
        "  (İniş Sebepleri)",
        "• Mekkî ve Medenî",
        "  Sure/Ayetler İlmî",
        "• Nâsih ve Mensûh"
    ], "#065f46")
    s += _kutu(196, 52, 168, 195, "#eff6ff", "#3b82f6", "2. LAFIZ VE DİL", [
        "(Kelime İlimleri)",
        "• Garîbü'l-Kur'ân",
        "  (Nadir Kelimeler)",
        "• Vücûh ve Nezâir",
        "• İ'râbü'l-Kur'ân",
        "• Kıraat İlmi"
    ], "#1e40af")
    s += _kutu(376, 52, 168, 195, "#fefce8", "#eab308", "3. ANLAM VE YORUM", [
        "(Mana İlimleri)",
        "• Muhkem ve Müteşâbih",
        "• Mücmel ve Mübeyyen",
        "• Müşkilü'l-Kur'ân",
        "• Münâsebâtü'l-Kur'ân"
    ], "#854d0e")
    s += _kutu(556, 52, 168, 195, "#f5f3ff", "#8b5cf6", "4. ANLATIM ÜSLUBU", [
        "(Edebî İlimler)",
        "• İ'câzü'l-Kur'ân",
        "• Kısasü'l-Kur'ân",
        "• Emsâlü'l-Kur'ân",
        "• Aksâmü'l-Kur'ân (Yemin)"
    ], "#5b21b6")
    return _svg(g, y, s)


def gorsel_2():
    """Nüzul Süreciyle İlgili İlimler: Esbâb-ı Nüzûl, Mekkî-Medenî ve Nâsih-Mensûh"""
    g, y = 740, 260
    s = _baslik(g, "NÜZUL SÜRECİ İLİMLERİ VE BİRBİRİYLE İLİŞKİSİ", "#1d4ed8")
    s += _kutu(20, 52, 340, 190, "#eff6ff", "#3b82f6", "ESBÂB-I NÜZÛL VE MEKKÎ-MEDENÎ", [
        "• ESBÂB-I NÜZÛL: Hz. Peygamber döneminde meydana",
        "  gelen bir olay veya sorulan bir soru üzerine ayetlerin",
        "  iniş sebeplerini inceler (Vâhidî -> Esbâbü'n-Nüzûl).",
        "• MEKKÎ - MEDENÎ: Hicretten ÖNCE inenlere Mekkî (iman,",
        "  tevhid, ahiret); Hicretten SONRA inenlere Medenî (hukuk,",
        "  ibadet, toplumsal düzen) denir."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 190, "#f0fdf4", "#16a34a", "NÂSİH - MENSÛH VE TEDRÎCÎLİK İLİŞKİSİ", [
        "• NESH: Önceki bir şer'î hükmün, daha sonra inen",
        "  yeni bir ayetle yürürlükten kaldırılmasıdır.",
        "  (Kaldıran ayete NÂSİH, hükmü kalkana MENSÛH denir).",
        "• BİRBİRİYLE İLİŞKİSİ: Nâsih ayeti Mensûh ayetten",
        "  ayırt edebilmek için ayetlerin Mekkî-Medenî sırasını",
        "  ve Esbâb-ı Nüzûlünü (kronolojisini) bilmek şarttır!"
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_3():
    """Lafız ve Anlam İlimleri: Garîbü'l-Kur'ân, Vücûh ve Nezâir, Muhkem ve Müteşâbih"""
    g, y = 740, 260
    s = _baslik(g, "LAFIZ VE ANLAM İLİMLERİ: GARÎB, VÜCÛH-NEZÂİR, MUHKEM-MÜTEŞÂBİH", "#6d28d9")
    s += _kutu(18, 52, 228, 190, "#f5f3ff", "#8b5cf6", "GARÎBÜ'L-KUR'ÂN", [
        "• Lehçe farklılıkları veya",
        "  az kullanılması sebebiyle",
        "  anlamı ilk bakışta",
        "  anlaşılmayan nadir",
        "  kelimeleri açıklar.",
        "• Râgıb el-İsfahânî ->",
        "  'el-Müfredât'"
    ], "#5b21b6")
    s += _kutu(256, 52, 228, 190, "#fdf4ff", "#d946ef", "VÜCÛH VE NEZÂİR", [
        "• VÜCÛH (Çok Anlamlılık):",
        "  Bir kelimenin farklı",
        "  ayetlerde farklı anlamda",
        "  kullanılması (Örn: Salât,",
        "  Hüdâ, Ümmet).",
        "• NEZÂİR (Eş Anlamlılık):",
        "  Farklı kelimelerin aynı mana."
    ], "#86198f")
    s += _kutu(494, 52, 228, 190, "#fefce8", "#eab308", "MUHKEM VE MÜTEŞÂBİH", [
        "• MUHKEM (Âl-i İmrân, 7):",
        "  Anlamı açık, net, yoruma",
        "  ihtiyaç duymayan temel",
        "  ayetler (Ümmü'l-Kitâb).",
        "• MÜTEŞÂBİH: Birden fazla",
        "  anlama ihtimali olan veya",
        "  Hurûf-u Mukattaa ayetleri."
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_4():
    """Edebî Anlatım İlimleri ve Klasik Ulûmü'l-Kur'ân Eserleri"""
    g, y = 740, 250
    s = _baslik(g, "ANLATIM İLİMLERİ VE KLASİK ULÛMÜ'L-KUR'ÂN ESERLERİ", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "KUR'AN'IN EDEBÎ ANLATIM İLİMLERİ", [
        "• İ'CÂZÜ'L-KUR'ÂN: Kur'an'ın dil, üslup ve içerik",
        "  bakımından benzerinin getirilemez oluşu (Mucizeliği).",
        "• KISASÜ'L-KUR'ÂN: İbret için anlatılan geçmiş peygamber",
        "  ve kavim kıssaları (Tarih kitabı değil, hidayet rehberi).",
        "• EMSÂL VE AKSÂM: Temsiller/benzetmeler ve yeminler."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#fff7ed", "#f97316", "EN MEŞHUR 2 KAPSAYICI ULÛMÜ'L-KUR'ÂN ESERİ", [
        "1. BEDREDDİN EZ-ZERKEŞÎ (ö. 1392):",
        "   'el-Burhân fî Ulûmi'l-Kur'ân' (47 Kur'an ilmini",
        "   bir araya getiren ilk büyük ansiklopedik eser).",
        "2. CELÂLEDDİN ES-SUYÛTÎ (ö. 1505):",
        "   'el-İtkân fî Ulûmi'l-Kur'ân' (80 Kur'an ilmini",
        "   sistematik olarak inceleyen en meşhur başyapıt)."
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