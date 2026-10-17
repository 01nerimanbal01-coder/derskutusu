# -*- coding: utf-8 -*-
"""10. Sınıf Türk Dili ve Edebiyatı — 4. Hafta görsel modülü:
Sözün Ezgisi: Şiir Dinletisi Hazırlama ve Sunma, Türkü Dinleme/İzleme ve İsim Tamlamaları"""

C_MOR = "#6c3483"
C_MAVI = "#1a5276"
C_YESIL = "#1e8449"
C_TURUNCU = "#b9770e"
C_KIRMIZI = "#922b21"
C_ACIK_MOR = "#f5eef8"
C_ACIK_MAVI = "#eaf2f8"
C_ACIK_YESIL = "#e9f7ef"
C_ACIK_SARI = "#fef9e7"
C_ACIK_KIRMIZI = "#fdedec"
C_KOYU = "#1c2833"
C_GRI = "#566573"
C_SINIR = "#d5d8dc"


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:10px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def gorsel_1():
    """Şiir Dinletisi Hazırlama ve Sunma Süreci."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Şiir Dinletisi Hazırlama ve Sunma Sürecinin 4 Aşaması</text>',
    ]
    adimlar = [
        ("1. Tema ve Metin Seçimi", "Ortak bir tema (vatan, doğa, sevgi,", "gurbet) etrafında edebi değeri yüksek", "şiirler seçilir ve sıralanır.", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("2. İş Bölümü ve Fon Müziği", "Sunucu, okuyucular ve teknik ekip", "belirlenir; şiirin duygusuna uygun", "enstrümantal fon müziği seçilir.", C_YESIL, C_ACIK_YESIL, 348, 58),
        ("3. Prova ve Diksiyon", "Vurgu, tonlama, durak, ulama ve", "beden dili (jest-mimik, göz teması)", "üzerinde sesli provalar yapılır.", C_TURUNCU, C_ACIK_SARI, 18, 160),
        ("4. Sahne Sunumu ve Değerlendirme", "Sahne heyecanı kontrol edilerek", "doğal ve etkileyici bir sesle sunulur;", "akran değerlendirmesi yapılır.", C_MOR, C_ACIK_MOR, 348, 160),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in adimlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="92" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+44}" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+62}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+79}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Şiir Okumada Ses Unsurları: Vurgu, Tonlama, Durak ve Beden Dili."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Şiir Sunumunda Ahengi ve Duyguyu Yansıtan Konuşma Unsurları</text>',
    ]
    unsurlar = [
        ("Vurgu ve Tonlama", "Kelime/cümle vurgusunu doğru", "yapmak; ses tonunu duyguya göre", "alçaltıp yükseltmek.", C_MAVI, C_ACIK_MAVI, 18),
        ("Durak ve Tempo", "Hece ölçüsündeki durak yerlerinde", "ve noktalama işaretlerinde", "nefes/anlam boşluğu bırakmak.", C_YESIL, C_ACIK_YESIL, 236),
        ("Jest, Mimik ve Göz Teması", "Abartıdan (yapmacıklıktan) uzak,", "şiirin ruhuna uygun yüz ifadesi", "ve dinleyiciyle bağ kurmak.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in unsurlar:
        p.append(f'<rect x="{x}" y="58" width="208" height="165" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="78" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="136" text-anchor="middle" font-size="10.5" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="158" text-anchor="middle" font-size="10.5" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Anonim Halk Şiiri: Türkü Nazım Biçimi (Bent + Kavuştak Yapısı)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Dinleme / İzleme: Türkü Nazım Biçiminin Yapı ve Ezgi Özellikleri</text>',
        f'<rect x="20" y="58" width="310" height="186" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<text x="175" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="{C_YESIL}">1. Yapısal Bölümler (Bent + Kavuştak)</text>',
        f'<rect x="36" y="94" width="278" height="62" rx="8" fill="#fff" stroke="{C_YESIL}"/>',
        f'<text x="175" y="115" text-anchor="middle" font-size="11" font-weight="700" fill="{C_KOYU}">BENT (Asıl Söz Bölümü)</text>',
        f'<text x="175" y="134" text-anchor="middle" font-size="10" fill="{C_GRI}">Türkünün asıl konusunun işlendiği</text>',
        f'<text x="175" y="148" text-anchor="middle" font-size="10" fill="{C_GRI}">3 veya 4 dizelik bölümlerdir (aaa / aaba).</text>',
        f'<rect x="36" y="166" width="278" height="64" rx="8" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}"/>',
        f'<text x="175" y="186" text-anchor="middle" font-size="11" font-weight="700" fill="{C_TURUNCU}">KAVUŞTAK (Bağlama / Nakarat)</text>',
        f'<text x="175" y="205" text-anchor="middle" font-size="10" fill="{C_KOYU}">Her bendin sonunda tekrarlanan</text>',
        f'<text x="175" y="220" text-anchor="middle" font-size="10" fill="{C_GRI}">ve ezgiyi bütünleyen dizelerdir (bb / cc).</text>',
        f'<rect x="350" y="58" width="310" height="186" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<text x="505" y="82" text-anchor="middle" font-size="12" font-weight="700" fill="{C_MAVI}">2. Ezgilerine Göre Türkü Türleri</text>',
        f'<rect x="366" y="96" width="278" height="64" rx="8" fill="#fff" stroke="{C_MAVI}"/>',
        f'<text x="505" y="116" text-anchor="middle" font-size="11" font-weight="700" fill="{C_MAVI}">Usullü (Kırık Hava) Türküler</text>',
        f'<text x="505" y="135" text-anchor="middle" font-size="10" fill="{C_GRI}">Ölçüsü ve ritmi belli, hareketli ezgilerdir:</text>',
        f'<text x="505" y="150" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">Zeybek, Horon, Bar, Halay, Karşılama</text>',
        f'<rect x="366" y="170" width="278" height="60" rx="8" fill="#fff" stroke="{C_MOR}"/>',
        f'<text x="505" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="{C_MOR}">Usulsüz (Uzun Hava) Türküler</text>',
        f'<text x="505" y="208" text-anchor="middle" font-size="10" fill="{C_GRI}">Serbest ritimli, içli ve hüzünlü ezgilerdir:</text>',
        f'<text x="505" y="222" text-anchor="middle" font-size="10" font-weight="700" fill="{C_KOYU}">Bozlak, Maya, Hoyrat, Divan, Gurbet Havası</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Şiir ve Türkü Dili: İsim Tamlamalarının Ahenk ve İmge İşlevi."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Şiir ve Türkülerde İsim Tamlamalarının Türleri ve Üsluba Katkısı</text>',
    ]
    turler = [
        ("Belirtili İsim Tamlaması", "Tamlayan (-ın/-in) ve tamlanan (-ı/-i)", "eki alır. Tamlayan ile tamlanan arasına", "sıfat girebilir: 'gurbetin acı rüzgârı'", C_MAVI, C_ACIK_MAVI, 18),
        ("Belirtisiz İsim Tamlaması", "Tamlayan ek almaz, yalnız tamlanan", "iyelik eki alır. Kalıplaşmış kavram ve", "benzetme kurar: 'gönül dağı, seher yeli'", C_YESIL, C_ACIK_YESIL, 236),
        ("Zincirleme İsim Tamlaması", "En az üç ismin iç içe geçmesiyle", "oluşur; zengin betimleme sağlar:", "'Anadolu türkülerinin gönül sızıları'", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in turler:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="78" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="135" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="158" text-anchor="middle" font-size="10.2" font-weight="700" fill="{renk}">{s3}</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    v["bolumler"][0]["gorsel"] = GORSELLER["b1"]
    v["bolumler"][1]["gorsel"] = GORSELLER["b2"]
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
