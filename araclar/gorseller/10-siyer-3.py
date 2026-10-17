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
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İSLAM ÖNCESİ HİCAZ'DA YAŞAM BİÇİMİ VE TOPLUMSAL TABAKALAŞMA", "#7c2d12")

    # Sol: Yaşam Biçimi
    s += Kutu(24, 48, 306, 194, "#fffbeb", "#d97706", 2, 10)
    s += Yazi(177, 70, "1. YAŞAM BİÇİMİNE GÖRE ARAP TOPLUMU", 10, "#b45309", "middle", True)

    s += Kutu(40, 84, 274, 68, "#ffffff", "#d97706", 1.5, 8)
    s += Yazi(177, 102, "A) BEDEVÎLER (Çöl / Konargöçer Hayat)", 9.8, "#b45309", "middle", True)
    s += Yazi(177, 120, "• Çadırlarda yaşar, deve ve koyun beslerler.", 8.8, "#1e293b", "middle", False)
    s += Yazi(177, 136, "• Cesur, cömert ve saf Arapçaya hâkimdirler.", 8.8, "#1e293b", "middle", False)

    s += Kutu(40, 160, 274, 68, "#ffffff", "#0284c7", 1.5, 8)
    s += Yazi(177, 178, "B) HADARÎLER (Şehirli / Yerleşik Hayat)", 9.8, "#0369a1", "middle", True)
    s += Yazi(177, 196, "• Mekke, Yesrib (Medine) ve Taif'te yaşarlar.", 8.8, "#1e293b", "middle", False)
    s += Yazi(177, 212, "• Kervan ticareti ve ziraatla uğraşırlar.", 8.8, "#1e293b", "middle", False)

    # Sağ: Toplumsal Sınıflar
    s += Kutu(350, 48, 306, 194, "#eff6ff", "#2563eb", 2, 10)
    s += Yazi(503, 70, "2. TOPLUMSAL TABAKALAŞMA (SINIFLAR)", 10, "#1d4ed8", "middle", True)

    siniflar = [
        ("1. HÜRLER (Eşrâf / Kabile Üyeleri)", "Tüm siyasi, ekonomik ve hukuki haklara sahip üst sınıf", "#059669", "#d1fae5"),
        ("2. MEVÂLÎ (Azatlı Köleler)", "Özgürlüğüne kavuşmuş ancak eski efendisinin kabilesine bağlı sınıf", "#d97706", "#fef3c7"),
        ("3. KÖLELER VE CARİYELER (Er-Rikâb)", "Alınıp satılan, hiçbir temel insan hakkı tanınmayan ezilen sınıf", "#dc2626", "#fef2f2")
    ]
    for i, (ad, acik, r, ar) in enumerate(siniflar):
        y = 84 + i * 50
        s += Kutu(366, y, 274, 42, ar, r, 1.5, 6)
        s += Yazi(503, y + 16, ad, 9.2, r, "middle", True)
        s += Yazi(503, y + 32, acik, 8.2, "#1e293b", "middle", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "CAHİLİYE DÖNEMİ SOSYAL YAPISINA ELEŞTİREL BAKIŞ", "#991b1b")

    s += Kutu(24, 48, 306, 194, "#fef2f2", "#dc2626", 2, 10)
    s += Kutu(24, 48, 306, 32, "#dc2626", "#dc2626", 1, 10)
    s += Yazi(177, 69, "KARANLIK VE ZALİM UYGULAMALAR", 10, "#ffffff", "middle", True)
    kotu = [
        "• Kör Asabiyet: \"Zalim de olsa mazlum da olsa",
        "  kabiledaşına yardım et!\" anlayışı.",
        "• Kan Davaları (Eyyâmü'l-Arab / Ficâr Savaşları).",
        "• Ve'dü'l-Benât: Kız çocuklarını diri diri gömme",
        "  ve kadını mirastan/haklardan mahrum bırakma.",
        "• Kölelik, tefecilik (ribâ), içki ve kumar."
    ]
    for i, m in enumerate(kotu):
        s += Yazi(38, 100 + i * 22, m, 9, "#1e293b", "start", False)

    s += Kutu(350, 48, 306, 194, "#ecfdf5", "#059669", 2, 10)
    s += Kutu(350, 48, 306, 32, "#059669", "#059669", 1, 10)
    s += Yazi(503, 69, "OLUMLU ERDEMLER (MÜRÜVVET) VE İSLAM'IN TUTUMU", 9.5, "#ffffff", "middle", True)
    iyi = [
        "• Cömertlik (Sehâ) ve Misafirperverlik (İkrâmü'd-dayf).",
        "• Ahde Vefa (Sözünde durma) ve Emaneti koruma.",
        "• Cesaret (Şecaat) ve Mazlumu himaye etme (Civâr).",
        "• Hilfü'l-Fudûl (Erdemliler Topluluğu): Mekke'de",
        "  haksızlığa uğrayanları koruyan adalet antlaşması.",
        "→ İslam zulmü kaldırmış, güzel erdemleri tamamlamıştır."
    ]
    for i, m in enumerate(iyi):
        s += Yazi(364, 100 + i * 22, m, 9, "#1e293b", "start", i == 5)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KABİLE YAPISI VE KABİLEYE MENSUBİYET BİÇİMLERİ", "#1e3a8a")

    ogeler = [
        ("ŞEYH / SEYYİD (Kabile Reisi)", "Yaş, tecrübe, cömertlik ve asaletle seçilen lider; hakem (kâhin/hakem) kararlarıyla kabile yönetilirdi.", "#2563eb", "#dbeafe"),
        ("1. NESEB (Kan Bağıyla Üyelik)", "Kabilenin ortak atasından gelen asli ve tam hak sahibi hür üyeler (Salîbe).", "#059669", "#d1fae5"),
        ("2. HİLF (Antlaşmayla Üyelik)", "Başka kabileden olup koruma veya ittifak antlaşmasıyla kabileye katılanlar (Halîf).", "#d97706", "#fef3c7"),
        ("3. VELÂ (Azatlık Yoluyla Üyelik)", "Azat edilen kölelerin eski efendilerinin kabilesine bağlılığı (Mevâlî) ve Halî' (kabileden atılanlar).", "#7c3aed", "#f3e8ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(ogeler):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 92
        s += Kutu(x, y, 312, 78, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10, r, "start", True)
        s += Yazi(x + 14, y + 44, acik[:50], 9, "#1e293b", "start", False)
        s += Yazi(x + 14, y + 60, acik[50:], 9, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "HİCAZ'DA KÜLTÜREL VE EDEBÎ HAYAT: ŞİİR, HİTABET VE PANAYIRLAR", "#6d28d9")

    unsurlar = [
        ("ŞİİR VE HİTABET", "Sözlü kültürün zirvesi; şairler kabilenin sözcüsü ve medya gücüydü", "#7c3aed", "#f3e8ff"),
        ("MUALLAKÂT-I SEB'A", "Panayırlarda birinci seçilip Kâbe duvarına asılan 'Yedi Askı' şiirleri", "#d97706", "#fef3c7"),
        ("UKÂZ, MECENNE, ZÜ'L-MECÂZ", "Hac mevsiminde kurulan büyük ticari, edebî ve kültürel panayırlar", "#059669", "#d1fae5"),
        ("ENSÂB, EYYÂM VE KEHÂNET", "Soy bilimi (ensâb), kabile savaşları tarihi ve yıldız/iz takibi (kıyâfe)", "#0284c7", "#e0f2fe")
    ]

    for i, (bas, acik, r, ar) in enumerate(unsurlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 74
        s += Kutu(x, y, 312, 62, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10, r, "start", True)
        s += Yazi(x + 14, y + 44, acik, 9, "#1e293b", "start", False)

    s += Kutu(24, 198, 632, 36, "#eef2ff", "#4338ca", 1.5, 8)
    s += Yazi(340, 220, "Hikmet: Edebiyat ve belagatin zirvede olduğu bir topluma, en büyük mucize olarak eşsiz belagate sahip Kur'an-ı Kerim indirilmiştir!", 9.4, "#312e81", "middle", True)
    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-siyer-3", 1, gorsel_1())
    kaydet("10-siyer-3", 2, gorsel_2())
    kaydet("10-siyer-3", 3, gorsel_3())
    kaydet("10-siyer-3", 4, gorsel_4())


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
