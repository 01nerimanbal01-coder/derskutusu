# -*- coding: utf-8 -*-
"""8. Sınıf Arapça — 2. Hafta SVG görselleri (kitap s. 14–17).
Konu: Kulüpler — صَديقي / صَديقَتي uyumu, إِذَنْ ile kulüp tahmini, في المَدْرَسة / في البَيْت sorumlulukları, soru ve bağlaç alıştırmaları.
"""
from ozet_gorsel import svg


def g1():
    """Bölüm 1: صَديقي (Erkek) ve صَديقَتي (Kız) Fiil ve Bağlaç Uyumu (s. 14-15)."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#1d4ed8"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">ARKADAŞIMIZIN KULÜP TERCİHİNİ ANLATMA (صَديقي / صَديقَتي)</text>')

    # Erkek satırı
    ic.append('<rect x="20" y="66" width="740" height="96" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>')
    ic.append('<text x="390" y="92" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">Erkek Arkadaş (صَديقي فُرْقان / حَسَن / كَرَم) → Fiiller يَـ / يُـ ile başlar</text>')
    ic.append('<text x="390" y="120" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">صَديقي فُرْقان يُحِبُّ قِراءَة الكُتُب، وَلِذٰلِكَ يَخْتارُ نادي المَكْتَبَة</text>')
    ic.append('<text x="390" y="145" text-anchor="middle" font-size="12" fill="#334155">Arkadaşım Furkan kitap okumayı sever, bu nedenle kütüphane kulübünü seçer.</text>')

    # Kız satırı
    ic.append('<rect x="20" y="176" width="740" height="96" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="2"/>')
    ic.append('<text x="390" y="202" text-anchor="middle" font-size="14" font-weight="700" fill="#831843">Kız Arkadaş (صَديقَتي سُمَيَّة / مَرْيَم / زَيْنَب) → Fiiller تَـ / تُـ ile başlar</text>')
    ic.append('<text x="390" y="230" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">زَيْنَب تُحِبُّ الرِّياضة، وَلٰكِنْ تُفَضِّلُ نادي الموسيقى</text>')
    ic.append('<text x="390" y="255" text-anchor="middle" font-size="12" fill="#334155">Zeynep sporu sever fakat müzik kulübünü tercih eder.</text>')

    return svg(780, 286, "".join(ic), "Erkek ve kız arkadaş tanıtımında fiil uyumu")


def g2():
    """Bölüm 2: Sorumluluktan Kulüp Tahmini Diyaloğu (s. 14, Etkinlik 12)."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#0f766e"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">SORUMLULUKTAN KULÜP TAHMİN ETME (خَمِّنْ نادِيَهُ)</text>')

    adimlar = [
        (30, 68, 500, 62, "#f0fdfa", "#0d9488", "هَلْ أَنْتَ مَسْؤول عَنْ أَدَوات الرِّياضِيَّة؟", "Spor malzemelerinden mi sorumlusun?"),
        (555, 68, 195, 62, "#fee2e2", "#e11d48", "لا.", "Hayır."),
        (30, 144, 500, 62, "#f0fdfa", "#0d9488", "هَلْ أَنْتَ مَسْؤول عَنْ تَرْتيب الكُتُب؟", "Kitapları düzenlemekten mi sorumlusun?"),
        (555, 144, 195, 62, "#dcfce7", "#16a34a", "نَعَم، صَحيح!", "Evet, doğru!"),
    ]
    for x, y, w, h, bg, st, ar, tr in adimlar:
        ic.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.8"/>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 26}" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">{ar}</text>')
        ic.append(f'<text x="{x + w // 2}" y="{y + 47}" text-anchor="middle" font-size="12" fill="#334155">{tr}</text>')

    ic.append('<rect x="30" y="220" width="720" height="62" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>')
    ic.append('<text x="390" y="246" text-anchor="middle" font-size="16" font-weight="700" fill="#78350f">إِذَنْ، أَنْتَ عُضْو في نادي المَكْتَبَة!</text>')
    ic.append('<text x="390" y="268" text-anchor="middle" font-size="13" font-weight="600" fill="#92400e">Öyleyse sen kütüphane kulübünün bir üyesisin!</text>')

    return svg(780, 296, "".join(ic), "Sorumluluktan kulüp tahmin etme diyaloğu")


def g3():
    """Bölüm 5: Okulda ve Evde Sorumlulukları Sınıflandırma (s. 16, Etkinlik 16)."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#4f46e5"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">أَنا مَسْؤول عَنْ... — OKULDA VE EVDE SORUMLULUKLARIM (s. 16)</text>')

    # Sol sütun: في المَدْرَسة
    ic.append('<rect x="20" y="65" width="360" height="235" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>')
    ic.append('<rect x="20" y="65" width="360" height="36" rx="10" fill="#2563eb"/>')
    ic.append('<text x="200" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">في المَدْرَسة (Okulda)</text>')

    okul = [
        ("اِحْتِرام المُدَرِّسين", "Öğretmenlere saygı göstermek"),
        ("الحِفاظ عَلى نَظافة الصَّفّ", "Sınıfın temizliğini korumak"),
        ("مُساعَدة الأَصْدِقاء في الصَّفّ", "Sınıfta arkadaşlara yardım etmek"),
        ("الاِسْتِماع إِلى المُدَرِّس في الدَّرْس", "Derste öğretmeni dinlemek"),
    ]
    for i, (ar, tr) in enumerate(okul):
        y = 118 + i * 44
        ic.append(f'<text x="200" y="{y}" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">{ar}</text>')
        ic.append(f'<text x="200" y="{y + 17}" text-anchor="middle" font-size="12" fill="#475569">{tr}</text>')

    # Sağ sütun: في البَيْت
    ic.append('<rect x="400" y="65" width="360" height="235" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>')
    ic.append('<rect x="400" y="65" width="360" height="36" rx="10" fill="#059669"/>')
    ic.append('<text x="580" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">في البَيْت (Evde)</text>')

    ev = [
        ("مُساعَدة الوالِدَين", "Anne ve babaya yardım etmek"),
        ("تَرْتيب الغُرْفة", "Odayı düzenlemek / toplamak"),
        ("أَدْرُسُ في البَيْت كُلَّ مَساء", "Her akşam evde ders çalışmak"),
        ("أَسْتَيْقِظُ مُبَكِّرًا في الصَّباح", "Sabahleyin erken uyanmak"),
    ]
    for i, (ar, tr) in enumerate(ev):
        y = 118 + i * 44
        ic.append(f'<text x="580" y="{y}" text-anchor="middle" font-size="14" font-weight="700" fill="#065f46">{ar}</text>')
        ic.append(f'<text x="580" y="{y + 17}" text-anchor="middle" font-size="12" fill="#475569">{tr}</text>')

    return svg(780, 312, "".join(ic), "Okuldaki ve evdeki sorumlulukların sınıflandırılması")


def g4():
    """Bölüm 6: Alıştırmalardaki Soru Sözcükleri ve Bağlaçlar (s. 17, التَّدْريبات)."""
    ic = []
    ic.append('<rect x="15" y="12" width="750" height="40" rx="8" fill="#b45309"/>')
    ic.append('<text x="390" y="37" text-anchor="middle" font-size="15" font-weight="700" fill="#ffffff">SORU SÖZCÜKLERİ VE BAĞLAÇ ALIŞTIRMALARI (التَّدْريبات - s. 17)</text>')

    satirlar = [
        (64, "#eff6ff", "#3b82f6", "مَنْ يَخْتارُ نادي التِّكْنولوجِيا؟", "عُمَر يَخْتارُ نادي التِّكْنولوجِيا (Kişi → مَنْ)"),
        (114, "#fef3c7", "#f59e0b", "لِماذا تَخْتارُ مَرْوة نادي الرَّسْم؟", "لِأَنَّها تُحِبُّ الرَّسْم (Sebep → لِماذا)"),
        (164, "#dcfce7", "#16a34a", "هَلْ تُحِبُّ الرِّياضة؟", "نَعَم، أُحِبُّ الرِّياضة (Onay → هَلْ)"),
        (214, "#f3e8ff", "#9333ea", "مَتى سَنَخْتارُ الأَنْدِية؟", "سَنَخْتارُ الأَنْدِية اليَوْم (Zaman → مَتى)"),
        (264, "#fee2e2", "#e11d48", "أَتُفَضِّلُ نادي المَسْرَحِيَّة أَمْ نادي الرَّسْم؟", "Soru cümlesinde 'yoksa' → أَمْ"),
    ]
    for y, bg, st, sol, sag in satirlar:
        ic.append(f'<rect x="20" y="{y}" width="365" height="42" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.8"/>')
        ic.append(f'<text x="202" y="{y + 26}" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">{sol}</text>')
        ic.append(f'<rect x="395" y="{y}" width="365" height="42" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>')
        ic.append(f'<text x="577" y="{y + 26}" text-anchor="middle" font-size="13" font-weight="600" fill="#1e293b">{sag}</text>')

    return svg(780, 318, "".join(ic), "Soru sözcükleri ve bağlaç alıştırmaları özeti")


def uygula(v):
    b = v["bolumler"]
    b[0]["gorsel"] = g1()
    b[1]["gorsel"] = g2()
    b[4]["gorsel"] = g3()
    b[5]["gorsel"] = g4()
