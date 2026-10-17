# -*- coding: utf-8 -*-
"""11. Sınıf Hitabet ve Mesleki Uygulama - 3. Hafta Görselleri (Ülkemizde Din Hizmetleri ve DİB)"""


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
    """Diyanet İşleri Başkanlığının Kuruluşu, Yasal Dayanağı ve Görevleri"""
    g, y = 740, 260
    s = _baslik(g, "DİYANET İŞLERİ BAŞKANLIĞI (DİB): KURULUŞU VE ANAYASAL KONUMU", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "TARİHÇE VE YASAL DAYANAK", [
        "• Osmanlı'da: Şeyhülislamlık (Meşihat) ve",
        "  1920'de Şer'iyye ve Evkaf Vekâleti.",
        "• Kuruluş: 3 Mart 1924 (429 sayılı Kanun).",
        "• İlk Başkan: Ankara Müftüsü Rıfat BÖREKÇİ.",
        "• Anayasa Md. 136: Genel idare içinde yer alır;",
        "  633 sayılı Kuruluş ve Görevleri Hakkında Kanun."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#eff6ff", "#3b82f6", "BAŞKANLIĞIN 3 TEMEL YASAL GÖREVİ", [
        "1. İslam dininin İNANÇ, İBADET ve AHLAK",
        "   esasları ile ilgili işleri yürütmek,",
        "2. Din konusunda TOPLUMU AYDINLATMAK",
        "   (sahih dini bilgi üretmek ve yaymak),",
        "3. İBADET YERLERİNİ (camileri ve mescitleri)",
        "   yönetmek."
    ], "#1e40af")
    return _svg(g, y, s)


def gorsel_2():
    """Cami İçi Din Hizmetleri ve Görevlileri"""
    g, y = 740, 260
    s = _baslik(g, "CAMİ İÇİ DİN HİZMETLERİ VE DİN GÖREVLİLERİ", "#1d4ed8")
    s += _kutu(18, 52, 228, 190, "#eff6ff", "#3b82f6", "İMAM-HATİP", [
        "• Mihrapta vakit, cuma, bayram",
        "  ve teravih namazlarını",
        "  kıldırır (İmamlık).",
        "• Minberde cuma ve bayram",
        "  HUTBELERİNİ okur (Hatiplik).",
        "• Cemaate rehberlik eder."
    ], "#1e3a8a")
    s += _kutu(256, 52, 228, 190, "#fefce8", "#eab308", "MÜEZZİN-KAYYIM", [
        "• Ezan okur, kamet getirir,",
        "  tesbihat ve sala okur",
        "  (Müezzinlik).",
        "• Caminin bakım, temizlik,",
        "  düzen ve güvenliğini",
        "  sağlar (Kayyımlık)."
    ], "#854d0e")
    s += _kutu(494, 52, 228, 190, "#f0fdf4", "#10b981", "VAİZ VE K.K. ÖĞRETİCİSİ", [
        "• VAİZ: Kürsüde cemaate dini",
        "  ve ahlaki konularda",
        "  sohbet/vaaz verir.",
        "• KUR'AN KURSU ÖĞRETİCİSİ:",
        "  4-6 yaş, yetişkin ve hafızlık",
        "  kurslarında eğitim verir."
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_3():
    """Cami Dışı Din Hizmetleri: Manevi Danışmanlık ve Rehberlik"""
    g, y = 740, 260
    s = _baslik(g, "CAMİ DIŞI DİN HİZMETLERİ: MANEVİ DANIŞMANLIK VE REHBERLİK", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "KURUMSAL MANEVİ DESTEK HİZMETLERİ", [
        "1. HASTANELER: Hasta ve hasta yakınlarına",
        "   moral ve manevi destek (teselli ve dua).",
        "2. CEZA İNFAZ KURUMLARI: Tutuklu ve hükümlülerin",
        "   ıslahı ve topluma yeniden kazandırılması.",
        "3. ÇOCUK EVLERİ, HUZUREVLERİ VE KYK YURTLARI:",
        "   Yaşlılara, kimsesiz çocuklara ve gençlere rehberlik."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "AİLE, FETVA VE YURT DIŞI HİZMETLERİ", [
        "• AİLE VE DİNÎ REHBERLİK BÜROLARI (ADRB):",
        "  Aile kurumunu koruma ve danışmanlık.",
        "• DİN İŞLERİ YÜKSEK KURULU & ALO 190 FETVA HATTI:",
        "  Vatandaşların dini sorularını cevaplandırma.",
        "• YURT DIŞI TEŞKİLATI: Müşavirlik ve ataşelikler",
        "  aracılığıyla yurt dışındaki vatandaşlarımıza hizmet."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Merkez ve Taşra Teşkilatı Yapısı"""
    g, y = 740, 245
    s = _baslik(g, "DİYANET İŞLERİ BAŞKANLIĞI TEŞKİLAT YAPISI", "#b91c1c")
    s += _kutu(20, 52, 340, 175, "#fef2f2", "#ef4444", "MERKEZ TEŞKİLATI (Ankara)", [
        "• Diyanet İşleri Başkanı ve Başkan Yardımcıları",
        "• Din İşleri Yüksek Kurulu (En üst karar ve danışma organı)",
        "• Din Hizmetleri Genel Müdürlüğü",
        "• Eğitim Hizmetleri / Hac ve Umre / Dini Yayınlar",
        "• Dış İlişkiler ve İnsan Kaynakları Genel Müdürlükleri"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 175, "#fff7ed", "#f97316", "TAŞRA VE YURT DIŞI TEŞKİLATI", [
        "• TAŞRA TEŞKİLATI: 81 İl Müftülüğü, İlçe Müftülükleri",
        "  ve Dini Yüksek İhtisas / Diyanet Akademisi Merkezleri.",
        "• YURT DIŞI TEŞKİLATI: Büyükelçiliklerde Din Hizmetleri",
        "  Müşavirlikleri, Başkonsolosluklarda Ataşelikler.",
        "• Türkiye Diyanet Vakfı (TDV - 1975): Hayır ve eğitim desteği."
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
