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
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Allah (cc) İle İletişim Yolları: Vahiy, İbadet ve Dua (DKAB.9.1.3)</text>'
    c += _kart(18, 54, 206, 170, "Vahiy (Kur\'an-ı Kerim)", [
        "• Allah\'tan (cc) insana doğru",
        "  gerçekleşen ilahi hitaptır.",
        "• İnsana yaratılış amacını,",
        "  inanç esaslarını ve ahlaki",
        "  ilkeleri bildirir."
    ], "#1a5276", "#eaf2f8")
    c += _kart(237, 54, 206, 170, "İbadet (Kulluk Bilinci)", [
        "• İnsandan Allah\'a (cc) yönelen",
        "  saygı, itaat ve bağlılıktır.",
        "• Dar Anlamı: Namaz, oruç,",
        "  zekât, hac gibi belirli erkanlar.",
        "• Geniş Anlamı: Allah rızası için",
        "  yapılan her güzel/salih davranış."
    ], "#1e8449", "#e9f7ef")
    c += _kart(456, 54, 206, 170, "Dua (Samimi Yakarış)", [
        "• Kulun kendi acizliğini bilerek",
        "  Yüce Yaratıcıya gönülden",
        "  yönelmesi ve istemesidir.",
        "• İbadetin özü ve ruhudur.",
        "• Zaman ve mekân sınırı yoktur."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">İbadetin Kabul Şartları ve İman - İbadet - Ahlak Bütünlüğü</text>'
    c += _kart(18, 54, 314, 170, "İbadetin Kabul Olmasının 3 Temel Şartı", [
        "1. İman: İbadetlerin geçerli olması için öncelikle",
        "   tevhid inancına sahip olmak gerekir.",
        "2. İhlas (Samimiyet): Gösterişten (riyadan) uzak,",
        "   yalnızca Allah\'ın (cc) rızasını kazanmak için yapmak.",
        "3. Sünnete Uygunluk: Hz. Peygamber\'in (sav) öğrettiği",
        "   ve uyguladığı biçimde yerine getirmek."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "İman, İbadet ve Güzel Ahlak İlişkisi", [
        "• İman kalpte kök salan bir ağaç gibidir; ibadetler",
        "  bu ağacı besleyen su, güzel ahlak ise meyvesidir.",
        "• Namaz insanı hayasızlıktan ve kötülükten alıkoyar.",
        "• Oruç sabrı ve irade eğitimini; zekât paylaşmayı;",
        "  hac ise eşitlik ve kardeşlik bilincini güçlendirir."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Duanın Türleri (Kavlî ve Fiilî Dua) ve Dua Adabı</text>'
    c += _kart(18, 54, 314, 170, "Kavlî (Sözlü) Dua ve Fiilî (Eylemsel) Dua", [
        "• Fiilî Dua: İnsanın ulaşmak istediği sonuç için",
        "  üzerine düşen tüm sebeplere başvurması ve",
        "  gayret göstermesidir (Örn: Sınava çalışmak,",
        "  tarlayı sürüp tohum ekmek, tedavi olmak).",
        "• Kavlî Dua: Sebepleri yerine getirdikten sonra",
        "  dil ve kalp ile Allah\'tan (cc) hayırlı sonuç istemektir."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 170, "Kur\'an ve Sünnete Göre Dua Adabı", [
        "• Duaya Allah\'a hamd ve Peygamberimize salavatla",
        "  başlamak; Esmaülhüsna (güzel isimler) ile yakarmak.",
        "• Korku ile ümit (havf ve reca) arasında, gizlice",
        "  ve alçakgönüllülükle (tazarru ile) dua etmek.",
        "• Yalnızca sıkıntılı zamanlarda değil, bolluk ve",
        "  rahatlık zamanlarında da dua ve şükre devam etmek."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#2874a6"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">İbadet ve Duanın Bireysel ve Toplumsal Hayata Yansımaları</text>'
    c += _kart(18, 54, 314, 165, "Bireysel Hayata Kazandırdıkları", [
        "• İnsana iç huzuru, güven ve ümit aşılar; yalnızlık",
        "  ve çaresizlik duygusunu ortadan kaldırır.",
        "• Zaman bilinci, öz disiplin ve sorumluluk duygusu",
        "  kazandırır.",
        "• Hayatın zorluklarına karşı sabır ve metanet verir."
    ], "#2874a6", "#eaf2f8")
    c += _kart(348, 54, 314, 165, "Toplumsal Hayata Kazandırdıkları", [
        "• Cemaatle kılınan namazlar ve hac ibadeti toplumsal",
        "  kaynaşmayı, birlik ve kardeşliği pekiştirir.",
        "• Zekât ve sadaka ibadetleri zengin ile fakir",
        "  arasındaki sevgi bağını ve sosyal adaleti güçlendirir.",
        "• Müminlerin birbirine hayır duası empatiyi artırır."
    ], "#1e8449", "#e9f7ef")
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
