# -*- coding: utf-8 -*-
"""10. Sınıf Kur'an-ı Kerim — 5. Hafta Görselleri
Konu: 2. Tema: Tecvit — Med (Uzatma) Çeşitleri (Asli Med ve Fer'i Medler)
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#047857", arka="#ecfdf5"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Med Harfleri (Elif, Vav, Ya) ve Asli Med (Medd-i Tabii) Şeması."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Tecvitte Med (Uzatma) Harfleri ve Medd-i Tabii (Asli Med)", "#047857", "#ecfdf5")

    harfler = [
        ("1. Harf-i Med: ELİF", "Kendisinden önceki harfin", "harekesi ÜSTÜN (-e / -a)", "olup kendisi harekesiz", "gelen Elif harfidir.", "Örnek: Kâle (1 Elif uzatılır)", "#059669", "#d1fae5"),
        ("2. Harf-i Med: VAV", "Kendisinden önceki harfin", "harekesi ÖTRE (-u / -ü)", "olup kendisi sakin (cezimli)", "gelen Vav harfidir.", "Örnek: Yekûlü (1 Elif uzatılır)", "#0284c7", "#e0f2fe"),
        ("3. Harf-i Med: YA", "Kendisinden önceki harfin", "harekesi ESRE (-i / -ı)", "olup kendisi sakin (cezimli)", "gelen Ya harfidir.", "Örnek: Kîle (1 Elif uzatılır)", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, a4, ex, r, bg) in enumerate(harfler):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="175" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="102" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+112}" y="120" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+112}" y="138" text-anchor="middle" fill="#1e293b" font-size="10.2">{a3}</text>'
        s += f'<text x="{x+112}" y="156" text-anchor="middle" fill="#1e293b" font-size="10.2">{a4}</text>'
        s += f'<text x="{x+112}" y="198" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{ex}</text>'

    s += '<rect x="28" y="242" width="704" height="44" rx="8" fill="#fff" stroke="#059669" stroke-width="1.4"/>'
    s += '<text x="380" y="261" text-anchor="middle" fill="#065f46" font-size="11" font-weight="700">Medd-i Tabii (Asli Med): Med harfinden sonra sebeb-i med (hemze veya sükûn) gelmezse</text>'
    s += '<text x="380" y="278" text-anchor="middle" fill="#047857" font-size="10.5">harf yalnızca 1 Elif miktarı (yaklaşık iki hareke süresi) uzatılır; hükmü VACİPTİR.</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Sebeb-i Med (Hemze ve Sükûn) ve Hemze Sebebiyle Oluşan Medler: Medd-i Muttasıl vs Medd-i Munfasıl."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Sebeb-i Med: Hemze Sebebiyle Oluşan Fer'i Medler (Muttasıl ve Munfasıl)", "#1d4ed8", "#eff6ff")

    # Üst bilgi: Sebeb-i Med
    s += '<rect x="30" y="52" width="700" height="36" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.2"/>'
    s += '<text x="380" y="74" text-anchor="middle" fill="#1e3a8a" font-size="11.5" font-weight="700">Sebeb-i Med (1 Eliften Fazla Uzatma Sebebi) İkidir:  1) HEMZE (Kırık/Uzun Elif)   2) SÜKÛN (Lazım veya Arız Cezim)</text>'

    # Sol: Medd-i Muttasıl
    s += '<rect x="30" y="100" width="340" height="192" rx="10" fill="#fff" stroke="#3b82f6" stroke-width="1.6"/>'
    s += '<rect x="30" y="100" width="340" height="28" rx="10" fill="#1d4ed8"/>'
    s += '<text x="200" y="119" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. MEDD-İ MUTTASIL (Bitişik Med)</text>'
    s += '<text x="200" y="148" text-anchor="middle" fill="#1e293b" font-size="10.5">Harf-i med ile sebeb-i med olan HEMZE</text>'
    s += '<text x="200" y="166" text-anchor="middle" fill="#1d4ed8" font-size="11" font-weight="700">AYNI KELİME İÇİNDE yan yana gelirse oluşur.</text>'
    s += '<rect x="48" y="182" width="304" height="94" rx="8" fill="#eff6ff" stroke="#93c5fd"/>'
    s += '<text x="200" y="204" text-anchor="middle" fill="#1e3a8a" font-size="11" font-weight="700">• Hükmü: VACİPTİR (Kısaltılamaz!)</text>'
    s += '<text x="200" y="226" text-anchor="middle" fill="#1e293b" font-size="10.5">• Uzatma Miktarı: Asım kıraatinde 4 Elif miktarı</text>'
    s += '<text x="200" y="248" text-anchor="middle" fill="#0369a1" font-size="10.5" font-weight="700">• Örnek: Câe, Es-Semâü, Ulâike, Sûe</text>'

    # Sağ: Medd-i Munfasıl
    s += '<rect x="390" y="100" width="340" height="192" rx="10" fill="#fff" stroke="#10b981" stroke-width="1.6"/>'
    s += '<rect x="390" y="100" width="340" height="28" rx="10" fill="#059669"/>'
    s += '<text x="560" y="119" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. MEDD-İ MUNFASIL (Ayrık Med)</text>'
    s += '<text x="560" y="148" text-anchor="middle" fill="#1e293b" font-size="10.5">Harf-i med birinci kelimenin sonunda, HEMZE ise</text>'
    s += '<text x="560" y="166" text-anchor="middle" fill="#059669" font-size="11" font-weight="700">İKİNCİ KELİMENİN BAŞINDA gelirse oluşur.</text>'
    s += '<rect x="408" y="182" width="304" height="94" rx="8" fill="#ecfdf5" stroke="#6ee7b7"/>'
    s += '<text x="560" y="204" text-anchor="middle" fill="#065f46" font-size="11" font-weight="700">• Hükmü: CAİZDİR (Farklı vecihleri vardır)</text>'
    s += '<text x="560" y="226" text-anchor="middle" fill="#1e293b" font-size="10.5">• Uzatma Miktarı: 1 ile 4 Elif arası (Hafs: 4 Elif)</text>'
    s += '<text x="560" y="248" text-anchor="middle" fill="#047857" font-size="10.5" font-weight="700">• Örnek: İnnâ a\'taynâ, Yâ eyyühe\'llezîne</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Sükûn Sebebiyle Oluşan Medler: Medd-i Lazım, Medd-i Arız ve Medd-i Lin."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Sükûn Sebebiyle Oluşan Fer'i Medler: Lazım, Arız ve Lin", "#7c3aed", "#f5f3ff")

    medler = [
        ("1. Medd-i Lâzım", "Sebep: Sükûn-u Lâzım", "Durulsa da geçilse de", "değişmeyen asli cezim/şedde", "gelirse oluşur.", "Hükmü: LÂZIM (Kesin 4 Elif)", "Örnek: Ed-Dâllîn, El-Hâkka", "#dc2626", "#fef2f2"),
        ("2. Medd-i Ârız", "Sebep: Sükûn-u Ârız", "Med harfinden sonraki son", "harf durak (vakıf) sebebiyle", "sakin kılınırsa oluşur.", "Hükmü: CAİZ (1-4 Elif)", "Örnek: El-Âlemîn (durunca)", "#0284c7", "#f0f9ff"),
        ("3. Medd-i Lîn", "Sebep: Lîn Harfi + Sükûn", "Öncesi üstünlü sakin Vav/Ya", "(ev, ey) sonrası durakla", "sakin kılınırsa oluşur.", "Hükmü: CAİZ (1-4 Elif)", "Örnek: Kureyş, Min havf", "#d97706", "#fffbeb"),
    ]
    for i, (bas, seb, a1, a2, a3, huk, ex, r, bg) in enumerate(medler):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="230" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="99" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{seb}</text>'
        s += f'<text x="{x+112}" y="122" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+112}" y="138" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+112}" y="154" text-anchor="middle" fill="#1e293b" font-size="10">{a3}</text>'
        s += f'<rect x="{x+14}" y="172" width="196" height="98" rx="8" fill="#fff" stroke="{r}"/>'
        s += f'<text x="{x+112}" y="198" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{huk}</text>'
        s += f'<text x="{x+112}" y="226" text-anchor="middle" fill="#334155" font-size="10" font-weight="700">{ex}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Med Çeşitleri Karşılaştırma ve Mertebeler Tablosu (Tul, Tevassut, Kasr)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Med Çeşitleri Özet Tablosu ve Uzatma Mertebeleri (Kasr, Tevassut, Tûl)", "#b45309", "#fffbeb")

    # Tablo Başlığı
    s += '<rect x="30" y="55" width="700" height="28" rx="6" fill="#b45309"/>'
    s += '<text x="105" y="74" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">Med Çeşidi</text>'
    s += '<text x="275" y="74" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">Sebebi</text>'
    s += '<text x="445" y="74" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">Uzatma Miktarı</text>'
    s += '<text x="615" y="74" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">Tecvit Hükmü</text>'

    satirlar = [
        ("Medd-i Tabii", "Sebeb-i med YOK", "1 Elif (Kasr)", "Vacip (Asli Med)"),
        ("Medd-i Muttasıl", "Aynı kelimede Hemze", "4 Elif (Tûl / Tevassut)", "Vacip"),
        ("Medd-i Munfasıl", "Ayrı kelimede Hemze", "1 - 4 Elif arası", "Caiz"),
        ("Medd-i Lâzım", "Sükûn-u Lâzım (Kalıcı cezim/şedde)", "4 Elif (Tûl)", "Lâzım (Farz/Kesin)"),
        ("Medd-i Ârız / Lîn", "Sükûn-u Ârız (Durak cezmi)", "1 - 4 Elif arası", "Caiz"),
    ]
    for i, (ad, seb, mik, huk) in enumerate(satirlar):
        y = 88 + i * 32
        bg = "#fff" if i % 2 == 0 else "#fef3c7"
        s += f'<rect x="30" y="{y}" width="700" height="30" fill="{bg}" stroke="#fcd34d" stroke-width="0.8"/>'
        s += f'<text x="105" y="{y+19}" text-anchor="middle" fill="#92400e" font-size="10.5" font-weight="700">{ad}</text>'
        s += f'<text x="275" y="{y+19}" text-anchor="middle" fill="#1e293b" font-size="10">{seb}</text>'
        s += f'<text x="445" y="{y+19}" text-anchor="middle" fill="#1e293b" font-size="10" font-weight="700">{mik}</text>'
        s += f'<text x="615" y="{y+19}" text-anchor="middle" fill="#b45309" font-size="10" font-weight="700">{huk}</text>'

    s += '<rect x="30" y="254" width="700" height="32" rx="6" fill="#fef3c7" stroke="#d97706"/>'
    s += '<text x="380" y="274" text-anchor="middle" fill="#92400e" font-size="10.5" font-weight="700">Uzatma Mertebeleri: Kasr (1 Elif) — Tevassut (2-3 Elif) — Tûl (4 Elif)</text>'

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
