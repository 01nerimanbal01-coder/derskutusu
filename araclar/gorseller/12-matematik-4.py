# -*- coding: utf-8 -*-
"""12. Sınıf Matematik — 4. Hafta görsel modülü: Üstel ve Logaritmik Denklemler ve Eşitsizlikler."""


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
        'text-anchor="middle">ÜSTEL VE LOGARİTMİK DENKLEMLERİN ÇÖZÜM YÖNTEMLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Üstel Denklemler", [
        "• a &gt; 0 ve a ≠ 1 olmak üzere:",
        "  a^f(x) = a^g(x)  &lt;=&gt;  f(x) = g(x)",
        "• Tabanlar eşitlenemiyorsa: a^f(x) = b  &lt;=&gt;  f(x) = log_a(b)",
        "• a^(2x) + p·a^x + q = 0 tipinde a^x = t (t &gt; 0)",
        "  değişken değiştirmesi yapılır",
        "• Negatif t kökleri üstel fonksiyonu sağlamaz!"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Logaritmik Denklemler", [
        "• log_a(f(x)) = c  &lt;=&gt;  f(x) = a^c",
        "• log_a(f(x)) = log_a(g(x))  &lt;=&gt;  f(x) = g(x)",
        "• ALTIN KURAL (Tanım Kümesi Kontrolü):",
        "  Bulunan her kök için mutlaka:",
        "  1) İç kısım: f(x) &gt; 0 ve g(x) &gt; 0",
        "  2) Taban: a &gt; 0 ve a ≠ 1 şartları kontrol edilir!"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">ÜSTEL VE LOGARİTMİK EŞİTSİZLİKLERDE TABAN KURALI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#d97706", "Durum 1: Taban a &gt; 1 (Artan Fonksiyon)", [
        "• Fonksiyon artan olduğundan eşitsizlik",
        "  YÖN DEĞİŞTİRMEZ!",
        "• Üstel: a^f(x) &lt; a^g(x)  &lt;=&gt;  f(x) &lt; g(x)",
        "• Logaritmik: log_a(f(x)) &lt; log_a(g(x))",
        "  &lt;=&gt;  0 &lt; f(x) &lt; g(x)",
        "• Örnek: log_3(x - 2) &lt; 2  =&gt;  0 &lt; x - 2 &lt; 9  =&gt;  2 &lt; x &lt; 11"
    ])
    ic += _kart(395, 50, 340, 175, "#8b5cf6", "Durum 2: Taban 0 &lt; a &lt; 1 (Azalan Fonksiyon)", [
        "• Fonksiyon azalan olduğundan eşitsizlik",
        "  YÖN DEĞİŞTİRİR!",
        "• Üstel: a^f(x) &lt; a^g(x)  &lt;=&gt;  f(x) &gt; g(x)",
        "• Logaritmik: log_a(f(x)) &lt; log_a(g(x))",
        "  &lt;=&gt;  f(x) &gt; g(x) &gt; 0",
        "• Örnek: log_(1/2)(x - 1) &gt; 3 =&gt; 0 &lt; x - 1 &lt; (1/2)³"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">GERÇEK HAYAT PROBLEMLERİ 1: DEPREM, SES VE pH ÖLÇEKLERİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Richter Ölçeği (Deprem)", [
        "• R = log(I / I₀)",
        "  R: Deprem büyüklüğü",
        "  I: Deprem yoğunluğu",
        "  I₀: Standart sarsıntı",
        "• Büyüklüğü 1 birim artan",
        "  depremin şiddeti 10 kat artar"
    ])
    ic += _kart(268, 50, 225, 175, "#ec4899", "Ses Şiddeti (Desibel - dB)", [
        "• L = 10 · log(I / I₀)",
        "  L: Ses düzeyi (dB)",
        "  I: Ses şiddeti (W/m²)",
        "  I₀ = 10⁻¹² W/m² (Eşik)",
        "• Ses şiddeti 10 katına çıkarsa",
        "  ses düzeyi 10 dB artar"
    ])
    ic += _kart(510, 50, 225, 175, "#14b8a6", "pH ve pOH Ölçeği (Kimya)", [
        "• pH = -log[H⁺]",
        "• pOH = -log[OH⁻]",
        "• 25 °C'de: pH + pOH = 14",
        "• [H⁺] = 10⁻³ M ise pH = 3",
        "• pH &lt; 7 asidik, pH = 7 nötr,",
        "  pH &gt; 7 bazik çözeltidir"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">GERÇEK HAYAT PROBLEMLERİ 2: ÜSTEL BÜYÜME VE BOZUNMA</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Nüfus Artışı ve Bileşik Faiz (Üstel Büyüme)", [
        "• Sürekli büyüme modeli: N(t) = N₀ · e^(k·t)",
        "  N₀: Başlangıç miktarı, k &gt; 0: Büyüme hızı sabiti",
        "• Yıllık artış modeli: A(t) = A₀ · (1 + r)^t",
        "• Bakteri çoğalması: Her periyotta 2 katına çıkarsa",
        "  N(t) = N₀ · 2^(t / T)",
        "• Geçen süre t'yi bulmak için her iki tarafın ln'i alınır"
    ])
    ic += _kart(395, 50, 340, 175, "#0ea5e9", "Radyoaktif Bozunma ve Yarı Ömür (Azalma)", [
        "• Bozunma modeli: M(t) = M₀ · e^(-k·t)",
        "• Yarılanma süresi (T_1/2) modeli:",
        "  M(t) = M₀ · (1/2)^(t / T_1/2)",
        "• Karbon-14 (C-14) testi ile fosil yaş tayini yapılır",
        "• Newton'un Soğuma Yasası:",
        "  T(t) = T_ortam + (T₀ - T_ortam) · e^(-k·t)"
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