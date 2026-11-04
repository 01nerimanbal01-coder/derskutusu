"""5. sınıf Sosyal Bilgiler 8. hafta (Yaşadığımız İlde Doğal ve Beşerî Çevredeki Değişimin Neden ve Sonuçları) çalışma kâğıdı görselleri.
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


def dogal_beseri_sema():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'Doğal Çevre Unsurları', YESIL_K, kalin=True)
    ic += yazi(91, 52, 'Dağlar · Doğal Göller', LAC)
    ic += yazi(91, 76, 'K = ?', YESIL_K, kalin=True)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Beşerî Çevre Unsurları', MAVI, kalin=True)
    ic += yazi(269, 52, 'L = ?', MAVI, kalin=True)
    ic += yazi(269, 76, 'M = ?', MAVI, kalin=True)
    return svg(360, 100, ic, 'Doğal çevre (K) ve beşerî çevre (L, M) sınıflandırma şeması.', 21)


def kirk_yil_degisim_panosu():
    kartlar = [
        ('1. Köprü ve Tünel', 'Ulaşım süresini kısaltır', MAVI, MAVI_A),
        ('2. Yeni Fabrikalar', 'İş imkânlarını artırır', TUR, TUR_A),
        ('3. Ovaya Konutlar', 'Tarımsal üretimi artırır', KIR, '#fdeaea'),
        ('4. Ağaçlandırma', 'Erozyonu ve kirliliği önler', YES, YES_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 37, alt, LAC)
    return svg(360, 106, ic, 'Çevresel değişimler ve etkileri dörtlü bilgi panosu.', 21)


def dort_degisim_ornek_karti():
    kartlar = [
        ('1. Kart', 'Dağa Tünel', MAVI, MAVI_A),
        ('2. Kart', 'Nehre Baraj', YES, YES_A),
        ('3. Kart', 'Ovaya Fabrika', TUR, TUR_A),
        ('4. Kart', 'Arıtma Tesisi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, ad, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 8}" y1="36" x2="{x + 74}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 41, 66, ad, LAC)
    return svg(360, 96, ic, 'Dağa tünel, nehre baraj, ovaya fabrika ve arıtma tesisi kartları.', 21)


def yesilova_degisim_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'Yeşilova · 1980 Yılı', YESIL_K, kalin=True)
    ic += yazi(91, 52, 'Geniş orman, meyve', LAC)
    ic += yazi(91, 74, 'bahçeleri ve az konut', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Yeşilova · 2026 Yılı', TUR, kalin=True)
    ic += yazi(269, 52, 'Çok katlı binalar, otoyol,', LAC)
    ic += yazi(269, 74, 'fabrikalar ve daralan ova', LAC)
    return svg(360, 100, ic, 'Yeşilova ilçesinin 1980 ve 2026 yıllarındaki arazi kullanımı karşılaştırması.', 21)


def kasaba_degisim_zinciri():
    adimlar = [
        ('Sanayi', 'Fabrika Kurulumu', TUR, TUR_A),
        ('Göç Artışı', 'Yeni İş Gücü', MAVI, MAVI_A),
        ('Yapılaşma', 'Konut ve Yollar', MOR, MOR_A),
        ('Koruma', 'Kent Ormanı', YES, YES_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 30, ust, renk, kalin=True)
        ic += yazi(x + 41, 64, alt, LAC)
    return svg(360, 96, ic, 'Sanayileşme, göç, yapılaşma ve çevre koruma adımları.', 21)


def surdurulebilir_sehir_karti():
    projeler = [
        ('1. Temiz Enerji', 'Güneş ve rüzgâr santrali', YES, YES_A),
        ('2. Yeşil Ulaşım', 'Tramvay ve bisiklet yolu', MAVI, MAVI_A),
        ('3. Ovayı Koruma', 'Kayalık zemine konutlar', TUR, TUR_A),
        ('4. Yeşil Kuşak', 'Yeni kent ormanı dikimi', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(projeler):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 37, alt, LAC)
    return svg(360, 106, ic, 'Sürdürülebilir şehir planı dört proje kartı.', 21)


def dort_unsur_ayrim_karti():
    unsurlar = [
        ('I. Unsur', 'Toros Dağları', YES, YES_A),
        ('II. Unsur', 'Taş Köprü', MAVI, MAVI_A),
        ('III. Unsur', 'Göksu Nehri', YES, YES_A),
        ('IV. Unsur', 'Rüzgâr Türbini', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, ad, renk, arka) in enumerate(unsurlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 28, bas, renk, kalin=True)
        ic += yazi(x + 41, 64, ad, LAC)
    return svg(360, 96, ic, 'Toros Dağları, Taş Köprü, Göksu Nehri ve Rüzgâr Türbini kartları.', 21)


def tarim_su_koruma_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{YES_A}" stroke="{YES}" stroke-width="1.5"/>'
    ic += yazi(180, 26, 'Sürdürülebilirlik ve Gelecek Mirası', YESIL_K, kalin=True)
    ic += yazi(180, 52, 'Verimli tarım ovaları ve temiz su havzaları', LAC)
    ic += yazi(180, 76, 'gelecek nesillerin yaşam güvencesidir.', LAC, kalin=True)
    return svg(360, 100, ic, 'Verimli tarım ovaları ve temiz su havzalarının korunması bilgi kartı.', 21)


def iki_sehir_sanayi_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="#fdeaea" stroke="{KIR}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'K Şehri Sanayisi', KIR, kalin=True)
    ic += yazi(91, 52, 'Bacalarda filtre yok ·', LAC)
    ic += yazi(91, 74, 'Atık su nehre akıyor', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'L Şehri Sanayisi', YESIL_K, kalin=True)
    ic += yazi(269, 52, 'Bacalar filtreli ·', LAC)
    ic += yazi(269, 74, 'Atık sular arıtılıyor', LAC)
    return svg(360, 100, ic, 'K şehri ve L şehri sanayi tesislerinin çevre uygulamaları karşılaştırması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = dogal_beseri_sema()
    s[4]['gorsel'] = kirk_yil_degisim_panosu()
    s[5]['gorsel'] = dort_degisim_ornek_karti()
    s[6]['gorsel'] = yesilova_degisim_karti()
    s[7]['gorsel'] = kasaba_degisim_zinciri()
    s[8]['gorsel'] = surdurulebilir_sehir_karti()
    s[9]['gorsel'] = dort_unsur_ayrim_karti()
    s[11]['gorsel'] = tarim_su_koruma_karti()
