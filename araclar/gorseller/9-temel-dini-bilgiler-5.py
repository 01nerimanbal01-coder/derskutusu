def _svg(w, h, icerik):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px;height:auto;display:block;margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">{icerik}</svg>'

def _kart(x, y, w, h, baslik, satirlar, renk="#1a5276", bg="#eaf2f8"):
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>'
    b += f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="10" fill="{renk}"/>'
    b += f'<text x="{x+w//2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>'
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*20}" font-size="11.2" fill="#1c2833">{s}</text>'
    return b

def gorsel_1():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Allah (cc), İnsan ve Kâinat İlişkisinde Deliller (TDB.9.1.2)</text>'
    c += _kart(18, 54, 314, 170, "Aklî Deliller (Tefekkür ve Gözlem)", [
        "• İnsanın aklı, mantığı ve kâinattaki gözlemleriyle",
        "  ulaştığı delillerdir.",
        "• Gaye ve Nizam Delili: Evrendeki hassas ölçü ve düzen.",
        "• İhtira (Hudûs) Delili: Yoktan yaratılış ve değişim.",
        "• Fıtrat Delili: İnsanın doğuştan inanma eğilimi."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 170, "Naklî Deliller (Vahiy ve Sünnet)", [
        "• Kur\'an-ı Kerim ayetleri ve Hz. Peygamber\'in (sav)",
        "  sahih hadisleriyle bildirilen kesin delillerdir.",
        "• İhlâs, Âyetel-Kürsî, Haşr, Mülk ve Yâsîn sureleri.",
        "• Aklî deliller ile naklî deliller birbirini destekler;",
        "  Kur\'an ayetleri sürekli akletmeye çağırır."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Kâinattaki Aklî Deliller: Nizam (Düzen), İnayet ve Hudûs Delilleri</text>'
    c += _kart(18, 54, 206, 175, "Nizam (Düzen ve Ölçü) Delili", [
        "• Gezegenlerin yörüngeleri,",
        "  gece-gündüz döngüsü, su ve",
        "  oksijen dengesi tesadüfen",
        "  oluşamaz.",
        "• \'Biz her şeyi bir ölçüye (kadere)",
        "  göre yarattık.\' (Kamer, 54/49)"
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 175, "İnayet (Uygunluk) Delili", [
        "• Evrendeki tüm şartların",
        "  insanın ve canlıların",
        "  yaşamasına en uygun",
        "  biçimde hazırlanmasıdır.",
        "• Atmosfer kalkanı, anne sütü,",
        "  toprağın verimliliği."
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 175, "Hudûs (Sonradan Var Olma)", [
        "• Evrendeki her varlık",
        "  sonradan var olmuştur",
        "  (hâdistir).",
        "• Sonradan var olan her şey,",
        "  ezelî ve ebedî bir Yaratıcıya",
        "  (Muhdis\'e) muhtaçtır."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">İlkeli Yaşamak: Tevhid, Adalet, Emanet ve Sorumluluk Bilinci</text>'
    c += _kart(18, 54, 314, 170, "İlkeli Yaşamanın Temel Esasları", [
        "• Hayatın başıboş olmadığını bilerek inanç ve",
        "  ahlak ilkelerine göre tutarlı bir ömür sürmektir.",
        "• \'Emrolunduğun gibi dosdoğru ol (istikamet)!\'",
        "  (Hûd, 11/112) ayetini rehber edinmektir.",
        "• Söz ile davranış arasında uyum sağlamaktır."
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 170, "İnsanın Üç Boyutlu Sorumluluğu", [
        "1. Allah\'a (cc) Karşı: İman, ibadet, şükür ve itaat.",
        "2. Kendisine ve İnsanlara Karşı: Aklını ve sağlığını",
        "   korumak, adaletli olmak, kul hakkına girmemek.",
        "3. Kâinata (Çevreye) Karşı: Doğayı Allah\'ın emaneti",
        "   bilerek imar etmek, israf ve fesattan kaçınmak."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">İki Kitap Metaforu: Tekvinî Ayetler (Kâinat) ve Tenzilî Ayetler (Kur\'an)</text>'
    c += _kart(18, 54, 314, 165, "Kâinat Kitabı (Tekvinî Ayetler)", [
        "• Allah\'ın (cc) kudret sıfatıyla yarattığı evren,",
        "  okunması gereken büyük bir kitaptır.",
        "• Güneş, ay, yıldızlar, dağlar ve insanın kendi",
        "  yaratılışı birer \'kevni (tekvinî) ayet\'tir.",
        "• Gözlem, bilim ve tefekkürle okunur."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 165, "Kur\'an-ı Kerim (Tenzilî / Kavlî Ayetler)", [
        "• Allah\'ın (cc) kelam sıfatıyla indirdiği vahiydir.",
        "• Kâinat kitabının nasıl okunacağını ve yaratılışın",
        "  amacını açıklayan ilahi rehberdir.",
        "• İlk emri \'Oku! (İkra)\' hem vahyi hem de",
        "  kâinatı Yaratan Rabbin adıyla okumayı emreder."
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}

def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for i, k in eş.items():
        if i < len(v.get("bolumler", [])):
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
