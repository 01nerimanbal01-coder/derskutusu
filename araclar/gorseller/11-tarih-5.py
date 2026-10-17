def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#B45309", bg="#FFFBEB"):
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
        '17. VE 18. YÜZYILDA AVRUPA\'DA BİLİM DEVRİMİ VE AYDINLANMA ÇAĞI</text>'
    )
    ic += _kart(20, 44, 310, 190, "AKIL ÇAĞI VE BİLİM DEVRİMİ", [
        "• Skolastik düşüncenin yerini deney ve gözlem aldı.",
        "• Kopernik ve Galileo: Güneş merkezli evren modeli.",
        "• Francis Bacon: Deneysel yöntem ve tümevarım ilkesi.",
        "• Rene Descartes: Rasyonalizm (Akılcılık - 'Düşünüyorum,",
        "  öyleyse varım') ve analitik geometri.",
        "• Isaac Newton: Evrensel kütle çekim yasası ve mekanik",
        "  evren anlayışı (Doğa yasalarının matematiksel izahı)."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "AYDINLANMA FELSEFESİ VE SONUÇLARI", [
        "• Immanuel Kant: 'Aklını kullanma cesaretini göster!'",
        "• John Locke: Doğal haklar (yaşam, özgürlük, mülkiyet)",
        "  ve liberal devlet kuramı.",
        "• Montesquieu: Kuvvetler ayrılığı (Yasama-Yürütme-Yargı).",
        "• J.J. Rousseau: Toplum Sözleşmesi ve milli egemenlik.",
        "• Sonuç: Sanayi İnkılabı'na bilimsel zemin, Fransız",
        "  İhtilali'ne ise fikrî ve siyasi zemin hazırladı."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'LALE DEVRİ (1718-1730): BATI\'YA AÇILAN İLK PENCERE</text>'
    )
    ic += _kart(20, 44, 205, 190, "SİYASİ VE DİPLOMATİK", [
        "• 1718 Pasarofça Antlaşması",
        "  ile başladı.",
        "• Padişah: III. Ahmed",
        "• Sadrazam: Nevşehirli",
        "  Damat İbrahim Paşa.",
        "• Avrupa'ya ilk geçici",
        "  elçilikler gönderildi (Paris:",
        "  Yirmisekiz Mehmed Çelebi)."
    ], "#D97706", "#FEF3C7")
    ic += _kart(237, 44, 205, 190, "KÜLTÜR VE TEKNOLOJİ", [
        "• İlk Türk matbaası kuruldu",
        "  (İbrahim Müteferrika ve",
        "  Said Efendi - 1727).",
        "• İlk basılan eser: Vankulu",
        "  Lügati (1729).",
        "• Tercüme heyetleri, Yalova'da",
        "  kağıt, İstanbul'da çini ve",
        "  kumaş imalathaneleri açıldı."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "SOSYAL VE SONUÇ", [
        "• Yeniçerilerden 'Tulumbacılar'",
        "  (İlk itfaiye) ocağı kuruldu.",
        "• İlk kez çiçek aşısı uygulandı.",
        "• Sivil mimari gelişti (III.",
        "  Ahmed Çeşmesi, Sadabad).",
        "• Dikkat: Lale Devri'nde",
        "  ASKERÎ ISLAHAT YOKTUR!",
        "• 1730 Patrona Halil İsyanı."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        '18. YÜZYIL OSMANLI ASKERÎ ISLAHATLARI VE AVRUPALI UZMANLAR</text>'
    )
    ic += _kart(20, 44, 205, 200, "I. MAHMUD DÖNEMİ", [
        "• Batı tarzı İLK askerî",
        "  ıslahatlar yapıldı.",
        "• Comte de Bonneval",
        "  (Humbaracı Ahmed Paşa)",
        "  getirildi.",
        "• Humbaracı ve Topçu",
        "  ocakları modernize edildi.",
        "• Hendesehane (Batı tarzı",
        "  ilk askerî teknik okul) açıldı."
    ], "#1D4ED8", "#EFF6FF")
    ic += _kart(237, 44, 205, 200, "III. MUSTAFA VE I. ABDÜLHAMİD", [
        "• Baron de Tott ve Sadrazam",
        "  Koca Ragıp / Halil Hamid Paşa.",
        "• Sürat Topçuları Ocağı kuruldu.",
        "• Deniz Mühendishanesi",
        "  (Mühendishane-i Bahr-i",
        "  Hümayun - 1773) açıldı.",
        "• İstihkâm Okulu kuruldu.",
        "• Ulufe alım-satımı yasaklandı,",
        "  Esham senetleri çıkarıldı."
    ], "#0F766E", "#F0FDFA")
    ic += _kart(455, 44, 205, 200, "III. SELİM (NİZAM-I CEDİD)", [
        "• Köklü ve planlı ıslahatlar",
        "  (Meşveret Meclisi raporları).",
        "• Nizam-ı Cedid Ordusu ve",
        "  İrad-ı Cedid Hazinesi kuruldu.",
        "• Kara Mühendishanesi (Berr-i",
        "  Hümayun) açıldı, Fransızca",
        "  resmî yabancı dil oldu.",
        "• Londra, Paris, Viyana, Berlin'de",
        "  İLK DAİMİ ELÇİLİKLER açıldı."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        '17. VE 18. YÜZYIL OSMANLI ISLAHATLARININ KARŞILAŞTIRMASI</text>'
    )
    satirlar = [
        ("17. YÜZYIL ISLAHATLARI", "Avrupa örnek alınmadı; Kanuni dönemine (Eski güçlü düzene) dönmek hedeflendi, baskı ve şiddet uygulandı.", "#DC2626", "#FEF2F2"),
        ("18. YÜZYIL ISLAHATLARI", "İlk kez Avrupa'nın bilim ve tekniği örnek alındı; Lale Devri'nde kültürel, I. Mahmud'dan itibaren askerî ıslahatlar yapıldı.", "#2563EB", "#EFF6FF"),
        ("MATBAA VE DİNİ ESERLER", "Hattatların işsiz kalmasını önlemek ve dini metinlerde hata yapmamak için dini kitapların matbaada basımı yasaklandı.", "#D97706", "#FEF3C7"),
        ("ISLAHATLARIN ENGELLERİ", "Yeniçeri Ocağı ve çıkarları zedelenen ulema/devlet adamlarının isyanları (Patrona Halil - 1730, Kabakçı Mustafa - 1807).", "#059669", "#ECFDF5")
    ]
    for i, (b, m, r, bg) in enumerate(satirlar):
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
