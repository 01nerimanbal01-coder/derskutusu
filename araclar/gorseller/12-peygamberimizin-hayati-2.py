# -*- coding: utf-8 -*-
"""12. Sınıf Peygamberimizin Hayatı — 2. Hafta SVG Görselleri"""

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
    """İtaat, İtisam, İttiba, Sünnet, Heva ve Bidat Kavramları"""
    W, H = 720, 320
    s = _baslik(W, H, "KAVRAMLAR", "Peygamberimize İtaat ve Bağlılıkla İlgili Temel Kavramlar", RENK["mavi"])
    cards = [
        ("İtaat &amp; İttiba", "Allah'ın ve Resulü'nün emir ve yasaklarına gönülden uymak; körü körüne taklit değil bilinçli bağlılıktır.", RENK["mavi"], RENK["acik_mavi"]),
        ("İtisam (الإعتصام)", "Günahtan korunmak; hayatı Kur'an ve sünnete göre düzenleyerek İslam'ı mutedil (dengeli) bir çizgide yaşamaktır.", RENK["yesil"], RENK["acik_yesil"]),
        ("Sünnet &amp; Hadis", "Sünnet Hz. Peygamber'in örnek uygulamaları ve yolu; hadis ise onun söz, fiil ve onaylarının (takrir) genel adıdır.", RENK["mor"], RENK["acik_mor"]),
        ("Hevâ &amp; Bid'at", "Hevâ dinî ölçüleri dikkate almadan nefsin arzusuna uymak; bid'at ise dinde sonradan uydurulan inanç ve amellerdir.", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (title, desc, rk, ark) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 22 + col * 344
        y = 64 + row * 124
        s += f'<rect x="{x}" y="{y}" width="332" height="110" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="{x+16}" y="{y+26}" font-size="13" font-weight="800" fill="{rk}">{title}</text>'
        words = desc.split()
        l1 = " ".join(words[:6])
        l2 = " ".join(words[6:12])
        l3 = " ".join(words[12:])
        s += f'<text x="{x+16}" y="{y+52}" font-size="11" fill="{RENK["lacivert"]}">{l1}</text>'
        s += f'<text x="{x+16}" y="{y+72}" font-size="11" fill="{RENK["lacivert"]}">{l2}</text>'
        s += f'<text x="{x+16}" y="{y+92}" font-size="11" fill="{RENK["lacivert"]}">{l3}</text>'
    s += "</svg>"
    return s


def gorsel_2():
    """Kur'an-ı Kerim'de Hz. Peygamber'e İtaat Ayetleri ve Nesiller"""
    W, H = 720, 320
    s = _baslik(W, H, "KUR'AN &amp; SÜNNET", "Peygamberimize İtaatin Kur'an'daki Delilleri ve İslam Nesilleri", RENK["yesil"])
    ayetler = [
        ("Nisâ, 80", "Kim Peygamber'e itaat ederse Allah'a itaat etmiş olur.", RENK["yesil"]),
        ("Âl-i İmrân, 31", "Eğer Allah'ı seviyorsanız bana uyun ki Allah da sizi sevsin.", RENK["mavi"]),
        ("Necm, 3–4", "O, kişisel arzusuna (hevâsına) göre konuşmaz.", RENK["mor"]),
        ("Nisâ, 59", "Allah'a itaat edin, Peygamber'e ve ülü'l-emre de itaat edin.", RENK["turuncu"]),
    ]
    for i, (sure, meal, rk) in enumerate(ayetler):
        y = 62 + i * 42
        s += f'<rect x="24" y="{y}" width="672" height="34" rx="7" fill="#fff" stroke="{rk}" stroke-width="1.5"/>'
        s += f'<rect x="24" y="{y}" width="135" height="34" rx="7" fill="{rk}"/>'
        s += f'<text x="91" y="{y+22}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{sure}</text>'
        s += f'<text x="175" y="{y+22}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">"{meal}"</text>'

    s += f'<rect x="24" y="236" width="672" height="66" rx="10" fill="{RENK["acik_yesil"]}" stroke="{RENK["yesil"]}" stroke-width="1.8"/>'
    s += f'<text x="360" y="258" text-anchor="middle" font-size="12.5" font-weight="800" fill="{RENK["yesil"]}">Sünneti Günümüze Taşıyan Üç Örnek Nesil</text>'
    s += f'<text x="360" y="284" text-anchor="middle" font-size="11.5" font-weight="700" fill="{RENK["lacivert"]}">1. Sahabe (Hz. Peygamber\'i gören müminler) → 2. Tâbiîn (Sahabeyi görenler) → 3. Tebeü\'t-Tâbiîn (Tâbiîni görenler)</text>'
    s += "</svg>"
    return s


def gorsel_3():
    """Sünnetin Kur'an'ı Açıklama (Beyan) ve Hüküm Koyma Görevi"""
    W, H = 720, 320
    s = _baslik(W, H, "SÜNNETİN ROLÜ", "İslam'ı Anlama ve Yaşamada Sünnetin Dört Temel İşlevi", RENK["turuncu"])
    cols = [
        ("1. Tebliğ", "Vahyi Eksiksiz İletme", "Allah'tan aldığı Kur'an ayetlerini hiçbir ekleme/çıkarma yapmadan insanlara ulaştırması.", RENK["mavi"], RENK["acik_mavi"]),
        ("2. Tebyin (Beyan)", "Mücmeli Açıklama", "Kur'an'da özetle emredilen namaz, oruç, zekât ve haccın nasıl yapılacağını uygulamalı göstermesi.", RENK["yesil"], RENK["acik_yesil"]),
        ("3. Teşri", "Hüküm Koyma", "Kur'an'da açıkça yer almayan konularda vahyin rehberliğinde helal ve haram sınırlarını belirlemesi.", RENK["mor"], RENK["acik_mor"]),
        ("4.Tezkiye &amp; İhya", "Toplumu Arındırma", "Kan davalarını bitirmesi, Evs-Hazrec barışını ve Muhacir-Ensar kardeşliğini (muâhât) kurması.", RENK["turuncu"], RENK["acik_turuncu"]),
    ]
    for i, (ad, alt, acik, rk, ark) in enumerate(cols):
        x = 20 + i * 172
        y = 64
        s += f'<rect x="{x}" y="{y}" width="160" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="160" height="34" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+80}" y="{y+22}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ad}</text>'
        s += f'<text x="{x+80}" y="{y+58}" text-anchor="middle" font-size="11" font-weight="700" fill="{rk}">{alt}</text>'
        words = acik.split()
        for j in range(0, len(words), 3):
            line = " ".join(words[j:j+3])
            s += f'<text x="{x+80}" y="{y+90 + (j//3)*22}" text-anchor="middle" font-size="10.5" fill="{RENK["lacivert"]}">{line}</text>'
    s += "</svg>"
    return s


def gorsel_4():
    """Sünnet-Vahiy Birlikteliği: Beşeriyet ve Risalet Yönü"""
    W, H = 720, 320
    s = _baslik(W, H, "BEŞER &amp; RESUL", "Hz. Peygamber'in Risalet (Peygamberlik) ve Beşeriyet (İnsani) Yönü", RENK["mor"])
    boxes = [
        ("İbadet ve Dinde İtidal (Denge) Ölçüsü", "Üç Sahabiye Verdiği Nebevi Cevap", [
            "• 'Gece hiç uyumadan namaz kılacağım, hep oruç",
            "  tutacağım, hiç evlenmeyeceğim' diyen 3 sahabiyi uyardı.",
            "• 'Ben bazen oruç tutar bazen yerim; gece namaz kılar",
            "  ve uyurum; evlilik de yaptım. Sünnetimden yüz çeviren",
            "  benden değildir!' buyurarak aşırılığı yasakladı.",
        ], RENK["mavi"], RENK["acik_mavi"]),
        ("Vahiy Dışı Uzmanlık ve İstişare Alanı", "Bedir'de Hubâb bin Münzir'in (ra) Görüşü", [
            "• Hubâb b. Münzir: 'Bu mevzi vahiy mi yoksa savaş",
            "  stratejisi ve taktik mi?' diye sordu.",
            "• Hz. Peygamber 'Savaş stratejisi ve taktiktir' buyurunca,",
            "  Hubâb'ın kuyuları kontrol altına alma teklifini kabul",
            "  ederek ordunun yerini değiştirdi.",
        ], RENK["mor"], RENK["acik_mor"]),
    ]
    for i, (b, alt, items, rk, ark) in enumerate(boxes):
        x = 24 + i * 344
        y = 64
        s += f'<rect x="{x}" y="{y}" width="328" height="236" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<rect x="{x}" y="{y}" width="328" height="36" rx="10" fill="{rk}"/>'
        s += f'<text x="{x+164}" y="{y+23}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{b}</text>'
        s += f'<text x="{x+16}" y="{y+60}" font-size="11.5" font-weight="700" fill="{rk}">{alt}</text>'
        for j, m in enumerate(items):
            s += f'<text x="{x+14}" y="{y+90 + j*28}" font-size="10.8" fill="{RENK["lacivert"]}">{m}</text>'
    s += "</svg>"
    return s


def gorsel_5():
    """Muaz bin Cebel Hadisi ve İslam Hukukunda Kaynak Sıralaması"""
    W, H = 720, 310
    s = _baslik(W, H, "HÜKÜM KAYNAKLARI", "Muâz bin Cebel (ra) Hadisinde Hüküm Verme Sıralaması", RENK["lacivert"])
    steps = [
        ("1. AŞAMA: ALLAH'IN KİTABI (KUR'AN-I KERİM)", "Bir meseleyle karşılaşıldığında ilk olarak Kur'an-ı Kerim'in açık hükümlerine başvurulur.", RENK["yesil"], RENK["acik_yesil"]),
        ("2. AŞAMA: RESULULLAH'IN SÜNNETİ", "Kur'an-ı Kerim'de açık hüküm bulunamazsa Hz. Peygamber'in (sav) sünnetine göre hüküm verilir.", RENK["mavi"], RENK["acik_mavi"]),
        ("3. AŞAMA: İÇTİHAT (AKLÎ MUHAKEME VE KIYAS)", "Kitap ve sünnette açıkça bulunmayan meselede Kur'an ve sünnetin ruhuna uygun içtihat edilir.", RENK["turuncu"], RENK["acik_turuncu"]),
    ]
    for i, (st, desc, rk, ark) in enumerate(steps):
        y = 64 + i * 76
        s += f'<rect x="24" y="{y}" width="672" height="62" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="42" y="{y+25}" font-size="13" font-weight="800" fill="{rk}">{st}</text>'
        s += f'<text x="42" y="{y+47}" font-size="11.5" font-weight="600" fill="{RENK["lacivert"]}">{desc}</text>'
    s += "</svg>"
    return s


def gorsel_6():
    """Bir Sahabi Tanıyorum: Abdullah bin Ömer (ra)"""
    W, H = 720, 320
    s = _baslik(W, H, "ÖRNEK SAHABİ", "Abdullah bin Ömer'in (ra) Hayatı ve Sünnete Bağlılığı", RENK["kirmizi"])
    cards = [
        ("Kimliği ve Gazveleri", "Hz. Ömer'in oğlu, müminlerin annesi Hz. Hafsa'nın (ra) kardeşidir. 15 yaşında Hendek Savaşı'na, Mekke'nin Fethi'ne ve İstanbul kuşatmasına katıldı.", RENK["mavi"], RENK["acik_mavi"]),
        ("İlmî Kişiliği (Müksirûn &amp; Fakih)", "Ebû Hüreyre'den (ra) sonra en çok hadis rivayet eden 2. sahabidir. Medine'de en çok fetva veren 7 fakihten biridir.", RENK["yesil"], RENK["acik_yesil"]),
        ("Hadis Rivayetindeki Titizliği", "Hz. Peygamber'den duyduğu hadisleri tek bir kelimesini bile değiştirmeden lafzıyla olduğu gibi aktarmaya özen göstermiştir.", RENK["turuncu"], RENK["acik_turuncu"]),
        ("Sünnete Eşsiz Bağlılığı", "Hz. Peygamber'in tavsiyesi üzerine gece namazını hiç terk etmemiş; onun namaz kıldığı yerlerde namaz kılmış, selamı yaymıştır.", RENK["kirmizi"], RENK["acik_kirmizi"]),
    ]
    for i, (title, desc, rk, ark) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = 22 + col * 344
        y = 64 + row * 124
        s += f'<rect x="{x}" y="{y}" width="332" height="110" rx="10" fill="{ark}" stroke="{rk}" stroke-width="1.8"/>'
        s += f'<text x="{x+16}" y="{y+26}" font-size="12.5" font-weight="800" fill="{rk}">{title}</text>'
        words = desc.split()
        l1 = " ".join(words[:6])
        l2 = " ".join(words[6:13])
        l3 = " ".join(words[13:])
        s += f'<text x="{x+16}" y="{y+52}" font-size="10.8" fill="{RENK["lacivert"]}">{l1}</text>'
        s += f'<text x="{x+16}" y="{y+72}" font-size="10.8" fill="{RENK["lacivert"]}">{l2}</text>'
        s += f'<text x="{x+16}" y="{y+92}" font-size="10.8" fill="{RENK["lacivert"]}">{l3}</text>'
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