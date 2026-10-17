# -*- coding: utf-8 -*-
"""8. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük — 5. Hafta Görselleri (Millî Uyanış: I. Dünya Savaşı ve Osmanlı)."""


def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:18px auto;'
        f'font-family:\'Plus Jakarta Sans\',system-ui,sans-serif;background:#f8fafc;'
        f'border:1px solid #e2e8f0;border-radius:14px;box-shadow:0 4px 12px rgba(15,23,42,0.05)">'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10b981", bg="#ecfdf5"):
    b = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{bg}" stroke="{renk}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="12" fill="{renk}"/>',
        f'<rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{renk}"/>',
        f'<text x="{x+w/2}" y="{y+22}" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">{baslik}</text>',
    ]
    for i, s in enumerate(satirlar):
        b.append(
            f'<text x="{x+14}" y="{y+56+i*22}" font-size="12" font-weight="600" fill="#1e293b">{s}</text>'
        )
    return "".join(b)


def gorsel_1():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">I. Dünya Savaşı\'nın (1914-1918) Genel, Özel ve Görünür Nedenleri</text>',
        _kart(25, 50, 225, 215, "1. Genel Nedenler", [
            "• Sanayi İnkılabı sonrası ham madde",
            "  ve pazar arayışı (Sömürgecilik).",
            "• Fransız İhtilali sonrası yayılan",
            "  Milliyetçilik akımı.",
            "• Devletler arası bloklaşma ve",
            "  hızlı silahlanma yarışı."
        ], "#e11d48", "#fff1f2"),
        _kart(267, 50, 225, 215, "2. Özel Nedenler", [
            "• Almanya ile İngiltere arasındaki",
            "  ekonomik ve sömürge rekabeti.",
            "• Fransa'nın kömür havzası olan",
            "  Alsas-Loren'i Almanya'dan geri istemesi.",
            "• Rusya'nın Panslavizm ve sıcak",
            "  denizlere inme politikası."
        ], "#0284c7", "#f0f9ff"),
        _kart(510, 50, 225, 215, "3. Kıvılcım (Görünür Neden)", [
            "• 28 Haziran 1914'te Avusturya-Macaristan",
            "  Veliahtı Ferdinand'ın Saraybosna'da",
            "  bir Sırp milliyetçisi tarafından",
            "  öldürülmesi.",
            "• Avusturya-Macaristan'ın Sırbistan'a",
            "  savaş açmasıyla savaş başladı."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Savaş Öncesi ve Sırasında Oluşan Bloklar (Üçlü İtilaf ve Üçlü İttifak)</text>',
        _kart(30, 50, 335, 215, "İtilaf (Anlaşma) Devletleri", [
            "• Kurucu Üçlü: İngiltere, Fransa, Rusya",
            "• Sonradan Katılanlar: Sırbistan, Japonya,",
            "  Romanya, Yunanistan, ABD ve İTALYA!",
            "• Dikkat: İtalya savaş başında İttifak grubundayken",
            "  Batı Anadolu vaadiyle (Londra Antlaşması)",
            "  taraf değiştirip İtilaf bloğuna geçmiştir!"
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "İttifak (Bağlaşma) Devletleri", [
            "• Kurucu Üçlü: Almanya, Avusturya-Macaristan,",
            "  İtalya (Savaş başlayınca taraf değiştirdi).",
            "• Sonradan Katılanlar: Osmanlı Devleti ve",
            "  Bulgaristan (Çanakkale zaferinden sonra).",
            "• Bulgaristan'ın katılımıyla Almanya ile",
            "  Osmanlı arasında kara bağlantısı sağlandı."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Osmanlı Devleti\'nin Savaşa Girişi: Tarafların Amaçları</text>',
        _kart(30, 50, 335, 215, "Almanya Neden Osmanlı'yı Yanında İstedi?", [
            "• Yeni cepheler açarak kendi üzerindeki savaş",
            "  yükünü hafifletmek.",
            "• Osmanlı'nın jeopolitik konumundan (Boğazlar,",
            "  Süveyş) yararlanıp İngiliz sömürge yollarını kesmek.",
            "• Halifenin dini gücünden (cihat çağrısından)",
            "  ve Osmanlı'nın insan/ham madde gücünden yararlanmak."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Osmanlı Neden Savaşa Girmek İstedi?", [
            "• Son savaşlarda (Trablusgarp ve Balkan)",
            "  kaybettiği toprakları geri almak.",
            "• Siyasi yalnızlıktan kurtulmak.",
            "• Kapitülasyonları ve Düyûn-u Umûmiye",
            "  (dış borçlar) baskısını kaldırmak.",
            "• Goben (Yavuz) ve Breslav (Midilli) olayıyla girdi."
        ], "#10b981", "#ecfdf5"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Osmanlı\'nın Savaştığı Cephelerin Sınıflandırılması</text>',
        _kart(30, 50, 335, 195, "1. Taarruz (Saldırı) ve 2. Yardım Cepheleri", [
            "• Taarruz Cepheleri (2K): KAFKAS ve KANAL",
            "  (Bizim saldırarak açtığımız cepheler).",
            "• Müttefiklere Yardım Cepheleri (Sonu -ya):",
            "  GALİÇYA, MAKEDONYA ve ROMANYA",
            "  (Sınırlarımız dışında yardım için açıldı)."
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "3. Savunma Cepheleri", [
            "• Çanakkale Cephesi (Tek zafer kazandığımız cephe!)",
            "• Irak (Kût'ül-Amâre başarısı) Cephesi",
            "• Hicaz-Yemen Cephesi (Fahreddin Paşa - Medine)",
            "• Suriye-Filistin Cephesi (Mustafa Kemal'in",
            "  Yıldırım Orduları komutanlığı yaptığı cephe)."
        ], "#16a34a", "#f0fdf4"),
    ]
    return _svg(w, h, "".join(s))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = {0: "b1", 1: "b2", 2: "b3", 4: "b4"}
    for idx, anahtar in eş.items():
        if idx < len(v.get("bolumler", [])):
            v["bolumler"][idx]["gorsel"] = GORSELLER[anahtar]
