"""7. sınıf Türkçe 9. hafta (Mustafa 1881-1920 Tarihe Atılan İmza, Düşünceyi Geliştirme Yolları, Söz Sanatları, Kip ve Kişi Ekleri) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10-10.5 pt Noto Sans (K150 EK)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=15):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=10.2, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def ikna_ve_dusunce_karti():
    ic = kutu(6, 6, 348, 76, MAVI_A, MAVI)
    ic += yazi(180, 22, 'Metin Kesiti · Tarihe Atılan İmza', 10.3, MAVI)
    ic += yazi(180, 42, '«Atatürk, "Egemenlik kayıtsız şartsız milletindir." sözüyle', 9.5, LAC, ince=True)
    ic += yazi(180, 58, 'yönetimi millete vermiş; 23 Nisan 1920’de 1. Mecliste', 9.5, LAC, ince=True)
    ic += yazi(180, 74, '300’ü aşkın milletvekili halkı temsil etmiştir.»', 9.5, KIR)
    return svg(360, 88, ic, 'Tanık gösterme ve sayısal veriler içeren metin kartı.', 15)


def dort_cekimli_fiil_fisi():
    kartlar = [
        ('1. Fiş', 'oku - du - k', MAVI, MAVI_A),
        ('2. Fiş', 'çalış - malı - sınız', TUR, TUR_A),
        ('3. Fiş', 'vazgeç - mez', YES, YES_A),
        ('4. Fiş', 'dinle - se - k', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 10.0, r)
        ic += f'<line x1="{x + 8}" y1="32" x2="{x + 74}" y2="32" stroke="{r}" stroke-width="0.9"/>'
        ic += yazi(x + 41, 54, alt, 9.2, LAC, ince=True)
    return svg(360, 82, ic, 'Dört çekimli fiilin kök, kip ve kişi ayrımı fişleri.', 14)


def uc_soz_sanati_panosu():
    dizeler = [
        ('I. Cümle', '«Kükreyen bir aslan gibi şahlandı Mehmetçik.»', MAVI, MAVI_A),
        ('II. Cümle', '«Yorgun gemi, hırçın dalgalarla dertleşti.»', YES, YES_A),
        ('III. Cümle', '«Bir ah çeksem karşıki dağlar yıkılır.»', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, dize, r, z) in enumerate(dizeler):
        y = 4 + i * 28
        ic += kutu(6, y, 348, 25, z, r, 6)
        ic += yazi(44, y + 16, bas, 9.8, r)
        ic += yazi(210, y + 16, dize, 9.4, LAC, ince=True)
    return svg(360, 90, ic, 'Benzetme, kişileştirme ve abartma içeren üç cümle panosu.', 15)


def haber_dilek_dort_kart():
    kutular = [
        ('1. Kart', 'Samsun’a çıktı (-tı)', MAVI, MAVI_A),
        ('2. Kart', 'Belgeseli izliyorlar (-yor)', YES, YES_A),
        ('3. Kart', 'Özenle koruyalım (-a-lım)', KIR, KIR_A),
        ('4. Kart', 'Ziyaret edeceğiz (-ecek)', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, icerik, r, z) in enumerate(kutular):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 42
        ic += kutu(x, y, 172, 36, z, r)
        ic += yazi(x + 86, y + 14, bas, 10.0, r)
        ic += yazi(x + 86, y + 29, icerik, 9.5, LAC, ince=True)
    return svg(360, 90, ic, 'Haber ve dilek kipleriyle çekimlenmiş dört fiil kartı.', 15)


def yazim_denetim_levhasi():
    ic = kutu(6, 6, 348, 74, KIR_A, KIR)
    ic += yazi(180, 22, 'Yazım Denetimi · Hatalı Sözcükleri Bulunuz', 10.2, KIR)
    ic += yazi(180, 44, '«Gazi Mustafa Kemal, 23 nisan 1920’de ankara’da', 9.5, LAC, ince=True)
    ic += yazi(180, 64, 'Büyük Millet Meclisini açarak milli mücadeleyi taçlandırdı.»', 9.5, LAC, ince=True)
    return svg(360, 86, ic, 'Tarih, yer adı ve tarihî dönem yazım yanlışlarını içeren kart.', 14)


def tarihe_imza_olay_seridi():
    adimlar = [
        ('1. Eğitim', 'Harp Akademisi', MAVI, MAVI_A),
        ('2. 1915', 'Çanakkale Zaferi', YES, YES_A),
        ('3. 19 Mayıs 1919', 'Samsun’a Çıkış', TUR, TUR_A),
        ('4. 23 Nisan 1920', 'TBMM’nin Açılışı', KIR, KIR_A),
    ]
    ic = ''
    for i, (bas, alt, r, z) in enumerate(adimlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 70, z, r)
        ic += yazi(x + 41, 24, bas, 9.8, r)
        ic += yazi(x + 41, 52, alt, 9.1, LAC, ince=True)
    return svg(360, 82, ic, 'Mustafa 1881-1920 Tarihe Atılan İmza kronolojik olay şeridi.', 14)


def kip_kisi_cozumleme_tablosu():
    ic = kutu(6, 6, 170, 76, MAVI_A, MAVI)
    ic += yazi(91, 22, '1 ve 2. Çözümleme', 10.1, MAVI)
    ic += yazi(91, 43, '1) anla-dı-k : Geçmiş · Biz', 9.3, LAC, ince=True)
    ic += yazi(91, 63, '2) gel-iyor-sunuz : Şimdiki · Siz', 9.3, LAC, ince=True)

    ic += kutu(184, 6, 170, 76, TUR_A, TUR)
    ic += yazi(269, 22, '3 ve 4. Çözümleme', 10.1, TUR)
    ic += yazi(269, 43, '3) bırak-maz : Geniş (-) · O', 9.3, LAC, ince=True)
    ic += yazi(269, 63, '4) çalış-a-lım : Emir · Sen (!)', 9.3, KIR)
    return svg(360, 88, ic, 'Dört çekimli fiilin kip ve kişi çözümleme tablosu.', 15)


def haber_dilek_karsilastirma_karti():
    ic = kutu(6, 6, 170, 74, YES_A, YES)
    ic += yazi(91, 22, '1. Fiil: «okuyoruz»', 10.2, YES)
    ic += yazi(91, 43, 'oku - yor - uz', 9.6, LAC)
    ic += yazi(91, 64, 'Kip Grubu: ?  ·  Anlamı: ?', 9.4, YES, ince=True)

    ic += kutu(184, 6, 170, 74, MOR_A, MOR)
    ic += yazi(269, 22, '2. Fiil: «okumalıyız»', 10.2, MOR)
    ic += yazi(269, 43, 'oku - malı - yız', 9.6, LAC)
    ic += yazi(269, 64, 'Kip Grubu: ?  ·  Anlamı: ?', 9.4, MOR, ince=True)
    return svg(360, 86, ic, 'okuyoruz ve okumalıyız fiillerinin kip ve anlam karşılaştırması.', 14)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ikna_ve_dusunce_karti()
    s[2]['gorsel'] = dort_cekimli_fiil_fisi()
    s[5]['gorsel'] = uc_soz_sanati_panosu()
    s[6]['gorsel'] = haber_dilek_dort_kart()
    s[7]['gorsel'] = yazim_denetim_levhasi()
    s[8]['gorsel'] = tarihe_imza_olay_seridi()
    s[9]['gorsel'] = kip_kisi_cozumleme_tablosu()
    s[11]['gorsel'] = haber_dilek_karsilastirma_karti()
