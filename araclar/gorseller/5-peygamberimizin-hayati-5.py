# -*- coding: utf-8 -*-
"""5. Sınıf Peygamberimizin Hayatı — 5. Hafta Görselleri (Peygamberimizin Çocukluğu: Sütanneye Verilmesi)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Peygamberimizi Emziren İlk Kişiler ve Sütanne Geleneği</text>',
        _kart(25, 50, 225, 215, "1. Annesi Hz. Âmine", [
            "• Peygamberimizi dünyaya geldikten",
            "  sonra ilk olarak öz annesi",
            "  Hz. Âmine bir süre emzirmiştir.",
            "• Şefkat ve merhametle yavrusunu",
            "  bağrına basmıştır.",
            "• Babası Hz. Abdullah vefat etmişti."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Süveybe Hatun", [
            "• Amcası Ebû Leheb'in cariyesi olan",
            "  Süveybe Hatun, Hz. Âmine'den",
            "  sonra Peygamberimizi emzirmiştir.",
            "• Peygamberimiz ve Hz. Hatice hayatları",
            "  boyunca Süveybe Hatun'a vefa",
            "  gösterip iyilikte bulunmuşlardır."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Sütanne Hz. Halîme", [
            "• Tâif yakınlarındaki Benî Sa'd",
            "  yurdundan gelen Hz. Halîme,",
            "  Peygamberimizin sütannesi olmuştur.",
            "• Peygamberimiz yaklaşık 4 yaşına",
            "  kadar Hz. Halîme'nin ailesinin",
            "  yanında sağlıklı şekilde büyümüştür."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mekke Aileleri Çocuklarını Neden Sütanneye Verirdi?</text>',
        _kart(30, 50, 335, 215, "1. Sağlıklı İklim ve Doğal Yaşam", [
            "• Mekke şehri çukur bir vadide yer aldığı",
            "  için havası çok sıcak ve bunaltıcıydı.",
            "• Bebeklerin salgın hastalıklardan korunması",
            "  ve yayla havasında gürbüz büyümesi",
            "  için kırsal bölgeler tercih edilirdi.",
            "• Doğa ile iç içe özgürce hareket ederlerdi."
        ], "#d97706", "#fffbeb"),
        _kart(395, 50, 335, 215, "2. Fasih (Duru) Arapça Öğrenme", [
            "• Mekke bir ticaret ve hac merkezi olduğu",
            "  için dışarıdan gelenlerle dil karışabiliyordu.",
            "• Benî Sa'd kabilesi ise Arapçayı en saf,",
            "  en fasih (duru ve düzgün) konuşan kabileydi.",
            "• Çocuklar ana dillerini en güzel ve",
            "  etkili şekilde bu yurtlarda öğrenirlerdi."
        ], "#2563eb", "#eff6ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Benî Sa\'d Yurdunda Peygamberimizin Süt Ailesi ve Bereket</text>',
        _kart(30, 50, 335, 215, "Peygamberimizin Süt Ailesi", [
            "• Sütannesi: Hz. Halîme (Halîme bint Ebî Züeyb)",
            "• Sütbabası: Hâris bin Abdüluzzâ",
            "• Sütkardeşleri: Abdullah, Üneyse ve",
            "  Şeymâ (Huzâfe) — ayrıca amcası Hz. Hamza",
            "  da hem Süveybe hem Halîme'den sütkardeşidir.",
            "• Şeymâ, Peygamberimize bakıcılık da yapmıştır."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Hz. Halîme'nin Evine Gelen Bereket", [
            "• Kuraklık yılı olmasına rağmen Peygamberimizin",
            "  gelişiyle Hz. Halîme'nin ailesi bolluğa kavuştu.",
            "• Zayıf binek hayvanları güçlendi, koyunlarının",
            "  sütü bereketlendi ve evlerine huzur doldu.",
            "• Sütkardeşleriyle sevgi, paylaşma ve",
            "  yardımlaşma içinde mutlu bir çocukluk geçirdi."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Peygamberimizin Süt Ailesine Ömür Boyu Vefası</text>',
        _kart(30, 50, 335, 195, "Hz. Halîme'ye Gösterilen Saygı", [
            "• Peygamberimiz büyüyüp evlendikten ve",
            "  peygamber olduktan sonra da sütannesini unutmadı.",
            "• Hz. Halîme ziyarete geldiğinde 'Anneciğim!'",
            "  diyerek ayağa kalkar, cübbesini yere serer",
            "  ve ihtiyaçlarını cömertçe karşılardı."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Sütkardeşi Şeymâ'ya Vefası", [
            "• Yıllar sonra Huneyn Savaşı sonrasında",
            "  sütkardeşi Şeymâ huzuruna geldiğinde",
            "  onu sevgiyle karşılayıp ikramda bulundu.",
            "• Bu örnek davranışlar bize aile büyüklerine",
            "  ve üzerimizde emeği olanlara vefayı öğretir."
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
