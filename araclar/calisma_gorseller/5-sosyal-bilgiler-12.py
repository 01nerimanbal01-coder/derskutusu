"""5. sınıf Sosyal Bilgiler 12. hafta (Ülkemize Kara Sınırı Olan Komşu Devletler ve Sınır Kapıları) görselleri.
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
        ('1. Batı (Avrupa) Sınırımız', 'Bulgaristan · Yunanistan', MAVI, MAVI_A),
        ('2. Kuzeydoğu ve Doğu Sınırımız', 'Gürcistan · Ermenistan · Nahçıvan · İran', YES, YES_A),
        ('3. Güney Sınırımız', 'Irak · Suriye (En uzun sınır)', TUR, TUR_A),
        ('4. Kuzey Kıyımız', 'Karadeniz (Kara sınırı değil)', CAM, CAM_A),
    ], 'Türkiye’nin yönlere göre kara sınırı komşuları şeması.')
    s[2]['gorsel'] = dortlu_kart([
        ('1. Bulgaristan', 'Sofya · Batı · Kapıkule', MAVI, MAVI_A),
        ('2. Gürcistan', 'Tiflis · Kuzeydoğu · Sarp', YES, YES_A),
        ('3. Irak', 'Bağdat · Güney · Habur', TUR, TUR_A),
        ('4. Suriye', 'Şam · Güney · Cilvegözü', MOR, MOR_A),
    ], 'Komşu ülkeler, başkentleri ve sınır kapıları bilgi kartları.')
    s[5]['gorsel'] = ikili_kart(
        'Enerji Hatları (BTC & TANAP)', 'Hazar petrolü ve doğal gazı', 'Bakü → Tiflis → Türkiye', TUR, TUR_A,
        'Demir İpek Yolu (BTK)', 'Bakü - Tiflis - Kars Hattı', 'Ortaklar: Azerbaycan & Gürcistan', YES, YES_A,
        'Azerbaycan, Gürcistan ve Türkiye arasındaki enerji ve demiryolu projeleri.'
    )
    s[6]['gorsel'] = ikili_kart(
        '1. Gümrük Tırı (Batı Rotası)', 'İstanbul → Edirne → Bulgaristan', 'En işlek kapı: Kapıkule', MAVI, MAVI_A,
        '2. Gümrük Tırı (Güney Rotası)', 'Şırnak → Irak (Bağdat)', 'Güney ticaret kapısı: Habur', TUR, TUR_A,
        'Batı ve güney ihracat rotalarındaki sınır kapıları.'
    )
    s[7]['gorsel'] = ikili_kart(
        'İhracat (Dış Satım Ürünlerimiz)', 'Otomotiv, beyaz eşya, makine', 'Tekstil, hazır giyim, gıda', YES, YES_A,
        'İthalat (Dış Alım Ürünlerimiz)', 'Doğal gaz, ham petrol', 'Enerji ve sanayi ham maddesi', MAVI, MAVI_A,
        'Türkiye’nin komşu ülkelerle ihracat ve ithalat ürünleri tablosu.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Kaynak Belirleme', 'Atlas, harita, resmî siteler', MAVI, MAVI_A),
        ('2. Bilgiyi Bulma', 'Başkent, sınır kapısı, ticaret', TUR, TUR_A),
        ('3. Bilgiyi Doğrulama', 'Farklı kaynaklarla karşılaştırma', YES, YES_A),
        ('4. Bilgileri Kaydetme', 'Harita ve tabloya işleme', MOR, MOR_A),
    ], 'Komşu devletler hakkında dört adımlı bilimsel araştırma süreci.')
    s[9]['gorsel'] = ikili_kart(
        'Batı ve Güney Sınırlarımız', 'Batı: Meriç Nehri doğal sınır', 'Güney: Suriye en uzun sınır (911 km)', CAM, CAM_A,
        'Doğu Sınırımız', 'Dağlık ve yüksek arazi yapısı', 'Gürbulak ve Dilucu geçit kapıları', YES, YES_A,
        'Kara sınırlarımızın fiziki ve coğrafi özellikleri kartı.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Ekonomik ve Ticari Katkı', 'Sınır ticareti, enerji ve ulaşım', 'Karşılıklı kalkınma ve turizm', MAVI, MAVI_A,
        'İnsani ve Kültürel Katkı', 'Afetlerde yardımlaşma, barış', 'Kültürel bağlar ve güvenlik', YES, YES_A,
        'Komşu devletlerle barışçıl ilişkilerin ekonomik ve insani katkıları.'
    )
