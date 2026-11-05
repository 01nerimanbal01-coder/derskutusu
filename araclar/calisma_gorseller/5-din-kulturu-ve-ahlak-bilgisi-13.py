"""5. sınıf Din Kültürü ve Ahlak Bilgisi 13. hafta (Hz. İbrahim Kıssası ve 2. Ünite Değerlendirmesi) görselleri.
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
    s[1]['gorsel'] = dortlu_kart([
        ('1. Gözlem: Yıldız', 'Doğup batıyor → İlah olamaz', MAVI, MAVI_A),
        ('2. Gözlem: Ay', 'Kaybolup gidiyor → İlah olamaz', MOR, MOR_A),
        ('3. Gözlem: Güneş', 'Batıp sönüyor → İlah olamaz', TUR, TUR_A),
        ('4. Sonuç: Tevhid İnancı', 'Evreni yaratan tek Allah’tır', YES, YES_A),
    ], 'Hz. İbrahim’in gök cisimlerini gözlemleyerek tevhide ulaşması.')
    s[2]['gorsel'] = ikili_kart(
        'Hazırlık Şartları (Dıştan 6)', 'Hadesten ve Necasetten Taharet', 'Setr-i Avret · Kıble · Vakit · Niyet', MAVI, MAVI_A,
        'Kılınış Şartları (İçten 6)', 'İftitah Tekbiri · Kıyam · Kıraat', 'Rükû · Secde · Ka’de-i Ahîre', YES, YES_A,
        'Namazın 6 hazırlık ve 6 kılınış şartı özet kartı.'
    )
    s[5]['gorsel'] = ikili_kart(
        'Rabbena لجعلنا (İbrahim 40)', 'Rabbic’alnî mukîmes-salâti...', 'Beni ve soyumu namaz kılan eyle', CAM, CAM_A,
        'Rabbenağfirlî (İbrahim 41)', 'Rabbenağfirlî ve li-vâlideyye...', 'Beni, annemi-babamı ve müminleri affet', MOR, MOR_A,
        'Hz. İbrahim’in Kur’an’da yer alan namaz ve bağışlanma duaları.'
    )
    s[6]['gorsel'] = dortlu_kart([
        ('1. Bölüm: Övgü ve İbadet', 'Et-tahiyyâtü lillâhi ves-salevâtü...', MAVI, MAVI_A),
        ('2. Bölüm: Selamlaşma', 'Es-selâmü aleyke eyyühen-nebiyyü...', YES, YES_A),
        ('3. Bölüm: Kelime-i Şehadet', 'Eşhedü en lâ ilâhe illallah...', TUR, TUR_A),
        ('Okunduğu Yer', 'Namazların ilk ve son oturuşu', MOR, MOR_A),
    ], 'Tahiyyat duasının üç anlam bölümü ve okunduğu yer.')
    s[7]['gorsel'] = ikili_kart(
        'Sorgulama Yöntemi', 'Putlar konuşamaz ve duyamaz', 'Kendilerini dahi koruyamazlar', KIR, KIR_A,
        'Verilen Mesaj (Enbiyâ 66-67)', 'Fayda ve zarar vermeyene tapılmaz', 'Akıl ile Tevhid gerçeği kavranır', YES, YES_A,
        'Putperestliğin akıl ve tevhid ilkesiyle sorgulanması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Akıl Yürütme ve Tevhid', 'Gök cisimlerinden Tevhide ulaşma', MAVI, MAVI_A),
        ('2. Tebliğ Mücadelesi', 'Babil halkını ve Nemrut’u davet', TUR, TUR_A),
        ('3. Ateş Mucizesi (Enbiyâ 69)', 'Ateşin serin ve güvenli olması', KIR, KIR_A),
        ('4. Kâbe’nin İnşası (Mekke)', 'Hz. İsmail ile Beytullah yapımı', YES, YES_A),
    ], 'Hz. İbrahim kıssasındaki temel olayların kronolojik akışı.')
    s[9]['gorsel'] = dortlu_kart([
        ('1. Adım: Tahiyyat Duası', 'Selam ve Kelime-i Şehadet', MAVI, MAVI_A),
        ('2. Adım: Salli ve Barik', 'Peygamberimize salavat duaları', MOR, MOR_A),
        ('3. Adım: Rabbena Duaları', 'Hz. İbrahim’in af ve namaz duası', YES, YES_A),
        ('4. Adım: Selam Verme', 'Sağa ve sola selam ile bitiş', TUR, TUR_A),
    ], 'Namazın son oturuşunda (ka’de-i ahîre) okunan dualar sırası.')
    s[11]['gorsel'] = ikili_kart(
        'Bireysel Kazanımlar', 'Beden-elbise temizliği · Zaman bilinci', 'Kötülüklerden uzaklaşma (Ankebût 45)', MAVI, MAVI_A,
        'Toplumsal Kazanımlar', 'Cemaatle omuz omuza eşitlik', 'Sevgi, yardımlaşma ve kardeşlik', YES, YES_A,
        'Namaz ibadetinin bireysel ve toplumsal faydaları.'
    )
