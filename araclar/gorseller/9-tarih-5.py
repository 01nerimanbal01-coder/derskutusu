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
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Tarihsel Bilginin Üretim Süreci: 5T Yöntemi Aşamaları (TAR.9.1.3)</text>'
    c += _kart(18, 54, 124, 180, "1. Tarama", [
        "• Kaynak arama",
        "• Belge, buluntu,",
        "  arşiv, kronik ve",
        "  sözlü kanıtları",
        "  toplama aşaması."
    ], "#1a5276", "#eaf2f8")
    c += _kart(150, 54, 124, 180, "2. Tasnif", [
        "• Sınıflandırma",
        "• Kaynakları",
        "  zamana, mekâna",
        "  ve konuya göre",
        "  ayırma aşaması."
    ], "#117864", "#e8f8f5")
    c += _kart(282, 54, 124, 180, "3. Tahlil", [
        "• Çözümleme",
        "• Eldeki verilerin",
        "  araştırma için",
        "  yeterli ve elverişli",
        "  olup olmadığı."
    ], "#b9770e", "#fef9e7")
    c += _kart(414, 54, 124, 180, "4. Tenkit", [
        "• Eleştiri süzgeci",
        "• Dış Tenkit (orijinallik)",
        "• İç Tenkit (tarafsızlık",
        "  ve doğruluk)",
        "  denetimi."
    ], "#922b21", "#fdedec")
    c += _kart(546, 54, 116, 180, "5. Terkip", [
        "• Sentez / Yazım",
        "• Doğrulanmış",
        "  bilgileri birleştirip",
        "  tarihsel eseri",
        "  inşa etme."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">1. ve 2. Aşama: Kaynak Tarama ve Tasnif (Sınıflandırma) Türleri</text>'
    c += _kart(18, 54, 314, 170, "Tarama (Kaynak Arama) Süreci", [
        "• Araştırma sorusu belirlendikten sonra konuyla",
        "  ilgili birinci elden (ana) ve ikinci elden kaynaklar",
        "  arşivlerde, kütüphanelerde ve müzelerde taranır.",
        "• Fermanlar, antlaşmalar, sikkeler, kitabeler,",
        "  vakayinameler ve arkeolojik buluntular toplanır."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "Tasnif (Sınıflandırma) Ölçütleri", [
        "• Zamana Göre: Orta Çağ Tarihi, 19. Yüzyıl Tarihi",
        "• Mekâna Göre: Anadolu Tarihi, Orta Asya Tarihi",
        "• Konuya Göre: Bilim Tarihi, İktisat Tarihi, Sanat Tarihi",
        "• Amaç: Yığın hâlindeki verileri düzenli hâle",
        "  getirerek araştırmayı kolaylaştırmaktır."
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#922b21"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">3. ve 4. Aşama: Tahlil (Çözümleme) ve Tenkit (Dış Tenkit - İç Tenkit)</text>'
    c += _kart(18, 54, 314, 175, "Dış Tenkit (Biçimsel / Fiziksel Eleştiri)", [
        "• Kaynağın kendisinin gerçek (orijinal) mi yoksa",
        "  sahte mi olduğunu denetler.",
        "• Eserin adı, yazarı, yazıldığı tarih ve yer,",
        "  kullanılan kâğıt, mürekkep ve yazı karakteri",
        "  dönemin özellikleriyle uyumlu mu diye bakılır."
    ], "#922b21", "#fdedec")
    c += _kart(348, 54, 314, 175, "İç Tenkit (İçerik / Güvenilirlik Eleştirisi)", [
        "• Kaynağın içindeki bilgilerin doğruluğunu ve",
        "  yazarın tarafsızlığını (nesnelliğini) denetler.",
        "• Yazar olayları çarpıtmış mı? Siyasi veya kişisel",
        "  ön yargısı var mı? Farklı kaynaklarla (çapraz",
        "  kontrol) bilgiler birbiriyle örtüşüyor mu?"
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">5. Aşama: Terkip (Sentez) ve Aşamalar Arasındaki Dinamik İlişki</text>'
    c += _kart(18, 54, 314, 165, "Terkip (Sentez / İnşa) Aşaması", [
        "• Tahlil ve tenkit süzgecinden geçerek doğruluğu",
        "  kanıtlanmış bilgilerin bir araya getirilmesidir.",
        "• Neden-sonuç ilişkisi, kronolojik sıra ve dönemin",
        "  şartları (anakronizmden kaçınma) gözetilerek",
        "  tarihsel anlatı / eser kaleme alınır."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 165, "Aşamalar Arası Geri Dönüşlü İlişki", [
        "• Aşamalar birbirinden kopuk değil, birbirini",
        "  tamamlayan sarmal bir süreçtir.",
        "• Tahlil veya tenkit aşamasında kaynak eksikliği",
        "  fark edilirse tekrar TARAMA aşamasına dönülür!",
        "• Yeni bir belge bulunduğunda terkip güncellenir."
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
