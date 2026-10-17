# -*- coding: utf-8 -*-
"""10. Sınıf Felsefe — 5. Hafta Görselleri
Konu: Felsefenin Bireysel ve Toplumsal İşlevlerinin Sorgulanması ve Tartışılması
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#6d28d9", arka="#f5f3ff"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Felsefenin Bireysel İşlevleri Şeması."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Felsefenin Bireysel İşlevleri: Kendini Tanıyan ve Özgür Düşünen Birey", "#6d28d9", "#f5f3ff")

    # Merkez Daire
    s += '<circle cx="380" cy="175" r="56" fill="#5b21b6" stroke="#c4b5fd" stroke-width="3"/>'
    s += '<text x="380" y="170" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">FELSEFE VE</text>'
    s += '<text x="380" y="188" text-anchor="middle" fill="#ddd6fe" font-size="12" font-weight="700">BİREY</text>'

    kutular = [
        (30, 62, "1. Kendini Tanıma ve Anlam Arayışı", "Sokrates'in 'Sorgulanmamış yaşam yaşanmaya", "değmez' ilkesiyle hayatın anlamını sorgular.", "#7c3aed"),
        (450, 62, "2. Önyargılardan ve Dogmalardan Arınma", "Körü körüne inanmak yerine kanıt ve gerekçe", "arayarak düşünsel bağımsızlığa ulaşır.", "#0284c7"),
        (30, 200, "3. Çok Yönlü ve Eleştirel Bakış", "Olaylara tek pencereden değil, farklı", "perspektiflerden bakabilme esnekliği kazanır.", "#0d9488"),
        (450, 200, "4. Tutarlı ve Kavramsal Düşünme", "Kendi fikirlerini mantıksal bütünlük içinde", "savunur; bilgi kirliliğine karşı direnç kazanır.", "#d97706"),
    ]
    for x, y, bas, a1, a2, r in kutular:
        s += f'<rect x="{x}" y="{y}" width="280" height="82" rx="10" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="{y}" width="280" height="25" rx="10" fill="{r}"/>'
        s += f'<text x="{x+140}" y="{y+17}" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+140}" y="{y+46}" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+140}" y="{y+64}" text-anchor="middle" fill="#334155" font-size="10">{a2}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Felsefenin Toplumsal İşlevleri Şeması."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Felsefenin Toplumsal İşlevleri: Demokrasi, Bilim ve Birlikte Yaşama Kültürü", "#0369a1", "#f0f9ff")

    islevler = [
        ("Demokrasi ve İnsan Hakları", "Özgürlük, eşitlik, adalet ve", "hukukun üstünlüğü kavramlarının", "kuramsal temelini atar.", "#0284c7", "#e0f2fe"),
        ("Hoşgörü ve Çoğulculuk", "Farklı inanç, kültür ve görüşlerin", "barış içinde bir arada yaşama", "kültürünü güçlendirir.", "#16a34a", "#f0fdf4"),
        ("Bilimlerin Doğuşu ve Gelişimi", "Merak ve soru sorma kültürüyle", "yeni bilim dallarının doğmasına", "ve etik denetimine öncülük eder.", "#7c3aed", "#f5f3ff"),
        ("Ortak Akıl ve Uzlaşı Dili", "Toplumsal kutuplaşma ve şiddet", "yerine rasyonel diyalog ve", "argüman kültürünü yerleştirir.", "#d97706", "#fffbeb"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(islevler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="60" width="168" height="220" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="60" width="168" height="30" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="80" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<circle cx="{x+84}" cy="128" r="22" fill="#fff" stroke="{r}" stroke-width="2"/>'
        s += f'<text x="{x+84}" y="134" text-anchor="middle" fill="{r}" font-size="15" font-weight="700">{i+1}</text>'
        s += f'<text x="{x+84}" y="178" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="196" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="214" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Felsefe Tarihinde Toplumu Dönüştüren Filozoflar ve Etkileri."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Düşünceden Eyleme: Felsefenin Tarihsel ve Toplumsal Dönüştürücü Gücü", "#0f766e", "#f0fdfa")

    dusunurler = [
        ("Sokrates &amp; Platon", "Antik Yunan", "'At Sineği' metaforuyla", "toplumu uyandırma; ideal", "devlet ve adalet arayışı.", "#0f766e"),
        ("Farabi &amp; İbn Rüşd", "İslam Dünyası", "'El-Medinetü'l-Fazıla' ile", "erdemli toplum tasarımı;", "akıl ve hikmet sentezi.", "#15803d"),
        ("Locke, Montesquieu, Rousseau", "Aydınlanma Çağı", "Kuvvetler ayrılığı, toplumsal", "sözleşme ve doğal haklarla", "modern demokrasinin inşası.", "#1d4ed8"),
        ("Kant &amp; Çağdaş Felsefe", "Modern Dünya", "'Sapere Aude!' (Aklını", "kullanma cesareti göster!)", "ve evrensel insan hakları.", "#7c3aed"),
    ]
    for i, (ad, donem, a1, a2, a3, r) in enumerate(dusunurler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="60" width="168" height="220" rx="10" fill="#fff" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="60" width="168" height="44" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="80" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{ad}</text>'
        s += f'<text x="{x+84}" y="96" text-anchor="middle" fill="#e2e8f0" font-size="9.5">{donem}</text>'
        s += f'<text x="{x+84}" y="142" text-anchor="middle" fill="#334155" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="162" text-anchor="middle" fill="#334155" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="182" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'
        if i < 3:
            s += f'<line x1="{x+168}" y1="170" x2="{x+180}" y2="170" stroke="#0f766e" stroke-width="2.5"/>'

    return _svg(w, h, s)


def gorsel_4():
    """21. Yüzyılda Felsefenin Güncel Sorunlarla İlişkisi (Yapay Zekâ, Ekoloji, Biyoetik, Dijital Çağ)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "21. Yüzyılda Felsefenin Yeni Sorgulama Alanları ve Güncel İşlevleri", "#b45309", "#fffbeb")

    alanlar = [
        ("Yapay Zekâ ve Robot Etiği", "Yapay zekâ bilinç kazanabilir mi?", "Otonom kararların ahlaki ve", "hukuki sorumluluğu kimdedir?", "#1d4ed8", "#eff6ff"),
        ("Biyoetik ve Tıp Felsefesi", "Genetik müdahale, klonlama ve", "yaşam hakkı sınırları hangi", "etik ilkelere göre çizilmelidir?", "#be123c", "#fff1f2"),
        ("Çevre Felsefesi ve Ekoloji", "İnsan doğanın efendisi mi yoksa", "bir parçası mıdır? Gelecek", "kuşaklara karşı ödevlerimiz nelerdir?", "#15803d", "#f0fdf4"),
        ("Dijital Çağ ve Hakikat Ötesi", "Sosyal medya yankı odaları ve", "dezenformasyon (post-truth) çağında", "doğru bilgiye nasıl ulaşılır?", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(alanlar):
        x = 28 + (i % 2) * 358
        y = 58 + (i // 2) * 116
        s += f'<rect x="{x}" y="{y}" width="344" height="102" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="{y}" width="344" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+172}" y="{y+18}" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+172}" y="{y+48}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+172}" y="{y+66}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+172}" y="{y+84}" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

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
