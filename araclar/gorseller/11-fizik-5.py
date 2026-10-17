# -*- coding: utf-8 -*-
"""11. Sınıf Fizik — 5. Hafta Görselleri
Konu: İtme ve Çizgisel Momentum: İtme-Momentum Değişimi İlişkisi ve Grafik Analizi
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0284c7", arka="#f0f9ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """İtme (I = F . Delta_t) ve Çizgisel Momentum (P = m . v) Kavramları."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İtme (I) ve Çizgisel Momentum (P) Kavramlarının Karşılaştırılması", "#0284c7", "#f0f9ff")

    # Sol: İtme
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#38bdf8" stroke-width="1.6"/>'
    s += '<rect x="30" y="55" width="335" height="30" rx="10" fill="#0284c7"/>'
    s += '<text x="197" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. İTME (Impulse — Sembol: I)</text>'
    s += '<text x="197" y="106" text-anchor="middle" fill="#0369a1" font-size="14" font-weight="700">I = F_net . Delta_t</text>'
    s += '<text x="48" y="136" fill="#1e293b" font-size="10.5">• Kuvvet ile kuvvetin etki süresinin çarpımıdır.</text>'
    s += '<text x="48" y="158" fill="#1e293b" font-size="10.5">• VEKTÖREL büyüklüktür; yönü F_net ile aynıdır.</text>'
    s += '<text x="48" y="180" fill="#1e293b" font-size="10.5">• SI Birimi: Newton . saniye (N . s)</text>'
    s += '<rect x="48" y="200" width="299" height="66" rx="8" fill="#e0f2fe" stroke="#0284c7"/>'
    s += '<text x="197" y="224" text-anchor="middle" fill="#0369a1" font-size="10.5" font-weight="700">Örnek: Raketin tenis topuna 0,02 saniye</text>'
    s += '<text x="197" y="244" text-anchor="middle" fill="#0369a1" font-size="10.5" font-weight="700">boyunca uyguladığı kuvvetin etkisi.</text>'

    # Sağ: Çizgisel Momentum
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#34d399" stroke-width="1.6"/>'
    s += '<rect x="395" y="55" width="335" height="30" rx="10" fill="#059669"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. ÇİZGİSEL MOMENTUM (Sembol: P)</text>'
    s += '<text x="562" y="106" text-anchor="middle" fill="#065f46" font-size="14" font-weight="700">P = m . v</text>'
    s += '<text x="413" y="136" fill="#1e293b" font-size="10.5">• Kütle ile hız vektörünün çarpımıdır (Hareket miktarı).</text>'
    s += '<text x="413" y="158" fill="#1e293b" font-size="10.5">• VEKTÖREL büyüklüktür; yönü hız (v) ile aynıdır.</text>'
    s += '<text x="413" y="180" fill="#1e293b" font-size="10.5">• SI Birimi: kg . m/s  (1 N . s = 1 kg . m/s)</text>'
    s += '<rect x="413" y="200" width="299" height="66" rx="8" fill="#d1fae5" stroke="#059669"/>'
    s += '<text x="562" y="224" text-anchor="middle" fill="#065f46" font-size="10.5" font-weight="700">Kinetik Enerji ile İlişkisi:</text>'
    s += '<text x="562" y="246" text-anchor="middle" fill="#047857" font-size="11.5" font-weight="700">E_k = P² / (2 . m)</text>'

    return _svg(w, h, s)


def gorsel_2():
    """İtme - Momentum Değişimi Teoremi (I = Delta_P = P_son - P_ilk) ve Vektörel Çıkarma."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İtme - Momentum Değişimi Teoremi: I = Delta_P = P_son - P_ilk", "#7c3aed", "#f5f3ff")

    # Sol: Teorem Türetimi
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#c4b5fd" stroke-width="1.5"/>'
    s += '<text x="197" y="78" text-anchor="middle" fill="#5b21b6" font-size="12" font-weight="700">Newton\'un 2. Yasasından Türetim</text>'

    adimlar = [
        "1) F_net = m . a   ve   a = (v_son - v_ilk) / Delta_t",
        "2) F_net = m . (v_son - v_ilk) / Delta_t",
        "3) F_net . Delta_t = m . v_son - m . v_ilk",
        "4) I = P_son - P_ilk = Delta_P",
    ]
    for i, st in enumerate(adimlar):
        y = 95 + i * 42
        bg = "#ede9fe" if i == 3 else "#f8fafc"
        s += f'<rect x="46" y="{y}" width="303" height="34" rx="6" fill="{bg}" stroke="#8b5cf6"/>'
        s += f'<text x="197" y="{y+22}" text-anchor="middle" fill="#4c1d95" font-size="11" font-weight="700">{st}</text>'

    # Sağ: Duvara Çarpıp Geri Dönen Top Örneği
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#c4b5fd" stroke-width="1.5"/>'
    s += '<text x="562" y="78" text-anchor="middle" fill="#dc2626" font-size="12" font-weight="700">DİKKAT: Duvara Çarpıp Geri Dönen Top!</text>'

    # Duvar ve top
    s += '<rect x="650" y="95" width="18" height="105" fill="#94a3b8" stroke="#475569"/>'
    s += '<circle cx="480" cy="120" r="12" fill="#0284c7"/>'
    s += '<line x1="496" y1="120" x2="625" y2="120" stroke="#0284c7" stroke-width="2.5"/>'
    s += '<text x="560" y="112" text-anchor="middle" fill="#0284c7" font-size="10.5" font-weight="700">P_ilk = +m.v (Sağa)</text>'

    s += '<circle cx="620" cy="175" r="12" fill="#dc2626"/>'
    s += '<line x1="604" y1="175" x2="475" y2="175" stroke="#dc2626" stroke-width="2.5"/>'
    s += '<text x="545" y="167" text-anchor="middle" fill="#dc2626" font-size="10.5" font-weight="700">P_son = -m.v (Sola)</text>'

    s += '<rect x="413" y="208" width="299" height="62" rx="8" fill="#fef2f2" stroke="#dc2626"/>'
    s += '<text x="562" y="230" text-anchor="middle" fill="#991b1b" font-size="10.5" font-weight="700">Vektörel Fark: Delta_P = P_son - P_ilk</text>'
    s += '<text x="562" y="252" text-anchor="middle" fill="#b91c1c" font-size="11.5" font-weight="700">Delta_P = (-m.v) - (+m.v) = -2.m.v  (Sıfır DEĞİL!)</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Net Kuvvet - Zaman (F-t) ve Momentum - Zaman (P-t) Grafikleri."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Grafik Analizi: Kuvvet-Zaman (F-t) Alanı ve Momentum-Zaman (P-t) Eğimi", "#0d9488", "#f0fdfa")

    # Sol: F-t Grafiği
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<text x="197" y="76" text-anchor="middle" fill="#0f766e" font-size="12" font-weight="700">1. Net Kuvvet - Zaman (F - t) Grafiği</text>'
    # Eksenler ve alan
    s += '<line x1="70" y1="210" x2="320" y2="210" stroke="#334155" stroke-width="2"/>'
    s += '<line x1="70" y1="95" x2="70" y2="235" stroke="#334155" stroke-width="2"/>'
    s += '<polygon points="70,210 70,125 200,125 270,210" fill="#99f6e4" stroke="#0d9488" stroke-width="2"/>'
    s += '<text x="165" y="175" text-anchor="middle" fill="#0f766e" font-size="11.5" font-weight="700">ALAN = İTME (I) = Delta_P</text>'
    s += '<text x="197" y="252" text-anchor="middle" fill="#1e293b" font-size="10.2">F-t grafiğinin zaman ekseniyle sınırladığı</text>'
    s += '<text x="197" y="268" text-anchor="middle" fill="#0f766e" font-size="10.5" font-weight="700">cebirsel ALAN, İtme ve Momentum Değişimini verir.</text>'

    # Sağ: P-t Grafiği
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<text x="562" y="76" text-anchor="middle" fill="#0f766e" font-size="12" font-weight="700">2. Momentum - Zaman (P - t) Grafiği</text>'
    s += '<line x1="435" y1="210" x2="685" y2="210" stroke="#334155" stroke-width="2"/>'
    s += '<line x1="435" y1="95" x2="435" y2="235" stroke="#334155" stroke-width="2"/>'
    s += '<line x1="435" y1="190" x2="645" y2="110" stroke="#2563eb" stroke-width="3"/>'
    s += '<text x="565" y="182" text-anchor="middle" fill="#1d4ed8" font-size="11" font-weight="700">EĞİM = Delta_P / Delta_t = F_net</text>'
    s += '<text x="562" y="252" text-anchor="middle" fill="#1e293b" font-size="10.2">P-t grafiğinin EĞİMİ cisme etki eden</text>'
    s += '<text x="562" y="268" text-anchor="middle" fill="#1d4ed8" font-size="10.5" font-weight="700">Net Kuvveti (F_net) verir (P-t ile v-t şekilce aynıdır!).</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Günlük Yaşamda İtme ve Etki Süresi: Hava Yastığı, Kask ve Tampon Tasarımı."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Mühendislik ve Güvenlik: Delta_P Sabitken Etki Süresini (Delta_t) Artırmak", "#d97706", "#fffbeb")

    s += '<rect x="36" y="56" width="688" height="54" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>'
    s += '<text x="380" y="78" text-anchor="middle" fill="#92400e" font-size="13" font-weight="700">Temel İlke:  Delta_P (Momentum Değişimi) SABİT iken;  Delta_t ARTARSA  ==&gt;  F_ort AZALIR!</text>'
    s += '<text x="380" y="98" text-anchor="middle" fill="#b45309" font-size="10.5">Çarpışma süresini uzatan esnek yüzeyler, cisme etki eden yıkıcı darbe kuvvetini küçültür.</text>'

    uygulamalar = [
        ("Otomobil Hava Yastığı", "Kaza anında şişerek sürücünün", "durma süresini (Delta_t) uzatır;", "darbe kuvvetini (F) azaltır.", "#0284c7"),
        ("Katlanabilir Araç Tamponu", "Çarpışmada ezilerek enerji", "sönümler ve etkileşim", "süresini artırır.", "#16a34a"),
        ("Kaleci Eldiveni &amp; Minder", "Topu tutarken elleri geriye", "çekmek veya sünger minder", "etki süresini uzatır.", "#7c3aed"),
        ("Boks Eldiveni &amp; Kask", "Yumruğun veya darbenin", "temas süresini uzatarak", "maksimum kuvveti düşürür.", "#dc2626"),
    ]
    for i, (bas, a1, a2, a3, r) in enumerate(uygulamalar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="124" width="168" height="160" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="124" width="168" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="142" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="182" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="200" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="218" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a3}</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
