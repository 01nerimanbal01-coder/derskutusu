# -*- coding: utf-8 -*-
"""10. Sınıf Hadis — 5. Hafta Görselleri
Konu: 1. Hadis İlmine Giriş — Sünnetin Dindeki Yeri ve Bağlayıcılığı
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#047857", arka="#ecfdf5"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """Kur'an-ı Kerim ve Sünnet Bütünlüğü (İtaat, Üsve-i Hasene, Hikmet)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "İslam'ın İki Temel Kaynağı: Kur'an-ı Kerim ve Sünnet Bütünlüğü", "#047857", "#ecfdf5")

    kutular = [
        ("1. Vahiy ve Hikmet Bütünlüğü", "Kur'an vahy-i metlüv (okunan),", "sünnet ise vahy-i gayr-i metlüv", "(hikmet) olarak birbirini tamamlar.", "#059669", "#d1fae5"),
        ("2. Peygambere İtaat Emri", "&quot;Kim Resûl'e itaat ederse", "Allah'a itaat etmiş olur.&quot;", "(Nisâ, 4/80; Haşr, 59/7)", "#0284c7", "#e0f2fe"),
        ("3. Üsve-i Hasene (En Güzel Örnek)", "Kur'an'ın ahlak ve ibadet", "ilkelerinin hayata geçirilmiş", "canlı modeli Hz. Peygamber'dir.", "#7c3aed", "#f5f3ff"),
        ("4. Beyan (Açıklama) Görevi", "İnsanlara indirilen Kur'an'ı", "açıklaması için Hz. Peygamber", "görevlendirilmiştir (Nahl, 44).", "#d97706", "#fffbeb"),
    ]
    for i, (bas, a1, a2, a3, r, bg) in enumerate(kutular):
        x = 28 + (i % 2) * 358
        y = 58 + (i // 2) * 116
        s += f'<rect x="{x}" y="{y}" width="344" height="102" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="{y}" width="344" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+172}" y="{y+18}" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+172}" y="{y+48}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+172}" y="{y+66}" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+172}" y="{y+84}" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a3}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Sünnetin Kur'an-ı Kerim'i Açıklama (Beyan) İşlevleri (Tefsil, Tahsis, Takyid, Teşri)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Sünnetin Kur'an-ı Kerim Karşısındaki 4 Temel Beyan (Açıklama) İşlevi", "#1d4ed8", "#eff6ff")

    islevler = [
        ("1. Mücmeli Tefsil Etme", "(Kapalıyı Açıklama)", "Kur'an'da özetle emredilen", "namazın rekâtlarını, zekât", "nisabını ve haccın yapılışını", "uygulamalı olarak açıklar.", "#1d4ed8", "#dbeafe"),
        ("2. Umumî Hükmü Tahsis", "(Geneli Sınırlandırma)", "Kur'an'daki genel bir", "hükmün hangi özel durumları", "kapsamadığını (istisnalarını)", "belirler (Miras vb.).", "#0d9488", "#ccfbf1"),
        ("3. Mutlakı Takyid Etme", "(Kayıtsızı Kayıtlama)", "Kur'an'da şartı belirtilmeyen", "bir hükmün (ör. vasiyetin", "malın 1/3'ü ile sınırlanması)", "ölçüsünü koyar.", "#7c3aed", "#f5f3ff"),
        ("4. Müstakil Hüküm Koyma", "(Teşri Yetkisi)", "Kur'an'da açıkça geçmeyen", "konularda (ehli eşek eti,", "yırtıcı kuşlar, sütakrabalığı)", "yeni hüküm koyar.", "#d97706", "#fffbeb"),
    ]
    for i, (bas, alt, a1, a2, a3, a4, r, bg) in enumerate(islevler):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="55" width="168" height="235" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="74" text-anchor="middle" fill="#fff" font-size="10.2" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="99" text-anchor="middle" fill="{r}" font-size="9.5" font-weight="700">{alt}</text>'
        s += f'<text x="{x+84}" y="132" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="150" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="168" text-anchor="middle" fill="#1e293b" font-size="10">{a3}</text>'
        s += f'<text x="{x+84}" y="186" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a4}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Sünnetin Bağlayıcılık Bakımından Ayrımı (Teşrii Sünnet vs Gayr-i Teşrii / Cibilli Sünnet)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Bağlayıcılık Bakımından Sünnet: Teşriî (Dini) ve Gayr-i Teşriî (Beşerî) Sünnet", "#b45309", "#fffbeb")

    # Sol: Teşrii Sünnet
    s += '<rect x="30" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#16a34a" stroke-width="1.6"/>'
    s += '<rect x="30" y="55" width="335" height="30" rx="10" fill="#16a34a"/>'
    s += '<text x="197" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">1. TEŞRİÎ (Dini / Bağlayıcı) SÜNNET</text>'
    s += '<text x="197" y="102" text-anchor="middle" fill="#166534" font-size="10.5" font-weight="700">Hz. Peygamber\'in &quot;Tebliğci, Hâkim ve Devlet Başkanı&quot;</text>'
    s += '<text x="197" y="118" text-anchor="middle" fill="#166534" font-size="10.5" font-weight="700">sıfatıyla ortaya koyduğu sünnetlerdir.</text>'
    s += '<rect x="46" y="132" width="303" height="136" rx="8" fill="#f0fdf4" stroke="#86efac"/>'
    s += '<text x="60" y="156" fill="#1e293b" font-size="10.2">• İnanç, ibadet, helal-haram ve ahlak hükümleri</text>'
    s += '<text x="60" y="178" fill="#1e293b" font-size="10.2">• Namaz, oruç, zekât ve hac uygulamaları</text>'
    s += '<text x="60" y="200" fill="#1e293b" font-size="10.2">• Aile, miras ve ticaret hukuku ilkeleri</text>'
    s += '<text x="197" y="242" text-anchor="middle" fill="#15803d" font-size="11" font-weight="700">HÜKMÜ: Tüm Müslümanlar için BAĞLAYICIDIR!</text>'

    # Sağ: Gayr-i Teşrii Sünnet
    s += '<rect x="395" y="55" width="335" height="230" rx="10" fill="#fff" stroke="#d97706" stroke-width="1.6"/>'
    s += '<rect x="395" y="55" width="335" height="30" rx="10" fill="#d97706"/>'
    s += '<text x="562" y="75" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">2. GAYR-İ TEŞRİÎ (Cibillî / Tecrübî) SÜNNET</text>'
    s += '<text x="562" y="102" text-anchor="middle" fill="#92400e" font-size="10.5" font-weight="700">Hz. Peygamber\'in bir &quot;İnsan (Beşer)&quot; olarak</text>'
    s += '<text x="562" y="118" text-anchor="middle" fill="#92400e" font-size="10.5" font-weight="700">yaptığı doğal ve yerel davranışlardır.</text>'
    s += '<rect x="411" y="132" width="303" height="136" rx="8" fill="#fffbeb" stroke="#fde68a"/>'
    s += '<text x="425" y="156" fill="#1e293b" font-size="10.2">• Yeme-içme, uyuma, yürüme (Cibillî sünnet)</text>'
    s += '<text x="425" y="178" fill="#1e293b" font-size="10.2">• İklime göre giyinme biçimi (Zevâid sünnet)</text>'
    s += '<text x="425" y="200" fill="#1e293b" font-size="10.2">• Hurma aşılama, savaşta mevzi seçimi (Tecrübî)</text>'
    s += '<text x="562" y="242" text-anchor="middle" fill="#b45309" font-size="11" font-weight="700">HÜKMÜ: Dini bir zorunluluk (farz/vacip) DEĞİLDİR.</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Sünnetsiz İslam İddialarına (Erîke Hadisi) Cevap ve Sünnetin Koruyucu Rolü."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Sünnetin Dini Koruyucu Rolü ve 'Erîke (Koltuk) Hadisi' Uyarısı", "#7c3aed", "#f5f3ff")

    s += '<rect x="36" y="56" width="688" height="96" rx="10" fill="#fff" stroke="#8b5cf6" stroke-width="1.6"/>'
    s += '<text x="380" y="80" text-anchor="middle" fill="#5b21b6" font-size="12" font-weight="700">Hz. Peygamber\'in (s.a.v.) Mucizevi Uyarısı (Erîke Hadisi):</text>'
    s += '<text x="380" y="104" text-anchor="middle" fill="#1e293b" font-size="10.5">&quot;Sakın sizden birinizi; emrettiğim veya yasakladığım bir husus kendisine iletildiğinde, koltuğuna</text>'
    s += '<text x="380" y="122" text-anchor="middle" fill="#1e293b" font-size="10.5">yaslanmış vaziyette: \'Biz bunu bilmeyiz, Allah\'ın Kitabında ne bulursak yalnız ona uyarız!\' derken bulmayayım!</text>'
    s += '<text x="380" y="140" text-anchor="middle" fill="#6d28d9" font-size="10.5" font-weight="700">Biliniz ki bana Kur\'an ve onunla birlikte bir o kadarı (Sünnet/Hikmet) daha verildi.&quot; (Ebû Dâvûd, Sünnet, 5)</text>'

    sonuclar = [
        ("İbadetler Uygulanamaz", "Sünnet olmadan 5 vakit namazın", "vakti, rekâtları ve kılınışı", "bilinemez.", "#dc2626"),
        ("Kur'an Keyfî Yorumlanır", "Ayetlerin iniş sebebi ve", "Peygamber uygulaması olmadan", "bütünlük bozulur.", "#d97706"),
        ("Ümmet Birliği Dağılır", "Sünnet, 14 asırdır Müslümanları", "ortak ibadet ve ahlakta", "birleştiren çimentodur.", "#16a34a"),
    ]
    for i, (bas, a1, a2, a3, r) in enumerate(sonuclar):
        x = 36 + i * 236
        s += f'<rect x="{x}" y="166" width="216" height="120" rx="10" fill="#fff" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="166" width="216" height="26" rx="10" fill="{r}"/>'
        s += f'<text x="{x+108}" y="184" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">{bas}</text>'
        s += f'<text x="{x+108}" y="214" text-anchor="middle" fill="#334155" font-size="10">{a1}</text>'
        s += f'<text x="{x+108}" y="232" text-anchor="middle" fill="#334155" font-size="10">{a2}</text>'
        s += f'<text x="{x+108}" y="250" text-anchor="middle" fill="{r}" font-size="10" font-weight="700">{a3}</text>'

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
