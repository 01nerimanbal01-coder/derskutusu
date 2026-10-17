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
    s += Baslik(W, "MEKÂNSAL BİLGİ TEKNOLOJİLERİNİN ÜÇ TEMEL BİLEŞENİ", "#0f766e")

    kartlar = [
        ("UZAKTAN ALGILAMA (UA)", "#0284c7", "#e0f2fe", [
            "Fiziksel temas olmadan algılama",
            "Gözlem uyduları ve İHA / Dronlar",
            "Pasif (Güneş) ve Aktif (Radar/LiDAR)",
            "Geniş alanların güncel görüntüsü"
        ]),
        ("KÜRESEL KONUMLANDIRMA (GNSS)", "#d97706", "#fef3c7", [
            "Uydu tabanlı hassas konum belirleme",
            "Enlem, boylam, yükselti ve zaman",
            "GPS, GLONASS, Galileo, BeiDou",
            "Navigasyon ve saha veri toplama"
        ]),
        ("COĞRAFİ BİLGİ SİSTEMLERİ (CBS)", "#059669", "#d1fae5", [
            "Mekânsal veriyi toplama ve depolama",
            "Katmanlı (vektör/raster) analiz",
            "Sorgulama, modelleme ve sentez",
            "Haritalama ve karar destek sistemi"
        ])
    ]

    kw = 200
    gap = 16
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, renk, acik, maddeler) in enumerate(kartlar):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 165, acik, renk, 2, 10)
        s += Kutu(x, y, kw, 32, renk, renk, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 10, "#ffffff", "middle", True)
        for j, m in enumerate(maddeler):
            s += Daire(x + 16, y + 54 + j * 28, 4, renk, renk, 1)
            s += Yazi(x + 26, y + 58 + j * 28, m, 9.5, "#1e293b", "start", False)

    s += Ok(sx + kw, 130, sx + kw + gap, 130, "#475569", 2)
    s += Ok(sx + 2 * kw + gap, 130, sx + 2 * (kw + gap), 130, "#475569", 2)
    s += Kutu(60, 222, W - 120, 28, "#f0fdf4", "#16a34a", 1.5, 8)
    s += Yazi(W // 2, 240, "UA ve GNSS ile elde edilen veriler, CBS ortamında bütünleştirilerek analiz ve haritalamaya dönüştürülür.", 10, "#166534", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 270
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "CBS KATMANLI YAPI VE VERİ MODELLERİ (VEKTÖR - RASTER)", "#1d4ed8")

    # Sol: Katmanlı yapı
    s += Kutu(24, 46, 300, 206, "#eff6ff", "#3b82f6", 1.5, 10)
    s += Yazi(174, 68, "CBS Katman (Layer) Mantığı", 11.5, "#1e40af", "middle", True)
    katmanlar = [
        ("1. İdari Sınırlar ve Yerleşme", "#2563eb", "#dbeafe", 82),
        ("2. Ulaşım ve Akarsu Ağı", "#0891b2", "#cffafe", 114),
        ("3. Arazi Kullanımı ve Bitki Örtüsü", "#16a34a", "#dcfce7", 146),
        ("4. Topoğrafya / Yükselti Modeli", "#d97706", "#fef3c7", 178),
        ("BÜTÜNLEŞİK CBS HARİTASI (SENTEZ)", "#7c3aed", "#ede9fe", 214)
    ]
    for ad, r, ar, y in katmanlar:
        s += Kutu(44, y, 260, 24, ar, r, 1.5, 6)
        s += Yazi(174, y + 16, ad, 9.5, r, "middle", True)

    # Sağ: Vektör vs Raster
    s += Kutu(344, 46, 312, 98, "#f0fdf4", "#16a34a", 1.5, 10)
    s += Yazi(500, 66, "VEKTÖR VERİ MODELİ (Koordinat Tabanlı)", 11, "#15803d", "middle", True)
    s += Daire(380, 96, 5, "#dc2626", "#991b1b", 1.5)
    s += Yazi(380, 122, "Nokta (Okul, Kuyu)", 9.5, "#1e293b", "middle", True)
    s += Cizgi(460, 106, 520, 86, "#2563eb", 3)
    s += Yazi(490, 122, "Çizgi (Yol, Akarsu)", 9.5, "#1e293b", "middle", True)
    s += Cokgen([(575, 106), (600, 82), (630, 92), (620, 110)], "#bbf7d0", "#15803d", 2)
    s += Yazi(602, 128, "Poligon (Göl, İl)", 9.5, "#1e293b", "middle", True)

    s += Kutu(344, 154, 312, 98, "#fffbeb", "#d97706", 1.5, 10)
    s += Yazi(500, 174, "RASTER VERİ MODELİ (Hücre / Piksel Tabanlı)", 11, "#b45309", "middle", True)
    renkler = ["#fde68a", "#fcd34d", "#fbbf24", "#f59e0b", "#60a5fa", "#34d399", "#a7f3d0", "#fcd34d", "#10b981"]
    for r_i in range(3):
        for c_i in range(3):
            s += Kutu(368 + c_i * 18, 184 + r_i * 18, 18, 18, renkler[r_i * 3 + c_i], "#92400e", 1, 0)
    s += Yazi(535, 200, "• Uydu görüntüleri ve hava fotoğrafları", 9.5, "#1e293b", "start", False)
    s += Yazi(535, 218, "• Sayısal Yükselti Modeli (SYM / DEM)", 9.5, "#1e293b", "start", False)
    s += Yazi(535, 236, "• Sıcaklık, yağış ve eğim yüzeyleri", 9.5, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "CBS VE UZAKTAN ALGILAMANIN BAŞLICA UYGULAMA ALANLARI", "#7c2d12")

    alanlar = [
        ("Afet ve Risk Yönetimi", "Deprem, sel, heyelan, çığ ve orman yangını risk/hasar haritaları", "#dc2626", "#fef2f2"),
        ("Çevre ve İklim İzleme", "Göl çekilmesi, buzul erimesi, ormansızlaşma ve kirlilik takibi", "#059669", "#ecfdf5"),
        ("Şehir Planlama ve Ulaşım", "Akıllı şehirler, altyapı ağı, trafik yoğunluğu ve tesis yer seçimi", "#2563eb", "#eff6ff"),
        ("Hassas Tarım ve Orman", "Ürün sağlığı (NDVI), rekolte tahmini, sulama ve toprak analizi", "#65a30d", "#f7fee7"),
        ("Arkeoloji ve Miras", "LiDAR ve termal algılamayla toprak altı antik yapıların tespiti", "#9333ea", "#faf5ff"),
        ("Sağlık ve Demografi", "Salgın hastalık yayılım haritaları, nüfus dağılışı ve hastane erişimi", "#0891b2", "#ecfeff")
    ]

    kw, kh = 306, 58
    for i, (bas, acik, r, ar) in enumerate(alanlar):
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
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "TÜRKİYE'DE UZAKTAN ALGILAMA UYDULARI VE CBS PLATFORMLARI", "#991b1b")

    uydular = [
        ("RASAT (2011)", "İlk yerli tasarım yer gözlem uydusu", "Haritacılık, afet ve çevre izleme (2022'de görevini tamamladı)", "#475569", "#f1f5f9"),
        ("GÖKTÜRK-2 (2012)", "Yüksek çözünürlüklü yerli gözlem uydusu", "TÜBİTAK UZAY üretimi; savunma, çevre ve planlama", "#1d4ed8", "#dbeafe"),
        ("GÖKTÜRK-1 (2016)", "Çok yüksek çözünürlüklü (0,5 m) uydu", "Coğrafi kısıtlama olmaksızın dünya genelinde görüntüleme", "#0369a1", "#e0f2fe"),
        ("İMECE (2023)", "Türkiye'nin ilk yerli metre altı gözlem uydusu", "Afet yönetimi, tarım, şehircilik ve savunma amaçlı", "#b91c1c", "#fee2e2")
    ]

    for i, (ad, alt, det, r, ar) in enumerate(uydular):
        x = 24 + (i % 2) * 320
        y = 46 + (i // 2) * 76
        s += Kutu(x, y, 312, 66, ar, r, 1.5, 8)
        s += Yazi(x + 14, y + 21, ad + " — " + alt, 10, r, "start", True)
        s += Yazi(x + 14, y + 44, det, 9.2, "#1e293b", "start", False)

    s += Kutu(24, 200, 632, 36, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(340, 222, "Ulusal CBS Platformları: HGM Küre / Atlas • TUCBS (Atlas) • AFAD (AFAD-RED) • TKGM Parsel Sorgu", 10, "#92400e", "middle", True)
    s += svg_bitir()
    return s


if __name__ == "__main__":
    kaydet("10-cografya-3", 1, gorsel_1())
    kaydet("10-cografya-3", 2, gorsel_2())
    kaydet("10-cografya-3", 3, gorsel_3())
    kaydet("10-cografya-3", 4, gorsel_4())


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
