"""7. sınıf Matematik 2. hafta (Rasyonel Sayıları Farklı Biçimlerde Gösterme ve Yorumlama) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K024/K048); görsel içi yazı 10.5-13 punto (K150 EK); kesirler yalnız dikey (K155)."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'
EKSI = '−'


def svg(w, h, ic, etiket, en_fazla=20):
    stil = f' style="max-height:calc({en_fazla}mm * var(--ck-olcek, 1))"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=12, renk=LAC, hiza='middle', ince=False):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ if ince else YAZI} fill="{renk}">{metin}</text>'


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.3, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def kesir(x, y, pay, payda, renk=LAC, boy=11.5, isaret=''):
    """Pay üstte, payda altta; (x, y) kesir çizgisinin ortası."""
    g = max(len(pay), len(payda)) * boy * 0.62 + 6
    ic = yazi(x - g / 2 - 2, y + boy * 0.35, isaret, boy, renk, 'end') if isaret else ''
    ic += yazi(x, y - 3, pay, boy, renk)
    ic += f'<line x1="{x - g / 2:.1f}" y1="{y}" x2="{x + g / 2:.1f}" y2="{y}" stroke="{renk}" stroke-width="1.4"/>'
    return ic + yazi(x, y + boy + 1, payda, boy, renk)


def ok_tanim(kimlik, renk=LAC):
    return (f'<marker id="{kimlik}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="{renk}"/></marker>')


def dort_olcum_karti():
    """Soru 1: I (0/9), II (-15/3), III (8/0), IV (4/-7) ölçüm kartları."""
    kartlar = [
        ('I. kart', '0', '9', MAVI, MAVI_A),
        ('II. kart', f'{EKSI}15', '3', YES, YES_A),
        ('III. kart', '8', '0', KIR, KIR_A),
        ('IV. kart', '4', f'{EKSI}7', MOR, MOR_A),
    ]
    ic = ''
    for i, (bas, p, q, r, z) in enumerate(kartlar):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 68, z, r, 8, 1.3)
        ic += yazi(x + 41, 22, bas, 11, r)
        ic += kutu(x + 16, 28, 50, 38, '#fff', r, 6, 1.1)
        ic += kesir(x + 41, 47, p, q, LAC, 12)
    return svg(360, 80, ic, 'Dört ölçüm kartı: I. kart 0 bölü 9, II. kart eksi 15 bölü 3, III. kart 8 bölü 0, IV. kart 4 bölü eksi 7.', 22)


def sayi_kumeleri_semasi():
    """Soru 2: Doğal sayı, tam sayı ve rasyonel sayı kümeleri iç içe şeması."""
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    ic += kutu(12, 10, 336, 74, MOR_A, MOR, 8, 1.3)
    ic += yazi(292, 26, 'Rasyonel Sayılar', 11, MOR)
    ic += kesir(304, 52, '2', '3', MOR, 11, EKSI)
    ic += kutu(20, 18, 224, 58, TUR_A, TUR, 7, 1.3)
    ic += yazi(188, 34, 'Tam Sayılar', 11, TUR)
    ic += yazi(188, 56, f'{EKSI}3, {EKSI}6', 11.5, LAC)
    ic += kutu(28, 26, 114, 42, MAVI_A, MAVI, 6, 1.3)
    ic += yazi(85, 42, 'Doğal Sayılar', 11, MAVI)
    ic += yazi(85, 58, '0, 3', 11.5, LAC)
    return svg(360, 94, ic, 'İç içe sayı kümeleri şeması: Doğal Sayılar (0, 3), onu kapsayan Tam Sayılar (eksi 3, eksi 6) ve en dışta Rasyonel Sayılar (eksi 2 bölü 3).', 20)


def sayi_dogrusu_dort_parca():
    """Soru 4: -2 ile 2 arası her birim 4 eş parçaya bölünmüş sayı doğrusu; K (-7/4), L (-3/4), M (5/4)."""
    x0, b, y = 28, 76, 46
    ic = f'<defs>{ok_tanim("m72ok1")}</defs>'
    ic += f'<line x1="{x0 - 14}" y1="{y}" x2="{x0 + 4 * b + 14}" y2="{y}" stroke="{LAC}" stroke-width="1.8" marker-start="url(#m72ok1)" marker-end="url(#m72ok1)"/>'
    for i in range(17):
        x = x0 + i * b / 4
        tam = i % 4 == 0
        ic += f'<line x1="{x:.1f}" y1="{y - (7 if tam else 4)}" x2="{x:.1f}" y2="{y + (7 if tam else 4)}" stroke="{LAC}" stroke-width="{1.6 if tam else 1.0}"/>'
        if tam:
            n = i // 4 - 2
            ic += yazi(x, y + 22, f'{EKSI}{-n}' if n < 0 else str(n), 12, LAC)
    for idx, ad, renk in [(1, 'K', KIR), (5, 'L', TUR), (13, 'M', MAVI)]:
        xk = x0 + idx * b / 4
        ic += f'<circle cx="{xk:.1f}" cy="{y}" r="4.8" fill="{renk}"/>'
        ic += kutu(xk - 11, y - 30, 22, 18, '#fff', renk, 4, 1.3)
        ic += yazi(xk, y - 17, ad, 11.5, renk)
    return svg(360, 78, ic, 'Sayı doğrusu eksi 2 ile 2 arası 4 eş parçalı: K noktası eksi 7 bölü 4, L noktası eksi 3 bölü 4, M noktası 5 bölü 4.', 22)


def eksi_konumu_karti():
    """Soru 5: -5/8 = (-5)/8 = 5/(-8) = k/24 eşitlik kartı."""
    ic = kutu(4, 4, 352, 76, MAVI_A, MAVI, 8, 1.3)
    ic += yazi(180, 20, 'Eksi İşaretinin Konumu ve Denk Gösterim', 11.5, MAVI)
    kutular = [
        (16, '5', '8', EKSI, MAVI),
        (102, f'{EKSI}5', '8', '', TUR),
        (188, '5', f'{EKSI}8', '', YES),
        (274, 'k', '24', '', MOR),
    ]
    for i, (x, p, q, isr, r) in enumerate(kutular):
        ic += kutu(x, 28, 70, 44, '#fff', r, 6, 1.2)
        ic += kesir(x + (38 if isr else 35), 50, p, q, LAC, 11.5, isr)
        if i < 3:
            ic += yazi(x + 78, 54, '=', 12.5, LAC)
    return svg(360, 84, ic, 'Eşitlik kartı: eksi 5 bölü 8 eşittir eksi 5 bölü 8 eşittir 5 bölü eksi 8 eşittir k bölü 24.', 22)


def mutlak_uzaklik_dogrusu():
    """Soru 7: Sıfıra eşit uzaklıktaki A ve B noktaları (toplam uzaklık 5 birim -> -5/2 ve 5/2)."""
    ic = kutu(4, 4, 352, 86, KUM, GRI, 8, 1.2)
    ic += f'<defs>{ok_tanim("m72ok2")}</defs>'
    x0, b, y = 36, 48, 52
    ic += f'<line x1="18" y1="{y}" x2="342" y2="{y}" stroke="{LAC}" stroke-width="1.8" marker-start="url(#m72ok2)" marker-end="url(#m72ok2)"/>'
    for n in range(-3, 4):
        x = 180 + n * b
        ic += f'<line x1="{x}" y1="{y - 6}" x2="{x}" y2="{y + 6}" stroke="{LAC}" stroke-width="1.5"/>'
        ic += yazi(x, y + 21, f'{EKSI}{-n}' if n < 0 else str(n), 11.5, LAC)
    xa, xb = 180 - 2.5 * b, 180 + 2.5 * b
    ic += f'<circle cx="{xa:.1f}" cy="{y}" r="5" fill="{KIR}"/>' + yazi(xa, y - 12, 'A', 12, KIR)
    ic += f'<circle cx="{xb:.1f}" cy="{y}" r="5" fill="{MAVI}"/>' + yazi(xb, y - 12, 'B', 12, MAVI)
    ic += f'<path d="M{xa:.1f} 26 H180" stroke="{KIR}" stroke-width="1.5"/><path d="M180 26 H{xb:.1f}" stroke="{MAVI}" stroke-width="1.5"/>'
    ic += kutu(108, 12, 144, 20, '#fff', TUR, 5, 1.1)
    ic += yazi(180, 26, 'Toplam uzaklık = 5 birim', 10.5, TUR)
    return svg(360, 94, ic, 'Sayı doğrusunda 0 noktasına eşit uzaklıkta A ve B noktaları; A ile B arası toplam uzaklık 5 birim.', 23)


def denk_kesir_zinciri():
    """Soru 9: 12/18 -> 2/★ -> ▲/15 denk kesir dönüşüm şeması."""
    ic = kutu(4, 4, 352, 82, TUR_A, TUR, 8, 1.3)
    ic += yazi(180, 20, 'Denk Kesir Dönüşüm Zinciri (En Sade Biçim → Genişletme)', 11, TUR)
    halkalar = [
        (20, '12', '18', MAVI, 'Başlangıç'),
        (145, '2', '★', YES, 'En sade'),
        (270, '▲', '15', MOR, 'Denk kesir'),
    ]
    for x, p, q, r, alt in halkalar:
        ic += kutu(x, 28, 70, 50, '#fff', r, 6, 1.3)
        ic += kesir(x + 35, 48, p, q, r if p in ('★', '▲') or q in ('★', '▲') else LAC, 12)
        ic += yazi(x + 35, 73, alt, 10.5, SOLUK, 'middle', True)
    ic += yazi(117, 52, '÷ 6 →', 11.5, YES)
    ic += yazi(242, 52, '× 5 →', 11.5, MOR)
    return svg(360, 90, ic, 'Denk kesir şeması: 12 bölü 18 kesri 6 ile sadeleşince 2 bölü yıldız, 5 ile genişletilince üçgen bölü 15 olur.', 22)


def esit_bolme_karsilastirma():
    """Soru 10: 2/3 kesri için I. (eş olmayan bölme) ve II. (eş bölme) sayı doğrusu karşılaştırması."""
    ic = kutu(4, 4, 172, 80, KIR_A, KIR, 8, 1.3)
    ic += yazi(90, 20, 'I. Çizim (Eş olmayan aralık)', 10.5, KIR)
    ic += f'<line x1="20" y1="48" x2="160" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    for x, lbl in [(28, '0'), (54, ''), (118, '•'), (152, '1')]:
        ic += f'<line x1="{x}" y1="42" x2="{x}" y2="54" stroke="{LAC}" stroke-width="1.4"/>'
        if lbl in ('0', '1'):
            ic += yazi(x, 70, lbl, 11.5, LAC)
    ic += f'<circle cx="118" cy="48" r="4.5" fill="{KIR}"/>' + yazi(118, 36, 'P', 11, KIR)

    ic += kutu(184, 4, 172, 80, YES_A, YES, 8, 1.3)
    ic += yazi(270, 20, 'II. Çizim (3 eş parça)', 10.5, YES)
    ic += f'<line x1="200" y1="48" x2="340" y2="48" stroke="{LAC}" stroke-width="1.8"/>'
    for i, x in enumerate([208, 250, 292, 334]):
        ic += f'<line x1="{x}" y1="42" x2="{x}" y2="54" stroke="{LAC}" stroke-width="1.4"/>'
        if i in (0, 3):
            ic += yazi(x, 70, '0' if i == 0 else '1', 11.5, LAC)
    ic += f'<circle cx="292" cy="48" r="4.5" fill="{YES}"/>' + yazi(292, 36, 'P', 11, YES)
    return svg(360, 88, ic, 'İki sayı doğrusu karşılaştırması: I. çizimde 0 ile 1 arası eşit bölünmemiş, II. çizimde 0 ile 1 arası 3 eş parçaya bölünüp 2. bölmede P noktası işaretlenmiş.', 22)


def su_alti_sensor_panosu():
    """Soru 13: Dört su altı sensörünün deniz seviyesine göre rasyonel derinlik kartları."""
    sensorler = [
        ('K sensörü', '3', '4', MAVI, MAVI_A),
        ('L sensörü', '7', '5', YES, YES_A),
        ('M sensörü', '9', '4', TUR, TUR_A),
        ('N sensörü', '12', '4', MOR, MOR_A),
    ]
    ic = ''
    for i, (ad, p, q, r, z) in enumerate(sensorler):
        x = 6 + i * 88
        ic += kutu(x, 6, 82, 74, z, r, 8, 1.3)
        ic += yazi(x + 41, 22, ad, 11, r)
        ic += kutu(x + 12, 28, 58, 44, '#fff', r, 6, 1.1)
        ic += kesir(x + 44, 50, p, q, LAC, 11.5, EKSI)
    return svg(360, 86, ic, 'Dört su altı sensörü derinlik panosu: K eksi 3 bölü 4 m, L eksi 7 bölü 5 m, M eksi 9 bölü 4 m, N eksi 12 bölü 4 m.', 22)


def sifir_bolme_kartlari():
    """Soru 14: 0/(-8) ve (-8)/0 karşılaştırma kartları."""
    ic = kutu(4, 4, 172, 76, YES_A, YES, 8, 1.3)
    ic += yazi(90, 20, '1. İşlem Kartı (Pay = 0)', 11, YES)
    ic += kesir(56, 48, '0', f'{EKSI}8', LAC, 12)
    ic += yazi(114, 52, '= 0', 12.5, YES)

    ic += kutu(184, 4, 172, 76, KIR_A, KIR, 8, 1.3)
    ic += yazi(270, 20, '2. İşlem Kartı (Payda = 0)', 11, KIR)
    ic += kesir(232, 48, f'{EKSI}8', '0', LAC, 12)
    ic += yazi(298, 52, '→ Tanımsız', 11.5, KIR)
    return svg(360, 84, ic, 'İki işlem kartı: 1. kartta 0 bölü eksi 8 eşittir 0; 2. kartta eksi 8 bölü 0 tanımsız.', 22)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = dort_olcum_karti()
    s[1]['gorsel'] = sayi_kumeleri_semasi()
    s[3]['gorsel'] = sayi_dogrusu_dort_parca()
    s[4]['gorsel'] = eksi_konumu_karti()
    s[6]['gorsel'] = mutlak_uzaklik_dogrusu()
    s[8]['gorsel'] = denk_kesir_zinciri()
    s[9]['gorsel'] = esit_bolme_karsilastirma()
    s[12]['gorsel'] = su_alti_sensor_panosu()
    s[13]['gorsel'] = sifir_bolme_kartlari()
