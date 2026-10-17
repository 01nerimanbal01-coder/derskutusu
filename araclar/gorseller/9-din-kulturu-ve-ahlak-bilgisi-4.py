# -*- coding: utf-8 -*-
"""9. Sınıf Din Kültürü ve Ahlak Bilgisi — 4. Hafta görsel modülü:
1. Ünite: Allah-İnsan İlişkisi — Doğruyu Arayan Bir Varlık Olarak İnsan, Bilgi Kaynakları ve Eleştirel Düşünme"""

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
    """İslam'da Doğru Bilginin Üç Temel Kaynağı (Selim Akıl, Sağlam Duyular, Sadık Haber)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İslam Düşüncesinde Doğru Bilginin Üç Temel Kaynağı (Esbâb-ı İlim)</text>',
    ]
    kaynaklar = [
        ("1. Selim Akıl (العَقْلُ السَّلِيم)", "Ön yargı ve tutkularla", "bozulmamış, doğru düşünen,", "muhakeme yapan temiz akıl.", "Dini sorumluluğun (teklif) şartı", C_MAVI, C_ACIK_MAVI, 18),
        ("2. Sağlam Duyular (الحَواسُّ السَّلِيمَة)", "İşitme, görme, koklama,", "tatma ve dokunma duyularıyla", "elde edilen gözlem/deney bilgisi.", "Fiziksel âlemi tanıma aracı", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Sadık Haber (الخَبَرُ الصّادِق)", "1) Vahiy (Kur'an ve Sünnet)", "2) Mütevatir Haber (Yalan üzere", "birleşmesi imkânsız topluluk haberi).", "Gayb ve inanç bilgisinin kaynağı", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, alt, renk, bg, x in kaynaklar:
        p.append(f'<rect x="{x}" y="58" width="208" height="186" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="10.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="108" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="128" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="148" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+12}" y="172" width="184" height="54" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        p.append(f'<text x="{x+104}" y="203" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{alt}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Kur'an-ı Kerim'de Doğru Bilgiyi Engelleyen Tutumlar (Zan, Taklit, Hevâ, Ön Yargı)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_KIRMIZI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Doğru Bilgiye Ulaşmanın Önündeki Engeller ve Eleştirel Düşünme</text>',
    ]
    engeller = [
        ("Zan ve Tahmin (الظَّنّ)", "Kesin delile dayanmayan şüpheli", "kanaat (Hucurât, 12; Necm, 28)", C_KIRMIZI, C_ACIK_KIRMIZI, 18, 56),
        ("Körü Körüne Taklit (التَّقْلِيد)", "Sorgulamadan «Atalarımızdan böyle", "gördük» demek (Bakara, 170)", C_TURUNCU, C_ACIK_SARI, 348, 56),
        ("Hevâ ve Heves (الهَوى)", "Nefsin bencil arzularını ve çıkarlarını", "hakikatin önüne koymak (Câsiye, 23)", C_MOR, C_ACIK_MOR, 18, 152),
        ("Taassup ve Ön Yargı", "Bağnazlık, kibir ve haberi", "araştırmadan yaymak (Hucurât, 6)", C_MAVI, C_ACIK_MAVI, 348, 152),
    ]
    for baslik, s1, s2, renk, bg, x, y in engeller:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="84" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+66}" text-anchor="middle" font-size="10.5" fill="{renk}" font-weight="700">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Bağlayıcı Olmayan Öznel Kaynaklar (Rüya, İlham, Keşf, Sezgi) ve Sınırları."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Nesnel Bilgi Kaynakları ile Öznel (Subjektif) Deneyimlerin Ayrımı</text>',
        f'<rect x="18" y="58" width="314" height="166" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Genel Geçer ve Bağlayıcı Kaynaklar</text>',
        f'<text x="32" y="108" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Vahiy ve Mütevatir Haber (Sadık Haber)</text>',
        f'<text x="32" y="130" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Selim Akıl</text>',
        f'<text x="32" y="152" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Sağlam Duyular</text>',
        f'<text x="32" y="182" font-size="10.5" font-weight="700" fill="{C_YESIL}">→ Tüm Müslümanlar için delil ve ölçüdür;</text>',
        f'<text x="42" y="200" font-size="10.5" font-weight="700" fill="{C_YESIL}">inanç ve fıkıh hükümleri bunlara dayanır.</text>',
        f'<rect x="348" y="58" width="314" height="166" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Öznel ve Bağlayıcı Olmayanlar</text>',
        f'<text x="362" y="108" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Rüya, İlham, Keşf ve Sezgi</text>',
        f'<text x="362" y="130" font-size="10.5" font-weight="700" fill="{C_KOYU}">• Fal, kehanet, burçlar ve batıl inançlar</text>',
        f'<text x="362" y="158" font-size="10.5" font-weight="700" fill="{C_KIRMIZI}">→ Kişiseldir ve denetlenemez; İslam\'da</text>',
        f'<text x="372" y="176" font-size="10.5" font-weight="700" fill="{C_KIRMIZI}">kesin bilgi ve dini hüküm kaynağı OLAMAZ!</text>',
        f'<text x="372" y="198" font-size="10" fill="{C_GRI}">(Peygamberlerin rüyaları vahiy olduğu için istisnadır)</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Dijital Çağda Bilgi Ahlakı ve Teyit (التَّبَيُّن — Hucurât, 6; İsrâ, 36)."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Bilgi Ahlakı ve Dijital Çağda Doğrulama (Tebeyyün / Tahkik)</text>',
    ]
    ilkeler = [
        ("İsrâ Suresi, 36. Ayet", "«Hakkında kesin bilgin olmayan", "şeyin peşine düşme! Çünkü kulak,", "göz ve kalp bundan sorumludur.»", C_MAVI, C_ACIK_MAVI, 18),
        ("Hucurât Suresi, 6. Ayet", "«Size bir fâsık haber getirirse,", "doğruluğunu araştırın (فَتَبَيَّنُوا) ki", "bilmeden kimseye zarar vermeyesiniz.»", C_YESIL, C_ACIK_YESIL, 236),
        ("Zümer Suresi, 18. Ayet", "«Sözü dinleyip de onun en", "güzeline (en doğrusuna) uyanlar", "akıl sahipleridir.»", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in ilkeler:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">Bilgi Sorumluluğu</text>')
    return _svg(w, h, "".join(p))


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    for i, k in enumerate(["b1", "b2", "b3", "b4"]):
        if i < len(v.get("bolumler", [])) and k in GORSELLER:
            v["bolumler"][i]["gorsel"] = GORSELLER[k]
    return v
