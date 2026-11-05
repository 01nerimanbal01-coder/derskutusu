"""11. sınıf Kimya 7. hafta görselleri (SVG; insan figürü yok; K178 beyaz bant yok; en_fazla=34)."""
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
    return cizelge4([('Etkin Çarpışma', 'Uygun yön + Yeterli enerji', MAVI, MAVI_A), ('Aktifleşmiş Komp.', 'Tepe noktası kararsız hâl', TUR, TUR_A), ('Eai = PEAK - PEg', 'İleri aktivasyon enerjisi', YES, YES_A), ('ΔH = Eai - Eag', 'Tepkime entalpisi bağıntısı', MOR, MOR_A)], 'Çarpışma teorisi ve PE kavramları')
def g1():
    return ikili('POTANSİYEL ENERJİ (PE) DİYAGRAMI HESAPLAMASI', 'PE(Giren) = 20 kJ · PE(AK) = 95 kJ', 'Eai = 95 - 20 = 75 kJ', 'PE(Ürün) = 45 kJ (Endotermik)', 'Eag = 95 - 45 = 50 kJ · ΔH = +25 kJ', MAVI, MAVI_A, TUR, TUR_A, 'Potansiyel enerji diyagramı sayısal analizi')
def g2():
    return kart('ETKİN ÇARPIŞMANIN İKİ ZORUNLU KOŞULU', '1) Çarpışan tanecikler uygun geometrik doğrultu ve yönde çarpışmalıdır.', '2) Tanecikler aktivasyon enerjisini (Ea) aşacak yeterli kinetik enerjiye sahip olmalıdır.', YES, YES_A, 'Etkin çarpışma şartları')
def g3():
    return cizelge4([('Ea > 0', 'Daima pozitif değerdir', MAVI, MAVI_A), ('Sıcaklık Artışı', 'Ea değerini değiştirmez', TUR, TUR_A), ('Ekzotermik (ΔH<0)', 'Eag > Eai bağıntısı', YES, YES_A), ('Katalizör Etkisi', 'Ea engelini düşürür', MOR, MOR_A)], 'Aktivasyon enerjisi temel özellikleri')
def g5():
    return akis4([('1. Çarpışma', 'Uygun yön ve KE >= Ea', YES, YES_A), ('2. Bağ Zayıflaması', 'KE -> PE dönüşümü', MAVI, MAVI_A), ('3. Tepe Noktası', 'Aktifleşmiş kompleks', TUR, TUR_A), ('4. Ürün Oluşumu', 'Yeni bağlar (2HCl)', MOR, MOR_A)], 'Kimyasal tepkimenin gerçekleşme basamakları')
def g6():
    return ikili('AKTİVASYON ENERJİSİ (Eai) VE TEPKİME HIZI İLİŞKİSİ', 'Eşik Enerjileri Karşılaştırması', 'Eai,1 = 45 kJ < Eai,2 = 70 kJ < Eai,3 = 115 kJ', 'Kural: Ea Küçüldükçe Hız Artar', 'Tepkime Hızları: r1 > r2 > r3', CAM, CAM_A, YES, YES_A, 'Aktivasyon enerjisi ve hız sıralaması')
def g7():
    return kart('TEPKİME HIZI, ENDOTERMİK GRAFİK VE KATALİZÖR', 'Tepkime hızı birim zamandaki etkin çarpışma sayısıyla doğru orantılıdır.', 'Endotermikte PE(ürün) > PE(giren) olur; Ea değerini yalnız katalizör düşürür.', TUR, TUR_A, 'Etkin çarpışma ve katalizör özeti')
def g8():
    return cizelge4([('PEAK - PEgiren', 'İleri eşik enerjisi (Eai)', MAVI, MAVI_A), ('PEAK - PEürün', 'Geri eşik enerjisi (Eag)', TUR, TUR_A), ('Eai > Eag', 'Endotermik (ΔH > 0)', KIR, KIR_A), ('Eai < Eag', 'Ekzotermik (ΔH < 0)', YES, YES_A)], 'PE diyagramı enerji farkları')

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
