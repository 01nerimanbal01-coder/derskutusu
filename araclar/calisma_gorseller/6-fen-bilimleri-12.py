"""6. sınıf Fen Bilimleri 12. hafta (İç Salgı Bezleri, Ergenlik Dönemi ve Sistemlerin Sağlığı) görselleri.
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
        'Yemek Sonrası Yüksek Şeker', 'Pankreas → K Hormonu salgılar', 'Kan şekerini normale düşürür', MAVI, MAVI_A,
        'Uzun Açlıkta Düşük Şeker', 'Pankreas → L Hormonu salgılar', 'Kan şekerini normale yükseltir', TUR, TUR_A,
        'Pankreas hormonlarının (K: İnsülin, L: Glukagon) kan şekeri dengesi şeması.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Boy-Kilo Artışı ve Sivilce', 'Kız ve Erkeklerde Ortak (Bedensel)', MAVI, MAVI_A),
        ('2. Ses Kalınlaşması', 'Yalnız Erkeklerde (Bedensel)', TUR, TUR_A),
        ('3. Yumurta Oluşumu', 'Yalnız Kızlarda (Bedensel)', MOR, MOR_A),
        ('4. Kimlik Arayışı ve Duygular', 'Kız ve Erkeklerde Ortak (Ruhsal)', YES, YES_A),
    ], 'Ergenlik dönemi bedensel ve ruhsal değişim kartları.')
    s[5]['gorsel'] = dortlu_kart([
        ('1. Hipofiz Bezi (Beyin Tabanı)', 'Büyüme hormonu + Bezlerin yöneticisi', MOR, MOR_A),
        ('2. Tiroit Bezi (Soluk Borusu Önü)', 'Tiroksin → Metabolizma hızı', MAVI, MAVI_A),
        ('3. Böbrek Üstü Bezi', 'Adrenalin → Korku ve heyecan', KIR, KIR_A),
        ('4. Pankreas', 'İnsülin ve Glukagon → Kan şekeri', YES, YES_A),
    ], 'Dört temel iç salgı bezi ve görevleri kartı.')
    s[6]['gorsel'] = ikili_kart(
        'Ergenlikte Ruhsal Değişimler', 'Kimlik arayışı · Bağımsızlık isteği', 'Duygusal dalgalanmalar (Normaldir)', MOR, MOR_A,
        'Sağlıklı Geçiş Rehberi', 'Spor, sanat, müzik ve kitap okuma', 'Aile ve rehberlik servisiyle iletişim', YES, YES_A,
        'Ergenlik dönemini sağlıklı geçirme yolları kartı.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Sinir Sistemi Çalışma Özelliği', 'İletim: Sinir hücreleriyle ÇOK HIZLI', 'Etki Süresi: KISA SÜRELİ (Anlık)', MAVI, MAVI_A,
        'İç Salgı Bezleri Çalışma Özelliği', 'İletim: Kan yoluyla YAVAŞ', 'Etki Süresi: UZUN SÜRELİ', TUR, TUR_A,
        'Sinir sistemi ve iç salgı bezlerinin çalışma hızı ve etki süresi karşılaştırması.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Tehlikenin Algılanması', 'Duyu organları → Beyne iletim', MAVI, MAVI_A),
        ('2. Hormon Salgılanması', 'Böbrek üstü bezi → Adrenalin', TUR, TUR_A),
        ('3. Kan Yoluyla Taşınma', 'Adrenalin → Kalp ve akciğere', MOR, MOR_A),
        ('4. Vücut Tepkisi', 'Kalp ve solunum hızlanır', KIR, KIR_A),
    ], 'Korku ve heyecan anında adrenalin hormonunun etki basamakları.')
    s[9]['gorsel'] = ikili_kart(
        'Dış Salgı Görevi (Enzim)', 'Sindirim öz suyunu kanalla', 'ince bağırsağa gönderir', TUR, TUR_A,
        'İç Salgı Görevi (Hormon)', 'İnsülin ve glukagon hormonlarını', 'doğrudan kana verir → KARMA BEZ', YES, YES_A,
        'Pankreasın karma bez (iç ve dış salgı) yapısı şeması.'
    )
    s[11]['gorsel'] = dortlu_kart([
        ('1. Dengeli Beslenme ve İyot', 'Tiroit (guatr) ve diyabetten korunma', YES, YES_A),
        ('2. Düzenli ve Yeterli Uyku', 'Büyüme hormonunun düzenli salgısı', MAVI, MAVI_A),
        ('3. Spor ve Stresten Uzak Durma', 'Sinir ve hormon dengesini koruma', CAM, CAM_A),
        ('4. Zararlı Alışkanlıklardan Kaçınma', 'Beyin ve organ sağlığını koruma', KIR, KIR_A),
    ], 'Denetleyici ve düzenleyici sistemlerin sağlığını koruma kuralları.')
