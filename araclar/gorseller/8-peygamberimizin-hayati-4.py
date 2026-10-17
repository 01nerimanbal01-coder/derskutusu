# -*- coding: utf-8 -*-
"""8. Sınıf Peygamberimizin Hayatı — 4. Hafta görsel modülü:
1. Ünite: Peygamberimizin Medine Yılları — Hicret ve Medine'de İslam Toplumunun Kuruluşu"""

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
    """Mekke'den Medine'ye Hicret Hazırlıkları: Akabe Biatları (621-622)."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hicretin Zemini: Mekke Dönemi Zorlukları ve Akabe Biatları (621–622)</text>',
    ]
    asamalar = [
        ("Mekke'deki Baskılar", "13 yıllık tebliğ sürecinde", "boykot, işkence ve Hüzün", "Yılı'nın yaşanması", C_KIRMIZI, C_ACIK_KIRMIZI, 18),
        ("1. Akabe Biatı (621)", "Yesribli 12 kişinin İslam'a", "girmesi ve Mus'ab bin", "Umeyr'in öğretmenliği", C_YESIL, C_ACIK_YESIL, 236),
        ("2. Akabe Biatı (622)", "Yesribli 75 Müslümanın", "Peygamberimizi (sav)", "şehirlerine davet etmesi", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in asamalar:
        p.append(f'<rect x="{x}" y="58" width="208" height="180" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="30" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+20}" y="176" width="168" height="46" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        alt = "Tâif yolculuğu ve sabır" if x == 18 else ("İslam'ın ilk öğretmeni" if x == 236 else "Hicret izni verildi")
        p.append(f'<text x="{x+104}" y="204" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">{alt}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Hicret Yolculuğu (622): Emanet, Tedbir ve Tevekkül."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Mekke\'den Yesrib\'e (Medine\'ye) Hicret Yolculuğu (Miladi 622)</text>',
    ]
    duraklar = [
        ("1. Emanet Bilinci", "Hz. Ali'nin (ra) emanetleri", "sahiplerine vermek için", "Mekke'de kalması", C_MAVI, C_ACIK_MAVI, 16),
        ("2. Sevr Mağarası", "Hz. Ebû Bekir (ra) ile", "3 gün gizlenme: «Üzülme,", "Allah bizimledir!»", C_TURUNCU, C_ACIK_SARI, 182),
        ("3. Kuba Mescidi", "İslam tarihinde inşa", "edilen ilk mescit", "(Takva Mescidi)", C_YESIL, C_ACIK_YESIL, 348),
        ("4. Medine'ye Varış", "Ranuna Vadisi'nde ilk", "Cuma namazı ve Yesrib'in", "Medinetü'n-Nebî olması", C_MOR, C_ACIK_MOR, 514),
    ]
    for i, (baslik, s1, s2, s3, renk, bg, x) in enumerate(duraklar):
        p.append(f'<rect x="{x}" y="60" width="150" height="182" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="60" width="150" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+75}" y="79" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+75}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+75}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+75}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<rect x="{x+18}" y="182" width="114" height="44" rx="8" fill="#fff" stroke="{renk}" stroke-width="1.2"/>')
        etiket = ["Muhammedü'l-Emîn", "Tevekkül (Tevbe, 40)", "İlk İbadethane", "Ebû Eyyûb el-Ensârî"][i]
        p.append(f'<text x="{x+75}" y="209" text-anchor="middle" font-size="10" font-weight="700" fill="{renk}">{etiket}</text>')
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Medine'de İslam Toplumunun Kuruluşunu Sağlayan 4 Temel Adım."""
    w, h = 680, 265
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Medine\'de İslam Toplumunun Kuruluşu: Dört Kurucu Adım</text>',
    ]
    adimlar = [
        ("1. Mescid-i Nebî ve Suffe", "İbadet, eğitim (Suffe Mektebi),", "danışma ve yönetim merkezi", C_MAVI, C_ACIK_MAVI, 18, 58),
        ("2. Muâhât (Ensar-Muhacir Kardeşliği)", "Mekkeli Muhacirler ile Medineli", "Ensar'ın öz kardeş ilan edilmesi", C_YESIL, C_ACIK_YESIL, 348, 58),
        ("3. Medine Sözleşmesi (Vatandaşlık)", "Müslümanlar ve Yahudiler arasında", "barış, güvenlik ve ortak savunma ilkesi", C_TURUNCU, C_ACIK_SARI, 18, 158),
        ("4. Medine Çarşısı ve Nüfus Sayımı", "Dürüst ticaret ortamının kurulması", "ve toplumsal yapının belirlenmesi", C_MOR, C_ACIK_MOR, 348, 158),
    ]
    for baslik, s1, s2, renk, bg, x, y in adimlar:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="88" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+19}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+50}" text-anchor="middle" font-size="11" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+70}" text-anchor="middle" font-size="11" fill="{renk}" font-weight="700">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Mescid-i Nebî'nin Bölümleri ve İşlevleri."""
    w, h = 680, 240
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Mescid-i Nebî\'nin Bölümleri: Mescit, Suffe ve Hücre-i Saâdet</text>',
    ]
    bolumler = [
        ("Mescit (İbadet ve Şûra)", "Günlük namazların kılındığı,", "elçilerin kabul edildiği ve", "toplumsal kararların alındığı alan.", C_MAVI, C_ACIK_MAVI, 18),
        ("Suffe (Eğitim Merkezi)", "Kimsesiz ve ilim öğrenmek isteyen", "sahabilerin (Ashâb-ı Suffe) kaldığı", "İslam'ın ilk yatılı okulu.", C_YESIL, C_ACIK_YESIL, 236),
        ("Hücre-i Saâdet", "Peygamberimiz (sav) ve ailesinin", "sade bir hayat sürdüğü", "mütevazı odalar.", C_MOR, C_ACIK_MOR, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in bolumler:
        p.append(f'<rect x="{x}" y="58" width="208" height="166" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s1}</text>')
        p.append(f'<text x="{x+104}" y="134" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s2}</text>')
        p.append(f'<text x="{x+104}" y="154" text-anchor="middle" font-size="10.5" fill="{C_KOYU}" font-weight="600">{s3}</text>')
        p.append(f'<text x="{x+104}" y="198" text-anchor="middle" font-size="10.5" font-weight="700" fill="{renk}">Medine Medeniyetinin Kalbi</text>')
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
