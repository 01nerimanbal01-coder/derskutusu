# -*- coding: utf-8 -*-
"""5. Sınıf Temel Dini Bilgiler — 5. Hafta Görselleri (Mümin Kimliğim: Kelime-i Tevhid ve Kelime-i Şehadet)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">İmanın Özü ve İslam\'ın Anahtarı: Kelime-i Tevhid ve Kelime-i Şehadet</text>',
        _kart(30, 50, 335, 215, "Kelime-i Tevhid (Birleme Sözü)", [
            "• Okunuşu: 'Lâ ilâhe illallâh,",
            "  Muhammedün Rasûlullâh.'",
            "• Anlamı: 'Allah'tan başka ilah yoktur,",
            "  Hz. Muhammed O'nun elçisidir.'",
            "• Birinci bölüm tevhidi (Allah'ın birliğini),",
            "  ikinci bölüm risaleti (peygamberliği) bildirir."
        ], "#0284c7", "#f0f9ff"),
        _kart(395, 50, 335, 215, "Kelime-i Şehadet (Tanıklık Sözü)", [
            "• Okunuşu: 'Eşhedü en lâ ilâhe illallâh ve",
            "  eşhedü enne Muhammeden abdühû ve rasûlüh.'",
            "• Anlamı: 'Ben şahitlik ederim ki Allah'tan",
            "  başka ilah yoktur; yine şahitlik ederim ki",
            "  Hz. Muhammed O'nun kulu ve elçisidir.'",
            "• İslam'ın beş şartından birincisidir."
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">İmanın Boyutları: Kalp ile Tasdik ve Dil ile İkrar</text>',
        _kart(25, 50, 225, 215, "1. Kalp ile Tasdik", [
            "• İmanın asıl yeri kalptir.",
            "• Allah'ın varlığını, birliğini ve",
            "  Hz. Muhammed'in (sav) elçiliğini",
            "  hiç şüphe duymadan kalpten",
            "  onaylamak (tasdik etmek) şarttır.",
            "• Kalbiyle inanan kimseye Mümin denir."
        ], "#8b5cf6", "#f5f3ff"),
        _kart(267, 50, 225, 215, "2. Dil ile İkrar", [
            "• Kalpteki inancı dil ile söyleyip",
            "  açıklamaya 'ikrar' denir.",
            "• Kelime-i Tevhid ve Kelime-i Şehadet",
            "  söyleyerek inancımızı ilan ederiz.",
            "• Böylece toplum içinde mümin ve",
            "  Müslüman kimliğimiz bilinir."
        ], "#2563eb", "#eff6ff"),
        _kart(510, 50, 225, 215, "3. Davranışlara Yansıma", [
            "• Kalpteki iman ve dildeki ikrar,",
            "  güzel ahlak ve salih amellerle",
            "  hayatımıza yansır.",
            "• İbadetler imanı korur ve besler.",
            "• Doğruluk, merhamet ve adalet",
            "  mümin kimliğinin meyvesidir."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mümin Kimliğinin Kazandırdığı Temel Özellikler</text>',
        _kart(30, 50, 335, 215, "Allah'a Güven ve Kulluk Bilinci", [
            "• Yalnızca Allah'a kulluk eder ve O'ndan",
            "  yardım diler (Tevhid bilinci).",
            "• Hz. Muhammed'i (sav) önce kul (abdühû),",
            "  sonra elçi (rasûlüh) olarak örnek alır.",
            "• Nimetlere şükreder, zorluklara sabreder.",
            "• Hayatının bir amacı olduğunu bilir."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Güvenilirlik ve Güzel Ahlak (el-Emîn)", [
            "• 'Müslüman, elinden ve dilinden diğer",
            "  insanların güvende olduğu kimsedir.' (Hadis)",
            "• Sözünde durur, emanete hıyanet etmez.",
            "• Anne-babasına, büyüklerine ve çevresine",
            "  karşı saygılı, merhametli ve dürüsttür.",
            "• İman ile güzel ahlakı birbirinden ayırmaz."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Günlük Hayatta Kelime-i Tevhid ve Şehadet Nerelerde Okunur?</text>',
        _kart(30, 50, 335, 195, "İbadetlerde ve Ezan-Kamette", [
            "• Günde beş vakit okunan Ezan ve Kamet'te",
            "  şehadet ifadeleri tüm dünyaya ilan edilir.",
            "• Namazların oturuşlarında okunan Tahiyyat",
            "  duasının sonunda Kelime-i Şehadet yer alır.",
            "• Müezzin tesbihatında ve zikirlerde okunur."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Hayatın Başlangıcından Sonuna Kadar", [
            "• Yeni doğan bebeğin kulağına ezan ve kametle",
            "  birlikte tevhid ve şehadet fısıldanır.",
            "• İslam'a yeni giren kimse şehadet getirir.",
            "• Yatarken, uyanırken ve iman tazelerken",
            "  müminin dilinden düşmeyen en yüce sözdür."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
