"""11. sınıf Türk Dili ve Edebiyatı 2. hafta görselleri.
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


def metin_cozumleme_kartlari():
    kartlar = [
        ('1. Karagöz Oyunu', 'Gölge &amp; Çatışma', TUR, TUR_A),
        ('2. Edebi Mektup', 'Samimi Fikir Bağı', YES, YES_A),
        ('3. Resmi Dilekçe', 'Yasal Talep Dili', MAVI, MAVI_A),
        ('4. Fiilimsiler', 'Cümle Bağdaşıklığı', MOR, MOR_A),
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
    return svg(360, 125, ic, 'Metin türleri çözümleme kartı.', 34)

def yazici_diyalog_mizahi():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 22, 'YAZICI FASLI: DİLSEL ÇATIŞMA VE NÜKTE MODELİ', 10.3, TUR)
    ic += kutu(20, 36, 145, 70, '#ffffff', TUR)
    ic += yazi(92, 56, 'Hacivat (Süslü Dil)', 9.4, TUR)
    ic += yazi(92, 76, 'Tahrirat-ı umumiyeyi', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'tanzim edelim...', 8.8, TUR, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Karagöz (Halk Sağduyusu)', 9.4, YESIL_K)
    ic += yazi(267, 76, 'Bakkal Tahir\'in un çuvalını', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'mı delelim? (Söz Oyunu)', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Yazıcı faslı diyalog mizahı modeli.', 34)

def muhavere_bolum_semasi():
    ic = kutu(6, 6, 348, 112, CAM_A, CAM)
    ic += yazi(180, 20, 'KARAGÖZ VE HACİVAT MUHAVERE (ATIŞMA) PLANI', 10.2, CAM)
    ic += kutu(20, 36, 145, 70, '#ffffff', CAM)
    ic += yazi(92, 56, 'Söz Cambazlığı', 9.6, CAM)
    ic += yazi(92, 76, 'Tekerleme &amp; ters anlama', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'Asıl olaydan bağımsız', 8.8, CAM, ince=True)

    ic += kutu(195, 36, 145, 70, MOR_A, MOR)
    ic += yazi(267, 56, 'Karakter Zıtlığı', 9.6, MOR)
    ic += yazi(267, 76, 'Aydın vs. Halk tipi', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Fasıla geçiş köprüsü', 8.8, MOR, ince=True)
    return svg(360, 125, ic, 'Muhavere bölümü planı şeması.', 34)

def tip_ozellikleri_diagrami():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 22, 'GÖLGE OYUNU TEMEL TİPLERİ VE TABAKALARI', 10.3, YESIL_K)
    ic += kutu(20, 38, 95, 68, '#ffffff', TUR)
    ic += yazi(67, 58, 'Çelebi', 9.4, TUR)
    ic += yazi(67, 78, 'Kibar Mirasyedi', 8.8, LAC, ince=True)
    ic += yazi(67, 92, 'İstanbul Şivesi', 8.8, TUR, ince=True)

    ic += kutu(132, 38, 95, 68, '#ffffff', KIR)
    ic += yazi(179, 58, 'Tuzsuz Bekir', 9.4, KIR)
    ic += yazi(179, 78, 'Kabadayı Külhan', 8.8, LAC, ince=True)
    ic += yazi(179, 92, 'Kaba Kuvvet', 8.8, KIR, ince=True)

    ic += kutu(245, 38, 95, 68, '#ffffff', MAVI)
    ic += yazi(292, 58, 'Beberuhi', 9.4, MAVI)
    ic += yazi(292, 78, 'Cüce &amp; Yaygaracı', 8.8, LAC, ince=True)
    ic += yazi(292, 92, 'Sokağın Dili', 8.8, MAVI, ince=True)
    return svg(360, 125, ic, 'Karagöz tipleri özellikleri şeması.', 34)

def tiplerin_perde_sirasi():
    ic = kutu(6, 6, 348, 112, MOR_A, MOR)
    ic += yazi(180, 20, 'GÖLGE OYUNU SAHNE VE PERDE SIRASI', 10.2, MOR)
    adımlar = [
        ('1. Hacivat', 'Semai &amp; Gazel', 16),
        ('2. Karagöz', 'Muhavere Atışma', 102),
        ('3. Tipler', 'Fasıl Çatışması', 188),
        ('4. Kapanış', 'Bitiş &amp; Af', 274),
    ]
    for b, d, x in adımlar:
        ic += kutu(x, 36, 70, 70, '#ffffff', MOR)
        ic += yazi(x + 35, 56, b, 9.3, MOR)
        ic += f'<line x1="{x + 6}" y1="64" x2="{x + 64}" y2="64" stroke="{MOR}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 84, d, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Tiplerin sahne akış sırası şeması.', 34)

def fiilimsi_baglantisi_kroki():
    ic = kutu(6, 6, 348, 112, MAVI_A, MAVI)
    ic += yazi(180, 22, 'CÜMLEDE FİİLİMSİ TÜRLERİ VE BAĞLANTI İŞLEVİ', 10.3, MAVI)
    ic += kutu(20, 36, 145, 70, '#ffffff', MAVI)
    ic += yazi(92, 56, 'Sıfat-Fiil (Ortaç)', 9.4, MAVI)
    ic += yazi(92, 76, '«yansıyan tasvirler»', 8.8, LAC, ince=True)
    ic += yazi(92, 92, 'İsmi niteleme işlevi', 8.8, MAVI, ince=True)

    ic += kutu(195, 36, 145, 70, YES_A, YES)
    ic += yazi(267, 56, 'Zarf-Fiil (Ulaç)', 9.4, YESIL_K)
    ic += yazi(267, 76, '«oynatarak güldürdü»', 8.8, LAC, ince=True)
    ic += yazi(267, 92, 'Durum bildiren bağlama', 8.8, YESIL_K, ince=True)
    return svg(360, 125, ic, 'Fiilimsi türleri ve işlevleri şeması.', 34)

def karagoz_tip_kartlari():
    ic = kutu(6, 6, 348, 112, YES_A, YES)
    ic += yazi(180, 20, 'KARAGÖZ OYUNU TİP VE TOPLUMSAL ROLLERİ', 10.1, YESIL_K)
    kartlar = [
        ('Hacivat', 'Aydın &amp; Süslü Dil', 16),
        ('Karagöz', 'Halk Sağduyusu', 102),
        ('Çelebi', 'Kibar Mirasyedi', 188),
        ('Tuzsuz Bekir', 'Kabadayı Külhan', 274),
    ]
    for s, snc, x in kartlar:
        ic += kutu(x, 34, 70, 72, '#ffffff', YESIL_K)
        ic += yazi(x + 35, 54, s, 8.8, YESIL_K)
        ic += f'<line x1="{x + 6}" y1="62" x2="{x + 64}" y2="62" stroke="{YESIL_K}" stroke-width="0.75"/>'
        ic += yazi(x + 35, 82, snc, 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Karagöz tipleri kartı.', 34)

def metin_sifre_kutulari():
    ic = kutu(6, 6, 348, 112, TUR_A, TUR)
    ic += yazi(180, 24, 'ŞİFRE KAVRAMI BULMA KUTULARI', 10.4, TUR)
    harfler = ['M', 'E', 'T', 'İ', 'N']
    for i, h in enumerate(harfler):
        x = 55 + i * 52
        ic += kutu(x, 42, 44, 52, '#ffffff', TUR, r=4)
        ic += yazi(x + 22, 74, h, 16.0, TUR)
        ic += yazi(x + 22, 36, f'{i + 1}. Harf', 8.4, LAC, ince=True)
    return svg(360, 125, ic, 'Metin kavramı şifre kutuları.', 34)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = metin_cozumleme_kartlari()
    s[0]['en_fazla'] = 34
    s[1]['gorsel'] = yazici_diyalog_mizahi()
    s[1]['en_fazla'] = 34
    s[2]['gorsel'] = muhavere_bolum_semasi()
    s[2]['en_fazla'] = 34
    s[3]['gorsel'] = tip_ozellikleri_diagrami()
    s[3]['en_fazla'] = 34
    s[5]['gorsel'] = tiplerin_perde_sirasi()
    s[5]['en_fazla'] = 34
    s[6]['gorsel'] = fiilimsi_baglantisi_kroki()
    s[6]['en_fazla'] = 34
    s[8]['gorsel'] = karagoz_tip_kartlari()
    s[8]['en_fazla'] = 34
    s[10]['gorsel'] = metin_sifre_kutulari()
    s[10]['en_fazla'] = 34
