# -*- coding: utf-8 -*-
"""12. Sınıf Kimya - 3. Hafta Görselleri (Standart Elektrot Potansiyelleri, Aktiflik, Nernst ve Derişim Pilleri)"""


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
    """Standart Elektrot Potansiyeli (E°) Kuralları ve Standart Hücre Potansiyeli"""
    g, y = 740, 265
    s = _baslik(g, "STANDART ELEKTROT POTANSİYELİ (E°) VE PİL GERİLİMİ KURALLARI", "#1d4ed8")
    s += _kutu(20, 52, 340, 195, "#eff6ff", "#3b82f6", "STANDART HÜCRE POTANSİYELİ (E°_hücre)", [
        "• Referans Elektrot: SHE (2H⁺ + 2e⁻ -> H₂, E° = 0,00 V)",
        "• İndirgenme potansiyeli KÜÇÜK (yükseltgenme potansiyeli",
        "  BÜYÜK) olan elektrot ANOT, diğeri KATOT olur.",
        "• E°_hücre = E°_yüks (Anot) + E°_ind (Katot)",
        "• Veya: E°_hücre = E°_ind (Katot) - E°_ind (Anot)",
        "• E°_hücre > 0 ise tepkime İSTEMLİDİR (Galvanik pil)."
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 195, "#f0fdf4", "#16a34a", "YARI TEPKİME İŞLEMLERİNİN E° DEĞERİNE ETKİSİ", [
        "1. Yarı tepkime TERS ÇEVRİLİRSE E° değerinin",
        "   İŞARETİ DEĞİŞİR (E°_yüks = -E°_ind).",
        "2. Yarı tepkime bir katsayı ile ÇARPILIR veya",
        "   BÖLÜNÜRSE E° değeri DEĞİŞMEZ! (Çünkü E° madde",
        "   miktarına bağlı olmayan yeğin bir özelliktir).",
        "3. İki yarı tepkime toplanırsa E° değerleri toplanır."
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_2():
    """Metalik Aktiflik Sırası ve Saklama Kabı / Aşınma Problemleri"""
    g, y = 740, 260
    s = _baslik(g, "ELEKTROKİMYASAL AKTİFLİK SIRASI VE İSTEMLİLİK TESTİ", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "METALİK AKTİFLİK VE YARI SOY / TAM SOY METALLER", [
        "• Elektron verme eğilimi (E°_yüks) büyük olan metal",
        "  daha AKTİFTİR (En aktifler: Li, K, Ba, Ca, Na, Mg, Al, Zn, Fe).",
        "• H₂'den aktif metaller (E°_yüks > 0) asitlerle H₂ gazı çıkarır.",
        "• Yarı Soy Metaller (Cu, Hg, Ag): E°_yüks < 0; yalnız",
        "  HNO₃ ve H₂SO₄ ile tepkime verir (H₂ gazı çıkarmaz!).",
        "• Tam Soy Metaller (Au, Pt): Asitlerle tepkime vermez (Kral suyu hariç)."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#fef2f2", "#ef4444", "METAL ÇUBUK / SAKLAMA KABI KURALI", [
        "• X(k) metali, Y²⁺(suda) çözeltisine daldırıldığında:",
        "• Eğer X metali Y'den AKTİFSE (X > Y):",
        "  - Kendiliğinden X(k) + Y²⁺ -> X²⁺ + Y(k) tepkimesi olur.",
        "  - X çubuğu/kabı AŞINIR ve çözelti X kabında SAKLANAMAZ!",
        "• Eğer X metali Y'den PASİFSE (X < Y):",
        "  - Tepkime OLMAZ, aşınma olmaz ve çözelti SAKLANABİLİR!"
    ], "#991b1b")
    return _svg(g, y, s)


def gorsel_3():
    """Pil Gerilimini (E_hücre) Etkileyen Faktörler (Le Chatelier İlkesi)"""
    g, y = 740, 260
    s = _baslik(g, "PİL POTANSİYELİNİ ETKİLEYEN FAKTÖRLER (DENGE YORUMU)", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "PİL TEPKİMESİ BİR DENGE TEPKİMESİDİR!", [
        "Anot(k) + Katot^n+(suda) <=> Anot^n+(suda) + Katot(k) + ISI",
        "• KURAL: Yapılan etki dengeyi ÜRÜNLERE (sağa)",
        "  kaydırırsa E_pil ARTAR; GİRENLERE (sola) kaydırırsa",
        "  E_pil AZALIR!",
        "• Elektrotların kütlesini/yüzey alanını veya çözelti",
        "  hacmini (derişimi değiştirmeden) artırmak E_pil'i DEĞİŞTİRMEZ!"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "PİL GERİLİMİNİ ARTIRAN ETKİLER (Sağa Kaydıranlar)", [
        "1. KATOT yarı hücresindeki katyon derişimini ARTIRMAK",
        "   (Katot kabına tuz eklemek veya su buharlaştırmak).",
        "2. ANOT yarı hücresindeki katyon derişimini AZALTMAK",
        "   (Anot kabına saf su eklemek veya iyonları çöktürmek).",
        "3. Sıcaklığı AZALTMAK (Pil tepkimeleri ekzotermiktir,",
        "   soğutulduğunda denge ürünlere kayar ve E_pil artar)."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Nernst Eşitliği ve Derişim Pilleri"""
    g, y = 740, 250
    s = _baslik(g, "NERNST EŞİTLİĞİ VE DERİŞİM PİLLERİ (25 °C)", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "NERNST EŞİTLİĞİ (Standart Olmayan Koşullar)", [
        "• Çözelti derişimleri 1 M'dan farklı olduğunda",
        "  hücre potansiyeli Nernst eşitliği ile hesaplanır:",
        "• E_pil = E°_pil - (0,0592 / n) · log Q",
        "  (Sorularda genellikle 0,0592 yerine 0,06 alınır).",
        "• n: Alınan/verilen e⁻ sayısı  |  Q = [Ürünler] / [Girenler]"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#fff7ed", "#f97316", "DERİŞİM PİLLERİ (Aynı Tür Elektrotlar, Farklı Derişim)", [
        "• Elektrotlar aynı metalden olduğu için E°_pil = 0 V'tur.",
        "• Derişimi KÜÇÜK (seyreltik) olan kap ANOT,",
        "  derişimi BÜYÜK (derişik) olan kap KATOT olur!",
        "• Zamanla anot derişimi artar, katot derişimi azalır;",
        "  derişimler eşitlendiğinde (M1 = M2) pil DURUR (E = 0)."
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
