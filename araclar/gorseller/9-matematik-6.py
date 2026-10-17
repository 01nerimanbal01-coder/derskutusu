def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'


def _kart(x, y, w, h, baslik, satirlar, bg, border, text_c):
    rx = 12
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg}" stroke="{border}" stroke-width="2"/>'
    s += f'<text x="{x + w/2}" y="{y + 26}" font-family="sans-serif" font-size="14" font-weight="bold" fill="{text_c}" text-anchor="middle">{baslik}</text>'
    s += f'<line x1="{x+12}" y1="{y+36}" x2="{x+w-12}" y2="{y+36}" stroke="{border}" stroke-width="1" stroke-dasharray="3,3"/>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x + w/2}" y="{y + 58 + i*22}" font-family="sans-serif" font-size="12" fill="#334155" text-anchor="middle">{st}</text>'
    return s


def gorsel_1():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">GERÇEK SAYILARIN TOPLAMA VE ÇARPMA ÖZELLİKLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Kapalılık &amp; Değişme", ["Her a, b gerçek sayısı için:", "a+b ve a.b gerçek sayıdır", "Değişme: a + b = b + a", "Değişme: a . b = b . a"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Birleşme &amp; Dağılma", ["(a+b)+c = a+(b+c)", "(a.b).c = a.(b.c)", "Dağılma: a.(b+c) = a.b + a.c", "Ortak çarpan parantezi!"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Birim, Ters &amp; Yutan", ["Toplama birim: 0 | Ters: -a", "Çarpma birim: 1 | Ters: 1/a", "(a ≠ 0 için a . (1/a) = 1)", "Çarpmada yutan eleman: 0"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">SAYISAL İŞLEMDEN CEBİRSEL ÖZDEŞLİĞE ANALOJİ</text>'
    ic += _kart(30, 56, 195, 160, "Tam Kare Özdeşliği", ["(a + b)² = a² + 2ab + b²", "(a - b)² = a² - 2ab + b²", "Sayısal: 103² = (100+3)²", "10000 + 600 + 9 = 10609"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "İki Kare Farkı", ["a² - b² = (a - b).(a + b)", "Sayısal Analoji:", "98 . 102 = (100-2).(100+2)", "= 100² - 2² = 9996"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Geometrik Modelleme", ["Kenarı (a+b) olan kare alanı:", "a² ve b² iki kare ile", "a.b alanlı iki dikdörtgen", "Toplam alan = a² + 2ab + b²"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">GERÇEK SAYILARDA SIRALAMA VE EŞİTSİZLİK ÖZELLİKLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Geçişme &amp; Toplama", ["a &lt; b ve b &lt; c ise a &lt; c", "a &lt; b iken her c için:", "a + c &lt; b + c", "Eşitsizlik yön değiştirmez"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Pozitif Sayıyla Çarpma", ["a &lt; b ve c &gt; 0 ise:", "a . c &lt; b . c", "Bölmede: a/c &lt; b/c", "Eşitsizlik yönü AYNIDIR"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Negatif Sayıyla Çarpma", ["a &lt; b ve c &lt; 0 ise:", "a . c &gt; b . c", "Negatifle çarpılıp bölününce", "Eşitsizlik YÖN DEĞİŞTİRİR!"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">CEBİRSEL İFADELERDE ÇARPANLARA AYIRMA STRATEJİLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Ortak Çarpan Parantezi", ["Dağılma özelliğinin tersi", "ax + ay = a.(x + y)", "6x²y - 9xy² = 3xy.(2x - 3y)", "Her terimde ortak olanı bul"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Gruplandırma Yöntemi", ["ax + ay + bx + by", "= a.(x + y) + b.(x + y)", "= (x + y).(a + b)", "4 terimli ifadelerde kullanılır"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Sıfır Çarpan Özelliği", ["a . b = 0 ise:", "a = 0 veya b = 0’dır", "(x - 3).(x + 5) = 0", "Çözüm: x = 3 veya x = -5"], "#f1f5f9", "#64748b", "#334155")
    return _svg(w, h, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    bolumler = v.get("bolumler", [])
    eslesme = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    for idx, key in eslesme:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[key]
