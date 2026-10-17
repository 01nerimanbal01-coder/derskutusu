# -*- coding: utf-8 -*-
"""7. Sınıf Matematik — 5. Hafta Görselleri (Rasyonel Sayılarda Karşılaştırma ve Sıralama)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Sayı Doğrusu Üzerinde Rasyonel Sayıların Karşılaştırılması</text>',
        _kart(25, 50, 225, 215, "1. Negatif Bölge (&lt; 0)", [
            "• 0'ın solunda yer alan sayılardır.",
            "• 0'dan sola doğru uzaklaştıkça",
            "  rasyonel sayının değeri KÜÇÜLÜR!",
            "• Örnek: -3/4 &gt; -7/4",
            "• Örnek: -0,2 &gt; -1,5",
            "• Negatif her sayı 0 ve pozitiften küçüktür."
        ], "#e11d48", "#fff1f2"),
        _kart(267, 50, 225, 215, "2. Referans Noktası (0 ve ±1/2)", [
            "• 0 ne negatiftir ne de pozitiftir.",
            "• Negatif sayılardan büyük,",
            "  pozitif sayılardan küçüktür.",
            "• Yarım (1/2 ve -1/2) ile bütüne",
            "  (1 ve -1) yakınlık stratejik",
            "  karşılaştırma referansıdır."
        ], "#2563eb", "#eff6ff"),
        _kart(510, 50, 225, 215, "3. Pozitif Bölge (&gt; 0)", [
            "• 0'ın sağında yer alan sayılardır.",
            "• 0'dan sağa doğru uzaklaştıkça",
            "  rasyonel sayının değeri BÜYÜR!",
            "• Örnek: 7/4 &gt; 3/4",
            "• Örnek: 1,5 &gt; 0,2",
            "• Sayı doğrusunda sağdaki daima büyüktür."
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Pozitif Rasyonel Sayıları Sıralama Yöntemleri</text>',
        _kart(30, 50, 335, 215, "Yöntem 1: Payda Eşitleme", [
            "• Paydaları eşit olan pozitif rasyonel",
            "  sayılardan payı büyük olan daha büyüktür.",
            "• Örnek: 2/3, 5/6 ve 7/12 sayılarını sıralayalım:",
            "• Paydaları 12'de eşitleriz:",
            "  2/3 = 8/12,  5/6 = 10/12,  7/12",
            "• Sıralama: 7/12 &lt; 2/3 &lt; 5/6"
        ], "#0284c7", "#f0f9ff"),
        _kart(395, 50, 335, 215, "Yöntem 2: Pay Eşitleme ve Ondalık Gösterim", [
            "• Payları eşit olan pozitif rasyonel sayılardan",
            "  paydası KÜÇÜK olan daha büyüktür!",
            "• Örnek: 4/5 &gt; 4/7 &gt; 4/11",
            "• Ondalık gösterime çevirme yöntemi:",
            "  3/4 = 0,75 ve 4/5 = 0,80 -> 4/5 &gt; 3/4",
            "• Devirli ondalıklarda basamaklar alt alta yazılır."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Negatif Rasyonel Sayıları Sıralamada Altın Kural</text>',
        _kart(30, 50, 335, 215, "1. Adım: Pozitifmiş Gibi Sırala", [
            "• Negatif işaretleri geçici olarak kapatılır.",
            "• Örnek: -2/5, -3/10, -7/10 sayılarını",
            "  pozitif kabul edelim: 2/5 = 4/10, 3/10, 7/10",
            "• Pozitif sıralama:",
            "  3/10 &lt; 4/10 &lt; 7/10",
            "  (yani 3/10 &lt; 2/5 &lt; 7/10)"
        ], "#d97706", "#fffbeb"),
        _kart(395, 50, 335, 215, "2. Adım: Eşitsizlik Yönünü Ters Çevir!", [
            "• Negatif sayılarda 0'a yakın olan daha",
            "  büyük olduğu için sıralama yönü ters döner!",
            "• Negatif sıralama:",
            "  -3/10 &gt; -2/5 &gt; -7/10",
            "• Veya küçükten büyüğe:",
            "  -7/10 &lt; -2/5 &lt; -3/10"
        ], "#0d9488", "#f0fdfa"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">İki Rasyonel Sayı Arasına Rasyonel Sayı Yerleştirme (Yoğunluk)</text>',
        _kart(30, 50, 335, 195, "Genişletme İle Aradaki Sayıları Bulma", [
            "• Örnek: 1/3 ile 2/3 arasında paydası 3 olan",
            "  rasyonel sayı görünmez.",
            "• Kesirleri 3 ile genişletirsek: 3/9 ve 6/9 olur.",
            "• Aralarındaki sayılar: 4/9 ve 5/9!",
            "• İki rasyonel sayı arasında sonsuz rasyonel sayı vardır."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Bütüne ve Yarıma Yakınlık Stratejisi", [
            "• Pay ile payda arasındaki fark sabitse:",
            "  Pozitif basit kesirlerde sayılar büyüdükçe",
            "  kesir 1 tama yaklaşır ve BÜYÜR: 9/10 &gt; 3/4 &gt; 1/2",
            "• Negatif basit kesirlerde ise tam tersine",
            "  -1/2 &gt; -3/4 &gt; -9/10 olur!"
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
