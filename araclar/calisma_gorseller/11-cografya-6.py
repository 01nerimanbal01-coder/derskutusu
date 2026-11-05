"""11. sınıf Coğrafya 6. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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

def g0():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    kaynaklar = [('Akifer', 'Geçirgen su tabakası', MAVI, MAVI_A), ('Voklüz', 'Karstik soğuk kaynak', YES, YES_A), ('Artezyen', 'Sondajlı basınçlı su', TUR, TUR_A), ('Fay Kaynağı', 'Kırık hattı sıcak su', KIR, KIR_A)]
    for i, (b, alt, c, d) in enumerate(kaynaklar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Yer altı su kaynakları sınıflandırma kartı', 34)

def g1():
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI) + yazi(180, 24, 'DÜNYA TATLI SU KAYNAKLARININ ORANSAL DAĞILIMI (%2,5)', 10, MAVI)
    ic += kutu(16, 36, 104, 64, '#f4f8fe', MAVI) + yazi(68, 56, 'Buzullar: %68,7', 10, MAVI) + yazi(68, 78, 'Kutup ve yüksek dağ', 8.5, SOLUK, ince=True)
    ic += kutu(128, 36, 104, 64, YES_A, YES) + yazi(180, 56, 'Yer Altı Suyu: %30,1', 9.5, YES) + yazi(180, 78, 'Akifer hazneleri', 8.5, SOLUK, ince=True)
    ic += kutu(240, 36, 104, 64, TUR_A, TUR) + yazi(292, 56, 'Yüzey Suları: %1,2', 9.5, TUR) + yazi(292, 78, 'Göl, akarsu, bataklık', 8.5, SOLUK, ince=True)
    return svg(360, 115, ic, 'Dünya tatlı su oranları grafiği', 34)

def g2():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI) + kutu(12, 12, 336, 91, KIR_A, KIR, 8)
    ic += yazi(180, 32, 'JEOTERMAL KAYNAKLAR: FAY KAYNAĞI VE GAYZER FARKI', 10, KIR)
    ic += yazi(180, 58, 'Türkiye genç kırıklı (faylı) yapıda olduğundan fay kaynakları yaygındır.', 9.5, LAC)
    ic += yazi(180, 82, 'Aktif volkanizma bulunmadığı için Türkiye\'de gayzer kaynağı görülmez.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Fay kaynağı ve gayzer karşılaştırma kartı', 34)

def g3():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    bilgiler = [('Tatlı Göl', 'Gideğeni (ayağı) var', MAVI, MAVI_A), ('Tuzlu Göl', 'Kapalı havza gölü', TUR, TUR_A), ('İç Deniz', 'Boğazla bağlı deniz', YES, YES_A), ('Buffer Analizi', 'CBS koruma kuşağı', MOR, MOR_A)]
    for i, (b, alt, c, d) in enumerate(bilgiler):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, alt, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Göl kimyası ve CBS temel kavramları', 34)

def g5():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    adimlar = [('1. Veri Girişi', 'Raster + Vektör', YES, YES_A), ('2. Çakıştırma', 'Yıllık alan kaybı', MAVI, MAVI_A), ('3. Buffer', 'Koruma kuşağı', TUR, TUR_A), ('4. Paylaşım', 'Web tematik harita', MOR, MOR_A)]
    for i, (bas, alt, c, d) in enumerate(adimlar):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, bas, 9.5, c) + yazi(x + 40, 68, alt, 8.5, LAC, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+82},56 {x+85},52 {x+85},60" fill="{GRI}"/>'
    return svg(360, 115, ic, 'Web CBS su yönetimi uygulama akışı', 34)

def g6():
    ic = kutu(4, 4, 352, 107, CAM_A, CAM) + yazi(180, 26, 'WEB TABANLI CBS VEKTÖR VERİ KATMANLARI', 10.5, CAM)
    ic += kutu(20, 38, 320, 62, '#eaf7fa', CAM) + yazi(180, 60, 'Poligon (Alan): Göl/Havza · Çizgi (Hat): Akarsu · Nokta: Su Kuyusu', 9.5, LAC) + yazi(180, 84, 'Mekânsal unsurlar geometrik boyutlarına göre katmanlara ayrılır.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Web CBS vektör veri modelleri', 34)

def g7():
    ic = kutu(4, 4, 352, 107, YES_A, YES) + yazi(180, 24, 'AKARSU HİDROLOJİSİ VE RASTER VERİ MODELİ', 10.5, YES)
    ic += kutu(16, 36, 328, 64, '#eaf8f0', YES) + yazi(180, 58, 'Debi (Akım: m³/sn)  ·  Kapalı Havza  ·  Raster (Piksel Uydu Verisi)', 9.5, LAC) + yazi(180, 82, 'Denize ulaşamayan akarsular kapalı havza oluşturur.', 9, SOLUK, ince=True)
    return svg(360, 115, ic, 'Akarsu kavramları ve raster veri kartı', 34)

def g8():
    ic = kutu(4, 4, 352, 107, GRI_A, GRI)
    su = [('Pasifik', 'En büyük okyanus', MAVI, MAVI_A), ('Kenar Deniz', 'Okyanus kıyısında', TUR, TUR_A), ('Düzenli Rejim', 'Yıl boyu dengeli', YES, YES_A), ('Lav Set Gölü', 'Van ve Çıldır Gölü', MOR, MOR_A)]
    for i, (b, tr, c, d) in enumerate(su):
        x = 10 + i * 86
        ic += kutu(x, 12, 80, 90, d, c) + yazi(x + 40, 36, b, 9.5, c) + f'<line x1="{x+8}" y1="48" x2="{x+72}" y2="48" stroke="{c}" stroke-width="0.8"/>' + yazi(x + 40, 72, tr, 8.5, LAC, ince=True)
    return svg(360, 115, ic, 'Okyanus, deniz ve göl türleri özeti', 34)

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
