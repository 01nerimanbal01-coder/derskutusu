# -*- coding: utf-8 -*-
"""12. Sınıf Fizik — 4. Hafta görsel modülü: Açısal Momentum ve Korunumu."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">AÇISAL MOMENTUM (L) BAĞINTILARI VE SAĞ EL KURALI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Açısal Momentum Formülleri", [
        "• Vektörel büyüklüktür, L ile gösterilir",
        "• SI birimi: kg·m²/s veya J·s (N·m·s)",
        "• Çizgisel momentumla: L = r · p = m · v · r",
        "• Eylemsizlik momentiyle: L = I · ω",
        "• v = ω · r ve I = m · r² bağıntıları birbirine",
        "  dönüştürülerek tüm dönen sistemlere uygulanır"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Açısal Momentumun Yönü (Sağ El Kuralı)", [
        "• Dört parmak: Dönme yönünü (ω ve v) gösterir",
        "• Avuç içi: Dönme merkezine (O noktasına) bakar",
        "• Açılan başparmak: Açısal momentumun (L) yönüdür",
        "• L vektörü, dönme düzlemine daima diktir",
        "• Açısal hız (ω) ile açısal momentum (L)",
        "  her zaman aynı yönlüdür"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">TORK - AÇISAL İVME VE AÇISAL MOMENTUM İLİŞKİSİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Net Tork ve Açısal İvme (α)", [
        "• Açısal ivme (α): Birim zamandaki açısal hız",
        "  değişimidir -> α = Δω / Δt (rad/s²)",
        "• Çizgisel ivme ile ilişkisi: a = α · r",
        "• Dönme hareketinin temel dinamiği: τ_net = I · α",
        "• Net tork sıfırdan farklıysa cisim açısal",
        "  ivme kazanır (hızlanır veya yavaşlar)"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Tork ve Açısal Momentum Değişimi", [
        "• Çizgisel harekette: F_net = ΔP / Δt",
        "• Dönme hareketinde: τ_net = ΔL / Δt",
        "• Birim zamandaki açısal momentum değişimi",
        "  sisteme etkiyen net dış torka eşittir",
        "• Tork açısal hızla aynı yönlüyse L artar,",
        "  zıt yönlüyse L azalır"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">AÇISAL MOMENTUMUN KORUNUMU (τ_dış = 0)</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Korunum Şartı", [
        "• Sisteme etki eden net dış",
        "  tork sıfırsa: τ_net = 0",
        "• ΔL = 0 -> L_ilk = L_son",
        "• I₁ · ω₁ = I₂ · ω₂",
        "• Açısal momentumun büyüklüğü",
        "  ve yönü sabit kalır"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Kollarını Kapatan Patenci", [
        "• Kollar kapatıldığında kütle",
        "  dönme eksenine yaklaşır (r ↓)",
        "• Eylemsizlik momenti azalır (I ↓)",
        "• L sabit kaldığından açısal",
        "  hız artar (ω ↑)",
        "• Dönme kinetik enerjisi artar"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "Gezegenlerin Hareketi", [
        "• Kütle çekim kuvveti Güneş",
        "  merkezinden geçer (τ = 0)",
        "• Gezegen Güneş'e yaklaşırken:",
        "  r azalır -> I azalır -> v ve ω artar",
        "• L = m · v · r her noktada",
        "  korunur ve eşittir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">ÖTELEME VE DÖNME DİNAMİĞİ BÜYÜKLÜKLERİNİN ANALOJİSİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Öteleme (Çizgisel) Hareket", [
        "• Kütle (Eylemsizlik ölçüsü): m (kg)",
        "• Çizgisel hız ve ivme: v (m/s), a (m/s²)",
        "• Kuvvet: F = m · a (N)",
        "• Çizgisel momentum: P = m · v (kg·m/s)",
        "• İtme - Momentum: F · Δt = ΔP",
        "• Öteleme kinetik enerjisi: E_k = (1/2) · m · v²"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Dönme (Açısal) Hareket", [
        "• Eylemsizlik momenti: I = Σ m·r² (kg·m²)",
        "• Açısal hız ve ivme: ω (rad/s), α (rad/s²)",
        "• Tork (Döndürme etkisi): τ = I · α (N·m)",
        "• Açısal momentum: L = I · ω (kg·m²/s)",
        "• Açısal itme: τ · Δt = ΔL",
        "• Dönme kinetik enerjisi: E_d = (1/2) · I · ω² = L²/(2I)"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]
