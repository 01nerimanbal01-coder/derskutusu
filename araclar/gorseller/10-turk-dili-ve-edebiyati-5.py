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
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Şiir Dinletisi Hazırlama ve Sunma Aşamaları (TDE3.3)</text>'
    c += _kart(18, 54, 206, 170, "1. Hazırlık ve Planlama", [
        "• Dinletinin ana temasını seçme",
        "• Temaya uygun şiirleri ve",
        "  şairleri belirleme",
        "• Sunum akış planı ve dikkat",
        "  çekici giriş metni hazırlama"
    ], "#6c3483", "#f5eef8")
    c += _kart(237, 54, 206, 170, "2. Çok Modlu Tasarım", [
        "• Şiirin duygusuna uygun",
        "  arka plan fon müziği seçme",
        "• Sahne dekoru, ışık ve görsel",
        "  sunum ögelerini kurgulama",
        "• Prova ve zaman yönetimi"
    ], "#1a5276", "#eaf2f8")
    c += _kart(456, 54, 206, 170, "3. Sahne ve Sunum", [
        "• Vurgu, tonlama ve duraklama",
        "• Diksiyon ve boğumlama",
        "• Jest, mimik ve göz teması",
        "• Şiirin ezgisini ve ahengini",
        "  dinleyiciye hissettirme"
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Şiir Okuma (İnşat) Sanatı: Ses, Diksiyon ve Beden Dili İlkeleri</text>'
    c += _kart(18, 54, 314, 175, "Sesin Etkili Kullanımı ve Diksiyon", [
        "• Boğumlama (Artikülasyon): Ünlü ve ünsüzleri",
        "  yutmadan, açık ve net biçimde seslendirme.",
        "• Vurgu ve Tonlama: Şiirin temasına (coşku, hüzün,",
        "  özlem) göre ses perdesini alçaltıp yükseltme.",
        "• Durak (Kesme): Nefes ve anlam duraklarına uyma."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 175, "Beden Dili ve Sahne Hakimiyeti", [
        "• Göz Teması: Kâğıda bağımlı kalmadan izleyicilerle",
        "  canlı ve samimi göz teması kurma.",
        "• Jest ve Mimikler: Yapaylıktan ve abartıdan uzak,",
        "  dizenin duygusuyla uyumlu el-kol ve yüz ifadeleri.",
        "• Duruş: Sahneyi dengeli ve öz güvenli kullanma."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sunum Metinlerinde Düşünceyi Geliştirme ve Geçiş İfadeleri</text>'
    c += _kart(18, 54, 314, 170, "Şiirler Arası Geçiş (Takdim) Konuşması", [
        "• Sunucu, okunacak şiirin yazıldığı dönemi, şairin",
        "  sanat anlayışını veya şiirin yazılış hikâyesini",
        "  kısa ve etkileyici cümlelerle tanıtır.",
        "• Tanımlama, karşılaştırma, örneklendirme ve",
        "  tanık gösterme yollarından yararlanılır."
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 170, "Bağdaşıklık ve Dinleyici İlgisini Tutma", [
        "• Konuşma dikkat çekici bir dize, soru veya",
        "  anekdotla başlatılır (TDE3.3.1).",
        "• Yabancı dillerden alınmış kelimeler yerine",
        "  Türkçe karşılıkları özenle tercih edilir.",
        "• Fon müziği sesin önüne geçmeyecek düzeyde tutulur."
    ], "#1e8449", "#e9f7ef")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Şiir Dinletisi Sürecini Değerlendirme ve Özgün Konuşmacı Kimliği (TDE3.4)</text>'
    c += _kart(18, 54, 314, 165, "Öz ve Akran Değerlendirmesi (TDE3.4.1)", [
        "• Davranış, heyecan kontrolü ve sahne duruşunu",
        "  değerlendirme.",
        "• İçerik kurgusu, şiir-müzik uyumu ve zaman",
        "  yönetimini değerlendirme.",
        "• Dinleyicilerin ve akranların görüşlerini alma."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 165, "Yeni Hedefler ve Paylaşım (TDE3.4.2)", [
        "• Geri bildirimler doğrultusunda gelecekteki",
        "  konuşmalar için yeni gelişim hedefleri belirleme.",
        "• Taklitten uzak \'özgün konuşmacı kimliği\' inşa etme.",
        "• Dinleti kaydını okulun resmî dijital ortamlarında",
        "  veya kültür-sanat etkinliklerinde paylaşma."
    ], "#2874a6", "#eaf2f8")
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
