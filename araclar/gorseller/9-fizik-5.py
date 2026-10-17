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
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Fiziksel Niceliklerin Sınıflandırılması ve SI Birim Sistemi</text>'
    c += _kart(18, 54, 314, 170, "Temel Nicelikler (7 Adet)", [
        "• Kendisinden başka bir niceliğin ölçülmesine",
        "  gerek duyulmadan tek başına ifade edilen",
        "  büyüklüklerdir.",
        "• Kodlama: K İ S A M U Z",
        "• Tamamı SKALER (yönsüz) büyüklüklerdir!"
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 170, "Türetilmiş Nicelikler", [
        "• İki ya da daha fazla temel nicelik kullanılarak",
        "  matematiksel bağıntılarla ifade edilen",
        "  büyüklüklerdir.",
        "• Örnek: Hız (m/s), Kuvvet (N), Enerji (J), Basınç (Pa)",
        "• Skaler veya vektörel olabilirler."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 265
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">SI Birim Sisteminde 7 Temel Nicelik (KISAMUZ Tablosu)</text>'
    c += _kart(18, 54, 314, 195, "K - İ - S - A Nicelikleri", [
        "1. Kütle (m): kilogram (kg) — Eşit kollu terazi",
        "2. Işık Şiddeti (I): kandela (cd) — Fotometre",
        "3. Sıcaklık (T): kelvin (K) — Termometre",
        "   (Dikkat: SI birimi Celsius °C değil Kelvin\'dir!)",
        "4. Akım Şiddeti (i): amper (A) — Ampermetre",
        "• Her birinin sembolü ve SI birimi evrenseldir."
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 195, "M - U - Z Nicelikleri", [
        "5. Madde Miktarı (n): mol (mol) — Ölçüm aleti yok",
        "   (Avogadro sayısı kadar tanecik içeren miktar)",
        "6. Uzunluk (l, x, h): metre (m) — Şerit metre / kumpas",
        "7. Zaman (t): saniye (s) — Kronometre / saat",
        "   (Dikkat: SI birimi saat veya dakika değil saniyedir!)",
        "• Kütlede SI birimi gram (g) değil kilogram (kg)\'dır!"
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Türetilmiş Nicelikler ve SI Birimlerinin Temel Birimler Cinsinden İfadesi</text>'
    c += _kart(18, 54, 314, 180, "Mekanik Türetilmiş Nicelikler", [
        "• Alan (A): m²  |  Hacim (V): m³",
        "• Sürat / Hız (v): metre/saniye (m/s)",
        "• İvme (a): metre/saniye² (m/s²)",
        "• Kuvvet (F): Newton (N) = kg · m / s²",
        "• Öz kütle (d): kg / m³"
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 180, "Enerji ve Elektrik Türetilmiş Nicelikleri", [
        "• İş / Enerji / Isı (W, E, Q): Joule (J) = N·m = kg·m²/s²",
        "• Güç (P): Watt (W) = J / s = kg · m² / s³",
        "• Basınç (P): Pascal (Pa) = N / m² = kg / (m · s²)",
        "• Elektrik Yükü (q): Coulomb (C) = A · s",
        "• Potansiyel Fark / Gerilim (V): Volt (V)"
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#2874a6"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Temel-Türetilmiş ile Skaler-Vektörel Çapraz Sınıflandırma</text>'
    c += _kart(18, 54, 314, 165, "Skaler Nicelikler (Yönsüz)", [
        "• Sayı ve birimle eksiksiz tanımlanır.",
        "• Temel ve Skaler: Kütle, Sıcaklık, Zaman,",
        "  Uzunluk, Akım şiddeti, Işık şiddeti, Madde miktarı.",
        "• Türetilmiş ve Skaler: Sürat, Enerji, İş, Güç,",
        "  Basınç, Hacim, Öz kütle, Elektrik yükü."
    ], "#2874a6", "#eaf2f8")
    c += _kart(348, 54, 314, 165, "Vektörel Nicelikler (Yönlü)", [
        "• Sayı ve birimin yanında DOĞRULTU ve YÖN gerekir.",
        "• Temel ve Vektörel: YOKTUR! (Hiçbir temel",
        "  nicelik vektörel değildir.)",
        "• Türetilmiş ve Vektörel: Yer değiştirme, Hız,",
        "  İvme, Kuvvet, Ağırlık, Momentum, Elektrik alan."
    ], "#117864", "#e8f8f5")
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
