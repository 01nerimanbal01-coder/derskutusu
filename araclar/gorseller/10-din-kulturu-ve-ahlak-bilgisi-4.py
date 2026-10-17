# -*- coding: utf-8 -*-
"""10. Sınıf Din Kültürü ve Ahlak Bilgisi — 4. Hafta görsel modülü:
Allah-Âlem İlişkisini Müşahede Etme: Kevnî Ayetler, Sünnetullah, Ölçü ve Düzen"""

C_MOR = "#6c3483"
C_MAVI = "#1a5276"
C_YESIL = "#1e8449"
C_TURUNCU = "#b9770e"
C_KIRMIZI = "#922b21"
C_ACIK_MOR = "#f5eef8"
C_ACIK_MAVI = "#eaf2f8"
C_ACIK_YESIL = "#e9f7ef"
C_ACIK_SARI = "#fef9e7"
C_ACIK_KIRMIZI = "#fdedec"
C_KOYU = "#1c2833"
C_GRI = "#566573"
C_SINIR = "#d5d8dc"


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def gorsel_1():
    """İki Kitap Anlayışı: Kavlî (Sözlü) Ayetler ve Kevnî (Yaratılış) Ayetleri."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Allah\'ın İki Tür Ayeti: Kavlî Ayetler (Kur\'an) ve Kevnî Ayetler (Kâinat)</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">1. Kavlî (Sözlü / Vahyî) Ayetler</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">• Kur\'an-ı Kerim\'de yer alan ilahi vahiydir.</text>',
        f'<text x="175" y="128" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Okunarak, anlaşılarak ve yaşanarak</text>',
        f'<text x="175" y="146" text-anchor="middle" font-size="10.2" fill="{C_GRI}">insana doğru yolu (hidayeti) gösterir.</text>',
        f'<text x="175" y="170" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• İnsanı sürekli kâinata bakmaya, akletmeye</text>',
        f'<text x="175" y="188" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">ve tefekkür etmeye davet eder.</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">2. Kevnî (Yaratılış / Kâinat) Ayetleri</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_KOYU}">• Evrendeki tüm varlıklar ve doğa olaylarıdır.</text>',
        f'<text x="505" y="128" text-anchor="middle" font-size="10.2" fill="{C_GRI}">• Gece-gündüzün oluşumu, yağmurun yağması,</text>',
        f'<text x="505" y="146" text-anchor="middle" font-size="10.2" fill="{C_GRI}">gezegenlerin yörüngesi, canlıların yapısı</text>',
        f'<text x="505" y="164" text-anchor="middle" font-size="10.2" fill="{C_GRI}">Allah\'ın varlığını, birliğini ve kudretini</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MAVI}">gösteren birer işaret (ayet) ve delildir.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Evrendeki Ölçü, Düzen ve Sünnetullah (İlahi Yasalar)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Evrendeki İlahi Yasalar: Sünnetullah (Âdetullah) ve Üç Boyutu</text>',
    ]
    yasalar = [
        ("1. Fiziksel Yasalar", "Madde ve enerjinin oluşumu,", "hareketi ve değişimi ile ilgili", "evrensel yasalardır (Yer çekimi,", "suyun kaldırma kuvveti, mevsimler).", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Biyolojik Yasalar", "Canlıların doğumu, beslenmesi,", "üremesi, solunumu ve çevreye", "uyumu ile ilgili ilahi yasalardır", "(Fotosentez, genetik, hücre yapısı).", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Toplumsal Yasalar", "Toplumların huzuru, yükselişi", "ve çöküşüyle ilgili neden-sonuç", "yasalarıdır (Adalet, emanet, ahlak,", "birlik ve yardımlaşma ilkeleri).", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, s4, renk, bg, x in yasalar:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="106" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="124" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="142" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
        p.append(f'<text x="{x+104}" y="162" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{s4}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Allah'ın Âlemle Sürekli İlişkisi: Yaratma, Yaşatma, Rızık ve İdare."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Âlemde Tecelli Eden İlahi İsim ve Sıfatlar (Esma-i Hüsna)</text>',
    ]
    isimler = [
        ("El-Hâlık ve El-Bâri'", "Yoktan var eden, her varlığı", "uyumlu ve kusursuz bir ölçüyle", "yaratan (Tekvin sıfatı).", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("Er-Rabb ve El-Kayyûm", "Âlemi her an terbiye eden,", "gözeten ve varlığını kendi", "kudretiyle ayakta tutan.", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("Er-Rezzâk ve El-Muhyî", "Canlılara hayat veren ve", "tüm varlıkların maddi-manevi", "rızkını kesintisiz sağlayan.", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("El-Alîm ve El-Hakîm", "Her şeyi sonsuz ilmiyle bilen;", "hiçbir şeyi boşuna yaratmayıp", "hikmet ve gayeyle yaratan.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in isimler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Allah-Âlem-İnsan İlişkisi: Halifelik, Emanet ve Çevre Bilinci."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Allah-Âlem İlişkisinde İnsanın Konumu ve Sorumlulukları</text>',
    ]
    sorumluluk = [
        ("1. Müşahede ve Tefekkür", "Kâinattaki düzeni gözlemleyip", "(müşahede) derinlemesine düşünerek", "Yaratıcı'nın kudretini kavramak.", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Bilimsel Araştırma", "Sünnetullah'ı (doğa yasalarını)", "keşfederek insanlığın faydasına", "bilim ve teknoloji üretmek.", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Emanet ve İmar (Mizan)", "Yeryüzünün halifesi olarak", "doğal dengeyi (mizanı) korumak;", "israf ve fesattan kaçınmak.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in sorumluluk:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="152" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
