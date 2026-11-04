"""7. sınıf Din Kültürü ve Ahlak Bilgisi 6. hafta (Ahiret İnancının İnsana Kazandırdıkları) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea'
GRI, CAM, CAM_A = '#9aa6bd', '#0e8fa8', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=21):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}">{metin}</text>'


def zilzal_ayet_levhasi():
    ic = f'<rect x="8" y="6" width="584" height="92" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Zilzâl Suresi 7 ve 8. Ayetler', 12, YES)
    ic += yazi(300, 50, '«Artık kim zerre ağırlığınca bir hayır işlerse onun mükâfatını görecektir.', 12, LAC, ince=True)
    ic += yazi(300, 72, 'Kim de zerre ağırlığınca bir kötülük işlerse onun cezasını görecektir.»', 12, LAC, ince=True)
    ic += yazi(300, 90, 'Zerre (en küçük parça) bile kaybolmaz · Hesap verme bilinci', 12, MAVI)
    return svg(600, 104, ic, 'Zilzal suresi 7-8. ayetler ve hesap verme bilinci levhası.', 20)


def dunya_ahiret_tutum_kartlari():
    kartlar = [
        ('1. Tutum', 'Yalnız Dünya', KIR, KIR_A),
        ('2. Tutum', 'Yalnız Ahiret', TUR, TUR_A),
        ('3. Tutum', 'Dengeli Yaşam', YES, YES_A),
        ('4. Tutum', 'İç Denetim', MAVI, MAVI_A),
    ]
    ic = ''
    for i, (no, ad, renk, arka) in enumerate(kartlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="72" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, no, 12, renk)
        ic += yazi(x + 70, 56, ad, 12, LAC, ince=True)
    return svg(600, 84, ic, 'Dünya ve ahiret dengesiyle ilgili dört tutum kartı.', 19)


def dort_soru_hadis_karti():
    sorular = [
        ('1. Soru · Ömür', 'Zamanını nerede tüketti?', MAVI, MAVI_A),
        ('2. Soru · İlim', 'Bildikleriyle ne yaptı?', YES, YES_A),
        ('3. Soru · Mal', 'Nereden kazanıp harcadı?', TUR, TUR_A),
        ('4. Soru · Beden', 'Sağlığını nerede yıprattı?', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(sorular):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="76" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 30, bas, 12, renk)
        ic += yazi(x + 70, 56, acik, 12, LAC, ince=True)
    return svg(600, 88, ic, 'Kıyamet günü insana sorulacak dört temel soru kartı.', 19)


def adalet_iki_yon_sema():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Haksızlığa Uğrayan İçin', 12, YES)
    ic += yazi(149, 50, 'Hiçbir hak kaybolmaz · Umut verir', 12, LAC, ince=True)
    ic += yazi(149, 74, 'İntikamdan korur · Meşru hak arama', 12, YES)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Haksızlık Yapmayı Düşünen İçin', 12, KIR)
    ic += yazi(451, 50, 'Kimsenin hakkı yanıma kalmaz', 12, LAC, ince=True)
    ic += yazi(451, 74, 'Kötülüğe karşı caydırıcı fren olur', 12, KIR)
    return svg(600, 100, ic, 'Ahiret adaletinin haksızlığa uğrayan ve haksızlık düşünen üzerindeki etkisi.', 20)


def iki_inanc_koprusu():
    ic = f'<rect x="8" y="6" width="180" height="84" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(98, 30, 'Melek İnancı', 12, MAVI)
    ic += yazi(98, 54, 'Kirâmen Kâtibîn', 12, LAC, ince=True)
    ic += yazi(98, 76, '«Kaydediliyor»', 12, MAVI)

    ic += f'<rect x="210" y="6" width="180" height="84" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.6"/>'
    ic += yazi(300, 30, 'Ahiret İnancı', 12, TUR)
    ic += yazi(300, 54, 'Mîzan ve Hesap Günü', 12, LAC, ince=True)
    ic += yazi(300, 76, '«Sorulacak»', 12, TUR)

    ic += f'<rect x="412" y="6" width="180" height="84" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.6"/>'
    ic += yazi(502, 30, 'Ortak Kazanım', 12, YES)
    ic += yazi(502, 54, 'Sağlam İç Denetim', 12, LAC, ince=True)
    ic += yazi(502, 76, '«Ahlaklı Yaşam»', 12, YES)
    return svg(600, 96, ic, 'Melek ve ahiret inancının iç denetim ve ahlaklı yaşama etkisi.', 20)


def ahlaki_karar_adimlari():
    adimlar = [
        ('1. Adım', 'Melek kaydı farkındalığı', MAVI, MAVI_A),
        ('2. Adım', 'Ahiret hesabı bilinci', TUR, TUR_A),
        ('3. Adım', 'İyiliği ve doğruyu seçme', YES, YES_A),
        ('4. Adım', 'Sabır ve iç huzur', MOR, MOR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 8 + i * 148
        ic += f'<rect x="{x}" y="8" width="136" height="68" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.6"/>'
        ic += yazi(x + 68, 32, ust, 12, renk)
        ic += yazi(x + 68, 56, alt, 12, LAC, ince=True)
        if i < 3:
            ic += f'<line x1="{x + 136}" y1="42" x2="{x + 148}" y2="42" stroke="{LAC}" stroke-width="1.8"/>'
    return svg(600, 84, ic, 'Melek ve ahiret bilinciyle dört aşamalı ahlaki karar süreci.', 19)


def taziye_ve_sabir_panosu():
    ic = f'<rect x="8" y="6" width="282" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.6"/>'
    ic += yazi(149, 26, 'Bakara Suresi 156. Ayet', 12, MOR)
    ic += yazi(149, 50, '«Biz şüphesiz Allah’a aidiz ve', 12, LAC, ince=True)
    ic += yazi(149, 72, 'şüphesiz O’na döneceğiz.»', 12, LAC, ince=True)

    ic += f'<rect x="310" y="6" width="282" height="88" rx="9" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.6"/>'
    ic += yazi(451, 26, 'Taziye Kültürümüz ve Teselli', 12, CAM)
    ic += yazi(451, 50, '«Başınız sağ olsun · Allah rahmet eylesin»', 12, LAC, ince=True)
    ic += yazi(451, 72, 'Ölüm yok oluş değil, yeniden buluşma umudu', 12, CAM)
    return svg(600, 100, ic, 'Sabır ayeti ve taziye kültürümüzde ahiret umudu panosu.', 20)


def kasas_denge_levhasi():
    ic = f'<rect x="8" y="6" width="584" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.6"/>'
    ic += yazi(300, 26, 'Kasas Suresi 77. Ayet · Dünya ve Ahiret Dengesi', 12, MAVI)
    ic += yazi(300, 50, '«Allah’ın sana verdiği şeylerde ahiret yurdunu ara. Dünyadan da nasibini unutma.', 12, LAC, ince=True)
    ic += yazi(300, 72, 'Allah’ın sana iyilik yaptığı gibi sen de iyilik yap ve bozgunculuk isteme.»', 12, LAC, ince=True)
    return svg(600, 100, ic, 'Kasas suresi 77. ayet dünya ve ahiret dengesi levhası.', 20)


def durum_davranis_tablosu():
    satirlar = [
        ('1. Gizli fırsat', 'Melekler kaydeder', 'Fırsatı kullanırım (Yanlış)', KIR_A, KIR),
        ('2. Gizli iyilik', 'Zerre kaybolmaz', 'İyiliği bırakırım (Yanlış)', TUR_A, TUR),
        ('3. Haksızlık', 'Adalet ahirettedir', 'Hakkımı meşru ararım (Doğru)', YES_A, YES),
        ('4. Büyük hata', 'Allah affedicidir', 'Ümidimi keserim (Yanlış)', MOR_A, MOR),
    ]
    ic = ''
    for i, (d, b, s, arka, renk) in enumerate(satirlar):
        x = 6 + i * 148
        ic += f'<rect x="{x}" y="6" width="140" height="84" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.5"/>'
        ic += yazi(x + 70, 26, d, 12, renk)
        ic += yazi(x + 70, 50, b, 12, LAC, ince=True)
        ic += yazi(x + 70, 74, s, 12, renk)
    return svg(600, 96, ic, 'Dört farklı durumda melek ve ahiret bilinci davranış kartları.', 20)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = zilzal_ayet_levhasi()
    s[1]['gorsel'] = dunya_ahiret_tutum_kartlari()
    s[3]['gorsel'] = dort_soru_hadis_karti()
    s[4]['gorsel'] = adalet_iki_yon_sema()
    s[6]['gorsel'] = iki_inanc_koprusu()
    s[7]['gorsel'] = ahlaki_karar_adimlari()
    s[8]['gorsel'] = taziye_ve_sabir_panosu()
    s[11]['gorsel'] = kasas_denge_levhasi()
    s[12]['gorsel'] = durum_davranis_tablosu()
