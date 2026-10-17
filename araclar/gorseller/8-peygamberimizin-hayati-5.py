# -*- coding: utf-8 -*-
"""8. Sınıf Peygamberimizin Hayatı — 5. Hafta Görselleri (Medine'de İslam Toplumunun Oluşumu)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Medine\'de İslam Toplumunu İnşa Eden 4 Kurucu Adım</text>',
        _kart(25, 50, 225, 215, "1. Mescid-i Nebevî ve Suffe", [
            "• İbadet, eğitim, yönetim ve",
            "  istişare merkezi olarak inşa edildi.",
            "• Yanına 'Suffe' (Ehl-i Suffe)",
            "  eklenerek İslam'ın ilk yatılı",
            "  üniversitesi kuruldu.",
            "• Ebû Hüreyre gibi âlimler yetişti."
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Muâhât (Kardeşlik Antlaşması)", [
            "• Mekkeli Muhacirler ile Medineli",
            "  Ensar birer ikişer kardeş ilan edildi.",
            "• Evs ve Hazrec kabileleri arasındaki",
            "  120 yıllık Buâs düşmanlığı bitirildi.",
            "• Îsâr (kardeşini kendine tercih etme)",
            "  ahlakının zirvesi yaşandı."
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Medine Sözleşmesi ve Pazar", [
            "• Müslümanlar, Yahudiler ve diğer",
            "  kabileler arasında imzalanan",
            "  tarihin ilk yazılı anayasalarındandır.",
            "• Din vicdan özgürlüğü ve ortak",
            "  savunma ilkesi kabul edildi.",
            "• Bağımsız Medine Pazarı kuruldu."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mescid-i Nebevî\'nin Çok Yönlü İşlevleri ve Ehl-i Suffe</text>',
        _kart(30, 50, 335, 215, "Mescid-i Nebevî'nin Toplumsal Rolü", [
            "• 1. İbadet Merkezi: Günde 5 vakit cemaatle namaz.",
            "• 2. Eğitim Merkezi: Halkın Kur'an ve sünneti öğrenmesi.",
            "• 3. Yönetim ve İstişare Merkezi: Önemli kararların",
            "  sahabilerle danışarak (şûra ile) alınması.",
            "• 4. Adalet ve Diplomasi: Davaların çözülmesi ve",
            "  yabancı elçilerin kabul edilmesi."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Suffe Mektebi ve Ashâb-ı Suffe", [
            "• Mescidin bitişiğindeki gölgelikli bölümdür.",
            "• Kimsesiz, bekâr ve ilim öğrenmeye adanmış",
            "  sahabiler (Ashâb-ı Suffe) burada kalırdı.",
            "• Peygamberimizden doğrudan Kur'an, yazı ve",
            "  dini hükümler öğrenip diğer kabilelere",
            "  öğretmen (muallim) olarak gönderilirlerdi."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Ensar-Muhacir Kardeşliği (Muâhât) ve Îsâr Örneği</text>',
        _kart(30, 50, 335, 215, "Sa'd bin Rebî ve Abdurrahman bin Avf", [
            "• Ensar'dan Sa'd bin Rebî, Muhacir kardeşi",
            "  Abdurrahman bin Avf'a malının ve bahçelerinin",
            "  yarısını vermeyi teklif etti.",
            "• Abdurrahman bin Avf ise: 'Allah malını ve",
            "  aileni sana mübarek kılsın; sen bana sadece",
            "  pazarın yolunu göster!' diyerek alın teriyle çalıştı."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Îsâr: Kardeşini Öz Nefsine Tercih Etmek", [
            "• Haşr suresi 9. ayette Ensar şöyle övülür:",
            "• 'Kendileri ihtiyaç içinde olsalar bile,",
            "  (Muhacir) kardeşlerini kendi nefislerine",
            "  tercih ederler (yu'sirûne alâ enfüsihim).'",
            "• Muhacirler de kardeşlerinin bu cömertliğini",
            "  istismar etmeyip üretime katılmışlardır."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Medine Sözleşmesi (Vatandaşlık Antlaşması) ve Ekonomik Bağımsızlık</text>',
        _kart(30, 50, 335, 195, "Medine Sözleşmesi'nin Temel Maddeleri", [
            "• Medine'deki tüm gruplar barış içinde yaşayacak.",
            "• Herkes kendi dinini yaşamakta özgürdür.",
            "• Medine'ye dışarıdan bir saldırı olursa",
            "  şehri tüm gruplar birlikte savunacaktır.",
            "• Anlaşmazlıklarda son hakem Hz. Muhammed'dir (sav)."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Medine İslam Pazarının Kurulması", [
            "• Haksız vergilerin, faizin, ölçü-tartı hilesinin",
            "  ve karaborsanın yasak olduğu yeni bir pazar kuruldu.",
            "• Müslüman tüccarlar dürüst ticaret ilkeleriyle",
            "  kısa sürede ekonomik bağımsızlık kazandı.",
            "• Nüfus sayımı yapılarak şehir düzeni sağlandı."
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
