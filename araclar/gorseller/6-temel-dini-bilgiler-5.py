# -*- coding: utf-8 -*-
"""6. Sınıf Temel Dini Bilgiler — 5. Hafta Görselleri (Mümin Kimliğim: İman-Amel Bütünlüğü ve Şehadet Bilinci)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mümin Kimliğinin Kurucu İlkeleri: Tevhid ve Şehadet Bilinci</text>',
        _kart(30, 50, 335, 215, "Kelime-i Tevhid ve İhlas", [
            "• 'Lâ ilâhe illallâh, Muhammedün Rasûlullâh.'",
            "• İhlas suresinde bildirildiği üzere Allah'ı",
            "  Ehad (tek) ve Samed (hiçbir şeye muhtaç",
            "  olmayan, her şeyin kendisine muhtaç olduğu)",
            "  olarak tanımak mümin kimliğinin temelidir.",
            "• Tevhid insanı yalnızca Allah'a kul yapar."
        ], "#0284c7", "#f0f9ff"),
        _kart(395, 50, 335, 215, "Kelime-i Şehadet ve Risalet", [
            "• 'Eşhedü en lâ ilâhe illallâh ve eşhedü",
            "  enne Muhammeden abdühû ve rasûlüh.'",
            "• Allah'ın birliğine ve Hz. Muhammed'in (sav)",
            "  önce kul, sonra elçi olduğuna şahitliktir.",
            "• Kalp ile tasdik (onaylama) ve dil ile",
            "  ikrar (söyleme) birleştiğinde iman tam olur."
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">İman ve Salih Amel Bütünlüğü: Ağaç Metaforu</text>',
        _kart(25, 50, 225, 215, "1. Kök: Kalpteki İman", [
            "• Ağacın toprağın altındaki sağlam",
            "  kökü, kalpteki sarsılmaz imandır.",
            "• İman esaslarının (Âmentü)",
            "  tamamına şüphe duymadan",
            "  bütüncül olarak inanılır.",
            "• Kök ne kadar derinse ağaç o kadar güçlüdür."
        ], "#8b5cf6", "#f5f3ff"),
        _kart(267, 50, 225, 215, "2. Gövde ve Dal: İbadetler", [
            "• Ağacın gövdesi ve dalları,",
            "  namaz, oruç, zekât ve dua gibi",
            "  temel ibadetlerdir.",
            "• İbadetler kalpteki imanı korur,",
            "  canlı tutar ve Allah ile bağı",
            "  her gün güçlendirir."
        ], "#2563eb", "#eff6ff"),
        _kart(510, 50, 225, 215, "3. Meyve: Güzel Ahlak", [
            "• Ağacın insanlara fayda veren",
            "  tatlı meyveleri, salih ameller",
            "  ve güzel ahlaktır.",
            "• Doğruluk, adalet, merhamet,",
            "  yardımlaşma ve emanet bilinci",
            "  iman ağacının meyveleridir."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'de Müminlerin Temel Özellikleri (Enfâl 2-4 ve Mü\'minûn 1-11)</text>',
        _kart(30, 50, 335, 215, "İç Dünyadaki ve İbadetteki Duruş", [
            "• Allah anıldığı zaman kalpleri titrer (saygı).",
            "• Allah'ın ayetleri okunduğunda imanları artar.",
            "• Yalnızca Rablerine tevekkül ederler (güvenirler).",
            "• Namazlarını huşû (derin saygı ve dikkat)",
            "  içinde ve vakitlerini koruyarak kılarlar.",
            "• Boş ve anlamsız işlerden yüz çevirirler."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Toplumsal Hayattaki Ahlaki Duruş", [
            "• Kendilerine verilen rızıktan infak ederler",
            "  (zekât ve sadaka verip paylaşırlar).",
            "• Emanetlerine ve verdikleri sözlere (ahitlerine)",
            "  titizlikle riayet ederler, hıyanet etmezler.",
            "• İffetlerini ve onurlarını korurlar.",
            "• İyiliği emredip kötülükten sakındırırlar."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Asr Suresi Işığında Mümin Kimliğinin 4 Altın İlkesi</text>',
        _kart(30, 50, 335, 195, "1. İman ve 2. Salih Amel (Bireysel Boyut)", [
            "• 1. İman Etmek: Tevhid ve risalet bilinciyle",
            "  Allah'a ve getirdiği hakikatlere inanmak.",
            "• 2. Salih Amel İşlemek: Allah'ın rızasına",
            "  uygun, hem kendine hem de insanlığa",
            "  faydalı güzel işler ve ibadetler yapmak."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "3. Hakkı ve 4. Sabrı Tavsiye (Toplumsal Boyut)", [
            "• 3. Birbirine Hakkı Tavsiye Etmek: Doğruluğu,",
            "  adaleti ve iyiliği çevresiyle paylaşmak.",
            "• 4. Birbirine Sabrı Tavsiye Etmek: Zorluklar",
            "  karşısında dayanışmak ve metanetli olmak.",
            "• Bu 4 ilke insanı ziyandan (zarardan) kurtarır."
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
