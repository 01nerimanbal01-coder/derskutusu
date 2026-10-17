# -*- coding: utf-8 -*-
import html as _html

def svg_basla(w, h):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:{w}px;display:block;margin:12px auto;font-family:system-ui,-apple-system,sans-serif;">'

def svg_bitir():
    return '</svg>'

def Arka(w, h, renk="#f8fafc"):
    return f'<rect width="{w}" height="{h}" rx="14" fill="{renk}" stroke="#cbd5e1" stroke-width="1.5"/>'

def Baslik(w, metin, renk="#1e3a8a"):
    return (f'<rect x="16" y="10" width="{w-32}" height="28" rx="7" fill="{renk}"/>'
            f'<text x="{w//2}" y="29" text-anchor="middle" font-size="12" font-weight="800" fill="#ffffff">{_html.escape(str(metin))}</text>')

def Kutu(x, y, w, h, dolgu="#ffffff", kenar="#94a3b8", kw=1.5, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Yazi(x, y, metin, punto=10, renk="#1e293b", hiza="middle", kalin=False):
    fw = ' font-weight="700"' if kalin else ''
    return f'<text x="{x}" y="{y}" text-anchor="{hiza}" font-size="{punto}" fill="{renk}"{fw}>{_html.escape(str(metin))}</text>'

def Daire(cx, cy, r, dolgu="#3b82f6", kenar="#1d4ed8", kw=1.5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Cizgi(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'

def Cokgen(noktalar, dolgu="#bbf7d0", kenar="#15803d", kw=2):
    pts = " ".join(f"{x},{y}" for x, y in noktalar)
    return f'<polygon points="{pts}" fill="{dolgu}" stroke="{kenar}" stroke-width="{kw}"/>'

def Ok(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'

def kaydet(*args):
    pass



def gorsel_1():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "FELSEFİ SORUYA GİDEN DÜŞÜNSEL SÜREÇ", "#4338ca")

    adimlar = [
        ("1. MERAK VE HAYRET", "Alışılmış olana şaşırma", "Varlığı olduğu gibi kabul etmeme", "#2563eb", "#dbeafe"),
        ("2. ŞÜPHE VE SORGULAMA", "Dogmaları askıya alma", "Ön yargıları eleştirel süzgeçten geçirme", "#7c3aed", "#ede9fe"),
        ("3. FELSEFİ SORU", "Öze ve kavrama yönelme", "'... nedir?' sorusunu sorma", "#c026d3", "#fae8ff"),
        ("4. ARAYIŞ VE DÜŞÜNCE", "Tek cevpla yetinmeme", "Yeni bakış açıları ve argüman üretme", "#059669", "#d1fae5")
    ]

    kw = 148
    gap = 12
    sx = (W - (4 * kw + 3 * gap)) // 2
    for i, (bas, m1, m2, r, ar) in enumerate(adimlar):
        x = sx + i * (kw + gap)
        y = 52
        s += Kutu(x, y, kw, 138, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 20, bas, 9.5, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 66, m1, 9.5, "#1e293b", "middle", True)
        s += Yazi(x + kw // 2, y + 92, m2, 9, "#475569", "middle", False)
        if i < 3:
            s += Ok(x + kw, y + 69, x + kw + gap, y + 69, "#475569", 2)

    s += Kutu(40, 204, W - 80, 32, "#eef2ff", "#4f46e5", 1.5, 8)
    s += Yazi(W // 2, 224, "Karl Jaspers: \"Felsefede sorular cevaplardan daha önemlidir ve her cevap yeni bir soruya dönüşür.\"", 10, "#312e81", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 270
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "GÜNDELİK, BİLİMSEL VE FELSEFİ SORULARIN KARŞILAŞTIRILMASI", "#0f766e")

    kolonlar = [
        ("GÜNDELİK SORU", "#d97706", "#fef3c7", [
            "Amacı: Pratik ihtiyacı giderme",
            "Kapsamı: Somut, anlık ve kişisel",
            "Cevabı: Kısa, doğrudan ve işlevsel",
            "Örnek: 'Bugün hava kaç derece?'",
            "Örnek: 'Otobüs saat kaçta gelir?'"
        ]),
        ("BİLİMSEL SORU", "#0284c7", "#e0f2fe", [
            "Amacı: Olgusal dünyayı açıklama",
            "Kapsamı: Deney ve gözleme konu olan",
            "Cevabı: Kanıtlanabilir, kesin ve nesnel",
            "Örnek: 'Su hangi sıcaklıkta kaynar?'",
            "Örnek: 'Hücre nasıl bölünür?'"
        ]),
        ("FELSEFİ SORU", "#7c3aed", "#f3e8ff", [
            "Amacı: Varlığın ve değerin özünü anlama",
            "Kapsamı: Tümel, kavramsal ve evrensel",
            "Cevabı: Öznel, tartışmaya açık, çoğul",
            "Örnek: 'Zaman ve gerçeklik nedir?'",
            "Örnek: 'İyi ve adil bir yaşam nedir?'"
        ])
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, r, ar, maddeler) in enumerate(kolonlar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 204, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 10.5, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            kalin = j >= 3
            s += Yazi(x + 12, y + 58 + j * 30, "• " + m, 9.3, "#1e293b", "start", kalin)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "FELSEFİ SORULARIN 6 TEMEL ÖZELLİĞİ", "#6d28d9")

    ozellikler = [
        ("1. Öze ve Kavrama Yöneliktir", "Olguların nasıl işlediğini değil, kavramın özünü ('Nedir?') sorgular.", "#4f46e5", "#eef2ff"),
        ("2. Kendi Başına Anlamlıdır", "Cevabı verilmese bile sorunun kendisi yeni bir bilinç ve ufuk açar.", "#0891b2", "#ecfeff"),
        ("3. Refleksiftir (Düşünme Üzerinedir)", "Zihnin kendi ürettiği bilgi, inanç ve kavramlar üzerine yeniden düşünmesidir.", "#059669", "#ecfdf5"),
        ("4. Kesin ve Tek Cevabı Yoktur", "Filozofların bakış açılarına göre değişen, bitmeyen cevaplar üretir.", "#d97706", "#fffbeb"),
        ("5. Evrenseldir", "Belirli bir zümreyi değil, tüm insanlığın ortak varoluş sorunlarını kuşatır.", "#dc2626", "#fef2f2"),
        ("6. İlk Nedenleri ve 'Olması Gerekeni' Sorar", "Yalnızca mevcut durumu değil, ideal olanı ve ilk ilkeleri araştırır.", "#9333ea", "#faf5ff")
    ]

    kw, kh = 306, 58
    for i, (bas, acik, r, ar) in enumerate(ozellikler):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 10)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10.5, r, "start", True)
        s += Yazi(x + 14, y + 42, acik, 9.2, "#334155", "start", False)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "FELSEFENİN TEMEL ALANLARI VE ÖRNEK FELSEFİ SORULARI", "#1e3a8a")

    alanlar = [
        ("ONTOLOJİ (Varlık Felsefesi)", "Gerçekten var olan nedir? Evrende bir amaç ve düzen var mıdır?", "#1d4ed8", "#dbeafe"),
        ("EPİSTEMOLOJİ (Bilgi Felsefesi)", "Doğru bilgi mümkün müdür? Bilginin kaynağı ve sınırı nedir?", "#047857", "#d1fae5"),
        ("ETİK (Ahlak Felsefesi)", "İyi ve kötünün ölçütü nedir? İnsan eylemlerinde özgür müdür?", "#b45309", "#fef3c7"),
        ("ESTETİK (Sanat Felsefesi)", "Güzel nedir? Ortak estetik yargılar var mıdır?", "#be185d", "#fce7f3"),
        ("SİYASET FELSEFESİ", "İdeal devlet düzeni olabilir mi? İktidarın meşruiyet kaynağı nedir?", "#7c3aed", "#ede9fe"),
        ("BİLİM VE DİN FELSEFESİ", "Bilimsel yöntem yanılmaz mıdır? İnanç ile akıl uzlaşabilir mi?", "#b91c1c", "#fee2e2")
    ]

    kw, kh = 306, 58
    for i, (bas, acik, r, ar) in enumerate(alanlar):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 10)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10.5, r, "start", True)
        s += Yazi(x + 14, y + 42, acik, 9.2, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-felsefe-3", 1, gorsel_1())
    kaydet("10-felsefe-3", 2, gorsel_2())
    kaydet("10-felsefe-3", 3, gorsel_3())
    kaydet("10-felsefe-3", 4, gorsel_4())


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
