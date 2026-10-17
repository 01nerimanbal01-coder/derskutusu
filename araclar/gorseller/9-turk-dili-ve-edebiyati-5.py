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
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Şiirden Betimleme Paragrafına Dönüşüm Süreci (TDE4.3)</text>'
    c += _kart(18, 54, 206, 170, "1. Şiiri Çözümleme", [
        "• Tema ve atmosferi belirle",
        "• İmge ve sembolleri çöz",
        "• Mekân, zaman ve varlık",
        "  ayrıntılarını tespit et",
        "• Duyusal ögeleri ayıkla"
    ], "#6c3483", "#f5eef8")
    c += _kart(237, 54, 206, 170, "2. Taslak Planlama", [
        "• Dikkat çekici giriş cümlesi",
        "• Bakış açısını seçme",
        "  (gözlemci / izlenimsel)",
        "• Sıralama düzeni kurma",
        "  (genelden özele / dıştan içe)"
    ], "#1a5276", "#eaf2f8")
    c += _kart(456, 54, 206, 170, "3. Paragrafa Aktarma", [
        "• Dizeleri kopyalamadan",
        "  özgün düzyazıya çevirme",
        "• Sıfatlar ve söz sanatlarıyla",
        "  zihinde resim çizme",
        "• Etkileyici bitiş cümlesi"
    ], "#117864", "#e8f8f5")
    return _svg(w, h, c)

def gorsel_2():
    w, h = 680, 245
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#1a5276"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Betimleme Türleri: Açıklayıcı (Bilgilendirici) ve İzlenimsel (Sanatsal) Betimleme</text>'
    c += _kart(18, 54, 314, 175, "Açıklayıcı (Bilgilendirici) Betimleme", [
        "• Amaç: Okura varlık veya mekân hakkında",
        "  nesnel ve açık bilgi vermektir.",
        "• Gözlem gerçekliği değiştirmeden aktarılır.",
        "• Kelimeler çoğunlukla gerçek anlamındadır.",
        "• Kişisel duygu ve yorumlara az yer verilir."
    ], "#1a5276", "#eaf2f8")
    c += _kart(348, 54, 314, 175, "İzlenimsel (Sanatsal / Edebî) Betimleme", [
        "• Amaç: Okurda estetik heyecan ve izlenim",
        "  uyandırmak, atmosferi hissettirmektir.",
        "• Öznel bakış açısı ve duygular ön plandadır.",
        "• Mecazlar, benzetmeler, kişileştirmeler ve",
        "  duyular arası aktarmalar yoğun kullanılır."
    ], "#922b21", "#fdedec")
    return _svg(w, h, c)

def gorsel_3():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#b9770e"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Beş Duyu ve Düşünceyi Geliştirme Yollarının Betimlemede Kullanımı</text>'
    c += _kart(18, 54, 314, 170, "Beş Duyuya Ait Ayrıntılar", [
        "• Görme: Renk, biçim, ışık-gölge, hareket",
        "• İşitme: Rüzgâr uğultusu, yaprak hışırtısı, sessizlik",
        "• Dokunma: Serinlik, pürüzlülük, nem, sıcaklık",
        "• Koklama ve Tatma: Toprak kokusu, tuzlu esinti",
        "• Çoklu duyular paragrafı canlandırır!"
    ], "#b9770e", "#fef9e7")
    c += _kart(348, 54, 314, 170, "Destekleyici Anlatım Araçları", [
        "• Benzetme: Soyut duyguları somut varlıklarla",
        "  görünür kılma ('kehribar sarısı yapraklar').",
        "• Karşılaştırma: Mekânın önceki ve şimdiki",
        "  hâlini kıyaslayarak etkiyi güçlendirme.",
        "• Niteleme Sıfatları: İsimlere renk ve durum katma."
    ], "#1e8449", "#e9f7ef")
    return _svg(w, h, c)

def gorsel_4():
    w, h = 680, 240
    c = f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="#d5d8dc" stroke-width="1.5"/>'
    c += f'<rect x="14" y="12" width="{w-28}" height="32" rx="8" fill="#117864"/>'
    c += f'<text x="{w//2}" y="33" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">Yazma Sürecini Değerlendirme ve Özgün Yazar Kimliği (TDE4.4)</text>'
    c += _kart(18, 54, 314, 170, "Öz ve Paydaş Değerlendirmesi (TDE4.4.1)", [
        "• İçerik Kontrolü: Şiirin atmosferi ve imgeleri",
        "  paragrafa doğru ve bütünlüklü yansıdı mı?",
        "• Dil ve Anlatım: Bağdaşıklık, bağlaşıklık, akıcılık",
        "  ve edebî söyleyiş inceliği sağlandı mı?",
        "• İmla: Yazım ve noktalama kurallarına uyuldu mu?"
    ], "#117864", "#e8f8f5")
    c += _kart(348, 54, 314, 170, "Geri Bildirim ve Yeni Hedefler (TDE4.4.2)", [
        "• Öğretmen ve akran değerlendirmelerini dikkate",
        "  alarak metni yeniden düzenleme (redaksiyon).",
        "• Gelecek yazılar için yeni üslup hedefleri koyma.",
        "• Özgün yazar kimliğini geliştirme ve ürünü",
        "  sınıf panosu / okul dergisinde paylaşma."
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
