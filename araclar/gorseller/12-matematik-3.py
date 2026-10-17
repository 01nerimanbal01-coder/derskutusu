# -*- coding: utf-8 -*-
"""12. Sınıf Matematik - 3. Hafta Görselleri (Logaritma Fonksiyonunun Özellikleri, Taban Değiştirme ve Denklemler)"""


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
    """Logaritma Fonksiyonunun Temel Özellikleri (Çarpım, Bölüm ve Kuvvet Kuralları)"""
    g, y = 740, 265
    s = _baslik(g, "LOGARİTMA FONKSİYONUNUN TEMEL ÖZELLİKLERİ (a > 0, a ≠ 1)", "#1d4ed8")
    s += _kutu(20, 52, 340, 195, "#eff6ff", "#3b82f6", "TEMEL VE ÇARPIM / BÖLÜM KURALLARI", [
        "1) log_a(1) = 0   ve   log_a(a) = 1",
        "   ln(1) = 0, ln(e) = 1  |  log(1) = 0, log(10) = 1",
        "2) Çarpımın Logaritması (Toplama dönüşür):",
        "   log_a(x · y) = log_a(x) + log_a(y)",
        "3) Bölümün Logaritması (Farka dönüşür):",
        "   log_a(x / y) = log_a(x) - log_a(y)"
    ], "#1e3a8a")
    s += _kutu(380, 52, 340, 195, "#f0fdf4", "#16a34a", "KUVVET VE ÜS ÖZELLİKLERİ", [
        "4) Üssün Başa Çarpan İnişi:",
        "   log_a(x^n) = n · log_a(x)",
        "5) Hem Tabanın Hem İçerinin Üssü:",
        "   log_(a^m)(x^n) = (n / m) · log_a(x)",
        "6) Üstteki Logaritmada Yer Değiştirme:",
        "   a^(log_b(c)) = c^(log_b(a))  ve  a^(log_a(x)) = x"
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_2():
    """Taban Değiştirme Kuralı ve Zincirleme Çarpım Sonuçları"""
    g, y = 740, 255
    s = _baslik(g, "TABAN DEĞİŞTİRME KURALI VE ÖNEMLİ SONUÇLARI", "#0f766e")
    s += _kutu(20, 52, 340, 185, "#ecfdf5", "#10b981", "TABAN DEĞİŞTİRME FORMÜLÜ", [
        "• a tabanındaki log_a(b) ifadesini c tabanına çevirme:",
        "  log_a(b) = log_c(b) / log_c(a)",
        "• 10 tabanında: log_a(b) = log(b) / log(a)",
        "• Doğal tabanda (e): log_a(b) = ln(b) / ln(a)",
        "• Ters Çevirme Sonucu: log_a(b) = 1 / log_b(a)"
    ], "#065f46")
    s += _kutu(380, 52, 340, 185, "#fefce8", "#eab308", "ZİNCİRLEME ÇARPIM VE GENİŞLETME", [
        "1) Çarpımsal Terslik:",
        "   log_a(b) · log_b(a) = 1",
        "2) Zincirleme Sadeleşme Kuralı:",
        "   log_a(b) · log_b(c) · log_c(d) = log_a(d)",
        "3) Aynı Kuvvetle Genişletme / Sadeleştirme:",
        "   log_a(b) = log_(a^k)(b^k)"
    ], "#854d0e")
    return _svg(g, y, s)


def gorsel_3():
    """Sık Yapılan Logaritma Hataları (Uyarı Tablosu)"""
    g, y = 740, 250
    s = _baslik(g, "DİKKAT: LOGARİTMADA EN SIK YAPILAN KAVRAM YANILGILARI!", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "YANLIŞ KULLANIMLAR (ASLA YAPMAYIN!)", [
        "• YANLIŞ: log_a(x + y) ≠ log_a(x) + log_a(y)",
        "• YANLIŞ: log_a(x - y) ≠ log_a(x) - log_a(y)",
        "  (Toplamın veya farkın logaritması parçalanamaz!)",
        "• YANLIŞ: (log_a(x)) / (log_a(y)) ≠ log_a(x - y)",
        "• YANLIŞ: (log_a(x))^n ≠ n · log_a(x)"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#ecfdf5", "#10b981", "DOĞRU KARŞILIKLARI", [
        "• DOĞRU: log_a(x · y) = log_a(x) + log_a(y)",
        "• DOĞRU: log_a(x / y) = log_a(x) - log_a(y)",
        "• DOĞRU: (log_a(x)) / (log_a(y)) = log_y(x)",
        "  (Bölüm şeklindeki iki logaritma taban değiştirmedir!)",
        "• DOĞRU: log_a(x^n) = n · log_a(x)"
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_4():
    """Basamak Sayısı Bulma ve Logaritmik Büyüklük Sıralaması"""
    g, y = 740, 245
    s = _baslik(g, "10 TABANINDA LOGARİTMA İLE BASAMAK SAYISI BULMA", "#6d28d9")
    s += _kutu(20, 52, 340, 175, "#f5f3ff", "#8b5cf6", "TAM KISIM (KARAKTERİSTİK) VE BASAMAK SAYISI", [
        "• A > 1 bir doğal sayı olmak üzere:",
        "  log(A) = n,xyz... ise A sayısı (n + 1) BASAMAKLIDIR!",
        "• Formül: Basamak Sayısı = Tam Değer[log(A)] + 1",
        "• Örnek: log(2) ≈ 0,301 ise 2^100 sayısının basamak sayısı:",
        "  log(2^100) = 100 · 0,301 = 30,1 -> 30 + 1 = 31 basamaklı!"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 175, "#fdf4ff", "#d946ef", "LOGARİTMALI İFADELERDE ARALIK BULMA", [
        "• x = log_a(b) sayısının hangi iki tam sayı arasında",
        "  olduğunu bulmak için b sayısı a'nın ardışık iki",
        "  tam sayı kuvveti arasına sıkıştırılır:",
        "• Örnek: x = log_3(50) için 3^3 = 27 < 50 < 81 = 3^4",
        "  olduğundan 3 < log_3(50) < 4 bulunur."
    ], "#86198f")
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
