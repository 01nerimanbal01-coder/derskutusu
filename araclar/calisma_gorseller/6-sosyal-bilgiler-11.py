"""6. sınıf Sosyal Bilgiler 11. hafta (Orta Asya’da Kurulan İlk Türk Devletlerinin Coğrafi, Siyasi, Ekonomik ve Kültürel Özellikleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-11 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=16):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.3, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def turkistan_cografya_semasi():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, 'Coğrafi Neden (Türkistan)', 10.0, MAVI)
    ic += yazi(91, 44, 'Sert karasal iklim ve', 9.4, LAC, ince=True)
    ic += yazi(91, 64, 'geniş bozkırlar (otlaklar)', 9.4, MAVI)

    ic += kutu(184, 6, 170, 76, YES_A, YES)
    ic += yazi(269, 22, 'Yaşam ve Sanat Sonucu', 10.0, YESIL_K)
    ic += yazi(269, 44, 'Hayvancılık · Yaylak-Kışlak', 9.4, LAC)
    ic += yazi(269, 64, 'Yurt çadırı · Taşınabilir sanat', 9.2, YESIL_K, ince=True)
    return svg(360, 88, ic, 'Türkistan coğrafyasının konargöçer yaşam ve sanata etkisi şeması.', 15)


def uc_turk_devleti_panosu():
    kartlar = [
        ('1. Asya Hun', 'Teoman · Metehan', MAVI, MAVI_A),
        ('2. Kök Türk', 'Bumin · Bilge Kağan', YES, YES_A),
        ('3. Uygurlar', 'Bögü Kağan · Yerleşik', TUR, TUR_A),
        ('4. Orhun Anıtı', 'II. Kök Türk Yazıtı', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.9, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 55, alt, 9.0, LAC, ince=True)
    return svg(360, 84, ic, 'Asya Hun, Kök Türk ve Uygur devletleri bilgi panosu.', 15)


def bilge_kagan_orhun_karti():
    ic = kutu(6, 6, 348, 76, CAM_A, CAM)
    ic += yazi(180, 22, 'ORHUN YAZITLARI · BİLGE KAĞAN ANITI (735)', 10.2, CAM)
    ic += yazi(180, 44, '“Türk milleti için gece uyumadım, gündüz oturmadım;', 9.6, LAC)
    ic += yazi(180, 64, 'çıplak milleti giydirdim, fakir milleti zengin kıldım.”', 9.6, CAM)
    return svg(360, 88, ic, 'Orhun Yazıtlarında sosyal devlet anlayışını yansıtan Bilge Kağan sözü.', 15)


def dort_kulturel_miras_karti():
    kartlar = [
        ('1. Pazırık Halısı', 'En eski düğümlü halı', MAVI, MAVI_A),
        ('2. Altın Elbiseli Adam', 'Esik Kurganı · Zırh', YES, YES_A),
        ('3. 12 Hayvanlı Takvim', 'Güneş yılı · Astronomi', MOR, MOR_A),
        ('4. Sulama Kanalları', 'Uygur tarım faaliyeti', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 44
        ic += kutu(x, y, 172, 38, z, r)
        ic += yazi(x + 86, y + 15, bas, 10.0, r)
        ic += yazi(x + 86, y + 31, alt, 9.2, LAC, ince=True)
    return svg(360, 94, ic, 'Pazırık Halısı, Altın Elbiseli Adam, Takvim ve Sulama Kanalları kartları.', 16)


def tore_hukuk_ustunlugu_karti():
    ic = kutu(6, 6, 348, 76, MOR_A, MOR)
    ic += yazi(180, 22, 'TÜRK DEVLET GELENEĞİNDE TÖRE VE ADALET', 10.2, MOR)
    ic += yazi(180, 44, 'Atasözü: “İl (devlet) gider, töre (hukuk) kalır.”', 9.8, LAC)
    ic += yazi(180, 65, 'Temel İlkeler: Könilik (Adalet), Uzluk (İyilik), Tüzlük (Eşitlik)', 9.3, MOR, ince=True)
    return svg(360, 88, ic, 'İlk Türk devletlerinde töre ve hukukun üstünlüğü kartı.', 15)


def tarihsel_kronoloji_seridi():
    adimlar = [
        ('MÖ 209 · Hun', 'Metehan &amp; Onlu Sistem', MAVI, MAVI_A),
        ('552 · I. Kök Türk', 'Bumin Kağan kurdu', YES, YES_A),
        ('682 · II. Kök Türk', 'Kutluk &amp; Orhun Anıtı', TUR, TUR_A),
        ('744 · Uygurlar', 'Yerleşik yaşam &amp; Matbaa', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 72, z, r)
        ic += yazi(x + 41, 24, bas, 9.4, r)
        ic += yazi(x + 41, 54, alt, 8.8, LAC, ince=True)
    return svg(360, 84, ic, 'Asya Hun, I. Kök Türk, II. Kök Türk ve Uygur kronoloji şeridi.', 15)


def kokturk_uygur_karsilastirma():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 21, 'Kök Türk Devleti', 10.2, MAVI)
    ic += yazi(91, 42, '• Yaşam: Konargöçer (Yurt çadırı)', 9.1, LAC, ince=True)
    ic += yazi(91, 62, '• 38 harfli Kök Türk Alfabesi', 9.1, MAVI)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 21, 'Uygur Devleti', 10.2, TUR)
    ic += yazi(269, 42, '• Yaşam: Yerleşik (Şehir, saray, tarım)', 9.0, LAC, ince=True)
    ic += yazi(269, 62, '• 18 harfli alfabe, kâğıt ve matbaa', 9.0, TUR)
    return svg(360, 88, ic, 'Kök Türk ve Uygur devletlerinin yaşam tarzı ve kültür karşılaştırması.', 15)


def metehan_vatan_sevgisi_karti():
    ic = kutu(6, 6, 348, 76, YES_A, YES)
    ic += yazi(180, 22, 'METEHAN’IN VATAN TOPRAĞI ANLAYIŞI', 10.2, YESIL_K)
    ic += yazi(180, 44, 'Komşu devlet Metehan’dan önce değerli atını, sonra çorak bir toprağı ister.', 9.4, LAC, ince=True)
    ic += yazi(180, 65, 'Metehan: “Toprak devletin temelidir ve milletin malıdır; onu kimseye veremem!”', 9.4, YESIL_K)
    return svg(360, 88, ic, 'Metehanın vatan toprağını milletin malı sayan tarihi sözü kartı.', 15)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = turkistan_cografya_semasi()
    s[2]['gorsel'] = uc_turk_devleti_panosu()
    s[5]['gorsel'] = bilge_kagan_orhun_karti()
    s[6]['gorsel'] = dort_kulturel_miras_karti()
    s[7]['gorsel'] = tore_hukuk_ustunlugu_karti()
    s[8]['gorsel'] = tarihsel_kronoloji_seridi()
    s[9]['gorsel'] = kokturk_uygur_karsilastirma()
    s[11]['gorsel'] = metehan_vatan_sevgisi_karti()
