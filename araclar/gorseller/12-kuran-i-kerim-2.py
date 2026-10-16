# -*- coding: utf-8 -*-
"""12. Sınıf Kur'an-ı Kerim — 2. Hafta SVG Görselleri"""

RENK = {
    "kirmizi": "#e63946",
    "mavi": "#2563eb",
    "yesil": "#16a34a",
    "turuncu": "#ea580c",
    "mor": "#7c3aed",
    "lacivert": "#1e293b",
    "acik_mavi": "#eff6ff",
    "acik_yesil": "#f0fdf4",
    "acik_turuncu": "#fff7ed",
    "acik_mor": "#f5f3ff",
    "acik_kirmizi": "#fef2f2",
    "gri": "#64748b",
    "acik_gri": "#f8fafc",
    "cizgi": "#cbd5e1",
}


def _baslik(W, H, etiket, baslik_metni, renk):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px; font-family:\'Inter\', \'Segoe UI\', sans-serif;">'
        f'<rect width="{W}" height="{H}" rx="14" fill="{RENK["acik_gri"]}" stroke="{RENK["cizgi"]}" stroke-width="1.5"/>'
        f'<rect x="16" y="14" width="110" height="24" rx="6" fill="{renk}"/>'
        f'<text x="71" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{etiket}</text>'
        f'<text x="138" y="31" font-size="15" font-weight="700" fill="{RENK["lacivert"]}">{baslik_metni}</text>'
        f'<line x1="16" y1="48" x2="{W-16}" y2="48" stroke="{RENK["cizgi"]}" stroke-width="1"/>'
    )


def gorsel_1():
    """Tercüme, Meal ve Tefsir Kavramları"""
    W, H = 720, 320
    s = _baslik(W, H, "KAVRAMLAR", "Tercüme (Harfî/Tefsirî), Meal ve Tefsir Farkı", RENK["mavi"])
    cols = [
        ("TERCÜME", "Bir dilden başka dile çeviri", [
            "• Harfî (Lafzî) Tercüme: Kelimesi",
            "  kelimesine birebir çeviri (Kur'an",
            "  için anlam kaybına yol açar).",
            "• Tefsirî (Manevî) Tercüme: Deyim",
            "  ve bağlamı gözeterek anlamı",
            "  aktaran çeviri yöntemi.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("MEAL", "Yaklaşık anlam çevirisi", [
            "• Sözlükte: 'Bir şeyin varacağı",
            "  yer, öz ve hülâsa' demektir.",
            "• Kur'an ayetlerinin başka bir",
            "  dile yaklaşık anlamla aktarımıdır.",
            "• Hiçbir meal Kur'an'ın Arapça",
            "  aslının yerini tutamaz.",
        ], RENK["yesil"], RENK["acik_yesil"]),
        ("TEFSİR", "Ayrıntılı açıklama ve yorum", [
            "• Sözlükte: 'Açıklamak, örtüyü",
            "  kaldırmak, beyan etmek' demektir.",
            "• Ayetleri nüzul sebebi, dil ve",
            "  hüküm yönüyle genişçe açıklar.",
            "• İlk müfessir bizzat Hz.",
            "  Muhammed'dir (sav).",
        ], RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (t, sub, items, rk, ark) in enumerate(cols):
        x = 20 + i * 230
        y = 64
        s += f'<rect x="{x}" y="{y}" width="218" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="218" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+109}" y="{y+22}" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{t}</text>'
        s += f'<text x="{x+109}" y="{y+54}" text-anchor="middle" font-size="11" font-weight="700" fill="{rk}">{sub}</text>'
        for j, it in enumerate(items):
            s += f'<text x="{x+12}" y="{y+82 + j*24}" font-size="11" fill="{RENK["lacivert"]}">{it}</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Rivayet ve Dirayet Tefsiri Karşılaştırması"""
    W, H = 720, 320
    s = _baslik(W, H, "TEFSİR ÇEŞİTLERİ", "Rivayet (Naklî) Tefsiri ve Dirayet (Aklî) Tefsiri", RENK["yesil"])
    boxes = [
        ("RİVAYET (ME'SÛR) TEFSİRİ", "Nakle Dayalı Tefsir Yöntemi", [
            "• Kur'an'ın Kur'an ile tefsir edilmesini esas alır.",
            "• Hz. Peygamber'in sünnetine ve açıklamalarına dayanır.",
            "• Sahabe ve tâbiin âlimlerinin nakillerini kullanır.",
            "• Örnek: Taberî, İbn Kesîr tefsirleri.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("DİRAYET (RE'Y / İÇTİHAT) TEFSİRİ", "Rivayet + Dil, Akıl ve Bilim Verileri", [
            "• Rivayet kaynaklarının yanında Arap dili ve edebiyatı,",
            "  mantık, fıkıh, kelam ve müspet bilimlerden yararlanır.",
            "• Ayetlerin hikmetlerini ve inceliklerini tefekkür eder.",
            "• Örnek: Fahreddin er-Râzî, Beyzâvî, Elmalılı Hamdi Yazır.",
        ], RENK["yesil"], RENK["acik_yesil"]),
    ]
    for i, (b, alt, maddeler, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+60}" font-size="11.5" font-weight="700" fill="{rk}">{alt}</text>'
        for j, m in enumerate(maddeler):
            s += f'<text x="{x+16}" y="{y+92 + j*30}" font-size="11.2" fill="{RENK["lacivert"]}">{m}</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """Meal ve Tefsirlerden Yararlanma İlkeleri"""
    W, H = 720, 330
    s = _baslik(W, H, "YÖNTEM İLKELERİ", "Meal ve Tefsir Okurken Dikkat Edilecek Temel İlkeler", RENK["turuncu"])
    ilkeler = [
        ("1. Konu Bütünlüğü", "Ayetleri tek başına değil, sure içi ve Kur'an bütünlüğü içinde okumak", RENK["mavi"], RENK["acik_mavi"]),
        ("2. Nüzul Sebebi ve Ortamı", "Ayetlerin indirildiği tarihsel ortamı ve sebeb-i nüzulü dikkate almak", RENK["yesil"], RENK["acik_yesil"]),
        ("3. Sünnet Rehberliği", "Hz. Peygamber'in ayetleri nasıl açıkladığına ve uyguladığına başvurmak", RENK["mor"], RENK["acik_mor"]),
        ("4. Karşılaştırmalı Okuma", "Tek bir meale bağlı kalmayıp güvenilir tefsir ve farklı meallere bakmak", RENK["turuncu"], RENK["acik_turuncu"]),
        ("5. Muhkem - Müteşabih", "Yoruma açık (müteşabih) ayetleri açık hükümlü (muhkem) ayetlerle anlamak", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (ad, acik, rk, ark) in enumerate(ilkeler):
        y = 60 + i * 51
        s += f'<rect x="24" y="{y}" width="672" height="43" rx="8" fill="{ark}" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="185" height="43" rx="8" fill="{rk}"/>'
        s += f'<text x="116" y="{y+26}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="224" y="{y+26}" font-size="11.8" font-weight="600" fill="{RENK["lacivert"]}">{acik}</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """Ülü'l-Azm Peygamberler ve İmran Ailesi (Hz. Meryem)"""
    W, H = 720, 320
    s = _baslik(W, H, "ÜLÜ'L-AZM", "Beş Ülü'l-Azm Peygamber ve İmran Ailesi", RENK["mor"])
    peyg = [
        ("Hz. Nuh (as)", RENK["mavi"]),
        ("Hz. İbrahim (as)", RENK["yesil"]),
        ("Hz. Musa (as)", RENK["turuncu"]),
        ("Hz. İsa (as)", RENK["mor"]),
        ("Hz. Muhammed (sav)", RENK["kirmizi"]),
    ]
    for i, (p, rk) in enumerate(peyg):
        x = 20 + i * 138
        s += f'<rect x="{x}" y="62" width="128" height="44" rx="8" fill="{rk}"/>'
        s += f'<text x="{x+64}" y="89" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{p}</text>'

    s += f'<rect x="20" y="122" width="680" height="180" rx="10" fill="#fff" stroke="{RENK["mor"]}" stroke-width="1.8"/>'
    s += f'<text x="360" y="148" text-anchor="middle" font-size="14" font-weight="800" fill="{RENK["mor"]}">İmran Ailesi ve Hz. Meryem\'in Seçkinliği (Âl-i İmrân Suresi)</text>'
    adimlar = [
        ("1. Hanne'nin Adak (Nezir) Duası", "İmran'ın eşi Hanne, karnındaki bebeği Beytülmakdis'e hizmet için Allah'a adadı."),
        ("2. Hz. Zekeriyya'nın (as) Himayesi", "Kız olarak doğan Hz. Meryem, teyzesinin eşi Peygamber Hz. Zekeriyya'nın bakımında yetişti."),
        ("3. İffet ve İbadet Örneği", "Mihrapta ibadetle meşgul olan Hz. Meryem'e Allah katından rızıklar ikram edildi."),
        ("4. İlahi Müjde (Kelimetullah)", "Melekler Hz. Meryem'e babasız olarak dünyaya gelecek 'Mesih İsa'yı müjdeledi."),
    ]
    for i, (k, v) in enumerate(adimlar):
        yy = 178 + i * 30
        s += f'<text x="38" y="{yy}" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">{k}:</text>'
        s += f'<text x="255" y="{yy}" font-size="11.2" fill="{RENK["gri"]}">{v}</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """Hz. İsa'nın (as) Mucizeleri, Tebliği ve Havariler"""
    W, H = 720, 320
    s = _baslik(W, H, "HZ. İSA (AS)", "Hz. İsa'nın Mucizeleri, İncil, Havariler ve 'Ahmet' Müjdesi", RENK["lacivert"])
    cards = [
        ("Babasız Doğum & Beşikte Konuşma", "Hz. Âdem gibi 'Ol!' (Kün) emriyle babasız yaratıldı; beşikteyken 'Ben Allah'ın kuluyum, bana kitap verdi' diyerek annesini temize çıkardı.", RENK["mavi"], RENK["acik_mavi"]),
        ("Allah'ın İzniyle Gösterdiği Mucizeler", "Çamurdan kuş şekli yapıp üfleyince canlanması, doğuştan kör olanları ve alaca (cüzzam) hastalarını iyileştirmesi, ölüleri diriltmesi.", RENK["yesil"], RENK["acik_yesil"]),
        ("İncil ve 'Ahmet' Müjdesi (Saf 6)", "Tevrat'ı doğrulayıcı olarak İncil verildi; kendisinden sonra gelecek ismi 'Ahmet' (Hz. Muhammed) olan son peygamberi müjdeledi.", RENK["turuncu"], RENK["acik_turuncu"]),
        ("Havariler (Ensârullah)", "'Allah yolunda kim bana yardımcı olacak?' çağrısına 'Allah yolunun yardımcıları biziz!' diyerek iman eden 12 samimi dostu.", RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (title, desc, rk, ark) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 22 + col * 344
        y = 64 + row * 124
        s += f'<rect x="{x}" y="{y}" width="332" height="110" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="{x+16}" y="{y+26}" font-size="12.5" font-weight="800" fill="{rk}">{title}</text>'
        # split desc into 3 lines roughly
        words = desc.split()
        l1 = " ".join(words[:7])
        l2 = " ".join(words[7:14])
        l3 = " ".join(words[14:])
        s += f'<text x="{x+16}" y="{y+52}" font-size="11" fill="{RENK["lacivert"]}">{l1}</text>'
        s += f'<text x="{x+16}" y="{y+72}" font-size="11" fill="{RENK["lacivert"]}">{l2}</text>'
        s += f'<text x="{x+16}" y="{y+92}" font-size="11" fill="{RENK["lacivert"]}">{l3}</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """Kur'an'da Hz. İsa İnancı vs Hristiyanlıktaki Teslis ve İnciller"""
    W, H = 720, 320
    s = _baslik(W, H, "KARŞILAŞTIRMA", "Kur'an'da Hz. İsa ve Hristiyanlıkta Ortaya Çıkan İnanç Farklılıkları", RENK["kirmizi"])
    boxes = [
        ("Kur'an-ı Kerim'e Göre Hz. İsa (as)", "Tevhit İnancı ve Peygamberlik", [
            "• Hz. İsa Allah'ın kulu ve seçkin elçisidir (ilah değildir).",
            "• Çarmıha gerilmemiş ve öldürülmemiştir; Allah onu",
            "  kendi katına yükseltmiştir (Nisâ suresi, 157–158).",
            "• İnsanlara yalnızca 'Rabbim ve Rabbiniz olan Allah'a",
            "  kulluk edin' (Mâide, 117) çağrısında bulunmuştur.",
        ], RENK["yesil"], RENK["acik_yesil"]),
        ("Tarihsel Süreçte Değişen Hristiyanlık İnancı", "Pavlus, Teslis ve Dört İncil", [
            "• Pavlus'un yorumlarıyla tevhit inancı bozulmuş;",
            "  Baba-Oğul-Kutsal Ruh üçlemesi (teslis) doğmuştur.",
            "• İznik (325) ve İstanbul (381) konsillerinde",
            "  Matta, Markos, Luka ve Yuhanna İncilleri seçilmiştir.",
            "• Hz. İsa'yı peygamber kabul eden Barnaba İncili reddedilmiştir.",
        ], RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (b, alt, maddeler, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+60}" font-size="11.5" font-weight="700" fill="{rk}">{alt}</text>'
        for j, m in enumerate(maddeler):
            s += f'<text x="{x+16}" y="{y+88 + j*28}" font-size="11" fill="{RENK["lacivert"]}">{m}</text>'
    s += "</svg>"
    return s


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
    "b5": gorsel_5(),
    "b6": gorsel_6(),
}



def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4", "b5", "b6"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
