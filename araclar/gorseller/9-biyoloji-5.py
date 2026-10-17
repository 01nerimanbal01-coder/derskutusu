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
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Bilimsel Araştırma Sürecinin Basamakları</text>'
    c += _kart(18, 54, 206, 175, "1. Gözlem ve Problem", [
        "• Nitel Gözlem: Beş duyu ile",
        "  yapılır, özneldir.",
        "• Nicel Gözlem: Ölçü aleti ile",
        "  yapılır, nesnel ve sayısaldır.",
        "• Merak edilen bilimsel",
        "  problem net biçimde tanımlanır."
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 175, "2. Hipotez ve Tahmin", [
        "• Hipotez: Probleme sunulan",
        "  geçici ve sınanabilir çözüm.",
        "• Tahmin: \'Eğer ... ise ... dır\'",
        "  kalıbıyla kurulan mantıksal",
        "  çıkarım cümlesidir.",
        "• Verilerle test edilmeye hazırdır."
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 175, "3. Kontrollü Deney ve Sonuç", [
        "• Kontrollü deneyle hipotez",
        "  sınanır ve veriler kaydedilir.",
        "• Desteklenmezse hipotez",
        "  değiştirilir / yenilenir.",
        "• Desteklenirse çıkarım yapılır",
        "  ve bilim dünyasıyla paylaşılır."
    ], "#6c3483", "#f5eef8")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Kontrollü Deneyde Değişken Türleri (Bağımsız, Bağımlı ve Kontrol)</text>'
    c += _kart(18, 54, 206, 170, "Bağımsız Değişken (Neden)", [
        "• Araştırmacının etkisini",
        "  test etmek amacıyla",
        "  bilerek değiştirdiği",
        "  faktördür (deneyde 1 tane).",
        "• Örn: Işık şiddeti / Sıcaklık"
    ], "#1a5276", "#eaf2f8")
    c += _kart(237, 54, 206, 170, "Bağımlı Değişken (Sonuç)", [
        "• Bağımsız değişkene bağlı",
        "  olarak değişen ve",
        "  deney sonunda ölçülen",
        "  sonuç değişkenidir.",
        "• Örn: Fotosentez hızı / Boy"
    ], "#b9770e", "#fef9e7")
    c += _kart(456, 54, 206, 170, "Kontrol Değişkeni (Sabit)", [
        "• Deney ve kontrol gruplarında",
        "  eşit / sabit tutulan tüm",
        "  diğer etkenlerdir.",
        "• Örn: Su miktarı, toprak",
        "  türü, bitki türü ve yaşı"
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Bilim Etiğinin Temel İlkeleri ve Araştırma Araçları (BİY.9.1.3)</text>'
    c += _kart(18, 54, 314, 170, "Bilim Etiğine Uygunluk İlkeleri", [
        "• Dürüstlük ve Açıklık: Verileri olduğu gibi sunma.",
        "• Tarafsızlık: Ön yargıdan ve çıkar çatışmasından uzak.",
        "• Kaynak Gösterme: Başka araştırmacıların emeğine",
        "  saygı duyarak atıf yapma (intihalden kaçınma).",
        "• Canlılara ve Çevreye Saygı: Deney hayvanlarına",
        "  ve insan deneklere zarar vermeme, Etik Kurul izni."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "Bilim Etiğini Denetleme Araçları", [
        "• Etik Kurul Onay Belgeleri (Klinik/Hayvan deneyleri)",
        "• Aydınlatılmış Onam Formu (Gönüllü katılımcı izni)",
        "• İntihal (Benzerlik) Tespit Yazılımları",
        "• Hakemli Bilimsel Dergi Değerlendirme Süreçleri",
        "• Açık Veri ve Laboratuvar Kayıt Defterleri"
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#922b21"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Bilimsel Araştırmalarda Etik İhlal Türleri (Sakınılması Gereken Davranışlar)</text>'
    c += _kart(18, 54, 206, 170, "İntihal (Aşırma)", [
        "• Başkalarının fikirlerini,",
        "  verilerini veya yazılarını",
        "  kaynak göstermeden",
        "  kendi eseriymiş gibi",
        "  kullanmaktır."
    ], "#922b21", "#fdedec")
    c += _kart(237, 54, 206, 170, "Uydurma ve Çarpıtma", [
        "• Uydurma (Fabrikasyon): Hiç",
        "  yapılmamış deneyin verisini",
        "  masa başında üretmek.",
        "• Çarpıtma (Falsifikasyon):",
        "  Verileri hipoteze uydurmak."
    ], "#b9770e", "#fef9e7")
    c += _kart(456, 54, 206, 170, "Diğer Etik İhlaller", [
        "• Duplikasyon: Aynı makaleyi",
        "  birden çok dergide basmak.",
        "• Dilimleme (Salamizasyon):",
        "  Bir araştırmayı yapay bölmek.",
        "• Haksız Yazarlık eklemek."
    ], "#6c3483", "#f5eef8")
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
