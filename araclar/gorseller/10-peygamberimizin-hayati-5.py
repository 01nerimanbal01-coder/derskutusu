# -*- coding: utf-8 -*-
"""10. Sınıf Peygamberimizin Hayatı — 5. Hafta Görselleri
Konu: 1. Ünite: Taif — İslam Davetine Taiflilerin Tepkisi ve Taif'in İslamlaşma Süreci
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#0f766e", arka="#f0fdfa"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Hüzün Yılından Taif Yolculuğuna: Nedenler ve İlk Muhataplar (Sakîf Kabilesi)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Nübüvvetin 10. Yılı (620): Taif Yolculuğunun Nedenleri ve Sakîf Kabilesi", "#0f766e", "#f0fdfa")

    adimlar = [
        ("1. Hüzün Yılı (Senetü'l-Hüzn)", "Hz. Hatice ve Ebu Talib'in", "vefatıyla Mekke'de himaye", "zayıfladı; baskı arttı.", "#dc2626", "#fef2f2"),
        ("2. Yeni Tebliğ Merkezi Arayışı", "Hz. Peygamber, evlatlığı", "Zeyd b. Harise ile Mekke'nin", "güneydoğusundaki Taif'e gitti.", "#0284c7", "#f0f9ff"),
        ("3. Sakîf İleri Gelenleriyle Görüşme", "Abdülyâlîl, Mes'ûd ve Habîb", "adlı üç kardeşi İslam'a", "ve himayeye davet etti.", "#d97706", "#fffbeb"),
        ("4. Taiflilerin Sert Tepkisi", "Lât putuna ve Mekke ile", "ticari çıkarlarına güvenerek", "daveti alayla reddettiler.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(adimlar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="175" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="10.2" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="116" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="136" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="156" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

    s += '<rect x="26" y="246" width="708" height="40" rx="8" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.2"/>'
    s += '<text x="380" y="270" text-anchor="middle" fill="#0f766e" font-size="11" font-weight="700">Zeyd b. Harise\'nin Fedakârlığı: Taif sokaklarında atılan taşlara karşı kendi bedenini Peygamberimize siper etmiştir.</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Üzüm Bağı, Addas'ın Müslüman Olması ve Hz. Peygamber'in Rahmet Tavrı."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Üzüm Bağında İlahi Teselli: Taif Duası, Addas ve Rahmet Peygamberi", "#15803d", "#f0fdf4")

    sahneler = [
        ("1. Taif Duası (Yakarış)", "Utbe ve Şeybe'nin bağına", "sığınan Hz. Peygamber:", "&quot;Allah'ım! Güçsüzlüğümü", "yalnız Sana arz ederim; Sen", "benden razı ol yeter!&quot;", "#15803d", "#dcfce7"),
        ("2. Ninovalı Köle Addas", "Üzüm ikram eden Hristiyan", "köle Addas, 'Bismillah' sözü", "ve Hz. Yunus'un kardeşi", "olduğunu duyunca iman etti.", "(İlk Taif meyvesi!)", "#0284c7", "#e0f2fe"),
        ("3. Dağlar Meleği ve Merhamet", "Cebrail ve Dağlar Meleğinin", "helak teklifine Rahmet", "Peygamberinin cevabı:", "&quot;Hayır! Belki soylarından", "Allah'a ibadet edenler çıkar.&quot;", "#b45309", "#fef3c7"),
    ]
    for i, (bas, a1, a2, a3, a4, a5, r, bg) in enumerate(sahneler):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="58" width="224" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="77" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="112" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+112}" y="132" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+112}" y="156" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'
        s += f'<text x="{x+112}" y="176" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a4}</text>'
        s += f'<text x="{x+112}" y="196" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a5}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Taif Dönüşü Eman (Mut'im b. Adî) ve Taif'in İslamlaşma Süreci (620 -> 630)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Taşlayan Şehirden İman Eden Şehre: Taif'in İslamlaşma Süreci (620 - 630)", "#1d4ed8", "#eff6ff")

    surec = [
        ("620 — Dönüş ve Eman", "Nahle vadisinde cinlerin", "Kur'an dinlemesi; Mut'im b. Adî'nin", "emanıyla Mekke'ye güvenli giriş.", "#0284c7"),
        ("630 (8. Yıl) — Huneyn &amp; Kuşatma", "Mekke'nin fethi sonrası Huneyn", "zaferi ve Taif Kuşatması; kuşatma", "kaldırılırken 'İslam'la şereflenmeleri' duası.", "#d97706"),
        ("Urve b. Mes'ûd es-Sekafî", "Hudeybiye'de elçi olan Urve", "Müslüman oldu; Taif'te ezan", "okurken şehit düştü.", "#dc2626"),
        ("630 (9. Yıl) — Sakîf Heyeti", "Taif temsilcileri Medine'ye", "gelerek kendi istekleriyle", "Müslüman oldu; Lât putu yıkıldı!", "#16a34a"),
    ]
    for i, (bas, a1, a2, r, *_) in enumerate(surec):
        y = 56 + i * 60
        s += f'<rect x="36" y="{y}" width="688" height="50" rx="8" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="36" y="{y}" width="215" height="50" rx="8" fill="{r}"/>'
        s += f'<text x="143" y="{y+30}" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="268" y="{y+21}" fill="#1e293b" font-size="10.5">{a1}</text>'
        s += f'<text x="268" y="{y+39}" fill="{r}" font-size="10.5" font-weight="700">{a2}</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Taif'in İslamlaşmasından Çıkarılan Nebevi İlkeler (Osman b. Ebi'l-As ve İlim Merkezi Taif)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Taif Sürecinden Günümüze Nebevi Tebliğ İlkeleri ve İslamlaşan Taif", "#7c3aed", "#f5f3ff")

    ilkeler = [
        ("Beddua Değil, Hidayet Duası", "En ağır zulüm anında bile", "intikam yerine gelecek nesillerin", "iman etmesini istemek.", "#7c3aed", "#f5f3ff"),
        ("Tavizsiz Tevhid İlkesi", "Sakîf heyetinin 'Lât putu kalsın,", "namazdan muaf olalım' şartlarını", "hikmetle reddedip tevhidi korumak.", "#dc2626", "#fef2f2"),
        ("Genç Vali: Osman b. Ebi'l-As", "Kur'an ve fıkıh bilgisiyle öne", "çıkan genç sahabi Osman b.", "Ebi'l-As'ı Taif'e vali atamak.", "#0284c7", "#f0f9ff"),
        ("Vefalı Şehir Taif", "Hz. Peygamber'in vefatından", "sonraki dinden dönme (ridde)", "olaylarında İslam'dan ayrılmadı!", "#16a34a", "#f0fdf4"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(ilkeler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="10.2" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="125" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="145" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="165" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

    return _svg(w, h, s)


GORSELLER = {
    "b1": gorsel_1(),
    "b2": gorsel_2(),
    "b3": gorsel_3(),
    "b4": gorsel_4(),
}


def uygula(v):
    eş = [(0, "b1"), (1, "b2"), (2, "b3"), (4, "b4")]
    bolumler = v.get("bolumler", [])
    for idx, anahtar in eş:
        if idx < len(bolumler):
            bolumler[idx]["gorsel"] = GORSELLER[anahtar]
