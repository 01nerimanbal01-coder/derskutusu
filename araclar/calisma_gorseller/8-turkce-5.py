"""8. sınıf Türkçe 5. hafta (konu, ana duygu, söz sanatları, akrostiş, yüklem) çalışma kâğıdı görselleri (SVG; PDF'te stil.css olmadığı için renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
YAZI_I = 'font-family="Noto Sans, sans-serif" font-weight="500"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek='', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI_I if ince else YAZI} fill="{renk}"{ek}>{metin}</text>'


def sozluk_karti():
    ic = f'<rect x="4" y="4" width="592" height="100" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/>'
    ic += f'<rect x="4" y="4" width="128" height="100" rx="10" fill="{MAVI}"/><rect x="108" y="4" width="24" height="100" fill="{MAVI}"/>'
    ic += yazi(68, 52, 'hasım', 26, '#fff') + yazi(68, 78, 'isim', 15, '#dbe5ff', ince=True)
    ic += yazi(148, 44, '1. Düşman.', 20, LAC, 'start', ince=True)
    ic += yazi(148, 80, '2. Oyunda, davada ya da yarışta karşı taraf.', 19, LAC, 'start', ince=True)
    return svg(600, 108, ic, 'Sözlük kartı: hasım (isim). 1. Düşman. 2. Oyunda, davada ya da yarışta karşı taraf.', 26)


def dortluk():
    dizeler = ['Kağnı tekeri gıcırdar karlı yollarda,', 'Anaların omzunda cephane, yürekte umut;',
               'Ne ayaz yıldırır onları ne de yorgunluk,', 'Her adım bir yemin: Kurtulacak bu yurt.']
    ic = f'<rect x="4" y="4" width="452" height="152" rx="12" fill="#fffaf2" stroke="{TUR}" stroke-width="2"/>'
    ic += f'<rect x="4" y="4" width="10" height="152" rx="5" fill="{TUR}"/>'
    for k, d in enumerate(dizeler):
        ic += yazi(40, 44 + k * 32, d, 18, LAC, 'start', ' font-style="italic"', ince=True)
    return svg(460, 160, ic, 'Dörtlük: Kağnı tekeri gıcırdar karlı yollarda, / Anaların omzunda cephane, yürekte umut; / Ne ayaz yıldırır onları ne de yorgunluk, / Her adım bir yemin: Kurtulacak bu yurt.', 28)


def benzetme_semasi():
    ic = f'<rect x="4" y="4" width="592" height="40" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.4"/>'
    ic += yazi(300, 30, '“Gece şehrin ışıkları inci gibi parlıyordu.”', 17, LAC, ince=True)
    kutu = [('Benzeyen', MAVI, MAVI_A), ('Kendisine benzetilen', TUR, TUR_A), ('Ortak özellik', YES, YES_A)]
    for i, (b, renk, acik) in enumerate(kutu):
        x = 14 + i * 196
        ic += f'<rect x="{x}" y="62" width="176" height="74" rx="10" fill="{acik}" stroke="{renk}" stroke-width="2"/>'
        ic += f'<rect x="{x}" y="62" width="176" height="28" rx="10" fill="{renk}"/><rect x="{x}" y="80" width="176" height="10" fill="{renk}"/>'
        ic += yazi(x + 88, 81, b, 14, '#fff')
        ic += f'<rect x="{x + 38}" y="100" width="100" height="26" rx="6" fill="#fff" stroke="{renk}" stroke-width="1.4" stroke-dasharray="5 4"/>' + yazi(x + 88, 119, '?', 17, renk)
        if i < 2:
            ic += f'<path d="M{x + 180} 99 h10 m-6 -5 l6 5 l-6 5" fill="none" stroke="{LAC}" stroke-width="2"/>'
    return svg(600, 140, ic, 'Benzetme şeması: cümle “Gece şehrin ışıkları inci gibi parlıyordu.” Altında boş üç kutu: benzeyen, kendisine benzetilen, ortak özellik.', 34)


def akrostis():
    dizeler = [('Z', 'or günlerde tek yürek oldu bu millet,'), ('A', 'l bayrak yeniden dalgalandı tepelerde,'),
               ('F', 'utbol maçında gol atan takım sevindi,'), ('E', 'mek veren her kahramana minnettarız,'),
               ('Y', 'urdun dört yanında çaldı zafer davulları.')]
    ic = f'<rect x="4" y="4" width="512" height="196" rx="10" fill="#fff" stroke="{MOR}" stroke-width="2"/>'
    for k, (h, d) in enumerate(dizeler):
        y = 44 + k * 35
        ic += yazi(40, y, f'{k + 1}.', 14, GRI, 'end', ince=True)
        ic += yazi(52, y, f'<tspan fill="{MOR}" font-size="22" font-weight="800">{h}</tspan>{d}', 17, LAC, 'start', ince=True)
    return svg(520, 204, ic, 'ZAFER akrostişi: 1. Zor günlerde tek yürek oldu bu millet, 2. Al bayrak yeniden dalgalandı tepelerde, 3. Futbol maçında gol atan takım sevindi, 4. Emek veren her kahramana minnettarız, 5. Yurdun dört yanında çaldı zafer davulları.', 40)


def harf_kartlari():
    harfler = ['A', 'T', 'A', '', 'Y', 'U', 'R', 'D', 'U']
    ic, x = '', 6
    for h in harfler:
        if not h:
            x += 26
            continue
        ic += f'<rect x="{x}" y="6" width="50" height="58" rx="8" fill="{YES_A}" stroke="{YES}" stroke-width="2"/>' + yazi(x + 25, 46, h, 28, LAC)
        x += 58
    return svg(x + 2, 70, ic, 'Harf kartları: A T A, boşluk, Y U R D U', 18)


def numarali_cumle():
    satirlar = [[('Cepheden ', None), ('dönen', 'I'), (' gaziler, köye ', None), ('girerken', 'II')],
                [('türkü ', None), ('söyleyerek', 'III'), (' ', None), ('ilerledi', 'IV'), ('.', None)]]
    ic = f'<rect x="4" y="4" width="592" height="92" rx="10" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.4"/>'
    for k, parca in enumerate(satirlar):
        akis = ''
        for metin, no in parca:
            metin = metin.replace(' ', '&#160;')
            if no:
                akis += (f'<tspan fill="{TUR}" font-weight="800" text-decoration="underline">{metin}</tspan>'
                         f'<tspan fill="{TUR}" font-size="12" font-weight="800" baseline-shift="super">({no})</tspan>')
            else:
                akis += metin
        ic += f'<text x="300" y="{42 + k * 34}" text-anchor="middle" font-size="19" {YAZI_I} fill="{LAC}">{akis}</text>'
    return svg(600, 100, ic, 'Cümle: Cepheden dönen (I) gaziler, köye girerken (II) türkü söyleyerek (III) ilerledi (IV).', 24)


def not_karti():
    ic = f'<rect x="4" y="4" width="512" height="112" rx="8" fill="#fffbe6" stroke="#d9b84a" stroke-width="1.8"/>'
    ic += f'<rect x="200" y="0" width="120" height="16" rx="3" fill="#f3e3a6" opacity="0.9"/>'
    ic += yazi(24, 40, 'Ece\'nin notu', 14, '#8a6d12', 'start')
    ic += yazi(24, 76, 'Gazilerin', 17, LAC, 'start', ince=True)
    ic += f'<rect x="114" y="56" width="110" height="28" rx="6" fill="none" stroke="{KIR}" stroke-width="2"/>'
    ic += yazi(120, 76, 'anlattıkları', 17, LAC, 'start', ince=True)
    ic += yazi(232, 76, 'bizim için canlı bir tarih dersiydi.', 17, LAC, 'start', ince=True)
    ic += f'<path d="M169 86 V100 H150" fill="none" stroke="{KIR}" stroke-width="1.8"/><path d="M150 100 l7 -4 v8 z" fill="{KIR}"/>'
    ic += yazi(144, 105, 'Yüklem', 14, KIR, 'end')
    return svg(520, 120, ic, 'Ece\'nin not kartı: Gazilerin anlattıkları bizim için canlı bir tarih dersiydi. “anlattıkları” sözcüğü kırmızı çerçeveyle “Yüklem” diye işaretlenmiş.', 28)


def nehir_cumlesi():
    ic = f'<rect x="4" y="4" width="592" height="56" rx="10" fill="{MAVI_A}" stroke="{MAVI}" stroke-width="2"/>'
    ic += yazi(300, 38, '“Nehir, gümüş bir kurdele gibi kıvrılarak şehitlere selam verdi.”', 17, LAC, ince=True)
    return svg(600, 64, ic, 'Cümle: Nehir, gümüş bir kurdele gibi kıvrılarak şehitlere selam verdi.', 16)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = sozluk_karti()
    s[3]['gorsel'] = dortluk()
    s[5]['gorsel'] = benzetme_semasi()
    s[7]['gorsel'] = akrostis()
    s[8]['gorsel'] = harf_kartlari()
    s[10]['gorsel'] = numarali_cumle()
    s[11]['gorsel'] = not_karti()
    s[12]['gorsel'] = nehir_cumlesi()
