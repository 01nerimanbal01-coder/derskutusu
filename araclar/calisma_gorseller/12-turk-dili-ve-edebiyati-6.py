"""12. sınıf Türk Dili ve Edebiyatı 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def kart4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (b, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.8, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.2, LAC, ince=True)
    return svg(360, 115, ic, etiket, 34)

def akis4(etiket, veri):
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    for i, (bas, alt, c, d) in enumerate(veri):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.8, c) + yazi(x + 40, 68, alt, 8.2, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, etiket, 34)

def pano(etiket, baslik, s1, s2, c=MAVI, d=MAVI_A, ic_d='#f4f8fe'):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    ic += kutu(16, 36, 328, 64, ic_d, c) + yazi(180, 58, s1, 9.8, LAC) + yazi(180, 82, s2, 8.8, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def uclu(etiket, baslik, k1, k2, k3, c=MAVI, d=MAVI_A):
    ic = kutu(4, 4, 352, 107, d, c) + yazi(180, 24, baslik, 10.2, c)
    for i, (b, alt, kc, kd) in enumerate([k1, k2, k3]):
        x = 16 + i * 112
        ic += kutu(x, 36, 104, 64, kd, kc) + yazi(x + 52, 56, b, 9.8, kc) + yazi(x + 52, 78, alt, 8.2, SOLUK, ince=True)
    return svg(360, 115, ic, etiket, 34)

def g0():
    return kart4('Kelimede anlam katmanları ve aktarmalar', [('Yan Anlam', 'Çekmecenin gözü', MAVI, MAVI_A), ('Ad Aktarması', 'Sait Faik’i okumak', TUR, TUR_A), ('Duyular Arası', 'Acı bir fren sesi', YES, YES_A), ('Terim Anlam', 'Bilinç akışı tekniği', MOR, MOR_A)])

def g1():
    return uclu('Birleşik fiillerin yazım kuralları', 'HİKÂYE METİNLERİNDE BİRLEŞİK FİİLLERİN YAZIMI', ('Ses Olayı Varsa', 'hissetmek, kaybolmak', YES, YES_A), ('Ses Olayı Yoksa', 'fark etmek, terk etmek', MAVI, MAVI_A), ('Kurallı Birleşikler', 'uyuyuverdi, dinleyekaldı', TUR, TUR_A), MAVI, MAVI_A)

def g2():
    return pano('Zarf-fiil eklerinden sonra virgül kuralı', 'NOKTALAMA UYARISI · ZARF-FİİL EKLERİ VE VİRGÜL KULLANIMI', 'Tek başına kullanılan zarf-fiil eklerinden (-ıp, -arak, -ınca, -madan) sonra VİRGÜL KONMAZ!', 'Örnek: "Kapıyı yavaşça açıp içeriye doğru bir adım attı." (Virgülsüz doğru kullanım)', KIR, KIR_A, '#fde8e7')

def g3():
    return kart4('Somutlaştırma, diyalog ve tırnak kuralları', [('Somutlaştırma', 'Soyutu somut kılma', YES, YES_A), ('Konuşma Çizgisi', 'Tırnakla kullanılmaz', KIR, KIR_A), ('Kaydolmak', 'Ünlü düşmesi -> Bitişik', MAVI, MAVI_A), ('Tırnak İçi Nokta', 'Tırnak içine konur', TUR, TUR_A)])

def g5():
    return akis4('Hikâye diyaloglarında noktalama sırası', [('1. İki Nokta (:)', 'seslendi (:) açıklama', MAVI, MAVI_A), ('2. Uzun Çizgi (—)', '(—) Bana kahve getir', TUR, TUR_A), ('3. Virgül (,)', 'getir evlat (,) dedi', YES, YES_A), ('4. Nokta (.)', 'dedi (.) cümle sonu', MOR, MOR_A)])

def g6():
    return pano('Kişileştirme ve ad aktarması mecazımürsel analizi', 'HİKÂYE CÜMLESİNDE ANLAM OLAYLARI ANALİZİ', '"Hırçın bir rüzgâr lambaları dövüyor" -> İnsandan Doğaya Aktarma (Kişileştirme)', '"Sobanın üstündeki çaydanlık kaynıyordu" -> İç-Dış İlişkisiyle Ad Aktarması (Mecazımürsel)', CAM, CAM_A, '#eaf7fa')

def g7():
    return pano('Bağlam, ayrı yazılan yardımcı fiil ve kişileştirme', 'BAĞLAM, YARDIMCI FİİL İMLASI VE TEŞHİS SANATI', 'Bağlam (Metin Bütünlüğü)  ·  Ses Olayı Yoksa Ayrı Yazım  ·  Kişileştirme (Teşhis)', 'Sözcükler hikâye içinde bağlama göre yeni mecaz ve çağrışım değerleri kazanır.', YES, YES_A, '#eaf8f0')

def g8():
    return kart4('Birleşik fiillerin bitişik ve ayrı yazımı', [('Ünsüz Türemesi', 'hissetmek, reddetmek', YES, YES_A), ('Ünlü Düşmesi', 'sabretmek, kaybolmak', MAVI, MAVI_A), ('Ses Olayı Yok', 'terk etmek, arz etmek', TUR, TUR_A), ('Kurallı Fiiller', 'bakakalmak (Bitişik)', MOR, MOR_A)])

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
