"""5. sınıf Fen Bilimleri 8. hafta (Kuvvetin Nitelikleri, Dinamometre ile Ölçüm ve Bilim Tarihinde Yer Çekimi) çalışma kâğıdı görselleri.
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


def sekiz_bolmeli_dinamometre_sema():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'R Cismi (8 Bölmeli)', MAVI, kalin=True)
    ic += yazi(91, 52, '3 bölme = 18 N', LAC, kalin=True)
    ic += yazi(91, 76, '1 bölme = 6 N', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'S Cismi (Aynı Araç)', TUR, kalin=True)
    ic += yazi(269, 52, '6 bölme = ? N', LAC, kalin=True)
    ic += yazi(269, 76, '8 Bölme Kapasite = ? N', LAC)
    return svg(360, 100, ic, '8 eşit bölmeli dinamometrede R cismi 3 bölme 18 N ve S cismi 6 bölme şeması.', 21)


def bilim_tarihi_panosu():
    kartlar = [
        ('1. El-Hâzinî', 'Yer merkezine çekim', YES, YES_A),
        ('2. Bîrûnî', 'Savrulmayı önleyen çekim', MAVI, MAVI_A),
        ('3. Hikmet Terazisi', 'Yalnız sıcaklık ölçer', KIR, '#fdeaea'),
        ('4. Isaac Newton', 'Kuvvet birimi Newton (N)', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, acik, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 37, acik, LAC)
    return svg(360, 106, ic, 'Bilim tarihinde yer çekimi ve kuvvet panosu: El-Hâzinî, Bîrûnî, Hikmet Terazisi, Newton.', 21)


def dort_dinamometre_hesap_karti():
    kartlar = [
        ('1. K Aracı', '40 N · 8 bölme', MAVI, MAVI_A),
        ('2. L Aracı', '60 N · 5 bölme', YES, YES_A),
        ('3. M Aracı', '90 N · 10 bölme', TUR, TUR_A),
        ('4. N Aracı', '120 N · 6 bölme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, veri, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 28, bas, renk, kalin=True)
        ic += f'<line x1="{x + 8}" y1="36" x2="{x + 74}" y2="36" stroke="{renk}" stroke-width="1"/>'
        ic += yazi(x + 41, 66, veri, LAC)
    return svg(360, 96, ic, 'K, L, M ve N dinamometrelerinin kapasite ve bölme sayısı kartları.', 21)


def hazini_biruni_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'El-Hâzinî (12. Yüzyıl)', YESIL_K, kalin=True)
    ic += yazi(91, 52, 'Mîzânü’l-Hikme eseri ve', LAC)
    ic += yazi(91, 74, 'yer merkezine çekim', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Bîrûnî (11. Yüzyıl)', MAVI, kalin=True)
    ic += yazi(269, 52, 'Dönen Dünya’da cisimleri', LAC)
    ic += yazi(269, 74, 'tutan çekim gücü', LAC)
    return svg(360, 100, ic, 'El-Hâzinî ve Bîrûnî’nin yer çekimi çalışmaları bilgi kartı.', 21)


def dort_yuk_siralama_karti():
    kartlar = [
        ('I. Yük', '20 N · 3 bölme', YES, YES_A),
        ('II. Yük', '40 N · 3 bölme', MAVI, MAVI_A),
        ('III. Yük', '50 N · 4 bölme', TUR, TUR_A),
        ('IV. Yük', '80 N · 4 bölme', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, alt, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 28, bas, renk, kalin=True)
        ic += yazi(x + 41, 64, alt, LAC)
    return svg(360, 96, ic, '10’ar bölmeli dört dinamometrede I, II, III ve IV. yüklerin uzama bölmeleri.', 21)


def ozdes_yay_uzama_tablosu():
    kutular = [
        ('K Aracı', '10 N yük', '2 cm uzama', YES, YES_A),
        ('L Aracı', '25 N yük', '5 cm uzama', MAVI, MAVI_A),
        ('M Aracı', '? N yük', '7 cm uzama', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 25, bas, renk, kalin=True)
        ic += yazi(x + 56, 52, s1, LAC, kalin=True)
        ic += yazi(x + 56, 76, s2, LAC)
    return svg(360, 100, ic, 'Özdeş yaylı K, L ve M dinamometrelerinde yük ve uzama miktarları.', 21)


def araba_kuvvet_yonu_sema():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(180, 24, 'Hareket Yönü: Doğu (Sağa Doğru)', LAC, kalin=True)
    ic += f'<rect x="120" y="38" width="120" height="32" rx="7" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(180, 59, 'Oyuncak Araba', MAVI, kalin=True)
    ic += yazi(62, 58, '← II. Kuvvet', KIR, kalin=True)
    ic += yazi(298, 58, 'I. Kuvvet →', YESIL_K, kalin=True)
    ic += yazi(180, 86, 'I: Hareketle aynı yön · II: Harekete zıt yön', LAC)
    return svg(360, 100, ic, 'Doğu yönünde giden oyuncak arabaya uygulanan I (aynı yön) ve II (zıt yön) kuvvetleri.', 21)


def top_etki_adimlari_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(91, 25, '1. Adım · Vuruş', YESIL_K, kalin=True)
    ic += yazi(91, 52, 'Duran topa kuvvet', LAC)
    ic += yazi(91, 74, 'uygulayıp hızlandırma', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, '2. Adım · Kontrol', TUR, kalin=True)
    ic += yazi(269, 52, 'Gelen topa zıt kuvvet', LAC)
    ic += yazi(269, 74, 'uygulayıp durdurma', LAC)
    return svg(360, 100, ic, 'Topa vurarak hızlandırma ve topu tutarak durdurma adımları.', 21)


def iki_yay_hassasiyet_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'K Sarmal Yayı', MAVI, kalin=True)
    ic += yazi(91, 52, '20 N yük → 6 cm uzar', LAC, kalin=True)
    ic += yazi(91, 76, 'İnce ve duyarlı yay', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{MOR_A}" stroke="{MOR}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'L Sarmal Yayı', MOR, kalin=True)
    ic += yazi(269, 52, '20 N yük → 2 cm uzar', LAC, kalin=True)
    ic += yazi(269, 76, 'Kalın ve sert yay', LAC)
    return svg(360, 100, ic, '20 N kuvvetle 6 cm uzayan K yayı ve 2 cm uzayan L yayı karşılaştırması.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sekiz_bolmeli_dinamometre_sema()
    s[4]['gorsel'] = bilim_tarihi_panosu()
    s[5]['gorsel'] = dort_dinamometre_hesap_karti()
    s[6]['gorsel'] = hazini_biruni_karti()
    s[7]['gorsel'] = dort_yuk_siralama_karti()
    s[8]['gorsel'] = ozdes_yay_uzama_tablosu()
    s[9]['gorsel'] = araba_kuvvet_yonu_sema()
    s[11]['gorsel'] = top_etki_adimlari_karti()
