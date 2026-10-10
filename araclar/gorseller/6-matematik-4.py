"""6. sınıf Matematik, 4. hafta: deneysel olasılık (deney, çıktı, olay, sıklık, göreli sıklık, deneysel olasılık).

Görseller yalnız MEB 6. sınıf Matematik ders kitabındaki bilgilerle çizilir (kitap s. 60-83).
Renk anlamı: deney = mavi, çıktı = turuncu, olay (ve olayı oluşturan çıktılar) = yeşil; spektrumda kırmızı boncuk = turuncu,
mavi boncuk = mavi; sütun grafiğinde her sütun çarktaki rengin adını taşır (mavi, turuncu, mor, yeşil); karşılaştırmada Ece = mavi, Mert = turuncu.
Her grafik tek ölçekle çizilir (eksen değerleri yazılıdır); sayı değerleri metindeki örneklerle aynıdır.
"""
from ozet_gorsel import svg, ok_isareti, kesir_svg


def deney_cikti_olay():
    """Deney → çıktılar → olay: madenî para atma ve sayı küpü atma (asal sayı gelmesi olayı)."""
    ic = '<defs>' + ok_isareti('okE4', 'g-s') + '</defs>'
    ic += '<text x="64" y="20" text-anchor="middle" font-size="13" font-weight="800" class="g-mf">Deney</text>'
    ic += '<text x="215" y="20" text-anchor="middle" font-size="13" font-weight="800" class="g-tf">Çıktılar</text>'
    ic += '<text x="371" y="20" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">Olay</text>'

    def kutu(x, y, w, h, a, s):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="{a}"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="{s}" stroke-width="2"/>')

    def iki_satir(cx, y, a, b, sinif):
        return (f'<text x="{cx}" y="{y + 20}" text-anchor="middle" font-size="12.5" font-weight="700" class="{sinif}">{a}</text>'
                f'<text x="{cx}" y="{y + 38}" text-anchor="middle" font-size="12.5" font-weight="700" class="{sinif}">{b}</text>')

    def ok(y):
        return (f'<line x1="122" y1="{y}" x2="138" y2="{y}" class="g-c" stroke-width="2" marker-end="url(#okE4)"/>'
                f'<line x1="292" y1="{y}" x2="308" y2="{y}" class="g-c" stroke-width="2" marker-end="url(#okE4)"/>')

    # satır 1: madenî para
    y = 30
    ic += kutu(8, y, 112, 58, 'g-ma', 'g-ms') + iki_satir(64, y, 'Madenî para', 'atma', 'g-mf')
    ic += kutu(140, y, 150, 58, 'g-ta', 'g-ts')
    ic += f'<rect x="150" y="{y + 16}" width="60" height="26" rx="13" class="g-z"/><rect x="150" y="{y + 16}" width="60" height="26" rx="13" class="g-ts" stroke-width="1.8"/>'
    ic += f'<text x="180" y="{y + 34}" text-anchor="middle" font-size="13" font-weight="700" class="g-tf">yazı</text>'
    ic += f'<rect x="220" y="{y + 16}" width="60" height="26" rx="13" class="g-yf"/>'
    ic += f'<text x="250" y="{y + 34}" text-anchor="middle" font-size="13" font-weight="700" class="g-b">tura</text>'
    ic += kutu(310, y, 122, 58, 'g-ya', 'g-ys') + iki_satir(371, y, 'Tura', 'gelmesi', 'g-yf') + ok(y + 29)
    # satır 2: sayı küpü
    y = 108
    ic += kutu(8, y, 112, 58, 'g-ma', 'g-ms') + iki_satir(64, y, 'Sayı küpü', 'atma', 'g-mf')
    ic += kutu(140, y, 150, 58, 'g-ta', 'g-ts')
    for k in range(6):
        cx = 154 + 23 * k
        n = k + 1
        if n in (2, 3, 5):
            ic += f'<circle cx="{cx}" cy="{y + 29}" r="10" class="g-yf"/>'
            ic += f'<text x="{cx}" y="{y + 33.5}" text-anchor="middle" font-size="12" font-weight="800" class="g-b">{n}</text>'
        else:
            ic += f'<circle cx="{cx}" cy="{y + 29}" r="10" class="g-z"/><circle cx="{cx}" cy="{y + 29}" r="10" class="g-ts" stroke-width="1.6"/>'
            ic += f'<text x="{cx}" y="{y + 33.5}" text-anchor="middle" font-size="12" font-weight="800" class="g-tf">{n}</text>'
    ic += kutu(310, y, 122, 58, 'g-ya', 'g-ys') + iki_satir(371, y, 'Asal sayı', 'gelmesi', 'g-yf') + ok(y + 29)
    ic += '<text x="8" y="188" font-size="12" class="g-s">Yeşil çıktılar, olayı oluşturan çıktılardır.</text>'
    return svg(440, 196, ic, 'Deney, çıktı ve olay. Parayı atınca üst yüze yazı ya da tura gelir; bu iki sonuç çıktıdır, tura gelmesi ise bir olaydır. '
               'Sayı küpü atma deneyinin çıktıları 1, 2, 3, 4, 5 ve 6’dır; asal sayı gelmesi olayı 2, 3 ve 5 çıktılarından oluşur.')


def spektrum():
    """Olasılık spektrumu: 0 imkânsız, 1/2, 1 kesin; kavanozdaki boncuklara göre tahmin konumları."""
    ic = '<text x="12" y="20" font-size="12.5" class="g-y">Kavanozda 3 kırmızı ve 5 mavi boncuk var.</text>'
    for k in range(8):
        sinif = 'g-tf' if k < 3 else 'g-mf'
        ic += f'<circle cx="{22 + 22 * k}" cy="42" r="8" class="{sinif}"/>'
    ic += '<rect x="30" y="104" width="380" height="16" rx="8" class="g-ma"/><rect x="30" y="104" width="380" height="16" rx="8" class="g-ms" stroke-width="2"/>'
    for x in (30, 220, 410):
        ic += f'<line x1="{x}" y1="98" x2="{x}" y2="126" class="g-ms" stroke-width="2"/>'
    for x, t in ((30, '0'), (220, '½'), (410, '1')):
        ic += f'<text x="{x}" y="146" text-anchor="middle" font-size="15" font-weight="800" class="g-y">{t}</text>'
    ic += '<text x="30" y="164" text-anchor="middle" font-size="12" class="g-s">imkânsız</text>'
    ic += '<text x="410" y="164" text-anchor="middle" font-size="12" class="g-s">kesin</text>'
    ic += '<circle cx="163" cy="112" r="10" class="g-tf"/><text x="163" y="90" text-anchor="middle" font-size="12.5" font-weight="700" class="g-tf">kırmızı</text>'
    ic += '<circle cx="277" cy="112" r="10" class="g-mf"/><text x="277" y="90" text-anchor="middle" font-size="12.5" font-weight="700" class="g-mf">mavi</text>'
    ic += '<text x="12" y="188" font-size="12" class="g-s">Turuncu daire: kırmızı boncuk çekme tahmini</text>'
    ic += '<text x="12" y="204" font-size="12" class="g-s">Mavi daire: mavi boncuk çekme tahmini</text>'
    return svg(440, 214, ic, 'Olasılık spektrumu: sol uçta 0 (imkânsız), ortada 1/2, sağ uçta 1 (kesin). Kavanozda 3 kırmızı ve 5 mavi boncuk vardır; '
               'mavi boncuk çekme tahmini 1/2’nin sağında, kırmızı boncuk çekme tahmini 1/2’nin solunda işaretlenir.')


def cark_grafigi():
    """Çarkın 24 çevrilişi: sıklık tablosu ve sütun grafiği (mavi 8, turuncu 6, mor 4, yeşil 6)."""
    veri = [('Mavi', 8, 'g-mf'), ('Turuncu', 6, 'g-tf'), ('Mor', 4, 'g-of'), ('Yeşil', 6, 'g-yf')]
    y0, b = 176, 17
    ic = '<text x="12" y="14" font-size="13" font-weight="800" class="g-y">Çark 24 kez çevrildi</text>'
    ic += '<text x="48" y="29" text-anchor="middle" font-size="12" class="g-s">Sıklık</text>'
    for v in (2, 4, 6, 8):
        y = y0 - b * v
        ic += f'<line x1="48" y1="{y}" x2="262" y2="{y}" class="g-c" stroke-width="1"/>'
    for v in (0, 2, 4, 6, 8):
        ic += f'<text x="40" y="{y0 - b * v + 4}" text-anchor="end" font-size="12" class="g-s">{v}</text>'
    ic += f'<line x1="48" y1="38" x2="48" y2="{y0}" class="g-c" stroke-width="2"/><line x1="48" y1="{y0}" x2="262" y2="{y0}" class="g-c" stroke-width="2"/>'
    for k, (ad, v, f) in enumerate(veri):
        x = 62 + 50 * k
        ic += f'<rect x="{x}" y="{y0 - b * v}" width="38" height="{b * v}" rx="3" class="{f}"/>'
        ic += f'<text x="{x + 19}" y="{y0 - b * v - 5}" text-anchor="middle" font-size="13" font-weight="800" class="g-y">{v}</text>'
        ic += f'<text x="{x + 19}" y="194" text-anchor="middle" font-size="12" class="g-y">{ad}</text>'
    # tablo
    ic += '<rect x="284" y="34" width="146" height="26" rx="6" class="g-mf"/>'
    ic += '<text x="296" y="52" font-size="12.5" font-weight="800" class="g-b">Renk</text><text x="418" y="52" text-anchor="end" font-size="12.5" font-weight="800" class="g-b">Sıklık</text>'
    for k, (ad, v, f) in enumerate(veri):
        y = 64 + 28 * k
        ic += f'<rect x="284" y="{y}" width="146" height="26" rx="6" class="g-ma"/>'
        ic += f'<circle cx="298" cy="{y + 13}" r="6" class="{f}"/>'
        ic += f'<text x="310" y="{y + 18}" font-size="13" class="g-y">{ad}</text><text x="418" y="{y + 18}" text-anchor="end" font-size="14" font-weight="800" class="g-y">{v}</text>'
    ic += '<rect x="284" y="176" width="146" height="26" rx="6" class="g-ya"/>'
    ic += '<text x="296" y="194" font-size="13" font-weight="800" class="g-yf">Toplam</text><text x="418" y="194" text-anchor="end" font-size="14" font-weight="800" class="g-yf">24</text>'
    return svg(440, 210, ic, 'Dört renkli çark 24 kez çevrildi. Okun gösterdiği renklerin sıklıkları: mavi 8, turuncu 6, mor 4, yeşil 6; toplam 24. '
               'Sütun grafiğinde sütunların yükseklikleri sıklıkları gösterir.')


def kup_tablosu():
    """Sayı küpünün 20 atışı: sıklık, göreli sıklık ve deneysel olasılık (yüzde)."""
    sik = [3, 4, 2, 5, 3, 3]
    c = (52, 132, 224, 322)
    ic = '<rect x="8" y="8" width="394" height="44" rx="8" class="g-mf"/>'
    ic += f'<text x="{c[0]}" y="26" text-anchor="middle" font-size="12" font-weight="800" class="g-b">Üst yüze</text>'
    ic += f'<text x="{c[0]}" y="42" text-anchor="middle" font-size="12" font-weight="800" class="g-b">gelen sayı</text>'
    ic += f'<text x="{c[1]}" y="35" text-anchor="middle" font-size="12" font-weight="800" class="g-b">Sıklık</text>'
    ic += f'<text x="{c[2]}" y="26" text-anchor="middle" font-size="12" font-weight="800" class="g-b">Göreli</text>'
    ic += f'<text x="{c[2]}" y="42" text-anchor="middle" font-size="12" font-weight="800" class="g-b">sıklık</text>'
    ic += f'<text x="{c[3]}" y="26" text-anchor="middle" font-size="12" font-weight="800" class="g-b">Deneysel</text>'
    ic += f'<text x="{c[3]}" y="42" text-anchor="middle" font-size="12" font-weight="800" class="g-b">olasılık (%)</text>'
    for i, s in enumerate(sik):
        yt = 60 + 34 * i
        yc = yt + 16
        en = s == max(sik)
        ic += f'<rect x="8" y="{yt}" width="394" height="32" rx="6" class="{"g-ta" if en else "g-ma"}"/>'
        f = 'g-tf' if en else 'g-y'
        ic += f'<text x="{c[0]}" y="{yc + 5}" text-anchor="middle" font-size="15" font-weight="800" class="{f}">{i + 1}</text>'
        ic += f'<text x="{c[1]}" y="{yc + 5}" text-anchor="middle" font-size="15" font-weight="{800 if en else 600}" class="{f}">{s}</text>'
        ic += kesir_svg(c[2], yc, str(s), '20', f, 12)
        ic += f'<text x="{c[3]}" y="{yc + 5}" text-anchor="middle" font-size="15" font-weight="{800 if en else 600}" class="{f}">%{s * 5}</text>'
    yt = 60 + 34 * 6
    yc = yt + 16
    ic += f'<rect x="8" y="{yt}" width="394" height="32" rx="6" class="g-ya"/>'
    ic += f'<text x="{c[0]}" y="{yc + 5}" text-anchor="middle" font-size="13" font-weight="800" class="g-yf">Toplam</text>'
    ic += f'<text x="{c[1]}" y="{yc + 5}" text-anchor="middle" font-size="15" font-weight="800" class="g-yf">{sum(sik)}</text>'
    ic += kesir_svg(c[2], yc, '20', '20', 'g-yf', 12)
    ic += f'<text x="{c[3]}" y="{yc + 5}" text-anchor="middle" font-size="15" font-weight="800" class="g-yf">%100</text>'
    return svg(410, yt + 44, ic, 'Bir sayı küpü 20 kez atıldı. Sıklıklar: 1 için 3, 2 için 4, 3 için 2, 4 için 5, 5 için 3, 6 için 3; toplam 20. '
               'Göreli sıklıklar 3/20, 4/20, 2/20, 5/20, 3/20 ve 3/20; deneysel olasılıklar yüzde 15, 20, 10, 25, 15 ve 15. En büyük deneysel olasılık 4 sayısındadır.')


def karsilastirma():
    """Ece (20 atışta 15) ve Mert (30 atışta 21): sıklık ile göreli sıklık karşılaştırması."""
    ic = '<line x1="222" y1="10" x2="222" y2="232" class="g-c" stroke-width="1"/>'

    def panel(x0, baslik, olcek, tikler, degerler, etiketler, alt, yazi):
        s = f'<text x="{x0 + 100}" y="18" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{baslik}</text>'
        for deger, yaz in tikler:
            y = 186 - olcek * deger
            if deger:
                s += f'<line x1="{x0 + 40}" y1="{y:g}" x2="{x0 + 186}" y2="{y:g}" class="g-c" stroke-width="1"/>'
            s += f'<text x="{x0 + 34}" y="{y + 4:g}" text-anchor="end" font-size="12" class="g-s">{yaz}</text>'
        s += f'<line x1="{x0 + 40}" y1="34" x2="{x0 + 40}" y2="186" class="g-c" stroke-width="2"/><line x1="{x0 + 40}" y1="186" x2="{x0 + 186}" y2="186" class="g-c" stroke-width="2"/>'
        for k, (v, f, ad, at) in enumerate(zip(degerler, ('g-mf', 'g-tf'), ('Ece', 'Mert'), ('20 atış', '30 atış'))):
            x = x0 + 56 + 60 * k
            h = olcek * v
            s += f'<rect x="{x}" y="{186 - h:g}" width="44" height="{h:g}" rx="3" class="{f}"/>'
            s += f'<text x="{x + 22}" y="{186 - h - 6:g}" text-anchor="middle" font-size="14" font-weight="800" class="g-y">{etiketler[k]}</text>'
            s += f'<text x="{x + 22}" y="204" text-anchor="middle" font-size="13" font-weight="700" class="g-y">{ad}</text>'
            s += f'<text x="{x + 22}" y="219" text-anchor="middle" font-size="11.5" class="g-s">{at}</text>'
        s += f'<text x="{x0 + 100}" y="246" text-anchor="middle" font-size="12.5" font-weight="800" class="{yazi}">{alt}</text>'
        return s

    ic += panel(16, 'Sıklık', 5, [(0, '0'), (10, '10'), (20, '20'), (30, '30')], (15, 21), ('15', '21'), 'Mert öne çıkar', 'g-tf')
    ic += panel(232, 'Göreli sıklık', 1.5, [(0, '0'), (50, '%50'), (100, '%100')], (75, 70), ('%75', '%70'), 'Ece öne çıkar', 'g-mf')
    return svg(440, 256, ic, 'Ece 20 atışta 15, Mert 30 atışta 21 isabet ettirdi. Sıklığa bakınca Mert 21 ile öndedir; göreli sıklığa bakınca Ece yüzde 75 ile öne geçer, '
               'Mert yüzde 70 ile geride kalır. Sıklık ve göreli sıklık grafikleri ayrı eksenlerle çizilmiştir.')


def uygula(o):
    g = {'Deney, çıktı ve olay': deney_cikti_olay(),
         'Olasılık spektrumu ve ilk tahminler': spektrum(),
         'Sonuçları kaydetmek: çetele, sıklık ve grafik': cark_grafigi(),
         'Deneysel olasılık': kup_tablosu(),
         'Tekrar sayısı ve sonuçları yorumlama': karsilastirma()}
    for b in o['bolumler']:
        if b['baslik'] in g:
            b['gorsel'] = g[b['baslik']]
