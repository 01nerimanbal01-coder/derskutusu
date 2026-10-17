# -*- coding: utf-8 -*-
"""10. Sınıf Fıkıh — 5. Hafta Görselleri
Konu: 1. Fıkıh İlmi ve Tarihi — Fıkıh Tarihi ve Dönemleri
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#b45309", arka="#fffbeb"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Fıkıh Tarihinin Kronolojik Dönemleri Şeması."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "İslam Hukuku (Fıkıh) Tarihinin Ana Dönemleri", "#b45309", "#fffbeb")

    donemler = [
        ("1. Hz. Peygamber Dönemi", "(610 - 632 / Teşri Devri)", "Vahyin (Kur'an ve Sünnet)", "indiği kurucu dönemdir.", "Mekke: İman ve ahlak;", "Medine: İbadet ve hukuk.", "#047857", "#ecfdf5"),
        ("2. Sahabe Dönemi", "(632 - ~710 / Hulefâ-yi Râşidîn)", "Yeni fetihlerle karşılaşılan", "sorunlara Kur'an, Sünnet,", "İcma ve Re'y (İçtihat) ile", "çözüm üretilmiştir.", "#0284c7", "#f0f9ff"),
        ("3. Tabiîn ve Tedvin Dönemi", "(8. - 10. Yüzyıl / Mezhepler)", "Ehl-i Re'y (Kûfe) ve Ehl-i", "Hadis (Medine) ekolleri", "doğmuş; fıkıh mezhepleri", "kurumsallaşmıştır.", "#7c3aed", "#f5f3ff"),
        ("4. Taklit, Kanunlaştırma &amp; Çağdaş", "(10. yy -> Günümüz)", "Mezhep içi tercih, Osmanlı'da", "Mecelle-i Ahkâm-ı Adliyye ve", "günümüz fıkıh kurullarında", "kolektif içtihat çalışmaları.", "#d97706", "#fffbeb"),
    ]
    for i, (bas, tarih, a1, a2, a3, a4, r, bg) in enumerate(donemler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="55" width="168" height="235" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="74" text-anchor="middle" fill="#fff" font-size="10.2" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="99" text-anchor="middle" fill="{r}" font-size="9.5" font-weight="700">{tarih}</text>'
        s += f'<text x="{x+84}" y="132" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="150" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="168" text-anchor="middle" fill="#1e293b" font-size="10">{a3}</text>'
        s += f'<text x="{x+84}" y="186" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a4}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Hz. Peygamber Dönemi Teşri (Yasama) İlkeleri ve Muaz b. Cebel Hadisi."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Hz. Peygamber Döneminde Teşri (Hüküm Koyma) İlkeleri ve İçtihat Eğitimi", "#047857", "#ecfdf5")

    # Sol: 3 Teşri İlkesi
    s += '<rect x="28" y="55" width="340" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="198" y="76" text-anchor="middle" fill="#065f46" font-size="12" font-weight="700">1. Teşri (Hüküm Koyma) İlkeleri</text>'

    ilkeler = [
        ("Tedrîcîlik (Aşamalı Hüküm):", "Hükümlerin toplumun alışması için zamana yayılarak konması."),
        ("Kolaylaştırma (Adem-i Harac):", "Zorluğun kaldırılması; 'Kolaylaştırınız, zorlaştırmayınız!'"),
        ("Yükümlülüklerin Azlığı:", "İnsan gücünü aşan ağır sorumlulukların yüklenmemesi."),
    ]
    for i, (b, ac) in enumerate(ilkeler):
        y = 92 + i * 58
        s += f'<rect x="44" y="{y}" width="308" height="48" rx="6" fill="#f0fdf4" stroke="#10b981"/>'
        s += f'<text x="54" y="{y+18}" fill="#065f46" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="54" y="{y+36}" fill="#334155" font-size="9.5">{ac}</text>'

    # Sağ: Muaz b. Cebel Yöntemi
    s += '<rect x="392" y="55" width="340" height="230" rx="10" fill="#fff" stroke="#6ee7b7" stroke-width="1.5"/>'
    s += '<text x="562" y="76" text-anchor="middle" fill="#065f46" font-size="12" font-weight="700">2. Muaz b. Cebel\'in Hüküm Sıralaması (Yemen)</text>'

    adim = [
        ("1. Adım: Kitabullah (Kur'an-ı Kerim)", "Önce Allah'ın Kitabına başvururum.", "#047857"),
        ("2. Adım: Sünnet-i Resulullah", "Kur'an'da bulamazsam Peygamberin Sünnetine bakarım.", "#0284c7"),
        ("3. Adım: Re'y ile İçtihat", "Orada da bulamazsam kendi görüşümle içtihat ederim!", "#d97706"),
    ]
    for i, (b, ac, r) in enumerate(adim):
        y = 92 + i * 58
        s += f'<rect x="408" y="{y}" width="308" height="48" rx="6" fill="#fff" stroke="{r}" stroke-width="1.4"/>'
        s += f'<text x="418" y="{y+18}" fill="{r}" font-size="10.5" font-weight="700">{b}</text>'
        s += f'<text x="418" y="{y+36}" fill="#334155" font-size="9.8">{ac}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Tabiîn Dönemi: Hicaz (Ehl-i Hadis) ve Irak/Kûfe (Ehl-i Re'y) Ekolleri."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Tabiîn Döneminde İki Büyük Fıkıh Havzası: Hicaz ve Irak Ekolleri", "#1d4ed8", "#eff6ff")

    # Sol: Hicaz (Ehl-i Hadis)
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#93c5fd" stroke-width="1.5"/>'
    s += '<rect x="30" y="55" width="335" height="30" rx="10" fill="#2563eb"/>'
    s += '<text x="197" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. HİCAZ / MEDİNE EKOLÜ (Ehl-i Hadis / Eser)</text>'
    s += '<text x="46" y="106" fill="#1e40af" font-size="10.5" font-weight="700">• Merkez:</text><text x="115" y="106" fill="#334155" font-size="10.5">Medine ve Mekke</text>'
    s += '<text x="46" y="130" fill="#1e40af" font-size="10.5" font-weight="700">• Sahabi Öncüleri:</text><text x="150" y="130" fill="#334155" font-size="10.5">Hz. Ömer, Zeyd b. Sabit, İbn Ömer, Hz. Aişe</text>'
    s += '<text x="46" y="154" fill="#1e40af" font-size="10.5" font-weight="700">• Tabiîn Öncüsü:</text><text x="145" y="154" fill="#334155" font-size="10.5">Fukaha-i Seb\'a (Said b. Müseyyeb vb.)</text>'
    s += '<text x="46" y="178" fill="#1e40af" font-size="10.5" font-weight="700">• Yöntemi:</text><text x="115" y="178" fill="#334155" font-size="10">Hadis ve sünnet mirası zengindir; gerçekleşmemiş</text>'
    s += '<text x="46" y="194" fill="#334155" font-size="10">farazi meseleler hakkında hüküm vermekten kaçınırlar.</text>'
    s += '<rect x="46" y="212" width="303" height="54" rx="6" fill="#eff6ff" stroke="#60a5fa"/>'
    s += '<text x="197" y="234" text-anchor="middle" fill="#1d4ed8" font-size="10.5" font-weight="700">Temsilcisi Mezhepler:</text>'
    s += '<text x="197" y="252" text-anchor="middle" fill="#1e293b" font-size="10.5">Maliki, Şafii ve Hanbeli Mezhepleri</text>'

    # Sağ: Irak (Ehl-i Re'y)
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#fcd34d" stroke-width="1.5"/>'
    s += '<rect x="395" y="55" width="335" height="30" rx="10" fill="#d97706"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. IRAK / KÛFE EKOLÜ (Ehl-i Re\'y)</text>'
    s += '<text x="411" y="106" fill="#92400e" font-size="10.5" font-weight="700">• Merkez:</text><text x="480" y="106" fill="#334155" font-size="10.5">Kûfe ve Basra (Kozmopolit bölge)</text>'
    s += '<text x="411" y="130" fill="#92400e" font-size="10.5" font-weight="700">• Sahabi Öncüleri:</text><text x="515" y="130" fill="#334155" font-size="10.5">Abdullah b. Mes\'ûd ve Hz. Ali</text>'
    s += '<text x="411" y="154" fill="#92400e" font-size="10.5" font-weight="700">• Tabiîn Öncüsü:</text><text x="510" y="154" fill="#334155" font-size="10.5">Alkame, İbrahim en-Nehaî, Hammad</text>'
    s += '<text x="411" y="178" fill="#92400e" font-size="10.5" font-weight="700">• Yöntemi:</text><text x="480" y="178" fill="#334155" font-size="10">Hükümlerin illetlerini (gerekçelerini) araştırır;</text>'
    s += '<text x="411" y="194" fill="#334155" font-size="10">kıyas ve farazi fıkıh yöntemini etkin kullanırlar.</text>'
    s += '<rect x="411" y="212" width="303" height="54" rx="6" fill="#fffbeb" stroke="#f59e0b"/>'
    s += '<text x="562" y="234" text-anchor="middle" fill="#b45309" font-size="10.5" font-weight="700">Temsilcisi Mezhep:</text>'
    s += '<text x="562" y="252" text-anchor="middle" fill="#1e293b" font-size="10.5">İmam Ebu Hanife ve Hanefi Mezhebi</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Dört Büyük Ameli-Fıkhi Mezhep ve Mecelle'den Günümüze Fıkıh."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Fıkıh Mezheplerinin Teşekkülü ve Kanunlaştırma (Mecelle) Süreci", "#7c3aed", "#f5f3ff")

    imamlar = [
        ("Hanefi Mezhebi", "İmam-ı Azam Ebu Hanife", "(v. 150/767 — Kûfe)", "Ebu Yusuf &amp; İmam Muhammed", "Kıyas ve İstihsan", "#0284c7"),
        ("Maliki Mezhebi", "İmam Malik b. Enes", "(v. 179/795 — Medine)", "Eser: El-Muvatta'", "Medine Ehlinin Ameli", "#16a34a"),
        ("Şafii Mezhebi", "İmam Muhammed eş-Şafii", "(v. 204/820 — Mısır)", "Eser: Er-Risâle (İlk Usul)", "Ehl-i Hadis &amp; Re'y Sentezi", "#d97706"),
        ("Hanbeli Mezhebi", "İmam Ahmed b. Hanbel", "(v. 241/855 — Bağdat)", "Eser: El-Müsned", "Nas ve Sahabe Kavli", "#7c3aed"),
    ]
    for i, (mez, imam, tar, eser, oz, r) in enumerate(imamlar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="55" width="168" height="175" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="55" width="168" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="73" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{mez}</text>'
        s += f'<text x="{x+84}" y="99" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{imam}</text>'
        s += f'<text x="{x+84}" y="116" text-anchor="middle" fill="#64748b" font-size="9.5">{tar}</text>'
        s += f'<text x="{x+84}" y="142" text-anchor="middle" fill="#1e293b" font-size="9.8">{eser}</text>'
        s += f'<text x="{x+84}" y="168" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{oz}</text>'

    s += '<rect x="26" y="242" width="708" height="44" rx="8" fill="#ede9fe" stroke="#7c3aed"/>'
    s += '<text x="380" y="261" text-anchor="middle" fill="#5b21b6" font-size="11" font-weight="700">Kanunlaştırma Dönemi (19. yy): Ahmet Cevdet Paşa başkanlığında hazırlanan 1851 maddelik</text>'
    s += '<text x="380" y="278" text-anchor="middle" fill="#6d28d9" font-size="10.5">&quot;Mecelle-i Ahkâm-ı Adliyye&quot;, İslam hukukunun medeni kanun tarzında ilk büyük kanunlaştırma eseridir.</text>'

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
