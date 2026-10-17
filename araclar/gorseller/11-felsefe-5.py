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
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">TARİHSEL SÜREÇTE İNSAN-DOĞA İLİŞKİSİNİN DÖNÜŞÜMÜ</text>'
    ic += _kart(20, 44, 310, 190, "GELENEKSEL / ORGANİK DOĞA ANLAYIŞI", [
        "• İlk Çağ ve geleneksel toplumlarda insan, kendisini",
        "  doğanın ayrılmaz ve uyumlu bir parçası görmüştür.",
        "• Doğa canlı bir organizma ve kutsal bir düzen (kozmos)",
        "  olarak kabul edilmiş, ona saygı duyulmuştur.",
        "• Üretim ve tüketim doğanın kendini yenileme hızıyla",
        "  (ekolojik döngüyle) uyumlu kalmıştır."
    ], "#059669", "#ECFDF5")
    ic += _kart(350, 44, 310, 190, "MODERN / MEKANİK DOĞA ANLAYIŞI", [
        "• Bilimsel devrim ve Sanayi Devrimi ile doğa, insanın",
        "  hükmedeceği mekanik bir nesne/kaynak görülmüştür.",
        "• Francis Bacon'ın 'Bilgi güçtür' ve Descartes'ın",
        "  'doğanın efendisi ve sahibi olma' fikri öne çıkmıştır.",
        "• Aşırı tüketim, fosil yakıt kullanımı ve sanayileşme",
        "  küresel ekolojik krizi tetiklemiştir."
    ], "#DC2626", "#FEF2F2")
    return _svg(w, h, ic)

def gorsel_2():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">ÇEVRE ETİĞİ YAKLAŞIMLARI: AHLAKİ DEĞERİN MERKEZİ</text>'
    ic += _kart(20, 44, 205, 190, "1. İNSAN MERKEZCİ ETİK", [
        "• Antroposentrik yaklaşım.",
        "• Ahlaki değerin tek sahibi",
        "  insandır; doğa araçsaldır.",
        "• Çevre, insanın çıkarları",
        "  ve refahı zarar görmesin",
        "  diye korunmalıdır.",
        "• Kısa/uzun vadeli insan",
        "  faydasını temel alır."
    ], "#D97706", "#FEF3C7")
    ic += _kart(237, 44, 205, 190, "2. CANLI MERKEZCİ ETİK", [
        "• Biyosentrik yaklaşım.",
        "• İnsan dışındaki tüm canlılar",
        "  (hayvan, bitki) özsel değere",
        "  sahiptir.",
        "• Albert Schweitzer: 'Yaşama",
        "  Saygı' etiği.",
        "• Paul Taylor: Doğaya saygı",
        "  ve her canlının yaşam hakkı."
    ], "#059669", "#ECFDF5")
    ic += _kart(455, 44, 205, 190, "3. ÇEVRE MERKEZCİ ETİK", [
        "• Ekosentrik (bütüncül) etik.",
        "• Canlılarla birlikte cansız",
        "  çevre (toprak, su, hava,",
        "  ekosistem) özsel değer taşır.",
        "• Aldo Leopold: 'Yeryüzü",
        "  Etiği' (Toprak Etiği).",
        "• Arne Naess: 'Derin Ekoloji'",
        "  (ekosistem bütünlüğü)."
    ], "#2563EB", "#EFF6FF")
    return _svg(w, h, ic)

def gorsel_3():
    w, h = 680, 260
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">ÇEVRE FELSEFESİNİN TEMEL SORULARI VE KAVRAMLARI</text>'
    adimlar = [
        ("1. ÖZSEL DEĞER Mİ, ARAÇSAL DEĞER Mİ?", "Doğanın sadece insana sağladığı fayda için mi yoksa kendi başına var olduğu için mi değerli olduğu sorusudur.", "#059669", "#ECFDF5"),
        ("2. YERYÜZÜ (TOPRAK) ETİĞİ — ALDO LEOPOLD", "İnsanı doğanın fatihi değil, toprağı, suyu, bitkileri ve hayvanları kapsayan biyotik topluluğun sade bir üyesi sayar.", "#2563EB", "#EFF6FF"),
        ("3. DERİN EKOLOJİ — ARNE NAESS", "Sığ ekolojinin kirliliği sadece insan sağlığı için önleme çabasına karşı doğanın içsel eşitliğini ve çeşitliliğini savunur.", "#7C3AED", "#F5F3FF"),
        ("4. GELECEK KUŞAKLARA KARŞI SORUMLULUK — HANS JONAS", "Henüz doğmamış nesillerin yaşanabilir bir yeryüzü hakkını koruyan 'Sorumluluk İlkesi' ve ekolojik adalet bilincidir.", "#D97706", "#FEF3C7")
    ]
    for i, (b, m, r, bg) in enumerate(adimlar):
        ic += _bant(44 + i * 50, b, m, r, bg)
    return _svg(w, h, ic)

def gorsel_4():
    w, h = 680, 250
    ic = '<text x="340" y="26" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SIĞ EKOLOJİ İLE DERİN EKOLOJİNİN KARŞILAŞTIRILMASI</text>'
    ic += _kart(20, 44, 310, 190, "SIĞ (YÜZEYSEL) EKOLOJİ HAREKETİ", [
        "• Temelde insan merkezci (antroposentrik) bakışı korur.",
        "• Çevre kirliliği ve kaynakların tükenmesiyle mücadele",
        "  ederken temel amacı gelişmiş ülkelerdeki insanların",
        "  sağlığını ve refah düzeyini korumaktır.",
        "• Doğayı hâlâ insanın kullanımına sunulmuş bir 'kaynak",
        "  deposu' olarak görür; sadece daha verimli kullanım ister."
    ], "#D97706", "#FEF3C7")
    ic += _kart(350, 44, 310, 190, "DERİN EKOLOJİ HAREKETİ (ARNE NAESS)", [
        "• Çevre merkezci (ekosentrik) bir dünya görüşü sunar.",
        "• Yeryüzündeki tüm yaşam biçimlerinin gelişme ve var",
        "  olma hakkının kendi başına (özsel) değer taşıdığını savunur.",
        "• Biyoçeşitliliğin zenginliğini korumanın ahlaki bir ödev",
        "  olduğunu, insanın yaşamsal ihtiyaçları dışında bu",
        "  zenginliği azaltmaya hakkı olmadığını vurgular."
    ], "#059669", "#ECFDF5")
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
