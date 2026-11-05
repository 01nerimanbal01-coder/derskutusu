# -*- coding: utf-8 -*-
"""10-cografya-6 çalışma kâğıdı görselleri.
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
    return uclu_sema('YERKÜRENİN İÇ YAPISI (GEOSFER)', [('1. Yer Kabuğu', 'Sial (Kıta) ve Sima (Okyanus)', 'En ince ve az yoğun katman'), ('2. Manto (Astenosfer)', 'Yerküre hacminin %84\'ü', 'Konveksiyonel akıntı merkezi'), ('3. Çekirdek (Nife)', 'Nikel (Ni) ve Demir (Fe)', 'En sıcak (6000°C) ve en yoğun')], '10-cografya-6 geosfer katmanları')

def g1():
    return karsilastir2('YÜZEYDEN MERKEZE DEĞİŞİM KURALI', 'Yer Kabuğundan Çekirdeğe', 'Sıcaklık düzenli olarak artar', 'Basınç ve yoğunluk (özkütle) artar', 'Sial ve Sima Farkı', 'Sial: Dağların altında kalın, az yoğun', 'Sima: Okyanus tabanında ince, yoğun', '10-cografya-6 iç yapı değişimi')

def g2():
    return karsilastir2('OKYANUS ORTASI SIRTLAR VE DALMA-BATMA', 'Uzaklaşan Sınır (Yapıcı)', 'Okyanus ortası sırtlarda yeni kabuk', 'Atlas Sırtı ve İzlanda oluşumu', 'Yaklaşan Sınır (Yıkıcı)', 'Dalma-batma zonunda kabuk erir', 'Dünya yüzölçümü sabit kalır', '10-cografya-6 kabuk döngüsü')

def g3():
    return kart4('LEVHA TEKTONİĞİNİN KANITLARI', [('Kıyı Uyumu', 'G. Amerika - Afrika'), ('Fosil Kanıtı', 'Mesosaurus sürüngeni'), ('Buzul İzleri', 'Tropikal kıtalarda izler'), ('Okyanus Tabanı', 'Sırttan uzağa yaş artar')], '10-cografya-6 Wegener kanıtları')

def g5():
    return kart4('PANGEA\'DAN GÜNÜMÜZE EVRİM', [('1. Paleozoyik', 'Tek süper kıta Pangea'), ('2. Mezozoyik', 'Laurasia ve Gondwana'), ('3. Tersiyer', 'Alp-Himalaya kıvrımı'), ('4. Kuvaterner', 'Ege ve Boğazların oluşumu')], '10-cografya-6 jeolojik evrim')

def g6():
    return uclu_sema('ÜÇ TÜR LEVHA SINIRI VE YER ŞEKİLLERİ', [('Yaklaşan (Çarpışan)', 'Kıta-Kıta: Himalaya Dağları', 'Kıta-Okyanus: And, Mariana'), ('Uzaklaşan (Ayrılan)', 'Okyanus: Atlas Ortası Sırtı', 'Kıta: Doğu Afrika Rift, Kızıldeniz'), ('Yanal (Transform)', 'Kabuk oluşmaz / yok olmaz', 'Kuzey Anadolu ve San Andreas')], '10-cografya-6 levha sınırları')

def g8():
    return kart4('LEVHA ETKİLEŞİMİ ÖRNEKLERİ', [('Avrasya - Hindistan', 'Himalaya Sıradağları'), ('Nazca - G. Amerika', 'And Dağları ve Hendeği'), ('K. Amerika - Avrasya', 'Atlas Okyanusu Sırtı'), ('Anadolu - Avrasya', 'Kuzey Anadolu Fayı (KAF)')], '10-cografya-6 levha eşleşmeleri')

def g11():
    return karsilastir2('TÜRKİYE\'NİN TEKTONİK KONUMU', 'Sıkıştıran Levhalar', 'Kuzeyde Avrasya Levhası', 'Güneyde Afrika ve Arap Levhaları', 'Oluşan Fay Hatları ve Sonuç', 'KAF, DAF ve BAF kırık kuşakları', 'Yüksek deprem ve jeotermal potansiyel', '10-cografya-6 Türkiye tektoniği')

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
