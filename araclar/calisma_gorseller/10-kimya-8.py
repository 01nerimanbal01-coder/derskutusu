# -*- coding: utf-8 -*-
"""10-kimya-8 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(ic, etiket):
    return f'<svg viewBox="0 0 360 115" style="width:100%;max-height:24mm;display:block;margin:1mm auto;" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=9.2, renk=LAC, hiza='middle', ince=False):
    temiz = str(metin).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{temiz}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=6, kalin=0.75):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def kart4(baslik, kartlar, etiket, ana_renk=MAVI, arka_renk=GRI_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(kartlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 80, 78, a, c, 6, 0.75)
        ic += yazi(x + 40, 44, b, 8.4, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 72}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 69, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, c1=MAVI, a1=MAVI_A, c2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, c1, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, c1)
    ic += kutu(12, 26, 162, 78, a1, c1, 6, 0.75)
    ic += yazi(93, 44, sol_b, 8.8, c1)
    ic += f'<line x1="22" y1="52" x2="164" y2="52" stroke="{c1}" stroke-width="0.6"/>'
    ic += yazi(93, 70, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 89, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 26, 162, 78, a2, c2, 6, 0.75)
    ic += yazi(267, 44, sag_b, 8.8, c2)
    ic += f'<line x1="196" y1="52" x2="338" y2="52" stroke="{c2}" stroke-width="0.6"/>'
    ic += yazi(267, 70, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 89, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 26, 108, 78, a, c, 6, 0.75)
        ic += yazi(x + 54, 44, b, 8.5, c)
        ic += f'<line x1="{x + 8}" y1="52" x2="{x + 100}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 54, 70, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 89, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM, arka_renk=CAM_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (YES, YES_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(adimlar):
        c, a = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 26, 78, 78, a, c, 6, 0.75)
        ic += yazi(x + 39, 44, b, 8.3, c)
        ic += yazi(x + 39, 68, d1, 7.5, LAC, ince=True)
        ic += yazi(x + 39, 88, d2, 7.1, SOLUK, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+80},64 {x+85},60 {x+85},68" fill="{ana_renk}"/>'
    return svg(ic, etiket)


def g0():
    return kart4('KİMYASAL TEPKİME DENKLEMİ BİLEŞENLERİ', [
        ('Tepken (Giren)', 'Okun sol tarafı', 'Harcanan maddeler'),
        ('Ürün (Çıkan)', 'Okun sağ tarafı', 'Oluşan maddeler'),
        ('Fiziksel Hâller', '(k) Katı, (s) Sıvı', '(g) Gaz, (suda) Çözelti'),
        ('MAH Sırası', 'Metal -> Ametal', '-> Hidrojen -> Oksijen')
    ], '10-kimya-8 tepkime bileşenleri')

def g1():
    return karsilastir2('ORGANİK YANMA DENKLEŞTİRMESİ (C3H8)',
        '1. Karbon ve Hidrojen Eşitlemesi', 'Girenlerde: 3 C ve 8 H atomu var', 'Ürünlere: 3 CO2 ve 4 H2O yazılır',
        '2. Oksijen Eşitlemesi (Son Adım)', 'Ürünlerde: (3·2) + (4·1) = 10 O atomu', 'Girenlere: 5 O2 yazılır (5·2 = 10 O)',
        '10-kimya-8 C3H8 yanması')

def g2():
    return karsilastir2('TEPKİMELERDE KORUNAN VE DEĞİŞEBİLENLER',
        'Daima Korunan Nicelikler', 'Atom türü ve sayısı, Toplam kütle', 'Toplam proton/nötron/elektron ve toplam yük',
        'Değişebilen Nicelikler', 'Toplam mol ve molekül sayısı, Gaz hacmi', 'Fiziksel hâl, renk, koku ve kimyasal özellik',
        '10-kimya-8 korunan özellikler')

def g4():
    return karsilastir2('TERMİT TEPKİMESİNDE MAH UYGULAMASI',
        'Ham Denklem: Al + Fe2O3 -> Al2O3 + Fe', 'Ürünlerde 2 Al var -> Girendeki Al önüne 2', 'Girende 2 Fe var -> Üründeki Fe önüne 2',
        'Denkleştirilmiş Tam Sayılı Denklem', '2 Al(k) + Fe2O3(k) -> Al2O3(k) + 2 Fe(s)', 'Al ve Fe katsayıları toplamı: 2 + 2 = 4',
        '10-kimya-8 termit tepkimesi')

def g6():
    return karsilastir2('ALT İNDİS VE ÖN KATSAYI FARKI',
        'Alt İndis Değiştirilemez! (Yanlış)', 'H2O -> H2O2 yazılırsa su yerine', 'hidrojen peroksit (farklı bileşik) olur',
        'Ön Katsayı Değiştirilir (Doğru)', '2 H2(g) + O2(g) -> 2 H2O(s)', 'Kimyasal tür korunur, atom sayısı eşitlenir',
        '10-kimya-8 alt indis ve katsayı')

def g7():
    return akis4('MAH YÖNTEMİYLE DENKLEŞTİRME ADIMLARI', [
        ('1. Metal (M)', 'Na, Mg, Al, Fe, Ca', 'atomlarını eşitle'),
        ('2. Ametal (A)', 'C, N, P, S, Cl, Br', 'atomlarını eşitle'),
        ('3. Hidrojen (H)', 'Bileşiklerdeki H', 'sayısını eşitle'),
        ('4. Oksijen (O)', 'En son O atomunu', 'kontrol edip eşitle')
    ], '10-kimya-8 MAH sırası')

def g8():
    return karsilastir2('YAPISINDA OKSİJEN BULUNAN BİLEŞİĞİN YANMASI',
        'Etil Alkol Yanması: C2H5OH + O2', '2 C ve 6 H için -> 2 CO2 + 3 H2O oluşur', 'Ürünlerde toplam: (2·2) + 3 = 7 O atomu',
        'Girenlerdeki Oksijen Hesabı (Dikkat!)', 'C2H5OH içinde 1 tane O atomu zaten var!', '7 - 1 = 6 O gerekir -> 3 O2 (Katsayı = 3)',
        '10-kimya-8 etil alkol yanması')

def g11():
    return karsilastir2('KESİRLİ KATSAYIDAN TAM SAYIYA GEÇİŞ (C2H6)',
        'Kesirli Katsayılı Ara Denklem', 'C2H6 + (7/2) O2 -> 2 CO2 + 3 H2O', 'Diatomik O2 önüne 7/2 kesri yazılabilir',
        'En Küçük Tam Sayılarla Genişletme (x2)', '2 C2H6 + 7 O2 -> 4 CO2 + 6 H2O', 'Tüm maddelerin katsayıları 2 ile çarpılır',
        '10-kimya-8 tam sayılı genişletme')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[4]['gorsel'] = g4()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
