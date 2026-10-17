# -*- coding: utf-8 -*-
"""9. Sınıf Peygamberimizin Hayatı — 4. Hafta görsel modülü:
1. Ünite: Peygamberimizin Hayatında Önemli Bir Şehir: Mekke — 2. İslam Öncesinde Mekke'nin Toplumsal Yapısı ve Cahiliye Kültürü"""

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
    """İslam Öncesi Arap Yarımadası'nda Yaşam Tarzı (Bedevî ve Hadarî) ve Toplumsal Sınıflar."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'İslam Öncesi Mekke\'de Yaşam Tarzı ve Sosyal Tabakalaşma</text>',
        # Sol: Yaşam Tarzı
        f'<rect x="18" y="58" width="314" height="182" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="58" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Yaşam Tarzına Göre Toplum</text>',
        f'<text x="32" y="108" font-size="11" font-weight="700" fill="{C_MAVI}">1. Bedevîler (البَدْو — Konargöçerler):</text>',
        f'<text x="42" y="126" font-size="10.5" fill="{C_KOYU}">• Çöl ve vahalarda çadırlarda yaşarlar.</text>',
        f'<text x="42" y="144" font-size="10.5" fill="{C_KOYU}">• Deve ve koyun yetiştiriciliğiyle geçinirler.</text>',
        f'<text x="32" y="172" font-size="11" font-weight="700" fill="{C_YESIL}">2. Hadarîler (الحَضَر — Yerleşikler):</text>',
        f'<text x="42" y="190" font-size="10.5" fill="{C_KOYU}">• Mekke, Yesrib ve Tâif gibi şehirlerde yaşarlar.</text>',
        f'<text x="42" y="208" font-size="10.5" fill="{C_KOYU}">• Kervan ticareti (Kureyş) ve tarımla uğraşırlar.</text>',
        # Sağ: Sosyal Tabakalar
        f'<rect x="348" y="58" width="314" height="182" rx="10" fill="{C_ACIK_KIRMIZI}" stroke="{C_KIRMIZI}" stroke-width="1.6"/>',
        f'<rect x="348" y="58" width="314" height="28" rx="10" fill="{C_KIRMIZI}"/>',
        f'<text x="505" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Keskin Sosyal Sınıflar (Eşitsizlik)</text>',
        f'<text x="362" y="108" font-size="11" font-weight="700" fill="{C_KOYU}">1. Hürler (Ahrâr / Eşrâf):</text>',
        f'<text x="372" y="124" font-size="10.5" fill="{C_GRI}">Kabile reisleri ve zengin tüccarlar (tüm haklara sahip).</text>',
        f'<text x="362" y="150" font-size="11" font-weight="700" fill="{C_TURUNCU}">2. Mevâlî (Azatlı Köleler ve Sığınmacılar):</text>',
        f'<text x="372" y="166" font-size="10.5" fill="{C_GRI}">Hür bir kabilenin himayesinde yaşayanlar.</text>',
        f'<text x="362" y="192" font-size="11" font-weight="700" fill="{C_KIRMIZI}">3. Köleler ve Cariyeler (Esirler):</text>',
        f'<text x="372" y="208" font-size="10.5" fill="{C_GRI}">Hiçbir insani hakkı olmayan, alınıp satılan kesim.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Cahiliye Kültürünün Temel Özellikleri (Asabiyet, Kan Davaları, Kadının Konumu)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_KIRMIZI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Cahiliye Dönemi (الجاهِلِيَّة) Toplumsal Karanlığının Temel Unsurları</text>',
    ]
    unsurlar = [
        ("Kabilecilik (Asabiyet)", "«Zalim de olsa mazlum da olsa", "kabile kardeşine yardım et!»", "anlayışı; hak değil güç üstündü.", C_KIRMIZI, C_ACIK_KIRMIZI, 18, 56),
        ("Kan Davaları (Eyyâmü'l-Arab)", "Kabileler arasında onlarca yıl", "süren yıkıcı intikam savaşları", "(Ficâr ve Basûs savaşları).", C_TURUNCU, C_ACIK_SARI, 348, 56),
        ("Kadın ve Kız Çocukları", "Kadına miras hakkı verilmemesi", "ve bazı kabilelerde kız çocuklarının", "diri diri gömülmesi (Ve'd-i Benât).", C_MOR, C_ACIK_MOR, 18, 152),
        ("Ekonomik ve Ahlaki Çöküş", "Tefecilik (ribâ/faiz), içki, kumar,", "fal okları ve zayıfların/yetimlerin", "mallarının gasp edilmesi.", C_MAVI, C_ACIK_MAVI, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in unsurlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+41}" text-anchor="middle" font-size="10" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+75}" text-anchor="middle" font-size="10" fill="{renk}" font-weight="700">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Mekke'de Dini Yapı (Putperestlik ve Hanîflik) ile Olumlu Erdemler (Hilfü'l-Fudûl)."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Mekke\'de İnanç Yapısı ve Cahiliye İçindeki Olumlu Değerler</text>',
    ]
    kutular = [
        ("Putperestlik (Şirk)", "Allah'a (cc) inanmakla birlikte", "putları (Hübel, Lât, Menât, Uzzâ)", "şefaatçi/aracı kabul etme.", C_KIRMIZI, C_ACIK_KIRMIZI, 18),
        ("Hanîflik (Tevhid İzleri)", "Hz. İbrahim'in (as) tevhid dinine", "bağlı kalıp putlara tapmayan", "muvahhidler (Zeyd b. Amr vb.).", C_YESIL, C_ACIK_YESIL, 236),
        ("Olumlu Erdemler & Hilfü'l-Fudûl", "Cömertlik, misafirperverlik, sözde", "durma ve mazlumu koruyan", "Erdemliler Topluluğu (590).", C_MAVI, C_ACIK_MAVI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in kutular:
        p.append(f'<rect x="{x}" y="58" width="208" height="172" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="202" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">Mekke Toplum Yapısı</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Mekke'de İdari, Ticari ve Kültürel Hayat (Dârünnedve, Haram Aylar, Panayırlar)."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Mekke\'de Yönetim, Kâbe Görevleri, Ticaret ve Edebiyat Panayırları</text>',
    ]
    kurumlar = [
        ("Dârünnedve ve Kâbe Görevleri", "Kusay b. Kilâb'ın kurduğu danışma", "meclisi; Sikâye, Rifâde, Sidâne,", "Liva ve Nedve görevleri.", C_MOR, C_ACIK_MOR, 18),
        ("Kış ve Yaz Kervanları (Îlâf)", "Kureyş'in kışın Yemen'e, yazın", "Şam'a düzenlediği uluslararası", "ticaret seferleri (Kureyş Suresi).", C_MAVI, C_ACIK_MAVI, 236),
        ("Haram Aylar ve Panayırlar", "Zilkade, Zilhicce, Muharrem, Recep;", "Ukâz, Mecenne ve Zülmecâz", "ticaret ve şiir panayırları.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in kurumlar:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">Sosyo-Kültürel Yapı</text>')
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
