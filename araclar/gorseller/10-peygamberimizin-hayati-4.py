# -*- coding: utf-8 -*-
"""10. Sınıf Peygamberimizin Hayatı — 4. Hafta görsel modülü:
Taif Yolculuğu (2. Bölüm): Nahle Vadisi, Mut'im bin Adî'nin Himayesi (Civâr) ve Tebliğde Ümit"""

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
    """Taif Dönüşü Güzergâhı: Karnü's-Seâlib, Nahle Vadisi ve Hira Dağı."""
    w, h = 680, 255
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Taif\'ten Mekke\'ye Dönüş Sürecindeki Önemli Duraklar (Nübüvvetin 10. Yılı)</text>',
    ]
    duraklar = [
        ("1. Karnü's-Seâlib", "Cebrail (as) ve Dağlar Meleği'nin", "gelmesi; Hz. Peygamber'in (sav)", "helak yerine hidayet dilemesi.", C_YESIL, C_ACIK_YESIL, 18),
        ("2. Nahle Vadisi", "Birkaç gün konaklama; Nusaybin", "cinlerinin Kur'an dinleyip", "iman etmesi (Ahkâf ve Cin sureleri).", C_MOR, C_ACIK_MOR, 236),
        ("3. Hira ve Mekke'ye Giriş", "Mut'im bin Adî'nin 'civâr'", "(himaye/eman) vermesiyle", "güvenle Kâbe'yi tavaf etmesi.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in duraklar:
        p.append(f'<rect x="{x}" y="58" width="208" height="178" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="114" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="135" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="156" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Cahiliye Döneminde Güvenlik Uygulaması: Civâr (Eman / Himaye) Sistemi."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Mekke\'ye Dönüşte \'Civâr\' (Himaye) Uygulaması ve Mut\'im bin Adî</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_SARI}" stroke="{C_TURUNCU}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_TURUNCU}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Neden Himaye (Civâr) Gerekti?</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">• Ebû Tâlib\'in vefatı ve Ebû Leheb\'in</text>',
        f'<text x="175" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">himayeyi kaldırması sonrası Taif\'e</text>',
        f'<text x="175" y="142" text-anchor="middle" font-size="10.2" fill="{C_GRI}">gidilmesi müşrikleri daha da kışkırtmıştı.</text>',
        f'<text x="175" y="168" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">• Hz. Peygamber (sav) tedbir alarak</text>',
        f'<text x="175" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_TURUNCU}">hukuki güvenlik (civâr) talep etmiştir.</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">Görüşülen Kişiler ve Sonuç</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">1. Ahnes bin Şerîk (Reddetti)</text>',
        f'<text x="505" y="126" text-anchor="middle" font-size="10.2" fill="{C_KOYU}">2. Süheyl bin Amr (Reddetti)</text>',
        f'<text x="505" y="148" text-anchor="middle" font-size="10.5" font-weight="700" fill="{C_YESIL}">3. Mut\'im bin Adî (Kabul Etti!)</text>',
        f'<text x="505" y="170" text-anchor="middle" font-size="10" fill="{C_GRI}">Oğullarıyla silahlanarak Harem-i Şerif\'te</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10" fill="{C_GRI}">Hz. Peygamber\'i (sav) himayesine aldığını ilan etti.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Taif'in İslamlaşma Süreci (Hicretin 8 ve 9. Yılları)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Hz. Peygamber\'in (sav) Duasının Kabulü: Taif\'in Müslüman Oluşu (630)</text>',
    ]
    surec = [
        ("620: Taif Yolculuğu ve Dua", "'Soylarından yalnız Allah'a", "ibadet edecek bir nesil çıkar'", "duasıyla Taif halkını affetmesi.", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("630 (H. 8): Taif Kuşatması", "Huneyn Savaşı sonrası kuşatma;", "Hz. Peygamber'in (sav) Taiflilerin", "hidayeti için tekrar dua etmesi.", C_TURUNCU, C_ACIK_SARI, 348, 56),
        ("630 (H. 9): Sakîf Heyeti", "Urve bin Mes'ûd'un şehadeti sonrası", "Taif (Sakîf) heyetinin Medine'ye", "gelerek kendi isteğiyle İslam'a girmesi.", C_YESIL, C_ACIK_YESIL, 18, 152),
        ("Sonuç: Sadık Bir İslam Şehri", "Lât putunun yıkılması ve Osman bin", "Ebü'l-Âs'ın vali atanmasıyla Taif'in", "İslam'ın sarsılmaz kalesi olması.", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in surec:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="10" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="10" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Taif Yolculuğundan Çıkarılan Evrensel İlkeler."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Taif Yolculuğundan Günümüze Yansıyan Nebevî İlkeler</text>',
    ]
    ilkeler = [
        ("1. Ümitsizliğe Kapılmama", "En ağır reddediliş ve", "sıkıntı anında bile yeni", "çözüm yolları aramak.", C_MAVI, C_ACIK_MAVI, 18),
        ("2. İntikam Değil Merhamet", "Kötülüğe kötülükle değil;", "affedicilik, dua ve gelecek", "nesli kazanma ufkuyla yaklaşmak.", C_YESIL, C_ACIK_YESIL, 236),
        ("3. Tedbir ve Vefa Ahlakı", "Güvenlik için meşru tedbirlere", "başvurmak ve yapılan iyiliği", "(Mut'im bin Adî'yi) asla unutmamak.", C_TURUNCU, C_ACIK_SARI, 454),
    ]
    for baslik, s1, s2, s3, renk, bg, x in ilkeler:
        p.append(f'<rect x="{x}" y="58" width="208" height="170" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="208" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+104}" y="77" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+104}" y="112" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+104}" y="132" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+104}" y="152" text-anchor="middle" font-size="10.2" fill="{C_GRI}">{s3}</text>')
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
    v["bolumler"][3]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
