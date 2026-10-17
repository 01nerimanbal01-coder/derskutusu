# -*- coding: utf-8 -*-
"""8. Sınıf Din Kültürü ve Ahlak Bilgisi — 5. Hafta Görselleri (Kaderle İlgili Kavramlar: Rızık, Tevekkül, Başarı, Sağlık)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Kaderle İlgili Kavramlar: Ömür, Ecel, Rızık ve Emek</text>',
        _kart(30, 50, 335, 215, "Ömür ve Ecel", [
            "• Ömür: İnsanın ve canlıların doğumundan",
            "  ölümüne kadar geçen yaşam süresidir.",
            "• Ecel: Ömrün bittiği, hayatın sona erdiği",
            "  andır (Her can ölümü tadacaktır - Enbiyâ, 35).",
            "• İnsanın görevi ömrünü ibadet, salih amel,",
            "  sağlığını koruma ve faydalı işlerle geçirmektir."
        ], "#0284c7", "#f0f9ff"),
        _kart(395, 50, 335, 215, "Rızık (er-Rezzâk) ve Helal Kazanç", [
            "• Rızık: Allah'ın tüm canlılar için yarattığı",
            "  maddi ve manevi her türlü nimettir.",
            "• er-Rezzâk: Rızkı yaratan ve veren yalnız Allah'tır.",
            "• Ancak rızka ulaşmak için çalışmak ve",
            "  emek harcamak insanın iradesine bağlıdır:",
            "  'İnsan için ancak çalıştığının karşılığı vardır' (Necm, 39)."
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Başarı - Başarısızlık ve Sağlık - Hastalık Kavramları</text>',
        _kart(30, 50, 335, 215, "Başarı ve Başarısızlık", [
            "• Başarı tesadüf değildir; hedef belirleme,",
            "  planlı çalışma ve azmin sonucudur.",
            "• Tembellik yapıp başarısızlığı 'Kaderim",
            "  böyleymiş' diyerek kadere yüklemek yanlıştır!",
            "• Başarıda şükretmek, başarısızlıkta ise",
            "  hataları düzeltip yeniden çalışmak esastır."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Sağlık ve Hastalık", [
            "• Sağlık, Allah'ın insana verdiği en büyük",
            "  emanettir; temizlik, dengeli beslenme ve",
            "  zararlı alışkanlıklardan kaçınmakla korunur.",
            "• Hastalandığımızda sabredip doktora gitmek",
            "  ve tedavi olmak Peygamberimizin sünnetidir:",
            "  'Ey Allah'ın kulları, tedavi olunuz!' (Hadis)"
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Doğru Tevekkül Anlayışı: Önce Tedbir, Sonra Takdir!</text>',
        _kart(25, 50, 225, 215, "1. Çalışma ve Tedbir", [
            "• Bir amaca ulaşmak için",
            "  fiziksel ve biyolojik yasalara",
            "  uygun olarak bütün maddi",
            "  sebepleri yerine getirmek.",
            "• Örnek: Sınav için düzenli",
            "  ders çalışmak; deveyi bağlamak."
        ], "#8b5cf6", "#f5f3ff"),
        _kart(267, 50, 225, 215, "2. Dua ve Allah'a Güven", [
            "• Üzerine düşen tüm görevi",
            "  eksiksiz yaptıktan sonra",
            "  sonucu Yüce Allah'tan",
            "  beklemek ve O'na güvenmek.",
            "• 'Karar verdiğin zaman artık",
            "  Allah'a tevekkül et!' (Âl-i İmrân, 159)"
        ], "#0d9488", "#f0fdfa"),
        _kart(510, 50, 225, 215, "3. Yanlış (Pasif) Anlayış", [
            "• Hiç çalışmadan, tedbir almadan",
            "  'Allah'a tevekkül ettim' demek",
            "  İslam'ın tevekkül anlayışı",
            "  değildir; tembelliktir!",
            "• Hz. Peygamber: 'Önce deveni",
            "  bağla, sonra Allah'a tevekkül et!'"
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hz. Ömer\'in Şam Yolculuğu ve Karantina (Tedbir) İlkesi</text>',
        _kart(30, 50, 335, 195, "Veba Salgını Karşısında Tedbir", [
            "• Hz. Ömer, Şam'da veba salgını çıktığını",
            "  öğrenince ordusuyla şehre girmekten vazgeçti.",
            "• 'Allah'ın kaderinden mi kaçıyorsun?' sorusuna:",
            "• 'Evet, Allah'ın bir kaderinden yine Allah'ın",
            "  başka bir kaderine kaçıyoruz!' cevabını verdi."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Biyolojik ve Toplumsal Yasalara Uyum", [
            "• Salgın hastalık olan yere girmemek ve",
            "  oradan dışarı çıkmamak (karantina) tedbirdir.",
            "• Depreme dayanıklı bina yapmak, trafik",
            "  kurallarına uymak ve aşı olmak da",
            "  doğru kader ve tevekkül bilincinin gereğidir."
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
