# -*- coding: utf-8 -*-
"""10-matematik-7 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket, en_fazla=32):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 360 115"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.5, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 80, 76, a, c, 6, 0.75)
        ic += yazi(x + 40, 48, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="58" x2="{x + 72}" y2="58" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 78, d, 7.5, LAC, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket):
    ic = kutu(4, 4, 352, 107, MAVI_A, MAVI, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, MAVI)
    ic += kutu(14, 28, 160, 76, '#f8fafc', MAVI, 6, 0.75)
    ic += yazi(94, 48, sol_b, 9, MAVI)
    ic += yazi(94, 68, sol_d1, 8, LAC, ince=True)
    ic += yazi(94, 88, sol_d2, 7.5, SOLUK, ince=True)
    ic += kutu(186, 28, 160, 76, '#f8fafc', TUR, 6, 0.75)
    ic += yazi(266, 48, sag_b, 9, TUR)
    ic += yazi(266, 68, sag_d1, 8, LAC, ince=True)
    ic += yazi(266, 88, sag_d2, 7.5, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 20, baslik, 10, ana_renk)
    renkler = [MAVI, TUR, MOR]
    for i, (b, d1, d2) in enumerate(uclu):
        c = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 28, 108, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 54, 48, b, 8.8, c)
        ic += yazi(x + 54, 68, d1, 7.8, LAC, ince=True)
        ic += yazi(x + 54, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)

def g0():
    return kart4('İKİ YÖNLÜ TABLO VE SIKLIK TÜRLERİ', [('Kategorik Değişken', 'Nitel sınıflandırma'), ('Marjinal Sıklık', 'Kenar toplamı / N'), ('Birleşik Sıklık', 'İç hücre / Genel N'), ('Koşullu Sıklık', 'İç hücre / Satır-Sütun')], '10-matematik-7 temel kavramlar')

def g1():
    return karsilastir2('BİRLEŞİK VE KOŞULLU GÖRELİ SIKLIK (N=250)', 'Birleşik Göreli Sıklık (Payda = 250)', 'Tüm katılımcılarda sosyal medya genci:', '120 / 250 = 48 / 100 = %48', 'Koşullu Göreli Sıklık (Payda = 150)', 'Gençlerin içinde sosyal medya oranı:', '120 / 150 = 4 / 5 = %80', '10-matematik-7 birlesik kosullu')

def g2():
    return karsilastir2('ATÖLYE ANKETİNDE BAĞIMSIZLIK (N=120)', 'Kızlarda Robotik Koşullu Sıklığı', "50 kızdan 30'u Robotik seçti:", '30 / 50 = 0,60 (%60)', 'Erkeklerde Robotik Koşullu Sıklığı', "70 erkekten 42'si Robotik seçti:", '42 / 70 = 0,60 (%60 -> İlişki YOK!)', '10-matematik-7 bagimsizlik')

def g3():
    return uclu_sema('GÖRELİ SIKLIKTA PAYDAYA NE YAZILIR?', [('Marjinal Göreli', 'Kenar Toplamı / N', 'Genel toplam paydada'), ('Birleşik Göreli', 'Hücre Değeri / N', 'Genel toplam paydada'), ('Koşullu Göreli', 'Hücre / Satır(Sütun)', 'Yalnız alt grup paydada!')], '10-matematik-7 payda kurali')

def g5():
    return kart4('İSTATİSTİKSEL ARAŞTIRMA SÜRECİ (4 ADIM)', [('1. Araştırma Sorusu', 'İki kategorik değişken'), ('2. Veri Toplama', 'Anket ve gözlem planı'), ('3. İki Yönlü Tablo', 'Göreli sıklık ve grafik'), ('4. Sonuç Yorumu', 'İlişki / bağımsızlık')], '10-matematik-7 arastirma adimlari')

def g6():
    return uclu_sema('SÜTUN GRAFİKLERİ VE İLİŞKİ YORUMU', [('Kümelenmiş Sütun', 'Alt gruplar yan yana', 'Sıklık veya % kıyaslar'), ('Yığılmış Sütun', '%100 tek sütun içinde', 'Koşullu % üst üste'), ('İlişki Ölçütü', 'Dilimler farklıysa -> İlişki', 'Aynıysa -> Bağımsız')], '10-matematik-7 sutun grafikleri')

def g8():
    return kart4('200 KİŞİLİK KULÜP ANKETİ (80 KIZ, 120 ERKEK)', [('Marjinal Kız Oranı', '80 / 200 = %40'), ('Birleşik Satranç Kız', '20 / 200 = %10'), ('Kız Koşullu Satranç', '20 / 80 = %25'), ('Toplam Birleşik Oran', '200 / 200 = 1 (%100)')], '10-matematik-7 anket oranlari')

def g11():
    return karsilastir2('HASTANE İLAÇ ETKİNLİĞİ ANALİZİ (N=100)', 'A İlacı Grubu (60 Hasta)', '48 hasta iyileşti -> Koşullu sıklık:', '48 / 60 = %80 iyileşme oranı', 'B İlacı Grubu (40 Hasta)', '20 hasta iyileşti -> Koşullu sıklık:', '20 / 40 = %50 (%80 != %50 -> İlişki VAR!)', '10-matematik-7 ilac analizi')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[3]['gorsel'] = g3()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
