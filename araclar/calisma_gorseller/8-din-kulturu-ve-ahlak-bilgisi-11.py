"""8. sınıf Din Kültürü ve Ahlak Bilgisi 11. hafta (Zekâtın Faydaları ve Hz. Şuayb) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); Noto Sans font-size=12 (K150 EK); eğik kesir ve beyaz bant yok (K155/K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#15803d', '#d63a3a', '#7c3aed', '#0e7490'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A, KUM = '#e8eefe', '#fef3c7', '#dcfce7', '#f3e8ff', '#fee2e2', '#e0f2fe', '#fffbeb'
YAZI = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-size="12" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kazanim_dort_kart():
    kartlar = [
        (4, 4, '1. Kart: Ekonomik Canlanma', 'Piyasada para dolaşımı', MAVI, MAVI_A),
        (214, 4, '2. Kart: Toplumsal Güvenlik', 'Suç oranlarının azalması', CAM, CAM_A),
        (4, 58, '3. Kart: Ruhsal Arınma', 'Şükür, şefkat ve iç huzur', YES, YES_A),
        (214, 58, '4. Kart: Sosyal Dayanışma', 'Zengin-fakir sevgi köprüsü', TUR, TUR_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 19, bas, r)
        ic += yazi(x + 101, y + 40, alt, LAC, ince=True)
    return svg(420, 110, ic, 'Zekât ve sadakanın bireysel ve toplumsal kazanım kartları.', 22)


def kaynak_ilkeler_panosu():
    ic = kutu(4, 4, 412, 98, YES_A, YES, 8)
    ic += yazi(210, 22, 'Kur’an ve Sünnette İnfak ile Ticaret İlkeleri', YES)
    ic += kutu(12, 32, 192, 62, KUM, TUR, 6)
    ic += yazi(108, 52, 'Bakara 261 · Hûd 85', TUR)
    ic += yazi(108, 78, 'Bereket ve Tam Ölçü', LAC, ince=True)
    ic += kutu(216, 32, 192, 62, MAVI_A, MAVI, 6)
    ic += yazi(312, 52, 'Hadis-i Şerif İlkeleri', MAVI)
    ic += yazi(312, 78, 'Gizlilik ve Veren El', LAC, ince=True)
    return svg(420, 106, ic, 'Bakara 261, Hûd 85 ve hadis ilkelerini gösteren kaynak panosu.', 21)


def yedi_basak_modeli():
    ic = kutu(4, 4, 412, 98, KUM, TUR, 8)
    ic += yazi(210, 22, 'Bakara Suresi 261. Ayet — İnfakın Bereket Temsili', TUR)
    ic += kutu(18, 36, 104, 54, YES_A, YES, 7)
    ic += yazi(70, 58, '1 Tohum', YES)
    ic += yazi(70, 79, '(İhlaslı İnfak)', LAC, ince=True)
    ic += yazi(142, 66, '→', TUR)
    ic += kutu(160, 36, 108, 54, MAVI_A, MAVI, 7)
    ic += yazi(214, 58, '7 Başak', MAVI)
    ic += yazi(214, 79, '(Her dalda 100)', LAC, ince=True)
    ic += yazi(286, 66, '→', TUR)
    ic += kutu(304, 36, 98, 54, MOR_A, MOR, 7)
    ic += yazi(353, 58, '700 Dane', MOR)
    ic += yazi(353, 79, '(Kat Kat Ecir)', LAC, ince=True)
    return svg(420, 106, ic, 'Bir tohumdan yedi başak ve yedi yüz dane bereket modeli.', 21)


def medyen_terazi_panosu():
    ic = kutu(4, 4, 200, 98, KIR_A, KIR, 8)
    ic += yazi(104, 22, 'Medyen Çarşısındaki Bozulma', KIR)
    ic += yazi(104, 48, '• Putlara tapma (Şirk)', LAC, ince=True)
    ic += yazi(104, 69, '• Eksik ölçme ve tartma', LAC, ince=True)
    ic += yazi(104, 90, '• Kervan yollarını kesme', KIR, ince=True)
    ic += kutu(216, 4, 200, 98, YES_A, YES, 8)
    ic += yazi(316, 22, 'Hz. Şuayb’ın (as) Çağrısı', YES)
    # Dengeli terazi çizimi
    ic += f'<line x1="316" y1="34" x2="316" y2="82" stroke="{YES}" stroke-width="1.5"/>'
    ic += f'<line x1="266" y1="48" x2="366" y2="48" stroke="{LAC}" stroke-width="1.5"/>'
    ic += f'<rect x="254" y="54" width="24" height="10" rx="2" fill="{KUM}" stroke="{TUR}" stroke-width="1.1"/>'
    ic += f'<rect x="354" y="54" width="24" height="10" rx="2" fill="{KUM}" stroke="{TUR}" stroke-width="1.1"/>'
    ic += yazi(316, 94, 'Tevhid + Adil Terazi (Hûd 85)', YES)
    return svg(420, 106, ic, 'Medyen halkının hileleri ve Hz. Şuayb’ın adil terazi çağrısı.', 21)


def sadaka_tasi_karti():
    ic = kutu(4, 4, 412, 98, CAM_A, CAM, 8)
    # Sadaka taşı silindirik sütun çizimi
    ic += f'<rect x="34" y="28" width="44" height="62" rx="6" fill="#cbd5e1" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<ellipse cx="56" cy="28" rx="22" ry="6" fill="#94a3b8" stroke="{LAC}" stroke-width="1.2"/>'
    ic += f'<ellipse cx="56" cy="28" rx="9" ry="3" fill="{LAC}"/>'
    ic += yazi(248, 26, 'Vakıf Medeniyeti Mirası: Sadaka Taşı', CAM)
    ic += yazi(248, 54, 'Gece gizlice bırakılır → İhtiyaç kadar alınır', LAC)
    ic += yazi(248, 80, 'Verende riya yok · Alanda mahcubiyet yok', YES, ince=True)
    return svg(420, 106, ic, 'Mimari sadaka taşı çizimi ve insan onurunu koruma ilkesi.', 21)


def sosyal_denge_akisi():
    adimlar = [
        (4, '1. Şükür', 'Zekât ayrılır', YES, YES_A),
        (108, '2. Paylaşım', 'Alım gücü artar', CAM, CAM_A),
        (212, '3. Ekonomi', 'Üretim canlanır', MAVI, MAVI_A),
        (316, '4. Huzur', 'Güven yerleşir', MOR, MOR_A),
    ]
    ic = ''
    for x, bas, alt, r, z in adimlar:
        ic += kutu(x, 8, 100, 88, z, r, 7)
        ic += yazi(x + 50, 34, bas, r)
        ic += f'<line x1="{x+10}" y1="46" x2="{x+90}" y2="46" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 50, 72, alt, LAC, ince=True)
    return svg(420, 104, ic, 'Zekâtın bireyden toplumsal huzura uzanan dört aşamalı etkisi.', 21)


def dort_esnaf_panosu():
    kartlar = [
        (4, 4, 'I. Esnaf', 'Kalibreli tam tartı', YES, YES_A),
        (214, 4, 'II. Esnaf', 'Ezik ürünü alta gizleme', KIR, KIR_A),
        (4, 58, 'III. Esnaf', 'Kusuru açıkça belirtme', MAVI, MAVI_A),
        (214, 58, 'IV. Esnaf', 'Stokçuluktan kaçınma', CAM, CAM_A),
    ]
    ic = ''
    for x, y, bas, alt, r, z in kartlar:
        ic += kutu(x, y, 202, 48, z, r, 7)
        ic += yazi(x + 101, y + 19, bas, r)
        ic += yazi(x + 101, y + 40, alt, LAC, ince=True)
    return svg(420, 110, ic, 'Dört farklı esnaf davranışını karşılaştıran iş ahlakı panosu.', 22)


def ikili_ekonomik_ahlak():
    ic = kutu(4, 4, 200, 96, YES_A, YES, 8)
    ic += yazi(104, 24, '1. Sütun: Hz. Şuayb Kıssası', YES)
    ic += yazi(104, 54, 'Hilesiz ölçü ve tartı', LAC)
    ic += yazi(104, 80, '→ Helal yoldan kazanmak', YES, ince=True)
    ic += kutu(216, 4, 200, 96, MAVI_A, MAVI, 8)
    ic += yazi(316, 24, '2. Sütun: Zekât ve Sadaka', MAVI)
    ic += yazi(316, 54, 'Yoksulun hakkını ödemek', LAC)
    ic += yazi(316, 80, '→ Adaletle paylaşmak', MAVI, ince=True)
    return svg(420, 104, ic, 'İslam ekonomik ahlakında helal kazanç ve adil paylaşım sütunları.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kazanim_dort_kart()
    s[2]['gorsel'] = kaynak_ilkeler_panosu()
    s[5]['gorsel'] = yedi_basak_modeli()
    s[6]['gorsel'] = medyen_terazi_panosu()
    s[7]['gorsel'] = sadaka_tasi_karti()
    s[8]['gorsel'] = sosyal_denge_akisi()
    s[9]['gorsel'] = dort_esnaf_panosu()
    s[11]['gorsel'] = ikili_ekonomik_ahlak()
