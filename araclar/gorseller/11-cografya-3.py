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


def Ok(x1, y1, x2, y2, renk="#475569", kw=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{renk}" stroke-width="{kw}" stroke-linecap="round"/>'


def gorsel_1():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "MEKÂNSAL SORUNLARIN ÇÖZÜMÜNDE COĞRAFYA BİLİMİNİN İLKELERİ", "#0f766e")

    ilkeler = [
        ("1. DAĞILIŞ İLKESİ", "Coğrafyaya özgü temel ilkedir!", "Sorunun nerede (yatay, dikey ve", "zamansal) görüldüğünü belirler.", "#059669", "#d1fae5"),
        ("2. NEDENSELLİK İLKESİ", "Sebep - Sonuç Analizi", "Mekânsal sorunun hangi doğal ve", "beşerî nedenlerle çıktığını açıklar.", "#0284c7", "#e0f2fe"),
        ("3. BAĞLANTI (KARŞILIKLI İLGİ)", "Bütüncül Etkileşim", "Sorunun iklim, su, toprak, nüfus ve", "ekonomiyle karşılıklı bağını kurar.", "#7c3aed", "#f3e8ff")
    ]

    kw = 202
    gap = 14
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, alt, m1, m2, r, ar) in enumerate(ilkeler):
        x = sx + i * (kw + gap)
        y = 48
        s += Kutu(x, y, kw, 154, ar, r, 2, 10)
        s += Kutu(x, y, kw, 32, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 21, bas, 9.8, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 60, alt, 9.5, r, "middle", True)
        s += Yazi(x + kw // 2, y + 88, m1, 9, "#1e293b", "middle", False)
        s += Yazi(x + kw // 2, y + 108, m2, 9, "#1e293b", "middle", False)

    s += Kutu(30, 214, W - 60, 32, "#fef3c7", "#d97706", 1.5, 8)
    s += Yazi(W // 2, 234, "Coğrafya; fiziki ve beşerî sistemleri birleştirerek mekânsal sorunlara sürdürülebilir planlama çözümleri üretir.", 9.5, "#92400e", "middle", True)
    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 260
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "ÖLÇEKLERİNE GÖRE MEKÂNSAL SORUNLAR VE COĞRAFİ ÇÖZÜMLER", "#1e3a8a")

    sorunlar = [
        ("YEREL / KENTSEL ÖLÇEK", "Çarpık kentleşme, kentsel ısı adası, taşkın, trafik ve hava kirliliği → Akıllı şehir planlaması, yeşil koridorlar ve dere yatağı koruma.", "#2563eb", "#dbeafe"),
        ("HAVZA / BÖLGESEL ÖLÇEK", "Konya Havzası obruk oluşumu, Tuz/Burdur Gölü kuruması, erozyon, müsilaj → Bütüncül havza yönetimi, damla sulama ve uygun ürün deseni.", "#d97706", "#fef3c7"),
        ("ULUSAL ÖLÇEK", "Bölgesel kalkınma farkları, iç göç baskısı, deprem ve orman yangını riskleri → Bölgesel kalkınma projeleri (GAP, DAP, DOKAP) ve afet CBS.", "#059669", "#d1fae5"),
        ("KÜRESEL ÖLÇEK", "Küresel iklim değişikliği, biyoçeşitlilik kaybı, çölleşme ve su krizi → Yenilenebilir enerji geçişi, karbon yutak alanlarının korunması.", "#dc2626", "#fef2f2")
    ]

    for i, (bas, acik, r, ar) in enumerate(sorunlar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 96
        s += Kutu(x, y, 312, 84, ar, r, 1.6, 8)
        s += Kutu(x, y, 312, 26, r, r, 1, 8)
        s += Yazi(x + 156, y + 18, bas, 9.5, "#ffffff", "middle", True)
        s += Yazi(x + 12, y + 44, acik[:50], 8.6, "#1e293b", "start", False)
        s += Yazi(x + 12, y + 60, acik[50:100], 8.6, "#1e293b", "start", False)
        s += Yazi(x + 12, y + 74, acik[100:], 8.6, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "WEB TABANLI CBS (WEB-GIS) MİMARİSİ VE AVANTAJLARI", "#6d28d9")

    adimlar = [
        ("1. COĞRAFİ VERİ SUNUCUSU", "Uydu görüntüleri, harita servisleri", "(WMS, WFS) ve bulut veri tabanı", "#2563eb", "#dbeafe"),
        ("2. İNTERNET AĞI (BULUT)", "Gerçek zamanlı veri paylaşımı", "ve çoklu kullanıcı erişimi", "#7c3aed", "#f3e8ff"),
        ("3. WEB TARAYICI / MOBİL", "Kurulum gerektirmeden katman", "açma, çizim, ölçüm ve sorgulama", "#059669", "#d1fae5")
    ]

    kw = 196
    gap = 18
    sx = (W - (3 * kw + 2 * gap)) // 2
    for i, (bas, m1, m2, r, ar) in enumerate(adimlar):
        x = sx + i * (kw + gap)
        y = 50
        s += Kutu(x, y, kw, 134, ar, r, 2, 10)
        s += Kutu(x, y, kw, 30, r, r, 1, 10)
        s += Yazi(x + kw // 2, y + 20, bas, 9.2, "#ffffff", "middle", True)
        s += Yazi(x + kw // 2, y + 64, m1, 9, "#1e293b", "middle", True)
        s += Yazi(x + kw // 2, y + 88, m2, 8.8, "#475569", "middle", False)
        if i &lt; 2:
            s += Ok(x + kw, y + 67, x + kw + gap, y + 67, "#64748b", 2)

    s += Kutu(28, 198, W - 56, 36, "#eef2ff", "#4338ca", 1.5, 8)
    s += Yazi(W // 2, 220, "Masaüstü CBS'den Farkı: Pahalı donanım ve yazılım kurulumu gerektirmez; internet tarayıcısıyla her yerden erişilir.", 9.4, "#312e81", "middle", True)
    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "BAŞLICA ULUSAL VE KÜRESEL WEB TABANLI CBS PLATFORMLARI", "#b45309")

    platformlar = [
        ("TUCBS Atlas (atlas.gov.tr)", "Çevre, Şehircilik ve İklim Değişikliği Bakanlığının ulusal web CBS portalı", "#dc2626", "#fef2f2"),
        ("HGM Küre ve HGM Atlas", "Harita Genel Müdürlüğünün yerli 3B/2B harita, ölçüm ve sorgulama platformu", "#0284c7", "#e0f2fe"),
        ("TKGM Parsel Sorgu / MEGSİS", "Tapu ve Kadastro Genel Müdürlüğünün ada/parsel ve mülkiyet sorgu sistemi", "#059669", "#ecfdf5"),
        ("MTA Yerbilimleri Portalı", "Diri fay hatları, heyelan, jeoloji ve maden katmanlarını sunan web CBS", "#d97706", "#fef3c7"),
        ("AFAD TDTH ve İRAP", "Türkiye Deprem Tehlike Haritaları İnteraktif Web Uygulaması", "#9333ea", "#faf5ff"),
        ("Google Earth Web / Copernicus", "Küresel uydu görüntüsü arşivi, zaman kaydırıcı ve Avrupa uzay gözlem portalı", "#475569", "#f1f5f9")
    ]

    kw, kh = 306, 56
    for i, (bas, acik, r, ar) in enumerate(platformlar):
        col = i % 2
        row = i // 2
        x = 26 + col * (kw + 16)
        y = 48 + row * (kh + 10)
        s += Kutu(x, y, kw, kh, ar, r, 1.5, 8)
        s += Yazi(x + 12, y + 20, bas, 9.6, r, "start", True)
        s += Yazi(x + 12, y + 40, acik, 8.6, "#1e293b", "start", False)

    s += svg_bitir()
    return s


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