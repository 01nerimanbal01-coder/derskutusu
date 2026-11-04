"""5. sınıf DKAB 8. hafta (Allah'ın Huzurunda Olmak: Namaz İbadeti ve Hükmüne Göre Namazlar) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 12 pt Noto Sans (K150 EK); kesir yok (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
ALTIN, YESIL_K = '#c9a227', '#0f6b45'
TR_FONT = 'font-family="Noto Sans, sans-serif" font-size="12"'


def svg(w, h, ic, etiket, en_fazla=18):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, renk=LAC, hiza='middle', kalin=False):
    agirlik = ' font-weight="700"' if kalin else ' font-weight="500"'
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" {TR_FONT}{agirlik} fill="{renk}">{metin}</text>'


def hukmune_gore_namaz_sema():
    kutular = [
        ('1. Farz', '5 Vakit · K = ?', MAVI, MAVI_A),
        ('2. Vacip', 'Bayram · L = ?', TUR, TUR_A),
        ('3. Nafile', 'Sünnet · M = ?', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="36" x2="{x + 102}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 56, 66, alt, LAC)
    return svg(360, 98, ic, 'Hükmüne göre namazlar şeması: Farz K, Vacip L, Nafile M.', 21)


def namaz_hukum_panosu():
    satirlar = [
        ('1. Akşam', 'Farz-ı ayn', MAVI, MAVI_A),
        ('2. Vitir', 'Vacip namaz', TUR, TUR_A),
        ('3. Bayram', 'Farz-ı kifâye', KIR, '#fdeaea'),
        ('4. Kuşluk', 'Nafile namaz', YES, YES_A),
    ]
    ic = ''
    for i, (sol, sag, renk, arka) in enumerate(satirlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 12, y + 27, f'{sol} · {sag}', LAC, 'start', kalin=True)
    return svg(360, 106, ic, 'Dört namaz ve dinî hüküm eşleştirme panosu.', 21)


def dort_namaz_karti():
    kartlar = [
        ('1. Kart', 'Sabah', MAVI, MAVI_A),
        ('2. Kart', 'Cenaze', MOR, MOR_A),
        ('3. Kart', 'Bayram', TUR, TUR_A),
        ('4. Kart', 'Teravih', YES, YES_A),
    ]
    ic = ''
    for i, (bas, ad, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 10}" y1="36" x2="{x + 72}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 41, 66, ad, LAC)
    return svg(360, 96, ic, 'Dört namaz kartı: Sabah, Cenaze, Bayram ve Teravih.', 21)


def ankebut_ayet_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(180, 26, 'Ankebût Suresi 45. Ayet Mesajı', YESIL_K, kalin=True)
    ic += yazi(180, 52, '“Şüphesiz namaz, insanı hayasızlıktan', LAC)
    ic += yazi(180, 76, 've kötülükten alıkoyar.”', LAC, kalin=True)
    return svg(360, 100, ic, 'Ankebût suresi 45. ayet ahlaki mesaj kartı.', 21)


def vakit_namazlari_zinciri():
    vakitler = [
        ('Öğle', 'Tepe Vakti', MAVI, MAVI_A),
        ('İkindi', 'Gölge Uzaması', TUR, TUR_A),
        ('Akşam', 'Gün Batımı', MOR, MOR_A),
        ('Yatsı', 'Gece Vakti', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(vakitler):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 30, ust, renk, kalin=True)
        ic += yazi(x + 41, 64, alt, LAC)
    return svg(360, 96, ic, 'Öğle, ikindi, akşam ve yatsı vakitleri sıralama kartları.', 21)


def namaz_erdemler_semasi():
    kutular = [
        ('Temizlik', 'Günde 5 kez', 'abdest alma', MAVI, MAVI_A),
        ('Zaman Bilinci', 'Vakitlere göre', 'günü planlama', TUR, TUR_A),
        ('Kardeşlik', 'Camide omuz', 'omuza saf tutma', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 25, bas, renk, kalin=True)
        ic += yazi(x + 56, 52, s1, LAC)
        ic += yazi(x + 56, 74, s2, LAC)
    return svg(360, 100, ic, 'Namazın kazandırdığı temizlik, zaman bilinci ve kardeşlik erdemleri.', 21)


def farz_ayn_kifaye_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'Farz-ı Ayn', MAVI, kalin=True)
    ic += yazi(91, 52, 'Her mükellefe ayrı ayrı', LAC)
    ic += yazi(91, 74, 'farzdır (5 vakit - Cuma)', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Farz-ı Kifâye', TUR, kalin=True)
    ic += yazi(269, 52, 'Bir grup kılınca diğerinden', LAC)
    ic += yazi(269, 74, 'düşer (Cenaze namazı)', LAC)
    return svg(360, 100, ic, 'Farz-ı ayn ve farz-ı kifâye karşılaştırma kartları.', 21)


def zaman_cemaat_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'Zaman Yönetimi', YESIL_K, kalin=True)
    ic += yazi(91, 52, 'Günü 5 vakte bölerek', LAC)
    ic += yazi(91, 74, 'disiplinli yaşama', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Cemaat Şuuru', MOR, kalin=True)
    ic += yazi(269, 52, 'Ayrım olmadan yan yana', LAC)
    ic += yazi(269, 74, 'birlik ve dayanışma', LAC)
    return svg(360, 100, ic, 'Zaman yönetimi ve cemaat şuuru bilgi kartları.', 21)


def hadis_benzetme_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.4"/>'
    ic += yazi(91, 25, '1. Hadis Benzetmesi', TUR, kalin=True)
    ic += yazi(91, 54, '“Namaz dinin', LAC)
    ic += yazi(91, 76, 'direğidir.”', LAC, kalin=True)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(269, 25, '2. Hadis Benzetmesi', MAVI, kalin=True)
    ic += yazi(269, 54, '“Namaz müminin', LAC)
    ic += yazi(269, 76, 'miracıdır.”', LAC, kalin=True)
    return svg(360, 100, ic, 'Namaz dinin direğidir ve müminin miracıdır hadis kartları.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = hukmune_gore_namaz_sema()
    s[4]['gorsel'] = namaz_hukum_panosu()
    s[5]['gorsel'] = dort_namaz_karti()
    s[6]['gorsel'] = ankebut_ayet_karti()
    s[7]['gorsel'] = vakit_namazlari_zinciri()
    s[8]['gorsel'] = namaz_erdemler_semasi()
    s[9]['gorsel'] = farz_ayn_kifaye_karti()
    s[11]['gorsel'] = zaman_cemaat_karti()
