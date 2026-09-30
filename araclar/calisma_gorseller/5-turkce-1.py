"""5. sınıf Türkçe 1. hafta (tahmin etme, yüzey anlam, söz varlığı) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fde8e7', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2b705'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
INCE = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {INCE if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def numara(x, y, n, renk):
    return f'<circle cx="{x}" cy="{y}" r="9" fill="{renk}"/>' + yazi(x, y + 4, str(n), 11, '#fff')


def kapak():
    """Kitap kapağı: başlık, ağaç, hazine haritası, kürek, sandık."""
    ic = kutu(100, 4, 160, 142, '#fef7e6', LAC, 6, 1.6) + f'<rect x="100" y="4" width="10" height="142" rx="3" fill="{LAC}"/>'
    ic += f'<rect x="110" y="12" width="150" height="28" fill="{YES}"/>' + yazi(185, 31, 'Bahçedeki Hazine', 13.5, '#fff')
    ic += f'<rect x="114" y="46" width="140" height="54" fill="{CAM_A}"/><rect x="114" y="100" width="140" height="40" fill="#bfe6c9"/>'
    ic += f'<circle cx="238" cy="60" r="8" fill="{ALTIN}"/>'
    # ağaç
    ic += f'<rect x="127" y="80" width="8" height="36" fill="{KAHVE}"/><circle cx="131" cy="72" r="15" fill="{YES}"/><circle cx="121" cy="82" r="9" fill="#0f8a44"/><circle cx="141" cy="82" r="9" fill="#0f8a44"/>'
    # harita
    ic += f'<rect x="156" y="58" width="60" height="40" rx="2" fill="#f6e7c1" stroke="#b08a4a" stroke-width="1.2" transform="rotate(-4 186 78)"/>'
    ic += f'<path d="M163 91 Q172 70 185 84 T207 68" fill="none" stroke="{KIR}" stroke-width="1.6" stroke-dasharray="3 2.5"/>'
    ic += f'<path d="M203 64 l8 8 M211 64 l-8 8" stroke="{KIR}" stroke-width="2.2" stroke-linecap="round"/>'
    # sandık
    ic += f'<rect x="170" y="112" width="26" height="16" rx="2" fill="#b86b2a" stroke="{KAHVE}" stroke-width="1.2"/><path d="M170 112 q13 -9 26 0" fill="#c97d38" stroke="{KAHVE}" stroke-width="1.2"/>'
    ic += f'<rect x="180" y="113" width="6" height="7" rx="1" fill="{ALTIN}"/>'
    # kürek
    ic += f'<line x1="232" y1="84" x2="232" y2="120" stroke="{KAHVE}" stroke-width="3" stroke-linecap="round"/><path d="M226 120 H238 L236 134 Q232 139 228 134 Z" fill="#7d8799"/>'
    return svg(360, 150, ic, 'Kitap kapağı: Bahçedeki Hazine. Kapakta bir ağaç, üzerinde kesik çizgili yol ve çarpı işareti olan bir harita, bir sandık ve bir kürek var', 30)


def s_bardak(x, y):
    g = (f'M{x - 9} {y + 4} C{x - 9} {y + 13} {x - 4} {y + 15} {x - 5} {y + 21} C{x - 6} {y + 26} {x - 9} {y + 29} {x - 9} {y + 34} '
         f'H{x + 9} C{x + 9} {y + 29} {x + 6} {y + 26} {x + 5} {y + 21} C{x + 4} {y + 15} {x + 9} {y + 13} {x + 9} {y + 4} Z')
    return (f'<path d="{g}" fill="#c0541b" stroke="{KAHVE}" stroke-width="1"/><ellipse cx="{x}" cy="{y + 37}" rx="17" ry="4" fill="#fff" stroke="{GRI}" stroke-width="1.2"/>'
            f'<path d="M{x - 3} {y - 1} q-3 -4 0 -8 M{x + 3} {y - 1} q-3 -4 0 -8" fill="none" stroke="{GRI}" stroke-width="1.2" stroke-linecap="round"/>')


def s_dere(x, y):
    return (f'<rect x="{x - 24}" y="{y - 6}" width="48" height="46" rx="6" fill="#bfe6c9"/>'
            f'<path d="M{x - 10} {y - 6} C{x - 2} {y + 8} {x - 16} {y + 22} {x - 4} {y + 40} H{x + 12} C{x} {y + 22} {x + 14} {y + 8} {x + 6} {y - 6} Z" fill="#7cc3f0"/>'
            f'<path d="M{x - 3} {y + 6} q3 3 6 0 M{x - 6} {y + 24} q3 3 6 0" fill="none" stroke="#fff" stroke-width="1.2"/>'
            f'<ellipse cx="{x - 16}" cy="{y + 30}" rx="4" ry="3" fill="{GRI}"/><ellipse cx="{x + 17}" cy="{y + 8}" rx="4" ry="3" fill="{GRI}"/>')


def s_hilal(x, y):
    return (f'<rect x="{x - 24}" y="{y - 6}" width="48" height="46" rx="6" fill="#1e2a55"/>'
            f'<circle cx="{x - 2}" cy="{y + 17}" r="13" fill="{ALTIN}"/><circle cx="{x + 5}" cy="{y + 12}" r="11" fill="#1e2a55"/>'
            f'<circle cx="{x + 14}" cy="{y + 30}" r="1.6" fill="#fff"/><circle cx="{x + 16}" cy="{y + 2}" r="1.3" fill="#fff"/><circle cx="{x - 16}" cy="{y + 2}" r="1.2" fill="#fff"/>')


def s_takvim(x, y):
    ic = f'<rect x="{x - 22}" y="{y - 4}" width="44" height="44" rx="4" fill="#fff" stroke="{GRI}" stroke-width="1.2"/><rect x="{x - 22}" y="{y - 4}" width="44" height="12" rx="4" fill="{KIR}"/>'
    ic += yazi(x, y + 5.5, 'EYLÜL', 8.5, '#fff')
    ic += ''.join(f'<rect x="{x - 18 + c * 9}" y="{y + 12 + r * 8}" width="6" height="5" fill="{GRI_A}"/>' for r in range(3) for c in range(4))
    return ic


def s_yaz_mevsim(x, y):
    return (f'<rect x="{x - 24}" y="{y - 6}" width="48" height="46" rx="6" fill="{CAM_A}"/><rect x="{x - 24}" y="{y + 22}" width="48" height="18" fill="#7cc3f0"/>'
            f'<path d="M{x - 24} {y + 32} h48 v2 a6 6 0 0 1 -6 6 h-36 a6 6 0 0 1 -6 -6 z" fill="#f3d9a4"/>'
            f'<circle cx="{x + 10}" cy="{y + 6}" r="7" fill="{ALTIN}"/>'
            + ''.join(f'<line x1="{x + 10 + 10 * c:.1f}" y1="{y + 6 + 10 * s:.1f}" x2="{x + 10 + 13 * c:.1f}" y2="{y + 6 + 13 * s:.1f}" stroke="{ALTIN}" stroke-width="1.4"/>'
                      for c, s in [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)])
            + f'<line x1="{x - 12}" y1="{y + 36}" x2="{x - 12}" y2="{y + 10}" stroke="{KAHVE}" stroke-width="1.6"/><path d="M{x - 24} {y + 12} Q{x - 12} {y} {x} {y + 12} Z" fill="{KIR}"/>')


def s_yazmak(x, y):
    ic = f'<rect x="{x - 20}" y="{y - 4}" width="36" height="44" rx="2" fill="#fff" stroke="{GRI}" stroke-width="1.2"/>'
    ic += ''.join(f'<line x1="{x - 16}" y1="{y + 6 + k * 8}" x2="{x + 12}" y2="{y + 6 + k * 8}" stroke="{MAVI_A}" stroke-width="1.2"/>' for k in range(4))
    ic += f'<path d="M{x - 15} {y + 20} q3 -5 6 0 t6 0 t6 0" fill="none" stroke="{LAC}" stroke-width="1.3"/>'
    ic += (f'<g transform="rotate(35 {x + 8} {y + 18})"><rect x="{x + 4}" y="{y - 8}" width="8" height="26" fill="{ALTIN}"/>'
           f'<path d="M{x + 4} {y + 18} L{x + 8} {y + 27} L{x + 12} {y + 18} Z" fill="#f3d9a4"/><path d="M{x + 6.6} {y + 24} L{x + 8} {y + 27} L{x + 9.4} {y + 24} Z" fill="{LAC}"/>'
           f'<rect x="{x + 4}" y="{y - 12}" width="8" height="4" fill="{KIR}"/></g>')
    return ic


def es_sesli():
    """Üç resim çifti: çay (bardak/dere), ay (hilal/takvim), yaz (mevsim/yazmak)."""
    ciz = [s_bardak, s_dere, s_hilal, s_takvim, s_yaz_mevsim, s_yazmak]
    renk = [TUR, TUR, MOR, MOR, CAM, CAM]
    ic = ''
    for p in range(3):
        x0 = 4 + p * 119
        ic += kutu(x0, 4, 114, 74, [TUR_A, MOR_A, CAM_A][p], renk[2 * p], 8, 1.2)
        for k in range(2):
            n = 2 * p + k
            cx = x0 + 30 + k * 54
            ic += ciz[n](cx, 30) + numara(cx - 20, 14, n + 1, renk[n])
    return svg(360, 82, ic, 'Resimler: 1 çay bardağı, 2 akan küçük dere, 3 gökyüzünde hilal, 4 Eylül takvim yaprağı, 5 güneşli deniz kıyısı, 6 kâğıda yazan kalem', 24)


def duyuru():
    """Oyun şenliği duyurusu (afiş)."""
    ic = kutu(8, 4, 344, 136, TUR_A, TUR, 10, 2)
    ic += f'<rect x="8" y="4" width="344" height="30" rx="10" fill="{TUR}"/><rect x="8" y="24" width="344" height="10" fill="{TUR}"/>'
    ic += yazi(180, 26, 'OYUN ŞENLİĞİ', 17, '#fff')
    ic += yazi(24, 56, 'Seksek · Çember çevirme · Mendil kapmaca', 12.5, LAC, 'start')
    ic += yazi(24, 80, '26 Eylül Cumartesi · 10.00–13.00', 12.5, KIR, 'start')
    ic += yazi(24, 102, 'Yer: Çınarlı Park', 12.5, LAC, 'start', True)
    ic += yazi(24, 126, 'Rahat ayakkabılarınızı giymeyi unutmayın!', 12, SOLUK, 'start', True)
    # seksek
    sx, sy = 322, 52
    for dx, dy in [(0, 72), (0, 56), (-9, 40), (9, 40), (0, 24)]:
        ic += f'<rect x="{sx + dx - 9}" y="{sy + dy - 16}" width="18" height="16" fill="#fff" stroke="{MAVI}" stroke-width="1.3"/>'
    return svg(360, 144, ic, 'Duyuru: Oyun şenliği. Seksek, çember çevirme, mendil kapmaca. 26 Eylül Cumartesi, 10.00-13.00. Yer: Çınarlı Park. Rahat ayakkabılarınızı giymeyi unutmayın!', 28)


def metin():
    """Defter sayfasında kısa metin (içeriği yansıtan kelimeler sorusu)."""
    satir = ['Dedem, çocukken arkadaşlarıyla en çok topaç',
             'çevirdiğini anlatır. Topacını tahtadan kendisi',
             'oymuş. İpini topaca sarar, bir hamlede yere',
             'fırlatırmış. Topaç ne kadar uzun dönerse o kadar',
             'sevinirmiş. Dedem eski topacını hâlâ saklıyor.']
    ic = kutu(4, 4, 352, 134, '#fffdf5', GRI, 6, 1.2) + f'<line x1="26" y1="4" x2="26" y2="138" stroke="{KIR}" stroke-width="1" opacity="0.6"/>'
    ic += yazi(180, 24, 'Dedemin Topacı', 13.5, MOR)
    for i, s in enumerate(satir):
        y = 50 + i * 20
        ic += f'<line x1="30" y1="{y + 5}" x2="350" y2="{y + 5}" stroke="{MAVI_A}" stroke-width="1"/>' + yazi(34, y, s, 12, LAC, 'start', True)
    # topaç
    tx, ty = 318, 18
    ic += (f'<path d="M{tx - 12} {ty} Q{tx} {ty - 8} {tx + 12} {ty} L{tx} {ty + 16} Z" fill="{KIR}"/><rect x="{tx - 1.5}" y="{ty - 10}" width="3" height="6" fill="{KAHVE}"/>'
           f'<path d="M{tx - 10} {ty + 2} Q{tx} {ty + 6} {tx + 10} {ty + 2}" fill="none" stroke="#fff" stroke-width="1.4"/>')
    return svg(360, 142, ic, 'Metin, Dedemin Topacı: Dedem, çocukken arkadaşlarıyla en çok topaç çevirdiğini anlatır. Topacını tahtadan kendisi oymuş. İpini topaca sarar, bir hamlede yere fırlatırmış. Topaç ne kadar uzun dönerse o kadar sevinirmiş. Dedem eski topacını hâlâ saklıyor.', 28)


def unsurlar():
    """A harita, B afiş, C grafik simge, D fotoğraf."""
    ic = ''
    renk = [YES, TUR, KIR, MAVI]
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 84, '#fff', renk[i], 8, 1.3)
        ic += f'<circle cx="{x0 + 13}" cy="17" r="9" fill="{renk[i]}"/>' + yazi(x0 + 13, 21, 'ABCD'[i], 11, '#fff')
    # A harita
    x = 4
    ic += (f'<path d="M{x + 18} 40 Q{x + 30} 28 {x + 52} 34 Q{x + 74} 38 {x + 70} 58 Q{x + 66 } 78 {x + 42} 78 Q{x + 16} 80 {x + 14} 62 Q{x + 10} 50 {x + 18} 40 Z" fill="#bfe6c9" stroke="{YES}" stroke-width="1"/>'
           f'<path d="M{x + 30} 36 Q{x + 40} 52 {x + 34} 62 T{x + 44} 78" fill="none" stroke="#5aa9e6" stroke-width="2.2"/>'
           f'<path d="M{x + 18} 58 L{x + 66} 50" stroke="{KIR}" stroke-width="1.4" stroke-dasharray="3 2"/>'
           f'<circle cx="{x + 56}" cy="52" r="2.6" fill="{LAC}"/><path d="M{x + 70} 12 l3 9 h-6 z" fill="{LAC}"/>' + yazi(x + 70, 30, 'K', 9, LAC))
    # B afiş
    x = 93
    ic += (f'<rect x="{x + 26}" y="30" width="44" height="52" fill="{TUR_A}" stroke="{TUR}" stroke-width="1.2"/><rect x="{x + 26}" y="30" width="44" height="12" fill="{TUR}"/>'
           + yazi(x + 48, 39.5, 'KİTAP', 7.5, '#fff') + f'<path d="M{x + 48} 47 l3 7 7 1 -5 5 1.5 7 -6.5 -3.5 -6.5 3.5 1.5 -7 -5 -5 7 -1 z" fill="{ALTIN}"/>'
           f'<rect x="{x + 32}" y="70" width="32" height="3" fill="{TUR}"/><rect x="{x + 36}" y="76" width="24" height="3" fill="{GRI}"/>')
    # C grafik simge (telefon yasak)
    x = 182
    ic += (f'<rect x="{x + 36}" y="36" width="14" height="26" rx="3" fill="{LAC}"/><rect x="{x + 38}" y="40" width="10" height="16" fill="#fff"/>'
           f'<circle cx="{x + 43}" cy="49" r="22" fill="none" stroke="{KIR}" stroke-width="4"/><line x1="{x + 28}" y1="34" x2="{x + 58}" y2="64" stroke="{KIR}" stroke-width="4"/>')
    # D fotoğraf
    x = 271
    ic += (f'<g transform="rotate(-5 {x + 44} 54)"><rect x="{x + 16}" y="30" width="56" height="48" fill="#fff" stroke="{GRI}" stroke-width="1.2"/>'
           f'<rect x="{x + 20}" y="34" width="48" height="34" fill="{CAM_A}"/><path d="M{x + 20} 68 L{x + 34} 48 L{x + 44} 60 L{x + 52} 52 L{x + 68} 68 Z" fill="{YES}"/>'
           f'<circle cx="{x + 60}" cy="42" r="4" fill="{ALTIN}"/><rect x="{x + 38}" y="26" width="12" height="7" fill="#f3d9a4" opacity="0.9"/></g>')
    return svg(360, 92, ic, 'A: harita, B: kitap afişi, C: telefon yasağı simgesi, D: dağ manzarası fotoğrafı', 24)


def grafik():
    """Dikey sütun grafiği: teneffüs oyunları (yakan top 9, halat çekme 11, çuval yarışı 4, birdirbir 6)."""
    x0, y0, x1, ust = 58, 142, 352, 32
    birim = (y0 - ust) / 12
    ic = yazi(190, 16, '5/B Sınıfının Seçtiği Teneffüs Oyunları', 13, LAC)
    for v in range(0, 13):
        y = y0 - v * birim
        ic += f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{GRI_A if v % 2 else "#d5dbe6"}" stroke-width="1"/>'
        if v % 2 == 0:
            ic += yazi(x0 - 6, y + 4, str(v), 10.5, SOLUK, 'end', True)
    ic += f'<line x1="{x0}" y1="{ust - 4}" x2="{x0}" y2="{y0}" stroke="{LAC}" stroke-width="1.4"/><line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{LAC}" stroke-width="1.4"/>'
    ic += f'<text x="16" y="{(ust + y0) / 2:.1f}" text-anchor="middle" font-size="10.5" {INCE} fill="{SOLUK}" transform="rotate(-90 16 {(ust + y0) / 2:.1f})">Öğrenci sayısı</text>'
    veri = [('Yakan top', 9, MAVI), ('Halat çekme', 11, TUR), ('Çuval yarışı', 4, YES), ('Birdirbir', 6, MOR)]
    adim = (x1 - x0) / 4
    for i, (ad, v, c) in enumerate(veri):
        cx = x0 + adim * (i + 0.5)
        ic += f'<rect x="{cx - 20:.1f}" y="{y0 - v * birim:.1f}" width="40" height="{v * birim:.1f}" rx="3" fill="{c}"/>'
        ic += yazi(cx, y0 + 16, ad, 11, LAC)
    return svg(360, 164, ic, 'Sütun grafiği: 5/B sınıfının seçtiği teneffüs oyunları. Yakan top 9, halat çekme 11, çuval yarışı 4, birdirbir 6 öğrenci', 32)


def merdiven():
    """Cümle merdiveni: 1 ve 2 dolu, 3-5 boş; kelime kartları."""
    ic = ''
    for i, k in enumerate(['gökyüzünde', 'süzülerek']):
        x = 196 + i * 82
        ic += kutu(x, 4, 76, 24, '#fff7d6', ALTIN, 5, 1.6) + yazi(x + 38, 20.5, k, 12, LAC)
    dolu = {1: 'Uçurtma uçtu.', 2: 'Renkli uçurtma uçtu.'}
    renk = [MAVI, YES, TUR, MOR, KIR]
    for k in range(1, 6):
        y = 36 + (5 - k) * 26
        w = 70 + k * 50
        c = renk[k - 1]
        if k in dolu:
            ic += kutu(32, y, w, 22, '#fff', c, 5, 1.5) + yazi(40, y + 15.5, dolu[k], 12, LAC, 'start', True)
        else:
            ic += kutu(32, y, w, 22, '#fff', c, 5, 1.5, ' stroke-dasharray="4 3"')
        ic += numara(16, y + 11, k, c)
    return svg(360, 168, ic, 'Cümle merdiveni: 1. basamak Uçurtma uçtu. 2. basamak Renkli uçurtma uçtu. 3, 4 ve 5. basamaklar boş. Kartlar: gökyüzünde, süzülerek', 30)


def kart():
    """Konu kartları kutusu ve çekilen kart; 30 saniye düşünme süresi."""
    ic = ''
    # kutu ve içindeki kartlar
    for i, c in enumerate([MAVI, YES, MOR]):
        ic += f'<rect x="{26 + i * 16}" y="{24 - i * 3}" width="30" height="40" rx="3" fill="#fff" stroke="{c}" stroke-width="1.3" transform="rotate({-10 + i * 10} {41 + i * 16} 44)"/>'
    ic += f'<path d="M14 48 H104 L98 108 H20 Z" fill="#c97d38" stroke="{KAHVE}" stroke-width="1.4"/><path d="M14 48 L4 36 M104 48 L114 36" stroke="{KAHVE}" stroke-width="1.4"/>'
    # çekilen kart
    ic += kutu(132, 10, 158, 96, TUR_A, TUR, 10, 2)
    ic += yazi(211, 32, 'KONU', 11, TUR) + f'<line x1="176" y1="40" x2="246" y2="40" stroke="{TUR}" stroke-width="1.2"/>'
    ic += yazi(211, 64, 'Bir oyunda yaşadığım', 12.5, LAC) + yazi(211, 84, 'unutulmaz an', 12.5, LAC)
    # kum saati
    hx, hy = 324, 20
    ic += (f'<rect x="{hx - 16}" y="{hy}" width="32" height="5" rx="2" fill="{KAHVE}"/><rect x="{hx - 16}" y="{hy + 55}" width="32" height="5" rx="2" fill="{KAHVE}"/>'
           f'<path d="M{hx - 12} {hy + 5} H{hx + 12} Q{hx + 12} {hy + 20} {hx + 2} {hy + 30} Q{hx + 12} {hy + 40} {hx + 12} {hy + 55} H{hx - 12} Q{hx - 12} {hy + 40} {hx - 2} {hy + 30} Q{hx - 12} {hy + 20} {hx - 12} {hy + 5} Z" fill="{CAM_A}" stroke="{CAM}" stroke-width="1.3"/>'
           f'<path d="M{hx - 7} {hy + 15} H{hx + 7} L{hx} {hy + 28} Z" fill="{ALTIN}"/><path d="M{hx - 10} {hy + 53} Q{hx} {hy + 42} {hx + 10} {hy + 53} Z" fill="{ALTIN}"/>')
    ic += yazi(hx, hy + 76, '30 saniye', 11, CAM) + yazi(hx, hy + 90, 'düşün', 11, CAM, 'middle', True)
    return svg(360, 114, ic, 'Konu kartları kutusu ve çekilen kart: Konu, bir oyunda yaşadığım unutulmaz an. Yanında kum saati: 30 saniye düşün', 24)


def uygula(o):
    s = o['sorular']
    s[1]['gorsel'] = kapak()
    s[5]['gorsel'] = es_sesli()
    s[6]['gorsel'] = duyuru()
    s[7]['gorsel'] = metin()
    s[8]['gorsel'] = grafik()
    s[9]['gorsel'] = merdiven()
    s[10]['gorsel'] = kart()
