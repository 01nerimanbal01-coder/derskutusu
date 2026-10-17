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
    s += Baslik(W, "İSLAM DÜŞÜNCESİNDE VARLIK SINIFLANDIRMASI: HÂLIK VE MAHLUK", "#0f766e")

    s += Kutu(26, 48, 302, 162, "#ecfdf5", "#059669", 2, 10)
    s += Kutu(26, 48, 302, 34, "#059669", "#059669", 1, 10)
    s += Yazi(177, 70, "ZORUNLU VARLIK (Vâcibü'l-Vücûd)", 10.5, "#ffffff", "middle", True)
    z_mad = [
        "• Yüce Allah'tır (cc); Hâlık (Yaratan) O'dur.",
        "• Varlığı kendindendir, başkasının varlığına muhtaç değildir.",
        "• Ezeli ve ebedidir (başlangıcı ve sonu yoktur).",
        "• Yokluğu düşünülemez; her şey O'na muhtaçtır (Samed)."
    ]
    for i, m in enumerate(z_mad):
        s += Yazi(40, 106 + i * 24, m, 9.2, "#1e293b", "start", i == 0)

    s += Ok(332, 128, 350, 128, "#0f766e", 2.5)

    s += Kutu(354, 48, 300, 162, "#eff6ff", "#2563eb", 2, 10)
    s += Kutu(354, 48, 300, 34, "#2563eb", "#2563eb", 1, 10)
    s += Yazi(504, 70, "MÜMKÜN VARLIK (Mümkinü'l-Vücûd)", 10.5, "#ffffff", "middle", True)
    m_mad = [
        "• Allah'ın dışındaki her şeydir (Âlem / Mâsivâ / Mahlukat).",
        "• Var olmak ve varlığını sürdürmek için Allah'a muhtaçtır.",
        "• Sonradan yaratılmıştır (hâdis); başlangıcı ve sonu vardır.",
        "• Allah'ın varlığına ve birliğine işaret eden birer 'âyet'tir."
    ]
    for i, m in enumerate(m_mad):
        s += Yazi(368, 106 + i * 24, m, 9.2, "#1e293b", "start", i == 0)

    s += Kutu(36, 220, W - 72, 28, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(W // 2, 238, "Fâtır Suresi 15. Ayet: \"Ey insanlar! Siz Allah'a muhtaçsınız; Allah ise her bakımdan sınırsız zengin olandır.\"", 9.8, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ÂLEMİN İKİ BOYUTU: ŞEHÂDET VE GAYB ÂLEMİ", "#1e3a8a")

    s += Kutu(26, 48, 304, 158, "#e0f2fe", "#0284c7", 2, 10)
    s += Yazi(178, 72, "ŞEHÂDET (GÖRÜNEN / MADDİ) ÂLEMİ", 11, "#0369a1", "middle", True)
    sh = [
        "• Beş duyu organımızla veya bilimsel deney/gözlem",
        "  araçlarıyla algılayabildiğimiz maddi evrendir.",
        "• Zaman, mekân, madde ve fizik yasalarıyla kuşatılmıştır.",
        "• Örnek: İnsanlar, hayvanlar, bitkiler, dağlar, denizler,",
        "  gezegenler, galaksiler ve atom altı parçacıklar."
    ]
    for i, m in enumerate(sh):
        s += Yazi(40, 98 + i * 20, m, 9.3, "#1e293b", "start", False)

    s += Kutu(350, 48, 304, 158, "#f3e8ff", "#7c3aed", 2, 10)
    s += Yazi(502, 72, "GAYB (DUYULAR ÖTESİ / MANEVİ) ÂLEMİ", 11, "#6d28d9", "middle", True)
    gy = [
        "• Duyu organlarımızla ve deneyle doğrudan",
        "  algılanamayan, yalnızca vahiy ile bilinen âlemdir.",
        "• Mutlak gaybı yalnızca Yüce Allah (Âlimü'l-Gayb) bilir.",
        "• Örnek: Melekler, cinler, ruh, berzah âlemi, kıyamet,",
        "  ahiret hayatı, cennet ve cehennem."
    ]
    for i, m in enumerate(gy):
        s += Yazi(364, 98 + i * 20, m, 9.3, "#1e293b", "start", False)

    s += Kutu(36, 216, W - 72, 28, "#ecfdf5", "#059669", 1.5, 8)
    s += Yazi(W // 2, 234, "Haşr Suresi 22. Ayet: \"O, kendisinden başka ilah olmayan Allah'tır; gaybı da şehâdet âlemini de bilendir.\"", 9.8, "#065f46", "middle", True)
    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ALLAH - ÂLEM İLİŞKİSİNİN DÖRT TEMEL BOYUTU", "#7c2d12")

    boyutlar = [
        ("1. YOKTAN YARATMA (Halk / İbdâ)", "Allah âlemi 'Ol!' (Kün) emriyle, örneği olmadan yoktan var etmiştir (El-Hâlık, El-Bâri, El-Musavvir).", "#2563eb", "#dbeafe"),
        ("2. ÖLÇÜ VE DÜZEN (Kader / Sünnetullah)", "Evrendeki her varlık hassas bir ölçü, denge ve ilahi yasalara (sünnetullah) göre yaratılmıştır.", "#059669", "#d1fae5"),
        ("3. YÖNETME VE KORUMA (Rubûbiyet / Kayyûm)", "Allah yarattığı evreni kendi hâline terk etmemiş; her an yaratma, koruma ve yönetme hâlindedir.", "#d97706", "#fef3c7"),
        ("4. RIZIKLANDIRMA VE RAHMET (Rezzâk / Rahmân)", "Yeryüzündeki tüm canlıların maddi ve manevi ihtiyaçlarını karşılayan, merhamet eden Allah'tır.", "#9333ea", "#f3e8ff")
    ]

    for i, (bas, acik, r, ar) in enumerate(boyutlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 76
        s += Kutu(x, y, 312, 66, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 22, bas, 10, r, "start", True)
        s += Yazi(x + 14, y + 44, acik[:52], 9, "#1e293b", "start", False)
        s += Yazi(x + 14, y + 58, acik[52:], 9, "#1e293b", "start", False)

    s += Kutu(24, 204, 632, 42, "#fef2f2", "#dc2626", 1.5, 8)
    s += Yazi(340, 222, "Rahmân Suresi 29. Ayet: \"Göklerde ve yerde bulunan herkes O'ndan ister. O, her an yeni bir ilahi tasarruftadır (yaratmadadır).\"", 9.5, "#991b1b", "middle", True)
    s += Yazi(340, 238, "Bu ayet, Allah'ın evreni yaratıp kenara çekildiğini iddia eden 'Deizm' anlayışını kesin olarak reddeder.", 9.2, "#7f1d1d", "middle", False)
    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 245
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "İKİ KİTAP: KUR'AN-I KERİM VE KAİNAT (EVREN) KİTABI", "#047857")

    s += Kutu(30, 50, 280, 140, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(170, 76, "KUR'AN-I KERİM (Vahiy Kitabı)", 11, "#065f46", "middle", True)
    s += Yazi(170, 104, "• Allah'ın kelam sıfatının tecellisidir.", 9.5, "#1e293b", "middle", False)
    s += Yazi(170, 126, "• Yazılı ve sözlü ilahi mesajlardan", 9.5, "#1e293b", "middle", False)
    s += Yazi(170, 144, "  (vahiylerden) oluşan 'âyet'lerdir.", 9.5, "#1e293b", "middle", False)
    s += Yazi(170, 170, "→ Okunur, anlaşılır ve yaşanır.", 9.5, "#047857", "middle", True)

    s += Kutu(370, 50, 280, 140, "#eff6ff", "#2563eb", 2, 10)
    s += Yazi(510, 76, "ÂLEM / EVREN (Kainat Kitabı)", 11, "#1e40af", "middle", True)
    s += Yazi(510, 104, "• Allah'ın tekvin ve kudret sıfatının tecellisidir.", 9.5, "#1e293b", "middle", False)
    s += Yazi(510, 126, "• Gece-gündüz, yağmur, canlılar gibi", 9.5, "#1e293b", "middle", False)
    s += Yazi(510, 144, "  kevnî (yaratılışsal) 'âyet'lerdir.", 9.5, "#1e293b", "middle", False)
    s += Yazi(510, 170, "→ Gözlemlenir, tefekkür edilir ve korunur.", 9.5, "#1d4ed8", "middle", True)

    s += Kutu(30, 202, 620, 30, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(340, 221, "Her iki kitaptaki 'âyet'ler de insanı tefekküre yöneltir ve Yüce Yaratıcı'nın varlığına, birliğine (tevhid) şahitlik eder.", 9.8, "#92400e", "middle", True)
    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-din-kulturu-ve-ahlak-bilgisi-3", 1, gorsel_1())
    kaydet("10-din-kulturu-ve-ahlak-bilgisi-3", 2, gorsel_2())
    kaydet("10-din-kulturu-ve-ahlak-bilgisi-3", 3, gorsel_3())
    kaydet("10-din-kulturu-ve-ahlak-bilgisi-3", 4, gorsel_4())


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
