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


def gorsel_1():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DİN HİZMETLERİNDE İLETİŞİM SÜRECİNİN TEMEL ÖGELERİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "İLETİŞİMİN BEŞ ANA UNSURU", [
        "1. Kaynak (Gönderici / Hatip / Davetçi):",
        "   İhlaslı, ilim sahibi, temsil gücü yüksek din görevlisi.",
        "2. Mesaj (İleti / İrşat İçeriği):",
        "   Kur'an ve Sünnet'e dayalı sahih, açık ve yapıcı bilgi.",
        "3. Kanal (Oluk / Yöntem):",
        "   Hutbe, vaaz, ders, kitle iletişim araçları, beden dili.",
        "4. Alıcı (Muhatap / Cemaat) ve 5. Geri Bildirim (Dönüt)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "KUR'AN'DA TEBLİĞ VE HİTABET METODU", [
        "• Nahl Suresi 125. Ayet (Üç Temel Yöntem):",
        "   1) Hikmetle davet (Derin kavrayış ve kesin delil)",
        "   2) Güzel öğüt (Mev'iza-i Hasene - Kalbe dokunan söz)",
        "   3) En güzel biçimde mücadele (Cedeli Ahsen)",
        "• Tâhâ Suresi 44. Ayet: Firavun'a bile 'yumuşak söz'",
        "  (Kavlen Leyyinâ) söylenmesinin emredilmesi."
    ], "#059669", "#ECFDF5")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'MUHATAP ANALİZİ VE HEDEF KİTLEYE GÖRE ÜSLUP</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. YAŞ VE EĞİTİM DÜZEYİ", [
        "• 'İnsanlara akıllarının",
        "  (anlayışlarının) seviyesine",
        "  göre konuşunuz.'",
        "• Çocuk ve gençlere sevdirici,",
        "  somut ve ümit verici dil.",
        "• Aydın ve genç kesime",
        "  akli deliller ve ikna.",
        "• Yaşlılara şefkat ve hürmet."
    ], "#0284C7", "#F0F9FF")
    ic += _kart(237, 44, 205, 190, "2. PSİKOLOJİK DURUM", [
        "• Taziyede teselli ve sabır;",
        "  düğün ve nikâhta sevinç",
        "  ve hayır dua üslubu.",
        "• Empati (Kendini muhatabın",
        "  yerine koyma) ve etkin",
        "  dinleme becerisi.",
        "• Yargılayıcı 'Sen Dili' yerine",
        "  kuşatıcı 'Ben/Biz Dili'."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "3. NEBEVİ İLKELER", [
        "• 'Kolaylaştırınız, zorlaştırmayınız;",
        "  müjdeleyiniz, nefret",
        "  ettirmeyiniz!' (Teysir ve Tebşir).",
        "• Hataları şahısları hedef",
        "  almadan ('Bana ne oluyor ki",
        "  bazılarını şöyle görüyorum')",
        "  nezaketle düzeltmek."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SÖZLÜ VE SÖZSÜZ İLETİŞİM: SES TONU, DİKSİYON VE BEDEN DİLİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "SÖZLÜ İLETİŞİM VE DİKSİYON", [
        "• Diksiyon: Kelimeleri doğru telaffuz etme, vurgu ve",
        "  tonlamayı (entonasyon) anlama uygun kullanma sanatı.",
        "• Monoton (tekdüze) ses tonu dinleyicinin dikkatini",
        "  dağıtır; ses tonu konunun heyecanına göre ayarlanmalıdır.",
        "• Akıcı, duru ve anlaşılır bir Türkçe kullanılmalı;",
        "  açıklamasız ağdalı terimlerden kaçınılmalıdır."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "SÖZSÜZ İLETİŞİM (BEDEN DİLİ)", [
        "• İletişimde etkinin en büyük payı beden dili ve ses",
        "  tonuna aittir.",
        "• Göz Teması: Dinleyicilerin tamamını kucaklayan",
        "  samimi ve dengeli bakış.",
        "• Jest (el-kol) ve Mimikler (yüz ifadeleri): Sözle",
        "  uyumlu, abartıdan uzak ve mütebessim çehre.",
        "• Duruş ve Kıyafet: Vakara uygun temiz ve düzenli görünüm."
    ], "#0D9488", "#F0FDFA")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'DİN HİZMETLERİNDE İLETİŞİM ENGELLERİ VE ÇÖZÜM YOLLARI</text>'
    )
    engeller = [
        ("1. TEMSİL EKSİKLİĞİ (SÖZ-EYLEM ÇELİŞKİSİ)", "Hatibin anlattığı ahlaki ilkeleri kendi hayatında yaşamaması (Saff, 2-3) güveni ve tesiri ortadan kaldırır.", "#DC2626", "#FEF2F2"),
        ("2. ÖNYARGI, KINAMA VE ÜSTENCİ DİL", "Muhatabı günahkâr diye küçümsemek, azarlamak ve hep korkutucu (inzâr) bir dil kullanmak kalpleri kapatır.", "#D97706", "#FEF3C7"),
        ("3. HAZIRLIKSIZLIK VE KONU DAĞINIKLIĞI", "Önceden plan yapmadan kürsüye çıkmak, süreyi aşmak ve zayıf/uydurma rivayetler anlatmak cemaati yorar.", "#7C3AED", "#F5F3FF"),
        ("4. ÇÖZÜM: İHLAS, TEBŞİR VE EMPATİ", "Samimiyet (ihlas), müjdeleyici üslup, sahih kaynak kullanımı ve güler yüzle muhatabın gönlüne hitap etmek.", "#059669", "#ECFDF5")
    ]
    for i, (b, m, r, bg) in enumerate(engeller):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
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
