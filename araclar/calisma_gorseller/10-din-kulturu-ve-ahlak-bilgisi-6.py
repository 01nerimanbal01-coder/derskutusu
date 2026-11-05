# -*- coding: utf-8 -*-
"""10-din-kulturu-ve-ahlak-bilgisi-6 çalışma kâğıdı görselleri.
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
    return kart4('KUR\'AN\'DAN MESAJLAR VE KAVRAMLAR', [('İsrâ 36. Ayet', 'Bilgi ve sorumluluk'), ('Mülk 23. Ayet', 'Duyu, akıl ve şükür'), ('el-Fuâd (Kalp)', 'Akletme ve idrak'), ('Tebeyyün', 'Haberi doğrulama')], '10-din-6 ayet ve kavramlar')

def g1():
    return karsilastir2('İSRÂ SURESİ 36. AYETİN İLKELERİ', 'Yasaklanan Tutumlar', 'Kesin bilgin olmayan şeyin ardına düşme', 'Zan, tahmin, iftira ve yalan şahitlik', 'Sorumlu Tutulan Yetiler', 'Kulak (Sem\'), Göz (Basar), Kalp (Fuâd)', 'Ahirette hepsi hesaba çekilecektir', '10-din-6 İsra 36 ilkeleri')

def g2():
    return karsilastir2('MÜLK SURESİ 23. AYET VE NİMETİN ŞÜKRÜ', 'İlahi Bilgi Donanımları', 'Kulaklar (İşitme) ve Gözler (Görme)', 'Kalpler (Akletme ve İman Merkezi)', 'Gerçek Şükür Nasıl Edilir?', 'Hakikati dinlemek ve ibretle bakmak', 'Aklı ilim ve salih amelde kullanmak', '10-din-6 Mülk 23 şükrü')

def g3():
    return uclu_sema('ÜÇ BİLGİ ARACI VE İSLAM BİLGİ KAYNAKLARI', [('1. Kulak (es-Sem\')', 'Anne karnında ilk gelişen', 'Sadık haberi (vahyi) dinler'), ('2. Göz (el-Ebsâr)', 'Şehadet âlemini gözlemler', 'Sağlam duyuları temsil eder'), ('3. Kalp (el-Ef\'ide)', 'Verileri muhakeme eder', 'Selim aklı ve vicdanı temsil eder')], '10-din-6 üç bilgi aracı')

def g5():
    return kart4('MEDYA AHLAKI VE BİLGİ DOĞRULAMA', [('1. Kaynak Kontrolü', 'Haber kimden geldi?'), ('2. Tahkik (Tebeyyün)', 'Kanıt ve delil arama'), ('3. Emanet Filtresi', 'İftira ve kul hakkı var mı?'), ('4. Sorumlu Paylaşım', 'Yalnız doğruyu aktarma')], '10-din-6 medya ahlakı adımları')

def g6():
    return karsilastir2('KUR\'AN\'DA KALP (EL-FUÂD) KAVRAMI', 'Biyolojik Anlamın Ötesinde', 'Yalnız kan pompalayan organ değildir', 'Düşünme, anlama ve akletme merkezidir', 'Bilgi ve İman Boyutu', 'Hak ile batılı ayıran selim akıldır', 'İman, vicdan ve sorumluluk yeridir', '10-din-6 kalp ve akıl')

def g8():
    return kart4('KUR\'AN\'I DOĞRU ANLAMA REHBERİ', [('Meal', 'Yaklaşık anlam çevirisi'), ('Tefsir', 'Geniş ve derin açıklama'), ('Siyak-Sibak', 'Ayetin öncesi-sonrası'), ('Esbâb-ı Nüzûl', 'Ayetlerin iniş sebepleri')], '10-din-6 meal ve tefsir')

def g11():
    return karsilastir2('DİJİTAL ÇAĞDA İSRÂ 36 VE HUCURÂT 6', 'Doğrulanmamış Haber Yaymak', 'Zan ve dezenformasyona ortak olmaktır', 'Kul hakkı ve toplumsal zarara yol açar', 'Müminin Bilgi Ahlakı', 'Haberi kaynağından tahkik etmektir', 'Kulak, göz ve kalp hesabını unutmamaktır', '10-din-6 dijital bilgi ahlakı')

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
