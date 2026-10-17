# -*- coding: utf-8 -*-
"""11. Sınıf Akaid - 3. Hafta Görselleri (Akaid İlminin Tanımı, Konusu, Amacı ve Kelamla İlişkisi)"""


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
    """Akaid Kavramının Etimolojisi ve İslam Dininin Üç Temel Boyutu"""
    g, y = 740, 260
    s = _baslik(g, "AKAİD KAVRAMI VE İSLAM DİNİNİN ÜÇ TEMEL BOYUTU", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "AKAİD (Akîde) KAVRAMI", [
        "• Kök: 'A-K-D' (Düğüm atmak, gönülden bağlanmak).",
        "• Tekili: AKÎDE  |  Çoğulu: AKÂİD",
        "• Terim Anlamı: İslam'da kesin olarak inanılması",
        "  farz olan iman esaslarını (inanç hükümlerini)",
        "  ayet ve hadisler ışığında inceleyen ilim dalıdır."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#eff6ff", "#3b82f6", "İSLAM DİNİNİN BÜTÜNLÜĞÜ (Ağaç Metaforu)", [
        "1. İTİKAD (AKAİD / İMAN): Ağacın KÖKLERİDİR.",
        "   Amellerin kabulü sağlam bir akîdeye bağlıdır.",
        "2. İBADET VE MUAMELAT (FIKIH): Ağacın GÖVDESİ",
        "   ve DALLARIDIR (Namaz, oruç, hukuk).",
        "3. AHLAK (TASAVVUF / EDEP): Ağacın MEYVESİDİR."
    ], "#1e40af")
    return _svg(g, y, s)


def gorsel_2():
    """Akaid İlminin Üç Ana Konusu: Usûlü's-Selâse"""
    g, y = 740, 260
    s = _baslik(g, "AKAİD İLMİNİN ÜÇ TEMEL KONUSU: USÛLÜ'S-SELÂSE", "#1d4ed8")
    s += _kutu(18, 52, 228, 190, "#eff6ff", "#3b82f6", "1. İLÂHİYYÂT", [
        "• Yüce Allah'ın varlığı ve",
        "  birliği (Tevhid ilkesi)",
        "• Allah'ın Zâtî ve Sübûtî",
        "  sıfatları ile Esmaülhüsna",
        "• Kader ve kaza inancı"
    ], "#1e3a8a")
    s += _kutu(256, 52, 228, 190, "#fefce8", "#eab308", "2. NÜBÜVVÂT", [
        "• Peygamberlere iman",
        "• Peygamberlerin sıfatları",
        "  (Sıdk, Emanet, Tebliğ,",
        "  Fetanet, İsmet) ve Mucize",
        "• İlahi Kitaplara iman"
    ], "#854d0e")
    s += _kutu(494, 52, 228, 190, "#f0fdf4", "#10b981", "3. SEM'İYYÂT (Uhreviyyât)", [
        "• Yalnızca vahiy (nakil)",
        "  yoluyla bilinebilen gaybî",
        "  konular:",
        "• Melekler, Kabir, Kıyamet,",
        "  Ba's, Haşir, Mizan, Cennet"
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_3():
    """Akaid İlmi ile Kelam İlminin Karşılaştırması"""
    g, y = 740, 260
    s = _baslik(g, "AKAİD İLMİ İLE KELAM İLMİ ARASINDAKİ İLİŞKİ VE FARKLAR", "#6d28d9")
    s += _kutu(20, 52, 340, 190, "#f5f3ff", "#8b5cf6", "AKAİD İLMİ (Betimleyici / Tasvirî)", [
        "• İnanç esaslarını tartışmaya ve felsefi polemiklere",
        "  girmeden açık, sade ve özet hâlde ortaya koyar.",
        "• Temel amacı müminin iman esaslarını doğru öğrenmesi",
        "  ve taklidî imandan tahkikî imana yükselmesidir.",
        "• Örnek: Ebu Hanife'nin 'el-Fıkhu'l-Ekber'i,",
        "  Ömer Nesefî'nin 'Akâidü'n-Nesefî' metni."
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 190, "#fdf4ff", "#d946ef", "KELAM İLMİ (İspatlayıcı ve Savunmacı)", [
        "• Akaid ilkelerini hem naklî (ayet-hadis) hem de",
        "  aklî/mantıkî delillerle (burhan) temellendirir.",
        "• İnkârcı akımlara, yabancı felsefelere ve batıl",
        "  mezheplere karşı İslam inancını savunur.",
        "• Akaid 'inanç metnini' verir; Kelam ise bu metnin",
        "  delillerini ve savunmasını inşa eder."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Akaid İlminin Kaynakları ve Klasik Akaid Metinleri"""
    g, y = 740, 250
    s = _baslik(g, "AKAİD İLMİNİN TEMEL KAYNAKLARI VE KLASİK ESERLERİ", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "AKAİDDE BİLGİ VE DELİL KAYNAKLARI", [
        "1. KUR'AN-I KERİM: Sübutu ve delaleti kesin (muhkem) ayetler.",
        "2. MÜTEVATİR SÜNNET: Yalan üzere birleşmesi imkânsız",
        "   toplulukların naklettiği kesin hadisler.",
        "   (Not: Âhâd haberler tek başına kesin akîde kurmaz.)",
        "3. SELİM AKIL: Vahyi anlayan ve tevhidi kavrayan akıl."
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#fff7ed", "#f97316", "ÖNCÜ ÂLİMLER VE TEMEL AKAİD METİNLERİ", [
        "• İmam-ı Azam Ebu Hanife (ö. 767) -> el-Fıkhu'l-Ekber",
        "• İmam Tahâvî (ö. 933) -> el-Akîdetü't-Tahâviyye",
        "• İmam Mâtürîdî (ö. 944) -> Kitâbü't-Tevhîd",
        "• Ömer en-Nesefî (ö. 1142) -> Metnü'l-Akâid (Nesefî Akaidi)",
        "• Sirâceddin el-Ûşî (ö. 1179) -> Kasîdetü'l-Emâlî"
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