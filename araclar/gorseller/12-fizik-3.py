# -*- coding: utf-8 -*-
"""12. Sınıf Fizik - 3. Hafta Görselleri (Dönerek Öteleme Hareketi, Eylemsizlik Momenti ve Dönme Kinetik Enerjisi)"""


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
    """Kaymadan Dönerek Öteleme Hareketinde Anlık Hız Vektörleri (K, O, L, M, N noktaları)"""
    g, y = 740, 275
    s = _baslik(g, "KAYMADAN DÖNEREK ÖTELEME: ÖTELEME + DÖNME = ANLIK YERE GÖRE HIZ", "#1d4ed8")
    s += _kutu(16, 52, 226, 205, "#eff6ff", "#3b82f6", "1. SAF ÖTELEME HIZI", [
        "• Tekerlek üzerindeki her",
        "  noktanın öteleme hızı",
        "  kütle merkezinin hızına (v)",
        "  yön ve büyüklükçe EŞİTTİR:",
        "• v_K = v_O = v_L = v_M = v",
        "  (Hepsi sağa doğru +x yönünde)"
    ], "#1e3a8a")
    s += _kutu(257, 52, 226, 205, "#fefce8", "#eab308", "2. SAF DÖNME HIZI", [
        "• Merkezde (O) dönme hızı: 0",
        "• Çember üzerindeki noktalarda",
        "  yarıçapa dik ve büyüklüğü v:",
        "• Üstte (K): sağa doğru (+v)",
        "• Altta (M): sola doğru (-v)",
        "• Yanda (L, N): düşey yönde (v)"
    ], "#854d0e")
    s += _kutu(498, 52, 226, 205, "#ecfdf5", "#10b981", "3. YERE GÖRE ANLIK HIZ", [
        "(Vektörel Toplam: v_öt + v_dön)",
        "• En Üst Nokta (K): v_K = 2v",
        "• Kütle Merkezi (O): v_O = v",
        "• Yan Noktalar (L, N): v·kök(2)",
        "• Yere Değme Noktası (M): v_M = 0",
        "• Genel Formül: v_X = ω · d_M"
    ], "#065f46")
    return _svg(g, y, s)


def gorsel_2():
    """Eylemsizlik Momenti (I = Σ m·r²) Kavramı ve Geometrik Cisimlerin Karşılaştırması"""
    g, y = 740, 260
    s = _baslik(g, "EYLEMSİZLİK MOMENTİ (I): DÖNME HAREKETİNE KARŞI DİRENÇ", "#0f766e")
    s += _kutu(20, 52, 340, 190, "#ecfdf5", "#10b981", "EYLEMSİZLİK MOMENTİ (I) NEDİR?", [
        "• Cismin dönme hareketindeki değişikliğe karşı",
        "  gösterdiği direncin ölçüsüdür (Skaler büyüklüktür).",
        "• SI Birimi: kg · m²  |  Temel Bağıntı: I = Σ m · r²",
        "• Bağlı Olduğu 3 Değişken:",
        "  1) Cismin kütlesi (m),  2) Dönme ekseninin yeri,",
        "  3) Kütle dağılımı (eksenden uzaklık r arttıkça I artar!)."
    ], "#065f46")
    s += _kutu(380, 52, 340, 190, "#eff6ff", "#3b82f6", "AYNI m VE r İÇİN EYLEMSİZLİK MOMENTİ SIRALAMASI", [
        "• İçi Boş Çember / Halka: I = m · r²  (En Büyük!)",
        "• İçi Dolu Silindir / Disk: I = (1/2) · m · r²",
        "• İçi Dolu Küre: I = (2/5) · m · r²  (En Küçük!)",
        "• İnce Çubuk (Ortasından): I = (1/12) · m · L²",
        "• İnce Çubuk (Ucundan): I = (1/3) · m · L²",
        "• Kütle merkezden dışa doğru toplandıkça I büyür!"
    ], "#1e3a8a")
    return _svg(g, y, s)


def gorsel_3():
    """Dönme Kinetik Enerjisi ve Toplam Kinetik Enerji"""
    g, y = 740, 255
    s = _baslik(g, "DÖNME VE DÖNEREK ÖTELEME KİNETİK ENERJİSİ", "#6d28d9")
    s += _kutu(20, 52, 340, 185, "#f5f3ff", "#8b5cf6", "1. DÖNME KİNETİK ENERJİSİ (E_dönme)", [
        "• Sabit bir eksen etrafında ω açısal hızıyla dönen",
        "  cismin sahip olduğu kinetik enerjidir:",
        "• E_dönme = (1/2) · I · ω²   (Birim: Joule - J)",
        "• Öteleme ile Benzerlik:",
        "  Kütle (m) <-> Eylemsizlik Momenti (I)",
        "  Çizgisel Hız (v) <-> Açısal Hız (ω)"
    ], "#5b21b6")
    s += _kutu(380, 52, 340, 185, "#fdf4ff", "#d946ef", "2. TOPLAM KİNETİK ENERJİ (Dönerek Öteleme)", [
        "• Hem öteleme hem dönme yapan tekerlek/kürenin",
        "  toplam kinetik enerjisi iki enerjinin toplamıdır:",
        "• E_toplam = E_öteleme + E_dönme",
        "• E_toplam = (1/2) · m · v² + (1/2) · I · ω²",
        "• Kaymadan dönmede v = ω · r yazılabilir."
    ], "#86198f")
    return _svg(g, y, s)


def gorsel_4():
    """Eğik Düzlemden Yuvarlanan Cisimlerin Yarışı (Küre, Disk, Çember)"""
    g, y = 740, 250
    s = _baslik(g, "EĞİK DÜZLEMDEN KAYMADAN YUVARLANAN CİSİMLERİN YARIŞI", "#b91c1c")
    s += _kutu(20, 52, 340, 180, "#fef2f2", "#ef4444", "ENERJİ KORUNUMU ANALİZİ", [
        "• h yüksekliğinden serbest bırakılan cisimde:",
        "  m · g · h = (1/2) · m · v² + (1/2) · I · ω²",
        "• Eylemsizlik momenti (I) KÜÇÜK olan cisim,",
        "  potansiyel enerjisinin daha büyük kısmını",
        "  ÖTELEME hızına (v) dönüştürür ve yarışı kazanır!"
    ], "#991b1b")
    s += _kutu(380, 52, 340, 180, "#fff7ed", "#f97316", "BİTİŞ ÇİZGİSİNE VARIŞ SIRALAMASI", [
        "• Eylemsizlik Momentleri: I_halka > I_disk > I_küre",
        "• Tabandaki Öteleme Hızları: v_küre > v_disk > v_halka",
        "• İniş Süreleri: t_küre < t_disk < t_halka",
        "• Sonuç: Eğik düzlemden aynı anda bırakılan içi dolu",
        "  KÜRE 1., DİSK (SİLİNDİR) 2., HALKA (ÇEMBER) 3. olur!"
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
