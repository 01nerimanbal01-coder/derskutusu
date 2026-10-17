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
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Metni Anlama: Tahmin Etme, Yüzey Anlam ve Anahtar Kelimeler</text>'
    ic += _kart(20, 45, 230, 175, "1. Okuma Öncesi Tahmin", [
        "• Metnin başlığını inceleme",
        "• Görsellerdeki ipuçlarını okuma",
        "• Ön bilgilerle bağ kurma",
        "• \'Metinde ne anlatılacak?\' sorusu",
        "• Okuma/dinleme sonrası kontrol"
    ], "#0284c7", "#f0f9ff")
    ic += _kart(265, 45, 230, 175, "2. Yüzey Anlam ve Anahtar Kelime", [
        "• Metinde açıkça verilen bilgiler",
        "• Kim, nerede, ne zaman, ne yaptı?",
        "• Anahtar Kelime: Metnin konusunu",
        "  en iyi yansıtan ipucu kelimeler",
        "• Metinde en sık vurgulanan kavramlar"
    ], "#059669", "#ecfdf5")
    ic += _kart(510, 45, 230, 175, "3. Öyküleyici Metnin Bölümleri", [
        "• Serim (Giriş): Kişi, yer ve zaman",
        "  tanıtılır, olaya giriş yapılır",
        "• Düğüm (Gelişme): Olaylar gelişir,",
        "  merak ve heyecan artar",
        "• Çözüm (Sonuç): Olay sonuca bağlanır"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 240, ic)

def gorsel_2():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Söz Sanatları: Benzetme (Teşbih) ve Kişileştirme (Teşhis)</text>'
    ic += _kart(20, 45, 350, 175, "Benzetme (Teşbih) Sanatı", [
        "• Aralarında ilgi bulunan iki varlıktan zayıf olanın",
        "  güçlü olana benzetilmesidir.",
        "• Unsurları: Benzeyen, Kendisine Benzetilen,",
        "  Benzetme Yönü ve Benzetme Edatı (gibi, kadar, sanki).",
        "• Örnek: \'Mustafa, deniz gibi masmavi gözleriyle baktı.\'"
    ], "#2563eb", "#eff6ff")
    ic += _kart(390, 45, 350, 175, "Kişileştirme (Teşhis) Sanatı", [
        "• İnsan dışındaki varlıklara (hayvanlara, bitkilere,",
        "  cansız nesnelere) insana ait özellikler verilmesidir.",
        "• Üzülmek, sevinmek, konuşmak, düşünmek, ağlamak vb.",
        "• Örnek: \'Selanik\'in rüzgârı küçük Mustafa\'ya fısıldadı.\'",
        "• Örnek: \'Eski oyuncak kutusu çocukları özlemle bekliyordu.\'"
    ], "#d97706", "#fffbeb")
    return _svg(760, 240, ic)

def gorsel_3():
    ic = '<rect x="0" y="0" width="760" height="250" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Düşüncenin Yönünü Değiştiren ve Destekleyen Bağlantı İfadeleri</text>'
    ic += _kart(20, 45, 230, 185, "Zıtlık / Geçiş İfadeleri", [
        "• ama, fakat, lakin, ancak",
        "• buna rağmen, oysa, ne var ki",
        "• Olumlu düşünceden olumsuza",
        "  veya olumsuzdan olumluya geçiş:",
        "• \'Yoruldu ama pes etmedi.\'"
    ], "#be123c", "#fff1f2")
    ic += _kart(265, 45, 230, 185, "Açıklama ve Destekleme", [
        "• çünkü, bu nedenle, bu yüzden",
        "• özellikle, hatta, üstelik, ayrıca",
        "• başka bir deyişle, yani, örneğin",
        "• Düşünceyi güçlendirir ve açıklar:",
        "• \'Başardı çünkü çok çalıştı.\'"
    ], "#0f766e", "#f0fdfa")
    ic += _kart(510, 45, 230, 185, "Özetleme ve Sonuç İfadeleri", [
        "• kısacası, özetle, sonuç olarak",
        "• sonunda, böylece, demek ki",
        "• Anlatılanları toparlar ve",
        "  ana fikre ulaştırır:",
        "• \'Kısacası emek en güzel hediyedir.\'"
    ], "#7c3aed", "#f5f3ff")
    return _svg(760, 250, ic)

def gorsel_4():
    ic = '<rect x="0" y="0" width="760" height="240" rx="12" fill="#f8fafc"/>'
    ic += '<text x="380" y="28" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Konuşmada Beden Dili ve Yazımda Büyük Harf - Noktalama Kuralları</text>'
    ic += _kart(20, 45, 350, 175, "Hazırlıksız Konuşma ve Beden Dili", [
        "• Göz teması kurmak ve dinleyicilere dönük durmak",
        "• Ses tonunu ve vurguyu duyguya göre ayarlamak",
        "• Jest (el-kol) ve mimikleri (yüz ifadelerini) doğal kullanmak",
        "• Konu dışına çıkmadan, bağlantı ifadeleriyle konuşmak",
        "• Akıcı okuma ve konuşmada noktalama duraklarına uymak"
    ], "#059669", "#ecfdf5")
    ic += _kart(390, 45, 350, 175, "Yazım Kuralları ve Noktalama İşaretleri", [
        "• Özel adlar (Mustafa Kemal Atatürk, Selanik) büyük harfle başlar",
        "• Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar",
        "• Özel adlara gelen çekim ekleri kesme işaretiyle (\') ayrılır",
        "• Sıralı cümleleri ve eş görevli kelimeleri ayırmada virgül (,)",
        "• Duygu bildiren ifadelerin sonunda ünlem (!) işareti kullanılır"
    ], "#1d4ed8", "#eff6ff")
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
