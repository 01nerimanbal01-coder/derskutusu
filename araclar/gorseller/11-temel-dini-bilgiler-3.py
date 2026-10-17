# -*- coding: utf-8 -*-
"""11. Sınıf Temel Dini Bilgiler - 3. Hafta Görselleri (Dünya-Ahiret Dengesi, Salih Amel ve Zamanın Kıymeti)"""


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
    """İslam'da Dünya ve Ahiret Dengesi (Kasas, 77 & Bakara, 201)"""
    g, y = 740, 260
    s = _baslik(g, "İSLAM'DA DÜNYA VE AHİRET DENGESİ: İKİ KANATLI KUŞ MİSALİ", "#0f766e")
    s += _kutu(20, 52, 220, 190, "#eff6ff", "#3b82f6", "DÜNYA HAYATI (Tarla)", [
        "• 'Dünya, ahiretin tarlasıdır.'",
        "• Helal rızık kazanmak,",
        "  yeryüzünü imar etmek ve",
        "  dünyadaki nasibini unutmamak",
        "  (Kasas Suresi, 77. ayet)."
    ], "#1e40af")
    s += _kutu(260, 52, 220, 190, "#fefce8", "#eab308", "ORTA YOL VE DENGE", [
        "• Ne dünyayı tamamen terk eden",
        "  ruhbanlık (tefrit), ne de",
        "  ahireti unutan dünyevileşme (ifrat).",
        "• 'Rabbimiz! Bize dünyada da",
        "  ahirette de iyilik (hasene) ver!'",
        "  (Bakara Suresi, 201. ayet)"
    ], "#854d0e")
    s += _kutu(500, 52, 220, 190, "#ecfdf5", "#10b981", "AHİRET HAYATI (Hasat)", [
        "• Ebedî yurt ve hesap günüdür.",
        "• Dünyada yapılan her iyilik",
        "  ve kötülüğün karşılığının",
        "  eksiksiz görüleceği yerdir",
        "  (Zilzâl Suresi, 7-8. ayetler)."
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_2():
    """Salih Amelin Kabul Şartları ve Sadaka-i Cariye"""
    g, y = 740, 260
    s = _baslik(g, "SALİH AMELİN ŞARTLARI VE AMEL DEFTERİNİ AÇIK TUTAN 3 ESER", "#15803d")
    s += _kutu(20, 52, 340, 190, "#f0fdf4", "#22c55e", "SALİH AMELİN KABUL ŞARTLARI", [
        "1. İMAN: Amelin geçerli olması için sağlam iman şarttır.",
        "2. İHLAS: Gösterişten (riya) uzak, yalnızca Allah rızası.",
        "3. SÜNNETE UYGUNLUK: Kur'an ve Sünnet ölçülerine uyum.",
        "• İbadetlerin yanı sıra insanlara, hayvanlara ve doğaya",
        "  fayda sağlayan her güzel davranış salih ameldir."
    ], "#166534")
    s += _kutu(380, 52, 340, 190, "#fefce8", "#eab308", "ÖLÜMDEN SONRA SEVABI KESİLMEYEN 3 AMEL", [
        "Hz. Peygamber'in (s.a.v.) hadisine göre (Müslim, Vasiyyet, 14):",
        "1. SADAKA-İ CARİYE: Cami, okul, çeşme, köprü, vakıf,",
        "   ağaç dikmek gibi kalıcı hayır kurumları.",
        "2. FAYDALI İLİM: Öğrenci yetiştirmek, eser bırakmak.",
        "3. HAYIRLI EVLAT: Anne-babasına dua eden salih evlat."
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_3():
    """Asr Suresi Işığında Zamanın Kıymeti ve Hüsrandan Kurtuluşun 4 İlkesi"""
    g, y = 740, 255
    s = _baslik(g, "ASR SURESİ: ZAMANIN KIYMETİ VE KURTULUŞUN DÖRT TEMEL İLKESİ", "#6d28d9")
    s += _kutu(16, 52, 168, 185, "#f5f3ff", "#8b5cf6", "1. İMAN ETMEK", [
        "('Elleîne âmenû')",
        "• Tevhid inancını ve",
        "  iman esaslarını kalpte",
        "  tereddütsüz tasdik",
        "  etmek (Temel kök)."
    ], "#5b21b6")
    s += _kutu(196, 52, 168, 185, "#eff6ff", "#3b82f6", "2. SALİH AMEL", [
        "('Ve amilü's-sâlihât')",
        "• İmanı ibadet, güzel",
        "  ahlak ve topluma",
        "  faydalı işlerle",
        "  eyleme dönüştürmek."
    ], "#1e40af")
    s += _kutu(376, 52, 168, 185, "#ecfdf5", "#10b981", "3. HAKKI TAVSİYE", [
        "('Tevâsav bi'l-hakk')",
        "• Toplumsal sorumluluk:",
        "  Doğruluğu, adaleti",
        "  ve iyiliği birbirine",
        "  hatırlatmak."
    ], "#065f46")
    s += _kutu(556, 52, 168, 185, "#fff7ed", "#f97316", "4. SABRI TAVSİYE", [
        "('Tevâsav bi's-sabr')",
        "• Zorluklara, ibadette",
        "  devamlılığa ve",
        "  günahlardan kaçınmaya",
        "  karşı direnç."
    ], "#9a3412")
    return _svg(g, y, s)


def gorsel_4():
    """Beş Şey Gelmeden Önce Beş Şeyin Kıymetini Bilmek (Hadis-i Şerif)"""
    g, y = 740, 245
    s = _baslik(g, "HADİS-İ ŞERİF: BEŞ ŞEY GELMEDEN ÖNCE BEŞ NİMETİN KIYMETİ", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "Kıymeti Bilinmesi Gereken 5 Nimet", [
        "1. İhtiyarlık gelmeden önce GENÇLİĞİN,",
        "2. Hastalık gelmeden önce SAĞLIĞIN (SIHHATİN),",
        "3. Fakirlik gelmeden önce ZENGİNLİĞİN (VARLIĞIN),",
        "4. Meşguliyet gelmeden önce BOŞ VAKTİN,",
        "5. Ölüm gelmeden önce HAYATIN kıymetini bil!"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#f8fafc", "#64748b", "İki Büyük Nimet ve Zaman Bilinci", [
        "• 'İki nimet vardır ki insanların çoğu onlar hususunda",
        "  aldanmıştır: SAĞLIK ve BOŞ VAKİT.' (Buhârî, Rikâk, 1)",
        "• 'İki günü eşit olan ziyandadır.' ilkesi, müminin",
        "  her yeni günde ilim, ahlak ve salih amelde",
        "  dünden daha ileriye gitmesini öğütler."
    ], "#334155")
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
