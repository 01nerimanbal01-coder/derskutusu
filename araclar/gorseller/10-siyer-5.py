# -*- coding: utf-8 -*-
"""10. Sınıf Siyer — 5. Hafta Görselleri
Konu: 1. Ünite: İslam Öncesi Dönem — Hz. Muhammed'in (sav) Risalet Öncesi Hayatı
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0d9488", arka="#f0fdfa"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Doğumundan Gençliğine Kronolojik Hayat Çizgisi (571 - 610)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Hz. Muhammed'in (s.a.v.) Risalet Öncesi Hayat Kronolojisi (571 - 610)", "#0d9488", "#f0fdfa")

    olaylar = [
        ("571 — Doğum &amp; Sütanne", "Mekke'de dünyaya gelişi;", "Benî Sa'd yurdunda sütannesi", "Halime'nin yanında 4 yıl.", "#0d9488"),
        ("576 - 578 — Yetim ve Öksüz", "6 yaşında annesi Âmine'nin", "(Ebvâ'da), 8 yaşında dedesi", "Abdülmuttalib'in vefatı.", "#0284c7"),
        ("579 - 591 — Ebu Talib Himayesi", "Amcası Ebu Talib'le Şam", "ticaret seferi (Rahip Bahîra);", "Ficâr Savaşı ve Hilfü'l-Fudûl.", "#7c3aed"),
        ("595 — Hz. Hatice ile Evlilik", "25 yaşında dürüst bir tüccar", "olarak (El-Emîn) 40 yaşındaki", "Hz. Hatice (Tâhire) ile evlilik.", "#16a34a"),
        ("605 - 610 — Hakemlik &amp; Hira", "35 yaşında Kâbe Hakemliği;", "Nûr Dağı Hira Mağarası'nda", "tahannüs (inziva ve tefekkür).", "#d97706"),
    ]
    for i, (bas, a1, a2, r, *_) in enumerate(olaylar):
        y = 52 + i * 48
        s += f'<rect x="34" y="{y}" width="692" height="42" rx="8" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="34" y="{y}" width="210" height="42" rx="8" fill="{r}"/>'
        s += f'<text x="139" y="{y+26}" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="260" y="{y+18}" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="260" y="{y+34}" fill="{r}" font-size="10" font-weight="700">{a2}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Gençlik Yıllarında Erdem ve Adalet: Ficâr Savaşı ve Hilfü'l-Fudûl (Erdemliler Topluluğu)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Adalet ve Barış Öncüsü Bir Genç: Hilfü'l-Fudûl (Erdemliler Cemiyeti)", "#1d4ed8", "#eff6ff")

    # Sol: Ficâr Savaşı
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<rect x="30" y="55" width="335" height="30" rx="10" fill="#0284c7"/>'
    s += '<text x="197" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. Ficâr Savaşındaki Tutumu (~589)</text>'
    s += '<text x="197" y="108" text-anchor="middle" fill="#1e293b" font-size="10.2">Haram aylarda Kureyş-Kinâne ile</text>'
    s += '<text x="197" y="126" text-anchor="middle" fill="#1e293b" font-size="10.2">Kays-Aylân arasında çıkan savaştır.</text>'
    s += '<rect x="48" y="146" width="299" height="118" rx="8" fill="#f0f9ff" stroke="#38bdf8"/>'
    s += '<text x="197" y="172" text-anchor="middle" fill="#0369a1" font-size="11" font-weight="700">Kan Dökmekten Sakınma:</text>'
    s += '<text x="197" y="196" text-anchor="middle" fill="#334155" font-size="10">Hz. Muhammed (s.a.v.) bu savaşta kimseye</text>'
    s += '<text x="197" y="214" text-anchor="middle" fill="#334155" font-size="10">ok atmamış; yalnız amcalarını korumak için</text>'
    s += '<text x="197" y="232" text-anchor="middle" fill="#0284c7" font-size="10" font-weight="700">kalkan tutup düşman oklarını toplamıştır.</text>'

    # Sağ: Hilfü'l-Fudûl
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<rect x="395" y="55" width="335" height="30" rx="10" fill="#1d4ed8"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. Hilfü\'l-Fudûl (Erdemliler Yeminleşmesi)</text>'
    s += '<text x="562" y="108" text-anchor="middle" fill="#1e293b" font-size="10.2">Yemenli tüccarın hakkının gasp edilmesi</text>'
    s += '<text x="562" y="126" text-anchor="middle" fill="#1e293b" font-size="10.2">üzerine Abdullah b. Cüd\'an\'ın evinde kuruldu.</text>'
    s += '<rect x="413" y="146" width="299" height="118" rx="8" fill="#eff6ff" stroke="#60a5fa"/>'
    s += '<text x="562" y="172" text-anchor="middle" fill="#1e40af" font-size="11" font-weight="700">Mazlumun Yanında Durma:</text>'
    s += '<text x="562" y="196" text-anchor="middle" fill="#334155" font-size="10">&quot;Mekke\'de yerli veya yabancı hiçbir mazlum</text>'
    s += '<text x="562" y="214" text-anchor="middle" fill="#334155" font-size="10">hakkını alıncaya kadar yalnız bırakılmayacaktır!&quot;</text>'
    s += '<text x="562" y="236" text-anchor="middle" fill="#1d4ed8" font-size="10" font-weight="700">&quot;İslam\'da da böyle bir anlaşmaya çağrılsam icabet ederim.&quot;</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Hz. Hatice ile Evliliği, Çocukları ve Kâbe Hakemliği (Hacerü'l-Esved)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Örnek Aile Hayatı ve Kâbe Hakemliği (Hacerü'l-Esved Krizi - 605)", "#15803d", "#f0fdf4")

    # Sol: Aile Hayatı ve Çocukları
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<text x="197" y="76" text-anchor="middle" fill="#166534" font-size="12" font-weight="700">1. Hz. Hatice (Tâhire) ile Yuvası ve Evlatları</text>'

    cocuklar = [
        ("Erkek Çocukları (Küçük yaşta vefat):", "1) Kâsım (Ebu'l-Kâsım künyesi), 2) Abdullah, 3) İbrâhim (Mâriye'den)"),
        ("Kız Çocukları:", "1) Zeyneb, 2) Rukıyye, 3) Ümmü Gülsüm, 4) Fâtıma (r.a.)"),
        ("Hane Halkı ve Vefa:", "Amcasının yükünü hafifletmek için Hz. Ali'yi, azat ettiği Zeyd b. Harise'yi evladı gibi büyütmüştür."),
    ]
    for i, (b, ac) in enumerate(cocuklar):
        y = 92 + i * 58
        s += f'<rect x="44" y="{y}" width="307" height="48" rx="6" fill="#f0fdf4" stroke="#22c55e"/>'
        s += f'<text x="54" y="{y+18}" fill="#15803d" font-size="10" font-weight="700">{b}</text>'
        s += f'<text x="54" y="{y+36}" fill="#334155" font-size="9.5">{ac}</text>'

    # Sağ: Kâbe Hakemliği
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#86efac" stroke-width="1.5"/>'
    s += '<text x="562" y="76" text-anchor="middle" fill="#166534" font-size="12" font-weight="700">2. Kâbe Hakemliği (35 Yaş — Miladi 605)</text>'

    s += '<rect x="413" y="92" width="299" height="175" rx="8" fill="#fef3c7" stroke="#d97706"/>'
    s += '<text x="562" y="114" text-anchor="middle" fill="#92400e" font-size="11" font-weight="700">Kanlı Kabile Savaşı Nasıl Önledi?</text>'
    s += '<text x="562" y="138" text-anchor="middle" fill="#334155" font-size="10">Selden zarar gören Kâbe onarılırken</text>'
    s += '<text x="562" y="154" text-anchor="middle" fill="#334155" font-size="10">Hacerü\'l-Esved\'i yerine koyma anlaşmazlığı çıktı.</text>'
    s += '<text x="562" y="176" text-anchor="middle" fill="#b45309" font-size="10.2" font-weight="700">&quot;Kapıdan giren El-Emîn\'dir, hükmüne razıyız!&quot;</text>'
    s += '<text x="562" y="198" text-anchor="middle" fill="#1e293b" font-size="10">Hırkasını (ridasını) yere serip taşı üzerine koydu;</text>'
    s += '<text x="562" y="216" text-anchor="middle" fill="#1e293b" font-size="10">her kabile reisi bir ucundan tutarak taşıdı</text>'
    s += '<text x="562" y="236" text-anchor="middle" fill="#15803d" font-size="10.2" font-weight="700">ve mübarek elleriyle taşı yerine yerleştirdi!</text>'

    return _svg(w, h, s)


def gorsel_4():
    """İsmet Sıfatı, Cahiliye Kötülüklerinden Korunmuşluğu ve Hira'da İnziva (Tahannüs)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Cahiliye Karanlığında Tertemiz Bir Hayat ve Hira Mağarası'nda İnziva", "#b45309", "#fffbeb")

    ozellikler = [
        ("Putlara Asla Tapmadı", "Hayatı boyunca putlara secde", "etmedi, putlar adına kesilen", "kurban etlerinden yemedi.", "#dc2626", "#fef2f2"),
        ("İçki ve Kumardan Uzak Durdu", "Cahiliye eğlencelerine, içki,", "kumar, fal okları ve faize", "hiçbir zaman bulaşmadı.", "#0284c7", "#f0f9ff"),
        ("Muhammedü'l-Emîn", "Sözünde durması ve emanetleri", "korumasıyla düşmanlarının bile", "güvendiği tek insandı.", "#16a34a", "#f0fdf4"),
        ("Hira'da Tahannüs (İnziva)", "35 yaşından sonra Ramazan", "aylarında Nûr Dağı Hira'da", "tefekkürle vahye hazırlandı.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(ozellikler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="125" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="145" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="165" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

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
