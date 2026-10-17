# -*- coding: utf-8 -*-
"""7. Sınıf Arapça — 5. Hafta Görselleri (1. Ünite: Meslekler - 3. Ders: Hayalim / Hulmî)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">3. Ders: Hayalim (Hulmî) — Yeni Meslekler ve Hedefler</text>',
        _kart(25, 50, 225, 215, "Havacılık, Uzay ve Bilim", [
            "• Tayyârun / Tayyâratün (Pilot)",
            "• Râidü fadâin (Astronot)",
            "• Âlimün / Âlimetün (Bilim insanı)",
            "• Mübarmicün (Yazılımcı / Programcı)",
            "• Muhteri'un (Mucit)",
            "• fi'l-Mustakbel (Gelecekte)"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "Medya, Hukuk ve Güvenlik", [
            "• Sahafiyyün / Sahafiyyetün (Gazeteci)",
            "• Müzî'un / Müzî'atün (Spiker/Sunucu)",
            "• Muhâmin / Muhâmiyetün (Avukat)",
            "• Kâdî / Kâdiyetün (Hâkim)",
            "• Şurtiyyün / Şurtiyyetün (Polis)",
            "• İtfâiyyün (İtfaiyeci)"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "Sanat, Spor ve Mimarlık", [
            "• Mi'mâriyyün (Mimar)",
            "• Rassâmün / Rassâmetün (Ressam)",
            "• Kâtibün / Kâtibetün (Yazar)",
            "• Riyâdiyyün (Sporcu)",
            "• Lâ'ibü kürati'l-kadem (Futbolcu)",
            "• Saydeliyyün (Eczacı)"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Gelecekteki Hayalini İfade Etme Kalıpları</text>',
        _kart(30, 50, 335, 215, "1. Hulmî en Ekûne... (Hayalim ... Olmak)", [
            "• Soru: Mâ huve hulmüke fi'l-mustakbel?",
            "  (Gelecekteki hayalin nedir? - Erkek)",
            "• Soru: Mâ huve hulmüki fi'l-mustakbel?",
            "  (Gelecekteki hayalin nedir? - Kız)",
            "• Cevap: Hulmî en ekûne tayyâran!",
            "  (Hayalim pilot olmaktır!)"
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "2. Ürîdü en Ekûne / Etemennâ en...", [
            "• Ürîdü en ekûne... (... olmak istiyorum)",
            "  Örnek: Ürîdü en ekûne tabîbeten.",
            "• Etemennâ en üsbiha... (... olmayı diliyorum)",
            "  Örnek: Etemennâ en üsbiha mühendisen.",
            "• Se-ekûnü / Se-üsbihu (... olacağım)",
            "  Örnek: Se-ekûnü âlimen fi'l-mustakbel."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Meslek Seçiminin Sebebini Açıklama: Li-ennenî ve Li-key</text>',
        _kart(30, 50, 335, 215, "Li-ennenî... (Çünkü Ben...)", [
            "• Soru: Limâzâ türîdü en tekûne tabîben?",
            "  (Neden doktor olmak istiyorsun?)",
            "• Cevap: Li-ennenî uhibbü müsâ'adete'l-merdâ.",
            "  (Çünkü ben hastalara yardım etmeyi seviyorum.)",
            "• Örnek: Li-ennenî uhibbü't-tayerâne.",
            "  (Çünkü ben uçmayı seviyorum.)"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Li-key / Li-... (-mek İçin / Amacıyla)", [
            "• Li-key üâlice'l-merdâ (Hastaları tedavi etmek için)",
            "• Li-key üallime'l-etfâle (Çocuklara öğretmek için)",
            "• Li-key üdâfi'a ani'l-mazlûmîn",
            "  (Mazlumları savunmak için - Avukat)",
            "• Li-key ehdime vatanî (Vatanıma hizmet için)",
            "• Sebep ve amaç cümleleri anlatımı zenginleştirir."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hikmetli Söz: Çalışmak ve İşi En Güzel Şekilde Yapmak (İtkân)</text>',
        _kart(30, 50, 335, 195, "Men Cedde Vecede (Çalışan Kazanır)", [
            "• Arapça Atasözü: 'Men cedde vecede,",
            "  ve men zera'a hasade.'",
            "• Anlamı: 'Ciddiyetle çalışan aradığını bulur;",
            "  tohum eken de hasat biçer.'",
            "• Hayallere ulaşmanın yolu gayret ve sabırdır."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "İnnallâhe Yuhibbü İzâ Amile... (Hadis)", [
            "• 'Şüphesiz Allah, sizden birinizin yaptığı",
            "  işi sağlam ve en güzel şekilde (itkân ile)",
            "  yapmasını sever.' (Hadis-i Şerif)",
            "• Hangi mesleği seçersek seçelim, işimizi",
            "  dürüst ve özenli yapmak ibadet bilincidir."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
