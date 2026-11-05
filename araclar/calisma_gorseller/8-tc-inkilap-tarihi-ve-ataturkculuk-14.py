# -*- coding: utf-8 -*-
"""8-tc-inkilap-tarihi-ve-ataturkculuk-14 çalışma kâğıdı görselleri.
SVG viewBox="0 0 360 115"; insan figürü yok (K024); metin arkası beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK = '#9aa6bd', '#eef1f6', '#5b6479'
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
        ic += kutu(x, 27, 80, 77, a, c, 6, 0.75)
        ic += yazi(x + 40, 44, b, 8.3, c)
        ic += f'<line x1="{x + 6}" y1="52" x2="{x + 74}" y2="52" stroke="{c}" stroke-width="0.6"/>'
        ic += yazi(x + 40, 69, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 40, 88, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def karsilastir2(baslik, sol_b, sol_d1, sol_d2, sag_b, sag_d1, sag_d2, etiket, r1=MAVI, a1=MAVI_A, r2=TUR, a2=TUR_A):
    ic = kutu(4, 4, 352, 107, GRI_A, r1, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, r1)
    ic += kutu(12, 27, 162, 77, a1, r1, 6, 0.75)
    ic += yazi(93, 45, sol_b, 8.8, r1)
    ic += yazi(93, 66, sol_d1, 7.8, LAC, ince=True)
    ic += yazi(93, 86, sol_d2, 7.4, SOLUK, ince=True)
    ic += kutu(186, 27, 162, 77, a2, r2, 6, 0.75)
    ic += yazi(267, 45, sag_b, 8.8, r2)
    ic += yazi(267, 66, sag_d1, 7.8, LAC, ince=True)
    ic += yazi(267, 86, sag_d2, 7.4, SOLUK, ince=True)
    return svg(ic, etiket)


def uclu_sema(baslik, uclu, etiket, ana_renk=YES, arka_renk=YES_A):
    ic = kutu(4, 4, 352, 107, arka_renk, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.6, ana_renk)
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (MOR, MOR_A)]
    for i, (b, d1, d2) in enumerate(uclu):
        c, a = renkler[i % 3]
        x = 12 + i * 114
        ic += kutu(x, 27, 108, 77, a, c, 6, 0.75)
        ic += yazi(x + 54, 45, b, 8.6, c)
        ic += yazi(x + 54, 66, d1, 7.6, LAC, ince=True)
        ic += yazi(x + 54, 86, d2, 7.2, SOLUK, ince=True)
    return svg(ic, etiket)


def akis4(baslik, adimlar, etiket, ana_renk=CAM):
    ic = kutu(4, 4, 352, 107, CAM_A, ana_renk, 6, 0.75)
    ic += yazi(180, 19, baslik, 9.5, ana_renk)
    renkler = [MAVI, YES, TUR, MOR]
    for i, (b, d1, d2) in enumerate(adimlar):
        c = renkler[i % 4]
        x = 10 + i * 86
        ic += kutu(x, 28, 78, 76, '#f8fafc', c, 6, 0.75)
        ic += yazi(x + 39, 46, b, 8.2, c)
        ic += yazi(x + 39, 67, d1, 7.4, LAC, ince=True)
        ic += yazi(x + 39, 86, d2, 7.0, SOLUK, ince=True)
        if i < 3:
            ic += f'<polygon points="{x+80},64 {x+85},60 {x+85},68" fill="{ana_renk}"/>'
    return svg(ic, etiket)


def g0():
    return kart4('DOĞU VE GÜNEY CEPHESİ KAHRAMANLARI', [('Kâzım Karabekir', '15. Kolordu · Doğu', 'Gümrü Zaferi (1920)'), ('Sütçü İmam', 'Maraş Direnişi', 'İlk kurşun ve kıyam'), ('Ali Saip Bey', 'Urfa Savunması', 'Kuva-yı Milliye'), ('Şahin Bey', 'Kilis–Antep Yolu', 'Gazi Antep (1921)')], '8-inkilap-14 Doğu ve Güney kahramanları')

def g1():
    return karsilastir2('GÜMRÜ ANTLAŞMASI (3 ARALIK 1920) VE ÖNEMİ', 'Askeri Zafer (15. Kolordu)', 'Kâzım Karabekir Paşa Ermenileri yendi', 'Sarıkamış, Kars ve Iğdır kurtarıldı', 'İlk Siyasi ve Diplomatik Başarı', 'TBMM’yi ve Misakımillî’yi tanıyan ilk devlet', 'Ermenistan Sevr Antlaşması’nı reddetti', '8-inkilap-14 Gümrü Antlaşması kartı')

def g2():
    return uclu_sema('GÜNEY CEPHESİ ŞEHİRLERİ VE GAZİLİK UNVANLARI', [('Gazi Antep (1921)', 'Şahin Bey · Karayılan', '25 Aralık 1921'), ('Kahraman Maraş (1973)', 'Sütçü İmam · Rıdvan H.', '12 Şubat 1920'), ('Şanlı Urfa (1984)', 'Ali Saip Bey · 12’ler', '11 Nisan 1920')], '8-inkilap-14 Güney şehirleri ve unvanları')

def g5():
    return karsilastir2('DOĞU CEPHESİ İLE GÜNEY CEPHESİ KARŞILAŞTIRMASI', 'Doğu Cephesi (Ermenilere Karşı)', 'Savaşan Güç: 15. Kolordu (Düzenli Ordu)', 'Kapanışı: 3 Aralık 1920 Gümrü Antlaşması', 'Güney Cephesi (Fransız + Ermeni)', 'Savaşan Güç: Kuva-yı Milliye (Halk)', 'Kapanışı: 20 Ekim 1921 Ankara Antlaşması', '8-inkilap-14 Doğu ve Güney cepheleri farkı')

def g6():
    return karsilastir2('MARAŞ SAVUNMASI: BAYRAK OLAYI VE BAĞIMSIZLIK RUHU', 'Maraş Kalesi Bayrak Olayı', 'Fransızlar kaledeki Türk bayrağını indirdi', 'Rıdvan Hoca: “Hür olmayan yerde cuma kılınmaz!”', 'Sonuç: Halkın Destansı Zaferi', 'Halk kaleye koşup Türk bayrağını yeniden çekti', '12 Şubat 1920’de Fransızlar Maraş’tan çekildi', '8-inkilap-14 Maraş Kalesi bayrak olayı')

def g7():
    return uclu_sema('DOĞU VE GÜNEYİN KAPANMASININ BATIYA ETKİSİ', [('1. Doğu Kapandı', 'Gümrü (Aralık 1920)', 'Birlikler Batı’ya geçti'), ('2. Güney Kapandı', 'Ankara (Ekim 1921)', 'Fransa savaştan çekildi'), ('3. Tek Hedef Batı', 'Tüm güç ve silahlar', 'Yunan cephesine toplandı')], '8-inkilap-14 cephelerin Batı’ya etkisi')

def g8():
    return akis4('DOĞU VE GÜNEY CEPHESİ KRONOLOJİSİ (1919–1921)', [('Eylül 1919', 'İngiliz->Fransız', 'Güneyin devri'), ('Şubat–Nisan 1920', 'Maraş ve Urfa', 'Halk zaferi'), ('3 Aralık 1920', 'Gümrü Antlaşması', 'Doğu kapandı'), ('20 Ekim 1921', 'Ankara Antlaşması', 'Güney kapandı')], '8-inkilap-14 kronoloji akışı')

def g11():
    return karsilastir2('ŞAHİN BEY’İN MEKTUBU VE KUVA-YI MİLLİYE İRADESİ', 'Şahin Bey (Kilis–Antep Yolu)', '“Düşman arabaları cesedimi çiğnemeden', 'Antep’e asla giremez!” (Mart 1920)', 'Millî Mücadele Ruhu', 'Silah ve cephane azlığına rağmen sivil direniş', 'Ya İstiklal Ya Ölüm! kararlılığının zaferi', '8-inkilap-14 Şahin Bey ve Kuva-yı Milliye')

def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = g0()
    s[1]['gorsel'] = g1()
    s[2]['gorsel'] = g2()
    s[5]['gorsel'] = g5()
    s[6]['gorsel'] = g6()
    s[7]['gorsel'] = g7()
    s[8]['gorsel'] = g8()
    s[11]['gorsel'] = g11()
