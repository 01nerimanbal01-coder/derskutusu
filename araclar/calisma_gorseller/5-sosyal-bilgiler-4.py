"""5. sınıf Sosyal Bilgiler 4. hafta (yardımlaşma ve dayanışma) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

LAC, MAVI, TUR, YES, KIR, MOR = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed'
MAVI_A, TUR_A, YES_A, MOR_A, GRI, GRI_A, SOLUK = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#9aa6bd', '#eef1f6', '#5b6479'
KIR_A, ALTIN = '#fdeaea', '#f2c14e'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=14, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=11, renk=LAC, hiza='start', ara=14):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}">{m}</text>'
                   for k, m in enumerate(satirlar))


def harf(x, y, h, renk=LAC):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{renk}"/>' + yazi(x, y + 4.5, h, 12, '#fff')


def ok(x1, x2, y, renk=SOLUK):
    return f'<path d="M{x1} {y} H{x2 - 6}" stroke="{renk}" stroke-width="2"/><path d="M{x2 - 7} {y - 5} L{x2} {y} L{x2 - 7} {y + 5} Z" fill="{renk}"/>'


def yildiz(cx, cy, r, renk='#fff'):
    nok = []
    for k in range(10):
        a = math.radians(-90 + k * 36)
        rr = r if k % 2 == 0 else r * 0.42
        nok.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(nok)}" fill="{renk}"/>'


def hilal(cx, cy, r, renk, zemin):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{renk}"/><circle cx="{cx + r * 0.32:.1f}" cy="{cy}" r="{r * 0.8:.1f}" fill="{zemin}"/>'


def sadaka():
    gece = '#16275e'
    ic = f'<rect x="4" y="4" width="150" height="128" rx="10" fill="{gece}"/>'
    ic += f'<path d="M4 106 H154 V122 a10 10 0 0 1 -10 10 H14 a10 10 0 0 1 -10 -10 Z" fill="#3a4673"/>'
    ic += hilal(132, 26, 11, '#ffe08a', gece)
    ic += ''.join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#fff"/>' for x, y in [(22, 18), (48, 30), (80, 14), (104, 34), (64, 50), (146, 50)])
    # çeşme
    ic += f'<rect x="14" y="52" width="46" height="54" fill="#d9cbb0" stroke="#8a7a5c" stroke-width="1.2"/>'
    ic += f'<path d="M10 52 H64 L58 44 H16 Z" fill="#c4b393" stroke="#8a7a5c" stroke-width="1"/>'
    ic += f'<path d="M24 100 V74 a13 13 0 0 1 26 0 V100 Z" fill="#b9a783" stroke="#8a7a5c" stroke-width="1"/>'
    ic += f'<rect x="34" y="78" width="6" height="5" fill="{GRI}"/><line x1="37" y1="83" x2="37" y2="92" stroke="#9cc7f0" stroke-width="1.6"/>'
    ic += f'<rect x="22" y="94" width="30" height="8" rx="2" fill="#a8956d" stroke="#8a7a5c" stroke-width="1"/>'
    # sadaka taşı
    ic += f'<rect x="92" y="98" width="38" height="8" rx="1.5" fill="#cfc2a6" stroke="#8a7a5c" stroke-width="1"/>'
    ic += f'<path d="M98 98 V58 a13 5 0 0 1 26 0 V98 Z" fill="#e6dccb" stroke="#8a7a5c" stroke-width="1.2"/>'
    ic += f'<ellipse cx="111" cy="58" rx="9" ry="3.2" fill="#4a3c26"/>'
    ic += f'<ellipse cx="108" cy="57.6" rx="3" ry="1.3" fill="{ALTIN}"/><ellipse cx="114" cy="58.4" rx="3" ry="1.3" fill="{ALTIN}"/>'
    ic += f'<circle cx="111" cy="44" r="3.6" fill="{ALTIN}" stroke="#b88a1a" stroke-width=".8"/><path d="M111 49 v4" stroke="{ALTIN}" stroke-width="1" stroke-dasharray="1.5 1.5"/>'
    ic += yazi(37, 122, 'çeşme', 10.5, '#fff') + yazi(111, 122, 'sadaka taşı', 10.5, '#fff')
    # notlar
    for k, (y, yuk, renk, zemin, satirlar) in enumerate([
            (4, 56, TUR, TUR_A, ['Yardım etmek isteyen,', 'parayı taşın oyuğuna', 'bırakır.']),
            (66, 66, MAVI, MAVI_A, ['İhtiyaç sahibi gece geç', 'saatte gelir; kimseye', 'görünmeden ihtiyacı', 'kadarını alır.'])]):
        ic += f'<rect x="164" y="{y}" width="192" height="{yuk}" rx="8" fill="{zemin}" stroke="{renk}" stroke-width="1.3"/>'
        ic += harf(180, y + 16, str(k + 1), renk) + duz(198, y + 20, satirlar, 11.5)
    return svg(360, 136, ic, 'Gece, ay ışığında bir çeşmenin yanında sadaka taşı; taşın üstündeki oyukta paralar. Not 1: Yardım etmek isteyen, parayı taşın oyuğuna bırakır. Not 2: İhtiyaç sahibi gece geç saatte gelir; kimseye görünmeden ihtiyacı kadarını alır.', 28)


def milli():
    ic = ''
    # emirler
    ic += f'<rect x="4" y="10" width="84" height="84" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>'
    ic += f'<path d="M32 20 H52 L58 26 V52 H32 Z" fill="#fff" stroke="{LAC}" stroke-width="1.2"/><path d="M52 20 V26 H58" fill="none" stroke="{LAC}" stroke-width="1"/>'
    ic += ''.join(f'<line x1="36" y1="{30 + k * 5}" x2="54" y2="{30 + k * 5}" stroke="{GRI}" stroke-width="1"/>' for k in range(3))
    ic += f'<circle cx="51" cy="47" r="4" fill="{KIR}"/>'
    ic += yazi(46, 68, 'Emirler', 11.5) + duz(46, 80, ['Mustafa', 'Kemal Paşa'], 9, SOLUK, 'middle', 10)
    ic += ok(90, 110, 52)
    # halkın gönderdikleri
    ic += f'<rect x="112" y="4" width="160" height="96" rx="8" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3"/>'
    ic += yazi(192, 21, 'Halkın gönderdikleri', 11.5, TUR)
    x = 140  # giyecek
    ic += (f'<path d="M{x - 13} 40 l8 -6 q5 5 10 0 l8 6 l5 10 l-6 3 l-3 -5 v20 h-18 v-20 l-3 5 l-6 -3 z" fill="{MAVI}" stroke="{LAC}" stroke-width=".9"/>'
           f'<line x1="{x}" y1="38" x2="{x}" y2="68" stroke="{MAVI_A}" stroke-width=".9"/>')
    x = 192  # yiyecek
    ic += (f'<path d="M{x - 18} 62 q-2 -22 18 -24 q20 2 18 24 z" fill="#d99a4e" stroke="#8a5a2b" stroke-width="1"/>'
           + ''.join(f'<path d="M{x - 9 + k * 9} 46 q3 5 0 10" fill="none" stroke="#8a5a2b" stroke-width="1"/>' for k in range(3)))
    x = 244  # cephane
    ic += (f'<rect x="{x - 17}" y="46" width="34" height="22" fill="#6b7a3a" stroke="#3f4a1f" stroke-width="1.2"/>'
           f'<path d="M{x - 17} 46 L{x + 17} 68 M{x + 17} 46 L{x - 17} 68" stroke="#4f5a28" stroke-width="1"/>'
           + ''.join(f'<path d="M{x - 11 + k * 7} 46 v-9 a2.5 3.5 0 0 1 5 0 v9 z" fill="#c9a227" stroke="#8a6d12" stroke-width=".7"/>' for k in range(4)))
    ic += ''.join(yazi(x, 88, ad, 11) for x, ad in [(140, 'giyecek'), (192, 'yiyecek'), (244, 'cephane')])
    ic += ok(274, 294, 52)
    # ordu
    ic += f'<rect x="296" y="10" width="60" height="84" rx="8" fill="{KIR_A}" stroke="{KIR}" stroke-width="1.3"/>'
    ic += f'<line x1="314" y1="22" x2="314" y2="66" stroke="{LAC}" stroke-width="2"/><rect x="315" y="23" width="32" height="21" fill="{KIR}"/>'
    ic += hilal(326, 33.5, 6.5, '#fff', KIR) + yildiz(335.5, 33.5, 3.4)
    ic += yazi(326, 84, 'Ordu', 12, KIR)
    return svg(360, 104, ic, 'Şema: Mustafa Kemal Paşa’nın emirleri, halkın gönderdikleri (giyecek, yiyecek, cephane), ordu. Oklar emirlerden halka, halktan orduya doğrudur.', 24)


def kizilay():
    ic = ''
    xs = [2, 95, 188, 281]
    yazilar = [['Giysiler', 'kutuya', 'bırakılır.'], ['Kutulardaki', 'giysiler', 'toplanır.'], None, ['Elde edilen', 'gelirle destek', 'verilir.']]
    for i, x in enumerate(xs):
        bos = yazilar[i] is None
        ic += (f'<rect x="{x}" y="4" width="81" height="100" rx="8" fill="{"#fff" if bos else GRI_A}" stroke="{TUR if bos else GRI}" stroke-width="1.4"'
               + (' stroke-dasharray="5 4"/>' if bos else '/>'))
        ic += harf(x + 13, 17, str(i + 1), TUR if bos else LAC)
        cx = x + 40.5
        if i == 0:
            ic += (f'<rect x="{cx - 15}" y="20" width="30" height="34" rx="3" fill="{KIR}"/><rect x="{cx - 10}" y="25" width="20" height="3.5" rx="1.5" fill="#5a1414"/>'
                   f'<circle cx="{cx}" cy="42" r="7" fill="#fff"/>' + hilal(cx - 1, 42, 4.6, KIR, '#fff'))
        elif i == 1:
            ic += (f'<rect x="{cx - 24}" y="26" width="30" height="20" rx="2" fill="#fff" stroke="{LAC}" stroke-width="1.2"/>'
                   f'<path d="M{cx + 6} 32 h10 l6 7 v7 h-16 z" fill="{MAVI}" stroke="{LAC}" stroke-width="1"/>'
                   f'<rect x="{cx + 9}" y="34" width="7" height="5" fill="{MAVI_A}"/>'
                   f'<circle cx="{cx - 15}" cy="48" r="4.5" fill="{LAC}"/><circle cx="{cx + 13}" cy="48" r="4.5" fill="{LAC}"/>'
                   + hilal(cx - 9, 36, 4.2, KIR, '#fff'))
        elif bos:
            ic += yazi(cx, 70, '?', 38, TUR)
        else:
            ic += (''.join(f'<ellipse cx="{cx - 8}" cy="{50 - k * 5}" rx="10" ry="3.4" fill="{ALTIN}" stroke="#b88a1a" stroke-width=".8"/>' for k in range(4))
                   + f'<path d="M{cx + 12} 30 c-4 -5 -10 0 -6 5 l6 6 l6 -6 c4 -5 -2 -10 -6 -5z" fill="{KIR}"/>')
        if not bos:
            ic += duz(cx, 70, yazilar[i], 10, LAC, 'middle', 13)
        if i < 3:
            ic += ok(x + 82, x + 94, 54)
    return svg(364, 108, ic, 'Türk Kızılay 2. El Tekstil projesinin aşamaları: 1 Giysiler kutuya bırakılır. 2 Kutulardaki giysiler toplanır. 3 boş bırakılmıştır. 4 Elde edilen gelirle destek verilir.', 25)


def vefa():
    satirlar = [('Pazartesi', 'Ev temizliği', MAVI), ('Çarşamba', 'Öz bakım desteği', MOR), ('Cuma', 'Hâl hatır sorma ziyareti', YES)]
    ic = f'<rect x="4" y="4" width="352" height="120" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<rect x="4" y="4" width="352" height="22" rx="10" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 20, 'Ulusal Vefa Programı · Haftalık ziyaret planı', 12, '#fff')
    ic += duz(180, 44, ['Hatice Hanım · 78 yaşında, yalnız yaşıyor'], 11.5, SOLUK, 'middle')
    for i, (g, m, r) in enumerate(satirlar):
        y = 54 + i * 23
        ic += f'<rect x="14" y="{y}" width="84" height="19" rx="5" fill="{r}"/>' + yazi(56, y + 14, g, 11.5, '#fff')
        ic += yazi(110, y + 14, m, 12, LAC, 'start')
        cx, cy = 330, y + 10
        if i == 0:  # süpürge
            ic += f'<line x1="{cx + 6}" y1="{cy - 9}" x2="{cx - 1}" y2="{cy + 3}" stroke="#8a5a2b" stroke-width="2"/><path d="M{cx - 5} {cy + 1} l7 4 l-4 6 l-9 -3 z" fill="{ALTIN}" stroke="#b88a1a" stroke-width=".8"/>'
        elif i == 1:  # damla ve havlu
            ic += f'<path d="M{cx - 5} {cy - 8} q6 8 0 14 q-6 -6 0 -14z" fill="#7cc4f5" stroke="{MAVI}" stroke-width=".8"/><rect x="{cx + 2}" y="{cy - 4}" width="9" height="12" rx="2" fill="{MOR_A}" stroke="{MOR}" stroke-width=".9"/>'
        else:  # konuşma balonu
            ic += f'<path d="M{cx - 10} {cy - 8} h20 a3 3 0 0 1 3 3 v9 a3 3 0 0 1 -3 3 h-12 l-6 5 v-5 h-2 a3 3 0 0 1 -3 -3 v-9 a3 3 0 0 1 3 -3z" fill="{YES_A}" stroke="{YES}" stroke-width="1"/><path d="M{cx} {cy - 3} c-2 -3 -6 0 -4 2.5 l4 4 l4 -4 c2 -2.5 -2 -5.5 -4 -2.5z" fill="{KIR}"/>'
    return svg(360, 128, ic, 'Ulusal Vefa Programı haftalık ziyaret planı. Hatice Hanım, 78 yaşında, yalnız yaşıyor. Pazartesi ev temizliği, Çarşamba öz bakım desteği, Cuma hâl hatır sorma ziyareti.', 32)


def meb():
    ic = ''
    for i, (ad, r, z) in enumerate([('Barınma', MAVI, MAVI_A), ('Arama kurtarma', TUR, TUR_A), ('Üretim', YES, YES_A)]):
        x = 4 + i * 120
        cx = x + 56
        ic += f'<rect x="{x}" y="4" width="112" height="86" rx="8" fill="{z}" stroke="{r}" stroke-width="1.3"/>'
        ic += f'<rect x="{x}" y="4" width="112" height="22" rx="8" fill="{r}"/><rect x="{x}" y="16" width="112" height="10" fill="{r}"/>' + yazi(cx, 20, ad, 11.5, '#fff')
        if i == 0:  # çatı altında yatak
            ic += (f'<path d="M{cx - 30} 52 L{cx} 32 L{cx + 30} 52" fill="none" stroke="{LAC}" stroke-width="2.2"/>'
                   f'<rect x="{cx - 22}" y="62" width="44" height="10" rx="2" fill="{MAVI}"/><rect x="{cx - 22}" y="55" width="12" height="7" rx="2.5" fill="#fff" stroke="{LAC}" stroke-width=".9"/>'
                   f'<path d="M{cx - 9} 62 h31 v-5 a4 4 0 0 0 -4 -4 h-27 z" fill="{MAVI_A}" stroke="{MAVI}" stroke-width=".9"/>'
                   f'<line x1="{cx - 22}" y1="72" x2="{cx - 22}" y2="80" stroke="{LAC}" stroke-width="2"/><line x1="{cx + 22}" y1="72" x2="{cx + 22}" y2="80" stroke="{LAC}" stroke-width="2"/>')
        elif i == 1:  # baret ve ışık
            ic += (f'<path d="M{cx - 22} 66 a22 22 0 0 1 44 0 z" fill="#f5c400" stroke="#a88600" stroke-width="1.2"/>'
                   f'<rect x="{cx - 27}" y="66" width="54" height="6" rx="3" fill="#e0b000" stroke="#a88600" stroke-width="1"/>'
                   f'<path d="M{cx - 3} 44 v22 M{cx + 3} 44 v22" stroke="#a88600" stroke-width="1"/>'
                   f'<rect x="{cx - 6}" y="48" width="12" height="8" rx="2" fill="#fff" stroke="{LAC}" stroke-width=".9"/>'
                   f'<path d="M{cx - 8} 46 l-10 -12 M{cx} 44 v-12 M{cx + 8} 46 l10 -12" stroke="{TUR}" stroke-width="1.6" stroke-linecap="round"/>')
        else:  # çadır ve battaniye
            ic += (f'<path d="M{cx - 40} 78 L{cx - 18} 38 L{cx + 4} 78 Z" fill="{YES}" stroke="#0c6e37" stroke-width="1.2"/><path d="M{cx - 18} 38 L{cx - 24} 78 H{cx - 12} Z" fill="#0c6e37"/>'
                   + ''.join(f'<rect x="{cx + 8}" y="{70 - k * 9}" width="30" height="8" rx="2" fill="{c}" stroke="{LAC}" stroke-width=".8"/>' for k, c in enumerate([MOR, TUR, MAVI, KIR])))
    return svg(364, 94, ic, 'Millî Eğitim Bakanlığının çalıştığı üç alan: barınma, arama kurtarma, üretim.', 22)


def yardimlar():
    ic = ''
    yazilar = [['Gıda kolisi', 'gönderme'], ['Battaniye', 'bağışlama'], ['Çocuklarla', 'oyun oynayıp', 'neşelendirme'], ['Para bağışında', 'bulunma']]
    for i, x in enumerate([2, 95, 188, 281]):
        cx = x + 42
        ic += f'<rect x="{x}" y="4" width="84" height="100" rx="8" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.2"/>' + harf(x + 13, 17, str(i + 1), [TUR, MOR, YES, MAVI][i])
        if i == 0:
            ic += (f'<path d="M{cx - 18} 30 h36 v24 h-36 z" fill="#d9a066" stroke="#8a5a2b" stroke-width="1.2"/><rect x="{cx - 4}" y="30" width="8" height="24" fill="#f3dfc0"/>'
                   f'<circle cx="{cx - 18}" cy="27" r="6" fill="{KIR}"/><path d="M{cx - 18} 21 q2 -4 5 -3" stroke="#6b4a2b" stroke-width="1.2" fill="none"/>'
                   f'<path d="M{cx + 8} 26 q8 -6 14 0 q-2 6 -14 4z" fill="#e9b872" stroke="#8a5a2b" stroke-width=".8"/>')
        elif i == 1:
            ic += ''.join(f'<rect x="{cx - 20}" y="{48 - k * 9}" width="40" height="8" rx="3" fill="{c}" stroke="{LAC}" stroke-width=".8"/>' for k, c in enumerate([MOR, MOR_A, MOR, MOR_A]))
        elif i == 2:
            ic += (f'<circle cx="{cx - 6}" cy="42" r="12" fill="#fff" stroke="{LAC}" stroke-width="1.2"/>'
                   f'<path d="M{cx - 6} 30 q-6 12 0 24 M{cx - 18} 42 h24 M{cx - 15} 34 q9 5 18 0 M{cx - 15} 50 q9 -5 18 0" fill="none" stroke="{YES}" stroke-width="1.2"/>'
                   f'<path d="M{cx + 14} 24 c-4 -5 -10 0 -6 5 l6 6 l6 -6 c4 -5 -2 -10 -6 -5z" fill="{KIR}"/>')
        else:
            ic += (f'<rect x="{cx - 22}" y="26" width="34" height="18" rx="2" fill="{YES_A}" stroke="{YES}" stroke-width="1.2"/><circle cx="{cx - 5}" cy="35" r="5" fill="none" stroke="{YES}" stroke-width="1.2"/>'
                   + ''.join(f'<ellipse cx="{cx + 10}" cy="{56 - k * 5}" rx="10" ry="3.4" fill="{ALTIN}" stroke="#b88a1a" stroke-width=".8"/>' for k in range(3)))
        ic += duz(cx, 74 if len(yazilar[i]) == 2 else 68, yazilar[i], 10.5, LAC, 'middle', 13)
    return svg(367, 108, ic, 'Depremzedelere yapılan yardımlar: 1 Gıda kolisi gönderme. 2 Battaniye bağışlama. 3 Çocuklarla oyun oynayıp neşelendirme. 4 Para bağışında bulunma.', 25)


def fikir_karti():
    ic = f'<rect x="4" y="4" width="352" height="158" rx="10" fill="#fff" stroke="{GRI}" stroke-width="1.4"/>'
    ic += f'<rect x="4" y="4" width="352" height="22" rx="10" fill="{LAC}"/><rect x="4" y="16" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 20, 'Fikir kartı · Yaşlılara yönelik', 12, '#fff')
    satirlar = [('Fikir', LAC, ['Mahalledeki yalnız yaşayan yaşlıların', 'alışverişine hafta sonları yardım etmek'], 34),
                ('Güçlü yön', YES, ['Sınıfta bu işe gönüllü çok öğrenci var.'], 70),
                ('Zayıf yön', KIR, ['Öğrenciler, yaşlıların evlerine', 'tek başlarına gidemez.'], 96),
                ('Alternatif çözüm', TUR, None, 132)]
    for ad, r, m, y in satirlar:
        ic += f'<rect x="12" y="{y}" width="96" height="20" rx="5" fill="{r}"/>' + yazi(60, y + 14, ad, 11, '#fff')
        if m:
            ic += duz(118, y + 14, m, 11.5)
        else:
            ic += f'<rect x="116" y="{y - 2}" width="232" height="24" rx="5" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.3" stroke-dasharray="5 4"/>' + yazi(232, y + 16, '?', 16, TUR)
    return svg(360, 166, ic, 'Fikir kartı, yaşlılara yönelik. Fikir: Mahalledeki yalnız yaşayan yaşlıların alışverişine hafta sonları yardım etmek. Güçlü yön: Sınıfta bu işe gönüllü çok öğrenci var. Zayıf yön: Öğrenciler, yaşlıların evlerine tek başlarına gidemez. Alternatif çözüm boş bırakılmıştır.', 40)


def basliklar():
    sutunlar = [('Okullara yönelik', MAVI, [['Kütüphaneye', 'kitap bağışı'], ['Kırtasiye seti', 'hazırlama']]),
                ('Çocuklara yönelik', TUR, [['Oyuncak toplama', 'kampanyası'], ['Kışlık mont', 'toplama']]),
                ('Yaşlılara yönelik', YES, [['Huzurevine', 'bulmaca götürme'], None])]
    ic = ''
    for i, (ad, r, ogeler) in enumerate(sutunlar):
        x = 4 + i * 120
        cx = x + 56
        ic += f'<rect x="{x}" y="4" width="112" height="22" rx="6" fill="{r}"/>' + yazi(cx, 19.5, ad, 10.5, '#fff')
        for k, og in enumerate(ogeler):
            y = 32 + k * 36
            if og:
                ic += f'<rect x="{x}" y="{y}" width="112" height="32" rx="6" fill="{GRI_A}" stroke="{GRI}" stroke-width="1.1"/>' + duz(cx, y + 13.5, og, 10.5, LAC, 'middle', 13)
            else:
                ic += f'<rect x="{x}" y="{y}" width="112" height="32" rx="6" fill="#fff" stroke="{TUR}" stroke-width="1.4" stroke-dasharray="5 4"/>' + yazi(cx, y + 23, '?', 18, TUR)
    return svg(364, 104, ic, 'Proje fikirleri üç başlıkta: Okullara yönelik: kütüphaneye kitap bağışı, kırtasiye seti hazırlama. Çocuklara yönelik: oyuncak toplama kampanyası, kışlık mont toplama. Yaşlılara yönelik: huzurevine bulmaca götürme ve boş bırakılmış bir kutu.', 25)


def paylasim():
    ic = ''
    yazilar = [['Sınavı kazanan', 'komşuya tebrik'], ['Evi yanan aileye', 'eşya desteği'], ['Bayramda', 'büyükleri ziyaret'], ['Hasta komşuya', 'çorba götürme']]
    renkler = [(MAVI, MAVI_A), (KIR, KIR_A), (YES, YES_A), (TUR, TUR_A)]
    for i, x in enumerate([2, 95, 188, 281]):
        cx = x + 42
        r, z = renkler[i]
        ic += f'<rect x="{x}" y="4" width="84" height="80" rx="8" fill="{z}" stroke="{r}" stroke-width="1.2"/>' + harf(x + 13, 17, str(i + 1), r)
        ic += '<g transform="translate(0 -3)">'
        if i == 0:  # tebrik kartı ve konfeti
            ic += (f'<rect x="{cx - 17}" y="24" width="34" height="30" rx="2" fill="#fff" stroke="{LAC}" stroke-width="1.1"/>'
                   + yildiz(cx, 37, 9, ALTIN)
                   + f'<line x1="{cx - 10}" y1="49" x2="{cx + 10}" y2="49" stroke="{GRI}" stroke-width="1.2"/>'
                   + ''.join(f'<rect x="{px}" y="{py}" width="3" height="5" rx="1" fill="{c}" transform="rotate({a} {px} {py})"/>'
                             for px, py, a, c in [(cx + 20, 24, 30, TUR), (cx + 24, 38, -25, MOR), (cx - 25, 30, 20, YES), (cx + 21, 52, 50, KIR)]))
        elif i == 1:  # kararmış ev ve eşya kolisi
            ic += (f'<path d="M{cx - 24} 38 L{cx - 10} 26 L{cx + 4} 38 V56 H{cx - 24} Z" fill="#8f96a3" stroke="#4b5160" stroke-width="1.1"/>'
                   f'<rect x="{cx - 14}" y="44" width="8" height="12" fill="#4b5160"/>'
                   f'<path d="M{cx - 2} 33 q-4 -6 1 -11 q0 5 4 6 q2 -4 0 -7 q7 5 3 12 z" fill="{TUR}" stroke="{KIR}" stroke-width=".7"/>'
                   f'<rect x="{cx + 6}" y="40" width="20" height="16" rx="1.5" fill="#d9a066" stroke="#8a5a2b" stroke-width="1"/>'
                   f'<rect x="{cx + 13.5}" y="40" width="5" height="16" fill="#f3dfc0"/>')
        elif i == 2:  # bayram şekeri kutusu
            ic += (f'<rect x="{cx - 20}" y="34" width="40" height="22" rx="3" fill="#fff" stroke="{YES}" stroke-width="1.2"/>'
                   + ''.join(f'<path d="M{px - 5} {py} l-3 -3 v6 z M{px + 5} {py} l3 -3 v6 z" fill="{c}"/><ellipse cx="{px}" cy="{py}" rx="5" ry="3.4" fill="{c}"/>'
                             for px, py, c in [(cx - 9, 41, KIR), (cx + 9, 41, MAVI), (cx - 9, 50, TUR), (cx + 9, 50, MOR)])
                   + hilal(cx - 2, 25, 6, YES, YES_A) + yildiz(cx + 7, 25, 3, YES))
        else:  # buharı tüten çorba kâsesi
            ic += (f'<path d="M{cx - 20} 42 h40 a20 14 0 0 1 -40 0 z" fill="#fff" stroke="{LAC}" stroke-width="1.2"/>'
                   f'<path d="M{cx - 18} 43 h36" stroke="#e08a3a" stroke-width="3"/>'
                   f'<rect x="{cx - 9}" y="55" width="18" height="3" rx="1.5" fill="{LAC}"/>'
                   + ''.join(f'<path d="M{cx + d} 37 q-3 -4 0 -8 q3 -4 0 -8" fill="none" stroke="{GRI}" stroke-width="1.4" stroke-linecap="round"/>' for d in (-8, 0, 8)))
        ic += '</g>' + duz(cx, 67, yazilar[i], 10.5, LAC, 'middle', 12)
    return svg(367, 88, ic, 'Bir mahallede komşuların davranışları: 1 Sınavı kazanan komşuya tebrik. 2 Evi yanan aileye eşya desteği. 3 Bayramda büyükleri ziyaret. 4 Hasta komşuya çorba götürme.', 22)


def uygula(o):
    s = o['sorular']
    s[12]['gorsel'] = paylasim()
    s[1]['gorsel'] = sadaka()
    s[2]['gorsel'] = milli()
    s[3]['gorsel'] = kizilay()
    s[5]['gorsel'] = vefa()
    s[6]['gorsel'] = meb()
    s[7]['gorsel'] = yardimlar()
    s[9]['gorsel'] = fikir_karti()
    s[11]['gorsel'] = basliklar()
