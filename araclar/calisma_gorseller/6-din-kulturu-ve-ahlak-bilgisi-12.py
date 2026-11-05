"""6. sınıf Din Kültürü ve Ahlak Bilgisi 12. hafta (Hz. Davud (as) ve Fil Suresi) görselleri.
SVG; insan figürü yok (K024); beyaz bant yok (K178)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#d97706', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
FONT = 'font-family="Noto Sans, sans-serif" font-size="11.5"'
AR_FONT = 'direction="rtl" unicode-bidi="isolate" lang="ar" font-family="Arial, sans-serif" font-size="18.5" font-weight="700"'


def svg(ic, etiket, w=360, h=115, mm=20):
    return f'<svg viewBox="0 0 {w} {h}" style="max-height:{mm}mm" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"/>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    ag = '700' if kalin else '500'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {FONT} font-weight="{ag}" fill="{renk}">{metin}</text>'


def ar_yazi(x, y, metin, renk=LAC, hiza='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {AR_FONT} fill="{renk}">{metin}</text>'


def ikili_kart(b1, s1a, s1b, r1, z1, b2, s2a, s2b, r2, z2, etiket, ar1=False, ar2=False):
    ic = kutu(6, 6, 170, 103, z1, r1)
    ic += yazi(91, 28, b1, r1, kalin=True)
    ic += (ar_yazi(91, 60, s1a, LAC) if ar1 else yazi(91, 58, s1a, LAC, kalin=True))
    ic += yazi(91, 90, s1b, r1)
    ic += kutu(184, 6, 170, 103, z2, r2)
    ic += yazi(269, 28, b2, r2, kalin=True)
    ic += (ar_yazi(269, 60, s2a, LAC) if ar2 else yazi(269, 58, s2a, LAC, kalin=True))
    ic += yazi(269, 90, s2b, r2)
    return svg(ic, etiket)


def dortlu_kart(kartlar, etiket, ar=False):
    konum = [(6, 6), (184, 6), (6, 60), (184, 60)]
    ic = ''
    for (x, y), (b1, b2, r, z) in zip(konum, kartlar):
        ic += kutu(x, y, 170, 48, z, r)
        ic += yazi(x + 85, y + 18, b1, r, kalin=True)
        ic += (ar_yazi(x + 85, y + 41, b2, LAC) if ar else yazi(x + 85, y + 39, b2, LAC))
    return svg(ic, etiket)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = ikili_kart(
        'Hadis-i Şerif (Buhârî)', '«Hiç kimse kendi elinin emeğinden', 'daha hayırlı bir rızık yememiştir.»', YES, YES_A,
        'Hz. Davud’un (as) Mesleği', 'Demiri yumuşatıp zırh yapma', 'Alın teri ve helal kazanç', TUR, TUR_A,
        'El emeği hadisi ve Hz. Davud’un demircilik/zırh sanatı kartı.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Ayet: Ashâb-ı Fîl', 'Elem tera keyfe fe’ale rabbüke...', MAVI, MAVI_A),
        ('2. Ayet: Tuzakların Bozulması', 'Elem yec’al keydehüm fî tadlîl', TUR, TUR_A),
        ('3. Ayet: Ebâbîl Kuşları', 'Ve ersele aleyhim tayran ebâbîl', YES, YES_A),
        ('4-5. Ayet: Siccîl ve Asfin Me’kûl', 'Termîhim... ke’asfin me’kûl', MOR, MOR_A),
    ], 'Fil suresinin beş ayetinin okunuş ve anlam kartları.')
    s[5]['gorsel'] = dortlu_kart([
        ('İlahi Kitabı: Zebur', 'Dört büyük kitaptan biri', MAVI, MAVI_A),
        ('İbadeti: Davud Orucu', 'Bir gün oruç, bir gün iftar', YES, YES_A),
        ('Yönetimi: Adalet ve Hikmet', 'Kudüs merkezli adil yönetim', MOR, MOR_A),
        ('Mucize ve Sanatı: ?', 'Demiri ateşsiz işleyip zırh yapma', TUR, TUR_A),
    ], 'Hz. Davud’un (as) temel özelliklerini özetleyen dörtlü şema.')
    s[6]['gorsel'] = ikili_kart(
        'Fil Suresi 3. Ayet Tamamlama', '«Ve ersele aleyhim ...»', 'Boşluğa gelecek ifade hangisidir?', MAVI, MAVI_A,
        'Ayetin Türkçe Anlamı', '«Üzerlerine sürü sürü (Ebâbîl)', 'kuşlar gönderdi.»', YES, YES_A,
        'Fil suresi 3. ayet okuma ve anlam tamamlama kartı.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Fil Olayı (Milattan Sonra 571)', 'Yemen Valisi Ebrehe’nin ordusu', 'Amaç: Kâbe’yi yıkmak', KIR, KIR_A,
        'İlahi Yardım ve Sonuç', 'Ebâbîl kuşları ve siccîl taşları', 'Kâbe korundu, ordu helak oldu', YES, YES_A,
        '571 Fil Olayı’nın nedeni ve sonucu bilgi kartı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Ayet', '... bi-ashâbil-fîl', MAVI, MAVI_A),
        ('2. Ayet', '... keydehüm fî tadlîl', TUR, TUR_A),
        ('3-4. Ayetler', '... tayran ebâbîl / min siccîl', YES, YES_A),
        ('5. Ayet', '... ke’asfin me’kûl', MOR, MOR_A),
    ], 'Fil suresi ayetlerinin sıralama kartları.')
    s[9]['gorsel'] = ikili_kart(
        'Hz. Davud (as) Kıssası', 'Zalim Calut’a karşı iman ve cesaret', 'Adalet, ibadet ve tevekkül', MAVI, MAVI_A,
        'Fil Suresi Mesajı', 'Kibirli Ebrehe’ye karşı ilahi kudret', 'Allah’ın (c.c.) gücü her şeyin üstündedir', YES, YES_A,
        'Hz. Davud kıssası ve Fil suresinin ortak mesajı.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Hükümdarlık ve Kamu Emaneti', 'Devlet hazinesine dokunmama', 'Halk arasında adaletle hükmetme', MAVI, MAVI_A,
        'El Emeği ve Çalışma Ahlakı', 'Zırh yapıp satarak geçinme', 'Üretkenlik ve helal rızık bilinci', YES, YES_A,
        'Hz. Davud’un hükümdarlığı ve kendi el emeğiyle geçinmesi şeması.'
    )
