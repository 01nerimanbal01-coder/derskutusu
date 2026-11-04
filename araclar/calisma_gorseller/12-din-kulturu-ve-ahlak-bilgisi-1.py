"""12. sınıf Din Kültürü ve Ahlak Bilgisi 1. hafta (Din ve Bilim İlişkisi) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; metin arkası beyaz bant yok (K178)."""

LAC = '#0b2257'
MAVI = '#2451d6'
MAVI_A = '#e8eefe'
TUR = '#ee7d12'
TUR_A = '#fff1df'
YES = '#12a150'
YES_A = '#e3f6ea'
MOR = '#7c3aed'
MOR_A = '#f0e9fe'
CAM = '#0e8fa8'
CAM_A = '#e0f4f8'
KIR = '#d63a3a'
KIR_A = '#fdeaea'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def dort_kavram_karti():
    kavramlar = [
        ('1. Sünnetullah', 'İlahi Yasalar · Doğa Düzeni', YES, YES_A),
        ('2. Âdetullah', 'Nedensellik · Sebepler Zinciri', MAVI, MAVI_A),
        ('3. Faydalı İlim', 'Ahlaki Gayret · Topluma Hizmet', TUR, TUR_A),
        ('4. Akıl &amp; Tefekkür', 'Delil İnceleme · Sağduyu', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kavramlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' · ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, alt.split(' · ')[1], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel din ve bilim kavram kartı.', 34)


def bilgi_sistemi_semasi():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'İSLAM BİLGİ VE ARAŞTIRMA SİSTEMİ', 10.8, YES)
    # Şema kutuları
    ic += kutu(16, 38, 98, 56, MAVI_A, MAVI)
    ic += yazi(65, 56, 'Varlık &amp; Âlem', 9.8, MAVI)
    ic += yazi(65, 74, 'Gözlem konusu', 9.0, LAC, ince=True)

    ic += kutu(131, 38, 98, 56, TUR_A, TUR)
    ic += yazi(180, 56, 'Akıl &amp; Tefekkür [?]', 9.8, TUR)
    ic += yazi(180, 74, 'Nizamı anlama', 9.0, LAC, ince=True)

    ic += kutu(246, 38, 98, 56, MOR_A, MOR)
    ic += yazi(295, 56, 'Hikmet &amp; Eylem', 9.8, MOR)
    ic += yazi(295, 74, 'Faydalı bilgi', 9.0, LAC, ince=True)
    return svg(360, 110, ic, 'İslam bilgi sistemi ve bilimsel araştırma kavram ağı.', 34)


def faydali_bilgi_karti():
    ic = kutu(6, 6, 170, 98, YES_A, YES)
    ic += yazi(91, 26, 'Faydalı İlim İlkeleri', 10.4, YES)
    ic += yazi(91, 48, 'İnsanlığın huzuruna hizmet', 9.5, LAC, ince=True)
    ic += yazi(91, 66, 'Doğayı ve canlıları koruma', 9.5, LAC, ince=True)
    ic += yazi(91, 84, 'Ahlaki sorumlulukla üretim', 9.5, YES)

    ic += kutu(184, 6, 170, 98, KIR_A, KIR)
    ic += yazi(269, 26, 'Sakınılan Bilgi (Faydasız)', 10.4, KIR)
    ic += yazi(269, 48, 'Yıkıma ve savaşa yol açan', 9.5, LAC, ince=True)
    ic += yazi(269, 66, 'İnsan fıtratını bozan', 9.5, LAC, ince=True)
    ic += yazi(269, 84, 'Kibre ve bencilliğe sevk eden', 9.5, KIR)
    return svg(360, 110, ic, 'Faydalı bilgi ve sakınılan bilgi karşılaştırması.', 34)


def din_bilim_iliskisi_karti():
    ic = kutu(6, 6, 348, 98, CAM_A, CAM)
    ic += yazi(180, 24, 'DİN VE BİLİMİN BÜTÜNLEŞEN BOYUTLARI', 10.6, CAM)
    ic += kutu(20, 36, 150, 58, MAVI_A, MAVI)
    ic += yazi(95, 54, 'Bilimin Alanı: Nasıl?', 10.0, MAVI)
    ic += yazi(95, 74, 'Olayların fiziksel mekanizması', 9.2, LAC, ince=True)

    ic += kutu(190, 36, 150, 58, YES_A, YES)
    ic += yazi(265, 54, 'Dinin Alanı: Niçin?', 10.0, YES)
    ic += yazi(265, 74, 'Yaratılış gayesi &amp; ahlaki değer', 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Din ve bilimin farklı sorulara yanıt arayan bütünlüğü.', 34)


def ilim_basamaklari_akisi():
    adımlar = [
        ('1. Gözlem', 'Evrende nizamı görme', YES, YES_A),
        ('2. Tefekkür', 'Nedenselliği araştırma', TUR, TUR_A),
        ('3. İlim', 'Delilli bilgiye ulaşma', MAVI, MAVI_A),
        ('4. Hizmet', 'Toplumun yararına sunma', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(adımlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.1, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' ')[0], 9.2, LAC, ince=True)
        ic += yazi(x + 41, 78, ' '.join(alt.split(' ')[1:]), 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'İslam medeniyetinde ilim basamakları.', 34)


def zumer_ayet_panosu():
    ic = kutu(6, 6, 348, 98, TUR_A, TUR)
    ic += yazi(180, 24, 'AYET TAHLİLİ · ZÜMER SURESİ, 9. AYET', 10.6, TUR)
    ic += yazi(180, 52, '“De ki: Hiç bilenlerle bilmeyenler bir olur mu?”', 10.2, LAC)
    ic += yazi(180, 76, 'Ana Fikir: İlmin, araştırmanın ve cehaletten uzaklaşmanın değeri', 9.4, TUR, ince=True)
    return svg(360, 110, ic, 'Zümer suresi 9. ayet tahlil panosu.', 34)


def dort_kaynak_karti():
    kaynaklar = [
        ('Alak Suresi', 'İlk vahiy: Oku &amp; Yaz', YES, YES_A),
        ('Zümer Suresi', 'İlmin üstün kıymeti', MAVI, MAVI_A),
        ('Hadis-i Şerif', 'İlim peşinde gayret', TUR, TUR_A),
        ('Tefekkür', 'Evrenden ibret alma', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, alt, r, z) in enumerate(kaynaklar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 96, z, r)
        ic += yazi(x + 41, 28, ad, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="38" x2="{x + 74}" y2="38" stroke="{r}" stroke-width="1"/>'
        ic += yazi(x + 41, 62, alt.split(' &amp; ')[0], 9.2, LAC, ince=True)
    return svg(360, 110, ic, 'Dört temel kaynak ve ilke kartı.', 34)


def sifre_kavram_panosu():
    ic = kutu(6, 6, 348, 98, YES_A, YES)
    ic += yazi(180, 24, 'HİKMET VE AKIL IŞIĞINDA İLİM AĞACI', 10.8, YES)
    ic += yazi(180, 50, 'HAKİKAT · BİLİM · AKIL · İSLAM · EVREN · AYET', 9.8, LAC)
    ic += yazi(180, 76, 'İpuçlarını çözerek gizli kavramı (6 harf) bulunuz.', 9.4, YES, ince=True)
    return svg(360, 110, ic, 'Şifre kavram panosu.', 34)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_kavram_karti()
    s[0]['en_fazla'] = 34
    s[0]['gorsel_var'] = True

    s[1]['gorsel'] = bilgi_sistemi_semasi()
    s[1]['en_fazla'] = 34
    s[1]['gorsel_var'] = True

    s[2]['gorsel'] = faydali_bilgi_karti()
    s[2]['en_fazla'] = 34
    s[2]['gorsel_var'] = True

    s[3]['gorsel'] = din_bilim_iliskisi_karti()
    s[3]['en_fazla'] = 34
    s[3]['gorsel_var'] = True

    s[5]['gorsel'] = ilim_basamaklari_akisi()
    s[5]['en_fazla'] = 34
    s[5]['gorsel_var'] = True

    s[6]['gorsel'] = zumer_ayet_panosu()
    s[6]['en_fazla'] = 34
    s[6]['gorsel_var'] = True

    s[8]['gorsel'] = dort_kaynak_karti()
    s[8]['en_fazla'] = 34
    s[8]['gorsel_var'] = True

    s[10]['gorsel'] = sifre_kavram_panosu()
    s[10]['en_fazla'] = 34
    s[10]['gorsel_var'] = True
