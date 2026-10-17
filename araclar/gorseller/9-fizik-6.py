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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">SKALER VE VEKTÖREL NİCELİKLERİN KARŞILAŞTIRILMASI</text>'
    ic += _kart(30, 56, 300, 160, "Skaler Nicelikler (Yönsüz)", ["• Sadece sayı ve birim ile tam ifade edilir", "• Doğrultu ve yön bilgisi içermez", "• Kütle (kg), Zaman (s), Sıcaklık (K), Uzunluk (m)", "• Alınan yol, Sürat, Enerji, İş, Güç, Basınç"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(350, 56, 300, 160, "Vektörel Nicelikler (Yönlü)", ["• Sayı, birim + DOĞRULTU ve YÖN gerekir", "• Sembolün üzerine ok işareti konur", "• Kuvvet (F), Ağırlık (G), Yer değiştirme (Δx)", "• Konum (x), Hız (v), İvme (a), Momentum (p)"], "#f0fdf4", "#22c55e", "#15803d")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">BİR VEKTÖRÜN DÖRT TEMEL ELEMANI</text>'
    ic += _kart(30, 56, 195, 160, "1. Başlangıç Noktası", ["Vektörün uygulama noktası", "Okun başladığı nokta (K)", "2. Doğrultu (Taşıyıcı Doğru)", "Doğu-Batı veya x-ekseni"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "3. Yön", ["Ok ucunun gösterdiği taraf", "Aynı doğrultuda iki zıt yön", "(Örn: +x yönü veya Doğu)", "Ok ucu yönü temsil eder"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "4. Büyüklük (Şiddet)", ["Vektörün sayısal değeri", "Okun boyu ile doğru orantılı", "|A| veya A ile gösterilir", "Büyüklük daima ≥ 0 (pozitif)"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">EŞİT VEKTÖRLER, ZIT VEKTÖRLER VE SKALERLE ÇARPIM</text>'
    ic += _kart(30, 56, 195, 160, "Eşit Vektörler (K = L)", ["Yönleri AYNI olmalı", "Doğrultuları AYNI olmalı", "Büyüklükleri EŞİT olmalı", "|K| = |L| her zaman K = L demek değildir!"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(242, 56, 195, 160, "Zıt Vektörler (K = -M)", ["Doğrultuları AYNI", "Büyüklükleri EŞİT (|K| = |M|)", "Yönleri birbirine ZIT (180°)", "-K vektörü K’nin tersidir"], "#ffe4e6", "#f43f5e", "#be123c")
    ic += _kart(454, 56, 195, 160, "Skalerle Çarpma (c . A)", ["c &gt; 0 ise yön değişmez", "c &lt; 0 ise yön 180° ters döner", "Büyüklük |c| katına çıkar", "Örn: -2A (zıt yönlü, 2 kat boy)"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">TEK BOYUTTA VE İKİ BOYUTTA VEKTÖRLERİN TOPLANMASI</text>'
    ic += _kart(30, 56, 195, 160, "Aynı Yönlü Vektörler", ["Büyüklükler toplanır:", "R = F1 + F2", "Bileşke (R) aynı yöndedir", "Maksimum bileşke elde edilir"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Zıt Yönlü Vektörler", ["Büyüklükler çıkarılır:", "R = |F1 - F2|", "Bileşke BÜYÜK olanın yönünde", "Eşit ve zıtsa R = 0 (Denge!)"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Uç Uca &amp; Dik Vektörler", ["Birinin bitimine diğeri eklenir", "İlk başlangıçtan son bitime R", "Aralarında 90° varsa Pisagor:", "R² = F1² + F2² (Örn: 3-4-5)"], "#f1f5f9", "#64748b", "#334155")
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
