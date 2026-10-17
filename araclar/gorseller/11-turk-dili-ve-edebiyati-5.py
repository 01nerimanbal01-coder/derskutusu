# -*- coding: utf-8 -*-
"""11. Sınıf Türk Dili ve Edebiyatı — 5. Hafta Görselleri
Konu: 1. Tema: Bir Diyeceğim Var! — Yazma Süreci (Bilgilendirici/Tartışmacı Metin) ve Dil Bilgisi (Cümlenin Ögeleri)
"""


def _svg(w, h, icerik):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="100%" style="max-width:{w}px;height:auto;display:block;'
        f'margin:14px auto;font-family:\'Segoe UI\',system-ui,sans-serif;">'
        f"{icerik}</svg>"
    )


def _kart(x, y, w, h, baslik, renk="#be123c", arka="#fff1f2"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="12" fill="{renk}"/>'
        f'<rect x="{x}" y="{y+18}" width="{w}" height="14" fill="{renk}"/>'
        f'<text x="{x+w/2}" y="{y+21}" text-anchor="middle" fill="#fff" '
        f'font-size="13" font-weight="700">{baslik}</text>'
    )


def gorsel_1():
    """'Bir Diyeceğim Var!' Temasında Yazma Süreci Aşamaları."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "'Bir Diyeceğim Var!' Temasında Tartışmacı ve Bilgilendirici Metin Yazma Süreci", "#be123c", "#fff1f2")

    adimlar = [
        ("1. Hazırlık &amp; Konu", "Toplumsal veya kültürel", "bir sorun belirlenir;", "hedef kitle ve tez", "(ana düşünce) seçilir.", "#be123c", "#ffe4e6"),
        ("2. Planlama &amp; Taslak", "Giriş (sorun), Gelişme", "(kanıt ve argümanlar)", "ve Sonuç (çözüm çağrısı)", "bölümleri kurgulanır.", "#0284c7", "#e0f2fe"),
        ("3. Düşünceyi Geliştirme", "Tanık gösterme, sayısal", "veriler, örnekleme ve", "karşılaştırma yolları", "etkin biçimde kullanılır.", "#16a34a", "#dcfce7"),
        ("4. Gözden Geçirme", "Yazım, noktalama ve", "cümlenin ögeleri kontrol", "edilerek metin okurla", "paylaşılır.", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, a1, a2, a3, a4, r, bg) in enumerate(adimlar):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="122" text-anchor="middle" fill="#1e293b" font-size="10.2">{a1}</text>'
        s += f'<text x="{x+84}" y="142" text-anchor="middle" fill="#1e293b" font-size="10.2">{a2}</text>'
        s += f'<text x="{x+84}" y="162" text-anchor="middle" fill="#1e293b" font-size="10.2">{a3}</text>'
        s += f'<text x="{x+84}" y="182" text-anchor="middle" fill="{r}" font-size="10.2" font-weight="700">{a4}</text>'

    return _svg(w, h, s)


def gorsel_2():
    """Makale, Fıkra (Köşe Yazısı) ve Deneme Türlerinin Karşılaştırılması."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Öğretici/Tartışmacı Metin Türleri: Makale, Fıkra (Köşe Yazısı) ve Deneme", "#1d4ed8", "#eff6ff")

    turler = [
        ("MAKALE", "Bilimsel ve Nesnel Yazı", "• Tezi kanıtlama zorunluluğu VAR", "• Ciddi, resmi ve nesnel üslup", "• Dipnot, kaynakça ve istatistik", "• Açıklayıcı ve tartışmacı anlatım", "#1d4ed8", "#dbeafe"),
        ("FIKRA (Köşe Yazısı)", "Güncel Gazete/Dergi Yazısı", "• Kanıtlama zorunluluğu YOK", "• Güncel toplumsal-siyasi konular", "• Samimi, kıvrak ve güncel dil", "• Gazete ve dergi sütunlarında", "#0d9488", "#ccfbf1"),
        ("DENEME", "Yazarın Kendisiyle Konuşması", "• Kanıtlama zorunluluğu YOK", "• Özgürce seçilen her konu ('Ben')", "• İçten, öznel ve sanatsal üslup", "• Söyleşi/Sohbetten farkı: İçedönük", "#7c3aed", "#f5f3ff"),
    ]
    for i, (bas, alt, m1, m2, m3, m4, r, bg) in enumerate(turler):
        x = 28 + i * 240
        s += f'<rect x="{x}" y="55" width="224" height="230" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.6"/>'
        s += f'<rect x="{x}" y="55" width="224" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+112}" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">{bas}</text>'
        s += f'<text x="{x+112}" y="100" text-anchor="middle" fill="{r}" font-size="10.5" font-weight="700">{alt}</text>'
        s += f'<text x="{x+20}" y="132" fill="#1e293b" font-size="10">{m1}</text>'
        s += f'<text x="{x+20}" y="156" fill="#1e293b" font-size="10">{m2}</text>'
        s += f'<text x="{x+20}" y="180" fill="#1e293b" font-size="10">{m3}</text>'
        s += f'<text x="{x+20}" y="204" fill="{r}" font-size="10" font-weight="700">{m4}</text>'

    return _svg(w, h, s)


def gorsel_3():
    """Dil Bilgisi: Cümlenin Temel ve Yardımcı Ögeleri Şeması (YÖN Kuralı)."""
    w, h = 760, 320
    s = _kart(10, 10, w - 20, h - 20, "Cümlenin Ögeleri: Temel Ögeler, Yardımcı Ögeler ve YÖN Bulma Sırası", "#047857", "#ecfdf5")

    # Sol: Temel Ögeler
    s += '<rect x="28" y="55" width="280" height="190" rx="10" fill="#fff" stroke="#10b981" stroke-width="1.6"/>'
    s += '<rect x="28" y="55" width="280" height="28" rx="10" fill="#059669"/>'
    s += '<text x="168" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">1. TEMEL ÖGELER (Önce Yüklem, Sonra Özne!)</text>'
    s += '<text x="44" y="104" fill="#065f46" font-size="11" font-weight="700">• YÜKLEM (Cümlenin Kalbi):</text>'
    s += '<text x="44" y="122" fill="#334155" font-size="10">Yargıyı bildirir; çekimli fiil veya ek-fiil</text>'
    s += '<text x="44" y="138" fill="#334155" font-size="10">almış isim/söz öbeğidir.</text>'
    s += '<text x="44" y="168" fill="#065f46" font-size="11" font-weight="700">• ÖZNE (İşi Yapan / Olan):</text>'
    s += '<text x="44" y="186" fill="#334155" font-size="10">Yükleme sorulan &quot;Kim?&quot; ve &quot;Ne?&quot;</text>'
    s += '<text x="44" y="202" fill="#334155" font-size="10">sorularına yanıt verir (Gerçek, Gizli, Sözde).</text>'

    # Sağ: Yardımcı Ögeler
    s += '<rect x="326" y="55" width="406" height="190" rx="10" fill="#fff" stroke="#10b981" stroke-width="1.6"/>'
    s += '<rect x="326" y="55" width="406" height="28" rx="10" fill="#0d9488"/>'
    s += '<text x="529" y="74" text-anchor="middle" fill="#fff" font-size="11.5" font-weight="700">2. YARDIMCI ÖGELER (Nesne ve Tümleçler)</text>'

    yardimci = [
        ("Belirtili Nesne:", "Neyi, Kimi, Nereyi? (-ı/-i/-u/-ü belirtme eki alır)"),
        ("Belirtisiz Nesne:", "Özneyi bulduktan sonra sorulan 'Ne?' sorusu"),
        ("Dolaylı Tümleç (Yer Tamlayıcısı):", "Kime, Kimde, Kimden / Nereye, Nerede, Nereden? (-e, -de, -den)"),
        ("Zarf Tümleci:", "Ne zaman, Nasıl, Niçin, Ne kadar, Ne ile, Kim ile?"),
    ]
    for i, (b, ac) in enumerate(yardimci):
        y = 95 + i * 36
        s += f'<text x="340" y="{y+12}" fill="#0f766e" font-size="10.2" font-weight="700">{b}</text>'
        s += f'<text x="340" y="{y+26}" fill="#334155" font-size="9.5">{ac}</text>'

    s += '<rect x="28" y="255" width="704" height="38" rx="8" fill="#fef3c7" stroke="#d97706"/>'
    s += '<text x="380" y="279" text-anchor="middle" fill="#92400e" font-size="11" font-weight="700">Altın Kural (YÖN Sırası): Önce 1. Yüklem, 2. Özne, 3. Nesne/Tümleçler bulunur; tamlamalar ve deyimler BÖLÜNMEZ!</text>'

    return _svg(w, h, s)


def gorsel_4():
    """Cümlede Vurgu ve Cümle Dışı Unsurlar (Ara Söz, Bağlaç, Ünlem)."""
    w, h = 760, 310
    s = _kart(10, 10, w - 20, h - 20, "Cümlede Vurgu Kuralları ve Ara Söz / Cümle Dışı Unsurlar", "#d97706", "#fffbeb")

    kutular = [
        ("Fiil Cümlesinde Vurgu", "Yüklemden HEMEN ÖNCEKİ", "öge vurgulanır:", "&quot;Kitabı dün KÜTÜPHANEDEN aldım.&quot;", "(Vurgu: Dolaylı Tümleçte)", "#d97706", "#fef3c7"),
        ("İsim Cümlesinde Vurgu", "Yüklemin KENDİSİNDEDİR:", "&quot;En güçlü iletişim aracı", "SAMİMİYETTİR.&quot;", "(Vurgu: Yüklemde)", "#0284c7", "#e0f2fe"),
        ("Mi / de / Soru Vurgusu", "'mi' soru eki ve 'de' bağlacı", "kendinden önceki ögeye", "vurguyu çeker.", "(Soru kelimesi vurgulanır)", "#7c3aed", "#f5f3ff"),
        ("Ara Söz ve Cümle Dışı Unsur", "İki virgül/kısa çizgi arasındaki", "ara sözler bir ögenin açıklayıcısı", "veya cümle dışı unsurdur.", "(Bağlaç ve ünlemler öge olmaz!)", "#16a34a", "#dcfce7"),
    ]
    for i, (bas, a1, a2, a3, a4, r, bg) in enumerate(kutular):
        x = 26 + i * 180
        s += f'<rect x="{x}" y="58" width="168" height="225" rx="10" fill="{bg}" stroke="{r}" stroke-width="1.5"/>'
        s += f'<rect x="{x}" y="58" width="168" height="28" rx="10" fill="{r}"/>'
        s += f'<text x="{x+84}" y="77" text-anchor="middle" fill="#fff" font-size="10.2" font-weight="700">{bas}</text>'
        s += f'<text x="{x+84}" y="118" text-anchor="middle" fill="#1e293b" font-size="10">{a1}</text>'
        s += f'<text x="{x+84}" y="138" text-anchor="middle" fill="#1e293b" font-size="10">{a2}</text>'
        s += f'<text x="{x+84}" y="162" text-anchor="middle" fill="{r}" font-size="9.8" font-weight="700">{a3}</text>'
        s += f'<text x="{x+84}" y="195" text-anchor="middle" fill="#475569" font-size="9.5">{a4}</text>'

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
