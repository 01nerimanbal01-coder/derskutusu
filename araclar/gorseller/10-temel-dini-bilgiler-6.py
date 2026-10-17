def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;'
        f'background:#fafcff;border:1px solid #e2e8f0;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#2563eb", bg="#eff6ff"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="10" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+19}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*19}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{s}</text>'
    return b


def gorsel_1():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'İslam’da İman ve Amel Bütünlüğü: Kalpten Eyleme Yansıyan Kulluk</text>'
        + _kart(20, 42, 200, 142, "1. Kalp ile Tasdik (Öz)", [
            "• İmanın esası ve temelidir",
            "• Allah’ın (cc) varlığını, birliğini",
            "  ve peygamberin getirdiklerini",
            "  gönülden onaylamaktır",
            "• Ağacın kökü gibidir"
        ], "#2563eb", "#eff6ff")
        + _kart(240, 42, 200, 142, "2. Dil ile İkrar (Beyan)", [
            "• Kalpteki imanı Kelime-i",
            "  Tevhit ve Kelime-i Şehadet",
            "  ile sözlü olarak açıklamaktır",
            "• Müslüman toplumun bir",
            "  ferdi olmanın göstergesidir"
        ], "#059669", "#ecfdf5")
        + _kart(460, 42, 200, 142, "3. Salih Amel (Meyve)", [
            "• İmanın ibadet ve güzel",
            "  ahlak olarak davranışa",
            "  dönüşmesidir (Asr Suresi)",
            "• Ağacın dalları ve meyvesi",
            "  gibi imanı korur ve besler"
        ], "#d97706", "#fffbeb")
    )
    return _svg(680, 198, ic)


def gorsel_2():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#065f46" text-anchor="middle">'
        'İnanç Bakımından İnsanların Sınıflandırılması</text>'
        + _kart(20, 42, 200, 140, "1. Mümin (İman Eden)", [
            "• Allah’a (cc) ve Hz. Peygamber’in",
            "  bildirdiği esaslara kalbiyle",
            "  inanıp diliyle ikrar eden",
            "• Güven veren ve güvenilen",
            "  insan demektir"
        ], "#059669", "#ecfdf5")
        + _kart(240, 42, 200, 140, "2. Kâfir / Müşrik (İnkâr)", [
            "• Kâfir: İman esaslarını",
            "  bilerek reddeden ve örten",
            "• Müşrik: Allah’a (cc) ortak",
            "  koşan kimse (Şirk en büyük",
            "  zulümdür - Lokmân 13)"
        ], "#dc2626", "#fef2f2")
        + _kart(460, 42, 200, 140, "3. Münafık (İkiyüzlü)", [
            "• Kalbiyle inanmadığı halde",
            "  çıkarı için diliyle ”inandım”",
            "  diyen ikiyüzlü kimse",
            "• Nifak: İç ve dışın birbirine",
            "  uymaması hastalığıdır"
        ], "#7c3aed", "#f5f3ff")
    )
    return _svg(680, 195, ic)


def gorsel_3():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#7c2d12" text-anchor="middle">'
        'Taklîdî İman ve Tahkîkî İman Karşılaştırması</text>'
        + _kart(25, 42, 300, 142, "Taklîdî İman (Çevreyi Taklit)", [
            "• Delillere ve araştırmaya dayanmadan, sadece",
            "  aileden ve çevreden görüldüğü gibi inanmaktır",
            "• Geçerlidir ancak şüphe ve itirazlar karşısında",
            "  sarsılma tehlikesi taşır",
            "• İlim ve tefekkürle güçlendirilmelidir"
        ], "#ea580c", "#fff7ed")
        + _kart(355, 42, 300, 142, "Tahkîkî İman (Bilinçli ve Delilli İman)", [
            "• Akli ve naklî delilleri araştırarak, sorgulayarak",
            "  ve kalben mutmain olarak (iç huzuruyla) inanmaktır",
            "• Şüphe rüzgârları karşısında sarsılmaz",
            "• İnsanı salih amele, ihsana ve güzel ahlaka",
            "  yönelten olgun iman seviyesidir"
        ], "#0284c7", "#f0f9ff")
    )
    return _svg(680, 196, ic)


def gorsel_4():
    ic = (
        '<text x="340" y="26" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1e3a8a" text-anchor="middle">'
        'Asr Suresi Işığında İnsanlığı Hüsrandan Kurtaran 4 Temel İlke</text>'
        + _kart(25, 42, 300, 138, "Bireysel Kulluk Boyutu", [
            "• 1. İman Etmek (الَّذِينَ آمَنُوا): Sağlam tevhit inancı",
            "• 2. Salih Amel İşlemek (وَعَمِلُوا الصَّالِحَاتِ):",
            "  İmanı ibadet, dürüstlük ve iyilikle hayata geçirmek"
        ], "#2563eb", "#eff6ff")
        + _kart(355, 42, 300, 138, "Toplumsal Sorumluluk Boyutu", [
            "• 3. Hakkı Tavsiye Etmek (وَتَوَاصَوْا بِالْحَقِّ): Doğruluğu",
            "  ve adaleti yaymak",
            "• 4. Sabrı Tavsiye Etmek (وَتَوَاصَوْا بِالصَّبْرِ): Zorluklara",
            "  ve günahlara karşı birlikte direnmek"
        ], "#16a34a", "#f0fdf4")
    )
    return _svg(680, 192, ic)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    bolumler = v.get("bolumler", [])
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[k]
