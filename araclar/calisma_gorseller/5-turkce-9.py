"""5. sınıf Türkçe 9. hafta (Oğlu Hüseyin'den Emine Ana'ya Mektuplar: Hikâye Unsurları, Kök ve Ek, Bağlantı İfadeleri, Yazım-Noktalama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_kok_turu_kartlari():
    kartlar = [
        ('1. Kart', 'Sevgili', 'Kök: sev-', YES, YES_A),
        ('2. Kart', 'Bayraktar', 'Kök: bayrak', MAVI, MAVI_A),
        ('3. Kart', 'Köylüler', 'Kök: köy', TUR, TUR_A),
        ('4. Kart', 'Suluğun', 'Kök: su', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, kel, kok, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r)
        ic += yazi(x + 41, 22, bas, 10.2, r)
        ic += yazi(x + 41, 45, kel, 10.6, LAC)
        ic += yazi(x + 41, 65, kok, 9.4, LAC, ince=True)
    return svg(360, 86, ic, 'Dört kelimenin köklerini gösteren inceleme kartları.', 15)


def yapim_cekim_inceleme_kartlari():
    kartlar = [
        ('1. Kelime', 'Göz - lük - çü', MAVI, MAVI_A),
        ('2. Kelime', 'Mektup - lar - ım', YES, YES_A),
        ('3. Kelime', 'Bil - gin', TUR, TUR_A),
        ('4. Kelime', 'Cephe - den', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ekler, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, ekler, 9.2, LAC)
    return svg(360, 84, ic, 'Yapım ve çekim eki almış dört kelime kartı.', 15)


def dort_cumle_ek_kartlari():
    kartlar = [
        ('I. Kart', 'ev - ler - in (Çekim)', MAVI, MAVI_A),
        ('II. Kart', 'gazete - ci - ler (Yapım+Çekim)', YES, YES_A),
        ('III. Kart', 'mektup - lar (Çekim)', TUR, TUR_A),
        ('IV. Kart', 'yol - u (Çekim)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, acik, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, acik, 9.4, LAC, ince=True)
    return svg(360, 94, ic, 'Dört cümledeki altı çizili kelimelerin ek yapısı.', 16)


def baglanti_ifadeleri_panosu():
    ic = kutu(6, 6, 170, 76, TUR_A, TUR)
    ic += yazi(91, 22, '1. Düşünce Yönünü Değiştirme', 9.9, TUR)
    ic += yazi(91, 44, '«Hava çok soğuktu [ K ]', 9.7, LAC, ince=True)
    ic += yazi(91, 64, 'nöbet yerini terk etmedik.»', 9.7, LAC)

    ic += kutu(184, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(269, 22, '2. Özetleme ve Sonuç Bildirme', 9.9, MAVI)
    ic += yazi(269, 44, '«[ L ] milletimiz birlik olarak', 9.7, LAC, ince=True)
    ic += yazi(269, 64, 'büyük zafere ulaşmıştır.»', 9.7, LAC)
    return svg(360, 88, ic, 'Düşüncenin yönünü değiştiren ve özetleyen bağlantı ifadeleri kartı.', 15)


def anlam_bagi_kok_karti():
    ic = kutu(6, 6, 170, 76, YES_A, YES)
    ic += yazi(91, 22, '1. Doğru Kök Çözümlemesi', 10.1, YESIL_K)
    ic += yazi(91, 44, 'Kelime: Simitçi → Kök: simit', 9.8, LAC)
    ic += yazi(91, 64, '(Simit ile simitçi arasında bağ var)', 9.1, YESIL_K, ince=True)

    ic += kutu(184, 6, 170, 76, KIR_A, KIR)
    ic += yazi(269, 22, '2. Hatalı Kök Çözümlemesi', 10.1, KIR)
    ic += yazi(269, 44, 'Kelime: Kelebek → Kök: kel (?)', 9.8, LAC)
    ic += yazi(269, 64, '(Kel ile kelebek arasında bağ yok!)', 9.1, KIR, ince=True)
    return svg(360, 88, ic, 'Simitçi ve kelebek kelimelerinde kök ve anlam bağı karşılaştırması.', 15)


def mektup_bolumleri_akis():
    bolumler = [
        ('1. Serim', 'Selam ve sağlık haberi', MAVI, MAVI_A),
        ('2. Düğüm-1', 'Atatürk’ün cepheye gelişi', TUR, TUR_A),
        ('3. Düğüm-2', 'Büyük taarruz hazırlığı', MOR, MOR_A),
        ('4. Çözüm', 'Zafer müjdesi ve veda', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(bolumler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.2, r)
        ic += yazi(x + 41, 55, alt, 8.9, LAC, ince=True)
    return svg(360, 84, ic, 'Metnin serim, düğüm ve çözüm bölümleri akış şeması.', 15)


def yazim_noktalama_denetim_panosu():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 21, 'Yazım ve Noktalama Kontrol Panosu', 10.4, MAVI)
    ic += yazi(180, 40, '1) Hitap: Canım Annem,   |   2) Tarih: 29 Ekim 1923’te', 9.6, LAC, ince=True)
    ic += yazi(180, 58, '3) Belirli Gün: 10 Kasım’da   |   4) Özel Ad + Yapım Eki: İzmir’liler (?)', 9.6, KIR)
    ic += yazi(180, 75, 'Kural: Özel adlara gelen yapım ekleri (-li, -lik, -ce) kesmeyle ayrılmaz!', 9.4, MAVI)
    return svg(360, 92, ic, 'Hitap, tarih ve özel adlara gelen eklerin yazımı panosu.', 16)


def hikaye_unsurlari_ozet_karti():
    unsurlar = [
        ('Kişiler', 'Hüseyin, Emine Ana, Atatürk', MAVI, MAVI_A),
        ('Mekân ve Zaman', 'Cephe · Millî Mücadele', TUR, TUR_A),
        ('Olay Örgüsü', 'Cepheden mektup ve zafer', YES, YES_A),
        ('Ana Fikir', 'Vatan sevgisi ve birlik ruhu', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(unsurlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.2, r)
        ic += yazi(x + 86, y + 31, alt, 9.3, LAC, ince=True)
    return svg(360, 94, ic, 'Oğlu Hüseyin’den Emine Ana’ya Mektuplar metninin hikâye unsurları.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dort_kok_turu_kartlari()
    s[2]['gorsel'] = yapim_cekim_inceleme_kartlari()
    s[5]['gorsel'] = dort_cumle_ek_kartlari()
    s[6]['gorsel'] = baglanti_ifadeleri_panosu()
    s[7]['gorsel'] = anlam_bagi_kok_karti()
    s[8]['gorsel'] = mektup_bolumleri_akis()
    s[9]['gorsel'] = yazim_noktalama_denetim_panosu()
    s[11]['gorsel'] = hikaye_unsurlari_ozet_karti()
