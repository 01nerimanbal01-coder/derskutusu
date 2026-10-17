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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">KALITIMIN TEMEL KAVRAMLARI</text>'
    ic += _kart(30, 56, 195, 160, "Gen ve Alel", ["Kalıtsal özellik birimi: Gen", "Biri anneden biri babadan", "gelen gen çifti: Alel", "Baskın (A) ve Çekinik (a)"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Saf ve Melez Döl", ["Saf (Homozigot): AA veya aa", "Aleller birbiriyle aynıdır", "Melez (Heterozigot): Aa", "Aleller birbirinden farklıdır"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Genotip ve Fenotip", ["Genotip: Gen yapısı (AA, Aa)", "Fenotip: Dış görünüş (Mor, Beyaz)", "Fenotip = Genotip + Çevre", "Çekinik özellik sadece aa’da!"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">MENDEL VE BEZELYELERDE BASKIN / ÇEKİNİK ÖZELLİKLER</text>'
    ic += _kart(30, 56, 195, 160, "Neden Bezelye?", ["Kolay yetiştirilir, hızlı ürer", "Kendi kendine tozlaşabilir", "Çok sayıda zıt karakteri var", "Maliyeti düşük ve gözlemi kolay"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Baskın Özellikler", ["Mor çiçek > Beyaz çiçek", "Sarı tohum > Yeşil tohum", "Düzgün tohum > Buruşuk", "Uzun boy > Kısa boy"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "İnsanda Kalıtsal Özellikler", ["Koyu göz > Açık (yeşil/mavi) göz", "Kıvırcık saç > Düz saç", "Ayrık kulak memesi > Yapışık", "Siyah saç > Sarı saç"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TEK KARAKTER ÇAPRAZLAMALARI (F1 VE F2 DÖLLERİ)</text>'
    ic += _kart(30, 56, 195, 160, "1. Çaprazlama: AA x aa", ["Saf Baskın x Saf Çekinik", "Oluşan döller: %100 Aa", "Genotip: %100 Melez", "Fenotip: %100 Baskın (Mor)"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "2. Çaprazlama: Aa x Aa", ["Melez x Melez çaprazlaması", "Oluşanlar: AA, Aa, Aa, aa", "Genotip: %25 AA, %50 Aa, %25 aa", "Fenotip: %75 Baskın, %25 Çekinik"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "3. Çaprazlama: Aa x aa", ["Melez x Saf Çekinik", "Oluşanlar: Aa, Aa, aa, aa", "Genotip: %50 Aa, %50 aa", "Fenotip: %50 Baskın, %50 Çekinik"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">İNSANDA CİNSİYETİN BELİRLENMESİ VE AKRABA EVLİLİĞİ</text>'
    ic += _kart(30, 56, 300, 160, "Cinsiyet Kalıtımı (XX x XY)", ["• Dişi birey: 44 + XX | Erkek birey: 44 + XY", "• Çaprazlama: XX x XY -> XX, XY, XX, XY", "• Kız veya erkek olma olasılığı daima %50’dir", "• Bebeğin cinsiyetini babadan gelen X veya Y belirler"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(350, 56, 300, 160, "Akraba Evliliğinin Sakıncaları", ["• Çekinik hastalık genlerinin (a) karşılaşma riski artar", "• Taşıyıcı ebeveynlerden (Aa x Aa) %25 hasta (aa) doğabilir", "• Akdeniz anemisi, orak hücreli anemi, kistik fibrozis", "• Evlilik öncesi genetik tarama ve danışmanlık önemlidir"], "#e0e7ff", "#6366f1", "#4338ca")
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
