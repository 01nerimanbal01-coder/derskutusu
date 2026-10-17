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
    s += Baslik(W, "HÜZÜN YILI'NDAN TAİF YOLCULUĞUNA TARİHSEL SÜREÇ (619 - 620)", "#991b1b")

    adimlar = [
        ("1. BOYKOTUN SONU", "3 yıllık Ebu Talib Mahallesi", "muhasarasının bitişi (619)", "#475569", "#f1f5f9"),
        ("2. HÜZÜN YILI (619)", "Ebû Tâlib ve Hz. Hatice'nin", "peş peşe vefatı (Senetü'l-Hüzn)", "#dc2626", "#fef2f2"),
        ("3. ARTAN MEKKE BASKISI", "Kabile korumasının kalkması", "ve tebliğin tıkanması", "#d97706", "#fef3c7"),
        ("4. TAİF YOLCULUĞU (620)", "Zeyd b. Hârise ile yeni", "bir tebliğ merkezi arayışı", "#059669", "#d1fae5")
    ]

    kw = 148
    gap = 12
    sx = (W - (4 * kw + 3 * gap)) // 2
    for i, (bas, m1, m2, r, ar) in enumerate(adimlar):
        x = sx + i * (kw + gap)
        y = 50
        s += Kutu(x, y, kw, 138, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 20, bas, 9.2, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 66, m1, 9, "#1e293b", "middle", True)
        s += Yazi(x + kw // 2, y + 88, m2, 8.8, "#475569", "middle", False)
        if i < 3:
            s += Ok(x + kw, y + 69, x + kw + gap, y + 69, "#64748b", 2)

    s += Kutu(34, 204, W - 68, 36, "#eff6ff", "#2563eb", 1.5, 8)
    s += Yazi(W // 2, 226, "Taif, Mekke'nin yaklaşık 100 km güneydoğusunda, Sakîf kabilesinin yaşadığı serin, verimli ve ticari öneme sahip şehirdir.", 9.5, "#1e40af", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TAİF'TE KARŞILAŞILAN ZORLUKLAR VE NEBEVİ DURUŞ", "#7c2d12")

    s += Kutu(26, 48, 304, 194, "#fef2f2", "#dc2626", 2, 10)
    s += Yazi(178, 70, "SAKÎF KABİLESİNİN TUTUMU", 11, "#b91c1c", "middle", True)
    sol = [
        "• Sakîf liderleri (Abdüleyl, Mes'ûd ve Habîb kardeşler)",
        "  Mekke ile olan ticari/siyasi çıkarlarını kaybetmekten korktu.",
        "• Lat putunun merkezinin Taif olması nedeniyle",
        "  tevhid davetini alay ve hakaretle reddettiler.",
        "• Ayaktakımını ve köleleri kışkırtarak yol boyunca",
        "  Hz. Peygamber'i (sav) ve Zeyd b. Hârise'yi taşlattılar.",
        "• Zeyd b. Hârise kendi bedenini Peygamberimize siper etti."
    ]
    for i, m in enumerate(sol):
        s += Yazi(38, 94 + i * 20, m, 9, "#1e293b", "start", i == 6)

    s += Kutu(350, 48, 304, 194, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(502, 70, "HZ. PEYGAMBER'İN (SAV) TEPKİSİ", 11, "#047857", "middle", True)
    sag = [
        "• Asla ümitsizliğe kapılmadı ve tebliğden vazgeçmedi.",
        "• Sığındığı bağda tüm acısını yalnız Allah'a arz ederek",
        "  tarihin en içli teslimiyet yakarışı olan 'Taif Duası'nı yaptı.",
        "• Bağda kendisine üzüm ikram eden Ninovalı Hristiyan",
        "  köle Addâs'a şefkatle yaklaşıp imanına vesile oldu.",
        "• Dağlar meleğinin helak teklifini reddederek:",
        "  'Belki Allah onların soyundan müminler çıkarır' buyurdu."
    ]
    for i, m in enumerate(sag):
        s += Yazi(362, 94 + i * 20, m, 9, "#1e293b", "start", i == 6)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TAİF YOLCULUĞUNUN DÖRT UNUTULMAZ TABLOSU", "#1e3a8a")

    tablolar = [
        ("1. Zeyd b. Hârise'nin Fedakârlığı", "Taif'te atılan taşlara karşı kendi vücudunu ve başını Resûlullah'a (sav) kalkan yaparak yaralanması", "#2563eb", "#dbeafe"),
        ("2. Eşsiz Taif Duası", "\"Allah'ım! Güçsüzlüğümü yalnız Sana arz ederim. Eğer bana karşı gazabın yoksa çektiğim eziyetlere aldırmam!\"", "#7c3aed", "#f3e8ff"),
        ("3. Addâs'ın Müslüman Oluşu", "'Bismillah' sözünden ve Yunus Peygamber (as) kardeşliğinden etkilenen Ninovalı köle Addâs'ın iman etmesi", "#059669", "#d1fae5"),
        ("4. Mut'im b. Adî'nin Eman'ı", "Mekke'ye dönüşte diplomatik tedbir olarak Mut'im bin Adî'nin himayesi (emanı) altında şehre girilmesi", "#d97706", "#fef3c7")
    ]

    for i, (bas, acik, r, ar) in enumerate(tablolar):
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
    s += Baslik(W, "TARİHSEL EMPATİ: HZ. ÂİŞE'YE GÖRE 'UHUD'DAN DAHA ZOR GÜN'", "#0f766e")

    s += Kutu(26, 48, 628, 82, "#fffbeb", "#d97706", 2, 10)
    s += Yazi(340, 72, "Hz. Âişe (ra) Soruyor: \"Ya Resûlallah! Hayatında Uhud gününden daha çetin bir gün yaşadın mı?\"", 10.5, "#b45309", "middle", True)
    s += Yazi(340, 96, "Hz. Peygamber'in (sav) Cevabı: Taif'ten dönüş günü, Karnü's-Seâlib'e varıncaya kadar yaşanan derin hüzün", 9.8, "#1e293b", "middle", False)
    s += Yazi(340, 116, "ve Cebrâil (as) ile Dağlar Meleği geldiğinde beddua yerine Taif'in gelecek nesilleri için hidayet dilemesi.", 9.8, "#1e293b", "middle", False)

    s += Kutu(26, 144, 628, 86, "#ecfdf5", "#059669", 2, 10)
    s += Yazi(340, 168, "NEBEVİ SABIR VE DUANIN MEYVESİ (HİCRETİN 9. YILI / 630)", 10.5, "#047857", "middle", True)
    s += Yazi(340, 192, "Taif'te Peygamberimizi taşlayan Sakîf kabilesinin çocukları ve torunları, sadece 10 yıl sonra", 9.8, "#1e293b", "middle", False)
    s += Yazi(340, 212, "Medine'ye heyet göndererek kendi rızalarıyla Müslüman olmuş ve İslam'ın sancağını taşımıştır!", 9.8, "#065f46", "middle", True)

    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-peygamberimizin-hayati-3", 1, gorsel_1())
    kaydet("10-peygamberimizin-hayati-3", 2, gorsel_2())
    kaydet("10-peygamberimizin-hayati-3", 3, gorsel_3())
    kaydet("10-peygamberimizin-hayati-3", 4, gorsel_4())


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
