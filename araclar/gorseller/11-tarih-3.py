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
    s += Baslik(W, "1683 - 1789 DÖNEMİ OSMANLI SİYASİ VE ASKERÎ KRONOLOJİSİ", "#991b1b")

    olaylar = [
        ("1683 - 1699", "II. Viyana ve Kutsal İttifak", "Karlofça (1699) ve İstanbul (1700) Antlaşmaları: İlk büyük toprak kaybı", "#dc2626", "#fef2f2"),
        ("1711 ve 1718", "Prut Zaferi ve Pasarofça", "Prut (1711) ile Azak geri alındı; Pasarofça (1718) ile Batı üstünlüğü kabul edildi", "#d97706", "#fef3c7"),
        ("1736 - 1739", "Belgrad Antlaşması (1739)", "Rusya ve Avusturya'ya karşı zafer; 18. yy'ın en kazançlı antlaşması, Karadeniz Türk gölü", "#059669", "#d1fae5"),
        ("1768 - 1774", "Küçük Kaynarca Ant. (1774)", "Çeşme Baskını (1770); Kırım müstakil oldu, Rusya Karadeniz'e ve kapitülasyonlara kavuştu", "#7c3aed", "#f3e8ff")
    ]

    for i, (tarih, bas, acik, r, ar) in enumerate(olaylar):
        x = 24 + (i % 2) * 320
        y = 48 + (i // 2) * 94
        s += Kutu(x, y, 312, 82, ar, r, 1.8, 8)
        s += Kutu(x, y, 312, 26, r, r, 1, 8)
        s += Yazi(x + 156, y + 18, f"{tarih} — {bas}", 9.5, "#ffffff", "middle", True)
        s += Yazi(x + 12, y + 46, acik[:50], 8.8, "#1e293b", "start", False)
        s += Yazi(x + 12, y + 64, acik[50:], 8.8, "#1e293b", "start", False)

    s += svg_bitir()
    return s


def gorsel_2():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KUTSAL İTTİFAK SAVAŞLARI VE KARLOFÇA ANTLAŞMASI (1699)", "#1e3a8a")

    s += Kutu(24, 48, 306, 192, "#eff6ff", "#2563eb", 1.8, 10)
    s += Yazi(177, 68, "Kutsal İttifak Devletleri (5 Devlet)", 10.2, "#1d4ed8", "middle", True)
    devletler = [
        "1. Avusturya (Habsburg): Macaristan ve Erdel'i aldı.",
        "2. Lehistan (Polonya): Podolya ve Ukrayna'yı aldı.",
        "3. Venedik: Mora Yarımadası ve Dalmaçya kıyılarını aldı.",
        "4. Rusya (1700 İstanbul Ant.): Azak Kalesi'ni aldı.",
        "5. Malta Şövalyeleri (Papalık teşvikiyle deniz desteği)."
    ]
    for i, m in enumerate(devletler):
        s += Yazi(38, 94 + i * 26, m, 9, "#1e293b", "start", True)

    s += Kutu(348, 48, 308, 192, "#fef2f2", "#dc2626", 1.8, 10)
    s += Yazi(502, 68, "Karlofça Antlaşmasının Tarihsel Sonuçları", 10.2, "#b91c1c", "middle", True)
    sonuclar = [
        "• Osmanlı Devleti Batı'da İLK KEZ büyük çapta",
        "  toprak kaybetti (Orta Avrupa egemenliği sona erdi).",
        "• Saldırı/fetih politikasından SAVUNMA ve kaybettiği",
        "  toprakları geri alma politikasına geçildi.",
        "• İngiltere ve Hollanda ilk kez 'arabulucu' oldu;",
        "  diplomasi (Reisülküttaplık) askeri gücün önüne geçti.",
        "• Garantör devlet Avusturya oldu (Süre: 25 yıl)."
    ]
    for i, m in enumerate(sonuclar):
        s += Yazi(362, 92 + i * 20, m, 8.9, "#1e293b", "start", i in (0, 2, 5))

    s += svg_bitir()
    return s


def gorsel_3():
    W, H = 680, 250
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "18. YÜZYILDA DİPLOMATİK DÖNÜM NOKTALARI: PASAROFÇA VE BELGRAD", "#0f766e")

    s += Kutu(24, 48, 306, 186, "#fffbeb", "#d97706", 1.8, 10)
    s += Kutu(24, 48, 306, 30, "#d97706", "#d97706", 1, 10)
    s += Yazi(177, 68, "PASAROFÇA ANTLAŞMASI (1718)", 10, "#ffffff", "middle", True)
    p_mad = [
        "• Venedik'ten Mora geri alındı, ancak Avusturya'ya",
        "  Belgrad, Banat ve Kuzey Sırbistan kaybedildi.",
        "• Osmanlı, kaybettiği toprakları geri alma ümidini",
        "  kaybederek 'Mevcut sınırları koruma ve barış'",
        "  politikasına geçti.",
        "• Batı'nın üstünlüğü kabul edilip LALE DEVRİ başladı."
    ]
    for i, m in enumerate(p_mad):
        s += Yazi(38, 98 + i * 21, m, 8.9, "#1e293b", "start", i == 5)

    s += Kutu(350, 48, 306, 186, "#ecfdf5", "#059669", 1.8, 10)
    s += Kutu(350, 48, 306, 30, "#059669", "#059669", 1, 10)
    s += Yazi(503, 68, "BELGRAD ANTLAŞMASI (1739)", 10, "#ffffff", "middle", True)
    b_mad = [
        "• Humbaracı Ahmet Paşa'nın ıslahatlarıyla güçlenen",
        "  ordu, hem Avusturya'yı hem Rusya'yı mağlup etti.",
        "• Belgrad geri alındı; Rusya'nın Karadeniz'de savaş",
        "  ve ticaret gemisi bulundurması yasaklandı.",
        "• Karadeniz'in 'Türk gölü' olduğunu belgeleyen SON,",
        "  Osmanlı'nın 18. yy'da imzaladığı EN KAZANÇLI antlaşmadır.",
        "• Arabulucu Fransa'ya kapitülasyonlar SÜRESİZ verildi (1740)."
    ]
    for i, m in enumerate(b_mad):
        s += Yazi(364, 98 + i * 19, m, 8.7, "#1e293b", "start", i in (4, 5, 6))

    s += svg_bitir()
    return s


def gorsel_4():
    W, H = 680, 255
    s = svg_basla(W, H)
    s += Arka(W, H, "#f8fafc")
    s += Baslik(W, "KÜÇÜK KAYNARCA ANTLAŞMASI (1774) VE KIRIM'IN KAYBI SÜRECİ", "#6d28d9")

    s += Kutu(24, 48, 312, 192, "#faf5ff", "#7c3aed", 1.8, 10)
    s += Yazi(180, 68, "Küçük Kaynarca'nın (1774) Ağır Maddeleri", 10, "#6d28d9", "middle", True)
    k_mad = [
        "1. Kırım Hanlığı siyasi olarak bağımsız oldu, yalnızca",
        "   dini bakımdan Osmanlı Halifesi'ne bağlı kaldı (İlk kez",
        "   halkı Türk ve Müslüman bir bölge kaybedildi!).",
        "2. Rusya Karadeniz'de donanma bulundurma ve Boğazlardan",
        "   ticaret gemisi geçirme hakkı elde etti.",
        "3. Rusya, Osmanlı'daki Ortodoksların koruyuculuğunu aldı.",
        "4. Osmanlı tarihinde İLK KEZ savaş tazminatı ödedi."
    ]
    for i, m in enumerate(k_mad):
        s += Yazi(36, 92 + i * 20, m, 8.7, "#1e293b", "start", i in (2, 5, 6))

    s += Kutu(352, 48, 304, 192, "#fef2f2", "#dc2626", 1.8, 10)
    s += Yazi(504, 68, "Kırım'ın Elden Çıkışının 3 Aşaması", 10, "#b91c1c", "middle", True)
    kirim = [
        ("1. KÜÇÜK KAYNARCA (1774)", "Kırım bağımsız devlet oldu (Osmanlı'dan koparıldı).", "#d97706", "#fef3c7"),
        ("2. AYNALI KAVAK TENKİHNAMESİ (1779)", "Rus yanlısı Şahin Giray'ın hanlığı onaylandı.", "#ea580c", "#ffedd5"),
        ("3. İLHAK (1783) VE YAŞ ANT. (1792)", "Rusya 1783'te Kırım'ı işgal etti; Yaş ile kabul edildi.", "#dc2626", "#fee2e2")
    ]
    for i, (bas, acik, r, ar) in enumerate(kirim):
        y = 84 + i * 50
        s += Kutu(366, y, 276, 42, ar, r, 1.5, 6)
        s += Yazi(504, y + 16, bas, 9, r, "middle", True)
        s += Yazi(504, y + 33, acik, 8.4, "#1e293b", "middle", False)

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
