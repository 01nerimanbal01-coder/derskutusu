# -*- coding: utf-8 -*-
"""10-turk-dili-ve-edebiyati-5 çalışma kâğıdı görselleri.
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
    return kart4('ŞİİR OKUMA (İNŞAT) TEMEL UNSURLARI', [('Vurgu', 'Anlamlı hece baskısı'), ('Tonlama', 'Duyguya göre ses perdesi'), ('Duraklama', 'Bilinçli nefes ve es'), ('Beden Dili', 'Doğal jest ve göz teması')], '10-turk-dili-ve-edebiyati-5 inşat unsurları')

def g1():
    return karsilastir2('DİNLETİ HAZIRLIĞINDA İLK İKİ AŞAMA', '1. Tema ve Amaç Belirleme', 'Örn: Vatan sevgisi, Doğa, Dostluk', 'Hedef kitle ve süre planlaması', '2. Şiir Seçkisi Oluşturma', 'Temaya ve ahenge uygun şiirler', 'Edebî değeri yüksek metin seçimi', '10-turk-dili-ve-edebiyati-5 ilk iki aşama')

def g2():
    return karsilastir2('ÇOK MODLU UNSURLARIN DOĞRU KULLANIMI', 'Doğru Uygulama', 'Hafif enstrümantal fon müziği', 'Şiirin atmosferini destekleyen görsel', 'Hatalı Uygulama', 'Sesi bastıran sözlü/yüksek müzik', 'Dikkat dağıtan karmaşık slaytlar', '10-turk-dili-ve-edebiyati-5 çok modlu unsurlar')

def g3():
    return uclu_sema('SAHNEDE SÖZSÜZ İLETİŞİM VE DURUŞ', [('Sahne Duruşu', 'Dik ve öz güvenli', 'Kürsüye kapanmama'), ('Göz Teması', 'Salonu eşit tarama', 'Kâğıda gömülmeme'), ('Jest ve Mimik', 'Duyguyla uyumlu', 'Abartıdan uzak')], '10-turk-dili-ve-edebiyati-5 beden dili')

def g5():
    return kart4('ŞİİR DİNLETİSİ SÜREÇ ADIMLARI', [('1. Tema & Şiir', 'Seçki hazırlığı'), ('2. Senaryo & Ses', 'Geçiş ve fon müziği'), ('3. Prova', 'Sahne ve teknik uyum'), ('4. Sunum & Dönüt', 'Dinleti ve değerlendirme')], '10-turk-dili-ve-edebiyati-5 süreç adımları')

def g6():
    return karsilastir2('ŞİİR TÜRÜNE GÖRE TONLAMA UYUMU', 'Epik / Kahramanlık Şiiri', 'Gür, coşkulu ve kararlı ses tonu', 'Vurgulu ve ritmik söyleyiş', 'Lirik / Özlem Şiiri', 'Yumuşak, içten ve duygusal ton', 'Duraklamalarla derinleşen ahenk', '10-turk-dili-ve-edebiyati-5 tür ve tonlama')

def g8():
    return kart4('DİNLETİ EKİBİ GÖREV DAĞILIMI', [('Okuyucular', 'Şiirleri seslendirme'), ('Sunucu', 'Geçiş metinlerini okuma'), ('Ses Sorumlusu', 'Fon müziği kontrolü'), ('Sahne Sorumlusu', 'Işık ve görsel akış')], '10-turk-dili-ve-edebiyati-5 görev dağılımı')

def g11():
    return karsilastir2('ÖZ VE AKRAN DEĞERLENDİRMESİ KÜLTÜRÜ', 'Öz Değerlendirme', 'Kendi ses, heyecan ve süre analizi', 'Öz farkındalık geliştirme', 'Akran Değerlendirmesi', 'Arkadaşa yapıcı ve somut dönüt', 'Birlikte öğrenme ve gelişme', '10-turk-dili-ve-edebiyati-5 değerlendirme')

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
