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
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Üçgenin Alan Bağıntısı ve Üçgen Türlerine Göre Yükseklik Konumu</text>'
    c += _kart(18, 54, 206, 175, "Dar Açılı Üçgen", [
        "• Alan(ABC) = (a · ha) / 2",
        "  = (b · hb) / 2 = (c · hc) / 2",
        "• Üç yüksekliğin üçü de",
        "  üçgenin İÇ bölgesindedir.",
        "• Diklik merkezi üçgenin",
        "  iç bölgesinde yer alır."
    ], "#1e8449", "#e9f7ef")
    c += _kart(237, 54, 206, 175, "Dik Açılı Üçgen", [
        "• Dik kenarlar birbirinin",
        "  yüksekliğidir!",
        "• Alan = (Dik kenarlar çarpımı)/2",
        "  = (Hipotenüs · h) / 2",
        "• Öklid Alan Bağıntısı:",
        "  b · c = a · ha"
    ], "#2874a6", "#eaf2f8")
    c += _kart(456, 54, 206, 175, "Geniş Açılı Üçgen", [
        "• Dar açılara ait iki yükseklik",
        "  üçgenin DIŞ bölgesine,",
        "  tabanın uzantısına iner!",
        "• Alan yine yalnızca taban (a)",
        "  ile dış yüksekliğin (ha)",
        "  çarpımının yarısıdır."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Kenar ve Yükseklik Değişiminin Üçgenin Alanına Etkisi (10.1.3)</text>'
    c += _kart(18, 54, 314, 170, "Yükseklik Sabit İken Taban Değişimi", [
        "• Yüksekliği (h) eşit olan iki üçgenin alanları",
        "  oranı, taban uzunlukları oranına eşittir:",
        "  Alan(ABD) / Alan(ADC) = |BD| / |DC|",
        "• Kenarortay, üçgenin alanını İKİ EŞİT parçaya böler.",
        "• Taban k katına çıkarsa alan da k katına çıkar."
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "Taban Sabit İken Yükseklik Değişimi", [
        "• Taban uzunluğu (a) eşit olan iki üçgenin alanları",
        "  oranı, o tabana ait yükseklikleri oranına eşittir:",
        "  Alan(ABC) / Alan(DBC) = h1 / h2",
        "• Paralel iki doğru arasında tabanı sabit kalan",
        "  üçgenin tepe noktası kaydırılsa da ALANI DEĞİŞMEZ!"
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Sinüs Alan Formülü, Eşkenar Üçgen Alanı ve Oran Kuralları</text>'
    c += _kart(18, 54, 314, 170, "Sinüs Alan Bağıntısı ve Eşkenar Üçgen", [
        "• İki kenarı (b, c) ve arasındaki açısı (A) bilinen",
        "  üçgenin alanı: Alan = (1/2) · b · c · sin(A)",
        "• Çünkü yüksekliğin trigonometrik karşılığı",
        "  hb = c · sin(A) değeridir.",
        "• Eşkenar Üçgen Alanı (a kenarlı): (a² · kök3) / 4"
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 170, "Hem Taban Hem Yükseklik Birlikte Değişirse", [
        "• Bir üçgenin tabanı m katına, o tabana ait",
        "  yüksekliği n katına çıkarılırsa yeni alan",
        "  (m · n) katına çıkar!",
        "• Örnek: Taban %20 artırılıp (1,2 katı), yükseklik",
        "  %10 azaltılırsa (0,9 katı) -> Yeni alan 1,08 (%8 artar)."
    ], "#1a5276", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Ağırlık Merkezi, İç Teğet Çember ve Benzerlik-Alan İlişkisi</text>'
    c += _kart(18, 54, 314, 165, "Ağırlık Merkezi (G) ve İç Teğet Çember (I)", [
        "• Üç kenarortayın kesiştiği ağırlık merkezi (G),",
        "  üçgenin alanını 6 EŞ ALANLI (S) üçgene ayırır.",
        "• G noktası köşelerle birleştirilirse 3 eş alan (2S) oluşur.",
        "• İç açıortayların kesişim noktası (I) köşelerle",
        "  birleştirilirse alanlar kenarlarla orantılıdır (a:b:c)."
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 165, "Benzer Üçgenlerde Alanlar Oranı (k²)", [
        "• Benzerlik oranı k olan iki üçgende hem taban",
        "  hem de yükseklik k katına çıktığı için:",
        "  Alanlar Oranı = k · k = k² (Benzerlik oranının karesi).",
        "• Orta taban üçgeni S ve 3S (1/4 oranında) böler."
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
