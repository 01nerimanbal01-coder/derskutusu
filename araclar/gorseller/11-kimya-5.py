# -*- coding: utf-8 -*-
"""11. Sınıf Kimya — 5. Hafta Görselleri
Konu: Tepkime Isılarının Toplanabilirliği (Hess Yasası) ve Kimyasal Tepkimelerde Çarpışma Teorisi
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#7c3aed", arka="#f5f3ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Hess Yasası (Tepkime Isılarının Toplanabilirliği) 3 Altın Kural."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Hess Yasası: Tepkime Entalpilerinin (Delta_H) Toplanabilirliği Kuralları", "#7c3aed", "#f5f3ff")

    kurallar = [
        ("1. Tepkime Ters Çevrilirse", "Girenler ve ürünler yer", "değiştirdiğinde Delta_H", "İŞARET DEĞİŞTİRİR!", "A -> B   (Delta_H = -100 kJ)", "B -> A   (Delta_H = +100 kJ)", "#dc2626", "#fef2f2"),
        ("2. Katsayı İle Çarpılır/Bölünürse", "Denklem hangi pozitif sayıyla", "(k) çarpılır veya bölünürse,", "Delta_H da k ile ÇARPILIR!", "A -> B   (Delta_H = -100 kJ)", "2A -> 2B (Delta_H = -200 kJ)", "#0284c7", "#f0f9ff"),
        ("3. Ara Basamaklar Toplanırsa", "Ara tepkimeler taraf tarafa", "toplandığında net tepkimenin", "entalpisi CEBİRSEL TOPLAMDIR:", "Delta_H_net = Delta_H1 + Delta_H2", "(Zıt taraftaki eşit türler sadeleşir)", "#16a34a", "#f0fdf4"),
    ]
    for i, (bas, a1, a2, a3, ex1, ex2, r, bg) in enumerate(kurallar):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="230" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="106" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+112}" y="124" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+112}" y="144" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{a3}</text>'
        s += f'<rect x="{x+12}" y="166" width="200" height="96" rx="8" fill="#fff" stroke="{r}"/>'
        s += f'<text x="{x+112}" y="198" text-anchor="middle" fill="#334155" font-size="10" font-weight="700">{ex1}</text>'
        s += f'<text x="{x+112}" y="226" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{ex2}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Hess Yasası Enerji Diyagramı (C + O2 -> CO2 Doğrudan ve İki Basamaklı Yol)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Hess Yasası Enerji Diyagramı: Entalpi Yoldan Bağımsız Bir Hal Fonksiyonudur", "#0284c7", "#f0f9ff")

    # Sol: Enerji basamakları
    s += '<rect x="30" y="55" width="380" height="230" rx="10" fill="#fff" stroke="#7dd3fc" stroke-width="1.5"/>'
    # Üst seviye: C(k) + O2(g)
    s += '<line x1="60" y1="85" x2="360" y2="85" stroke="#1e293b" stroke-width="3"/>'
    s += '<text x="210" y="76" text-anchor="middle" fill="#1e293b" font-size="11" font-weight="700">Başlangıç: C(k) + O2(g)</text>'

    # Orta seviye: CO(g) + 1/2 O2(g)
    s += '<line x1="210" y1="165" x2="375" y2="165" stroke="#d97706" stroke-width="2.5"/>'
    s += '<text x="292" y="156" text-anchor="middle" fill="#b45309" font-size="10" font-weight="700">Ara: CO(g) + 1/2 O2(g)</text>'

    # Alt seviye: CO2(g)
    s += '<line x1="60" y1="245" x2="360" y2="245" stroke="#16a34a" stroke-width="3"/>'
    s += '<text x="210" y="264" text-anchor="middle" fill="#15803d" font-size="11" font-weight="700">Sonuç: CO2(g)</text>'

    # Oklar
    s += '<line x1="110" y1="88" x2="110" y2="240" stroke="#dc2626" stroke-width="3"/>'
    s += '<text x="115" y="170" fill="#dc2626" font-size="10.5" font-weight="700">Delta_H_net = -393,5 kJ</text>'

    s += '<line x1="285" y1="88" x2="285" y2="140" stroke="#0284c7" stroke-width="2.2"/>'
    s += '<text x="292" y="118" fill="#0284c7" font-size="9.8" font-weight="700">Delta_H1 = -110,5 kJ</text>'

    s += '<line x1="285" y1="168" x2="285" y2="240" stroke="#7c3aed" stroke-width="2.2"/>'
    s += '<text x="292" y="210" fill="#7c3aed" font-size="9.8" font-weight="700">Delta_H2 = -283,0 kJ</text>'

    # Sağ: Açıklama
    s += '<rect x="428" y="55" width="302" height="230" rx="10" fill="#fff" stroke="#7dd3fc" stroke-width="1.5"/>'
    s += '<text x="579" y="80" text-anchor="middle" fill="#0369a1" font-size="12" font-weight="700">Neden Toplam Değişmez?</text>'
    s += '<text x="579" y="110" text-anchor="middle" fill="#334155" font-size="10.2">Entalpi (H) bir HAL FONKSİYONUDUR;</text>'
    s += '<text x="579" y="128" text-anchor="middle" fill="#334155" font-size="10.2">izlenen yola veya basamak sayısına değil,</text>'
    s += '<text x="579" y="146" text-anchor="middle" fill="#0369a1" font-size="10.2" font-weight="700">yalnız ilk ve son duruma bağlıdır.</text>'
    s += '<rect x="444" y="168" width="270" height="96" rx="8" fill="#e0f2fe" stroke="#0284c7"/>'
    s += '<text x="579" y="194" text-anchor="middle" fill="#1e293b" font-size="10.5" font-weight="700">Delta_H_net = Delta_H1 + Delta_H2</text>'
    s += '<text x="579" y="218" text-anchor="middle" fill="#dc2626" font-size="11" font-weight="700">-393,5 kJ = (-110,5) + (-283,0)</text>'
    s += '<text x="579" y="242" text-anchor="middle" fill="#475569" font-size="9.8">(Germain Henri Hess, 1840)</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Çarpışma Teorisi ve Etkin Çarpışmanın 2 Şartı."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Kimyasal Tepkimelerde Hız: Çarpışma Teorisi ve Etkin Çarpışma Şartları", "#0d9488", "#f0fdfa")

    sartlar = [
        ("1. Şart: Uygun Geometrik Doğrultu", "Tanecikler bağların kopup yeni", "bağların oluşabileceği doğru", "açı ve doğrultuda çarpışmalıdır.", "(Merkez-merkez uygun yönelim)", "#0d9488", "#ccfbf1"),
        ("2. Şart: Yeterli Kinetik Enerji (E_a)", "Çarpışan taneciklerin toplam", "kinetik enerjisi en az Eşik Enerjisi", "(Aktifleşme Enerjisi, E_a) kadar", "olmalıdır (E_a daima POZİTİFTİR!).", "#d97706", "#fef3c7"),
        ("Sonuç: Aktifleşmiş Kompleks", "İki şartı sağlayan ETKİN ÇARPIŞMA", "sonucunda yüksek enerjili ve", "kararsız ara durum olan", "Aktifleşmiş Kompleks oluşur.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, a4, r, bg) in enumerate(sartlar):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="58" width="224" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="77" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="118" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+112}" y="138" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+112}" y="158" text-anchor="middle" fill="#1e293b" font-size="10.2">{a3}</text>'
        s += f'<text x="{x+112}" y="188" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a4}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Potansiyel Enerji (PE) - Tepkime Koordinatı Grafiği (E_ai, E_ag ve Delta_H İlişkisi)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Potansiyel Enerji Grafiği: İleri/Geri Aktifleşme Enerjisi ve Delta_H", "#15803d", "#f0fdf4")

    # Sol: PE Grafiği
    s += '<rect x="30" y="55" width="350" height="230" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<line x1="65" y1="245" x2="350" y2="245" stroke="#334155" stroke-width="2"/>'
    s += '<line x1="65" y1="75" x2="65" y2="245" stroke="#334155" stroke-width="2"/>'
    # Eğri (Ekzotermik örnek)
    s += '<path d="M65,165 L115,165 Q185,60 245,215 L325,215" fill="none" stroke="#16a34a" stroke-width="3"/>'
    s += '<circle cx="182" cy="112" r="5" fill="#dc2626"/>'
    s += '<text x="182" y="98" text-anchor="middle" fill="#dc2626" font-size="9.5" font-weight="700">Aktifleşmiş Kompleks (Tepe)</text>'
    s += '<text x="90" y="156" text-anchor="middle" fill="#1e293b" font-size="9.5" font-weight="700">Girenler</text>'
    s += '<text x="295" y="206" text-anchor="middle" fill="#1e293b" font-size="9.5" font-weight="700">Ürünler</text>'
    # E_ai ve E_ag okları
    s += '<line x1="150" y1="112" x2="150" y2="165" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,2"/>'
    s += '<text x="130" y="142" fill="#0284c7" font-size="9.5" font-weight="700">E_ai</text>'
    s += '<line x1="215" y1="112" x2="215" y2="215" stroke="#7c3aed" stroke-width="2" stroke-dasharray="3,2"/>'
    s += '<text x="235" y="165" fill="#7c3aed" font-size="9.5" font-weight="700">E_ag</text>'

    # Sağ: Formüller
    s += '<rect x="398" y="55" width="332" height="230" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<text x="564" y="78" text-anchor="middle" fill="#166534" font-size="12" font-weight="700">PE Grafiği Temel Bağıntıları</text>'

    formuller = [
        ("1) E_ai = PE(Tepe) - PE(Girenler)", "İleri aktifleşme enerjisi (Daima E_ai > 0)"),
        ("2) E_ag = PE(Tepe) - PE(Ürünler)", "Geri aktifleşme enerjisi (Daima E_ag > 0)"),
        ("3) Delta_H = E_ai - E_ag", "E_ai < E_ag ise Ekzotermik (Delta_H < 0)"),
        ("4) Delta_H = PE(Ürünler) - PE(Girenler)", "E_ai > E_ag ise Endotermik (Delta_H > 0)"),
    ]
    for i, (f1, f2) in enumerate(formuller):
        y = 92 + i * 45
        s += f'<rect x="412" y="{y}" width="304" height="38" rx="6" fill="#f0fdf4" stroke="#22c55e"/>'
        s += f'<text x="422" y="{y+16}" fill="#15803d" font-size="10.2" font-weight="700">{f1}</text>'
        s += f'<text x="422" y="{y+31}" fill="#334155" font-size="9.5">{f2}</text>'

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
