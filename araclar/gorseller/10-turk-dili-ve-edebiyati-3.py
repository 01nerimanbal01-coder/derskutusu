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
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "SÖZÜN EZGİSİ TEMASI: SÖZLÜ GELENEKTEN HALK ŞİİRİNE SÜREKLİLİK", "#991b1b")

    sol = [
        ("KOŞUK (İslamiyet Öncesi)", "Sığır ve şölen törenlerinde kopuzla; doğa, aşk, yiğitlik", "#1d4ed8", "#dbeafe"),
        ("SAGU (İslamiyet Öncesi)", "Yuğ (cenaze) törenlerinde ölen kişinin ardından yakılan şiir", "#4338ca", "#e0e7ff"),
        ("SAV VE DESTAN", "Atasözü niteliğindeki özlü sözler ve milletin kahramanlık anlatıları", "#0f766e", "#ccfbf1")
    ]
    sag = [
        ("KOŞMA (Âşık Edebiyatı)", "11'li heceyle saz eşliğinde; güzelleme, koçaklama, taşlama", "#b91c1c", "#fee2e2"),
        ("AĞIT (Halk Şiiri)", "Sagunun halk şiirindeki karşılığı; acı ve kayıpların ezgili ifadesi", "#9333ea", "#f3e8ff"),
        ("TÜRKÜ, MÂNİ VE NİNNİ", "Anonim halk şiirinin ezgiyle bütünleşen temel nazım biçimleri", "#c2410c", "#ffedd5")
    ]

    for i in range(3):
        b1, a1, r1, ar1 = sol[i]
        b2, a2, r2, ar2 = sag[i]
        y = 48 + i * 56
        s += Kutu(22, y, 296, 48, ar1, r1, 1.5, 8)
        s += Yazi(34, y + 19, b1, 10, r1, "start", True)
        s += Yazi(34, y + 36, a1, 8.8, "#1e293b", "start", False)

        s += Ok(322, y + 24, 358, y + 24, "#64748b", 2)

        s += Kutu(362, y, 296, 48, ar2, r2, 1.5, 8)
        s += Yazi(374, y + 19, b2, 10, r2, "start", True)
        s += Yazi(374, y + 36, a2, 8.8, "#1e293b", "start", False)

    s += Kutu(36, 220, W - 72, 28, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(W // 2, 238, "Ortak Payda: Dörtlük nazım birimi • Hece ölçüsü (7, 8, 11'li) • Sade Türkçe • Ezgi (Kopuz / Bağlama)", 9.8, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TÜRKÜ NAZIM BİÇİMİNİN YAPISI: BENT VE KAVUŞTAK", "#0f766e")

    # Sol: Yapı şeması
    s += Kutu(26, 48, 300, 194, "#ecfdf5", "#059669", 1.5, 10)
    s += Yazi(176, 68, "Türkünün Yapısal Bölümleri", 11, "#065f46", "middle", True)

    s += Kutu(46, 82, 260, 64, "#ffffff", "#059669", 1.5, 8)
    s += Yazi(176, 102, "1. BENT (Asıl Söz Bölümü)", 10.5, "#047857", "middle", True)
    s += Yazi(176, 120, "• Türkünün asıl konusunun işlendiği", 9.2, "#1e293b", "middle", False)
    s += Yazi(176, 136, "  3 veya 4 dizelik bölümlerdir (aaab / cccb).", 9.2, "#1e293b", "middle", False)

    s += Ok(176, 146, 176, 162, "#059669", 2)

    s += Kutu(46, 162, 260, 64, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(176, 182, "2. KAVUŞTAK (Bağlama / Nakarat)", 10.5, "#b45309", "middle", True)
    s += Yazi(176, 200, "• Her bendin sonunda aynen tekrarlanan", 9.2, "#1e293b", "middle", False)
    s += Yazi(176, 216, "  1, 2 veya 4 dizelik ezgili bölümdür.", 9.2, "#1e293b", "middle", False)

    # Sağ: Ezgilerine göre türküler
    s += Kutu(346, 48, 308, 194, "#eff6ff", "#2563eb", 1.5, 10)
    s += Yazi(500, 68, "Ezgilerine Göre Türküler", 11, "#1e40af", "middle", True)

    s += Kutu(364, 82, 272, 68, "#ffffff", "#2563eb", 1.5, 8)
    s += Yazi(500, 102, "A) USULLÜ TÜRKÜLER (Kırık Havalar)", 10, "#1d4ed8", "middle", True)
    s += Yazi(500, 120, "• Ölçüsü, ritmi ve temposu belirgindir.", 9.2, "#1e293b", "middle", False)
    s += Yazi(500, 136, "• Oyun havaları: Zeybek, halay, horon, bar, karşılama.", 9.2, "#1e293b", "middle", False)

    s += Kutu(364, 160, 272, 68, "#faf5ff", "#7c3aed", 1.5, 8)
    s += Yazi(500, 180, "B) USULSÜZ TÜRKÜLER (Uzun Havalar)", 10, "#6d28d9", "middle", True)
    s += Yazi(500, 198, "• Serbest ritimli, içli ve hüzünlü ezgilerdir.", 9.2, "#1e293b", "middle", False)
    s += Yazi(500, 214, "• Türleri: Bozlak, maya, hoyrat, divan, barak, ağıt.", 9.2, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ŞİİR DİNLETİSİ (KONUŞMA) VE SESLENDİRME İLKELERİ", "#4f46e5")

    ilkeler = [
        ("1. Vurgu ve Tonlama", "Şiirin duygu değerine (coşku, hüzün, özlem) uygun ses tonu ve kelime vurgusu", "#2563eb", "#dbeafe"),
        ("2. Durak ve Ölçü Uyumu", "Hece ölçüsünün durak yerlerine (4+4+3 veya 6+5) ve iç ritme dikkat etme", "#059669", "#d1fae5"),
        ("3. Diksiyon ve Boğumlama", "Sesleri, heceleri ve kelimeleri yutmadan açık, anlaşılır biçimde telaffuz etme", "#d97706", "#fef3c7"),
        ("4. Beden Dili ve Göz Teması", "Abartıdan uzak jest-mimikler ve dinleyicilerle kurulan doğal göz teması", "#9333ea", "#f3e8ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(ilkeler):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 72
        s += Kutu(x, y, 312, 60, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10.5, r, "start", True)
        s += Yazi(x + 14, y + 42, acik, 9, "#1e293b", "start", False)

    s += Kutu(24, 196, 632, 38, "#eef2ff", "#4338ca", 1.5, 8)
    s += Yazi(340, 219, "Şiir Dinletisi Aşamaları: Metin Seçimi → Tema ve Ahenk Çözümlemesi → Fon Müziği/Prova → Sahne Sunumu", 9.8, "#312e81", "middle", True)
    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TÜRKÜ VE KOŞMA NAZIM BİÇİMLERİNİN KARŞILAŞTIRMASI", "#b45309")

    s += Kutu(26, 48, 304, 186, "#fff7ed", "#ea580c", 1.5, 10)
    s += Yazi(178, 70, "TÜRKÜ (Anonim / Âşık Halk Şiiri)", 11, "#c2410c", "middle", True)
    t_mad = [
        "• Genellikle anonimdir (söyleyeni zamanla unutulur).",
        "• Bent ve kavuştak (bağlama/nakarat) bölümlerinden oluşur.",
        "• 7'li, 8'li ve 11'li hece ölçüsüyle söylenir.",
        "• Ezgisi en belirleyici unsurdur (kırık hava / uzun hava).",
        "• Son dörtlükte mahlas yer almayabilir."
    ]
    for i, m in enumerate(t_mad):
        s += Yazi(40, 96 + i * 26, m, 9.4, "#1e293b", "start", False)

    s += Kutu(350, 48, 304, 186, "#f0fdf4", "#16a34a", 1.5, 10)
    s += Yazi(502, 70, "KOŞMA (Âşık Tarzı Halk Şiiri)", 11, "#15803d", "middle", True)
    k_mad = [
        "• Söyleyeni (âşığı/ozanı) bellidir, bireysel yaratımdır.",
        "• Kavuştak zorunluluğu yoktur; dörtlüklerden oluşur.",
        "• Çoğunlukla 11'li (6+5 veya 4+4+3) hece ölçüsü kullanılır.",
        "• Uyak düzeni abab / cccb / dddb şeklindedir.",
        "• Son dörtlükte âşık mutlaka mahlasını (tapşırma) söyler."
    ]
    for i, m in enumerate(k_mad):
        s += Yazi(364, 96 + i * 26, m, 9.4, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-turk-dili-ve-edebiyati-3", 1, gorsel_1())
    kaydet("10-turk-dili-ve-edebiyati-3", 2, gorsel_2())
    kaydet("10-turk-dili-ve-edebiyati-3", 3, gorsel_3())
    kaydet("10-turk-dili-ve-edebiyati-3", 4, gorsel_4())


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
