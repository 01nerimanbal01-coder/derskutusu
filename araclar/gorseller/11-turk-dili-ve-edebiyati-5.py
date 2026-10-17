def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#059669", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def _bant(y, b, m, r, bg):
    return (
        f'<rect x="25" y="{y}" width="630" height="42" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
        f'<text x="40" y="{y+33}" font-size="10.5" fill="#1E293B">{m}</text>'
    )


def gorsel_1():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SÖZLÜ İLETİŞİM SÜRECİ VE BAŞLICA İLETİŞİM ENGELLERİ</text>'
    ic += _kart(20, 44, 310, 190, "YARGILAYICI VE BASKICI ENGELLER", [
        "• Emir vermek ve yönlendirmek ('Hemen şunu yap!').",
        "• Uyarmak ve gözdağı vermek ('Yoksa kötü olur!').",
        "• Suçlamak, eleştirmek ve yargılamak ('Hep senin yüzünden').",
        "• Alay etmek, lakap takmak ve utandırmak.",
        "• Ahlak dersi vermek ('Senin yerinde olsam...').",
        "• Bu tutumlar karşı tarafta savunma ve direnç yaratır."
    ], "#DC2626", "#FEF2F2")
    ic += _kart(350, 44, 310, 190, "DİNLEME VE ALGILAMA KAYNAKLI ENGELLER", [
        "• Önyargılı yaklaşmak ve niyet okumak.",
        "• Empati kurmamak (Kendini muhatabın yerine koymamak).",
        "• Söz kesmek ve dinliyormuş gibi görünmek.",
        "• Konuyu saptırmak veya işi şakaya vurmak.",
        "• Sosyal statü, eğitim ve söz varlığı farkını (Karagöz",
        "  ve Hacivat'ta olduğu gibi) dikkate almamak."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">İLETİŞİM ENGELLERİNİ AŞMANIN ANAHTARI: BEN DİLİ VE AKTİF DİNLEME</text>'
    ic += _kart(20, 44, 310, 190, "SEN DİLİ YERİNE 'BEN DİLİ' KULLANMAK", [
        "• Sen Dili (Engelleyici): Kişiliği hedef alır, suçlayıcıdır",
        "  ve öfke uyandırır ('Çok sorumsuzsun, hep gecikiyorsun!').",
        "• Ben Dili (Yapıcı): Davranışın konuşmacı üzerindeki",
        "  somut etkisini ve duyguyu açıklar ('Geç kaldığında",
        "  meraklanıyorum ve çalışmamız aksıyor').",
        "• Ben dili empatiyi güçlendirir ve çatışmayı çözer."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "AKTİF (ETKİN) DİNLEME VE BEDEN DİLİ", [
        "• Göz teması kurmak ve muhataba odaklanmak.",
        "• Söz kesmeden, savunmaya geçmeden dinlemek.",
        "• Baş hareketleri ve kısa geri bildirimlerle ('Anlıyorum')",
        "  dinlediğini hissettirmek.",
        "• Ses tonu, vurgu, tonlama ve jest/mimikleri",
        "  sözlü mesajla uyumlu ve samimi kullanmak."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SÖZLÜ İLETİŞİM ENGELLERİNİ KONU ALAN DRAMA SÜRECİ</text>'
    adimlar = [
        ("1. HAZIRLIK VE ISINMA AŞAMASI", "Konunun (günlük hayattaki iletişim engellerinin) belirlenmesi, dramatik durumun ve çatışmanın kurgulanması, rol dağılımı.", "#059669", "#ECFDF5"),
        ("2. CANLANDIRMA (DOĞAÇLAMA VE ROL OYNAMA)", "Farklı bakış açılarını deneyimleyerek iletişim engellerinin ve çözüm yollarının ses tonu, vurgu ve beden diliyle sergilenmesi.", "#2563EB", "#EFF6FF"),
        ("3. DEĞERLENDİRME VE TARTIŞMA AŞAMASI", "Canlandırma sonrasında yaşanan iletişim kazalarının, duyguların ve öz/akran değerlendirme ölçütlerinin paylaşılması.", "#7C3AED", "#F5F3FF"),
        ("4. GELENEKSEL TİYATRO (KARAGÖZ) İLE BAĞLANTI", "Karagöz (halk dili, yanlış anlamalar) ile Hacivat (aydın/süslü dil) arasındaki iletişim çatışmalarının dramatik analizi.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">DRAMATİK METİNLERDE YAPI UNSURLARI VE FİİLİMSİLER</text>'
    ic += _kart(20, 44, 310, 190, "DRAMATİK METNİN YAPI UNSURLARI", [
        "• Dramatik Örgü: Olayların sebep-sonuç içinde akışı.",
        "• Çatışma: Karşıt duygu, düşünce veya statülerin",
        "  (aydın-halk, eski-yeni, hayal-gerçek) karşılaşması.",
        "• Kişiler (Tipler ve Karakterler): Karagöz, Hacivat,",
        "  Çelebi vb. sosyal statülerini dilleriyle yansıtırlar.",
        "• Mekân (Yer) ve Zaman: Olayın geçtiği çevre ve süre."
    ], "#7C3AED", "#F5F3FF")
    ic += _kart(350, 44, 310, 190, "KONUŞMA VE METİNDE FİİLİMSİLER (EYLEMSİLER)", [
        "• İsim-Fiil (Ad-Eylem): -ma/-me, -ış/-iş, -mak/-mek",
        "  (ör. 'beklemek için', 'konuşmaya bırakalım').",
        "• Sıfat-Fiil (Ortaç): -an/-en, -ası, -mez, -ar, -dik,",
        "  -ecek, -miş (ör. 'yazılmış bir ferman', 'oturanlar').",
        "• Zarf-Fiil (Bağ-Fiil / Ulaç): -ıp, -arak, -ınca,",
        "  -ken, -dıkça (ör. 'evden çıkarak', 'geçerken')."
    ], "#0891B2", "#ECFEFF")
    return _svg(w, h, ic)

GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    harita = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in harita.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
