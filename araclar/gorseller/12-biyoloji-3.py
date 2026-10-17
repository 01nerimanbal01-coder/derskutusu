# -*- coding: utf-8 -*-
"""12. Sınıf Biyoloji - 3. Hafta Görselleri (Genetik Şifre, Santral Dogma ve Protein Sentezi)"""


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
    """Genetik Şifre (Kod - Kodon - Antikodon) ve 64 Kodon Dağılımı"""
    g, y = 740, 265
    s = _baslik(g, "GENETİK ŞİFRE SİSTEMİ: KOD, KODON VE ANTİKODON (4³ = 64 ŞİFRE)", "#0f766e")
    s += _kutu(18, 52, 228, 195, "#ecfdf5", "#10b981", "1. GENETİK KOD (DNA)", [
        "• DNA'nın kalıp (anlamlı)",
        "  ipliği üzerindeki üçlü",
        "  nükleotit dizisidir.",
        "• 4 çeşit nükleotitten",
        "  4³ = 64 çeşit üçlü şifre",
        "  (kod) oluşur (Örn: TAC)."
    ], "#065f46")
    s += _kutu(256, 52, 228, 195, "#eff6ff", "#3b82f6", "2. KODON (mRNA)", [
        "• mRNA üzerindeki üçlü",
        "  nükleotit dizisidir (64 çeşit).",
        "• Başlangıç Kodonu: AUG",
        "  (Metiyonin şifreler - 1 adet).",
        "• Durdurucu Kodonlar: UAA,",
        "  UAG, UGA (Amino asit şifrelemez!)"
    ], "#1e3a8a")
    s += _kutu(494, 52, 228, 195, "#fefce8", "#eab308", "3. ANTİKODON (tRNA)", [
        "• tRNA'nın mRNA kodonunu",
        "  tanıyan üçlü nükleotit ucudur.",
        "• 3 durdurucu kodonun",
        "  antikodon karşılığı YOKTUR!",
        "• Bu nedenle hücrede en fazla",
        "  64 - 3 = 61 çeşit tRNA vardır."
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_2():
    """Santral Dogma Süreci: Replikasyon, Transkripsiyon ve Translasyon"""
    g, y = 740, 260
    s = _baslik(g, "SANTRAL DOGMA: GENETİK BİLGİNİN TEK YÖNLÜ AKIŞI", "#1d4ed8")
    s += _kutu(18, 52, 228, 190, "#eff6ff", "#3b82f6", "1. REPLİKASYON (DNA -> DNA)", [
        "• Yalnız bölünecek hücrelerde",
        "  interfazda gerçekleşir.",
        "• Enzim: DNA Polimeraz",
        "• Harcanan: Deoksiribonükleotit",
        "  (A, T, G, C) ve ATP",
        "• Hata olursa kalıtsal olabilir!"
    ], "#1e3a8a")
    s += _kutu(256, 52, 228, 190, "#f0fdf4", "#16a34a", "2. TRANSKRİPSİYON (DNA->mRNA)", [
        "• Yazılım / Okuma evresidir.",
        "• DNA'nın yalnız ilgili GEN",
        "  bölgesi açılır.",
        "• Enzim: RNA Polimeraz",
        "• Harcanan: Ribonükleotit",
        "  (A, U, G, C) ve ATP."
    ], "#14532d")
    s += _kutu(494, 52, 228, 190, "#f5f3ff", "#8b5cf6", "3. TRANSLASYON (mRNA->Protein)", [
        "• Okunan şifrenin RİBOZOMDA",
        "  proteine çevrilmesidir.",
        "• Tüm canlılarda RİBOZOM",
        "  organelinde gerçekleşir.",
        "• Harcanan: Amino asit ve ATP;",
        "  peptit bağı kurulur (+Su)."
    ], "#5b21b6")
    return _svg(g, y, s)


def gorsel_3():
    """Prokaryot ve Ökaryot Hücrede Santral Dogma Olaylarının Gerçekleştiği Yerler"""
    g, y = 740, 250
    s = _baslik(g, "PROKARYOT VE ÖKARYOT HÜCREDE OLAYLARIN GERÇEKLEŞTİĞİ YERLER", "#6d28d9")
    s += _kutu(20, 52, 340, 180, "#f5f3ff", "#8b5cf6", "PROKARYOT HÜCRE (Bakteri ve Arke)", [
        "• Replikasyon (DNA Eşlenmesi): SİTOPLAZMA",
        "• Transkripsiyon (mRNA Sentezi): SİTOPLAZMA",
        "• Translasyon (Protein Sentezi): RİBOZOM (Sitoplazmada)",
        "• Çekirdek zarı olmadığı için transkripsiyon ve",
        "  translasyon sitoplazmada eş zamanlı başlayabilir."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 180, "#fdf4ff", "#d946ef", "ÖKARYOT HÜCRE (Bitki, Hayvan, Mantar, Protista)", [
        "• Replikasyon: ÇEKİRDEK, MİTOKONDRİ ve KLOROPLAST",
        "• Transkripsiyon: ÇEKİRDEK, MİTOKONDRİ ve KLOROPLAST",
        "• Translasyon: RİBOZOM (Sitoplazma, granüllü ER,",
        "  çekirdek dış zarı, mitokondri ve kloroplast içindeki",
        "  ribozomlarda gerçekleşir)."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Polizom (Poliribozom) Yapısı ve Biyolojik Avantajı"""
    g, y = 740, 245
    s = _baslik(g, "POLİZOM (POLİRİBOZOM) VE BİR GEN - BİR POLİPEPTİT HİPOTEZİ", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "POLİZOM (POLİRİBOZOM) NEDİR?", [
        "• Tek bir mRNA molekülünün birden fazla ribozom",
        "  tarafından peş peşe okunmasıyla oluşan yapıdır.",
        "• Amaç: Aynı çeşit proteinden KISA SÜREDE ve",
        "  ENERJİ TASARRUFUYLA çok sayıda üretmektir!",
        "• Üretilen tüm proteinlerin amino asit dizilimi AYNIDIR."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#fff7ed", "#f97316", "BEADLE VE TATUM: BİR GEN - BİR POLİPEPTİT", [
        "• Neurospora crassa (ekmek küfü) deneyleriyle",
        "  her genin belirli bir enzimin (polipeptidin) sentezinden",
        "  sorumlu olduğu kanıtlanmıştır.",
        "• Gen 1 -> Enzim 1 -> Öncül Maddeyi Ornitine çevirir",
        "• Gen 2 -> Enzim 2 -> Ornitini Sitrüline -> Arjinine çevirir."
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
