# -*- coding: utf-8 -*-
"""11. Sınıf Felsefe - 3. Hafta Görselleri (Çevre ve İnsan İlişkisi: Çevre Etiği Yaklaşımları)"""


def _svg(g, y, icerik):
    return (
        f'<svg viewBox="0 0 {g} {y}" width="100%" xmlns="http://www.w3.org/2000/svg" '
        f'style="max-width:{g}px;display:block;margin:14px auto;background:#fff;'
        f'border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _baslik(g, metin, renk="#1e293b"):
    return (
        f'<rect x="0" y="0" width="{g}" height="38" rx="10" fill="{renk}"/>'
        f'<rect x="0" y="20" width="{g}" height="18" fill="{renk}"/>'
        f'<text x="{g//2}" y="25" font-family="Arial,sans-serif" font-size="14" '
        f'font-weight="bold" fill="#ffffff" text-anchor="middle">{metin}</text>'
    )


def _kutu(x, y, g, yk, r_ark, r_ken, baslik, satirlar, r_bas="#0f172a"):
    ic = f'<rect x="{x}" y="{y}" width="{g}" height="{yk}" rx="8" fill="{r_ark}" stroke="{r_ken}" stroke-width="1.8"/>'
    ic += f'<text x="{x+g//2}" y="{y+22}" font-family="Arial,sans-serif" font-size="12.5" font-weight="bold" fill="{r_bas}" text-anchor="middle">{baslik}</text>'
    ic += f'<line x1="{x+10}" y1="{y+30}" x2="{x+g-10}" y2="{y+30}" stroke="{r_ken}" stroke-width="1"/>'
    for i, s in enumerate(satirlar):
        ic += f'<text x="{x+g//2}" y="{y+48+i*18}" font-family="Arial,sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s}</text>'
    return ic


def gorsel_1():
    """Ahlaki İlgi Çemberinin Genişlemesi: İnsan -> Canlılar -> Ekosistem"""
    g, y = 740, 290
    s = _baslik(g, "ÇEVRE ETİĞİNDE AHLAKİ İLGİ ÇEMBERİNİN GENİŞLEMESİ", "#15803d")
    # İç içe halkalar (sol taraf)
    cx, cy = 195, 165
    s += f'<circle cx="{cx}" cy="{cy}" r="105" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
    s += f'<text x="{cx}" y="{cy-82}" font-family="Arial,sans-serif" font-size="11.5" font-weight="bold" fill="#14532d" text-anchor="middle">3. EKOSENTRİZM (Ekosistem)</text>'
    s += f'<text x="{cx}" y="{cy+93}" font-family="Arial,sans-serif" font-size="10.5" fill="#14532d" text-anchor="middle">Toprak, Su, Hava, Cansız Doğa + Türler</text>'

    s += f'<circle cx="{cx}" cy="{cy}" r="68" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>'
    s += f'<text x="{cx}" y="{cy-45}" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#854d0e" text-anchor="middle">2. BİYOSENTRİZM</text>'
    s += f'<text x="{cx}" y="{cy+54}" font-family="Arial,sans-serif" font-size="10.5" fill="#854d0e" text-anchor="middle">Hayvanlar, Bitkiler, Tüm Canlılar</text>'

    s += f'<circle cx="{cx}" cy="{cy}" r="33" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>'
    s += f'<text x="{cx}" y="{cy-3}" font-family="Arial,sans-serif" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">1. İNSAN</text>'
    s += f'<text x="{cx}" y="{cy+11}" font-family="Arial,sans-serif" font-size="9.5" fill="#991b1b" text-anchor="middle">(Antroposentrizm)</text>'

    # Sağ taraf açıklama kutuları
    s += _kutu(345, 52, 375, 68, "#fef2f2", "#ef4444", "Araçsal Değer Anlayışı (İnsan Merkezci)", [
        "Yalnızca insan öznel ve mutlak değere sahiptir.",
        "Doğa, insanın ihtiyaçları için bir 'kaynak / araç'tır."
    ], "#991b1b")
    s += _kutu(345, 130, 375, 68, "#fefce8", "#eab308", "Yaşama Saygı İlkesi (Canlı Merkezci)", [
        "Canlı olan her varlık kendinde (içsel) değere sahiptir.",
        "Albert Schweitzer ve Paul Taylor öncülük etmiştir."
    ], "#854d0e")
    s += _kutu(345, 208, 375, 68, "#f0fdf4", "#22c55e", "Bütüncül Doğa Etiği (Çevre Merkezci)", [
        "Canlı ve cansız tüm biyosfer ahlaki özne kabul edilir.",
        "Aldo Leopold (Toprak Etiği) ve Arne Naess (Derin Ekoloji)."
    ], "#14532d")
    return _svg(g, y, s)


def gorsel_2():
    """Üç Temel Çevre Etiği Yaklaşımının Karşılaştırması"""
    g, y = 740, 275
    s = _baslik(g, "ÜÇ TEMEL ÇEVRE ETİĞİ YAKLAŞIMININ KARŞILAŞTIRMASI", "#0f766e")
    s += _kutu(18, 52, 228, 206, "#fff1f2", "#f43f5e", "1. ANTROPOSENTRİZM", [
        "Merkez: Yalnızca İNSAN",
        "Doğanın Değeri: Araçsal değer",
        "Doğa Anlayışı: Mekanik / Hammadde",
        "Çevre Koruma Gerekçesi:",
        "'Doğa bozulursa insan zarar görür'",
        "(Aydınlanma sonrası modern görüş)"
    ], "#be123c")
    s += _kutu(256, 52, 228, 206, "#fefce8", "#eab308", "2. BİYOSENTRİZM", [
        "Merkez: TÜM CANLILAR",
        "Doğanın Değeri: Canlılarda içsel değer",
        "Temel İlke: Yaşama Saygı Etiği",
        "Temsilciler: A. Schweitzer, P. Taylor",
        "Görüş: 'İnsan doğanın efendisi değil,",
        "yaşam topluluğunun bir üyesidir.'"
    ], "#a16207")
    s += _kutu(494, 52, 228, 206, "#ecfdf5", "#10b981", "3. EKOSENTRİZM", [
        "Merkez: TÜM EKOSİSTEM",
        "Doğanın Değeri: Bütüncül içsel değer",
        "Kapsam: Canlılar + Toprak, Su, Hava",
        "Temsilciler: A. Leopold, Arne Naess",
        "Görüş: 'Yeryüzü bir mülk değil,",
        "ait olduğumuz bir topluluktur.'"
    ], "#047857")
    return _svg(g, y, s)


def gorsel_3():
    """Sığ Ekoloji ve Derin Ekoloji (Arne Naess) Karşılaştırması"""
    g, y = 740, 260
    s = _baslik(g, "ARNE NAESS: SIĞ EKOLOJİ VE DERİN EKOLOJİ AYRIMI", "#1d4ed8")
    s += _kutu(20, 52, 340, 192, "#eff6ff", "#3b82f6", "SIĞ (YÜZEYSEL) EKOLOJİ", [
        "• Antroposentrik (insan merkezci) temellidir.",
        "• Kirlilik ve kaynak tükenmesiyle mücadele eder;",
        "  ancak amacı 'insanın refahını korumak'tır.",
        "• Doğayı hâlâ ekonomik bir sermaye olarak görür.",
        "• Sorunların kök nedenine (tüketim kültürüne) inmez,",
        "  yalnızca geçici teknik çözümler üretir."
    ], "#1e40af")
    s += _kutu(380, 52, 340, 192, "#f0fdf4", "#16a34a", "DERİN EKOLOJİ (Arne Naess)", [
        "• Ekosentrik (çevre merkezci) temellidir.",
        "• Doğadaki her varlık insan yararına bakılmaksızın",
        "  kendi başına yaşama ve gelişme hakkına sahiptir.",
        "• Biyoçeşitliliği ve ortak yaşamı (simbiyoz) savunur.",
        "• Endüstriyel tüketim ideolojisinin kökten değişmesini",
        "  ve 'ekolojik benlik' bilincini şart koşar."
    ], "#15803d")
    return _svg(g, y, s)


def gorsel_4():
    """Hans Jonas: Gelecek Nesillere Karşı Sorumluluk Etiği ve Ekolojik Buyruk"""
    g, y = 740, 250
    s = _baslik(g, "HANS JONAS VE GELECEK NESİLLERE KARŞI SORUMLULUK ETİĞİ", "#6d28d9")
    s += _kutu(20, 52, 335, 180, "#f5f3ff", "#8b5cf6", "Geleneksel Etikten Farkı", [
        "• Geleneksel etik yalnızca 'şimdi ve burada'",
        "  yaşayan insanlar arasındaki ilişkiyi düzenlerdi.",
        "• Modern teknoloji ise gezegenin geleceğini",
        "  ve henüz doğmamış kuşakları tehdit etmektedir.",
        "• Bu yüzden etik, geleceği de kapsamak zorundadır."
    ], "#5b21b6")
    s += _kutu(385, 52, 335, 180, "#fdf4ff", "#d946ef", "Ekolojik Koşulsuz Buyruk (Hans Jonas)", [
        "\"Öyle hareket et ki, eylemlerinin sonuçları",
        "yeryüzünde gerçek insan yaşamının",
        "sürekliliği ve doğanın bütünlüğü ile",
        "uyumlu olsun!\"",
        "• Doğa bize miras değil, gelecek nesillerin emanetidir."
    ], "#86198f")
    return _svg(g, y, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for k, sv in GORSELLER.items():
        idx = int(k[1:]) - 1
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = sv
    return v