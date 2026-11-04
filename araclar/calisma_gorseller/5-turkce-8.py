"""5. sınıf Türkçe 8. hafta (Oğlu Hüseyin'den Emine Ana'ya Mektuplar: Metin İncelemesi, Mektup Türü ve Deyimler) çalışma kâğıdı görselleri.
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


def mektup_bolum_semasi():
    ic = f'<rect x="6" y="6" width="348" height="92" rx="10" fill="#fbfcff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<rect x="218" y="12" width="124" height="22" rx="5" fill="{MAVI_A}" stroke="{MAVI}"/>'
    ic += yazi(280, 27, 'K (Sağ Üst Köşe)', MAVI, kalin=True)
    ic += f'<rect x="18" y="36" width="134" height="22" rx="5" fill="{TUR_A}" stroke="{TUR}"/>'
    ic += yazi(85, 51, 'L (Sol Üst Satır)', TUR, kalin=True)
    ic += f'<rect x="18" y="64" width="184" height="24" rx="5" fill="{YES_A}" stroke="{YES}"/>'
    ic += yazi(110, 80, 'M (Orta Paragraflar)', YESIL_K, kalin=True)
    ic += f'<rect x="218" y="64" width="124" height="24" rx="5" fill="{MOR_A}" stroke="{MOR}"/>'
    ic += yazi(280, 80, 'N (Sağ Alt Köşe)', MOR, kalin=True)
    return svg(360, 104, ic, 'Mektup sayfa düzeninde K, L, M ve N bölümleri şeması.', 21)


def hitap_yazim_kartlari():
    kartlar = [
        ('1. Kart', 'sevgili anneciğim.', KIR, '#fdeaea'),
        ('2. Kart', 'Kıymetli öğretmenim;', TUR, TUR_A),
        ('3. Kart', 'Canım Anneciğim,', YES, YES_A),
        ('4. Kart', 'aziz Dostum!', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, met, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 37, met, LAC)
    return svg(360, 106, ic, 'Dört mektup hitap ifadesi yazım kartı.', 21)


def dort_deyim_cumle_karti():
    kartlar = [
        ('1. Kart', 'Gözü yollarda', 'kalmak', MAVI, MAVI_A),
        ('2. Kart', 'Gözünü', 'kırpmamak', YES, YES_A),
        ('3. Kart', 'Tek yürek', 'olmak', TUR, TUR_A),
        ('4. Kart', 'Kulak', 'kabartmak', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kartlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="86" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 24, bas, renk, kalin=True)
        ic += yazi(x + 41, 50, s1, LAC)
        ic += yazi(x + 41, 74, s2, LAC, kalin=True)
    return svg(360, 98, ic, 'Dört deyim kartı: gözü yollarda kalmak, gözünü kırpmamak, tek yürek olmak, kulak kabartmak.', 21)


def huseyin_mektup_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{TUR_A}" stroke="{ALTIN}" stroke-width="1.5"/>'
    ic += yazi(180, 25, 'Er Hüseyin’den Emine Ana’ya Mektup', TUR, kalin=True)
    ic += yazi(180, 52, '“Canım Anacığım, ellerinden hasretle öperim.', LAC)
    ic += yazi(180, 76, 'Vatan toprağını canımız pahasına koruyoruz.”', LAC, kalin=True)
    return svg(360, 100, ic, 'Er Hüseyin’in annesi Emine Ana’ya yazdığı mektup parçası.', 21)


def mektup_sira_adimlari():
    adimlar = [
        ('Sağ Üst', 'Tarih ve Yer', MAVI, MAVI_A),
        ('Sol Üst', 'Hitap Sözü', TUR, TUR_A),
        ('Orta Bölüm', 'Gövde Metni', YES, YES_A),
        ('Sağ Alt', 'Ad ve İmza', MOR, MOR_A),
    ]
    ic = ''
    for i, (ust, alt, renk, arka) in enumerate(adimlar):
        x = 6 + i * 88
        ic += f'<rect x="{x}" y="6" width="82" height="84" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 41, 30, ust, renk, kalin=True)
        ic += yazi(x + 41, 64, alt, LAC)
    return svg(360, 96, ic, 'Mektup bölümlerinin yukarıdan aşağıya doğru sıralama kartları.', 21)


def deyim_ozellik_panosu():
    kutular = [
        ('Kalıplaşmış Söz', 'Kelimeleri asla', 'değiştirilemez', MAVI, MAVI_A),
        ('Mecaz Anlam', 'Gerçek anlamdan', 'farklı kullanılır', TUR, TUR_A),
        ('Etkili Anlatım', 'Duyguyu kısa ve', 'güçlü anlatır', YES, YES_A),
    ]
    ic = ''
    for i, (bas, s1, s2, renk, arka) in enumerate(kutular):
        x = 6 + i * 118
        ic += f'<rect x="{x}" y="6" width="112" height="88" rx="9" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 56, 25, bas, renk, kalin=True)
        ic += yazi(x + 56, 52, s1, LAC)
        ic += yazi(x + 56, 76, s2, LAC)
    return svg(360, 100, ic, 'Deyimlerin kalıplaşmış olma, mecaz anlam ve etkili anlatım özellikleri.', 21)


def deyim_yanlis_kullanim_karti():
    kartlar = [
        ('I. Kart', 'Kulağı yollarda kaldı', KIR, '#fdeaea'),
        ('II. Kart', 'Gözünü kırpmadan', YES, YES_A),
        ('III. Kart', 'İçi rahatladı', MAVI, MAVI_A),
        ('IV. Kart', 'Tek yürek oldu', TUR, TUR_A),
    ]
    ic = ''
    for i, (bas, met, renk, arka) in enumerate(kartlar):
        x = 6 + (i % 2) * 176
        y = 6 + (i // 2) * 50
        ic += f'<rect x="{x}" y="{y}" width="172" height="44" rx="8" fill="{arka}" stroke="{renk}" stroke-width="1.4"/>'
        ic += yazi(x + 86, y + 19, bas, renk, kalin=True)
        ic += yazi(x + 86, y + 37, met, LAC)
    return svg(360, 106, ic, 'Deyimlerin doğru ve yanlış kullanımlarını gösteren dört kart.', 21)


def cephe_mektup_onem_karti():
    ic = f'<rect x="6" y="6" width="170" height="88" rx="9" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.4"/>'
    ic += yazi(91, 25, 'Edebî Değeri', MAVI, kalin=True)
    ic += yazi(91, 52, 'İçten duygular, hasret', LAC)
    ic += yazi(91, 74, 've duru Türkçe anlatımı', LAC)

    ic += f'<rect x="184" y="6" width="170" height="88" rx="9" fill="{YES_A}" stroke="{YES}" stroke-width="1.4"/>'
    ic += yazi(269, 25, 'Tarihî Belge Değeri', YESIL_K, kalin=True)
    ic += yazi(269, 52, 'Cephedeki mücadeleye', LAC)
    ic += yazi(269, 74, 'ilk elden tanıklık etmesi', LAC)
    return svg(360, 100, ic, 'Cephe mektuplarının edebî ve tarihî belge değerini gösteren kartlar.', 21)


def ataturk_milli_birlik_karti():
    ic = f'<rect x="6" y="6" width="348" height="88" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += yazi(180, 25, 'Millî Mücadele ve Tek Yürek Millet', MAVI, kalin=True)
    ic += yazi(180, 52, 'Atatürk’ün liderliğinde cephedeki Mehmetçik', LAC)
    ic += yazi(180, 76, 've fedakâr analar vatan sevgisiyle zafere ulaştı.', LAC, kalin=True)
    return svg(360, 100, ic, 'Atatürk’ün liderliğinde millî birlik ve vatan sevgisi metin kartı.', 21)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = mektup_bolum_semasi()
    s[4]['gorsel'] = hitap_yazim_kartlari()
    s[5]['gorsel'] = dort_deyim_cumle_karti()
    s[6]['gorsel'] = huseyin_mektup_karti()
    s[7]['gorsel'] = mektup_sira_adimlari()
    s[8]['gorsel'] = deyim_ozellik_panosu()
    s[9]['gorsel'] = deyim_yanlis_kullanim_karti()
    s[11]['gorsel'] = cephe_mektup_onem_karti()
