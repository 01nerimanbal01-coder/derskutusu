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
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Harita Okuma ve Uygulama Süreci (COĞ.9.2.1)</text>'
    c += _kart(18, 54, 206, 170, "1. Harita Bileşenlerini Okuma", [
        "• Başlık: Haritanın kullanım amacı",
        "• Lejant: Sembol, renk ve işaretler",
        "• Ölçek: Küçültme oranı ve uzunluk",
        "• Koordinat Ağı: Mutlak konum",
        "• Yön Oku: Coğrafi yön tayini"
    ], "#1a5276", "#eaf2f8")
    c += _kart(237, 54, 206, 170, "2. İlişkileri Çözümleme", [
        "• Fiziki yapı (yükselti, eğim, akarsu)",
        "  ile beşerî dağılış (yerleşme,",
        "  ulaşım, tarım) arasındaki",
        "  nedensellik bağını kurma.",
        "• Mekânsal örüntüyü fark etme."
    ], "#117864", "#e8f8f5")
    c += _kart(456, 54, 206, 170, "3. Çıkarım ve Tahmin", [
        "• Farklı yıllara ait haritalardan",
        "  mekânsal değişimi yorumlama.",
        "• Afet riski, arazi kullanımı",
        "  veya güzergâh seçimi için",
        "  coğrafi çıkarımda bulunma."
    ], "#b9770e", "#fef9e7")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 250
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1e8449"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Fiziki Haritalarda Renk Basamakları ve İzohips (Eş Yükselti) İlkeleri</text>'
    c += _kart(18, 54, 314, 180, "Renklendirme Yöntemi (Yükselti Basamakları)", [
        "• 0 - 500 m: Yeşil ve tonları (Alçak ovalar)",
        "• 500 - 1000 m: Sarı (Platolar ve orta yükselti)",
        "• 1000 - 1500 m: Turuncu (Yüksek platolar)",
        "• 1500 m ve üzeri: Kahverengi (Sıradağlar)",
        "• Denizlerde açık maviden koyu maviye derinlik artar.",
        "• Dikkat: Renkler bitki örtüsünü DEĞİL yükseltiyi gösterir!"
    ], "#1e8449", "#e9f7ef")
    c += _kart(348, 54, 314, 180, "İzohips (Eş Yükselti) Haritalarını Yorumlama", [
        "• Eğrilerin sıklaştığı yerde EĞİM FAZLA (dik yamaç),",
        "  seyrekleştiği yerde EĞİM AZDIR (yatay/düzlük).",
        "• Akarsuyun her iki yamacındaki komşu iki izohipsin",
        "  yükseltisi birbirine eşittir.",
        "• V şeklindeki büklümlerin sivri ucu yüksek yeri",
        "  gösteriyorsa VADİ, alçak yeri gösteriyorsa SIRTTIR."
    ], "#2874a6", "#eaf2f8")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#6c3483"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Topografya Haritalarında Yer Şekilleri: Vadi, Sırt, Boyun, Çukur ve Delta</text>'
    c += _kart(18, 54, 314, 175, "Tepe, Boyun, Çanak ve Falez", [
        "• Tepe (Doruk): İç içe kapalı eğrilerin merkezi.",
        "• Boyun: İki tepe arasında kalan geçit alanı.",
        "• Kapalı Çukur (Çanak): İçe doğru ok (→) işaretiyle",
        "  gösterilen krater veya obruk çukurlukları.",
        "• Falez (Yalıyar): İzohipslerin kıyıda üst üste çakışması."
    ], "#6c3483", "#f5eef8")
    c += _kart(348, 54, 314, 175, "Delta Ovası ve Haliç Ayrımı", [
        "• Delta Ovası: Akarsuyun taşıdığı alüvyonlarla kıyı",
        "  çizgisinin denize doğru üçgen çıkıntı yapmasıdır.",
        "• Haliç: Gelgit genliği yüksek okyanus kıyılarında",
        "  akarsu ağzının karaya doğru girinti yapmasıdır.",
        "• Delta olan kıyıda haliç, haliç olan kıyıda delta olmaz!"
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 235
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Harita Uygulamaları: Uzunluk, Eğim Hesaplama ve Mekânsal Dağılış Yorumu</text>'
    c += _kart(18, 54, 314, 165, "Uzunluk ve Eğim Uygulamaları", [
        "• Gerçek Uzunluk (GU) = Harita Uzunluğu × Ölçek Paydası",
        "• Eğim (%) = (Yükselti Farkı / Yatay Uzaklık) × 100",
        "• Eğim (‰) = (Yükselti Farkı / Yatay Uzaklık) × 1000",
        "• Dikkat: Eğim hesabında yükselti farkı (h) ile yatay",
        "  uzaklık (L) mutlaka AYNI BİRİME (metre) çevrilir!"
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 165, "Tematik ve Koroplet/Noktalama Haritaları", [
        "• Noktalama Yöntemi: Nüfus, tarım ürünü veya sanayi",
        "  tesislerinin yoğunluk ve dağılışını noktalarla gösterir.",
        "• Koroplet (Dereceli Renklendirme): İdari sınırlar",
        "  içinde oran/yoğunluk verilerini renk tonlarıyla sunar.",
        "• Akış (Çizgi) Haritaları: Göç, ticaret ve ulaşım yönü."
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
