# -*- coding: utf-8 -*-
"""7. Sınıf Peygamberimizin Hayatı — 5. Hafta Görselleri (İsrâ ve Miraç Mucizesi)."""


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
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Hüzün Yılından İlahi Teselliye: İsrâ ve Miraç Kavramları</text>',
        _kart(25, 50, 225, 215, "1. Arka Plan: Hüzün Yılı", [
            "• Boykot yıllarının ardından",
            "  amcası Ebû Tâlib ve eşi",
            "  Hz. Hatice'nin vefat etmesi",
            "• Tâif yolculuğunda karşılaşılan",
            "  ağır baskı ve üzüntüler",
            "• Yüce Allah'ın elçisini tesellisi"
        ], "#e11148" if False else "#e11d48", "#fff1f2"),
        _kart(267, 50, 225, 215, "2. İsrâ (Gece Yürüyüşü)", [
            "• Sözlük anlamı: Geceleyin yürütmek.",
            "• Mekke'deki Mescid-i Harâm'dan",
            "  Kudüs'teki Mescid-i Aksâ'ya",
            "  yapılan mucizevi gece yolculuğu.",
            "• İsrâ suresi 1. ayette açıkça",
            "  bildirilmiştir."
        ], "#0284c7", "#f0f9ff"),
        _kart(510, 50, 225, 215, "3. Miraç (Göklere Yükseliş)", [
            "• Sözlük anlamı: Yükselme aracı, merdiven.",
            "• Mescid-i Aksâ'dan başlayıp gök",
            "  katlarına ve Sidretü'l-Müntehâ'ya",
            "  yükseliş mucizesi.",
            "• Diğer peygamberlerle buluşma ve",
            "  ilahi kudret ayetlerini görme."
        ], "#8b5cf6", "#f5f3ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_2():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Miraç Gecesinde Ümmete Verilen 3 Büyük İlahi Hediye</text>',
        _kart(25, 50, 225, 215, "1. Beş Vakit Namaz", [
            "• Müminin miracı olan beş vakit",
            "  namaz bu gecede farz kılındı.",
            "• Kulun günde beş kez doğrudan",
            "  Rabbine yönelip huzuruna",
            "  çıkmasını sağlayan en temel",
            "  ibadettir."
        ], "#10b981", "#ecfdf5"),
        _kart(267, 50, 225, 215, "2. Âmenerrasûlü Ayetleri", [
            "• Bakara suresinin son iki ayeti",
            "  (285 ve 286. ayetler) vahyedildi.",
            "• İman esaslarını, İslam'ın kolaylık",
            "  dini olduğunu (güç yetirilemeyen",
            "  yükümlülük olmadığını) ve bağışlanma",
            "  dualarını içerir."
        ], "#2563eb", "#eff6ff"),
        _kart(510, 50, 225, 215, "3. Bağışlanma Müjdesi", [
            "• Allah'a hiçbir şeyi ortak",
            "  koşmayan (şirkten uzak duran)",
            "  müminlerin büyük günahlarının",
            "  Allah'ın rahmetiyle bağışlanacağı",
            "  ve sonunda cennete girecekleri",
            "  müjdesi verildi."
        ], "#d97706", "#fffbeb"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_3():
    w, h = 760, 290
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">İsrâ Suresi 23-39. Ayetlerdeki Ahlaki İlkeler (Miraç İlkeleri)</text>',
        _kart(30, 50, 335, 215, "Aileye Saygı, İnfak ve Hayat Hakkı", [
            "• Yalnızca Allah'a kulluk etmek (Tevhid).",
            "• Anne ve babaya 'öf' bile dememek, onlara",
            "  iyilik ve merhametle davranmak.",
            "• Akrabaya, yoksula ve yolda kalmışa hakkını",
            "  vermek; cimrilik ve israftan (saçıp savurmaktan)",
            "  kaçınmak ve cana kıymamak."
        ], "#0d9488", "#f0fdfa"),
        _kart(395, 50, 335, 215, "Emanet, Dürüstlük ve Tevazu", [
            "• Yetimin malına koruma amacı dışında yaklaşmamak.",
            "• Verilen söze sadık kalmak ('Çünkü verilen",
            "  sözden sorumluluk vardır' - İsrâ, 34).",
            "• Ölçü ve tartıyı tam ve adaletli yapmak.",
            "• Hakkında bilgi sahibi olunmayan şeyin",
            "  peşine düşmemek ve yeryüzünde böbürlenmemek."
        ], "#4f46e5", "#eef2ff"),
    ]
    return _svg(w, h, "".join(s))


def gorsel_4():
    w, h = 760, 270
    s = [
        f'<text x="{w/2}" y="30" font-size="16" font-weight="800" fill="#0f172a" text-anchor="middle">Mescid-i Aksâ\'nın Önemi ve Hz. Ebû Bekir\'in \'es-Sıddîk\' Unvanı</text>',
        _kart(30, 50, 335, 195, "Kudüs ve Mescid-i Aksâ Bilinci", [
            "• Mescid-i Aksâ, Müslümanların İLK KIBLESİ",
            "  ve yeryüzündeki üç kutsal mescitten biridir.",
            "• İsrâ mucizesi Mekke (Mescid-i Harâm) ile",
            "  Kudüs (Mescid-i Aksâ) arasında kıyamete",
            "  kadar sürecek manevi bir kardeşlik bağı kurmuştur."
        ], "#16a34a", "#f0fdf4"),
        _kart(395, 50, 335, 195, "Hz. Ebû Bekir: es-Sıddîk (Tereddütsüz Doğrulayan)", [
            "• Müşrikler Miraç haberini duyunca alay etmek",
            "  için Hz. Ebû Bekir'e koştular.",
            "• Hz. Ebû Bekir, 'Eğer bunu O söylediyse",
            "  şüphesiz doğrudur!' diyerek tam teslimiyet",
            "  gösterdi ve 'es-Sıddîk' unvanını aldı."
        ], "#9333ea", "#faf5ff"),
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
