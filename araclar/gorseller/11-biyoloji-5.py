def _svg(w, h, icerik):
    return (
        f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
        f'style="width:100%;height:auto;display:block;font-family:\'Segoe UI\',sans-serif;">'
        f'<rect width="{w}" height="{h}" rx="12" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5"/>'
        f'{icerik}</svg>'
    )


def _kart(x, y, w, h, baslik, satirlar, renk="#10B981", bg="#ECFDF5"):
    b = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.8"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="10" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="12" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+20}" font-size="11.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{baslik}</text>'
    )
    for i, s in enumerate(satirlar):
        b += f'<text x="{x+12}" y="{y+48+i*18}" font-size="10.5" fill="#1E293B">{s}</text>'
    return b


def gorsel_1():
    w, h = 680, 260
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'BİTKİSEL HORMONLAR: BÜYÜMEYİ TEŞVİK EDENLER VE ENGELLEYENLER</text>'
    )
    ic += _kart(20, 44, 310, 198, "BÜYÜMEYİ TEŞVİK EDEN HORMONLAR", [
        "1. Oksin (IAA - İndol Asetik Asit):",
        "   • Sürgün ucu (koleoptil) ve genç yapraklarda üretilir.",
        "   • Hücre uzamasını, yönelmeyi (tropizma) ve köklenmeyi sağlar.",
        "2. Giberellin (GA):",
        "   • Gövde uzamasını, tohum çimlenmesini ve çiçeklenmeyi uyarır.",
        "3. Sitokinin:",
        "   • Kök uçlarında sentezlenir, ksilemle yukarı taşınır.",
        "   • Hücre bölünmesini uyarır, yaprak yaşlanmasını geciktirir."
    ], "#10B981", "#ECFDF5")
    ic += _kart(350, 44, 310, 198, "OLGUNLAŞMA VE BÜYÜMEYİ ENGELLEYENLER", [
        "4. Etilen (Gaz Halindeki Tek Hormon):",
        "   • Meyve olgunlaşmasını (nişastanın şekere dönüşümü) sağlar.",
        "   • Yaprak dökümünü (absisyon) ve çiçek solmasını hızlandırır.",
        "   • Üretildiği yerden havayla diğer meyveleri de etkiler.",
        "5. Absisik Asit (ABA - Stres Hormonu):",
        "   • Kuraklıkta stomaları kapatarak su kaybını önler.",
        "   • Tohumun uygunsuz şartlarda çimlenmesini engeller (dormansi).",
        "   • Giberellin ile antagonist (zıt) çalışır."
    ], "#D97706", "#FEF3C7")
    return _svg(w, h, ic)


def gorsel_2():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'OKSİN HORMONU VE KOLEOPTİL DENEYLERİ (WENT VE DARWIN)</text>'
    )
    ic += _kart(20, 44, 205, 190, "1. SİMETRİK IŞIK", [
        "• Işık tepeden dik gelir.",
        "• Oksin ucu terk ederek",
        "  alt bölgelere eşit dağılır.",
        "• Koleoptil yukarı doğru",
        "  düz (simetrik) büyür.",
        "• Yönelme (eğilme) olmaz.",
        "• Normal boyuna uzama."
    ], "#2563EB", "#EFF6FF")
    ic += _kart(237, 44, 205, 190, "2. TEK YÖNLÜ IŞIK", [
        "• Işık sağdan verildiğinde",
        "  oksin karanlık (sol)",
        "  tarafa doğru göç eder.",
        "• Karanlık tarafta hücreler",
        "  daha hızlı uzar.",
        "• Sürgün ışığa doğru yönelir",
        "  (Pozitif Fototropizma)."
    ], "#10B981", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "3. MİKA VE AGAR ENGELİ", [
        "• Agar blok oksini geçirir",
        "  -> Yönelme DEVAM EDER.",
        "• Mika / Cam plaka oksini",
        "  geçirmez -> Yönelme DURUR.",
        "• Ucu kesilen koleoptil",
        "  uzamaz ve ışığa yönelmez.",
        "• Oksin kimyasal bir mesajcıdır."
    ], "#9333EA", "#FAF5FF")
    return _svg(w, h, ic)


def gorsel_3():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'APİKAL DOMİNANSİ (TEPE BASKINLIĞI) VE SİTOKİNİN - OKSİN ETKİLEŞİMİ</text>'
    )
    ic += _kart(20, 44, 310, 190, "TEPE TOMURCUĞU SAĞLAM İKEN", [
        "• Uç (apikal) meristemde bol miktarda oksin üretilir.",
        "• Yukarıdan aşağıya taşınan oksin, yanal (aksiller)",
        "  tomurcukların gelişmesini baskılar (Apikal Dominansi).",
        "• Bitki yanlara doğru değil, boyuna doğru uzar.",
        "• Çam ve servi gibi bitkilerde konik gövde oluşturur.",
        "• İpucu: Kök gelişiminde ise yüksek oksin büyümeyi",
        "  baskılarken, düşük oksin kök uzamasını hızlandırır."
    ], "#0891B2", "#ECFEFF")
    ic += _kart(350, 44, 310, 190, "TEPE TOMURCUĞU KESİLDİĞİNDE (BUDAMA)", [
        "• Oksin kaynağı ortadan kalktığı için baskı sona erer.",
        "• Kökte üretilen sitokinin hormonu yanal tomurcukları",
        "  uyararak yan dalların hızla gelişmesini sağlar.",
        "• Bitki çalılaşır, daha gür ve bol meyveli hale gelir.",
        "• Doku kültüründe Oksin/Sitokinin oranı:",
        "   - Oksin yüksek -> Kök farklılaşması başlar.",
        "   - Sitokinin yüksek -> Sürgün/gövde farklılaşması başlar."
    ], "#E11D48", "#FFF1F2")
    return _svg(w, h, ic)


def gorsel_4():
    w, h = 680, 250
    ic = (
        '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">'
        'TOHUM ÇİMLENMESİNDE GİBERELLİN (GA) VE ABSİSİK ASİT (ABA) DENGESİ</text>'
    )
    adimlar = [
        ("1. DORMANSİ (UYKU HALİ)", "Tohumda ABA derişimi yüksektir; metabolizma bazal düzeydedir, kış ve kuraklıkta çimlenme engellenir.", "#DC2626", "#FEF2F2"),
        ("2. SU ALMA (İMBİBİSYON)", "Ortamda yeterli su bulunduğunda tohum su alarak şişer; ABA derişimi hızla düşer ve kabuk çatlar.", "#2563EB", "#EFF6FF"),
        ("3. GİBERELLİN SALINIMI", "Embriyo giberellin (GA) salgılar; GA, sindirim enzimlerini (alfa-amilaz) aktifleşmeye uyarır.", "#9333EA", "#FAF5FF"),
        ("4. NİŞASTA SİNDİRİMİ VE ÇİMLENME", "Endospermdeki nişasta glikoza yıkılır; embriyo mitozla bölünerek ilk kök (radikula) ve gövdeyi çıkarır.", "#16A34A", "#F0FDF4")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        y = 44 + i * 48
        ic += (
            f'<rect x="25" y="{y}" width="630" height="40" rx="8" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
            f'<text x="40" y="{y+16}" font-size="11" font-weight="bold" fill="{r}">{b}</text>'
            f'<text x="40" y="{y+32}" font-size="10.5" fill="#1E293B">{m}</text>'
        )
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