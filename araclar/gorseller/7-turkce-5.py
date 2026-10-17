# -*- coding: utf-8 -*-
"""7. Sınıf Türkçe — 5. Hafta Görselleri (Sen Sor O Yanıtlasın / Sporda ve Yaşamda Hedefe Odaklan)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Dinleme / İzleme Süreci: Sporda ve Yaşamda Hedefe Odaklan</text>',
        _kart(25, 50, 225, 215, "1. Dinleme Öncesi Hazırlık", [
            "• Başlık ve görsellerden hareketle",
            "  metnin içeriğine dair tahmin yapma",
            "• Dinleme amacını belirleme",
            "• Spor, azim ve hedef kavramları",
            "  üzerine ön bilgileri harekete geçirme",
            "• Not alma araçlarını hazırlama"
        ], "#0284c7", "#f0f9ff"),
        _kart(267, 50, 225, 215, "2. Dinleme Sırası Stratejileri", [
            "• Anahtar kelimeleri ve önemli",
            "  detayları not alarak dinleme",
            "• Konuşmacının vurgu ve tonlamasına",
            "  dikkat ederek örtülü anlamları sezme",
            "• Sorulan sorular ile verilen yanıtlar",
            "  arasındaki mantıksal bağı izleme"
        ], "#10b981", "#ecfdf5"),
        _kart(510, 50, 225, 215, "3. Dinleme Sonrası Analiz", [
            "• Tahminlerle metnin gerçek içeriğini",
            "  karşılaştırma ve doğrulama",
            "• Metnin konusunu ve ana fikrini",
            "  kendi cümleleriyle özetleme",
            "• Başarıda disiplin ve odaklanmanın",
            "  rolü hakkında çıkarımlar yapma"
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Sen Sor O Yanıtlasın: Mülakat (Görüşme) ve Röportaj Teknikleri</text>',
        _kart(30, 50, 335, 215, "Mülakat (Görüşme) Özellikleri", [
            "• Alanında uzman, başarılı veya tanınmış bir",
            "  kişiyle soru-cevap şeklinde yapılan konuşmadır.",
            "• Görüşme öncesinde konuk hakkında kapsamlı",
            "  araştırma yapılır ve açık uçlu sorular hazırlanır.",
            "• 'Evet/Hayır' ile bitecek sığ sorular yerine",
            "  'Nasıl?', 'Neden?' soruları tercih edilir."
        ], "#2563eb", "#eff6ff"),
        _kart(395, 50, 335, 215, "Röportaj İle Mülakat Arasındaki Fark", [
            "• Mülakatta yazar kendi yorumunu katmadan",
            "  soru ve cevapları olduğu gibi aktarır.",
            "• Röportajda ise yazar soru-cevabın yanı sıra",
            "  kendi gözlemlerini, izlenimlerini, ortam",
            "  betimlemelerini ve fotoğrafları metne katar.",
            "• Her iki tür de bilgilendirici metinlerdendir."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hedefe Odaklanma Basamakları ve Söz Varlığı</text>',
        _kart(30, 50, 335, 215, "Sporda ve Yaşamda Başarı İlkeleri", [
            "• 1. Gerçekçi ve ölçülebilir hedef belirleme",
            "• 2. Planlı çalışma ve öz disiplin geliştirme",
            "• 3. Dikkat dağıtıcı unsurları yönetip odaklanma",
            "• 4. Başarısızlıklardan ders çıkarıp pes etmeme",
            "• 5. Zihinsel dayanıklılık ve takım ruhu",
            "• 6. Centilmenlik (Fair-play) ve ahlaki duruş"
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Metindeki Deyimler ve Kavramlar", [
            "• Hedefe kilitlenmek: Bütün dikkatini ve",
            "  enerjisini amacına yöneltmek.",
            "• Ter dökmek: Büyük emek ve çaba harcamak.",
            "• Göğsünü kabartmak: Başarıyla gururlandırmak.",
            "• Pes etmemek: Zorluklar karşısında yılmamak.",
            "• Azim: Engelleri aşma konusundaki kararlılık."
        ], "#e11d48", "#fff1f2"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Metin İçi ve Metin Dışı Anlam İlişkileri</text>',
        _kart(30, 50, 335, 195, "Amaç-Sonuç ve Koşul-Sonuç Cümleleri", [
            "• Amaç-Sonuç: 'Millî takıma seçilmek amacıyla",
            "  her sabah antrenman yapıyor.' (Hangi amaçla?)",
            "• Koşul-Sonuç: 'Düzenli çalışırsan hedefine",
            "  ulaşırsın.' (Hangi şartla?)",
            "• Sebep-Sonuç: 'Odaklandığı için atışı kazandı.'"
        ], "#4f46e5", "#eef2ff"),
        _kart(395, 50, 335, 195, "Örtülü Anlam ve Çıkarım Yapma", [
            "• Örtülü Anlam: 'Bu yıl da şampiyon oldu.'",
            "  (Önceki yıllarda da şampiyon olduğu anlaşılır.)",
            "• Çıkarım: Metindeki ipuçlarından hareketle",
            "  doğrudan söylenmeyen ana düşünceye ulaşmak.",
            "• Çoklu ortam (ses/görsel) ögelerini yorumlama."
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
