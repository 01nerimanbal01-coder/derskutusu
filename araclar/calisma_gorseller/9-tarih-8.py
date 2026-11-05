"""9. sınıf Tarih 8. hafta görselleri (SVG; insan figürü yok K024; K178 beyaz bant yok; max-height:24mm)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'
STIL = 'width:100%;max-height:24mm;display:block;margin:1mm auto;'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="{STIL}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 77, a, c, 5, 0.75)
        ic += yazi(x + 40, 46, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="54" x2="{x + 72}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 90, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, c1)
    ic += kutu(12, 28, 162, 77, a1, c1, 6, 0.75)
    ic += yazi(93, 46, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="54" x2="164" y2="54" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 72, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 91, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 28, 162, 77, a2, c2, 6, 0.75)
    ic += yazi(267, 46, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="54" x2="338" y2="54" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 72, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 91, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 77, a, c, 6, 0.75)
        ic += yazi(x + 54, 46, b, 8.6, c)
        ic += f'<line x1="{x + 10}" y1="54" x2="{x + 98}" y2="54" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 72, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 91, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 9.8, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 8 + i * 87
        ic += kutu(x, 28, 79, 77, a, c, 5, 0.75)
        ic += yazi(x + 39.5, 46, b, 8.2, c)
        ic += yazi(x + 39.5, 70, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39.5, 89, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ox = x + 80.5
            ic += f'<polygon points="{ox:.1f},62 {ox+5:.1f},66.5 {ox:.1f},71" fill="{ana_renk}"/>'
    return svg(ic, etiket)

def g0():
    return kart4('DİJİTAL TARİHÇİLİK KAVRAMLARI VE ARAÇLARI', [
        ('Sonradan Dijital', 'Taranmış ferman', 've tahrir defteri'),
        ('Doğuştan Dijital', 'E-posta, web sitesi', 'Sosyal medya kaydı'),
        ('OCR & HTR', 'Optik ve el yazısı', 'metin çözümleme'),
        ('H-GIS & 3B', 'Tarihsel CBS harita', 'Sanal müze modeli')
    ], '9-tarih-8 dijital kavramlar')

def g1():
    return karsilastir2('DİJİTAL KAYNAKLARIN KÖKENİNE GÖRE SINIFLANDIRILMASI',
        'Sonradan Dijitalleştirilmiş (Digitized)', 'Aslı kâğıt, parşömen veya taş olan belgeler', 'Örn: Taranmış Osmanlı arşiv vesikaları, eski gazeteler',
        'Doğuştan Dijital (Born-Digital)', 'Doğrudan dijital ortamda üretilen kayıtlar', 'Örn: Resmî web siteleri, e-postalar, veri tabanları',
        '9-tarih-8 kaynak türleri')

def g2():
    return uclu_sema('BÜYÜK VERİ (BIG DATA) VE DİJİTAL ARŞİVLERİMİZ', [
        ('Dijital Arşivler', 'Cumhurbaşkanlığı Arşivi', 'TTK ve Milli Kütüphane'),
        ('Üst Veri (Metadata)', 'Tarih, yer, yazar', 'Aranabilir etiketleme'),
        ('Büyük Veri Analizi', 'Yüz binlerce sicilin', 'algoritmayla analizi')
    ], '9-tarih-8 büyük veri')

def g3():
    return karsilastir2('DİJİTAL TARİHÇİLİĞİN FIRSATLARI VE RİSKLERİ',
        'Sağladığı Kolaylıklar (Fırsatlar)', 'Saniyeler içinde uzaktan arşiv erişimi', 'H-GIS haritalama ve 3B görselleştirme',
        'Barındırdığı Tehlikeler (Riskler)', 'Dezenformasyon, sahte görsel (deepfake)', 'Veri kaybı ve intihal (etik ihlal) riski',
        '9-tarih-8 fırsat ve risk', YES, YES_A, KIR, KIR_A)

def g5():
    return akis4('ARŞİV BELGESİNİN DİJİTALLEŞTİRİLME VE ANALİZ SÜRECİ', [
        ('1. Sayısallaştırma', 'Yüksek çözünürlüklü', 'belge taraması'),
        ('2. Üst Veri', 'Metadata kimlik', 'etiketi ekleme'),
        ('3. OCR / HTR', 'El yazısını dijital', 'metne dönüştürme'),
        ('4. Veri Tabanı', 'Uzaktan erişim ve', 'Büyük Veri analizi')
    ], '9-tarih-8 dijitalleşme akışı')

def g6():
    return kart4('DİJİTAL KAYNAK TENKİDİ (DOĞRULAMA) ÖLÇÜTLERİ', [
        ('Kurumsal Uzantı', '.gov.tr ve .edu.tr', 'Resmî/akademik site'),
        ('Birincil Kaynak', 'Arşiv belgesine', 'açık atıf kontrolü'),
        ('Çapraz Doğrulama', 'Farklı bağımsız', 'kaynaklarla kıyas'),
        ('Yazar & Etik', 'Uzmanlık denetimi', 'Eksiksiz kaynakça')
    ], '9-tarih-8 dijital tenkit')

def g7():
    return karsilastir2('DİJİTAL KORUMA VE ARAŞTIRMA ETİĞİ İLKELERİ',
        'Dijital Karanlık Çağ Riskine Karşı', 'Eskiyen formatları güncel tutmak', 'Kurumsal yedekleme ve arşiv standartları',
        'Akademik Etik ve Telif Hakları', 'İntihalden (bilgi hırsızlığı) kaçınmak', 'Dijital kaynakları ve erişim tarihini belirtmek',
        '9-tarih-8 koruma ve etik', MOR, MOR_A, CAM, CAM_A)

def g10():
    return karsilastir2('OCR VE HTR YAZILIMLARININ TARİHÇİYE KATKISI',
        'OCR (Optik Karakter Tanıma)', 'Matbu (basılı) kitap ve eski gazeteleri', 'saniyeler içinde aranabilir metne çevirir',
        'HTR (El Yazısı Tanıma Teknolojisi)', 'Osmanlıca rika/divani el yazması belgeleri', 'çözümleyerek dijital taramaya açar',
        '9-tarih-8 OCR ve HTR', MAVI, MAVI_A, TUR, TUR_A)

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[10]['gorsel'] = g10()
