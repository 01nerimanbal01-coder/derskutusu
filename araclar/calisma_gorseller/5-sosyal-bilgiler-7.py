"""5. sınıf Sosyal Bilgiler 7. hafta (Yaşadığımız İlin Göreceli Konumu: Yeryüzü Şekilleri, İklim, Ulaşım ve Nüfus Özellikleri) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def ankara_pusula_komsular_svg():
    ic = f'<rect x="6" y="6" width="588" height="114" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    cx, cy = 300, 63
    ic += f'<line x1="168" y1="{cy}" x2="432" y2="{cy}" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<line x1="{cx}" y1="26" x2="{cx}" y2="100" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<rect x="242" y="47" width="116" height="32" rx="8" fill="{MAVI}" stroke="{LAC}" stroke-width="1.5"/>'
    ic += yazi(cx, 67, 'ANKARA', 11.5, '#fff')
    # Kuzey, Güney, Batı, Doğu kutuları
    yonler = [
        (230, 10, 140, 24, 'Kuzey: Çankırı', YES, YES_A),
        (230, 92, 140, 24, 'Güney: Konya', TUR, TUR_A),
        (24, 51, 152, 24, 'Batı: Eskişehir', MOR, MOR_A),
        (424, 51, 152, 24, 'Doğu: Kırıkkale', KIR, '#fdeaea'),
    ]
    for x, y, w, h, met, renk, arka in yonler:
        ic += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + w / 2, y + 16, met, 10.6, LAC)
    return svg(600, 126, ic, 'Ankara ilinin dört ana yöndeki komşuları: Kuzeyde Çankırı, Güneyde Konya, Batıda Eskişehir, Doğuda Kırıkkale.', 19)


def fiziki_harita_basamak_kartlari_svg():
    kartlar = [
        ('1. İl: Bursa', 'Renk: Yeşil Tonu', 'Yükselti: 0 – 500 m', YES, YES_A),
        ('2. İl: Konya', 'Renk: Sarı - Turuncu', 'Yükselti: 500 – 1500 m', TUR, TUR_A),
        ('3. İl: Erzurum', 'Renk: Kahverengi', 'Yükselti: 1500 m üzeri', KAHVE, '#f5ebe1'),
        ('4. İl: Adana', 'Renk: Yeşil Tonu', 'Yükselti: 0 – 500 m', YESIL_K, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.6, LAC)
        ic += yazi(x + 68, 74, s2, 10.4, LAC, ince=True)
    return svg(600, 104, ic, 'Dört ilin fiziki harita renkleri ve yükselti basamakları: Bursa ve Adana yeşil, Konya sarı-turuncu, Erzurum kahverengi.', 18)


def il_ekonomi_kartlari_svg():
    kartlar = [
        ('1. Kart: Adana', 'Çukurova deltası ve', 'Seyhan-Ceyhan nehirleri', YES, YES_A),
        ('2. Kart: Kocaeli', 'Otoyol, demir yolu ve', 'işlek liman kavşağı', MAVI, MAVI_A),
        ('3. Kart: Antalya', 'Uzun Akdeniz kıyısı', 've bol güneşli günler', TUR, TUR_A),
        ('4. Kart: Kars', 'Yüksek platolar ve', 'gür yaz çayırları', KAHVE, '#f5ebe1'),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.4, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.4, LAC, ince=True)
    return svg(600, 104, ic, 'Adana, Kocaeli, Antalya ve Kars illerinin göreceli konum özelliklerini gösteren dört kart.', 18)


def mugla_hakkari_nisan_karti_svg():
    ic = f'<rect x="8" y="8" width="282" height="92" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Muğla (Aynı Nisan Günü — 26 °C)', 11.2, TUR)
    ic += yazi(24, 50, 'Konum: Ege ve Akdeniz kıyısı (0–200 m)', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 70, 'Hava: Güneşli ve ılık bahar havası', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 88, 'Yaşam: Kısa kollu giysi ve deniz etkinliği', 10.5, TUR, 'start')

    ic += f'<rect x="310" y="8" width="282" height="92" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Hakkâri (Aynı Nisan Günü — 2 °C)', 11.2, MAVI)
    ic += yazi(326, 50, 'Konum: Denizden uzak, yüksek dağlık (1700 m+)', 10.5, LAC, 'start', ince=True)
    ic += yazi(326, 70, 'Hava: Soğuk ve kar yağışlı', 10.5, LAC, 'start', ince=True)
    ic += yazi(326, 88, 'Yaşam: Kalın kışlık giysi ve kar temizliği', 10.5, MAVI, 'start')
    return svg(600, 108, ic, 'Aynı nisan gününde Muğla (26 derece, kıyı) ve Hakkâri (2 derece, yüksek dağlık) hava ve yaşam karşılaştırması.', 18)


def nufus_etki_zinciri_svg():
    adimlar = [
        ('Elverişli Konum', 'Düz ova ve kıyı kavşağı', YES, YES_A),
        ('Ulaşım ve Liman', 'Fabrika ve ticaret artışı', MAVI, MAVI_A),
        ('İş Olanakları', 'Yeni istihdam alanları', TUR, TUR_A),
        ('Yoğun Nüfus', 'Göç alma ve kalabalıklaşma', MOR, MOR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="80" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 36, ust, 11, renk)
        ic += yazi(x + 68, 62, alt, 10.4, LAC, ince=True)
    return svg(600, 96, ic, 'Göreceli konumun sanayi, iş imkânları ve nüfus yoğunluğunu artırma zinciri.', 18)


def k_ve_l_illeri_karsilastirma_svg():
    ic = f'<rect x="8" y="8" width="282" height="92" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'K İli Göreceli Konum Özeti', 11.2, YESIL_K)
    ic += yazi(24, 50, 'Yükselti: 120 m (Düz ve verimli kıyı ovası)', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 70, 'İklim: Kışları ılık, yağışlı denizel iklim', 10.5, LAC, 'start', ince=True)
    ic += yazi(24, 88, 'Ulaşım: İşlek liman, otoyol ve demir yolu', 10.5, YESIL_K, 'start')

    ic += f'<rect x="310" y="8" width="282" height="92" rx="10" fill="#f5ebe1" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'L İli Göreceli Konum Özeti', 11.2, KAHVE)
    ic += yazi(326, 50, 'Yükselti: 1950 m (Sarp ve engebeli dağlar)', 10.5, LAC, 'start', ince=True)
    ic += yazi(326, 70, 'İklim: Uzun, çok soğuk ve karlı kış mevsimi', 10.5, LAC, 'start', ince=True)
    ic += yazi(326, 88, 'Ulaşım: Dar dağ geçitleri, deniz bağlantısı yok', 10.5, KAHVE, 'start')
    return svg(600, 108, ic, 'K ili (120 m kıyı ovası, limanlı) ile L ili (1950 m sarp dağlık, karasal) göreceli konum karşılaştırma kartları.', 18)


def turizm_kartlari_svg():
    kartlar = [
        ('1. Kart: Bursa', 'Uludağ kayak pistleri', 've kar kalınlığı', MAVI, MAVI_A),
        ('2. Kart: Nevşehir', 'Kapadokya peri bacaları', 've tarihî yer altı şehirleri', MOR, MOR_A),
        ('3. Kart: Muğla', 'Güneşli koylar, sıcak', 'deniz ve kumsallar', TUR, TUR_A),
        ('4. Kart: Çanakkale', 'Gelibolu Yarımadası', 'tarihî şehitlik ve anıtlar', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 26, bas, 11.2, renk)
        ic += f'<line x1="{x + 14}" y1="34" x2="{x + 122}" y2="34" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 68, 54, s1, 10.4, LAC, ince=True)
        ic += yazi(x + 68, 72, s2, 10.4, LAC, ince=True)
    return svg(600, 104, ic, 'Dört turizm tanıtım kartı: 1. Bursa Uludağ, 2. Nevşehir Kapadokya, 3. Muğla koylar, 4. Çanakkale şehitlik ve anıtlar.', 18)


def bati_dogu_yukselis_kesiti_svg():
    ic = f'<rect x="6" y="6" width="588" height="104" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 24, 'Türkiye Batı — Doğu Yükselti ve Harita Rengi Kesiti', 11.2, LAC)
    # Üç basamak: Batı (İzmir), İç (Ankara), Doğu (Erzurum)
    ic += f'<rect x="28" y="68" width="166" height="30" rx="5" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(111, 82, 'Batı: İzmir (0–500 m)', 10.6, YESIL_K)
    ic += yazi(111, 94, 'Fiziki Renk: Yeşil', 10, LAC, ince=True)

    ic += f'<rect x="216" y="52" width="166" height="46" rx="5" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(299, 70, 'İç: Ankara (500–1500 m)', 10.6, TUR)
    ic += yazi(299, 88, 'Fiziki Renk: Sarı-Turuncu', 10, LAC, ince=True)

    ic += f'<rect x="404" y="34" width="168" height="64" rx="5" fill="#f5ebe1" stroke="{KAHVE}" stroke-width="1.6"/>'
    ic += yazi(488, 58, 'Doğu: Erzurum (1500 m+)', 10.6, KAHVE)
    ic += yazi(488, 80, 'Fiziki Renk: Kahverengi', 10, LAC, ince=True)
    return svg(600, 116, ic, 'Batıdan (İzmir, yeşil) doğuya (Erzurum, kahverengi) doğru yükseltinin artışını gösteren kesit şeması.', 18)


def iki_harita_turu_karti_svg():
    ic = f'<rect x="8" y="8" width="282" height="86" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Harita A: Türkiye Siyasi (İdari) Haritası', 11, MAVI)
    ic += yazi(149, 50, '81 ilimizin idari sınırları, bölgeleri,', 10.6, LAC, ince=True)
    ic += yazi(149, 70, 'komşu iller ve sınır kapıları gösterilir.', 10.6, LAC, ince=True)

    ic += f'<rect x="310" y="8" width="282" height="86" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Harita B: Türkiye Fiziki Haritası', 11, YESIL_K)
    ic += yazi(451, 50, 'Dağlar, ovalar, platolar, akarsular ve', 10.6, LAC, ince=True)
    ic += yazi(451, 70, 'renklerle yükselti basamakları gösterilir.', 10.6, LAC, ince=True)
    return svg(600, 102, ic, 'Harita A (Türkiye Siyasi Haritası) ve Harita B (Türkiye Fiziki Haritası) karşılaştırma kartları.', 18)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ankara_pusula_komsular_svg()
    s[4]['gorsel'] = fiziki_harita_basamak_kartlari_svg()
    s[5]['gorsel'] = il_ekonomi_kartlari_svg()
    s[6]['gorsel'] = mugla_hakkari_nisan_karti_svg()
    s[7]['gorsel'] = nufus_etki_zinciri_svg()
    s[8]['gorsel'] = k_ve_l_illeri_karsilastirma_svg()
    s[9]['gorsel'] = turizm_kartlari_svg()
    s[10]['gorsel'] = bati_dogu_yukselis_kesiti_svg()
    s[12]['gorsel'] = iki_harita_turu_karti_svg()
