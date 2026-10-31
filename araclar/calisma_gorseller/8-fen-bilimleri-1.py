"""8. sınıf Fen Bilimleri 1. hafta (Mevsimlerin Oluşumu: eksen eğikliği, dolanma hareketi, ışın açısı ve dört önemli tarih) çalışma kâğıdı görselleri (SVG; insan figürü yok K024/K048; görsel içi yazı 10.5-12.5 pt K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, KAHVE, YESIL_K = '#c9a227', '#8a5a2b', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=17):
    stil = f' style="max-height:calc(16mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=11.5, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def rozet(x, y, metin, renk, r=10, boy=11):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{renk}" stroke-width="2"/>' + yazi(x, y + boy * 0.35, metin, boy, renk)


def isik_egim_deneyi():
    ic = f'<rect x="6" y="6" width="286" height="114" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(149, 23, 'K Yüzeyi · Dik Işınlar (90°)', 11.8, TUR)
    for x in (96, 128, 160):
        ic += f'<line x1="{x}" y1="34" x2="{x}" y2="76" stroke="{TUR}" stroke-width="2.4"/>'
        ic += f'<path d="M{x - 4} 70 l4 6 l4 -6" fill="none" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<line x1="66" y1="80" x2="232" y2="80" stroke="{LAC}" stroke-width="2.5"/>'
    ic += f'<line x1="94" y1="80" x2="162" y2="80" stroke="{KIR}" stroke-width="5"/>'
    ic += yazi(149, 98, 'Dar aydınlanma alanı (S₁)', 11, KIR)
    ic += yazi(149, 113, 'Birim yüzeye düşen enerji: Fazla', 10.6, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="114" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(451, 23, 'L Yüzeyi · Eğik Işınlar (30°)', 11.8, MAVI)
    for x in (368, 404, 440):
        ic += f'<line x1="{x}" y1="34" x2="{x + 48}" y2="76" stroke="{TUR}" stroke-width="2.4"/>'
        ic += f'<path d="M{x + 41} 75 l7 1 l-2 -7" fill="none" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<line x1="348" y1="80" x2="554" y2="80" stroke="{LAC}" stroke-width="2.5"/>'
    ic += f'<line x1="406" y1="80" x2="500" y2="80" stroke="{MAVI}" stroke-width="5"/>'
    ic += yazi(451, 98, 'Geniş aydınlanma alanı (S₂ > S₁)', 11, MAVI)
    ic += yazi(451, 113, 'Birim yüzeye düşen enerji: Az', 10.6, LAC, ince=True)
    return svg(600, 126, ic, 'Özdeş el fenerleriyle K yüzeyine dik (90°), L yüzeyine eğik (30°) gönderilen ışınların aydınlattığı alanlar.', 23)


def dolanma_konumlari():
    ic = f'<rect x="6" y="6" width="588" height="128" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += f'<ellipse cx="300" cy="70" rx="210" ry="44" fill="none" stroke="{GRI}" stroke-width="1.6" stroke-dasharray="5 3"/>'
    # Güneş
    ic += f'<circle cx="300" cy="70" r="18" fill="#f5c421" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(300, 74, 'Güneş', 10.8, LAC)
    konumlar = [
        (90, 70, 'I (21 Haziran)', 'KYK: Yaz', MAVI, 32, 70),
        (300, 114, 'II (23 Eylül)', 'KYK: Sonbahar', TUR, 405, 122),
        (510, 70, 'III (21 Aralık)', 'KYK: Kış', MOR, 558, 70),
        (300, 26, 'IV (21 Mart)', 'KYK: İlkbahar', YES, 195, 22),
    ]
    for cx, cy, ad, alt, renk, tx, ty in konumlar:
        ic += f'<circle cx="{cx}" cy="{cy}" r="12" fill="{MAVI_A}" stroke="{renk}" stroke-width="2"/>'
        ic += f'<line x1="{cx - 5}" y1="{cy + 13}" x2="{cx + 5}" y2="{cy - 13}" stroke="{KIR}" stroke-width="1.8"/>'
        ic += yazi(tx, ty - 4, ad, 10.8, renk)
        ic += yazi(tx, ty + 10, alt, 10.2, LAC, ince=True)
    return svg(600, 140, ic, 'Dünya’nın Güneş çevresindeki dört konumu: I (21 Haziran), II (23 Eylül), III (21 Aralık), IV (21 Mart).', 24)


def dort_tarih_kartlari():
    kartlar = [
        ('1. Kart · 21 Haziran', 'KYK’de en uzun gündüz yaşanır;', 'gündüzler kısalmaya başlar.', TUR, TUR_A),
        ('2. Kart · 23 Eylül', 'Gece ve gündüz eşitlenir (12 sa);', 'KYK’de yaprak dökümü dönemi.', MAVI, MAVI_A),
        ('3. Kart · 21 Aralık', 'KYK’de en uzun gece yaşanır;', 'GYK’de yaz mevsimi başlar.', MOR, MOR_A),
        ('4. Kart · 21 Mart', 'Gece ve gündüz eşitlenir (12 sa);', 'KYK’de havalar ısınmaya başlar.', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 298
        y = 4 + (i // 2) * 60
        ic += f'<rect x="{x}" y="{y}" width="286" height="52" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += f'<rect x="{x}" y="{y}" width="8" height="52" rx="4" fill="{renk}"/>'
        ic += yazi(x + 18, y + 18, bas, 11.2, renk, 'start')
        ic += yazi(x + 18, y + 34, s1, 10.6, LAC, 'start', ince=True)
        ic += yazi(x + 18, y + 47, s2, 10.6, LAC, 'start', ince=True)
    return svg(600, 124, ic, 'Dört önemli tarih kartı: 21 Haziran, 23 Eylül, 21 Aralık ve 21 Mart.', 22)


def golge_boyu_grafik():
    ic = f'<rect x="6" y="6" width="588" height="116" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.5"/>'
    ic += yazi(300, 23, 'M Şehrinde Öğle Vakti Gölge Boyunun Yıl İçindeki Değişimi', 11.8, LAC)
    ic += f'<line x1="64" y1="34" x2="64" y2="96" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="64" y1="96" x2="540" y2="96" stroke="{LAC}" stroke-width="1.8"/>'
    ic += yazi(54, 44, 'Uzun', 10.2, LAC, 'end', ince=True)
    ic += yazi(54, 96, '0', 10.5, KIR, 'end')
    barlar = [
        (120, 66, '21 Mart', MAVI),
        (240, 38, '21 Haziran', TUR),
        (360, 66, '23 Eylül', YES),
        (480, 96, '21 Aralık', KIR),
    ]
    for x, y_ust, tarih, renk in barlar:
        h = 96 - y_ust
        if h > 0:
            ic += f'<rect x="{x - 18}" y="{y_ust}" width="36" height="{h}" rx="4" fill="{renk}"/>'
        else:
            ic += f'<circle cx="{x}" cy="96" r="5" fill="{KIR}"/>'
            ic += yazi(x, 84, 'Gölge = 0', 10.5, KIR)
        ic += yazi(x, 111, tarih, 10.6, LAC)
    return svg(600, 128, ic, 'M şehrinde öğle vakti gölge boyu grafiği: 21 Haziran en uzun, 21 Aralık sıfır.', 23)


def isin_enerji_zinciri():
    adlar = [
        ('1. Halka', 'Eksen Eğikliği', MAVI, MAVI_A),
        ('2. Halka', 'Dik / Dike Yakın', TUR, TUR_A),
        ('3. Halka', 'Dar Aydınlanma', YES, YES_A),
        ('4. Halka', 'Çok Birim Enerji', KIR, '#fdeaea'),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="10" width="132" height="68" rx="12" fill="{arka}" stroke="{renk}" stroke-width="1.8"/>'
        ic += yazi(x + 66, 34, ust, 11.5, renk)
        ic += yazi(x + 66, 56, alt, 10.8, LAC)
        if i < 3:
            ic += f'<line x1="{x + 134}" y1="44" x2="{x + 146}" y2="44" stroke="{LAC}" stroke-width="2"/>'
            ic += f'<path d="M{x + 141} 39 l5 5 l-5 5" fill="none" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 88, ic, 'Işın açısı, aydınlanan alan ve birim yüzey enerjisi zinciri.', 20)


def uzaklik_yanilgisi_kart():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 25, '3 Ocak (Günberi Konumu)', 11.8, MAVI)
    ic += yazi(149, 47, 'Güneş’e uzaklık: 147 milyon km (En yakın)', 10.6, LAC, ince=True)
    ic += yazi(149, 65, 'Türkiye’de (KYK) yaşanan: Kış mevsimi', 10.8, MAVI)
    ic += yazi(149, 83, 'Güney yarım kürede: Yaz mevsimi', 10.6, LAC, ince=True)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 25, '4 Temmuz (Günöte Konumu)', 11.8, TUR)
    ic += yazi(451, 47, 'Güneş’e uzaklık: 152 milyon km (En uzak)', 10.6, LAC, ince=True)
    ic += yazi(451, 65, 'Türkiye’de (KYK) yaşanan: Yaz mevsimi', 10.8, TUR)
    ic += yazi(451, 83, 'Güney yarım kürede: Kış mevsimi', 10.6, LAC, ince=True)
    return svg(600, 110, ic, '3 Ocak (147 milyon km, Türkiye kış) ve 4 Temmuz (152 milyon km, Türkiye yaz) karşılaştırma kartları.', 21)


def iki_sehir_kure():
    ic = f'<rect x="6" y="6" width="588" height="106" rx="10" fill="#f7fafe" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(150, 26, 'Tarih: 21 Haziran Konumu', 11.8, MAVI)
    # Güneş ışınları soldan
    for y in (42, 62, 82):
        ic += f'<line x1="36" y1="{y}" x2="210" y2="{y}" stroke="{TUR}" stroke-width="2.2"/>'
        ic += f'<path d="M204 {y - 4} l6 4 l-6 4" fill="none" stroke="{TUR}" stroke-width="1.8"/>'
    ic += yazi(115, 35, 'Güneş ışınları', 10.8, TUR)
    # Dünya küresi
    cx, cy, r = 270, 60, 38
    ic += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{MAVI_A}" stroke="{LAC}" stroke-width="2"/>'
    ic += f'<line x1="{cx - 16}" y1="{cy + 42}" x2="{cx + 16}" y2="{cy - 42}" stroke="{KIR}" stroke-width="1.8" stroke-dasharray="4 2"/>'
    ic += f'<line x1="{cx - 36}" y1="{cy - 12}" x2="{cx + 36}" y2="{cy + 12}" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<circle cx="{cx - 8}" cy="{cy - 16}" r="4.5" fill="{YES}"/><text x="{cx + 2}" y="{cy - 12}" font-size="11.5" {YAZI} fill="{YESIL_K}">P</text>'
    ic += f'<circle cx="{cx - 16}" cy="{cy + 16}" r="4.5" fill="{MOR}"/><text x="{cx - 6}" y="{cy + 20}" font-size="11.5" {YAZI} fill="{MOR}">R</text>'
    # Sağ bilgi
    ic += f'<rect x="348" y="16" width="232" height="86" rx="8" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(464, 36, '21 Haziran Gözlem Notu', 11.5, LAC)
    ic += yazi(464, 56, 'P şehri Kuzey yarım kürededir.', 10.6, YESIL_K, ince=True)
    ic += yazi(464, 74, 'R şehri Güney yarım kürededir.', 10.6, MOR, ince=True)
    ic += yazi(464, 92, 'Kuzey kutbu Güneş’e dönüktür.', 10.6, LAC, ince=True)
    return svg(600, 118, ic, '21 Haziran tarihinde Kuzey yarım küredeki P şehri ve Güney yarım küredeki R şehrinin Dünya üzerindeki konumu.', 22)


def model_karsilastirma():
    ic = f'<rect x="6" y="6" width="286" height="98" rx="10" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.6"/>'
    ic += yazi(149, 24, '1. Model · Dik Eksen (Eğiklik = 0°)', 11.5, LAC)
    ic += f'<circle cx="64" cy="62" r="24" fill="#fff" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="64" y1="30" x2="64" y2="94" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<line x1="40" y1="62" x2="88" y2="62" stroke="{MAVI}" stroke-width="1.5" stroke-dasharray="3 2"/>'
    ic += yazi(185, 52, 'Dönme ekseni yörünge', 10.8, LAC, ince=True)
    ic += yazi(185, 70, 'düzlemine tam diktir;', 10.8, LAC, ince=True)
    ic += yazi(185, 88, 'açı yıl boyu değişmez.', 10.8, KIR)

    ic += f'<rect x="308" y="6" width="286" height="98" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(451, 24, '2. Model · Eğik Eksen (23° 27′)', 11.5, YESIL_K)
    ic += f'<circle cx="366" cy="62" r="24" fill="#fff" stroke="{LAC}" stroke-width="1.8"/>'
    ic += f'<line x1="354" y1="92" x2="378" y2="32" stroke="{KIR}" stroke-width="2"/>'
    ic += f'<line x1="344" y1="54" x2="388" y2="70" stroke="{MAVI}" stroke-width="1.5" stroke-dasharray="3 2"/>'
    ic += yazi(487, 52, 'Gerçek Dünya modeli:', 10.8, LAC, ince=True)
    ic += yazi(487, 70, 'Yıl boyunca ışınların', 10.8, LAC, ince=True)
    ic += yazi(487, 88, 'düşme açısı değişir.', 10.8, YESIL_K)
    return svg(600, 110, ic, '1. Model dik eksenli (0° eğiklik) ve 2. Model eğik eksenli (23° 27′) Dünya karşılaştırması.', 21)


def toplam_birim_enerji_pano():
    ic = f'<rect x="6" y="6" width="286" height="94" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(149, 25, 'Deneydeki Sabit Değişken', 11.5, MAVI)
    ic += yazi(149, 48, 'Özdeş iki el fenerinden çıkan', 10.8, LAC, ince=True)
    ic += yazi(149, 66, 'toplam ışık enerjisi birbirine', 10.8, LAC, ince=True)
    ic += yazi(149, 84, 'tamamen eşittir (E₁ = E₂).', 11, MAVI)

    ic += f'<rect x="308" y="6" width="286" height="94" rx="10" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(451, 25, 'Birim Yüzeye Düşen Enerji Farkı', 11.5, TUR)
    ic += yazi(451, 48, 'Dik açıda: Dar alan → Birim enerji çok', 10.8, LAC, ince=True)
    ic += yazi(451, 66, 'Eğik açıda: Geniş alan → Birim enerji az', 10.8, LAC, ince=True)
    ic += yazi(451, 84, 'Isınma farkını birim enerji belirler.', 11, TUR)
    return svg(600, 106, ic, 'Toplam ışık enerjisinin eşit olması ve birim yüzeye düşen enerjinin aydınlanan alana göre değişmesi.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = isik_egim_deneyi()
    s[4]['gorsel'] = dolanma_konumlari()
    s[5]['gorsel'] = dort_tarih_kartlari()
    s[6]['gorsel'] = golge_boyu_grafik()
    s[7]['gorsel'] = isin_enerji_zinciri()
    s[8]['gorsel'] = uzaklik_yanilgisi_kart()
    s[9]['gorsel'] = iki_sehir_kure()
    s[10]['gorsel'] = model_karsilastirma()
    s[12]['gorsel'] = toplam_birim_enerji_pano()
