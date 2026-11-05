"""6. sınıf Sosyal Bilgiler 12. hafta (Türk Dünyasıyla İş Birlikleri ve İlk Türk Devletleri) görselleri.
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
        ('TDT (Türk Devletleri Teşkilatı)', 'Siyasi, ekonomik ve stratejik çatı', MAVI, MAVI_A),
        ('TİKA', 'Kalkınma ve tarihî eser restorasyonu', TUR, TUR_A),
        ('TÜRKSOY', 'Ortak kültür, sanat ve festivaller', MOR, MOR_A),
        ('Maarif Vakfı & Yunus Emre Enst.', 'Okul, üniversite ve Türkçe eğitimi', YES, YES_A),
    ], 'Türkiye’nin Türk dünyasıyla iş birliği yürüttüğü dört temel kurum.')
    s[2]['gorsel'] = dortlu_kart([
        ('1. Asya Hun Devleti', 'Teoman / Mete Han · Onlu Sistem', MAVI, MAVI_A),
        ('2. Kök Türk Devletleri', 'Bumin / Bilge Kağan · Orhun Yazıtları', YES, YES_A),
        ('3. Uygur Devleti', 'Yerleşik hayat · Matbaa ve kâğıt', TUR, TUR_A),
        ('4. Kurgan Mirası', 'Esik (Altın Elbiseli) · Pazırık Halısı', MOR, MOR_A),
    ], 'Türkistan’da kurulan ilk Türk devletleri ve kültür mirası kartları.')
    s[5]['gorsel'] = ikili_kart(
        'Esik Kurganı Buluntusu', 'Altın Elbiseli Adam Zırhı', 'Kanıt: İleri maden ve altın işçiliği', TUR, TUR_A,
        'Pazırık Kurganı Buluntusu', 'Dünyanın en eski düğümlü halısı', 'Kanıt: İleri dokumacılık sanatı', MOR, MOR_A,
        'Esik ve Pazırık kurganlarından çıkan maden ve dokuma eserleri.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Orhun Yazıtları (Bilge Kağan)', '«Aç milleti doyurdum, çıplak milleti', 'giydirdim, az milleti çoğalttım.»', MAVI, MAVI_A,
        'Yönetim İlkemiz', 'Halkın refah ve mutluluğu', 'Anlayış: Sosyal Devlet Anlayışı', YES, YES_A,
        'Orhun Yazıtları’ndaki sosyal devlet anlayışı metin kartı.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Mete Han ve Onlu Sistem (MÖ 209)', 'Onbaşı → Yüzbaşı → Binbaşı → Tümen', 'Disiplinli ve hızlı hareket yeteneği', MAVI, MAVI_A,
        'Günümüze Mirası', 'Türk Kara Kuvvetleri kuruluş yılı', 'Modern dünya ordularına örnek model', TUR, TUR_A,
        'Mete Han’ın Onlu askeri sistemi ve günümüz ordularına etkisi.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('MÖ 220 / MÖ 209', 'Asya Hun Devleti ve Onlu Sistem', MAVI, MAVI_A),
        ('MS 552', 'I. Kök Türk Devleti’nin kuruluşu', YES, YES_A),
        ('MS 720–735', 'II. Kök Türk ve Orhun Yazıtları', TUR, TUR_A),
        ('MS 744', 'Uygur Devleti ve yerleşik yaşam', MOR, MOR_A),
    ], 'İlk Türk devletleri kronolojik zaman şeridi.')
    s[9]['gorsel'] = ikili_kart(
        'Hun ve Kök Türk (Konargöçer)', 'Çadır (Yurt) ve taşınabilir sanat', 'Hayvancılık, dokuma ve maden', MAVI, MAVI_A,
        'Uygur Devleti (Yerleşik Yaşam)', 'Ordu-Balık şehri, saray ve tapınak', 'Tarım, duvar resmi (fresk) ve matbaa', YES, YES_A,
        'Konargöçer bozkır yaşamı ile Uygur yerleşik yaşamının karşılaştırması.'
    )
    s[11]['gorsel'] = ikili_kart(
        'Ortak Tarih, Dil ve Kültür', 'Dede Korkut, Orhun, Nevruz', 'Kardeşlik ve karşılıklı güven', MOR, MOR_A,
        'Günümüz Ortak Projeleri (TDT)', 'Orta Koridor ulaşım ve enerji', 'Ortak alfabe, eğitim ve ticaret', YES, YES_A,
        'Türk Devletleri Teşkilatı ortak kültür mirası ve güncel iş birlikleri.'
    )
