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
    s += Baslik(W, "İSLAM'DA HAYATIN ANLAMI: İNANÇ, İBADET VE AHLAK BÜTÜNLÜĞÜ", "#0f766e")

    kartlar = [
        ("1. İNANÇ (İMÂN / AKÂİD)", "#2563eb", "#dbeafe", [
            "Ağacın KÖKÜ gibidir",
            "Tevhid ve İman Esasları",
            "Kalp ile tasdik, dil ile ikrar",
            "Hayata anlam ve yön verir"
        ]),
        ("2. İBADET (AMEL / KULLUK)", "#059669", "#d1fae5", [
            "Ağacın GÖVDESİ ve DALLARI",
            "Namaz, oruç, zekât, hac, dua",
            "İmanı korur ve canlı tutar",
            "Kul ile Allah bağını güçlendirir"
        ]),
        ("3. AHLAK (FAZİLET / İHSAN)", "#7c3aed", "#f3e8ff", [
            "Ağacın TATLI MEYVESİDİR",
            "Adalet, dürüstlük, merhamet, iffet",
            "İman ve ibadetin hedefidir",
            "Toplumsal huzuru inşa eder"
        ])
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, r, ar, maddeler) in enumerate(kartlar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 154, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 9.8, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            s += Yazi(x + kw // 2, y + 56 + j * 24, m, 9.3, "#1e293b", "middle", j == 0)

    s += Ok(sx + kw, 125, sx + kw + gap, 125, "#475569", 2)
    s += Ok(sx + 2 * kw + gap, 125, sx + 2 * (kw + gap), 125, "#475569", 2)

    s += Kutu(34, 212, W - 68, 30, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(W // 2, 231, "Kur'an-ı Kerim'de \"İman edip salih amel işleyenler\" (آمَنُوا وَعَمِلُوا الصَّالِحَاتِ) ifadesi bu ayrılmaz bütünlüğü vurgular.", 9.6, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İSLAM DİNİNİN İKİ TEMEL KAYNAĞI: KUR'AN-I KERİM VE SÜNNET", "#1e3a8a")

    s += Kutu(26, 48, 304, 194, "#ecfdf5", "#059669", 2, 10)
    s += Kutu(26, 48, 304, 32, "#059669", "#059669", 1, 10)
    s += Yazi(178, 69, "1. KUR'AN-I KERİM (Kitap / Vahiy)", 10.5, "#ffffff", "middle", True)
    k_mad = [
        "• İslam'ın birinci ve temel kaynağıdır.",
        "• Lafzı ve manası Yüce Allah'a ait son ilahi kitaptır.",
        "• Tevatür yoluyla hiçbir değişikliğe uğramadan gelmiştir.",
        "• Başvuru Araçları: Meal (yaklaşık çeviri), Tefsir",
        "  (geniş açıklama) ve Fihrist / Konulu Kur'an İndeksi."
    ]
    for i, m in enumerate(k_mad):
        s += Yazi(40, 102 + i * 24, m, 9.2, "#1e293b", "start", i == 0)

    s += Kutu(350, 48, 304, 194, "#eff6ff", "#2563eb", 2, 10)
    s += Kutu(350, 48, 304, 32, "#2563eb", "#2563eb", 1, 10)
    s += Yazi(502, 69, "2. SÜNNET VE SAHİH HADİSLER", 10.5, "#ffffff", "middle", True)
    s_mad = [
        "• İslam'ın ikinci temel kaynağıdır.",
        "• Hz. Peygamber'in (sav) söz (kavlî), davranış (fiilî)",
        "  ve onaylarını (takrîrî) kapsar.",
        "• Kur'an'ın anlaşılmasını ve yaşanmasını sağlar (Tebyîn).",
        "• Başlıca Kaynaklar: Kütüb-i Sitte (Buhârî, Müslim vb.)"
    ]
    for i, m in enumerate(s_mad):
        s += Yazi(364, 102 + i * 24, m, 9.2, "#1e293b", "start", i == 0)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TEMEL DİNİ KAYNAKLARDAN DOĞRU BİLGİYE ULAŞMA ADIMLARI", "#6d28d9")

    adimlar = [
        ("1. Konu ve Kavram Tespiti", "Araştırılacak konuyla ilgili anahtar kavramları (emanet, adalet, sorumluluk) belirleme", "#2563eb", "#dbeafe"),
        ("2. Meal ve Tefsire Başvurma", "Güvenilir Kur'an meallerinden ayetleri bulma ve bağlamını (sebeb-i nüzul) tefsirden okuma", "#059669", "#d1fae5"),
        ("3. Sahih Hadis Kaynaklarını Tarama", "Riyâzü's-Sâlihîn ve Kütüb-i Sitte gibi muteber eserlerden Hz. Peygamber'in uygulamasını inceleme", "#d97706", "#fef3c7"),
        ("4. Bütüncül Değerlendirme ve İlke", "Ayet ve hadisleri tek tek cımbızlamadan, bütünlük içinde anlayıp hayat ilkesine dönüştürme", "#9333ea", "#f3e8ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(adimlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 92
        s += Kutu(x, y, 312, 78, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10.2, r, "start", True)
        s += Yazi(x + 14, y + 44, acik[:50], 9, "#1e293b", "start", False)
        s += Yazi(x + 14, y + 60, acik[50:], 9, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 245
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İLKELİ BİR HAYAT SÜRMENİN DÖRT TEMEL GÖSTERGESİ", "#b45309")

    ilkeler = [
        ("İSTİKAMET (Doğruluk)", "\"Emrolunduğun gibi dosdoğru ol!\" (Hûd, 11/112) — Özü ile sözü bir olmak", "#0284c7", "#e0f2fe"),
        ("EMANET VE SORUMLULUK", "Allah'a, kendine, ailesine, topluma ve çevreye karşı görevlerini yerine getirmek", "#059669", "#ecfdf5"),
        ("İTİDAL (Ölçülülük / Denge)", "İfrat (aşırılık) ve tefritten (ihmalden) kaçınıp orta yolu (ümmet-i vasat) tutmak", "#d97706", "#fef3c7"),
        ("İHSAN BİLİNCİ", "Her an Allah'ın huzurundaymış ve O kendisini görüyormuş gibi güzel yaşamak", "#dc2626", "#fef2f2")
    ]

    for i, (bas, acik, r, ar) in enumerate(ilkeler):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 86
        s += Kutu(x, y, 312, 72, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 24, bas, 10, r, "start", True)
        s += Yazi(x + 14, y + 48, acik[:52], 9, "#1e293b", "start", False)
        s += Yazi(x + 14, y + 62, acik[52:], 9, "#1e293b", "start", False)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-temel-dini-bilgiler-3", 1, gorsel_1())
    kaydet("10-temel-dini-bilgiler-3", 2, gorsel_2())
    kaydet("10-temel-dini-bilgiler-3", 3, gorsel_3())
    kaydet("10-temel-dini-bilgiler-3", 4, gorsel_4())


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
