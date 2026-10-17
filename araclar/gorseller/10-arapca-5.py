# -*- coding: utf-8 -*-
"""10. Sınıf Arapça — 5. Hafta Görselleri
Konu: Ünite 1: Değerlerim — Ders 1: Akrabalarım (Akrabalık Kavramları ve Sıla-i Rahim)
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
    """Baba Tarafı ve Anne Tarafı Akrabalık Kelimeleri (Amm, Ammet, Hal, Halet, Cedd, Ceddet)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Arapçada Akrabalarım (El-Ekarib): Baba Tarafı ve Anne Tarafı Akrabalar", "#0d9488", "#f0fdfa")

    # Üst Merkez: Büyükbaba ve Büyükanne
    s += '<rect x="190" y="50" width="380" height="44" rx="8" fill="#0f766e"/>'
    s += '<text x="380" y="69" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">El-Cedd (Dede / Büyükbaba)  &amp;  El-Ceddetü (Nine / Büyükanne)</text>'
    s += '<text x="380" y="86" text-anchor="middle" fill="#99f6e4" font-size="10">El-Hafîd (Erkek Torun) — El-Hafîdetü (Kız Torun)</text>'

    # Sol: Baba Tarafı
    s += '<rect x="28" y="106" width="340" height="186" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<rect x="28" y="106" width="340" height="28" rx="10" fill="#0284c7"/>'
    s += '<text x="198" y="125" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">Baba Tarafı Akrabalar (Caniibü\'l-Eb)</text>'

    baba_t = [
        ("El-Amm (Amca):", "Babanın erkek kardeşi (Ehu'l-eb)"),
        ("El-Ammetü (Hala):", "Babanın kız kardeşi (Uhtu'l-eb)"),
        ("İbnü'l-Amm / İbnü'l-Ammeti:", "Amca oğlu / Hala oğlu (Erkek kuzen)"),
        ("Bintü'l-Amm / Bintü'l-Ammeti:", "Amca kızı / Hala kızı (Kız kuzen)"),
    ]
    for i, (k, ac) in enumerate(baba_t):
        y = 144 + i * 35
        s += f'<text x="42" y="{y+14}" fill="#0369a1" font-size="10.5" font-weight="700">{k}</text>'
        s += f'<text x="210" y="{y+14}" fill="#334155" font-size="10">{ac}</text>'

    # Sağ: Anne Tarafı
    s += '<rect x="392" y="106" width="340" height="186" rx="10" fill="#fff" stroke="#5eead4" stroke-width="1.5"/>'
    s += '<rect x="392" y="106" width="340" height="28" rx="10" fill="#7c3aed"/>'
    s += '<text x="562" y="125" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">Anne Tarafı Akrabalar (Canibü\'l-Ümm)</text>'

    anne_t = [
        ("El-Hâl (Dayı):", "Annenin erkek kardeşi (Ehu'l-ümm)"),
        ("El-Hâletü (Teyze):", "Annenin kız kardeşi (Uhtu'l-ümm)"),
        ("İbnü'l-Hâl / İbnü'l-Hâleti:", "Dayı oğlu / Teyze oğlu (Erkek kuzen)"),
        ("Bintü'l-Hâl / Bintü'l-Hâleti:", "Dayı kızı / Teyze kızı (Kız kuzen)"),
    ]
    for i, (k, ac) in enumerate(anne_t):
        y = 144 + i * 35
        s += f'<text x="406" y="{y+14}" fill="#6d28d9" font-size="10.5" font-weight="700">{k}</text>'
        s += f'<text x="568" y="{y+14}" fill="#334155" font-size="10">{ac}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """İsim Tamlaması (İzafet / Muzaf - Muzafun İleyh) ile Akrabalık İlişkisi Kurma."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Arapçada İsim Tamlaması (El-İzafe) ile Akrabalık İfadesi Kurma", "#1d4ed8", "#eff6ff")

    # Yapı kutuları
    s += '<rect x="40" y="58" width="310" height="100" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>'
    s += '<text x="195" y="82" text-anchor="middle" fill="#1e40af" font-size="13" font-weight="700">1. MUZAF (Tamlanan — İlk Kelime)</text>'
    s += '<text x="195" y="106" text-anchor="middle" fill="#1e293b" font-size="10.5">• Başına EL- (harf-i tarif) ALMAZ!</text>'
    s += '<text x="195" y="126" text-anchor="middle" fill="#1e293b" font-size="10.5">• Sonuna TENVİN (-un/-in/-an) ALMAZ!</text>'
    s += '<text x="195" y="145" text-anchor="middle" fill="#1d4ed8" font-size="10.5" font-weight="700">Örnek: Ehu (Kardeşi) / İbnü (Oğlu)</text>'

    s += '<text x="380" y="114" text-anchor="middle" fill="#2563eb" font-size="24" font-weight="700">+</text>'

    s += '<rect x="410" y="58" width="310" height="100" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6"/>'
    s += '<text x="565" y="82" text-anchor="middle" fill="#166534" font-size="13" font-weight="700">2. MUZAFUN İLEYH (Tamlayan)</text>'
    s += '<text x="565" y="106" text-anchor="middle" fill="#1e293b" font-size="10.5">• Belirli ise başına EL- alır.</text>'
    s += '<text x="565" y="126" text-anchor="middle" fill="#1e293b" font-size="10.5">• Daima MECRUR (sonu esreli / -i) olur!</text>'
    s += '<text x="565" y="145" text-anchor="middle" fill="#15803d" font-size="10.5" font-weight="700">Örnek: el-Ebi (Babanın) / el-Ammi (Amcanın)</text>'

    # Örnek şeritler
    ornekler = [
        ("Vâlidü'l-ebi = El-Cedd", "Babanın babası = Dede"),
        ("Uhtu'l-ümmi = El-Hâletü", "Annenin kız kardeşi = Teyze"),
        ("İbnü'l-ehi / Bintü'l-uhti", "Erkek kardeşin oğlu / Kız kardeşin kızı (Yeğen)"),
        ("Sılatü'r-rahimi", "Akrabalık bağını gözetmek / Akraba ziyareti"),
    ]
    for i, (ar_ok, tr) in enumerate(ornekler):
        x = 40 + (i % 2) * 350
        y = 175 + (i // 2) * 55
        s += f'<rect x="{x}" y="{y}" width="330" height="44" rx="8" fill="#fff" stroke="#93c5fd" stroke-width="1.2"/>'
        s += f'<text x="{x+14}" y="{y+19}" fill="#1e3a8a" font-size="11" font-weight="700">{ar_ok}</text>'
        s += f'<text x="{x+14}" y="{y+35}" fill="#475569" font-size="10">{tr}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Bitişik İyelik Zamirleri (Mutasıl Zamirler) ile Akrabalarım."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İyelik Zamirleriyle Akraba Tanıtımı (Ammî, Ammetüke, Cedduhû)", "#b45309", "#fffbeb")

    zamirler = [
        ("Benim (-î)", "Amm-î / Hâl-î", "Benim amcam / Benim dayım", "#d97706"),
        ("Senin — Erkek (-ke)", "Ammü-ke / Ceddetü-ke", "Senin amcan / Senin ninen", "#0284c7"),
        ("Senin — Kadın (-ki)", "Ammü-ki / Hâletü-ki", "Senin amcan / Senin teyzen", "#7c3aed"),
        ("Onun — Erkek (-hû)", "Ammü-hû / Ceddü-hû", "Onun amcası / Onun dedesi", "#0d9488"),
        ("Onun — Kadın (-hâ)", "Ammü-hâ / Hâlü-hâ", "Onun amcası / Onun dayısı", "#dc2626"),
        ("Bizim (-nâ)", "Usretü-nâ / Ekaribü-nâ", "Bizim ailemiz / Bizim akrabalarımız", "#16a34a"),
    ]
    for i, (bas, ok, tr, r) in enumerate(zamirler):
        x = 28 + (i % 3) * 240
        y = 58 + (i // 3) * 116
        s += f'<rect x="{x}" y="{y}" width="224" height="100" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="{y}" width="224" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="{y+18}" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="{y+52}" text-anchor="middle" fill="{r}" font-size="11.5" font-weight="700">{ok}</text>'
        s += f'<text x="{x+112}" y="{y+76}" text-anchor="middle" fill="#334155" font-size="10">{tr}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Sıla-i Rahim (Akraba Ziyareti) Fiilleri ve Değerlerimiz."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Değerlerim: Sıla-i Rahim (Akraba Ziyareti) ve İletişim Kalıpları", "#15803d", "#f0fdf4")

    kalip = [
        ("Ezûru ekaribî fi'l-utleti", "Tatilde akrabalarımı ziyaret ederim.", "Fiil: Zâra - Yezûru (Ziyaret etmek)"),
        ("Ehterimü'l-kibâra ve erhamü's-sığâra", "Büyüklere saygı duyar, küçüklere şefkat gösteririm.", "Fiil: İhterame - Yehterimü (Saygı duymak)"),
        ("Üsâidü ceddî ve ceddetî", "Dedeme ve nineme yardım ederim.", "Fiil: Sâade - Yüsâidü (Yardım etmek)"),
        ("Sılatü'r-rahimi tezîdü'l-mehabbete", "Sıla-i rahim (akraba ziyareti) sevgiyi artırır.", "Değer: El-Mehabbe ve't-Teâvün (Sevgi ve Yardımlaşma)"),
    ]
    for i, (ar_ok, tr, notu) in enumerate(kalip):
        y = 56 + i * 60
        s += f'<rect x="36" y="{y}" width="688" height="50" rx="8" fill="#fff" stroke="#22c55e" stroke-width="1.4"/>'
        s += f'<text x="52" y="{y+20}" fill="#166534" font-size="11.5" font-weight="700">{ar_ok}</text>'
        s += f'<text x="52" y="{y+38}" fill="#334155" font-size="10.5">{tr}</text>'
        s += f'<text x="708" y="{y+29}" text-anchor="end" fill="#0d9488" font-size="10" font-weight="700">{notu}</text>'

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
