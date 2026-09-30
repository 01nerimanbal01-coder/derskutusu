"""7. sınıf Türkçe 1. hafta (Martı Jonathan Livingston, metnin bölümleri, noktalı virgül, e-posta) çalışma kâğıdı görselleri (SVG; insan figürü yok; renkler açık hex)."""
import math

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


def rozet(x, y, h, renk, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4, h, 11, '#fff')


def ilk_kulac():
    """Metin başlığı ve resmi: havuz, bone, gözlük."""
    ic = kutu(60, 4, 240, 132, '#fff', CAM, 10, 1.6) + yazi(180, 28, 'İlk Kulaç', 16, CAM)
    ic += f'<rect x="76" y="40" width="208" height="84" rx="4" fill="#7cc3f0"/>'
    for k in range(1, 4):
        y = 40 + k * 21
        ic += ''.join(f'<circle cx="{80 + j * 8}" cy="{y}" r="2.4" fill="{KIR if j % 2 else "#fff"}"/>' for j in range(26))
    ic += ''.join(f'<path d="M{90 + j * 40} {50 + (j % 3) * 21} q5 -3 10 0 t10 0" fill="none" stroke="#fff" stroke-width="1.2" opacity="0.8"/>' for j in range(4))
    # kenarda bone ve gözlük
    ic += f'<path d="M210 118 a16 13 0 0 1 32 0 z" fill="{TUR}"/><path d="M214 112 q12 -6 24 0" fill="none" stroke="#fff" stroke-width="1.2" opacity="0.7"/>'
    ic += (f'<ellipse cx="256" cy="113" rx="7" ry="5" fill="#bfe3f5" stroke="{LAC}" stroke-width="1.6"/><ellipse cx="274" cy="113" rx="7" ry="5" fill="#bfe3f5" stroke="{LAC}" stroke-width="1.6"/>'
           f'<path d="M263 113 h4" stroke="{LAC}" stroke-width="1.6"/>')
    ic += f'<rect x="200" y="118" width="84" height="6" fill="#dfe6ee"/>'
    return svg(360, 140, ic, 'Metin başlığı: İlk Kulaç. Resimde kulvarları ayrılmış bir yüzme havuzu, havuz kenarında bir bone ve bir yüzücü gözlüğü var', 25)


def martı(x, y, renk=LAC):
    return f'<path d="M{x - 10} {y} q5 -6 10 0 q5 -6 10 0" fill="none" stroke="{renk}" stroke-width="2" stroke-linecap="round"/>'


def ucus():
    """Dört uçuş yolu: A düz eğik, B zikzak, C düz yatay, D yay biçimli (kavis)."""
    ic = ''
    for i in range(4):
        x0 = 4 + i * 89
        ic += kutu(x0, 4, 84, 96, CAM_A, CAM, 8, 1.2) + rozet(x0 + 13, 17, 'ABCD'[i], CAM)
        ic += f'<path d="M{x0 + 2} 86 q10 -5 20 0 t20 0 t20 0 t20 0 v12 h-80 z" fill="#7cc3f0"/>'
        sx, sy = x0 + 24, 36
        ic += martı(sx, sy - 6)
        if i == 0:
            yol = f'M{sx} {sy} L{x0 + 66} 82'
        elif i == 1:
            yol = f'M{sx} {sy} L{x0 + 56} 46 L{x0 + 30} 58 L{x0 + 62} 68 L{x0 + 44} 82'
        elif i == 2:
            yol = f'M{sx} {sy} L{x0 + 76} {sy}'
        else:
            yol = f'M{sx} {sy} C{x0 + 90} {sy - 6} {x0 + 84} 74 {x0 + 50} 82'
        ic += f'<path d="{yol}" fill="none" stroke="{TUR}" stroke-width="2" stroke-dasharray="4 3"/>'
    return svg(360, 104, ic, 'Uçuş yolları: A denize doğru düz eğik çizgi, B zikzak, C düz yatay çizgi, D denize doğru yay biçiminde eğri', 22)


def kartlar():
    """Karışık sıradaki hikâye kartları."""
    kart = [('A', 'Bir hafta sonra Deniz, rampadan düşmeden indi.', TUR, TUR_A),
            ('B', 'Deniz, parkta kaykayla ilk kez rampaya çıkmak istedi.', MAVI, MAVI_A),
            ('C', 'Her denemede dengesini kaybetti, dizi sıyrıldı.', MOR, MOR_A)]
    ic = ''
    for i, (h, s, c, d) in enumerate(kart):
        y = 4 + i * 34
        ic += kutu(4, y, 352, 29, d, c, 8, 1.3) + rozet(21, y + 14.5, h, c) + yazi(38, y + 19, s, 12, LAC, 'start', True)
    return svg(360, 106, ic, 'Kartlar: A Bir hafta sonra Deniz, rampadan düşmeden indi. B Deniz, parkta kaykayla ilk kez rampaya çıkmak istedi. C Her denemede dengesini kaybetti, dizi sıyrıldı.', 24)


def notlar():
    """Ece'nin konuşma notları."""
    satir = [('Ne zaman?', 'Geçen kış'), ('Ne öğrenmeye çalışıyordum?', 'Satranç oynamayı'),
             ('Ne yapmam gerekiyordu?', 'Taşların hareketlerini öğrenmek'), ('Ne yaptım?', 'Her akşam dedemle oynadım.'),
             ('Sonuç ne oldu?', 'Okul turnuvasında üçüncü oldum.')]
    ic = kutu(4, 4, 412, 128, '#fff8dc', ALTIN, 6, 1.4) + yazi(210, 22, 'Konuşma notlarım', 12.5, KAHVE)
    for i, (s, c) in enumerate(satir):
        y = 44 + i * 20
        ic += f'<line x1="14" y1="{y + 6}" x2="406" y2="{y + 6}" stroke="#f0dca0" stroke-width="1"/>'
        ic += yazi(16, y, s, 11.5, LAC, 'start') + yazi(206, y, c, 11.5, SOLUK, 'start', True)
    return svg(420, 136, ic, 'Konuşma notlarım: Ne zaman? Geçen kış. Ne öğrenmeye çalışıyordum? Satranç oynamayı. Ne yapmam gerekiyordu? Taşların hareketlerini öğrenmek. Ne yaptım? Her akşam dedemle oynadım. Sonuç ne oldu? Okul turnuvasında üçüncü oldum.', 29)


def nv(parca, x, y):
    """Noktalı virgülleri turuncu gösteren satır."""
    ic = ''.join(f'<tspan fill="{TUR}" font-weight="800">;</tspan>' if p == ';' else p for p in parca)
    return f'<text x="{x}" y="{y}" font-size="12" {INCE} fill="{LAC}">{ic}</text>'


def cumleler():
    cum = [['Rüzgâr sertleşti, dalgalar büyüdü', ';', ' martılar kıyıya döndü.'],
           ['Rafta kalem, silgi, cetvel', ';', ' dolapta boya, fırça vardı.'],
           ['Jonathan', ';', ' sabırlı, cesur ve kararlıydı.']]
    ic = ''
    for i, p in enumerate(cum):
        y = 4 + i * 32
        ic += kutu(4, y, 392, 27, '#fff', GRI, 8, 1.2) + rozet(21, y + 13.5, str(i + 1), TUR) + nv(p, 38, y + 18)
    return svg(400, 98, ic, 'Cümleler: 1. Rüzgâr sertleşti, dalgalar büyüdü; martılar kıyıya döndü. 2. Rafta kalem, silgi, cetvel; dolapta boya, fırça vardı. 3. Jonathan; sabırlı, cesur ve kararlıydı.', 22)


def gelen_kutusu():
    ic = kutu(4, 4, 352, 112, '#fff', GRI, 8, 1.3) + f'<rect x="4" y="4" width="352" height="22" rx="8" fill="{MAVI}"/><rect x="4" y="18" width="352" height="8" fill="{MAVI}"/>'
    ic += yazi(16, 19.5, 'Belediye · Gelen kutusu', 11.5, '#fff', 'start')
    konu = ['Merhaba', 'Okul önündeki sokak lambası yanmıyor', 'ACİL!!!']
    for i, k in enumerate(konu):
        y = 32 + i * 28
        ic += f'<rect x="10" y="{y}" width="340" height="24" rx="4" fill="{MAVI_A if i % 2 == 0 else GRI_A}"/>'
        ic += rozet(24, y + 12, str(i + 1), MAVI, 8)
        ic += f'<rect x="40" y="{y + 7}" width="12" height="9" rx="1" fill="none" stroke="{SOLUK}" stroke-width="1.1"/><path d="M40 {y + 7} l6 5 l6 -5" fill="none" stroke="{SOLUK}" stroke-width="1.1"/>'
        ic += yazi(62, y + 16.5, 'Konu:', 11.5, SOLUK, 'start', True) + yazi(98, y + 16.5, k, 12, LAC, 'start')
    return svg(360, 120, ic, 'Belediyenin gelen kutusu, konu satırları: 1. Merhaba 2. Okul önündeki sokak lambası yanmıyor 3. ACİL!!!', 26)


def eposta():
    ic = kutu(4, 4, 352, 172, '#fff', GRI, 8, 1.3) + f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{GRI_A}"/><rect x="4" y="16" width="352" height="8" fill="{GRI_A}"/>'
    ic += ''.join(f'<circle cx="{16 + k * 12}" cy="14" r="3.5" fill="{c}"/>' for k, c in enumerate([KIR, ALTIN, YES]))
    ic += yazi(14, 42, 'Kime:', 11.5, SOLUK, 'start', True) + yazi(58, 42, 'Park ve Bahçeler Müdürlüğü', 11.5, LAC, 'start')
    ic += yazi(14, 60, 'Konu:', 11.5, SOLUK, 'start', True) + yazi(58, 60, 'Çınar Parkı’ndaki kırık salıncak', 11.5, LAC, 'start')
    ic += (f'<path d="M18 72 v8 a3 3 0 0 0 6 0 v-9 a2 2 0 0 0 -4 0 v8" fill="none" stroke="{SOLUK}" stroke-width="1.2"/>'
           + yazi(30, 80, 'Ek: salincak.jpg', 11, SOLUK, 'start', True))
    ic += f'<line x1="12" y1="88" x2="348" y2="88" stroke="{GRI}" stroke-width="0.8"/>'
    govde = ['Sayın Yetkili,', 'Çınar Parkı’ndaki salıncaklardan birinin zinciri kopmuş.',
             'Küçük çocuklar yine de bu salıncağa binmeye çalışıyor.', 'Bilgilerinize sunarım.', 'Ali Kaya']
    for i, s in enumerate(govde):
        ic += yazi(14, 106 + i * 16, s, 11.5, LAC, 'start', True)
    return svg(360, 180, ic, 'E-posta. Kime: Park ve Bahçeler Müdürlüğü. Konu: Çınar Parkı’ndaki kırık salıncak. Ek: salincak.jpg. Sayın Yetkili, Çınar Parkı’ndaki salıncaklardan birinin zinciri kopmuş. Küçük çocuklar yine de bu salıncağa binmeye çalışıyor. Bilgilerinize sunarım. Ali Kaya', 38)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = ilk_kulac()
    s[4]['gorsel'] = ucus()
    s[6]['gorsel'] = kartlar()
    s[7]['gorsel'] = notlar()
    s[8]['gorsel'] = cumleler()
    s[10]['gorsel'] = gelen_kutusu()
    s[11]['gorsel'] = eposta()
