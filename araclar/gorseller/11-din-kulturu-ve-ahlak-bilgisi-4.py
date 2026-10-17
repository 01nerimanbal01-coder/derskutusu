def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:0 auto;'
        f'font-family:\'Segoe UI\',Roboto,sans-serif">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", arkaplan="#eff6ff"):
    b_yuk = 30
    s = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
        f'fill="{arkaplan}" stroke="{renk}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="{b_yuk}" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y + b_yuk - 8}" width="{w}" height="8" fill="{renk}"/>'
        f'<text x="{x + w / 2}" y="{y + 20}" fill="#ffffff" font-size="12.5" '
        f'font-weight="bold" text-anchor="middle">{baslik}</text>'
    )
    yy = y + b_yuk + 19
    for st in satirlar:
        s += f'<text x="{x + 12}" y="{yy}" fill="#1e293b" font-size="11.5">{st}</text>'
        yy += 18
    return s


def gorsel_1():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'AKIL, İRADE VE SORUMLULUK EKSENİNDE KADER KAVRAMLARININ YORUMU</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1. Ömür, Ecel ve Sağlık",
        [
            "• Ömür: Doğumdan ölüme geçen",
            "  yaşam süresi; Ecel: Ölüm anı.",
            "• İnsanın Sorumluluğu: Sağlığını",
            "  korumak, tehlikeden kaçınmak,",
            "  hastalandığında tedavi olmak.",
            "• 'Kendi elinizle kendinizi",
            "  tehlikeye atmayın!' (Bakara, 195).",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "2. Rızık, Emek ve Başarı",
        [
            "• Rezzâk olan Yüce Allah her",
            "  canlının rızkını yaratmıştır.",
            "• İnsanın Sorumluluğu: Helal",
            "  yoldan çalışıp rızkını aramak.",
            "• 'İnsan için ancak çalıştığının",
            "  karşılığı vardır!' (Necm, 39).",
            "• Tembellik kader bahanesi olamaz.",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        510, 42, 230, 198,
        "3. Tevekkül ve Tedbir",
        [
            "• Tevekkül = Akıl ve İradeyle",
            "  Tüm Tedbirleri Almak + Sonucu",
            "  Allah'a Havale Edip Güvenmek.",
            "• Tedbir almadan beklemeye",
            "  'Tevâkül (Tembellik)' denir.",
            "• 'Önce deveni bağla, sonra",
            "  Allah'a tevekkül et!' (Hadis).",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'ELEŞTİREL DÜŞÜNME: YANLIŞ KADER ALGISI İLE SAHİH İSLAM KADER İNANCI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Yanlış (Cebrî / Fatalist) Kader Algısı",
        [
            "• İnsanın iradesini ve sorumluluğunu yok sayar.",
            "• Suç işleyip 'Ne yapayım, kaderim böyleymiş, ben",
            "  kader kurbanıyım!' diyerek sorumluluktan kaçar.",
            "• Depreme dayanıksız bina yapıp yıkılınca suçu",
            "  kadere atar; tedbirsizliği kadercilikle örter.",
            "• Kur'an'da müşriklerin 'Allah dileseydi ortak",
            "  koşmazdık' (En'âm, 148) bahanesine benzer.",
        ],
        "#dc2626", "#fef2f2"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Sahih İslam (Kur'an ve Sünnet) Kader Anlayışı",
        [
            "• İnsan akıl ve cüz'î irade sahibi özgür bir",
            "  varlıktır; seçtiği her eylemden sorumludur.",
            "• Sünnetullah (fiziksel, biyolojik, toplumsal",
            "  yasalar) gözetilerek bütün tedbirler alınır.",
            "• 'Başınıza gelen herhangi bir musibet, kendi",
            "  ellerinizle işledikleriniz yüzündendir' (Şûrâ, 30).",
            "• Kader, insanı tembelliğe değil çabaya yöneltir.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'İLAHİ İLİM VE İNSAN ÖZGÜRLÜĞÜ: "İLİM MALUMA TABİDİR" İLKESİ</text>'
    )
    ic += _kart(
        20, 42, 720, 198,
        "Soru: 'Allah Benim Ne Yapacağımı Önceden Biliyorsa, Ben Nasıl Özgür Olabilirim?'",
        [
            "• Kelam İlmindeki Temel İlke: 'el-İlmü tâbiun li'l-ma'lûm' (Bilgi, bilinen şeye tabidir).",
            "• Açıklama: Yüce Allah zaman ve mekândan münezzeh (ezelî ve ebedî) olduğu için, geçmişi, şimdiyi ve",
            "  geleceği tek bir 'an' gibi kuşatan sonsuz ilmiyle insanın kendi özgür iradesiyle neyi seçeceğini bilir.",
            "• Allah bildiği için biz o fiili zorla yapmayız; biz cüz'î irademizle o fiili seçip yapacağımız için Allah bilir!",
            "• Temsil (Metafor): Bir öğretmenin yıllardır tanıdığı çalışkan bir öğrencinin sınavda 100 alacağını",
            "  veya meteoroloji uzmanının yarın yağmur yağacağını önceden bilmesi, öğrenciyi zorlamadığı gibi;",
            "  Yüce Allah'ın yanılmaz ezeli ilmi de kulun özgür iradesini ortadan kaldırmaz!",
        ],
        "#7c3aed", "#f5f3ff"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'TARİHÎ ÖRNEK: HZ. ÖMER\'İN (RA) ŞAM VEBA SALGINI KARŞISINDAKİ İÇTİHADI</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Olay: Amvâs (Şam) Veba Salgını ve Karantina",
        [
            "• Halife Hz. Ömer (ra) Şam'a giderken şehirde",
            "  bulaşıcı veba (taun) salgını çıktığını öğrendi.",
            "• Sahabilerle istişare ederek orduyu salgın",
            "  bölgesine sokmama ve geri dönme kararı aldı.",
            "• Ebû Ubeyde b. Cerrâh (ra): 'Ey Ömer! Allah'ın",
            "  kaderinden mi kaçıyorsun?' diye sordu.",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Hz. Ömer'in (ra) Hikmetli Cevabı ve Çıkarım",
        [
            "• Hz. Ömer (ra): 'Evet! Allah'ın kaderinden,",
            "  yine Allah'ın kaderine kaçıyoruz!' buyurdu.",
            "• Çıkarım: Salgın hastalık nasıl Allah'ın koyduğu",
            "  biyolojik bir yasa (kader) ise; karantina ve",
            "  tedbir alarak hastalıktan korunmak da Allah'ın",
            "  insana verdiği akıl ve irade yasasıdır (kaderdir)!",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


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
    v["bolumler"][3]["gorsel"] = GORSELLER["b4"]
