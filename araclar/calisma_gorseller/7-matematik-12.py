"""7. sınıf Matematik 12. hafta (Çizgi, Sütun, Daire Grafiği ile Aritmetik Ortalama, Medyan ve Mod) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178); Noto Sans 12px."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'


def svg(ic, etiket, w=360, h=115, mm=21):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def sicaklik_cizgi_grafigi():
    ic = kutu(6, 6, 348, 103, MAVI_A, MAVI)
    ic += yazi(180, 22, '5 Günlük Hava Sıcaklığı Çizgi Grafiği (°C)', MAVI, kalin=True)
    ic += f'<polyline points="45,82 112,66 180,50 248,74 315,42" fill="none" stroke="{KIR}" stroke-width="2.2"/>'
    noktalar = [(45, 82, 'Pzt: 16°'), (112, 66, 'Sal: 20°'), (180, 50, 'Çar: 22°'), (248, 74, 'Per: 18°'), (315, 42, 'Cum: 24°')]
    for x, y, et in noktalar:
        ic += f'<circle cx="{x}" cy="{y}" r="4" fill="{KIR}"/>'
        ic += yazi(x, 101, et, LAC, kalin=True)
    return svg(ic, 'Pazartesiden cumaya 5 günlük sıcaklık değerlerini gösteren çizgi grafiği.')


def kulup_dagilim_kartlari():
    kartlar = [
        (6, 6, '1. Bilim Kulübü', '18 Öğrenci (Toplam 72)', MAVI, MAVI_A),
        (184, 6, '2. Spor Kulübü', '27 Öğrenci (Toplam 72)', YES, YES_A),
        (6, 60, '3. Sanat Kulübü', '15 Öğrenci (Toplam 72)', TUR, TUR_A),
        (184, 60, '4. Doğa Kulübü', '12 Öğrenci (Toplam 72)', MOR, MOR_A),
    ]
    ic = ''
    for x, y, b1, b2, r, z in kartlar:
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 20, b1, r, kalin=True)
        ic += yazi(x + 85, y + 40, b2, LAC)
    return svg(ic, 'Toplam 72 öğrencinin dört okul kulübüne dağılımı.')


def medyan_mod_veri_karti():
    ic = kutu(6, 6, 348, 103, MOR_A, MOR)
    ic += yazi(180, 26, '8 Öğrencinin Deneme Sınavı Doğru Sayıları', MOR, kalin=True)
    ic += yazi(180, 56, 'Veri Grubu: 8 , 12 , 10 , 12 , 15 , 12 , 18 , 25', LAC, kalin=True)
    ic += yazi(180, 86, 'İpucu: Önce küçükten büyüğe sıralayınız → 8, 10, 12, 12, 12, 15, 18, 25', MAVI, kalin=True)
    return svg(ic, 'Sekiz terimli veri grubunda ortanca ve tepe değer bulma kartı.')


def meyve_bahcesi_daire():
    ic = kutu(6, 6, 168, 103, YES_A, YES)
    ic += f'<circle cx="90" cy="58" r="38" fill="#bbf7d0" stroke="{YES}" stroke-width="1.5"/>'
    ic += f'<line x1="90" y1="58" x2="90" y2="20" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="90" y1="58" x2="128" y2="58" stroke="{LAC}" stroke-width="1.3"/>'
    ic += f'<line x1="90" y1="58" x2="62" y2="84" stroke="{LAC}" stroke-width="1.3"/>'
    ic += yazi(90, 104, 'Toplam: 180 Ağaç (360°)', YES, kalin=True)
    ic += kutu(182, 6, 172, 103, TUR_A, TUR)
    ic += yazi(268, 26, 'Merkez Açı Dağılımı', TUR, kalin=True)
    ic += yazi(268, 50, 'Kiraz: 90° · Armut: 120°', LAC)
    ic += yazi(268, 74, 'Elma: 360° - 210° = 150°', KIR, kalin=True)
    ic += yazi(268, 96, '180 ağaçta kaç elma var?', MAVI, kalin=True)
    return svg(ic, '180 ağaçlık bahçenin merkez açılarına göre daire grafiği.')


def okunan_sayfa_sutun():
    ic = kutu(6, 6, 348, 103, CAM_A, CAM)
    ic += yazi(180, 22, '4 Öğrencinin Günlük Okuduğu Sayfa Sayısı', CAM, kalin=True)
    barlar = [(40, 68, 20, 'Ali: 20', MAVI), (120, 58, 30, 'Ece: 30', YES), (200, 48, 40, 'Can: 40', TUR), (280, 38, 50, 'Naz: 50', MOR)]
    for x, y, h, et, r in barlar:
        ic += f'<rect x="{x}" y="{y}" width="44" height="{h}" rx="3" fill="{r}"/>'
        ic += yazi(x + 22, 102, et, LAC, kalin=True)
    return svg(ic, 'Dört öğrencinin okuduğu sayfa sayılarını gösteren sütun grafiği.')


def dort_grup_ortalama():
    gruplar = [
        (6, 'A Grubu', '6, 8, 10, 12', MAVI, MAVI_A),
        (94, 'B Grubu', '10, 14, 15, 17', YES, YES_A),
        (182, 'C Grubu', '15, 18, 20, 23', TUR, TUR_A),
        (270, 'D Grubu', '20, 22, 26, 28', MOR, MOR_A),
    ]
    ic = ''
    for x, ad, veri, r, z in gruplar:
        ic += kutu(x, 6, 84, 103, z, r)
        ic += yazi(x + 42, 36, ad, r, kalin=True)
        ic += yazi(x + 42, 70, veri, LAC, kalin=True)
    return svg(ic, 'Dört farklı veri grubunun aritmetik ortalamalarının sıralanması.')


def basketbol_istikrar_karti():
    ic = kutu(6, 6, 172, 103, MAVI_A, MAVI)
    ic += yazi(92, 26, 'Kaan’ın 5 Maçlık Sayıları', MAVI, kalin=True)
    ic += yazi(92, 54, '18 , 19 , 20 , 21 , 22', LAC, kalin=True)
    ic += yazi(92, 78, 'Ortalama = 20 sayı', YES, kalin=True)
    ic += yazi(92, 98, 'Açıklık = 22 - 18 = 4', MAVI, kalin=True)
    ic += kutu(184, 6, 170, 103, TUR_A, TUR)
    ic += yazi(269, 26, 'Mert’in 5 Maçlık Sayıları', TUR, kalin=True)
    ic += yazi(269, 54, '8 , 12 , 20 , 26 , 34', LAC, kalin=True)
    ic += yazi(269, 78, 'Ortalama = 20 sayı', YES, kalin=True)
    ic += yazi(269, 98, 'Açıklık = 34 - 8 = 26', KIR, kalin=True)
    return svg(ic, 'İki basketbolcunun maç sayıları, ortalamaları ve açıklıkları.')


def uc_deger_maas_karti():
    ic = kutu(6, 6, 348, 103, YES_A, YES)
    ic += yazi(180, 26, 'Bir İş Yerindeki 7 Çalışanın Aylık Maaşları (Bin TL)', YES, kalin=True)
    ic += yazi(180, 54, '20  ·  22  ·  22  ·  [ 24 ]  ·  26  ·  28  ·  120 (Uç Değer!)', LAC, kalin=True)
    ic += yazi(180, 84, 'Ortanca (Medyan) = 24 bin TL   |   Aritmetik Ortalama = 37,4 bin TL', KIR, kalin=True)
    return svg(ic, 'Uç değer içeren maaş verisinde ortanca ve aritmetik ortalama karşılaştırması.')


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sicaklik_cizgi_grafigi()
    s[2]['gorsel'] = kulup_dagilim_kartlari()
    s[5]['gorsel'] = medyan_mod_veri_karti()
    s[6]['gorsel'] = meyve_bahcesi_daire()
    s[7]['gorsel'] = okunan_sayfa_sutun()
    s[8]['gorsel'] = dort_grup_ortalama()
    s[9]['gorsel'] = basketbol_istikrar_karti()
    s[11]['gorsel'] = uc_deger_maas_karti()
