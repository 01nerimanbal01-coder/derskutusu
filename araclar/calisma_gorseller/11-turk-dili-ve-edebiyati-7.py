"""11. sınıf Türk Dili ve Edebiyatı 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'

def svg(w, h, ic, etiket, en_fazla=34):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'

def yazi(x, y, metin, boy=11, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'

def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'

def cizelge4(elemanlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(elemanlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(adimlar, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.2, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def ikili(baslik, b1, a1, b2, a2, c1, d1, c2, d2, etiket):
    ic = kutu(4, 4, 352, 107, d1, c1) + yazi(180, 24, baslik, 10.2, c1)
    ic += kutu(16, 36, 156, 64, GRI_A, c1) + yazi(94, 56, b1, 9.5, c1) + yazi(94, 78, a1, 8.2, SOLUK, ince=True)
    ic += kutu(188, 36, 156, 64, d2, c2) + yazi(266, 56, b2, 9.5, c2) + yazi(266, 78, a2, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def kart(baslik, s1, s2, c, d, etiket):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, d, c, 8)
    ic += yazi(180, 32, baslik, 10.2, c) + yazi(180, 58, s1, 9.5, LAC) + yazi(180, 82, s2, 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return cizelge4([('Çok Modlu Metin', 'Yazı + Ses + Görüntü', MAVI, MAVI_A), ('Özel Mektup', 'Samimi ve içten üslup', YES, YES_A), ('Edebî Mektup', 'Sanat ve fikir paylaşımı', TUR, TUR_A), ('Dilekçe', 'Resmî talep ve şikâyet', MOR, MOR_A)], 'Metin ve mektup türleri')
def g1():
    return ikili('RESMÎ DİLEKÇEDE SAYFA YERLEŞİM DÜZENİ', 'Sol Alt Köşe Unsurları', 'Açık Adres, Telefon ve Ekler', 'Sağ Alt Köşe Unsurları', 'Tarih, İmza ve Ad-Soyad', MAVI, MAVI_A, YES, YES_A, 'Dilekçede sağ alt ve sol alt yerleşimi')
def g2():
    return kart('RESMÎ YAZIŞMALARDA ARZ VE RİCA KURALI', 'Vatandaştan resmî makama veya alt makamdan üst makama: Gereğini arz ederim.', 'Üst makamdan alt makama yazılan talimat yazılarında: Gereğini rica ederim.', TUR, TUR_A, 'Arz ederim ve rica ederim farkı')
def g3():
    return cizelge4([('Örtük İleti', 'Sembol ve tondan çıkarım', MAVI, MAVI_A), ('Âli’ye Mektuplar', 'Mehmet Kaplan (Edebî)', YES, YES_A), ('Zorunlu Unsurlar', 'Ad, imza ve açık adres', TUR, TUR_A), ('Kurumsal E-Posta', 'Net konu ve resmî dil', MOR, MOR_A)], 'Çok modlu metin, dilekçe ve e-posta ilkeleri')
def g5():
    return akis4([('1. Makam Adı', 'Üst ortaya büyük harfle', YES, YES_A), ('2. Gövde Metni', 'Kısa talep + Arz ederim', MAVI, MAVI_A), ('3. Sağ Alt Köşe', 'Tarih, İmza ve Ad-Soyad', TUR, TUR_A), ('4. Sol Alt Köşe', 'Açık Adres, Tel ve Ekler', MOR, MOR_A)], 'Dilekçe yazım ve yerleşim sırası')
def g6():
    return ikili('EDEBÎ MEKTUP ÖRNEKLERİ VE MAZİ KORİDORU', 'Nurullah Ataç', 'Okuruma Mektuplar (Deneme-Mektup)', 'Mehmet Kaplan (Âli’ye Mektuplar)', 'Karamazof Kardeşler -> Mazi Koridoru', CAM, CAM_A, MOR, MOR_A, 'Türk edebiyatında edebi mektup örnekleri')
def g7():
    return kart('AÇIK İLETİ, 3071 SAYILI KANUN VE EDEBÎ MEKTUP', 'Doğrudan anlatılan mesaja açık ileti denir; dilekçeye 30 gün içinde cevap verilir.', 'Nurullah Ataç’ın Okuruma Mektuplar eseri edebî mektup türünün önemli örneğidir.', YES, YES_A, 'Açık ileti ve 3071 sayılı dilekçe kanunu')
def g8():
    return cizelge4([('Üst Orta', 'Kurum ve şehir başlığı', MAVI, MAVI_A), ('Sağ Üst (Mektup)', 'Yer ve tarih bilgisi', TUR, TUR_A), ('Sağ Alt (Dilekçe)', 'Tarih, imza ve ad-soyad', YES, YES_A), ('Sol Alt (Dilekçe)', 'Adres, iletişim ve ekler', MOR, MOR_A)], 'Mektup ve dilekçede sayfa konumları')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
