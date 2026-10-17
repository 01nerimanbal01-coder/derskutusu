# -*- coding: utf-8 -*-
"""10. Sınıf Arapça — 4. Hafta görsel modülü:
Ünite 1: Değerlerim — Ders 1: Akrabalarım (Akraba Ziyareti, İsim ve Fiil Cümleleri, Meslek Diyalogları)"""

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
    """Sıla-i Rahim ve Akraba İlişkilerinde Kullanılan Müzari Fiiller."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Akraba İlişkileri ve Mesleklerde Hedef Müzari Fiiller (الأَفْعَالُ الْمُضَارِعَةُ)</text>',
    ]
    fiiller = [
        ("يُحِبُّ / يَحْتَرِمُ", "Sever / Saygı duyar", "أُحِبُّ جَدِّي وَأَحْتَرِمُ جَدَّتِي", "(Dedemi severim ve nineme saygı duyarım)", C_YESIL, C_ACIK_YESIL, 18, 56),
        ("يَزُورُ / يَهْتَمُّ (بِـ)", "Ziyaret eder / İlgilenir", "نَزُورُ أَقَارِبَنَا فِي الْعِيدِ", "(Bayramda akrabalarımızı ziyaret ederiz)", C_MAVI, C_ACIK_MAVI, 348, 56),
        ("يَفْحَصُ / يُدَرِّسُ", "Muayene eder / Ders verir", "الطَّبِيبُ يَفْحَصُ الْمَرْضَى", "(Doktor hastaları muayene eder)", C_TURUNCU, C_ACIK_SARI, 18, 156),
        ("يَسُوقُ / يُحَافِظُ (عَلَى)", "Sürer / Korur", "الشُّرْطِيُّ يُحَافِظُ عَلَى الأَمْنِ", "(Polis güvenliği korur)", C_MOR, C_ACIK_MOR, 348, 156),
    ]
    for ar, tr, ornek_ar, ornek_tr, renk, bg, x, y in fiiller:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="90" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="26" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+18}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{ar} — {tr}</text>')
        p.append(f'<text x="{x+157}" y="{y+48}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{C_KOYU}">{ornek_ar}</text>')
        p.append(f'<text x="{x+157}" y="{y+72}" text-anchor="middle" font-size="10" fill="{C_GRI}">{ornek_tr}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Soru Kalıpları: Meslek ve Çalışma Yeri Sorma (مَا مِهْنَةُ...؟ / أَيْنَ يَعْمَلُ...؟)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Meslek ve Çalışma Yeri Diyalog Kalıpları (مَا مِهْنَةُ...؟ / أَيْنَ يَعْمَلُ...؟)</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Eril (Müzekker) Akraba İçin</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="12" font-weight="700" fill="{C_KOYU}">مَا مِهْنَةُ عَمِّكَ؟  →  هُوَ مُهَنْدِسٌ.</text>',
        f'<text x="175" y="125" text-anchor="middle" font-size="9.8" fill="{C_GRI}">(Amcanın mesleği nedir? → O mühendistir.)</text>',
        f'<text x="175" y="154" text-anchor="middle" font-size="12" font-weight="700" fill="{C_MAVI}">أَيْنَ يَعْمَلُ عَمُّكَ؟  →  يَعْمَلُ فِي الْمَصْنَعِ.</text>',
        f'<text x="175" y="174" text-anchor="middle" font-size="9.8" fill="{C_GRI}">(Amcan nerede çalışıyor? → Fabrikada çalışıyor.)</text>',
        f'<text x="175" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="{C_YESIL}">مَاذَا يَفْعَلُ؟  →  يُصَمِّمُ الآلَاتِ.</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_MOR}" stroke="{C_MOR}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_MOR}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Dişil (Müennes) Akraba İçin</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="12" font-weight="700" fill="{C_KOYU}">مَا مِهْنَةُ خَالَتِكِ؟  →  هِيَ مُمَرِّضَةٌ.</text>',
        f'<text x="505" y="125" text-anchor="middle" font-size="9.8" fill="{C_GRI}">(Teyzenin mesleği nedir? → O hemşiredir.)</text>',
        f'<text x="505" y="154" text-anchor="middle" font-size="12" font-weight="700" fill="{C_MOR}">أَيْنَ تَعْمَلُ خَالَتُكِ؟  →  تَعْمَلُ فِي الْمُسْتَشْفَى.</text>',
        f'<text x="505" y="174" text-anchor="middle" font-size="9.8" fill="{C_GRI}">(Teyzen nerede çalışıyor? → Hastanede çalışıyor.)</text>',
        f'<text x="505" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="{C_TURUNCU}">مَاذَا تَفْعَلُ؟  →  تَهْتَمُّ بِالْمَرْضَى.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """İsim Cümlesi (الجملة الاسمية) ve Fiil Cümlesi (الجملة الفعلية) Karşılaştırması."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İsim Cümlesi ve Fiil Cümlesinde Tekil - İkil - Çoğul Uyumu</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">İsim Cümlesi (Mübteda + Haber Uyumu)</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">الْمُعَلِّمُ مُجْتَهِدٌ (Tekil)</text>',
        f'<text x="175" y="132" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">الْمُعَلِّمَانِ مُجْتَهِدَانِ (İkil: -âni)</text>',
        f'<text x="175" y="158" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">الْمُعَلِّمُونَ مُجْتَهِدُونَ (Çoğul: -ûne)</text>',
        f'<text x="175" y="190" text-anchor="middle" font-size="10" fill="{C_GRI}">İsim cümlesinde haber, mübtedaya hem</text>',
        f'<text x="175" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="{C_TURUNCU}">cinsiyet hem de sayı bakımından uyar!</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Fiil Cümlesi (Başta Fiil Tekil Kalır!)</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">يَعْمَلُ الْمُهَنْدِسُ (Tekil Fâil)</text>',
        f'<text x="505" y="132" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">يَعْمَلُ الْمُهَنْدِسَانِ (İkil Fâil)</text>',
        f'<text x="505" y="158" text-anchor="middle" font-size="11.5" font-weight="700" fill="{C_KOYU}">يَعْمَلُ الْمُهَنْدِسُونَ (Çoğul Fâil)</text>',
        f'<text x="505" y="190" text-anchor="middle" font-size="10" fill="{C_GRI}">Fiil cümle başında geldiğinde fâil ikil veya</text>',
        f'<text x="505" y="208" text-anchor="middle" font-size="10" font-weight="700" fill="{C_YESIL}">çoğul olsa da fiil daima TEKİL (مُفْرَد) gelir!</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_4():
    """İyelik (Muttasıl) Zamirleri ile Akrabalık Kelimeleri."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Akrabalık İsimlerinin Muttasıl (İyelik) Zamirlerle Kullanımı</text>',
    ]
    zamirler = [
        ("ـِي (Benim)", "جَدِّي / خَالَتِي", "Benim dedem / teyzem", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("ـكَ / ـكِ (Senin)", "عَمُّكَ / عَمَّتُكِ", "Senin amcan (eril) / halan (dişil)", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("ـهُ / ـهَا (Onun)", "وَالِدُهُ / وَالِدَتُهَا", "Onun (eril) babası / Onun (dişil) annesi", C_TURUNCU, C_ACIK_SARI, 18, 148),
        ("ـنَا (Bizim)", "أَقَارِبُنَا / أُسْرَتُنَا", "Bizim akrabalarımız / ailemiz", C_MOR, C_ACIK_MOR, 348, 148),
    ]
    for baslik, ar, tr, renk, bg, x, y in zamirler:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="82" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+46}" text-anchor="middle" font-size="13" font-weight="700" fill="{C_KOYU}">{ar}</text>')
        p.append(f'<text x="{x+157}" y="{y+68}" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{tr}</text>')
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
