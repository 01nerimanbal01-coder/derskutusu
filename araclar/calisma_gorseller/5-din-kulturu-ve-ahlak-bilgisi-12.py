"""5. sınıf Din Kültürü ve Ahlak Bilgisi 12. hafta (Namazın İnsana Kazandırdıkları ve Tahiyyat Duası) görselleri.
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
        'Hadis-i Şerif Benzetmesi', 'Günde 5 Kez Nehirde Yıkanmak', 'Maddi kirlerden arınma', CAM, CAM_A,
        'Beş Vakit Namaz', 'Abdest + Manevi Huzur', 'Hata ve günahlardan arınma', YES, YES_A,
        'Nehir benzetmesi ve beş vakit namazın temizlik kazandırması şeması.'
    )
    s[2]['gorsel'] = dortlu_kart([
        ('1. Bölüm: İbadetler', 'Ettehiyyâtü lillâhi vessalevâtü...', MAVI, MAVI_A),
        ('2. Bölüm: Peygamber’e Selam', 'Esselâmü aleyke eyyühen-nebiyyü...', YES, YES_A),
        ('3. Bölüm: Salih Kullara Selam', 'Esselâmü aleynâ ve alâ ibâdillâhis...', TUR, TUR_A),
        ('4. Bölüm: Kelime-i Şehadet', 'Eşhedü en lâ ilâhe illallah...', MOR, MOR_A),
    ], 'Tahiyyat (Ettehiyyâtü) duasının dört ana bölümü.')
    s[5]['gorsel'] = ikili_kart(
        'Bireysel Kazanımlar', 'Manevi huzur ve iç güven', 'Temizlik + Zaman disiplini', MAVI, MAVI_A,
        'Toplumsal Kazanımlar (?)', 'Cemaatle aynı safta eşitlik', '? → Kardeşlik ve dayanışma', YES, YES_A,
        'Namazın bireysel ve toplumsal kazanımları karşılaştırma şeması.'
    )
    s[6]['gorsel'] = ikili_kart(
        'Tahiyyat Duası 3. Cümle', '« ... ve alâ ibâdillâhis-sâlihîn »', 'Boşluğa gelecek ifade hangisidir?', MOR, MOR_A,
        'Cümlenin Anlamı', 'Selam bize ve Allah’ın', 'salih (iyi) kullarına olsun.', TUR, TUR_A,
        'Tahiyyat duasındaki selam cümlesi tamamlama kartı.'
    )
    s[7]['gorsel'] = ikili_kart(
        'Ankebût Suresi, 45. Ayet', '«Şüphesiz namaz, insanı', 'hayâsızlıktan ve kötülükten alıkoyar.»', YES, YES_A,
        'Ahlaki Yansıması', 'Doğruluk, dürüstlük, tevazu', 'Kötü söz ve hileden kaçınma', MAVI, MAVI_A,
        'Ankebût suresi 45. ayet ve ahlaki olgunluk kartı.'
    )
    s[8]['gorsel'] = dortlu_kart([
        ('1. Sözlü-Bedeni-Mali İbadet', 'Ettehiyyâtü lillâhi...', MAVI, MAVI_A),
        ('2. Hz. Peygamber’e Selam', 'Esselâmü aleyke eyyühen-nebiyyü...', YES, YES_A),
        ('3. Bize ve Salihlere Selam', 'Esselâmü aleynâ ve alâ...', TUR, TUR_A),
        ('4. Tevhit ve Şehadet', 'Eşhedü en lâ ilâhe illallah...', MOR, MOR_A),
    ], 'Tahiyyat duasının okunuş sırası kartları.')
    s[9]['gorsel'] = ikili_kart(
        '2. Rekat Sonu (İlk Oturuş)', 'Ka’de-i Ûlâ', 'Tahiyyat duası okunur', MAVI, MAVI_A,
        '4. Rekat Sonu (Son Oturuş)', 'Ka’de-i Ahîre', 'Tahiyyat + Salli-Barik + Rabbena', YES, YES_A,
        'Dört rekatlık namazda Tahiyyat duasının okunduğu oturuşlar.'
    )
    s[11]['gorsel'] = dortlu_kart([
        ('Sabah · Öğle · İkindi', 'Gündüzü planlama disiplini', MAVI, MAVI_A),
        ('Akşam · Yatsı', 'Akşamı ve dinlenmeyi planlama', MOR, MOR_A),
        ('Günde 5 Vakit Abdest', 'El, yüz, ayak ve beden temizliği', CAM, CAM_A),
        ('Elbise ve Secde Yeri', 'Çevre ve kıyafet temizliği bilinci', YES, YES_A),
    ], 'Beş vakit namaz çizelgesinin zaman ve temizlik bilincine katkısı.')
