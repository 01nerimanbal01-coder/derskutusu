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
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sayı Kümeleri Hiyerarşisi: N ⊂ Z ⊂ Q ⊂ R ve Q ∪ Q\' = R</text>'
    c += _kart(18, 54, 152, 180, "Doğal Sayılar (N)", [
        "• N = {0, 1, 2, 3, ...}",
        "• Sayma: N+ = {1, 2, ...}",
        "• Ardışık elemanlar",
        "  arasında tam sayı",
        "  bulunmaz (ayrık).",
        "• En küçük eleman: 0"
    ], "#1e8449", "#e9f7ef")
    c += _kart(182, 54, 152, 180, "Tam Sayılar (Z)", [
        "• Z = {..., -2, -1, 0, 1, ...}",
        "• Z = Z- ∪ {0} ∪ Z+",
        "• N kümesini kapsar.",
        "• Çıkarma işlemine",
        "  göre kapalıdır.",
        "• Yoğun değildir."
    ], "#2874a6", "#eaf2f8")
    c += _kart(346, 54, 152, 180, "Rasyonel Sayılar (Q)", [
        "• a,b ∈ Z ve b ≠ 0",
        "  için a/b biçiminde",
        "  yazılabilen sayılar.",
        "• İki rasyonel sayı",
        "  arasında sonsuz Q",
        "  vardır (yoğundur)."
    ], "#b9770e", "#fef9e7")
    c += _kart(510, 54, 152, 180, "Gerçek Sayılar (R)", [
        "• R = Q ∪ Q\' (İrrasyonel)",
        "• Sayı doğrusunu",
        "  boşluksuz doldurur.",
        "• π, e ve kök dışına",
        "  çıkamayan sayılar",
        "  Q\' kümesindedir."
    ], "#7d3c98", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sayı Kümelerinin Kapalılık Özelliği Karşılaştırma Tablosu</text>'
    c += _kart(18, 54, 206, 172, "Toplama (+) ve Çarpma (·)", [
        "• N kümesi: KAPALIDIR (+ ve ·)",
        "• Z kümesi: KAPALIDIR (+ ve ·)",
        "• Q kümesi: KAPALIDIR (+ ve ·)",
        "• R kümesi: KAPALIDIR (+ ve ·)",
        "• Q\' (İrrasyonel): KAPALI DEĞİLDİR!",
        "  Örn: (2 - kök3) + (2 + kök3) = 4 ∈ Q"
    ], "#117864", "#e8f8f5")
    c += _kart(237, 54, 206, 172, "Çıkarma (-) İşlemi", [
        "• N kümesi: KAPALI DEĞİLDİR",
        "  Karşı örnek: 3 - 7 = -4 ∉ N",
        "• Z kümesi: KAPALIDIR",
        "• Q kümesi: KAPALIDIR",
        "• R kümesi: KAPALIDIR",
        "• Q\' kümesi: KAPALI DEĞİLDİR"
    ], "#b9770e", "#fef9e7")
    c += _kart(456, 54, 206, 172, "Bölme (÷, Bölen ≠ 0)", [
        "• N kümesi: KAPALI DEĞİLDİR",
        "• Z kümesi: KAPALI DEĞİLDİR",
        "  Karşı örnek: 5 ÷ 2 = 2,5 ∉ Z",
        "• Q - {0}: KAPALIDIR",
        "• R - {0}: KAPALIDIR",
        "• 0\'a bölme tanımsızdır!"
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Gerçek Sayılarda (R) Toplama ve Çarpma İşlemlerinin Cebirsel Özellikleri</text>'
    c += _kart(18, 54, 314, 180, "Toplama İşleminin Özellikleri (+)", [
        "1. Kapalılık: ∀a, b ∈ R için a + b ∈ R",
        "2. Değişme: a + b = b + a",
        "3. Birleşme: (a + b) + c = a + (b + c)",
        "4. Etkisiz (Birim) Eleman: 0  (a + 0 = a)",
        "5. Ters Eleman: a\'nın toplama tersi -a\'dır;",
        "   a + (-a) = 0 (Her gerçek sayının tersi vardır)"
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 180, "Çarpma İşleminin Özellikleri (·)", [
        "1. Kapalılık: ∀a, b ∈ R için a · b ∈ R",
        "2. Değişme ve Birleşme: a·b = b·a, (a·b)·c = a·(b·c)",
        "3. Etkisiz (Birim) Eleman: 1  (a · 1 = a)",
        "4. Yutan Eleman: 0  (a · 0 = 0)",
        "5. Ters Eleman: a ≠ 0 için 1/a  (a · 1/a = 1)",
        "6. Dağılma: a · (b ± c) = a·b ± a·c"
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sıralama, Arada Olma (Yoğunluk) ve Matematiksel Muhakeme Süreci</text>'
    c += _kart(18, 54, 314, 165, "Arada Olma (Yoğunluk) Özelliği", [
        "• N ve Z kümelerinde ardışık iki tam sayı arasında",
        "  başka bir tam sayı yoktur (yoğun değildir).",
        "• Q ve R kümelerinde her a < b için a < (a+b)/2 < b",
        "  olduğundan iki sayı arasında SONSUZ sayı vardır.",
        "• Bu özelliğe kümenin YOĞUNLUĞU denir."
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 165, "Varsayım, Genelleme ve Karşı Örnek", [
        "• Varsayım: Sayı kümelerindeki örüntülerden yola",
        "  çıkarak kurulan matematiksel iddiadır.",
        "• Doğrulama: Cebirsel ispatla genelleme yapılır.",
        "• Çürütme (Karşı Örnek): İddianın yanlışlığını",
        "  göstermek için TEK BİR karşı örnek yeterlidir!"
    ], "#1e8449", "#e9f7ef")
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
