"""8. sınıf T.C. İnkılap Tarihi ve Atatürkçülük 3. hafta (Mustafa Kemal’in Fikir Hayatının Oluşması) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5–12.5 pt (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=24):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def dort_sehir_semasi():
    """Selânik, Manastır, Sofya ve İstanbul şehir ortam kartları."""
    kartlar = [
        ('Selânik', 'İşlek liman · Demir yolu', MAVI, MAVI_A),
        ('Manastır', 'Konsolosluklar · M. Tevfik Bey', TUR, TUR_A),
        ('Sofya (1913)', 'Ataşemiliter · Meclis · Opera', YES, YES_A),
        ('İstanbul', 'Başkent · Elçilikler · Basın', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 11, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört şehir kartı: Selânik liman ve demir yolu, Manastır konsolosluklar, Sofya ataşemiliter ve meclis, İstanbul başkent ve basın.', 18)


def selanik_manastir_karti():
    """Selânik ve Manastır karşılaştırma şeması."""
    ic = kutu(4, 4, 172, 82, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(90, 20, 'Selânik Ortamı', 11, MAVI)
    ic += yazi(90, 38, 'Avrupa ile demir yolu ve', 10.5, LAC, 'middle', True)
    ic += yazi(90, 53, 'liman bağlantısı sayesinde', 10.5, LAC, 'middle', True)
    ic += yazi(90, 68, 'Batı etkisine açık şehirdi.', 10.5, MAVI)

    ic += kutu(184, 4, 172, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(270, 20, 'Manastır Ortamı', 11, TUR)
    ic += yazi(270, 38, 'Avrupa devletlerinin açtığı', 10.5, LAC, 'middle', True)
    ic += yazi(270, 53, 'konsolosluklar üzerinden Batı', 10.5, LAC, 'middle', True)
    ic += yazi(270, 68, 'siyaseti izlenebiliyordu.', 10.5, TUR)
    return svg(360, 90, ic, 'Selânik ve Manastır şehirlerinin Batı ile temas sağlayan ortam özellikleri.', 18)


def sofya_gorev_panosu():
    """1913 Sofya ataşemiliterlik görevi panosu."""
    ic = kutu(4, 4, 352, 92, KUM, GRI, 8, 1.3)
    ic += f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 19, 'SOFYA ATAŞEMİLİTERLİK GÖREVİ (1913) GÖZLEMLERİ', 10.5, '#fff')
    adimlar = [
        ('Diplomasi & Sanat', 'Elçiler · Opera', MAVI, MAVI_A, 10),
        ('Türk Azınlık', 'Basın ve haklar', TUR, TUR_A, 126),
        ('Bulgar Meclisi', 'Parlamenter rejim', YES, YES_A, 242),
    ]
    for bas, alt, r, z, x in adimlar:
        ic += kutu(x, 32, 108, 56, z, r, 7, 1.2)
        ic += yazi(x + 54, 50, bas, 10.5, r)
        ic += yazi(x + 54, 70, alt, 10.5, LAC, 'middle', True)
    return svg(360, 100, ic, 'Sofya ataşemiliterlik görevi panosu: Diplomasi ve kültür, Bulgaristan Türkleri, Bulgar Meclisi.', 19)


def fikir_kronoloji_seridi():
    """Selânik'ten Sofya'ya fikir gelişim basamakları."""
    duraklar = [
        ('1. Adım', 'Selânik', MAVI, MAVI_A),
        ('2. Adım', 'Manastır', TUR, TUR_A),
        ('3. Adım', 'İstanbul', MOR, MOR_A),
        ('4. Adım', 'Sofya (1913)', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, r, z) in enumerate(duraklar):
        x = 4 + i * 89
        ic += kutu(x, 8, 83, 58, z, r, 7, 1.3)
        ic += yazi(x + 41.5, 28, ust, 10.5, r)
        ic += yazi(x + 41.5, 48, alt, 11, LAC)
    return svg(358, 74, ic, 'Dört gelişim basamağı: Selânik, Manastır, İstanbul ve 1913 Sofya.', 18)


def yerli_aydinlar_semasi():
    """Dört yerli şair ve yazarın etki şeması."""
    kartlar = [
        ('Namık Kemal', 'Vatan sevgisi, milliyetçilik', MAVI, MAVI_A),
        ('M. Emin Yurdakul', '? (Düşünce katkısı)', TUR, TUR_A),
        ('Tevfik Fikret', '? (Düşünce katkısı)', YES, YES_A),
        ('Ziya Gökalp', 'Türkleşmek, muasırlaşmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x, y = 4 + (i % 2) * 180, 4 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r, 7, 1.3)
        ic += yazi(x + 10, y + 16, bas, 10.8, r, 'start')
        ic += yazi(x + 10, y + 31, alt, 10.5, LAC, 'start', True)
    return svg(360, 92, ic, 'Dört yerli aydın şeması: Namık Kemal, Mehmet Emin Yurdakul, Tevfik Fikret, Ziya Gökalp.', 18)


def yabanci_dusunurler_kartlari():
    """Montesquieu, Kant, Rousseau ve Voltaire özet kartları."""
    kartlar = [
        ('Montesquieu', ['Kanunların Ruhu', 'Cumhuriyet fikri'], MAVI, MAVI_A, 4),
        ('Kant & Voltaire', ['Akıl ve bilimsellik', 'Demokratikleşme'], TUR, TUR_A, 122),
        ('Rousseau', ['Hukuk devleti', 'Millî egemenlik'], YES, YES_A, 240),
    ]
    ic = ''
    for bas, sat, r, z, x in kartlar:
        ic += kutu(x, 4, 116, 76, z, r, 8, 1.3)
        ic += yazi(x + 58, 20, bas, 10.5, r)
        ic += yazi(x + 58, 42, sat[0], 10.5, LAC, 'middle', True)
        ic += yazi(x + 58, 60, sat[1], 10.5, LAC, 'middle', True)
    return svg(360, 84, ic, 'Yabancı düşünürler: Montesquieu, Kant, Voltaire ve Rousseau.', 18)


def istanbul_bilgi_karti():
    """İstanbul'da Beyoğlu-Galata ve Fransızca gazetelerle çözüm arayışı kartı."""
    ic = kutu(4, 4, 352, 78, MOR_A, MOR, 8, 1.3)
    ic += yazi(180, 20, 'Başkent İstanbul’da Gözlem ve Çözüm Arayışı', 11, MOR)
    ic += kutu(12, 28, 164, 46, '#fff', MOR, 6, 1.2)
    ic += yazi(94, 45, 'Beyoğlu ve Galata:', 10.5, LAC, 'middle', True)
    ic += yazi(94, 62, 'Elçilikler ve kültür ortamı', 10.5, MOR)
    ic += kutu(184, 28, 164, 46, '#fff', YES, 6, 1.2)
    ic += yazi(266, 45, 'Fransızca gazeteler:', 10.5, LAC, 'middle', True)
    ic += yazi(266, 62, 'Yenilikçi çözüm arayışı', 10.5, YES)
    return svg(360, 86, ic, 'İstanbul da Beyoğlu ve Galata ortamı ile Fransızca gazeteleri izleyerek çözüm arama.', 18)


def uc_kaynak_haritasi():
    """Mustafa Kemal'in fikir hayatını besleyen 3 ana kaynak şeması."""
    ic = kutu(80, 4, 200, 24, LAC, LAC, 12, 1.2)
    ic += yazi(180, 20, 'Fikir Hayatını Besleyen 3 Kaynak', 10.8, '#fff')
    kaynaklar = [
        ('1. Kaynak', 'Yaşadığı Şehirler', MAVI, MAVI_A, 4),
        ('2. Kaynak', 'Düşünür-Yazarlar', TUR, TUR_A, 122),
        ('3. Kaynak', 'Okuduğu Eserler', YES, YES_A, 240),
    ]
    for ust, alt, r, z, x in kaynaklar:
        ic += kutu(x, 34, 116, 44, z, r, 7, 1.3)
        ic += yazi(x + 58, 51, ust, 10.5, r)
        ic += yazi(x + 58, 68, alt, 10.5, LAC)
    return svg(360, 82, ic, 'Mustafa Kemal in fikir hayatını besleyen üç kaynak: Yaşadığı şehirler, düşünür ve yazarlar, okuduğu eserler.', 18)


def sentez_degerlendirme_karti():
    """Yerli aydınlar ile Batılı düşünürlerin sentezini gösteren kart."""
    ic = kutu(4, 4, 172, 74, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, 'Yerli Aydınların Etkisi', 10.8, YES)
    ic += yazi(90, 42, 'Namık Kemal · Ziya Gökalp', 10.5, LAC, 'middle', True)
    ic += yazi(90, 58, '→ Vatan ve millî değerler', 10.5, YES)

    ic += kutu(184, 4, 172, 74, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(270, 20, 'Batılı Düşünürlerin Etkisi', 10.8, MAVI)
    ic += yazi(270, 42, 'Kant · Montesquieu · Rousseau', 10.5, LAC, 'middle', True)
    ic += yazi(270, 58, '→ Akıl, bilim, egemenlik', 10.5, MAVI)
    return svg(360, 82, ic, 'Yerli aydınların millî değerler etkisi ile Batılı düşünürlerin akıl, bilim ve halk egemenliği etkisi.', 18)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_sehir_semasi()
    s[1]['gorsel'] = selanik_manastir_karti()
    s[5]['gorsel'] = sofya_gorev_panosu()
    s[6]['gorsel'] = fikir_kronoloji_seridi()
    s[7]['gorsel'] = yerli_aydinlar_semasi()
    s[8]['gorsel'] = yabanci_dusunurler_kartlari()
    s[9]['gorsel'] = istanbul_bilgi_karti()
    s[10]['gorsel'] = uc_kaynak_haritasi()
    s[13]['gorsel'] = sentez_degerlendirme_karti()
