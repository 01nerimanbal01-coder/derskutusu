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
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HARİTA OLMA ŞARTLARI VE HARİTANIN TEMEL ELEMANLARI</text>'
    ic += _kart(30, 56, 195, 160, "3 Temel Şart (Kroki Farkı)", ["1. Kuşbakışı görünüm", "2. Düzleme aktarma", "3. ÖLÇEK (Krokide ölçek yok!)", "Bilim dalı: Kartografya"], "#eff6ff", "#3b82f6", "#1d4ed8")
    ic += _kart(242, 56, 195, 160, "Başlık, Ölçek &amp; Yön Oku", ["Başlık: Haritanın kullanım amacı", "Ölçek: Küçültme oranı", "Yön Oku: Kuzeyi gösterir", "Coğrafi Koordinatlar (Paralel/M.)"], "#f0fdf4", "#22c55e", "#15803d")
    ic += _kart(454, 56, 195, 160, "Lejant (Harita Anahtarı)", ["Haritadaki özel işaretlerin,", "sembollerin ve renklerin", "ne anlama geldiğini açıklayan", "harita dili tablosudur"], "#fef3c7", "#f59e0b", "#b45309")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HARİTA PROJEKSİYON (İZ DÜŞÜM) YÖNTEMLERİ</text>'
    ic += _kart(30, 56, 195, 160, "1. Silindirik Projeksiyon", ["Ekvator ve çevresinde (0°-30°)", "bozulma EN AZDIR", "Kutuplara gidildikçe bozulma artar", "Örn: Brezilya, Endonezya, Kenya"], "#fae8ff", "#d946ef", "#a21caf")
    ic += _kart(242, 56, 195, 160, "2. Konik Projeksiyon", ["Orta kuşak ülkelerinde (30°-60°)", "bozulma EN AZDIR", "Alan koruyan çizimler", "Örn: Türkiye, Fransa, Japonya"], "#e0f2fe", "#0284c7", "#0369a1")
    ic += _kart(454, 56, 195, 160, "3. Düzlem (Ufki) Proj.", ["Kutup noktaları ve çevresinde", "(60°-90°) bozulma EN AZDIR", "Dar alanların çiziminde kullanılır", "Örn: Antarktika, Grönland, İzlanda"], "#ffe4e6", "#f43f5e", "#be123c")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">BÜYÜK ÖLÇEKLİ VE KÜÇÜK ÖLÇEKLİ HARİTALAR</text>'
    ic += _kart(30, 56, 300, 160, "Büyük Ölçekli Haritalar (Örn: 1/20.000)", ["• Paydadaki sayı KÜÇÜKTÜR (Az küçültülmüştür)", "• Dar alanları gösterir (Şehir planı, topoğrafya)", "• Ayrıntıyı gösterme gücü YÜKSEKTİR", "• Hata ve bozulma oranı AZDIR"], "#ede9fe", "#8b5cf6", "#6d28d9")
    ic += _kart(350, 56, 300, 160, "Küçük Ölçekli Haritalar (Örn: 1/5.000.000)", ["• Paydadaki sayı BÜYÜKTÜR (Çok küçültülmüştür)", "• Geniş alanları gösterir (Dünya, Kıta, Duvar haritası)", "• Ayrıntıyı gösterme gücü DÜŞÜKTÜR", "• Hata ve bozulma oranı FAZLADIR"], "#dcfce7", "#10b981", "#047857")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 240
    ic = f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>'
    ic += f'<text x="{w/2}" y="38" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a" text-anchor="middle">HARİTA TÜRLERİ VE ÖLÇEK HESAPLAMALARI</text>'
    ic += _kart(30, 56, 195, 160, "Genel Haritalar", ["Fiziki Haritalar (Yükselti/Renk)", "Siyasi (İdari) Haritalar (Sınır)", "Topoğrafya ve Atlas Haritaları", "(Yükselti SADECE Fizikide!)"], "#ffedd5", "#f97316", "#c2410c")
    ic += _kart(242, 56, 195, 160, "Tematik (Özel) Haritalar", ["Belirli bir konuya odaklanır:", "İklim, Toprak, Nüfus yoğunluğu,", "Maden, Deprem, Turizm haritası", "Uzmanlık gerektiren haritalar"], "#e0e7ff", "#6366f1", "#4338ca")
    ic += _kart(454, 56, 195, 160, "Ölçek ve Uzunluk Formülü", ["Gerçek Uzunluk = Harita U. x Ölçek P.", "cm’den km’ye: 5 sıfır silinir!", "1/500.000 -> 1 cm = 5 km", "Kesir ölçek ve Çizgi ölçek"], "#f1f5f9", "#64748b", "#334155")
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
