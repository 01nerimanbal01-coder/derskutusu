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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">RASYONEL SAYILARDA TOPLAMA VE ÇIKARMA İŞLEMİ</text>'
    ic += _kart(30, 56, 195, 160, "1. Eşit Paydalar", ["Paylar toplanır/çıkarılır", "Ortak payda aynen yazılır", "(-2/7) + (-3/7) = -5/7", "İşaret kurallarına dikkat!"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "2. Farklı Paydalar", ["Paydalar EKOK ile eşitlenir", "Genişletme işlemi yapılır", "(3/4) - (5/6) = (9-10)/12", "Sonuç: -1/12 (en sade hal)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "3. İşlem Özellikleri", ["Değişme ve Birleşme var", "Etkisiz eleman: 0", "Toplama göre ters: -a/b", "(a/b) + (-a/b) = 0"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">RASYONEL SAYILARDA ÇARPMA VE BÖLME İŞLEMİ</text>'
    ic += _kart(30, 56, 195, 160, "Çarpma Kuralları", ["Pay x Pay / Payda x Payda", "Önce sadeleştirme yap!", "Aynı işaretliler: (+)", "Zıt işaretliler: (-)"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "Çarpmaya Göre Ters", ["Pay ve payda yer değiştirir", "İşaret ASLA değişmez!", "-3/5 tersi -> -5/3", "0 sayısının tersi YOKTUR"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "Bölme İşlemi", ["1. sayı aynen yazılır", "2. sayı ters çevrilip çarpılır", "(a/b) : (c/d) = (a/b) . (d/c)", "Ana kesir çizgisi hizası!"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">RASYONEL SAYILARIN KUVVETLERİ VE ÇOK ADIMLI İŞLEMLER</text>'
    ic += _kart(30, 56, 195, 160, "Karesi ve Küpü", ["Negatifin çift kuvveti (+)", "(-2/3)² = +4/9", "Negatifin tek kuvveti (-)", "(-2/3)³ = -8/27"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "İşlem Önceliği", ["1. Üslü ifadeler", "2. Parantez içi işlemler", "3. Çarpma veya bölme", "4. Toplama veya çıkarma"], "#fef9c3", "#eab308", "#a16207")
    ic += _kart(454, 56, 195, 160, "Merdivenli Kesirler", ["En alt/iç basamaktan başla", "Ana kesir çizgisini belirle", "Üstteki pay, alttaki payda", "Adım adım sadeleştir"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">RASYONEL SAYI PROBLEMLERİ ÇÖZÜM STRATEJİLERİ</text>'
    ic += _kart(30, 56, 195, 160, "Bütünden Parçaya", ["Bütünün kesir kadarı:", "Sayı kesir ile ÇARPILIR", "120 TL'nin 3/4'ü:", "120 . (3/4) = 90 TL"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Parçadan Bütüne", ["Kesir kadarı verilen bütün:", "Sayı kesre BÖLÜNÜR", "2/5'i 40 olan sayı:", "40 : (2/5) = 100"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Kalanın Kalanı", ["Önce 1'den çıkarıp kalanı bul", "Kalan kesirle yeni kesri çarp", "1/3'ü, sonra kalanın 1/2'si:", "(2/3) . (1/2) = 1/3"], "#f1f5f9", "#64748b", "#334155")
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
