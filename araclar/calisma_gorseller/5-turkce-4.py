"""5. sınıf Türkçe 4. hafta (Bir İp Bul, Oyuna Başla!: konuşma, akıcı okuma, isim-fiil, yazım, e-posta) çalışma kâğıdı görselleri.
SVG; insan figürü yok (K048); görsel içi yazı sayfa puntosunda (K150 EK: 13 birim ≈ gövde, 12 ≈ tablo puntosu); renkler açık hex."""

LAC, MAVI, TUR, YES, KIR, MOR, CAM = '#0b2257', '#2451d6', '#ee7d12', '#12a150', '#d63a3a', '#7c3aed', '#0e8fa8'
MAVI_A, TUR_A, YES_A, MOR_A, KIR_A, CAM_A = '#e8eefe', '#fff1df', '#e3f6ea', '#f0e9fe', '#fdeaea', '#e0f4f8'
GRI, GRI_A, SOLUK, KAHVE, ALTIN, KUM = '#9aa6bd', '#eef1f6', '#5b6479', '#8a5a2b', '#f2c14e', '#fffdf5'
YAZI = 'font-family="Noto Sans, sans-serif" font-weight="700"'
DUZ = 'font-family="Noto Sans, sans-serif" font-weight="400"'


def svg(w, h, ic, etiket, en_fazla=None):
    stil = f' style="max-height:{en_fazla}mm"' if en_fazla else ''
    return f'<svg viewBox="0 0 {w} {h}"{stil} role="img" aria-label="{etiket}">{ic}</svg>'


def yazi(x, y, metin, boy=13, renk=LAC, hiza='middle', ek=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{hiza}" font-size="{boy}" {YAZI} fill="{renk}"{ek}>{metin}</text>'


def duz(x, y, satirlar, boy=13, renk=LAC, hiza='start', ara=16, ek=''):
    return ''.join(f'<text x="{x:.1f}" y="{y + k * ara:.1f}" text-anchor="{hiza}" font-size="{boy}" {DUZ} fill="{renk}"{ek}>{m}</text>'
                   for k, m in enumerate(satirlar))


def kutu(x, y, w, h, dolgu, cizgi, r=8, kalin=1.4, ek=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{dolgu}" stroke="{cizgi}" stroke-width="{kalin}"{ek}/>'


def numara(x, y, n, renk=LAC, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>' + yazi(x, y + 4.3, str(n), 11.5, '#fff')


def ok(x1, y1, x2, y2, renk=SOLUK, kalin=2):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    bx, by = x2 - 7 * ux, y2 - 7 * uy
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{renk}" stroke-width="{kalin}"/>'
            f'<path d="M{bx + 5 * px:.1f} {by + 5 * py:.1f} L{x2:.1f} {y2:.1f} L{bx - 5 * px:.1f} {by - 5 * py:.1f} Z" fill="{renk}"/>')


def ip(d, renk=KAHVE, kalin=4):
    """Örgü ip: kalın kahverengi yol + üstünde açık renk kısa çizgiler."""
    return (f'<path d="{d}" fill="none" stroke="{renk}" stroke-width="{kalin}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#e4c08a" stroke-width="{kalin * 0.35:.1f}" stroke-dasharray="3 4" stroke-linecap="round"/>')


def oyunlar():
    """Beş ip oyununun simge kartları (eşleştirme sorusu)."""
    adlar = [['Halat', 'çekme'], ['İp', 'çevirme'], ['Bayrak', 'koşusu'], ['Lazer', 'oyunu'], ['Kedi', 'beşiği']]
    renkler = [(MAVI, MAVI_A), (TUR, TUR_A), (YES, YES_A), (MOR, MOR_A), (CAM, CAM_A)]
    ic = ''
    for i, x in enumerate([2, 74, 146, 218, 290]):
        r, z = renkler[i]
        cx = x + 34
        ic += kutu(x, 2, 68, 96, z, r, 8, 1.3)
        if i == 0:  # halat: kalın ip, ortada kırmızı kurdele, altında sınır çizgisi
            ic += ip(f'M{cx - 28} 34 H{cx + 28}', KAHVE, 6) + f'<rect x="{cx - 4}" y="27" width="8" height="14" rx="1.5" fill="{KIR}"/>'
            ic += f'<line x1="{cx}" y1="46" x2="{cx}" y2="58" stroke="{KIR}" stroke-width="1.6" stroke-dasharray="3 2"/>'
        elif i == 1:  # ip çevirme: dairesel iz ve ortadaki ip ucu
            ic += f'<circle cx="{cx}" cy="40" r="22" fill="none" stroke="{TUR}" stroke-width="1.2" stroke-dasharray="4 3"/>'
            ic += ip(f'M{cx} 40 L{cx + 18} 27', KAHVE, 3) + f'<circle cx="{cx}" cy="40" r="3.5" fill="{TUR}"/>'
            ic += f'<path d="M{cx + 20} 22 l5 4 l-6 3" fill="none" stroke="{TUR}" stroke-width="1.4"/>'
        elif i == 2:  # bayrak koşusu: atlama ipi ve bayrak
            ic += ip(f'M{cx - 24} 46 Q{cx - 10} 22 {cx + 4} 46', KAHVE, 3)
            ic += f'<rect x="{cx - 27}" y="44" width="5" height="12" rx="1.5" fill="{YES}"/><rect x="{cx + 2}" y="44" width="5" height="12" rx="1.5" fill="{YES}"/>'
            ic += f'<line x1="{cx + 20}" y1="22" x2="{cx + 20}" y2="58" stroke="{LAC}" stroke-width="1.6"/><path d="M{cx + 21} 23 h14 l-4 6 l4 6 h-14 z" fill="{KIR}"/>'
        elif i == 3:  # lazer: iki ağaç gövdesi arasında çapraz ipler, hedef
            for gx in (cx - 26, cx + 22):
                ic += f'<rect x="{gx}" y="18" width="6" height="42" rx="2" fill="{KAHVE}"/>'
            ic += ip(f'M{cx - 20} 24 L{cx + 22} 44', '#c9a24a', 2) + ip(f'M{cx - 20} 48 L{cx + 22} 28', '#c9a24a', 2) + ip(f'M{cx - 20} 38 L{cx + 22} 56', '#c9a24a', 2)
            ic += f'<circle cx="{cx + 30}" cy="12" r="6" fill="#fff" stroke="{KIR}" stroke-width="1.5"/><circle cx="{cx + 30}" cy="12" r="2" fill="{KIR}"/>'
        else:  # kedi beşiği: uçları bağlı ipin baklava biçimi
            d = f'M{cx - 26} 40 L{cx - 10} 24 L{cx + 10} 56 L{cx + 26} 40 L{cx + 10} 24 L{cx - 10} 56 Z'
            ic += ip(d, '#b23a6e', 2.5)
        ic += yazi(cx, 76, adlar[i][0], 12, LAC) + yazi(cx, 90, adlar[i][1], 12, LAC)
    return svg(362, 100, ic, 'Beş ip oyununun simgeleri: Halat çekme, ortasında kurdele olan kalın halat ve sınır çizgisi. İp çevirme, dairesel iz çizen ip. Bayrak koşusu, atlama ipi ve bayrak. Lazer oyunu, iki ağaç arasına çapraz bağlanmış ipler ve hedef. Kedi beşiği, uçları bağlı ipin baklava biçimi.', 26)


def halat_alani():
    """Halat çekme alanı: üstten görünüm, sınır çizgisi, iki takım alanı, çekme yönleri (insan yok)."""
    ic = kutu(6, 6, 348, 96, YES_A, YES, 6, 1.4)
    ic += f'<rect x="6" y="6" width="174" height="96" rx="6" fill="{MAVI_A}" opacity=".55"/><rect x="180" y="6" width="174" height="96" rx="6" fill="{TUR_A}" opacity=".7"/>'
    ic += f'<line x1="180" y1="6" x2="180" y2="102" stroke="{KIR}" stroke-width="2.2" stroke-dasharray="6 4"/>'
    ic += ip('M34 56 H326', KAHVE, 7) + f'<rect x="175" y="47" width="10" height="18" rx="2" fill="{KIR}"/>'
    ic += yazi(92, 26, 'A takımının alanı', 13, MAVI) + yazi(268, 26, 'B takımının alanı', 13, TUR)
    ic += ok(150, 82, 40, 82, MAVI, 2.2) + ok(210, 82, 320, 82, TUR, 2.2)
    ic += yazi(95, 98, 'çekme yönü', 11.5, MAVI) + yazi(265, 98, 'çekme yönü', 11.5, TUR)
    ic += f'<rect x="132" y="2" width="96" height="16" rx="8" fill="{KIR}"/>' + yazi(180, 13.5, 'sınır çizgisi', 11.5, '#fff')
    return svg(360, 106, ic, 'Üstten görünen oyun alanı: ortada kırmızı kesik sınır çizgisi, çizginin üstünde kurdeleli kalın halat; solda A takımının alanı, sağda B takımının alanı; oklar iki yana çekme yönünü gösteriyor.', 27)


def duyuru_karti():
    """İp atlama şenliği duyuru kartı; I, II, III numaralı noktalar."""
    ic = kutu(6, 4, 348, 118, TUR_A, TUR, 10, 1.8)
    ic += f'<rect x="6" y="4" width="348" height="28" rx="10" fill="{TUR}"/><rect x="6" y="22" width="348" height="10" fill="{TUR}"/>'
    ic += yazi(180, 24, 'İP ATLAMA ŞENLİĞİ', 15, '#fff')
    satirlar = [('Başlangıç:', ['10', '45'], 'I', 56), ('Katılım:', ['1', '250 öğrenci'], 'II', 84), ('Bilgi:', ['www', 'meb', 'gov', 'tr'], 'III', 112)]
    # Noto Sans Bold 13.5 ile ölçülmüş genişlikler (PIL, 17.10.2026); nokta kırmızı daire olarak çizilir, numara satır sonunda.
    gen = {'10': 15.4, '45': 15.4, '1': 7.7, '250 öğrenci': 77.6, 'www': 34.8, 'meb': 29.8, 'gov': 24.7, 'tr': 11.9}
    for etiket, parcalar, rom, y in satirlar:
        ic += yazi(22, y, etiket, 13, SOLUK, 'start')
        x = 112
        for k, p in enumerate(parcalar):
            ic += yazi(x, y, p, 13.5, LAC, 'start')
            x += gen[p]
            if k < len(parcalar) - 1:
                ic += f'<circle cx="{x + 3:.1f}" cy="{y - 1.8}" r="2.8" fill="{KIR}"/>'
                x += 6.5
        ic += f'<rect x="{x + 10:.1f}" y="{y - 12}" width="{14 + 6 * len(rom)}" height="15" rx="4" fill="{KIR}"/>' + yazi(x + 17 + 3 * len(rom), y - 1, rom, 10.5, '#fff')
    return svg(360, 126, ic, 'Duyuru kartı: İp Atlama Şenliği. Başlangıç: 10.45, kırmızı nokta, satır sonunda I. Katılım: 1.250 öğrenci, kırmızı nokta, satır sonunda II. Bilgi: www.meb.gov.tr, kırmızı noktalar, satır sonunda III.', 32)


def defter():
    """Defter sayfası: satır sonunda bölünmüş üç kelime (bah-çe, kurd-ele yanlış, ip-lik)."""
    # Satır genişlikleri Noto Sans 13 ile ölçüldü (PIL, 17.10.2026); numara kısa çizginin hemen sağında.
    satir = [('Dün teneffüste arkadaşlarımla bah-', 1, 216.3), ('çede ip atladık. İpin ucuna kurd-', 2, 195.8), ('ele bağladık. Oyun bitince ip-', 3, 176.9), ('liği sepete koyduk.', 0, 113.8)]
    ic = kutu(4, 4, 352, 112, KUM, GRI, 6, 1.2) + f'<line x1="30" y1="4" x2="30" y2="116" stroke="{KIR}" stroke-width="1" opacity=".6"/>'
    ic += ''.join(f'<circle cx="16" cy="{y}" r="3" fill="{GRI_A}" stroke="{GRI}" stroke-width=".8"/>' for y in (30, 60, 90))
    for i, (s, n, gen) in enumerate(satir):
        y = 32 + i * 24
        ic += f'<line x1="34" y1="{y + 6}" x2="350" y2="{y + 6}" stroke="{MAVI_A}" stroke-width="1"/>'
        ic += duz(40, y, [s], 13, LAC, 'start')
        if n:
            ic += numara(40 + gen + 13, y - 4.5, n, KIR, 8)
    return svg(360, 120, ic, 'Defter sayfası, dört satır: Dün teneffüste arkadaşlarımla bah- (1) / çede ip atladık. İpin ucuna kurd- (2) / ele bağladık. Oyun bitince ip- (3) / liği sepete koyduk.', 34)


def eposta():
    """Arda'nın e-postası: Kimden, Kime, Konu dolu; selam var; kapanış ve imza yok."""
    ic = kutu(4, 4, 352, 164, '#fff', GRI, 8, 1.3) + f'<rect x="4" y="4" width="352" height="20" rx="8" fill="{GRI_A}"/><rect x="4" y="16" width="352" height="8" fill="{GRI_A}"/>'
    ic += ''.join(f'<circle cx="{x}" cy="14" r="3.2" fill="{c}"/>' for x, c in [(16, KIR), (27, ALTIN), (38, YES)])
    ic += yazi(180, 18.5, 'Yeni ileti', 11.5, SOLUK)
    for k, (etiket, deger) in enumerate([('Kimden:', 'arda@eposta.com'), ('Kime:', 'selin@eposta.com'), ('Konu:', 'Kedi beşiği kuralları')]):
        y = 42 + k * 18
        ic += f'<rect x="14" y="{y - 12}" width="52" height="15" rx="4" fill="{MAVI_A}"/>' + yazi(40, y - 1, etiket, 11.5, MAVI)
        ic += yazi(74, y, deger, 12.5, LAC, 'start')
        ic += f'<line x1="14" y1="{y + 5}" x2="346" y2="{y + 5}" stroke="{GRI_A}" stroke-width="1"/>'
    ic += duz(16, 106, ['Merhaba Selin,', 'Geçen hafta oynadığımız kedi beşiği oyununun kurallarını', 'bana yazar mısın? Hafta sonu kuzenime öğretmek istiyorum.'], 12.5, LAC, 'start', 16)
    ic += f'<rect x="286" y="146" width="60" height="16" rx="8" fill="{MAVI}"/>' + yazi(316, 157.5, 'Gönder', 11.5, '#fff')
    return svg(360, 172, ic, 'E-posta penceresi. Kimden: arda@eposta.com. Kime: selin@eposta.com. Konu: Kedi beşiği kuralları. İleti: Merhaba Selin, Geçen hafta oynadığımız kedi beşiği oyununun kurallarını bana yazar mısın? Hafta sonu kuzenime öğretmek istiyorum. İleti burada bitiyor; kapanış ve imza yok. Gönder düğmesi.', 44)


def gunluk():
    """Efe'nin günlüğü: tarih ve uzun cümle."""
    ic = kutu(14, 4, 342, 78, KUM, GRI, 6, 1.2)
    ic += ''.join(f'<rect x="4" y="{y}" width="18" height="6" rx="3" fill="{GRI}"/>' for y in (14, 36, 58))
    ic += yazi(30, 22, '8 Ekim, Perşembe', 12, MOR, 'start') + f'<line x1="30" y1="27" x2="340" y2="27" stroke="{MOR}" stroke-width="1" opacity=".5"/>'
    ic += duz(30, 44, ['Teneffüs zili çalınca ipimizi alıp bahçeye çıktık, gölgeli', 'köşede iki takıma ayrıldık ve halat çekmeye başladık.'], 12.5, LAC, 'start', 17)
    return svg(360, 86, ic, 'Günlük sayfası, 8 Ekim Perşembe: Teneffüs zili çalınca ipimizi alıp bahçeye çıktık, gölgeli köşede iki takıma ayrıldık ve halat çekmeye başladık.', 22)


def kelime_grafik():
    """Lazer oyunu metnindeki kelimelerin geçme sayısı (sütun grafiği)."""
    veri = [('ip', 7, MAVI), ('ağaç', 4, YES), ('hedef', 3, TUR), ('öğle', 1, GRI), ('rüzgâr', 1, GRI)]
    ic = yazi(180, 14, 'Lazer oyunu metninde kelimelerin geçme sayısı', 12.5, LAC)
    tx, ty, h = 44, 100, 70
    ic += f'<line x1="{tx}" y1="{ty - h - 4}" x2="{tx}" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/><line x1="{tx}" y1="{ty}" x2="344" y2="{ty}" stroke="{SOLUK}" stroke-width="1.2"/>'
    for v in (0, 2, 4, 6):
        y = ty - v * h / 7
        ic += f'<line x1="{tx - 3}" y1="{y:.1f}" x2="344" y2="{y:.1f}" stroke="{GRI_A}" stroke-width="1"/>' + yazi(tx - 7, y + 4, str(v), 11.5, SOLUK, 'end')
    for i, (k, n, renk) in enumerate(veri):
        x = tx + 18 + i * 60
        yuk = n * h / 7
        ic += f'<rect x="{x}" y="{ty - yuk:.1f}" width="34" height="{yuk:.1f}" rx="3" fill="{renk}"/>'
        ic += yazi(x + 17, ty - yuk - 4, str(n), 12, LAC) + yazi(x + 17, ty + 15, k, 13, LAC)
    return svg(360, 122, ic, 'Sütun grafiği, lazer oyunu metninde kelimelerin geçme sayısı: ip 7, ağaç 4, hedef 3, öğle 1, rüzgâr 1.', 30)


def degerlendirme():
    """Öğretmenin konuşma değerlendirme kartı: üç ölçüt tamam, iki ölçüt geliştirilecek."""
    satirlar = [('Göz teması', True, 'farklı arkadaşlarına baktı'), ('El ve kol hareketleri', True, 'anlatımı destekledi'), ('Olayların sırası', True, 'akışa uygundu'),
                ('Yüz ifadesi', False, 'duyguları yansıtmadı'), ('Konuşmayı bitirme', False, 'sonucu söylemedi')]
    ic = kutu(4, 4, 352, 132, '#fff', LAC, 8, 1.4) + f'<rect x="4" y="4" width="352" height="24" rx="8" fill="{LAC}"/><rect x="4" y="18" width="352" height="10" fill="{LAC}"/>'
    ic += yazi(180, 21, 'KONUŞMA DEĞERLENDİRME KARTI', 12.5, '#fff')
    for i, (olcut, tamam, notu) in enumerate(satirlar):
        y = 48 + i * 20.5
        renk, z = (YES, YES_A) if tamam else (KIR, KIR_A)
        ic += f'<rect x="12" y="{y - 13}" width="18" height="18" rx="4" fill="{z}" stroke="{renk}" stroke-width="1.3"/>'
        ic += (f'<path d="M16 {y - 4} l4 4 l7 -9" fill="none" stroke="{renk}" stroke-width="2.2" stroke-linecap="round"/>' if tamam
               else f'<path d="M16 {y - 9} l10 10 M26 {y - 9} l-10 10" stroke="{renk}" stroke-width="2.2" stroke-linecap="round"/>')
        ic += yazi(38, y, olcut, 13, LAC, 'start') + duz(190, y, [notu], 12, SOLUK, 'start')
    return svg(360, 140, ic, 'Konuşma değerlendirme kartı. Göz teması: tamam, farklı arkadaşlarına baktı. El ve kol hareketleri: tamam, anlatımı destekledi. Olayların sırası: tamam, akışa uygundu. Yüz ifadesi: eksik, duyguları yansıtmadı. Konuşmayı bitirme: eksik, sonucu söylemedi.', 38)


def uygula(o):
    s = o['sorular']
    s[0]['gorsel'] = oyunlar()
    s[1]['gorsel'] = halat_alani()
    s[4]['gorsel'] = duyuru_karti()
    s[5]['gorsel'] = defter()
    s[7]['gorsel'] = eposta()
    s[8]['gorsel'] = gunluk()
    s[9]['gorsel'] = kelime_grafik()
    s[11]['gorsel'] = degerlendirme()
