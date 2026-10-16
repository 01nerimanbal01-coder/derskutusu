# -*- coding: utf-8 -*-
"""12. Sınıf Mesleki Arapça — 2. Hafta SVG Görselleri"""

RENK = {
    "kirmizi": "#e63946",
    "mavi": "#2563eb",
    "yesil": "#16a34a",
    "turuncu": "#ea580c",
    "mor": "#7c3aed",
    "lacivert": "#1e293b",
    "acik_mavi": "#eff6ff",
    "acik_yesil": "#f0fdf4",
    "acik_turuncu": "#fff7ed",
    "acik_mor": "#f5f3ff",
    "acik_kirmizi": "#fef2f2",
    "gri": "#64748b",
    "acik_gri": "#f8fafc",
    "cizgi": "#cbd5e1",
}


def _baslik(W, H, etiket, baslik_metni, renk):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px; font-family:\'Inter\', \'Segoe UI\', sans-serif;">'
        f'<rect width="{W}" height="{H}" rx="14" fill="{RENK["acik_gri"]}" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
        f'<rect x="16" y="14" width="110" height="24" rx="6" fill="{renk}"/>'
        f'<text x="71" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{etiket}</text>'
        f'<text x="138" y="31" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{baslik_metni}</text>'
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="{RENK["cizgi"]}" stroke-width="1"/>'
    )


def gorsel_1():
    """el-İlahiyyat (الإلهيات) — Tevhit, Vahdaniyet ve Şirk Kavramları"""
    W, H = 720, 320
    s = _baslik(W, H, "KELİMELER", "2. Ders: el-İlâhiyyât (الإلٰهيّات) Temel Kelime ve İfadeleri", RENK["mavi"])
    kelimeler = [
        ("وَحْدانِيَّة / تَوْحيد", "Vahdâniyye / Tevhîd", "Allah'ın birliği / Birlemek", RENK["yesil"], RENK["acik_yesil"]),
        ("وَحْدَهُ لا شَريكَ لَهُ", "Vahdehû lâ şerîke leh", "O tektir, ortağı yoktur", RENK["mavi"], RENK["acik_mavi"]),
        ("الشِّرْك / شَريك", "eş-Şirk / Şerîk", "Ortak koşma / Ortak", RENK["kirmizi"], RENK["acik_kirmizi"]),
        ("إِخْلاص / مُخْلِصين", "İhlâs / Muhlisîn", "Samimiyet / Dini yalnız Allah'a has kılanlar", RENK["mor"], RENK["acik_mor"]),
        ("الدِّينُ الْحَقّ", "ed-Dînu'l-Hakk", "Hak din (İslam)", RENK["turuncu"], RENK["acik_turuncu"]),
        ("الأُلُوهِيَّة / العِبادَة", "el-Ulûhiyye / el-İbâde", "İlahlık / Kulluk ve ibadet", RENK["lacivert"], "#e2e8f0"),
    ]
    for i, (ar, okunus, tr, rk, ark) in enumerate(kelimeler):
        col = i % 2
        row = i // 2
        x = 22 + col * 344
        y = 62 + row * 82
        s += f'<rect x="{x}" y="{y}" width="332" height="72" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.6"/>'
        s += f'<text x="{x+314}" y="{y+28}" text-anchor="end" font-size="16" font-weight="700" fill="{rk}">{ar}</text>'
        s += f'<text x="{x+16}" y="{y+26}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{okunus}</text>'
        s += f'<text x="{x+16}" y="{y+52}" font-size="11.5" fill="{RENK["gri"]}">{tr}</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Tevhit ve İhlas Ayetleri (Âl-i İmrân 19 ve Beyyine 5)"""
    W, H = 720, 320
    s = _baslik(W, H, "AYETLER", "Tevhit, İslam ve İhlası Vurgulayan Kur'an Ayetleri", RENK["yesil"])
    s += f'<rect x="24" y="64" width="672" height="110" rx="10" fill="{RENK["acik_yesil"]}" stroke="{RENK["yesil"]}" stroke-width="1.8"/>'
    s += f'<text x="360" y="96" text-anchor="middle" font-size="18" font-weight="700" fill="{RENK["yesil"]}">إِنَّ الدِّينَ عِنْدَ اللّٰهِ الْإِسْلَامُ</text>'
    s += f'<text x="360" y="124" text-anchor="middle" font-size="12" font-weight="700" fill="{RENK["lacivert"]}">"Şüphesiz Allah katında din İslam\'dır." (Âl-i İmrân suresi, 19. ayet)</text>'
    s += f'<text x="360" y="150" text-anchor="middle" font-size="11" fill="{RENK["gri"]}">İslam; tevhit inancıyla yalnız Allah\'a teslim olmak ve O\'na hiçbir şeyi ortak koşmamaktır.</text>'

    s += f'<rect x="24" y="190" width="672" height="114" rx="10" fill="{RENK["acik_mavi"]}" stroke="{RENK["mavi"]}" stroke-width="1.8"/>'
    s += f'<text x="360" y="222" text-anchor="middle" font-size="17" font-weight="700" fill="{RENK["mavi"]}">وَمَا أُمِرُوا إِلَّا لِيَعْبُدُوا اللّٰهَ مُخْلِصِينَ لَهُ الدِّينَ حُنَفَاءَ</text>'
    s += f'<text x="360" y="250" text-anchor="middle" font-size="12" font-weight="700" fill="{RENK["lacivert"]}">"Oysa onlara, dini yalnız Allah\'a has kılarak (ihlasla) O\'na kulluk etmeleri emredilmişti." (Beyyine, 5)</text>'
    s += f'<text x="360" y="276" text-anchor="middle" font-size="11" fill="{RENK["gri"]}">Anahtar kalıp: لا يَعْبُدونَ مَعَهُ أَحَدًا (O\'nunla birlikte hiçbir kimseye/varlığa kulluk etmezler).</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """Sahih Fiil (الفعل الصحيح) ve Üç Alt Türü"""
    W, H = 720, 320
    s = _baslik(W, H, "KAVÂİD", "Sahih Fiil (الفِعْلُ الصَّحِيح) ve Üç Kısmı", RENK["mor"])
    s += f'<rect x="190" y="60" width="340" height="52" rx="10" fill="{RENK["mor"]}"/>'
    s += f'<text x="360" y="83" text-anchor="middle" font-size="15" font-weight="800" fill="#fff">الفِعْلُ الصَّحِيح (Sahih Fiil)</text>'
    s += f'<text x="360" y="102" text-anchor="middle" font-size="11" fill="#fff">Asli harflerinde illet harfi (و - ا - ي) bulunmayan fiildir</text>'

    turler = [
        ("1. السَّالِم (Sâlim)", "Hemze ve şedde YOK", "كَتَبَ • دَرَسَ • عَلِمَ • حَفِظَ", "Asli harflerinde hemze veya şedde bulunmayan sahih fiil", RENK["yesil"], RENK["acik_yesil"]),
        ("2. المَهْمُوز (Mehmûz)", "Kökünde HEMZE (ء) var", "أَخَذَ • سَأَلَ • قَرَأَ • بَدَأَ", "Asli harflerinden biri hemze (أ) olan sahih fiil", RENK["mavi"], RENK["acik_mavi"]),
        ("3. المُضَعَّف (Muda'af)", "2. ve 3. harfi AYNI (ّ)", "مَدَّ • رَدَّ • ظَنَّ • ضَلَّ", "İkinci ve üçüncü kök harfi aynı olup şeddelenen fiil", RENK["turuncu"], RENK["acik_turuncu"]),
    ]
    for i, (ad, kisa, ornek, acik, rk, ark) in enumerate(turler):
        x = 20 + i * 230
        y = 142
        s += f'<line x1="360" y1="112" x2="{x+109}" y2="{y}" stroke="{rk}" stroke-width="2"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="158" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="32" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+109}" y="{y+21}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="{x+109}" y="{y+54}" text-anchor="middle" font-size="11.5" font-weight="700" fill="{rk}">{kisa}</text>'
        s += f'<text x="{x+109}" y="{y+86}" text-anchor="middle" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{ornek}</text>'
        s += f'<text x="{x+109}" y="{y+122}" text-anchor="middle" font-size="10.2" fill="{RENK["gri"]}">{acik[:28]}</text>'
        s += f'<text x="{x+109}" y="{y+138}" text-anchor="middle" font-size="10.2" fill="{RENK["gri"]}">{acik[28:]}</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """Mehmûz Fiil (الفعل المهموز) ve Hemzenin Yeri"""
    W, H = 720, 320
    s = _baslik(W, H, "MEHMÛZ FİİL", "Mehmûz Fiilin (المَهْمُوز) Üç Konumu: Başta, Ortada, Sonda", RENK["turuncu"])
    cols = [
        ("Mehmûzü'l-Fâ (Başta ء)", "1. Kök Harfi Hemze", [
            ("أَخَذَ", "ehaze — aldı"),
            ("أَكَلَ", "ekele — yedi"),
            ("أَمَرَ", "emera — emretti"),
            ("أَذِنَ", "ezine — izin verdi"),
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("Mehmûzü'l-Ayn (Ortada ء)", "2. Kök Harfi Hemze", [
            ("سَأَلَ", "se'ele — sordu"),
            ("دَأَبَ", "de'ebe — gayret etti"),
            ("سَئِمَ", "se'ime — usandı"),
            ("زَأَرَ", "ze'era — kükredi"),
        ], RENK["yesil"], RENK["acik_yesil"]),
        ("Mehmûzü'l-Lâm (Sonda ء)", "3. Kök Harfi Hemze", [
            ("قَرَأَ", "kara'e — okudu"),
            ("بَدَأَ", "bede'e — başladı"),
            ("مَلَأَ", "mele'e — doldurdu"),
            ("نَشَأَ", "neşe'e — yetişti"),
        ], RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (t, sub, items, rk, ark) in enumerate(cols):
        x = 20 + i * 230
        y = 64
        s += f'<rect x="{x}" y="{y}" width="218" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+109}" y="{y+22}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{t}</text>'
        s += f'<text x="{x+109}" y="{y+54}" text-anchor="middle" font-size="11" font-weight="700" fill="{rk}">{sub}</text>'
        for j, (ar, tr) in enumerate(items):
            yy = y + 88 + j * 36
            s += f'<text x="{x+24}" y="{yy}" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{ar}</text>'
            s += f'<text x="{x+85}" y="{yy}" font-size="11.5" fill="{RENK["gri"]}">({tr})</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """Muda'af ve Sâlim Fiil Örnekleri"""
    W, H = 720, 320
    s = _baslik(W, H, "MUDA'AF & SÂLİM", "Muda'af (المُضَعَّف) ve Sâlim (السَّالِم) Fiil Örnekleri", RENK["lacivert"])
    boxes = [
        ("المُضَعَّف (Muda'af Fiiller)", "2. ve 3. harfi aynı olup şeddelenenler", [
            ("مَدَّ (أَصْلُهُ: مَدَدَ)", "medde — uzattı"),
            ("رَدَّ (أَصْلُهُ: رَدَدَ)", "radde — geri çevirdi"),
            ("مَسَّ (أَصْلُهُ: مَسِسَ)", "messe — dokundu"),
            ("ضَلَّ / ظَنَّ / شَكَّ / حَجَّ", "saptı / zannetti / şüphelendi / hac yaptı"),
        ], RENK["turuncu"], RENK["acik_turuncu"]),
        ("السَّالِم (Sâlim Fiiller)", "İçinde illet harfi, hemze ve şedde olmayanlar", [
            ("كَتَبَ / دَرَسَ", "ketebe (yazdı) / derase (ders çalıştı)"),
            ("عَلِمَ / حَفِظَ", "alime (bildi) / hafiza (ezberledi, korudu)"),
            ("جَلَسَ / شَرَحَ", "celese (oturdu) / şeraha (açıkladı)"),
            ("عَبَدَ / شَكَرَ", "abede (kulluk etti) / şekera (şükretti)"),
        ], RENK["yesil"], RENK["acik_yesil"]),
    ]
    for i, (b, alt, items, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+58}" font-size="11" font-weight="700" fill="{rk}">{alt}</text>'
        for j, (ar, tr) in enumerate(items):
            yy = y + 92 + j * 36
            s += f'<text x="{x+16}" y="{yy}" font-size="13" font-weight="700" fill="{RENK["lacivert"]}">• {ar}</text>'
            s += f'<text x="{x+16}" y="{yy+16}" font-size="10.8" fill="{RENK["gri"]}">  {tr}</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """Sahih Fiili Tanıma Algoritması (Kontrol Şeması)"""
    W, H = 720, 310
    s = _baslik(W, H, "ÖZET ŞEMA", "Bir Fiilin Sahih Türünü (Sâlim / Mehmûz / Muda'af) Bulma Adımları", RENK["kirmizi"])
    steps = [
        ("1. ADIM: Mâzî (Geçmiş Zaman) 3 Harfli Köküne Bak", "Fiil çekimli veya mezîd ise önce üç harfli sülâsî mücerred köküne indirilir (Örn: يَعْبُدُونَ → عَبَدَ).", RENK["lacivert"], "#e2e8f0"),
        ("2. ADIM: Kökte İllet Harfi (و - ا - ي) Var mı?", "Yoksa fiil SAHİH FİİLDİR (الفعل الصحيح). Varsa Mu'tel fiildir (Örn: وَأَدَ fiilinde 'و' bulunduğu için sahih değil, mu'teldir!).", RENK["kirmizi"], RENK["acik_kirmizi"]),
        ("3. ADIM: Kökte Hemze (أ / ء) veya Şedde (ّ) Var mı?", "Hemze varsa → MEHMÛZ (أَخَذَ، سَأَلَ، قَرَأَ) | Şedde varsa → MUDA'AF (مَدَّ، ضَلَّ) | İkisi de yoksa → SÂLİM (كَتَبَ، عَبَدَ).", RENK["yesil"], RENK["acik_yesil"]),
    ]
    for i, (st, desc, rk, ark) in enumerate(steps):
        y = 64 + i * 76
        s += f'<rect x="24" y="{y}" width="672" height="62" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="42" y="{y+25}" font-size="13" font-weight="800" fill="{rk}">{st}</text>'
        s += f'<text x="42" y="{y+47}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">{desc}</text>'
    s += "</svg>"
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
    "b5": gorsel_5(),
    "b6": gorsel_6(),
}



def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
