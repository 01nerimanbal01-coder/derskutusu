# -*- coding: utf-8 -*-
"""11. Sınıf Hitabet ve Mesleki Uygulama — 4. Hafta görsel modülü: Ülkemizde Din Hizmetlerinin Müşahedesi."""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif">'
        f'<rect width="{w}" height="{h}" rx="16" fill="#0f172a"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, renk, baslik, satirlar):
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="#1e293b" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<text x="{x + w // 2}" y="{y + 21}" fill="#ffffff" font-size="13" '
        f'font-weight="700" text-anchor="middle">{baslik}</text>'
    )
    ty = y + 52
    for st in satirlar:
        s += (
            f'<text x="{x + 12}" y="{ty}" fill="#e2e8f0" font-size="11.5">'
            f'{st}</text>'
        )
        ty += 19
    return s


def gorsel_1():
    ic = (
        '<text x="380" y="30" fill="#38bdf8" font-size="16" font-weight="700" '
        'text-anchor="middle">ÜLKEMİZDE DİN HİZMETLERİNİN TEMEL ALANLARI</text>'
    )
    ic += _kart(25, 50, 340, 175, "#0284c7", "Cami İçi Din Hizmetleri", [
        "• Vakit, Cuma, Teravih ve Bayram namazları",
        "• Hutbe, vaaz ve mukabele programları",
        "• Camilerde Kur'an-ı Kerim ve dini bilgiler öğretimi",
        "• Kandil geceleri ve mevlid programları",
        "• Kadın, genç ve çocuk dostu cami etkinlikleri",
        "• İmam-hatip ve müezzin-kayyım rehberliği"
    ])
    ic += _kart(395, 50, 340, 175, "#10b981", "Cami Dışı ve Kurumsal Hizmetler", [
        "• Aile ve Dini Rehberlik Büroları (ADRB)",
        "• Gençlik merkezleri ve öğrenci yurtlarında rehberlik",
        "• Hastane, cezaevi ve huzurevlerinde manevi destek",
        "• Afet bölgelerinde (deprem, sel) manevi danışmanlık",
        "• Alo 190 Dini Soruları Cevaplandırma Hattı",
        "• Görsel, işitsel ve dijital yayınlarla irşat"
    ])
    return _svg(760, 245, ic)


def gorsel_2():
    ic = (
        '<text x="380" y="30" fill="#f59e0b" font-size="16" font-weight="700" '
        'text-anchor="middle">DİN HİZMETLERİNİ MÜŞAHEDE (SAHA GÖZLEMİ) AŞAMALARI</text>'
    )
    ic += _kart(25, 50, 170, 175, "#d97706", "1. Hazırlık &amp; Merak", [
        "• Gözlemlenecek hizmet",
        "  alanını belirlemek",
        "• Merak edilen konuları",
        "  tespit etmek",
        "• Gözlem formu ve",
        "  planı oluşturmak"
    ])
    ic += _kart(210, 50, 170, 175, "#8b5cf6", "2. Soru Sorma", [
        "• Din görevlilerine",
        "  yöneltilecek soruları",
        "  hazırlamak",
        "• Hedef kitlenin",
        "  ihtiyaçlarını sormak",
        "• İletişim dilini ölçmek"
    ])
    ic += _kart(395, 50, 170, 175, "#ec4899", "3. Saha İncelemesi", [
        "• Hutbe, vaaz veya",
        "  rehberlik sürecini",
        "  yerinde izlemek",
        "• Beden dili, ses tonu",
        "  ve üslubu gözlemlemek",
        "• Fiziki ortamı incelemek"
    ])
    ic += _kart(580, 50, 155, 175, "#14b8a6", "4. Çıkarım Yapma", [
        "• Gözlem verilerini",
        "  değerlendirmek",
        "• Güçlü yönleri ve",
        "  önerileri raporlamak",
        "• Mesleki tecrübe",
        "  kazanmak"
    ])
    return _svg(760, 245, ic)


def gorsel_3():
    ic = (
        '<text x="380" y="30" fill="#a855f7" font-size="16" font-weight="700" '
        'text-anchor="middle">MANEVİ DANIŞMANLIK VE REHBERLİK HİZMETLERİ</text>'
    )
    ic += _kart(25, 50, 225, 175, "#6366f1", "Hastaneler &amp; Yaşlı Bakım", [
        "• Hastalara ve hasta yakınlarına",
        "  sabır ve ümit aşılama",
        "• Huzurevlerindeki yaşlılarla",
        "  yalnızlığı gideren sohbetler",
        "• Moral ve manevi direnci",
        "  güçlendirici ziyaretler"
    ])
    ic += _kart(268, 50, 225, 175, "#0ea5e9", "Gençlik &amp; Aile Rehberliği", [
        "• KYK yurtları ve Diyanet",
        "  Gençlik Merkezlerinde sohbet",
        "• ADRB aracılığıyla aile içi",
        "  iletişim ve değerler eğitimi",
        "• Bağımlılıkla mücadelede",
        "  manevi rehabilitasyon desteği"
    ])
    ic += _kart(510, 50, 225, 175, "#10b981", "Cezaevleri &amp; Çocuk Evleri", [
        "• Tutuklu ve hükümlülerin",
        "  topluma yeniden kazandırılması",
        "• Tövbe, ümit ve ahlaki",
        "  yenilenme bilinci kazandırma",
        "• Sevgi evlerindeki çocuklara",
        "  şefkat ve değer rehberliği"
    ])
    return _svg(760, 245, ic)


def gorsel_4():
    ic = (
        '<text x="380" y="30" fill="#10b981" font-size="16" font-weight="700" '
        'text-anchor="middle">ETKİLİ DİN HİZMETİNDE İLETİŞİM VE HİTABET ÖLÇÜTLERİ</text>'
    )
    ic += _kart(25, 50, 340, 175, "#059669", "Nebevi İrşat İlkeleri", [
        "• Kolaylaştırınız, zorlaştırmayınız (Teysîr)",
        "• Müjdeleyiniz, nefret ettirmeyiniz (Tebşîr)",
        "• Hikmetle ve güzel öğütle davet (Nahl 125)",
        "• Muhatabın seviyesine ve ihtiyacına göre konuşmak",
        "• Şefkat, tebessüm ve samimiyeti (ihlas) korumak",
        "• Söz ile davranış (temsil) bütünlüğü sağlamak"
    ])
    ic += _kart(395, 50, 340, 175, "#0284c7", "Çağdaş ve Dijital İmkânların Kullanımı", [
        "• Diyanet TV, Diyanet Radyo ve e-hizmet portalları",
        "• Ses, akustik ve görsel sunum teknolojileri",
        "• Engelli vatandaşlar için engelsiz cami ve işaret dili",
        "• Sosyal medyada sahih dini bilgi üretimi",
        "• Cami kütüphaneleri ve okuma salonları",
        "• Gönüllülük ve Türkiye Diyanet Vakfı (TDV) faaliyetleri"
    ])
    return _svg(760, 245, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    b = v.get("bolumler", [])
    if len(b) > 0:
        b[0]["gorsel"] = GORSELLER["b1"]
    if len(b) > 1:
        b[1]["gorsel"] = GORSELLER["b2"]
    if len(b) > 2:
        b[2]["gorsel"] = GORSELLER["b3"]
    if len(b) > 4:
        b[4]["gorsel"] = GORSELLER["b4"]