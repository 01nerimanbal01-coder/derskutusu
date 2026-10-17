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
        '18. YÜZYIL DOĞU CEPHESİ: OSMANLI - İRAN MÜCADELELERİ VE ANTLAŞMALARI</text>'
    )
    ic += _kart(
        20, 42, 230, 198,
        "1724 İstanbul Antlaşması",
        [
            "• İran'daki (Safevî) iç karışıklıklar",
            "  üzerine Osmanlı ve Rusya",
            "  Kafkasya'da karşı karşıya geldi.",
            "• Fransa arabuluculuğuyla imzalandı.",
            "• İran toprakları Osmanlı ile",
            "  Rusya arasında paylaşıldı.",
            "• İLK Osmanlı-Rus İttifakıdır!",
        ],
        "#2563eb", "#eff6ff"
    )
    ic += _kart(
        265, 42, 230, 198,
        "1732 Ahmed Paşa ve 1736 İstanbul",
        [
            "• 1732 Ahmed Paşa Ant.: Tebriz",
            "  İran'a bırakıldı, Kafkasya",
            "  Osmanlı'da kaldı (I. Mahmud).",
            "• İran'da Nadir Şah, Safevî",
            "  hanedanına son verip Afşar",
            "  hanedanını kurdu.",
            "• 1736 İstanbul Ant. imzalandı.",
        ],
        "#d97706", "#fffbeb"
    )
    ic += _kart(
        510, 42, 230, 198,
        "1746 Kerden (II. Kasr-ı Şirin)",
        [
            "• Nadir Şah ile yapılan son",
            "  büyük savaşlar sonucunda",
            "  1746'da imzalandı.",
            "• 1639 Kasr-ı Şirin Antlaşması",
            "  sınırlarına geri dönüldü.",
            "• Bundan dolayı 'II. Kasr-ı Şirin'",
            "  olarak adlandırılır.",
        ],
        "#059669", "#ecfdf5"
    )
    return _svg(760, 265, ic)


def gorsel_2():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'KARADENİZ HÂKİMİYETİNİN VE KIRIM\'IN KADEMELİ KAYIP SÜRECİ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Karadeniz Statüsünün Değişimi (1700-1774)",
        [
            "• 1700 İstanbul: Azak Kalesi Rusya'ya verildi →",
            "  Rusya Karadeniz'e ilk adımını attı.",
            "• 1711 Prut: Azak Kalesi geri alındı → Karadeniz",
            "  yeniden tamamen Osmanlı kontrolüne geçti.",
            "• 1739 Belgrad: Rusya'nın Karadeniz'de savaş ve",
            "  ticaret gemisi bulunduramayacağı son kez onaylandı.",
            "• 1774 Küçük Kaynarca: Türk gölü olma özelliği BİTTİ!",
        ],
        "#0284c7", "#f0f9ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Kırım'ın Elden Çıkış Aşamaları (Şifresi: KAY)",
        [
            "• 1) 1774 Küçük Kaynarca Antlaşması: Kırım,",
            "  Osmanlı'dan koparılıp 'bağımsız' yapıldı (dini",
            "  bakımdan Osmanlı Halifesine bağlı kaldı).",
            "• 2) 1779 Aynalıkavak Tenkihnamesi: Rus yanlısı",
            "  Şahin Giray'ın Kırım Hanlığı tanındı.",
            "• 3) 1783: Rusya Kırım'ı resmen İLHAK ETTİ.",
            "• 4) 1792 Yaş Antlaşması: Kırım'ın Rusya'ya ait",
            "  olduğu Osmanlı tarafından resmen kabul edildi.",
        ],
        "#dc2626", "#fef2f2"
    )
    return _svg(760, 265, ic)


def gorsel_3():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        'RUSYA VE AVUSTURYA\'NIN OSMANLI\'YI PAYLAŞMA PROJELERİ (1780\'LER)</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "1. Grek Projesi (Çariçe II. Katerina)",
        [
            "• Rus Çariçesi II. Katerina tarafından hazırlandı.",
            "• Amaç: Türkleri Avrupa'dan ve İstanbul'dan",
            "  tamamen çıkarmak.",
            "• İstanbul merkezli ve başında Rus Prensi",
            "  Konstantin'in bulunacağı kukla bir 'Grek (Bizans)",
            "  Devleti' kurmak.",
            "• Rusya'yı doğrudan sıcak denizlere indirmek.",
        ],
        "#7c3aed", "#f5f3ff"
    )
    ic += _kart(
        395, 42, 345, 198,
        "2. Dakya Projesi (Rusya + Avusturya)",
        [
            "• Rusya ile Avusturya İmparatoru II. Joseph",
            "  arasında yapılan gizli paylaşım planıdır.",
            "• Amaç: Osmanlı egemenliğindeki Eflak, Boğdan",
            "  ve Besarabya topraklarında Rusya ve Avusturya'ya",
            "  bağlı tampon bir 'Dakya Devleti' kurmak.",
            "• Sırbistan, Bosna ve Hersek'i ise Avusturya'ya",
            "  bırakarak Balkanlar'ı paylaşmak.",
        ],
        "#d97706", "#fffbeb"
    )
    return _svg(760, 265, ic)


def gorsel_4():
    ic = (
        '<rect x="5" y="5" width="750" height="255" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
        '<text x="380" y="28" fill="#0f172a" font-size="14.5" font-weight="bold" text-anchor="middle">'
        '1683-1789 MÜCADELELERİNİN GENEL SONUÇLARI: KILIÇTAN KALEME GEÇİŞ</text>'
    )
    ic += _kart(
        20, 42, 345, 198,
        "Siyasi ve Diplomatik Dönüşüm",
        [
            "• Saldırı ve fetih politikası sona erdi; önce",
            "  'kaybedilenleri geri alma' (1699-1718), sonra",
            "  'mevcut toprakları koruma' politikasına geçildi.",
            "• Seyfiye (asker) sınıfının ağırlığı azalırken,",
            "  Kalemiye (bürokrasi/diplomasi) sınıfı ve",
            "  Reisülküttaplık makamı ön plana çıktı.",
            "• Avrupa'da geçici elçilikler açıldı (Lale Devri).",
        ],
        "#059669", "#ecfdf5"
    )
    ic += _kart(
        395, 42, 345, 198,
        "Askerî, Ekonomik ve Toplumsal Sonuçlar",
        [
            "• Batı tarzı ilk askeri ıslahatlar başladı",
            "  (Humbaracı Ahmed Paşa, Hendesehane, Baron de Tott).",
            "• 1740'ta Fransa'ya verilen kapitülasyonlar",
            "  sürekli hale getirildi; 1774'te Rusya'ya da verildi.",
            "• Uzun savaşların finansmanı için Malikâne (boyu",
            "  iltizam) ve 1775'te Esham (iç borçlanma) uygulandı.",
            "• Kaybedilen yerlerden Anadolu'ya göçler yaşandı.",
        ],
        "#2563eb", "#eff6ff"
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
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
