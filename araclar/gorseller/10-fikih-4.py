# -*- coding: utf-8 -*-
"""10. Sınıf Fıkıh — 4. Hafta görsel modülü:
1. Fıkıh İlmi ve Tarihi — Fıkıh İlminin Temel İlkeleri İle İlgili Argümanlar, Zarûriyyât-ı Hamse ve Azimet-Ruhsat"""

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
    """Fıkhın Gayesi (Makâsıdü'ş-Şerîa): Zarûriyyât-ı Hamse (Korunması Zorunlu 5 Temel Değer)."""
    w, h = 680, 260
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MAVI}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Makâsıdü\'ş-Şerîa: Zarûriyyât-ı Hamse (Korunması Zorunlu 5 Temel Hak)</text>',
    ]
    haklar = [
        ("1. Dinin Korunması", "(Hıfzu'd-Dîn)", "İnanç ve ibadet", "özgürlüğünün güvencesi.", C_YESIL, C_ACIK_YESIL, 16),
        ("2. Canın Korunması", "(Hıfzu'n-Nefs)", "Yaşama hakkı ve beden", "bütünlüğünün dokunulmazlığı.", C_KIRMIZI, C_ACIK_KIRMIZI, 146),
        ("3. Aklın Korunması", "(Hıfzu'l-Akl)", "Düşünme yetisinin korunması;", "sarhoş edici şeylerin yasağı.", C_MAVI, C_ACIK_MAVI, 276),
        ("4. Neslin Korunması", "(Hıfzu'n-Nesl)", "Aile kurumunun, iffetin", "ve çocuk haklarının korunması.", C_MOR, C_ACIK_MOR, 406),
        ("5. Malın Korunması", "(Hıfzu'l-Mâl)", "Helal mülkiyet hakkı; hırsızlık,", "faiz ve rüşvetin yasaklanması.", C_TURUNCU, C_ACIK_SARI, 536),
    ]
    for baslik, ar, s1, s2, renk, bg, x in haklar:
        p.append(f'<rect x="{x}" y="58" width="126" height="184" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="58" width="126" height="28" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+63}" y="76" text-anchor="middle" font-size="9.8" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+63}" y="106" text-anchor="middle" font-size="9.8" font-weight="700" fill="{renk}">{ar}</text>')
        p.append(f'<text x="{x+63}" y="138" text-anchor="middle" font-size="9.2" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+63}" y="158" text-anchor="middle" font-size="9.2" fill="{C_GRI}">{s2}</text>')
    return _svg(w, h, "".join(p))


def gorsel_2():
    """Tekliflerde Kolaylık: Azîmet ve Ruhsat Hükümleri."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_YESIL}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Tekliflerde Kolaylık Argümanı: Azîmet ve Ruhsat Dengesi</text>',
        f'<rect x="18" y="56" width="314" height="178" rx="10" fill="{C_ACIK_MAVI}" stroke="{C_MAVI}" stroke-width="1.6"/>',
        f'<rect x="18" y="56" width="314" height="28" rx="10" fill="{C_MAVI}"/>',
        f'<text x="175" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Azîmet (Normal Şartlardaki Hüküm)</text>',
        f'<text x="175" y="106" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">• Herhangi bir zorluk veya mazeret</text>',
        f'<text x="175" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">yokken bütün mükelleflerin uymakla</text>',
        f'<text x="175" y="142" text-anchor="middle" font-size="10.2" fill="{C_GRI}">yükümlü olduğu asli hükümlerdir.</text>',
        f'<text x="175" y="168" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MAVI}">Örn: Su varken abdest almak; 4 rekâtlı</text>',
        f'<text x="175" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_MAVI}">farz namazları tam ve ayakta kılmak.</text>',
        f'<rect x="348" y="56" width="314" height="178" rx="10" fill="{C_ACIK_YESIL}" stroke="{C_YESIL}" stroke-width="1.6"/>',
        f'<rect x="348" y="56" width="314" height="28" rx="10" fill="{C_YESIL}"/>',
        f'<text x="505" y="75" text-anchor="middle" font-size="11.5" font-weight="700" fill="#fff">Ruhsat (Mazerete Bağlı Kolaylık)</text>',
        f'<text x="505" y="106" text-anchor="middle" font-size="10.2" font-weight="600" fill="{C_KOYU}">• Hastalık, yolculuk (seferîlik), su</text>',
        f'<text x="505" y="124" text-anchor="middle" font-size="10.2" fill="{C_GRI}">bulamama veya zaruret gibi arızî</text>',
        f'<text x="505" y="142" text-anchor="middle" font-size="10.2" fill="{C_GRI}">sebeplerle tanınan geçici kolaylıklardır.</text>',
        f'<text x="505" y="168" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">Örn: Teyemmüm yapmak; yolculukta 4 rekâtlı</text>',
        f'<text x="505" y="186" text-anchor="middle" font-size="10.2" font-weight="700" fill="{C_YESIL}">farzları 2 rekât kılmak ve orucu ertelemek.</text>',
    ]
    return _svg(w, h, "".join(p))


def gorsel_3():
    """Fıkıh İlkelerinin Kur'an ve Sünnet Argümanları (Delilleri)."""
    w, h = 680, 250
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_TURUNCU}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Fıkhın Temel İlkelerini Destekleyen Ayet ve Hadis Argümanları</text>',
    ]
    deliller = [
        ("Tekliflerde Kolaylık Argümanı", "Bakara 185: 'Allah sizin için kolaylık", "diler, zorluk dilemez.'  |  Bakara 286:", "'Allah kimseye gücünün üstünde yük yüklemez.'", C_MAVI, C_ACIK_MAVI, 18, 56),
        ("Helallerde Genişlik Argümanı", "Bakara 29: 'Yeryüzünde ne varsa hepsini", "sizin için yaratan O'dur.' (Eşyada aslolan", "ibâhadır / mübahlıktır kaidesi).", C_YESIL, C_ACIK_YESIL, 348, 56),
        ("Adalet ve Hakkaniyet Argümanı", "Nisâ 58: 'İnsanlar arasında hükmettiğiniz", "zaman adaletle hükmedin.'  |  Mâide 8:", "'Bir topluluğa olan kininiz sizi adaletten saptırmasın.'", C_TURUNCU, C_ACIK_SARI, 18, 152),
        ("Zararın Giderilmesi Argümanı", "Hadis-i Şerif: 'Zarar vermek de yoktur,", "zarara zararla karşılık vermek de yoktur.'", "(Mecelle m. 19: الضرر والضرار لا يكون).", C_MOR, C_ACIK_MOR, 348, 152),
    ]
    for baslik, s1, s2, s3, renk, bg, x, y in deliller:
        p.append(f'<rect x="{x}" y="{y}" width="314" height="86" rx="10" fill="{bg}" stroke="{renk}" stroke-width="1.6"/>')
        p.append(f'<rect x="{x}" y="{y}" width="314" height="25" rx="10" fill="{renk}"/>')
        p.append(f'<text x="{x+157}" y="{y+17}" text-anchor="middle" font-size="11.2" font-weight="700" fill="#fff">{baslik}</text>')
        p.append(f'<text x="{x+157}" y="{y+42}" text-anchor="middle" font-size="9.8" font-weight="600" fill="{C_KOYU}">{s1}</text>')
        p.append(f'<text x="{x+157}" y="{y+58}" text-anchor="middle" font-size="9.8" fill="{C_GRI}">{s2}</text>')
        p.append(f'<text x="{x+157}" y="{y+74}" text-anchor="middle" font-size="9.8" fill="{C_GRI}">{s3}</text>')
    return _svg(w, h, "".join(p))


def gorsel_4():
    """Kamu Yararı (Maslahat) ve Örfün Fıkıhtaki Yeri."""
    w, h = 680, 245
    p = [
        f'<rect width="{w}" height="{h}" rx="12" fill="#fbfcfc" stroke="{C_SINIR}" stroke-width="1.5"/>',
        f'<rect x="14" y="12" width="652" height="34" rx="8" fill="{C_MOR}"/>',
        f'<text x="340" y="34" text-anchor="middle" font-size="13.5" font-weight="700" fill="#fff">'
        f'Kamu Yararı (Maslahat), Zararların Önlenmesi ve Sahih Örf</text>',
    ]
    ilkeler = [
        ("Kamu Yararı Önceliği", "Mecelle m. 26: 'Zarar-ı âmmı", "def' için zarar-ı hâs ihtiyar", "olunur.' (Toplum yararı üstündür).", C_MAVI, C_ACIK_MAVI, 18),
        ("Kötülüğü Önleme Önceliği", "Mecelle m. 30: 'Def'-i mefâsid", "celb-i menâfi'den evlâdır.'", "(Zararı önlemek faydadan öncedir).", C_YESIL, C_ACIK_YESIL, 236),
        ("Sahih Örfün İtibarı", "Mecelle m. 36: 'Âdet muhakkemdir.'", "İslam'a aykırı olmayan örf ve", "teamül hukuki delil kabul edilir.", C_TURUNCU, C_ACIK_SARI, 454),
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
    v["bolumler"][2]["gorsel"] = GORSELLER["b3"]
    v["bolumler"][4]["gorsel"] = GORSELLER["b4"]
