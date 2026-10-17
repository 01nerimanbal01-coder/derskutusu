# -*- coding: utf-8 -*-
"""8. Sınıf İngilizce — 5. Hafta Görselleri (Unit 2: Teen Life - Expressing Preferences & Personal Opinions)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Expressing Preferences: PREFER vs. WOULD RATHER</text>',
        _kart(30, 50, 335, 215, "1. PREFER + Noun / V-ing + TO + Noun / V-ing", [
            "• İki isim arasında tercih: prefer A to B",
            "  Örnek: I prefer pop music TO rock music.",
            "• İki eylem arasında tercih: prefer V-ing TO V-ing",
            "  Örnek: She prefers reading books TO watching TV.",
            "• Dikkat: 'prefer' yapısında arada 'than' değil,",
            "  daima 'TO' edatı ve fiilde '-ing' kullanılır!"
        ], "#0284c7", "#f0f9ff"),
        _kart(395, 50, 335, 215, "2. WOULD RATHER + V1 + THAN + V1", [
            "• Yalın fiille tercih: would rather V1 than V1",
            "  Örnek: I would rather go camping THAN stay home.",
            "• Kısaltması: I'd rather listen to jazz than rap.",
            "• Olumsuz şekli: I'd rather NOT go out tonight.",
            "• Dikkat: 'would rather' sonrasında fiil YALIN (V1)",
            "  gelir ve karşılaştırmada 'THAN' kullanılır!"
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Stating Personal Opinions: Adjectives &amp; Expressions</text>',
        _kart(25, 50, 225, 215, "Opinion Starter Phrases", [
            "• In my opinion, ... (Bence)",
            "• To me, ... / For me, ... (Bana göre)",
            "• I think / I believe ...",
            "• From my point of view, ...",
            "• If you ask me, ...",
            "• What do you think about...?"
        ], "#8b5cf6", "#f5f3ff"),
        _kart(267, 50, 225, 215, "Positive Adjectives (+)", [
            "• terrific / awesome (harika)",
            "• impressive (etkileyici)",
            "• harmonic / energetic (uyumlu/enerjik)",
            "• trendy / fashionable (modaya uygun)",
            "• exciting / fascinating (heyecan verici)",
            "• relaxing / fun (rahatlatıcı/eğlenceli)"
        ], "#2563eb", "#eff6ff"),
        _kart(510, 50, 225, 215, "Negative Adjectives (-)", [
            "• unbearable (katlanılmaz)",
            "• ridiculous (saçma / gülünç)",
            "• snob (züppe / kendini beğenmiş)",
            "• boring / dull (sıkıcı)",
            "• loud / noisy (çok gürültülü)",
            "• nerdy / old-fashioned (demode)"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Teen Life Vocabulary: Music Types, Camping &amp; Free Time</text>',
        _kart(30, 50, 335, 215, "Music Genres (Müzik Türleri)", [
            "• Classical / Jazz / Folk (Halk müziği)",
            "• Pop / Rock / Heavy Metal / Rap / Beatbox",
            "• Indian / Techno / Opera",
            "• Example: 'I am fond of folk music because",
            "  it is authentic and relaxing.'",
            "• Example: 'I can't stand heavy metal; it's unbearable!'"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Camping Equipment &amp; Activities", [
            "• pitch a tent (çadır kurmak)",
            "• make a campfire (kamp ateşi yakmak)",
            "• sleeping bag (uyku tulumu) &amp; backpack (sırt çantası)",
            "• torch / flashlight (el feneri) &amp; compass (pusula)",
            "•pocketknife (çakı) &amp; rope (ip / halat)",
            "• trekking / hiking (doğa yürüyüşü)"
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Making Simple Inquiries: Question Words &amp; Frequency</text>',
        _kart(30, 50, 335, 195, "Key Question Patterns", [
            "• How often do you train? — Twice a week.",
            "• What kind of music/books do you like?",
            "• Who is your favourite singer/author?",
            "• Which one do you prefer, cycling or skating?",
            "• Why do you prefer casual clothes?"
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Frequency Expressions Review", [
            "• Always (100%) &gt; Usually &gt; Often &gt; Sometimes",
            "  &gt; Rarely / Seldom &gt; Hardly ever &gt; Never (0%)",
            "• Once a day / Twice a week / Three times a month",
            "• Every morning / On weekdays / At weekends",
            "• Example: 'I seldom wear formal clothes.'"
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
