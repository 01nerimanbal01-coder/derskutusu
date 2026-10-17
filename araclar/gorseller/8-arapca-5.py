# -*- coding: utf-8 -*-
"""8. Sınıf Arapça — 5. Hafta Görselleri (1. Ünite: Etkinlikler - 3. Ders: Gezi / er-Rihletü)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">3. Ders: Gezi (er-Rihletü) — Gezi Türleri ve Hazırlık Kelimeleri</text>',
        _kart(25, 50, 225, 215, "Gezi Türleri", [
            "• Rihletün medresiyyetün (Okul gezisi)",
            "• Rihletün ilmiyyetün (Bilim gezisi)",
            "• Rihletün siyâhiyyetün (Turistik gezi)",
            "• Rihletün bahriyyetün (Deniz/Gemi gezisi)",
            "• Rihletün târîhiyyetün (Tarihi gezi)",
            "• Nüzhetün (Piknik / Doğa gezintisi)"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "Gezi Mekânları", [
            "• el-Mathafü (Müze)",
            "• el-Gâbetü (Orman)",
            "• el-Cebelü (Dağ) &amp; el-Buhayratü (Göl)",
            "• el-Medînetü'l-kadîmetü (Antik şehir)",
            "• Hadîkatü'l-hayevânât (Hayvanat bahçesi)",
            "• Şâtiü'l-bahri (Deniz kıyısı / Sahil)"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "Ulaşım ve Gezi Eşyaları", [
            "• bi'l-Hâfileti (Otobüsle)",
            "• bi'l-Kitâri (Trenle) / bi's-Sefîneti (Gemiyle)",
            "• Hakîbetü's-seferi (Seyahat çantası)",
            "• Âletü't-tasvîr (Fotoğraf makinesi)",
            "• el-Harîtatü (Harita) &amp; el-Bûsalatü (Pusula)",
            "• el-Haymetü (Çadır)"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Gezide Yapılan Etkinlikler: Mâzî (Geçmiş) ve Müzâri (Şimdiki) Fiiller</text>',
        _kart(30, 50, 335, 215, "Mâzî (Geçmiş Zaman) İle Gezi Anlatımı", [
            "• Zehebnâ ile'l-mathafi (Müzeye gittik).",
            "• Rakibnâ el-hâfilete (Otobüse bindik).",
            "• Şâhednâ el-âsâre't-târîhiyye (Tarihi eserleri izledik).",
            "• İltakatnâ suveran cemîleten (Güzel fotoğraflar çektik).",
            "• Tecavvelnâ fi'l-gâbeti (Ormanda dolaştık).",
            "• Raca'nâ fi'l-mesâi (Akşamleyin döndük)."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Müzâri ve Gelecek Zaman İle Gezi Planı", [
            "• Se-nünazzimu rihleten (Bir gezi düzenleyeceğiz).",
            "• Se-nezhebü yevme's-sebti (Cumartesi günü gideceğiz).",
            "• Nezûru'l-medînete (Şehri ziyaret ediyoruz).",
            "• Nestemti'u bi'l-manzari (Manzaranın tadını çıkarıyoruz).",
            "• Nüfekkiru fî halkillâhi (Allah'ın yaratışını düşünüyoruz).",
            "• Nuhâfizu ale'l-bîeti (Çevreyi koruyoruz)."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Gezi Diyaloglarında Soru Edatları ve Zaman İfadeleri</text>',
        _kart(30, 50, 335, 215, "Soru Kalıpları", [
            "• İlâ eyne zehebtüm? (Nereye gittiniz?)",
            "• Metâ bede'eti'r-rihletü? (Gezi ne zaman başladı?)",
            "• Keyfe zehebtüm ilâ hünâke? (Oraya nasıl gittiniz?)",
            "• Mea men zehebte? (Kiminle gittin?)",
            "• Mâzâ şâhedtüm fi'r-rihleti? (Gezide ne gördünüz?)",
            "• Keyfe kâneti'r-rihletü? (Gezi nasıldı?)"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Gezi İzlenimlerini Anlatan Sıfatlar", [
            "• Kâneti'r-rihletü mümti'aten! (Gezi çok keyifliydi!)",
            "• Rihletün müfîdetün ve râi'atün (Faydalı ve harika gezi).",
            "• el-Manzaru cemîlün cidden (Manzara çok güzel).",
            "• el-Hevâü nakıyyün (Hava tertemiz).",
            "• Mesrûrun / Saîdün (Mutlu, sevinçli).",
            "• Müte'abün kalîlen (Biraz yorgun)."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Seyahat Edebi, Çevre Bilinci ve Tefekkür</text>',
        _kart(30, 50, 335, 195, "Yeryüzünde Gezip Tefekkür Etmek", [
            "• 'De ki: Yeryüzünde gezip dolaşın da Allah'ın",
            "  yaratmaya nasıl başladığına bir bakın!' (Ankebût, 20)",
            "• Gezi sadece eğlence değil; aynı zamanda yeni",
            "  bilgiler öğrenme, tarihi tanıma ve doğadaki",
            "  ilahi düzeni tefekkür etme vesilesidir."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Yolculuk Duası ve Çevre Temizliği", [
            "• Yolculuğa çıkarken binek/sefer duası okunur.",
            "• Gezi sırasında grup kurallarına uyulur ve",
            "  arkadaşlarla yardımlaşılır (et-Teâvün).",
            "• Orman ve piknik alanları temiz bırakılır:",
            "  'en-Nezâfetü mine'l-îmân' (Temizlik imandandır)."
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
