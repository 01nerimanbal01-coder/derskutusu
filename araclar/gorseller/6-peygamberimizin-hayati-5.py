# -*- coding: utf-8 -*-
"""6. Sınıf Peygamberimizin Hayatı — 5. Hafta Görselleri (Gençlik Yıllarında Ticaret Ahlakı ve el-Emîn)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Gençlik Yıllarında Peygamberimizin Çalışma Hayatı ve Ticaret Ahlakı</text>',
        _kart(25, 50, 225, 215, "1. Alın Teri ve Emek", [
            "• Küçük yaşta amcası Ebû Tâlib'e",
            "  yük olmamak için çobanlık yaptı.",
            "• Gençliğinde amcasıyla ticaret",
            "  kervanlarına katılarak tecrübe kazandı.",
            "• Kendi elinin emeğiyle helal",
            "  rızık kazanmaya önem verdi."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Dürüst Ticaret İlkeleri", [
            "• Malın kusurunu asla gizlemedi.",
            "• Ölçü ve tartıda haksızlık yapmadı.",
            "• Söz verdiği vakitte ve yerde",
            "  borcunu ve sözünü yerine getirdi.",
            "• Alışverişte kolaylık, nezaket",
            "  ve şeffaflık ilkesini benimsedi."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Hz. Hatice İle Ortaklık", [
            "• Dürüstlüğüyle tanınınca Hz. Hatice'nin",
            "  ticaret kervanını Şam/Busra'ya götürdü.",
            "• Kervan yardımcısı Meysere onun",
            "  üstün ahlakına ve doğruluğuna şahit oldu.",
            "• Bu güven, Hz. Hatice ile mutlu",
            "  evliliğinin de temelini oluşturdu."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">el-Emîn Sıfatının Somut Örnekleri: Sözünde Durma ve Emanet</text>',
        _kart(30, 50, 335, 215, "Abdullah bin Ebi'l-Hamsâ Hatırası", [
            "• Peygamberlikten önce Peygamberimizle alışveriş",
            "  yapan Abdullah, 'Bekle, hemen geliyorum' dedi.",
            "• Ancak sözünü unutup üç gün sonra geldiğinde",
            "  Peygamberimizi aynı yerde beklerken buldu!",
            "• Peygamberimiz onu azarlamadı; sadece 'Beni",
            "  biraz yordun, üç gündür buradayım' buyurdu."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Sâib bin Ebî Sâib'in Şahitliği", [
            "• Gençliğinde Peygamberimizle ticaret ortaklığı",
            "  yapan Sâib, yıllar sonra Müslüman olduğunda:",
            "• 'O benim en hayırlı ortağımdı; ne tartışır",
            "  ne de hile ve anlaşmazlık çıkarırdı!' demiştir.",
            "• Mekkeliler en değerli emanetlerini gözleri",
            "  kapalı olarak Muhammedü'l-Emîn'e bırakırdı."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Cahiliye Kötülüklerinden Korunmuş Tertemiz Bir Gençlik</text>',
        _kart(30, 50, 335, 215, "Uzak Durduğu Yanlış Davranışlar", [
            "• Hayatının hiçbir döneminde putlara tapmadı.",
            "• İçki, kumar, fal okları ve panayır",
            "  eğlencelerindeki aşırılıklara hiç yaklaşmadı.",
            "• Yalan, hile, alay, kibir ve kaba söz",
            "  onun dilinden ve kalbinden hiç geçmedi.",
            "• Kan davalarına ve zulme asla ortak olmadı."
        ], "#e11d48", "#fff1f2"),
        _kart(395, 50, 335, 215, "Kuşandığı Yüksek Erdemler", [
            "• Sıdk (Doğruluk) ve Emânet (Güvenilirlik)",
            "• İffet ve Hayâ (Utanma duygusu ve edep)",
            "• Hilm (Yumuşak huyluluk) ve Sabır",
            "• Şecaat (Cesaret) ve Adalet (Hilfü'l-fudûl)",
            "• Cömertlik, misafirperverlik ve merhamet",
            "• Tefekkür (Hira'da kâinatı derinlemesine düşünme)"
        ], "#0d9488", "#f0fdfa"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Günümüz Gençleri İçin Peygamberimizden Ahlaki İlkeler</text>',
        _kart(30, 50, 335, 195, "Okulda ve Arkadaşlıkta Güven", [
            "• Verdiğimiz sözü zamanında tutmak.",
            "• Ödünç aldığımız eşyayı sağlam teslim etmek.",
            "• Arkadaşlarımızın sırrını emanet bilip korumak.",
            "• Sınavlarda ve ödevlerde kendi emeğimizle,",
            "  kopya ve hileden uzak başarı aramak."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Dijital Dünyada ve Sosyal Hayatta Edep", [
            "• Sosyal medyada ve oyunlarda doğru sözlü",
            "  olmak, siber zorbalıktan uzak durmak.",
            "• Haksızlığa uğrayan arkadaşımızın yanında",
            "  durup adaleti ve barışı savunmak.",
            "• Zamanımızı faydalı ilim ve sporla değerlendirmek."
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
