"""5. sınıf Din Kültürü ve Ahlak Bilgisi 9. hafta (Namazın Kılınışı: Namazın Hazırlık Şartları ve Rükünleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.4, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def sart_rukun_karisik_sema():
    ic = kutu(6, 6, 170, 82, MAVI_A, MAVI)
    ic += yazi(91, 21, 'Hazırlık Şartları (Dıştan)', 10.4, MAVI)
    ic += yazi(91, 41, 'I. İstikbal-i kıble', 10.0, LAC, ince=True)
    ic += yazi(91, 59, 'II. Kıraat (Kur’an okuma)', 10.0, KIR)
    ic += yazi(91, 77, 'III. Vakit', 10.0, LAC, ince=True)

    ic += kutu(184, 6, 170, 82, YES_A, YES)
    ic += yazi(269, 21, 'Namazın Rükünleri (İçten)', 10.4, YESIL_K)
    ic += yazi(269, 41, 'A. İftitah tekbiri', 10.0, LAC, ince=True)
    ic += yazi(269, 59, 'B. Niyet (Namaza yönelme)', 10.0, KIR)
    ic += yazi(269, 77, 'C. Secde', 10.0, LAC, ince=True)
    return svg(360, 94, ic, 'Namazın hazırlık şartları ve rükünleri sınıflandırma tablosu.', 16)


def rukun_uygulama_kartlari():
    kartlar = [
        ('1. Rükün', 'Başlama tekbiri', MAVI, MAVI_A),
        ('2. Rükün', 'Dizleri tutup eğilme', YES, YES_A),
        ('3. Rükün', 'Yere kapanma (2 kez)', TUR, TUR_A),
        ('4. Rükün', 'Son oturuş', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.4, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 56, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, 'Namazın dört rüknünü özetleyen uygulama kartları.', 15)


def ahmet_hazirlik_listesi():
    adimlar = [
        ('1. Adım', 'Abdest aldı', MAVI, MAVI_A),
        ('2. Adım', 'Temiz kıyafet giydi', YES, YES_A),
        ('3. Adım', 'Ezanı dinledi', TUR, TUR_A),
        ('4. Adım', 'Kâbe yönüne döndü', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.4, r)
        ic += yazi(x + 41, 55, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, 'Namaza başlamadan önce yapılan dört hazırlık adımı.', 15)


def ruku_secde_tesbih_karti():
    ic = kutu(6, 6, 170, 78, YES_A, YES)
    ic += yazi(91, 22, 'K Rüknü Tesbihi (3 Kere)', 10.3, YESIL_K)
    ic += yazi(91, 46, '«Sübhâne rabbiye’l-azîm»', 10.1, LAC)
    ic += yazi(91, 68, '(Büyük Rabbim noksandan uzaktır)', 9.2, LAC, ince=True)

    ic += kutu(184, 6, 170, 78, TUR_A, TUR)
    ic += yazi(269, 22, 'L Rüknü Tesbihi (3 Kere)', 10.3, TUR)
    ic += yazi(269, 46, '«Sübhâne rabbiye’l-a’lâ»', 10.1, LAC)
    ic += yazi(269, 68, '(Yüce Rabbim noksandan uzaktır)', 9.2, LAC, ince=True)
    return svg(360, 90, ic, 'Rükû ve secdede okunan tesbihler ve anlamları.', 15)


def iki_taharet_karsilastirma():
    ic = kutu(6, 6, 170, 78, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Hadesten Taharet', 10.4, MAVI)
    ic += yazi(91, 45, 'Hükmi / Manevi Temizlik', 9.9, LAC)
    ic += yazi(91, 66, 'Abdest · Gusül · Teyemmüm', 9.5, MAVI, ince=True)

    ic += kutu(184, 6, 170, 78, CAM_A, CAM)
    ic += yazi(269, 22, 'Necasetten Taharet', 10.4, CAM)
    ic += yazi(269, 45, 'Gözle Görülür Maddi Temizlik', 9.9, LAC)
    ic += yazi(269, 66, 'Beden · Elbise · Namaz Yeri', 9.5, CAM, ince=True)
    return svg(360, 90, ic, 'Hadesten taharet ve necasetten taharet karşılaştırması.', 15)


def bir_rekat_akis_kartlari():
    adimlar = [
        ('I. Adım', 'Rükû (Eğilme)', TUR, TUR_A),
        ('II. Adım', 'İftitah Tekbiri', MAVI, MAVI_A),
        ('III. Adım', 'İki Kez Secde', MOR, MOR_A),
        ('IV. Adım', 'Kıyam ve Kıraat', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 10.4, r)
        ic += yazi(x + 41, 55, alt, 9.6, LAC, ince=True)
    return svg(360, 84, ic, 'Bir rekâtın kılınışında yer alan dört temel rükün kartı.', 15)


def iki_rekat_ozet_panosu():
    ic = kutu(6, 6, 348, 80, MAVI_A, MAVI)
    ic += yazi(180, 22, 'İki Rekâtlık Namazın Kılınış Özeti', 10.6, MAVI)
    ic += yazi(180, 42, '• Vakit girince abdestli olarak kıbleye dönülüp niyet edilir.', 9.8, LAC, ince=True)
    ic += yazi(180, 59, '• 1. Rekât: Tekbir → Sübhaneke, Fatiha, Sure → Rükû → 2 Secde.', 9.8, LAC, ince=True)
    ic += yazi(180, 76, '• 2. Rekât Sonu: Tahiyyat, Salli-Barik, Rabbena → Sağa/Sola Selam.', 9.8, MAVI)
    return svg(360, 92, ic, 'İki rekâtlık namazın kılınış aşamaları bilgi panosu.', 16)


def secde_hadis_panosu():
    ic = kutu(6, 6, 348, 76, TUR_A, ALTIN)
    ic += yazi(180, 23, 'Hadis-i Şerif · Secde Bilinci', 10.5, TUR)
    ic += yazi(180, 46, '«Kulun Rabbine en yakın olduğu an secde hâlidir;', 10.0, LAC)
    ic += yazi(180, 65, 'öyleyse secdede çokça dua ediniz.» (Müslim, Salât, 215)', 9.7, LAC, ince=True)
    return svg(360, 88, ic, 'Secde anının önemini bildiren hadis-i şerif kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sart_rukun_karisik_sema()
    s[2]['gorsel'] = rukun_uygulama_kartlari()
    s[5]['gorsel'] = ahmet_hazirlik_listesi()
    s[6]['gorsel'] = ruku_secde_tesbih_karti()
    s[7]['gorsel'] = iki_taharet_karsilastirma()
    s[8]['gorsel'] = bir_rekat_akis_kartlari()
    s[9]['gorsel'] = iki_rekat_ozet_panosu()
    s[11]['gorsel'] = secde_hadis_panosu()
