# -*- coding: utf-8 -*-
"""7-turkce-14 çalışma kâğıdı görselleri.
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
    return kart4('ZARFLAR (BELİRTEÇLER) VE SORULARI', [('Durum Zarfı', 'Nasıl?', 'sessizce, dikkatle'), ('Zaman Zarfı', 'Ne zaman?', 'dün, akşamleyin'), ('Yer-Yön Zarfı', 'Nereye? (Eksiz)', 'içeri, dışarı, ileri'), ('Miktar Zarfı', 'Ne kadar?', 'çok, az, oldukça')], '7-turkce-14 zarf türleri kartları')

def g1():
    return karsilastir2('YER-YÖN ZARFI İLE İSİM AYRIMI KURALI', 'Yer-Yön Zarfı (Ek Almaz!)', 'içeri girdi · aşağı indi · dışarı çıktı', 'Fiile sorulan “Nereye?” sorusuna cevaptır', 'Ek Alırsa İsimleşir (Zarf Değildir)', 'içeriye girdi · aşağıda bekliyor · dışarıdan', 'Hal eki (-e, -de, -den) alınca isim olur', '7-turkce-14 yer-yön zarfı kuralı')

def g2():
    return uclu_sema('SÖZ SANATLARI VE DÜŞÜNCEYİ GELİŞTİRME', [('Kişileştirme & İntak', 'İnsani özellik verme', 'Varlığı konuşturma'), ('Benzetme & Tezat', 'Gibi kadar ile ilgi', 'Zıt kavramlar bir arada'), ('Tanık Gösterme', 'Uzman sözü alıntısı', 'Tartışmayı güçlendirir')], '7-turkce-14 söz sanatları şeması')

def g5():
    return kart4('CÜMLEDE ZARF ANALİZİ (DİKKAT: SIFAT vs. ZARF)', [('Dün akşam', 'Zaman Zarfı', 'Ne zaman çalıştı?'), ('içerideki oda', 'Sıfat (-ki eki)', 'Hangi oda? (İsim)'), ('oldukça', 'Miktar Zarfı', 'Ne kadar dikkatli?'), ('dikkatli', 'Durum Zarfı', 'Nasıl çalıştı?')], '7-turkce-14 cümle zarf analizi')

def g6():
    return karsilastir2('TEMA METİNLERİ: ESKİCİ VE YA HAYIR SÖYLE..', 'Eskici (Refik Halit Karay)', 'Küçük Hasan’ın gurbetteki yalnızlığı', 'Ana dili Türkçe ile kurulan sıcak gönül bağı', 'Ya Hayır Söyle.. (İletişim Ahlakı)', 'Tatlı dil, empati ve etkin dinleme', 'Yüz yüze ve dijital ortamda nezaket', '7-turkce-14 metin karşılaştırması')

def g7():
    return karsilastir2('SIFAT İLE DURUM ZARFI ARASINDAKİ FARK', 'İsmi Niteleyen -> SIFAT', 'Soğuk rüzgâr (Nasıl rüzgâr? -> İsim)', 'Güzel şiir (Nasıl şiir? -> İsim)', 'Fiili Belirten -> DURUM ZARFI', 'Soğuk davrandı (Nasıl davrandı? -> Fiil)', 'Güzel konuştu (Nasıl konuştu? -> Fiil)', '7-turkce-14 sıfat ve zarf farkı')

def g8():
    return akis4('OKUMA VE METİN İNCELEME BASAMAKLARI', [('1. Okuma', 'Vurgu ve tonlama', 'Anlayarak okuma'), ('2. Çözümleme', 'Unsurlara ayırma', 'Konu, olay, kişi'), ('3. Çıkarım', 'İpuçlarından hareket', 'Örtük anlam bulma'), ('4. Değerlendirme', 'Ölçütlerle yargı', 'Üslup ve tutarlılık')], '7-turkce-14 okuma basamakları')

def g11():
    return uclu_sema('ETKİLİ VE NAZİK İLETİŞİMİN 3 ALTIN KURALI', [('1. Ben Dili', 'Suçlamadan duygu', 'ifade etme'), ('2. Etkin Dinleme', 'Söz kesmeden', 'göz teması kurma'), ('3. Dijital Nezaket', 'Saygılı üslup', 'Kırıcı sözden kaçınma')], '7-turkce-14 iletişim ilkeleri')

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
