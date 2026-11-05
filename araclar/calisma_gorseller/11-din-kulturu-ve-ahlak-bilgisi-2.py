"""11. sınıf Din Kültürü 2. hafta görselleri.
SVG; insan figürü yok (K024); görsel içi yazı Noto Sans; max-height:34mm; çizgiler <=0.75pt."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def sunnetullah_kartlari():
    kartlar = [
        ('1. Sünnetullah', 'Evrensel Yasalar', YES, YES_A),
        ('2. Cüzi İrade', 'Özgür Tercih Gücü', MAVI, MAVI_A),
        ('3. Mükellef', 'Akıl ve Sorumluluk', TUR, TUR_A),
        ('4. Tevekkül', 'Emek ve Güven', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, oz, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 8, 82, 108, z, r)
        ic += kutu(x + 8, 16, 66, 26, r, r, r=4)
        ic += yazi(x + 41, 33, str(i + 1), 12.0, '#ffffff')
        ic += yazi(x + 41, 62, ad, 9.1, r)
        ic += f'<line x1="{x + 8}" y1="72" x2="{x + 74}" y2="72" stroke="{r}" stroke-width="0.75"/>'
        ic += yazi(x + 41, 92, oz, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Sünnetullah ve mükellefiyet kavramları kartı.', 34)

def yanlis_kader_karsilastirma():
    ic = kutu(6, 6, 348, 112, KIR_A, KIR)
    ic += yazi(180, 22, 'DOĞRU KADER ANLAYIŞI VE HATALI YAKLAŞIM', 10.3, KIR)
    ic += kutu(20, 36, 145, 70, '#ffffff', KIR)
    ic += yazi(92, 56, 'Hatalı Anlayış (Cebriye)', 9.4, KIR)
    ic += yazi(92, 76, 'Kader mahkûmuyum bahanesi', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Tedbirsizlik &amp; İhmal', 8.8, KIR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'İslami Kader İnancı', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Akıl, irade ve tam sorumluluk', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Tedbir + Emek + Tevekkül', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Kader anlayışı karşılaştırma modeli.', 34)

def adalet_terazisi_semasi():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'MÜKELLEFİYETİN İKİ TEMEL ZİHİNSEL DİREĞİ', 10.3, YESIL_K)
    ic += kutu(20, 36, 145, 70, '#ffffff', YES)
    ic += yazi(92, 56, '1. Akıl Sahibi Olmak', 9.6, YESIL_K)
    ic += yazi(92, 76, 'İyi ve kötüyü kavrama', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Dini hitabı anlama şartı', 8.8, YESIL_K, ince=True)

    ic += kutu(195, 36, 145, 70, MAVI_A, MAVI)
    ic += yazi(267, 56, '2. Cüzi İrade Hürriyeti', 9.6, MAVI)
    ic += yazi(267, 76, 'Özgürce karar ve seçim gücü', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Ahlaki mesuliyetin kaynağı', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Mükellefiyet şartları akıl ve irade kartı.', 34)

def ilahi_sifatlar_ve_insan():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'İLAHİ SIFATLAR VE KULUN İRADESİ DENGESİ', 10.3, TUR)
    ic += kutu(20, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(67, 58, 'İlim Sıfatı', 9.4, TUR)
    ic += yazi(67, 78, 'Geçmişi &amp; Geleceği', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Ezelî Bilme', 8.8, TUR, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', YES)
    ic += yazi(179, 58, 'İrade Sıfatı', 9.4, YESIL_K)
    ic += yazi(179, 78, 'Külli Dileme', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Evrensel Ölçü', 8.8, YESIL_K, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', MAVI)
    ic += yazi(292, 58, 'Kudret Sıfatı', 9.4, MAVI)
    ic += yazi(292, 78, 'Mutlak Güç', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Yaratma Yetisi', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'İlim, irade ve kudret sıfatları şeması.', 34)

def eylem_sorumluluk_basamaklari():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'İNSANIN AHLAKİ EYLEM VE MESULİYET ADIMLARI', 10.2, CAM)
    adımlar = [
        ('1. Bilgi', 'Akılla Ayırt Etme', 16),
        ('2. Tercih', 'İradeyle Seçim', 102),
        ('3. Fiil', 'Eyleme Dökme', 188),
        ('4. Mesuliyet', 'Hesap Verme', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', CAM)
        ic += yazi(x + 35, 56, b, 9.3, CAM)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{CAM}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.2, LAC, ince=True)
    return svg(360, 125, ic, 'Ahlaki eylem basamakları şeması.', 34)

def uc_ilahi_sifat_semasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 22, 'ALLAH\'IN EVRENİ KUŞATAN ÜÇ TEMEL SIFATI', 10.3, MOR)
    ic += kutu(20, 36, 95, 70, '#ffffff', MOR)
    ic += yazi(67, 56, '1. İlim', 9.6, MOR)
    ic += yazi(67, 76, 'Kuşatıcı Bilgi', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'Zorlama içermez', 8.8, MOR, ince=True)

    ic += kutu(132, 36, 95, 70, '#ffffff', TUR)
    ic += yazi(179, 56, '2. İrade', 9.6, TUR)
    ic += yazi(179, 76, 'Külli Takdir', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Kural Koyucu', 8.8, TUR, ince=True)

    ic += kutu(245, 36, 95, 70, '#ffffff', YESIL_K)
    ic += yazi(292, 56, '3. Kudret', 9.6, YESIL_K)
    ic += yazi(292, 76, 'Sonsuz Güç', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Var Eden Kudret', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'İlim, irade ve kudret kavramları kartı.', 34)

def ahlaki_kavramlar_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'İNSANIN TERCİH ALANI: HAYIR VE ŞER', 10.1, YESIL_K)
    kartlar = [
        ('Hidayet', 'Hak Yolu Seçme', 16),
        ('Dalalet', 'Haktan Sapma', 102),
        ('Hayır', 'Faydalı İyilik', 188),
        ('Şer', 'Zararlı Kötülük', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Ahlaki kavramlar eşleştirme kartı.', 34)

def irade_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, MAVI)
    harfler = ['İ', 'R', 'A', 'D', 'E']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', MAVI, r=4)
        ic += yazi(x + 22, 74, h, 16.0, MAVI)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'İrade kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = sunnetullah_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = yanlis_kader_karsilastirma()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = adalet_terazisi_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = ilahi_sifatlar_ve_insan()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = eylem_sorumluluk_basamaklari()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = uc_ilahi_sifat_semasi()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = ahlaki_kavramlar_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = irade_sifre_kutulari()
    s[10]['en_fazla'] = 34
