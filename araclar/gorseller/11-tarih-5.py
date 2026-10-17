def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">PASAROFÇA ANTLAŞMASI (1718) VE LALE DEVRİ\'NE GEÇİŞ</text>'
    ic += _kart(20, 44, 310, 190, "PASAROFÇA ANTLAŞMASI (21 TEMMUZ 1718)", [
        "• Osmanlı-Venedik-Avusturya savaşları sonunda",
        "  İngiltere ve Hollanda arabuluculuğuyla imzalandı.",
        "• Mora Yarımadası Osmanlı'da kaldı; ancak Belgrad,",
        "  Banat Yaylası ve Kuzey Sırbistan Avusturya'ya verildi.",
        "• Osmanlı Devleti, kaybettiği toprakları savaşla geri",
        "  alma politikasından vazgeçip barış siyasetine yöneldi."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "LALE DEVRİ YÖNETİMİ VE DİPLOMASİ (1718-1730)", [
        "• Dönemin Padişahı: III. Ahmed.",
        "• Dönemin Sadrazamı: Nevşehirli Damat İbrahim Paşa.",
        "• Avrupa'yı yakından tanımak için Viyana, Paris, Moskova",
        "  ve Lehistan'a İLK GEÇİCİ ELÇİLİKLER gönderildi.",
        "• Yirmisekiz Çelebi Mehmed Efendi'nin 'Paris",
        "  Sefaretnamesi' Batılılaşmada öncü rehber oldu."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">LALE DEVRİ\'NDE BİLİM, KÜLTÜR, SANAT VE SAĞLIK ISLAHATLARI</text>'
    adimlar = [
        ("1. İLK TÜRK MATBAASI (1727) — İBRAHİM MÜTEFERRİKA &amp; SAİD EFENDİ", "Şeyhülislam Yenişehirli Abdullah Efendi'nin fetvasıyla kuruldu; dini olmayan eserler basıldı (İlk eser: Vankulu Lügati, 1729).", "#059669", "#ECFDF5"),
        ("2. TERCÜME HEYETİ VE KÜTÜPHANELER", "Şair Nedim ve Yanyalı Esad Efendi'nin yer aldığı heyet Doğu ve Batı dillerinden tarih, astronomi ve felsefe eserleri çevirdi.", "#2563EB", "#EFF6FF"),
        ("3. TULUMBACILAR OCAĞI VE ÇİÇEK AŞISI", "Gerçek Davut Ağa (Davut Gerçek) tarafından Yeniçeri Ocağı bünyesinde ilk itfaiye (Tulumbacılar) kuruldu; çiçek aşısı uygulandı.", "#7C3AED", "#F5F3FF"),
        ("4. SANAYİ İMALATHANELERİ (KÂĞIT, ÇİNİ, ÇUHA)", "Yalova'da kâğıt imalathanesi, İstanbul'da kumaş/çuha atölyesi ve Tekfur Sarayı'nda çini imalathanesi açıldı.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">LALE DEVRİ\'NDE MİMARİ, EDEBİYAT VE SOSYAL HAYAT</text>'
    ic += _kart(20, 44, 310, 190, "MİMARİ VE SANAT (SİVİL MİMARİ ÖNE ÇIKTI)", [
        "• Kâğıthane'de (Sadâbâd) Fransız Versay Sarayı",
        "  örnek alınarak köşkler, kasırlar ve bahçeler yapıldı.",
        "• Sivil mimari gelişti: Sultanahmet'teki III. Ahmed",
        "  Çeşmesi ve Enderun Kütüphanesi dönemin şaheserleridir.",
        "• Minyatür sanatında Levnî, dönemin giyim-kuşam",
        "  ve eğlence kültürünü Surname-i Vehbi'de resmetti."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "EDEBİYAT VE KÜLTÜREL DEĞİŞİM", [
        "• Divan edebiyatında mahallîleşme akımının temsilcisi",
        "  Şair Nedim, şarkılarıyla dönemin ruhunu yansıttı.",
        "• 'Lale Devri' tabiri ilk kez Yahya Kemal Beyatlı",
        "  tarafından kullanılmış, tarihçi Ahmed Refik Altınay'ın",
        "  eseriyle tarih literatürüne yerleşmiştir.",
        "• Batı'dan rokoko ve barok bezeme unsurları alındı."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">LALE DEVRİ\'NİN ÖZELLİKLERİ VE PATRONA HALİL İSYANI (1730)</text>'
    ic += _kart(20, 44, 310, 190, "LALE DEVRİ ISLAHATLARININ TEMEL FARKI", [
        "• 17. yüzyıl ıslahatlarından farklı olarak İLK KEZ",
        "  Avrupa'nın bilim, teknik ve kültürü örnek alındı.",
        "• Kültür, sanat, diplomasi, basın, sağlık ve belediyecilik",
        "  alanlarında köklü yenilikler yapıldı.",
        "• ÖNEMLİ NOT: Lale Devri'nde ASKERÎ ALANDA",
        "  bir ıslahat yapılmamıştır (Askerî ıslahat I. Mahmud'ladır)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "PATRONA HALİL İSYANI (EYLÜL 1730)", [
        "• Nedenleri: İran (Safevi) savaşlarının uzaması ve",
        "  Tebriz'in kaybı, ağır vergiler, enflasyon ve Sadâbâd",
        "  eğlencelerindeki lüks ve israfa duyulan tepki.",
        "• Sonuçları: Sadrazam Damat İbrahim Paşa ve Şair Nedim",
        "  hayatını kaybetti; III. Ahmed tahttan indirildi, yerine",
        "  I. Mahmud geçti; matbaa ve teknik yeniliklere dokunulmadı."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
