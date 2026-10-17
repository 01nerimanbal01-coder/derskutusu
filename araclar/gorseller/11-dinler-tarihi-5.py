def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#D97706", bg="#FEF3C7"):
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
        'HİNDUİZM\'İN TARİHÇESİ VE TANRI ANLAYIŞI (TRİMURTİ)</text>'
    )
    ic += _kart(20, 44, 310, 190, "GENEL ÖZELLİKLERİ (SANATANA DHARMA)", [
        "• Dünyanın yaşayan en eski geleneksel dinidir (MÖ 2000).",
        "• Belirli bir kurucusu ve tek bir amentüsü YOKTUR.",
        "• Mensupları dinlerine 'Sanatana Dharma' (Ezeli-Ebedi",
        "  Yasa / Düzen) adını verirler.",
        "• Milli/Etnik bir dindir; Hindistan ve Nepal'de yaygındır.",
        "• Politeist (çok tanrılı) görünümün altında tek mutlak",
        "  gerçeklik 'Brahman' ve 'Trimurti' (Üçlü Tanrı) vardır."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "TRİMURTİ (ÜÇLÜ İLAHİ TEZAHÜR)", [
        "1. BRAHMA: Yaratıcı Tanrı (Evreni var eden güç).",
        "2. VİŞNU: Koruyucu Tanrı (Evrenin düzenini korur;",
        "   yeryüzüne Rama ve Krişna gibi 'Avatar' bedenleriyle",
        "   indiğine inanılır).",
        "3. ŞİVA: Yok Edici ve Yeniden Dönüştürücü Tanrı.",
        "• ATMAN: İnsanın içindeki ölümsüz ruh/öz; kurtuluş,",
        "  Atman'ın evrensel ruh Brahman ile birleşmesidir."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'HİNDUİZM\'İN KUTSAL METİNLERİ: ŞRUTİ VE SMRİTİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "1. ŞRUTİ (İŞİTİLEN / VAHYEDİLEN METİNLER)", [
        "• En kutsal ve değiştirilemez metinler: VEDALAR.",
        "• Dört Veda Kitabı:",
        "   - Rigveda (İlahiler - En eski Veda metni)",
        "   - Samaveda (Ezgi ve melodiler)",
        "   - Yacurveda (Kurban duaları ve ritüeller)",
        "   - Atharvaveda (Sihir, büyü ve şifa duaları)",
        "• Upanişadlar: Vedaların sonundaki felsefi/mistik yorumlar."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(350, 44, 310, 190, "2. SMRİTİ (HATIRLANAN / İNSANİ GELENEK)", [
        "• Bilge kişilerce yazılan destan ve hukuk metinleri.",
        "• Mahabharata Destanı: Dünyanın en uzun destanıdır;",
        "  içindeki 'Bhagavad Gita' (Tanrının Şarkısı - Krişna",
        "  ile Arjuna'nın diyaloğu) en çok okunan kutsal metindir.",
        "• Ramayana Destanı: Prens Rama ve eşi Sita'nın öyküsü.",
        "• Manu Kanunnamesi: Kast kurallarını ve toplumsal",
        "  hukuku düzenleyen metinler ve Puranalar."
    ], "#7C3AED", "#F5F3FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'TOPLUMSAL YAPI: KAST SİSTEMİ (VARNA) VE TABAKALAR</text>'
    )
    tabakalar = [
        ("1. BRAHMANLAR (DİN ADAMLARI VE BİLGİNLER)", "Kast piramidinin en üst tabakası; kutsal Vedaları okuma ve kurban törenlerini yönetme yetkisine sahiptirler.", "#7C3AED", "#F5F3FF"),
        ("2. KŞATRİYALAR (HÜKÜMDARLAR, PRENSLER VE ASKERLER)", "Devlet yönetimi, ordu komutanlığı ve ülkenin savunmasından sorumlu yönetici ve savaşçı sınıftır.", "#2563EB", "#EFF6FF"),
        ("3. VAİŞYALAR (TÜCCARLAR, ESNAF VE ÇİFTÇİLER)", "Ticaret, tarım ve hayvancılıkla uğraşarak toplumun ekonomik üretimini sağlayan sınıftır.", "#059669", "#ECFDF5"),
        ("4. ŞUDRALAR (İŞÇİLER) VE PARYALAR (DALİTLER)", "Şudralar ilk üç kasta hizmet eden işçilerdir; Paryalar (Dokunulmazlar) ise hiçbir kasta dahil edilmeyen en alt gruptur.", "#DC2626", "#FEF2F2")
    ]
    for i, (b, m, r, bg) in enumerate(tabakalar):
        y = 44 + i * 50
        ic += (
            f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'TEMEL İNANÇ ESASLARI (KARMA - SAMSARA - MOKŞA) VE İBADETLER</text>'
    )
    ic += _kart(20, 44, 310, 190, "KARMA, REENKARNASYON VE MOKŞA", [
        "• KARMA: 'Ne ekersen onu biçersin' nedensellik yasası;",
        "  bu hayattaki eylemler bir sonraki doğumu belirler.",
        "• SAMSARA / TENASÜH (Reenkarnasyon): Ruhun (Atman)",
        "  ölümden sonra başka bir insan, hayvan veya bitki",
        "  bedeninde tekrar dünyaya gelmesi döngüsüdür.",
        "• MOKŞA: Ruh göçü çarkından kurtularak ebedi huzura",
        "  ve Brahman ile bütünleşmeye ulaşmaktır."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "İBADETLER (PUCA) VE KUTSAL SEMBOLLER", [
        "• Puca: Evdeki veya tapınaktaki (Mandir) tanrı",
        "  heykelleri önünde yapılan günlük bireysel ibadet.",
        "• Ganj Nehri (Varanasi/Benares): Kutsal nehirde",
        "  yıkanmanın günahlardan arındırdığına inanılır.",
        "• Antyeşti: Ölülerin yakılarak küllerinin Ganj'a savrulması.",
        "• Ahimsa (Canlılara zarar vermeme) ve İneklerin kutsallığı.",
        "• Bayramlar: Diwali (Işık) ve Holi (Renk/Bahar) bayramı."
    ], "#0891B2", "#ECFEFF")
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
