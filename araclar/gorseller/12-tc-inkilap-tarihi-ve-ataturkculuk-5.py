def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#DC2626", bg="#FEF2F2"):
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
        'KUVÂ-YI MİLLİYE RUHU VE SAMSUN\'A ÇIKIŞ (19 MAYIS 1919)</text>'
    )
    ic += _kart(20, 44, 310, 190, "KUVÂ-YI MİLLİYE (MİLLÎ KUVVETLER)", [
        "• Mondros sonrası Osmanlı ordusunun terhis edilmesi,",
        "  İstanbul Hükümeti'nin sessiz kalması ve İzmir'in",
        "  işgali (15 Mayıs 1919) üzerine halkın kurduğu",
        "  silahlı direniş birlikleridir.",
        "• İlk silahlı direniş: Güneyde Dörtyol (19 Aralık 1918),",
        "  Batıda Ayvalık ve Ödemiş cephelerinde başladı.",
        "• Düzenli ordu kurulana kadar düşmanı oyaladı ve iç isyanları bastırdı."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "9. ORDU MÜFETTİŞLİĞİ VE SAMSUN RAPORU", [
        "• Mustafa Kemal Paşa, 9. Ordu Müfettişi sıfatıyla",
        "  19 Mayıs 1919'da Samsun'a çıktı.",
        "• Görünürdeki Görev: Karadeniz'deki Rum-Türk",
        "  çatışmasını önlemek ve silahları toplamak.",
        "• Asıl Amaç: Anadolu'da Milli Mücadele'yi başlatmak.",
        "• Samsun Raporu (22 Mayıs 1919): 'Karadeniz'deki",
        "  karışıklığın sebebi Türkler değil, Rum çeteleridir!'"
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'GENELGELER DÖNEMİ: HAVZA VE AMASYA GENELGESİ (HAZİRAN 1919)</text>'
    )
    ic += _kart(20, 44, 310, 200, "HAVZA GENELGESİ (28 MAYIS 1919)", [
        "• Mustafa Kemal Paşa'nın tek başına yayımladığı",
        "  ilk ulusal genelgedir.",
        "• İşgallere karşı bütün yurtta protesto MİTİNGLERİ",
        "  düzenlenmesi ve İtilaf Devletleri ile İstanbul'a",
        "  kınama telgrafları çekilmesi istendi.",
        "• Mitinglerde Hristiyan azınlığa kötü davranılmaması",
        "  uyarısı yapıldı (Mondros 7. maddeye bahane vermemek için!).",
        "• Önemi: Milli bilincin uyandırılması sağlandı."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 200, "AMASYA GENELGESİ (22 HAZİRAN 1919) - İHTİLAL BİLDİRİSİ", [
        "• Rauf, Refet, Ali Fuat ve Kazım Karabekir Paşa'nın onayıyla:",
        "• GEREKÇE: 'Vatanın bütünlüğü, milletin bağımsızlığı",
        "  tehlikededir; İstanbul Hükümeti görevini yapamamaktadır.'",
        "• AMAÇ VE YÖNTEM: 'Milletin bağımsızlığını yine milletin",
        "  azim ve kararı kurtaracaktır!' (İlk kez MİLLÎ EGEMENLİK!).",
        "• 'Her türlü etki ve denetimden uzak MİLLÎ BİR KURUL",
        "  (Temsil Heyeti) oluşturulmalı ve Sivas'ta kongre toplanmalıdır.'",
        "• Sonrası: Mustafa Kemal askerlikten istifa etti (Sine-i Millet)."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'ERZURUM KONGRESİ (23 TEMMUZ - 7 AĞUSTOS 1919) VE KARARLARI</text>'
    )
    ic += _kart(20, 44, 310, 190, "TOPLANMA AMACI: BÖLGESEL", [
        "• Doğu Anadolu Müdafaa-i Hukuk ve Trabzon Muhafaza-i",
        "  Hukuk Cemiyetlerince Ermeni ve Rum tehdidine karşı",
        "  BÖLGESEL amaçla toplandı.",
        "• Mustafa Kemal Paşa kongre başkanlığına seçilince",
        "  tüm yurdu kapsayan ULUSAL KARARLAR alındı.",
        "• 9 kişilik Temsil Heyeti ilk kez oluşturuldu",
        "  (Yetkisi başlangıçta Doğu illeriyle sınırlıydı)."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "ALINAN KARARLAR: ULUSAL", [
        "• 'Milli sınırlar içinde vatan bir bütündür, parçalanamaz!'",
        "  (İlk kez MİLLÎ SINIRLARDAN bahsedildi - Misak-ı Milli temeli).",
        "• 'Kuvâ-yı Milliye'yi etkin, milli iradeyi hâkim kılmak esastır.'",
        "• 'Manda ve himaye kabul olunamaz!' (İlk kez reddedildi).",
        "• 'Hristiyan azınlıklara siyasi hâkimiyetimizi ve sosyal",
        "  dengemizi bozucu ayrıcalıklar verilemez.'",
        "• 'Mebusan Meclisi derhal toplanmalıdır.'"
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'SİVAS KONGRESİ (4-11 EYLÜL 1919) VE AMASYA GÖRÜŞMELERİ</text>'
    )
    adimlar = [
        ("HEM TOPLANIŞI HEM KARARLARI ULUSAL", "Elazığ Valisi Ali Galip olayı engeline rağmen toplandı; Erzurum kararları bütün vatanı kapsayacak şekilde genişletildi.", "#DC2626", "#FEF2F2"),
        ("MANDA VE HİMAYE KESİN OLARAK REDDEDİLDİ", "Amerikan mandası tartışmaları 'Ya istiklal ya ölüm!' parolasıyla bir daha gündeme gelmemek üzere kesin olarak reddedildi.", "#2563EB", "#EFF6FF"),
        ("TÜM CEMİYETLER TEK ÇATIDA BİRLEŞTİRİLDİ", "Bütün yararlı cemiyetler 'Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti' (ARMHC) adıyla birleştirildi; İrade-i Milliye gazetesi çıkarıldı.", "#059669", "#ECFDF5"),
        ("TEMSİL HEYETİ'NİN İLK SİYASİ ZAFERİ", "Damat Ferit Hükümeti istifa etti; Ali Rıza Paşa Hükümeti Temsil Heyeti ile Amasya Görüşmeleri'ni yaparak varlığını resmen tanıdı!", "#7C3AED", "#F5F3FF")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
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
