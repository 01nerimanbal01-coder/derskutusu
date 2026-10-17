def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sabit İvmeli Harekette Grafik Dönüşümleri: Eğim ve Alan Kuralları (FİZ.10.1.3)</text>'
    c += _kart(18, 54, 314, 175, "Eğim (Türev / Değişim Oranı) İlişkisi", [
        "• Konum-Zaman (x-t) grafiğinin EĞİMİ",
        "  -> Anlık Hızı (v) verir.",
        "• Hız-Zaman (v-t) grafiğinin EĞİMİ",
        "  -> İvmeyi (a = Δv / Δt) verir.",
        "• Merdiven Kuralı: x -> v -> a yönünde",
        "  giderken grafiğin EĞİMİ alınır!"
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 175, "Alan (Birikim) İlişkisi", [
        "• İvme-Zaman (a-t) grafiğinin zaman ekseniyle",
        "  arasındaki ALAN -> Hız Değişimini (Δv) verir.",
        "• Hız-Zaman (v-t) grafiğinin zaman ekseniyle",
        "  arasındaki ALAN -> Yer Değiştirmeyi (Δx) verir.",
        "• Merdiven Kuralı: a -> v -> x yönünde",
        "  giderken grafiğin ALANI alınır!"
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Hız-Zaman (v-t) Grafiğinden Matematiksel Modellere Ulaşma</text>'
    c += _kart(18, 54, 206, 180, "1. Hız Denklemi", [
        "• v-t grafiğinin eğimi sabit",
        "  ivmeyi (a) verir:",
        "  a = (v - v0) / t",
        "• Buradan son hız modeli:",
        "  v = v0 + a · t",
        "• Yavaşlamada: v = v0 - a · t"
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 180, "2. Konum / Yer Değiştirme", [
        "• v-t grafiğinin altındaki",
        "  yamuk alanı Δx\'i verir:",
        "  Δx = v0·t + (1/2)·a·t²",
        "• İlk hızsız (v0 = 0) ise:",
        "  Δx = (1/2) · a · t²",
        "• Ortalama hız: vort = (v0+v)/2"
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 180, "3. Zamansız Hız Denklemi", [
        "• t = (v - v0)/a ifadesi",
        "  Δx = ((v+v0)/2)·t içinde",
        "  yerine yazılırsa:",
        "  v² = v0² + 2 · a · Δx",
        "• Yavaşlayan harekette:",
        "  v² = v0² - 2 · a · Δx"
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Konum-Zaman (x-t) Grafiğinde Parabol Kollarının Yorumu (Genç K - Yaşlı K)</text>'
    c += _kart(18, 54, 314, 170, "Hızlanan Hareket (Eğim Mutlakça Artar)", [
        "• x-t grafiğinde parabolün eğimi zamanla",
        "  dikleşiyorsa cisim HIZLANMAKTADIR.",
        "• Pozitif yönde hızlanan: Yukarı doğru dikleşen eğri.",
        "• Negatif yönde hızlanan: Aşağı doğru dikleşen eğri.",
        "• Hız vektörü (v) ile ivme vektörü (a) AYNI YÖNLÜDÜR."
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 170, "Yavaşlayan Hareket (Eğim Mutlakça Azalır)", [
        "• x-t grafiğinde parabolün eğimi zamanla",
        "  yataylaşıyorsa cisim YAVAŞLAMAKTADIR.",
        "• Pozitif yönde yavaşlayan: Yukarı çıkarken yataylaşan.",
        "• Negatif yönde yavaşlayan: Aşağı inerken yataylaşan.",
        "• Hız vektörü (v) ile ivme vektörü (a) ZIT YÖNLÜDÜR."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Grafik Okurken Yön Değiştirme Anlarının Tespiti ve Tek Zaman Dilimi</text>'
    c += _kart(18, 54, 314, 165, "Cisim Ne Zaman Yön Değiştirir?", [
        "• Konum-Zaman (x-t) grafiğinde: Grafiğin TEPE",
        "  veya ÇUKUR (dönüm) noktalarında yön değiştirir!",
        "• Hız-Zaman (v-t) grafiğinde: Grafiğin ZAMAN",
        "  EKSENİNİ KESTİĞİ (+ bölgesinden - bölgesine",
        "  veya -\'den +\'ya geçtiği) anda yön değiştirir!"
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 165, "Ardışık Eşit Zamanlarda Yol Oranı (x - 3x - 5x)", [
        "• İlk hızsız (v0 = 0) sabit ivmeyle hızlanan cisim",
        "  her t süresinde sırasıyla:",
        "  x, 3x, 5x, 7x, 9x ... kadar yer değiştirir.",
        "• Toplam konumları ise t² ile orantılı olarak",
        "  x, 4x, 9x, 16x, 25x ... şeklinde artar."
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
