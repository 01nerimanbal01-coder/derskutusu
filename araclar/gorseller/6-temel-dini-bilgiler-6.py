def _svg(w, h, icerik):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#0284c7", bg="#f0f9ff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="2"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
    s += f'<text x="{x+w/2}" y="{y+20}" font-family="sans-serif" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{baslik}</text>'
    for i, st in enumerate(satirlar):
        s += f'<text x="{x+12}" y="{y+50+i*20}" font-family="sans-serif" font-size="11.5" fill="#1e293b">{st}</text>'
    return s

def gorsel_1():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">İman, İslam ve İhsan Halkalarında Mümin Kimliği</text>'
    ic += _kart(20, 45, 230, 185, "1. Kalpte İman (İnanç)", [
        "• Allah\'ın varlığına ve birliğine",
        "  (Tevhid) gönülden inanmak",
        "• 6 iman esasını tasdik etmek",
        "• Kelime-i Tevhid ve Şehadet",
        "• Kimliğin sarsılmaz kökü"
    ], "#059669", "#ecfdf5")
    ic += _kart(265, 45, 230, 185, "2. Organlarda İslam (İbadet)", [
        "• İmanı ibadetlerle yaşamak",
        "• Namaz, oruç, zekât ve hac",
        "• Dua, şükür ve Kur\'an okuma",
        "• Helal-haram ölçülerine uymak",
        "• Kimliğin görünür gövdesi"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(510, 45, 230, 185, "3. Davranışta İhsan (Ahlak)", [
        "• Allah\'ı görüyormuşçasına",
        "  samimi ve dürüst yaşamak",
        "• Doğruluk, emanet ve adalet",
        "• Saygı, merhamet ve infak",
        "• Kimliğin tatlı meyvesi"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Kur\'an-ı Kerim\'de (Mü\'minûn ve Hucurât Surelerinde) Müminlerin Özellikleri</text>'
    ic += _kart(20, 45, 350, 175, "Mü\'minûn Suresi 1-11. Ayetlerde Müminler", [
        "• Namazlarını huşû (saygı ve samimiyet) içinde kılarlar",
        "• Boş ve faydasız işlerden/sözlerden (lağv) yüz çevirirler",
        "• Zekâtlarını verir, ihtiyaç sahiplerini gözetirler",
        "• İffetlerini ve namuslarını titizlikle korurlar",
        "• Emanetlerine ve verdikleri sözlere (ahitlerine) riayet ederler"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(390, 45, 350, 175, "Hucurât Suresi 10-12. Ayetlerde Kardeşlik Ahlakı", [
        "• \'Müminler ancak kardeştir\' ilkesiyle birbirini severler",
        "• İnsanlarla alay etmez ve kötü lakaplar takmazlar",
        "• Kötü zandan (su-i zan) kaçınır, hüsn-i zan beslerler",
        "• Başkalarının gizli hallerini ve kusurlarını (tecessüs) araştırmazlar",
        "• Birbirlerinin arkasından gıybet (dedikodu) yapmazlar"
    ], "#1d4ed8", "#eff6ff")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Mümin Kimliğini Müşahede Etmenin 4 Temel Değer Boyutu</text>'
    kutular = [
        ("ADALET", "Hak ve hukuku", "gözetmek", "Tarafsız olmak", "#0284c7", "#f0f9ff"),
        ("SAYGI", "Anne-babaya ve", "büyüklere hürmet", "Mahremiyete özen", "#059669", "#ecfdf5"),
        ("SORUMLULUK", "Emaneti korumak", "Sözünde durmak", "Görevini yapmak", "#d97706", "#fffbeb"),
        ("YARDIMSEVERLİK", "Paylaşmak (İnfak)", "Yetimi gözetmek", "Dayanışma içinde", "#9333ea", "#faf5ff")
    ]
    for i, (b, s1, s2, s3, r, bg) in enumerate(kutular):
        x = 20 + i * 184
        ic += f'<rect x="{x}" y="50" width="168" height="165" rx="10" fill="{bg}" stroke="{r}" stroke-width="2"/>'
        ic += f'<rect x="{x}" y="50" width="168" height="30" rx="10" fill="{r}"/>'
        ic += f'<text x="{x+84}" y="70" font-family="sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{b}</text>'
        ic += f'<text x="{x+84}" y="108" font-family="sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s1}</text>'
        ic += f'<text x="{x+84}" y="128" font-family="sans-serif" font-size="11.5" fill="#1e293b" text-anchor="middle">{s2}</text>'
        ic += f'<text x="{x+84}" y="172" font-family="sans-serif" font-size="11.5" font-weight="bold" fill="{r}" text-anchor="middle">{s3}</text>'
    return _svg(760, 240, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Örnek Müminin İletişim Dili ve Öz Değerlendirme</text>'
    ic += _kart(20, 45, 350, 175, "Müminin Günlük İletişim İlkeleri", [
        "• Karşılaştığında \'Esselâmü aleyküm\' diyerek selam verir",
        "• Yemeğe ve işe \'Bismillah\', sonunda \'Elhamdülillah\' der",
        "• Tatlı dilli, güler yüzlü (tebessüm sadakadır) ve naziktir",
        "• Öfkelendiğinde öfkesini yutar ve affedici olur (Âl-i İmrân, 134)",
        "• İyiliği teşvik eder, kötülükten kibarca sakındırır"
    ], "#0369a1", "#f0f9ff")
    ic += _kart(390, 45, 350, 175, "Özü Sözü Bir Olmak (Sıdk ve İhlas)", [
        "• Mümin göründüğü gibi olan, olduğu gibi görünen kişidir",
        "• İnsanların yanında nasıl dürüstse yalnızken de öyledir",
        "• Kul hakkına girmekten ateşten kaçınır gibi sakınır",
        "• Doğayı, su kaynaklarını ve hayvanları Allah\'ın emaneti bilir",
        "• Bulunduğu her ortama güven, huzur ve bereket katar"
    ], "#15803d", "#f0fdf4")
    return _svg(760, 240, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4()
}

def uygula(v):
    hedefler = [0, 1, 2, 4]
    anahtarlar = ["b1", "b2", "b3", "b4"]
    for idx, k in zip(hedefler, anahtarlar):
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[k]
